"""Compact staged publication files while retaining the full review content.

Main gene content remains HTML. Bulky supporting panels are stored losslessly
and restored on page load, with compressed downloads available without JS.
The adjacent source HTML is never changed by staging.
"""

from __future__ import annotations

import gzip
from hashlib import sha256
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re

import minify_html

from ai_gene_review.export.browser_payload import (
    COLUMNAR_DATA_JS_PREFIX,
    encode_browser_data_js,
)

PANEL_CLASSES = {"markdown-content", "yaml-content", "collapse-content"}


def _minify_gene_html(text: str) -> str:
    """Retain inter-element spaces, including headings styled as inline text."""
    marker = 'PAGESWHITESPACE'
    while marker in text:
        marker += 'X'
    protected = re.compile(r'<(pre|code|textarea|script|style)\b[^>]*>.*?</\1\s*>', re.I | re.S)
    pieces = []
    end = 0
    for match in protected.finditer(text):
        pieces.append(re.sub(r'>\s+<', f'>{marker}<', text[end:match.start()]))
        pieces.append(match[0])
        end = match.end()
    pieces.append(re.sub(r'>\s+<', f'>{marker}<', text[end:]))
    compact = minify_html.minify(
        ''.join(pieces), keep_closing_tags=True, keep_html_and_head_opening_tags=True,
        keep_input_type_text_attr=True,
    )
    return compact.replace(marker, ' ')


class _Panels(HTMLParser):
    """Find exact inner-HTML spans without reserializing their markup."""

    def __init__(self, text: str) -> None:
        super().__init__(convert_charrefs=False)
        self.offsets = [0]
        for line in text.split("\n"):
            self.offsets.append(self.offsets[-1] + len(line) + 1)
        self.depth = 0
        self.active: tuple[int, int] | None = None
        self.spans: list[tuple[int, int]] = []
        self.feed(text)

    def source_position(self) -> int:
        line, column = self.getpos()
        return self.offsets[line - 1] + column

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "div":
            return
        self.depth += 1
        classes = (dict(attrs).get("class") or "").split()
        if self.active is None and PANEL_CLASSES.intersection(classes):
            start_tag = self.get_starttag_text()
            assert start_tag is not None
            self.active = (self.depth, self.source_position() + len(start_tag))

    def handle_endtag(self, tag: str) -> None:
        if tag != "div":
            return
        if self.active and self.depth == self.active[0]:
            self.spans.append((self.active[1], self.source_position()))
            self.active = None
        self.depth -= 1


def _write_asset(path: Path, content: bytes) -> int:
    """Write a generated asset once, refusing an existing-path collision."""
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError(f"Generated Pages asset collision: {path}")
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return len(content)


def compact_gene_page(output_dir: Path, page: Path) -> int:
    """Compact one generated gene page and return net bytes saved."""
    original = page.read_text(encoding="utf-8")
    if "</body>" not in original or re.search(r"<base\b", original, re.IGNORECASE):
        return 0
    updated = original
    asset_bytes = 0
    panels = 0
    for start, end in reversed(_Panels(original).spans):
        content = original[start:end]
        if len(content) < 1024 or re.search(r"<(?:script|style)\b", content, re.IGNORECASE):
            continue
        raw = content.encode("utf-8")
        compressed = gzip.compress(raw, mtime=0)
        path = output_dir / "_pages-content" / (sha256(raw).hexdigest() + ".html.gz")
        url = Path(os.path.relpath(path, page.parent)).as_posix()
        replacement = (
            f'<div data-pages-content="{url}"><p role="status">Loading supporting content…</p>'
            f'<a href="{url}" download>Download this section (compressed HTML)</a>'
            '<noscript><p>Enable JavaScript to view this section here, or download it above.</p></noscript></div>'
        )
        if len(compressed) + len(replacement.encode()) >= len(raw):
            continue
        asset_bytes += _write_asset(path, compressed)
        updated = updated[:start] + replacement + updated[end:]
        panels += 1
    if panels:
        loader = Path(__file__).with_name("pages_content.js").read_bytes()
        path = output_dir / "_pages-assets" / (sha256(loader).hexdigest() + ".js")
        asset_bytes += _write_asset(path, loader)
        url = Path(os.path.relpath(path, page.parent)).as_posix()
        updated = updated.replace("</body>", f'<script defer src="{url}"></script></body>')
    # Limit minification to generated gene markup with its known template CSS.
    # pre/code retain whitespace; supporting content above retains exact bytes.
    updated = _minify_gene_html(updated)
    page.write_text(updated, encoding="utf-8")
    return len(original.encode()) - len(updated.encode()) - asset_bytes


def compact_browser_data(output_dir: Path) -> int:
    """Losslessly gzip the known columnar payload, retaining data.js's contract.

    Unknown script formats are left intact rather than interpreted as data.
    The decoder executes no source code and preserves special property names.
    """
    path = output_dir / "app/data.js"
    original = path.read_text(encoding="utf-8")
    if not original.startswith(COLUMNAR_DATA_JS_PREFIX):
        return 0
    decoder = json.JSONDecoder()
    columns, end = decoder.raw_decode(original, len(COLUMNAR_DATA_JS_PREFIX))
    if original[end:end + 3] != ",r=":
        return 0
    rows, end = decoder.raw_decode(original, end + 3)
    suffix = ";window.searchData=" + encode_browser_data_js([]).split(";window.searchData=", 1)[1]
    if original[end:] != suffix:
        return 0
    packed = json.dumps({"columns": columns, "rows": rows}, ensure_ascii=False, separators=(",", ":")).encode()
    compressed = gzip.compress(packed, mtime=0)
    loader = Path(__file__).with_name("pages_browser_data.js").read_bytes()
    if len(compressed) + len(loader) >= len(original.encode()):
        return 0
    asset_bytes = _write_asset(path.with_name("data.json.gz"), compressed)
    path.write_bytes(loader)
    return len(original.encode()) - len(loader) - asset_bytes
