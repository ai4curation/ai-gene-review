# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** Hsp22
- **Gene symbol:** Hsp22
- **UniProt accession:** P02515

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** conditional-nuclear-localization
- **Source file:** genes/DROME/Hsp22/Hsp22-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Assess conditional nuclear localization of Drosophila melanogaster Hsp22/P02515 separately from its predominant mitochondrial localization. Actual PTHR45640 v19 tree places exact target leaf PTN000163333 below nucleus IBD PTN000897708 (no recovered loss on target path); family size or donor count is not evidence of failure. Full primary10896659 (author ResearchGate PDF/text) verifies endogenous S2 mitochondrial colocalization after35C1h plus2hrecovery, specific antibodies, and matrix fractionation/protease protection in transfected hamster cells; N-terminal import-mutant mapping does not itself prove universal nuclear exclusion. Earlier primary6772504 DOI10.1016/0012-1606(80)90320-6 publisher abstract explicitly reports22kDa as well as23/26/27kDa proteins in nuclear/chromatin/nucleolar preparations after37C heat shock; retrieve full18-page paper and examine biochemical band identity, fraction purity, EM autoradiography specificity and later reassessments. Is apparent Hsp22 nuclear signal real, transient, or contamination/misidentification? Distinguish absence of evidence from demonstrated absence. Compare but do not conflate Hsp23/P02516: full6801431 UNIGE PDF has salivary gland nuclear IF after37C1h, preimmune control and antibody IP specificity; full1986 DOI10.1139/g86-152 author ResearchGate text has Kc nucleolar IF but explicitly cannot exclude Hsp26/Hsp27 antibody cross-reaction. Those data currently support contextual Hsp23 localization and do not demonstrate Hsp22 import. PMID3109982 whole-insect soluble/particulate fractionation is not automatically nuclear localization. Mammalian HSPB8/Hsp22 and plant Hsp22 are distinct targets; do not transfer their nuclear results by shared nickname. Review later native fly targeting, proteomic and stress time-course evidence; provide exact constructs, assays, source passages and calibrated conclusion about Hsp22 nucleus IBA. Do not repeat established holdase/refolding or general longevity research.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Assess conditional nuclear localization of Drosophila melanogaster Hsp22/P02515 separately
  from its predominant mitochondrial localization. Actual PTHR45640 v19 tree places exact target leaf
  PTN000163333 below nucleus IBD PTN000897708 (no recovered loss on target path); family size or donor
  count is not evidence of failure. Full primary10896659 (author ResearchGate PDF/text) verifies endogenous
  S2 mitochondrial colocalization after35C1h plus2hrecovery, specific antibodies, and matrix fractionation/protease
  protection in transfected hamster cells; N-terminal import-mutant mapping does not itself prove universal
  nuclear exclusion. Earlier primary6772504 DOI10.1016/0012-1606(80)90320-6 publisher abstract explicitly
  reports22kDa as well as23/26/27kDa proteins in nuclear/chromatin/nucleolar preparations after37C heat
  shock; retrieve full18-page paper and examine biochemical band identity, fraction purity, EM autoradiography
  specificity and later reassessments. Is apparent Hsp22 nuclear signal real, transient, or contamination/misidentification?
  Distinguish absence of evidence from demonstrated absence. Compare but do not conflate Hsp23/P02516:
  full6801431 UNIGE PDF has salivary gland nuclear IF after37C1h, preimmune control and antibody IP specificity;
  full1986 DOI10.1139/g86-152 author ResearchGate text has Kc nucleolar IF but explicitly cannot exclude
  Hsp26/Hsp27 antibody cross-reaction. Those data currently support contextual Hsp23 localization and
  do not demonstrate Hsp22 import. PMID3109982 whole-insect soluble/particulate fractionation is not automatically
  nuclear localization. Mammalian HSPB8/Hsp22 and plant Hsp22 are distinct targets; do not transfer their
  nuclear results by shared nickname. Review later native fly targeting, proteomic and stress time-course
  evidence; provide exact constructs, assays, source passages and calibrated conclusion about Hsp22 nucleus
  IBA. Do not repeat established holdase/refolding or general longevity research.'
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
**Generated:** 2026-09-21T05:16:23.915814

1. PMID:10896659
2. PMID:19948727
3. PMID:19420297
4. PMID:15491684
5. PMID:26155908
6. PMID:3109982