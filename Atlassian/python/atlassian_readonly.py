#!/usr/bin/env python3
"""
Read-Only Atlassian API Integration
Provides SECURE READ-ONLY access to Atlassian services (Jira, Confluence)

Security Features:
- Read-only operations only (GET requests)
- No write, update, or delete operations
- Restricted API token permissions
- Audit logging for all API calls

Setup:
1. Create .env file with read-only credentials
2. Generate API token with READ-ONLY permissions
3. Use this module for safe data retrieval

Required .env variables:
    ATLASSIAN_EMAIL=your.email@company.com
    ATLASSIAN_API_TOKEN=your_readonly_api_token
    ATLASSIAN_DOMAIN=yourcompany.atlassian.net
"""

import os
import sys
from typing import Optional, Dict, Any, List, TYPE_CHECKING
from pathlib import Path
import json
from datetime import datetime

if TYPE_CHECKING:
    from requests.auth import HTTPBasicAuth

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False
    print("⚠️  python-dotenv not installed. Install with: pip install python-dotenv")

try:
    import requests
    from requests.auth import HTTPBasicAuth
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("⚠️  requests not installed. Install with: pip install requests")


class ReadOnlyAtlassianConfig:
    """Read-Only Atlassian API configuration manager"""
    
    def __init__(self, env_file: str = ".env"):
        """
        Initialize read-only Atlassian configuration
        
        Args:
            env_file: Path to .env file (default: .env in current directory)
        """
        self.env_file = Path(env_file)
        self.read_only = True  # Enforce read-only mode
        self._load_environment()
        
        # Load credentials from environment
        self.email = os.getenv('ATLASSIAN_EMAIL')
        self.api_token = os.getenv('ATLASSIAN_API_TOKEN')
        self.domain = os.getenv('ATLASSIAN_DOMAIN')
        self.jira_project = os.getenv('JIRA_PROJECT_KEY', '')
        
        # Validate credentials
        self._validate_credentials()
        
        print("🔒 READ-ONLY MODE: Only GET operations allowed")
    
    def _load_environment(self):
        """Load environment variables from .env file"""
        if DOTENV_AVAILABLE and self.env_file.exists():
            load_dotenv(self.env_file)
            print(f"✅ Loaded credentials from {self.env_file}")
        elif self.env_file.exists():
            # Manual parsing if python-dotenv not available
            print(f"⚠️  Manually loading {self.env_file}")
            with open(self.env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip().strip('"').strip("'")
        else:
            print(f"⚠️  No .env file found at {self.env_file}")
    
    def _validate_credentials(self):
        """Validate that required credentials are present"""
        missing = []
        
        if not self.email:
            missing.append('ATLASSIAN_EMAIL')
        if not self.api_token:
            missing.append('ATLASSIAN_API_TOKEN')
        if not self.domain:
            missing.append('ATLASSIAN_DOMAIN')
        
        if missing:
            print(f"❌ Missing required environment variables: {', '.join(missing)}")
            print("\n📝 Setup Instructions for READ-ONLY Token:")
            print("   1. Go to https://id.atlassian.com/manage-profile/security/api-tokens")
            print("   2. Click 'Create API token'")
            print("   3. ⚠️  IMPORTANT: Use a LIMITED account or configure Jira permissions")
            print("      to READ-ONLY for this token")
            print("   4. Add to .env file")
            raise ValueError("Missing required Atlassian credentials")
        
        print("✅ All Atlassian credentials loaded successfully")
    
    def get_auth(self) -> "HTTPBasicAuth":
        """Get HTTP Basic Auth object for API requests"""
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests library required. Install with: pip install requests")
        return HTTPBasicAuth(self.email, self.api_token)
    
    def get_jira_url(self, endpoint: str = "") -> str:
        """Get full Jira API URL"""
        base_url = f"https://{self.domain}/rest/api/3"
        return f"{base_url}/{endpoint.lstrip('/')}" if endpoint else base_url
    
    def get_confluence_url(self, endpoint: str = "") -> str:
        """Get full Confluence API URL"""
        base_url = f"https://{self.domain}/wiki/rest/api"
        return f"{base_url}/{endpoint.lstrip('/')}" if endpoint else base_url
    
    def test_connection(self) -> bool:
        """Test connection to Atlassian API"""
        if not REQUESTS_AVAILABLE:
            print("❌ requests library not available")
            return False
        
        try:
            response = requests.get(
                self.get_jira_url("myself"),
                auth=self.get_auth(),
                timeout=10
            )
            
            if response.status_code == 200:
                user_data = response.json()
                print(f"✅ Successfully connected to Atlassian (READ-ONLY)")
                print(f"   Logged in as: {user_data.get('displayName', 'Unknown')}")
                print(f"   Email: {user_data.get('emailAddress', 'Unknown')}")
                print(f"   🔒 Mode: READ-ONLY (GET operations only)")
                return True
            else:
                print(f"❌ Connection failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")
            return False


class ReadOnlyJiraClient:
    """Read-Only Jira API client - GET operations only"""
    
    def __init__(self, config: ReadOnlyAtlassianConfig):
        self.config = config
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests library required")
        
        print("🔒 Jira Client initialized in READ-ONLY mode")
    
    def _log_request(self, operation: str, endpoint: str):
        """Log all API requests for audit purposes"""
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] READ: {operation} -> {endpoint}")
    
    def get_issue(self, issue_key: str) -> Optional[Dict]:
        """
        Get Jira issue by key (READ-ONLY)
        
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            
        Returns:
            Issue data dictionary or None if not found
        """
        self._log_request("get_issue", issue_key)
        
        try:
            response = requests.get(
                self.config.get_jira_url(f"issue/{issue_key}"),
                auth=self.config.get_auth(),
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Failed to get issue {issue_key}: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error getting issue: {str(e)}")
            return None
    
    def search_issues(self, jql: str, max_results: int = 50, fields: List[str] = None) -> List[Dict]:
        """
        Search Jira issues using JQL (READ-ONLY)
        
        Args:
            jql: JQL query string
            max_results: Maximum number of results to return
            fields: List of fields to include (default: all)
            
        Returns:
            List of issue dictionaries
        """
        self._log_request("search_issues", jql)
        
        try:
            params = {
                "jql": jql,
                "maxResults": max_results
            }
            
            if fields:
                params["fields"] = ",".join(fields)
            
            response = requests.get(
                self.config.get_jira_url("search"),
                auth=self.config.get_auth(),
                params=params,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json().get('issues', [])
            else:
                print(f"❌ Search failed: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error searching issues: {str(e)}")
            return []
    
    def get_project(self, project_key: str) -> Optional[Dict]:
        """
        Get project information (READ-ONLY)
        
        Args:
            project_key: Project key (e.g., "PROJ")
            
        Returns:
            Project data dictionary or None
        """
        self._log_request("get_project", project_key)
        
        try:
            response = requests.get(
                self.config.get_jira_url(f"project/{project_key}"),
                auth=self.config.get_auth(),
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Failed to get project: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error getting project: {str(e)}")
            return None
    
    def get_issue_comments(self, issue_key: str) -> List[Dict]:
        """
        Get comments for an issue (READ-ONLY)
        
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            
        Returns:
            List of comment dictionaries
        """
        self._log_request("get_comments", issue_key)
        
        try:
            response = requests.get(
                self.config.get_jira_url(f"issue/{issue_key}/comment"),
                auth=self.config.get_auth(),
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get('comments', [])
            else:
                print(f"❌ Failed to get comments: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error getting comments: {str(e)}")
            return []
    
    def get_issue_transitions(self, issue_key: str) -> List[Dict]:
        """
        Get available transitions for an issue (READ-ONLY)
        
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            
        Returns:
            List of available transitions
        """
        self._log_request("get_transitions", issue_key)
        
        try:
            response = requests.get(
                self.config.get_jira_url(f"issue/{issue_key}/transitions"),
                auth=self.config.get_auth(),
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get('transitions', [])
            else:
                print(f"❌ Failed to get transitions: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error getting transitions: {str(e)}")
            return []


class ReadOnlyConfluenceClient:
    """Read-Only Confluence API client - GET operations only"""
    
    def __init__(self, config: ReadOnlyAtlassianConfig):
        self.config = config
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests library required")
        
        print("🔒 Confluence Client initialized in READ-ONLY mode")
    
    def _log_request(self, operation: str, endpoint: str):
        """Log all API requests for audit purposes"""
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] READ: {operation} -> {endpoint}")
    
    def get_page(self, page_id: str, expand: List[str] = None) -> Optional[Dict]:
        """
        Get Confluence page by ID (READ-ONLY)
        
        Args:
            page_id: Page ID
            expand: List of fields to expand (e.g., ['body.storage', 'version'])
            
        Returns:
            Page data dictionary or None
        """
        self._log_request("get_page", page_id)
        
        try:
            params = {}
            if expand:
                params['expand'] = ','.join(expand)
            
            response = requests.get(
                self.config.get_confluence_url(f"content/{page_id}"),
                auth=self.config.get_auth(),
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Failed to get page: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error getting page: {str(e)}")
            return None
    
    def search_content(self, cql: str, limit: int = 25) -> List[Dict]:
        """
        Search Confluence content using CQL (READ-ONLY)
        
        Args:
            cql: Confluence Query Language string
            limit: Maximum results to return
            
        Returns:
            List of search results
        """
        self._log_request("search_content", cql)
        
        try:
            params = {
                'cql': cql,
                'limit': limit
            }
            
            response = requests.get(
                self.config.get_confluence_url("content/search"),
                auth=self.config.get_auth(),
                params=params,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json().get('results', [])
            else:
                print(f"❌ Search failed: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error searching content: {str(e)}")
            return []
    
    def get_space(self, space_key: str) -> Optional[Dict]:
        """
        Get Confluence space information (READ-ONLY)
        
        Args:
            space_key: Space key (e.g., "TECH")
            
        Returns:
            Space data dictionary or None
        """
        self._log_request("get_space", space_key)
        
        try:
            response = requests.get(
                self.config.get_confluence_url(f"space/{space_key}"),
                auth=self.config.get_auth(),
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Failed to get space: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error getting space: {str(e)}")
            return None


def main():
    """CLI for testing read-only Atlassian connection"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Read-Only Atlassian API Tool',
        epilog='🔒 This tool only performs READ operations. No data will be modified.'
    )
    parser.add_argument('--test', action='store_true', help='Test connection')
    parser.add_argument('--get-issue', type=str, metavar='KEY', help='Get Jira issue by key')
    parser.add_argument('--search-jira', type=str, metavar='JQL', help='Search Jira with JQL')
    parser.add_argument('--get-project', type=str, metavar='KEY', help='Get Jira project info')
    parser.add_argument('--get-page', type=str, metavar='ID', help='Get Confluence page by ID')
    parser.add_argument('--search-confluence', type=str, metavar='CQL', help='Search Confluence with CQL')
    parser.add_argument('--get-space', type=str, metavar='KEY', help='Get Confluence space info')
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        config = ReadOnlyAtlassianConfig()
        
        if args.test:
            config.test_connection()
            
        elif args.get_issue:
            jira = ReadOnlyJiraClient(config)
            issue = jira.get_issue(args.get_issue)
            if issue:
                print(f"\n📋 Issue: {issue['key']}")
                print(f"   Summary: {issue['fields']['summary']}")
                print(f"   Status: {issue['fields']['status']['name']}")
                print(f"   Type: {issue['fields']['issuetype']['name']}")
                
        elif args.search_jira:
            jira = ReadOnlyJiraClient(config)
            issues = jira.search_issues(args.search_jira)
            print(f"\n🔍 Found {len(issues)} issues:")
            for issue in issues:
                print(f"   {issue['key']}: {issue['fields']['summary']}")
                
        elif args.get_project:
            jira = ReadOnlyJiraClient(config)
            project = jira.get_project(args.get_project)
            if project:
                print(f"\n📁 Project: {project['key']}")
                print(f"   Name: {project['name']}")
                print(f"   Lead: {project.get('lead', {}).get('displayName', 'Unknown')}")
                
        elif args.get_page:
            confluence = ReadOnlyConfluenceClient(config)
            page = confluence.get_page(args.get_page, expand=['body.storage', 'version'])
            if page:
                print(f"\n📄 Page: {page['title']}")
                print(f"   ID: {page['id']}")
                print(f"   Version: {page['version']['number']}")
                
        elif args.search_confluence:
            confluence = ReadOnlyConfluenceClient(config)
            results = confluence.search_content(args.search_confluence)
            print(f"\n🔍 Found {len(results)} pages:")
            for result in results:
                print(f"   {result['title']} (ID: {result['id']})")
                
        elif args.get_space:
            confluence = ReadOnlyConfluenceClient(config)
            space = confluence.get_space(args.get_space)
            if space:
                print(f"\n📚 Space: {space['key']}")
                print(f"   Name: {space['name']}")
                print(f"   Type: {space['type']}")
        else:
            # Show config
            print("\n📋 Current Configuration (READ-ONLY):")
            print(f"   Domain: {config.domain}")
            print(f"   Email: {config.email}")
            print(f"   Mode: 🔒 READ-ONLY")
            print(f"   Jira URL: {config.get_jira_url()}")
            print(f"   Confluence URL: {config.get_confluence_url()}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

