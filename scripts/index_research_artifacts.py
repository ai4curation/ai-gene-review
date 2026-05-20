#!/usr/bin/env python3
"""Build an index of Edison artifacts recorded in deep-research reports.

By default this scans genes/** for deep-research Markdown files, excluding
paired citations files, and writes reports/research_artifact_index.yaml.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


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


def is_deep_research_report(path: Path) -> bool:
    """Return True for report files and False for citations sidecars."""
    name = path.name
    return (
        path.suffix == ".md"
        and "-deep-research" in name
        and not name.endswith("-citations.md")
        and not name.endswith(".citations.md")
    )


def provider_from_filename(name: str) -> str | None:
    """Infer provider from a deep-research filename."""
    stem = name.removesuffix(".md")
    marker = "-deep-research-"
    if marker in stem:
        provider = stem.rsplit(marker, 1)[-1]
        return provider or None
    return None


def report_context(report_path: Path, root: Path) -> tuple[str | None, str | None]:
    """Infer organism and gene directory names for reports under genes/."""
    try:
        relative = report_path.relative_to(root)
    except ValueError:
        return None, None
    parts = relative.parts
    if len(parts) >= 3:
        return parts[0], parts[1]
    return None, None


def resolved_artifact_path(report_path: Path, root: Path, artifact_path: str) -> str:
    """Resolve an artifact path relative to root for collision detection."""
    candidate = (report_path.parent / artifact_path).resolve()
    try:
        return candidate.relative_to(root.resolve()).as_posix()
    except ValueError:
        return candidate.as_posix()


def build_index(root: Path) -> dict[str, Any]:
    """Scan root recursively for deep-research reports and build an index."""
    report_files = sorted(
        path for path in root.rglob("*.md") if is_deep_research_report(path)
    )

    reports: list[dict[str, Any]] = []
    index_by_trajectory_id: dict[str, dict[str, Any]] = {}
    path_map: dict[str, list[str]] = defaultdict(list)

    for report_path in report_files:
        try:
            text = report_path.read_text(encoding="utf-8")
        except OSError:
            continue

        metadata, _ = split_frontmatter(text)
        artifacts = metadata.get("artifacts") or []
        if not isinstance(artifacts, list):
            artifacts = []

        organism, gene = report_context(report_path, root)
        relative_report = report_path.relative_to(root).as_posix()
        provider = metadata.get("provider") or provider_from_filename(report_path.name)
        entry: dict[str, Any] = {
            "file": relative_report,
            "organism": organism,
            "gene": gene,
            "provider": provider,
            "model": metadata.get("model"),
            "trajectory_id": metadata.get("trajectory_id"),
            "citation_count": metadata.get("citation_count"),
            "artifact_count": metadata.get("artifact_count", len(artifacts)),
            "artifacts": [],
        }

        for artifact in artifacts:
            if not isinstance(artifact, dict):
                continue
            path = artifact.get("path")
            resolved_path = (
                resolved_artifact_path(report_path, root, str(path)) if path else None
            )
            artifact_entry = {
                "filename": artifact.get("filename"),
                "path": path,
                "resolved_path": resolved_path,
                "media_type": artifact.get("media_type"),
                "is_image": str(artifact.get("media_type") or "").startswith("image/"),
            }
            entry["artifacts"].append(artifact_entry)
            if resolved_path:
                path_map[resolved_path].append(relative_report)

        reports.append(entry)

        trajectory_id = entry.get("trajectory_id")
        if trajectory_id:
            if trajectory_id in index_by_trajectory_id:
                existing = index_by_trajectory_id[trajectory_id]
                existing["_collision"] = True
                if "reports" not in existing:
                    first_report = existing.pop("report", None)
                    existing["reports"] = [first_report] if first_report else []
                existing["reports"].append(relative_report)
            else:
                index_by_trajectory_id[trajectory_id] = {
                    "report": relative_report,
                    "provider": entry["provider"],
                    "artifact_count": entry["artifact_count"],
                    "artifact_paths": [
                        artifact["resolved_path"]
                        for artifact in entry["artifacts"]
                        if artifact.get("resolved_path")
                    ],
                }

    collisions = []
    for artifact_path, report_list in sorted(path_map.items()):
        unique_reports = list(dict.fromkeys(report_list))
        if len(unique_reports) > 1:
            collisions.append({"path": artifact_path, "reports": unique_reports})

    reports_with_artifacts = [
        report for report in reports if report["artifact_count"] > 0
    ]
    return {
        "generated": datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "root": root.as_posix(),
        "report_count": len(reports),
        "reports_with_artifacts_count": len(reports_with_artifacts),
        "artifact_total": sum(
            report["artifact_count"] for report in reports_with_artifacts
        ),
        "collision_count": len(collisions),
        "reports": reports,
        "index_by_trajectory_id": index_by_trajectory_id,
        "collisions": collisions,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("genes"),
        help="Root directory to scan recursively (default: genes)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output YAML path (default: reports/research_artifact_index.yaml)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if artifact path collisions are detected",
    )
    args = parser.parse_args(argv)

    if not args.root.is_dir():
        print(f"ERROR: root directory not found: {args.root}", file=sys.stderr)
        return 1

    output_path = args.output or Path("reports/research_artifact_index.yaml")
    index = build_index(args.root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        yaml.dump(index, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    print(
        f"Indexed {index['report_count']} reports "
        f"({index['reports_with_artifacts_count']} with artifacts, "
        f"{index['artifact_total']} total artifacts): {output_path}"
    )

    if index["collisions"]:
        print(f"WARNING: {index['collision_count']} artifact path collision(s):")
        for collision in index["collisions"]:
            print(f"  {collision['path']}: {', '.join(collision['reports'])}")
        if args.check:
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
