# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BPT5
- **Taxon:** Escherichia phage T5 (NCBITaxon:2695836)
- **Gene directory:** D15
- **Gene symbol:** D15
- **UniProt accession:** P06229

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-d15-late-transcription
- **Source file:** genes/BPT5/D15/D15-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the failure of T5 late gene expression in the absence of D15 nuclease activity is a direct template requirement or an indirect consequence of failed replication may be decidable from the published record, and if it is not, saying so precisely is the useful result. Already recorded and not to be re-derived: that D15 is a 291-residue magnesium-dependent FEN-family nuclease expressed early in infection, that it carries processive 5'-3' exonucleolysis and structure-specific endonucleolysis at single-strand/double-strand junctions in one active site, that substrate selection is structural rather than sequence-based with the 5' arm threading a helical arch, that metal occupancy and pH decide which reaction predominates, that the enzyme is required for T5 genome replication and for maturation of concatemers into the single-stranded-interruption-containing virion DNA, and that the 1973 proposal attributes the late-transcription block to nicks or gaps the nuclease introduces. Single analysis only. The question is separability. Establish whether any published experiment uncouples the replication requirement from the transcription requirement: a temperature-sensitive or amber D15 allele shifted after replication is underway, a host or phage mutant in which replication proceeds without D15, an in vitro late-promoter transcription assay on nicked against intact template, or a hydroxyurea-type or inhibitor block of replication that leaves D15 active. For each such experiment, state what was measured, whether late transcripts or only late proteins were scored, and whether the timing permits the conclusion. Then address the template-structure claim on its own terms: state where the single-stranded interruptions of mature T5 DNA lie relative to the mapped late promoters, whether their positions are sequence-defined and reproducible between preparations or variable, and whether anything is known about which enzyme makes them, since an interruption pattern that is reproducible and promoter-proximal supports the direct proposal while a variable one does not. State also which RNA polymerase transcribes T5 late genes and what, if anything, is known about template-structure requirements of that polymerase on a nicked duplex, distinguishing a requirement for a nick from a requirement for replication-generated ends or for displacement synthesis. Finally say which of the two explanations the evidence favours, and if the record contains no experiment that separates them, say so plainly and name the single experiment that would. A verdict of unresolved is an acceptable and expected outcome here; do not assemble a mechanism from plausibility. Note explicitly if the primary 1973 and 1980 papers are not retrievable, since much of this literature predates electronic full text.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the failure of T5 late gene expression in the absence of D15 nuclease activity is
  a direct template requirement or an indirect consequence of failed replication may be decidable from
  the published record, and if it is not, saying so precisely is the useful result. Already recorded and
  not to be re-derived: that D15 is a 291-residue magnesium-dependent FEN-family nuclease expressed early
  in infection, that it carries processive 5''-3'' exonucleolysis and structure-specific endonucleolysis
  at single-strand/double-strand junctions in one active site, that substrate selection is structural
  rather than sequence-based with the 5'' arm threading a helical arch, that metal occupancy and pH decide
  which reaction predominates, that the enzyme is required for T5 genome replication and for maturation
  of concatemers into the single-stranded-interruption-containing virion DNA, and that the 1973 proposal
  attributes the late-transcription block to nicks or gaps the nuclease introduces. Single analysis only.
  The question is separability. Establish whether any published experiment uncouples the replication requirement
  from the transcription requirement: a temperature-sensitive or amber D15 allele shifted after replication
  is underway, a host or phage mutant in which replication proceeds without D15, an in vitro late-promoter
  transcription assay on nicked against intact template, or a hydroxyurea-type or inhibitor block of replication
  that leaves D15 active. For each such experiment, state what was measured, whether late transcripts
  or only late proteins were scored, and whether the timing permits the conclusion. Then address the template-structure
  claim on its own terms: state where the single-stranded interruptions of mature T5 DNA lie relative
  to the mapped late promoters, whether their positions are sequence-defined and reproducible between
  preparations or variable, and whether anything is known about which enzyme makes them, since an interruption
  pattern that is reproducible and promoter-proximal supports the direct proposal while a variable one
  does not. State also which RNA polymerase transcribes T5 late genes and what, if anything, is known
  about template-structure requirements of that polymerase on a nicked duplex, distinguishing a requirement
  for a nick from a requirement for replication-generated ends or for displacement synthesis. Finally
  say which of the two explanations the evidence favours, and if the record contains no experiment that
  separates them, say so plainly and name the single experiment that would. A verdict of unresolved is
  an acceptable and expected outcome here; do not assemble a mechanism from plausibility. Note explicitly
  if the primary 1973 and 1980 papers are not retrievable, since much of this literature predates electronic
  full text.'
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
**Generated:** 2026-11-26T12:43:53.236798

1. PMID:4357874
2. PMID:1095368
3. PMID:2419589
4. PMID:6248541
5. PMID:24198424
6. PMID:19592061
7. PMID:4522782
8. PMID:32722583
9. PMID:4359432
10. PMID:1092331
11. PMID:7264606
12. PMID:6287031
13. PMID:6316267
14. PMID:23236447
15. PMID:9380501
16. PMID:9889266
17. PMID:8657312
18. PMID:27273516
19. PMID:2211703
20. PMID:17559871
21. PMID:4596299
22. PMID:10364212