# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** AGR3
- **Gene symbol:** AGR3
- **UniProt accession:** Q8TD06

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-activity
- **Source file:** genes/human/AGR3/AGR3-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

The described activity is a core function of AGR3. Current rationale: AGR3 is an ER-retained AGR/thioredoxin-like protein in ciliated airway epithelial cells that is required for normal calcium-dependent regulation of ciliary beat frequency and mucociliary clearance. The molecular client or catalytic activity remains unresolved, and current evidence does not justify a canonical protein disulfide isomerase activity annotation.

## Term and Decision Context

- Molecular function: not specified
- Description: AGR3 is an ER-retained AGR/thioredoxin-like protein in ciliated airway epithelial cells that is required for normal calcium-dependent regulation of ciliary beat frequency and mucociliary clearance. The molecular client or catalytic activity remains unresolved, and current evidence does not justify a canonical protein disulfide isomerase activity annotation.
- Directly involved in: epithelial cilium movement involved in extracellular fluid movement (GO:0003351), calcium-mediated signaling (GO:0019722)
- Locations: endoplasmic reticulum (GO:0005783)

## Reference Context

- PMID:25751668
- file:human/AGR3/AGR3-deep-research-falcon.md

## Source Context YAML

```yaml
description: AGR3 is an ER-retained AGR/thioredoxin-like protein in ciliated airway epithelial cells that
  is required for normal calcium-dependent regulation of ciliary beat frequency and mucociliary clearance.
  The molecular client or catalytic activity remains unresolved, and current evidence does not justify
  a canonical protein disulfide isomerase activity annotation.
directly_involved_in:
- id: GO:0003351
  label: epithelial cilium movement involved in extracellular fluid movement
- id: GO:0019722
  label: calcium-mediated signaling
locations:
- id: GO:0005783
  label: endoplasmic reticulum
supported_by:
- reference_id: PMID:25751668
  supporting_text: AGR3 deficiency had no detectable effects on ciliary beat frequency (CBF) when airways
    were perfused with a calcium-free solution, suggesting that AGR3 is required for calcium-mediated
    regulation of ciliary function. Decreased CBF was associated with impaired mucociliary clearance in
    AGR3-deficient airways.
  reference_section_type: ABSTRACT
- reference_id: file:human/AGR3/AGR3-deep-research-falcon.md
  supporting_text: AGR3 lacks the canonical PDI/thioredoxin CXXC or WCXXC motif; structure paper reports
    a DCYQS motif with solvent-exposed Cys71 in reduced state. Because the second catalytic cysteine is
    absent and an adjacent acidic residue likely raises cysteine pKa, AGR3 is inferred to have reduced/atypical
    thiol-disulfide exchange activity relative to classical PDIs
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
5. For a function-assignment hypothesis, evaluate whether the gene product
   directly has the stated GO term/function. Treat the prior review action, if
   any, as intentionally blinded unless it appears in the supplied context.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

Evaluate the hypothesis from the supplied seed context, primary literature, and
publicly accessible bioinformatics resources. Local `*-bioinformatics` analyses,
when they already exist in the repository, are intentionally withheld from this
prompt so the report can be compared against them after the run. Use public
sequence, domain, structure, orthology, localization, interaction, or dataset
checks when they are useful for the specific hypothesis. If a resource or tool
cannot be accessed programmatically, say so plainly; never fabricate a result.
Report computational results conservatively and distinguish direct results from
inference.

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

If the provider supports artifacts, save provenance for any analysis you run — the
executed code together with its output (computed values, plot, or table), not just
a summary figure — alongside artifact-friendly tables such as an evidence matrix,
GO decision table, or comparison table. Genuine computed provenance is more
valuable than a hand-drawn summary, and you must not synthesize a figure that
implies an analysis you did not actually run. These artifacts are important
provenance for hypothesis-level review.

**Provider:** openscientist
**Generated:** 2026-07-04T16:30:08.086827

1. PMID:25751668
2. PMID:29969106
3. PMID:12592373
4. PMID:26170690
5. PMID:39026356
6. PMID:22361111
7. PMID:31611954
8. PMID:39673647
9. PMID:25416956
10. PMID:32296183
11. PMID:31291711
12. PMID:32724387
13. PMID:34519905
14. PMID:24747240
15. PMID:20186508
16. PMID:27068954
17. PMID:37216546