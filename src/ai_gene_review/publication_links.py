"""Keep source-document links valid when publishing into a mirrored tree."""

from __future__ import annotations

from html import escape, unescape
import os
from pathlib import Path
import re
from urllib.parse import quote, unquote, urljoin, urlsplit

from ai_gene_review.tools.pages_dependencies import BASE_PATH, SITE_HOSTS

URL_ATTRIBUTE = re.compile(r'''(?P<attr>\b(?:href|src))=(?P<q>["'])(?P<url>.*?)(?P=q)''', re.DOTALL)


def protect_scientific_notation(content: str) -> str:
    """Escape bracketed chemical/index notation that Markdown treats as links.

    These bare subscripts and charge suffixes are not publication filenames.
    Ordinary links, including extensionless names, remain unchanged.
    """
    literal = re.compile(r'```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]*`|^(?: {4}|\t).*(?:\n|$)', re.MULTILINE)
    notation = re.compile(r'(?<![!\\])\[([^\]\n]+)\]\((n(?:[+-]\d+)?|i|[Gg][Ss]|\d+[+-])\)')
    pieces = []
    end = 0
    for match in literal.finditer(content):
        pieces.append(notation.sub(lambda m: rf'\[{m[1]}]({m[2]})', content[end:match.start()]))
        pieces.append(match[0])
        end = match.end()
    pieces.append(notation.sub(lambda m: rf'\[{m[1]}]({m[2]})', content[end:]))
    return ''.join(pieces)


def restore_scientific_html_notation(content: str, page: Path) -> str:
    """Repair the same Markdown misparse in already-rendered provider reports."""
    def restore(match: re.Match[str]) -> str:
        parsed = urlsplit(unescape(match['url']))
        suffix = unquote(parsed.path)
        if parsed.scheme or parsed.netloc or not re.fullmatch(r'n(?:[+-]\d+)?|i|[Gg][Ss]|\d+[+-]', suffix):
            return match[0]
        if (page.parent / suffix).exists():
            return match[0]
        return f'[{match["label"]}]({escape(suffix)})'

    return re.sub(r'<a\b[^>]*href="(?P<url>[^"]+)"[^>]*>(?P<label>.*?)</a>', restore, content, flags=re.DOTALL)


def rewrite_publication_links(
    content: str, source_path: Path, output_path: Path, repo_root: Path,
    mirrored_project_assets: set[Path] | None = None,
) -> str:
    """Resolve known local assets from source context, preserving missing links.

    Only existing, public repository targets are rewritten. Unknown paths stay
    visible to the staging audit. Already-valid generated links are retained.
    """
    if re.search(r'<base\b', content, re.IGNORECASE):
        return content
    root = repo_root.resolve()
    source_path = source_path.resolve()
    output_path = output_path.resolve()
    projects = root / 'projects'

    def public(path: Path) -> bool:
        resolved = path.resolve()
        return resolved.is_relative_to(root) and not any(
            part.startswith('.') for part in resolved.relative_to(root).parts
        )

    def existing(path: Path) -> Path | None:
        if public(path) and path.exists():
            return path.resolve()
        if path.suffix == '.html':
            md = path.with_suffix('.md')
            if public(md) and md.is_file():
                return md.resolve()
        return None

    def rewrite(match: re.Match[str]) -> str:
        raw = unescape(match['url'])
        parsed = urlsplit(raw)
        if not parsed.path or parsed.scheme not in {'', 'http', 'https'}:
            return match[0]
        if parsed.netloc and parsed.netloc not in SITE_HOSTS:
            return match[0]
        path = unquote(parsed.path)
        if path.startswith('/'):
            if path.startswith(BASE_PATH) or path in {'/', '/index.html'}:
                return match[0]
            candidate = existing(root / path.lstrip('/'))
            if candidate is None:
                return match[0]
            new_path = BASE_PATH + quote(candidate.relative_to(root).as_posix(), safe='/')
        else:
            current = output_path.parent / path
            if public(current) and current.exists():
                return match[0]
            candidate = existing(source_path.parent / path)
            if candidate is None:
                candidate = existing(current)
            if candidate is None:
                if not output_path.is_relative_to(root):
                    return match[0]
                public_url = 'https://ai4curation.io' + BASE_PATH + output_path.relative_to(root).as_posix()
                effective = urlsplit(urljoin(public_url, raw))
                if effective.path.startswith(BASE_PATH) or effective.path in {'/', '/index.html'}:
                    return match[0]
                candidate = existing(root / unquote(effective.path).lstrip('/'))
                if candidate is None:
                    return match[0]
                url = parsed._replace(path=BASE_PATH + quote(candidate.relative_to(root).as_posix(), safe='/')).geturl()
                return f'{match["attr"]}={match["q"]}{escape(url, quote=True)}{match["q"]}'
            destination = candidate
            if candidate.is_relative_to(projects):
                mirrored = root / 'pages/projects' / candidate.relative_to(projects)
                if candidate.suffix in {'.md', '.markdown'}:
                    destination = mirrored.with_suffix('.html')
                elif candidate.is_dir() or mirrored.exists() or candidate in (mirrored_project_assets or set()):
                    destination = mirrored
            new_path = quote(Path(os.path.relpath(destination, output_path.parent)).as_posix(), safe='/')
            if candidate.is_dir() and not new_path.endswith('/'):
                new_path += '/'
        url = parsed._replace(path=new_path).geturl()
        return f'{match["attr"]}={match["q"]}{escape(url, quote=True)}{match["q"]}'

    return URL_ATTRIBUTE.sub(rewrite, content)
