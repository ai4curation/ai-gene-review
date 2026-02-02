#!/usr/bin/env python3
"""
Fix deep research references using surgical string manipulation.
Adds supported_by reference to the first ACCEPT annotation in existing_annotations.
"""

import re
from pathlib import Path


def find_deep_research_file(gene_dir: Path) -> str | None:
    """Find the deep research file in a gene directory."""
    patterns = ['deep-research', 'falcon-research', 'perplexity-research', 'research']
    for f in gene_dir.iterdir():
        if f.is_file() and f.suffix == '.md':
            for pattern in patterns:
                if pattern in f.name.lower():
                    return f.name
    return None


def get_species_gene_from_path(yaml_path: Path) -> tuple[str, str]:
    """Extract species and gene from path."""
    parts = yaml_path.parts
    for i, p in enumerate(parts):
        if p == 'genes' and i + 2 < len(parts):
            return parts[i+1], parts[i+2]
    return None, None


def add_reference_to_file(yaml_path: Path, dry_run: bool = False) -> bool:
    """Add deep research reference to the first ACCEPT annotation."""
    gene_dir = yaml_path.parent
    deep_research_file = find_deep_research_file(gene_dir)

    if not deep_research_file:
        return False

    species, gene = get_species_gene_from_path(yaml_path)
    if not species or not gene:
        return False

    file_ref = f"file:{species}/{gene}/{deep_research_file}"

    content = yaml_path.read_text()

    # Check if file reference already exists in existing_annotations section
    # Split content into before and after existing_annotations
    if 'existing_annotations:' not in content:
        return False

    # Find existing_annotations section and check for file refs there
    ea_start = content.find('existing_annotations:')
    ea_section = content[ea_start:]

    # Find end of existing_annotations (next top-level key)
    next_section = re.search(r'\n[a-z_]+:', ea_section[20:])
    if next_section:
        ea_section = ea_section[:20 + next_section.start()]

    # Check if file ref already in existing_annotations
    if file_ref in ea_section or f"file:{species}/{gene}/" in ea_section and "research" in ea_section:
        return False

    # Find first "action: ACCEPT" or "action: NEW" in existing_annotations
    accept_pattern = re.compile(r'(\s+action:\s+(?:ACCEPT|NEW))\n')
    match = accept_pattern.search(ea_section)

    if not match:
        # No ACCEPT or NEW annotations found
        return False

    # Position in the full content
    insert_pos = ea_start + match.end()

    # Build the supported_by block to insert
    # First, check if there's already a supported_by section for this annotation
    next_term_pos = content.find('- term:', insert_pos)
    if next_term_pos == -1:
        next_term_pos = len(content)

    section_after_action = content[insert_pos:next_term_pos]

    if 'supported_by:' in section_after_action:
        # Find the supported_by section and add to it
        sb_pos = content.find('supported_by:', insert_pos)
        if sb_pos < next_term_pos:
            # Find the first item in supported_by
            first_item = content.find('- reference_id:', sb_pos)
            if first_item != -1 and first_item < next_term_pos:
                # Add new entry before the first item
                indent = "      "  # Standard indent for supported_by items
                new_entry = f"{indent}- reference_id: {file_ref}\n{indent}  supporting_text: See deep research file for comprehensive analysis\n"
                new_content = content[:first_item] + new_entry + content[first_item:]
            else:
                # Empty supported_by, add after it
                insert_at = content.find('\n', sb_pos) + 1
                indent = "      "
                new_entry = f"{indent}- reference_id: {file_ref}\n{indent}  supporting_text: See deep research file for comprehensive analysis\n"
                new_content = content[:insert_at] + new_entry + content[insert_at:]
        else:
            return False
    else:
        # No supported_by section, add one
        indent = "    "  # Standard indent for review fields
        new_block = f"{indent}supported_by:\n{indent}  - reference_id: {file_ref}\n{indent}    supporting_text: See deep research file for comprehensive analysis\n"
        new_content = content[:insert_pos] + new_block + content[insert_pos:]

    if dry_run:
        print(f"  Would add reference at position {insert_pos}")
        return True

    yaml_path.write_text(new_content)
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fix deep research references')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of files')
    args = parser.parse_args()

    genes_dir = Path('genes')
    yaml_files = list(genes_dir.rglob('*-ai-review.yaml'))

    fixed = 0

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

        content = yaml_path.read_text()

        # More precise check - look for file refs specifically in existing_annotations
        ea_start = content.find('existing_annotations:')
        if ea_start == -1:
            continue

        # Find the next top-level section
        next_section = re.search(r'\n[a-z_]+:', content[ea_start + 20:])
        if next_section:
            ea_end = ea_start + 20 + next_section.start()
        else:
            ea_end = len(content)

        ea_section = content[ea_start:ea_end]

        # Check if any file: reference with research exists in ea_section
        if re.search(r'reference_id:\s*file:[^\n]*research[^\n]*\.md', ea_section):
            continue

        print(f"Processing: {yaml_path}")
        if add_reference_to_file(yaml_path, dry_run=args.dry_run):
            fixed += 1
            print(f"  {'Would fix' if args.dry_run else 'Fixed'}")

    print(f"\n{'Would fix' if args.dry_run else 'Fixed'}: {fixed} files")


if __name__ == '__main__':
    main()
