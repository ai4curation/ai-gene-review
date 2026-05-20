#!/usr/bin/env python
"""Custom HTML renderer for gene review YAML files using Jinja2."""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


_RELATIVE_URL_ATTR_PATTERN = re.compile(
    r'(?P<attr>\b(?:src|href))=(?P<quote>["\'])(?P<url>[^"\']+)(?P=quote)',
    re.IGNORECASE,
)

_GENE_RESEARCH_START_PATTERNS = (
    re.compile(r"(?m)^## Research Report\b.*$"),
    re.compile(r"(?m)^# (?!Gene Research for Functional Annotation\s*$).+"),
    re.compile(r"(?m)^The \*\*.+?\*\* gene\b.*$"),
    re.compile(r"(?m)^The .+? gene\b.*$"),
    re.compile(r"(?m)^\*\*Primary role:\*\*.*$"),
)


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
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        return data if data else {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Invalid YAML in {yaml_path}: {e}")


def split_front_matter(text: str) -> Tuple[Dict[str, Any], str]:
    """Split YAML front matter from Markdown content."""
    normalized = text.replace("\r\n", "\n")
    lines = normalized.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, normalized

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            try:
                metadata = yaml.safe_load("\n".join(lines[1:index])) or {}
            except yaml.YAMLError:
                return {}, normalized
            if not isinstance(metadata, dict):
                metadata = {}
            return metadata, "\n".join(lines[index + 1 :])

    return {}, normalized


def is_deep_research_markdown(path: Path) -> bool:
    """Return True for deep-research report Markdown files, excluding citations."""
    name = path.name
    return (
        path.suffix == ".md"
        and "-deep-research" in name
        and not name.endswith("-citations.md")
        and not name.endswith(".citations.md")
    )


def normalize_embedded_markdown(text: str) -> str:
    """Remove wrapper indentation commonly found in embedded agent transcripts."""
    normalized = text.strip("\n")
    indented_lines = [
        line
        for line in normalized.splitlines()
        if line.strip() and line.startswith("        ")
    ]
    if len(indented_lines) >= 3:
        normalized = re.sub(r"(?m)^ {8}", "", normalized)
    return normalized.strip()


def extract_deep_research_body(text: str) -> Tuple[Dict[str, Any], str]:
    """Extract the rendered report body from a deep-research Markdown file."""
    metadata, body = split_front_matter(text)

    output_chunks = re.split(r"(?m)^## Output\s*$", body)
    if len(output_chunks) > 1:
        body = output_chunks[-1]

    body = normalize_embedded_markdown(body)
    starts = [
        match.start()
        for pattern in _GENE_RESEARCH_START_PATTERNS
        for match in [pattern.search(body)]
        if match
    ]
    if starts:
        body = body[min(starts) :]

    return metadata, normalize_embedded_markdown(body)


def extract_display_title(text: str, fallback: str) -> str:
    """Extract a compact display title from Markdown content."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            if title and title != "Gene Research for Functional Annotation":
                return title
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            if title and title not in {"Question", "Output"}:
                return title
        if stripped.startswith("### "):
            return stripped[4:].strip()
        if (
            stripped
            and len(stripped) <= 120
            and not stripped.startswith(("-", "|", "```"))
        ):
            return stripped
    return fallback


def provider_from_deep_research_filename(name: str) -> Optional[str]:
    """Infer provider from a deep-research filename when metadata is absent."""
    stem = name.removesuffix(".md")
    marker = "-deep-research-"
    if marker in stem:
        provider = stem.rsplit(marker, 1)[-1]
        return provider or None
    return None


def humanize_provider(value: Optional[str]) -> Optional[str]:
    """Convert a provider slug into a readable label."""
    if not value:
        return None
    special_cases = {
        "bioreason": "BioReason",
        "bioreason-rl": "BioReason RL",
        "bioreason-sft": "BioReason SFT",
        "codex": "Codex",
        "cyberian": "Cyberian",
        "falcon": "Falcon",
        "manual": "Manual",
        "openai": "OpenAI",
        "openscientist": "OpenScientist",
        "perplexity": "Perplexity",
        "perplexity-lite": "Perplexity Lite",
    }
    normalized = str(value).strip().lower()
    if normalized in special_cases:
        return special_cases[normalized]
    return " ".join(
        part.capitalize() for part in re.split(r"[-_]+", normalized) if part
    )


def _is_relative_url(url: str) -> bool:
    return not re.match(r"^(?:[a-z][a-z0-9+.-]*:|/|#|\?)", url, re.IGNORECASE)


def rebase_relative_url(url: str, base_prefix: str) -> str:
    """Prefix relative URLs so report assets resolve from the rendered page."""
    if not url or base_prefix in {"", "."} or not _is_relative_url(url):
        return url
    return f"{base_prefix.rstrip('/')}/{url.lstrip('./')}"


def rebase_relative_html_urls(html: str, base_prefix: str) -> str:
    """Prefix relative src/href URLs inside rendered Markdown HTML."""
    if not html or base_prefix in {"", "."}:
        return html

    def _replace(match: re.Match[str]) -> str:
        url = match.group("url")
        rebased = rebase_relative_url(url, base_prefix)
        if rebased == url:
            return match.group(0)
        return (
            f"{match.group('attr')}={match.group('quote')}"
            f"{rebased}{match.group('quote')}"
        )

    return _RELATIVE_URL_ATTR_PATTERN.sub(_replace, html)


def normalize_artifact_metadata(
    metadata: Dict[str, Any],
    base_prefix: str = "",
) -> List[Dict[str, Any]]:
    """Normalize Edison artifact frontmatter for template rendering."""
    artifacts = metadata.get("artifacts") or []
    if not isinstance(artifacts, list):
        return []

    normalized = []
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        path = artifact.get("path") or artifact.get("filename")
        media_type = artifact.get("media_type") or ""
        normalized.append(
            {
                "filename": artifact.get("filename"),
                "path": path,
                "href": rebase_relative_url(str(path), base_prefix) if path else None,
                "media_type": media_type,
                "is_image": media_type.startswith("image/"),
                "description": artifact.get("description"),
                "source": artifact.get("source"),
                "data_storage_id": artifact.get("data_storage_id"),
            }
        )
    return normalized


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
    product_type = data.get("product_type", "PROTEIN").upper()
    data["is_rna_gene"] = product_type in [
        "RNA",
        "LNCRNA",
        "MIRNA",
        "SNRNA",
        "SNORNA",
        "TRNA",
        "RRNA",
        "NCRNA",
    ]

    # Add statistics
    stats = {
        "total_annotations": 0,
        "accepted_annotations": 0,
        "removed_annotations": 0,
        "modified_annotations": 0,
        "undecided_annotations": 0,
        "core_functions_count": 0,
        "references_count": 0,
    }

    if "existing_annotations" in data and data["existing_annotations"]:
        annotations = data["existing_annotations"]
        stats["total_annotations"] = len(annotations)

        for ann in annotations:
            if "review" in ann and ann["review"]:
                action = ann["review"].get("action", "UNDECIDED")
            else:
                action = ann.get("action", "UNDECIDED")

            if action == "ACCEPT":
                stats["accepted_annotations"] += 1
            elif action == "REMOVE":
                stats["removed_annotations"] += 1
            elif action == "MODIFY":
                stats["modified_annotations"] += 1
            elif action in ["UNDECIDED", "PENDING"]:
                stats["undecided_annotations"] += 1

    if "core_functions" in data and data["core_functions"]:
        stats["core_functions_count"] = len(data["core_functions"])

    if "references" in data and data["references"]:
        stats["references_count"] = len(data["references"])

    data["stats"] = stats

    # Create reference lookup dictionary for easy access in template
    reference_lookup = {}
    if "references" in data and data["references"]:
        for ref in data["references"]:
            if "id" in ref:
                reference_lookup[ref["id"]] = ref
    data["reference_lookup"] = reference_lookup

    # Normalize annotation structure for easier template access
    if "existing_annotations" in data:
        for ann in data["existing_annotations"]:
            # If review exists, flatten it for easier access
            if "review" in ann and ann["review"]:
                review = ann["review"]
                ann["action"] = review.get("action", "UNDECIDED")
                ann["reason"] = review.get("reason", "")
                ann["summary"] = review.get("summary", "")
                ann["proposed_replacement_terms"] = review.get(
                    "proposed_replacement_terms", []
                )
            elif "action" not in ann:
                ann["action"] = "UNDECIDED"

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

        # Deep-research reports need dedicated processing to strip generated
        # wrappers and preserve provider/model/artifact metadata.
        if is_deep_research_markdown(md_file):
            continue

        # Skip citations files (included in deep research)
        if md_file.name.endswith("-citations.md"):
            continue
        if md_file.name.endswith(".citations.md"):
            continue

        # Skip pathway files (separate HTML exists)
        if md_file.name.endswith("-pathway.md"):
            continue

        # Create a display name from the filename
        name = md_file.stem
        # Remove gene prefix if present for cleaner display
        gene_name = gene_dir.name
        if name.startswith(gene_name + "-"):
            name = name[len(gene_name) + 1 :]
        elif name.startswith(gene_name + "_"):
            name = name[len(gene_name) + 1 :]

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


def process_markdown_content(content: str, base_prefix: str = "") -> str:
    """Process markdown content to HTML with enhanced features.

    Args:
        content: Raw markdown content
        base_prefix: Optional URL/path prefix for relative links in the
            rendered HTML.

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
            return f"[PMID:{pmid}]({url})"

    content = re.sub(r'\[PMID:(\d+)(?:\s+"([^"]+)")?\]', replace_pmid, content)

    # Convert markdown to HTML with useful extensions
    md = markdown.Markdown(
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "toc",
            "attr_list",
            "def_list",
            "nl2br",  # Convert newlines to <br>
        ]
    )

    html = md.convert(content)
    html = rebase_relative_html_urls(html, base_prefix)

    return html


def _find_citations_file(md_path: Path) -> Optional[Path]:
    """Find the citations file paired with a deep-research report."""
    candidates = [
        md_path.with_name(f"{md_path.stem}-citations.md"),
        Path(f"{md_path}.citations.md"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def collect_deep_research_sections(
    gene_dir: Path,
    output_dir: Optional[Path] = None,
) -> List[Dict[str, Any]]:
    """Collect deep-research reports for a gene directory and render them."""
    sections: List[Dict[str, Any]] = []

    for md_path in sorted(gene_dir.glob("*-deep-research*.md")):
        if not md_path.is_file() or not is_deep_research_markdown(md_path):
            continue

        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError as e:
            print(f"Warning: Could not read {md_path}: {e}", file=sys.stderr)
            continue

        metadata, body = extract_deep_research_body(text)
        if not body:
            continue

        base_prefix = ""
        if output_dir is not None:
            base_prefix = os.path.relpath(
                md_path.parent.resolve(), output_dir.resolve()
            )

        html_content = process_markdown_content(body, base_prefix=base_prefix)
        provider = metadata.get("provider") or provider_from_deep_research_filename(
            md_path.name
        )
        provider_label = humanize_provider(str(provider)) if provider else None
        content_title = extract_display_title(body, md_path.stem)
        title = provider_label or content_title
        subtitle = content_title
        if subtitle.casefold() in {
            "",
            title.casefold(),
            "gene research for functional annotation",
        }:
            subtitle = None

        citations_file = _find_citations_file(md_path)
        citations_href = None
        if citations_file is not None:
            if output_dir is not None:
                citations_href = os.path.relpath(
                    citations_file.resolve(), output_dir.resolve()
                )
            else:
                citations_href = citations_file.name

        artifacts = normalize_artifact_metadata(metadata, base_prefix=base_prefix)
        sections.append(
            {
                "title": title,
                "subtitle": subtitle,
                "filename": md_path.name,
                "content": html_content,
                "provider": provider,
                "provider_label": provider_label,
                "model": metadata.get("model"),
                "citation_count": metadata.get("citation_count"),
                "citations_file": citations_file.name if citations_file else None,
                "citations_href": citations_href,
                "artifact_count": metadata.get("artifact_count", len(artifacts)),
                "artifacts": artifacts,
                "trajectory_id": metadata.get("trajectory_id"),
                "start_time": metadata.get("start_time"),
                "end_time": metadata.get("end_time"),
            }
        )

    return sections


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
    if not curie or ":" not in curie:
        return "#"

    prefix, identifier = curie.split(":", 1)

    url_patterns = {
        "GO": "https://www.ebi.ac.uk/QuickGO/term/GO:{}",
        "PMID": "https://pubmed.ncbi.nlm.nih.gov/{}",
        "NCBITaxon": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={}",
        "UniProtKB": "https://www.uniprot.org/uniprotkb/{}",
        "EC": "https://www.enzyme-database.org/query.php?ec={}",
        "CHEBI": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:{}",
        "CL": "https://www.ebi.ac.uk/ols/ontologies/cl/terms?iri=http://purl.obolibrary.org/obo/CL_{}",
        "UBERON": "https://www.ebi.ac.uk/ols/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_{}",
        "HP": "https://hpo.jax.org/app/browse/term/HP:{}",
        "SO": "https://www.ebi.ac.uk/ols/ontologies/so/terms?iri=http://purl.obolibrary.org/obo/SO_{}",
        "ECO": "https://www.ebi.ac.uk/ols/ontologies/eco/terms?iri=http://purl.obolibrary.org/obo/ECO_{}",
    }

    if prefix in url_patterns:
        return url_patterns[prefix].format(identifier)
    elif prefix == "GO_REF":
        return f"https://github.com/geneontology/go-site/blob/master/metadata/gorefs/goref-{identifier}.md"
    elif prefix == "file":
        # Local file references don't get URLs
        return "#"
    else:
        # Generic OBO for unknown ontologies
        return f"https://www.ebi.ac.uk/ols/search?q={curie}"


def render_html(
    data: Dict[str, Any], template_path: Path, yaml_content: str = ""
) -> str:
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
        autoescape=select_autoescape(["html", "j2"]),
    )

    # Add custom filter for CURIE to URL conversion
    env.filters["curie_to_url"] = curie_to_url

    # Load and render template
    template = env.get_template(template_path.name)
    html = template.render(gene=data, yaml_content=yaml_content)

    return html


def render_gene_review(
    yaml_path: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None,
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
    with open(yaml_path, "r") as f:
        yaml_content = f.read()

    gene_dir = yaml_path.parent

    # Set default output path before processing Markdown, so report-local
    # artifact URLs can be rebased correctly for custom output locations.
    if output_path is None:
        if yaml_path.name.endswith("-ai-review.yaml"):
            output_path = yaml_path.parent / yaml_path.name.replace(
                "-ai-review.yaml", "-ai-review.html"
            )
        else:
            output_path = yaml_path.with_suffix(".html")

    # Find and process markdown files
    markdown_files = find_markdown_files(gene_dir)
    markdown_sections = []

    for display_name, md_path in markdown_files:
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
            if content.strip():  # Only include non-empty files
                html_content = process_markdown_content(content)
                markdown_sections.append(
                    {
                        "title": display_name,
                        "filename": md_path.name,
                        "content": html_content,
                    }
                )
        except Exception as e:
            print(f"Warning: Could not process {md_path}: {e}", file=sys.stderr)

    data["deep_research_sections"] = collect_deep_research_sections(
        gene_dir,
        output_dir=output_path.parent,
    )
    data["markdown_sections"] = markdown_sections

    # Load predictions review if it exists
    gene_symbol = data.get("gene_symbol", yaml_path.stem.replace("-ai-review", ""))
    predictions_path = gene_dir / f"{gene_symbol}-predictions-review.yaml"
    if predictions_path.exists():
        predictions_data = load_gene_review(predictions_path)
        data["predictions"] = predictions_data
    else:
        data["predictions"] = None

    # Check for pathway HTML file
    pathway_html = gene_dir / f"{gene_symbol}-pathway.html"
    if pathway_html.exists():
        data["pathway_html_file"] = pathway_html.name
    else:
        data["pathway_html_file"] = None

    # Set default template if not provided
    if template_path is None:
        module_dir = Path(__file__).parent
        template_path = module_dir / "templates" / "gene_review.html.j2"
        if not template_path.exists():
            raise FileNotFoundError(f"Default template not found at {template_path}")

    # Render HTML
    html = render_html(data, template_path, yaml_content)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path


def render_all_reviews(
    directory: Path,
    template_path: Optional[Path] = None,
    pattern: str = "*-ai-review.yaml",
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
        """,
    )

    parser.add_argument(
        "input",
        type=Path,
        nargs="?",
        help="Input YAML file or directory (when using --all)",
    )

    parser.add_argument(
        "-o", "--output", type=Path, help="Output HTML file (only for single file)"
    )

    parser.add_argument(
        "-t", "--template", type=Path, help="Path to custom Jinja2 template"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Render all *-ai-review.yaml files in directory",
    )

    parser.add_argument(
        "--pattern",
        default="*-ai-review.yaml",
        help="File pattern when using --all (default: *-ai-review.yaml)",
    )

    args = parser.parse_args()

    if not args.input:
        parser.error("Input file or directory required")

    if args.all and args.output:
        parser.error("Cannot specify output file when using --all")

    try:
        if args.all:
            if not args.input.is_dir():
                parser.error(
                    f"When using --all, input must be a directory: {args.input}"
                )
            render_all_reviews(
                args.input, template_path=args.template, pattern=args.pattern
            )
        else:
            if not args.input.is_file():
                parser.error(f"Input file not found: {args.input}")
            output = render_gene_review(
                args.input, output_path=args.output, template_path=args.template
            )
            print(f"✓ Rendered to {output}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
