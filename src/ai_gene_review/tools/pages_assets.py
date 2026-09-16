"""Share literal renderer assets in staged pages without changing source output."""

from __future__ import annotations

from hashlib import sha256
import os
from pathlib import Path
import re

TEMPLATES = ("gene_review.html.j2", "project.html.j2", "module.html.j2")
BLOCK = re.compile(r"<(?P<tag>style|script)>(?P<body>.*?)</(?P=tag)>", re.DOTALL)
ASSET_DIR = "_pages-assets"
MIN_BLOCK_BYTES = 1024


def _template_blocks(templates: Path) -> dict[str, tuple[str, str]]:
    """Select exact, literal blocks whose meaning does not depend on their URL."""
    blocks = {}
    for name in TEMPLATES:
        path = templates / name
        if not path.is_file():
            continue
        # Match the renderer's trailing-whitespace normalization.
        text = "\n".join(line.rstrip() for line in path.read_text().splitlines())
        for match in BLOCK.finditer(text):
            block, body, tag = match.group(), match["body"], match["tag"]
            if len(block.encode()) < MIN_BLOCK_BYTES:
                continue
            if any(marker in block for marker in ("{{", "{%", "{#")):
                continue
            if tag == "style" and re.search(r"url\s*\(|@import", body, re.IGNORECASE):
                continue
            if tag == "script" and re.search(
                r"currentScript|import\s*[.(]|document\.write|sourceMappingURL", body
            ):
                continue
            extension = "css" if tag == "style" else "js"
            name = sha256(body.encode()).hexdigest() + "." + extension
            blocks[block] = (name, body)
    return blocks


def share_template_assets(
    output_dir: Path, pages: list[Path], templates: Path | None = None
) -> int:
    """Replace recognized inline blocks with shared files; return net bytes saved.

    Replacements stay in the same DOM position. Classic scripts remain
    synchronous. Unknown/dynamic blocks and documents with a base element are
    left alone. No CSS or JavaScript is minified or otherwise rewritten.
    """
    templates = templates or Path(__file__).parents[1] / "templates"
    blocks = _template_blocks(templates)
    savings = 0
    written: set[Path] = set()
    for page in pages:
        original = page.read_text()
        if re.search(r"<base\b", original, re.IGNORECASE):
            continue
        updated = original
        for block, (name, body) in blocks.items():
            if block not in updated:
                continue
            asset = output_dir / ASSET_DIR / name
            relative_url = Path(os.path.relpath(asset, page.parent)).as_posix()
            replacement = (
                f'<link rel="stylesheet" href="{relative_url}">'
                if name.endswith(".css")
                else f'<script src="{relative_url}"></script>'
            )
            if asset not in written:
                if asset.exists():
                    if asset.read_text() != body:
                        raise ValueError(f"Generated Pages asset collision: {asset}")
                else:
                    asset.parent.mkdir(parents=True, exist_ok=True)
                    asset.write_text(body)
                    savings -= len(body.encode())
                written.add(asset)
            updated = updated.replace(block, replacement)
        if updated != original:
            page.write_text(updated)
            savings += len(original.encode()) - len(updated.encode())
    return savings
