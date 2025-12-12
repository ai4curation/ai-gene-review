#!/usr/bin/env python3
"""Wrapper for deep-research-client that handles gene symbol lookup and reduces justfile repetition.

This script:
1. Accepts organism, gene_or_uniprot, provider, and optional alias
2. Looks up the gene symbol from UniProt file if alias not provided
3. Calls deep-research-client with both gene_symbol and gene_or_uniprot variables
4. Handles output path construction
"""

import argparse
import subprocess
import sys
from pathlib import Path
import re


def parse_uniprot_gene_name(uniprot_file: Path) -> str:
    """Extract gene name from UniProt file.

    Args:
        uniprot_file: Path to UniProt text file

    Returns:
        Gene name/symbol from the file

    Raises:
        ValueError: If gene name cannot be found
    """
    if not uniprot_file.exists():
        raise FileNotFoundError(f"UniProt file not found: {uniprot_file}")

    with open(uniprot_file) as f:
        for line in f:
            # Look for gene name line like: GN   Name=TP53; Synonyms=P53;
            # or: GN   Name=mxcE {ECO:0000313|EMBL:ACS42506.1};
            if line.startswith("GN   Name="):
                match = re.search(r'Name=([^;{]+)', line)
                if match:
                    # Strip whitespace and any trailing annotations
                    return match.group(1).strip()

    raise ValueError(f"Could not find gene name in {uniprot_file}")


def parse_uniprot_context(uniprot_file: Path) -> dict:
    """Extract comprehensive context from UniProt file for gene identification.

    Args:
        uniprot_file: Path to UniProt text file

    Returns:
        Dictionary with fields: accession, protein_description, gene_info,
        organism_full, protein_family, protein_domains
    """
    if not uniprot_file.exists():
        return {}

    context = {
        'accession': '',
        'protein_description': '',
        'gene_info': '',
        'organism_full': '',
        'protein_family': '',
        'protein_domains': []
    }

    de_lines = []
    os_lines = []

    with open(uniprot_file) as f:
        for line in f:
            line = line.rstrip()

            # Extract Accession (AC)
            if line.startswith("AC   "):
                if not context['accession']:
                    # Get first accession
                    ac = line[5:].split(';')[0].strip()
                    context['accession'] = ac

            # Extract Description (DE) - collect all DE lines
            elif line.startswith("DE   "):
                de_lines.append(line[5:].strip())

            # Extract Gene Name info (GN) - full line with all details
            elif line.startswith("GN   "):
                if not context['gene_info']:
                    context['gene_info'] = line[5:].strip()
                else:
                    # Continuation line
                    context['gene_info'] += ' ' + line[5:].strip()

            # Extract Organism/Species (OS) - can span multiple lines
            elif line.startswith("OS   "):
                os_lines.append(line[5:].strip())

            # Extract Similarity/Family info (CC -!- SIMILARITY)
            # Note: SIMILARITY is typically a single line, extract just that
            elif line.startswith("CC   -!- SIMILARITY:"):
                # Extract just this line, remove evidence codes
                text = line[20:].strip()
                # Remove evidence codes like {ECO:...}
                text = re.sub(r'\{ECO:[^}]+\}', '', text).strip()
                context['protein_family'] = text

            # Extract InterPro/Pfam domains from DR lines
            elif line.startswith("DR   InterPro;"):
                parts = line[5:].split(';')
                if len(parts) >= 3:
                    domain_id = parts[1].strip()
                    domain_name = parts[2].strip()
                    context['protein_domains'].append(f"{domain_name} ({domain_id})")
            elif line.startswith("DR   Pfam;"):
                parts = line[5:].split(';')
                if len(parts) >= 3:
                    domain_id = parts[1].strip()
                    domain_name = parts[2].strip()
                    context['protein_domains'].append(f"{domain_name} ({domain_id})")

    # Process collected lines
    context['protein_description'] = ' '.join(de_lines)
    context['organism_full'] = ' '.join(os_lines)

    # Limit domains to first 5 to avoid overwhelming the prompt
    if len(context['protein_domains']) > 5:
        context['protein_domains'] = context['protein_domains'][:5]

    return context


def run_deep_research(
    organism: str,
    gene_id: str,
    provider: str,
    gene_symbol: str,
    output_path: Path,
    uniprot_context: dict = None,
    extra_args: list = None,
    use_template: bool = True
) -> int:
    """Run deep-research-client with proper arguments.

    Args:
        organism: Organism name
        gene_id: Gene identifier (UniProt ID, locus tag, or gene symbol)
        provider: Provider name (openai, perplexity, perplexity-lite, falcon, cyberian)
        gene_symbol: Gene symbol/name to use in template
        output_path: Where to write output
        uniprot_context: Dictionary with UniProt context fields
        extra_args: Additional arguments to pass
        use_template: Whether to use template (False for perplexity-lite)

    Returns:
        Exit code from deep-research-client
    """
    # Map internal provider names to deep-research-client provider names
    # perplexity-lite is our internal name, but we use perplexity provider with params
    actual_provider = "perplexity" if provider == "perplexity-lite" else provider

    if use_template:
        cmd = [
            "uv", "run", "deep-research-client", "research",
            "--template", "templates/gene_research_go_focused.md",
            "--var", f"organism={organism}",
            "--var", f"gene_id={gene_id}",
            "--var", f"gene_symbol={gene_symbol}",
            "--provider", actual_provider,
            "--output", str(output_path)
        ]

        # Add UniProt context variables if available
        if uniprot_context:
            if uniprot_context.get('accession'):
                cmd.extend(["--var", f"uniprot_accession={uniprot_context['accession']}"])
            if uniprot_context.get('protein_description'):
                cmd.extend(["--var", f"protein_description={uniprot_context['protein_description']}"])
            if uniprot_context.get('gene_info'):
                cmd.extend(["--var", f"gene_info={uniprot_context['gene_info']}"])
            if uniprot_context.get('organism_full'):
                cmd.extend(["--var", f"organism_full={uniprot_context['organism_full']}"])
            # Provide default for protein_family if not available
            protein_family = uniprot_context.get('protein_family') or "Not specified in UniProt"
            cmd.extend(["--var", f"protein_family={protein_family}"])
            if uniprot_context.get('protein_domains'):
                domains_str = '; '.join(uniprot_context['protein_domains'])
                cmd.extend(["--var", f"protein_domains={domains_str}"])
    else:
        # For perplexity-lite, use direct query with perplexity provider
        query = (
            f"Research the {gene_symbol} ({gene_id}) gene in {organism}, "
            f"focusing on its molecular function, biological processes, and cellular localization. "
            f"Include information about protein domains, known interactions, and any disease associations."
        )
        cmd = [
            "uv", "run", "deep-research-client", "research",
            query,
            "--provider", actual_provider,
            "--param", "reasoning_effort=low",
            "--param", "model=sonar-pro",
            "--output", str(output_path)
        ]

    if extra_args:
        cmd.extend(extra_args)

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Wrapper for deep-research-client with gene symbol lookup"
    )

    parser.add_argument("organism", help="Organism name")
    parser.add_argument("gene_id", help="Gene identifier (UniProt ID, locus tag, or gene symbol)")
    parser.add_argument("provider", help="Provider (openai, perplexity, perplexity-lite, falcon)")
    parser.add_argument("--alias", help="Gene symbol alias (if not provided, will lookup from UniProt)")
    parser.add_argument("--extra-args", nargs=argparse.REMAINDER, help="Extra args to pass to deep-research-client")

    args = parser.parse_args()

    # Determine gene symbol and parse UniProt context
    uniprot_context = None
    if args.alias:
        gene_symbol = args.alias
        base_dir = Path(f"genes/{args.organism}/{args.alias}")
    else:
        # Try to lookup from UniProt file
        # First try with gene_id as directory name
        uniprot_file = Path(f"genes/{args.organism}/{args.gene_id}/{args.gene_id}-uniprot.txt")

        if uniprot_file.exists():
            try:
                gene_symbol = parse_uniprot_gene_name(uniprot_file)
                print(f"Looked up gene symbol from UniProt: {gene_symbol}")
            except ValueError as e:
                print(f"Warning: {e}", file=sys.stderr)
                print(f"Using {args.gene_id} as gene symbol", file=sys.stderr)
                gene_symbol = args.gene_id

            # Parse comprehensive UniProt context
            uniprot_context = parse_uniprot_context(uniprot_file)
            if uniprot_context:
                print(f"Extracted UniProt context:")
                print(f"  Accession: {uniprot_context.get('accession', 'N/A')}")
                print(f"  Protein: {uniprot_context.get('protein_description', 'N/A')[:80]}...")
                print(f"  Family: {uniprot_context.get('protein_family', 'N/A')[:80]}...")
        else:
            # UniProt file doesn't exist yet, use gene_id as symbol
            print(f"UniProt file not found, using {args.gene_id} as gene symbol")
            gene_symbol = args.gene_id

        base_dir = Path(f"genes/{args.organism}/{args.gene_id}")

    # Construct output path
    if args.provider == "perplexity-lite":
        output_file = base_dir / f"{base_dir.name}-deep-research-perplexity-lite.md"
        use_template = False
    else:
        output_file = base_dir / f"{base_dir.name}-deep-research-{args.provider}.md"
        use_template = True

    # Create directory if it doesn't exist
    base_dir.mkdir(parents=True, exist_ok=True)

    # Run deep research
    return run_deep_research(
        organism=args.organism,
        gene_id=args.gene_id,
        provider=args.provider,
        gene_symbol=gene_symbol,
        output_path=output_file,
        uniprot_context=uniprot_context,
        extra_args=args.extra_args,
        use_template=use_template
    )


if __name__ == "__main__":
    sys.exit(main())
