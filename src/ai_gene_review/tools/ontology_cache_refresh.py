"""Recheck corpus terms in a fresh LTV cache, then verify that cache offline.

Unlike warming, refresh never reads the retained LTV label or membership cache
during validation. Only a complete, covered run without blocking findings may
produce an applicable candidate. Ontology changes and service failures remain
visible in the report; neither permits an unchecked cache to replace the keeper.

The supported corpus is the same as ontology_cache_coverage: gene, prediction,
and PANTHER family reviews. Module-specific validators are not covered here.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import os
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

from ai_gene_review.tools import ontology_cache_coverage as coverage
from ai_gene_review.tools.cache_lint import check_file


def digest(path: Path) -> str:
    """Hash a file without loading large ontology snapshots into memory."""
    checksum = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            checksum.update(block)
    return checksum.hexdigest()


def inventory(folder: Path) -> dict[str, str]:
    """Fingerprint retained data; transient lock files are not cache content."""
    if any(p.is_symlink() for p in folder.rglob("*")):
        raise ValueError(f"Cache must not contain symbolic links: {folder}")
    return {
        p.relative_to(folder).as_posix(): digest(p)
        for p in sorted(folder.rglob("*"))
        if p.is_file() and not p.name.endswith(".lock")
    }


def fingerprint(paths: list[Path], root: Path) -> str:
    """Hash names and contents together, recording a corpus without copying it."""
    records = []
    for path in sorted(set(p.resolve() for p in paths)):
        name = (
            path.relative_to(root).as_posix()
            if path.is_relative_to(root)
            else str(path)
        )
        records.append([name, digest(path)])
    return hashlib.sha256(yaml.safe_dump(records).encode()).hexdigest()


def source_provenance(config: Path, root: Path) -> dict:
    """Describe adapters and hash available local sources, without fetching more.

    OLS is live: an adapter URL and retrieval time are not an immutable release.
    A refreshed LTV cache also does not update an existing OAK SQLite database.
    """
    adapters = (yaml.safe_load(config.read_text()) or {}).get("ontology_adapters", {})
    sources = []
    for prefix, adapter in sorted(adapters.items()):
        if not isinstance(adapter, str):
            continue
        path = None
        if adapter.startswith("sqlite:obo:"):
            path = (
                Path.home()
                / ".data/oaklib"
                / f"{adapter.removeprefix('sqlite:obo:')}.db"
            )
        elif adapter.startswith("simpleobo:"):
            path = root / adapter.removeprefix("simpleobo:")
        if path is not None and path.is_file():
            sources.append(
                {"prefix": prefix, "adapter": adapter, "sha256": digest(path)}
            )
    return {
        "adapters": adapters,
        "local_sources": sources,
        "source_note": "OLS is live and unpinned. Local source hashes identify snapshots where available; missing hashes do not assert a pinned release.",
    }


def run_batch(
    kind: coverage.DocumentKind,
    files: list[Path],
    offline: bool,
    fresh: Path,
    root: Path,
    config: Path,
    timeout: float,
    attempts: int,
) -> tuple[str, int, str | None]:
    """Run actual LTV, retrying only timeouts and explicit service outages."""
    command = coverage.ltv_command(kind, files, offline, fresh)
    command[command.index("-c") + 1] = str(config)
    for attempt in range(attempts):
        reason = None
        try:
            result = subprocess.run(
                command,
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
                timeout=timeout,
                env={**os.environ, "NO_COLOR": "1", "TERM": "dumb", "FORCE_COLOR": "0"},
            )
            output = result.stdout + "\n" + result.stderr
            code = result.returncode
            if "Traceback (most recent call last):" in output:
                return output, code, "validator failed"
            outcome = coverage.classify_online_pass(output, code)
            if outcome != "outage":
                return output, code, None if outcome == "ok" else "validator failed"
            reason = "service unavailable"
        except subprocess.TimeoutExpired:
            output, code, reason = (
                "Validator exceeded the per-batch timeout",
                2,
                "timeout",
            )
        if offline or attempt + 1 == attempts:
            return output, code, reason
        time.sleep(min(2 ** (attempt + 1), 8))
    raise AssertionError("attempts must be positive")


def read_rows(path: Path) -> tuple[list[str], dict[str, dict[str, str]]]:
    """Read an LTV CSV, keyed by its CURIE column."""
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        header = list(reader.fieldnames or [])
        if not header or header[0] != "curie":
            raise ValueError(f"Not an LTV CURIE cache: {path}")
        rows: list[dict[str, str]] = []
        for row in reader:
            if any(key is None or value is None for key, value in row.items()):
                raise ValueError(f"Malformed cache row in {path}")
            rows.append(
                {
                    key: value
                    for key, value in row.items()
                    if key is not None and value is not None
                }
            )
    result = {row["curie"]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError(f"Duplicate CURIEs in {path}")
    return header, result


def make_candidate(retained: Path, fresh: Path, candidate: Path) -> dict:
    """Overlay revalidated entries, retaining unrelated data and stable timestamps.

    Labels outside this corpus are retained, explicitly not claimed refreshed.
    Refreshed enum files contain only the newly proven memberships. Their old
    completion markers are removed, because a corpus is not a full closure.
    """
    shutil.copytree(retained, candidate, ignore=shutil.ignore_patterns("*.lock"))
    changes: dict = {
        "labels_added": [],
        "labels_changed": [],
        "enum_memberships_added": 0,
        "enum_memberships_removed": 0,
    }
    for source in sorted(fresh.rglob("*.csv")):
        if check_file(source):
            raise ValueError(f"Invalid generated cache ordering: {source}")
        relative = source.relative_to(fresh)
        if not (relative.parts[0] == "enums" or source.name == "terms.csv"):
            raise ValueError(f"Unexpected LTV output: {relative}")
        target = candidate / relative
        header, new = read_rows(source)
        old_header, old = read_rows(target) if target.exists() else (header, {})
        if header != old_header:
            raise ValueError(f"Cache format changed: {relative}")
        if "label" in header:
            for curie, row in new.items():
                previous = old.get(curie)
                if previous is None:
                    changes["labels_added"].append(curie)
                elif previous["label"] != row["label"]:
                    changes["labels_changed"].append(
                        {
                            "curie": curie,
                            "before": previous["label"],
                            "after": row["label"],
                        }
                    )
                else:
                    row["retrieved_at"] = previous.get("retrieved_at", "")
            rows = old | new
        else:
            changes["enum_memberships_added"] += len(new.keys() - old.keys())
            changes["enum_memberships_removed"] += len(old.keys() - new.keys())
            rows = new
            target.with_suffix(".csv.complete").unlink(missing_ok=True)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=header, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows[key] for key in sorted(rows))
    return changes


def apply_candidate(candidate: Path, retained: Path, expected: dict[str, str]) -> None:
    """Swap the cache only after checks, restoring it if the replacement fails."""
    with tempfile.TemporaryDirectory(
        prefix=".ontology-cache-swap-", dir=retained.parent
    ) as directory:
        stage = Path(directory)
        replacement, backup = stage / "replacement", stage / "previous"
        shutil.copytree(candidate, replacement)
        if inventory(retained) != expected:
            raise ValueError(
                "Retained cache changed during refresh; refusing to overwrite it"
            )
        retained.rename(backup)
        try:
            replacement.rename(retained)
        except OSError:
            backup.rename(retained)
            raise


def refresh(
    grouped: dict[coverage.DocumentKind, list[Path]],
    *,
    root: Path,
    cache_dir: Path,
    output_dir: Path,
    oak_config: Path,
    apply: bool = False,
    attempts: int = 3,
    timeout: float = 600,
) -> dict:
    """Build and check a fresh cache; emit diagnostics even when validation fails."""
    root, cache_dir, output_dir, oak_config = (
        p.resolve() for p in (root, cache_dir, output_dir, oak_config)
    )
    work = [
        (kind, batch)
        for kind, paths in grouped.items()
        for batch in coverage.batches([p.resolve() for p in paths])
    ]
    if not work:
        raise ValueError("No review files to refresh")
    if attempts < 1 or timeout <= 0:
        raise ValueError("Attempts and timeout must be positive")
    if output_dir.is_relative_to(cache_dir) or cache_dir.is_relative_to(output_dir):
        raise ValueError("Output and retained cache paths must not overlap")
    if not cache_dir.is_dir():
        raise ValueError(f"Retained cache directory does not exist: {cache_dir}")
    before = inventory(cache_dir)
    output_dir.mkdir(parents=True, exist_ok=False)
    fresh = output_dir / "fresh-cache"
    fresh.mkdir()
    inputs = [p for _, batch in work for p in batch]
    schemas = sorted(
        {p.resolve() for kind in grouped for p in kind.schema.parent.glob("*.yaml")}
    )
    report: dict = {
        "ready": False,
        "applied": False,
        "failures": [],
        "changed_files": [],
        "provenance": {
            "started_utc": datetime.now(timezone.utc).isoformat(),
            "ltv_version": importlib.metadata.version("linkml-term-validator"),
            "oaklib_version": importlib.metadata.version("oaklib"),
            "input_files": len(inputs),
            "input_sha256": fingerprint(inputs, root),
            "schema_sha256": fingerprint(schemas, root),
            "oak_config_sha256": digest(oak_config),
            "refresh_scope": "Terms checked by LTV in the supplied gene, prediction and family reviews; not module-specific or arbitrary ontology metadata checks.",
        },
    }
    for phase, offline in [("online", False), ("offline", True)]:
        result = coverage.CoverageReport(remote=coverage.remote_prefixes(oak_config))
        for number, (kind, batch) in enumerate(work, 1):
            print(
                f"[{phase}] batch {number}/{len(work)}: {len(batch)} files",
                file=sys.stderr,
                flush=True,
            )
            output, code, failure = run_batch(
                kind, batch, offline, fresh, root, oak_config, timeout, attempts
            )
            (output_dir / f"{phase}-{number:04}.log").write_text(output)
            prior = len(result.unchecked_files)
            coverage.parse_offline_output(output, code, batch, result)
            result.files_checked += len(batch) - (len(result.unchecked_files) - prior)
            if failure:
                report["failures"].append(
                    {"phase": phase, "batch": number, "reason": failure}
                )
                break
        report[phase] = result.to_dict()
        if (
            report["failures"]
            or not result.complete
            or result.files_checked != len(inputs)
        ):
            break
    report["provenance"].update(source_provenance(oak_config, root))
    report["provenance"]["finished_utc"] = datetime.now(timezone.utc).isoformat()
    phases = [report.get(name, {}) for name in ("online", "offline")]
    report["ready"] = not report["failures"] and all(
        phase.get("complete")
        and phase.get("covered")
        and phase.get("files_checked") == len(inputs)
        and not phase.get("blocking_label_mismatches")
        and not any(f["severity"] == "ERROR" for f in phase.get("other_findings", []))
        for phase in phases
    )
    if (
        fingerprint(inputs, root) != report["provenance"]["input_sha256"]
        or fingerprint(schemas, root) != report["provenance"]["schema_sha256"]
        or digest(oak_config) != report["provenance"]["oak_config_sha256"]
    ):
        report["ready"] = False
        report["failures"].append(
            {"reason": "Inputs or validation definitions changed during refresh"}
        )
    if report["ready"]:
        candidate = output_dir / "candidate-cache"
        report["changes"] = make_candidate(cache_dir, fresh, candidate)
        after = inventory(candidate)
        report["changed_files"] = sorted(
            name
            for name in before.keys() | after.keys()
            if before.get(name) != after.get(name)
        )
        if apply:
            apply_candidate(candidate, cache_dir, before)
            report["applied"] = True
    (output_dir / "report.yaml").write_text(yaml.safe_dump(report, sort_keys=False))
    summary = [
        "Refresh ontology term caches",
        "============================",
        "",
        f"Ready for cache update: **{report['ready']}**",
        "",
        f"Corpus: {len(inputs)} files. LTV {report['provenance']['ltv_version']}.",
        f"Changed cache files: {len(report['changed_files'])}.",
        "",
        "See the workflow artifact's report.yaml for coverage, findings and source hashes.",
        "This refresh does not edit gene reviews or provider research. Refreshed enums remain partial; labels outside the corpus are retained, not claimed refreshed.",
        "",
        "## Provenance",
        "",
        "```yaml",
        yaml.safe_dump(report["provenance"], sort_keys=False).rstrip(),
        "```",
        "",
        "Refs #5731.",
        "",
    ]
    (output_dir / "summary.md").write_text("\n".join(summary))
    return report


def main(argv: list[str] | None = None) -> int:
    """Refresh the supported corpus, optionally applying a verified candidate."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "inputs",
        nargs="*",
        type=Path,
        default=[Path("genes"), Path("interpro/panther")],
    )
    parser.add_argument("--cache-dir", type=Path, default=Path("cache"))
    parser.add_argument(
        "--output-dir", type=Path, default=Path("reports/ontology-cache-refresh")
    )
    parser.add_argument("--oak-config", type=Path, default=coverage.OAK_CONFIG)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Replace retained cache only after successful online and offline checks",
    )
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument(
        "--timeout", type=float, default=600, help="Seconds per validator batch"
    )
    args = parser.parse_args(argv)
    report = refresh(
        coverage.expand_inputs(args.inputs),
        root=coverage.PROJECT_ROOT,
        cache_dir=args.cache_dir,
        output_dir=args.output_dir,
        oak_config=args.oak_config,
        apply=args.apply,
        attempts=args.attempts,
        timeout=args.timeout,
    )
    return 0 if report["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
