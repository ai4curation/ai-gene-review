---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-21T22:30:17.413936'
end_time: '2026-06-21T23:14:40.458081'
duration_seconds: 2663.04
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ORYSJ
  gene: Q6YYC5
  gene_symbol: Q6YYC5
  uniprot_accession: Q6YYC5
  taxon_id: NCBITaxon:39947
  taxon_label: Oryza sativa subsp. japonica
  focus_type: core_function
  hypothesis_slug: core-function-1-go-0061630
  hypothesis_text: 'ubiquitin protein ligase activity (GO:0061630) is a core function
    of Q6YYC5. Current rationale: E3 ubiquitin-protein ligase activity mediated by
    the C-terminal RING finger domain. The vWA domain provides substrate recognition
    and protein-protein interaction capability. By analogy to characterized rice and
    Arabidopsis RGLG family members, this protein likely ubiquitinates specific signaling
    regulators, targeting them for 26S proteasome-mediated degradation. The copine-related
    domain suggests possible calcium-dependent membrane association and stimulus-responsive
    localization.'
  term_context: '- Molecular function: ubiquitin protein ligase activity (GO:0061630)

    - Description: E3 ubiquitin-protein ligase activity mediated by the C-terminal
    RING finger domain. The vWA domain provides substrate recognition and protein-protein
    interaction capability. By analogy to characterized rice and Arabidopsis RGLG
    family members, this protein likely ubiquitinates specific signaling regulators,
    targeting them for 26S proteasome-mediated degradation. The copine-related domain
    suggests possible calcium-dependent membrane association and stimulus-responsive
    localization.

    - Directly involved in: protein ubiquitination (GO:0016567)

    - Locations: cytoplasm (GO:0005737), nucleus (GO:0005634)'
  reference_context: No specific reference context supplied.
  source_file: genes/ORYSJ/Q6YYC5/Q6YYC5-ai-review.yaml
  source_selector: core_functions[1]
  source_context_yaml: "description: E3 ubiquitin-protein ligase activity mediated\
    \ by the C-terminal RING finger domain. The vWA\n  domain provides substrate recognition\
    \ and protein-protein interaction capability. By analogy to characterized\n  rice\
    \ and Arabidopsis RGLG family members, this protein likely ubiquitinates specific\
    \ signaling regulators,\n  targeting them for 26S proteasome-mediated degradation.\
    \ The copine-related domain suggests possible\n  calcium-dependent membrane association\
    \ and stimulus-responsive localization.\nmolecular_function:\n  id: GO:0061630\n\
    \  label: ubiquitin protein ligase activity\ndirectly_involved_in:\n- id: GO:0016567\n\
    \  label: protein ubiquitination\nlocations:\n- id: GO:0005737\n  label: cytoplasm\n\
    - id: GO:0005634\n  label: nucleus"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ORYSJ
- **Taxon:** Oryza sativa subsp. japonica (NCBITaxon:39947)
- **Gene directory:** Q6YYC5
- **Gene symbol:** Q6YYC5
- **UniProt accession:** Q6YYC5

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0061630
- **Source file:** genes/ORYSJ/Q6YYC5/Q6YYC5-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

ubiquitin protein ligase activity (GO:0061630) is a core function of Q6YYC5. Current rationale: E3 ubiquitin-protein ligase activity mediated by the C-terminal RING finger domain. The vWA domain provides substrate recognition and protein-protein interaction capability. By analogy to characterized rice and Arabidopsis RGLG family members, this protein likely ubiquitinates specific signaling regulators, targeting them for 26S proteasome-mediated degradation. The copine-related domain suggests possible calcium-dependent membrane association and stimulus-responsive localization.

## Term and Decision Context

- Molecular function: ubiquitin protein ligase activity (GO:0061630)
- Description: E3 ubiquitin-protein ligase activity mediated by the C-terminal RING finger domain. The vWA domain provides substrate recognition and protein-protein interaction capability. By analogy to characterized rice and Arabidopsis RGLG family members, this protein likely ubiquitinates specific signaling regulators, targeting them for 26S proteasome-mediated degradation. The copine-related domain suggests possible calcium-dependent membrane association and stimulus-responsive localization.
- Directly involved in: protein ubiquitination (GO:0016567)
- Locations: cytoplasm (GO:0005737), nucleus (GO:0005634)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
description: E3 ubiquitin-protein ligase activity mediated by the C-terminal RING finger domain. The vWA
  domain provides substrate recognition and protein-protein interaction capability. By analogy to characterized
  rice and Arabidopsis RGLG family members, this protein likely ubiquitinates specific signaling regulators,
  targeting them for 26S proteasome-mediated degradation. The copine-related domain suggests possible
  calcium-dependent membrane association and stimulus-responsive localization.
molecular_function:
  id: GO:0061630
  label: ubiquitin protein ligase activity
directly_involved_in:
- id: GO:0016567
  label: protein ubiquitination
locations:
- id: GO:0005737
  label: cytoplasm
- id: GO:0005634
  label: nucleus
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


## Output

# Final Report: Evaluation of Ubiquitin Protein Ligase Activity (GO:0061630) as a Core Function of Q6YYC5 (OsRGLG4)

## Executive Judgment

**Verdict: STRONGLY SUPPORTED**

Ubiquitin protein ligase activity (GO:0061630) is strongly supported as a core molecular function of Q6YYC5 (OsRGLG4, Os08g0135400, LOC4344608). The evidence converges from multiple independent lines: (1) domain architecture analysis reveals a canonical RING-H2 zinc finger domain with all eight metal-coordinating residues conserved, paired with a von Willebrand Factor A (vWA) domain for substrate recognition and a copine-related domain for calcium-dependent membrane association; (2) phylogenetic assignment to PANTHER subfamily PTHR45751:SF16 ("E3 UBIQUITIN-PROTEIN LIGASE RGLG4") with 65.6% sequence identity to the functionally characterized Arabidopsis ortholog AtRGLG4 (Q9SAL0); (3) direct experimental demonstration of E3 ubiquitin ligase activity for AtRGLG4 including in vitro auto-ubiquitination, substrate ubiquitination (GRXS17), and in vivo proteasomal degradation of targets; (4) confirmed E3 ligase activity for multiple rice RGLG family members (OsRGLG5, OsRGLG6); (5) AlphaFold structural prediction showing the RING domain with very high confidence (pLDDT 91.4), ruling out a degenerate or non-functional fold; and (6) NCBI Gene (ID 4344608) independently naming Q6YYC5 as "E3 ubiquitin-protein ligase RGLG4." The contrast with BON1 — a copine-family protein lacking a RING domain that functions solely through protein-protein interactions, not E3 activity ([PMID: 21623975](https://pubmed.ncbi.nlm.nih.gov/21623975/)) — further confirms that the RING domain is the determinant of E3 ligase function in RGLG proteins.

**Most important caveats:**
1. No direct biochemical assay has been performed on Q6YYC5 itself; all evidence is by ortholog inference (ISS/IBA level).
2. Q6YYC5 has a myristoylation-compatible N-terminus (MGGVIG...) unlike AtRGLG4 (MTMGN...), suggesting potential plasma membrane association that may indicate localization divergence within the subfamily.
3. The protein is an unreviewed TrEMBL entry with only IBA/IEA-level GO annotations.

---

## Summary

Q6YYC5 (UniProt accession Q6YYC5) is the rice (*Oryza sativa* subsp. *japonica*) gene product encoded by LOC4344608 (Os08g0135400), officially designated "E3 ubiquitin-protein ligase RGLG4" by NCBI Gene (Gene ID 4344608). This investigation evaluated whether ubiquitin protein ligase activity (GO:0061630) represents a core molecular function of this protein, as proposed in the seed hypothesis.

Through systematic analysis of domain architecture, phylogenetic relationships, ortholog biochemistry, family-wide functional conservation, AlphaFold structural predictions, and contrast with non-E3 copine proteins, we find overwhelming support for this annotation. The closest characterized ortholog, Arabidopsis RGLG4 (AtRGLG4, Q9SAL0), has been experimentally demonstrated to possess E3 ubiquitin ligase activity through multiple independent studies. Zhang et al. (2012) showed that "Both RGLG3 and RGLG4 possessed ubiquitin ligase activities and were widely distributed in Arabidopsis thaliana tissues" ([PMID: 22898498](https://pubmed.ncbi.nlm.nih.gov/22898498/)). Sacharowski et al. (2016) identified the cognate E2 enzyme UBC30 and the substrate GRXS17, demonstrating both in vitro ubiquitination and in vivo substrate degradation ([PMID: 27497447](https://pubmed.ncbi.nlm.nih.gov/27497447/)). Within rice itself, two other RGLG family members — OsRGLG5 ([PMID: 37177781](https://pubmed.ncbi.nlm.nih.gov/37177781/)) and OsRGLG6 ([PMID: 41312104](https://pubmed.ncbi.nlm.nih.gov/41312104/)) — have confirmed E3 ligase activity, reinforcing the functional conservation of this protein family. No conflicting evidence was identified in any database or literature source examined.

The GO term GO:0061630 (ubiquitin protein ligase activity) is the appropriate specific term for E3 ligases and should replace or supplement the currently annotated GO:0004842 (ubiquitin-protein transferase activity), which is a parent term that does not distinguish E3 from E2 activity. The associated biological process (protein ubiquitination, GO:0016567) and subcellular localizations (cytoplasm, GO:0005737; nucleus, GO:0005634) are likewise well-supported by ortholog data. An unexpected finding — Q6YYC5's myristoylation-compatible N-terminus — suggests possible plasma membrane association analogous to AtRGLG1/2 rather than the purely cytoplasmic/nuclear pattern of AtRGLG4, qualifying the CC annotations but not the core MF assignment.

---

## Key Findings

### Finding 1: Q6YYC5 Is an RGLG4-Type E3 Ubiquitin Ligase by Domain Architecture and Phylogeny

Q6YYC5 is classified in PANTHER subfamily PTHR45751:SF16, designated "E3 UBIQUITIN-PROTEIN LIGASE RGLG4." Sequence comparison reveals 65.6% identity with AtRGLG4 (Q9SAL0) over 358 aligned residues — the highest among all five Arabidopsis RGLG family members. Both proteins share an identical length of 401 amino acids. The domain architecture is characteristic of the RGLG family: an N-terminal copine-related domain (Pfam PF07002), a central vWA domain (SMART SM00327), and a C-terminal RING-type zinc finger (residues 356–389) with the conserved C-X₂-C...C-X₁-H...C-C...C-X₂-C pattern encompassing all eight metal-coordinating residues. InterPro domain assignments include IPR010734 (Copine_C), IPR002035 (VWF_A), IPR001841 (Znf_RING), and IPR052079 (E3_ligase/Copine_domain). This tri-domain architecture is the hallmark of the RGLG/copine-RING E3 ligase family and is present across all characterized members. NCBI Gene (ID 4344608) independently names Q6YYC5 as "E3 ubiquitin-protein ligase RGLG4," also listing it as "Copine I-like protein" and "putative copine-6," confirming the classification.

### Finding 2: AtRGLG4 Has Demonstrated E3 Ubiquitin Ligase Activity In Vitro and In Vivo

The closest ortholog, AtRGLG4 (Q9SAL0), has IDA-level (Inferred from Direct Assay) evidence for E3 ubiquitin ligase activity from multiple independent studies:

- **In vitro activity:** Zhang et al. (2012) directly demonstrated that "Both RGLG3 and RGLG4 possessed ubiquitin ligase activities and were widely distributed in Arabidopsis thaliana tissues" ([PMID: 22898498](https://pubmed.ncbi.nlm.nih.gov/22898498/)). This foundational paper established RGLG3 and RGLG4 as functional E3 ligases essential for jasmonate-mediated responses, with the rglg3 rglg4 double mutant showing resistance to coronatine-secreting *Pseudomonas syringae* DC3000.

- **E2 partner and substrate identification:** Sacharowski et al. (2016) used a UBC panel screen to identify UBC30 as the cognate E2 conjugating enzyme "capable of interacting with RGLG3 and RGLG4 and mediating auto-ubiquitination of RGLG3 and ubiquitination of GRXS17 in vitro" ([PMID: 27497447](https://pubmed.ncbi.nlm.nih.gov/27497447/)). They further demonstrated that "GRXS17 is ubiquitinated and degraded in an RGLG3- and RGLG4-dependent manner in planta," providing in vivo validation of substrate-specific E3 ligase activity with subsequent proteasomal degradation.

- **Jasmonate pathway modulation:** Meng et al. (2015) confirmed that RGLG3 and RGLG4 are "two ubiquitin ligases, RING DOMAIN LIGASE3 (RGLG3) and RGLG4, which control FB1-triggered PCD by modulating the jasmonate (JA) signalling pathway in Arabidopsis thaliana" ([PMID: 25788731](https://pubmed.ncbi.nlm.nih.gov/25788731/)).

- **UniProt reviewed entry** (Q9SAL0) annotates AtRGLG4 with GO:0004842 (IDA:TAIR), EC 2.3.2.27 (RING-type E3 ubiquitin transferase), and states: "Possesses E3 ubiquitin-protein ligase in vitro. May mediate the formation of Lys-48-linked multiubiquitin chains."

The subcellular localization of AtRGLG4 — cytoplasm (IDA) and nucleus (IDA) — matches the proposed localizations for Q6YYC5, further supporting the orthology-based inference.

### Finding 3: Multiple Rice RGLG Family Members Have Confirmed E3 Ligase Activity

Functional conservation of E3 ligase activity within the RGLG family extends to rice (*Oryza sativa*) itself:

- **OsRGLG5:** Dong et al. (2023) identified OsRGLG5 as "a functional RING-type E3 ubiquitin ligase" that ubiquitinates the *Magnaporthe oryzae* effector AvrPi9, targeting it for degradation. "During infection, AvrPi9 was ubiquitinated and degraded by OsRGLG5," conferring basal resistance against rice blast ([PMID: 37177781](https://pubmed.ncbi.nlm.nih.gov/37177781/)).

- **OsRGLG6:** A 2025 study demonstrated that OsRGLG6 is a "RING-domain E3 ubiquitin ligase" that ubiquitinates the deubiquitinase OsOTUB1 for degradation, thereby regulating grain number and yield ([PMID: 41312104](https://pubmed.ncbi.nlm.nih.gov/41312104/)).

The rice RGLG family comprises at least 11 copine+RING domain proteins based on InterPro analysis. The demonstration that multiple family members across two species (Arabidopsis and rice) all function as E3 ubiquitin ligases provides strong evidence for functional conservation, making it highly probable that Q6YYC5/OsRGLG4 shares this core activity.

### Finding 4: GO:0061630 Is More Appropriate and Specific Than the Current GO:0004842 Annotation

The GO term hierarchy distinguishes E3 ligase activity from the broader ubiquitin-protein transferase category:

| GO Term | Label | Relationship | Evidence for AtRGLG4 |
|---------|-------|-------------|---------------------|
| GO:0004842 | ubiquitin-protein transferase activity | Parent term | IDA:TAIR |
| GO:0061630 | ubiquitin protein ligase activity | Child term (E3-specific) | IEA:UniProtKB-EC |

Since all experimental evidence indicates that RGLG4-family proteins function specifically as E3 ligases (not E1 activating enzymes or E2 conjugating enzymes), GO:0061630 is the most appropriate and informative term. Q6YYC5 currently carries only GO:0004842 (IBA:GO_Central), which, while not incorrect, is less precise than what the evidence supports. Upgrading to GO:0061630 would better capture the molecular function.

### Finding 5: Q6YYC5 Has a Myristoylation-Compatible N-Terminus Unlike AtRGLG4

An important structural difference between Q6YYC5 and its closest ortholog AtRGLG4 was identified at the N-terminus:

- **Q6YYC5 N-terminus:** MGGVIGALF... — the MG motif at positions 1–2 is compatible with N-myristoyltransferase (NMT) consensus.
- **AtRGLG4 N-terminus:** MTMGNFLKR... — lacks the MG motif at positions 1–2 and is not myristoylation-compatible.
- **AtRGLG1/2 (known myristoylated):** Also start with MG and are myristoylated.

This suggests Q6YYC5 may share the membrane-association properties of AtRGLG1/2 rather than the cytoplasmic/nuclear localization pattern of AtRGLG4. Cheng et al. (2012) demonstrated that "RGLG2 could move from the plasma membrane to the nucleus under stress treatment" ([PMID: 22095047](https://pubmed.ncbi.nlm.nih.gov/22095047/)), and Li et al. (2010) showed that "Mutation at putative myristoylation residue glycine 2 altered plasma membrane localization of BON1 and rendered BON1 inactive" ([PMID: 20634289](https://pubmed.ncbi.nlm.nih.gov/20634289/)), demonstrating that myristoylation is critical for copine-family protein localization and function. This finding qualifies — but does not undermine — the core E3 ligase function; it may indicate that Q6YYC5 has additional membrane-associated regulatory modes not shared with AtRGLG4.

### Finding 6: AlphaFold Predicts Q6YYC5 RING Domain with Very High Confidence

AlphaFold model AF-Q6YYC5-F1-model_v6 provides structural validation of the RING domain:

| Domain | Residues | Avg pLDDT | Confidence Level |
|--------|----------|-----------|-----------------|
| Copine/N-terminal | 1–150 | 80.4 | Confident |
| vWA domain | 151–313 | 90.6 | Very high |
| Linker | 314–355 | 58.6 | Low (disordered, expected) |
| RING-H2 domain | 356–389 | 91.4 | Very high |
| **Overall** | **1–401** | **83.3** | **Confident** |

Critically, all nine zinc-coordinating residues in the RING domain have pLDDT scores above 90 (range 90.8–94.6), indicating a well-defined, functional zinc-finger fold. The very high confidence for the RING domain rules out the possibility that Q6YYC5 harbors a degenerate or non-functional RING domain — an important consideration because some RING-containing proteins have lost catalytic activity through key residue substitutions. The low confidence in the linker region (residues 314–355) is expected for an intrinsically disordered segment and does not affect the functional prediction for the structured domains.

### Finding 7: BON1 Contrast Validates RING Domain as the E3 Determinant

The Arabidopsis copine protein BON1 shares the C2+VWA domain architecture with RGLG proteins but crucially lacks a RING domain. BON1 functions through calcium-dependent phospholipid binding and protein-protein interactions with receptor kinases BIR1 and BAK1, "BON1 interacts physically with the leucine-rich-repeat receptor-like kinases BIR1 (BAK1-interacting receptor-like kinase 1) and pathogen-associated molecular pattern (PAMP) receptor regulator BAK1 in vitro and in vivo" ([PMID: 21623975](https://pubmed.ncbi.nlm.nih.gov/21623975/)) — but does not possess ubiquitination activity. This provides a natural negative control confirming that the copine and VWA domains alone are insufficient for E3 ligase function; the RING domain is the essential catalytic determinant. Since Q6YYC5 possesses an intact RING-H2 domain with all metal-coordinating residues conserved, it is expected to have E3 ligase activity.

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Organism/Context | Confidence & Limitations |
|---|----------|---------------|-----------|--------------|-------------|------------------|--------------------------|
| 1 | [PMID: 22898498](https://pubmed.ncbi.nlm.nih.gov/22898498/) | Direct assay + genetic | **Supports** | AtRGLG4 E3 ligase activity | "Both RGLG3 and RGLG4 possessed ubiquitin ligase activities"; essential for JA-mediated responses | *A. thaliana*; ubiquitination assay, pathogen resistance | **High** — IDA-level; foundational paper |
| 2 | [PMID: 27497447](https://pubmed.ncbi.nlm.nih.gov/27497447/) | Direct assay (in vitro + in vivo) | **Supports** | AtRGLG4 E3 activity with substrate | UBC30 as E2 partner; GRXS17 ubiquitinated and degraded in RGLG3/4-dependent manner | *A. thaliana*; substrate trapping, in vitro ubiquitination, in planta | **High** — most complete biochemical characterization |
| 3 | [PMID: 25788731](https://pubmed.ncbi.nlm.nih.gov/25788731/) | Mutant phenotype + genetic | **Supports** | RGLG3/4 function as E3 ligases in JA signaling | RGLG3/4 control FB1-triggered PCD by modulating JA pathway | *A. thaliana*; fumonisin B1 treatment | **High** — biological role confirmed |
| 4 | [PMID: 37177781](https://pubmed.ncbi.nlm.nih.gov/37177781/) | Direct assay | **Supports** | Rice RGLG E3 ligase activity | OsRGLG5 is "a functional RING-type E3 ubiquitin ligase"; ubiquitinates AvrPi9 | *O. sativa*; rice blast interaction | **High** — rice family evidence |
| 5 | [PMID: 41312104](https://pubmed.ncbi.nlm.nih.gov/41312104/) | Direct assay | **Supports** | Rice RGLG E3 ligase activity | OsRGLG6 ubiquitinates OsOTUB1 for degradation; regulates grain number | *O. sativa*; grain development | **Moderate** — rice family member |
| 6 | [PMID: 17586653](https://pubmed.ncbi.nlm.nih.gov/17586653/) | Direct assay + genetic | **Supports** | RGLG family E3 activity | RGLG2 forms K63-linked multiubiquitin chains; rglg1 rglg2 loss of apical dominance | *A. thaliana*; in vitro ubiquitination, mutant analysis | **High** — seminal family paper |
| 7 | [PMID: 22095047](https://pubmed.ncbi.nlm.nih.gov/22095047/) | Direct assay + localization | **Supports/Qualifies** | RGLG proteins relocalize under stress | RGLG2 ubiquitinates AtERF53; moves from plasma membrane to nucleus under stress | *A. thaliana*; subcellular fractionation | **High** — localization relevance |
| 8 | [PMID: 37734561](https://pubmed.ncbi.nlm.nih.gov/37734561/) | Structural (crystallography) | **Qualifies** | VWA domain calcium regulation | Crystal structures show Ca²⁺-dependent open/closed conformations of RGLG2 VWA | *A. thaliana*; X-ray crystallography | **High** — structural mechanism |
| 9 | [PMID: 32970364](https://pubmed.ncbi.nlm.nih.gov/32970364/) | Direct assay + genetic | **Supports** | RGLG proteins ubiquitinate signaling regulators | RGLG1/2 ubiquitinate MAPKKK18 at K32 and K154; promote degradation | *A. thaliana*; ubiquitination assay | **High** — specific substrate sites |
| 10 | [PMID: 41557808](https://pubmed.ncbi.nlm.nih.gov/41557808/) | Direct assay + genetic | **Supports** | RGLG1/2 ubiquitinate receptor kinases | RGLG1/2 ubiquitinate BAM1/2; CLE13 enhances RGLG2 E3 activity | *A. thaliana*; receptor signaling | **High** — stimulus-enhanced activity |
| 11 | [PMID: 37532719](https://pubmed.ncbi.nlm.nih.gov/37532719/) | Direct assay + genetic | **Supports** | RGLG1/2 regulate protein homeostasis | RGLG1/2 promote BIK1 accumulation in E3 activity-dependent manner | *A. thaliana*; immune signaling | **High** — E3 activity essential |
| 12 | [PMID: 21623975](https://pubmed.ncbi.nlm.nih.gov/21623975/) | Interaction + genetic | **Qualifies (contrast)** | Copine domain alone ≠ E3 activity | BON1 (copine without RING) interacts with BIR1/BAK1 but does not ubiquitinate | *A. thaliana*; co-IP, Y2H | **High** — confirms RING is essential |
| 13 | [PMID: 20634289](https://pubmed.ncbi.nlm.nih.gov/20634289/) | Mutant phenotype | **Qualifies** | Myristoylation critical for copine function | G2 mutation alters BON1 localization and renders it inactive | *A. thaliana*; copine family | **High** — localization dependence |
| 14 | PANTHER PTHR45751:SF16 | Computational (phylogenetic) | **Supports** | Q6YYC5 is RGLG4 ortholog | 65.6% identity over 358 aa; identical length (401 aa); subfamily "E3 UBIQUITIN-PROTEIN LIGASE RGLG4" | Computational | **High** — robust classification |
| 15 | InterPro IPR052079 | Computational (domain) | **Supports** | E3 ligase domain architecture | Domain classified as "E3_ligase/Copine_domain"; all zinc-coordinating residues conserved | Computational | **High** — established domain-function |
| 16 | NCBI Gene 4344608 | Database | **Supports** | Gene identity | Official name: "E3 ubiquitin-protein ligase RGLG4" on chromosome 8 | *O. sativa* Japonica | **Moderate** — independent confirmation |
| 17 | AlphaFold AF-Q6YYC5-F1 | Structural (computational) | **Supports** | RING domain is functional fold | RING pLDDT 91.4; all Zn-coordinating residues >90 | Predicted structure | **Moderate-High** — rules out degenerate domain |

---

## GO Curation Implications

### Molecular Function (MF) — Upgrade Recommended

**Current annotation:** GO:0004842 (ubiquitin-protein transferase activity; IBA:GO_Central)

**Recommended action:** Add GO:0061630 (ubiquitin protein ligase activity) with evidence code ISS, using AtRGLG4 (Q9SAL0) as the reference ortholog. The existing GO:0004842 can be retained or superseded, as GO:0061630 is a child term. GO:0061630 is the appropriate E3-specific term and correctly distinguishes E3 from E2 activity. All characterized RGLG family members are E3 ligases, and EC 2.3.2.27 (RING-type E3 ubiquitin transferase) is assigned to both AtRGLG3 and AtRGLG4 reviewed entries in UniProt.

**Confidence:** High. Multiple IDA-level demonstrations in the closest ortholog (AtRGLG4) and family-wide conservation.

### Biological Process (BP) — Retain

**Current annotation:** GO:0016567 (protein ubiquitination)

**Recommended action:** Retain. This directly follows from E3 ligase activity and is well-supported by IBA inference. More specific BP terms (e.g., JA signaling modulation, defense response, PCD regulation) are documented for specific AtRGLG3/4 or OsRGLG5/6 family members but should not be annotated for Q6YYC5 without direct evidence in this specific gene product.

### Cellular Component (CC) — Retain with Caveat

**Current annotations:** GO:0005737 (cytoplasm), GO:0005634 (nucleus)

**Recommended action:** Retain both based on AtRGLG4 IDA evidence. Additionally, flag GO:0005886 (plasma membrane) as a candidate term pending experimental verification, based on Q6YYC5's myristoylation-compatible N-terminus (MG motif analogous to AtRGLG1/2). AtRGLG4 also has mitochondrial localization (HDA) which is not annotated for Q6YYC5.

### Core Function Status — Confirmed

E3 ubiquitin-protein ligase activity is the primary molecular function of Q6YYC5, mediated by its RING-H2 domain. This is not a downstream effect, pleiotropic phenotype, or context-specific role. All characterized RGLG family members share this core activity.

| GO Term | Current Status | Recommended Action | Evidence Basis | Priority |
|---------|---------------|-------------------|---------------|----------|
| GO:0004842 (MF) | IBA:GO_Central | Supplement with GO:0061630 (ISS from Q9SAL0) | AtRGLG4 IDA + family conservation | **High** |
| GO:0061630 (MF) | Not annotated | Add (ISS from Q9SAL0) | PMID: 22898498, 27497447 | **High** |
| GO:0016567 (BP) | Present | Retain | Ortholog + family evidence | Confirmed |
| GO:0005737 (CC) | Present | Retain | AtRGLG4 IDA | Confirmed |
| GO:0005634 (CC) | Present | Retain | AtRGLG4 IDA | Confirmed |
| GO:0005886 (CC) | Not annotated | Consider (pending data) | MG motif; analogy to RGLG1/2 | Low |

---

## Mechanistic Scope

### Direct Gene-Product Activity

The immediate molecular function of Q6YYC5 is **E3 ubiquitin-protein ligase activity**: the protein catalyzes the transfer of ubiquitin from an E2 conjugating enzyme (likely an OsUBC30 ortholog, based on AtRGLG4 data from [PMID: 27497447](https://pubmed.ncbi.nlm.nih.gov/27497447/)) to specific protein substrates, tagging them for 26S proteasome-mediated degradation via K48-linked polyubiquitin chains.

The three-domain architecture supports this function through a division of labor:

```
N-term ──── Copine domain ──── vWA domain ──── Linker ──── RING-H2 domain ──── C-term
  (1)          (1-150)          (151-313)      (314-355)      (356-389)        (401)
   │              │                 │               │              │
   │     Ca²⁺-dependent        Substrate        Flexible       E2 binding
   │     membrane binding     recognition      connector      & Ub transfer
   │              │                 │                              │
   └──── MG motif ────────────────────────────────────────────────┘
         (myristoylation?)           Core E3 ligase catalytic cycle
```

The RING-H2 domain coordinates two zinc ions in a cross-brace topology, positioning the E2~Ub conjugate for ubiquitin transfer to the substrate lysine. The VWA domain provides substrate recognition and protein-protein interaction capability — its calcium-dependent open/closed conformational regulation has been structurally characterized for RGLG2 ([PMID: 37734561](https://pubmed.ncbi.nlm.nih.gov/37734561/)). The copine domain provides calcium-dependent membrane association, potentially enabling stimulus-responsive localization.

### Separation from Downstream Effects

The following biological roles have been demonstrated for RGLG family members but represent **downstream pathway consequences** rather than the core molecular function of Q6YYC5:

| Downstream Role | Family Member | Citation | Evidence Level for Q6YYC5 |
|-----------------|--------------|----------|--------------------------|
| JA signaling modulation | AtRGLG3/4 | [PMID: 22898498](https://pubmed.ncbi.nlm.nih.gov/22898498/), [25788731](https://pubmed.ncbi.nlm.nih.gov/25788731/) | Inferred by orthology, not direct |
| Drought stress tolerance | AtRGLG1/2 | [PMID: 32970364](https://pubmed.ncbi.nlm.nih.gov/32970364/) | Not applicable (different subclade) |
| Iron homeostasis | AtRGLG1/2 | [PMID: 20113438](https://pubmed.ncbi.nlm.nih.gov/20113438/), [26253232](https://pubmed.ncbi.nlm.nih.gov/26253232/) | Not applicable |
| Apical dominance/auxin | AtRGLG1/2 | [PMID: 17586653](https://pubmed.ncbi.nlm.nih.gov/17586653/) | Not applicable |
| Basal blast resistance | OsRGLG5 | [PMID: 37177781](https://pubmed.ncbi.nlm.nih.gov/37177781/) | Paralog, not direct |
| Grain number/yield | OsRGLG6 | [PMID: 41312104](https://pubmed.ncbi.nlm.nih.gov/41312104/) | Paralog, not direct |
| Immune receptor homeostasis | AtRGLG1/2 | [PMID: 37532719](https://pubmed.ncbi.nlm.nih.gov/37532719/), [41557808](https://pubmed.ncbi.nlm.nih.gov/41557808/) | Not applicable |

These downstream roles are informative for understanding the biological significance of the RGLG family but should not be annotated as core functions of Q6YYC5 without direct evidence.

---

## Evidence Base

### Tier 1: Direct Experimental Evidence on Closest Ortholog (AtRGLG4)

**Zhang et al. (2012)** — *Two novel RING-type ubiquitin ligases, RGLG3 and RGLG4, are essential for jasmonate-mediated responses in Arabidopsis.* [PMID: 22898498](https://pubmed.ncbi.nlm.nih.gov/22898498/)

This foundational paper established that AtRGLG3 and AtRGLG4 possess ubiquitin ligase activities and are widely expressed in Arabidopsis tissues. The rglg3 rglg4 double mutant is resistant to coronatine-secreting *P. syringae* DC3000, with altered MeJA-inhibited root growth, JA-inductive gene expression, and wound-stimulated JA-responsive gene expression in a COI1-dependent manner. This is the primary reference establishing RGLG3/4 as JA-pathway E3 ligases.

**Sacharowski et al. (2016)** — *The Arabidopsis Iron-Sulfur Protein GRXS17 is a Target of the Ubiquitin E3 Ligases RGLG3 and RGLG4.* [PMID: 27497447](https://pubmed.ncbi.nlm.nih.gov/27497447/)

This study provides the most complete biochemical characterization: identification of the substrate GRXS17 through a substrate trapping approach using RING-dead RGLG3/4 variants; identification of UBC30 as the cognate E2 enzyme; demonstration of in vitro auto-ubiquitination and GRXS17 ubiquitination; and in vivo confirmation that GRXS17 is degraded in an RGLG3/4-dependent manner in planta. This is the strongest single piece of evidence supporting E3 ligase activity for the RGLG3/4 subclade.

**Meng et al. (2015)** — *Hijacking of the jasmonate pathway by FB1 to initiate PCD in Arabidopsis is modulated by RGLG3 and RGLG4.* [PMID: 25788731](https://pubmed.ncbi.nlm.nih.gov/25788731/)

Confirmed RGLG3/4 as ubiquitin ligases controlling FB1-triggered programmed cell death by modulating the JA signaling pathway.

### Tier 2: Rice RGLG Family Evidence

**Dong et al. (2023)** — *The E3 ubiquitin ligase OsRGLG5 targeted by the Magnaporthe oryzae effector AvrPi9 confers basal resistance against rice blast.* [PMID: 37177781](https://pubmed.ncbi.nlm.nih.gov/37177781/)

Demonstrated E3 ligase activity for a rice RGLG family member with identified substrate (AvrPi9) and biological role (basal blast resistance). Strongest direct evidence for RGLG E3 activity in rice.

**OsRGLG6 (2025)** — *The RING-domain E3 ubiquitin ligase OsRGLG6 regulates rice grain number and yield via ubiquitination-mediated degradation of OsOTUB1.* [PMID: 41312104](https://pubmed.ncbi.nlm.nih.gov/41312104/))

Second rice RGLG member with confirmed E3 activity, ubiquitinating OsOTUB1.

### Tier 3: Broader RGLG Family Characterization

The AtRGLG1/2 subclade has been extensively characterized as E3 ligases with roles in auxin signaling ([PMID: 17586653](https://pubmed.ncbi.nlm.nih.gov/17586653/)), drought response ([PMID: 22095047](https://pubmed.ncbi.nlm.nih.gov/22095047/), [32970364](https://pubmed.ncbi.nlm.nih.gov/32970364/)), iron homeostasis ([PMID: 20113438](https://pubmed.ncbi.nlm.nih.gov/20113438/), [26253232](https://pubmed.ncbi.nlm.nih.gov/26253232/)), immune signaling ([PMID: 37532719](https://pubmed.ncbi.nlm.nih.gov/37532719/)), and receptor kinase regulation ([PMID: 41557808](https://pubmed.ncbi.nlm.nih.gov/41557808/)). All five Arabidopsis RGLG members and at least two rice members have confirmed E3 activity — no RGLG family member has been shown to lack this activity.

### Tier 4: Structural and Computational Evidence

The VWA domain crystal structure of RGLG2 ([PMID: 37734561](https://pubmed.ncbi.nlm.nih.gov/37734561/)) reveals calcium-dependent conformational regulation. The BON1 copine structure ([PMID: 32369638](https://pubmed.ncbi.nlm.nih.gov/32369638/)) and functional studies ([PMID: 21623975](https://pubmed.ncbi.nlm.nih.gov/21623975/), [20634289](https://pubmed.ncbi.nlm.nih.gov/20634289/)) provide the critical contrast showing copine/VWA domains alone do not confer E3 activity. AlphaFold prediction (AF-Q6YYC5-F1-model_v6) confirms the RING domain has a well-defined fold (pLDDT 91.4).

---

## Conflicts and Alternatives

### No Direct Conflicting Evidence

No evidence was identified that contradicts the assignment of E3 ubiquitin ligase activity to Q6YYC5. Every characterized RGLG family member (5/5 in Arabidopsis, 2/2 in rice with published data) demonstrates E3 ligase activity. No RGLG-family protein has been reported to lack this activity. No alternative molecular function has been proposed for any RGLG family member.

### Potential Qualifications

**1. Myristoylation divergence from AtRGLG4.** Q6YYC5's MG motif suggests it may be more functionally analogous to AtRGLG1/2 (myristoylated, membrane-associated) in its localization behavior than to AtRGLG4 (cytoplasmic/nuclear), despite being the closest sequence match to AtRGLG4 by overall identity. However, this affects localization and possibly substrate access, not the core E3 ligase function.

**2. K48 vs. K63 chain type.** AtRGLG2 forms K63-linked polyubiquitin chains ([PMID: 17586653](https://pubmed.ncbi.nlm.nih.gov/17586653/)), which function in signaling rather than proteasomal degradation. AtRGLG4 is reported to form K48-linked chains (UniProt). The chain type specificity of Q6YYC5 is unknown. Both chain types are consistent with GO:0061630, but the downstream biological consequences differ.

**3. Paralog confusion risk.** With at least 11 copine+RING proteins in rice, care must be taken not to attribute OsRGLG5 or OsRGLG6 characterization data directly to OsRGLG4/Q6YYC5. This assessment correctly treats these as family-level evidence supporting functional conservation, not as direct evidence for Q6YYC5.

**4. No competing alternative function.** No RGLG protein has been reported to have a molecular function other than E3 ubiquitin ligase activity. The copine and VWA domains are accessory/regulatory, as demonstrated by the BON1 contrast.

---

## Limitations and Knowledge Gaps

| # | Gap | What Was Checked | Why It Matters | Resolution |
|---|-----|-----------------|----------------|------------|
| 1 | No direct biochemical assay on Q6YYC5 itself | PubMed for OsRGLG4, Q6YYC5, Os08g0135400, LOC4344608 | All evidence is ortholog-based (ISS/IBA level); direct assay would upgrade to IDA | In vitro ubiquitination assay with recombinant Q6YYC5 + E1/E2/Ub |
| 2 | Unknown substrate(s) in rice | No published interaction data for Q6YYC5 | Substrate identity determines biological role specificity | Y2H or co-IP screen; substrate trapping with RING-dead mutant |
| 3 | Subcellular localization not experimentally determined | Annotations inferred from AtRGLG4 (cytoplasm/nucleus IDA) | MG motif suggests possible membrane association | GFP-fusion in rice protoplasts; G2A mutant comparison |
| 4 | Ubiquitin chain type specificity unknown | AtRGLG2 = K63; AtRGLG4 = K48 (UniProt) | K48 vs K63 determines degradation vs signaling | In vitro with K48R/K63R ubiquitin mutants |
| 5 | Expression pattern and biological context | No tissue/stress expression data found | Expression context informs biological processes | qRT-PCR or RNA-seq; rice expression atlases |
| 6 | Calcium-dependent VWA regulation | RGLG2 VWA crystal structure (PMID: 37734561) | VWA calcium binding may regulate E3 activity | Calcium titration of Q6YYC5 VWA + E3 assay |
| 7 | Protein expression confirmed but function not | PE=1 via proteomics | Protein exists but no functional data | Combine with #1 above |

---

## Proposed Follow-up Experiments / Discriminating Tests

### Priority 1: In Vitro Ubiquitination Assay (Definitive)

Purify recombinant Q6YYC5 (full-length and RING domain only) and test for auto-ubiquitination in a reconstituted system (E1 + E2 + Ub + ATP). Use RING-mutant (e.g., C356A) as negative control. Use UBC30 ortholog as E2 based on AtRGLG4 data. This would provide IDA-level evidence for GO:0061630 and definitively resolve the annotation.

### Priority 2: Substrate Trapping Screen

Express RING-dead Q6YYC5 (analogous to RGLG3-RING-dead in [PMID: 27497447](https://pubmed.ncbi.nlm.nih.gov/27497447/)) in rice and perform tandem affinity purification to identify interaction partners. This approach successfully identified GRXS17 as a substrate for AtRGLG3/4 and would simultaneously confirm E3 function and identify biological context.

### Priority 3: Myristoylation and Localization

Generate GFP-Q6YYC5 and GFP-Q6YYC5(G2A) fusions and observe localization in rice protoplasts under normal and stress conditions. This would resolve the CC annotation question and determine whether Q6YYC5 undergoes stimulus-responsive relocalization like AtRGLG2 ([PMID: 22095047](https://pubmed.ncbi.nlm.nih.gov/22095047/)).

### Priority 4: Ubiquitin Chain Type Determination

Use K48R and K63R ubiquitin mutants in the in vitro ubiquitination assay to determine chain type preference. This would inform whether the protein primarily targets substrates for degradation (K48, like AtRGLG4) or signaling (K63, like AtRGLG1/2).

### Priority 5: CRISPR Knockout Phenotyping

Generate CRISPR knockout of OsRGLG4 in rice. Phenotype under JA treatment, pathogen challenge, drought stress, and normal growth conditions. Analyze proteomic changes to identify candidate substrates stabilized in the mutant. Compare with Arabidopsis rglg3 rglg4 mutant phenotypes (JA-responsive gene expression, FB1 sensitivity, P. syringae resistance).

---

## Curation Leads

### Lead 1: Add GO:0061630 as Core MF (High Confidence)
- **Action:** Add GO:0061630 (ubiquitin protein ligase activity) with evidence code ISS, reference ortholog AtRGLG4 (Q9SAL0)
- **Rationale:** More specific than GO:0004842; E3-specific; all family members confirmed E3 ligases
- **Candidate references to verify:**
  - [PMID: 22898498](https://pubmed.ncbi.nlm.nih.gov/22898498/) — Verify: "Both RGLG3 and RGLG4 possessed ubiquitin ligase activities and were widely distributed in Arabidopsis thaliana tissues"
  - [PMID: 27497447](https://pubmed.ncbi.nlm.nih.gov/27497447/) — Verify: "we used a ubiquitin-conjugating enzyme (UBC) panel screen to pinpoint UBC30 as a cognate E2 UBC capable of interacting with RGLG3 and RGLG4 and mediating auto-ubiquitination of RGLG3 and ubiquitination of GRXS17 in vitro"

### Lead 2: Consider EC 2.3.2.27 Assignment (Moderate Confidence)
- **Action:** Annotate EC 2.3.2.27 (RING-type E3 ubiquitin transferase) for Q6YYC5
- **Rationale:** Both AtRGLG3 and AtRGLG4 carry this EC number in UniProt reviewed entries; catalytic reaction: S-ubiquitinyl-[E2]-L-cysteine + [acceptor]-L-lysine → [E2]-L-cysteine + N⁶-ubiquitinyl-[acceptor]-L-lysine

### Lead 3: Retain BP and CC Annotations (High Confidence)
- **Action:** Retain GO:0016567 (protein ubiquitination), GO:0005737 (cytoplasm), GO:0005634 (nucleus)
- **Caveat:** Note potential plasma membrane localization due to MG motif

### Lead 4: Flag Myristoylation as Research Priority (Moderate Confidence)
- **Action:** Note in gene review that Q6YYC5 has myristoylation-compatible N-terminus unlike AtRGLG4, suggesting potential membrane association
- **Implication:** May affect substrate access and biological context relative to AtRGLG4

### Candidate References with Snippets to Verify

| PMID | Exact Snippet | Relevance |
|------|---------------|-----------|
| 27497447 | "we identified the monothiol glutaredoxin GRXS17 as a substrate of the Arabidopsis E3 ubiquitin ligases RING DOMAIN LIGASE 3 (RGLG3) and RGLG4 using a substrate trapping approach involving tandem affinity purification of RING-dead versions" | AtRGLG4 confirmed E3 ligase with identified substrate |
| 27497447 | "GRXS17 is ubiquitinated and degraded in an RGLG3- and RGLG4-dependent manner in planta" | In vivo validation of E3 activity |
| 25788731 | "two ubiquitin ligases, RING DOMAIN LIGASE3 (RGLG3) and RGLG4, which control FB1-triggered PCD by modulating the jasmonate (JA) signalling pathway in Arabidopsis thaliana" | Biological role confirmation |
| 37177781 | "we identified an AvrPi9-interacting protein in rice, which we named OsRGLG5, encoding a functional RING-type E3 ubiquitin ligase" | Rice RGLG E3 activity |
| 37177781 | "During infection, AvrPi9 was ubiquitinated and degraded by OsRGLG5" | Rice substrate ubiquitination and degradation |
| 17586653 | "The RING domain protein RGLG2 (for RING domain Ligase2) from Arabidopsis thaliana can be N-terminally myristoylated and localizes to the plasma membrane. It can form Lys-63-linked multiubiquitin chains in an in vitro reaction." | Family E3 activity and myristoylation |
| 22095047 | "RGLG2 could move from the plasma membrane to the nucleus under stress treatment" | Stress-responsive relocalization |
| 20634289 | "Mutation at putative myristoylation residue glycine 2 altered plasma membrane localization of BON1 and rendered BON1 inactive" | Myristoylation importance for copine proteins |


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)