# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** THEVB
- **Taxon:** Thermosynechococcus vestitus BP-1 (NCBITaxon:197221)
- **Gene directory:** tlr1902
- **Gene symbol:** tlr1902
- **UniProt accession:** Q8DHP3

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-tlr1902-glycan-specificity
- **Source file:** genes/THEVB/tlr1902/tlr1902-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Which glycan Thermosynechococcus elongatus BP-1 Tlr1902 (Q8DHP3) hydrolyses may be predictable from its catalytic architecture. Single analysis only: assign the glycoside hydrolase family of Tlr1902 from its sequence and predicted structure, identify the catalytic acid/base and nucleophile residues and state whether both are present; compare the substrate-binding cleft with structurally characterised members of the same family that act on xylan and on cellulose or other beta-glucans, mapping the aromatic platform residues and any subsite-defining loops, and state which substrate the cleft geometry favours; check whether the genome of this strain encodes the other enzymes a xylan or cellulose utilisation pathway would require, and whether tlr1902 sits in a relevant gene cluster; and report any public transcriptomic evidence for its regulation. State which substrate class is predicted, how confidently, and whether a cyanobacterium with no known access to plant cell-wall polysaccharides makes an endogenous substrate the more likely explanation.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Which glycan Thermosynechococcus elongatus BP-1 Tlr1902 (Q8DHP3) hydrolyses may be predictable
  from its catalytic architecture. Single analysis only: assign the glycoside hydrolase family of Tlr1902
  from its sequence and predicted structure, identify the catalytic acid/base and nucleophile residues
  and state whether both are present; compare the substrate-binding cleft with structurally characterised
  members of the same family that act on xylan and on cellulose or other beta-glucans, mapping the aromatic
  platform residues and any subsite-defining loops, and state which substrate the cleft geometry favours;
  check whether the genome of this strain encodes the other enzymes a xylan or cellulose utilisation pathway
  would require, and whether tlr1902 sits in a relevant gene cluster; and report any public transcriptomic
  evidence for its regulation. State which substrate class is predicted, how confidently, and whether
  a cyanobacterium with no known access to plant cell-wall polysaccharides makes an endogenous substrate
  the more likely explanation.'
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
**Generated:** 2026-11-25T07:51:13.345494

1. PMID:29155107
2. PMID:33103248
3. PMID:14670951
4. PMID:41161445
5. PMID:32732029
6. PMID:30061529
7. PMID:29533991
8. PMID:27723474
9. PMID:27563004
10. PMID:37552253
11. PMID:39688685
12. PMID:29520599
13. PMID:19727881
14. PMID:30535915