"""Resolve static publication dependencies without changing their public URLs."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit


BASE_PATH = "/ai-gene-review/"
SITE_ORIGIN = "https://ai4curation.io"
SITE_HOSTS = {"ai4curation.io", "ai4curation.github.io"}
CSS_URL = re.compile(r"url\(\s*['\"]?([^'\"\s)]+)['\"]?\s*\)", re.IGNORECASE)
CSS_IMPORT = re.compile(r"@import\s+['\"]([^'\"]+)['\"]", re.IGNORECASE)
JS_URL = re.compile(r"(?<![\w$.])(?:fetch|import)\(\s*['\"]([^'\"]+)['\"]\s*[,)]")
JS_FETCH = re.compile(r"(?<![\w$.])fetch\(\s*['\"]([^'\"]+)['\"]\s*[,)]")
JS_IMPORT = re.compile(r"(?<![\w$.])import\(\s*['\"]([^'\"]+)['\"]\s*[,)]")
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
        self.unavailable: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value for name, value in attrs if value is not None}
        if values.get('data-unavailable-artifact'):
            self.unavailable.append(values['data-unavailable-artifact'])
        if tag == "base":
            if self.base is None:
                self.base = values.get("href")
            return
        for name in ("href", "src", "poster", "data", "data-pages-content"):
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

        if (
            tag == "link"
            and "modulepreload" in (values.get("rel") or "").split()
            and values.get("href")
        ):
            self.scripts.append(values["href"])

    def handle_endtag(self, tag: str) -> None:
        if tag == self.raw_element:
            self.raw_element = None

    def handle_data(self, data: str) -> None:
        if self.raw_element == "style":
            self.links.extend(_css_links(data))
        elif self.raw_element == "script":
            self.links.extend(JS_URL.findall(data))
            self.scripts.extend(JS_IMPORT.findall(data))


def _public_path(repo_root: Path, url: str) -> Path | None:
    """Map a public site URL to a safe repository path, retaining its path."""
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
    if source.is_dir() or parsed.path.endswith("/"):
        target /= "index.html"
        source /= "index.html"
    resolved = source.resolve()
    if not resolved.is_relative_to(repo_root):
        return None
    if any(p.startswith(".") for p in resolved.relative_to(repo_root).parts):
        return None
    return target


def _off_base_repository_url(repo_root: Path, url: str) -> str | None:
    """Flag likely missing-prefix links, leaving unrelated host projects alone."""
    parsed = urlsplit(url)
    if (
        parsed.scheme not in {"http", "https"}
        or parsed.netloc not in SITE_HOSTS
        or parsed.path.startswith(BASE_PATH)
    ):
        return None
    # Reuse containment/hidden-path checks before checking repository existence.
    candidate = _public_path(
        repo_root, SITE_ORIGIN + BASE_PATH + parsed.path.lstrip("/")
    )
    # The organization homepage is a legitimate destination shared by projects.
    if candidate is None or candidate == Path("index.html"):
        return None
    normalized_url = parsed._replace(query="", fragment="").geturl()
    if (repo_root / candidate).is_file():
        return normalized_url
    if candidate.suffix.lower() == ".html":
        # Only the fallback needs another safety check (it may be a symlink).
        # Encode the decoded filename so literal # and ? remain path characters.
        fallback_url = (
            SITE_ORIGIN
            + BASE_PATH
            + quote(candidate.with_suffix(".md").as_posix(), safe="/")
        )
        fallback = _public_path(repo_root, fallback_url)
        if fallback is not None and (repo_root / fallback).is_file():
            return normalized_url
    return None


@dataclass
class DependencyLinks:
    """Existing dependencies and unique missing local targets."""

    existing: set[Path] = field(default_factory=set)
    missing: set[Path] = field(default_factory=set)
    off_base: set[str] = field(default_factory=set)
    unavailable: set[Path] = field(default_factory=set)


@dataclass
class DependencyResolver:
    """Resolve literal static URLs with a script cache scoped to one build.

    Fetch URLs retain each owning document's base URL. Navigation is followed
    without depth or size truncation. Dynamic JavaScript is not interpreted.
    """

    repo_root: Path
    script_cache: dict[Path, tuple[list[str], list[str]]] = field(default_factory=dict)

    def scan(self, relative: Path, content: str) -> DependencyLinks:
        """Collect safe existing paths and report missing local files."""
        document_url = SITE_ORIGIN + BASE_PATH + relative.as_posix()
        scripts: list[str] = []
        unavailable: list[str] = []
        if relative.suffix.lower() in {".html", ".htm"}:
            parser = _HTMLLinks()
            parser.feed(content)
            links = parser.links
            # Static snapshot: apply the first base to the complete document;
            # this does not simulate parser-time loads before a late base tag.
            document_url = urljoin(document_url, parser.base or "")
            scripts = [urljoin(document_url, src) for src in parser.scripts]
            unavailable = parser.unavailable
        elif relative.suffix.lower() == ".css":
            links = _css_links(content)
        elif relative.suffix.lower() == ".js":
            # Imports are relative to the script; fetch() is relative to the owning
            # document and is handled while scanning that document below.
            links = JS_IMPORT.findall(content)
        else:
            return DependencyLinks()

        result = DependencyLinks()
        for path in unavailable:
            target = _public_path(self.repo_root, urljoin(document_url, path))
            if target is not None:
                result.unavailable.add(target)

        def collect(url: str) -> Path | None:
            target = _public_path(self.repo_root, url)
            if target is None:
                off_base = _off_base_repository_url(self.repo_root, url)
                if off_base is not None:
                    result.off_base.add(off_base)
                return None
            if (self.repo_root / target).is_file():
                result.existing.add(target)
                return target
            result.missing.add(target)
            return None

        for link in links:
            if link.strip() and not link.startswith("#"):
                collect(urljoin(document_url, link))
        visited_scripts: set[Path] = set()
        while scripts:
            script_url = scripts.pop()
            script = collect(script_url)
            if script is None or script in visited_scripts:
                continue
            visited_scripts.add(script)
            if script not in self.script_cache:
                script_text = (self.repo_root / script).read_text(errors="ignore")
                self.script_cache[script] = (
                    JS_FETCH.findall(script_text),
                    JS_IMPORT.findall(script_text),
                )
            fetches, imports = self.script_cache[script]
            for link in fetches:
                collect(urljoin(document_url, link))
            scripts.extend(urljoin(script_url, link) for link in imports)
        return result
