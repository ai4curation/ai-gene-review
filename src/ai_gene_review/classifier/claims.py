"""Extract self-contained structured claims from AIGR YAML documents.

Supports extracting evidence-backed assertions via RFC 6901 JSON Pointer
(`evidence_path`) from:
- ``/core_functions/<i>/supported_by/<j>``
- ``/existing_annotations/<i>/review/supported_by/<j>``
- ``/references/<i>/findings/<j>``
- ``/proposed_new_terms/<i>/supported_by/<j>``
- ``**/knowledge_gaps/<i>/provenance/<j>``
- ``**/finding_review/supported_by/<j>``
- ``**/evidence/<j>`` (for ``ModuleReview`` documents)
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

EVIDENCE_CONTAINERS = frozenset({"supported_by", "provenance", "evidence"})
STRIP_ASSERTION_FIELDS = frozenset(
    {
        "supported_by",
        "provenance",
        "evidence",
        "additional_reference_ids",
        "knowledge_gaps",
    }
)


def _decode_token(token: str) -> str:
    return token.replace("~1", "/").replace("~0", "~")


def _encode_pointer(tokens: list[str]) -> str:
    if not tokens:
        return "/"
    return "/" + "/".join(
        token.replace("~", "~0").replace("/", "~1") for token in tokens
    )


def parse_pointer(pointer: str) -> list[str]:
    """Parse an RFC 6901 JSON Pointer into decoded path tokens."""
    if not pointer.startswith("/"):
        raise ValueError(f"JSON Pointer must start with '/': {pointer!r}")
    if pointer == "/":
        return []
    return [_decode_token(token) for token in pointer[1:].split("/")]


def resolve_pointer(document: Any, tokens: list[str]) -> list[tuple[str, Any]]:
    """Return ``(token, node)`` steps from the document root to *tokens*."""
    current = document
    steps: list[tuple[str, Any]] = []
    for token in tokens:
        if isinstance(current, Mapping):
            if token not in current:
                raise KeyError(f"Missing mapping key {token!r}")
            current = current[token]
        elif isinstance(current, list):
            index = int(token)
            current = current[index]
        else:
            raise TypeError(f"Cannot traverse {type(current).__name__} at {token!r}")
        steps.append((token, current))
    return steps


def _build_about(document: Mapping[str, Any]) -> dict[str, Any]:
    """Extract top-level entity identity (`gene`, `module`, `family`, or `rule`)."""
    if "gene_symbol" in document:
        gene: dict[str, Any] = {
            "id": deepcopy(document.get("id")),
            "gene_symbol": deepcopy(document["gene_symbol"]),
        }
        if document.get("product_type"):
            gene["product_type"] = deepcopy(document["product_type"])
        if document.get("taxon"):
            gene["taxon"] = deepcopy(document["taxon"])
        return {"gene": gene}
    if "rule_type" in document or "rule" in document:
        return {
            "rule": {
                "id": deepcopy(document.get("id")),
                "rule_type": deepcopy(document.get("rule_type")),
            }
        }
    if "title" in document and "id" in document:
        return {
            "module": {
                "id": deepcopy(document["id"]),
                "title": deepcopy(document["title"]),
            }
        }
    if "id" in document:
        return {"entity": {"id": deepcopy(document["id"])}}
    raise ValueError(
        "Document does not contain recognizable AIGR entity identity (gene_symbol, title, or id)"
    )


def _normalize_evidence_item(
    raw_evidence: Mapping[str, Any],
    *,
    fallback_reference_id: str | None = None,
    fallback_title: str | None = None,
) -> dict[str, Any]:
    """Normalize an AIGR supporting-text or module evidence item."""
    ref_id = (
        raw_evidence.get("reference_id")
        or raw_evidence.get("source_id")
        or raw_evidence.get("reference")
        or fallback_reference_id
    )
    if not isinstance(ref_id, str) or not ref_id.strip():
        raise ValueError(
            f"Evidence item does not carry a valid reference_id/source_id: {raw_evidence!r}"
        )
    snippet = raw_evidence.get("supporting_text")
    if snippet is None:
        snippet = raw_evidence.get("supporting_text_fulltext") or raw_evidence.get(
            "snippet"
        )
    if not isinstance(snippet, str) or not snippet.strip():
        raise ValueError(
            f"Evidence item for {ref_id!r} has no non-empty supporting_text"
        )
    normalized: dict[str, Any] = {
        "reference_id": ref_id.strip(),
        "reference": ref_id.strip(),
        "supporting_text": snippet,
        "snippet": snippet,
    }
    if fallback_title or raw_evidence.get("title"):
        normalized["title"] = deepcopy(raw_evidence.get("title") or fallback_title)
    if raw_evidence.get("reference_section_type"):
        normalized["reference_section_type"] = deepcopy(
            raw_evidence["reference_section_type"]
        )
    if "full_text_unavailable" in raw_evidence:
        normalized["full_text_unavailable"] = bool(
            raw_evidence["full_text_unavailable"]
        )
    if raw_evidence.get("statement"):
        normalized["statement"] = deepcopy(raw_evidence["statement"])
    return normalized


def _clean_mapping(
    node: Mapping[str, Any],
    *,
    include_review_reason: bool = False,
) -> dict[str, Any]:
    """Copy a mapping while stripping evidence lists and editorial review prose."""
    cleaned: dict[str, Any] = {}
    for key, value in node.items():
        if key in STRIP_ASSERTION_FIELDS:
            continue
        if key == "review" and isinstance(value, Mapping):
            review_copy: dict[str, Any] = {}
            for r_key in ("action", "summary", "proposed_replacement_terms"):
                if value.get(r_key) is not None:
                    review_copy[r_key] = deepcopy(value[r_key])
            if include_review_reason and value.get("reason"):
                review_copy["reason"] = deepcopy(value["reason"])
            if value.get("propagation_review") and isinstance(
                value["propagation_review"], Mapping
            ):
                prop = {
                    k: deepcopy(v)
                    for k, v in value["propagation_review"].items()
                    if k in ("root_cause", "failure_modes", "residue_claims")
                }
                if prop:
                    review_copy["propagation_review"] = prop
            if review_copy:
                cleaned["review"] = review_copy
            continue
        cleaned[key] = deepcopy(value)
    return cleaned


def extract_claim(
    document: Mapping[str, Any],
    evidence_path: str,
    *,
    include_review_reason: bool = False,
) -> dict[str, Any]:
    """Build a self-contained structured claim for one AIGR evidence item.

    Parameters
    ----------
    document:
        Parsed AIGR YAML document (e.g. ``GeneReview`` or ``ModuleReview``).
    evidence_path:
        RFC 6901 JSON Pointer to the evidence item, such as
        ``/core_functions/0/supported_by/0``,
        ``/existing_annotations/1/review/supported_by/0``, or
        ``/references/2/findings/0``.
    include_review_reason:
        Whether to retain ``review.reason`` when extracting a claim from
        ``/existing_annotations/<i>/review/supported_by/<j>``. Defaults to
        ``False`` so multi-reference rationale prose does not leak other
        citations into a single-reference claim check.
    """
    tokens = parse_pointer(evidence_path)
    steps = resolve_pointer(document, tokens)
    if not tokens:
        raise ValueError("evidence_path must point to a specific evidence item")

    about = _build_about(document)
    section = tokens[0]

    # Case 1: /references/<i>/findings/<j>
    if len(tokens) == 4 and tokens[0] == "references" and tokens[2] == "findings":
        ref_node = steps[1][1]
        finding_node = steps[3][1]
        if not isinstance(ref_node, Mapping) or not isinstance(finding_node, Mapping):
            raise ValueError(
                f"Invalid reference finding structure at {evidence_path!r}"
            )
        selected_evidence = _normalize_evidence_item(
            finding_node,
            fallback_reference_id=ref_node.get("id"),
            fallback_title=ref_node.get("title"),
        )
        assertion: dict[str, Any] = {
            "statement": deepcopy(finding_node.get("statement")),
        }
        if finding_node.get("finding_review") and isinstance(
            finding_node["finding_review"], Mapping
        ):
            fr = {
                k: deepcopy(v)
                for k, v in finding_node["finding_review"].items()
                if k in ("finding_status", "superseded_by")
            }
            if fr:
                assertion["finding_review"] = fr
        assertion_path = _encode_pointer(tokens)
        return {
            "about": about,
            "origin": {
                "assertion_path": assertion_path,
                "evidence_path": evidence_path,
                "section": "references",
            },
            "assertion": assertion,
            "selected_evidence": selected_evidence,
        }

    # Case 2: Standard evidence list (.../<supported_by|provenance|evidence>/<j>)
    if len(tokens) < 3 or tokens[-2] not in EVIDENCE_CONTAINERS:
        raise ValueError(
            f"Expected pointer to an item in {sorted(EVIDENCE_CONTAINERS)} or "
            f"/references/<i>/findings/<j>: {evidence_path!r}"
        )

    evidence_node = steps[-1][1]
    if not isinstance(evidence_node, Mapping):
        raise ValueError(f"Evidence target at {evidence_path!r} is not a mapping")

    # Look up reference title from top-level references[] if available
    ref_id = evidence_node.get("reference_id") or evidence_node.get("source_id")
    ref_title: str | None = None
    if isinstance(ref_id, str) and isinstance(document.get("references"), list):
        for ref_entry in document["references"]:
            if isinstance(ref_entry, Mapping) and ref_entry.get("id") == ref_id:
                ref_title = ref_entry.get("title")
                break

    selected_evidence = _normalize_evidence_item(
        evidence_node, fallback_title=ref_title
    )

    # If the evidence is under /existing_annotations/<i>/review/supported_by/<j>,
    # lift to the enclosing existing_annotations/<i> entry so the GO term,
    # qualifier, evidence_type, and review action/summary are all part of the
    # claim assertion.
    if (
        len(tokens) >= 5
        and tokens[0] == "existing_annotations"
        and tokens[2] == "review"
        and tokens[3] == "supported_by"
    ):
        assertion_tokens = tokens[:2]
        ann_node = steps[1][1]
        if not isinstance(ann_node, Mapping):
            raise ValueError(
                f"Annotation node at {_encode_pointer(assertion_tokens)!r} is not a mapping"
            )
        assertion = _clean_mapping(
            ann_node, include_review_reason=include_review_reason
        )
    else:
        assertion_tokens = tokens[:-2]
        target_node = steps[-3][1]
        if not isinstance(target_node, Mapping):
            raise ValueError(
                f"Assertion node at {_encode_pointer(assertion_tokens)!r} is not a mapping"
            )
        assertion = _clean_mapping(
            target_node, include_review_reason=include_review_reason
        )

    # Attach isoform context from top-level functional_isoforms / alternative_products
    # if the assertion specifies an isoform.
    isoform_id = assertion.get("isoform")
    if isoform_id and "gene" in about:
        for alt in document.get("alternative_products") or []:
            if isinstance(alt, Mapping) and alt.get("id") == isoform_id:
                about["gene"]["isoform"] = {
                    "id": alt["id"],
                    "name": alt.get("name"),
                }
                break

    return {
        "about": about,
        "origin": {
            "assertion_path": _encode_pointer(assertion_tokens),
            "evidence_path": evidence_path,
            "section": section,
        },
        "assertion": assertion,
        "selected_evidence": selected_evidence,
    }
