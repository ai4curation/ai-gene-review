"""Extract de-leaked GOA annotation cases for accept-state (`ActionEnum`) benchmarks.

In `ai-gene-review`, each entry in `existing_annotations` pairs a machine-fetched
GOA row (`term`, `qualifier`, `extensions`, `negated`, `evidence_type`,
`original_reference_id`, `retired`, `isoform`, `supporting_entities`) with a
curator-authored `review` (`action`, `summary`, `reason`,
`proposed_replacement_terms`, `supported_by`, `propagation_review`,
`consistency_exception`).

To benchmark an agent or classifier on predicting `review.action` (and related
accept-state facets) without data leakage, `extract_annotation_case` strips:
- Every `review` object on `target_annotation` and all `sibling_annotations`
- Any `existing_annotations` row where `review.action == "NEW"` (since `NEW`
  rows were proposed by the reviewer and did not exist in the input GOA file)
- Top-level curator syntheses: `description`, `core_functions`,
  `proposed_new_terms`, `suggested_questions`, `suggested_experiments`,
  `knowledge_gaps`, `status`, and `functional_isoforms`
- Reviewer-authored fields on `references[]`: `findings` and `reference_review`
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

from ai_gene_review.classifier.claims import (
    _encode_pointer,
    parse_pointer,
    resolve_pointer,
)
from ai_gene_review.classifier.rubric import COARSE_ACTION_MAP, coarse_action

GOA_ROW_FIELDS = (
    "term",
    "qualifier",
    "extensions",
    "negated",
    "evidence_type",
    "original_reference_id",
    "retired",
    "isoform",
    "supporting_entities",
)


def _strip_goa_row(row: Mapping[str, Any]) -> dict[str, Any]:
    """Return only the machine-fetched GOA fields of an ExistingAnnotation row."""
    cleaned: dict[str, Any] = {}
    for field in GOA_ROW_FIELDS:
        if row.get(field) is not None:
            cleaned[field] = deepcopy(row[field])
    return cleaned


PRIMARY_REFERENCE_PREFIXES = (
    "PMID:",
    "GO_REF:",
    "Reactome:",
    "DOI:",
    "PMC:",
)


def _is_primary_source_ref(ref_id: str) -> bool:
    """Return True if ref_id is a primary literature/database source (not an internal agent report)."""
    if any(ref_id.startswith(prefix) for prefix in PRIMARY_REFERENCE_PREFIXES):
        return True
    if ref_id.startswith("file:") and ref_id.endswith("-uniprot.txt"):
        return True
    return False


def _extract_supporting_excerpts(review: Mapping[str, Any]) -> list[dict[str, str]]:
    """Extract non-leaky verbatim supporting text quotes from primary sources in review.supported_by."""
    excerpts: list[dict[str, str]] = []
    supported_by = review.get("supported_by")
    if not isinstance(supported_by, list):
        return excerpts
    for item in supported_by:
        if not isinstance(item, Mapping):
            continue
        ref_id = item.get("reference_id")
        snippet = item.get("supporting_text")
        if (
            isinstance(ref_id, str)
            and _is_primary_source_ref(ref_id)
            and isinstance(snippet, str)
            and snippet.strip()
        ):
            entry: dict[str, str] = {
                "reference_id": ref_id,
                "supporting_text": snippet.strip(),
            }
            if (
                isinstance(item.get("supporting_text_fulltext"), str)
                and item["supporting_text_fulltext"].strip()
            ):
                entry["supporting_text_fulltext"] = item[
                    "supporting_text_fulltext"
                ].strip()
            excerpts.append(entry)
    return excerpts


def _collapse_sibling_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Deduplicate sibling GOA rows by (term.id, qualifier, negated) for compact context."""
    grouped: dict[tuple[str, str, str, bool], dict[str, Any]] = {}
    for row in rows:
        term = row.get("term") or {}
        term_id = str(term.get("id") or "")
        term_label = str(term.get("label") or "")
        qualifier = str(row.get("qualifier") or "")
        negated = bool(row.get("negated", False))
        key = (term_id, term_label, qualifier, negated)
        ev = row.get("evidence_type")
        if key not in grouped:
            entry: dict[str, Any] = {
                "term": {"id": term_id, "label": term_label},
            }
            if qualifier:
                entry["qualifier"] = qualifier
            if negated:
                entry["negated"] = True
            entry["evidence_types"] = [ev] if ev else []
            entry["count"] = 1
            grouped[key] = entry
        else:
            grouped[key]["count"] += 1
            if ev and ev not in grouped[key]["evidence_types"]:
                grouped[key]["evidence_types"].append(ev)
    return list(grouped.values())


def _strip_reference_metadata(ref: Mapping[str, Any]) -> dict[str, Any]:
    """Return only non-leaky publication metadata for a reference entry."""
    cleaned: dict[str, Any] = {}
    for field in (
        "id",
        "title",
        "is_invalid",
        "publication_type",
        "full_text_unavailable",
    ):
        if ref.get(field) is not None:
            cleaned[field] = deepcopy(ref[field])
    return cleaned


def extract_annotation_case(
    document: Mapping[str, Any],
    annotation_path: str,
    *,
    include_sibling_annotations: bool = True,
    collapse_siblings: bool = True,
    include_supporting_excerpts: bool = True,
    include_references_metadata: bool = True,
    relevant_references_only: bool = True,
    allow_generic_protein_binding: bool = False,
) -> dict[str, Any]:
    """Build a de-leaked structured annotation case for an `existing_annotations` row.

    Parameters
    ----------
    document:
        Parsed `GeneReview` YAML mapping.
    annotation_path:
        RFC 6901 JSON Pointer to the target annotation, e.g.
        ``/existing_annotations/2``.
    include_sibling_annotations:
        Whether to include the other pre-existing GOA rows for the same gene
        (with their `review` blocks stripped and `NEW` rows excluded). Enabled
        by default because GO curation rules (`TOO_GENERAL`, `SAME_TERM`
        consistency) depend on the gene's other GOA rows.
    collapse_siblings:
        When True (default), deduplicate sibling GOA rows by `(term, qualifier)`
        into compact summary entries (`evidence_types`, `count`) so genes with
        many GOA annotations do not bloat the classifier context window.
    include_supporting_excerpts:
        When True (default), preserve verbatim `supporting_text` quotes from
        primary sources (`PMID:`, `GO_REF:`, `*-uniprot.txt`) in
        `supporting_excerpts` while excluding curator rationale/action and
        internal agent synthesis files.
    include_references_metadata:
        Whether to include non-leaky reference titles/types from `references[]`.
    relevant_references_only:
        When True (default), restrict `references_metadata` to references cited
        by `target_annotation` or `supporting_excerpts`.
    allow_generic_protein_binding:
        When False (default), reject target annotations on bare ``GO:0005515``
        (`protein binding`) and omit ``GO:0005515`` from sibling summaries, as
        ``GO:0005515`` is governed by a mechanical policy rule rather than
        substantive biological reasoning.
    """
    tokens = parse_pointer(annotation_path)
    if len(tokens) != 2 or tokens[0] != "existing_annotations":
        raise ValueError(
            f"annotation_path must be '/existing_annotations/<i>', got {annotation_path!r}"
        )
    steps = resolve_pointer(document, tokens)
    target_index = int(tokens[1])
    raw_target = steps[-1][1]
    if not isinstance(raw_target, Mapping):
        raise ValueError(f"Target at {annotation_path!r} is not a mapping")

    review = raw_target.get("review") or {}
    if isinstance(review, Mapping) and review.get("action") == "NEW":
        raise ValueError(
            f"Annotation at {annotation_path!r} has action='NEW' (curator-proposed, not an existing GOA row)"
        )
    target_term = raw_target.get("term") or {}
    if (
        not allow_generic_protein_binding
        and isinstance(target_term, Mapping)
        and target_term.get("id") == "GO:0005515"
    ):
        raise ValueError(
            f"Annotation at {annotation_path!r} uses generic GO:0005515 protein binding, "
            "which is governed by a deterministic policy and is not an informative benchmark target"
        )

    gene_info: dict[str, Any] = {
        "id": deepcopy(document.get("id")),
        "gene_symbol": deepcopy(document.get("gene_symbol")),
        "product_type": deepcopy(document.get("product_type", "PROTEIN")),
        "taxon": deepcopy(document.get("taxon")),
    }
    if document.get("aliases"):
        gene_info["aliases"] = deepcopy(document["aliases"])
    if document.get("alternative_products"):
        # Include only UniProt isoform IDs, names, and sequence notes; strip agent descriptions
        isoforms = []
        for alt in document["alternative_products"]:
            if isinstance(alt, Mapping) and alt.get("id"):
                entry: dict[str, Any] = {"id": deepcopy(alt["id"])}
                if alt.get("name"):
                    entry["name"] = deepcopy(alt["name"])
                if alt.get("sequence_note"):
                    entry["sequence_note"] = deepcopy(alt["sequence_note"])
                isoforms.append(entry)
        if isoforms:
            gene_info["alternative_products"] = isoforms

    target_annotation = _strip_goa_row(raw_target)
    supporting_excerpts = (
        _extract_supporting_excerpts(review)
        if include_supporting_excerpts and isinstance(review, Mapping)
        else []
    )

    raw_siblings: list[dict[str, Any]] = []
    if include_sibling_annotations:
        all_rows = document.get("existing_annotations") or []
        for idx, row in enumerate(all_rows):
            if idx == target_index or not isinstance(row, Mapping):
                continue
            row_review = row.get("review") or {}
            if isinstance(row_review, Mapping) and row_review.get("action") == "NEW":
                continue
            row_term = row.get("term") or {}
            if (
                not allow_generic_protein_binding
                and isinstance(row_term, Mapping)
                and row_term.get("id") == "GO:0005515"
            ):
                continue
            sibling_entry = _strip_goa_row(row)
            sibling_entry["annotation_path"] = _encode_pointer(
                ["existing_annotations", str(idx)]
            )
            raw_siblings.append(sibling_entry)

    sibling_annotations = (
        _collapse_sibling_rows(raw_siblings) if collapse_siblings else raw_siblings
    )

    result: dict[str, Any] = {
        "about": {"gene": gene_info},
        "origin": {
            "annotation_path": annotation_path,
            "index": target_index,
        },
        "target_annotation": target_annotation,
    }
    if supporting_excerpts:
        result["supporting_excerpts"] = supporting_excerpts
    if include_sibling_annotations:
        result["sibling_annotations"] = sibling_annotations
        result["sibling_raw_count"] = len(raw_siblings)
    if include_references_metadata and isinstance(document.get("references"), list):
        relevant_ids: set[str] = set()
        if target_annotation.get("original_reference_id"):
            relevant_ids.add(str(target_annotation["original_reference_id"]))
        for exc in supporting_excerpts:
            relevant_ids.add(exc["reference_id"])
        refs_meta = [
            _strip_reference_metadata(r)
            for r in document["references"]
            if isinstance(r, Mapping)
            and r.get("id")
            and _is_primary_source_ref(str(r["id"]))
            and (not relevant_references_only or str(r["id"]) in relevant_ids)
        ]
        if refs_meta:
            result["references_metadata"] = refs_meta
    return result


def derive_annotation_review_target(
    document: Mapping[str, Any],
    annotation_path: str,
) -> dict[str, Any]:
    """Extract the curator's ground-truth review metadata from an `existing_annotations` row.

    Used during benchmark case ingestion to populate initial review records and
    aspect judgments. Never included in the model's `annotation_case` input.
    """
    tokens = parse_pointer(annotation_path)
    steps = resolve_pointer(document, tokens)
    raw_target = steps[-1][1]
    if not isinstance(raw_target, Mapping):
        raise ValueError(f"Target at {annotation_path!r} is not a mapping")
    review = raw_target.get("review")
    if not isinstance(review, Mapping) or not review.get("action"):
        raise ValueError(
            f"Annotation at {annotation_path!r} does not have a completed review.action"
        )
    action = str(review["action"])
    if action not in COARSE_ACTION_MAP:
        raise ValueError(
            f"Annotation at {annotation_path!r} has action={action!r}, which is not an existing-annotation accept state"
        )

    out: dict[str, Any] = {
        "action": action,
        "coarse_action": coarse_action(action),
        "is_core": (
            "CORE"
            if action == "ACCEPT"
            else (
                "NON_CORE"
                if action in ("KEEP_AS_NON_CORE", "TOO_GENERAL")
                else "NOT_APPLICABLE"
            )
        ),
    }
    if review.get("summary"):
        out["summary"] = str(review["summary"])
    if review.get("reason"):
        out["reason"] = str(review["reason"])
    if review.get("proposed_replacement_terms"):
        out["proposed_replacement_terms"] = deepcopy(
            review["proposed_replacement_terms"]
        )
    if review.get("supported_by"):
        out["supported_by"] = deepcopy(review["supported_by"])
    prop = review.get("propagation_review")
    if isinstance(prop, Mapping):
        if prop.get("root_cause"):
            out["propagation_root_cause"] = str(prop["root_cause"])
        if prop.get("failure_modes"):
            out["propagation_failure_modes"] = list(prop["failure_modes"])
    return out
