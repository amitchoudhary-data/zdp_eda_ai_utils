# Secure Atlassian API Integration for Cursor

Complete guide to securely connect Cursor with Atlassian services (Jira, Confluence) using API tokens.

## 🔐 Security First

This implementation ensures:
- ✅ Credentials stored in `.env` file (git-ignored)
- ✅ Never commit API tokens to git
- ✅ Environment variables for secure access
- ✅ HTTPBasicAuth for API authentication
- ✅ No hardcoded credentials in code

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Dependencies

```bash
# Install required Python packages
pip install requests python-dotenv

# Or using pip3
pip3 install requests python-dotenv
```

### Step 2: Get Your Atlassian API Token

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Give it a name (e.g., "Cursor Development")
4. Copy the token (you'll only see it once!)

### Step 3: Run Setup Wizard

```bash
cd "/Users/amit.choudhary/Downloads/Repos EDA/zdp_eda_ai_utils/Analysis"
python3 atlassian_config.py --setup
```

The wizard will ask for:
- Your Atlassian email
- Your Atlassian domain (e.g., `zendesk.atlassian.net`)
- Your API token
- Optional: Default Jira project key

### Step 4: Test Connection

```bash
python3 atlassian_config.py --test
```

You should see:
```
✅ Successfully connected to Atlassian
   Logged in as: Your Name
   Email: your.email@company.com
```

## 📁 File Structure

```
Analysis/
├── atlassian_config.py     # Secure API configuration
├── env_template.txt         # Template for .env file
├── .env                     # YOUR CREDENTIALS (git-ignored)
└── .gitignore              # Ensures .env is never committed
```

## 🔧 Manual Setup (Alternative)

If you prefer manual setup:

### 1. Create `.env` file

```bash
# Copy template
cp env_template.txt .env

# Edit with your credentials
nano .env  # or use your preferred editor
```

### 2. Fill in your credentials in `.env`:

```bash
ATLASSIAN_EMAIL=your.email@company.com
ATLASSIAN_API_TOKEN=your_actual_api_token_here
ATLASSIAN_DOMAIN=yourcompany.atlassian.net
JIRA_PROJECT_KEY=PROJ  # Optional
```

### 3. Ensure `.env` is git-ignored

```bash
# Check if .env is in .gitignore
grep -q "^\.env$" .gitignore || echo ".env" >> .gitignore
```

## 💻 Usage Examples

### Python Usage

```python
from atlassian_config import AtlassianConfig, JiraClient

# Initialize configuration (automatically loads from .env)
config = AtlassianConfig()

# Create Jira client
jira = JiraClient(config)

# Get a specific issue
issue = jira.get_issue("PROJ-123")
print(f"Issue: {issue['fields']['summary']}")

# Search for issues
issues = jira.search_issues("project = PROJ AND status = 'In Progress'")
for issue in issues:
    print(f"{issue['key']}: {issue['fields']['summary']}")

# Create a new issue
new_issue = jira.create_issue(
    project="PROJ",
    summary="SFDC Field Analysis Needed",
    description="Analyze these fields: subscription_model_type, is_price_ramp",
    issue_type="Task"
)
```

### Command Line Usage

```bash
# Test connection
python3 atlassian_config.py --test

# Get specific issue
python3 atlassian_config.py --get-issue "PROJ-123"

# Search with JQL
python3 atlassian_config.py --search "project = PROJ AND status = 'In Progress'"

# Show current configuration
python3 atlassian_config.py
```

## 🤖 Using with Cursor

Cursor can now access Atlassian APIs through this secure configuration:

### Example: Create Analysis Tasks

```python
#!/usr/bin/env python3
"""Create Jira tasks for field analysis results"""

from atlassian_config import AtlassianConfig, JiraClient

# Your analysis results
fields_to_analyze = [
    {
        "name": "subscription_model_type",
        "criticality": "CRITICAL",
        "recommendation": "KEEP current sync"
    },
    {
        "name": "is_price_ramp", 
        "criticality": "CRITICAL",
        "recommendation": "KEEP current sync"
    }
]

# Initialize
config = AtlassianConfig()
jira = JiraClient(config)

# Create tasks
for field in fields_to_analyze:
    summary = f"Review {field['name']} sync configuration"
    description = f"""
Field: {field['name']}
Criticality: {field['criticality']}
Recommendation: {field['recommendation']}

Please review the analysis and confirm sync strategy.
"""
    
    issue = jira.create_issue(
        project=config.jira_project,
        summary=summary,
        description=description,
        issue_type="Task"
    )
    
    if issue:
        print(f"✅ Created: {issue['key']}")
```

## 🔒 Security Best Practices

### ✅ DO:

- Store credentials in `.env` file
- Add `.env` to `.gitignore`
- Use environment variables
- Rotate API tokens periodically
- Use specific API token permissions
- Test connection before use

### ❌ DON'T:

- Commit `.env` to git
- Hardcode credentials in scripts
- Share API tokens in chat/email
- Use your personal token for shared scripts
- Store tokens in code comments

## 🛠️ Troubleshooting

### Issue: "Missing required environment variables"

**Solution:**
```bash
# Verify .env file exists
ls -la .env

# Check contents (safely)
cat .env | grep -v TOKEN

# Reload environment
python3 atlassian_config.py --test
```

### Issue: "Connection failed: 401"

**Causes:**
- Invalid API token
- Wrong email address
- Token permissions insufficient

**Solution:**
```bash
# Generate new API token
# https://id.atlassian.com/manage-profile/security/api-tokens

# Update .env file
nano .env

# Test again
python3 atlassian_config.py --test
```

### Issue: "Connection failed: 404"

**Causes:**
- Wrong domain name
- API endpoint doesn't exist

**Solution:**
```bash
# Verify domain in .env
# Should be: company.atlassian.net (not https://company.atlassian.net)

# Test connection
python3 atlassian_config.py --test
```

### Issue: "requests library not available"

**Solution:**
```bash
pip3 install requests python-dotenv
```

## 📚 Available API Operations

### Jira

- ✅ Get issue by key
- ✅ Search issues with JQL
- ✅ Create new issues
- ✅ Get current user info
- 🔜 Update issues (add if needed)
- 🔜 Add comments (add if needed)
- 🔜 Transition issues (add if needed)

### Confluence

- 🔜 Get page content
- 🔜 Create pages
- 🔜 Search content

## 🔗 Useful Links

- [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
- [Jira REST API Docs](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Confluence REST API Docs](https://developer.atlassian.com/cloud/confluence/rest/v1/intro/)
- [JQL (Jira Query Language)](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)

## 📝 Example Workflows

### Workflow 1: Analysis Results → Jira Tasks

```python
# After field analysis
from atlassian_config import JiraClient, AtlassianConfig

config = AtlassianConfig()
jira = JiraClient(config)

# Create tasks for high-priority fields
for field in critical_fields:
    jira.create_issue(
        project="DATA",
        summary=f"Review {field} sync strategy",
        description=analysis_results[field],
        issue_type="Task"
    )
```

### Workflow 2: Track Analysis Progress

```python
# Search for analysis-related tickets
issues = jira.search_issues(
    "project = DATA AND labels = 'field-analysis' AND status != Done"
)

for issue in issues:
    print(f"Pending: {issue['key']} - {issue['fields']['summary']}")
```

### Workflow 3: Documentation Updates

```python
# When adding to Confluence later
from atlassian_config import AtlassianConfig

config = AtlassianConfig()
confluence_url = config.get_confluence_url("content")

# Use requests to create/update pages
# (Confluence client implementation can be added)
```

## 🎯 Next Steps

1. ✅ Complete setup wizard
2. ✅ Test connection
3. ✅ Try example commands
4. ✅ Integrate with your analysis workflows
5. 📊 Create automation scripts for common tasks

---

**Version:** 1.0  
**Last Updated:** October 2025  
**Security Level:** Production-Ready  
**Supported Services:** Jira, Confluence (API v3)

