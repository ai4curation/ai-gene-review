#!/usr/bin/env python3
"""Mark annotations not in GOA as retired."""

import logging
import sys
from pathlib import Path
from typing import Set, Tuple

import click
import pandas as pd
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def load_goa_annotations(goa_file: Path) -> Set[Tuple[str, str, str]]:
    """Load GOA annotations and return a set of (term_id, evidence_type, pmid) tuples."""
    if not goa_file.exists():
        logger.error(f"GOA file not found: {goa_file}")
        return set()

    try:
        df = pd.read_csv(goa_file, sep='\t', comment='!')

        # Extract GO term ID, evidence code, and reference
        annotations = set()
        for _, row in df.iterrows():
            # Try different column name variants
            go_id = row.get('GO TERM', row.get('GO_ID', row.get('go_id', '')))
            evidence = row.get('GO EVIDENCE CODE', row.get('Evidence', row.get('evidence_code', '')))
            ref = row.get('REFERENCE', row.get('DB:Reference', row.get('reference', '')))

            if go_id and evidence:
                # Clean up reference - extract PMID if present
                if 'PMID:' in str(ref):
                    pmid = ref.split('|')[0] if '|' in ref else ref
                else:
                    pmid = ref
                annotations.add((go_id, evidence, str(pmid)))

        return annotations
    except Exception as e:
        logger.error(f"Error loading GOA file {goa_file}: {e}")
        return set()


def fix_retired_annotations(yaml_file: Path, dry_run: bool = False) -> int:
    """Mark annotations not in GOA as retired.

    Returns the number of annotations marked as retired.
    """
    if not yaml_file.exists():
        logger.error(f"YAML file not found: {yaml_file}")
        return 0

    # Find corresponding GOA file
    gene_dir = yaml_file.parent
    gene_name = gene_dir.name
    goa_file = gene_dir / f"{gene_name}-goa.tsv"

    if not goa_file.exists():
        logger.warning(f"GOA file not found: {goa_file}")
        return 0

    logger.info(f"Processing {yaml_file}")

    # Load GOA annotations
    goa_annotations = load_goa_annotations(goa_file)
    if not goa_annotations:
        logger.warning(f"No annotations found in GOA file: {goa_file}")
        return 0

    # Load YAML
    try:
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading YAML from {yaml_file}: {e}")
        return 0

    if not data or 'existing_annotations' not in data:
        logger.warning(f"No existing_annotations found in {yaml_file}")
        return 0

    retired_count = 0
    existing_annotations = data.get('existing_annotations', [])

    for annotation in existing_annotations:
        if not isinstance(annotation, dict):
            continue

        # Skip if already retired
        if annotation.get('retired'):
            continue

        term = annotation.get('term', {})
        go_id = term.get('id', '')
        evidence = annotation.get('evidence_type', '')
        ref = annotation.get('original_reference_id', '')

        # Clean up reference
        if 'PMID:' in str(ref):
            pass
        else:
            pass

        # Check if annotation exists in GOA
        found_in_goa = False
        for goa_go, goa_ev, goa_ref in goa_annotations:
            if go_id == goa_go:
                # Check if evidence matches (or is similar)
                if evidence == goa_ev or \
                   (evidence in ['IDA', 'IMP', 'IGI', 'IPI'] and goa_ev in ['IDA', 'IMP', 'IGI', 'IPI']):
                    found_in_goa = True
                    break

        if not found_in_goa and evidence not in ['IEA', 'ISS', 'ISO', 'IBA']:
            # Mark as retired if it's an experimental annotation not in GOA
            logger.info(f"  Marking as retired: {go_id} ({term.get('label', '')}) - {evidence} - {ref}")
            annotation['retired'] = True
            retired_count += 1

    if retired_count > 0 and not dry_run:
        # Write back the updated YAML
        try:
            with open(yaml_file, 'w') as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            logger.info(f"✅ Marked {retired_count} annotations as retired in {yaml_file}")
        except Exception as e:
            logger.error(f"Error writing YAML to {yaml_file}: {e}")
            return 0
    elif dry_run:
        logger.info(f"[DRY RUN] Would mark {retired_count} annotations as retired in {yaml_file}")
    else:
        logger.info(f"No annotations need to be marked as retired in {yaml_file}")

    return retired_count


@click.command()
@click.argument('yaml_files', nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option('--all-genes', is_flag=True,
              help='Process all gene review files in the genes/ directory')
@click.option('--dry-run', is_flag=True,
              help='Show what would be updated without making changes')
def main(yaml_files, all_genes, dry_run):
    """Mark annotations not in GOA as retired in gene review YAML files."""

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
        # Process only files with validation errors
        error_files = [
            'genes/mouse/Ctnnb1/Ctnnb1-ai-review.yaml',
            'genes/human/TRAF6/TRAF6-ai-review.yaml',
            'genes/human/JAK1/JAK1-ai-review.yaml'
        ]
        files_to_process = [Path(f) for f in error_files if Path(f).exists()]
        logger.info(f"Processing files with known GOA errors: {len(files_to_process)} files")

    total_retired = 0
    files_updated = 0

    for yaml_file in files_to_process:
        count = fix_retired_annotations(yaml_file, dry_run)
        if count > 0:
            total_retired += count
            files_updated += 1

    if dry_run:
        logger.info(f"[DRY RUN] Would mark {total_retired} annotations as retired across {files_updated} files")
    else:
        logger.info(f"✅ Marked {total_retired} annotations as retired across {files_updated} files")


if __name__ == '__main__':
    main()