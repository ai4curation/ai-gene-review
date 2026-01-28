#!/usr/bin/env python
"""Render project markdown files to HTML with auto-linked gene symbols.

This module converts project markdown files (from projects/) to HTML,
automatically linking gene symbols to their corresponding gene review pages.
"""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def build_symbol_to_species_index(genes_dir: Path) -> Dict[str, List[str]]:
    """Build index mapping gene symbols to their species directories.

    Scans the genes directory structure (genes/<species>/<gene>/) and builds
    a dictionary mapping each gene symbol to the list of species it appears in.

    Args:
        genes_dir: Path to the genes directory

    Returns:
        Dictionary mapping gene symbols to list of species, e.g.:
        {'GPX4': ['human'], 'ATG7': ['human', 'yeast'], ...}

    >>> from pathlib import Path
    >>> import tempfile
    >>> import os
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     genes = Path(tmpdir) / "genes"
    ...     (genes / "human" / "GPX4").mkdir(parents=True)
    ...     (genes / "human" / "TP53").mkdir(parents=True)
    ...     (genes / "mouse" / "Gpx4").mkdir(parents=True)
    ...     index = build_symbol_to_species_index(genes)
    ...     sorted(index.keys())
    ['GPX4', 'Gpx4', 'TP53']
    >>> index['GPX4']
    ['human']
    """
    index: Dict[str, List[str]] = {}

    if not genes_dir.exists():
        return index

    for species_dir in genes_dir.iterdir():
        if not species_dir.is_dir():
            continue

        species = species_dir.name

        for gene_dir in species_dir.iterdir():
            if not gene_dir.is_dir():
                continue

            symbol = gene_dir.name

            if symbol not in index:
                index[symbol] = []
            index[symbol].append(species)

    # Sort species lists for deterministic behavior
    for symbol in index:
        index[symbol].sort()

    return index


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter from markdown content.

    Extracts YAML frontmatter delimited by '---' at the start of the file.

    Args:
        content: Raw markdown content

    Returns:
        Tuple of (frontmatter_dict, remaining_content)

    >>> fm, body = parse_frontmatter("---\\nspecies: [human]\\ntitle: Test\\n---\\n# Hello")
    >>> fm['species']
    ['human']
    >>> fm['title']
    'Test'
    >>> body.strip()
    '# Hello'

    >>> fm, body = parse_frontmatter("# No frontmatter here")
    >>> fm
    {}
    >>> body
    '# No frontmatter here'
    """
    # Check if content starts with frontmatter delimiter
    if not content.startswith('---'):
        return {}, content

    # Find the closing delimiter
    lines = content.split('\n')
    end_idx = None

    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        # No closing delimiter found
        return {}, content

    # Extract and parse frontmatter
    frontmatter_lines = lines[1:end_idx]
    frontmatter_text = '\n'.join(frontmatter_lines)

    try:
        frontmatter = yaml.safe_load(frontmatter_text) or {}
    except yaml.YAMLError:
        frontmatter = {}

    # Return remaining content (after the closing ---)
    remaining = '\n'.join(lines[end_idx + 1:])

    return frontmatter, remaining


def replace_gene_symbols(
    content: str,
    symbol_index: Dict[str, List[str]],
    species_hints: Optional[List[str]] = None,
    base_path: str = "../../genes",
) -> Tuple[str, List[str]]:
    """Replace gene symbols in markdown content with links to gene review pages.

    Finds gene symbols at word boundaries and replaces them with markdown links.
    Handles bold symbols (**SYMBOL**) and plain symbols.

    Args:
        content: Markdown content to process
        symbol_index: Dictionary mapping symbols to species lists
        species_hints: Optional list of species to prefer for ambiguous symbols
        base_path: Relative path prefix from output location to genes directory

    Returns:
        Tuple of (modified_content, list_of_warnings)

    >>> index = {'GPX4': ['human'], 'ATG7': ['human', 'yeast']}
    >>> content, warnings = replace_gene_symbols("**GPX4** is important", index)
    >>> "GPX4" in content and "human" in content
    True
    >>> len(warnings)
    0

    >>> content, warnings = replace_gene_symbols("ATG7 is ambiguous", index)
    >>> "ATG7" in warnings[0]
    True
    """
    warnings: List[str] = []
    species_hints = species_hints or []

    # Track which symbols we've already processed to avoid duplicate warnings
    processed_ambiguous: set = set()

    def resolve_species(symbol: str) -> Optional[str]:
        """Resolve which species to link for a symbol."""
        if symbol not in symbol_index:
            return None

        species_list = symbol_index[symbol]

        if len(species_list) == 1:
            return species_list[0]

        # Try to resolve using species hints
        matching = [s for s in species_list if s in species_hints]

        if len(matching) == 1:
            return matching[0]

        # Still ambiguous
        if symbol not in processed_ambiguous:
            processed_ambiguous.add(symbol)
            warnings.append(
                f"Ambiguous symbol '{symbol}' found in species: {', '.join(species_list)}. "
                f"Add 'species: [{species_list[0]}]' to frontmatter to resolve."
            )

        return None

    def make_link(symbol: str, species: str) -> str:
        """Create a markdown link to the gene review page."""
        url = f"{base_path}/{species}/{symbol}/{symbol}-ai-review.html"
        return f"[{symbol}]({url})"

    def replace_match(match: re.Match) -> str:
        """Replace a matched symbol with a link if resolvable."""
        full_match = match.group(0)
        symbol = match.group('symbol')

        species = resolve_species(symbol)

        if species is None:
            return full_match

        link = make_link(symbol, species)

        # Preserve bold markers if present
        if full_match.startswith('**') and full_match.endswith('**'):
            return f"**{link}**"

        return link

    # Build regex pattern for all known symbols
    # Sort by length (longest first) to avoid partial matches
    symbols = sorted(symbol_index.keys(), key=len, reverse=True)

    if not symbols:
        return content, warnings

    # Escape special regex characters in symbols
    escaped_symbols = [re.escape(s) for s in symbols]
    symbols_pattern = '|'.join(escaped_symbols)

    # Pattern to match:
    # 1. Bold symbols: **SYMBOL**
    # 2. Plain symbols at word boundaries
    # Negative lookbehind for alphanumeric/underscore to avoid partial matches
    # Negative lookahead for alphanumeric/underscore/hyphen to avoid partial matches
    pattern = rf'(?P<bold>\*\*)?(?P<symbol>{symbols_pattern})(?P=bold)?(?![a-zA-Z0-9_-])'

    # Use a more careful approach: only match at word boundaries
    # This pattern handles:
    # - Start of line or after whitespace/punctuation
    # - End of line or before whitespace/punctuation
    pattern = rf'(?<![a-zA-Z0-9_])(?P<bold>\*\*)?(?P<symbol>{symbols_pattern})(?(bold)\*\*)(?![a-zA-Z0-9_-])'

    result = re.sub(pattern, replace_match, content)

    return result, warnings


def process_markdown_content(content: str) -> str:
    """Convert markdown content to HTML with useful extensions.

    Handles mermaid diagrams, tables, code blocks, etc.

    Args:
        content: Markdown content

    Returns:
        HTML content
    """
    # Process mermaid blocks for HTML
    def replace_mermaid(match: re.Match) -> str:
        mermaid_code = match.group(1)
        return f'\n<div class="mermaid">\n{mermaid_code}\n</div>'

    # Replace mermaid code blocks with div elements
    processed = re.sub(
        r'```mermaid\n(.*?)\n```',
        replace_mermaid,
        content,
        flags=re.DOTALL
    )

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'codehilite',
        'toc',
        'attr_list',
        'def_list',
        'nl2br',
    ])

    return md.convert(processed)


def render_project(
    md_path: Path,
    output_dir: Path = Path("pages/projects"),
    genes_dir: Path = Path("genes"),
    template_path: Optional[Path] = None,
) -> Tuple[Path, List[str]]:
    """Render a single project markdown file to HTML.

    Args:
        md_path: Path to the markdown file
        output_dir: Directory for output HTML files
        genes_dir: Path to the genes directory for building symbol index
        template_path: Optional path to custom Jinja2 template

    Returns:
        Tuple of (output_path, list_of_warnings)

    Raises:
        FileNotFoundError: If markdown file doesn't exist
    """
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    # Read content and parse frontmatter
    raw_content = md_path.read_text()
    frontmatter, content = parse_frontmatter(raw_content)

    # Build symbol index
    symbol_index = build_symbol_to_species_index(genes_dir)

    # Get species hints from frontmatter
    species_hints = frontmatter.get('species', [])
    if isinstance(species_hints, str):
        species_hints = [species_hints]

    # Replace gene symbols with links
    linked_content, warnings = replace_gene_symbols(
        content,
        symbol_index,
        species_hints=species_hints,
        base_path="../../genes",
    )

    # Convert to HTML
    html_content = process_markdown_content(linked_content)

    # Determine title
    title = frontmatter.get('title')
    if not title:
        # Try to extract from first heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            title = heading_match.group(1).strip()
        else:
            title = md_path.stem

    # Set up template
    if template_path is None:
        module_dir = Path(__file__).parent
        template_path = module_dir / "templates" / "project.html.j2"

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(template_path.parent),
        autoescape=select_autoescape(['html', 'j2'])
    )
    template = env.get_template(template_path.name)

    # Render HTML
    html = template.render(
        title=title,
        content=html_content,
        source_file=md_path.name,
        warnings=warnings,
        frontmatter=frontmatter,
    )

    # Create output directory and write file
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{md_path.stem}.html"
    output_path.write_text(html)

    return output_path, warnings


def render_all_projects(
    projects_dir: Path = Path("projects"),
    output_dir: Path = Path("pages/projects"),
    genes_dir: Path = Path("genes"),
) -> Tuple[List[Path], List[str]]:
    """Render all project markdown files to HTML.

    Args:
        projects_dir: Directory containing project markdown files
        output_dir: Directory for output HTML files
        genes_dir: Path to the genes directory

    Returns:
        Tuple of (list_of_output_paths, list_of_all_warnings)
    """
    output_paths: List[Path] = []
    all_warnings: List[str] = []

    if not projects_dir.exists():
        print(f"Projects directory not found: {projects_dir}")
        return output_paths, all_warnings

    md_files = sorted(projects_dir.glob("*.md"))

    if not md_files:
        print(f"No markdown files found in {projects_dir}")
        return output_paths, all_warnings

    print(f"Found {len(md_files)} project files to render")

    for md_file in md_files:
        try:
            output_path, warnings = render_project(
                md_file,
                output_dir=output_dir,
                genes_dir=genes_dir,
            )
            output_paths.append(output_path)

            if warnings:
                all_warnings.extend([f"{md_file.name}: {w}" for w in warnings])
                print(f"  {md_file.name} -> {output_path.name} ({len(warnings)} warnings)")
            else:
                print(f"  {md_file.name} -> {output_path.name}")

        except Exception as e:
            print(f"  {md_file.name}: ERROR - {e}")
            all_warnings.append(f"{md_file.name}: Error rendering - {e}")

    print(f"\nRendered {len(output_paths)}/{len(md_files)} projects to {output_dir}")

    if all_warnings:
        print(f"\n{len(all_warnings)} warnings:")
        for warning in all_warnings[:10]:  # Show first 10
            print(f"  - {warning}")
        if len(all_warnings) > 10:
            print(f"  ... and {len(all_warnings) - 10} more")

    return output_paths, all_warnings


if __name__ == "__main__":
    # Simple CLI for testing
    import sys

    if len(sys.argv) < 2:
        print("Usage: python render_projects.py <project.md> [output_dir]")
        print("       python render_projects.py --all")
        sys.exit(1)

    if sys.argv[1] == "--all":
        render_all_projects()
    else:
        md_path = Path(sys.argv[1])
        output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("pages/projects")
        output_path, warnings = render_project(md_path, output_dir)
        print(f"Rendered to: {output_path}")
        if warnings:
            print(f"Warnings: {warnings}")
