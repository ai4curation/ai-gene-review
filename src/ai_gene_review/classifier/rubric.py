"""Rubrics and choice definitions for AIGR benchmark tasks.

Defines two primary benchmark rubrics:
1. ``EVIDENCE_CLAIM_RUBRIC`` (``aigr-evidence-claim-v1``): evaluates whether a
   cited supporting_text excerpt (and optional cached reference text) supports
   an AIGR structured claim (`core_functions`, `existing_annotations`,
   `findings`, `proposed_new_terms`, `knowledge_gaps`, or `modules`).
2. ``ANNOTATION_ACTION_RUBRIC`` (``aigr-annotation-action-v1``): evaluates the
   curator accept-state classification (`ActionEnum`: `ACCEPT`,
   `KEEP_AS_NON_CORE`, `REMOVE`, `MODIFY`, `MARK_AS_OVER_ANNOTATED`,
   `TOO_GENERAL`, `UNDECIDED`) for an existing GOA annotation row given the
   gene's biological context, sibling annotations, and supporting evidence.
"""

from __future__ import annotations

from ai_gene_review.classifier.base import Choice

# =============================================================================
# 1. Evidence-Claim Match Rubric
# =============================================================================

EVIDENCE_CLAIM_RUBRIC = "aigr-evidence-claim-v1"

EVIDENCE_CLAIM_INSTRUCTION = (
    "Decide whether the provided reference text supports the structured gene "
    "curation claim. Compare the text against the biological entity (`about` "
    "gene, taxon, isoform, or module) and the asserted function, process, "
    "cellular component, finding, or knowledge gap. Ignore other fields inside "
    "`selected_evidence` except the quoted `supporting_text` (`snippet`).\n\n"
    "Rubric:\n"
    "- MATCH: The text directly supports the claim as stated, including the "
    "gene/ortholog identity, GO term or functional role, and cellular/biological "
    "context. Editorial clarifications in square brackets (e.g. `[CFAP300 shows]`) "
    "and `...` elisions are valid when the underlying source text substantiates "
    "the claim.\n"
    "- PARTIAL: The text supports part of the claim or a related broader/narrower "
    "finding (for example, it establishes localization or a mutant phenotype "
    "without the specific molecular mechanism, or assays a model-organism "
    "ortholog when the claim is unqualified), so key aspects of the claim are "
    "left unsupported or over-specified.\n"
    "- MISMATCH: The text is unrelated to the claim, contradicts it, describes "
    "a different gene/paralog without establishing relevance to the target gene, "
    "or fails to support the core assertion."
)

EVIDENCE_CLAIM_ASPECTS_INSTRUCTION = (
    "Judge each requested JSON Pointer path of the structured gene curation "
    "claim against the provided reference text. Return `/` for the whole claim "
    "and each listed path for that specific field or sub-assertion. Ignore "
    "`selected_evidence` metadata except the quoted `supporting_text` (`snippet`)."
)

EVIDENCE_CLAIM_CHOICES = (
    Choice(
        "MATCH",
        "the reference text directly supports this claim or aspect at the stated specificity",
    ),
    Choice(
        "PARTIAL",
        "the reference text supports only part of this claim/aspect or supports a broader/related statement",
    ),
    Choice(
        "MISMATCH",
        "the reference text does not support, is unrelated to, or contradicts this claim/aspect",
    ),
)


# =============================================================================
# 2. Annotation Action (Accept-State) Classification Rubric
# =============================================================================

ANNOTATION_ACTION_RUBRIC = "aigr-annotation-action-v1"

ANNOTATION_ACTION_INSTRUCTION = (
    "Classify the review action (`ActionEnum`) for the `target_annotation` GOA "
    "row of the gene described in `about`, using the sibling GOA annotations and "
    "the provided reference / UniProt evidence.\n\n"
    "Follow the AI Gene Review (AIGR) curation rules strictly:\n"
    "1. Judge claims about the gene, not evidence codes: duplicate rows that share "
    "a true GO term (e.g. from IEA, ISS, IBA, and IDA) reinforce each other; "
    "never use REMOVE to deduplicate them.\n"
    "2. ACCEPT: The annotation is accurate, supported by evidence, at the "
    "appropriate level of specificity, and represents a core evolved function, "
    "process, or localization of the gene.\n"
    "3. KEEP_AS_NON_CORE: The annotation is accurate and as specific as the "
    "evidence allows, but describes a secondary, peripheral, pleiotropic, or "
    "downstream developmental/contextual effect rather than a core function.\n"
    "4. MODIFY: The essence of the annotation is sound, but a better GO term "
    "should replace it (`proposed_replacement_terms`). Use MODIFY when the term "
    "is right but more general than the row's own evidence supports (refine to "
    "the specific descendant term), or when a lateral/sign correction is needed "
    "(e.g. `positive` -> `negative regulation`, or `enables` vs `contributes_to` "
    "term adjustment).\n"
    "5. TOO_GENERAL: The term is true of the gene, but uninformative because a "
    "more specific descendant term already asserted elsewhere on this gene "
    "(in `sibling_annotations`) entails it, and this row's own evidence does not "
    "independently warrant modifying this row.\n"
    "6. MARK_AS_OVER_ANNOTATED: The term is not completely fabricated, but over-interprets "
    "indirect, phenotypic, or pathway-upstream perturbation data as direct "
    "involvement or activity.\n"
    "7. REMOVE: The annotation is biologically unsupported or false based on "
    "combined evidence (e.g. contradicted experimentally, paralog/domain "
    "over-propagation where ligand specificity or catalytic function diverged, "
    "cascade IEA from a false inference, or wrong organism/lineage). Never REMOVE "
    "an experimental annotation solely because a cached abstract mentions another "
    "gene if the full text is unavailable.\n"
    "8. UNDECIDED: The evidence is genuinely ambiguous or the relevant primary "
    "publication full text is unavailable and cannot be verified from other sources."
)

ANNOTATION_ACTION_CHOICES = (
    Choice(
        "ACCEPT",
        "the annotation is accurate, appropriately specific, and represents a core function, process, or location of the gene",
    ),
    Choice(
        "KEEP_AS_NON_CORE",
        "the annotation is accurate and appropriately specific, but represents a secondary, contextual, or pleiotropic non-core role",
    ),
    Choice(
        "MODIFY",
        "the annotation is directionally sound, but a more specific or corrected replacement GO term is warranted by the evidence",
    ),
    Choice(
        "TOO_GENERAL",
        "the term is true of the gene but uninformative because a more specific term already present on the gene subsumes it",
    ),
    Choice(
        "MARK_AS_OVER_ANNOTATED",
        "the term over-interprets indirect phenotype, downstream, or complex-wide effects as direct gene function",
    ),
    Choice(
        "REMOVE",
        "the annotation is biologically unsupported or false for this gene (contradicted, false phylogenetic/domain propagation, or cascade error)",
    ),
    Choice(
        "UNDECIDED",
        "the annotation cannot be resolved confidently from available evidence or accessible publication text",
    ),
)

COARSE_ACTION_CHOICES = (
    Choice(
        "KEEP",
        "retain the annotation as true (`ACCEPT` or `KEEP_AS_NON_CORE`)",
    ),
    Choice(
        "REFINE",
        "the term is true/sound in essence but should be replaced by or subsumed under a more specific/accurate term (`MODIFY` or `TOO_GENERAL`)",
    ),
    Choice(
        "REJECT",
        "do not retain the annotation as a valid direct claim (`REMOVE` or `MARK_AS_OVER_ANNOTATED`)",
    ),
    Choice(
        "DEFER",
        "defer decision due to insufficient or inaccessible evidence (`UNDECIDED`)",
    ),
)

COARSE_ACTION_MAP: dict[str, str] = {
    "ACCEPT": "KEEP",
    "KEEP_AS_NON_CORE": "KEEP",
    "MODIFY": "REFINE",
    "TOO_GENERAL": "REFINE",
    "REMOVE": "REJECT",
    "MARK_AS_OVER_ANNOTATED": "REJECT",
    "UNDECIDED": "DEFER",
}


def coarse_action(action: str) -> str:
    """Map a fine-grained ``ActionEnum`` value to its 4-way coarse category."""
    if action not in COARSE_ACTION_MAP:
        raise ValueError(f"Unsupported annotation review action: {action!r}")
    return COARSE_ACTION_MAP[action]
