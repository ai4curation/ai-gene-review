# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** dyf-6
- **Gene symbol:** dyf-6
- **UniProt accession:** Q0G838

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-dyf6-ift52-interface-conservation
- **Source file:** genes/worm/dyf-6/dyf-6-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Caenorhabditis elegans DYF-6/IFT46 (Q0G838) contacts the IFT-B1 core through its conserved C-terminal IFT46_B_C domain, which retains the IFT52-binding interface resolved in the Chlamydomonas IFT52-IFT46 crystal structure, whereas its N-terminal region has lost the ODA16-binding features used to load outer dynein arms in motile-cilia organisms, consistent with a pure IFT-B scaffold role in nematode sensory cilia. Single analysis only: align DYF-6 with Chlamydomonas, human and other IFT46 orthologs, map the IFT52-contacting residues from the IFT52-IFT46 complex structure onto DYF-6, predict the DYF-6/OSM-6(IFT52) complex with AlphaFold-Multimer and compare interface residues, and score conservation of the N-terminal ODA16-binding region in nematodes versus organisms with motile cilia; state whether DYF-6 is predicted to bind IFT52 directly and whether it retains a cargo-adaptor region.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Caenorhabditis elegans DYF-6/IFT46 (Q0G838) contacts the IFT-B1 core through its conserved
  C-terminal IFT46_B_C domain, which retains the IFT52-binding interface resolved in the Chlamydomonas
  IFT52-IFT46 crystal structure, whereas its N-terminal region has lost the ODA16-binding features used
  to load outer dynein arms in motile-cilia organisms, consistent with a pure IFT-B scaffold role in nematode
  sensory cilia. Single analysis only: align DYF-6 with Chlamydomonas, human and other IFT46 orthologs,
  map the IFT52-contacting residues from the IFT52-IFT46 complex structure onto DYF-6, predict the DYF-6/OSM-6(IFT52)
  complex with AlphaFold-Multimer and compare interface residues, and score conservation of the N-terminal
  ODA16-binding region in nematodes versus organisms with motile cilia; state whether DYF-6 is predicted
  to bind IFT52 directly and whether it retains a cargo-adaptor region.'
focus_type: free_text
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
**Generated:** 2026-11-23T23:38:42.526771

1. PMID:25349261
2. PMID:28298440
3. PMID:39880089
4. PMID:28302912
5. PMID:16648645
6. PMID:28479320
7. PMID:20435895
8. PMID:18852297
9. PMID:36354106
10. PMID:28701346
11. PMID:32239748
12. PMID:37363725
13. PMID:38517430
14. PMID:29915351
15. PMID:30133350
16. PMID:35674692
17. PMID:39309499