# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae S288C (NCBITaxon:559292)
- **Gene directory:** YET2
- **Gene symbol:** YET2
- **UniProt accession:** Q04210

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-yet2-interface-exclusion
- **Source file:** genes/yeast/YET2/YET2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Why Yet2p (Q04210) does not stably join the Yet1p-Yet3p complex may be readable from its interface residues. That Yet2p is an ER polytopic BCAP29/BCAP31-family protein with three transmembrane helices and a C-terminal di-lysine retrieval motif, that it is non-essential and low-abundance, and that it associates only minimally with the Yet1p-Yet3p complex and the translocation machinery, is already established, so do not re-derive it. Single analysis only: align Yet1p, Yet2p and Yet3p with the human BAP29 and BAP31 proteins and across fungi, and map onto predicted structures the coiled-coil and transmembrane positions that mediate BAP29-BAP31 heterodimerisation in the characterised human pair, naming the source for those positions; state residue by residue which of those interface positions Yet2p retains and which it has lost or substituted, and whether the substitutions are conservative or charge-reversing, comparing against Yet1p and Yet3p at the same positions as the internal control; assess whether Yet2p is predicted to homodimerise instead, or to be interface-dead; and check whether the interface positions Yet2p lacks are the ones conserved across fungi. State whether the architecture explains the exclusion from the complex, and say plainly if interface prediction cannot distinguish a genuinely altered interface from an ordinary sequence difference.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Why Yet2p (Q04210) does not stably join the Yet1p-Yet3p complex may be readable from its
  interface residues. That Yet2p is an ER polytopic BCAP29/BCAP31-family protein with three transmembrane
  helices and a C-terminal di-lysine retrieval motif, that it is non-essential and low-abundance, and
  that it associates only minimally with the Yet1p-Yet3p complex and the translocation machinery, is already
  established, so do not re-derive it. Single analysis only: align Yet1p, Yet2p and Yet3p with the human
  BAP29 and BAP31 proteins and across fungi, and map onto predicted structures the coiled-coil and transmembrane
  positions that mediate BAP29-BAP31 heterodimerisation in the characterised human pair, naming the source
  for those positions; state residue by residue which of those interface positions Yet2p retains and which
  it has lost or substituted, and whether the substitutions are conservative or charge-reversing, comparing
  against Yet1p and Yet3p at the same positions as the internal control; assess whether Yet2p is predicted
  to homodimerise instead, or to be interface-dead; and check whether the interface positions Yet2p lacks
  are the ones conserved across fungi. State whether the architecture explains the exclusion from the
  complex, and say plainly if interface prediction cannot distinguish a genuinely altered interface from
  an ordinary sequence difference.'
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
**Generated:** 2026-11-25T19:30:05.176796

1. PMID:23967155
2. PMID:8612576
3. PMID:12886015
4. PMID:20378542
5. PMID:43069579
6. PMID:21372176
7. PMID:38766039
8. PMID:41432297
9. PMID:41330486