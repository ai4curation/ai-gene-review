#!/usr/bin/env python3
"""Fetch and record artifacts from an Edison deep-research trajectory.

This script saves artifacts beside a gene deep-research report and updates the
report frontmatter with trajectory and artifact metadata. It requires
EDISON_API_KEY, but most helper functions are pure enough to test without live
Edison access.

Example:
    uv run python scripts/fetch_edison_artifacts.py \
        0ab9e2d2-7601-4bbe-ba01-e26bfce94cfd \
        genes/human/TP53/TP53-deep-research-falcon.md
"""

from __future__ import annotations

import argparse
import base64
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class ArtifactRecord:
    """Normalized Edison artifact payload used by the writer and frontmatter."""

    filename: str
    content_base64: str
    media_type: str | None = None
    source: str | None = None
    data_storage_id: str | None = None
    description: str | None = None
    path: str | None = None


def _load_api_key() -> str:
    """Return EDISON_API_KEY, falling back to FUTUREHOUSE_API_KEY."""
    key = os.getenv("EDISON_API_KEY") or os.getenv("FUTUREHOUSE_API_KEY")
    if key:
        return key.strip()
    raise SystemExit(
        "EDISON_API_KEY is not set.\n"
        "Export it before running this script, for example:\n"
        "    export EDISON_API_KEY=<your-api-key>"
    )


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return (frontmatter_dict, body) from Markdown text."""
    normalized = text.replace("\r\n", "\n")
    lines = normalized.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, normalized

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            try:
                metadata = yaml.safe_load("\n".join(lines[1:index])) or {}
            except yaml.YAMLError:
                return {}, normalized
            if not isinstance(metadata, dict):
                metadata = {}
            return metadata, "\n".join(lines[index + 1 :])

    return {}, normalized


def safe_artifact_filename(filename: str, fallback: str) -> str:
    """Return a path-safe artifact filename without directory components."""
    name = Path(str(filename or "")).name.strip()
    if not name:
        name = fallback
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name)
    return name or fallback


def artifact_directory_for_report(report_file: Path) -> Path:
    """Return the artifact directory for a deep-research report."""
    return report_file.parent / f"{report_file.stem}_artifacts"


def artifact_value(artifact: Any, field: str, default: Any = None) -> Any:
    """Read a field from either a dict-like or attribute-style artifact."""
    if isinstance(artifact, dict):
        return artifact.get(field, default)
    return getattr(artifact, field, default)


def normalize_artifacts(artifacts: list[Any]) -> list[ArtifactRecord]:
    """Convert Edison/deep-research-client artifact objects to records."""
    records: list[ArtifactRecord] = []
    used_names: set[str] = set()

    for index, artifact in enumerate(artifacts, start=1):
        filename = safe_artifact_filename(
            str(artifact_value(artifact, "filename", "")),
            fallback=f"artifact_{index}",
        )
        if filename in used_names:
            stem = Path(filename).stem or f"artifact_{index}"
            suffix = Path(filename).suffix
            counter = 2
            while f"{stem}_{counter}{suffix}" in used_names:
                counter += 1
            filename = f"{stem}_{counter}{suffix}"
        used_names.add(filename)

        records.append(
            ArtifactRecord(
                filename=filename,
                content_base64=str(artifact_value(artifact, "content_base64", "")),
                media_type=artifact_value(artifact, "media_type"),
                source=artifact_value(artifact, "source"),
                data_storage_id=artifact_value(artifact, "data_storage_id"),
                description=artifact_value(artifact, "description"),
            )
        )

    return records


def write_artifacts(
    records: list[ArtifactRecord],
    report_file: Path,
    *,
    overwrite: bool = False,
) -> list[ArtifactRecord]:
    """Decode and write artifact records beside report_file."""
    artifact_dir = artifact_directory_for_report(report_file)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    written: list[ArtifactRecord] = []
    for record in records:
        content = base64.b64decode(record.content_base64)
        destination = artifact_dir / record.filename
        if (
            destination.exists()
            and not overwrite
            and destination.read_bytes() != content
        ):
            raise FileExistsError(
                f"Refusing to overwrite existing artifact with different content: {destination}"
            )
        destination.write_bytes(content)
        record.path = destination.relative_to(report_file.parent).as_posix()
        written.append(record)

    return written


def artifact_metadata(records: list[ArtifactRecord]) -> list[dict[str, Any]]:
    """Return frontmatter-safe metadata for records."""
    return [
        {
            "filename": record.filename,
            "path": record.path or record.filename,
            "media_type": record.media_type,
            "source": record.source,
            "data_storage_id": record.data_storage_id,
            "description": record.description,
        }
        for record in records
    ]


def render_artifacts_section(records: list[ArtifactRecord]) -> str:
    """Render a Markdown Artifacts section for report bodies."""
    lines = ["\n## Artifacts\n"]
    for record in records:
        path = record.path or record.filename
        label = record.description or record.filename
        if (record.media_type or "").startswith("image/"):
            lines.append(f"![{label}]({path})")
        else:
            lines.append(f"- [{label}]({path})")
    return "\n".join(lines) + "\n"


def update_research_text(
    text: str,
    trajectory_id: str,
    records: list[ArtifactRecord],
) -> str:
    """Return report Markdown updated with trajectory and artifact metadata."""
    metadata, body = split_frontmatter(text)
    metadata["trajectory_id"] = trajectory_id
    metadata["artifact_count"] = len(records)
    metadata["artifacts"] = artifact_metadata(records)

    updated = f"---\n{yaml.dump(metadata, default_flow_style=False, sort_keys=False)}---\n{body}"

    has_artifacts_section = re.search(r"(?m)^## Artifacts\s*$", body) is not None
    if records and not has_artifacts_section:
        section = render_artifacts_section(records)
        if re.search(r"(?m)^## Citations\s*$", updated):
            updated = re.sub(
                r"(?m)^## Citations\s*$", f"{section}\n## Citations", updated, count=1
            )
        else:
            updated = updated.rstrip() + "\n" + section

    return updated


def fetch_artifacts(
    trajectory_id: str,
    report_file: Path,
    *,
    dry_run: bool = False,
    overwrite: bool = False,
) -> int:
    """Fetch artifacts for trajectory_id and update report_file."""
    from deep_research_client.models import ProviderConfig
    from deep_research_client.providers.falcon import FalconProvider
    from edison_client import EdisonClient
    from edison_client.models.app import TaskResponseVerbose

    api_key = _load_api_key()
    client = EdisonClient(api_key=api_key)

    print(f"Fetching trajectory {trajectory_id} ...")
    task_response = client.get_task(trajectory_id, verbose=True)

    if not isinstance(task_response, TaskResponseVerbose):
        print(f"Unexpected response type: {type(task_response)}", file=sys.stderr)
        return 0

    print(f"Task status: {task_response.status}")
    provider = FalconProvider(ProviderConfig(name="falcon", api_key=api_key))
    artifacts = provider._extract_artifacts(client, [task_response])
    records = normalize_artifacts(artifacts)

    if not records:
        print("No artifacts found in trajectory.")
        return 0

    print(f"Found {len(records)} artifact(s).")
    if dry_run:
        for record in records:
            print(f"  Would save: {record.filename}")
        return len(records)

    written = write_artifacts(records, report_file, overwrite=overwrite)
    updated = update_research_text(
        report_file.read_text(encoding="utf-8"), trajectory_id, written
    )
    report_file.write_text(updated, encoding="utf-8")
    for record in written:
        print(f"  Saved artifact: {record.path}")
    print(f"Updated frontmatter: {report_file}")
    return len(written)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trajectory_id", help="Edison trajectory UUID")
    parser.add_argument("research_file", type=Path, help="Deep-research Markdown file")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and list artifacts without writing files or updating Markdown",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow existing artifact files to be overwritten",
    )
    args = parser.parse_args(argv)

    if not args.research_file.exists():
        print(f"ERROR: research file not found: {args.research_file}", file=sys.stderr)
        return 1

    count = fetch_artifacts(
        args.trajectory_id,
        args.research_file,
        dry_run=args.dry_run,
        overwrite=args.overwrite,
    )
    print(f"Done: {count} artifact(s) processed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
