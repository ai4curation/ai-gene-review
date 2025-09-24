#!/usr/bin/env python3
"""Refresh PMID titles in gene review YAML files.

This script looks for references with 'TODO: Fetch title' and replaces them
with actual titles from cached publication files.
"""

import logging
import re
import sys
from pathlib import Path
from typing import Dict, Optional

import click
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def extract_title_from_publication(pmid: str, publications_dir: Path) -> Optional[str]:
    """Extract title from cached publication file."""
    pub_file = publications_dir / f"PMID_{pmid}.md"

    if not pub_file.exists():
        logger.warning(f"Publication file not found: {pub_file}")
        return None

    try:
        content = pub_file.read_text()

        # Try to extract title from markdown format
        # Usually appears as # Title or **Title:** format
        title_patterns = [
            r'^#\s+(.+?)(?:\n|$)',  # Markdown header
            r'\*\*Title:\*\*\s*(.+?)(?:\n|$)',  # Bold title field
            r'^Title:\s*(.+?)(?:\n|$)',  # Plain title field
            r'^(.+?)(?:\n\n|\n$)',  # First line (fallback)
        ]

        for pattern in title_patterns:
            match = re.search(pattern, content, re.MULTILINE)
            if match:
                title = match.group(1).strip()
                # Clean up the title
                title = title.replace('**', '').strip()
                if title and not title.startswith('PMID'):
                    return title

        logger.warning(f"Could not extract title from {pub_file}")
        return None

    except Exception as e:
        logger.error(f"Error reading {pub_file}: {e}")
        return None


def refresh_pmid_titles(yaml_file: Path, publications_dir: Path, dry_run: bool = False) -> int:
    """Refresh PMID titles in a gene review YAML file.

    Returns the number of titles updated.
    """
    if not yaml_file.exists():
        logger.error(f"YAML file not found: {yaml_file}")
        return 0

    logger.info(f"Processing {yaml_file}")

    try:
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading YAML from {yaml_file}: {e}")
        return 0

    if not data or 'references' not in data:
        logger.warning(f"No references found in {yaml_file}")
        return 0

    updated_count = 0
    references = data.get('references', [])

    for ref in references:
        if not isinstance(ref, dict):
            continue

        title = ref.get('title', '')
        pmid = ref.get('id', '')

        # Check if title needs updating
        if title and title.startswith('TODO'):
            # Extract PMID number
            pmid_match = re.search(r'PMID:(\d+)', pmid)
            if not pmid_match:
                logger.warning(f"Could not extract PMID from: {pmid}")
                continue

            pmid_num = pmid_match.group(1)
            new_title = extract_title_from_publication(pmid_num, publications_dir)

            if new_title:
                logger.info(f"  Updating PMID:{pmid_num}: {new_title[:50]}...")
                ref['title'] = new_title
                updated_count += 1
            else:
                logger.warning(f"  Could not find title for PMID:{pmid_num}")

    if updated_count > 0 and not dry_run:
        # Write back the updated YAML
        try:
            with open(yaml_file, 'w') as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            logger.info(f"✅ Updated {updated_count} titles in {yaml_file}")
        except Exception as e:
            logger.error(f"Error writing YAML to {yaml_file}: {e}")
            return 0
    elif dry_run:
        logger.info(f"[DRY RUN] Would update {updated_count} titles in {yaml_file}")
    else:
        logger.info(f"No titles needed updating in {yaml_file}")

    return updated_count


@click.command()
@click.argument('yaml_files', nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option('--publications-dir',
              type=click.Path(exists=True, path_type=Path),
              default='publications',
              help='Directory containing cached publication files')
@click.option('--all-genes', is_flag=True,
              help='Process all gene review files in the genes/ directory')
@click.option('--dry-run', is_flag=True,
              help='Show what would be updated without making changes')
def main(yaml_files, publications_dir, all_genes, dry_run):
    """Refresh PMID titles in gene review YAML files.

    This script looks for references with 'TODO: Fetch title' and replaces them
    with actual titles from cached publication files.
    """
    publications_dir = Path(publications_dir)

    if not publications_dir.exists():
        logger.error(f"Publications directory not found: {publications_dir}")
        sys.exit(1)

    files_to_process = []

    if all_genes:
        # Find all gene review YAML files
        genes_dir = Path('genes')
        if genes_dir.exists():
            files_to_process = list(genes_dir.glob('*/*/*-ai-review.yaml'))
            logger.info(f"Found {len(files_to_process)} gene review files")
        else:
            logger.error("genes/ directory not found")
            sys.exit(1)
    elif yaml_files:
        files_to_process = list(yaml_files)
    else:
        logger.error("No files specified. Use --all-genes or provide file paths")
        sys.exit(1)

    total_updated = 0
    files_updated = 0

    for yaml_file in files_to_process:
        count = refresh_pmid_titles(yaml_file, publications_dir, dry_run)
        if count > 0:
            total_updated += count
            files_updated += 1

    if dry_run:
        logger.info(f"[DRY RUN] Would update {total_updated} titles across {files_updated} files")
    else:
        logger.info(f"✅ Updated {total_updated} titles across {files_updated} files")


if __name__ == '__main__':
    main()