"""Assemble generated web output into a GitHub Pages artifact directory.

The renderers intentionally keep writing gene HTML beside the review YAML so a
curator can open a page locally.  This module collects only the files needed by
the public site into a disposable directory, providing a boundary between
source data and deployable output.
"""

from __future__ import annotations

import argparse
import json
import io
import tarfile
from html import escape
import os
import shutil
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import quote

from ai_gene_review.tools.pages_assets import share_template_assets
from ai_gene_review.tools.pages_compaction import compact_browser_data, compact_gene_page
from ai_gene_review.tools.pages_dependencies import TEXT_ASSETS, DependencyResolver
from ai_gene_review.publication_links import rewrite_publication_links, restore_scientific_html_notation


PAGES_SIZE_BUDGET_BYTES = 1_000_000_000
PAGES_ARCHIVE_BUDGET_BYTES = 1_073_741_824
MIB = 1024 * 1024
BROWSER_FILES = ("index.html", "data.js", "schema.js")
PREDICTION_BROWSER_FILES = (*BROWSER_FILES, "source-files.json")


@dataclass(frozen=True)
class SiteManifest:
    """Summary of files copied into the Pages staging directory."""

    total_bytes: int
    total_files: int
    archive_bytes: int
    gene_pages: int
    project_pages: int
    module_pages: int
    linked_source_files_not_staged: int
    linked_source_bytes_not_staged: int
    broken_local_link_paths: list[str]
    off_base_path_urls: list[str]
    shared_asset_bytes_saved: int = 0
    content_compaction_bytes_saved: int = 0
    unavailable_source_artifact_paths: list[str] = field(default_factory=list)
    size_budget_bytes: int = PAGES_SIZE_BUDGET_BYTES
    archive_size_budget_bytes: int = PAGES_ARCHIVE_BUDGET_BYTES
    archive_checksum_required: bool = True

    @property
    def broken_local_links(self) -> int:
        """Number of distinct missing static local targets."""
        return len(self.broken_local_link_paths)

    @property
    def off_base_path_links(self) -> int:
        """Likely missing site-prefix links matching repository content."""
        return len(self.off_base_path_urls)

    @property
    def deployable(self) -> bool:
        """Readiness policy shared by CLI reporting and deployment."""
        return (
            self.total_bytes <= self.size_budget_bytes
            and self.archive_bytes <= self.archive_size_budget_bytes
            and self.linked_source_files_not_staged == 0
            and self.broken_local_links == 0
            and self.off_base_path_links == 0
        )


def pages_archive_bytes(output_dir: Path) -> int:
    """Size of upload-pages-artifact's GNU tar, using metadata without reading bodies.

    Match its dot-file exclusions, dereferencing and 20-block record padding.
    Staging produces regular files/directories; reject unexpected symlinks.
    """
    size = 0
    with tarfile.open(fileobj=io.BytesIO(), mode='w', format=tarfile.GNU_FORMAT,
                      dereference=True, encoding='utf-8') as archive:
        for path in [output_dir, *output_dir.rglob('*')]:
            relative = path.relative_to(output_dir)
            if any(part.startswith('.') for part in relative.parts):
                continue
            if path.is_symlink():
                raise ValueError(f'Unexpected symlink in Pages artifact: {relative}')
            name = '.' if path == output_dir else './' + relative.as_posix()
            info = archive.gettarinfo(str(path), arcname=name)
            size += len(info.tobuf(format=tarfile.GNU_FORMAT, encoding='utf-8'))
            if info.isfile():
                size += ((info.size + 511) // 512) * 512
    size += 1024  # Two end-of-archive blocks.
    return ((size + tarfile.RECORDSIZE - 1) // tarfile.RECORDSIZE) * tarfile.RECORDSIZE


def _copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def _require_file(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"Required Pages input is missing: {path}")


def _stage_prediction_browser(repo_root: Path, output_dir: Path) -> None:
    """Include the predictions app and public files linked from its dynamic rows."""
    relative = Path("app/predictions")
    if not (repo_root / relative).is_dir():
        return
    for filename in PREDICTION_BROWSER_FILES:
        source = repo_root / relative / filename
        _require_file(source)
        _copy_file(source, output_dir / relative / filename)
    sources = json.loads((repo_root / relative / "source-files.json").read_text())
    if not isinstance(sources, list) or not all(isinstance(path, str) for path in sources):
        raise ValueError("Invalid prediction browser source manifest")
    for name in sources:
        path = Path(name)
        source = repo_root / path
        resolved = source.resolve()
        if (
            not path.parts or path.is_absolute()
            or any(part.startswith(".") for part in path.parts)
            or path.parts[0] == "_site"
            or not resolved.is_relative_to(repo_root)
            or any(part.startswith(".") for part in resolved.relative_to(repo_root).parts)
            or resolved.is_relative_to(repo_root / "_site")
        ):
            raise ValueError(f"Invalid prediction browser source: {name}")
        _require_file(source)
        _copy_file(source, output_dir / path)


def _safe_clean_output(repo_root: Path, output_dir: Path) -> None:
    """Only remove the repository's dedicated, ignored staging directory."""
    resolved_root = repo_root.resolve()
    resolved_output = output_dir.resolve()
    if resolved_output == resolved_root or resolved_root not in resolved_output.parents:
        raise ValueError("Pages output directory must be inside the repository root")
    if resolved_output != resolved_root / "_site":
        raise ValueError(
            "Pages output directory must be the repository's _site directory"
        )
    git_root = subprocess.run(
        ["git", "-C", str(resolved_root), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if git_root.returncode or Path(git_root.stdout.strip()).resolve() != resolved_root:
        raise ValueError("Pages repository root must be a Git worktree root")
    if resolved_output.exists():
        shutil.rmtree(resolved_output)
    resolved_output.mkdir(parents=True)


@dataclass(frozen=True)
class StagingLinkAudit:
    """Excluded absolute source paths, missing relative paths, and off-base URLs."""

    excluded_sources: set[Path]
    missing_paths: set[Path]
    off_base_urls: set[str]
    unavailable_paths: set[Path]


def _stage_directory_index(repo_root: Path, output_dir: Path, target: Path) -> bool:
    """Give explicitly linked public source directories a browsable index."""
    if target.name != 'index.html':
        return False
    relative = target.parent
    source_relative = relative
    if relative.is_relative_to('pages/projects'):
        source_relative = Path('projects') / relative.relative_to('pages/projects')
    source = repo_root / source_relative
    if not source.is_dir() or source.is_symlink() or not source.resolve().is_relative_to(repo_root):
        return False
    if any(part.startswith('.') for part in source.resolve().relative_to(repo_root).parts):
        return False
    links = []
    for child in sorted(source.iterdir()):
        if (child.name.startswith('.') or child.name in {'__pycache__', 'node_modules'}
                or child.is_symlink() or not child.resolve().is_relative_to(repo_root)):
            continue
        original = child.relative_to(repo_root)
        destination = original
        if original.is_relative_to('projects'):
            mirrored = Path('pages') / original
            if child.is_dir():
                destination = mirrored / 'index.html'
            elif child.suffix in {'.md', '.markdown'} and (
                (output_dir / mirrored.with_suffix('.html')).is_file()
                or (repo_root / mirrored.with_suffix('.html')).is_file()
            ):
                destination = mirrored.with_suffix('.html')
            elif (output_dir / mirrored).is_file() or (repo_root / mirrored).is_file():
                destination = mirrored
        elif child.is_dir():
            destination /= 'index.html'
        href = quote(Path(os.path.relpath(destination, relative)).as_posix(), safe='/')
        links.append(f'<li><a href="{href}">{escape(child.name)}{ "/" if child.is_dir() else ""}</a></li>')
    title = escape(source_relative.as_posix())
    document = f'<!doctype html><html lang="en"><meta charset="utf-8"><title>{title}</title><h1>{title}</h1><ul>{"".join(links)}</ul></html>'
    path = output_dir / target
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding='utf-8')
    return True


def _stage_linked_files(repo_root: Path, output_dir: Path) -> StagingLinkAudit:
    """Copy static dependencies transitively and return any excluded public files.

    Scan each HTML/CSS/JS file only once. Referenced notes, downloads, reports,
    images, and their dependencies keep their paths and original bytes.
    """
    pending = [
        p.relative_to(output_dir)
        for p in output_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in TEXT_ASSETS
    ]
    scanned: set[Path] = set()
    omitted: set[Path] = set()
    broken: set[Path] = set()
    off_base: set[str] = set()
    unavailable: set[Path] = set()
    resolver = DependencyResolver(repo_root)
    while pending:
        relative = pending.pop()
        if relative in scanned:
            continue
        scanned.add(relative)
        content = (output_dir / relative).read_text(errors="ignore")
        if relative.suffix.lower() in {'.html', '.htm'}:
            source = repo_root / relative
            if relative.is_relative_to('pages/projects'):
                candidate = repo_root / relative.relative_to('pages')
                if candidate.is_file():
                    source = candidate
                elif candidate.with_suffix('.md').is_file():
                    source = candidate.with_suffix('.md')
            repaired = rewrite_publication_links(content, source, repo_root / relative, repo_root)
            repaired = restore_scientific_html_notation(repaired, repo_root / relative)
            if repaired != content:
                (output_dir / relative).write_text(repaired, encoding='utf-8')
                content = repaired
        links = resolver.scan(relative, content)
        broken.update(links.missing)
        for missing in links.missing:
            if not (output_dir / missing).is_file() and _stage_directory_index(repo_root, output_dir, missing):
                pending.append(missing)
        off_base.update(links.off_base)
        unavailable.update(links.unavailable)
        for target in links.existing:
            source = repo_root / target
            destination = output_dir / target
            if not destination.is_file():
                # Keep the existing exclusion of orphan review HTML, even if an
                # old index still links to it. Report it instead of publishing it.
                if (
                    source.name.endswith("-ai-review.html")
                    and not source.with_suffix(".yaml").is_file()
                ):
                    omitted.add(source)
                    continue
                _copy_file(source, destination)
            if target.suffix.lower() in TEXT_ASSETS and target not in scanned:
                pending.append(target)
    return StagingLinkAudit(
        omitted,
        {path for path in broken if not (output_dir / path).is_file()},
        off_base,
        unavailable,
    )


def stage_pages(repo_root: Path, output_dir: Path) -> SiteManifest:
    """Copy the current generated site into ``output_dir``.

    The staged layout deliberately matches the current ``main:/`` Pages URLs.
    Linked source material and supplemental reports retain their public paths.
    ``pages/`` remains a transitional mixed-output area and is copied wholesale
    until its manually maintained inputs are separated in a later migration.
    ``output_dir`` must resolve to the repository's dedicated ``_site`` directory.
    """

    repo_root = repo_root.resolve()
    output_dir = output_dir.resolve()
    _safe_clean_output(repo_root, output_dir)

    for root_file in ("index.html", ".nojekyll"):
        source = repo_root / root_file
        _require_file(source)
        _copy_file(source, output_dir / root_file)

    review_files = sorted((repo_root / "genes").glob("*/*/*-ai-review.yaml"))
    if not review_files:
        raise FileNotFoundError("No gene review YAML files were found")

    # Derive pages from reviews instead of globbing HTML. This prevents a stale
    # local page for a deleted review from leaking into the deployment.
    gene_pages = [review.with_suffix(".html") for review in review_files]
    missing_pages = [page for page in gene_pages if not page.is_file()]
    if missing_pages:
        preview = ", ".join(
            str(path.relative_to(repo_root)) for path in missing_pages[:5]
        )
        suffix = (
            "" if len(missing_pages) <= 5 else f" (and {len(missing_pages) - 5} more)"
        )
        raise FileNotFoundError(f"Missing rendered gene pages: {preview}{suffix}")

    for source in gene_pages:
        _copy_file(source, output_dir / source.relative_to(repo_root))

    pages_source = repo_root / "pages"
    if not pages_source.is_dir():
        raise FileNotFoundError(f"Required Pages input is missing: {pages_source}")
    shutil.copytree(
        pages_source,
        output_dir / "pages",
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".DS_Store"),
    )

    for browser_file in BROWSER_FILES:
        source = repo_root / "app" / browser_file
        _require_file(source)
        _copy_file(source, output_dir / "app" / browser_file)

    _stage_prediction_browser(repo_root, output_dir)

    audit = _stage_linked_files(repo_root, output_dir)
    linked_sources = audit.excluded_sources
    broken_links = audit.missing_paths
    # Scan/copy dependencies before replacing inline blocks: the new assets
    # exist only in the artifact and contain no URL-relative dependencies.
    generated_pages = [output_dir / p.relative_to(repo_root) for p in gene_pages]
    generated_pages.extend((output_dir / "pages").rglob("*.html"))
    shared_asset_bytes_saved = share_template_assets(output_dir, generated_pages)
    content_compaction_bytes_saved = sum(
        compact_gene_page(output_dir, output_dir / page.relative_to(repo_root))
        for page in gene_pages
    ) + compact_browser_data(output_dir)
    # Check the URLs actually emitted by sharing/minification/compaction too.
    # The first audit above checks links inside panels before they are compressed.
    published_resolver = DependencyResolver(output_dir)
    for page in generated_pages:
        links = published_resolver.scan(page.relative_to(output_dir), page.read_text())
        broken_links.update(links.missing)
        audit.off_base_urls.update(links.off_base)
    staged_files = [path for path in output_dir.rglob("*") if path.is_file()]
    manifest = SiteManifest(
        shared_asset_bytes_saved=shared_asset_bytes_saved,
        content_compaction_bytes_saved=content_compaction_bytes_saved,
        unavailable_source_artifact_paths=sorted(p.as_posix() for p in audit.unavailable_paths),
        off_base_path_urls=sorted(audit.off_base_urls),
        broken_local_link_paths=sorted(p.as_posix() for p in broken_links),
        total_bytes=sum(path.stat().st_size for path in staged_files),
        total_files=len(staged_files),
        archive_bytes=pages_archive_bytes(output_dir),
        gene_pages=len(gene_pages),
        project_pages=len(list((output_dir / "pages" / "projects").rglob("*.html"))),
        module_pages=len(list((output_dir / "pages" / "modules").rglob("*.html"))),
        linked_source_files_not_staged=len(linked_sources),
        linked_source_bytes_not_staged=sum(
            path.stat().st_size for path in linked_sources
        ),
    )

    if manifest.project_pages == 0:
        raise FileNotFoundError("The staged site contains no rendered project pages")
    if manifest.module_pages == 0:
        raise FileNotFoundError("The staged site contains no rendered module pages")

    return manifest


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Optional path for a JSON size/count report (outside the site is recommended)",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    repo_root = args.repo_root.resolve()
    output_dir = repo_root / "_site"

    manifest = stage_pages(repo_root, output_dir)
    manifest_json = (
        json.dumps(
            {
                **asdict(manifest),
                "broken_local_links": manifest.broken_local_links,
                "off_base_path_links": manifest.off_base_path_links,
                "deployable": manifest.deployable,
            },
            indent=2,
        )
        + "\n"
    )

    if args.manifest:
        manifest_path = args.manifest
        if not manifest_path.is_absolute():
            manifest_path = repo_root / manifest_path
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(manifest_json)

    size_mib = manifest.total_bytes / MIB
    print(f"Staged {manifest.total_files:,} files in {output_dir}")
    print(f"Uncompressed site size: {size_mib:,.1f} MiB")
    print(f"Tar archive size: {manifest.archive_bytes / MIB:,.1f} MiB")
    print(
        f"Shared template assets saved: {manifest.shared_asset_bytes_saved / MIB:,.1f} MiB"
    )
    print(
        "Rendered pages: "
        f"{manifest.gene_pages:,} genes, "
        f"{manifest.project_pages:,} projects, "
        f"{manifest.module_pages:,} modules"
    )
    if manifest.total_bytes > manifest.size_budget_bytes:
        print(
            f"::warning title=Pages size budget exceeded::"
            f"Staged site is {size_mib:,.1f} MiB; warning threshold is "
            f"{manifest.size_budget_bytes:,} bytes. Reduce it before switching Pages to Actions."
        )
    if manifest.archive_bytes > manifest.archive_size_budget_bytes:
        print(
            "::warning title=Pages archive budget exceeded::"
            f"Tar requires {manifest.archive_bytes:,} bytes including headers/padding; "
            f"budget is {manifest.archive_size_budget_bytes:,}. Deployment is blocked."
        )
    if manifest.off_base_path_links:
        print(
            "::warning title=Pages links missing site prefix::"
            f"{manifest.off_base_path_links:,} likely off-base links; "
            "see off_base_path_urls in the manifest. Deployment is blocked."
        )
    if manifest.broken_local_links:
        print(
            "::warning title=Broken local Pages links::"
            f"{manifest.broken_local_links:,} missing static targets; "
            "see broken_local_link_paths in the manifest. Deployment is blocked."
        )
    if manifest.linked_source_files_not_staged:
        linked_size_mib = manifest.linked_source_bytes_not_staged / MIB
        print(
            "::warning title=Linked files are outside the Pages artifact::"
            f"Published files link to {manifest.linked_source_files_not_staged:,} "
            f"existing repository files ({linked_size_mib:,.1f} MiB) that are not "
            "staged. Resolve these omissions before deployment."
        )


if __name__ == "__main__":
    main()
