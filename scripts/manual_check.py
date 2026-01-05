#!/usr/bin/env python3
"""
Help manually check publication files by extracting key information.
"""

import os
import re
from pathlib import Path

def extract_key_info(filepath):
    """Extract title from metadata and first 500 chars after ## Full Text."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pmid = filepath.stem
        
        # Extract title from metadata
        title_match = re.search(r'^title:\s*(.+?)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "No title found"
        
        # Check if full text is available
        if "full_text_available: false" in content:
            return pmid, title, "NO FULL TEXT", ""
        
        # Extract first part of full text
        fulltext_match = re.search(r'## Full Text\s*\n(.*)', content, re.DOTALL)
        if not fulltext_match:
            return pmid, title, "NO FULL TEXT SECTION", ""
        
        fulltext = fulltext_match.group(1)[:500].replace('\n', ' ')
        
        # Extract key terms from abstract
        abstract_match = re.search(r'## Abstract\s*\n(.*?)(?=\n## Full Text|\Z)', content, re.DOTALL)
        abstract = abstract_match.group(1)[:300] if abstract_match else ""
        
        return pmid, title, abstract, fulltext
        
    except Exception as e:
        return filepath.stem, "", "", f"Error: {e}"

def main():
    publications_dir = Path("publications")
    md_files = sorted(publications_dir.glob("*.md"))
    
    # Process in batches of 10
    batch_size = 10
    
    for i in range(0, len(md_files), batch_size):
        batch = md_files[i:i+batch_size]
        print(f"\n{'='*80}")
        print(f"BATCH {i//batch_size + 1} (Files {i+1}-{min(i+batch_size, len(md_files))})")
        print('='*80)
        
        for filepath in batch:
            pmid, title, abstract_preview, fulltext_preview = extract_key_info(filepath)
            
            if "NO FULL TEXT" in abstract_preview:
                continue
            
            print(f"\n{pmid}:")
            print(f"Title: {title[:80]}...")
            print(f"Abstract preview: {abstract_preview[:150]}...")
            print(f"Full text preview: {fulltext_preview[:150]}...")
            
        input("\nPress Enter to continue to next batch...")

if __name__ == "__main__":
    main()