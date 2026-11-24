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
- **Hypothesis slug:** kgap-at5g03810-gdsl-site-and-subfamily
- **Source file:** genes/ARATH/At5g03810/At5g03810-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether Arabidopsis AT5G03810 (Q9FFN0) is a catalytically competent GDSL esterase/lipase, and which substrate class its closest characterised relatives act on, can be narrowed by sequence and structure. Single analysis only: map the four GDSL-family conserved blocks and the catalytic Ser-Gly-Asn-His residues onto the AT5G03810 AlphaFold model by comparison with structures of characterised SGNH/GDSL hydrolases, test whether the catalytic triad and oxyanion hole are assembled, place AT5G03810 in a phylogeny of characterised Arabidopsis and other plant GDSL esterases/lipases with known substrates (acetylesterases, cutin/suberin-related, lipid-hydrolysing), check for a signal peptide, and state whether it is predicted catalytically competent and which characterised clade, if any, it falls into.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether Arabidopsis AT5G03810 (Q9FFN0) is a catalytically competent GDSL esterase/lipase,
  and which substrate class its closest characterised relatives act on, can be narrowed by sequence and
  structure. Single analysis only: map the four GDSL-family conserved blocks and the catalytic Ser-Gly-Asn-His
  residues onto the AT5G03810 AlphaFold model by comparison with structures of characterised SGNH/GDSL
  hydrolases, test whether the catalytic triad and oxyanion hole are assembled, place AT5G03810 in a phylogeny
  of characterised Arabidopsis and other plant GDSL esterases/lipases with known substrates (acetylesterases,
  cutin/suberin-related, lipid-hydrolysing), check for a signal peptide, and state whether it is predicted
  catalytically competent and which characterised clade, if any, it falls into.'
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
**Generated:** 2026-11-24T12:52:44.954284

1. PMID:28510842
2. PMID:16301800
3. PMID:12842470
4. PMID:8401599
5. PMID:9330910
6. PMID:11130714
7. PMID:27862469
8. PMID:18273534
9. PMID:32188942
10. PMID:15697222
11. PMID:33505839
12. PMID:42191640
13. PMID:40694629