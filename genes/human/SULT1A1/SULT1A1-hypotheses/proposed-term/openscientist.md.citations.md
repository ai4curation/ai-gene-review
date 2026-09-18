# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** SULT1A1
- **Gene symbol:** SULT1A1
- **UniProt accession:** P50225

## Focus

- **Focus type:** proposed_go_term
- **Hypothesis slug:** proposed-term
- **Source file:** genes/human/SULT1A1/SULT1A1-ai-review.yaml
- **Source selector:** proposed_new_terms[1]

## Seed Hypothesis

SULT1A1 should be considered for GO term .

## Term and Decision Context

- Proposed term:

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
proposed_name: thyroid hormone sulfotransferase activity
proposed_definition: 'Catalysis of the reaction: 3''-phosphoadenosine 5''-phosphosulfate + an iodothyronine
  = adenosine 3'',5''-bisphosphate + an iodothyronine sulfate + H+. The sulfonate group is transferred
  to the phenolic 4''-hydroxyl of the outer ring of thyroid hormones and their metabolites, including
  L-thyroxine (T4), 3,3'',5-triiodo-L-thyronine (T3), 3,3'',5''-triiodo-L-thyronine (reverse T3) and 3,3''-diiodo-L-thyronine.'
justification: GO has no molecular function term for iodothyronine sulfation, although it is a principal
  route of thyroid hormone inactivation and is the highest-affinity chemistry documented for SULT1A1 (Km
  0.14 uM for 3,3'-T2, roughly 240-fold tighter than SULT1A3). UniProt curates four distinct iodothyronine
  RHEA reactions for it on P50225 (RHEA:67876, RHEA:67888, RHEA:67892, RHEA:83575) with ECO:0000269 evidence,
  and Reactome models three of them (R-HSA-176474, R-HSA-176585). At present curators must fall back on
  either GO:0008146 sulfotransferase activity, which loses the substrate entirely, or GO:0004062 aryl
  sulfotransferase activity, which is correct chemically but does not distinguish thyroid hormone from
  any other phenol. The term would also apply to SULT1A3, SULT1B1 and SULT1E1, all of which sulfate iodothyronines.
proposed_parent:
  id: GO:0004062
  label: aryl sulfotransferase activity
supported_by:
- reference_id: PMID:10199779
  supporting_text: In all cases, the substrate preference was 3,3'-T2 >> rT3 > T3 > T4.
  reference_section_type: ABSTRACT
- reference_id: file:human/SULT1A1/SULT1A1-uniprot.txt
  supporting_text: Catalyzes the sulfation of T4 (L-thyroxine/3,5,3',5'-tetraiodothyronine), T3 (3,5,3'-triiodothyronine),
    rT3 (3,3',5'-triiodothyronine) and 3,3'-T2 (3,3'-diiodothyronine), with a substrate preference of
    3,3'-T2 > rT3 > T3 > T4.
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
**Generated:** 2026-08-31T02:11:25.150602

1. PMID:10199779
2. PMID:11739018
3. PMID:15531517
4. PMID:9848125