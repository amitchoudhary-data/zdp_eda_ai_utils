# 🚨 ZDP On-Call Assistant - Quick Start Guide

---

## 🤖 ON-CALL SUPPORT AGENT (Recommended)

**How to Activate:**
1. Open Cursor IDE in the `cursor_all_repos` workspace
2. The `.cursorrules` file automatically activates the ON-CALL SUPPORT AGENT
3. You'll see the welcome message:
   ```
   🚨 WELCOME ONCALL ENGINEER!! 🚨
   
   DAG FAILED?? LET ME HELP JUST PROVIDE THE ERROR LOGS!!
   ```
4. **Just paste your error logs** - everything else happens automatically!

**What Happens Automatically:**
| Step | Action |
|------|--------|
| ✅ **Sync Repos** | Pulls latest from main branch on all affected repos |
| ✅ **Read Dependencies** | References DAG_DEPENDENCY_MASTER_REFERENCE.md |
| ✅ **Fetch Runbook** | Gets owner info from Confluence |
| ✅ **Analyze Impact** | Maps downstream DAGs (BLOCKED vs STALE) |
| ✅ **Generate Message** | Creates copy-paste Slack message with @owners |
| ✅ **Incident Guidance** | Advises whether to declare incident |
| ✅ **Journal Entry** | Prompts for oncall journal update |

---

## 1️⃣ Prerequisites

| Requirement | Details |
|-------------|---------|
| **Cursor IDE** | AI-powered code editor (required) |
| **Confluence API Token** | Stored in `zdp_oncall_assistant/.env` |
| **Workspace Repos** | All repos should be in same parent folder |

**Required Repositories:**
```
cursor_all_repos/
├── zdp_dbt_customer/
├── zdp_dbt_finance/
├── zdp_dbt_scd2_fivetran/
├── zdp_dbt_cleansed_salesforce/
├── zdp_dbt_cleansed_xactly/
├── zdp_dbt_data_delivery_service/
├── zdp_dbt_enterprise_data_ml/
└── zdp_oncall_assistant/
```

---

## ⚠️ Critical Rules for AI Assistant

| Rule | Description |
|------|-------------|
| **🛑 Consent for MD Changes** | NEVER commit changes to MD files without asking: "ARE YOU SURE YOU WANT TO COMMIT THESE CHANGES IN MD FILE?" |
| **🛑 Consent for Code Changes** | NO CODE CHANGES in any repository without explicit user approval |
| **🔄 Auto-Sync Repos** | ALWAYS run `git pull origin main` on affected repos BEFORE starting analysis |

**Pre-Analysis Command (runs automatically):**
```bash
cd /Users/chaitanya.makashir/cursor_all_repos/<REPO_NAME> && git checkout main && git pull origin main
```

---

## 2️⃣ Reference Files

| File | Purpose |
|------|---------|
| `DAG_DEPENDENCY_MASTER_REFERENCE.md` | Maps 89 DAGs, downstream impacts, severity levels, cascade chains |
| `RUNBOOK_INTEGRATION.md` | Confluence API setup for fetching owner info |
| `zdp_oncall_assistant/.env` | Stores Confluence credentials (CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN) |

---

## 3️⃣ How It Works

```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│  PASTE LOGS     │ →  │  AI SYNCS REPOS  │ →  │  AI ANALYZES     │ →  │  GET OUTPUT         │
│  in Cursor Chat │    │  (Auto git pull) │    │  • DAG deps      │    │  • Root cause       │
│  + add prompt:  │    │  on all affected │    │  • Git history   │    │  • Impact analysis  │
│  "refer DAG_    │    │  repositories    │    │  • Confluence    │    │  • Slack message    │
│   DEPENDENCY_   │    │                  │    │  • Code files    │    │  • Code fix         │
│   MASTER_REF.md"│    │                  │    │                  │    │  • Incident advice  │
└─────────────────┘    └──────────────────┘    └──────────────────┘    └─────────────────────┘
```

**Prompt Template:**
```
[Paste Airflow failure logs here]

refer DAG_DEPENDENCY_MASTER_REFERENCE.md file
```

---

## 4️⃣ Output

| Section | What You Get |
|---------|--------------|
| **Failure Summary** | DAG name, error, severity (🔴 CATASTROPHIC → 🟢 LOW) |
| **Root Cause** | Why it failed + git history of recent changes |
| **Downstream Impact** | # of affected DAGs, BLOCKED vs STALE DATA |
| **Slack Message** | Copy-paste ready message with @owner mentions |
| **Code Fix** | File path + proposed fix + PR draft (if applicable) |
| **Incident Guidance** | Whether to declare incident based on severity |
| **Journal Entry** | 2-3 liner summary for oncall journal |

**Sample Output:**
```
🚨 DAG: zdp_dbt_customer_financial_bookings
📊 Severity: 🟠 HIGH | Impact: 2 DAGs

📨 COPY-PASTE MESSAGE:
Hi Team, FYI, there will be a delay in loading today's data 
for fact_financial_bookings due to [ROOT_CAUSE]. 
cc- @owners
```

---

## 5️⃣ Incident & Post-Failure Steps

| Step | When | Action |
|------|------|--------|
| **🚨 Incident Check** | After analysis | AI advises if incident should be declared based on severity |
| **📋 Incident Summary** | If raising incident | AI provides brief summary for incident declaration |
| **📝 Post-Incident** | After resolution | AI asks for resolution details → creates post-incident summary |
| **📓 Oncall Journal** | After EVERY failure | AI asks which solution was used → generates 2-3 liner summary |

**Incident Declaration Guide:** [EDA Incident Guide](https://zendesk.atlassian.net/wiki/spaces/EDATA/pages/edit-v2/7349600412)

**Oncall Journal:** [Update Daily Journal](https://docs.google.com/document/d/1_SvwE7xfW5HzzoYLOfrK1uGoIndosEHeG3Dq50Q_Sbo/edit?tab=t.all1vnh5oyuy#heading=h.cm3s4ka1s9yr)

| Severity | Incident Required? |
|----------|-------------------|
| 🔴 CATASTROPHIC (10+ DAGs) | ✅ YES - MANDATORY |
| 🟠 HIGH (5-9 DAGs) | ⚠️ RECOMMENDED |
| 🟡 MEDIUM (2-4 DAGs) | ❓ OPTIONAL |
| 🟢 LOW (0-1 DAGs) | ❌ NO |

---

**Support:** `#edw-ops` | **Maintained By:** EDA Team
