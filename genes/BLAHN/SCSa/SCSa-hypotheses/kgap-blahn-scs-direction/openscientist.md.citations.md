# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BLAHN
- **Taxon:** Blastocystis sp. ATCC 50177/Nand II (NCBITaxon:478820)
- **Gene directory:** SCSa
- **Gene symbol:** SCSa
- **UniProt accession:** B3FHT4

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-blahn-scs-direction
- **Source file:** genes/BLAHN/SCSa/SCSa-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the Blastocystis succinyl-CoA synthetase runs in the ATP-forming direction in the mitochondrion-related organelle, and which pathway it serves, can be constrained by thermodynamics, by the organelle's enzyme inventory, and by comparison with the other anaerobic eukaryotes whose organellar substrate-level phosphorylation has been measured, even though no flux has been measured in this organism. Already recorded and not to be re-derived: that the recombinant alpha/beta enzyme catalyses ATP-dependent succinyl-CoA formation and is specific for ATP with no detectable GTP activity, that the alpha subunit forms an active enzyme with the Plasmodium falciparum beta subunit, that the organism lacks a complete tricarboxylic acid cycle and oxidative phosphorylation, that the organelle has cristae, a membrane potential, a genome and an [FeFe] hydrogenase, that a transcript for acetate:succinate CoA-transferase exists and that this activity and succinate thiokinase activity are present in organelle fractions of another subtype, and that transcripts for the enzyme are as abundant as those for glycolytic enzymes. Single analysis only. First, treat the direction as a thermodynamic and kinetic question rather than a matter of nomenclature: state the standard free energy of the reaction and in which direction it is near equilibrium, and then say what intracellular succinyl-CoA, CoA, succinate, ADP, ATP and phosphate concentrations would be needed to drive net ATP formation, noting that assay direction in vitro says nothing about direction in vivo for a near-equilibrium ligase. Second, inventory the pathway: establish from the genome of this subtype, naming the accessions, whether acetate:succinate CoA-transferase, the enzymes that would supply succinyl-CoA, and the enzymes that would consume succinate are present, and whether a route exists that regenerates succinate so the CoA-transferase and the synthetase could run as a cycle; state whether acetate, succinate or both are reported end products of Blastocystis, distinguishing the subtype of this entry from others. Third, compare with the measured cases: state for Trichomonas vaginalis and for the other anaerobic eukaryotes in which organellar substrate-level phosphorylation by succinyl-CoA synthetase has been assayed, which direction the enzyme runs, what evidence established it, and whether the Blastocystis inventory matches those organisms or differs in a way that matters. Fourth, consider the alternative explicitly: that the enzyme runs in the succinyl-CoA-forming direction to supply succinyl-CoA for biosynthesis, and say what in the genome or the literature argues for or against it, including whether the organism has a demand for succinyl-CoA. Then give the direction the evidence favours, with the strength it deserves. If the evidence cannot distinguish the directions, say so plainly and name the measurement that would; a verdict of unresolved is acceptable. Do not infer the physiological direction from the assay direction or from the enzyme's name, and do not propose a GO annotation that asserts a direction the analysis cannot reach.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the Blastocystis succinyl-CoA synthetase runs in the ATP-forming direction in the
  mitochondrion-related organelle, and which pathway it serves, can be constrained by thermodynamics,
  by the organelle''s enzyme inventory, and by comparison with the other anaerobic eukaryotes whose organellar
  substrate-level phosphorylation has been measured, even though no flux has been measured in this organism.
  Already recorded and not to be re-derived: that the recombinant alpha/beta enzyme catalyses ATP-dependent
  succinyl-CoA formation and is specific for ATP with no detectable GTP activity, that the alpha subunit
  forms an active enzyme with the Plasmodium falciparum beta subunit, that the organism lacks a complete
  tricarboxylic acid cycle and oxidative phosphorylation, that the organelle has cristae, a membrane potential,
  a genome and an [FeFe] hydrogenase, that a transcript for acetate:succinate CoA-transferase exists and
  that this activity and succinate thiokinase activity are present in organelle fractions of another subtype,
  and that transcripts for the enzyme are as abundant as those for glycolytic enzymes. Single analysis
  only. First, treat the direction as a thermodynamic and kinetic question rather than a matter of nomenclature:
  state the standard free energy of the reaction and in which direction it is near equilibrium, and then
  say what intracellular succinyl-CoA, CoA, succinate, ADP, ATP and phosphate concentrations would be
  needed to drive net ATP formation, noting that assay direction in vitro says nothing about direction
  in vivo for a near-equilibrium ligase. Second, inventory the pathway: establish from the genome of this
  subtype, naming the accessions, whether acetate:succinate CoA-transferase, the enzymes that would supply
  succinyl-CoA, and the enzymes that would consume succinate are present, and whether a route exists that
  regenerates succinate so the CoA-transferase and the synthetase could run as a cycle; state whether
  acetate, succinate or both are reported end products of Blastocystis, distinguishing the subtype of
  this entry from others. Third, compare with the measured cases: state for Trichomonas vaginalis and
  for the other anaerobic eukaryotes in which organellar substrate-level phosphorylation by succinyl-CoA
  synthetase has been assayed, which direction the enzyme runs, what evidence established it, and whether
  the Blastocystis inventory matches those organisms or differs in a way that matters. Fourth, consider
  the alternative explicitly: that the enzyme runs in the succinyl-CoA-forming direction to supply succinyl-CoA
  for biosynthesis, and say what in the genome or the literature argues for or against it, including whether
  the organism has a demand for succinyl-CoA. Then give the direction the evidence favours, with the strength
  it deserves. If the evidence cannot distinguish the directions, say so plainly and name the measurement
  that would; a verdict of unresolved is acceptable. Do not infer the physiological direction from the
  assay direction or from the enzyme''s name, and do not propose a GO annotation that asserts a direction
  the analysis cannot reach.'
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
**Generated:** 2026-11-26T14:20:43.803969

1. PMID:38780415
2. PMID:9501211
3. PMID:18452512
4. PMID:12095995
5. PMID:22474284
6. PMID:32763239
7. PMID:7808480
8. PMID:8410536
9. PMID:18024431
10. PMID:19103231
11. PMID:15744302
12. PMID:21378103
13. PMID:41635752
14. PMID:18757809
15. PMID:18403202
16. PMID:20085767