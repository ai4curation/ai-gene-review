#!/usr/bin/env python3
"""
Comprehensive check of publication files for HTML scraping issues.
"""

import os
import re
from pathlib import Path

def check_known_problematic_content(content):
    """Check for known problematic full text replacements."""
    issues = []
    
    # Check for the generic Dscam homeostatic review
    if "Dscam-mediated homeostatic mechanisms" in content:
        if "## Abstract" in content:
            abstract = content.split("## Abstract")[1].split("## Full Text")[0] if "## Full Text" in content else ""
            if "homeostatic" not in abstract.lower() and "plasticity" not in abstract.lower():
                issues.append("Generic Dscam homeostatic review replacing original content")
    
    # Check for Beat/Side protein paper
    if "Beat/Side proteins play in olfactory circuit assembly" in content or \
       ("Beaten path (Beat) family" in content and "Sidestep (Side) family" in content and "heterophilic interaction network" in content):
        if "## Abstract" in content:
            abstract = content.split("## Abstract")[1].split("## Full Text")[0] if "## Full Text" in content else ""
            if "beat" not in abstract.lower() and "side" not in abstract.lower():
                issues.append("Beat/Side protein paper replacing original content")
    
    # Check for cricket neuroplasticity paper
    if "Gryllus bimaculatus" in content and "prothoracic ganglion" in content:
        if "## Abstract" in content:
            abstract = content.split("## Abstract")[1].split("## Full Text")[0] if "## Full Text" in content else ""
            if "cricket" not in abstract.lower() and "gryllus" not in abstract.lower():
                issues.append("Cricket neuroplasticity paper replacing original content")
    
    # Check for HFD/autophagy paper
    if "high-fat diet (HFD)" in content and "autophagy" in content and "intermediate-term memory" in content:
        if "## Abstract" in content:
            abstract = content.split("## Abstract")[1].split("## Full Text")[0] if "## Full Text" in content else ""
            if "high-fat" not in abstract.lower() and "hfd" not in abstract.lower() and "diet" not in abstract.lower():
                if "autophagy" not in abstract.lower():
                    issues.append("HFD/autophagy paper replacing original content")
    
    return issues

def main():
    publications_dir = Path("publications")
    
    if not publications_dir.exists():
        print("Publications directory not found!")
        return
    
    problem_pmids = []
    
    # Get all .md files
    md_files = sorted(publications_dir.glob("*.md"))
    
    print(f"Checking {len(md_files)} publication files...")
    print("=" * 60)
    
    for i, filepath in enumerate(md_files):
        if i % 100 == 0:
            print(f"Progress: {i}/{len(md_files)}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pmid = filepath.stem
            
            # Check if full text is available
            if "full_text_available: false" in content or "## Full Text" not in content:
                continue
            
            issues = check_known_problematic_content(content)
            
            if issues:
                for issue in issues:
                    problem_pmids.append((pmid, issue))
                    print(f"❌ {pmid}: {issue}")
        
        except Exception as e:
            problem_pmids.append((filepath.stem, f"Error reading file: {e}"))
    
    print("=" * 60)
    print(f"\nFound {len(problem_pmids)} problematic files out of {len(md_files)} total files")
    
    # Write results to file
    with open("PROBLEM_PMIDS.md", "w") as f:
        f.write("# Problematic Publication Files\n\n")
        f.write(f"Found {len(problem_pmids)} files with HTML scraping issues out of {len(md_files)} total files.\n\n")
        
        if problem_pmids:
            # Group by issue type
            issue_groups = {}
            for pmid, issue in problem_pmids:
                if issue not in issue_groups:
                    issue_groups[issue] = []
                issue_groups[issue].append(pmid)
            
            f.write("## Issues Found\n\n")
            
            for issue, pmids in issue_groups.items():
                f.write(f"### {issue}\n\n")
                f.write(f"Found in {len(pmids)} files:\n\n")
                for pmid in sorted(pmids):
                    f.write(f"- {pmid}\n")
                f.write("\n")
    
    print(f"\nResults written to PROBLEM_PMIDS.md")

if __name__ == "__main__":
    main()