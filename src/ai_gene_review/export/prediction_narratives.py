"""Export narrative prediction sets while keeping their assessment units distinct.

BioReason's one-paragraph functional summaries have independent correctness and
completeness scores. ProtNLM narrative categories describe presence of judgments
within a reviewed record. Neither is a list of atomic GO/EC prediction claims.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
from textwrap import dedent
from typing import Any
from urllib.parse import quote, unquote, urlsplit

import yaml


NARRATIVE_CATEGORIES = {"COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP", "SUPPORTED"}
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def _read_yaml(path: Path) -> dict[str, Any]:
    """Read an optional mapping without importing arbitrary YAML objects."""
    if not path.is_file():
        return {}
    data = yaml.load(path.read_text(), Loader=YAML_LOADER)
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML mapping: {path}")
    return data


def _read_csv(path: Path) -> list[dict[str, str]]:
    """Read an optional benchmark table."""
    if not path.is_file():
        return []
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def _link(path: Path | None, output_dir: Path) -> str:
    """Link only established files relative to the exported browser directory."""
    if path is None or not path.is_file():
        return ""
    return quote(Path(os.path.relpath(path, output_dir)).as_posix(), safe="/")


def _section(text: str, heading: str) -> str:
    """Extract a named Markdown section, tolerating indented SFT exports."""
    match = re.search(
        rf"^[ \t]*#{{1,6}}[ \t]+{re.escape(heading)}[ \t]*\n(.*?)(?=^[ \t]*#{{1,6}}[ \t]+|\Z)",
        text,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return match.group(1).strip() if match else ""


def _plain_excerpt(text: str, limit: int = 900) -> str:
    """Make a short searchable excerpt; full review text remains at its source link."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^[ \t]*[#>]+[ \t]*", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*`]", "", text)
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _prediction_summary(raw_text: str, review_text: str) -> str:
    """Extract model text without substituting its review or a reasoning trace."""
    summary = _section(raw_text, "Functional Summary")
    if not summary:
        # ProtNLM reviews quote the original paragraph; keep the first contiguous
        # quote rather than treating later evidence quotations as model output.
        match = re.search(r"(?:^[ \t]*>[^\n]*(?:\n|$))+", review_text, re.MULTILINE)
        summary = match.group(0) if match else ""
    return _plain_excerpt(summary)


def _review_prose(text: str) -> str:
    """Remove model quotations and source boilerplate from an assessment excerpt."""
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    lines = []
    table_columns: list[tuple[int, str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith((">", "#", "Source:", "Target:", "Original prediction")):
            continue
        if re.match(
            r"(?i)^(?:the )?(?:bioreason|model|functional summary|prediction).*\b(?:states|says|reads|follows|predicts)\s*:\s*$",
            stripped,
        ):
            continue
        if stripped.startswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(re.fullmatch(r"[-: ]+", cell) for cell in cells):
                continue
            if not table_columns:
                table_columns = [
                    (index, label)
                    for index, label in enumerate(cells)
                    if re.search(
                        r"(?i)assessment|decision|rationale|evidence|reason", label
                    )
                ]
                continue
            lines.append(
                "; ".join(
                    f"{label}: {cells[index]}"
                    for index, label in table_columns
                    if index < len(cells)
                )
            )
        else:
            table_columns = []
            lines.append(line)
    return _plain_excerpt("\n".join(lines))


def _review_summary(text: str) -> str:
    """Export the reviewer's assessment separately from the model's functional claims."""
    if not text:
        return "No review recorded."
    headings = re.findall(r"^[ \t]*#{1,6}[ \t]+(.+?)[ \t]*$", text, re.MULTILINE)
    preferred = [
        "Functional Summary Review",
        "Assessment",
        "Claim-level assessment",
        "Claim assessment",
        "Claim assessments",
        "Atomic assessment",
        "Atomic assessments",
        "Atomic claim assessments",
        "Atomic claims",
        "Claim-level decisions",
        "Claim and evidence",
        "Claims and evidence",
        "Original prediction and assessment",
    ]
    for heading in preferred + [
        h for h in headings if h.lower().startswith("assessment:")
    ]:
        section = _section(text, heading)
        if section and (summary := _review_prose(section)):
            return summary
    introduction = re.split(r"^[ \t]*##[ \t]+", text, maxsplit=1, flags=re.MULTILINE)[0]
    return (
        _review_prose(introduction)
        or _review_prose(text)
        or "Review text available at source."
    )


def _frontmatter(text: str) -> dict[str, Any]:
    """Read source metadata from an indented or unindented SFT raw export."""
    match = re.match(r"\s*---[ \t]*\n(.*?)\n[ \t]*---(?:\n|$)", text, re.DOTALL)
    if not match:
        return {}
    data = yaml.load(dedent(match.group(1)), Loader=YAML_LOADER)
    return data if isinstance(data, dict) else {}


def _scores(text: str) -> dict[str, int]:
    """Read only explicit BioReason correctness/completeness scores on the 1–5 scale."""
    scores = {}
    for field in ("correctness", "completeness"):
        match = re.search(
            rf"\*\*{field}\*\*:[ \t]*(\d+)[ \t]*/[ \t]*5\b", text, re.IGNORECASE
        )
        if match and 1 <= int(match.group(1)) <= 5:
            scores[field] = int(match.group(1))
    return scores


def _protnlm_raw(root: Path, review: Path, text: str) -> Path | None:
    """Resolve actual local source artifacts already identified by a ProtNLM review."""
    gene = review.parent.name
    candidates = [
        review.parent / f"{gene}-protnlm-source.json",
        review.parent / f"{gene}-protnlm-source.xml",
        review.parent / f"{gene}-predictions-source.json",
    ]
    for target in re.findall(r"\]\(([^)]+)\)", text):
        parsed = urlsplit(target)
        if not parsed.scheme and not parsed.netloc:
            candidates.append((review.parent / unquote(parsed.path)).resolve())
    for target in re.findall(r"`([^`\n]+)`", text):
        if target.startswith("projects/"):
            candidates.append(root / target)
    for path in candidates:
        if (
            path.is_file()
            and path.resolve().is_relative_to(root)
            and path.name.endswith((".json", ".xml", ".jsonl.gz", ".csv"))
            and any(
                word in path.name.lower()
                for word in ("protnlm", "prediction", "source")
            )
        ):
            return path
    return None


def _protnlm_version(review: Path, text: str) -> str:
    """Preserve existing source version or an explicitly named XML/API snapshot."""
    sidecar = _read_yaml(
        review.with_name(f"{review.parent.name}-protnlm-predictions-review.yaml")
    )
    versions = sorted(
        {
            str(p["source_version"])
            for p in sidecar.get("predictions", [])
            if p.get("source_version")
        }
    )
    if versions:
        return "; ".join(versions)
    xml = re.search(r"post-processed-[\w_]+\.xml", text)
    if xml:
        return xml.group(0)
    snapshot = re.search(r"(?:snapshot|retrieved|dated)[ \t]*(\d{4}-\d{2}-\d{2})", text)
    return f"API snapshot {snapshot.group(1)}" if snapshot else "Not recorded"


def _benchmark_raw(
    root: Path, members: list[dict[str, str]], cache: dict[Path, set[str]]
) -> Path | None:
    """Resolve a manifest-declared snapshot only after finding the exact target in it."""
    for member in members:
        if not member.get("cohort_source"):
            continue
        cohort_source = root / member["cohort_source"]
        manifest = cohort_source.with_name(cohort_source.stem + "-manifest.json")
        if not manifest.is_file():
            continue
        snapshot_name = json.loads(manifest.read_text()).get("prediction_snapshot")
        if not snapshot_name:
            continue
        snapshot = (manifest.parent / snapshot_name).resolve()
        if (
            not snapshot.is_file()
            or not snapshot.is_relative_to(root)
            or not snapshot.name.endswith(".jsonl.gz")
        ):
            continue
        if snapshot not in cache:
            with gzip.open(snapshot, "rt") as stream:
                cache[snapshot] = {
                    record["primaryAccession"]
                    for line in stream
                    if (record := json.loads(line)).get("primaryAccession")
                }
        if member["accession"] in cache[snapshot]:
            return snapshot
    return None


def _identity(
    row: dict[str, Any], reference: dict[str, Any], target_ids: set[str]
) -> None:
    """Preserve exact benchmark targets and flag disagreements with curated references."""
    reference_id = str(reference.get("id") or "")
    if len(target_ids) > 1:
        row["protein_id"] = ""
        row["identity_status"] = "Conflicting targets"
        row["quality_notes"].append(
            "Conflicting benchmark accessions: " + ", ".join(sorted(target_ids))
        )
    else:
        row["protein_id"] = next(iter(target_ids), reference_id)
        row["identity_status"] = "Recorded" if row["protein_id"] else "Unresolved"
    row["reference_protein_id"] = reference_id
    if reference_id and row["protein_id"] and reference_id != row["protein_id"]:
        row["identity_status"] = "Target differs from reference"
        row["quality_notes"].append(
            f"Prediction target {row['protein_id']} differs from curated reference {reference_id}; exact target retained."
        )
    if not row["protein_id"]:
        row["quality_notes"].append("Exact target accession is not established.")


def _apply_quality(
    row: dict[str, Any], quality: dict[str, str], paths: dict[str, Path | None]
) -> None:
    """Expose recorded quality with hash freshness, without silently re-certifying it."""
    checked = False
    stale = row["metadata_status"] == "Stale"
    for field, path in paths.items():
        expected = quality.get(field)
        if not expected:
            continue
        checked = True
        actual = (
            hashlib.sha256(path.read_bytes()).hexdigest()
            if path and path.is_file()
            else None
        )
        if actual != expected:
            stale = True
            row["quality_notes"].append(
                f"Stale benchmark quality: {field} does not match the current file."
            )
    for field in (
        "input_quality",
        "exclusion_reason",
        "model_version",
        "export_timestamp",
    ):
        if quality.get(field):
            row[field] = quality[field]
    for field in ("input_sequence_length", "reference_sequence_length"):
        if quality.get(field):
            row[field] = int(quality[field])
    if quality.get("performance_included") in ("true", "false"):
        row["performance_included"] = quality["performance_included"] == "true"
    input_id = quality.get("cached_uniprot_id", "")
    if input_id:
        row["input_protein_id"] = input_id
    if quality.get("input_quality") == "WRONG_INPUT_SEQUENCE" or (
        input_id and row["protein_id"] and input_id != row["protein_id"]
    ):
        row["identity_status"] = "Input mismatch"
        row["quality_notes"].append(
            f"Recorded input accession {input_id or 'unknown'} does not represent target {row['protein_id'] or 'unknown'}; inspect the input-quality exclusion."
        )
    row["metadata_status"] = (
        "Stale" if stale else "Hashes match" if checked else "Not checked"
    )
    row["performance_metadata_current"] = checked and not stale


def collect_narrative_sets(root: Path, output_dir: Path) -> list[dict[str, Any]]:
    """Collect canonical BioReason/ProtNLM narrative sets, including unreviewed RL output.

    Only ``genes/<species>/<gene>/`` is scanned: copied experiment reviews under
    projects do not become additional observations. Raw-only RL records retain a
    stable set identifier when a review is subsequently added. Metadata conflicts
    remain visible in ``quality_notes`` rather than changing the underlying reviews.
    """
    root, output_dir = root.resolve(), output_dir.resolve()
    bio_base = root / "projects/BIOREASON_COMPARISON"
    benchmark = _read_csv(bio_base / "benchmark-genes.csv")
    quality_rows = _read_csv(bio_base / "benchmark-quality.csv")
    quality_by_gene = {(r["organism"], r["gene"]): r for r in quality_rows}
    prot_base = root / "projects/PROTNLM_EVALUATION"
    scope = _read_csv(prot_base / "family-curation/scope.csv")
    registry = _read_yaml(prot_base / "narrative-review-index.yaml")
    indexed = {r["review_file"]: r for r in registry.get("reviews", [])}

    sources: dict[Path, tuple[str, Path | None, Path | None]] = {}
    for raw_source in (root / "genes").glob("*/*/*-bioreason-rl-predictions.md"):
        review_source = raw_source.with_name(
            raw_source.name.replace("-predictions.md", "-review.md")
        )
        sources[raw_source] = (
            "RL",
            raw_source,
            review_source if review_source.is_file() else None,
        )
    for raw_source in (root / "genes").glob("*/*/*-deep-research-bioreason-sft.md"):
        if _section(raw_source.read_text(), "Functional Summary"):
            review_source = raw_source.with_name(
                f"{raw_source.parent.name}-bioreason-sft-review.md"
            )
            sources[raw_source] = (
                "SFT",
                raw_source,
                review_source if review_source.is_file() else None,
            )
    for variant in ("rl", "sft"):
        for review_source in (root / "genes").glob(
            f"*/*/*-bioreason-{variant}-review.md"
        ):
            gene = review_source.parent.name
            raw_source = review_source.with_name(
                f"{gene}-bioreason-rl-predictions.md"
                if variant == "rl"
                else f"{gene}-deep-research-bioreason-sft.md"
            )
            sources[raw_source] = (
                variant.upper(),
                raw_source if raw_source.is_file() else None,
                review_source,
            )
    for review_source in (root / "genes").glob("*/*/*-protnlm-function-review.md"):
        sources[review_source] = (
            "ProtNLM",
            _protnlm_raw(root, review_source, review_source.read_text()),
            review_source,
        )

    rows = []
    snapshot_accessions: dict[Path, set[str]] = {}
    for identity_path, (variant, raw, review) in sorted(sources.items()):
        species, gene = identity_path.parts[-3:-1]
        source = review or raw
        assert source is not None
        source_file = source.relative_to(root).as_posix()
        raw_text = raw.read_text() if raw and raw.suffix == ".md" else ""
        review_text = review.read_text() if review else ""
        reference_path = identity_path.parent / f"{gene}-ai-review.yaml"
        reference = _read_yaml(reference_path)
        prediction_summary = _prediction_summary(raw_text, review_text)
        row: dict[str, Any] = {
            "set_id": "narrative:" + identity_path.relative_to(root).as_posix(),
            "gene_symbol": gene,
            "species": species,
            "taxon_label": str((reference.get("taxon") or {}).get("label") or species),
            "projects": [
                "PROTNLM_EVALUATION" if variant == "ProtNLM" else "BIOREASON_COMPARISON"
            ],
            "cohorts": [],
            "output_type": "Functional summary",
            "output_state": "Predictions emitted"
            if prediction_summary
            else "Not recorded",
            "review_state": "Unreviewed",
            "document_status": "",
            "claim_count": None,
            "representation": "Narrative",
            "assessment_categories": [],
            "summary": _review_summary(review_text),
            "prediction_summary": prediction_summary,
            "source_file": source_file,
            "source_link": _link(source, output_dir),
            "review_link": _link(reference_path.with_suffix(".html"), output_dir),
            "raw_link": _link(raw, output_dir),
            "claims_link": "",
            "quality_notes": [],
            "metadata_status": "Not checked",
            "default_visible": True,
            "superseded_by": "",
        }
        if variant == "ProtNLM":
            assert review is not None
            members = [
                r
                for r in scope
                if r["role"] == "prediction_target"
                and r["species"] == species
                and r["gene_symbol"] == gene
            ]
            if raw is None:
                raw = _benchmark_raw(root, members, snapshot_accessions)
                row["raw_link"] = _link(raw, output_dir)
            _identity(row, reference, {r["accession"] for r in members})
            row.update(
                source_method="ProtNLM2",
                source_version=_protnlm_version(review, review_text),
                cohorts=sorted({r["cohort"] for r in members}),
                assessment_scheme="Narrative category presence",
            )
            entry = indexed.get(source_file)
            if (
                entry
                and entry.get("review_sha256")
                == hashlib.sha256(review.read_bytes()).hexdigest()
            ):
                categories = entry["categories"]
                if (
                    not categories
                    or not set(categories) <= NARRATIVE_CATEGORIES
                    or len(categories) != len(set(categories))
                ):
                    raise ValueError(f"Invalid narrative category index: {source_file}")
                row.update(
                    assessment_categories=categories,
                    review_state="Reviewed",
                    document_status="COMPLETE",
                    metadata_status="Hashes match",
                )
            elif entry:
                row.update(
                    review_state="Index stale",
                    document_status="DRAFT",
                    metadata_status="Stale",
                )
                row["quality_notes"].append(
                    "Narrative category index hash does not match the current review; indexed categories withheld."
                )
            else:
                row.update(review_state="Awaiting review", document_status="DRAFT")
                row["quality_notes"].append(
                    "Narrative review exists but has no checked category-index entry."
                )
        else:
            benchmark_source = (
                identity_path.with_name(f"{gene}-bioreason-{variant.lower()}-review.md")
                .relative_to(root)
                .as_posix()
            )
            matches = [r for r in benchmark if r.get("source_file") == benchmark_source]
            quality = (
                quality_by_gene.get((species, gene), {}) if variant == "RL" else {}
            )
            target_ids = {r["uniprot_id"] for r in matches if r.get("uniprot_id")}
            if quality.get("expected_uniprot_id"):
                target_ids.add(quality["expected_uniprot_id"])
            metadata = _frontmatter(raw_text)
            if metadata.get("uniprot_id"):
                target_ids.add(str(metadata["uniprot_id"]))
            _identity(row, reference, target_ids)
            versions = sorted(
                {r["source_version"] for r in matches if r.get("source_version")}
            )
            row.update(
                source_method=f"BioReason-Pro-{variant}",
                source_version="; ".join(versions)
                or str(
                    metadata.get("source") or "Web export; model version unavailable"
                ),
                cohorts=sorted({r["benchmark"] for r in matches if r.get("benchmark")}),
                assessment_scheme="Correctness/completeness (1–5)",
            )
            if review:
                scores = _scores(review_text)
                row.update(scores)
                complete = len(scores) == 2
                row.update(
                    review_state="Reviewed" if complete else "Awaiting review",
                    document_status="COMPLETE" if complete else "DRAFT",
                )
                if not complete:
                    row["quality_notes"].append(
                        "Both narrative scores must be explicitly recorded on the 1–5 scale."
                    )
                for field, value in scores.items():
                    for record in matches:
                        if record.get(field) and record[field] != str(value):
                            row["metadata_status"] = "Stale"
                            row["quality_notes"].append(
                                f"Stale benchmark score: {field}={record[field]}; current review records {value}."
                            )
            _apply_quality(
                row,
                quality,
                {
                    "review_sha256": review,
                    "prediction_sha256": raw,
                    "reference_sha256": reference_path,
                    "uniprot_sha256": identity_path.parent / f"{gene}-uniprot.txt",
                    "current_goa_sha256": identity_path.parent / f"{gene}-goa.tsv",
                },
            )
        rows.append(row)
    return rows
