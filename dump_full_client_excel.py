import zipfile
import xml.etree.ElementTree as ET

path = 'downloaded_client_sheet.xlsx'

with zipfile.ZipFile(path, 'r') as z:
    # 1. Print Sheet Names from workbook.xml
    wb_tree = ET.fromstring(z.read('xl/workbook.xml'))
    sheets = wb_tree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet')
    for s in sheets:
        print(f"Sheet Name: {s.attrib.get('name')}, Sheet ID: {s.attrib.get('sheetId')}, r:id: {s.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')}")

    # 2. Shared strings
    shared_strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
        for elem in tree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'):
            shared_strings.append(elem.text or '')

    # 3. Print actual cell data for each sheet
    for s in sheets:
        s_name = s.attrib.get('name')
        s_id = s.attrib.get('sheetId')
        s_file = f"xl/worksheets/sheet{s_id}.xml"
        if s_file in z.namelist():
            print(f"\n=================== TAB: {s_name} ({s_file}) ===================")
            tree = ET.fromstring(z.read(s_file))
            rows = tree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row')
            for r_idx, row in enumerate(rows[:10]):
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
                    print(f"Row {r_idx+1}: " + " | ".join(row_vals))
