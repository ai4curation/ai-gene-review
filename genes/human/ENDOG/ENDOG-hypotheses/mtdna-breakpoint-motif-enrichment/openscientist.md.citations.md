# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** ENDOG
- **Gene symbol:** ENDOG
- **UniProt accession:** Q14249

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** mtdna-breakpoint-motif-enrichment
- **Source file:** genes/human/ENDOG/ENDOG-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ENDOG's cleavage-site preferences explain where mitochondrial DNA breakpoints fall: breakpoints of nuclear mitochondrial insertions (NUMTs) and of mtDNA deletions are enriched at G-quadruplex-forming and C-rich motifs in the mitochondrial genome, relative to position- and composition-matched control sites.

## Term and Decision Context

- This must be a computational analysis on sequence and coordinate data, not a literature review. Compute, do not cite: scan the human mitochondrial reference sequence (rCRS, NC_012920.1) for G-quadruplex propensity (e.g. G4Hunter) and for the C-rich motifs ENDOG is reported to cleave, then test whether published mtDNA breakpoint coordinates fall at those motifs more often than position- and base-composition-matched control sites. Report the test used, effect size and p-value.
- Breakpoint coordinate sources to use if obtainable: the NUMT catalogue of 1637 NUMTs across 66083 genomes (PMID:36198798, supplementary tables give mtDNA coordinates); MITOMAP's mtDNA deletion breakpoint table; and the common 9 bp deletion hotspot at mtDNA 8271-8281. Per-individual NUMT genotypes are UK Biobank controlled-access and are NOT needed: this tests where breakpoints sit in the mtDNA sequence, not who carries them.
- Biological background for the motifs, already established, do not re-derive: human ENDOG prefers oxidatively damaged, nicked and gapped DNA (PMID:41854021); it binds G-quadruplex structures at the 9 bp deletion hotspot and induces breaks there (PMID:36394256); in mouse it cleaves C-rich motifs in a mitochondrial transcript (PMID:39752519); and yeast EndoG limits transfer of long mtDNA to the nucleus (PMID:39227600).
- State clearly if the breakpoint coordinate data cannot be obtained programmatically, and in that case report the motif scan alone rather than substituting a literature summary. A negative result, no enrichment over matched controls, is a valid and useful outcome.

## Reference Context

- PMID:36198798
- PMID:36394256
- PMID:39752519
- PMID:41854021
- PMID:39227600

## Source Context YAML

```yaml
hypothesis: 'Human ENDOG''s cleavage-site preferences explain where mitochondrial DNA breakpoints fall:
  breakpoints of nuclear mitochondrial insertions (NUMTs) and of mtDNA deletions are enriched at G-quadruplex-forming
  and C-rich motifs in the mitochondrial genome, relative to position- and composition-matched control
  sites.'
focus_type: free_text
context:
- 'This must be a computational analysis on sequence and coordinate data, not a literature review. Compute,
  do not cite: scan the human mitochondrial reference sequence (rCRS, NC_012920.1) for G-quadruplex propensity
  (e.g. G4Hunter) and for the C-rich motifs ENDOG is reported to cleave, then test whether published mtDNA
  breakpoint coordinates fall at those motifs more often than position- and base-composition-matched control
  sites. Report the test used, effect size and p-value.'
- 'Breakpoint coordinate sources to use if obtainable: the NUMT catalogue of 1637 NUMTs across 66083 genomes
  (PMID:36198798, supplementary tables give mtDNA coordinates); MITOMAP''s mtDNA deletion breakpoint table;
  and the common 9 bp deletion hotspot at mtDNA 8271-8281. Per-individual NUMT genotypes are UK Biobank
  controlled-access and are NOT needed: this tests where breakpoints sit in the mtDNA sequence, not who
  carries them.'
- 'Biological background for the motifs, already established, do not re-derive: human ENDOG prefers oxidatively
  damaged, nicked and gapped DNA (PMID:41854021); it binds G-quadruplex structures at the 9 bp deletion
  hotspot and induces breaks there (PMID:36394256); in mouse it cleaves C-rich motifs in a mitochondrial
  transcript (PMID:39752519); and yeast EndoG limits transfer of long mtDNA to the nucleus (PMID:39227600).'
- State clearly if the breakpoint coordinate data cannot be obtained programmatically, and in that case
  report the motif scan alone rather than substituting a literature summary. A negative result, no enrichment
  over matched controls, is a valid and useful outcome.
reference_id:
- PMID:36198798
- PMID:36394256
- PMID:39752519
- PMID:41854021
- PMID:39227600
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
**Generated:** 2026-10-26T21:15:48.028332

1. PMID:36198798
2. PMID:36394256
3. PMID:39752519
4. PMID:41854021
5. PMID:39227600