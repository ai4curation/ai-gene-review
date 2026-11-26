# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ARATH
- **Taxon:** Arabidopsis thaliana (NCBITaxon:3702)
- **Gene directory:** At5g03810
- **Gene symbol:** At5g03810
- **UniProt accession:** Q9FFN0

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-at5g03810-family-context
- **Source file:** genes/ARATH/At5g03810/At5g03810-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

What AT5G03810 does may be constrained by the one thing that distinguishes it from the other hundred Arabidopsis GDSL enzymes: its immediate genomic and family context. That the 353-residue precursor has a cleavable signal peptide, five predicted N-glycosylation sites and an intact SGNH Ser-Asp-His triad, that the names and EC 3.1.1.- are family assignments rather than measurements, that no publication mentions the gene and protein existence is inferred from homology alone, and that it sits in a tandem pair with the equally uncharacterised AT5G03820 and more distantly with AT3G16370 whose product is in apoplastic fluid, are already recorded, so do not re-derive them. Single analysis only: place AT5G03810 within the Arabidopsis GDSL family phylogeny and name its closest relatives that have any functional characterisation, giving identities and stating for each what substrate was measured, since substrate preference in this family tracks clade rather than overall identity; compare AT5G03810 with AT5G03820 residue by residue across the substrate-binding groove and the oxyanion hole, and state whether the tandem pair is near-identical, which would support the redundancy explanation the gap offers for the absent phenotype, or divergent, which would not; report what public expression data say about where and when each of the pair is transcribed, including whether they are co-expressed or reciprocally expressed, and state plainly if the data are absent rather than inferring from the family; and state whether the tandem arrangement is conserved in other Brassicaceae or is an Arabidopsis-specific duplication. State which substrate class and which tissue context the evidence supports, and say plainly if nothing distinguishes this gene from the rest of its family, which is the expected answer for a wholly uncharacterised member.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'What AT5G03810 does may be constrained by the one thing that distinguishes it from the other
  hundred Arabidopsis GDSL enzymes: its immediate genomic and family context. That the 353-residue precursor
  has a cleavable signal peptide, five predicted N-glycosylation sites and an intact SGNH Ser-Asp-His
  triad, that the names and EC 3.1.1.- are family assignments rather than measurements, that no publication
  mentions the gene and protein existence is inferred from homology alone, and that it sits in a tandem
  pair with the equally uncharacterised AT5G03820 and more distantly with AT3G16370 whose product is in
  apoplastic fluid, are already recorded, so do not re-derive them. Single analysis only: place AT5G03810
  within the Arabidopsis GDSL family phylogeny and name its closest relatives that have any functional
  characterisation, giving identities and stating for each what substrate was measured, since substrate
  preference in this family tracks clade rather than overall identity; compare AT5G03810 with AT5G03820
  residue by residue across the substrate-binding groove and the oxyanion hole, and state whether the
  tandem pair is near-identical, which would support the redundancy explanation the gap offers for the
  absent phenotype, or divergent, which would not; report what public expression data say about where
  and when each of the pair is transcribed, including whether they are co-expressed or reciprocally expressed,
  and state plainly if the data are absent rather than inferring from the family; and state whether the
  tandem arrangement is conserved in other Brassicaceae or is an Arabidopsis-specific duplication. State
  which substrate class and which tissue context the evidence supports, and say plainly if nothing distinguishes
  this gene from the rest of its family, which is the expected answer for a wholly uncharacterised member.'
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
**Generated:** 2026-11-26T08:03:47.123065

1. PMID:32188942
2. PMID:20033440
3. PMID:23430565
4. PMID:18538804
5. PMID:40694629
6. PMID:35577991
7. PMID:35147444
8. PMID:30598046
9. PMID:38923126
10. PMID:42594629
11. PMID:42450553
12. PMID:42436383
13. PMID:37008509
14. PMID:36609252
15. PMID:32670311