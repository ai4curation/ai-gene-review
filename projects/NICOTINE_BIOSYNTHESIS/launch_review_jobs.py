#!/usr/bin/env python3
"""Launch nicotine-biosynthesis review setup jobs from a CSV queue."""

from __future__ import annotations

import argparse
import csv
import shlex
import subprocess
from pathlib import Path
from typing import Iterable

DEFAULT_WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_JOBS_FILE = Path("projects/NICOTINE_BIOSYNTHESIS/review_jobs.csv")


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Fetch/create review stubs for Nicotiana attenuata nicotine pathway jobs."
        )
    )
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=DEFAULT_WORKSPACE_ROOT,
        help=(
            "Repository workspace root. Relative paths are resolved from here and "
            "commands execute with this as the working directory."
        ),
    )
    parser.add_argument(
        "--jobs-file",
        type=Path,
        default=DEFAULT_JOBS_FILE,
        help="CSV file containing review jobs.",
    )
    parser.add_argument(
        "--status",
        default="launch_ready",
        help="Only launch rows with this status value. Default: launch_ready",
    )
    parser.add_argument(
        "--with-deep-research",
        action="store_true",
        help="Also enqueue deep-research runs after fetch-gene.",
    )
    parser.add_argument(
        "--deep-research-provider",
        default="codex",
        choices=["openai", "perplexity", "perplexity-lite", "falcon", "cyberian", "codex"],
        help="Deep-research provider when --with-deep-research is set.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Pass --force to fetch-gene.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only launch the first N matching rows.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print commands without executing them.",
    )
    parser.add_argument(
        "--include-existing",
        action="store_true",
        help=(
            "Rerun jobs whose alias review directory already exists under "
            "genes/<species>/<alias>/."
        ),
    )
    return parser.parse_args()


def load_jobs(path: Path) -> list[dict[str, str]]:
    """Load review jobs from CSV."""
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def resolve_path(path: Path, workspace_root: Path) -> Path:
    """Resolve a path relative to the workspace root."""
    if path.is_absolute():
        return path
    return workspace_root / path


def job_review_file(job: dict[str, str], workspace_root: Path) -> Path:
    """Return the seeded review path for a queued alias."""
    alias = job["alias"]
    return workspace_root / "genes" / job["species"] / alias / f"{alias}-ai-review.yaml"


def collect_matching_jobs(
    jobs: Iterable[dict[str, str]],
    status: str,
    workspace_root: Path,
    include_existing: bool = False,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    """Split rows into selected, already-launched, and unresolved buckets."""
    selected: list[dict[str, str]] = []
    existing: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []

    for job in jobs:
        if job.get("status") != status:
            continue
        if not job.get("fetch_id"):
            unresolved.append(job)
            continue
        if job_review_file(job, workspace_root).exists():
            existing.append(job)
            if include_existing:
                selected.append(job)
            continue
        selected.append(job)

    return selected, existing, unresolved


def build_fetch_command(job: dict[str, str], force: bool) -> list[str]:
    """Build the just fetch-gene command for a single job row."""
    command = [
        "just",
        "fetch-gene",
        job["species"],
        job["fetch_id"],
        "--alias",
        job["alias"],
    ]
    if force:
        command.append("--force")
    return command


def build_deep_research_command(job: dict[str, str], provider: str) -> list[str]:
    """Build the just deep-research command for a single job row."""
    return [
        "just",
        f"deep-research-{provider}",
        job["species"],
        job["fetch_id"],
        "--alias",
        job["alias"],
    ]


def run_command(command: list[str], dry_run: bool, cwd: Path) -> None:
    """Run or print a command."""
    printable = shlex.join(command)
    print(f"$ {printable}")
    if not dry_run:
        subprocess.run(command, check=True, cwd=cwd)


def main() -> None:
    """Entry point."""
    args = parse_args()
    workspace_root = args.workspace_root.resolve()
    jobs_file = resolve_path(args.jobs_file, workspace_root)
    jobs = load_jobs(jobs_file)
    matching_jobs = [job for job in jobs if job.get("status") == args.status]
    runnable, existing, unresolved = collect_matching_jobs(
        jobs=jobs,
        status=args.status,
        workspace_root=workspace_root,
        include_existing=args.include_existing,
    )
    new_launch_count = len(runnable) - (len(existing) if args.include_existing else 0)

    if args.limit is not None:
        runnable = runnable[: args.limit]

    print(f"Workspace root: {workspace_root}")
    print(f"Jobs file: {jobs_file}")
    print(f"Matching rows for status={args.status!r}: {len(matching_jobs)}")
    print(f"  new launch targets: {new_launch_count}")
    print(f"  already launched aliases: {len(existing)}")
    print(f"  unresolved rows: {len(unresolved)}")
    print(f"  selected for execution: {len(runnable)}")

    if not runnable:
        print("No jobs selected for execution.")
        if existing and not args.include_existing:
            print(
                "Use --include-existing to rerun aliases that already have seeded review files."
            )
        if unresolved:
            print("\nUnresolved rows:")
            for job in unresolved:
                print(f"- {job['job_id']}: {job['canonical_symbol']} ({job['notes']})")
        return

    for index, job in enumerate(runnable, start=1):
        print(f"\n[{index}/{len(runnable)}] {job['job_id']} -> {job['alias']}")
        run_command(
            build_fetch_command(job, args.force),
            args.dry_run,
            cwd=workspace_root,
        )
        if args.with_deep_research:
            run_command(
                build_deep_research_command(job, args.deep_research_provider),
                args.dry_run,
                cwd=workspace_root,
            )

    if unresolved:
        print("\nUnresolved rows:")
        for job in unresolved:
            print(f"- {job['job_id']}: {job['canonical_symbol']} ({job['notes']})")


if __name__ == "__main__":
    main()
