#!/usr/bin/env python3
"""CLI wrapper for OpenAI Deep Research API for gene research."""

import sys
import time
import traceback
from pathlib import Path
from typing import Optional

import click
import httpx
from openai import OpenAI

from ai_gene_review.etl.gene import expand_organism_name, fetch_uniprot_data


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
@click.argument("gene_symbol", type=str)
@click.option("--organism", default="human", help="Organism (default: human)")
@click.option(
    "--model", default="o3-deep-research-2025-06-26", help="Deep research model to use"
)
@click.option(
    "--output-dir",
    type=click.Path(),
    help="Output directory for results (defaults to genes/<organism>/<gene>/)",
)
@click.option(
    "--api-key",
    envvar="OPENAI_API_KEY",
    help="OpenAI API key (or set OPENAI_API_KEY env var)",
)
@click.option(
    "--save-reasoning",
    is_flag=True,
    default=False,
    help="Save reasoning steps to debug file (default: off)",
)
@click.option(
    "--system-prompt-file",
    type=click.Path(exists=True),
    help="File containing custom system prompt (optional)",
)
@click.option(
    "--timeout",
    type=int,
    default=600,
    help="Request timeout in seconds (default: 600, i.e., 10 minutes)",
)
@click.option(
    "--max-retries",
    type=int,
    default=3,
    help="Maximum number of retries on timeout (default: 3)",
)
@click.option(
    "--uniprot-id",
    type=str,
    help="UniProt ID for the gene (optional, but highly recommended for accuracy)",
)
def research_gene(
    gene_symbol: str,
    organism: str,
    model: str,
    output_dir: Optional[str],
    api_key: Optional[str],
    save_reasoning: bool,
    system_prompt_file: Optional[str],
    timeout: int,
    max_retries: int,
    uniprot_id: Optional[str],
):
    """Research a gene using OpenAI's Deep Research API.

    This tool performs comprehensive research on a given gene symbol,
    gathering information about its function, structure, disease associations,
    and relevant literature.

    Examples:
        deep-research CFAP300
        deep-research TP53 --organism human --output-dir custom/path
        deep-research rhlB --organism PSEAE --uniprot-id Q9HXE5
    """
    if not api_key:
        click.echo(
            "Error: OpenAI API key required. Set OPENAI_API_KEY environment variable or use --api-key option.",
            err=True,
        )
        sys.exit(1)

    # Initialize OpenAI client with custom timeout
    http_client = httpx.Client(
        timeout=httpx.Timeout(
            connect=30.0,  # Connection timeout
            read=timeout,  # Read timeout
            write=30.0,  # Write timeout
            pool=30.0,  # Pool timeout
        )
    )
    client = OpenAI(api_key=api_key, http_client=http_client)

    # Determine output directory
    if output_dir:
        output_path = Path(output_dir)
    else:
        output_path = Path("genes") / organism / gene_symbol

    output_path.mkdir(parents=True, exist_ok=True)

    # Load system prompt (custom or default)
    if system_prompt_file:
        with open(system_prompt_file, "r", encoding="utf-8") as f:
            system_message = f.read()
    else:
        system_message = """You are a molecular biologist and gene annotation expert conducting comprehensive research to support GO annotation curation.

Provide detailed, well-cited information focusing on:
1. Gene function and molecular mechanisms
2. Cellular localization and subcellular components  
3. Biological processes involvement
4. Disease associations and phenotypes
5. Protein domains and structural features
6. Expression patterns and regulation
7. Evolutionary conservation
8. Key experimental evidence and literature

Format as a comprehensive research report with citations suitable for Gene Ontology annotation curation."""

    # Expand organism name for better research results
    organism_full = expand_organism_name(organism)

    # Parse UniProt metadata if available
    uniprot_metadata = ""
    if uniprot_id:
        try:
            uniprot_text = fetch_uniprot_data(uniprot_id)
            uniprot_metadata = parse_uniprot_metadata(uniprot_text, uniprot_id)
            click.echo(f"✅ Loaded UniProt metadata for {uniprot_id}")
        except Exception as e:
            click.echo(f"⚠️  Could not fetch UniProt data for {uniprot_id}: {e}", err=True)
            uniprot_metadata = f"UniProt ID: {uniprot_id}\n"

    if not uniprot_metadata:
        click.echo(f"⚠️  Could not fetch UniProt data for {uniprot_id}", err=True)
        sys.exit(1)

    # Build enhanced user query with metadata
    user_query = f"""Research the {organism_full} gene {gene_symbol}.

{uniprot_metadata}

Provide a comprehensive report covering function, localization, processes, domains, disease associations, expression, conservation, and relevant GO terms.

IMPORTANT: Focus specifically on the gene identified by the metadata above, particularly the UniProt ID, locus tag, and protein description if provided.

Sometimes different genes in the same organism have the same name. In this case, the gene being reviewed is the one identified by the metadata above.
"""

    click.echo(f"Starting deep research on {gene_symbol} ({organism_full})...")
    click.echo(f"Metadata: {uniprot_metadata}")
    click.echo(f"Output will be saved to: {output_path}")
    click.echo(f"Timeout set to: {timeout} seconds")
    click.echo(f"Max retries: {max_retries}")

    response = None
    last_error = None
    
    for attempt in range(max_retries):
        try:
            # Make the Deep Research API call
            if attempt > 0:
                click.echo(f"\n🔄 Retry attempt {attempt + 1}/{max_retries}...")
            else:
                click.echo("\n⏳ This may take several minutes to complete...")
            
            response = client.responses.create(
            model=model,
            input=[
                {
                    "role": "developer",
                    "content": [{"type": "input_text", "text": system_message}],
                },
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": user_query}],
                },
            ],
            tools=[{"type": "web_search_preview"}],
        )
            break  # Success, exit retry loop
            
        except httpx.ReadTimeout as e:
            last_error = e
            click.echo(f"\n⚠️  Timeout error (attempt {attempt + 1}/{max_retries}): {e}", err=True)
            if attempt < max_retries - 1:
                click.echo("Will retry in 5 seconds...", err=True)
                import time
                time.sleep(5)
            
        except httpx.HTTPStatusError as e:
            last_error = e
            click.echo(f"\n⚠️  HTTP error (attempt {attempt + 1}/{max_retries}): {e}", err=True)
            click.echo(f"Status code: {e.response.status_code}", err=True)
            if attempt < max_retries - 1:
                click.echo("Will retry in 5 seconds...", err=True)
                import time
                time.sleep(5)
                
        except Exception as e:
            last_error = e
            click.echo(f"\n⚠️  Unexpected error (attempt {attempt + 1}/{max_retries}): {type(e).__name__}: {e}", err=True)
            if attempt < max_retries - 1:
                click.echo("Will retry in 5 seconds...", err=True)
                import time
                time.sleep(5)
    
    if response is None:
        click.echo(f"\n❌ Failed after {max_retries} attempts", err=True)
        click.echo("\n📋 Full stacktrace:", err=True)
        click.echo("-" * 60, err=True)
        traceback.print_exc()
        click.echo("-" * 60, err=True)
        
        if isinstance(last_error, httpx.ReadTimeout):
            click.echo("\n💡 Suggestions:", err=True)
            click.echo("  - Try increasing the timeout with --timeout option (e.g., --timeout 1200 for 20 minutes)", err=True)
            click.echo("  - The deep research models can take 10-20 minutes for complex queries", err=True)
            click.echo("  - Check OpenAI service status at https://status.openai.com/", err=True)
        
        sys.exit(1)
    
    try:

        # Extract the final report
        final_output = response.output[-1]
        if hasattr(final_output, "content") and final_output.content:  # type: ignore
            content = final_output.content  # type: ignore
            if isinstance(content, list) and len(content) > 0:
                first_content = content[0]
                if hasattr(first_content, "text"):
                    report_text = first_content.text  # type: ignore
                else:
                    report_text = str(first_content)
            else:
                report_text = str(content)
        else:
            report_text = str(final_output)

        # Save the research report
        report_file = output_path / f"{gene_symbol}-deep-research.md"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(f"# Deep Research Report: {gene_symbol} ({organism})\n\n")
            f.write("Generated using OpenAI Deep Research API\n\n")
            f.write("---\n\n")
            f.write(report_text)

        click.echo(f"✅ Research completed and saved to: {report_file}")

        # Extract and save citations if available
        if hasattr(final_output, "content") and final_output.content:  # type: ignore
            content = final_output.content  # type: ignore
            if isinstance(content, list) and len(content) > 0:
                first_content = content[0]
                if hasattr(first_content, "annotations"):
                    annotations = first_content.annotations  # type: ignore
                    if annotations:
                        citations_file = output_path / f"{gene_symbol}-citations.md"
                        with open(citations_file, "w", encoding="utf-8") as f:
                            f.write(f"# Citations for {gene_symbol} Research\n\n")
                            for i, annotation in enumerate(annotations, 1):
                                f.write(f"{i}. {annotation}\n")
                        click.echo(f"📚 Citations saved to: {citations_file}")

        # Save reasoning steps if available and requested
        if save_reasoning:
            reasoning_steps = [
                item
                for item in response.output
                if hasattr(item, "type") and item.type == "reasoning"
            ]  # type: ignore
            if reasoning_steps:
                reasoning_file = output_path / f"{gene_symbol}-reasoning.md"
                with open(reasoning_file, "w", encoding="utf-8") as f:
                    f.write(f"# Reasoning Steps for {gene_symbol} Research\n\n")
                    for i, step in enumerate(reasoning_steps, 1):
                        f.write(f"## Step {i}\n\n")
                        if hasattr(step, "content"):  # type: ignore
                            step_content = step.content  # type: ignore
                            if isinstance(step_content, list) and len(step_content) > 0:
                                if hasattr(step_content[0], "text"):
                                    f.write(f"{step_content[0].text}\n\n")  # type: ignore
                                else:
                                    f.write(f"{step_content[0]}\n\n")
                            else:
                                f.write(f"{step_content}\n\n")
                        else:
                            f.write(f"{step}\n\n")
                click.echo(f"🧠 Reasoning steps saved to: {reasoning_file}")
            else:
                click.echo("ℹ️  No reasoning steps available to save")

    except Exception as e:
        click.echo(f"\n❌ Error processing response: {type(e).__name__}: {e}", err=True)
        click.echo("\n📋 Full stacktrace:", err=True)
        click.echo("-" * 60, err=True)
        traceback.print_exc()
        click.echo("-" * 60, err=True)
        sys.exit(1)
    
    finally:
        # Clean up HTTP client
        if 'http_client' in locals():
            http_client.close()


if __name__ == "__main__":
    research_gene()
