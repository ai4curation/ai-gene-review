# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** A3GALT2
- **Gene symbol:** A3GALT2
- **UniProt accession:** U3KPV4

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-a3galt2-catalytic-integrity
- **Source file:** genes/human/A3GALT2/A3GALT2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether human A3GALT2 (U3KPV4) retains a competent glycosyltransferase active site, and whether the reported very weak iGb3 synthase activity is the expected output of an intact enzyme or of a degraded one, may be assessable from sequence. That overexpression of a reconstructed coding sequence gave MS-detectable iGb3 and iGb4 characterised as very weak, and that an earlier human catalytic-domain chimera was negative, is already recorded, so do not re-derive those experiments. Single analysis only: assign the GT family and the closest characterised relative, and state residue by residue whether the catalytic and donor-binding positions of that family are intact in human A3GALT2, naming the DXD or equivalent metal-binding motif, the catalytic base and the UDP-galactose contacts with positions in both proteins, so that any substitution is auditable; compare the human sequence with the functional rat, mouse and other mammalian A3GALT2 orthologs across those same positions and report every position where human differs, which is the test that distinguishes a pseudogene-like decay from an intact gene; state whether human A3GALT2 shows the signatures of pseudogenisation, a disrupted reading frame, a lost splice site, or relaxed selection measured against its functional orthologs, giving the measurement; and state whether the predicted type-II signal anchor is intact in the human sequence, since a lost anchor would mislocalise an otherwise competent enzyme and would itself explain weak activity. State whether human A3GALT2 is predicted to be catalytically competent, and say plainly if sequence cannot distinguish an intact weak enzyme from a decaying one.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether human A3GALT2 (U3KPV4) retains a competent glycosyltransferase active site, and whether
  the reported very weak iGb3 synthase activity is the expected output of an intact enzyme or of a degraded
  one, may be assessable from sequence. That overexpression of a reconstructed coding sequence gave MS-detectable
  iGb3 and iGb4 characterised as very weak, and that an earlier human catalytic-domain chimera was negative,
  is already recorded, so do not re-derive those experiments. Single analysis only: assign the GT family
  and the closest characterised relative, and state residue by residue whether the catalytic and donor-binding
  positions of that family are intact in human A3GALT2, naming the DXD or equivalent metal-binding motif,
  the catalytic base and the UDP-galactose contacts with positions in both proteins, so that any substitution
  is auditable; compare the human sequence with the functional rat, mouse and other mammalian A3GALT2
  orthologs across those same positions and report every position where human differs, which is the test
  that distinguishes a pseudogene-like decay from an intact gene; state whether human A3GALT2 shows the
  signatures of pseudogenisation, a disrupted reading frame, a lost splice site, or relaxed selection
  measured against its functional orthologs, giving the measurement; and state whether the predicted type-II
  signal anchor is intact in the human sequence, since a lost anchor would mislocalise an otherwise competent
  enzyme and would itself explain weak activity. State whether human A3GALT2 is predicted to be catalytically
  competent, and say plainly if sequence cannot distinguish an intact weak enzyme from a decaying one.'
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
**Generated:** 2026-11-26T00:38:43.942485

1. PMID:18630988
2. PMID:10854427
3. PMID:18651752
4. PMID:12011052
5. PMID:15229192
6. PMID:14621997
7. PMID:12499401
8. PMID:22520506
9. PMID:17493636
10. PMID:18192272
11. PMID:17298992
12. PMID:17206613
13. PMID:16456004
14. PMID:17372206
15. PMID:15539565
16. PMID:23280365
17. PMID:22742596
18. PMID:12626403