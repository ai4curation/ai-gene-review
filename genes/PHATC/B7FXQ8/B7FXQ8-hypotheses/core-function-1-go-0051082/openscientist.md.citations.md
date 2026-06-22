# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** PHATC
- **Taxon:** Phaeodactylum tricornutum (strain CCAP 1055/1) (NCBITaxon:556484)
- **Gene directory:** B7FXQ8
- **Gene symbol:** HSP20A
- **UniProt accession:** B7FXQ8

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0051082
- **Source file:** genes/PHATC/B7FXQ8/B7FXQ8-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

unfolded protein binding (GO:0051082) is a core function of HSP20A. Current rationale: HSP20A contains the conserved alpha-crystallin domain characteristic of the sHSP/HSP20 family, which mediates direct binding to partially unfolded, misfolded, or aggregation-prone client proteins through recognition of exposed hydrophobic surface regions. This holdase activity -- binding non-native proteins to prevent their irreversible aggregation -- is the primary molecular function of the sHSP family. The CDD annotation ACD_sHsps-like (cd06464) and InterPro domain IPR002068 confirm the presence of a functional alpha-crystallin domain competent for substrate binding. sHSPs exhibit broad, promiscuous substrate specificity for non-native proteins rather than targeting specific individual clients.

## Term and Decision Context

- Molecular function: unfolded protein binding (GO:0051082)
- Description: HSP20A contains the conserved alpha-crystallin domain characteristic of the sHSP/HSP20 family, which mediates direct binding to partially unfolded, misfolded, or aggregation-prone client proteins through recognition of exposed hydrophobic surface regions. This holdase activity -- binding non-native proteins to prevent their irreversible aggregation -- is the primary molecular function of the sHSP family. The CDD annotation ACD_sHsps-like (cd06464) and InterPro domain IPR002068 confirm the presence of a functional alpha-crystallin domain competent for substrate binding. sHSPs exhibit broad, promiscuous substrate specificity for non-native proteins rather than targeting specific individual clients.
- Directly involved in: response to heat (GO:0009408), protein complex oligomerization (GO:0051259), cellular response to unfolded protein (GO:0034620)
- Locations: cytoplasm (GO:0005737)

## Reference Context

- UniProt:B7FXQ8
- file:PHATC/B7FXQ8/B7FXQ8-deep-research-falcon.md

## Source Context YAML

```yaml
molecular_function:
  id: GO:0051082
  label: unfolded protein binding
description: HSP20A contains the conserved alpha-crystallin domain characteristic of the sHSP/HSP20 family,
  which mediates direct binding to partially unfolded, misfolded, or aggregation-prone client proteins
  through recognition of exposed hydrophobic surface regions. This holdase activity -- binding non-native
  proteins to prevent their irreversible aggregation -- is the primary molecular function of the sHSP
  family. The CDD annotation ACD_sHsps-like (cd06464) and InterPro domain IPR002068 confirm the presence
  of a functional alpha-crystallin domain competent for substrate binding. sHSPs exhibit broad, promiscuous
  substrate specificity for non-native proteins rather than targeting specific individual clients.
directly_involved_in:
- id: GO:0009408
  label: response to heat
- id: GO:0051259
  label: protein complex oligomerization
- id: GO:0034620
  label: cellular response to unfolded protein
locations:
- id: GO:0005737
  label: cytoplasm
supported_by:
- reference_id: UniProt:B7FXQ8
  supporting_text: Belongs to the small heat shock protein (HSP20) family. {ECO:0000256|PROSITE-ProRule:PRU00285,
    ECO:0000256|RuleBase:RU003616}.
- reference_id: UniProt:B7FXQ8
  supporting_text: DOMAIN 47..155 /note="SHSP" /evidence="ECO:0000259|PROSITE:PS01031"; InterPro IPR002068
    A-crystallin/Hsp20_dom; Pfam PF00011 HSP20; CDD cd06464 ACD_sHsps-like.
- reference_id: file:PHATC/B7FXQ8/B7FXQ8-deep-research-falcon.md
  supporting_text: HSP20A functions as an ATP-independent molecular chaperone, distinguishing it from
    ATP-dependent chaperones such as HSP70 and HSP90. Small heat shock proteins operate as holdase chaperones
    -- they bind to partially unfolded, misfolded, or aggregation-prone proteins and maintain them in
    a folding-competent state.
- reference_id: file:PHATC/B7FXQ8/B7FXQ8-deep-research-falcon.md
  supporting_text: 'HSP20 family proteins form dynamic oligomeric structures ranging from dimers to large
    assemblies of 24 or more subunits. The oligomeric state is functionally significant: dimers often
    represent the active chaperone form, while larger oligomers may serve as inactive storage pools.'
- reference_id: file:PHATC/B7FXQ8/B7FXQ8-deep-research-falcon.md
  supporting_text: In P. tricornutum, heat-shock transcription factor networks are unusually expanded
    and are implicated in temperature adaptation, with HSFs directly controlling thermal-tolerance programs.
    In related marine microalgae, HSP20-family genes are associated with heat tolerance and adaptation
    to environmental fluctuation.
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
**Generated:** 2026-06-22T00:02:11.816263

1. PMID:31091419
2. PMID:27744332
3. PMID:24045939
4. PMID:16143830
5. PMID:40210887
6. PMID:38525917
7. PMID:41926723
8. PMID:38959781
9. PMID:41967568
10. PMID:23661567
11. PMID:20621668
12. PMID:20075630
13. PMID:26116912
14. PMID:20378850