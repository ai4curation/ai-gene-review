# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** KLB
- **Gene symbol:** KLB
- **UniProt accession:** Q86Z14

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-klb-gh1-residual-glycoside-site
- **Source file:** genes/human/KLB/KLB-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Neither glycoside-hydrolase-like domain of human beta-Klotho (KLB, Q86Z14) retains a GH1 active site capable of any glycoside chemistry: in each domain at least one of the two catalytic glutamates (acid/base and nucleophile) and the conserved glycone-binding residues of active GH1 beta-glucosidases are substituted, and in the D1 domain the former substrate pocket is repurposed as the binding site for the FGF19/FGF21 C-terminal tail seen in crystal structures of KLB with FGF21. Single analysis only: align both KLB GH-like domains with active GH1 enzymes (e.g. human cytosolic beta-glucosidase GBA3 and lactase-phlorizin hydrolase domains) and with alpha-Klotho, map the two catalytic glutamates and glycone-binding residues onto each domain using the KLB crystal structure, measure whether a sugar-sized pocket remains in each domain and what occupies it, score these positions across vertebrate KLB orthologs, and state whether either domain is predicted to retain residual glycosidase or sugar-binding capacity.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Neither glycoside-hydrolase-like domain of human beta-Klotho (KLB, Q86Z14) retains a GH1
  active site capable of any glycoside chemistry: in each domain at least one of the two catalytic glutamates
  (acid/base and nucleophile) and the conserved glycone-binding residues of active GH1 beta-glucosidases
  are substituted, and in the D1 domain the former substrate pocket is repurposed as the binding site
  for the FGF19/FGF21 C-terminal tail seen in crystal structures of KLB with FGF21. Single analysis only:
  align both KLB GH-like domains with active GH1 enzymes (e.g. human cytosolic beta-glucosidase GBA3 and
  lactase-phlorizin hydrolase domains) and with alpha-Klotho, map the two catalytic glutamates and glycone-binding
  residues onto each domain using the KLB crystal structure, measure whether a sugar-sized pocket remains
  in each domain and what occupies it, score these positions across vertebrate KLB orthologs, and state
  whether either domain is predicted to retain residual glycosidase or sugar-binding capacity.'
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
**Generated:** 2026-11-24T00:18:25.149842

1. PMID:29342138
2. PMID:17627937
3. PMID:18829467
4. PMID:19117008
5. PMID:19059246
6. PMID:9363890
7. PMID:30944224
8. PMID:29342135
9. PMID:30038432
10. PMID:25378396
11. PMID:23970553
12. PMID:24434184
13. PMID:19730882
14. PMID:23652548
15. PMID:27622885
16. PMID:28614116
17. PMID:27469036