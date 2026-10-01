# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** DESRO
- **Taxon:** Desmodus rotundus (NCBITaxon:9430)
- **Gene directory:** K9IMD0
- **Gene symbol:** K9IMD0
- **UniProt accession:** K9IMD0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** lactotransferrin-functions-and-draculin-specialization
- **Source file:** genes/DESRO/K9IMD0/K9IMD0-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Desmodus rotundus lactotransferrin/draculin K9IMD0 retains transferrin-family metal binding GO:0046872, iron/monoatomic ion transport GO:0006826/GO:0006811, serine-type peptidase/peptidase/hydrolase activity GO:0008236/GO:0008233/GO:0016787 and proteolysis GO:0006508, antibacterial humoral response GO:0019731, defense response to bacterium GO:0042742 and immune system process GO:0002376. Evaluate these independently of its anticoagulant role. Separately assess early/recycling endosome and plasma-membrane association GO:0005769/GO:0055037/GO:0005886, considering uptake and receptor-associated pools of a secreted protein. Trace the exact relationship of K9IMD0 to the purified draculin in PMID:7740503 and the salivary proteomics identification PMID:23748026. Distinguish measurements on this protein from human lactoferrin and other transferrins; test any claimed loss of iron-binding sites or protease activity against sequence/structure. Anticoagulant specialization does not itself exclude another inherited function; missing transmembrane topology does not exclude peripheral association.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Desmodus rotundus lactotransferrin/draculin K9IMD0 retains transferrin-family metal binding
  GO:0046872, iron/monoatomic ion transport GO:0006826/GO:0006811, serine-type peptidase/peptidase/hydrolase
  activity GO:0008236/GO:0008233/GO:0016787 and proteolysis GO:0006508, antibacterial humoral response
  GO:0019731, defense response to bacterium GO:0042742 and immune system process GO:0002376. Evaluate
  these independently of its anticoagulant role. Separately assess early/recycling endosome and plasma-membrane
  association GO:0005769/GO:0055037/GO:0005886, considering uptake and receptor-associated pools of a
  secreted protein. Trace the exact relationship of K9IMD0 to the purified draculin in PMID:7740503 and
  the salivary proteomics identification PMID:23748026. Distinguish measurements on this protein from
  human lactoferrin and other transferrins; test any claimed loss of iron-binding sites or protease activity
  against sequence/structure. Anticoagulant specialization does not itself exclude another inherited function;
  missing transmembrane topology does not exclude peripheral association.
focus_type: function_assignment
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
**Generated:** 2026-09-21T01:28:37.605918

1. PMID:23748026
2. PMID:9795244
3. PMID:10556567
4. PMID:7740503
5. PMID:23411029
6. PMID:12535064
7. PMID:9770539
8. PMID:11163480