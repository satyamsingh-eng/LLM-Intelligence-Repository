# Arvocap Client Wealth Statement — Dynamic Output Format & Real-Time Run Cost Analysis

**Target Output**: Dynamic 5-Page Client Wealth Statement PDF & Real-Time Token Telemetry Payload  
**Branding Palette**: Arvocap Gold (`#C5922B`), Dark Slate (`#1A1D20`), Clean Off-White (`#FBFBFD`), Electric Blue Accent (`#0066FF`)  
**Input Repository**: Google Drive Folder ID / URL (`input_data_source` — acts as core data & CRM repository)  
**Output Channel**: Primary Email PDF Attachment (`recipient_email`) via Gmail / Amazon SES  
**Cost Measurement**: Calculated dynamically per run by KARAX platform telemetry (`real_run_cost_usd`)

---

## 1. Product Input Parameters & Execution Telemetry

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      WORKFLOW RUNTIME INPUT PARAMETERS                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ • input_data_source: Google Drive Folder ID (e.g., 1vYrkqdf3ZKo815...)     │
│ • recipient_email:    Target Email Address for PDF attachment               │
│ • flex_id_filter:     Client Flex ID Filter (e.g., FLX-984210-KE)           │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       KARAX RUNTIME TELEMETRY HUD                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ Step 1A (Gemini Drive OCR): Measured Input/Output Tokens & Cost USD         │
│ Step 1B (DeepSeek Drive CRM): Measured Input/Output Tokens & Cost USD       │
│ Step 2 (Kimi K3 Reasoning): Measured Input/Output Tokens & Cost USD        │
│ Step 3 (Python Code Math):  Zero AI Token Cost ($0.00)                       │
│ Step 4 (Email Dispatch):    Gmail / Amazon SES Attachment Status           │
├─────────────────────────────────────────────────────────────────────────────┤
│ Single-Run Total Cost:      real_run_cost_usd                              │
│ Projected 10k Monthly Cost: real_run_cost_usd × 10,000                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Dynamic Output Specification Payload (`statement_output.json`)

```json
{
  "report_reference": "{{generated_report_ref}}",
  "flex_id": "{{input.flex_id}}",
  "client_name": "{{input.first_name}} {{input.last_name}}",
  "account_type": "{{input.account_type}}",
  "period": "{{reporting_period}}",
  "total_aum_kes": "{{calculated_aum_kes}}",
  "total_aum_usd": "{{calculated_aum_usd}}",
  "gross_monthly_interest_kes": "{{calculated_gross_interest}}",
  "kra_withholding_tax_kes": "{{calculated_kra_tax}}",
  "net_monthly_payout_kes": "{{calculated_net_payout}}",
  "effective_net_yield_pa": "{{calculated_net_yield_rate}}",
  "rebalancing_recommendation": {
    "proposal": "{{kimi_k3_rebalancing_proposal}}",
    "annual_tax_savings_kes": "{{calculated_tax_savings}}"
  },
  "runtime_cost_telemetry": {
    "executed_input_tokens": "{{telemetry.total_input_tokens}}",
    "executed_output_tokens": "{{telemetry.total_output_tokens}}",
    "prompt_cache_hits": "{{telemetry.cache_hit_tokens}}",
    "real_run_cost_usd": "{{telemetry.single_run_cost_usd}}",
    "projected_10k_monthly_cost_usd": "{{telemetry.projected_10k_cost_usd}}"
  },
  "delivery_status": {
    "email_sent": "{{dispatch.email_status}}",
    "recipient_email": "{{input.recipient_email}}",
    "pdf_attachment": "Arvocap_Wealth_Statement_{{input.flex_id}}.pdf",
    "advisor_approved": "{{dispatch.advisor_signoff_status}}",
    "advisor_name": "{{input.advisor_name}}"
  }
}
```

---

## 3. Email Notification Template with PDF Attachment

```text
Subject: Arvocap Asset Managers — Monthly Wealth Statement (Ref: {{report_reference}})

Dear {{client_name}},

Please find attached your official 5-page Monthly Wealth Statement for {{reporting_period}} covering account Flex ID: {{flex_id}}.

📊 PORTFOLIO HIGHLIGHTS:
• Account Name: {{entity_name}}
• Arvocap Flex ID: {{flex_id}}
• Total Portfolio AUM: KSh {{total_aum_kes}}
• Net Monthly Yield Accrued: KSh {{net_monthly_payout_kes}} (+1.02% Net M-o-M)
• Annualized Net Yield: {{effective_net_yield_pa}}

💡 ADVISOR RECOMMENDATION ({{advisor_name}}):
{{rebalancing_recommendation_summary}}

The attached 5-page PDF statement contains your itemized KRA Withholding Tax audit ledger, sub-fund holdings breakdown, and macroeconomic market commentary.

Warm regards,

Arvocap Wealth Management Team
Arvocap Asset Managers Ltd · Headquarters: Nairobi, Kenya
Tel: +254 709 002600 · Web: www.arvocap.com
```

---

## 4. Desktop Specification File Paths

* **Master Workflow Spec**: `/Users/satyyy/Desktop/ARVOCAP_WORKFLOW_SPEC.md`
* **Output & Cost Spec**: `/Users/satyyy/Desktop/ARVOCAP_OUTPUT_FORMAT_SPEC.md`
