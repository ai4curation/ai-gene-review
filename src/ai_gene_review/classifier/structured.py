"""Build classification tasks for AIGR evidence-claim and annotation-action benchmarks."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import yaml

from ai_gene_review.classifier.aspects import (
    annotation_action_aspects_schema,
    claim_aspects_schema,
)
from ai_gene_review.classifier.base import Choice, ClassificationTask
from ai_gene_review.classifier.rubric import (
    ANNOTATION_ACTION_CHOICES,
    ANNOTATION_ACTION_INSTRUCTION,
    COARSE_ACTION_CHOICES,
    EVIDENCE_CLAIM_ASPECTS_INSTRUCTION,
    EVIDENCE_CLAIM_CHOICES,
    EVIDENCE_CLAIM_INSTRUCTION,
)


def _dump_yaml(data: Mapping[str, Any]) -> str:
    return yaml.safe_dump(
        dict(data), sort_keys=False, allow_unicode=True, width=100
    ).strip()


def _evidence_claim_context(
    claim: Mapping[str, Any],
    source_text: str | None = None,
) -> str:
    selected = claim.get("selected_evidence")
    if not isinstance(selected, Mapping):
        raise ValueError("structured claim must include selected_evidence")
    snippet = selected.get("supporting_text") or selected.get("snippet")
    if not isinstance(snippet, str) or not snippet.strip():
        raise ValueError(
            "structured claim selected_evidence must include non-empty supporting_text/snippet"
        )
    sections = [
        f"Structured claim (YAML):\n{_dump_yaml(claim)}",
        f"Supporting text excerpt:\n{snippet.strip()}",
    ]
    if source_text is not None:
        if not source_text.strip():
            raise ValueError("source_text must be non-empty when provided")
        sections.append(f"Full cached reference text:\n{source_text.strip()}")
    return "\n\n".join(sections)


def structured_evidence_claim_match_task(
    claim: Mapping[str, Any],
    source_text: str | None = None,
    *,
    choices: Sequence[Choice] = EVIDENCE_CLAIM_CHOICES,
) -> ClassificationTask:
    """Create a whole-claim `MATCH` / `PARTIAL` / `MISMATCH` classification task."""
    return ClassificationTask(
        instruction=EVIDENCE_CLAIM_INSTRUCTION,
        context=_evidence_claim_context(claim, source_text),
        choices=tuple(choices),
        question="Does the reference text support the structured gene curation claim?",
    )


def structured_evidence_claim_aspects_task(
    claim: Mapping[str, Any],
    source_text: str | None = None,
    *,
    choices: Sequence[Choice] = EVIDENCE_CLAIM_CHOICES,
) -> ClassificationTask:
    """Create a per-aspect JSON-schema classification task for a structured claim."""
    return ClassificationTask(
        instruction=EVIDENCE_CLAIM_ASPECTS_INSTRUCTION,
        context=_evidence_claim_context(claim, source_text),
        output_schema=claim_aspects_schema(claim, choices),
        question="Return the support judgment for `/` and each requested aspect path.",
    )


def _annotation_action_context(
    annotation_case: Mapping[str, Any],
    *,
    reference_texts: Mapping[str, str] | None = None,
    uniprot_text: str | None = None,
) -> str:
    if not isinstance(annotation_case.get("target_annotation"), Mapping):
        raise ValueError("annotation_case must include target_annotation")
    sections = [
        f"Annotation review case (YAML):\n{_dump_yaml(annotation_case)}",
    ]
    excerpts = annotation_case.get("supporting_excerpts")
    if isinstance(excerpts, list) and excerpts:
        excerpt_lines = []
        for item in excerpts:
            if isinstance(item, Mapping) and item.get("supporting_text"):
                ref_id = item.get("reference_id") or "source"
                excerpt_lines.append(f'- [{ref_id}] "{item["supporting_text"]}"')
        if excerpt_lines:
            sections.append("Supporting text excerpts:\n" + "\n".join(excerpt_lines))
    if uniprot_text and uniprot_text.strip():
        sections.append(f"UniProt record excerpt:\n{uniprot_text.strip()}")
    if reference_texts:
        for ref_id, text in reference_texts.items():
            if isinstance(text, str) and text.strip():
                sections.append(f"Reference {ref_id}:\n{text.strip()}")
    return "\n\n".join(sections)


def annotation_action_task(
    annotation_case: Mapping[str, Any],
    *,
    reference_texts: Mapping[str, str] | None = None,
    uniprot_text: str | None = None,
    choices: Sequence[Choice] = ANNOTATION_ACTION_CHOICES,
) -> ClassificationTask:
    """Create a 7-way `ActionEnum` classification task for an existing GOA annotation."""
    return ClassificationTask(
        instruction=ANNOTATION_ACTION_INSTRUCTION,
        context=_annotation_action_context(
            annotation_case,
            reference_texts=reference_texts,
            uniprot_text=uniprot_text,
        ),
        choices=tuple(choices),
        question="What is the appropriate AIGR review action (ActionEnum) for target_annotation?",
    )


def annotation_action_coarse_task(
    annotation_case: Mapping[str, Any],
    *,
    reference_texts: Mapping[str, str] | None = None,
    uniprot_text: str | None = None,
    choices: Sequence[Choice] = COARSE_ACTION_CHOICES,
) -> ClassificationTask:
    """Create a 4-way coarse accept-state (`KEEP`, `REFINE`, `REJECT`, `DEFER`) task."""
    return ClassificationTask(
        instruction=ANNOTATION_ACTION_INSTRUCTION,
        context=_annotation_action_context(
            annotation_case,
            reference_texts=reference_texts,
            uniprot_text=uniprot_text,
        ),
        choices=tuple(choices),
        question="What is the coarse review disposition (KEEP, REFINE, REJECT, DEFER) for target_annotation?",
    )


def annotation_action_aspects_task(
    annotation_case: Mapping[str, Any],
    *,
    reference_texts: Mapping[str, str] | None = None,
    uniprot_text: str | None = None,
    include_propagation: bool = True,
) -> ClassificationTask:
    """Create a multi-aspect classification task (`/`, `/coarse_action`, `/is_core`, `/propagation_root_cause`)."""
    return ClassificationTask(
        instruction=ANNOTATION_ACTION_INSTRUCTION,
        context=_annotation_action_context(
            annotation_case,
            reference_texts=reference_texts,
            uniprot_text=uniprot_text,
        ),
        output_schema=annotation_action_aspects_schema(
            annotation_case, include_propagation=include_propagation
        ),
        question="Return the review judgments for `/` (ActionEnum) and each requested aspect path.",
    )
