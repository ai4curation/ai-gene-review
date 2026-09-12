# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** SOYBN
- **Taxon:** Glycine max (NCBITaxon:3847)
- **Gene directory:** C6T1A2
- **Gene symbol:** C6T1A2
- **UniProt accession:** C6T1A2

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0003700
- **Source file:** genes/SOYBN/C6T1A2/C6T1A2-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

DNA-binding transcription factor activity (GO:0003700) is a core function of C6T1A2. Current rationale: C6T1A2 is predicted to function as a DNA-binding transcription factor based on its C2H2-type zinc finger domain (residues 79-106), its classification in the Zinc_finger_protein_7 family (IPR053266), and its inclusion in a soybean transcription factor ORFeome. No experimental evidence directly demonstrates transcription factor activity for this specific protein; the annotation is inferred from domain architecture and family membership. The protein coordinates a zinc ion via the C2H2 zinc finger motif to stabilize the DNA-binding fold.

## Term and Decision Context

- Molecular function: DNA-binding transcription factor activity (GO:0003700)
- Description: C6T1A2 is predicted to function as a DNA-binding transcription factor based on its C2H2-type zinc finger domain (residues 79-106), its classification in the Zinc_finger_protein_7 family (IPR053266), and its inclusion in a soybean transcription factor ORFeome. No experimental evidence directly demonstrates transcription factor activity for this specific protein; the annotation is inferred from domain architecture and family membership. The protein coordinates a zinc ion via the C2H2 zinc finger motif to stabilize the DNA-binding fold.
- Locations: nucleus (GO:0005634)

## Reference Context

- UniProtKB:C6T1A2
- file:SOYBN/C6T1A2/C6T1A2-deep-research-falcon.md

## Source Context YAML

```yaml
description: C6T1A2 is predicted to function as a DNA-binding transcription factor based on its C2H2-type
  zinc finger domain (residues 79-106), its classification in the Zinc_finger_protein_7 family (IPR053266),
  and its inclusion in a soybean transcription factor ORFeome. No experimental evidence directly demonstrates
  transcription factor activity for this specific protein; the annotation is inferred from domain architecture
  and family membership. The protein coordinates a zinc ion via the C2H2 zinc finger motif to stabilize
  the DNA-binding fold.
molecular_function:
  id: GO:0003700
  label: DNA-binding transcription factor activity
locations:
- id: GO:0005634
  label: nucleus
supported_by:
- reference_id: UniProtKB:C6T1A2
  supporting_text: InterPro; IPR053266; Zinc_finger_protein_7.
- reference_id: UniProtKB:C6T1A2
  supporting_text: PANTHER; PTHR47593; ZINC FINGER PROTEIN 4-LIKE; 1.
- reference_id: file:SOYBN/C6T1A2/C6T1A2-deep-research-falcon.md
  supporting_text: Based on InterPro domain annotation showing C2H2-type zinc finger domains (IPR013087,
    IPR036236, IPR053266), this protein is predicted to function as a DNA-binding transcription factor
    localized to the nucleus.
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
**Generated:** 2026-06-21T22:30:13.641560

1. PMID:18347915
2. PMID:21367962
3. PMID:24808098
4. PMID:7599312
5. PMID:41495890
6. PMID:26268547
7. PMID:40158630
8. PMID:42260296
9. PMID:42115908
10. PMID:16227574