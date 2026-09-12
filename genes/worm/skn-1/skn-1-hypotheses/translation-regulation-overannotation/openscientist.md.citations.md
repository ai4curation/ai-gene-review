# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** skn-1
- **Gene symbol:** skn-1

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** translation-regulation-overannotation
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

C. elegans SKN-1 (P34707) carries an IEA annotation for regulation of translation (GO:0006417), but its established activity is as a bZIP / Nrf-like transcription factor acting on RNA polymerase II target genes (e.g. Phase II detoxification genes). Using protein-domain and sequence analysis (presence or absence of RNA-binding or translation-factor domains), transcription-factor target / regulon and co-expression evidence, and the literature, determine whether SKN-1 DIRECTLY regulates translation (supporting GO:0006417) or whether this IEA annotation is an over-annotation of an indirect, transcription-mediated effect. Consider isoform-specific roles (SKN-1A/B/C) if relevant.

## Term and Decision Context

- Term: regulation of translation (GO:0006417)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: C. elegans SKN-1 (P34707) carries an IEA annotation for regulation of translation (GO:0006417),
  but its established activity is as a bZIP / Nrf-like transcription factor acting on RNA polymerase II
  target genes (e.g. Phase II detoxification genes). Using protein-domain and sequence analysis (presence
  or absence of RNA-binding or translation-factor domains), transcription-factor target / regulon and
  co-expression evidence, and the literature, determine whether SKN-1 DIRECTLY regulates translation (supporting
  GO:0006417) or whether this IEA annotation is an over-annotation of an indirect, transcription-mediated
  effect. Consider isoform-specific roles (SKN-1A/B/C) if relevant.
focus_type: free_text
term_id: GO:0006417
term_label: regulation of translation
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
prompt so the report can be compared against them after the run. Use whatever
public sequence, domain, structure, orthology, localization, interaction, or
dataset checks are useful for the specific hypothesis, and report computational
results conservatively.

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

**Provider:** openscientist
**Generated:** 2026-06-21T22:09:49.839066

1. PMID:27528192
2. PMID:21177963
3. PMID:20700440
4. PMID:30282029
5. PMID:11830574
6. PMID:25688864
7. PMID:22240150
8. PMID:32502151
9. PMID:38466732
10. PMID:9015263
11. PMID:25643626
12. PMID:34407394
13. PMID:15201219
14. PMID:37316035