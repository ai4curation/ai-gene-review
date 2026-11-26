# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ASPFU
- **Taxon:** Aspergillus fumigatus Af293 (NCBITaxon:330879)
- **Gene directory:** erg13B
- **Gene symbol:** erg13B
- **UniProt accession:** Q4WXT8

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-erg13b-paralog-divergence
- **Source file:** genes/ASPFU/erg13B/erg13B-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the two Aspergillus fumigatus HMG-CoA synthases erg13A and erg13B have diverged, or are a redundant pair, may be testable from sequence even though neither has been assayed. That both Af293 proteins sit in PANTHER PTHR43323:SF2, that UniProt attributes the HMG-CoA synthase reaction to both, and that Q4WXT8 is protein-existence level 3 with the function inferred by homology rather than assay, are already recorded, so do not re-derive them. Single analysis only: align the two paralogs to each other and to a characterised fungal HMG-CoA synthase, giving pairwise identities, and state residue by residue whether each retains the catalytic cysteine, the two histidines and the acetyl-CoA and acetoacetyl-CoA binding positions that the structural literature assigns, naming the structure and quoting the assignments, so that any asymmetric loss of catalytic machinery is visible rather than assumed; test whether the paralogs show asymmetric selection since their duplication by comparing their rates against a single-copy ortholog in a related Aspergillus that did not duplicate, giving the measurement, since one relaxed copy and one constrained copy is the signature that would make a divergence reading credible, and state plainly if synonymous sites are too saturated to compute; report whether the duplication is shared across Aspergillus species or specific to this lineage, since a retained ancient duplicate is a different claim from a recent one; and state whether either gene carries a distinguishing feature that could partition function without changing the active site, such as a different targeting signal, a divergent N-terminus or a promoter in a different regulatory context. State whether a functional difference is predicted, and say plainly if sequence cannot distinguish redundancy from divergence, which is the expected answer if the paralogs are nearly identical.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the two Aspergillus fumigatus HMG-CoA synthases erg13A and erg13B have diverged,
  or are a redundant pair, may be testable from sequence even though neither has been assayed. That both
  Af293 proteins sit in PANTHER PTHR43323:SF2, that UniProt attributes the HMG-CoA synthase reaction to
  both, and that Q4WXT8 is protein-existence level 3 with the function inferred by homology rather than
  assay, are already recorded, so do not re-derive them. Single analysis only: align the two paralogs
  to each other and to a characterised fungal HMG-CoA synthase, giving pairwise identities, and state
  residue by residue whether each retains the catalytic cysteine, the two histidines and the acetyl-CoA
  and acetoacetyl-CoA binding positions that the structural literature assigns, naming the structure and
  quoting the assignments, so that any asymmetric loss of catalytic machinery is visible rather than assumed;
  test whether the paralogs show asymmetric selection since their duplication by comparing their rates
  against a single-copy ortholog in a related Aspergillus that did not duplicate, giving the measurement,
  since one relaxed copy and one constrained copy is the signature that would make a divergence reading
  credible, and state plainly if synonymous sites are too saturated to compute; report whether the duplication
  is shared across Aspergillus species or specific to this lineage, since a retained ancient duplicate
  is a different claim from a recent one; and state whether either gene carries a distinguishing feature
  that could partition function without changing the active site, such as a different targeting signal,
  a divergent N-terminus or a promoter in a different regulatory context. State whether a functional difference
  is predicted, and say plainly if sequence cannot distinguish redundancy from divergence, which is the
  expected answer if the paralogs are nearly identical.'
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
**Generated:** 2026-11-26T08:07:50.450313

1. PMID:15292254
2. PMID:8755743
3. PMID:22510038
4. PMID:28757960
5. PMID:42172680
6. PMID:17428571
7. PMID:38684680
8. PMID:38769341
9. PMID:40937856
10. PMID:38975761
11. PMID:39670730