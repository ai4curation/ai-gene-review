# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** TRIVA
- **Taxon:** Trichomonas vaginalis (NCBITaxon:5722)
- **Gene directory:** ALPHA-SCS1
- **Gene symbol:** ALPHA-SCS1
- **UniProt accession:** P53399

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-triva-scs-pairing
- **Source file:** genes/TRIVA/ALPHA-SCS1/ALPHA-SCS1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Which of the three Trichomonas vaginalis beta subunits this alpha subunit pairs with, and which nucleotide the resulting enzyme uses, may be approachable by interface coevolution rather than by the specificity determinants, which are likely to be uninformative here. That three alpha and three beta genes exist, that all three alphas keep the phosphohistidine, that all three betas carry Gly at position 20 of the mature chain, a residue found in no assayed enzyme of the family, and that hydrogenosomes show both ADP- and GDP-dependent activity with a native enzyme larger than the usual dimer, are already recorded, so do not re-derive them. A companion analysis of the Dictyostelium enzyme established that Gln20beta is the only position with a mechanistic assignment to nucleotide discrimination and that it predicts in one direction only, so treat Gly20beta as uninformative unless evidence says otherwise and say so. Single analysis only: state what the structural literature assigns to the alpha-beta interface of a characterised succinyl-CoA synthetase, naming the structure and quoting the statements, then list the interface positions and report what each of the three alphas and each of the three betas has at them, so that any pairing signal is visible as a pattern rather than asserted; test whether the residue differences among the three alphas and among the three betas are concentrated at interface positions or distributed at random, giving the measurement, since only the former would support specific pairing; state whether coevolution or phylogenetic congruence between the alpha and beta gene families supports a particular pairing, and whether the trees are even resolvable at 8 to 14 differences per 309 residues; and state whether anything in the sequences bears on the larger-than-dimeric native enzyme, such as an oligomerisation surface absent from the dimeric enzymes. State which pairing and nucleotide use are predicted, and say plainly if the sequences cannot support any pairing assignment, which is the expected answer if the paralogs are too similar to carry a signal.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Which of the three Trichomonas vaginalis beta subunits this alpha subunit pairs with, and
  which nucleotide the resulting enzyme uses, may be approachable by interface coevolution rather than
  by the specificity determinants, which are likely to be uninformative here. That three alpha and three
  beta genes exist, that all three alphas keep the phosphohistidine, that all three betas carry Gly at
  position 20 of the mature chain, a residue found in no assayed enzyme of the family, and that hydrogenosomes
  show both ADP- and GDP-dependent activity with a native enzyme larger than the usual dimer, are already
  recorded, so do not re-derive them. A companion analysis of the Dictyostelium enzyme established that
  Gln20beta is the only position with a mechanistic assignment to nucleotide discrimination and that it
  predicts in one direction only, so treat Gly20beta as uninformative unless evidence says otherwise and
  say so. Single analysis only: state what the structural literature assigns to the alpha-beta interface
  of a characterised succinyl-CoA synthetase, naming the structure and quoting the statements, then list
  the interface positions and report what each of the three alphas and each of the three betas has at
  them, so that any pairing signal is visible as a pattern rather than asserted; test whether the residue
  differences among the three alphas and among the three betas are concentrated at interface positions
  or distributed at random, giving the measurement, since only the former would support specific pairing;
  state whether coevolution or phylogenetic congruence between the alpha and beta gene families supports
  a particular pairing, and whether the trees are even resolvable at 8 to 14 differences per 309 residues;
  and state whether anything in the sequences bears on the larger-than-dimeric native enzyme, such as
  an oligomerisation surface absent from the dimeric enzymes. State which pairing and nucleotide use are
  predicted, and say plainly if the sequences cannot support any pairing assignment, which is the expected
  answer if the paralogs are too similar to carry a signal.'
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
**Generated:** 2026-11-26T04:47:02.945277

1. PMID:9917402
2. PMID:33174373
3. PMID:31282474
4. PMID:31077495
5. PMID:9622355
6. PMID:32763239
7. PMID:33645539