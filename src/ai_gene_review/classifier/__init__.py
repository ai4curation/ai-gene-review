"""Closed-set classifiers, structured claim extractors, and benchmark task builders for AIGR."""

from ai_gene_review.classifier.annotation_nodes import (
    derive_annotation_review_target,
    extract_annotation_case,
)
from ai_gene_review.classifier.aspects import (
    annotation_action_aspect_paths,
    annotation_action_aspects_schema,
    claim_aspect_paths,
    claim_aspects_schema,
)
from ai_gene_review.classifier.base import (
    Choice,
    ClassificationResult,
    ClassificationTask,
    Classifier,
)
from ai_gene_review.classifier.claims import extract_claim, parse_pointer
from ai_gene_review.classifier.rubric import (
    ANNOTATION_ACTION_CHOICES,
    ANNOTATION_ACTION_INSTRUCTION,
    ANNOTATION_ACTION_RUBRIC,
    COARSE_ACTION_CHOICES,
    COARSE_ACTION_MAP,
    EVIDENCE_CLAIM_ASPECTS_INSTRUCTION,
    EVIDENCE_CLAIM_CHOICES,
    EVIDENCE_CLAIM_INSTRUCTION,
    EVIDENCE_CLAIM_RUBRIC,
    coarse_action,
)
from ai_gene_review.classifier.structured import (
    annotation_action_aspects_task,
    annotation_action_coarse_task,
    annotation_action_task,
    structured_evidence_claim_aspects_task,
    structured_evidence_claim_match_task,
)
from ai_gene_review.classifier.typesafe import (
    DEFAULT_BASE_URL,
    DEFAULT_MODEL,
    TypeSafeClassifier,
    render_prompt,
    response_schema,
)

__all__ = [
    "ANNOTATION_ACTION_CHOICES",
    "ANNOTATION_ACTION_INSTRUCTION",
    "ANNOTATION_ACTION_RUBRIC",
    "COARSE_ACTION_CHOICES",
    "COARSE_ACTION_MAP",
    "Choice",
    "ClassificationResult",
    "ClassificationTask",
    "Classifier",
    "DEFAULT_BASE_URL",
    "DEFAULT_MODEL",
    "EVIDENCE_CLAIM_ASPECTS_INSTRUCTION",
    "EVIDENCE_CLAIM_CHOICES",
    "EVIDENCE_CLAIM_INSTRUCTION",
    "EVIDENCE_CLAIM_RUBRIC",
    "TypeSafeClassifier",
    "annotation_action_aspect_paths",
    "annotation_action_aspects_schema",
    "annotation_action_aspects_task",
    "annotation_action_coarse_task",
    "annotation_action_task",
    "claim_aspect_paths",
    "claim_aspects_schema",
    "coarse_action",
    "derive_annotation_review_target",
    "extract_annotation_case",
    "extract_claim",
    "parse_pointer",
    "render_prompt",
    "response_schema",
    "structured_evidence_claim_aspects_task",
    "structured_evidence_claim_match_task",
]
