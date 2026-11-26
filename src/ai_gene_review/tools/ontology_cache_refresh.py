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
    adapters = (yaml.safe_load(config.read_text(encoding="utf-8")) or {}).get(
        "ontology_adapters", {}
    )
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
    deadline: float | None = None,
) -> tuple[str, int, str | None]:
    """Run actual LTV, retrying only timeouts and explicit service outages."""
    command = coverage.ltv_command(kind, files, offline, fresh, config=config)
    if not offline:
        command.append("--saturate-enum-caches")
    for attempt in range(attempts):
        remaining = (
            timeout if deadline is None else min(timeout, deadline - time.monotonic())
        )
        if remaining <= 0:
            return "Total runtime budget exhausted", 2, "runtime budget exhausted"
        reason = None
        try:
            result = subprocess.run(
                command,
                cwd=root,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
                timeout=remaining,
                env={
                    **os.environ,
                    "NO_COLOR": "1",
                    "TERM": "dumb",
                    "FORCE_COLOR": "0",
                    "PYTHONIOENCODING": "utf-8",
                    "PYTHONUTF8": "1",
                },
            )
            output = result.stdout + "\n" + result.stderr
            code = result.returncode
            if "Traceback (most recent call last):" in output:
                return output, code, "validator failed"
            outcome = coverage.classify_online_pass(output, code)
            if outcome != "outage":
                return output, code, None if outcome == "ok" else "validator failed"
            reason = "service unavailable"
        except subprocess.TimeoutExpired as exc:
            parts = [
                part.decode("utf-8", errors="replace")
                if isinstance(part, bytes)
                else part
                for part in (exc.stdout, exc.stderr)
                if part
            ]
            output = "\n".join(parts) + "\nValidator exceeded its runtime limit"
            code = 2
            reason = (
                "runtime budget exhausted"
                if deadline is not None and time.monotonic() >= deadline
                else "timeout"
            )
        if offline or attempt + 1 == attempts:
            return output, code, reason
        delay = float(min(2 ** (attempt + 1), 8))
        if deadline is not None:
            delay = max(0.0, min(delay, deadline - time.monotonic()))
        time.sleep(delay)
    raise AssertionError("attempts must be positive")


def read_rows(path: Path) -> tuple[list[str], dict[str, dict[str, str]]]:
    """Read an LTV CSV, keyed by its CURIE column."""
    with path.open(newline="", encoding="utf-8") as handle:
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
    Fresh completion markers are retained only with their matching enum CSV.
    The caller must reject incomplete closures and unapproved membership losses.
    """
    shutil.copytree(retained, candidate, ignore=shutil.ignore_patterns("*.lock"))
    changes: dict = {
        "labels_added": [],
        "labels_changed": [],
        "enum_memberships_added": 0,
        "enum_memberships_removed": 0,
        "enums": [],
        "incomplete_enums": [],
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
            added, removed = len(new.keys() - old.keys()), len(old.keys() - new.keys())
            changes["enum_memberships_added"] += added
            changes["enum_memberships_removed"] += removed
            rows = new
            marker = source.with_suffix(".csv.complete")
            complete = (
                marker.is_file()
                and marker.read_text(encoding="utf-8").strip() == "complete"
            )
            changes["enums"].append(
                {
                    "file": relative.as_posix(),
                    "before": len(old),
                    "after": len(new),
                    "added": added,
                    "removed": removed,
                    "complete": complete,
                }
            )
            target.parent.mkdir(parents=True, exist_ok=True)
            target_marker = target.with_suffix(".csv.complete")
            if complete:
                shutil.copyfile(marker, target_marker)
            else:
                target_marker.unlink(missing_ok=True)
                changes["incomplete_enums"].append(relative.as_posix())
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=header, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows[key] for key in sorted(rows))
    return changes


def apply_candidate(candidate: Path, retained: Path, expected: dict[str, str]) -> None:
    """Swap the cache only after checks, restoring it if the replacement fails."""
    # Do not put the sole retained copy in an auto-deleted TemporaryDirectory.
    # A killed process leaves this recovery directory on disk.
    stage = Path(tempfile.mkdtemp(prefix=".ontology-cache-swap-", dir=retained.parent))
    replacement, backup = stage / "replacement", stage / "previous"
    try:
        shutil.copytree(candidate, replacement)
        if inventory(retained) != expected:
            raise ValueError(
                "Retained cache changed during refresh; refusing to overwrite it"
            )
        try:
            retained.rename(backup)
            replacement.rename(retained)
        except BaseException:
            # Also recover on KeyboardInterrupt/SystemExit; never delete a backup
            # if restoring it fails or another writer has occupied the old path.
            if backup.exists() and not retained.exists():
                backup.rename(retained)
            raise
    except BaseException:
        if not backup.exists():
            shutil.rmtree(stage)
        raise
    else:
        shutil.rmtree(stage)


def write_report(report: dict, output_dir: Path) -> None:
    """Atomically checkpoint diagnostics and a durable, reviewable PR summary."""
    changes = report.get("changes", {})
    advisory = len(report.get("online", {}).get("advisory_label_mismatches", []))
    summary = [
        "Refresh ontology term caches",
        "",
        f"Ready for cache update: **{report['ready']}**; applied: **{report['applied']}**.",
        f"Status: {report['status']}. Corpus: {report['provenance']['input_files']} files.",
        f"Batches completed/planned: {report['progress']['batches_completed']}/{report['progress']['batches_planned']}.",
        f"Elapsed seconds: {report['progress']['elapsed_seconds']:.1f}.",
        f"Changed cache files: {len(report['changed_files'])}.",
        "",
        "## Semantic changes",
        "",
        f"Labels added: {len(changes.get('labels_added', []))}; labels changed: {len(changes.get('labels_changed', []))}.",
        f"Memberships added: **{changes.get('enum_memberships_added', 0)}**; removed: **{changes.get('enum_memberships_removed', 0)}**.",
        f"Advisory label mismatches: **{advisory}** (online pass; offline repeats are not double-counted).",
        "Candidate counts describe only generated files; an incomplete run does not certify a refresh.",
        "",
        "```yaml",
        yaml.safe_dump(changes, sort_keys=False, allow_unicode=True).rstrip(),
        "```",
        "",
        "## Failures",
        "",
        yaml.safe_dump(
            report["failures"], sort_keys=False, allow_unicode=True
        ).rstrip(),
        "",
        "## Provenance",
        "",
        "```yaml",
        yaml.safe_dump(
            report["provenance"], sort_keys=False, allow_unicode=True
        ).rstrip(),
        "```",
        "",
        "Only complete fresh enum closures may be applied; unrelated entries are retained, not claimed refreshed.",
        "Curated records and provider research are unchanged. Refs #5731.",
        "",
    ]
    for name, content in [
        ("report.yaml", yaml.safe_dump(report, sort_keys=False, allow_unicode=True)),
        ("summary.md", "\n".join(summary)),
    ]:
        temporary = output_dir / f".{name}.tmp"
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(output_dir / name)


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
    max_runtime: float = 18000,
    max_enum_removals: int = 0,
) -> dict:
    """Build full closures and replay offline, checkpointing even on failures.

    Membership removals default to zero. A positive removal budget authorizes
    only that many losses; it never bypasses coverage or completeness checks.
    """
    started = time.monotonic()
    root, cache_dir, output_dir, oak_config = (
        p.resolve() for p in (root, cache_dir, output_dir, oak_config)
    )
    work = [
        (coverage.DocumentKind(root / kind.schema, kind.target_class), batch)
        for kind, paths in grouped.items()
        for batch in coverage.batches([root / p for p in paths])
    ]
    if not work:
        raise ValueError("No review files to refresh")
    if attempts < 1 or timeout <= 0 or max_runtime <= 0 or max_enum_removals < 0:
        raise ValueError(
            "Attempts/time limits must be positive and removal budget nonnegative"
        )
    if output_dir.is_relative_to(cache_dir) or cache_dir.is_relative_to(output_dir):
        raise ValueError("Output and retained cache paths must not overlap")
    if not cache_dir.is_dir():
        raise ValueError(f"Retained cache directory does not exist: {cache_dir}")
    if output_dir.exists():
        raise ValueError(
            f"Output directory already exists; choose a new path to preserve earlier evidence: {output_dir}"
        )
    before = inventory(cache_dir)
    output_dir.mkdir(parents=True)
    fresh = output_dir / "fresh-cache"
    fresh.mkdir()
    inputs = [p for _, batch in work for p in batch]
    schemas = sorted(
        {p.resolve() for kind, _ in work for p in kind.schema.parent.glob("*.yaml")}
    )
    report: dict = {
        "ready": False,
        "applied": False,
        "status": "running",
        "failures": [],
        "changed_files": [],
        "progress": {
            "batches_planned": 2 * len(work),
            "batches_completed": 0,
            "elapsed_seconds": 0.0,
        },
        "provenance": {
            "started_utc": datetime.now(timezone.utc).isoformat(),
            "ltv_version": importlib.metadata.version("linkml-term-validator"),
            "oaklib_version": importlib.metadata.version("oaklib"),
            "input_files": len(inputs),
            "max_runtime_seconds": max_runtime,
            "max_enum_removals": max_enum_removals,
            "refresh_scope": "Labels checked by LTV in supplied gene, prediction and family reviews; full closures for encountered enums, including shared definition caches. No module-specific validation.",
        },
    }

    def checkpoint() -> None:
        report["progress"]["elapsed_seconds"] = round(time.monotonic() - started, 3)
        write_report(report, output_dir)

    stage = "prepare"
    checkpoint()
    try:
        report["provenance"].update(
            {
                "input_sha256": fingerprint(inputs, root),
                "schema_sha256": fingerprint(schemas, root),
                "oak_config_sha256": digest(oak_config),
            }
        )
        for phase, offline in [("online", False), ("offline", True)]:
            stage = phase
            result = coverage.CoverageReport(
                remote=coverage.remote_prefixes(oak_config)
            )
            for number, (kind, batch) in enumerate(work, 1):
                report["progress"].update({"phase": phase, "batch": number})
                report[phase] = result.to_dict()
                checkpoint()
                if time.monotonic() >= started + max_runtime:
                    report["failures"].append(
                        {
                            "phase": phase,
                            "batch": number,
                            "reason": "runtime budget exhausted",
                        }
                    )
                    break
                print(
                    f"[{phase}] batch {number}/{len(work)}: {len(batch)} files",
                    file=sys.stderr,
                    flush=True,
                )
                output, code, failure = run_batch(
                    kind,
                    batch,
                    offline,
                    fresh,
                    root,
                    oak_config,
                    timeout,
                    attempts,
                    deadline=started + max_runtime,
                )
                (output_dir / f"{phase}-{number:04}.log").write_text(
                    output, encoding="utf-8"
                )
                coverage.record_batch_output(output, code, batch, result)
                if failure:
                    report["failures"].append(
                        {"phase": phase, "batch": number, "reason": failure}
                    )
                else:
                    report["progress"]["batches_completed"] += 1
                report[phase] = result.to_dict()
                checkpoint()
                if failure or not result.complete:
                    break
            report[phase] = result.to_dict()
            if (
                report["failures"]
                or not result.complete
                or result.files_checked != len(inputs)
            ):
                break
        report["provenance"].update(source_provenance(oak_config, root))
        phases = [report.get(name, {}) for name in ("online", "offline")]
        eligible = not report["failures"] and all(
            phase.get("complete")
            and phase.get("covered")
            and phase.get("files_checked") == len(inputs)
            and not phase.get("blocking_label_mismatches")
            and not any(
                f["severity"] == "ERROR" for f in phase.get("other_findings", [])
            )
            for phase in phases
        )
        if not eligible and not report["failures"]:
            report["failures"].append(
                {
                    "reason": "Validation or offline coverage is incomplete or contains blocking findings"
                }
            )
        if (
            fingerprint(inputs, root) != report["provenance"]["input_sha256"]
            or fingerprint(schemas, root) != report["provenance"]["schema_sha256"]
            or digest(oak_config) != report["provenance"]["oak_config_sha256"]
        ):
            report["failures"].append(
                {"reason": "Inputs or validation definitions changed during refresh"}
            )
        if inventory(cache_dir) != before:
            report["failures"].append(
                {"reason": "Retained cache changed during refresh"}
            )
        # Even a failed pass reports its candidate deltas, without claiming them applicable.
        stage = "candidate"
        inventory(fresh)  # refuse generated symlinks before overlaying
        candidate = output_dir / "candidate-cache"
        report["changes"] = make_candidate(cache_dir, fresh, candidate)
        after = inventory(candidate)
        report["changed_files"] = sorted(
            name
            for name in before.keys() | after.keys()
            if before.get(name) != after.get(name)
        )
        changes = report["changes"]
        if changes["incomplete_enums"]:
            report["failures"].append(
                {
                    "reason": "Fresh enum closures are incomplete",
                    "files": changes["incomplete_enums"],
                }
            )
        if changes["enum_memberships_removed"] > max_enum_removals:
            report["failures"].append(
                {
                    "reason": "Enum membership removals exceed explicit budget",
                    "removed": changes["enum_memberships_removed"],
                    "allowed": max_enum_removals,
                }
            )
        if time.monotonic() >= started + max_runtime and not any(
            "runtime budget" in f["reason"] for f in report["failures"]
        ):
            report["failures"].append(
                {"reason": "runtime budget exhausted before application"}
            )
        report["ready"] = eligible and not report["failures"]
        checkpoint()
        if report["ready"] and apply:
            stage = "apply"
            apply_candidate(candidate, cache_dir, before)
            report["applied"] = True
        report["status"] = "finished"
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        report["ready"] = False
        report["status"] = "failed"
        report["failures"].append(
            {"phase": stage, "reason": f"{type(exc).__name__}: {exc}"}
        )
    finally:
        if report["status"] == "running":
            report["ready"] = False
            report["status"] = "interrupted"
            report["failures"].append(
                {
                    "phase": stage,
                    "reason": "Refresh interrupted; inspect checkpoints and any .ontology-cache-swap-* recovery directory",
                }
            )
        report["provenance"]["finished_utc"] = datetime.now(timezone.utc).isoformat()
        checkpoint()
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
    parser.add_argument(
        "--max-runtime",
        type=float,
        default=18000,
        help="Total runtime budget in seconds, including retries",
    )
    parser.add_argument(
        "--max-enum-removals",
        type=int,
        default=0,
        help="Explicit maximum number of removed enum memberships",
    )
    args = parser.parse_args(argv)
    root = coverage.PROJECT_ROOT
    report = refresh(
        coverage.expand_inputs([root / p for p in args.inputs]),
        root=coverage.PROJECT_ROOT,
        cache_dir=root / args.cache_dir,
        output_dir=root / args.output_dir,
        oak_config=root / args.oak_config,
        apply=args.apply,
        attempts=args.attempts,
        timeout=args.timeout,
        max_runtime=args.max_runtime,
        max_enum_removals=args.max_enum_removals,
    )
    return 0 if report["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
