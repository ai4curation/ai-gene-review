# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** HAECO
- **Taxon:** Haemonchus contortus (NCBITaxon:6289)
- **Gene directory:** Q25022
- **Gene symbol:** tub12-16
- **UniProt accession:** Q25022

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-q25022-locus-identity
- **Source file:** genes/HAECO/Q25022/Q25022-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Which modern Haemonchus contortus beta-tubulin locus the beta 12-16 cDNA corresponds to may be decidable by sequence comparison against the current genome assemblies. That Q25022 is the full-length beta 12-16 cDNA of Geary et al., that an ungapped alignment keeps it distinct from both the later A2TF56 resistant-isolate sequence and the older tub8-9 cDNA, that it is 448 residues with the Tubulin/FtsZ GTPase and C-terminal domains, and that it carries Phe167, Glu198 and Phe200 at the three canonical benzimidazole-resistance positions, is already recorded, so do not re-derive any of it. Single analysis only: list the beta-tubulin genes annotated in the current H. contortus reference assemblies, giving each one's gene identifier, protein length and the isotype name used for it in the anthelmintic-resistance literature, and quote the statements that establish which locus the field calls isotype 1 and which isotype 2; align Q25022 to each predicted protein and report percent identity and the number of differences for every one, so that the best match is visible as a margin over the runner-up rather than asserted; state what each candidate locus carries at positions 167, 198 and 200, since the resistance-position state is the property the gap couples to drug selection, and say whether the best-matching locus is the one under benzimidazole selection; and state whether the differences between Q25022 and its best match are consistent with isolate polymorphism or require it to be a separate locus or paralog, giving the number and kind of substitutions. State which locus and isotype class Q25022 corresponds to, and say plainly if the assemblies cannot distinguish two candidates.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Which modern Haemonchus contortus beta-tubulin locus the beta 12-16 cDNA corresponds to may
  be decidable by sequence comparison against the current genome assemblies. That Q25022 is the full-length
  beta 12-16 cDNA of Geary et al., that an ungapped alignment keeps it distinct from both the later A2TF56
  resistant-isolate sequence and the older tub8-9 cDNA, that it is 448 residues with the Tubulin/FtsZ
  GTPase and C-terminal domains, and that it carries Phe167, Glu198 and Phe200 at the three canonical
  benzimidazole-resistance positions, is already recorded, so do not re-derive any of it. Single analysis
  only: list the beta-tubulin genes annotated in the current H. contortus reference assemblies, giving
  each one''s gene identifier, protein length and the isotype name used for it in the anthelmintic-resistance
  literature, and quote the statements that establish which locus the field calls isotype 1 and which
  isotype 2; align Q25022 to each predicted protein and report percent identity and the number of differences
  for every one, so that the best match is visible as a margin over the runner-up rather than asserted;
  state what each candidate locus carries at positions 167, 198 and 200, since the resistance-position
  state is the property the gap couples to drug selection, and say whether the best-matching locus is
  the one under benzimidazole selection; and state whether the differences between Q25022 and its best
  match are consistent with isolate polymorphism or require it to be a separate locus or paralog, giving
  the number and kind of substitutions. State which locus and isotype class Q25022 corresponds to, and
  say plainly if the assemblies cannot distinguish two candidates.'
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
**Generated:** 2026-11-26T03:26:03.085407

1. PMID:36113620
2. PMID:1741017
3. PMID:42302569
4. PMID:42931220
5. PMID:42696219
6. PMID:42357801
7. PMID:41064838
8. PMID:40245470
9. PMID:39671856
10. PMID:39260013
11. PMID:39141122
12. PMID:37536387
13. PMID:37321794
14. PMID:37165895
15. PMID:36690654
16. PMID:42431032