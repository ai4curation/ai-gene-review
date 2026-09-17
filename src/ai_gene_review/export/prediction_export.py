"""Export canonical prediction reviews without conflating output and review states.

A prediction set is one document/method/version combination. Empty lists remain
sets, and absent lists remain unknown output. Source categories and review scores
are preserved; a review score is never treated as a model probability.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import csv
import hashlib
import os
from pathlib import Path
import re
from typing import Any
from urllib.parse import quote, urlencode

import yaml

from ai_gene_review.export.prediction_narratives import collect_narrative_sets

ASSESSMENT_SCORES = {
    "COR": 2,
    "CNN": 2,
    "LSP": 2,
    "UNC": 1,
    "PLI": 0,
    "NPI": 0,
    "REP": 0,
}
PREDICTION_FILENAME = re.compile(r"(?:^|-)predictions(?:-|\.)")
PENDING_RATIONALE = re.compile(
    r"\b(?:requires?|awaiting|needs?|pending) (?:a )?(?:manual |expert )?(?:assessment|review)\b|\bnot yet (?:reviewed|assessed)\b",
    re.I,
)
AUTOMATIC_RATIONALE = re.compile(
    r"^(?:Deterministic (?:exact-match )?comparison|Automatically (?:classified|compared|assigned)|Auto-compared)\b|^GO-GPT correctly predicted this term, which is already in the curated review\.",
    re.I,
)


def stable_set_id(source_file: str, method: str, version: str) -> str:
    """Identify a source set independently of checkout location and row ordering.

    >>> stable_set_id('genes/X/G/G-predictions.yaml', 'M', 'v') == stable_set_id('genes/X/G/G-predictions.yaml', 'M', 'v')
    True
    """
    identity = "\0".join((source_file, method, version))
    return "ps-" + hashlib.sha256(identity.encode()).hexdigest()[:20]


def source_link(path: Path, output_dir: Path) -> str:
    """Return an escaped relative link suitable for the deployed browser."""
    return quote(
        Path(os.path.relpath(path.resolve(), output_dir.resolve())).as_posix(), safe="/"
    )


def _text(value: object) -> str:
    """Preserve text-like metadata while giving absent values an empty string."""
    return "" if value is None else str(value)


def _filename_method(path: Path) -> str:
    """Infer only named source methods for documents with no prediction rows."""
    name = path.stem
    for suffix, method in (
        ("-protnlm-predictions-review", "ProtNLM2"),
        ("-sft-predictions", "BioReason-Pro-SFT"),
        ("-gogpt-leaf-predictions", "GO-GPT"),
        ("-gogpt-predictions", "GO-GPT"),
        ("-det-predictions-review", "DeepECTF"),
    ):
        if name.endswith(suffix):
            return method
    prefix = path.parent.name + "-"
    if name.startswith(prefix):
        method = re.sub(r"-predictions(?:-review)?$", "", name[len(prefix) :])
        if method and method != "predictions-review" and method != "predictions":
            return method
    return "Unknown method"


def _representation(path: Path) -> str:
    """Identify explicitly named leaf/full forms without assuming equal runs."""
    if path.name.endswith("-gogpt-leaf-predictions.yaml"):
        return "leaf"
    if path.name.endswith("-gogpt-predictions.yaml"):
        return "full"
    return "standard"


def _review_state(review: dict[str, Any]) -> str:
    """Separate explicit pending/automatic templates from substantive judgments."""
    summary = _text(review.get("summary")).strip()
    assessment = _text(review.get("assessment"))
    if assessment == "PENDING" or PENDING_RATIONALE.search(summary):
        return "Awaiting review"
    if AUTOMATIC_RATIONALE.search(summary):
        return "Automatic comparison"
    if assessment in ASSESSMENT_SCORES and summary:
        return "Reviewed"
    return "Unreviewed"


def _set_review_state(
    rows: list[dict[str, Any]], document: dict[str, Any], explicit_empty: bool
) -> str:
    """Aggregate actual row states; COMPLETE alone does not establish review."""
    states = {row["review_state"] for row in rows}
    if len(states) == 1:
        return next(iter(states))
    if states:
        return "Partially reviewed"
    description = _text(document.get("description")).strip()
    if PENDING_RATIONALE.search(description):
        return "Awaiting review"
    if AUTOMATIC_RATIONALE.search(description):
        return "Automatic comparison"
    if explicit_empty and description and document.get("status") == "COMPLETE":
        return "Reviewed"
    return "Unreviewed"


def _evidence_text(review: dict[str, Any]) -> str:
    """Join stored source identifiers and excerpts without manufacturing support."""
    return "\n\n".join(
        ": ".join(
            filter(
                None,
                (
                    _text(support.get("reference_id")),
                    _text(support.get("supporting_text")),
                ),
            )
        )
        for support in review.get("supported_by") or []
    )


def _resolve_source(value: str, path: Path, root: Path) -> Path | None:
    """Resolve existing repository sources, including gene-relative file CURIEs."""
    relative = value.removeprefix("file:")
    if "://" in relative or re.match(r"^(?:PMID|DOI|doi|GO_REF):", relative):
        return None
    for candidate in (
        root / relative,
        root / "genes" / relative,
        path.parent / relative,
    ):
        if candidate.is_file() and candidate.resolve().is_relative_to(root.resolve()):
            return candidate
    return None


def _raw_link(
    document: dict[str, Any],
    rows: list[dict[str, Any]],
    path: Path,
    root: Path,
    output_dir: Path,
) -> str:
    """Link only established raw prediction sources, never an unrelated gene paper."""
    sources = [_text(row.get("source_reference_id")) for row in rows]
    sources += [_text(source) for source in document.get("source_documents") or []]
    candidates: list[Path] = []
    for value in sources:
        resolved = _resolve_source(value, path, root)
        if resolved is None:
            continue
        name = resolved.name.lower()
        if ("prediction" in name or "protnlm" in name or "gogpt" in name) and not any(
            marker in name
            for marker in ("review", "notes", "manifest", "inventory", "result")
        ):
            candidates.append(resolved)
    # Prefer readable exact-gene snapshots to compressed cohort archives.
    candidates.sort(
        key=lambda candidate: (
            candidate.suffix == ".gz",
            candidate.parent != path.parent,
        )
    )
    return source_link(candidates[0], output_dir) if candidates else ""


def _scope_memberships(root: Path) -> dict[tuple[str, str, str], set[str]]:
    """Load exact target membership from the frozen ProtNLM scope registry."""
    path = root / "projects/PROTNLM_EVALUATION/family-curation/scope.csv"
    members: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    if path.is_file():
        with path.open() as stream:
            for row in csv.DictReader(stream):
                if row.get("role") == "prediction_target":
                    key = (row["species"], row["gene_symbol"], row["accession"])
                    members[key].add(row["cohort"])
    return members


def _bioreason_memberships(root: Path) -> list[dict[str, str]]:
    """Read the project's explicit benchmark registry when present."""
    path = root / "projects/BIOREASON_COMPARISON/benchmark-genes.csv"
    if not path.is_file():
        return []
    with path.open() as stream:
        return list(csv.DictReader(stream))


def _memberships(
    document: dict[str, Any],
    rows: list[dict[str, Any]],
    path: Path,
    method: str,
    version: str,
    scope: dict[tuple[str, str, str], set[str]],
    bioreason: list[dict[str, str]],
    root: Path,
) -> tuple[list[str], list[str], list[str]]:
    """Use declared project paths and exact accession membership, not gene names alone."""
    project_names: set[str] = set()
    sources = [_text(source) for source in document.get("source_documents") or []]
    sources += [_text(row.get("source_reference_id")) for row in rows]
    for value in sources:
        parts = Path(value.removeprefix("file:")).parts
        if "projects" in parts:
            index = parts.index("projects")
            if index + 1 < len(parts):
                project_names.add(Path(parts[index + 1]).stem)
    cohorts: set[str] = set()
    notes: list[str] = []
    if "protnlm" in method.lower():
        for gene in {path.parent.name, _text(document.get("gene_symbol"))}:
            key = (path.parent.parent.name, gene, _text(document.get("id")))
            cohorts.update(scope.get(key, set()))
        if cohorts:
            project_names.add("PROTNLM_EVALUATION")
        elif (root / "projects/PROTNLM_EVALUATION.md").is_file():
            project_names.add("PROTNLM_EVALUATION")
            notes.append(
                "ProtNLM project membership inferred from the named method; no exact frozen cohort membership was found."
            )
    if method in {"GO-GPT", "BioReason-Pro-SFT"}:
        matches = [
            row
            for row in bioreason
            if row.get("organism") == path.parent.parent.name
            and row.get("gene") in {path.parent.name, document.get("gene_symbol")}
            and row.get("uniprot_id") == document.get("id")
        ]
        if matches:
            project_names.add("BIOREASON_COMPARISON")
            for row in matches:
                if (
                    row.get("source_file") == path.relative_to(root).as_posix()
                    and row.get("source_version", "") == version
                ):
                    cohorts.add(row["benchmark"])
        elif (root / "projects/BIOREASON_COMPARISON.md").is_file():
            project_names.add("BIOREASON_COMPARISON")
            notes.append(
                "BioReason project membership inferred from the named method; no exact benchmark registry membership was found."
            )
    if method == "DeepECTF":
        matched_projects = []
        for name in ("BIOREASON_COMPARISON", "VALIDATING_ECOLI_PREDICTIONS"):
            page = root / "projects" / f"{name}.md"
            if page.is_file() and re.search(
                r"DeepECTF|DeepECTransformer", page.read_text()
            ):
                project_names.add(name)
                matched_projects.append(name)
        if matched_projects:
            notes.append(
                "Project association derived from the DeepECTF method explicitly described by the local project pages; no cohort membership inferred."
            )
    return sorted(project_names), sorted(cohorts), notes


def _quality_notes(review: dict[str, Any], prediction: dict[str, Any]) -> list[str]:
    """Flag source inconsistencies while leaving source assessments unchanged."""
    notes = []
    assessment = _text(review.get("assessment"))
    if (
        assessment in ASSESSMENT_SCORES
        and review.get("confidence_score") != ASSESSMENT_SCORES[assessment]
    ):
        notes.append(
            f"Stored review score {review.get('confidence_score')!r} disagrees with {assessment} (expected {ASSESSMENT_SCORES[assessment]})."
        )
    elif assessment and assessment not in ASSESSMENT_SCORES:
        notes.append(
            f"Stored assessment {assessment!r} is outside the VDCL categories."
        )
    term = prediction.get("predicted_term") or {}
    if not term.get("id"):
        notes.append("Predicted term identifier is not recorded.")
    if not term.get("label") or term.get("label") == "Unknown":
        notes.append("Predicted term label is missing or Unknown in the source.")
    return notes


def _output_type(predictions: list[dict[str, Any]]) -> str:
    """Keep GO, EC and mixed/unspecified output types distinct."""
    types = {_text(row.get("predicted_term_type")) for row in predictions}
    if types and all(value.startswith("GO_") for value in types):
        return "GO terms"
    if types == {"EC"}:
        return "EC numbers"
    return "GO/EC terms"


def _collect_yaml(
    root: Path, output_dir: Path
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Collect canonical gene-side prediction YAML files and their individual terms."""
    scope = _scope_memberships(root)
    bioreason = _bioreason_memberships(root)
    sets: list[dict[str, Any]] = []
    claims: list[dict[str, Any]] = []
    for path in sorted((root / "genes").glob("*/*/*.yaml")):
        if not PREDICTION_FILENAME.search(path.name):
            continue
        document = yaml.safe_load(path.read_text())
        if (
            not isinstance(document, dict)
            or not document.get("id")
            or not document.get("gene_symbol")
        ):
            continue
        predictions = document.get("predictions")
        if predictions is not None and not isinstance(predictions, list):
            raise ValueError(f"{path}: predictions must be a list or null")
        groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for prediction in predictions or []:
            if not isinstance(prediction, dict) or "predicted_term" not in prediction:
                raise ValueError(
                    f"{path}: prediction row lacks a predicted_term object"
                )
            method = _text(prediction.get("source_method")) or _filename_method(path)
            version = _text(prediction.get("source_version"))
            groups[(method, version)].append(prediction)
        if not groups:
            groups[(_filename_method(path), "")] = []
        for (method, version), group in sorted(groups.items()):
            relative = path.relative_to(root).as_posix()
            set_id = stable_set_id(relative, method, version)
            projects, cohorts, membership_notes = _memberships(
                document, group, path, method, version, scope, bioreason, root
            )
            review_path = path.parent / f"{path.parent.name}-ai-review.html"
            raw_link = _raw_link(document, group, path, root, output_dir)
            common_notes = list(membership_notes)
            if not review_path.is_file():
                common_notes.append("The local gene review HTML page is unavailable.")
            if not raw_link and document.get("source_documents"):
                declared_raw = [
                    _text(value)
                    for value in document["source_documents"]
                    if re.search(r"prediction|protnlm|gogpt", _text(value), re.I)
                    and not re.search(
                        r"review|notes|manifest|inventory|result",
                        Path(_text(value)).name,
                        re.I,
                    )
                ]
                if declared_raw:
                    common_notes.append(
                        "A declared raw prediction source is unavailable or cannot be resolved locally."
                    )
            common: dict[str, Any] = {
                "set_id": set_id,
                "gene_symbol": _text(document.get("gene_symbol")),
                "protein_id": _text(document.get("id")),
                "species": path.parent.parent.name,
                "taxon_label": _text((document.get("taxon") or {}).get("label")),
                "source_method": method,
                "source_version": version,
                "projects": projects,
                "cohorts": cohorts,
                "output_type": _output_type(group),
                "output_state": "Predictions emitted"
                if group
                else "No GO/EC predictions"
                if predictions == []
                else "Not recorded",
                "document_status": _text(document.get("status")),
                "claim_count": len(group) if predictions is not None else None,
                "representation": _representation(path),
                "assessment_scheme": "VDCL",
                "source_file": relative,
                "source_link": source_link(path, output_dir),
                "review_link": source_link(review_path, output_dir)
                if review_path.is_file()
                else "",
                "raw_link": raw_link,
                "claims_link": "?" + urlencode({"dataset": "claims", "set_id": set_id}),
                "default_visible": True,
                "superseded_by": "",
            }
            set_claims: list[dict[str, Any]] = []
            repeated: Counter[tuple[str, str]] = Counter()
            for prediction in group:
                term = prediction.get("predicted_term") or {}
                review = prediction.get("review") or {}
                term_id, term_type = (
                    _text(term.get("id")),
                    _text(prediction.get("predicted_term_type")),
                )
                identity = (term_id, term_type)
                repeated[identity] += 1
                claim_id = (
                    "pc-"
                    + hashlib.sha256(
                        "\0".join(
                            (set_id, term_id, term_type, str(repeated[identity]))
                        ).encode()
                    ).hexdigest()[:20]
                )
                row = dict(
                    common,
                    claim_id=claim_id,
                    term_id=term_id,
                    term_label=_text(term.get("label")),
                    term_type=term_type,
                    assessment=_text(review.get("assessment")),
                    review_score=review.get("confidence_score"),
                    error_type=_text(review.get("error_type")),
                    summary=_text(review.get("summary")),
                    evidence=_evidence_text(review),
                    review_state=_review_state(review),
                    quality_notes=common_notes + _quality_notes(review, prediction),
                    set_link="?" + urlencode({"dataset": "sets", "set_id": set_id}),
                )
                row["assessment_categories"] = (
                    [row["assessment"]] if row["assessment"] else []
                )
                row["output_type"] = _output_type([prediction])
                set_claims.append(row)
            categories = sorted(
                {row["assessment"] for row in set_claims if row["assessment"]}
            )
            set_row = dict(
                common,
                review_state=_set_review_state(set_claims, document, predictions == []),
                assessment_categories=categories,
                summary=_text(document.get("description")),
                quality_notes=sorted(
                    set(common_notes)
                    | {note for row in set_claims for note in row["quality_notes"]}
                ),
            )
            if "predictions" not in document or predictions is None:
                set_row["quality_notes"].append(
                    "The predictions list is not recorded; zero emitted predictions cannot be inferred."
                )
            sets.append(set_row)
            claims.extend(set_claims)
    return sets, claims


def _prefer_leaf(sets: list[dict[str, Any]], claims: list[dict[str, Any]]) -> None:
    """Mark a full view superseded only by a leaf view of the identical source run."""
    leaves = {
        (
            str(Path(row["source_file"]).parent),
            row["protein_id"],
            row["source_method"],
            row["source_version"],
        ): row["set_id"]
        for row in sets
        if row["representation"] == "leaf"
    }
    superseded: dict[str, str] = {}
    for row in sets:
        key = (
            str(Path(row["source_file"]).parent),
            row["protein_id"],
            row["source_method"],
            row["source_version"],
        )
        if row["representation"] == "full" and key in leaves:
            row["default_visible"] = False
            row["superseded_by"] = leaves[key]
            superseded[row["set_id"]] = leaves[key]
    for row in claims:
        if row["set_id"] in superseded:
            row["default_visible"] = False
            row["superseded_by"] = superseded[row["set_id"]]


def collect_prediction_data(root: Path, output_dir: Path) -> dict[str, Any]:
    """Collect separate set/claim datasets from canonical gene-side prediction files.

    Paths under project experiments are deliberately excluded. Leaf and full views
    remain in the payload; only an explicitly equal method/version pair shares a
    default representation. The export does not infer training membership.
    """
    root = root.resolve()
    sets, claims = _collect_yaml(root, output_dir)
    _prefer_leaf(sets, claims)
    yaml_set_count = len(sets)
    narratives = collect_narrative_sets(root, output_dir)
    sets.extend(narratives)
    return {
        "sets": sets,
        "claims": claims,
        "metadata": {
            "schema_version": 1,
            "set_count": len(sets),
            "claim_count": len(claims),
            "yaml_set_count": yaml_set_count,
            "narrative_set_count": len(narratives),
            "default_set_count": sum(row["default_visible"] for row in sets),
            "default_claim_count": sum(row["default_visible"] for row in claims),
            "source_file_count": len({row["source_file"] for row in sets}),
            "scope": "Canonical genes/ prediction documents; project experiment copies excluded.",
            "review_score_description": "Stored VDCL review score (0–2), not model confidence or probability.",
            "representation_policy": "Prefer leaf only over a full representation with the same gene, accession, method and version; retain all source variants.",
        },
    }
