"""Assemble generated web output into a GitHub Pages artifact directory.

The renderers intentionally keep writing gene HTML beside the review YAML so a
curator can open a page locally.  This module collects only the files needed by
the public site into a disposable directory, providing a boundary between
source data and deployable output.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from ai_gene_review.tools.pages_dependencies import TEXT_ASSETS, linked_repository_files


MIB = 1024 * 1024
BROWSER_FILES = ("index.html", "data.js", "schema.js")



@dataclass(frozen=True)
class SiteManifest:
    """Summary of files copied into the Pages staging directory."""

    total_bytes: int
    total_files: int
    gene_pages: int
    project_pages: int
    module_pages: int
    linked_source_files_not_staged: int
    linked_source_bytes_not_staged: int


def _copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def _require_file(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"Required Pages input is missing: {path}")


def _safe_clean_output(repo_root: Path, output_dir: Path) -> None:
    """Only remove the repository's dedicated, ignored staging directory."""
    resolved_root = repo_root.resolve()
    resolved_output = output_dir.resolve()
    if resolved_output == resolved_root or resolved_root not in resolved_output.parents:
        raise ValueError("Pages output directory must be inside the repository root")
    if resolved_output != resolved_root / "_site":
        raise ValueError("Pages output directory must be the repository's _site directory")
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


def _stage_linked_files(repo_root: Path, output_dir: Path) -> set[Path]:
    """Copy static dependencies transitively and return any excluded public files.

    Scan each HTML/CSS/JS file only once. Referenced notes, downloads, reports,
    images, and their dependencies keep their paths and original bytes.
    """
    pending = [p.relative_to(output_dir) for p in output_dir.rglob("*")
               if p.is_file() and p.suffix.lower() in TEXT_ASSETS]
    scanned: set[Path] = set()
    omitted: set[Path] = set()
    while pending:
        relative = pending.pop()
        if relative in scanned:
            continue
        scanned.add(relative)
        content = (output_dir / relative).read_text(errors="ignore")
        for target in linked_repository_files(repo_root, relative, content):
            source = repo_root / target
            destination = output_dir / target
            if not destination.is_file():
                # Keep the existing exclusion of orphan review HTML, even if an
                # old index still links to it. Report it instead of publishing it.
                if source.name.endswith("-ai-review.html") and not source.with_suffix(".yaml").is_file():
                    omitted.add(source)
                    continue
                _copy_file(source, destination)
            if target.suffix.lower() in TEXT_ASSETS and target not in scanned:
                pending.append(target)
    return omitted


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
        preview = ", ".join(str(path.relative_to(repo_root)) for path in missing_pages[:5])
        suffix = (
            ""
            if len(missing_pages) <= 5
            else f" (and {len(missing_pages) - 5} more)"
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

    linked_sources = _stage_linked_files(repo_root, output_dir)
    staged_files = [path for path in output_dir.rglob("*") if path.is_file()]
    manifest = SiteManifest(
        total_bytes=sum(path.stat().st_size for path in staged_files),
        total_files=len(staged_files),
        gene_pages=len(gene_pages),
        project_pages=len(list((output_dir / "pages" / "projects").rglob("*.html"))),
        module_pages=len(list((output_dir / "pages" / "modules").rglob("*.html"))),
        linked_source_files_not_staged=len(linked_sources),
        linked_source_bytes_not_staged=sum(path.stat().st_size for path in linked_sources),
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
        "--warn-size-mib",
        type=int,
        default=1024,
        help="Warn when the uncompressed site exceeds this many MiB",
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
    manifest_json = json.dumps(asdict(manifest), indent=2) + "\n"

    if args.manifest:
        manifest_path = args.manifest
        if not manifest_path.is_absolute():
            manifest_path = repo_root / manifest_path
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(manifest_json)

    size_mib = manifest.total_bytes / MIB
    print(f"Staged {manifest.total_files:,} files in {output_dir}")
    print(f"Uncompressed site size: {size_mib:,.1f} MiB")
    print(
        "Rendered pages: "
        f"{manifest.gene_pages:,} genes, "
        f"{manifest.project_pages:,} projects, "
        f"{manifest.module_pages:,} modules"
    )
    if size_mib > args.warn_size_mib:
        print(
            f"::warning title=Pages size budget exceeded::"
            f"Staged site is {size_mib:,.1f} MiB; warning threshold is "
            f"{args.warn_size_mib:,} MiB. Reduce it before switching Pages to Actions."
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
