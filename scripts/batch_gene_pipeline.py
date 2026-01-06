#!/usr/bin/env python3
"""Batch gene pipeline: fetch genes and run deep research.

This script processes a file of gene information, fetches gene data,
and runs specified deep research providers for each gene.

Input file format (CSV or TSV):
    organism,gene
    organism,gene,uniprot_id
    organism,gene,uniprot_id,alias

Examples:
    human,TP53
    human,BRCA1,P38398
    METEA,C5B1I4,,mllA
    9BACT,F0JBF1,,HgcB
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple


def parse_gene_file(file_path: Path) -> List[Tuple[str, str, Optional[str], Optional[str]]]:
    """Parse gene file and return list of (organism, gene, uniprot_id, alias) tuples.

    Supports two formats:
    1. organism,gene[,uniprot_id][,alias]
       Example: human,TP53
       Example: METEA,C5B1I4,,mllA

    2. organism,uniprot_id,gene_symbol (detected when column 1 looks like UniProt ID)
       Example: human,P15941,MUC1
       This is converted to: organism=human, gene=P15941, alias=MUC1

    Args:
        file_path: Path to input file

    Returns:
        List of tuples: (organism, gene, uniprot_id, alias)
        uniprot_id and alias may be None
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    def looks_like_uniprot_id(s: str) -> bool:
        """Check if string looks like a UniProt accession (e.g., P15941, Q9Y6A1)."""
        import re
        # UniProt IDs are typically 6-10 alphanumeric characters, starting with letter
        return bool(re.match(r'^[A-Z][0-9][A-Z0-9]{3,8}$', s))

    genes = []
    with open(file_path) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue

            # Handle both CSV and TSV
            parts = [p.strip() for p in line.replace("\t", ",").split(",")]

            if len(parts) < 2:
                print(f"Warning: Line {line_num} has invalid format, skipping: {line}", file=sys.stderr)
                continue

            organism = parts[0]

            # Detect format based on whether column 1 looks like a UniProt ID
            if len(parts) == 3 and looks_like_uniprot_id(parts[1]):
                # Format: organism,uniprot_id,gene_symbol
                gene = parts[1]  # UniProt ID becomes the gene_id
                uniprot_id = None  # Not used in this format
                alias = parts[2]  # Gene symbol becomes alias
            else:
                # Format: organism,gene[,uniprot_id][,alias]
                gene = parts[1]
                uniprot_id = parts[2] if len(parts) > 2 and parts[2] else None
                alias = parts[3] if len(parts) > 3 and parts[3] else None

            genes.append((organism, gene, uniprot_id, alias))

    return genes


def run_fetch_gene(organism: str, gene: str, uniprot_id: Optional[str] = None,
                   alias: Optional[str] = None, force: bool = False) -> bool:
    """Run fetch-gene via just command.

    Args:
        organism: Organism name
        gene: Gene symbol or UniProt ID
        uniprot_id: Optional UniProt ID to pass as --uniprot-id
        alias: Optional alias for directory/file naming
        force: Whether to force overwrite existing files

    Returns:
        True if successful, False otherwise
    """
    # Build command
    cmd = ["just", "fetch-gene", organism, gene]

    # Add optional arguments
    if alias:
        cmd.extend(["--alias", alias])
    if uniprot_id:
        cmd.extend(["--uniprot-id", uniprot_id])
    if force:
        cmd.append("--force")

    print(f"  Running: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ fetch-gene failed: {e}", file=sys.stderr)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        return False


def run_deep_research(organism: str, gene_id: str, provider: str,
                     alias: Optional[str] = None) -> bool:
    """Run deep research via just command.

    Args:
        organism: Organism name
        gene_id: Gene identifier (UniProt ID, locus tag, or gene symbol)
        provider: Deep research provider (openai, perplexity, perplexity-lite, falcon)
        alias: Optional alias for gene symbol (if not provided, looked up from UniProt)

    Returns:
        True if successful, False otherwise
    """
    # Build command
    target = f"deep-research-{provider}"
    cmd = ["just", target, organism, gene_id]

    if alias:
        cmd.extend(["--alias", alias])

    print(f"  Running: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ deep-research-{provider} failed: {e}", file=sys.stderr)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Batch gene pipeline: fetch genes and run deep research",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Fetch genes only
    python scripts/batch_gene_pipeline.py genes.txt

    # Fetch and run perplexity research
    python scripts/batch_gene_pipeline.py genes.txt --providers perplexity

    # Fetch and run multiple providers
    python scripts/batch_gene_pipeline.py genes.txt --providers openai perplexity perplexity-lite

    # Force overwrite existing files
    python scripts/batch_gene_pipeline.py genes.txt --force

    # Skip fetch step (only run research)
    python scripts/batch_gene_pipeline.py genes.txt --skip-fetch --providers perplexity

Input file format (CSV or TSV):

Format 1 - Gene-first (for genes without UniProt ID or when using locus tags):
    organism,gene
    organism,gene,uniprot_id
    organism,gene,uniprot_id,alias

Format 2 - UniProt-first (auto-detected when column 1 is a UniProt ID):
    organism,uniprot_id,gene_symbol

Example files:

Format 1:
    human,TP53
    human,BRCA1,P38398
    METEA,C5B1I4,,mllA
    9BACT,F0JBF1,,HgcB

Format 2 (auto-detected):
    human,P15941,MUC1
    human,O60763,USO1
    human,P04118,CLPS
        """
    )

    parser.add_argument(
        "input_file",
        type=Path,
        help="File containing gene information (CSV or TSV format)"
    )

    parser.add_argument(
        "--providers",
        nargs="+",
        choices=["openai", "perplexity", "perplexity-lite", "falcon"],
        help="Deep research providers to run (can specify multiple)"
    )

    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="Skip fetch-gene step (only run deep research)"
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite existing files when fetching"
    )

    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        default=True,
        help="Continue processing even if individual steps fail (default: True)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be processed without actually running commands"
    )

    args = parser.parse_args()

    # Parse input file
    try:
        genes = parse_gene_file(args.input_file)
    except Exception as e:
        print(f"Error parsing input file: {e}", file=sys.stderr)
        return 1

    if not genes:
        print("No genes found in input file", file=sys.stderr)
        return 1

    print(f"Processing {len(genes)} genes...")
    print()

    # Dry run mode - just show what would be processed
    if args.dry_run:
        print("DRY RUN - showing what would be processed:")
        print()
        for idx, (organism, gene, uniprot_id, alias) in enumerate(genes, 1):
            gene_name = alias if alias else gene
            print(f"[{idx}/{len(genes)}] {organism}/{gene_name}")

            if not args.skip_fetch:
                cmd = ["just", "fetch-gene", organism, gene]
                if alias:
                    cmd.extend(["--alias", alias])
                if uniprot_id:
                    cmd.extend(["--uniprot-id", uniprot_id])
                if args.force:
                    cmd.append("--force")
                print(f"  Would run: {' '.join(cmd)}")

            if args.providers:
                for provider in args.providers:
                    cmd = ["just", f"deep-research-{provider}", organism, gene]
                    if alias:
                        cmd.extend(["--alias", alias])
                    print(f"  Would run: {' '.join(cmd)}")

            print()
        return 0

    # Track statistics
    stats = {
        "total": len(genes),
        "fetch_success": 0,
        "fetch_failed": 0,
        "fetch_skipped": 0,
    }

    # Add provider stats
    if args.providers:
        for provider in args.providers:
            stats[f"{provider}_success"] = 0
            stats[f"{provider}_failed"] = 0

    # Process each gene
    for idx, (organism, gene, uniprot_id, alias) in enumerate(genes, 1):
        gene_name = alias if alias else gene
        print(f"[{idx}/{len(genes)}] Processing {organism}/{gene_name}")

        # Step 1: Fetch gene data
        if not args.skip_fetch:
            fetch_success = run_fetch_gene(organism, gene, uniprot_id, alias, args.force)

            if fetch_success:
                stats["fetch_success"] += 1
                print("  ✓ Fetch successful")
            else:
                stats["fetch_failed"] += 1
                print("  ✗ Fetch failed", file=sys.stderr)

                if not args.continue_on_error:
                    print("Stopping due to error (use --continue-on-error to continue)", file=sys.stderr)
                    break

                # Skip research if fetch failed
                print("  Skipping research for this gene")
                print()
                continue
        else:
            stats["fetch_skipped"] += 1
            print("  ⊘ Skipping fetch step")

        # Step 2: Run deep research providers
        if args.providers:
            for provider in args.providers:
                print(f"  Running {provider} deep research...")

                research_success = run_deep_research(organism, gene, provider, alias)

                if research_success:
                    stats[f"{provider}_success"] += 1
                    print(f"  ✓ {provider} successful")
                else:
                    stats[f"{provider}_failed"] += 1
                    print(f"  ✗ {provider} failed", file=sys.stderr)

                    if not args.continue_on_error:
                        print("Stopping due to error (use --continue-on-error to continue)", file=sys.stderr)
                        return 1

        print()

    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total genes: {stats['total']}")

    if not args.skip_fetch:
        print(f"Fetch successful: {stats['fetch_success']}")
        print(f"Fetch failed: {stats['fetch_failed']}")
    else:
        print(f"Fetch skipped: {stats['fetch_skipped']}")

    if args.providers:
        print()
        for provider in args.providers:
            print(f"{provider} successful: {stats[f'{provider}_success']}")
            print(f"{provider} failed: {stats[f'{provider}_failed']}")

    # Return non-zero if there were any failures
    total_failed = stats["fetch_failed"]
    if args.providers:
        total_failed += sum(stats[f"{p}_failed"] for p in args.providers)

    return 1 if total_failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
