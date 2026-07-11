# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** CLCN7
- **Gene symbol:** CLCN7

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** topology-transepithelial-overannotation
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

Human CLCN7 (ClC-7) carries an annotation for transepithelial chloride transport (GO:0030321), but it is reported to be an intracellular endolysosomal electrogenic 2Cl-/1H+ antiporter residing in the lysosomal membrane and the osteoclast ruffled border rather than in the epithelial plasma membrane. Using membrane-topology prediction (e.g. DeepTMHMM/Phobius), analysis of subcellular-targeting / lysosomal sorting signals, and subcellular-localization evidence, determine whether GO:0030321 (transepithelial chloride transport) is justified or is an over-annotation, and what the best-supported cellular localization and transport role of ClC-7 actually are.

## Term and Decision Context

- Term: transepithelial chloride transport (GO:0030321)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human CLCN7 (ClC-7) carries an annotation for transepithelial chloride transport (GO:0030321),
  but it is reported to be an intracellular endolysosomal electrogenic 2Cl-/1H+ antiporter residing in
  the lysosomal membrane and the osteoclast ruffled border rather than in the epithelial plasma membrane.
  Using membrane-topology prediction (e.g. DeepTMHMM/Phobius), analysis of subcellular-targeting / lysosomal
  sorting signals, and subcellular-localization evidence, determine whether GO:0030321 (transepithelial
  chloride transport) is justified or is an over-annotation, and what the best-supported cellular localization
  and transport role of ClC-7 actually are.
focus_type: free_text
term_id: GO:0030321
term_label: transepithelial chloride transport
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
**Generated:** 2026-06-21T22:12:17.424745

1. PMID:32851177
2. PMID:17897319
3. PMID:18449189
4. PMID:21527911
5. PMID:15706348
6. PMID:16525474
7. PMID:17110406
8. PMID:20817731
9. PMID:32749217
10. PMID:38294065
11. PMID:26346547
12. PMID:25663454
13. PMID:24103576
14. PMID:17477025
15. PMID:11053039
16. PMID:20430974
17. PMID:33495814
18. PMID:12111250
19. PMID:16179405
20. PMID:24159188
21. PMID:23983121