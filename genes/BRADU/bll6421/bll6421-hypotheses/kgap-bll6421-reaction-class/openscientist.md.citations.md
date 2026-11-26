# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BRADU
- **Taxon:** Bradyrhizobium diazoefficiens USDA 110 (NCBITaxon:224911)
- **Gene directory:** bll6421
- **Gene symbol:** bll6421
- **UniProt accession:** Q89GC4

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-bll6421-reaction-class
- **Source file:** genes/BRADU/bll6421/bll6421-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the molecular activity of bll6421 can be constrained beyond its family label by a residue-level and family-ranking analysis, in the way that worked for its operon neighbour, is the question. Carry forward from the completed run on bll6422 and do not re-derive any of it: that the eight-gene operon with its divergent LysR regulator is a gene-for-gene syntenic copy of the genetically defined Herbaspirillum naringenin degradation operon, that the operon responds to the soybean isoflavone genistein in a NodW-dependent way, that no flavonoid has been shown to be consumed by this organism, that no enzyme in the operon is flavonoid-specific by sequence, and that the operon notably lacks the meta-cleavage product hydrolase that would name the compound its neighbour receives. Synteny and induction are therefore established and silent about chemistry, and nothing in this run should lean on them to name a substrate. Already recorded for bll6421 itself: that it is a Rossmann-fold epimerase/dehydratase-family protein related to Herbaspirillum FdeJ, and that neither a nucleotide-sugar substrate nor the proposed oxaloacetate-releasing flavonoid-intermediate reaction has been established. Single analysis only. Place bll6421 within the extended short-chain dehydrogenase/reductase and NAD-dependent nucleotide-sugar epimerase/dehydratase families at residue level: report whether the dinucleotide-binding motif and the catalytic constellation characteristic of each candidate subfamily are present or absent, naming the positions in this protein and confirming each against the local UniProt record, and distinguish explicitly between the UDP-glucose 4-epimerase type catalytic set, the dTDP-glucose 4,6-dehydratase and GDP-mannose 4,6-dehydratase types, and the nucleotide-independent epimerases and dehydratases of the same fold. State whether the cofactor is predicted to be NAD or NADP and on what basis. Then rank the protein across the reviewed members of the candidate families as was done for its neighbour, reporting an effect size rather than a nearest-neighbour identity alone, and say which side of the epimerase/dehydratase division it falls on, or that it falls on neither cleanly. Separately, state what reaction FdeJ is actually assigned in the characterised Herbaspirillum pathway, whether that assignment rests on measurement or on annotation, and whether bll6421 is the syntenic equivalent of FdeJ or of another cistron. If no nucleotide-sugar or flavonoid substrate can be constrained, say plainly that the substrate is unconstrained and report only the reaction class, as the neighbour's analysis did; a split verdict in which the chemistry is narrowed and the substrate is not is the expected shape of the answer. Do not infer a substrate from locus membership, and do not propose a GO annotation that names a compound the analysis cannot reach.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the molecular activity of bll6421 can be constrained beyond its family label by a
  residue-level and family-ranking analysis, in the way that worked for its operon neighbour, is the question.
  Carry forward from the completed run on bll6422 and do not re-derive any of it: that the eight-gene
  operon with its divergent LysR regulator is a gene-for-gene syntenic copy of the genetically defined
  Herbaspirillum naringenin degradation operon, that the operon responds to the soybean isoflavone genistein
  in a NodW-dependent way, that no flavonoid has been shown to be consumed by this organism, that no enzyme
  in the operon is flavonoid-specific by sequence, and that the operon notably lacks the meta-cleavage
  product hydrolase that would name the compound its neighbour receives. Synteny and induction are therefore
  established and silent about chemistry, and nothing in this run should lean on them to name a substrate.
  Already recorded for bll6421 itself: that it is a Rossmann-fold epimerase/dehydratase-family protein
  related to Herbaspirillum FdeJ, and that neither a nucleotide-sugar substrate nor the proposed oxaloacetate-releasing
  flavonoid-intermediate reaction has been established. Single analysis only. Place bll6421 within the
  extended short-chain dehydrogenase/reductase and NAD-dependent nucleotide-sugar epimerase/dehydratase
  families at residue level: report whether the dinucleotide-binding motif and the catalytic constellation
  characteristic of each candidate subfamily are present or absent, naming the positions in this protein
  and confirming each against the local UniProt record, and distinguish explicitly between the UDP-glucose
  4-epimerase type catalytic set, the dTDP-glucose 4,6-dehydratase and GDP-mannose 4,6-dehydratase types,
  and the nucleotide-independent epimerases and dehydratases of the same fold. State whether the cofactor
  is predicted to be NAD or NADP and on what basis. Then rank the protein across the reviewed members
  of the candidate families as was done for its neighbour, reporting an effect size rather than a nearest-neighbour
  identity alone, and say which side of the epimerase/dehydratase division it falls on, or that it falls
  on neither cleanly. Separately, state what reaction FdeJ is actually assigned in the characterised Herbaspirillum
  pathway, whether that assignment rests on measurement or on annotation, and whether bll6421 is the syntenic
  equivalent of FdeJ or of another cistron. If no nucleotide-sugar or flavonoid substrate can be constrained,
  say plainly that the substrate is unconstrained and report only the reaction class, as the neighbour''s
  analysis did; a split verdict in which the chemistry is narrowed and the substrate is not is the expected
  shape of the answer. Do not infer a substrate from locus membership, and do not propose a GO annotation
  that names a compound the analysis cannot reach.'
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
**Generated:** 2026-11-26T13:38:12.825023

1. PMID:23125118
2. PMID:27878922