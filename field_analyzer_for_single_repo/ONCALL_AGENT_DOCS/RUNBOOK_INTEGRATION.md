# DAG Runbook Integration - Fetch from Confluence via cURL

## 🎯 Overview

When analyzing DAG failures, the AI assistant automatically fetches runbook data from Confluence using credentials stored in `.env` file. All owner information, troubleshooting steps, and contacts are fetched dynamically from live Confluence pages.

---

## ✅ Setup Complete!

**Credentials are already configured in:**
```
/Users/chaitanya.makashir/cursor_all_repos/zdp_oncall_assistant/.env
```

The AI will automatically use these credentials when you report a DAG failure.

---

## 📋 .env File Format

The `.env` file contains:
```bash
# Confluence API Configuration for Runbook Integration
CONFLUENCE_URL=https://zendesk.atlassian.net
CONFLUENCE_USERNAME=your-email@zendesk.com
CONFLUENCE_API_TOKEN=your-api-token
```

**Location:** `/Users/chaitanya.makashir/cursor_all_repos/zdp_oncall_assistant/.env`

---

## 🚀 How to Use

Just tell the AI about a DAG failure, and it will automatically:

1. **Find the DAG file** in repository
2. **Extract Confluence runbook URL** from DAG docstring
3. **Load credentials** from `.env` file
4. **Run curl command** to fetch runbook data
5. **Parse and extract** owners, contacts, troubleshooting steps
6. **Combine with dependency analysis** from `DAG_DEPENDENCY_MASTER_REFERENCE.md`
7. **Generate complete report** with copy-paste ready Slack message

---

## 💡 Example Usage

### Just say:
```
DAG name: zdp_dbt_sales_productivity_attainment failed
```

### AI will automatically:
```bash
# Step 1: Find DAG file
find /Users/chaitanya.makashir/cursor_all_repos -name "zdp_dbt_sales_productivity_attainment.py"

# Step 2: Extract runbook URL
grep -o 'https://zendesk.atlassian.net/wiki/[^)]*' <dag_file>

# Step 3: Load credentials and fetch runbook
cd /Users/chaitanya.makashir/cursor_all_repos/zdp_oncall_assistant
source .env
curl -s -u "${CONFLUENCE_USERNAME}:${CONFLUENCE_API_TOKEN}" \
  "https://zendesk.atlassian.net/wiki/rest/api/content/${PAGE_ID}?expand=body.storage,version,space"

# Step 4: Parse JSON and extract information
# Step 5: Generate complete report
```

---

## 📊 What Gets Extracted from Confluence

**Automatically fetched from runbook:**
- ✅ Business Owner
- ✅ Technical Owners
- ✅ Slack Channel name and URL
- ✅ Troubleshooting steps
- ✅ Past incidents and resolutions
- ✅ Common issues and fixes
- ✅ Contact information
- ✅ Related documentation links

**Combined with dependency map:**
- ✅ Severity level (CATASTROPHIC/HIGH/MEDIUM/LOW)
- ✅ Downstream impact (number of affected DAGs)
- ✅ Impact type (BLOCKED vs STALE DATA)
- ✅ Dependency chain visualization

---

## 🔧 Manual cURL Command (Optional)

If you want to fetch runbook manually:

```bash
# Navigate to directory
cd /Users/chaitanya.makashir/cursor_all_repos/zdp_oncall_assistant

# Load credentials
source .env

# Fetch runbook for a specific page ID
PAGE_ID="7433683170"  # Example: uptempo runbook
curl -s -u "${CONFLUENCE_USERNAME}:${CONFLUENCE_API_TOKEN}" \
  -H "Accept: application/json" \
  "https://zendesk.atlassian.net/wiki/rest/api/content/${PAGE_ID}?expand=body.storage,version,space,metadata.labels" \
  | jq '.'
```

---

## 🔒 Security

- ✅ Credentials stored in `.env` file (gitignored)
- ✅ Never committed to version control
- ✅ File permissions restricted to owner only
- ✅ API token can be rotated anytime

**To update credentials:**
```bash
nano /Users/chaitanya.makashir/cursor_all_repos/zdp_oncall_assistant/.env
```

---

## 📂 File Structure

```
cursor_all_repos/
├── RUNBOOK_INTEGRATION.md                    # This file
├── DAG_DEPENDENCY_MASTER_REFERENCE.md        # Dependency map
└── zdp_oncall_assistant/
    └── .env                                  # ✅ Your Confluence credentials
```

---

## ✨ Real Example - Tested Successfully

```bash
$ AI analyzes: "DAG name: dbt_scd2_fivetran_uptempo"

✓ Found DAG file
✓ Extracted URL: https://zendesk.atlassian.net/wiki/spaces/EDATA/pages/7433683170/
✓ Loaded credentials from .env
✓ Fetched runbook data via curl
✓ Parsed JSON response
✓ Extracted owners and contacts

Result:
- Title: To be removed: Uptempo
- Owner: EDA Team
- Slack: #zendesk-uptempo-integration
- Schedule: Daily at 2:00 AM UTC
- Last Updated: Nov 03, 2025 by Rutwik More
- Troubleshooting steps: [Complete list from runbook]
- Common errors: [Full table from runbook]
```

---

## 🎯 Complete Workflow

```
User: "DAG zdp_dbt_sales_productivity_attainment failed"
    ↓
AI finds: /zdp_dbt_customer/dags/zdp_dbt_sales_productivity_attainment.py
    ↓
AI extracts: https://zendesk.atlassian.net/wiki/x/4QuUwAE
    ↓
AI loads: zdp_oncall_assistant/.env credentials
    ↓
AI runs: curl -u username:token <confluence_api_url>
    ↓
AI parses: JSON response for owners/contacts/troubleshooting
    ↓
AI checks: DAG_DEPENDENCY_MASTER_REFERENCE.md for impact
    ↓
AI generates: Complete incident report with:
    ✓ Real owner names from runbook
    ✓ Slack channel from runbook
    ✓ Troubleshooting steps from runbook
    ✓ Downstream impact from dependency map
    ✓ Copy-paste ready message with @mentions
```

---

## 📋 DAGs with Runbooks (Auto-fetched)

✅ **Customer Domain:**
- zdp_dbt_customer_foundational
- zdp_dbt_customer_full_refresh
- zdp_dbt_sales_productivity_attainment

✅ **Finance Domain:**
- zdp_dbt_finance_foundational
- zdp_dbt_finance_functional
- zdp_dbt_finance_*

✅ **SCD2 Fivetran:**
- dbt_scd2_fivetran_salesforce_*
- dbt_scd2_fivetran_uptempo
- dbt_scd2_fivetran_xactly
- dbt_scd2_fivetran_zuora
- dbt_scd2_fivetran_*

✅ **Data Delivery Service:**
- zdp_dbt_dds_*

*All runbook data fetched automatically from Confluence!*

---

**Last Updated:** December 3, 2025  
**Maintained By:** EDA Team  
**Status:** ✅ READY TO USE
