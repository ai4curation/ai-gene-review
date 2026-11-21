"""Aspect path discovery and JSON Schema compilation for AIGR benchmark tasks."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from functools import lru_cache
from pathlib import Path
from typing import Any

from linkml_runtime.utils.schemaview import SchemaView

from ai_gene_review.classifier.base import Choice
from ai_gene_review.classifier.claims import encode_pointer
from ai_gene_review.classifier.rubric import (
    ANNOTATION_ACTION_CHOICES,
    COARSE_ACTION_CHOICES,
    EVIDENCE_CLAIM_CHOICES,
)

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "gene_review.yaml"

SKIP_ASPECT_SLOTS = frozenset(
    {
        "supported_by",
        "provenance",
        "evidence",
        "additional_reference_ids",
        "knowledge_gaps",
        "original_reference_id",
        "retired",
    }
)

PROPAGATED_EVIDENCE_TYPES = frozenset(
    {"IBA", "IBD", "IKR", "IRD", "ISS", "ISO", "ISA", "ISM", "IGC", "RCA", "IEA"}
)

PROPAGATION_ROOT_CAUSE_CHOICES = (
    Choice(
        "NO_FAILURE_CORE", "propagated annotation is correct and core for the target"
    ),
    Choice(
        "NO_FAILURE_NON_CORE",
        "propagated annotation is biologically defensible but contextual, secondary, or generic",
    ),
    Choice(
        "SOURCE_BAD",
        "source annotation is wrong, miscited, homonym-confused, or contradicted",
    ),
    Choice(
        "SOURCE_STALE_OR_MISSING",
        "transferred term no longer appears on the current source record, or donor tracing cannot recover it",
    ),
    Choice(
        "SOURCE_WEAK_OR_INFERRED",
        "source exists but is only inferred, statement-level, or otherwise weak for propagation",
    ),
    Choice(
        "EVIDENCE_CIRCULAR_OR_REDUNDANT",
        "propagation chain transfers from another transfer, or the target already has stronger direct evidence",
    ),
    Choice(
        "PROPAGATION_BAD",
        "source annotation is sound, but the term should not propagate to this target",
    ),
    Choice(
        "TERM_SCOPING_PROBLEM",
        "biology is related, but the GO term is too broad, too specific, or has the wrong role or qualifier",
    ),
    Choice(
        "UNRESOLVED",
        "propagation issue was investigated but could not be classified confidently",
    ),
)

CORE_STATUS_CHOICES = (
    Choice(
        "CORE",
        "the annotation represents a core evolved function, process, or location (`ACCEPT`)",
    ),
    Choice(
        "NON_CORE",
        "the annotation is true of the gene but non-core or subsumed (`KEEP_AS_NON_CORE` or `TOO_GENERAL`)",
    ),
    Choice(
        "NOT_APPLICABLE",
        "the annotation is rejected, modified to another term, or deferred (`REMOVE`, `MARK_AS_OVER_ANNOTATED`, `MODIFY`, `UNDECIDED`)",
    ),
)


@lru_cache(maxsize=1)
def _schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


def _slot_description(slot_name: str) -> str:
    view = _schema_view()
    slot = view.induced_slot(slot_name) if slot_name in view.all_slots() else None
    if slot and slot.description:
        return " ".join(str(slot.description).split())
    # Synthetic wrapper keys in `about` that are not LinkML slots in gene_review.yaml
    wrapper_descriptions = {
        "gene": "Target gene identity (UniProt accession, HGNC/MOD symbol, and taxon).",
        "module": "Target biological module identity.",
        "rule": "Target UniProt annotation rule identity.",
        "entity": "Target biological entity identity.",
    }
    return wrapper_descriptions.get(slot_name, f"Claim field {slot_name!r}.")


def _choice_property(description: str, choices: Sequence[Choice]) -> dict[str, Any]:
    rules = " ".join(
        f"Return {choice.value} if {choice.description}." for choice in choices
    )
    return {
        "type": "string",
        "enum": [choice.value for choice in choices],
        "description": f"{description} {rules}".strip(),
    }


def claim_aspect_paths(claim: Mapping[str, Any]) -> list[str]:
    """Return the ordered JSON Pointer paths scored for an AIGR structured claim."""
    paths = ["/"]
    about = claim.get("about")
    if isinstance(about, Mapping):
        for key in ("gene", "module", "rule", "entity"):
            if key in about:
                paths.append(encode_pointer(["about", key]))
                break
    assertion = claim.get("assertion")
    if isinstance(assertion, Mapping):
        for key, value in assertion.items():
            if key in SKIP_ASPECT_SLOTS or value is None or value == [] or value == {}:
                continue
            paths.append(encode_pointer(["assertion", key]))
    return paths


def claim_aspects_schema(
    claim: Mapping[str, Any],
    choices: Sequence[Choice] = EVIDENCE_CLAIM_CHOICES,
) -> dict[str, Any]:
    """Build a JSON object schema with one enum property per claim aspect path."""
    paths = claim_aspect_paths(claim)
    properties: dict[str, Any] = {}
    for path in paths:
        if path == "/":
            desc = (
                "Overall claim support: whether the reference text supports the "
                "complete structured gene curation claim."
            )
        elif path.startswith("/about/"):
            entity_key = path.split("/")[-1]
            desc = (
                f"Entity grounding ({path}): {_slot_description(entity_key)} "
                "Judge whether the reference text is about this gene/ortholog or module."
            )
        else:
            slot_name = path.split("/")[-1]
            desc = f"Aspect {path} ({slot_name}): {_slot_description(slot_name)}"
        properties[path] = _choice_property(desc, choices)
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


def annotation_action_aspect_paths(
    annotation_case: Mapping[str, Any],
    *,
    include_propagation: bool = True,
) -> list[str]:
    """Return the aspect paths for an annotation accept-state evaluation."""
    paths = ["/", "/coarse_action", "/is_core"]
    target = annotation_case.get("target_annotation") or {}
    ev_type = str(target.get("evidence_type") or "")
    if include_propagation and ev_type in PROPAGATED_EVIDENCE_TYPES:
        paths.append("/propagation_root_cause")
    return paths


def annotation_action_aspects_schema(
    annotation_case: Mapping[str, Any],
    *,
    include_propagation: bool = True,
) -> dict[str, Any]:
    """Build a multi-aspect JSON schema for annotation accept-state classification.

    - ``/``: fine-grained ``ActionEnum`` judgment
    - ``/coarse_action``: 4-way coarse accept state (``KEEP``, ``REFINE``, ``REJECT``, ``DEFER``)
    - ``/is_core``: whether the annotation is a core function (``CORE``, ``NON_CORE``, ``NOT_APPLICABLE``)
    - ``/propagation_root_cause`` (when propagated): ``PropagationRootCauseEnum``
    """
    properties: dict[str, Any] = {
        "/": _choice_property(
            "Primary fine-grained review action (ActionEnum) for the target GOA annotation.",
            ANNOTATION_ACTION_CHOICES,
        ),
        "/coarse_action": _choice_property(
            "Coarse 4-way disposition of the annotation (KEEP, REFINE, REJECT, DEFER).",
            COARSE_ACTION_CHOICES,
        ),
        "/is_core": _choice_property(
            "Whether the annotation represents a core evolved function of the gene.",
            CORE_STATUS_CHOICES,
        ),
    }
    target = annotation_case.get("target_annotation") or {}
    ev_type = str(target.get("evidence_type") or "")
    if include_propagation and ev_type in PROPAGATED_EVIDENCE_TYPES:
        properties["/propagation_root_cause"] = _choice_property(
            "Root-cause classification for this propagated/inferred annotation.",
            PROPAGATION_ROOT_CAUSE_CHOICES,
        )
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }
