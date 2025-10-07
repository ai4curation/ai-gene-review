#!/usr/bin/env python3
"""Validate that all PMID citations in markdown files are present in the corresponding review YAML."""
import re
import sys
import yaml
from pathlib import Path
from typing import Set, List, Tuple, Optional

def extract_pmids_from_markdown(content: str) -> Tuple[Set[str], Set[str]]:
    """
    Extract all PMIDs from markdown content and identify invalid ones.
    
    Looks for patterns like:
    - [PMID:12345]
    - [PMID:12345, "text"]
    - PMID:12345 (without brackets)
    
    Also catches invalid PMIDs like:
    - PMID:xxx8232552
    - PMID:abc123
    
    Returns:
        Tuple of (valid_pmids, invalid_pmids)
        valid_pmids: Set of valid PMID strings (e.g., {"PMID:12345", "PMID:67890"})
        invalid_pmids: Set of invalid PMID strings (e.g., {"PMID:xxx8232552"})
    """
    valid_pmids = set()
    invalid_pmids = set()
    
    # Pattern to find all PMID references (valid or invalid)
    # This catches PMID: followed by any non-whitespace characters
    all_pmid_pattern = r'PMID:([^\s,\]]+)'
    
    for match in re.finditer(all_pmid_pattern, content):
        pmid_value = match.group(1)
        full_pmid = f"PMID:{pmid_value}"
        
        # Check if the PMID value is all digits (valid)
        if pmid_value.isdigit():
            valid_pmids.add(full_pmid)
        else:
            # Remove trailing punctuation if present
            cleaned_value = pmid_value.rstrip('.,;:)')
            if cleaned_value.isdigit():
                valid_pmids.add(f"PMID:{cleaned_value}")
            else:
                invalid_pmids.add(full_pmid)
    
    return valid_pmids, invalid_pmids

def extract_pmids_from_yaml(yaml_path: Path) -> Set[str]:
    """
    Extract all PMIDs from the references section of a review YAML file.
    
    Returns:
        Set of PMID strings from the references
    """
    pmids: set[str] = set()
    
    if not yaml_path.exists():
        return pmids
    
    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        
        if data and 'references' in data:
            for ref in data['references']:
                if 'id' in ref and ref['id'].startswith('PMID:'):
                    pmids.add(ref['id'])
    except Exception as e:
        print(f"Warning: Could not parse YAML file {yaml_path}: {e}")
    
    return pmids

def find_review_yaml(markdown_path: Path) -> Optional[Path]:
    """
    Find the corresponding review YAML file for a markdown file.
    
    For a file like genes/human/JAK1/JAK1-pathway.md,
    looks for genes/human/JAK1/JAK1-ai-review.yaml
    """
    # Get the gene directory
    gene_dir = markdown_path.parent
    
    # Look for *-ai-review.yaml files in the same directory
    review_files = list(gene_dir.glob("*-ai-review.yaml"))
    
    if review_files:
        return review_files[0]  # Return the first match
    
    return None

def validate_pmid_references(markdown_path: Path) -> Tuple[bool, List[str], List[str], List[str]]:
    """
    Validate that all PMIDs in a markdown file are present in the corresponding review YAML.
    
    Returns:
        Tuple of (is_valid, missing_pmids, invalid_pmids, extra_info_messages)
    """
    if not markdown_path.exists():
        return False, [], [], [f"File not found: {markdown_path}"]
    
    # Find corresponding review YAML
    review_yaml = find_review_yaml(markdown_path)
    if not review_yaml:
        return False, [], [], [f"No review YAML found for {markdown_path}"]
    
    # Extract PMIDs from both files
    try:
        md_content = markdown_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        # Try with a more permissive encoding
        try:
            md_content = markdown_path.read_text(encoding='latin-1')
        except Exception as e:
            return False, [], [], [f"Could not read file: {e}"]
    valid_md_pmids, invalid_md_pmids = extract_pmids_from_markdown(md_content)
    yaml_pmids = extract_pmids_from_yaml(review_yaml)
    
    # Find missing PMIDs (in markdown but not in YAML)
    missing_pmids = valid_md_pmids - yaml_pmids
    
    # Info about what was found
    info = []
    if invalid_md_pmids:
        info.append(f"Found {len(invalid_md_pmids)} INVALID PMIDs in markdown")
    info.append(f"Found {len(valid_md_pmids)} valid PMIDs in markdown")
    info.append(f"Found {len(yaml_pmids)} PMIDs in review YAML")
    
    if missing_pmids:
        info.append(f"Missing from review: {', '.join(sorted(missing_pmids))}")
    
    # Invalid if there are invalid PMIDs OR missing PMIDs
    is_valid = len(invalid_md_pmids) == 0 and len(missing_pmids) == 0
    
    return is_valid, list(missing_pmids), list(invalid_md_pmids), info

def validate_file(file_path: Path, verbose: bool = True) -> bool:
    """Validate a single markdown file."""
    if verbose:
        print(f"\nValidating {file_path}:")

    is_valid, missing_pmids, invalid_pmids, info = validate_pmid_references(file_path)

    if verbose:
        for msg in info:
            print(f"  {msg}")

    if is_valid:
        if verbose:
            print(f"  ✅ All PMID citations are valid and present in the review file")
        return True
    else:
        error_found = False

        if invalid_pmids:
            error_found = True
            if verbose:
                print(f"  ❌ Invalid PMID format(s) found:")
                for pmid in sorted(invalid_pmids):
                    print(f"    - {pmid} (PMIDs must contain only digits)")
                print(f"  Please fix the PMID format - PMIDs should only contain numbers.")

        if missing_pmids:
            error_found = True
            if verbose:
                print(f"  ❌ Missing PMIDs in review file:")
                for pmid in sorted(missing_pmids):
                    print(f"    - {pmid}")
                print(f"  These PMIDs are cited in the markdown but not found in the references section of the review YAML.")
                print(f"  Please add them to the review file or remove the citations.")

        return False

def validate_directory(dir_path: Path) -> bool:
    """Validate all pathway markdown files in a directory."""
    # Only validate *-pathway.md files
    md_files = list(dir_path.rglob("*-pathway.md"))

    if not md_files:
        print(f"No pathway markdown files found in {dir_path}")
        return True

    print(f"Checking {len(md_files)} pathway markdown files for PMID references...")

    # Filter to only files that contain PMID references
    files_with_pmids = []
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            # Try with a more permissive encoding
            try:
                content = md_file.read_text(encoding='latin-1')
            except Exception as e:
                print(f"  Warning: Could not read {md_file}: {e}")
                continue
        if 'PMID:' in content:
            files_with_pmids.append(md_file)

    if not files_with_pmids:
        print("No pathway files with PMID references found")
        return True

    print(f"Validating {len(files_with_pmids)} pathway files with PMID references...")

    all_valid = True
    invalid_files = []

    for md_file in files_with_pmids:
        # Use quiet mode for files that pass
        if not validate_file(md_file, verbose=False):
            all_valid = False
            invalid_files.append(md_file)

    if all_valid:
        print(f"✅ All {len(files_with_pmids)} pathway files have valid PMID references")
    else:
        print(f"\n❌ {len(invalid_files)} pathway file(s) have PMID issues:")
        # Now show details only for the invalid files
        for md_file in invalid_files:
            validate_file(md_file, verbose=True)
        print(f"\n{'='*60}")
        print(f"❌ {len(invalid_files)} file(s) have missing PMID references in their review files")
        print(f"   Please update the review YAML files to include all cited PMIDs")

    return all_valid

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python validate_pmid_references.py <pathway_file_or_directory>")
        print("\nExamples:")
        print("  python validate_pmid_references.py genes/human/JAK1/JAK1-pathway.md")
        print("  python validate_pmid_references.py genes/human/")
        print("  python validate_pmid_references.py genes/")
        print("\nThis tool validates PMID citations in *-pathway.md files only.")
        print("It checks that:")
        print("  1. All PMIDs have valid format (only digits)")
        print("  2. All cited PMIDs are present in the corresponding *-ai-review.yaml file")
        print("\nNote: *-notes.md and other markdown files are NOT validated (they can be freeform)")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if path.is_file():
        # Single file validation - only validate if it's a pathway file
        if not path.name.endswith('-pathway.md'):
            print(f"Skipping {path.name} - only *-pathway.md files are validated")
            print("(Notes and other markdown files can have freeform content)")
            sys.exit(0)
        success = validate_file(path)
        sys.exit(0 if success else 1)
    elif path.is_dir():
        success = validate_directory(path)
        sys.exit(0 if success else 1)
    else:
        print(f"Error: {path} is not a file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()