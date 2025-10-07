#!/usr/bin/env python3
"""CLI wrapper for FutureHouse Falcon API for gene research."""

import sys
import time
import traceback
from pathlib import Path
from typing import Any, Optional

import click
from futurehouse_client import FutureHouseClient, JobNames

from ai_gene_review.etl.gene import expand_organism_name, fetch_uniprot_data, resolve_gene_to_uniprot
from ai_gene_review.tools.deep_research import parse_uniprot_metadata


@click.command()
@click.argument("organism", type=str)
@click.argument("gene_or_uniprot", type=str)
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
    "--api-key",
    envvar="FUTUREHOUSE_API_KEY",
    help="FutureHouse API key (or set FUTUREHOUSE_API_KEY env var)",
)
@click.option(
    "--save-citations",
    is_flag=True,
    default=True,
    help="Save citations to separate file (default: on)",
)
@click.option(
    "--system-prompt-file",
    type=click.Path(exists=True),
    help="File containing custom system prompt (optional)",
)
@click.option(
    "--max-retries",
    type=int,
    default=3,
    help="Maximum number of retries on error (default: 3)",
)
def research_gene_falcon(
    organism: str,
    gene_or_uniprot: str,
    alias: Optional[str],
    output_dir: Optional[str],
    api_key: Optional[str],
    save_citations: bool,
    system_prompt_file: Optional[str],
    max_retries: int,
):
    """Research a gene using FutureHouse's Falcon API.

    This tool performs comprehensive research on a given gene using Falcon,
    gathering information about its function, structure, disease associations,
    and relevant literature.

    The second argument can be either a gene symbol or a UniProt ID.
    - Gene symbols are automatically resolved to UniProt IDs
    - When providing a UniProt ID directly, use --alias to specify the gene name

    Examples:
        deep-research-falcon human CFAP300         # Gene symbol
        deep-research-falcon worm pgl-1             # Gene symbol
        deep-research-falcon human TP53 --output-dir custom/path
        deep-research-falcon PSEAE Q9HXE5 --alias rhlB    # UniProt ID with alias
        deep-research-falcon ACEPA A0A1Y0Y121 --alias xdhB  # UniProt ID with alias
    """
    if not api_key:
        click.echo(
            "Error: FutureHouse API key required. Set FUTUREHOUSE_API_KEY environment variable or use --api-key option.",
            err=True,
        )
        sys.exit(1)

    # Determine if gene_or_uniprot is a UniProt ID or gene symbol
    # UniProt IDs typically match pattern: [A-Z0-9]{6,10} or [A-Z][0-9]{5}
    import re
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
            click.echo(f"  just deep-research-falcon {organism} <UNIPROT_ID> --alias {gene_symbol}", err=True)
            sys.exit(1)

    # Use alias for directory and file names if provided
    dir_name = alias if alias else gene_symbol

    # Initialize FutureHouse client
    client = FutureHouseClient(api_key=api_key)

    # Determine output directory
    if output_dir:
        output_path = Path(output_dir)
    else:
        output_path = Path("genes") / organism / dir_name

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

    # Parse UniProt metadata - required
    uniprot_metadata = ""
    if uniprot_id:
        try:
            uniprot_text = fetch_uniprot_data(uniprot_id)
            uniprot_metadata = parse_uniprot_metadata(uniprot_text, uniprot_id)
            click.echo(f"✅ Loaded UniProt metadata for {uniprot_id}")
            # Extract actual gene name from metadata if available and we used UniProt ID directly
            if uniprot_pattern.match(gene_or_uniprot) and alias and 'gene_name' in uniprot_metadata:
                # Update gene_symbol to be the actual gene name from UniProt for the query
                gene_info = parse_uniprot_metadata(uniprot_text, uniprot_id)
                if 'Gene Name:' in gene_info:
                    for line in gene_info.split('\n'):
                        if line.startswith('Gene Name:'):
                            actual_gene = line.split('Gene Name:')[1].strip()
                            if actual_gene:
                                gene_symbol = actual_gene
                                break
        except Exception as e:
            click.echo(f"❌ Error: Could not fetch UniProt data for {uniprot_id}: {e}", err=True)
            click.echo("Deep research requires UniProt metadata to ensure accuracy.", err=True)
            sys.exit(1)
    else:
        # This should not happen now since we resolve gene symbols
        click.echo(f"❌ Error: UniProt ID could not be determined.", err=True)
        sys.exit(1)

    if not uniprot_metadata:
        click.echo(f"❌ Error: Could not fetch UniProt data for {uniprot_id}", err=True)
        sys.exit(1)

    # Build enhanced user query with metadata
    user_query = f"""Research the {organism_full} gene {gene_symbol}.

{uniprot_metadata}

Provide a comprehensive report covering function, localization, processes, domains, disease associations, expression, conservation, and relevant GO terms.

IMPORTANT: Focus specifically on the gene identified by the metadata above, particularly the UniProt ID, locus tag, and protein description if provided.

Sometimes different genes in the same organism have the same name. In this case, the gene being reviewed is the one identified by the metadata above.
"""

    click.echo(f"Starting deep research on {gene_symbol} ({organism_full}) using Falcon...")
    if alias:
        click.echo(f"Using alias '{alias}' for directory and file names")
    click.echo(f"UniProt ID: {uniprot_id}")
    click.echo(f"Output will be saved to: {output_path}")
    click.echo(f"Max retries: {max_retries}")

    response = None
    last_error: Optional[Exception] = None

    for attempt in range(max_retries):
        try:
            # Make the Falcon API call
            if attempt > 0:
                click.echo(f"\n🔄 Retry attempt {attempt + 1}/{max_retries}...")
            else:
                click.echo("\n⏳ This may take several minutes to complete...")

            # Combine system message and user query for Falcon
            full_query = f"{system_message}\n\n{user_query}"

            # Use Falcon API for deep research
            task_data = {
                "name": JobNames.FALCON,  # Use FALCON for comprehensive research
                "query": full_query
            }

            response = client.run_tasks_until_done(task_data)
            break  # Success, exit retry loop

        except Exception as e:
            last_error = e
            click.echo(f"\n⚠️  Error (attempt {attempt + 1}/{max_retries}): {type(e).__name__}: {e}", err=True)
            if attempt < max_retries - 1:
                click.echo("Will retry in 5 seconds...", err=True)
                time.sleep(5)

    if response is None:
        click.echo(f"\n❌ Failed after {max_retries} attempts", err=True)
        click.echo("\n📋 Full stacktrace:", err=True)
        click.echo("-" * 60, err=True)
        traceback.print_exc()
        click.echo("-" * 60, err=True)

        click.echo("\n💡 Suggestions:", err=True)
        click.echo("  - Check your FutureHouse API key is valid", err=True)
        click.echo("  - Check FutureHouse service status", err=True)

        sys.exit(1)

    try:
        # Extract the report text from Falcon response
        # The response should be a list containing PQATaskResponse objects
        report_text = None
        citations_data = None
        task_response: Any = None

        if isinstance(response, list) and len(response) > 0:
            # Get the first (and usually only) response
            task_response = response[0]

            # Extract formatted_answer if available (preferred)
            if hasattr(task_response, 'formatted_answer') and task_response.formatted_answer:
                report_text = task_response.formatted_answer
            elif hasattr(task_response, 'answer') and task_response.answer:
                report_text = task_response.answer
            else:
                # Fallback to string representation
                report_text = str(task_response)

            # Try to extract any additional response data for debugging
            if hasattr(task_response, 'status'):
                click.echo(f"Task status: {task_response.status}")

        elif hasattr(response, 'formatted_answer'):
            task_response = response
            report_text = response.formatted_answer
        elif hasattr(response, 'answer'):
            report_text = response.answer
        elif hasattr(response, 'result'):
            report_text = response.result
        elif hasattr(response, 'content'):
            report_text = response.content
        elif isinstance(response, dict):
            # Try various possible keys
            if 'formatted_answer' in response:
                report_text = response['formatted_answer']
            elif 'answer' in response:
                report_text = response['answer']
            elif 'result' in response:
                report_text = response['result']
            elif 'content' in response:
                report_text = response['content']
            else:
                click.echo(f"Warning: Unknown response structure, keys: {list(response.keys()) if isinstance(response, dict) else 'N/A'}")
                report_text = str(response)
        elif isinstance(response, str):
            report_text = response
        else:
            click.echo(f"Warning: Unexpected response type: {type(response)}")
            report_text = str(response)

        # Validate that we got meaningful content
        if not report_text or len(report_text.strip()) < 100:
            click.echo(f"Warning: Response seems too short ({len(report_text) if report_text else 0} chars), using full response")
            report_text = str(response)

        # Save the research report using dir_name for filenames
        report_file = output_path / f"{dir_name}-falcon-research.md"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(f"# Falcon Research Report: {gene_symbol} ({organism})\n\n")
            f.write("Generated using FutureHouse Falcon API\n\n")
            if alias and uniprot_id:
                f.write(f"UniProt ID: {uniprot_id}\n")
                f.write(f"Directory alias: {alias}\n\n")
            f.write("---\n\n")
            f.write(report_text)

        click.echo(f"✅ Research completed and saved to: {report_file}")

        # Extract and save citations if available in the response
        if save_citations:
            citations = []

            # If task_response wasn't set above, try to get it from response
            if task_response is None:
                if isinstance(response, list) and len(response) > 0:
                    task_response = response[0]
                else:
                    task_response = response

            # Try to extract citations from the response
            if task_response and hasattr(task_response, 'sources'):
                citations = task_response.sources
            elif task_response and hasattr(task_response, 'citations'):
                citations = task_response.citations
            elif task_response and hasattr(task_response, 'references'):
                citations = task_response.references
            elif isinstance(task_response, dict):
                if 'sources' in task_response:
                    citations = task_response['sources']
                elif 'citations' in task_response:
                    citations = task_response['citations']
                elif 'references' in task_response:
                    citations = task_response['references']

            # Extract inline citations from the text using regex patterns
            import re

            # Look for Falcon-style citations like (elsen2005ppsramultifaceted pages 6-8)
            falcon_citations = re.findall(r'\(([^)]+pages?[^)]+)\)', report_text or '')

            # Look for standard patterns like [PMID:12345678], [1], etc.
            standard_refs = re.findall(r'\[([^\]]+)\]', report_text or '')

            # Combine all citation sources
            all_inline_citations = falcon_citations + standard_refs

            if all_inline_citations and not citations:
                citations = all_inline_citations
            elif all_inline_citations and citations:
                # Merge both sources
                citations.extend(all_inline_citations)

            # Save citations if we found any
            if citations:
                citations_file = output_path / f"{dir_name}-falcon-citations.md"
                with open(citations_file, "w", encoding="utf-8") as f:
                    f.write(f"# Citations for {gene_symbol} Research (Falcon)\n\n")

                    # Remove duplicates while preserving order
                    seen = set()
                    unique_citations = []
                    for citation in citations:
                        citation_str = str(citation)
                        if citation_str not in seen:
                            seen.add(citation_str)
                            unique_citations.append(citation)

                    if isinstance(unique_citations, list):
                        for i, citation in enumerate(unique_citations, 1):
                            f.write(f"{i}. {citation}\n")
                    else:
                        f.write(str(unique_citations))

                click.echo(f"📚 Citations saved to: {citations_file} ({len(unique_citations)} unique citations)")
            else:
                click.echo("📚 No citations found in response")

    except Exception as e:
        click.echo(f"\n❌ Error processing response: {type(e).__name__}: {e}", err=True)
        click.echo("\n📋 Full stacktrace:", err=True)
        click.echo("-" * 60, err=True)
        traceback.print_exc()
        click.echo("-" * 60, err=True)
        sys.exit(1)


if __name__ == "__main__":
    research_gene_falcon()