# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** STAT3
- **Gene symbol:** STAT3

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** readout-go-0030335
- **Source file:** genes/human/STAT3/STAT3-ai-review.yaml
- **Source selector:** existing_annotations[247]

## Seed Hypothesis

The existing STAT3 GO annotation to positive regulation of cell migration (GO:0030335) is currently action ACCEPT and was flagged by the ASSAY_TO_FUNCTION readout class CELL_MIGRATION_INVASION. Decide whether this BP term is a CORE function of STAT3 (a primary process the gene product evolved to drive) versus a DOWNSTREAM, secondary, or context-dependent consequence of its core molecular activity that is better captured as non-core. Distinguish a 'real, documented effect' (which may not be in question) from a 'core function'. Flag rationale: ACCEPT BP call aligned to CELL_MIGRATION_INVASION; rubric default is non-core unless gene is in the machinery

## Term and Decision Context

- Term: positive regulation of cell migration (GO:0030335)
- Evidence type: IMP
- Original reference: PMID:31638206
- Current review action: UNDECIDED
- Review summary: Experimental evidence (IMP) supports positive regulation of cell migration for STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]
- Review reason: Real but borderline core vs non-core. STAT3's core molecular function is signal-dependent DNA-binding transcription factor activity (JAK-STAT); cell migration is a downstream transcriptional consequence rather than an activity STAT3 itself performs, and STAT3 is not part of the cytoskeletal/ adhesion motility machinery. The IMP evidence (knockdown/overexpression migration phenotype) is the classic indirect "perturb gene -> phenotype" inference. Flagged by the ASSAY_TO_FUNCTION CELL_MIGRATION_INVASION readout class; given STAT3 is high-profile and the call is genuinely contested (oncogenic migration driver vs downstream consequence), deferred to expert review rather than unilaterally demoted (issue #1422; staged OpenScientist hypothesis job under STAT3-hypotheses/).

## Reference Context

- PMID:31638206

## Source Context YAML

```yaml
term:
  id: GO:0030335
  label: positive regulation of cell migration
evidence_type: IMP
original_reference_id: PMID:31638206
review:
  summary: Experimental evidence (IMP) supports positive regulation of cell migration for STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]
  action: UNDECIDED
  reason: 'Real but borderline core vs non-core. STAT3''s core molecular function is signal-dependent
    DNA-binding transcription factor activity (JAK-STAT); cell migration is a downstream transcriptional
    consequence rather than an activity STAT3 itself performs, and STAT3 is not part of the cytoskeletal/
    adhesion motility machinery. The IMP evidence (knockdown/overexpression migration phenotype) is the
    classic indirect "perturb gene -> phenotype" inference. Flagged by the ASSAY_TO_FUNCTION CELL_MIGRATION_INVASION
    readout class; given STAT3 is high-profile and the call is genuinely contested (oncogenic migration
    driver vs downstream consequence), deferred to expert review rather than unilaterally demoted (issue
    #1422; staged OpenScientist hypothesis job under STAT3-hypotheses/).'
  supported_by:
  - reference_id: PMID:31638206
    supporting_text: Oct 11. MicroRNA‑4500 suppresses tumor progression in non‑small cell lung cancer
      by regulating STAT3.
```

## Research Objective

Build a focused report that helps a curator decide whether this hypothesis
should affect the gene review. Address the focus type directly:

1. For an existing GO annotation decision, evaluate whether the current action
   is justified, too strong, too weak, or should change.
2. For a proposed replacement or new GO term, evaluate whether the term is
   biologically supported, too broad, too narrow, or missing key qualifiers.
3. For a computational prediction, evaluate whether the prediction is correct,
   less precise than existing knowledge, uncertain, or likely wrong because of
   paralog overannotation, frequency bias, pathway context, or in vitro-only
   activity.
4. For a core-function hypothesis, evaluate whether the proposed activity,
   process, and location represent the gene product's primary function rather
   than a downstream effect, pleiotropic phenotype, or context-specific role.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

## Required Output

### Executive Judgment

Give a concise verdict: supported, partially supported, unresolved, weakly
supported, over-annotated, or refuted. Explain the reasoning and the most
important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (direct assay, mutant phenotype, localization, interaction,
  structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies / competing
- Claim tested
- Key finding
- Organism, tissue, cell type, or assay context
- Confidence and limitations

### GO Curation Implications

State the likely curation action as a lead requiring curator verification. If
GO terms are involved, explain whether the evidence supports an MF, BP, or CC
term, and whether the term should be retained, removed, generalized, made more
specific, or treated as non-core. Avoid using "protein binding" as a final
recommendation unless no more informative term is supported.

### Mechanistic Scope

Describe the immediate molecular or cellular function being tested. Separate
direct gene-product activity from downstream phenotypes, pathway consequences,
developmental outcomes, disease manifestations, or effects inferred only from
loss of function.

### Conflicts and Alternatives

Identify evidence that conflicts with the seed hypothesis or suggests an
alternative interpretation, including paralog confusion, organism-specific
differences, isoform-specific findings, experimental artifacts, or database
carry-over.

### Knowledge Gaps

List explicit uncertainties that matter for curation. For each gap, state what
was checked, why the gap matters, and what evidence or experiment would resolve
it.

### Discriminating Tests

Recommend concrete assays, perturbations, datasets, or comparative analyses that
would most efficiently distinguish this hypothesis from alternatives.

### Curation Leads

Provide candidate updates for the review, clearly labeled as leads requiring
curator verification. Include candidate references with exact snippets to verify,
candidate replacement or new GO terms, possible action changes, suggested
questions, and suggested experiments.

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.
