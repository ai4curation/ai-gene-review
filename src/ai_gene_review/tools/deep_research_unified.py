#!/usr/bin/env python3
"""Unified CLI wrapper for deep research using deep-research-client library."""

import sys
import re
from pathlib import Path
from typing import Optional

import click
from deep_research_client import DeepResearchClient
from deep_research_client.templates import TemplateManager

from ai_gene_review.etl.gene import expand_organism_name, fetch_uniprot_data, resolve_gene_to_uniprot


def parse_uniprot_metadata(uniprot_text: str, uniprot_id: str) -> str:
    """Parse key metadata from UniProt text format.

    Extracts the most important fields for gene identification and research.

    Args:
        uniprot_text: Raw UniProt entry in text format
        uniprot_id: UniProt accession ID

    Returns:
        Formatted string with key metadata
    """
    lines = uniprot_text.split('\n')
    metadata = {}

    # Parse key fields
    current_section = None
    for line in lines:
        # Check for new sections
        if line.startswith('CC   -!-'):
            current_section = None  # Reset section tracker

        if line.startswith('ID   '):
            # Extract entry name
            parts = line.split()
            if len(parts) > 1:
                metadata['entry_name'] = parts[1]

        elif line.startswith('AC   '):
            # Primary accession
            metadata['uniprot_id'] = line[5:].split(';')[0].strip()

        elif line.startswith('DE   RecName:'):
            # Protein name
            if 'Full=' in line:
                name_part = line.split('Full=')[1]
                name = name_part.split('{')[0].strip().rstrip(';')
                metadata['protein_name'] = name

        elif line.startswith('DE            EC='):
            # EC number
            ec_part = line.split('EC=')[1]
            ec = ec_part.split(' ')[0].rstrip(';')
            metadata['ec_number'] = ec

        elif line.startswith('GN   Name='):
            # Gene name
            name_part = line.split('Name=')[1]
            gene = name_part.split(' ')[0].split(';')[0].split('{')[0]
            metadata['gene_name'] = gene

        elif line.startswith('GN   OrderedLocusNames='):
            # Locus tag
            locus_part = line.split('OrderedLocusNames=')[1]
            locus = locus_part.split(';')[0]
            metadata['locus_tag'] = locus

        elif line.startswith('GN   Synonyms='):
            # Gene synonyms
            syn_part = line.split('Synonyms=')[1]
            synonyms = syn_part.split(';')[0]
            metadata['synonyms'] = synonyms

        elif line.startswith('OS   '):
            # Organism
            if 'organism' not in metadata:
                metadata['organism'] = line[5:].rstrip('.')
            else:
                metadata['organism'] += ' ' + line[5:].rstrip('.')

        elif line.startswith('OX   NCBI_TaxID='):
            # Taxonomy ID
            tax_id = line.split('NCBI_TaxID=')[1].rstrip(';')
            metadata['ncbi_taxid'] = tax_id

        elif line.startswith('CC   -!- FUNCTION:'):
            # Function description
            current_section = 'function'
            func = line.split('FUNCTION:')[1].strip()
            metadata['function'] = func
        elif line.startswith('CC       ') and current_section == 'function':
            # Continue function description
            continuation = line[9:].strip()
            metadata['function'] += ' ' + continuation

        elif line.startswith('CC   -!- SUBCELLULAR LOCATION:'):
            # Subcellular location
            current_section = 'location'
            loc = line.split('SUBCELLULAR LOCATION:')[1].strip()
            metadata['subcellular_location'] = loc
        elif line.startswith('CC       ') and current_section == 'location':
            # Continue location description
            continuation = line[9:].strip()
            metadata['subcellular_location'] += ' ' + continuation

        elif line.startswith('CC   -!- SUBUNIT:'):
            # Subunit information
            current_section = 'subunit'
            subunit = line.split('SUBUNIT:')[1].strip()
            metadata['subunit'] = subunit
        elif line.startswith('CC       ') and current_section == 'subunit':
            # Continue subunit description
            continuation = line[9:].strip()
            metadata['subunit'] += ' ' + continuation

    # Clean up all fields to remove evidence codes at the end
    for key in ['function', 'subcellular_location', 'subunit']:
        if key in metadata:
            text = metadata[key]
            if '{ECO:' in text:
                text = text.split('{ECO:')[0].strip()
            metadata[key] = text

    # Format metadata for prompt
    result = []
    result.append("=== UNIPROT METADATA ===")
    result.append(f"UniProt ID: {metadata.get('uniprot_id', uniprot_id)}")
    result.append(f"Entry Name: {metadata.get('entry_name', 'N/A')}")

    if 'gene_name' in metadata:
        result.append(f"Gene Name: {metadata['gene_name']}")
    if 'locus_tag' in metadata:
        result.append(f"Locus Tag: {metadata['locus_tag']}")
    if 'synonyms' in metadata:
        result.append(f"Gene Synonyms: {metadata['synonyms']}")

    if 'protein_name' in metadata:
        result.append(f"Protein Name: {metadata['protein_name']}")
    if 'ec_number' in metadata:
        result.append(f"EC Number: {metadata['ec_number']}")

    if 'organism' in metadata:
        result.append(f"Organism: {metadata['organism']}")
    if 'ncbi_taxid' in metadata:
        result.append(f"NCBI Taxonomy ID: {metadata['ncbi_taxid']}")

    if 'function' in metadata:
        # Clean up function text
        func_text = metadata['function'].replace('{ECO:', ' {ECO:')
        result.append(f"Function: {func_text}")

    if 'subcellular_location' in metadata:
        result.append(f"Subcellular Location: {metadata['subcellular_location']}")

    if 'subunit' in metadata:
        result.append(f"Subunit: {metadata['subunit']}")

    result.append("======================")

    return '\n'.join(result)


@click.command()
@click.argument("organism", type=str)
@click.argument("gene_or_uniprot", type=str)
@click.option(
    "--provider",
    type=click.Choice(['openai', 'falcon', 'perplexity', 'mock'], case_sensitive=False),
    help="Research provider to use (defaults to auto-detect from available API keys)",
)
@click.option(
    "--model",
    type=str,
    help="Model to use with provider (e.g., 'sonar-pro' for Perplexity)",
)
@click.option(
    "--alias",
    type=str,
    help="Alias to use for directory name and file prefixes instead of gene symbol",
)
@click.option(
    "--output-dir",
    type=click.Path(),
    help="Output directory for results (defaults to genes/<organism>/<gene>/)",
)
@click.option(
    "--template",
    type=click.Path(exists=True),
    help="Custom template file to use (defaults to gene_research_go_focused.md)",
)
@click.option(
    "--no-cache",
    is_flag=True,
    help="Bypass cache for this query",
)
@click.option(
    "--separate-citations",
    is_flag=True,
    help="Save citations to separate file",
)
def research_gene_unified(
    organism: str,
    gene_or_uniprot: str,
    provider: Optional[str],
    model: Optional[str],
    alias: Optional[str],
    output_dir: Optional[str],
    template: Optional[str],
    no_cache: bool,
    separate_citations: bool,
):
    """Unified deep research using deep-research-client library.

    This tool performs comprehensive research on a given gene using multiple
    research providers (OpenAI, FutureHouse Falcon, Perplexity AI).

    The second argument can be either a gene symbol or a UniProt ID.
    - Gene symbols are automatically resolved to UniProt IDs
    - When providing a UniProt ID directly, use --alias to specify the gene name

    Examples:
        deep-research-unified human CFAP300
        deep-research-unified human TP53 --provider perplexity --model sonar-pro
        deep-research-unified PSEAE Q9HXE5 --alias rhlB --provider openai
        deep-research-unified worm pgl-1 --output-dir custom/path
    """
    # Determine if gene_or_uniprot is a UniProt ID or gene symbol
    uniprot_pattern = re.compile(r'^[A-Z][0-9][A-Z0-9]{3}[0-9]$|^[A-Z0-9]{6,10}$')

    if uniprot_pattern.match(gene_or_uniprot):
        # Likely a UniProt ID
        uniprot_id = gene_or_uniprot
        gene_symbol = alias if alias else gene_or_uniprot
    else:
        # Likely a gene symbol - resolve it to UniProt ID
        gene_symbol = gene_or_uniprot
        try:
            click.echo(f"Resolving gene symbol '{gene_symbol}' to UniProt ID...")
            uniprot_id = resolve_gene_to_uniprot(gene_symbol, organism)
            click.echo(f"✅ Resolved to UniProt ID: {uniprot_id}")
        except ValueError as e:
            click.echo(f"❌ Error: {e}", err=True)
            click.echo(f"If you have the UniProt ID, you can provide it directly:", err=True)
            click.echo(f"  just deep-research {organism} <UNIPROT_ID> --alias {gene_symbol} --provider {provider or 'openai'}", err=True)
            sys.exit(1)

    # Use alias for directory and file names if provided
    dir_name = alias if alias else gene_symbol

    # Determine output directory
    if output_dir:
        output_path = Path(output_dir)
    else:
        output_path = Path("genes") / organism / dir_name

    output_path.mkdir(parents=True, exist_ok=True)

    # Fetch and parse UniProt metadata
    try:
        uniprot_text = fetch_uniprot_data(uniprot_id)
        uniprot_metadata = parse_uniprot_metadata(uniprot_text, uniprot_id)
        click.echo(f"✅ Loaded UniProt metadata for {uniprot_id}")
    except Exception as e:
        click.echo(f"❌ Error: Could not fetch UniProt data for {uniprot_id}: {e}", err=True)
        click.echo("Deep research requires UniProt metadata to ensure accuracy.", err=True)
        sys.exit(1)

    # Initialize deep research client with cache configuration
    from deep_research_client.models import CacheConfig
    cache_config = CacheConfig(enabled=not no_cache)
    client = DeepResearchClient(cache_config=cache_config)

    # Check available providers
    available_providers = client.get_available_providers()
    if not available_providers:
        click.echo("❌ Error: No research providers available. Please set API keys:", err=True)
        click.echo("  - OPENAI_API_KEY for OpenAI Deep Research", err=True)
        click.echo("  - FUTUREHOUSE_API_KEY for FutureHouse Falcon", err=True)
        click.echo("  - PERPLEXITY_API_KEY for Perplexity AI", err=True)
        sys.exit(1)

    # Determine provider to use
    if provider:
        if provider not in available_providers:
            click.echo(f"❌ Error: Provider '{provider}' not available.", err=True)
            click.echo(f"Available providers: {', '.join(available_providers)}", err=True)
            sys.exit(1)
    else:
        # Auto-select provider (prefer perplexity > openai > falcon)
        provider_priority = ['perplexity', 'openai', 'falcon']
        for preferred in provider_priority:
            if preferred in available_providers:
                provider = preferred
                break
        if not provider:
            provider = available_providers[0]

    click.echo(f"Using provider: {provider}")
    if model:
        click.echo(f"Using model: {model}")

    # Prepare template and variables
    template_manager = TemplateManager()

    # Use custom template or default
    if template:
        template_path = Path(template)
    else:
        template_path = Path(__file__).parent.parent.parent.parent / "templates" / "gene_research_go_focused.md"

    if not template_path.exists():
        click.echo(f"❌ Error: Template file not found: {template_path}", err=True)
        sys.exit(1)

    # Prepare template variables
    organism_full = expand_organism_name(organism)
    variables = {
        "gene": gene_symbol,
        "organism": organism_full,
        "uniprot_metadata": uniprot_metadata,
    }

    try:
        # Render template with variables
        query = template_manager.render_template(template_path, variables)

        # Prepare template info for metadata
        template_info = {
            'template_file': str(template_path.name),
            'template_variables': {k: v for k, v in variables.items() if k != 'uniprot_metadata'}  # Exclude large metadata
        }

        click.echo(f"Starting deep research on {gene_symbol} ({organism_full})...")
        if alias:
            click.echo(f"Using alias '{alias}' for directory and file names")
        click.echo(f"UniProt ID: {uniprot_id}")
        click.echo(f"Output will be saved to: {output_path}")
        click.echo("⏳ This may take several minutes to complete...")

        # Perform research
        result = client.research(
            query=query,
            provider=provider,
            template_info=template_info,
            model=model
        )

        # Determine output filename with new naming convention: GENE-deep-research-PROVIDER.md
        provider_name = result.provider or provider
        output_file = output_path / f"{dir_name}-deep-research-{provider_name}.md"

        # Save the research report
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.markdown)

        click.echo(f"✅ Research completed and saved to: {output_file}")

        # Display some metadata
        if result.cached:
            click.echo("📄 Result retrieved from cache")
        if result.duration_seconds:
            click.echo(f"⏱️  Duration: {result.duration_seconds:.1f} seconds")
        if hasattr(result, 'citations') and result.citations:
            click.echo(f"📚 Found {len(result.citations)} citations")

        # Save citations separately if requested
        if separate_citations and hasattr(result, 'citations') and result.citations:
            citations_file = output_path / f"{dir_name}-deep-research-{provider_name}-citations.md"
            with open(citations_file, "w", encoding="utf-8") as f:
                f.write(f"# Citations for {gene_symbol} Research ({provider_name})\n\n")
                for i, citation in enumerate(result.citations, 1):
                    f.write(f"{i}. {citation}\n")
            click.echo(f"📚 Citations saved to: {citations_file}")

    except Exception as e:
        click.echo(f"❌ Error during research: {type(e).__name__}: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    research_gene_unified()