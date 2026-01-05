#!/usr/bin/env python3
"""
Check publication files for potential HTML scraping issues by comparing abstract to full text.
"""

import os
import re
from pathlib import Path

def extract_abstract_keywords(content):
    """Extract key terms from the abstract section."""
    abstract_match = re.search(r'## Abstract\s*\n(.*?)(?=\n## Full Text|\Z)', content, re.DOTALL)
    if not abstract_match:
        return set()
    
    abstract_text = abstract_match.group(1).lower()
    
    # Extract key scientific terms
    keywords = set()
    
    # Species names
    species = re.findall(r'\b(?:drosophila|mouse|mice|human|rat|xenopus|aplysia|gryllus|cricket|mosquito|ant)\b', abstract_text)
    keywords.update(species)
    
    # Gene/protein names
    genes = re.findall(r'\b(?:dscam\d*|beat|side|toll|netrin|pak\d*|dock|slit|robo|ephrin|semaphorin)\b', abstract_text)
    keywords.update(genes)
    
    # Anatomical terms
    anatomy = re.findall(r'\b(?:mushroom bod|antennal lobe|olfactory|retina|cortex|hippocampus|ganglion|axon|dendrite|neuron|synapse)\b', abstract_text)
    keywords.update(anatomy)
    
    # Extract year from abstract
    year_match = re.search(r'\b(19\d{2}|20\d{2})\b', abstract_text)
    if year_match:
        keywords.add(year_match.group(1))
    
    return keywords

def extract_fulltext_keywords(content):
    """Extract key terms from the full text section."""
    fulltext_match = re.search(r'## Full Text\s*\n(.*)', content, re.DOTALL)
    if not fulltext_match:
        return set()
    
    # Just check first 2000 chars of full text
    fulltext = fulltext_match.group(1)[:2000].lower()
    
    keywords = set()
    
    # Species names
    species = re.findall(r'\b(?:drosophila|mouse|mice|human|rat|xenopus|aplysia|gryllus|cricket|mosquito|ant)\b', fulltext)
    keywords.update(species)
    
    # Gene/protein names
    genes = re.findall(r'\b(?:dscam\d*|beat|side|toll|netrin|pak\d*|dock|slit|robo|ephrin|semaphorin)\b', fulltext)
    keywords.update(genes)
    
    # Anatomical terms
    anatomy = re.findall(r'\b(?:mushroom bod|antennal lobe|olfactory|retina|cortex|hippocampus|ganglion|axon|dendrite|neuron|synapse)\b', fulltext)
    keywords.update(anatomy)
    
    return keywords

def check_for_generic_review(content):
    """Check if the full text is the generic Dscam review."""
    return "Dscam-mediated homeostatic mechanisms" in content

def check_for_beat_side(content):
    """Check if the full text is the Beat/Side paper."""
    return "Beat/Side proteins play in olfactory circuit assembly" in content

def check_for_cricket(content):
    """Check if the full text is about crickets."""
    return "Gryllus bimaculatus" in content and "prothoracic ganglion" in content

def check_publication(filepath):
    """Check if a publication file has potential scraping issues."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pmid = filepath.stem
        
        # Quick checks for known problematic patterns
        if check_for_generic_review(content):
            abstract_keywords = extract_abstract_keywords(content)
            if not ("homeostatic" in abstract_keywords or "plasticity" in abstract_keywords):
                return pmid, "Generic Dscam homeostatic review replacing original content"
        
        if check_for_beat_side(content):
            abstract_keywords = extract_abstract_keywords(content)
            if not ("beat" in abstract_keywords or "side" in abstract_keywords):
                return pmid, "Beat/Side protein paper replacing original content"
        
        if check_for_cricket(content):
            abstract_keywords = extract_abstract_keywords(content)
            if not ("cricket" in abstract_keywords or "gryllus" in abstract_keywords):
                return pmid, "Cricket neuroplasticity paper replacing original content"
        
        # Compare abstract and full text keywords
        abstract_keywords = extract_abstract_keywords(content)
        fulltext_keywords = extract_fulltext_keywords(content)
        
        if len(abstract_keywords) > 3 and len(fulltext_keywords) > 3:
            # Calculate overlap
            overlap = abstract_keywords & fulltext_keywords
            if len(overlap) < len(abstract_keywords) * 0.3:  # Less than 30% overlap
                return pmid, f"Low keyword overlap: Abstract has {abstract_keywords - fulltext_keywords}, Full text has {fulltext_keywords - abstract_keywords}"
        
        return None, None
        
    except Exception as e:
        return filepath.stem, f"Error reading file: {e}"

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
        if i % 50 == 0:
            print(f"Progress: {i}/{len(md_files)}")
        
        pmid, issue = check_publication(filepath)
        if pmid:
            problem_pmids.append((pmid, issue))
            print(f"❌ {pmid}: {issue}")
    
    print("=" * 60)
    print(f"\nFound {len(problem_pmids)} problematic files out of {len(md_files)} total files")
    
    # Write detailed results
    with open("PROBLEM_PMIDS_DETAILED.md", "w") as f:
        f.write("# Problematic Publication Files - Detailed Analysis\n\n")
        f.write(f"Found {len(problem_pmids)} files with potential HTML scraping issues out of {len(md_files)} total files.\n\n")
        
        if problem_pmids:
            # Group by issue type
            generic_review = []
            beat_side = []
            cricket = []
            other = []
            
            for pmid, issue in problem_pmids:
                if "Generic Dscam" in issue:
                    generic_review.append(pmid)
                elif "Beat/Side" in issue:
                    beat_side.append(pmid)
                elif "Cricket" in issue:
                    cricket.append(pmid)
                else:
                    other.append((pmid, issue))
            
            if generic_review:
                f.write("## Files with Generic Dscam Review Content\n\n")
                for pmid in generic_review:
                    f.write(f"- {pmid}\n")
                f.write("\n")
            
            if beat_side:
                f.write("## Files with Beat/Side Protein Content\n\n")
                for pmid in beat_side:
                    f.write(f"- {pmid}\n")
                f.write("\n")
            
            if cricket:
                f.write("## Files with Cricket Neuroplasticity Content\n\n")
                for pmid in cricket:
                    f.write(f"- {pmid}\n")
                f.write("\n")
            
            if other:
                f.write("## Other Issues\n\n")
                f.write("| PMID | Issue |\n")
                f.write("|------|-------|\n")
                for pmid, issue in other:
                    f.write(f"| {pmid} | {issue} |\n")
    
    print(f"\nDetailed results written to PROBLEM_PMIDS_DETAILED.md")

if __name__ == "__main__":
    main()