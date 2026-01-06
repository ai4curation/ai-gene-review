#!/usr/bin/env python3
"""
Add deep research file references to existing_annotations.

This script finds genes where deep research files exist but are not
referenced in existing_annotations, and adds a supported_by reference
to the first annotation that has action: ACCEPT or NEW.
"""

import os
import re
import sys
from pathlib import Path
import yaml

# Custom YAML handling to preserve formatting
class QuotedString(str):
    pass

def quoted_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

yaml.add_representer(QuotedString, quoted_presenter)

def find_deep_research_file(gene_dir: Path) -> str | None:
    """Find the deep research file in a gene directory."""
    # Look for various research file patterns
    patterns = ['deep-research', 'falcon-research', 'perplexity-research', 'research']
    for f in gene_dir.iterdir():
        if f.is_file() and f.suffix == '.md':
            for pattern in patterns:
                if pattern in f.name.lower():
                    return f.name
    return None

def get_species_gene_from_path(yaml_path: Path) -> tuple[str, str]:
    """Extract species and gene from path like genes/BACSU/sigG/sigG-ai-review.yaml"""
    parts = yaml_path.parts
    # Find 'genes' in path and get next two parts
    for i, p in enumerate(parts):
        if p == 'genes' and i + 2 < len(parts):
            return parts[i+1], parts[i+2]
    return None, None

def build_file_ref(species: str, gene: str, filename: str) -> str:
    """Build the file reference string."""
    return f"file:{species}/{gene}/{filename}"

def has_deep_research_ref(data: dict, file_ref: str) -> bool:
    """Check if any annotation references the deep research file."""
    annotations = data.get('existing_annotations', [])
    for ann in annotations:
        review = ann.get('review', {})
        supported_by = review.get('supported_by', [])
        for support in supported_by:
            ref_id = support.get('reference_id', '')
            if file_ref in ref_id or (species_gene_part := file_ref.split('/')[-1]) in ref_id:
                return True

    # Also check core_functions
    core_functions = data.get('core_functions', [])
    for cf in core_functions:
        supported_by = cf.get('supported_by', [])
        for support in supported_by:
            ref_id = support.get('reference_id', '')
            if file_ref in ref_id:
                return True

    return False

def add_deep_research_ref(yaml_path: Path, dry_run: bool = False) -> bool:
    """Add deep research reference to the first suitable annotation."""
    gene_dir = yaml_path.parent
    deep_research_file = find_deep_research_file(gene_dir)

    if not deep_research_file:
        return False

    species, gene = get_species_gene_from_path(yaml_path)
    if not species or not gene:
        print(f"  Could not parse path: {yaml_path}")
        return False

    file_ref = build_file_ref(species, gene, deep_research_file)

    # Read the YAML file
    with open(yaml_path, 'r') as f:
        content = f.read()

    # Check if already references deep research
    if file_ref in content or deep_research_file in content:
        return False

    # Parse YAML
    data = yaml.safe_load(content)
    if not data:
        return False

    annotations = data.get('existing_annotations', [])
    if not annotations:
        return False

    # Find first annotation with ACCEPT or NEW action to add reference
    target_idx = None
    for i, ann in enumerate(annotations):
        review = ann.get('review', {})
        action = review.get('action', '')
        if action in ('ACCEPT', 'NEW'):
            target_idx = i
            break

    if target_idx is None:
        # Fall back to first annotation
        target_idx = 0

    if dry_run:
        print(f"  Would add {file_ref} to annotation {target_idx}")
        return True

    # Add the reference using regex to preserve YAML formatting
    # Find the annotation and add supported_by if missing, or append to it

    # Strategy: Find the review section of the target annotation and add supported_by
    # This is complex with raw string manipulation, so let's use a simpler approach:
    # Add a comment and the reference at the end of the review section

    ann = annotations[target_idx]
    review = ann.get('review', {})

    if 'supported_by' not in review:
        review['supported_by'] = []

    # Add the deep research reference
    review['supported_by'].append({
        'reference_id': file_ref,
        'supporting_text': 'See deep research file for comprehensive analysis'
    })

    # Update the data
    annotations[target_idx]['review'] = review
    data['existing_annotations'] = annotations

    # Also ensure the reference is in the references section
    references = data.get('references', [])
    ref_exists = any(r.get('id') == file_ref for r in references)
    if not ref_exists:
        # Check if a similar reference exists
        deep_research_refs = [r for r in references if 'deep-research' in r.get('id', '')]
        if not deep_research_refs:
            references.append({
                'id': file_ref,
                'title': f'Deep research on {gene} function',
                'findings': []
            })
            data['references'] = references

    # Write back
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)

    return True

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Add deep research references to annotations')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of files to process')
    args = parser.parse_args()

    genes_dir = Path('genes')
    if not genes_dir.exists():
        print("Error: genes directory not found")
        sys.exit(1)

    # Find all ai-review.yaml files
    yaml_files = list(genes_dir.rglob('*-ai-review.yaml'))

    fixed = 0
    skipped = 0

    for yaml_path in yaml_files:
        if args.limit and fixed >= args.limit:
            break

        gene_dir = yaml_path.parent
        deep_research_file = find_deep_research_file(gene_dir)

        if not deep_research_file:
            continue

        species, gene = get_species_gene_from_path(yaml_path)
        if not species or not gene:
            continue

        # Check if this file needs fixing - look for the full reference pattern
        with open(yaml_path, 'r') as f:
            content = f.read()

        file_ref = f"file:{species}/{gene}/{deep_research_file}"
        # Check for the actual file reference pattern, not just the filename
        if file_ref in content:
            skipped += 1
            continue

        print(f"Processing: {yaml_path}")
        if add_deep_research_ref(yaml_path, dry_run=args.dry_run):
            fixed += 1
            print(f"  {'Would fix' if args.dry_run else 'Fixed'}: {yaml_path.name}")

    print(f"\n{'Would fix' if args.dry_run else 'Fixed'}: {fixed} files")
    print(f"Already OK: {skipped} files")

if __name__ == '__main__':
    main()
