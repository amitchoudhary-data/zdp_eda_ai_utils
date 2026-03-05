# Quick Reference Guide 🚀

## Two Modes Available

### 1. **Read-Only Mode** (Recommended) 🔒
**File:** `atlassian_readonly.py`
- ✅ Only GET operations
- ✅ Cannot modify data
- ✅ Audit logging
- ✅ Safe for production

### 2. **Full Access Mode** ⚠️
**File:** `atlassian_config.py`
- ✅ GET operations
- ⚠️ Can create/update/delete
- ⚠️ Higher risk

## Installation (Required)

```bash
# Option 1: System-wide (requires admin)
pip3 install --break-system-packages requests python-dotenv

# Option 2: Virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install requests python-dotenv
```

## Quick Start Commands

### Read-Only Mode Commands

```bash
# Test connection
python3 atlassian_readonly.py --test

# Get a specific issue
python3 atlassian_readonly.py --get-issue "DATA-123"

# Search for issues
python3 atlassian_readonly.py --search-jira "project = DATA AND status = 'In Progress'"

# Get project info
python3 atlassian_readonly.py --get-project "DATA"

# Get Confluence page
python3 atlassian_readonly.py --get-page "123456789"

# Search Confluence
python3 atlassian_readonly.py --search-confluence "title ~ 'SFDC' AND space = TECH"
```

### Field Analysis with Claude CLI

```bash
# Run field analysis
python3 simple_field_analyzer.py \
  --fields="subscription_model_type,is_price_ramp" \
  --claude-cli

# Generate prompt only (no Claude CLI)
python3 simple_field_analyzer.py \
  --fields="subscription_model_type,is_price_ramp"
```

## Python Code Examples

### Read Jira Issues

```python
from atlassian_readonly import ReadOnlyAtlassianConfig, ReadOnlyJiraClient

config = ReadOnlyAtlassianConfig()
jira = ReadOnlyJiraClient(config)

# Get issue
issue = jira.get_issue("DATA-123")
print(issue['fields']['summary'])

# Search issues
issues = jira.search_issues("project = DATA")
for issue in issues:
    print(f"{issue['key']}: {issue['fields']['summary']}")
```

### Read Confluence Pages

```python
from atlassian_readonly import ReadOnlyAtlassianConfig, ReadOnlyConfluenceClient

config = ReadOnlyAtlassianConfig()
confluence = ReadOnlyConfluenceClient(config)

# Get page
page = confluence.get_page("123456", expand=['body.storage'])
print(page['title'])

# Search
results = confluence.search_content("text ~ 'SFDC'")
for result in results:
    print(result['title'])
```

## Files Overview

| File | Purpose |
|------|---------|
| `atlassian_readonly.py` | 🔒 Read-only API client |
| `atlassian_config.py` | ⚠️ Full-access API client |
| `simple_field_analyzer.py` | Field analysis tool |
| `.env` | **Your credentials (NEVER commit!)** |
| `env_template.txt` | Template for `.env` |
| `README_READONLY.md` | Full read-only documentation |
| `ATLASSIAN_SETUP.md` | Full setup guide |

## Security Checklist

- [ ] Create `.env` file with your credentials
- [ ] Verify `.env` is in `.gitignore`
- [ ] Use read-only mode (`atlassian_readonly.py`)
- [ ] Create read-only service account (optional but recommended)
- [ ] Test connection: `python3 atlassian_readonly.py --test`
- [ ] Review audit logs regularly

## Common Use Cases

### 1. Check if field analysis ticket exists

```bash
python3 atlassian_readonly.py --search-jira \
  "project = DATA AND text ~ 'subscription_model_type'"
```

### 2. Get all comments on a ticket

```python
jira = ReadOnlyJiraClient(config)
comments = jira.get_issue_comments("DATA-123")
for comment in comments:
    print(f"{comment['author']['displayName']}: {comment['body']}")
```

### 3. Find documentation pages

```bash
python3 atlassian_readonly.py --search-confluence \
  "title ~ 'Field Analysis' AND space = TECH"
```

### 4. Export issues to CSV

```python
import csv
jira = ReadOnlyJiraClient(config)
issues = jira.search_issues("project = DATA", max_results=1000)

with open('issues.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Key', 'Summary', 'Status'])
    for issue in issues:
        writer.writerow([
            issue['key'],
            issue['fields']['summary'],
            issue['fields']['status']['name']
        ])
```

## Troubleshooting

### Issue: "Missing required environment variables"

**Fix:**
```bash
# Create .env file
cp env_template.txt .env
nano .env  # Add your credentials
```

### Issue: "requests not installed"

**Fix:**
```bash
pip3 install --break-system-packages requests python-dotenv
```

### Issue: "Permission denied"

**Fix:**
- Contact Jira admin for read permissions
- Or create read-only service account

### Issue: ".env file not found"

**Fix:**
```bash
cd "/Users/amit.choudhary/Downloads/Repos EDA/zdp_eda_ai_utils/Analysis"
cp env_template.txt .env
# Edit .env with your credentials
```

## Next Steps

1. **Install dependencies** (if not done)
2. **Create/update `.env`** file
3. **Test connection**: `python3 atlassian_readonly.py --test`
4. **Try a search**: `python3 atlassian_readonly.py --search-jira "project = DATA"`
5. **Integrate with your workflows**

## Getting Help

- Read `README_READONLY.md` for detailed read-only documentation
- Read `ATLASSIAN_SETUP.md` for complete setup guide
- Check `.env` file exists and has correct values
- Verify network connectivity to Atlassian

---

**Quick Start:** `./quick_start.sh` (automated setup)  
**Mode:** Use `atlassian_readonly.py` for safety 🔒

