# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** XENLA
- **Taxon:** Xenopus laevis (NCBITaxon:8355)
- **Gene directory:** zic1
- **Gene symbol:** zic1
- **UniProt accession:** O73689

## Focus

- **Focus type:** proposed_go_term
- **Hypothesis slug:** border-pax3-zic-coexpression-scrna
- **Source file:** genes/XENLA/zic1/zic1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

At the Xenopus neural plate border, zic1 and pax3 are co-expressed in the same cells, and that double-positive population is the one that progresses to neural crest (snai2/sox10/foxd3-positive), whereas zic1-only cells sit in the preplacodal/anterior neural domain; zic2, zic3, zic4 and zic5 are also expressed in the pax3+zic1+ border population. Test this with one analysis: in the public X. tropicalis single-cell time course of Briggs et al. 2018 (PMID:29700227), identify neural plate border and early neural crest cells and quantify per-cell co-expression of pax3, zic1-5 and crest specifiers across stages. Report the result even if inconclusive.

## Term and Decision Context

- Term: neural plate border formation (proposed new term) (no id)

## Reference Context

- PMID:29700227
- PMID:15843410
- PMID:17409353

## Source Context YAML

```yaml
hypothesis: 'At the Xenopus neural plate border, zic1 and pax3 are co-expressed in the same cells, and
  that double-positive population is the one that progresses to neural crest (snai2/sox10/foxd3-positive),
  whereas zic1-only cells sit in the preplacodal/anterior neural domain; zic2, zic3, zic4 and zic5 are
  also expressed in the pax3+zic1+ border population. Test this with one analysis: in the public X. tropicalis
  single-cell time course of Briggs et al. 2018 (PMID:29700227), identify neural plate border and early
  neural crest cells and quantify per-cell co-expression of pax3, zic1-5 and crest specifiers across stages.
  Report the result even if inconclusive.'
focus_type: proposed_go_term
term_label: neural plate border formation (proposed new term)
context: []
reference_id:
- PMID:29700227
- PMID:15843410
- PMID:17409353
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
**Generated:** 2026-10-09T18:06:27.251271

1. PMID:15843410
2. PMID:17409353
3. PMID:41718037
4. PMID:41256729
5. PMID:30012125
6. PMID:29852131
7. PMID:34638777
8. PMID:40939754
9. PMID:32891623
10. PMID:32640092
11. PMID:16871625
12. PMID:9655809
13. PMID:29442320
14. PMID:29700227