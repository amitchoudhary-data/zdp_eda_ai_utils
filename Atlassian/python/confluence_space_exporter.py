#!/usr/bin/env python3
"""
Confluence Space to Markdown Exporter
Exports all pages from a Confluence space to a single markdown file

Usage:
    python3 confluence_space_exporter.py --space ZDM
    python3 confluence_space_exporter.py --space ZDM --output zdm_pages.md
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import re

try:
    from atlassian_readonly import ReadOnlyAtlassianConfig, ReadOnlyConfluenceClient
except ImportError:
    print("❌ Error: atlassian_readonly.py not found")
    print("   Make sure you're in the correct directory")
    sys.exit(1)

try:
    import html2text
    HTML2TEXT_AVAILABLE = True
except ImportError:
    HTML2TEXT_AVAILABLE = False
    print("⚠️  html2text not installed (optional but recommended)")
    print("   Install with: pip3 install --break-system-packages html2text")
    print("   Continuing without HTML to Markdown conversion...")


class ConfluenceSpaceExporter:
    """Export Confluence space pages to markdown"""
    
    def __init__(self, config: ReadOnlyAtlassianConfig):
        self.config = config
        self.client = ReadOnlyConfluenceClient(config)
        
        # Initialize HTML to Markdown converter
        if HTML2TEXT_AVAILABLE:
            self.h2t = html2text.HTML2Text()
            self.h2t.ignore_links = False
            self.h2t.ignore_images = False
            self.h2t.body_width = 0  # Don't wrap text
        else:
            self.h2t = None
    
    def get_space_info(self, space_key: str) -> Optional[Dict]:
        """Get information about the space"""
        print(f"📚 Getting space info for: {space_key}")
        return self.client.get_space(space_key)
    
    def get_all_pages(self, space_key: str, limit: int = 1000) -> List[Dict]:
        """Get all pages in a space"""
        print(f"🔍 Searching for pages in space: {space_key}")
        
        # Use CQL to find all pages in the space
        cql = f"space = {space_key} AND type = page"
        pages = self.client.search_content(cql, limit=limit)
        
        print(f"✅ Found {len(pages)} pages")
        return pages
    
    def get_page_content(self, page_id: str) -> Optional[Dict]:
        """Get full page content with body"""
        return self.client.get_page(
            page_id,
            expand=['body.storage', 'version', 'ancestors', 'children']
        )
    
    def html_to_markdown(self, html_content: str) -> str:
        """Convert HTML content to Markdown"""
        if self.h2t and html_content:
            try:
                markdown = self.h2t.handle(html_content)
                return markdown.strip()
            except Exception as e:
                print(f"⚠️  Error converting HTML to Markdown: {str(e)}")
                return self._strip_html_basic(html_content)
        else:
            return self._strip_html_basic(html_content)
    
    def _strip_html_basic(self, html_content: str) -> str:
        """Basic HTML tag stripping if html2text not available"""
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', html_content)
        # Decode HTML entities
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&amp;', '&')
        text = text.replace('&quot;', '"')
        return text.strip()
    
    def export_space_to_markdown(
        self,
        space_key: str,
        output_file: str = None,
        include_metadata: bool = True
    ) -> str:
        """
        Export entire Confluence space to markdown file
        
        Args:
            space_key: Space key (e.g., "ZDM")
            output_file: Output filename (default: {space_key}_export.md)
            include_metadata: Include page metadata in output
            
        Returns:
            Path to created markdown file
        """
        # Set default output filename
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"{space_key.lower()}_export_{timestamp}.md"
        
        print(f"\n{'='*70}")
        print(f"📖 Confluence Space Exporter")
        print(f"{'='*70}")
        
        # Get space info
        space_info = self.get_space_info(space_key)
        if not space_info:
            print(f"❌ Could not access space: {space_key}")
            print("   Check your permissions and space key")
            return None
        
        space_name = space_info.get('name', space_key)
        print(f"   Space: {space_name} ({space_key})")
        print(f"   Type: {space_info.get('type', 'Unknown')}")
        
        # Get all pages
        pages = self.get_all_pages(space_key)
        
        if not pages:
            print(f"⚠️  No pages found in space {space_key}")
            return None
        
        # Create markdown file
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write(f"# {space_name} - Confluence Space Export\n\n")
            f.write(f"**Space Key:** {space_key}  \n")
            f.write(f"**Exported:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            f.write(f"**Total Pages:** {len(pages)}  \n")
            f.write(f"**Confluence URL:** https://{self.config.domain}/wiki/spaces/{space_key}\n\n")
            f.write(f"---\n\n")
            
            # Write table of contents
            f.write(f"## Table of Contents\n\n")
            for i, page in enumerate(pages, 1):
                title = page.get('title', 'Untitled')
                page_id = page.get('id', '')
                # Create anchor link (remove special chars)
                anchor = re.sub(r'[^\w\s-]', '', title).replace(' ', '-').lower()
                f.write(f"{i}. [{title}](#{anchor})\n")
            
            f.write(f"\n---\n\n")
            
            # Export each page
            print(f"\n📄 Exporting pages:")
            for i, page_summary in enumerate(pages, 1):
                page_id = page_summary.get('id')
                title = page_summary.get('title', 'Untitled')
                
                print(f"   [{i}/{len(pages)}] {title}")
                
                # Get full page content
                page = self.get_page_content(page_id)
                
                if not page:
                    f.write(f"## {title}\n\n")
                    f.write(f"*Could not retrieve page content*\n\n")
                    f.write(f"---\n\n")
                    continue
                
                # Write page header
                f.write(f"## {title}\n\n")
                
                # Write metadata if requested
                if include_metadata:
                    version = page.get('version', {})
                    f.write(f"**Page ID:** {page_id}  \n")
                    f.write(f"**Version:** {version.get('number', 'Unknown')}  \n")
                    
                    # Get last modified info
                    if 'when' in version:
                        f.write(f"**Last Modified:** {version['when'][:10]}  \n")
                    if 'by' in version:
                        author = version['by'].get('displayName', 'Unknown')
                        f.write(f"**Last Modified By:** {author}  \n")
                    
                    # Page URL
                    page_url = f"https://{self.config.domain}/wiki/spaces/{space_key}/pages/{page_id}"
                    f.write(f"**URL:** [{page_url}]({page_url})  \n")
                    f.write(f"\n")
                
                # Get page content
                body = page.get('body', {}).get('storage', {})
                html_content = body.get('value', '')
                
                if html_content:
                    # Convert to markdown
                    markdown_content = self.html_to_markdown(html_content)
                    f.write(f"{markdown_content}\n\n")
                else:
                    f.write(f"*No content*\n\n")
                
                # Add separator
                f.write(f"---\n\n")
        
        print(f"\n{'='*70}")
        print(f"✅ Export completed successfully!")
        print(f"   Output file: {output_file}")
        print(f"   Total pages: {len(pages)}")
        
        # Get file size
        file_size = Path(output_file).stat().st_size
        size_mb = file_size / (1024 * 1024)
        print(f"   File size: {size_mb:.2f} MB")
        print(f"{'='*70}\n")
        
        return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Export Confluence space to markdown file',
        epilog='Example: python3 confluence_space_exporter.py --space ZDM'
    )
    
    parser.add_argument(
        '--space',
        required=True,
        help='Confluence space key (e.g., ZDM)'
    )
    
    parser.add_argument(
        '--output',
        help='Output markdown file (default: {space}_export_{timestamp}.md)'
    )
    
    parser.add_argument(
        '--no-metadata',
        action='store_true',
        help='Exclude page metadata from export'
    )
    
    parser.add_argument(
        '--limit',
        type=int,
        default=1000,
        help='Maximum number of pages to export (default: 1000)'
    )
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        config = ReadOnlyAtlassianConfig()
        
        # Create exporter
        exporter = ConfluenceSpaceExporter(config)
        
        # Export space
        output_file = exporter.export_space_to_markdown(
            space_key=args.space,
            output_file=args.output,
            include_metadata=not args.no_metadata
        )
        
        if output_file:
            print(f"💡 View the exported file:")
            print(f"   open {output_file}")
            print(f"\n💡 Or with your preferred editor:")
            print(f"   code {output_file}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

