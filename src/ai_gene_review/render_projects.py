#!/usr/bin/env python
"""Render project markdown files to HTML with auto-linked gene symbols.

This module converts project markdown files (from projects/) to HTML,
automatically linking gene symbols to their corresponding gene review pages.
"""

import re
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import unquote, urlparse

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

MARKDOWN_SUFFIXES = {".md", ".markdown"}
NOTEBOOK_SUFFIXES = {".ipynb"}


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


def _frontmatter_bool(value: Any, default: bool) -> bool:
    """Parse a permissive boolean-like frontmatter value."""
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "yes", "on", "1"}:
            return True
        if normalized in {"false", "no", "off", "0"}:
            return False
    if isinstance(value, (int, float)):
        return bool(value)
    return default


def should_autolink_gene_symbols(frontmatter: Dict[str, Any]) -> bool:
    """Return whether automatic prose gene-symbol linking should run.

    The default remains on for project pages. Use
    ``autolink_gene_symbols: false`` in frontmatter for paper-like pages where
    prose gene symbols should not become review links. ``suppress_gene_symbol_links``
    is accepted as an explicit inverse alias.
    """
    if "autolink_gene_symbols" in frontmatter:
        return _frontmatter_bool(frontmatter["autolink_gene_symbols"], default=True)
    if "auto_link_gene_symbols" in frontmatter:
        return _frontmatter_bool(frontmatter["auto_link_gene_symbols"], default=True)
    if "suppress_gene_symbol_links" in frontmatter:
        return not _frontmatter_bool(
            frontmatter["suppress_gene_symbol_links"],
            default=False,
        )
    return True


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
        """Resolve which species to link for a symbol.

        ``species_hints`` is treated as a *priority-ordered* preference list: the
        first hinted species that actually has a review for the symbol wins. This
        lets a multi-species project list every species it covers (so the
        all-projects table is complete) while still disambiguating symbols that
        exist in more than one of those species.
        """
        if symbol not in symbol_index:
            return None

        species_list = symbol_index[symbol]

        if len(species_list) == 1:
            return species_list[0]

        # Resolve using the priority-ordered species hints: first match wins.
        for hint in species_hints:
            if hint in species_list:
                return hint

        # Still ambiguous: no hint matched any species carrying this symbol.
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
    # Sort by length (longest first) to avoid partial matches.
    # Exclude very short symbols from prose auto-linking. One- and two-character gene
    # names are common enough in this repository to be valid review folders, but they
    # also collide with ordinary text such as "don't", author initials, and allele
    # suffixes. Link those through explicit <gene> tags instead.
    symbols = sorted(
        (s for s in symbol_index.keys() if len(s) >= 3 and not s.isdigit()),
        key=len,
        reverse=True,
    )

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
    pattern = rf'(?<![a-zA-Z0-9_/])(?P<bold>\*\*)?(?P<symbol>{symbols_pattern})(?(bold)\*\*)(?![a-zA-Z0-9_-])'

    symbol_regex = re.compile(pattern)
    preserve_regex = re.compile(
        r'(?P<fenced>```.*?```)'
        r'|(?P<code>`[^`]*`)'
        r'|(?P<link>\[[^\]]*\]\([^)]*\))',
        flags=re.DOTALL,
    )

    # Do not auto-link inside code spans/blocks or existing markdown links.
    # Project pages often use code spans for literal identifiers, and linking
    # inside them creates malformed markdown such as `[gene](...)/P12345`.
    parts: List[str] = []
    last_end = 0
    for match in preserve_regex.finditer(content):
        if match.start() > last_end:
            parts.append(symbol_regex.sub(replace_match, content[last_end:match.start()]))
        parts.append(match.group(0))
        last_end = match.end()

    if last_end < len(content):
        parts.append(symbol_regex.sub(replace_match, content[last_end:]))

    result = ''.join(parts)

    return result, warnings


def replace_gene_tags(
    content: str,
    genes_dir: Path,
    base_path: str = "../../genes",
) -> Tuple[str, List[str]]:
    """Replace explicit ``<gene>`` tags with links to gene review pages.

    This is for project-page examples whose visible text is not just the gene
    symbol, such as ``E/P00720`` or ``M2/F8IZX5``. The tag must specify the
    report target explicitly:

    ``<gene species="BPT4" symbol="E">E/P00720</gene>``
    """
    warnings: List[str] = []
    tag_regex = re.compile(
        r"<gene\b(?P<attrs>[^>]*)>(?P<label>.*?)</gene>",
        flags=re.DOTALL,
    )
    attr_regex = re.compile(
        r"""([A-Za-z_][\w:-]*)\s*=\s*(?:"([^"]*)"|'([^']*)')"""
    )

    def replace_tag(match: re.Match) -> str:
        attrs = {
            attr_match.group(1): attr_match.group(2) or attr_match.group(3) or ""
            for attr_match in attr_regex.finditer(match.group("attrs"))
        }
        label = match.group("label").strip()
        species = attrs.get("species")
        symbol = attrs.get("symbol")

        if not species or not symbol:
            warnings.append(
                f"Gene tag is missing required species/symbol attributes: {match.group(0)}"
            )
            return label or match.group(0)

        if not label:
            label = symbol

        target_dir = genes_dir / species / symbol
        if not target_dir.exists():
            warnings.append(
                f"Gene tag target not found for species='{species}' symbol='{symbol}'"
            )
            return label

        url = f"{base_path}/{species}/{symbol}/{symbol}-ai-review.html"
        return f"[{label}]({url})"

    return tag_regex.sub(replace_tag, content), warnings


# UniProt-style species mnemonics are five uppercase alphanumerics (e.g. ARATH,
# POPTR, 9INFA). A few model organisms use lowercase common-name directories
# instead; keep that an explicit small allowlist so the regex stays precise.
SPECIES_CODE_EXCEPTIONS = ("human", "mouse", "rat", "worm", "yeast")


def replace_species_qualified_symbols(
    content: str,
    genes_dir: Path,
    base_path: str = "../../genes",
) -> Tuple[str, List[str]]:
    """Replace ``CODE/symbol`` prose references with gene-review links.

    This is the lightweight inline convention for disambiguating gene symbols in
    multi-species project prose, where a bare symbol (e.g. ``CASPL4C1``) is
    ambiguous because reviews exist in several species. Writing the species code
    in front -- ``POPTR/CASPL4C1`` -- links to that species' review explicitly,
    without hardcoding any path. The rendered link keeps the full ``CODE/symbol``
    text, which is informative in a cross-species document.

    ``CODE`` must be a five-character uppercase UniProt mnemonic (e.g. ``ARATH``,
    ``POPTR``, ``9INFA``) or one of a small set of lowercase model-organism
    directory names (``human``, ``mouse``, ``rat``, ``worm``, ``yeast``). The
    reference is only linked when ``genes/CODE/symbol/`` actually exists, so the
    regex can stay permissive while precision comes from the filesystem check. A
    ``CODE`` that is itself a known species directory but whose ``symbol`` is
    missing yields a warning (likely a typo); anything else is left untouched.

    >>> from pathlib import Path
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory() as tmp:
    ...     g = Path(tmp) / "genes"
    ...     (g / "POPTR" / "CASPL4C1").mkdir(parents=True)
    ...     out, warns = replace_species_qualified_symbols(
    ...         "See POPTR/CASPL4C1 for detail.", g)
    ...     ("[POPTR/CASPL4C1](" in out, warns)
    (True, [])
    """
    warnings: List[str] = []

    code_alt = "|".join(["[A-Z0-9]{5}", *(re.escape(c) for c in SPECIES_CODE_EXCEPTIONS)])
    # Not preceded by a word char or '/' (so paths like genes/POPTR/CASPL4C1 do
    # not match), CODE/symbol, not followed by a word char.
    pattern = re.compile(
        rf"(?<![A-Za-z0-9_/])"
        rf"(?P<code>{code_alt})"
        # Symbols may contain internal '.'/'-' (e.g. NaPMT1.1, lrx-1) but must
        # start and end on an alphanumeric so trailing punctuation is excluded.
        rf"/(?P<symbol>[A-Za-z0-9](?:[\w.\-]*[A-Za-z0-9])?)"
        rf"(?![A-Za-z0-9_])"
    )
    preserve_regex = re.compile(
        r'(?P<fenced>```.*?```)'
        r'|(?P<code>`[^`]*`)'
        r'|(?P<link>\[[^\]]*\]\([^)]*\))',
        flags=re.DOTALL,
    )

    def replace_match(match: re.Match) -> str:
        code = match.group("code")
        symbol = match.group("symbol")
        if (genes_dir / code / symbol).is_dir():
            url = f"{base_path}/{code}/{symbol}/{symbol}-ai-review.html"
            return f"[{code}/{symbol}]({url})"
        # Only warn when CODE is clearly a species directory we know about, so a
        # stray "ABOUT/foo" in prose stays silent.
        if (genes_dir / code).is_dir():
            warnings.append(
                f"Species-qualified symbol '{code}/{symbol}' not found "
                f"(no genes/{code}/{symbol})."
            )
        return match.group(0)

    # Do not link inside code spans/blocks or existing markdown links.
    parts: List[str] = []
    last_end = 0
    for match in preserve_regex.finditer(content):
        if match.start() > last_end:
            parts.append(pattern.sub(replace_match, content[last_end:match.start()]))
        parts.append(match.group(0))
        last_end = match.end()
    if last_end < len(content):
        parts.append(pattern.sub(replace_match, content[last_end:]))

    return "".join(parts), warnings


def link_uniprot_code_spans(
    content: str,
    base_url: str = "https://www.uniprot.org/uniprotkb/",
) -> str:
    """Replace backticked ``symbol/accession`` samples with UniProt links.

    Project review pages use these code spans for row-level SPKW spot checks
    where there is no local AIGR gene-review page. Linking them makes the
    sampled evidence inspectable without confusing them with local reviews.
    """
    accession = (
        r"(?:[OPQ][0-9][A-Z0-9]{3}[0-9]"
        r"|[A-NR-Z][0-9][A-Z][A-Z0-9]{2}[0-9](?:[A-Z][A-Z0-9]{2}[0-9])?)"
    )
    pattern = re.compile(
        rf"`(?:(?P<label>[^`/\s]+/(?P<accession>{accession}))"
        rf"|(?P<bare_accession>{accession}))`"
    )

    def replace_match(match: re.Match) -> str:
        label = match.group("label") or match.group("bare_accession")
        accession = match.group("accession") or match.group("bare_accession")
        return f"[{label}]({base_url}{accession}/entry)"

    return pattern.sub(replace_match, content)


def link_go_ids(
    content: str,
    base_url: str = "http://amigo.geneontology.org/amigo/term/",
) -> str:
    """Replace bare GO IDs in markdown with links to AmiGO.

    Only links GO IDs that are not already inside markdown links ``[...](...)``
    or inline code backticks.

    Args:
        content: Markdown content to process
        base_url: URL prefix for GO term links

    Returns:
        Content with bare GO IDs converted to markdown links

    >>> link_go_ids("GO:0051082 is important")
    '[GO:0051082](http://amigo.geneontology.org/amigo/term/GO:0051082) is important'

    >>> link_go_ids("[GO:0051082](http://example.com)")
    '[GO:0051082](http://example.com)'

    >>> link_go_ids("`GO:0051082`")
    '`GO:0051082`'

    >>> link_go_ids("uses GO:0044183 and GO:0051082")
    'uses [GO:0044183](http://amigo.geneontology.org/amigo/term/GO:0044183) and [GO:0051082](http://amigo.geneontology.org/amigo/term/GO:0051082)'

    >>> link_go_ids("[already linked GO:0051082](some-url) but GO:0044183 is bare")
    '[already linked GO:0051082](some-url) but [GO:0044183](http://amigo.geneontology.org/amigo/term/GO:0044183) is bare'
    """
    # Match (in priority order):
    # 1. Fenced code blocks ```...``` — preserve
    # 2. Inline code `...` — preserve
    # 3. Markdown links [...](...) — preserve
    # 4. Bare GO:NNNNNNN — replace with link
    pattern = (
        r'(?P<fenced>```.*?```)'
        r'|(?P<code>`[^`]*`)'
        r'|(?P<link>\[[^\]]*\]\([^)]*\))'
        r'|(?P<go_id>GO:\d{7})'
    )

    def _replace(match: re.Match) -> str:
        if match.group('go_id'):
            go_id = match.group('go_id')
            return f"[{go_id}]({base_url}{go_id})"
        return match.group(0)

    return re.sub(pattern, _replace, content, flags=re.DOTALL)


def process_markdown_content(content: str) -> str:
    """Convert markdown content to HTML with useful extensions.

    Handles mermaid diagrams, tables, code blocks, rendered-source link
    conversion, etc.

    Args:
        content: Markdown content

    Returns:
        HTML content

    >>> process_markdown_content("[link](foo.md)")
    '<p><a href="foo.html">link</a></p>'
    >>> process_markdown_content("[link](SPKW-APOPTOSIS.md)")
    '<p><a href="SPKW-APOPTOSIS.html">link</a></p>'
    >>> process_markdown_content("[link](../other/file.md)")
    '<p><a href="../other/file.html">link</a></p>'
    >>> process_markdown_content("[nb](notebooks/example.ipynb)")
    '<p><a href="notebooks/example.ipynb.html">nb</a></p>'
    >>> "http://example.com/page.md" in process_markdown_content("[ext](http://example.com/page.md)")
    True
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

    def convert_rendered_link(match: re.Match) -> str:
        text = match.group(1)
        url = match.group(2)
        parsed = urlparse(url)
        if parsed.scheme or parsed.netloc:
            return match.group(0)

        path = parsed.path
        lower_path = path.lower()
        if lower_path.endswith(".md"):
            path = path[:-3] + ".html"
        elif lower_path.endswith(".markdown"):
            path = path[:-9] + ".html"
        elif lower_path.endswith(".ipynb"):
            path = path + ".html"

        url = parsed._replace(path=path).geturl()
        return f'[{text}]({url})'

    processed = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        convert_rendered_link,
        processed
    )

    # Enable markdown processing inside HTML blocks like <details>
    processed = processed.replace('<details>', '<details markdown="1">')

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'codehilite',
        'toc',
        'attr_list',
        'def_list',
        'nl2br',
        'md_in_html',
    ])

    return md.convert(processed)


def project_bundle_markdown_files(md_path: Path, projects_dir: Path) -> List[Path]:
    """Return markdown files that belong to a top-level project page.

    Rendering ``projects/FOO.md`` should include supporting pages under
    ``projects/FOO/``. Rendering a file that is already inside a support folder
    remains scoped to that single file.
    """
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    md_path = md_path.resolve()
    projects_root = projects_dir.resolve()
    files = [md_path]

    if md_path.is_relative_to(projects_root):
        rel_path = md_path.relative_to(projects_root)
        if len(rel_path.parts) == 1 and md_path.suffix.lower() in MARKDOWN_SUFFIXES:
            support_dir = projects_root / md_path.stem
            if support_dir.is_dir():
                files.extend(sorted(support_dir.rglob("*.md")))

    # De-duplicate while preserving deterministic order.
    seen: set[Path] = set()
    unique_files: List[Path] = []
    for file_path in files:
        resolved = file_path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique_files.append(resolved)

    return unique_files


def _extract_local_reference_urls(markdown_content: str) -> List[str]:
    """Extract raw URLs from markdown links/images and simple HTML attrs."""
    urls: List[str] = []
    urls.extend(
        match.group(1)
        for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", markdown_content)
    )
    urls.extend(
        match.group(1)
        for match in re.finditer(
            r"\b(?:src|href)\s*=\s*[\"']([^\"']+)[\"']",
            markdown_content,
            flags=re.IGNORECASE,
        )
    )
    urls.extend(
        match.group(1)
        for match in re.finditer(
            r"^\s*\[[^\]]+\]:\s*(\S+)",
            markdown_content,
            flags=re.MULTILINE,
        )
    )
    return urls


def _local_url_path(url: str) -> Optional[str]:
    """Return a filesystem path for a local URL, or None for non-local URLs."""
    url = url.strip()
    if not url or url.startswith("#"):
        return None
    if url.startswith("<") and url.endswith(">"):
        url = url[1:-1]

    # Drop optional markdown title text from forms like: image.png "caption".
    url = url.split()[0]
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or parsed.path.startswith("/"):
        return None
    if not parsed.path:
        return None

    return unquote(parsed.path)


def _referenced_local_files(md_path: Path, projects_dir: Path) -> List[Path]:
    """Find existing local files referenced by a markdown file."""
    root = projects_dir.resolve()
    files: List[Path] = []
    seen: set[Path] = set()

    for url in _extract_local_reference_urls(md_path.read_text()):
        local_path = _local_url_path(url)
        if local_path is None:
            continue

        candidate = (md_path.parent / local_path).resolve()
        if not candidate.is_file():
            continue
        if not candidate.is_relative_to(root):
            continue
        if candidate in seen:
            continue

        seen.add(candidate)
        files.append(candidate)

    return files


def referenced_local_assets(md_path: Path, projects_dir: Path) -> List[Path]:
    """Find non-rendered local assets referenced by a markdown file."""
    return [
        path
        for path in _referenced_local_files(md_path, projects_dir)
        if path.suffix.lower() not in MARKDOWN_SUFFIXES | NOTEBOOK_SUFFIXES
    ]


def referenced_local_notebooks(md_path: Path, projects_dir: Path) -> List[Path]:
    """Find local notebooks referenced by a markdown file."""
    return [
        path
        for path in _referenced_local_files(md_path, projects_dir)
        if path.suffix.lower() in NOTEBOOK_SUFFIXES
    ]


def _flatten_sidecar_values(value: Any) -> List[str]:
    """Return string paths nested under a sidecars frontmatter value."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        paths: List[str] = []
        for nested_value in value.values():
            paths.extend(_flatten_sidecar_values(nested_value))
        return paths
    if isinstance(value, (list, tuple, set)):
        paths = []
        for nested_value in value:
            paths.extend(_flatten_sidecar_values(nested_value))
        return paths
    return []


def referenced_frontmatter_sidecars(md_path: Path, projects_dir: Path) -> List[Path]:
    """Find local files declared under ``sidecars:`` frontmatter."""
    frontmatter, _ = parse_frontmatter(md_path.read_text())
    sidecars = frontmatter.get("sidecars")
    if sidecars is None:
        return []

    root = projects_dir.resolve()
    files: List[Path] = []
    seen: set[Path] = set()

    for url in _flatten_sidecar_values(sidecars):
        local_path = _local_url_path(url)
        if local_path is None:
            continue

        candidate = (md_path.parent / local_path).resolve()
        if not candidate.is_file():
            continue
        if not candidate.is_relative_to(root):
            continue
        if candidate.suffix.lower() in MARKDOWN_SUFFIXES | NOTEBOOK_SUFFIXES:
            continue
        if candidate in seen:
            continue

        seen.add(candidate)
        files.append(candidate)

    return files


def notebook_output_path(
    notebook_path: Path,
    output_dir: Path,
    projects_dir: Path,
) -> Path:
    """Return the mirrored HTML path for a project notebook."""
    rel_path = notebook_path.resolve().relative_to(projects_dir.resolve())
    return output_dir.resolve() / Path(str(rel_path) + ".html")


def render_notebook(
    notebook_path: Path,
    output_dir: Path,
    projects_dir: Path,
) -> List[Path]:
    """Render an existing notebook to static HTML without executing it."""
    import nbformat
    from nbconvert import HTMLExporter

    output_path = notebook_output_path(notebook_path, output_dir, projects_dir)

    with notebook_path.open(encoding="utf-8") as handle:
        notebook = nbformat.read(handle, as_version=4)

    html, resources = HTMLExporter().from_notebook_node(notebook)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    output_paths = [output_path]

    # Most nbconvert HTML output embeds rich outputs, but some exporters may
    # emit sibling resource files. Preserve those if present.
    for name, data in resources.get("outputs", {}).items():
        resource_path = (output_path.parent / name).resolve()
        if resource_path.is_relative_to(output_path.parent.resolve()):
            resource_path.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(data, bytes):
                resource_path.write_bytes(data)
            else:
                resource_path.write_text(str(data), encoding="utf-8")
            output_paths.append(resource_path)

    return output_paths


def convert_referenced_notebooks(
    md_files: List[Path],
    output_dir: Path,
    projects_dir: Path,
) -> Tuple[List[Path], List[str]]:
    """Render notebooks referenced by project markdown files."""
    output_paths: List[Path] = []
    warnings: List[str] = []
    seen_notebooks: set[Path] = set()

    for md_file in md_files:
        for notebook_path in referenced_local_notebooks(md_file, projects_dir):
            if notebook_path in seen_notebooks:
                continue
            seen_notebooks.add(notebook_path)

            try:
                output_paths.extend(
                    render_notebook(
                        notebook_path,
                        output_dir=output_dir,
                        projects_dir=projects_dir,
                    )
                )
            except Exception as e:
                warnings.append(
                    f"{notebook_path.name}: Error rendering notebook - {e}"
                )

    return output_paths, warnings


def copy_referenced_assets(
    md_files: List[Path],
    output_dir: Path,
    projects_dir: Path,
    rendered_paths: Optional[List[Path]] = None,
) -> List[Path]:
    """Copy local assets referenced by markdown content or sidecar metadata."""
    projects_root = projects_dir.resolve()
    output_root = output_dir.resolve()
    rendered = {path.resolve() for path in (rendered_paths or [])}
    copied: List[Path] = []
    seen_assets: set[Path] = set()

    for md_file in md_files:
        asset_paths = referenced_local_assets(
            md_file,
            projects_dir,
        ) + referenced_frontmatter_sidecars(md_file, projects_dir)
        for asset_path in asset_paths:
            if asset_path in seen_assets:
                continue
            seen_assets.add(asset_path)

            rel_path = asset_path.resolve().relative_to(projects_root)
            output_path = output_root / rel_path
            if output_path.resolve() in rendered:
                continue

            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(asset_path, output_path)
            copied.append(output_path)

    return copied


def render_project(
    md_path: Path,
    output_dir: Path = Path("pages/projects"),
    genes_dir: Path = Path("genes"),
    template_path: Optional[Path] = None,
    projects_dir: Optional[Path] = None,
) -> Tuple[Path, List[str]]:
    """Render a single project markdown file to HTML.

    Projects follow the ``FOO.md`` + ``FOO/`` convention: a project is a
    top-level markdown file, optionally accompanied by a same-named folder
    holding supporting material (sub-pages, data, scripts). When ``projects_dir``
    is supplied, any subfolder structure is mirrored into ``output_dir`` so that
    ``FOO/bar.md`` renders to ``FOO/bar.html`` and relative links between a
    project page and its supporting pages resolve unchanged.

    Args:
        md_path: Path to the markdown file
        output_dir: Directory for output HTML files
        genes_dir: Path to the genes directory for building symbol index
        template_path: Optional path to custom Jinja2 template
        projects_dir: Root projects directory; when given, the output path
            mirrors ``md_path``'s location relative to it. When ``None`` the
            file is rendered flat as ``output_dir/<stem>.html``.

    Returns:
        Tuple of (output_path, list_of_warnings)

    Raises:
        FileNotFoundError: If markdown file doesn't exist
    """
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    # Determine the output path (mirroring any project subfolder structure) and
    # how deep the rendered file sits, so links back to genes/ use the right
    # number of ``../`` segments.
    if projects_dir is not None and md_path.resolve().is_relative_to(
        projects_dir.resolve()
    ):
        rel_path = md_path.resolve().relative_to(projects_dir.resolve())
    else:
        rel_path = Path(md_path.name)
    subdir_depth = len(rel_path.parts) - 1
    # From pages/projects/<...>.html the repo-root genes/ dir is two levels up,
    # plus one extra level per project subfolder.
    genes_base_path = "../" * (2 + subdir_depth) + "genes"

    # Read content and parse frontmatter
    raw_content = md_path.read_text()
    frontmatter, content = parse_frontmatter(raw_content)

    # Build symbol index
    symbol_index = build_symbol_to_species_index(genes_dir)

    # Get species hints from frontmatter
    species_hints = frontmatter.get('species', [])
    if isinstance(species_hints, str):
        species_hints = [species_hints]

    # Replace explicit gene tags first. The generated markdown links are then
    # preserved by the ordinary auto-linker.
    content, tag_warnings = replace_gene_tags(
        content,
        genes_dir=genes_dir,
        base_path=genes_base_path,
    )

    # Resolve explicit ``CODE/symbol`` species-qualified references next. These
    # disambiguate symbols shared across species without hardcoding paths, and
    # the generated links are preserved by the bare-symbol auto-linker below.
    content, qualified_warnings = replace_species_qualified_symbols(
        content,
        genes_dir=genes_dir,
        base_path=genes_base_path,
    )

    # Replace prose gene symbols with links unless the page opts out. Explicit
    # <gene> tags above still link because they are intentional, not automatic.
    if should_autolink_gene_symbols(frontmatter):
        linked_content, symbol_warnings = replace_gene_symbols(
            content,
            symbol_index,
            species_hints=species_hints,
            base_path=genes_base_path,
        )
    else:
        linked_content, symbol_warnings = content, []
    warnings = tag_warnings + qualified_warnings + symbol_warnings

    # Link raw SPKW sample rows such as `MCP/P06491` to UniProt. Local review
    # links are already explicit via <gene> tags or ordinary symbol autolinks.
    linked_content = link_uniprot_code_spans(linked_content)

    # Auto-link bare GO IDs
    linked_content = link_go_ids(linked_content)

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

    # Create output directory and write file, mirroring subfolder structure
    output_path = output_dir / rel_path.with_suffix(".html")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html)

    return output_path, warnings


def readme_index_alias_path(
    md_path: Path,
    output_path: Path,
    projects_dir: Path,
) -> Optional[Path]:
    """Return the support-folder index alias path for a README page."""
    if md_path.name.lower() != "readme.md":
        return None

    md_path = md_path.resolve()
    projects_root = projects_dir.resolve()
    if not md_path.is_relative_to(projects_root):
        return None

    rel_path = md_path.relative_to(projects_root)
    if len(rel_path.parts) <= 1:
        return None

    return output_path.with_name("index.html")


def write_readme_index_alias(
    md_path: Path,
    output_path: Path,
    projects_dir: Path,
) -> Optional[Path]:
    """Write index.html next to rendered support-folder README.html."""
    index_path = readme_index_alias_path(md_path, output_path, projects_dir)
    if index_path is None:
        return None

    index_path.write_text(output_path.read_text(encoding="utf-8"), encoding="utf-8")
    return index_path


def render_project_bundle(
    md_path: Path,
    output_dir: Path = Path("pages/projects"),
    genes_dir: Path = Path("genes"),
    template_path: Optional[Path] = None,
    projects_dir: Path = Path("projects"),
) -> Tuple[List[Path], List[str]]:
    """Render a project page plus its same-named supporting folder.

    This is the public "render a project" behavior used by the CLI. For a
    top-level ``projects/FOO.md`` file it renders both that file and every
    ``*.md`` file under ``projects/FOO/``. It also renders linked notebooks,
    writes ``index.html`` aliases for support-folder READMEs, and copies local
    non-rendered assets while preserving paths under ``output_dir``.
    """
    md_files = project_bundle_markdown_files(md_path, projects_dir)
    output_paths: List[Path] = []
    all_warnings: List[str] = []

    for bundle_file in md_files:
        output_path, warnings = render_project(
            bundle_file,
            output_dir=output_dir,
            genes_dir=genes_dir,
            template_path=template_path,
            projects_dir=projects_dir,
        )
        output_paths.append(output_path)
        index_path = write_readme_index_alias(bundle_file, output_path, projects_dir)
        if index_path is not None:
            output_paths.append(index_path)
        if warnings:
            all_warnings.extend([f"{bundle_file.name}: {w}" for w in warnings])

    notebook_paths, notebook_warnings = convert_referenced_notebooks(
        md_files,
        output_dir=output_dir,
        projects_dir=projects_dir,
    )
    output_paths.extend(notebook_paths)
    all_warnings.extend(notebook_warnings)

    copied_assets = copy_referenced_assets(
        md_files,
        output_dir=output_dir,
        projects_dir=projects_dir,
        rendered_paths=output_paths,
    )
    output_paths.extend(copied_assets)

    return output_paths, all_warnings


def latest_review_status(manual_reviews: Any) -> Optional[str]:
    """Return the ``status`` of the most recent manual review, if any.

    ``manual_reviews`` is the optional project-frontmatter list of reviewer
    sign-offs. The "most recent" entry is the one with the greatest ``date``
    (ISO ``YYYY-MM-DD`` sorts lexicographically); entries without a date sort
    earliest. Returns ``None`` when there are no reviews or the latest carries
    no status.

    >>> latest_review_status([
    ...     {"reviewed_by": "cjm", "date": "2024-01-01", "status": "CHANGES_REQUESTED"},
    ...     {"reviewed_by": "cjm", "date": "2024-03-02", "status": "READY"},
    ... ])
    'READY'
    >>> latest_review_status([]) is None
    True
    """
    if not isinstance(manual_reviews, list):
        return None
    entries = [r for r in manual_reviews if isinstance(r, dict)]
    if not entries:
        return None
    latest = max(entries, key=lambda r: str(r.get("date") or ""))
    status = latest.get("status")
    return str(status) if status is not None else None


def render_projects_table(
    projects_dir: Path = Path("projects"),
    output_dir: Path = Path("pages/projects"),
    template_path: Optional[Path] = None,
) -> Path:
    """Render a derived table of all top-level projects from their frontmatter.

    A "project" is a top-level ``projects/FOO.md`` page (``README.md`` and the
    supporting material inside ``FOO/`` folders are excluded). For each project
    the table surfaces metadata pulled from its YAML frontmatter (title,
    ``maturity``, ``tags``, ``species``, ``genes``) plus a count of supporting
    markdown docs in its ``FOO/`` folder. The rendered page provides client-side
    filtering by tag/maturity/species and a title/slug search. This complements
    the hand-curated ``index.html`` by guaranteeing every project is listed.

    Args:
        projects_dir: Directory containing project markdown files
        output_dir: Directory for output HTML files
        template_path: Optional path to custom Jinja2 template

    Returns:
        Path to the written ``all-projects.html`` file.
    """
    if template_path is None:
        module_dir = Path(__file__).parent
        template_path = module_dir / "templates" / "projects_table.html.j2"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    rows: List[Dict[str, Any]] = []
    for md_path in sorted(projects_dir.glob("*.md")):
        if md_path.name == "README.md":
            continue
        frontmatter, content = parse_frontmatter(md_path.read_text())

        title = frontmatter.get("title")
        if not title:
            heading_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            title = heading_match.group(1).strip() if heading_match else md_path.stem

        def _as_list(value: Any) -> List[str]:
            if value is None:
                return []
            if isinstance(value, (list, tuple)):
                return [str(v) for v in value]
            return [str(value)]

        species = _as_list(frontmatter.get("species"))
        genes = _as_list(frontmatter.get("genes"))
        tags = _as_list(frontmatter.get("tags"))

        # ``maturity`` is the controlled-vocabulary project lifecycle field;
        # fall back to the legacy free-text ``status`` if a page predates it.
        maturity = frontmatter.get("maturity") or frontmatter.get("status")
        if maturity is not None:
            maturity = str(maturity)

        # Count supporting markdown docs in the project's FOO/ folder, if any.
        support_dir = projects_dir / md_path.stem
        support_count = (
            len(list(support_dir.rglob("*.md"))) if support_dir.is_dir() else 0
        )

        manual_reviews = frontmatter.get("manual_reviews")
        review_status = latest_review_status(manual_reviews)
        review_count = (
            len(manual_reviews) if isinstance(manual_reviews, list) else 0
        )

        rows.append(
            {
                "slug": md_path.stem,
                "title": title,
                "url": f"{md_path.stem}.html",
                "species": species,
                "genes": genes,
                "tags": tags,
                "maturity": maturity,
                "support_count": support_count,
                "review_status": review_status,
                "review_count": review_count,
            }
        )

    rows.sort(key=lambda r: str(r["title"]).casefold())

    # Stable, meaningful ordering for the controlled vocabularies so the
    # template can render filter chips deterministically.
    maturity_order = ["SCOPING", "IN_PROGRESS", "MATURE", "COMPLETE", "ARCHIVED"]
    tag_order = ["FLAGSHIP", "BIOLOGY_DOMAIN", "PIPELINE", "OBSOLETION"]
    review_status_order = ["READY", "CHANGES_REQUESTED"]
    all_maturities = [m for m in maturity_order if any(r["maturity"] == m for r in rows)]
    all_tags = [t for t in tag_order if any(t in r["tags"] for r in rows)]
    all_species = sorted({s for r in rows for s in r["species"]})
    all_review_statuses = [
        s for s in review_status_order if any(r["review_status"] == s for r in rows)
    ]

    env = Environment(
        loader=FileSystemLoader(template_path.parent),
        autoescape=select_autoescape(["html", "j2"]),
    )
    template = env.get_template(template_path.name)
    html = template.render(
        rows=rows,
        all_maturities=all_maturities,
        all_tags=all_tags,
        all_species=all_species,
        all_review_statuses=all_review_statuses,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "all-projects.html"
    output_path.write_text(html)
    return output_path


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

    # Render top-level project pages (FOO.md) and any supporting markdown that
    # lives inside a project's FOO/ folder, mirroring the subfolder structure.
    md_files = sorted(projects_dir.rglob("*.md"))

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
                projects_dir=projects_dir,
            )
            output_paths.append(output_path)
            index_path = write_readme_index_alias(md_file, output_path, projects_dir)
            if index_path is not None:
                output_paths.append(index_path)

            if warnings:
                all_warnings.extend([f"{md_file.name}: {w}" for w in warnings])
                print(f"  {md_file.name} -> {output_path.name} ({len(warnings)} warnings)")
            else:
                print(f"  {md_file.name} -> {output_path.name}")

        except Exception as e:
            print(f"  {md_file.name}: ERROR - {e}")
            all_warnings.append(f"{md_file.name}: Error rendering - {e}")

    print(f"\nRendered {len(output_paths)}/{len(md_files)} projects to {output_dir}")

    notebook_paths, notebook_warnings = convert_referenced_notebooks(
        md_files,
        output_dir=output_dir,
        projects_dir=projects_dir,
    )
    output_paths.extend(notebook_paths)
    all_warnings.extend(notebook_warnings)
    if notebook_paths:
        print(f"Rendered {len(notebook_paths)} referenced notebook HTML file(s)")

    copied_assets = copy_referenced_assets(
        md_files,
        output_dir=output_dir,
        projects_dir=projects_dir,
        rendered_paths=output_paths,
    )
    output_paths.extend(copied_assets)
    if copied_assets:
        print(f"Copied {len(copied_assets)} referenced asset files to {output_dir}")

    # Derived, metadata-driven table of all top-level projects.
    table_path = render_projects_table(projects_dir, output_dir)
    output_paths.append(table_path)
    print(f"Rendered project table -> {table_path}")

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
