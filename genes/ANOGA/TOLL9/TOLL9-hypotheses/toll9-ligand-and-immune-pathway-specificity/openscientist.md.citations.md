# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ANOGA
- **Taxon:** Anopheles gambiae (NCBITaxon:7165)
- **Gene directory:** TOLL9
- **Gene symbol:** TOLL9
- **UniProt accession:** Q5TWL7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** toll9-ligand-and-immune-pathway-specificity
- **Source file:** genes/ANOGA/TOLL9/TOLL9-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Anopheles gambiae TOLL9 (Q5TWL7/AGAP006974) has pattern-recognition receptor activity and participates in innate immunity through the Toll signaling pathway. Assess actual target phylogeny and transfer scope, ligand and accessory/downstream partners. Current target leaf PTN000688561 in PTHR24365 descends from PTN002808045 supporting generic receptor/signaling/plasma membrane. PMID33963082 establishes Bombyx Toll9 LPS recognition with MD-2-like partners, including a chimera whose TM/TIR regions are mouse TLR4; distinguish those experiments. PMID21386906 reports Drosophila Toll9 knockout without basal or inducible antibacterial AMP defects under tested conditions, while acknowledging overexpression-induced signaling. PMID38191283 reports AGAP006974 induction after mosGILT disruption, not target perturbation. Determine whether conservation supports PRR/Toll immune roles or target divergence changes them; a small experimental donor set alone is not weak evidence. Do not assume every insect Toll uses Spaetzle, or confuse recognition of processed host cytokine with GO0038187 microbial PAMP recognition. The separate inflammatory-response row is already resolved by explicit GO0006954 vertebrate-only constraint and is not this question.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Anopheles gambiae TOLL9 (Q5TWL7/AGAP006974) has pattern-recognition receptor activity and
  participates in innate immunity through the Toll signaling pathway. Assess actual target phylogeny and
  transfer scope, ligand and accessory/downstream partners. Current target leaf PTN000688561 in PTHR24365
  descends from PTN002808045 supporting generic receptor/signaling/plasma membrane. PMID33963082 establishes
  Bombyx Toll9 LPS recognition with MD-2-like partners, including a chimera whose TM/TIR regions are mouse
  TLR4; distinguish those experiments. PMID21386906 reports Drosophila Toll9 knockout without basal or
  inducible antibacterial AMP defects under tested conditions, while acknowledging overexpression-induced
  signaling. PMID38191283 reports AGAP006974 induction after mosGILT disruption, not target perturbation.
  Determine whether conservation supports PRR/Toll immune roles or target divergence changes them; a small
  experimental donor set alone is not weak evidence. Do not assume every insect Toll uses Spaetzle, or
  confuse recognition of processed host cytokine with GO0038187 microbial PAMP recognition. The separate
  inflammatory-response row is already resolved by explicit GO0006954 vertebrate-only constraint and is
  not this question.
focus_type: function_assignment
context: []
reference_id: []
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
**Generated:** 2026-09-21T02:12:30.270212

1. PMID:33963082
2. PMID:21386906
3. PMID:38191283
4. PMID:35238667
5. PMID:25573502