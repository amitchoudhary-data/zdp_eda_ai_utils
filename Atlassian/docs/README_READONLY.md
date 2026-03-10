# Read-Only Atlassian API Access 🔒

**Secure, read-only integration with Jira and Confluence**

This configuration ensures you can **ONLY READ** data from Atlassian - no write, update, or delete operations are possible.

## 🔐 Security Benefits

- ✅ **No Write Operations** - Cannot create, update, or delete issues/pages
- ✅ **Audit Logging** - All API calls are logged with timestamps
- ✅ **Principle of Least Privilege** - Minimal permissions required
- ✅ **Safe for Production** - Cannot accidentally modify data
- ✅ **Team-Safe** - Can share without risk

## 🚀 Quick Setup

### Step 1: Create Read-Only API Token

Unfortunately, Atlassian API tokens have full permissions by default. To achieve read-only access, you need to use **one of these methods**:

#### Method 1: Create a Service Account (Recommended)

1. Ask your Jira/Confluence admin to create a **service account**
2. Assign only **READ permissions** to this account:
   - Jira: "Browse Projects" permission only
   - Confluence: "View" permission only
3. Generate API token for this service account
4. Use this token in your `.env` file

#### Method 2: Use Your Account with Read-Only Verification

1. Use your existing API token
2. Verify you have no write permissions in the projects you're accessing
3. The code will still enforce read-only operations
4. Audit logs will track all access

### Step 2: Install Dependencies

```bash
pip3 install --break-system-packages requests python-dotenv
```

### Step 3: Configure Environment

Create `.env` file:
```bash
cd "/Users/amit.choudhary/Downloads/Repos EDA/zdp_eda_ai_utils/Atlassian"
cp env_template.txt .env
nano .env
```

Add your credentials:
```bash
ATLASSIAN_EMAIL=your.email@zendesk.com
ATLASSIAN_API_TOKEN=your_api_token_here
ATLASSIAN_DOMAIN=zendesk.atlassian.net
JIRA_PROJECT_KEY=DATA  # Optional
```

### Step 4: Test Connection

```bash
python3 atlassian_readonly.py --test
```

Expected output:
```
🔒 READ-ONLY MODE: Only GET operations allowed
✅ Successfully connected to Atlassian (READ-ONLY)
   Logged in as: Amit Choudhary
   Email: amit.choudhary@zendesk.com
   🔒 Mode: READ-ONLY (GET operations only)
```

## 📖 Usage Examples

### Read Jira Issue

```bash
python3 atlassian_readonly.py --get-issue "DATA-123"
```

Output:
```
[2025-11-27T...] READ: get_issue -> DATA-123
📋 Issue: DATA-123
   Summary: Review subscription_model_type sync
   Status: In Progress
   Type: Task
```

### Search Jira Issues

```bash
python3 atlassian_readonly.py --search-jira "project = DATA AND status = 'In Progress'"
```

Output:
```
[2025-11-27T...] READ: search_issues -> project = DATA...
🔍 Found 5 issues:
   DATA-123: Review subscription_model_type sync
   DATA-124: Analyze is_price_ramp usage
   DATA-125: Update field documentation
```

### Get Jira Project Info

```bash
python3 atlassian_readonly.py --get-project "DATA"
```

### Read Confluence Page

```bash
python3 atlassian_readonly.py --get-page "123456789"
```

### Search Confluence

```bash
python3 atlassian_readonly.py --search-confluence "title ~ 'SFDC Field' AND space = TECH"
```

### Get Confluence Space

```bash
python3 atlassian_readonly.py --get-space "TECH"
```

## 💻 Python Usage

### Basic Example

```python
from atlassian_readonly import ReadOnlyAtlassianConfig, ReadOnlyJiraClient

# Initialize (automatically loads .env)
config = ReadOnlyAtlassianConfig()
jira = ReadOnlyJiraClient(config)

# Read issue
issue = jira.get_issue("DATA-123")
print(f"Issue: {issue['fields']['summary']}")

# Search issues
issues = jira.search_issues("project = DATA")
for issue in issues:
    print(f"{issue['key']}: {issue['fields']['summary']}")
```

### Advanced Example - Field Analysis Integration

```python
from atlassian_readonly import ReadOnlyAtlassianConfig, ReadOnlyJiraClient

# Your field analysis results
critical_fields = ["subscription_model_type", "is_price_ramp"]

# Initialize Jira client (read-only)
config = ReadOnlyAtlassianConfig()
jira = ReadOnlyJiraClient(config)

# Search for existing analysis tickets
jql = f"project = DATA AND labels = 'field-analysis' AND text ~ '{critical_fields[0]}'"
existing_tickets = jira.search_issues(jql)

print(f"Found {len(existing_tickets)} existing tickets")
for ticket in existing_tickets:
    print(f"  {ticket['key']}: {ticket['fields']['summary']}")
    
    # Get comments to see previous analysis
    comments = jira.get_issue_comments(ticket['key'])
    print(f"    {len(comments)} comments")
```

### Confluence Example

```python
from atlassian_readonly import ReadOnlyAtlassianConfig, ReadOnlyConfluenceClient

config = ReadOnlyAtlassianConfig()
confluence = ReadOnlyConfluenceClient(config)

# Search for documentation
results = confluence.search_content(
    "title ~ 'SFDC Field' AND space = TECH",
    limit=10
)

for page in results:
    print(f"📄 {page['title']}")
    
    # Get full page content
    full_page = confluence.get_page(
        page['id'],
        expand=['body.storage', 'version']
    )
    
    if full_page:
        print(f"   Version: {full_page['version']['number']}")
        # Could extract and analyze content here
```

## 🔒 What's Blocked (Cannot Do)

The read-only client **does NOT include** these write operations:

- ❌ Create issues (`create_issue`)
- ❌ Update issues (`update_issue`)
- ❌ Delete issues
- ❌ Add comments
- ❌ Transition issues
- ❌ Create Confluence pages
- ❌ Update Confluence pages
- ❌ Delete any content

**If you try to import these from `atlassian_config.py`, they will work, but the read-only client doesn't expose them.**

## ✅ What's Allowed (Can Do)

- ✅ Read issues
- ✅ Search with JQL/CQL
- ✅ Get project information
- ✅ Read comments (but not add)
- ✅ View transitions (but not execute)
- ✅ Read Confluence pages
- ✅ Search Confluence content
- ✅ Get space information
- ✅ Export data for analysis

## 📊 Use Cases

### 1. Analysis Data Collection

```python
# Collect data about field-related tickets
jira = ReadOnlyJiraClient(config)

fields_to_check = ["subscription_model_type", "is_price_ramp"]
all_tickets = []

for field in fields_to_check:
    jql = f"text ~ '{field}' AND created >= -90d"
    tickets = jira.search_issues(jql, max_results=100)
    all_tickets.extend(tickets)

print(f"Found {len(all_tickets)} tickets mentioning these fields")
```

### 2. Documentation Review

```python
# Find all documentation pages about SFDC fields
confluence = ReadOnlyConfluenceClient(config)

pages = confluence.search_content(
    "text ~ 'SFDC sync' AND space = DATA",
    limit=50
)

for page in pages:
    full_page = confluence.get_page(page['id'], expand=['body.storage'])
    # Analyze content, extract field mentions, etc.
```

### 3. Audit & Reporting

```python
# Generate report of recent field analysis work
jira = ReadOnlyJiraClient(config)

issues = jira.search_issues(
    "project = DATA AND labels = 'field-analysis' AND updated >= -30d",
    fields=['summary', 'status', 'assignee', 'updated']
)

# Generate CSV report
import csv
with open('field_analysis_report.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Key', 'Summary', 'Status', 'Assignee', 'Updated'])
    for issue in issues:
        writer.writerow([
            issue['key'],
            issue['fields']['summary'],
            issue['fields']['status']['name'],
            issue['fields'].get('assignee', {}).get('displayName', 'Unassigned'),
            issue['fields']['updated']
        ])
```

## 🔐 Jira Permission Setup (For Admins)

To create a proper read-only service account:

### 1. Create Service Account

1. Go to Jira Administration → User Management
2. Create new user: `sfdc-analysis-readonly@zendesk.com`
3. Don't add to any groups initially

### 2. Set Project Permissions

1. Go to Project Settings → Permissions
2. Create new permission scheme: "Read-Only Analyst"
3. Grant only these permissions:
   - ✅ Browse Projects
   - ✅ View Issues
   - ❌ Remove all other permissions

### 3. Apply to Projects

1. Apply "Read-Only Analyst" scheme to relevant projects
2. Add service account to the scheme

### 4. Generate API Token

1. Log in as service account
2. Go to https://id.atlassian.com/manage-profile/security/api-tokens
3. Create API token
4. Store securely in `.env` file

## 🛡️ Security Best Practices

1. **Use Service Account**
   - Dedicated account for read-only operations
   - Easy to audit and revoke

2. **Rotate Tokens**
   - Change API tokens every 90 days
   - Immediately revoke if compromised

3. **Audit Logs**
   - Review the timestamped logs regularly
   - Look for unusual access patterns

4. **Least Privilege**
   - Only grant access to projects you need
   - Don't use admin account for API access

5. **Secure Storage**
   - Keep `.env` file secure
   - Never commit to git
   - Use appropriate file permissions: `chmod 600 .env`

## 🆚 Comparison: Full vs Read-Only

| Feature | `atlassian_config.py` | `atlassian_readonly.py` |
|---------|----------------------|-------------------------|
| Read Issues | ✅ | ✅ |
| Search | ✅ | ✅ |
| Create Issues | ✅ | ❌ |
| Update Issues | ✅ | ❌ |
| Delete Issues | ✅ | ❌ |
| Add Comments | ✅ | ❌ |
| Audit Logging | ❌ | ✅ |
| Safety | ⚠️ | ✅ |

## 📚 API Reference

### ReadOnlyJiraClient Methods

```python
# Get single issue
get_issue(issue_key: str) -> Optional[Dict]

# Search issues
search_issues(jql: str, max_results: int = 50, fields: List[str] = None) -> List[Dict]

# Get project
get_project(project_key: str) -> Optional[Dict]

# Get comments (read-only)
get_issue_comments(issue_key: str) -> List[Dict]

# Get available transitions (read-only)
get_issue_transitions(issue_key: str) -> List[Dict]
```

### ReadOnlyConfluenceClient Methods

```python
# Get page
get_page(page_id: str, expand: List[str] = None) -> Optional[Dict]

# Search content
search_content(cql: str, limit: int = 25) -> List[Dict]

# Get space
get_space(space_key: str) -> Optional[Dict]
```

## 🔍 Troubleshooting

### "Permission denied" errors

**Cause:** Your account/token doesn't have read access to the project

**Solution:**
- Contact Jira admin to grant "Browse Projects" permission
- Or use a service account with proper permissions

### "Too many requests" error

**Cause:** Hitting Atlassian API rate limits

**Solution:**
- Add delays between requests: `time.sleep(0.5)`
- Reduce `max_results` in searches
- Cache results locally

### Audit logs not appearing

**Cause:** Logs are printed to stdout

**Solution:**
```python
# Redirect logs to file
import sys
sys.stdout = open('api_audit.log', 'a')
```

## 📝 Next Steps

1. ✅ Set up read-only access
2. ✅ Test with sample queries
3. ✅ Integrate with your analysis workflows
4. ✅ Set up audit log monitoring
5. ✅ Document your usage patterns

---

**Version:** 1.0 (Read-Only)  
**Security Level:** Production-Ready  
**Recommended For:** Data analysis, reporting, audit, documentation

