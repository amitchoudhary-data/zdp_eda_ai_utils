#!/usr/bin/env python3
"""
Secure Atlassian API Integration
Provides secure access to Atlassian services (Jira, Confluence, etc.)

Setup:
1. Create .env file with your credentials (this file is gitignored)
2. Never commit credentials to git
3. Use this module to access Atlassian APIs securely

Required .env variables:
    ATLASSIAN_EMAIL=your.email@company.com
    ATLASSIAN_API_TOKEN=your_api_token
    ATLASSIAN_DOMAIN=yourcompany.atlassian.net
    JIRA_PROJECT_KEY=PROJ  # Optional
"""

import os
import sys
from typing import Optional, Dict, Any, TYPE_CHECKING
from pathlib import Path
import json

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


class AtlassianConfig:
    """Secure Atlassian API configuration manager"""
    
    def __init__(self, env_file: str = ".env"):
        """
        Initialize Atlassian configuration
        
        Args:
            env_file: Path to .env file (default: .env in current directory)
        """
        self.env_file = Path(env_file)
        self._load_environment()
        
        # Load credentials from environment
        self.email = os.getenv('ATLASSIAN_EMAIL')
        self.api_token = os.getenv('ATLASSIAN_API_TOKEN')
        self.domain = os.getenv('ATLASSIAN_DOMAIN')
        self.jira_project = os.getenv('JIRA_PROJECT_KEY', '')
        
        # Validate credentials
        self._validate_credentials()
    
    def _load_environment(self):
        """Load environment variables from .env file"""
        if DOTENV_AVAILABLE and self.env_file.exists():
            load_dotenv(self.env_file)
            print(f"✅ Loaded credentials from {self.env_file}")
        elif self.env_file.exists():
            # Manual parsing if python-dotenv not available
            print(f"⚠️  Manually loading {self.env_file} (install python-dotenv for better support)")
            with open(self.env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip().strip('"').strip("'")
        else:
            print(f"⚠️  No .env file found at {self.env_file}")
            print("   Checking environment variables...")
    
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
            print("\n📝 Setup Instructions:")
            print(f"   1. Create {self.env_file} in this directory")
            print("   2. Add the following variables:")
            print("      ATLASSIAN_EMAIL=your.email@company.com")
            print("      ATLASSIAN_API_TOKEN=your_api_token")
            print("      ATLASSIAN_DOMAIN=yourcompany.atlassian.net")
            print("\n🔐 How to get API token:")
            print("   1. Go to https://id.atlassian.com/manage-profile/security/api-tokens")
            print("   2. Click 'Create API token'")
            print("   3. Copy the token and add to .env file")
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
            # Test Jira connection
            response = requests.get(
                self.get_jira_url("myself"),
                auth=self.get_auth(),
                timeout=10
            )
            
            if response.status_code == 200:
                user_data = response.json()
                print(f"✅ Successfully connected to Atlassian")
                print(f"   Logged in as: {user_data.get('displayName', 'Unknown')}")
                print(f"   Email: {user_data.get('emailAddress', 'Unknown')}")
                return True
            else:
                print(f"❌ Connection failed: {response.status_code}")
                print(f"   Response: {response.text[:200]}")
                return False
                
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")
            return False
    
    def get_config_dict(self) -> Dict[str, Any]:
        """Get configuration as dictionary (without sensitive data)"""
        return {
            "domain": self.domain,
            "email": self.email,
            "jira_project": self.jira_project,
            "jira_base_url": self.get_jira_url(),
            "confluence_base_url": self.get_confluence_url(),
            "api_token_set": bool(self.api_token)
        }


class JiraClient:
    """Simple Jira API client"""
    
    def __init__(self, config: AtlassianConfig):
        self.config = config
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests library required")
    
    def get_issue(self, issue_key: str) -> Optional[Dict]:
        """Get Jira issue by key"""
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
    
    def search_issues(self, jql: str, max_results: int = 50) -> list:
        """Search Jira issues using JQL"""
        try:
            response = requests.get(
                self.config.get_jira_url("search"),
                auth=self.config.get_auth(),
                params={"jql": jql, "maxResults": max_results},
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
    
    def create_issue(self, project: str, summary: str, description: str, 
                     issue_type: str = "Task") -> Optional[Dict]:
        """Create a new Jira issue"""
        try:
            payload = {
                "fields": {
                    "project": {"key": project},
                    "summary": summary,
                    "description": {
                        "type": "doc",
                        "version": 1,
                        "content": [{
                            "type": "paragraph",
                            "content": [{"type": "text", "text": description}]
                        }]
                    },
                    "issuetype": {"name": issue_type}
                }
            }
            
            response = requests.post(
                self.config.get_jira_url("issue"),
                auth=self.config.get_auth(),
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=10
            )
            
            if response.status_code == 201:
                issue = response.json()
                print(f"✅ Created issue: {issue['key']}")
                return issue
            else:
                print(f"❌ Failed to create issue: {response.status_code}")
                print(f"   Response: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error creating issue: {str(e)}")
            return None


def main():
    """CLI for testing Atlassian connection"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Atlassian API Configuration Tool')
    parser.add_argument('--test', action='store_true', help='Test connection')
    parser.add_argument('--setup', action='store_true', help='Setup wizard')
    parser.add_argument('--get-issue', type=str, help='Get Jira issue by key')
    parser.add_argument('--search', type=str, help='Search Jira with JQL')
    
    args = parser.parse_args()
    
    if args.setup:
        setup_wizard()
        return
    
    try:
        # Load configuration
        config = AtlassianConfig()
        
        if args.test:
            config.test_connection()
        elif args.get_issue:
            client = JiraClient(config)
            issue = client.get_issue(args.get_issue)
            if issue:
                print(json.dumps(issue, indent=2))
        elif args.search:
            client = JiraClient(config)
            issues = client.search_issues(args.search)
            print(f"Found {len(issues)} issues")
            for issue in issues:
                print(f"  {issue['key']}: {issue['fields']['summary']}")
        else:
            # Just show config
            print("\n📋 Current Configuration:")
            print(json.dumps(config.get_config_dict(), indent=2))
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


def setup_wizard():
    """Interactive setup wizard"""
    print("🔧 Atlassian API Setup Wizard")
    print("="*60)
    
    env_file = Path(".env")
    
    if env_file.exists():
        overwrite = input(f"\n⚠️  {env_file} already exists. Overwrite? (y/N): ")
        if overwrite.lower() != 'y':
            print("Setup cancelled.")
            return
    
    print("\n📝 Enter your Atlassian credentials:")
    email = input("   Email: ").strip()
    domain = input("   Domain (e.g., yourcompany.atlassian.net): ").strip()
    api_token = input("   API Token: ").strip()
    project = input("   Jira Project Key (optional): ").strip()
    
    # Write to .env file
    with open(env_file, 'w') as f:
        f.write(f"# Atlassian API Configuration\n")
        f.write(f"# Generated: {__import__('datetime').datetime.now()}\n\n")
        f.write(f"ATLASSIAN_EMAIL={email}\n")
        f.write(f"ATLASSIAN_API_TOKEN={api_token}\n")
        f.write(f"ATLASSIAN_DOMAIN={domain}\n")
        if project:
            f.write(f"JIRA_PROJECT_KEY={project}\n")
    
    print(f"\n✅ Configuration saved to {env_file}")
    print("\n🔐 IMPORTANT: Add .env to .gitignore to keep credentials secure!")
    
    # Test connection
    test = input("\nTest connection now? (Y/n): ")
    if test.lower() != 'n':
        try:
            config = AtlassianConfig()
            config.test_connection()
        except Exception as e:
            print(f"❌ Test failed: {str(e)}")


if __name__ == "__main__":
    main()

