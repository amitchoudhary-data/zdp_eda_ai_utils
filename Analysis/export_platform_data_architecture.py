#!/usr/bin/env python3
"""
Platform Data Architecture Exporter
Exports Platform Data Architecture documentation with PDD/EDA/Data Engineering perspective

Usage:
    python3 export_platform_data_architecture.py
    python3 export_platform_data_architecture.py --page-id 970330740
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
    sys.exit(1)

try:
    import html2text
    HTML2TEXT_AVAILABLE = True
except ImportError:
    HTML2TEXT_AVAILABLE = False
    print("⚠️  html2text not installed (using basic conversion)")


class PlatformDataArchitectureExporter:
    """Export Platform Data Architecture with data engineering focus"""
    
    def __init__(self, config: ReadOnlyAtlassianConfig):
        self.config = config
        self.client = ReadOnlyConfluenceClient(config)
        
        # Initialize HTML to Markdown converter
        if HTML2TEXT_AVAILABLE:
            self.h2t = html2text.HTML2Text()
            self.h2t.ignore_links = False
            self.h2t.ignore_images = False
            self.h2t.body_width = 0
        else:
            self.h2t = None
    
    def html_to_markdown(self, html_content: str) -> str:
        """Convert HTML content to Markdown"""
        if self.h2t and html_content:
            try:
                markdown = self.h2t.handle(html_content)
                return markdown.strip()
            except Exception as e:
                print(f"⚠️  Error converting HTML: {str(e)}")
                return self._strip_html_basic(html_content)
        else:
            return self._strip_html_basic(html_content)
    
    def _strip_html_basic(self, html_content: str) -> str:
        """Basic HTML tag stripping"""
        text = re.sub(r'<[^>]+>', '', html_content)
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&amp;', '&')
        text = text.replace('&quot;', '"')
        return text.strip()
    
    def get_page_with_children(self, page_id: str, depth: int = 2) -> List[Dict]:
        """Get page and its child pages up to specified depth"""
        print(f"📄 Fetching page: {page_id}")
        
        pages = []
        page = self.client.get_page(page_id, expand=['body.storage', 'version', 'children.page'])
        
        if not page:
            return pages
        
        pages.append(page)
        
        # Get child pages if depth > 0
        if depth > 0 and 'children' in page and 'page' in page['children']:
            children = page['children']['page'].get('results', [])
            print(f"   Found {len(children)} child pages")
            
            for child in children:
                child_id = child.get('id')
                if child_id:
                    child_pages = self.get_page_with_children(child_id, depth - 1)
                    pages.extend(child_pages)
        
        return pages
    
    def search_related_pages(self, keywords: List[str], space: str = "ENG") -> List[Dict]:
        """Search for pages related to keywords"""
        print(f"🔍 Searching for related pages...")
        
        all_pages = []
        for keyword in keywords:
            cql = f"space = {space} AND text ~ '{keyword}'"
            results = self.client.search_content(cql, limit=50)
            all_pages.extend(results)
        
        # Remove duplicates
        seen = set()
        unique_pages = []
        for page in all_pages:
            page_id = page.get('id')
            if page_id not in seen:
                seen.add(page_id)
                unique_pages.append(page)
        
        print(f"   Found {len(unique_pages)} unique related pages")
        return unique_pages
    
    def export_to_markdown(
        self,
        page_id: str,
        output_file: str,
        include_children: bool = True,
        include_related: bool = True
    ) -> str:
        """
        Export Platform Data Architecture to markdown
        
        Args:
            page_id: Main page ID (970330740 for Platform Data Architecture)
            output_file: Output filename
            include_children: Include child pages
            include_related: Include related pages
        """
        print(f"\n{'='*70}")
        print(f"📊 Platform Data Architecture Exporter")
        print(f"{'='*70}\n")
        
        # Get main page and children
        pages = self.get_page_with_children(page_id, depth=2 if include_children else 0)
        
        if not pages:
            print("❌ Could not retrieve page")
            return None
        
        main_page = pages[0]
        
        # Search for related pages
        related_pages = []
        if include_related:
            keywords = ["PDD", "EDA", "data engineering", "data platform", "data pipeline"]
            related_pages = self.search_related_pages(keywords, space="ENG")
        
        # Create markdown file
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write(f"# Platform Data Architecture\n")
            f.write(f"## Data Engineering Perspective: PDD, EDA, and Platform Data\n\n")
            
            f.write(f"**Document Type:** Technical Architecture Documentation  \n")
            f.write(f"**Perspective:** Platform Data Domain (PDD), Enterprise Data Architecture (EDA)  \n")
            f.write(f"**Focus:** Data Engineering & Product Analytics  \n")
            f.write(f"**Exported:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            f.write(f"**Source:** [Platform Data Architecture]")
            f.write(f"(https://{self.config.domain}/wiki/spaces/ENG/pages/{page_id})  \n\n")
            
            f.write(f"---\n\n")
            
            # Executive Summary
            f.write(f"## Executive Summary\n\n")
            f.write(f"This document provides a comprehensive overview of Zendesk's Platform Data ")
            f.write(f"Architecture from a **data engineering and product analytics perspective**. ")
            f.write(f"It covers:\n\n")
            f.write(f"- **PDD (Platform Data Domain)**: Core data infrastructure and pipelines\n")
            f.write(f"- **EDA (Enterprise Data Architecture)**: Enterprise-wide data strategy\n")
            f.write(f"- **Data Engineering**: Technical implementation and best practices\n")
            f.write(f"- **Product Analytics**: Data models supporting product insights\n\n")
            
            f.write(f"---\n\n")
            
            # Table of Contents
            f.write(f"## Table of Contents\n\n")
            f.write(f"### Core Architecture\n")
            for i, page in enumerate(pages, 1):
                title = page.get('title', 'Untitled')
                anchor = re.sub(r'[^\w\s-]', '', title).replace(' ', '-').lower()
                f.write(f"{i}. [{title}](#{anchor})\n")
            
            if related_pages:
                f.write(f"\n### Related Documentation\n")
                for i, page in enumerate(related_pages, len(pages) + 1):
                    title = page.get('title', 'Untitled')
                    anchor = re.sub(r'[^\w\s-]', '', title).replace(' ', '-').lower()
                    f.write(f"{i}. [{title}](#{anchor})\n")
            
            f.write(f"\n---\n\n")
            
            # Main content sections
            f.write(f"# Core Platform Data Architecture\n\n")
            
            # Export main pages
            print(f"\n📄 Exporting core architecture pages:")
            for i, page in enumerate(pages, 1):
                page_id = page.get('id')
                title = page.get('title', 'Untitled')
                
                print(f"   [{i}/{len(pages)}] {title}")
                
                # Determine section level based on hierarchy
                level = 2 if i == 1 else 3
                f.write(f"{'#' * level} {title}\n\n")
                
                # Add metadata
                version = page.get('version', {})
                page_url = f"https://{self.config.domain}/wiki/spaces/ENG/pages/{page_id}"
                f.write(f"**Page ID:** {page_id}  \n")
                f.write(f"**Version:** {version.get('number', 'Unknown')}  \n")
                if 'when' in version:
                    f.write(f"**Last Updated:** {version['when'][:10]}  \n")
                f.write(f"**Source:** [{page_url}]({page_url})  \n\n")
                
                # Data Engineering Context
                f.write(f"#### Data Engineering Context\n\n")
                if "platform" in title.lower():
                    f.write(f"*This section covers platform-level data engineering concepts ")
                    f.write(f"relevant to PDD and EDA initiatives.*\n\n")
                elif "pipeline" in title.lower():
                    f.write(f"*This section describes data pipeline architecture and ")
                    f.write(f"ETL/ELT processes.*\n\n")
                elif "model" in title.lower():
                    f.write(f"*This section details data modeling approaches for analytics ")
                    f.write(f"and product intelligence.*\n\n")
                
                # Page content
                body = page.get('body', {}).get('storage', {})
                html_content = body.get('value', '')
                
                if html_content:
                    markdown_content = self.html_to_markdown(html_content)
                    f.write(f"{markdown_content}\n\n")
                else:
                    f.write(f"*No content available*\n\n")
                
                f.write(f"---\n\n")
            
            # Related documentation section
            if related_pages:
                f.write(f"\n# Related Platform Data Documentation\n\n")
                f.write(f"The following pages provide additional context for data engineering ")
                f.write(f"and platform data initiatives:\n\n")
                
                print(f"\n📚 Including related documentation:")
                for i, page_summary in enumerate(related_pages, 1):
                    page_id = page_summary.get('id')
                    title = page_summary.get('title', 'Untitled')
                    
                    print(f"   [{i}/{len(related_pages)}] {title}")
                    
                    # Get full page
                    page = self.client.get_page(page_id, expand=['body.storage', 'version'])
                    
                    if page:
                        f.write(f"## {title}\n\n")
                        
                        version = page.get('version', {})
                        page_url = f"https://{self.config.domain}/wiki/spaces/ENG/pages/{page_id}"
                        f.write(f"**Source:** [{page_url}]({page_url})  \n")
                        if 'when' in version:
                            f.write(f"**Last Updated:** {version['when'][:10]}  \n")
                        f.write(f"\n")
                        
                        body = page.get('body', {}).get('storage', {})
                        html_content = body.get('value', '')
                        
                        if html_content:
                            markdown_content = self.html_to_markdown(html_content)
                            # Limit related content to summary
                            lines = markdown_content.split('\n')
                            summary = '\n'.join(lines[:20])  # First 20 lines
                            f.write(f"{summary}\n\n")
                            if len(lines) > 20:
                                f.write(f"*[See full page for complete details]({page_url})*\n\n")
                        
                        f.write(f"---\n\n")
            
            # Appendix - Data Engineering Glossary
            f.write(f"\n# Appendix: Data Engineering Glossary\n\n")
            f.write(f"## Key Terms\n\n")
            f.write(f"- **PDD (Platform Data Domain)**: The organizational domain responsible for ")
            f.write(f"platform-level data infrastructure, pipelines, and services\n")
            f.write(f"- **EDA (Enterprise Data Architecture)**: The enterprise-wide data strategy, ")
            f.write(f"governance, and architectural standards\n")
            f.write(f"- **Data Engineering**: The practice of designing, building, and maintaining ")
            f.write(f"data pipelines and infrastructure\n")
            f.write(f"- **Product Analytics**: Analysis of product usage data to drive product decisions\n")
            f.write(f"- **ETL/ELT**: Extract, Transform, Load / Extract, Load, Transform data processes\n")
            f.write(f"- **Data Pipeline**: Automated workflow for moving and transforming data\n")
            f.write(f"- **Data Model**: Structured representation of data entities and relationships\n\n")
        
        print(f"\n{'='*70}")
        print(f"✅ Export completed successfully!")
        print(f"   Output file: {output_file}")
        
        file_size = Path(output_file).stat().st_size / (1024 * 1024)
        print(f"   File size: {file_size:.2f} MB")
        print(f"{'='*70}\n")
        
        return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Export Platform Data Architecture with data engineering perspective'
    )
    
    parser.add_argument(
        '--page-id',
        default='970330740',
        help='Main page ID (default: 970330740 for Platform Data Architecture)'
    )
    
    parser.add_argument(
        '--output',
        default='platform_data_architecture_pdd_eda.md',
        help='Output markdown file'
    )
    
    parser.add_argument(
        '--no-children',
        action='store_true',
        help='Do not include child pages'
    )
    
    parser.add_argument(
        '--no-related',
        action='store_true',
        help='Do not include related pages'
    )
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        config = ReadOnlyAtlassianConfig()
        
        # Create exporter
        exporter = PlatformDataArchitectureExporter(config)
        
        # Export
        output_file = exporter.export_to_markdown(
            page_id=args.page_id,
            output_file=args.output,
            include_children=not args.no_children,
            include_related=not args.no_related
        )
        
        if output_file:
            print(f"💡 View the exported file:")
            print(f"   open {output_file}")
            print(f"\n💡 Or with VS Code:")
            print(f"   code {output_file}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

