# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ASPFU
- **Taxon:** Aspergillus fumigatus Af293 (NCBITaxon:330879)
- **Gene directory:** hmg2
- **Gene symbol:** hmg2
- **UniProt accession:** Q4WSY2

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-hmg2-paralog-contribution
- **Source file:** genes/ASPFU/hmg2/hmg2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the weakly expressed hmg2 paralogue contributes measurably to mevalonate flux, ergosterol production or siderophore output in Aspergillus fumigatus is the question, and a companion run on this organism has already shown how this kind of question goes wrong. Already recorded and not to be re-derived: that hmg2 encodes the second HMG-CoA reductase, a polytopic endoplasmic-reticulum membrane enzyme predicted to use NADPH to reduce HMG-CoA to mevalonate, that this reaction supplies ergosterol, broader isoprenoid and triacetylfusarinine C biosynthesis, that hmg2 is expressed much more weakly than hmg1 under tested conditions, that clinical-isolate data do not establish Hmg2 variation as a major triazole-resistance mechanism, and that the available perturbation data directly test hmg1 and do not resolve whether hmg2 contributes under any condition. Carry forward and hold the distinction it forced: a run on the duplicated HMG-CoA synthases of this organism found that three independent lines, clade retention, sub-telomeric chromosomal address and codon adaptation, establish one paralogue as principal and the other as accessory, and then refused to convert that rank asymmetry into a division of labour, because codon bias indexes average translation and chromosomal address predicts dispensability while neither says which reaction a protein performs when the reaction is identical in both. Weak expression is a statement of rank. Do not present it as a statement of function. Single analysis only. First establish catalytic and topological integrity: report whether Hmg2 carries the complete class I HMG-CoA reductase catalytic set and the expected membrane topology, naming the positions in this protein and confirming each against the local UniProt record, and say whether anything is missing or degenerate, since a decayed copy would answer the question outright. Second, treat the expression claim quantitatively rather than qualitatively: state the datasets that resolve both paralogues, the conditions they cover, and the actual ratio, and say explicitly whether any tested condition inverts or narrows it, since a condition-specific inversion is the one expression result that would bear on function. Note whether iron starvation and hypoxia, the conditions under which the siderophore and ergosterol branches are most stressed, are among those covered, and say plainly if they are not. Third, state what perturbation evidence exists for either paralogue in this organism, and whether hmg1 perturbation is lethal or merely impairing, because a non-lethal hmg1 phenotype would imply residual flux that hmg2 could be supplying, while a lethal one would leave the question open. Then give the verdict with the strength it deserves, and if the record cannot establish a measurable contribution, say that plainly and name the experiment that would. Do not infer a branch-specific role from expression level or from pathway logic, and do not propose a GO annotation assigning a branch of isoprenoid or siderophore biosynthesis to this paralogue.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the weakly expressed hmg2 paralogue contributes measurably to mevalonate flux, ergosterol
  production or siderophore output in Aspergillus fumigatus is the question, and a companion run on this
  organism has already shown how this kind of question goes wrong. Already recorded and not to be re-derived:
  that hmg2 encodes the second HMG-CoA reductase, a polytopic endoplasmic-reticulum membrane enzyme predicted
  to use NADPH to reduce HMG-CoA to mevalonate, that this reaction supplies ergosterol, broader isoprenoid
  and triacetylfusarinine C biosynthesis, that hmg2 is expressed much more weakly than hmg1 under tested
  conditions, that clinical-isolate data do not establish Hmg2 variation as a major triazole-resistance
  mechanism, and that the available perturbation data directly test hmg1 and do not resolve whether hmg2
  contributes under any condition. Carry forward and hold the distinction it forced: a run on the duplicated
  HMG-CoA synthases of this organism found that three independent lines, clade retention, sub-telomeric
  chromosomal address and codon adaptation, establish one paralogue as principal and the other as accessory,
  and then refused to convert that rank asymmetry into a division of labour, because codon bias indexes
  average translation and chromosomal address predicts dispensability while neither says which reaction
  a protein performs when the reaction is identical in both. Weak expression is a statement of rank. Do
  not present it as a statement of function. Single analysis only. First establish catalytic and topological
  integrity: report whether Hmg2 carries the complete class I HMG-CoA reductase catalytic set and the
  expected membrane topology, naming the positions in this protein and confirming each against the local
  UniProt record, and say whether anything is missing or degenerate, since a decayed copy would answer
  the question outright. Second, treat the expression claim quantitatively rather than qualitatively:
  state the datasets that resolve both paralogues, the conditions they cover, and the actual ratio, and
  say explicitly whether any tested condition inverts or narrows it, since a condition-specific inversion
  is the one expression result that would bear on function. Note whether iron starvation and hypoxia,
  the conditions under which the siderophore and ergosterol branches are most stressed, are among those
  covered, and say plainly if they are not. Third, state what perturbation evidence exists for either
  paralogue in this organism, and whether hmg1 perturbation is lethal or merely impairing, because a non-lethal
  hmg1 phenotype would imply residual flux that hmg2 could be supplying, while a lethal one would leave
  the question open. Then give the verdict with the strength it deserves, and if the record cannot establish
  a measurable contribution, say that plainly and name the experiment that would. Do not infer a branch-specific
  role from expression level or from pathway logic, and do not propose a GO annotation assigning a branch
  of isoprenoid or siderophore biosynthesis to this paralogue.'
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
**Generated:** 2026-11-26T19:45:05.887317

1. PMID:22106303
2. PMID:42908572
3. PMID:33081232
4. PMID:19883779
5. PMID:18757806
6. PMID:32670238
7. PMID:31866965
8. PMID:16110826