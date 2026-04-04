#!/usr/bin/env python3
"""Launch nicotine-biosynthesis review setup jobs from a CSV queue."""

from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path
from typing import Iterable


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Fetch/create review stubs for Nicotiana attenuata nicotine pathway jobs."
        )
    )
    parser.add_argument(
        "--jobs-file",
        type=Path,
        default=Path("projects/NICOTINE_BIOSYNTHESIS/review_jobs.csv"),
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
    return parser.parse_args()


def load_jobs(path: Path) -> list[dict[str, str]]:
    """Load review jobs from CSV."""
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def iter_matching_jobs(
    jobs: Iterable[dict[str, str]], status: str
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Split jobs into runnable and unresolved rows for a given status."""
    runnable: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []

    for job in jobs:
        if job.get("status") != status:
            continue
        if job.get("fetch_id"):
            runnable.append(job)
        else:
            unresolved.append(job)

    return runnable, unresolved


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


def run_command(command: list[str], dry_run: bool) -> None:
    """Run or print a command."""
    printable = " ".join(command)
    print(f"$ {printable}")
    if not dry_run:
        subprocess.run(command, check=True)


def main() -> None:
    """Entry point."""
    args = parse_args()
    jobs = load_jobs(args.jobs_file)
    runnable, unresolved = iter_matching_jobs(jobs, args.status)

    if args.limit is not None:
        runnable = runnable[: args.limit]

    if not runnable:
        print(f"No runnable jobs found with status={args.status!r}")
        if unresolved:
            print(f"Unresolved rows with matching status: {len(unresolved)}")
        return

    for job in runnable:
        run_command(build_fetch_command(job, args.force), args.dry_run)
        if args.with_deep_research:
            run_command(
                build_deep_research_command(job, args.deep_research_provider),
                args.dry_run,
            )

    if unresolved:
        print("\nUnresolved rows:")
        for job in unresolved:
            print(f"- {job['job_id']}: {job['canonical_symbol']} ({job['notes']})")


if __name__ == "__main__":
    main()

