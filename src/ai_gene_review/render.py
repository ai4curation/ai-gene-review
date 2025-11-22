#!/usr/bin/env python
"""Custom HTML renderer for gene review YAML files using Jinja2."""

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def load_gene_review(yaml_path: Path) -> Dict[str, Any]:
    """Load a gene review YAML file.

    Args:
        yaml_path: Path to the YAML file

    Returns:
        Dictionary containing the gene review data

    Raises:
        FileNotFoundError: If the YAML file doesn't exist
        yaml.YAMLError: If the YAML file is invalid

    >>> from pathlib import Path
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
    ...     _ = f.write('id: TEST123\\ngene_symbol: TEST\\n')
    ...     path = Path(f.name)
    >>> data = load_gene_review(path)
    >>> data['id']
    'TEST123'
    >>> path.unlink()
    """
    if not yaml_path.exists():
        raise FileNotFoundError(f"YAML file not found: {yaml_path}")

    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        return data if data else {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Invalid YAML in {yaml_path}: {e}")


def enrich_gene_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Enrich gene data with computed fields and ensure consistency.

    Args:
        data: Raw gene review data

    Returns:
        Enriched gene review data

    >>> data = {'existing_annotations': [{'action': 'ACCEPT'}, {'action': 'REMOVE'}]}
    >>> enriched = enrich_gene_data(data)
    >>> enriched['stats']['total_annotations']
    2
    >>> enriched['stats']['accepted_annotations']
    1
    """
    # Determine if this is an RNA gene
    product_type = data.get('product_type', 'PROTEIN').upper()
    data['is_rna_gene'] = product_type in ['RNA', 'LNCRNA', 'MIRNA', 'SNRNA', 'SNORNA', 'TRNA', 'RRNA', 'NCRNA']

    # Add statistics
    stats = {
        'total_annotations': 0,
        'accepted_annotations': 0,
        'removed_annotations': 0,
        'modified_annotations': 0,
        'undecided_annotations': 0,
        'core_functions_count': 0,
        'references_count': 0
    }

    if 'existing_annotations' in data and data['existing_annotations']:
        annotations = data['existing_annotations']
        stats['total_annotations'] = len(annotations)

        for ann in annotations:
            if 'review' in ann and ann['review']:
                action = ann['review'].get('action', 'UNDECIDED')
            else:
                action = ann.get('action', 'UNDECIDED')

            if action == 'ACCEPT':
                stats['accepted_annotations'] += 1
            elif action == 'REMOVE':
                stats['removed_annotations'] += 1
            elif action == 'MODIFY':
                stats['modified_annotations'] += 1
            elif action in ['UNDECIDED', 'PENDING']:
                stats['undecided_annotations'] += 1

    if 'core_functions' in data and data['core_functions']:
        stats['core_functions_count'] = len(data['core_functions'])

    if 'references' in data and data['references']:
        stats['references_count'] = len(data['references'])

    data['stats'] = stats

    # Create reference lookup dictionary for easy access in template
    reference_lookup = {}
    if 'references' in data and data['references']:
        for ref in data['references']:
            if 'id' in ref:
                reference_lookup[ref['id']] = ref
    data['reference_lookup'] = reference_lookup

    # Normalize annotation structure for easier template access
    if 'existing_annotations' in data:
        for ann in data['existing_annotations']:
            # If review exists, flatten it for easier access
            if 'review' in ann and ann['review']:
                review = ann['review']
                ann['action'] = review.get('action', 'UNDECIDED')
                ann['reason'] = review.get('reason', '')
                ann['summary'] = review.get('summary', '')
                ann['proposed_replacement_terms'] = review.get('proposed_replacement_terms', [])
            elif 'action' not in ann:
                ann['action'] = 'UNDECIDED'

    return data


def find_markdown_files(gene_dir: Path) -> List[Tuple[str, Path]]:
    """Find relevant markdown files in the gene directory.

    Args:
        gene_dir: Directory containing gene files

    Returns:
        List of (display_name, file_path) tuples
    """
    markdown_files = []

    # Find all .md files in the gene directory (not recursive)
    for md_file in gene_dir.glob("*.md"):
        # Skip if it's a directory somehow
        if not md_file.is_file():
            continue

        # Skip citations files (included in deep research)
        if md_file.name.endswith('-citations.md'):
            continue

        # Skip pathway files (separate HTML exists)
        if md_file.name.endswith('-pathway.md'):
            continue

        # Create a display name from the filename
        name = md_file.stem
        # Remove gene prefix if present for cleaner display
        gene_name = gene_dir.name
        if name.startswith(gene_name + "-"):
            name = name[len(gene_name) + 1:]
        elif name.startswith(gene_name + "_"):
            name = name[len(gene_name) + 1:]

        # Make the name more readable
        display_name = name.replace("-", " ").replace("_", " ").title()
        markdown_files.append((display_name, md_file))

    # Check for bioinformatics results
    bioinfo_dir = gene_dir / (gene_dir.name + "-bioinformatics")
    if bioinfo_dir.exists() and bioinfo_dir.is_dir():
        results_file = bioinfo_dir / "RESULTS.md"
        if results_file.exists():
            markdown_files.append(("Bioinformatics Results", results_file))

    # Sort by display name for consistent ordering
    # But prioritize certain files
    priority_order = {
        "Deep Research": 1,
        "Notes": 2,
        "Bioinformatics Results": 3,
    }

    def sort_key(item):
        display_name = item[0]
        for key, priority in priority_order.items():
            if key in display_name:
                return (priority, display_name)
        return (999, display_name)

    markdown_files.sort(key=sort_key)

    return markdown_files


def process_markdown_content(content: str) -> str:
    """Process markdown content to HTML with enhanced features.

    Args:
        content: Raw markdown content

    Returns:
        Processed HTML content
    """
    # Convert PMID citations to links if they're in [PMID:12345 "text"] format
    def replace_pmid(match):
        pmid = match.group(1)
        text = match.group(2) if match.group(2) else ""
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"
        if text:
            return f'[PMID:{pmid}]({url} "{text}")'
        else:
            return f'[PMID:{pmid}]({url})'

    content = re.sub(r'\[PMID:(\d+)(?:\s+"([^"]+)")?\]', replace_pmid, content)

    # Convert markdown to HTML with useful extensions
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'codehilite',
        'toc',
        'attr_list',
        'def_list',
        'nl2br'  # Convert newlines to <br>
    ])

    html = md.convert(content)

    return html


def curie_to_url(curie: str) -> str:
    """Convert a CURIE to a URL for linking.

    Args:
        curie: CURIE identifier (e.g., GO:0005737, PMID:12345)

    Returns:
        URL for the identifier

    >>> curie_to_url('GO:0005737')
    'https://www.ebi.ac.uk/QuickGO/term/GO:0005737'
    >>> curie_to_url('PMID:12345')
    'https://pubmed.ncbi.nlm.nih.gov/12345'
    >>> curie_to_url('NCBITaxon:9606')
    'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9606'
    """
    if not curie or ':' not in curie:
        return '#'

    prefix, identifier = curie.split(':', 1)

    url_patterns = {
        'GO': 'https://www.ebi.ac.uk/QuickGO/term/GO:{}',
        'PMID': 'https://pubmed.ncbi.nlm.nih.gov/{}',
        'NCBITaxon': 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={}',
        'UniProtKB': 'https://www.uniprot.org/uniprotkb/{}',
        'EC': 'https://www.enzyme-database.org/query.php?ec={}',
        'CHEBI': 'https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{}',
        'CL': 'https://www.ebi.ac.uk/ols/ontologies/cl/terms?iri=http://purl.obolibrary.org/obo/CL_{}',
        'UBERON': 'https://www.ebi.ac.uk/ols/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_{}',
        'HP': 'https://hpo.jax.org/app/browse/term/HP:{}',
        'SO': 'https://www.ebi.ac.uk/ols/ontologies/so/terms?iri=http://purl.obolibrary.org/obo/SO_{}',
        'ECO': 'https://www.ebi.ac.uk/ols/ontologies/eco/terms?iri=http://purl.obolibrary.org/obo/ECO_{}',
    }

    if prefix in url_patterns:
        return url_patterns[prefix].format(identifier)
    elif prefix == 'GO_REF':
        return f'https://github.com/geneontology/go-site/blob/master/metadata/gorefs/goref-{identifier}.md'
    elif prefix == 'file':
        # Local file references don't get URLs
        return '#'
    else:
        # Generic OBO for unknown ontologies
        return f'https://www.ebi.ac.uk/ols/search?q={curie}'


def render_html(data: Dict[str, Any], template_path: Path, yaml_content: str = '') -> str:
    """Render gene review data as HTML using Jinja2 template.

    Args:
        data: Gene review data
        template_path: Path to the Jinja2 template file
        yaml_content: Raw YAML content for preview

    Returns:
        Rendered HTML string
    """
    # Set up Jinja2 environment
    template_dir = template_path.parent
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'j2'])
    )

    # Add custom filter for CURIE to URL conversion
    env.filters['curie_to_url'] = curie_to_url

    # Load and render template
    template = env.get_template(template_path.name)
    html = template.render(gene=data, yaml_content=yaml_content)

    return html


def render_gene_review(
    yaml_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None
) -> Path:
    """Render a gene review YAML file to HTML.

    Args:
        yaml_path: Path to the gene review YAML file
        output_path: Optional output path for HTML file
        template_path: Optional path to custom Jinja2 template

    Returns:
        Path to the generated HTML file

    Raises:
        FileNotFoundError: If input files don't exist
        yaml.YAMLError: If YAML is invalid
    """
    # Load and process data
    data = load_gene_review(yaml_path)
    data = enrich_gene_data(data)

    # Read raw YAML content for preview
    with open(yaml_path, 'r') as f:
        yaml_content = f.read()

    # Find and process markdown files
    gene_dir = yaml_path.parent
    markdown_files = find_markdown_files(gene_dir)
    markdown_sections = []

    for display_name, md_path in markdown_files:
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if content.strip():  # Only include non-empty files
                html_content = process_markdown_content(content)
                markdown_sections.append({
                    'title': display_name,
                    'filename': md_path.name,
                    'content': html_content
                })
        except Exception as e:
            print(f"Warning: Could not process {md_path}: {e}", file=sys.stderr)

    data['markdown_sections'] = markdown_sections

    # Check for pathway HTML file
    gene_symbol = data.get('gene_symbol', yaml_path.stem.replace('-ai-review', ''))
    pathway_html = gene_dir / f"{gene_symbol}-pathway.html"
    if pathway_html.exists():
        data['pathway_html_file'] = pathway_html.name
    else:
        data['pathway_html_file'] = None

    # Set default template if not provided
    if template_path is None:
        module_dir = Path(__file__).parent
        template_path = module_dir / "templates" / "gene_review.html.j2"
        if not template_path.exists():
            raise FileNotFoundError(f"Default template not found at {template_path}")

    # Set default output path if not provided
    if output_path is None:
        if yaml_path.name.endswith('-ai-review.yaml'):
            output_path = yaml_path.parent / yaml_path.name.replace('-ai-review.yaml', '-ai-review.html')
        else:
            output_path = yaml_path.with_suffix('.html')

    # Render HTML
    html = render_html(data, template_path, yaml_content)

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return output_path


def render_all_reviews(
    directory: Path,
    template_path: Optional[Path] = None,
    pattern: str = "*-ai-review.yaml"
) -> List[Path]:
    """Render all gene review YAML files in a directory tree.

    Args:
        directory: Root directory to search
        template_path: Optional path to custom template
        pattern: File pattern to match

    Returns:
        List of generated HTML file paths
    """
    output_files: List[Path] = []
    yaml_files = list(directory.rglob(pattern))

    if not yaml_files:
        print(f"No files matching '{pattern}' found in {directory}")
        return output_files

    print(f"Found {len(yaml_files)} files to render")

    for yaml_file in yaml_files:
        try:
            output_path = render_gene_review(yaml_file, template_path=template_path)
            output_files.append(output_path)
            print(f"✓ Rendered {yaml_file.name}")
        except Exception as e:
            print(f"✗ Failed to render {yaml_file}: {e}", file=sys.stderr)
            continue

    print(f"\nSuccessfully rendered {len(output_files)}/{len(yaml_files)} files")
    return output_files


def main():
    """Command-line interface for the renderer."""
    parser = argparse.ArgumentParser(
        description="Render gene review YAML files as HTML",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Render a single file
  python -m ai_gene_review.render genes/human/CFAP300/CFAP300-ai-review.yaml

  # Render with custom output
  python -m ai_gene_review.render genes/human/CFAP300/CFAP300-ai-review.yaml -o output.html

  # Render all files in directory
  python -m ai_gene_review.render --all genes/

  # Use custom template
  python -m ai_gene_review.render genes/human/CFAP300/CFAP300-ai-review.yaml --template custom.html.j2
        """
    )

    parser.add_argument(
        "input",
        type=Path,
        nargs="?",
        help="Input YAML file or directory (when using --all)"
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output HTML file (only for single file)"
    )

    parser.add_argument(
        "-t", "--template",
        type=Path,
        help="Path to custom Jinja2 template"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Render all *-ai-review.yaml files in directory"
    )

    parser.add_argument(
        "--pattern",
        default="*-ai-review.yaml",
        help="File pattern when using --all (default: *-ai-review.yaml)"
    )

    args = parser.parse_args()

    if not args.input:
        parser.error("Input file or directory required")

    if args.all and args.output:
        parser.error("Cannot specify output file when using --all")

    try:
        if args.all:
            if not args.input.is_dir():
                parser.error(f"When using --all, input must be a directory: {args.input}")
            render_all_reviews(args.input, template_path=args.template, pattern=args.pattern)
        else:
            if not args.input.is_file():
                parser.error(f"Input file not found: {args.input}")
            output = render_gene_review(args.input, output_path=args.output, template_path=args.template)
            print(f"✓ Rendered to {output}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()