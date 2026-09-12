# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** AQUCT
- **Taxon:** Aquarana catesbeiana (NCBITaxon:8400)
- **Gene directory:** A0A2G9RZF1
- **Gene symbol:** A0A2G9RZF1
- **UniProt accession:** A0A2G9RZF1

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0005201
- **Source file:** genes/AQUCT/A0A2G9RZF1/A0A2G9RZF1-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

extracellular matrix structural constituent (GO:0005201) is a core function of A0A2G9RZF1. Current rationale: The precise molecular function of A0A2G9RZF1 is unknown. Based on domain architecture, it contains a single CUB domain, which is a non-catalytic extracellular recognition module that mediates protein-protein interactions. CUB domains function as modular binding surfaces supporting recognition and assembly of macromolecular complexes in extracellular biology. The FunFam classification to PCPE1 (Procollagen C-endopeptidase enhancer 1) suggests a possible role as an extracellular matrix structural constituent, but the short length (156 aa) and absence of additional functional domains preclude confident functional assignment. PANTHER PAINT annotations for the broader PTHR24251 family include metalloendopeptidase activity, but this protein lacks any identifiable protease domain and should not be annotated with that function.

## Term and Decision Context

- Molecular function: extracellular matrix structural constituent (GO:0005201)
- Description: The precise molecular function of A0A2G9RZF1 is unknown. Based on domain architecture, it contains a single CUB domain, which is a non-catalytic extracellular recognition module that mediates protein-protein interactions. CUB domains function as modular binding surfaces supporting recognition and assembly of macromolecular complexes in extracellular biology. The FunFam classification to PCPE1 (Procollagen C-endopeptidase enhancer 1) suggests a possible role as an extracellular matrix structural constituent, but the short length (156 aa) and absence of additional functional domains preclude confident functional assignment. PANTHER PAINT annotations for the broader PTHR24251 family include metalloendopeptidase activity, but this protein lacks any identifiable protease domain and should not be annotated with that function.
- Locations: extracellular region (GO:0005576)

## Reference Context

- file:AQUCT/A0A2G9RZF1/A0A2G9RZF1-uniprot.txt
- file:AQUCT/A0A2G9RZF1/A0A2G9RZF1-deep-research-falcon.md

## Source Context YAML

```yaml
description: The precise molecular function of A0A2G9RZF1 is unknown. Based on domain architecture, it
  contains a single CUB domain, which is a non-catalytic extracellular recognition module that mediates
  protein-protein interactions. CUB domains function as modular binding surfaces supporting recognition
  and assembly of macromolecular complexes in extracellular biology. The FunFam classification to PCPE1
  (Procollagen C-endopeptidase enhancer 1) suggests a possible role as an extracellular matrix structural
  constituent, but the short length (156 aa) and absence of additional functional domains preclude confident
  functional assignment. PANTHER PAINT annotations for the broader PTHR24251 family include metalloendopeptidase
  activity, but this protein lacks any identifiable protease domain and should not be annotated with that
  function.
molecular_function:
  id: GO:0005201
  label: extracellular matrix structural constituent
locations:
- id: GO:0005576
  label: extracellular region
supported_by:
- reference_id: file:AQUCT/A0A2G9RZF1/A0A2G9RZF1-uniprot.txt
  supporting_text: '[UniProt record: CUB domain at residues 31-147; InterPro IPR000859 CUB_dom; Pfam PF00431
    CUB; FunFam 2.60.120.290:FF:000005 Procollagen C-endopeptidase enhancer 1; PANTHER PTHR24251 OVOCHYMASE-RELATED]'
- reference_id: file:AQUCT/A0A2G9RZF1/A0A2G9RZF1-deep-research-falcon.md
  supporting_text: '[CUB domains are almost exclusively found in secreted, extracellular, or plasma membrane-associated
    proteins; they serve as modular binding surfaces supporting recognition and assembly of macromolecular
    complexes for extracellular biology]'
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
**Generated:** 2026-06-22T00:46:43.168118

1. PMID:21954942
2. PMID:20551380
3. PMID:19801683
4. PMID:12393877
5. PMID:30078642
6. PMID:17446170
7. PMID:18664565
8. PMID:25642644
9. PMID:10500163
10. PMID:24117177
11. PMID:16819821
12. PMID:30295181
13. PMID:21093502