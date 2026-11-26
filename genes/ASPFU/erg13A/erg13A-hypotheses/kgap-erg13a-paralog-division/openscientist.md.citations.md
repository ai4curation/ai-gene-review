# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ASPFU
- **Taxon:** Aspergillus fumigatus Af293 (NCBITaxon:330879)
- **Gene directory:** erg13A
- **Gene symbol:** erg13A
- **UniProt accession:** Q4WBQ3

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-erg13a-paralog-division
- **Source file:** genes/ASPFU/erg13A/erg13A-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the respective in-vivo contributions of the two Aspergillus fumigatus HMG-CoA synthase paralogues can be distinguished is the question, and a companion run on this organism has already removed one way the division of labour might have worked. Already recorded and not to be re-derived: that both Af293 proteins sit in PANTHER PTHR43323:SF2, that UniProt attributes the HMG-CoA synthase reaction to both, and that the available evidence does not distinguish their expression, activity or pathway flux. Carry forward and do not re-derive: a run on the mitochondrial thiolase erg10A established that neither paralogue is mitochondrial, both carrying N-terminal net charges inside a cytosolic control range against a mitochondrial control median of plus five, and that this organism therefore has no mitochondrial-type HMG-CoA synthase, so a compartmental division of labour between the two is excluded and should not be proposed. Single analysis only. Work the question on three axes and keep them separate. First, catalytic integrity: report whether each paralogue carries the complete HMG-CoA synthase catalytic set, naming the positions in each protein and confirming each against the local UniProt records, and say explicitly whether either has lost a catalytic or substrate-binding residue, since a degenerate copy would answer the question outright. State the identity between the two proteins and their identity to the characterised yeast and human enzymes, and say whether either is truncated or carries an unusual insertion or deletion relative to the family. Second, expression: state what is actually measured about transcript or protein abundance for each gene, naming the datasets or publications and the conditions, and say plainly if the available data are from whole-genome studies that do not resolve the paralogues or do not cover the relevant conditions. Transcriptional co-regulation with the downstream ergosterol or siderophore branches would be informative, so say whether either gene is co-regulated with either branch and on what evidence. Third, requirement: state whether either gene has been deleted, repressed or shown essential, and what the phenotype was, distinguishing a published genetic result from an inference. If one paralogue is essential and the other dispensable, that settles the division of labour; if both are dispensable singly, say whether a double perturbation has been attempted. Then say which of the three axes, if any, separates the paralogues, and with what strength. If none does, say plainly that the paralogues cannot be distinguished on current evidence and name the single experiment that would separate them, which is an acceptable and expected outcome. Do not propose a compartmental division of labour, which the companion run excludes, and do not propose a GO annotation that assigns a branch of isoprenoid biosynthesis to one paralogue unless the evidence separates them.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the respective in-vivo contributions of the two Aspergillus fumigatus HMG-CoA synthase
  paralogues can be distinguished is the question, and a companion run on this organism has already removed
  one way the division of labour might have worked. Already recorded and not to be re-derived: that both
  Af293 proteins sit in PANTHER PTHR43323:SF2, that UniProt attributes the HMG-CoA synthase reaction to
  both, and that the available evidence does not distinguish their expression, activity or pathway flux.
  Carry forward and do not re-derive: a run on the mitochondrial thiolase erg10A established that neither
  paralogue is mitochondrial, both carrying N-terminal net charges inside a cytosolic control range against
  a mitochondrial control median of plus five, and that this organism therefore has no mitochondrial-type
  HMG-CoA synthase, so a compartmental division of labour between the two is excluded and should not be
  proposed. Single analysis only. Work the question on three axes and keep them separate. First, catalytic
  integrity: report whether each paralogue carries the complete HMG-CoA synthase catalytic set, naming
  the positions in each protein and confirming each against the local UniProt records, and say explicitly
  whether either has lost a catalytic or substrate-binding residue, since a degenerate copy would answer
  the question outright. State the identity between the two proteins and their identity to the characterised
  yeast and human enzymes, and say whether either is truncated or carries an unusual insertion or deletion
  relative to the family. Second, expression: state what is actually measured about transcript or protein
  abundance for each gene, naming the datasets or publications and the conditions, and say plainly if
  the available data are from whole-genome studies that do not resolve the paralogues or do not cover
  the relevant conditions. Transcriptional co-regulation with the downstream ergosterol or siderophore
  branches would be informative, so say whether either gene is co-regulated with either branch and on
  what evidence. Third, requirement: state whether either gene has been deleted, repressed or shown essential,
  and what the phenotype was, distinguishing a published genetic result from an inference. If one paralogue
  is essential and the other dispensable, that settles the division of labour; if both are dispensable
  singly, say whether a double perturbation has been attempted. Then say which of the three axes, if any,
  separates the paralogues, and with what strength. If none does, say plainly that the paralogues cannot
  be distinguished on current evidence and name the single experiment that would separate them, which
  is an acceptable and expected outcome. Do not propose a compartmental division of labour, which the
  companion run excludes, and do not propose a GO annotation that assigns a branch of isoprenoid biosynthesis
  to one paralogue unless the evidence separates them.'
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
**Generated:** 2026-11-26T18:42:46.279722

1. PMID:17352532
2. PMID:22309491
3. PMID:21062375
4. PMID:27185182
5. PMID:18838595
6. PMID:31134001
7. PMID:18787699
8. PMID:27438727
9. PMID:25375670
10. PMID:18989462
11. PMID:23617799
12. PMID:23264772
13. PMID:37334711
14. PMID:32225059