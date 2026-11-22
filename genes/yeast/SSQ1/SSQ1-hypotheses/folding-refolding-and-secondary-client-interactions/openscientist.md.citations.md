# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** SSQ1
- **Gene symbol:** SSQ1
- **UniProt accession:** Q05931

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** folding-refolding-and-secondary-client-interactions
- **Source file:** genes/yeast/SSQ1/SSQ1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Ssq1 (Q05931; YLR369W; Ssc2p) retains protein folding/refolding or unfolded-protein holdase activity alongside its established ATP-dependent Isu/Grx5 Fe-S cluster transfer role. Separately, Ssq1 has a biologically meaningful interaction with Nop1 (P15646). Assess each claim independently against actual GO definitions, target primary assays and experimental context. Actual PTHR19375 treeinfo target path contains folding/refolding IBD PTN000452648, cytoplasm node PTN002321897 and mitochondrial/ISC node PTN000452554, terminating at PTN000452606; no NOT/IRD assertion lies on that path. Do not equate donor count, predominant matrix location or specialist status with universal loss. Full PMID12756240 Fig8 establishes lack of Mdj1 stimulation of Ssq1 ATPase and Isu engagement, not a general refolding assay; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2003_Dutkiewicz_JBC.pdf . PMID20224575 introduction infers folding loss from partner specificity. PMID11601843 abstract explicitly reports ATP-regulated unfolded-substrate binding; retrieve full assays before deciding folding versus binding. Crucial full PMID16431909 Fig4C shows Ssq1 protects guanidine-denatured rhodanese against aggregation, strongest without nucleotide or with ADP, by light scattering; not restored rhodanese enzymatic activity. Fig4A/B shows ATP/Jac1-independent protection of purified Nfs1 activity, while Fig4D shows Ssq1-depleted mitochondrial lysate Nfs1 activity unchanged; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2006_Dutkiewicz_JBC.pdf . Full PMID23615440 Fig3D detects in-vitro Cia1 binding displaced by LPPVK, distinct from nonoverlapping Grx5 binding; its folding-language interpretation is not itself a refolding assay. Full PMID10779357 Discussion reports no Yfh1 aggregation/protease-sensitivity difference in wild-type versus ssq1 deletion despite processing delay; this specific negative does not prove no capacity on other clients. Distinguish native folding, reactivation of misfolded substrate, aggregation prevention, ATP-driven scaffold remodeling and cargo delivery requirements of GO0140309. Identify whether any more precise MF represents established Ssq1 action without inventing a new foldase claim. For Nop1, original IPI rows cite16554755 and19536198. Full19536198 uses TAP-MS whole-cell complexes and spoke inference, shares methods/data lineage with16554755, and includes Ssc2 as an alias; inspect exact Nop1-YLR369W supplement entries and independence, target localization or functional assays. Native matrix residence alone neither disproves the interaction nor proves a nuclear pool. Report any unresolved source-access limits and do not infer direct binary binding or target refolding from AP-MS alone.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae Ssq1 (Q05931; YLR369W; Ssc2p) retains protein folding/refolding or
  unfolded-protein holdase activity alongside its established ATP-dependent Isu/Grx5 Fe-S cluster transfer
  role. Separately, Ssq1 has a biologically meaningful interaction with Nop1 (P15646). Assess each claim
  independently against actual GO definitions, target primary assays and experimental context. Actual
  PTHR19375 treeinfo target path contains folding/refolding IBD PTN000452648, cytoplasm node PTN002321897
  and mitochondrial/ISC node PTN000452554, terminating at PTN000452606; no NOT/IRD assertion lies on that
  path. Do not equate donor count, predominant matrix location or specialist status with universal loss.
  Full PMID12756240 Fig8 establishes lack of Mdj1 stimulation of Ssq1 ATPase and Isu engagement, not a
  general refolding assay; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2003_Dutkiewicz_JBC.pdf
  . PMID20224575 introduction infers folding loss from partner specificity. PMID11601843 abstract explicitly
  reports ATP-regulated unfolded-substrate binding; retrieve full assays before deciding folding versus
  binding. Crucial full PMID16431909 Fig4C shows Ssq1 protects guanidine-denatured rhodanese against aggregation,
  strongest without nucleotide or with ADP, by light scattering; not restored rhodanese enzymatic activity.
  Fig4A/B shows ATP/Jac1-independent protection of purified Nfs1 activity, while Fig4D shows Ssq1-depleted
  mitochondrial lysate Nfs1 activity unchanged; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2006_Dutkiewicz_JBC.pdf
  . Full PMID23615440 Fig3D detects in-vitro Cia1 binding displaced by LPPVK, distinct from nonoverlapping
  Grx5 binding; its folding-language interpretation is not itself a refolding assay. Full PMID10779357
  Discussion reports no Yfh1 aggregation/protease-sensitivity difference in wild-type versus ssq1 deletion
  despite processing delay; this specific negative does not prove no capacity on other clients. Distinguish
  native folding, reactivation of misfolded substrate, aggregation prevention, ATP-driven scaffold remodeling
  and cargo delivery requirements of GO0140309. Identify whether any more precise MF represents established
  Ssq1 action without inventing a new foldase claim. For Nop1, original IPI rows cite16554755 and19536198.
  Full19536198 uses TAP-MS whole-cell complexes and spoke inference, shares methods/data lineage with16554755,
  and includes Ssc2 as an alias; inspect exact Nop1-YLR369W supplement entries and independence, target
  localization or functional assays. Native matrix residence alone neither disproves the interaction nor
  proves a nuclear pool. Report any unresolved source-access limits and do not infer direct binary binding
  or target refolding from AP-MS alone.
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
**Generated:** 2026-09-21T03:07:32.706864

1. PMID:11601843
2. PMID:16431909
3. PMID:16554755
4. PMID:19536198
5. PMID:23615440
6. PMID:20224575
7. PMID:10779357
8. PMID:12756240