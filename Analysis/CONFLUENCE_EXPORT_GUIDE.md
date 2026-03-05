# Confluence Space Export Guide 📚

Export entire Confluence spaces to markdown files using read-only API access.

## 🚀 Quick Start

### Export the ZDM Space

```bash
cd "/Users/amit.choudhary/Downloads/Repos EDA/zdp_eda_ai_utils/Analysis"

# Export with default settings
python3 confluence_space_exporter.py --space ZDM

# Export with custom filename
python3 confluence_space_exporter.py --space ZDM --output zdm_documentation.md

# Export without metadata
python3 confluence_space_exporter.py --space ZDM --no-metadata
```

## 📦 Prerequisites

### 1. Install Required Packages

```bash
# Core dependencies (required)
pip3 install --break-system-packages requests python-dotenv

# HTML to Markdown converter (highly recommended)
pip3 install --break-system-packages html2text
```

### 2. Ensure .env is Configured

Your `.env` file should have:
```bash
ATLASSIAN_EMAIL=amit.choudhary@zendesk.com
ATLASSIAN_API_TOKEN=your_token_here
ATLASSIAN_DOMAIN=zendesk.atlassian.net
```

### 3. Test Connection

```bash
python3 atlassian_readonly.py --test
```

## 📖 Usage Examples

### Basic Export

```bash
python3 confluence_space_exporter.py --space ZDM
```

Output:
```
📚 Getting space info for: ZDM
✅ Found 42 pages
📄 Exporting pages:
   [1/42] Data Platform Overview
   [2/42] SFDC Field Documentation
   ...
✅ Export completed successfully!
   Output file: zdm_export_20251127_143052.md
```

### Export Multiple Spaces

```bash
# Export ZDM space
python3 confluence_space_exporter.py --space ZDM --output zdm_docs.md

# Export TECH space
python3 confluence_space_exporter.py --space TECH --output tech_docs.md

# Export DATA space
python3 confluence_space_exporter.py --space DATA --output data_docs.md
```

### Export with Options

```bash
# Limit to first 100 pages
python3 confluence_space_exporter.py --space ZDM --limit 100

# Exclude metadata (cleaner output)
python3 confluence_space_exporter.py --space ZDM --no-metadata

# Custom output filename
python3 confluence_space_exporter.py --space ZDM --output my_docs.md
```

## 📄 Output Format

The exported markdown file includes:

### 1. Header with Space Info
```markdown
# Space Name - Confluence Space Export

**Space Key:** ZDM
**Exported:** 2025-11-27 14:30:52
**Total Pages:** 42
**Confluence URL:** https://zendesk.atlassian.net/wiki/spaces/ZDM
```

### 2. Table of Contents
```markdown
## Table of Contents

1. [Data Platform Overview](#data-platform-overview)
2. [SFDC Field Documentation](#sfdc-field-documentation)
3. [Price Ramp Logic](#price-ramp-logic)
...
```

### 3. Page Content (with metadata)
```markdown
## SFDC Field Documentation

**Page ID:** 123456789
**Version:** 5
**Last Modified:** 2025-11-20
**Last Modified By:** Amit Choudhary
**URL:** [https://zendesk.atlassian.net/wiki/spaces/ZDM/pages/123456789](...)

[Markdown content of the page...]

---
```

## 🛠️ Features

- ✅ **Read-Only** - Safe, no modifications to Confluence
- ✅ **Complete Export** - All pages in the space
- ✅ **Table of Contents** - Easy navigation
- ✅ **Metadata** - Version, author, dates
- ✅ **HTML to Markdown** - Clean formatting
- ✅ **Audit Logging** - Timestamps for all API calls
- ✅ **Error Handling** - Continues even if some pages fail

## 📊 What Gets Exported

### Included:
- ✅ Page titles
- ✅ Page content (converted to Markdown)
- ✅ Version numbers
- ✅ Last modified date/author
- ✅ Page URLs
- ✅ Page hierarchy (in TOC)

### Not Included:
- ❌ Attachments (files, images)
- ❌ Comments
- ❌ Page restrictions/permissions
- ❌ Embedded macros (converted to text)
- ❌ Page history (only latest version)

## 🔧 Advanced Usage

### Python Script Integration

```python
from confluence_space_exporter import ConfluenceSpaceExporter
from atlassian_readonly import ReadOnlyAtlassianConfig

# Initialize
config = ReadOnlyAtlassianConfig()
exporter = ConfluenceSpaceExporter(config)

# Export space
output_file = exporter.export_space_to_markdown(
    space_key="ZDM",
    output_file="zdm_export.md",
    include_metadata=True
)

print(f"Exported to: {output_file}")
```

### Export Multiple Spaces in Batch

```python
spaces_to_export = ["ZDM", "TECH", "DATA", "ENG"]

for space_key in spaces_to_export:
    print(f"\nExporting {space_key}...")
    output_file = f"{space_key.lower()}_documentation.md"
    
    exporter.export_space_to_markdown(
        space_key=space_key,
        output_file=output_file
    )
    
    print(f"✅ {space_key} exported to {output_file}")
```

### Custom Processing

```python
# Get all pages first
pages = exporter.get_all_pages("ZDM")

# Filter pages by title
data_pages = [p for p in pages if "data" in p['title'].lower()]

print(f"Found {len(data_pages)} pages about data")

# Get specific page content
for page_summary in data_pages:
    page = exporter.get_page_content(page_summary['id'])
    # Process page...
```

## 🔍 Finding Your Space Key

If you don't know your space key:

1. Go to your Confluence space
2. Look at the URL: `https://zendesk.atlassian.net/wiki/spaces/ZDM/pages/...`
3. The space key is `ZDM`

Or search all spaces:
```python
from atlassian_readonly import ReadOnlyAtlassianConfig, ReadOnlyConfluenceClient

config = ReadOnlyAtlassianConfig()
confluence = ReadOnlyConfluenceClient(config)

# Search for spaces (not a direct method in our client, but you can search)
results = confluence.search_content("type=space", limit=100)
for result in results:
    print(f"Space: {result.get('title')} ({result.get('key')})")
```

## ⚡ Performance

- **Small space** (< 50 pages): 10-30 seconds
- **Medium space** (50-200 pages): 1-3 minutes
- **Large space** (200-500 pages): 3-10 minutes
- **Very large space** (500+ pages): 10+ minutes

API rate limits may apply for very large exports.

## 🐛 Troubleshooting

### Issue: "Could not access space"

**Cause:** No read permission or invalid space key

**Solution:**
```bash
# Verify space key is correct
# Check you have read access to the space
# Test connection first
python3 atlassian_readonly.py --test
```

### Issue: "No pages found"

**Cause:** Empty space or permission issues

**Solution:**
- Verify space key: `--space ZDM` (case sensitive)
- Check permissions in Confluence UI
- Try a different space you know has content

### Issue: "html2text not installed"

**Cause:** Optional package missing

**Solution:**
```bash
pip3 install --break-system-packages html2text
```

Note: Export will work without it, but formatting won't be as clean.

### Issue: Export is slow

**Cause:** Large space with many pages

**Solution:**
- Be patient - it needs to fetch each page individually
- Use `--limit` to export fewer pages for testing
- Consider exporting smaller spaces first

### Issue: Some pages have garbled content

**Cause:** Complex HTML/macros in Confluence

**Solution:**
- Install html2text for better conversion: `pip3 install html2text`
- Or view original page in Confluence (URLs are in export)

## 📝 Example Output Structure

```
zdm_export_20251127_143052.md
├── Header (Space info)
├── Table of Contents
├── Page 1
│   ├── Metadata
│   └── Content (Markdown)
├── Page 2
│   ├── Metadata
│   └── Content (Markdown)
└── ... (all pages)
```

## 🔐 Security Notes

- ✅ Uses read-only API client
- ✅ No modifications to Confluence
- ✅ All API calls are logged
- ✅ Respects Confluence permissions
- ⚠️ Exported files contain all page content - store securely

## 💡 Use Cases

### 1. Documentation Backup

```bash
# Regular backup of important spaces
python3 confluence_space_exporter.py --space ZDM --output backups/zdm_$(date +%Y%m%d).md
```

### 2. Offline Documentation

```bash
# Export for offline reading
python3 confluence_space_exporter.py --space TECH --output tech_offline.md
```

### 3. Content Migration

```bash
# Export before migrating to new system
python3 confluence_space_exporter.py --space DATA --output data_migration.md
```

### 4. Search & Analysis

```bash
# Export to markdown for easier text search
python3 confluence_space_exporter.py --space ZDM --no-metadata
# Then use: grep "SFDC" zdm_export_*.md
```

### 5. Documentation Review

```bash
# Export for team review
python3 confluence_space_exporter.py --space TECH
# Share the .md file for comments
```

## 🎯 Next Steps

1. **Install dependencies** (if not done):
   ```bash
   pip3 install --break-system-packages requests python-dotenv html2text
   ```

2. **Test connection**:
   ```bash
   python3 atlassian_readonly.py --test
   ```

3. **Export your first space**:
   ```bash
   python3 confluence_space_exporter.py --space ZDM
   ```

4. **View the result**:
   ```bash
   open zdm_export_*.md
   ```

---

**Tool:** `confluence_space_exporter.py`  
**Mode:** 🔒 Read-Only (Safe)  
**Reference:** Based on https://zendesk.atlassian.net/wiki/spaces/ZDM/pages

