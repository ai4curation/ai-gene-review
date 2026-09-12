# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** SCO1
- **Gene symbol:** SCO1

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0016531
- **Source file:** genes/human/SCO1/SCO1-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

copper chaperone activity (GO:0016531) is a core function of SCO1. Current rationale: SCO1 is a mitochondrial copper chaperone/assembly factor that helps deliver copper to the CuA site of MT-CO2 during Complex IV biogenesis. Its core function is not mature Complex IV catalysis, but copper handling within the COX2 maturation pathway.

## Term and Decision Context

- Molecular function: copper chaperone activity (GO:0016531)
- Description: SCO1 is a mitochondrial copper chaperone/assembly factor that helps deliver copper to the CuA site of MT-CO2 during Complex IV biogenesis. Its core function is not mature Complex IV catalysis, but copper handling within the COX2 maturation pathway.
- Directly involved in: mitochondrial respiratory chain complex IV assembly (GO:0033617), respiratory chain complex IV assembly (GO:0008535)
- Locations: mitochondrial inner membrane (GO:0005743)

## Reference Context

- PMID:15229189
- file:human/SCO1/SCO1-uniprot.txt

## Source Context YAML

```yaml
description: SCO1 is a mitochondrial copper chaperone/assembly factor that helps deliver copper to the
  CuA site of MT-CO2 during Complex IV biogenesis. Its core function is not mature Complex IV catalysis,
  but copper handling within the COX2 maturation pathway.
molecular_function:
  id: GO:0016531
  label: copper chaperone activity
directly_involved_in:
- id: GO:0033617
  label: mitochondrial respiratory chain complex IV assembly
- id: GO:0008535
  label: respiratory chain complex IV assembly
locations:
- id: GO:0005743
  label: mitochondrial inner membrane
supported_by:
- reference_id: PMID:15229189
  supporting_text: Our results demonstrate that the human SCO proteins have non-overlapping, cooperative
    functions in mitochondrial copper delivery.
  full_text_unavailable: true
- reference_id: file:human/SCO1/SCO1-uniprot.txt
  supporting_text: Copper metallochaperone essential for the maturation of cytochrome c oxidase subunit
    II (MT-CO2/COX2). Together with SCO2, involved in delivering copper to the Cu(A) site on MT-CO2/COX2.
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

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

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

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.

**Provider:** openscientist
**Generated:** 2026-05-20T10:21:26.181325

1. PMID:15229189
2. PMID:19336478
3. PMID:14604533
4. PMID:28973536
5. PMID:41621246
6. PMID:32061935
7. PMID:29381136
8. PMID:35981890
9. PMID:40679281
10. PMID:19295170
11. PMID:20388558
12. PMID:20136502
13. PMID:15113935
14. PMID:25792727
15. PMID:21821119