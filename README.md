# ZDP EDA AI Utils

Utilities for EDA data platform analysis and operations.

## Folder Structure

```
zdp_eda_ai_utils/
│
├── Atlassian/                  # Jira & Confluence integration
│   ├── python/                 # Python API clients & export scripts
│   ├── docs/                   # Setup guides & API reference
│   ├── output/                 # Exported Confluence content
│   ├── .env / env_template.txt # Credentials (never commit .env)
│   ├── requirements.txt        # Python dependencies
│   └── quick_start.sh          # Automated setup script
│
├── Impact_Analysis/            # DBT model impact analysis
│   └── impact_analysis.md      # Hybrid analysis template (GitHub MCP + local)
│
└── ONCALL_AGENT_DOCS/          # Oncall runbooks & DAG references
    ├── DAG_DEPENDENCY_MASTER_REFERENCE.md
    ├── ONCALL_QUICK_START_GUIDE.md
    └── RUNBOOK_INTEGRATION.md
```

## Quick Start

### Impact Analysis (Cursor + GitHub MCP)
See `Impact_Analysis/impact_analysis.md` for the step-by-step template.

### Atlassian API
```bash
cd Atlassian
pip install -r requirements.txt
cp env_template.txt .env   # add your credentials
cd python
python3 atlassian_readonly.py --test
```

### Oncall
See `ONCALL_AGENT_DOCS/ONCALL_QUICK_START_GUIDE.md`.
