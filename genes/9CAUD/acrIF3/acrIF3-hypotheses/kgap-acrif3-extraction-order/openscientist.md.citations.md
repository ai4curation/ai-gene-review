# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** 9CAUD
- **Taxon:** Pseudomonas phage JBD5 (NCBITaxon:1223261)
- **Gene directory:** acrIF3
- **Gene symbol:** acrIF3
- **UniProt accession:** L7P7R7

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-acrif3-extraction-order
- **Source file:** genes/9CAUD/acrIF3/acrIF3-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether AcrIF3 can extract Cas2/3 that is already engaged with a licensed R-loop, or can only intercept free Cas2/3 before recruitment, is a question about the order of events rather than about the interaction, and the useful result may be a precise statement of what the published record cannot distinguish. Already recorded and not to be re-derived: that AcrIF3 is a 139-residue homodimer of Pseudomonas phage JBD5, that it binds the type I-F Cas2/3 helicase-nuclease and stabilises an ADP-bound state, that it masks surfaces required for recruitment to the DNA-bound Csy surveillance complex, that target recognition by Csy is retained while downstream DNA destruction and Cas3-dependent primed spacer acquisition are inhibited, and that the target-bound nuclease-free surveillance complex can consequently repress transcription. Single analysis only. Treat interception and extraction as competing models with distinguishable consequences. State what the structures actually show about the AcrIF3 binding surface: whether it overlaps the Csy-binding surface of Cas2/3 sterically, so that the two associations are mutually exclusive, or whether it lies adjacent so that a ternary complex is possible in principle, giving the evidence for the call. Then ask what would have to be true for extraction: whether AcrIF3 binding to Cas2/3 is thermodynamically strong enough to compete with a recruited, R-loop-engaged complex, quoting any measured affinities for AcrIF3 to Cas2/3 and for Cas2/3 to the target-bound Csy complex and saying plainly if either is unmeasured; and whether the ADP-bound state it stabilises is a state a recruited Cas2/3 can occupy, since trapping a nucleotide state is a different mechanism from occluding a surface. Say what experimental designs would separate the models, and then state whether any published experiment implements one: an order-of-addition assay in which AcrIF3 is supplied after R-loop formation rather than before, a single-molecule or kinetic measurement of Cas2/3 dissociation in the presence of the inhibitor, or an in vivo experiment in which the inhibitor is induced after interference has begun. Report for each whether it exists and what it showed. Consider also whether the biology makes one model necessary: a phage delivering an anti-CRISPR into a cell with pre-existing primed interference would need extraction, whereas one establishing infection ahead of recruitment would not, so say what is known about the timing of acrIF3 expression during infection relative to interference. If the record cannot separate the models, say so plainly and name the one experiment that would; an unresolved verdict is acceptable and expected. Do not infer extraction from the strength of inhibition in a steady-state assay, which cannot distinguish the two orders, and do not propose a GO annotation on the strength of this analysis.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether AcrIF3 can extract Cas2/3 that is already engaged with a licensed R-loop, or can
  only intercept free Cas2/3 before recruitment, is a question about the order of events rather than about
  the interaction, and the useful result may be a precise statement of what the published record cannot
  distinguish. Already recorded and not to be re-derived: that AcrIF3 is a 139-residue homodimer of Pseudomonas
  phage JBD5, that it binds the type I-F Cas2/3 helicase-nuclease and stabilises an ADP-bound state, that
  it masks surfaces required for recruitment to the DNA-bound Csy surveillance complex, that target recognition
  by Csy is retained while downstream DNA destruction and Cas3-dependent primed spacer acquisition are
  inhibited, and that the target-bound nuclease-free surveillance complex can consequently repress transcription.
  Single analysis only. Treat interception and extraction as competing models with distinguishable consequences.
  State what the structures actually show about the AcrIF3 binding surface: whether it overlaps the Csy-binding
  surface of Cas2/3 sterically, so that the two associations are mutually exclusive, or whether it lies
  adjacent so that a ternary complex is possible in principle, giving the evidence for the call. Then
  ask what would have to be true for extraction: whether AcrIF3 binding to Cas2/3 is thermodynamically
  strong enough to compete with a recruited, R-loop-engaged complex, quoting any measured affinities for
  AcrIF3 to Cas2/3 and for Cas2/3 to the target-bound Csy complex and saying plainly if either is unmeasured;
  and whether the ADP-bound state it stabilises is a state a recruited Cas2/3 can occupy, since trapping
  a nucleotide state is a different mechanism from occluding a surface. Say what experimental designs
  would separate the models, and then state whether any published experiment implements one: an order-of-addition
  assay in which AcrIF3 is supplied after R-loop formation rather than before, a single-molecule or kinetic
  measurement of Cas2/3 dissociation in the presence of the inhibitor, or an in vivo experiment in which
  the inhibitor is induced after interference has begun. Report for each whether it exists and what it
  showed. Consider also whether the biology makes one model necessary: a phage delivering an anti-CRISPR
  into a cell with pre-existing primed interference would need extraction, whereas one establishing infection
  ahead of recruitment would not, so say what is known about the timing of acrIF3 expression during infection
  relative to interference. If the record cannot separate the models, say so plainly and name the one
  experiment that would; an unresolved verdict is acceptable and expected. Do not infer extraction from
  the strength of inhibition in a steady-state assay, which cannot distinguish the two orders, and do
  not propose a GO annotation on the strength of this analysis.'
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
**Generated:** 2026-11-26T18:38:42.926123

1. PMID:31474367
2. PMID:30033364
3. PMID:30033365
4. PMID:26522594
5. PMID:27455460
6. PMID:30872121
7. PMID:26416740
8. PMID:27585537
9. PMID:35697070
10. PMID:35301482
11. PMID:28438998
12. PMID:42156407