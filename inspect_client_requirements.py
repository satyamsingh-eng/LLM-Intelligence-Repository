import json
import os
import sys
import base64
import io
import zipfile
import xml.etree.ElementTree as ET
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

token_file = os.path.expanduser('~/.hermes/profiles/professional/google_token.json')

with open(token_file) as f:
    tdata = json.load(f)

creds = Credentials(
    token=tdata.get('token') or tdata.get('access_token'),
    refresh_token=tdata.get('refresh_token'),
    token_uri=tdata.get('token_uri', 'https://oauth2.googleapis.com/token'),
    client_id=tdata.get('client_id'),
    client_secret=tdata.get('client_secret'),
    scopes=tdata.get('scopes')
)

drive_service = build('drive', 'v3', credentials=creds)
gmail_service = build('gmail', 'v1', credentials=creds)

file_id = '1DRCby6JCXQdar1lFrunhGouoi5VIGvrW'

print(f"--- DOWNLOADING OFFICE FILE FROM DRIVE: {file_id} ---")
file_metadata = drive_service.files().get(fileId=file_id, fields='id, name, mimeType').execute()
print(f"File Name: {file_metadata.get('name')}")
print(f"Mime Type: {file_metadata.get('mimeType')}")

request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while not done:
    status, done = downloader.next_chunk()

fh.seek(0)
local_excel_path = 'downloaded_client_sheet.xlsx'
with open(local_excel_path, 'wb') as f:
    f.write(fh.read())

print(f"✅ Saved to {local_excel_path}!")

# Parse XLSX manually with zipfile & xml
def parse_xlsx(path):
    with zipfile.ZipFile(path, 'r') as z:
        # Load shared strings
        shared_strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            for elem in tree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'):
                shared_strings.append(elem.text or '')

        # Load sheets
        sheet_files = [f for f in z.namelist() if f.startswith('xl/worksheets/sheet') and f.endswith('.xml')]
        for s_file in sorted(sheet_files):
            print(f"\n=== {s_file} ===")
            tree = ET.fromstring(z.read(s_file))
            for row in tree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                row_vals = []
                for cell in row.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                    val_elem = cell.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                    cell_type = cell.attrib.get('t')
                    cell_val = ''
                    if val_elem is not None and val_elem.text:
                        v = val_elem.text
                        if cell_type == 's' and int(v) < len(shared_strings):
                            cell_val = shared_strings[int(v)]
                        else:
                            cell_val = v
                    row_vals.append(cell_val)
                if any(row_vals):
                    print(" | ".join(row_vals))

parse_xlsx(local_excel_path)

# 2. Search Gmail for John Ngure / Arvocap / Pratyush email threads
print("\n--- SEARCHING GMAIL FOR ARVOCAP / JOHN NGURE / PRATYUSH THREADS ---")
query = 'Arvocap OR "John Ngure" OR j.ngure@arvocap.com'
results = gmail_service.users().messages().list(userId='me', q=query).execute()
messages = results.get('messages', [])

print(f"Found {len(messages)} matching email messages.")
threads_seen = set()

for m in messages:
    thread_id = m['threadId']
    if thread_id in threads_seen:
        continue
    threads_seen.add(thread_id)
    
    thread = gmail_service.users().threads().get(userId='me', id=thread_id).execute()
    print(f"\n=================== GMAIL THREAD ID: {thread_id} ===================")
    for msg in thread.get('messages', []):
        headers = {h['name']: h['value'] for h in msg['payload']['headers']}
        sender = headers.get('From')
        subject = headers.get('Subject')
        date = headers.get('Date')
        print(f"\nDate: {date}\nFrom: {sender}\nSubject: {subject}")
        
        snippet = msg.get('snippet')
        print(f"Snippet: {snippet}")
        
        parts = [msg['payload']]
        while parts:
            part = parts.pop(0)
            if part.get('parts'):
                parts.extend(part['parts'])
            if part.get('mimeType') == 'text/plain':
                data = part.get('body', {}).get('data')
                if data:
                    body_text = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
                    print("--- BODY TEXT ---")
                    print(body_text[:2500])
