"""Resolve static publication dependencies without changing their public URLs."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


BASE_PATH = "/ai-gene-review/"
SITE_ORIGIN = "https://ai4curation.io"
SITE_HOSTS = {"ai4curation.io", "ai4curation.github.io"}
CSS_URL = re.compile(r"url\(\s*['\"]?([^'\"\s)]+)['\"]?\s*\)", re.IGNORECASE)
CSS_IMPORT = re.compile(r"@import\s+['\"]([^'\"]+)['\"]", re.IGNORECASE)
JS_URL = re.compile(r"(?:fetch|import)\(\s*['\"]([^'\"]+)['\"]\s*[,)]")
JS_FETCH = re.compile(r"fetch\(\s*['\"]([^'\"]+)['\"]\s*[,)]")
JS_IMPORT = re.compile(r"import\(\s*['\"]([^'\"]+)['\"]\s*[,)]")
TEXT_ASSETS = {".html", ".htm", ".css", ".js"}


def _css_links(text: str) -> list[str]:
    """Extract CSS URLs and quoted imports, ignoring comments."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return CSS_URL.findall(text) + CSS_IMPORT.findall(text)


class _HTMLLinks(HTMLParser):
    """Collect resource/navigation links and the document's first base URL."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.base: str | None = None
        self.raw_element: str | None = None
        self.scripts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "base":
            if self.base is None:
                self.base = values.get("href")
            return
        for name in ("href", "src", "poster", "data"):
            if values.get(name):
                self.links.append(values[name])
        if values.get("srcset"):
            # URLs in srcset cannot contain literal whitespace; spaces are encoded.
            for candidate in values["srcset"].split(","):
                if candidate.strip():
                    self.links.append(candidate.strip().split()[0])
        if values.get("style"):
            self.links.extend(_css_links(values["style"]))
        if tag in {"style", "script"}:
            self.raw_element = tag
        if tag == "script" and values.get("src"):
            self.scripts.append(values["src"])

    def handle_endtag(self, tag: str) -> None:
        if tag == self.raw_element:
            self.raw_element = None

    def handle_data(self, data: str) -> None:
        if self.raw_element == "style":
            self.links.extend(_css_links(data))
        elif self.raw_element == "script":
            self.links.extend(JS_URL.findall(data))


def _public_file(repo_root: Path, url: str) -> Path | None:
    """Map a public site URL to an existing repository file, retaining its path."""
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or parsed.netloc not in SITE_HOSTS:
        return None
    if not parsed.path.startswith(BASE_PATH):
        return None
    target = Path(unquote(parsed.path.removeprefix(BASE_PATH)))
    if (
        target.is_absolute()
        or any(p.startswith(".") for p in target.parts)
        or (target.parts and target.parts[0] == "_site")
    ):
        return None
    source = repo_root / target
    if source.is_dir():
        target /= "index.html"
        source /= "index.html"
    resolved = source.resolve()
    if not resolved.is_relative_to(repo_root):
        return None
    if any(p.startswith(".") for p in resolved.relative_to(repo_root).parts):
        return None
    return target if source.is_file() else None


def linked_repository_files(repo_root: Path, relative: Path, content: str) -> set[Path]:
    """Return existing public files referenced by HTML, CSS, or literal JS URLs.

    Results retain their URL paths, even for in-repository symlinks. Links out
    of the site, hidden paths, and symlinks outside the repository are excluded.
    Directory links resolve to index.html. Dynamic JavaScript URLs are not
    interpreted; browser smoke checks remain necessary before deployment.
    """
    document_url = SITE_ORIGIN + BASE_PATH + relative.as_posix()
    scripts: list[str] = []
    if relative.suffix.lower() in {".html", ".htm"}:
        parser = _HTMLLinks()
        parser.feed(content)
        links = parser.links
        document_url = urljoin(document_url, parser.base or "")
        scripts = [urljoin(document_url, src) for src in parser.scripts]
    elif relative.suffix.lower() == ".css":
        links = _css_links(content)
    elif relative.suffix.lower() == ".js":
        # Imports are relative to the script; fetch() is relative to the owning
        # document and is handled while scanning that document below.
        links = JS_IMPORT.findall(content)
    else:
        return set()

    dependencies: set[Path] = set()
    for link in links:
        if not link.strip() or link.startswith("#"):
            continue
        target = _public_file(repo_root, urljoin(document_url, link))
        if target is not None:
            dependencies.add(target)
    visited_scripts: set[Path] = set()
    while scripts:
        script_url = scripts.pop()
        script = _public_file(repo_root, script_url)
        if script is None or script in visited_scripts:
            continue
        visited_scripts.add(script)
        dependencies.add(script)
        script_text = (repo_root / script).read_text(errors="ignore")
        for link in JS_FETCH.findall(script_text):
            target = _public_file(repo_root, urljoin(document_url, link))
            if target is not None:
                dependencies.add(target)
        scripts.extend(
            urljoin(script_url, link) for link in JS_IMPORT.findall(script_text)
        )
    return dependencies
