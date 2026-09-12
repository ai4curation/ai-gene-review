# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ARTAN
- **Taxon:** Artemisia annua (NCBITaxon:35608)
- **Gene directory:** A0A2U1PS28
- **Gene symbol:** A0A2U1PS28
- **UniProt accession:** A0A2U1PS28

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-2-go-0005525
- **Source file:** genes/ARTAN/A0A2U1PS28/A0A2U1PS28-ai-review.yaml
- **Source selector:** core_functions[2]

## Seed Hypothesis

GTP binding (GO:0005525) is a core function of A0A2U1PS28. Current rationale: GUF1/EF-4 binds GTP as a prerequisite for its ribosome-dependent function. The G-domain contains conserved nucleotide-binding elements (P-loop, switch I, switch II) and the GTP-bound form is required for association with translating mitoribosomes.

## Term and Decision Context

- Molecular function: GTP binding (GO:0005525)
- Description: GUF1/EF-4 binds GTP as a prerequisite for its ribosome-dependent function. The G-domain contains conserved nucleotide-binding elements (P-loop, switch I, switch II) and the GTP-bound form is required for association with translating mitoribosomes.
- Directly involved in: mitochondrial translational elongation (GO:0070125)
- Locations: mitochondrial matrix (GO:0005759)

## Reference Context

- file:ARTAN/A0A2U1PS28/A0A2U1PS28-uniprot.txt

## Source Context YAML

```yaml
description: GUF1/EF-4 binds GTP as a prerequisite for its ribosome-dependent function. The G-domain contains
  conserved nucleotide-binding elements (P-loop, switch I, switch II) and the GTP-bound form is required
  for association with translating mitoribosomes.
molecular_function:
  id: GO:0005525
  label: GTP binding
directly_involved_in:
- id: GO:0070125
  label: mitochondrial translational elongation
locations:
- id: GO:0005759
  label: mitochondrial matrix
supported_by:
- reference_id: file:ARTAN/A0A2U1PS28/A0A2U1PS28-uniprot.txt
  supporting_text: Binds to mitochondrial ribosomes in a GTP-dependent manner.
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
prompt so the report can be compared against them after the run. Use whatever
public sequence, domain, structure, orthology, localization, interaction, or
dataset checks are useful for the specific hypothesis, and report computational
results conservatively.

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
**Generated:** 2026-06-22T01:56:47.336613

1. PMID:25712150
2. PMID:27092003
3. PMID:27137929
4. PMID:18442968
5. PMID:18362332
6. PMID:20657179
7. PMID:17110332
8. PMID:23662805
9. PMID:26486472
10. PMID:28320876
11. PMID:19172743
12. PMID:24272752