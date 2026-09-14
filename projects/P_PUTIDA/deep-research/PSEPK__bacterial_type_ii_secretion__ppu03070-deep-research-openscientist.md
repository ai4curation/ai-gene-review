---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T02:15:23.717519'
end_time: '2026-08-11T02:44:19.346082'
duration_seconds: 1735.63
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial type II secretion
  module_summary: A species-neutral module for secretion of folded proteins from the
    bacterial periplasm across the outer membrane by the type II secretion system.
    The module comprises the inner-membrane platform, cytosolic secretion ATPase,
    pseudopilus, and outer-membrane secretin. Sec- and Tat-dependent delivery of substrates
    to the periplasm and unrelated fimbrial systems are outside the module boundary.
  module_outline: "- Bacterial type II secretion\n  - 1. Inner-membrane platform assembly\n\
    \  - Type II secretion inner-membrane platform\n  - 2. ATP-dependent energization\n\
    \  - Type II secretion ATPase\n  - 3. Pseudopilus assembly and displacement\n\
    \  - Type II secretion pseudopilus\n  - 4. Outer-membrane translocation\n  - Type\
    \ II secretion outer-membrane secretin"
  module_connections: No explicit connections.
  pathway_query: ppu03070
  pathway_id: ppu03070
  pathway_name: Bacterial secretion system
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03070 with 42 primary genes; module
    area: transport_motility_signaling.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '61'
  candidate_genes: '- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase
    YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)

    - secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)

    - secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)

    - yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary
    bucket kegg:ppu03060)

    - secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)

    - secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket
    kegg:ppu03060)

    - tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary
    bucket kegg:ppu03060)

    - tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - xcpX: PP_1042 | Q88P11 | Type II secretion system protein K (primary bucket
    kegg:ppu03070)

    - xcpP: PP_1045 | Q88P08 | Type II secretion pathway protein XcpP (primary bucket
    kegg:ppu03070)

    - xcpQ: PP_1046 | Q88P07 | Type II secretion pathway protein XcpQ (primary bucket
    kegg:ppu03070)

    - gspE: PP_1047 | Q88P06 | General secretion pathway protein E (primary bucket
    kegg:ppu03070)

    - gspF: PP_1048 | Q88P05 | General secretion pathway protein F (primary bucket
    kegg:ppu03070)

    - gspG: PP_1049 | Q88P04 | Type II secretion system core protein G (primary bucket
    kegg:ppu03070)

    - xcpU: PP_1050 | Q88P03 | Type II secretion pathway protein XcpU (primary bucket
    kegg:ppu03070)

    - xcpV: PP_1051 | Q88P02 | Type II secretion pathway protein XcpV (primary bucket
    kegg:ppu03070)

    - xcpW: PP_1052 | Q88P01 | Type II secretion pathway protein XcpW (primary bucket
    kegg:ppu03070)

    - xcpY: PP_1053 | Q88P00 | Type II secretion pathway protein XcpY (primary bucket
    kegg:ppu03070)

    - secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8;
    primary bucket kegg:ppu03060)

    - PP_1449: PP_1449 | Q88MW9 | Filamentous haemagglutinin FhaB/tRNA nuclease CdiA-like
    TPS domain-containing protein (primary bucket kegg:ppu03070)

    - PP_1450: PP_1450 | Q88MW8 | Activation/secretion protein, TPS family (primary
    bucket kegg:ppu03070)

    - ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four
    homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - PP_1798: PP_1798 | Q88LX9 | Outer membrane efflux protein (primary bucket kegg:ppu01501)

    - vgrG-I: PP_2614 | Q88JN5 | Type 6 secretion system protein (primary bucket kegg:ppu03070)

    - hcpC-I: PP_2615 | Q88JN4 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)

    - PP_2616: PP_2616 | Q88JN3 | Type IV / VI secretion system DotU domain-containing
    protein (primary bucket kegg:ppu03070)

    - PP_2618: PP_2618 | Q88JN1 | Type VI secretion system lipoprotein TssJ (primary
    bucket kegg:ppu03070)

    - PP_2627: PP_2627 | Q88JM2 | Type VI secretion system membrane subunit TssM (primary
    bucket kegg:ppu03070)

    - PP_3089: PP_3089 | Q88IB0 | Type VI secretion system effector, Hcp1 family (primary
    bucket kegg:ppu03070)

    - PP_3090: PP_3090 | Q88IA9 | OmpA domain protein (primary bucket kegg:ppu03070)

    - PP_3091: PP_3091 | Q88IA8 | ImcF-like family protein (primary bucket kegg:ppu03070)

    - PP_3092: PP_3092 | Q88IA7 | Type IV / VI secretion system DotU domain-containing
    protein (primary bucket kegg:ppu03070)

    - PP_3094: PP_3094 | Q88IA5 | Type VI secretion system lipoprotein TssJ (primary
    bucket kegg:ppu03070)

    - clpV: PP_3095 | Q88IA4 | Protein ClpV1 (primary bucket kegg:ppu03070)

    - PP_3106: PP_3106 | Q88I93 | Uncharacterized protein (primary bucket kegg:ppu03070)

    - PP_3385: PP_3385 | Q88HH3 | Type IV / VI secretion system DotU domain-containing
    protein (primary bucket kegg:ppu03070)

    - vgrG-II: PP_3386 | Q88HH2 | Type 6 secretion system protein (primary bucket
    kegg:ppu03070)

    - xcpT: PP_3423 | Q88HD7 | Type II secretion system core protein G (primary bucket
    kegg:ppu03070)

    - xcpS: PP_3424 | Q88HD6 | Type II secretion pathway protein XcpS (primary bucket
    kegg:ppu03070)

    - PP_3476: PP_3476 | Q88H85 | Type II secretion system protein G (primary bucket
    kegg:ppu03070)

    - PP_3477: PP_3477 | Q88H84 | Secretion type II protein related to protein G (primary
    bucket kegg:ppu03070)

    - PP_3478: PP_3478 | Q88H83 | Secretion protein (primary bucket kegg:ppu03070)

    - PP_3483: PP_3483 | Q88H78 | Type II secretion system protein (primary bucket
    kegg:ppu03070)

    - vgrG-III: PP_4049 | Q88FP0 | Type 6 secretion system protein (primary bucket
    kegg:ppu03070)

    - PP_4071: PP_4071 | Q88FL8 | Type VI secretion system membrane subunit TssM (primary
    bucket kegg:ppu03070)

    - PP_4079: PP_4079 | Q88FL1 | Type VI secretion system lipoprotein TssJ (primary
    bucket kegg:ppu03070)

    - PP_4081: PP_4081 | Q88FK9 | Type 4/6 secretion system (primary bucket kegg:ppu03070)

    - hcpC-II: PP_4082 | Q88FK8 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)

    - PP_4886: PP_4886 | Q88DE1 | Hcp1 family type VI secretion system effector (primary
    bucket kegg:ppu03070)

    - PP_4923: PP_4923 | Q88DA4 | Outer membrane efflux protein (primary bucket kegg:ppu01501)

    - PP_4926: PP_4926 | Q88DA1 | Membrane fusion protein (MFP) family protein (primary
    bucket kegg:ppu03070)

    - cyaB: PP_4927 | Q88DA0 | Cyclolysin secretion/processing ATP-binding protein
    CyaB (EC 3.4.22.-) (EC 3.4.22.-; primary bucket kegg:ppu03070)

    - tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary
    bucket kegg:ppu03060)

    - tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)

    - ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor)
    (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - PP_5190: PP_5190 | Q88CJ1 | Type II secretion system protein (primary bucket
    kegg:ppu03070)

    - PP_5238: PP_5238 | Q88CE3 | Fimbrial protein (primary bucket kegg:ppu03070)

    - secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket
    kegg:ppu03060)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_type_ii_secretion__ppu03070-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_type_ii_secretion__ppu03070-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial type II secretion in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03070
- Resolved ID: ppu03070
- Resolved name: Bacterial secretion system
- Source: KEGG

Resolved local bucket kegg:ppu03070 with 42 primary genes; module area: transport_motility_signaling.

## Candidate Genes From Local Metadata

Candidate gene count: 61

- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)
- secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)
- secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)
- yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary bucket kegg:ppu03060)
- secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)
- secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket kegg:ppu03060)
- tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary bucket kegg:ppu03060)
- tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- xcpX: PP_1042 | Q88P11 | Type II secretion system protein K (primary bucket kegg:ppu03070)
- xcpP: PP_1045 | Q88P08 | Type II secretion pathway protein XcpP (primary bucket kegg:ppu03070)
- xcpQ: PP_1046 | Q88P07 | Type II secretion pathway protein XcpQ (primary bucket kegg:ppu03070)
- gspE: PP_1047 | Q88P06 | General secretion pathway protein E (primary bucket kegg:ppu03070)
- gspF: PP_1048 | Q88P05 | General secretion pathway protein F (primary bucket kegg:ppu03070)
- gspG: PP_1049 | Q88P04 | Type II secretion system core protein G (primary bucket kegg:ppu03070)
- xcpU: PP_1050 | Q88P03 | Type II secretion pathway protein XcpU (primary bucket kegg:ppu03070)
- xcpV: PP_1051 | Q88P02 | Type II secretion pathway protein XcpV (primary bucket kegg:ppu03070)
- xcpW: PP_1052 | Q88P01 | Type II secretion pathway protein XcpW (primary bucket kegg:ppu03070)
- xcpY: PP_1053 | Q88P00 | Type II secretion pathway protein XcpY (primary bucket kegg:ppu03070)
- secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8; primary bucket kegg:ppu03060)
- PP_1449: PP_1449 | Q88MW9 | Filamentous haemagglutinin FhaB/tRNA nuclease CdiA-like TPS domain-containing protein (primary bucket kegg:ppu03070)
- PP_1450: PP_1450 | Q88MW8 | Activation/secretion protein, TPS family (primary bucket kegg:ppu03070)
- ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- PP_1798: PP_1798 | Q88LX9 | Outer membrane efflux protein (primary bucket kegg:ppu01501)
- vgrG-I: PP_2614 | Q88JN5 | Type 6 secretion system protein (primary bucket kegg:ppu03070)
- hcpC-I: PP_2615 | Q88JN4 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)
- PP_2616: PP_2616 | Q88JN3 | Type IV / VI secretion system DotU domain-containing protein (primary bucket kegg:ppu03070)
- PP_2618: PP_2618 | Q88JN1 | Type VI secretion system lipoprotein TssJ (primary bucket kegg:ppu03070)
- PP_2627: PP_2627 | Q88JM2 | Type VI secretion system membrane subunit TssM (primary bucket kegg:ppu03070)
- PP_3089: PP_3089 | Q88IB0 | Type VI secretion system effector, Hcp1 family (primary bucket kegg:ppu03070)
- PP_3090: PP_3090 | Q88IA9 | OmpA domain protein (primary bucket kegg:ppu03070)
- PP_3091: PP_3091 | Q88IA8 | ImcF-like family protein (primary bucket kegg:ppu03070)
- PP_3092: PP_3092 | Q88IA7 | Type IV / VI secretion system DotU domain-containing protein (primary bucket kegg:ppu03070)
- PP_3094: PP_3094 | Q88IA5 | Type VI secretion system lipoprotein TssJ (primary bucket kegg:ppu03070)
- clpV: PP_3095 | Q88IA4 | Protein ClpV1 (primary bucket kegg:ppu03070)
- PP_3106: PP_3106 | Q88I93 | Uncharacterized protein (primary bucket kegg:ppu03070)
- PP_3385: PP_3385 | Q88HH3 | Type IV / VI secretion system DotU domain-containing protein (primary bucket kegg:ppu03070)
- vgrG-II: PP_3386 | Q88HH2 | Type 6 secretion system protein (primary bucket kegg:ppu03070)
- xcpT: PP_3423 | Q88HD7 | Type II secretion system core protein G (primary bucket kegg:ppu03070)
- xcpS: PP_3424 | Q88HD6 | Type II secretion pathway protein XcpS (primary bucket kegg:ppu03070)
- PP_3476: PP_3476 | Q88H85 | Type II secretion system protein G (primary bucket kegg:ppu03070)
- PP_3477: PP_3477 | Q88H84 | Secretion type II protein related to protein G (primary bucket kegg:ppu03070)
- PP_3478: PP_3478 | Q88H83 | Secretion protein (primary bucket kegg:ppu03070)
- PP_3483: PP_3483 | Q88H78 | Type II secretion system protein (primary bucket kegg:ppu03070)
- vgrG-III: PP_4049 | Q88FP0 | Type 6 secretion system protein (primary bucket kegg:ppu03070)
- PP_4071: PP_4071 | Q88FL8 | Type VI secretion system membrane subunit TssM (primary bucket kegg:ppu03070)
- PP_4079: PP_4079 | Q88FL1 | Type VI secretion system lipoprotein TssJ (primary bucket kegg:ppu03070)
- PP_4081: PP_4081 | Q88FK9 | Type 4/6 secretion system (primary bucket kegg:ppu03070)
- hcpC-II: PP_4082 | Q88FK8 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)
- PP_4886: PP_4886 | Q88DE1 | Hcp1 family type VI secretion system effector (primary bucket kegg:ppu03070)
- PP_4923: PP_4923 | Q88DA4 | Outer membrane efflux protein (primary bucket kegg:ppu01501)
- PP_4926: PP_4926 | Q88DA1 | Membrane fusion protein (MFP) family protein (primary bucket kegg:ppu03070)
- cyaB: PP_4927 | Q88DA0 | Cyclolysin secretion/processing ATP-binding protein CyaB (EC 3.4.22.-) (EC 3.4.22.-; primary bucket kegg:ppu03070)
- tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary bucket kegg:ppu03060)
- tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)
- ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor) (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- PP_5190: PP_5190 | Q88CJ1 | Type II secretion system protein (primary bucket kegg:ppu03070)
- PP_5238: PP_5238 | Q88CE3 | Fimbrial protein (primary bucket kegg:ppu03070)
- secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket kegg:ppu03060)

## Generic Module Context

### Working Scope

A species-neutral module for secretion of folded proteins from the bacterial periplasm across the outer membrane by the type II secretion system. The module comprises the inner-membrane platform, cytosolic secretion ATPase, pseudopilus, and outer-membrane secretin. Sec- and Tat-dependent delivery of substrates to the periplasm and unrelated fimbrial systems are outside the module boundary.

### Provisional Biological Outline

- Bacterial type II secretion
  - 1. Inner-membrane platform assembly
  - Type II secretion inner-membrane platform
  - 2. ATP-dependent energization
  - Type II secretion ATPase
  - 3. Pseudopilus assembly and displacement
  - Type II secretion pseudopilus
  - 4. Outer-membrane translocation
  - Type II secretion outer-membrane secretin

### Known Relationships Among Steps

No explicit connections.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Module/Pathway/Taxon Review: Bacterial Type II Secretion in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03070` ("Bacterial secretion system" overview map)
**Module scope reviewed:** Type II secretion system (T2SS / Xcp / general secretory pathway main terminal branch)
**Curation verdict:** **Module COVERED** — all four canonical steps map to specific KT2440 genes; the supplied candidate list requires substantial revision.

---

## 1. Executive Summary

*Pseudomonas putida* KT2440 encodes a **single, complete Type II secretion system (T2SS)** of the *Xcp* subfamily in a contiguous chromosomal cluster spanning **PP_1042 and PP_1045–PP_1055**, plus the shared prepilin peptidase **PilD (PP_0632)**. Every step of the generic T2SS module — (1) inner-membrane platform, (2) cytosolic secretion ATPase, (3) pseudopilus assembly, and (4) outer-membrane secretin — maps cleanly to identified genes with **no gaps**. On satisfiability grounds the module should be marked **covered** for this organism.

The principal curation problem is **not** module satisfiability but the **quality of the supplied candidate list**. The 61 candidates inherited from KEGG bucket `ppu03070` are drawn from a broad "Bacterial secretion system" overview map, not from a T2SS-specific module. As a result the list is heavily contaminated: only **10 of 61 candidates** belong to the genuine Xcp T2SS, while the remaining ~50 are members of *other* secretion machineries (Sec/Tat translocons, three Type VI secretion clusters, a Type I/RTX system, a two-partner/Type Vb system) or are over-propagated T2SS-family homologs that actually belong to **Type IV pilus (T4P)** and orphan loci. Simultaneously, the list **omits three genuine Xcp components** (xcpZ/GspM = PP_1054, gspN = PP_1055, and the essential prepilin peptidase pilD = PP_0632).

The actionable recommendations are therefore: (a) mark the T2SS module **covered**; (b) **add** PP_1054, PP_1055, and PP_0632 to the module; (c) **exclude** the ~46 out-of-module genes belonging to Sec/Tat, T6SS, T1SS/RTX, and T5SS/TPS systems (they belong to their own modules); and (d) flag ~8 "type II secretion"-labeled genes (PP_3423, PP_3424, the PP_3474–3484 locus, PP_5190) as **candidate_uncertain / over-annotated** because they are Type IV pilus or orphan homologs that share Pfam domain families with T2SS but lack a cognate secretin+ATPase+pseudopilus operon.

---

## 2. Target-Organism Pathway Definition

### What the module includes

The Type II secretion system (also called the **general secretory pathway main terminal branch, GSP-MTB**, or in *Pseudomonas* the **Xcp** system) secretes **folded** proteins from the **periplasm** across the **outer membrane** into the extracellular milieu. It is a two-step pathway: substrates are first delivered to the periplasm by the Sec or Tat translocons (which are *upstream* of, and not part of, T2SS), and then the T2SS machine translocates the folded substrate across the outer membrane. As established in the foundational review of T2SS architecture, "the multi-gene family necessary for secretion of these enzymes is now known as the type II system or the main terminal branch (MTB) of the general secretion pathway (GSP)" ([PMID: 9641973](https://pubmed.ncbi.nlm.nih.gov/9641973/)).

The machine has four functional/structural sub-assemblies, which correspond to the four generic module steps:

| Step | Sub-assembly | Function |
|------|-------------|----------|
| 1 | Inner-membrane (IM) platform | Anchors the machine; couples ATPase to pseudopilus (GspC/F/L/M) |
| 2 | Secretion ATPase | Cytoplasmic motor energizing the machine (GspE) |
| 3 | Pseudopilus | Piston-like fiber that pushes substrate through the secretin (GspG–K major/minor pseudopilins, matured by prepilin peptidase PilD) |
| 4 | Outer-membrane secretin | Gated channel in the outer membrane (GspD / XcpQ) |

### Which neighboring pathways must be kept separate

The KEGG `ppu03070` overview map lumps **all** protein secretion systems together. For a T2SS-specific module the following must be treated as **separate modules/buckets**:

- **Sec translocon and Tat pathway** (KEGG `ppu03060`, "Protein export"): SecA/B/D/E/F/G/Y, YajC, YidC, Ffh, FtsY, TatA/B/C. These deliver substrates *to* the periplasm; they are prerequisites for, but not components of, T2SS.
- **Type VI secretion (T6SS):** contractile injection systems — three separate clusters in KT2440.
- **Type I secretion / RTX (ABC-transporter + MFP + TolC):** one-step ATP-driven export.
- **Type V / two-partner secretion (TPS, autotransporters):** Sec-dependent OM insertion.
- **Type IV pilus (T4P) and Tad/Flp appendages:** share the GspD/GspE/GspF/GspG domain families with T2SS but are motility/adhesion machines, not secretion systems.

### Alternate names / database definitions

- *Pseudomonas* nomenclature: **Xcp** (extracellular protein) system; genes xcpP–Z + xcpA (=pilD).
- Generic nomenclature: **Gsp** (general secretory pathway), genes gspC–gspO.
- Correspondence: XcpP=GspC, XcpQ=GspD, XcpR=GspE, XcpS=GspF, XcpT=GspG, XcpU=GspH, XcpV=GspI, XcpW=GspJ, XcpX=GspK, XcpY=GspL, XcpZ=GspM, and the prepilin peptidase XcpA=PilD.

---

## 3. Expected Step Model and KT2440 Coverage

```
         SUBSTRATE (folded, in periplasm; delivered by Sec/Tat = ppu03060)
                                 |
   OUTER MEMBRANE  ============[ SECRETIN GspD/XcpQ ]============   Step 4
                                 |   (PP_1046)
                          [ pseudopilus tip/minor pilins ]
   PERIPLASM              [ GspG–K major/minor pseudopilus ]        Step 3
                          PP_1049/1050/1051/1052/1042
                          matured by PilD (PP_0632)
   INNER MEMBRANE  =====[ IM PLATFORM GspC/F/L/M ]=================  Step 1
                        PP_1045 / PP_1048 / PP_1053 / PP_1054
                                 |
   CYTOPLASM              [ ATPase GspE/XcpR ]  ---- ATP            Step 2
                                 PP_1047
```

| Module step | Canonical components | KT2440 gene(s) | Status |
|-------------|---------------------|----------------|--------|
| 1. IM platform | GspC, GspF, GspL, GspM | PP_1045 (xcpP/GspC), PP_1048 (gspF), PP_1053 (xcpY/GspL), PP_1054 (xcpZ/GspM) | **Covered** |
| 2. Secretion ATPase | GspE | PP_1047 (gspE/XcpR) | **Covered** |
| 3. Pseudopilus | GspG (major) + GspH–K (minor), PilD peptidase | PP_1049 (gspG), PP_1050 (xcpU/GspH), PP_1051 (xcpV/GspI), PP_1052 (xcpW/GspJ), PP_1042 (xcpX/GspK); PilD = PP_0632 | **Covered** |
| 4. OM secretin | GspD | PP_1046 (xcpQ/GspD) | **Covered** |

Accessory component GspN = PP_1055 completes the cluster. The canonical Xcp system "requires at least 12 xcp gene products (XcpA and XcpP to -Z)" ([PMID: 11208795](https://pubmed.ncbi.nlm.nih.gov/11208795/)); KT2440 encodes the full XcpP–Z set contiguously plus XcpA/PilD elsewhere, so **all four steps are satisfied**.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence T2SS components (the true Xcp cluster)

These 10 candidates (plus 3 additions) constitute the genuine T2SS. Evidence type: UniProt annotation of proteome UP000000556 combined with contiguous operon structure and canonical Xcp/Gsp domain assignments.

| Gene | Locus | UniProt | Role in T2SS | Module step | Caveat |
|------|-------|---------|--------------|-------------|--------|
| xcpX | PP_1042 | Q88P11 | GspK minor pseudopilin | 3 | — |
| xcpP | PP_1045 | Q88P08 | GspC IM platform / secretin linker | 1 | — |
| xcpQ | PP_1046 | Q88P07 | GspD outer-membrane secretin (584 aa, OM) | 4 | Diagnostic OM channel |
| gspE | PP_1047 | Q88P06 | GspE/XcpR secretion ATPase | 2 | Energizing motor |
| gspF | PP_1048 | Q88P05 | GspF IM platform (polytopic) | 1 | Domain shared with T4P |
| gspG | PP_1049 | Q88P04 | GspG major pseudopilin | 3 | — |
| xcpU | PP_1050 | Q88P03 | GspH minor pseudopilin | 3 | — |
| xcpV | PP_1051 | Q88P02 | GspI minor pseudopilin | 3 | — |
| xcpW | PP_1052 | Q88P01 | GspJ minor pseudopilin | 3 | — |
| xcpY | PP_1053 | Q88P00 | GspL IM platform | 1 | — |
| **xcpZ** | **PP_1054** | Q88NZ9 | GspM IM platform (128 aa) | 1 | **Missing from candidate list — ADD** |
| **gspN** | **PP_1055** | Q88NZ8 | GspN accessory | (accessory) | **Missing from candidate list — ADD** |
| **pilD** | **PP_0632** | Q88Q64 | Prepilin peptidase (EC 3.4.23.43) | 3 (maturation) | **Missing; shared with T4P — ADD** |

**Curation-relevant note:** The ATPase XcpR/GspE role is directly supported by experimental work in the sister species *P. aeruginosa*: "XcpR, a putative nucleotide-binding protein, is essential for the secretion process across the outer membrane" ([PMID: 9882649](https://pubmed.ncbi.nlm.nih.gov/9882649/)) and "Assembly of XcpR in the cytoplasmic membrane is required for extracellular protein secretion." Species transfer *P. aeruginosa → P. putida* is **strong** here: both are fluorescent pseudomonads with orthologous, syntenic xcp clusters, and cross-species Xcp machinery exchange has been demonstrated ([PMID: 11208795](https://pubmed.ncbi.nlm.nih.gov/11208795/)).

### 4.2 Out-of-module candidates (belong to other secretion systems)

These should be **excluded** from the T2SS module and re-filed to their own modules.

| Group | KT2440 candidates | Correct module | Why excluded |
|-------|------------------|----------------|--------------|
| **Sec/Tat translocons** | yidC (PP_0006), secE (PP_0441), secY (PP_0474), yajC (PP_0834), secD (PP_0835), secF (PP_0836), tatC-I (PP_1039), tatB-I (PP_1040), tatA-I (PP_1041), secA (PP_1345), ffh (PP_1461), tatA-II (PP_5016), tatB (PP_5017), tatC-II (PP_5018), secB (PP_5053), ftsY (PP_5111), secG (PP_5706) | ppu03060 (Protein export) | Deliver substrates *to* periplasm; upstream of T2SS, not part of it |
| **Type VI secretion (3 clusters)** | vgrG-I/II/III (PP_2614, PP_3386, PP_4049), hcpC-I/II (PP_2615, PP_4082), TssM (PP_2627, PP_4071), TssJ (PP_2618, PP_3094, PP_4079), ClpV (PP_3095), ImcF (PP_3091), DotU (PP_2616, PP_3092, PP_3385), Hcp effectors (PP_3089, PP_4886), OmpA (PP_3090), PP_3106, PP_4081 | T6SS module | Contractile injection nanomachine; unrelated to T2SS |
| **Type I / RTX + efflux** | cyaB (PP_4927), MFP (PP_4926), OM efflux PP_1798, PP_4923 | T1SS / ppu01501 | One-step ABC-transporter export |
| **Type Vb / TPS** | PP_1449 (CdiA-like TPS), PP_1450 (TPS activation/secretion) | T5SS/TPS module | Two-partner secretion |

Rationale confirmed by the T2SS definition: T2SS is the "main terminal branch (MTB) of the general secretion pathway" for folded exoproteins ([PMID: 9641973](https://pubmed.ncbi.nlm.nih.gov/9641973/)), mechanistically and evolutionarily distinct from Sec/Tat, T1SS, T5SS, and T6SS.

### 4.3 Over-propagated "T2SS" homologs (Type IV pilus / orphan loci)

These candidates carry "type II secretion" labels but are **not** part of the Xcp T2SS. They should be marked **candidate_uncertain** pending full gene review.

| Locus | UniProt | Annotation | Actual assignment | Diagnostic |
|-------|---------|-----------|-------------------|-----------|
| PP_3423 (xcpT) + PP_3424 (xcpS) | Q88HD7 / Q88HD6 | GspG pseudopilin + GspF platform | **Orphan T4P-like pair** | Isolated pseudopilin+platform with NO cognate secretin or ATPase nearby (flanked by histidine kinases PP_3420/3421, RND-MFP PP_3425) |
| PP_5190 | Q88CJ1 | "Type II secretion system protein" | **MshE/GspE-family pilus ATPase** | Carries MshEN (PF05157) + T2SSE (PF00437); isolated, neighbours are Lrp regulator + glycine-cleavage genes — not a T2SS operon |
| PP_3474–3484 locus (incl. PP_3475/3476/3477 pseudopilins, PP_3478 secretin, PP_3483 ATPase, PP_3480 PilO) | multiple | Various "type II secretion" | **Self-contained second pilus/secretion machine (T4P/Tad-like)** | Has secretin (PP_3478, PF00263+PF03958+STN), single assembly ATPase (PP_3483), PilO alignment protein (PP_3480, PF10741), CsgE (PP_3474) — architecture of a pilus, and lacks a retraction ATPase (PilT is elsewhere at PP_5093) |
| PP_5238 | Q88CE3 | Fimbrial protein | **Fimbrial/CU pilus** | Not a secretion component — mark not_expected |

The mechanistic basis for these over-annotations is domain sharing: "one of the core components of the Xcp system is the inner-membrane protein XcpS (GspF), homologues of which can be identified in type II secretion machineries as well as in type IV piliation systems" ([PMID: 17464073](https://pubmed.ncbi.nlm.nih.gov/17464073/)). Because GspD/PilQ, GspE-family ATPases, GspF/PilC, and GspG-type pilins are common to both T2SS and T4P, **Pfam domain content alone cannot assign a gene to T2SS** — operon context (presence of a cognate secretin + ATPase + full pseudopilus set) is required.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### Missing from candidate list (genuine components to ADD)
- **PP_1054 (xcpZ/GspM)** — IM platform, part of step 1.
- **PP_1055 (gspN)** — accessory component completing the cluster.
- **PP_0632 (pilD)** — prepilin peptidase, essential for pseudopilus maturation (step 3). Shared with T4P, which is why it was likely filed separately.

### Over-annotations to DOWNGRADE (candidate_uncertain)
- **PP_3423, PP_3424** — orphan GspG/GspF pair; no secretin/ATPase.
- **PP_5190** — isolated MshE/GspE-family pilus ATPase.
- **PP_3475, PP_3476, PP_3477, PP_3478, PP_3483** — components of the independent PP_3474–3484 pilus locus, NOT Xcp.

### Not expected in the T2SS module
- **PP_5238** — fimbrial protein (chaperone-usher pilus).

### Key ambiguity: the PP_3474–3484 locus
This locus is a **self-contained, independently regulated minor pilus/secretion machine** distinct from both Xcp T2SS and the main Type IVa pilus. It contains a GspD/PilQ secretin (PP_3478, OM, 621 aa), a single GspE/T2SSE ATPase (PP_3483, 598 aa), three GspG-type pseudopilins (PP_3475/3476/3477), a PilO alignment protein (PP_3480), a CsgE curli-assembly homolog (PP_3474), and an in-cluster response-regulator receiver (PP_3484). Critically it has **no retraction ATPase** (the dedicated Type IVa PilT is at PP_5093), so it is neither the Xcp T2SS nor the canonical twitching-motility T4aP. Its true function (a possible Tad-like or minor pilus/secretion appendage) is an **open question** — resolving it would require a full `fetch-gene` review and ideally experimental characterization. Domain content alone is insufficient because these families are shared with T2SS ([PMID: 17464073](https://pubmed.ncbi.nlm.nih.gov/17464073/)).

---

## 6. Module and GO-Curation Recommendations

| Module step | Status | KT2440 genes |
|-------------|--------|--------------|
| 1. Inner-membrane platform | **covered** | PP_1045, PP_1048, PP_1053, PP_1054 |
| 2. Secretion ATPase | **covered** | PP_1047 |
| 3. Pseudopilus (+maturation) | **covered** | PP_1049, PP_1050, PP_1051, PP_1052, PP_1042; PP_0632 (PilD) |
| 4. Outer-membrane secretin | **covered** | PP_1046 |

**Overall: module_covered.** All four steps map to specific genes with no gaps.

Additional curation actions:
1. **Candidate-list revision:** ADD PP_1054, PP_1055, PP_0632; EXCLUDE the ~46 Sec/Tat, T6SS, T1SS/RTX, and T5SS/TPS genes (re-file to their own modules); DOWNGRADE PP_3423, PP_3424, PP_3475–3478, PP_3483, PP_5190 to candidate_uncertain; mark PP_5238 not_expected.
2. **Module boundary confirmation:** The generic four-step module boundary is **correct** for this organism — no revision needed. The problem is entirely at the candidate-provisioning stage, because the source bucket is KEGG's broad `ppu03070` overview map rather than a T2SS-specific module.
3. **GO annotations:** For the confirmed Xcp genes, GO:0015628 (protein secretion by the type II secretion system) is appropriate. For the T4P/orphan homologs, GO:0015628 is likely **over-propagated**; GO:0043683 (type IV pilus assembly) or a generic pilus term is more accurate. No new GO term requests are needed.
4. **New module document:** Consider a separate module document for the PP_3474–3484 pilus locus to capture that it is a distinct machine, preventing repeated mis-filing into T2SS.

---

## 7. Genes to Promote to Full `fetch-gene` Review

| Locus | Reason | Priority |
|-------|--------|----------|
| PP_0632 (pilD) | Essential shared prepilin peptidase; confirm single copy serves both Xcp and T4P | High |
| PP_1046 (xcpQ/GspD) | Diagnostic secretin; confirm OM localization and gating | High |
| PP_3478 (secretin), PP_3483 (ATPase) | Anchor of the ambiguous PP_3474–3484 locus; determine T4P vs. Tad vs. minor-pilus identity | High |
| PP_3423 / PP_3424 | Orphan GspG/GspF pair — determine whether functional or pseudogenized fragment | Medium |
| PP_5190 | Isolated MshE/GspE ATPase — confirm pilus (not T2SS) assignment | Medium |
| PP_1054 (xcpZ/GspM), PP_1055 (gspN) | Confirm addition to module and cluster co-transcription | Medium |

---

## 8. Limitations and Knowledge Gaps

- **Species transfer:** Direct functional/mutant evidence for T2SS in *P. putida* KT2440 specifically is limited; the strongest experimental data (XcpR essentiality, cross-species Xcp exchange) come from *P. aeruginosa* ([PMID: 9882649](https://pubmed.ncbi.nlm.nih.gov/9882649/), [PMID: 11208795](https://pubmed.ncbi.nlm.nih.gov/11208795/)). Transfer to KT2440 is judged **strong** on the basis of orthology and synteny, but formal KT2440 secretion assays were not located in this review.
- **Substrate identity:** The extracellular substrates secreted by the KT2440 Xcp system were not systematically enumerated here. In *P. aeruginosa*, T2SS secretes lipases/esterases and other exoenzymes; a candidate KT2440 substrate class (e.g., lipolytic enzymes) is plausible by analogy but not confirmed for this strain.
- **Ambiguous locus:** The precise function of PP_3474–3484 (T4P vs. Tad-like vs. minor pilus/secretion) remains unresolved from sequence alone.
- **Assignments are annotation/synteny-based:** Component-to-step mapping rests on UniProt annotation, Pfam/InterPro domains, and operon context, not on KT2440 experimental data. This is appropriate for curation but should be flagged as homology-inferred, not experimentally verified, for the target strain.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | How it supports the review |
|------|-----------------|----------------------------|
| [9641973](https://pubmed.ncbi.nlm.nih.gov/9641973/) | *Macromolecular assembly and secretion across the bacterial cell envelope: type II protein secretion systems* | Defines T2SS as the GSP main terminal branch for folded exoproteins — the module boundary used to include Xcp and exclude Sec/Tat, T1SS, T5SS, T6SS |
| [11208795](https://pubmed.ncbi.nlm.nih.gov/11208795/) | *Exchange of Xcp (Gsp) secretion machineries between P. aeruginosa and P. alcaligenes* | Establishes the canonical ≥12-component Xcp set (XcpA + XcpP–Z), the completeness template; demonstrates cross-species Xcp machinery transfer |
| [9882649](https://pubmed.ncbi.nlm.nih.gov/9882649/) | *Assembly of XcpR in the cytoplasmic membrane is required for extracellular protein secretion in P. aeruginosa* | Direct experimental evidence for the XcpR/GspE ATPase (KT2440 PP_1047) as the essential energizing component (module step 2) |
| [17464073](https://pubmed.ncbi.nlm.nih.gov/17464073/) | *Interaction domains in the P. aeruginosa type II secretory apparatus component XcpS (GspF)* | Documents that GspF/XcpS-type components occur in both T2SS and Type IV pili — the mechanistic basis for over-propagated T2SS annotations on T4P genes (PP_3423/3424, PP_3474–3484) |
| [10559163](https://pubmed.ncbi.nlm.nih.gov/10559163/) | *A novel lipolytic enzyme located in the outer membrane of P. aeruginosa* | Context on Pseudomonas surface/secreted lipolytic enzymes and alternative (autotransporter) secretion routes — background for distinguishing T2SS substrates from other export pathways |

(The azoreductase paper [PMID: 19238379] surfaced during literature search is not relevant to T2SS and is not used for T2SS claims.)

---

## 10. Proposed Follow-up Experiments / Actions

1. **Curation (immediate):** Apply the candidate-list revision — add PP_1054/PP_1055/PP_0632, exclude the ~46 out-of-module genes, downgrade the ~8 over-annotated T4P/orphan homologs, mark PP_5238 not_expected. Mark the module **covered**.
2. **Full gene reviews:** Promote the six loci in Section 7 to `fetch-gene`, prioritizing PP_0632, PP_1046, and the PP_3478/PP_3483 anchors of the ambiguous locus.
3. **Experimental (target strain):** A KT2440 xcpQ (PP_1046) or xcpR (PP_1047) deletion coupled with secretome comparison (culture-supernatant proteomics) would provide the first direct KT2440 evidence and identify native substrates.
4. **Locus characterization:** Transcriptional and mutant analysis of PP_3474–3484 to determine whether it functions as a pilus, adhesion appendage, or minor secretion system, resolving the main open question.
5. **Provisioning fix:** Replace the KEGG `ppu03070` overview-map bucket with a T2SS-specific ortholog seed (e.g., a curated Xcp/Gsp gene set) to prevent recurrence of the contamination pattern in future automated candidate lists.

---

*Prepared for manual module satisfiability and gene-annotation curation. Confidence: module coverage HIGH (homology + synteny + strong cross-Pseudomonas experimental support); candidate-list dispositions HIGH for the Xcp core and Sec/Tat/T6SS/T1SS/T5SS exclusions, MEDIUM for the T4P/orphan downgrades pending full gene review.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_type_ii_secretion__ppu03070-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_type_ii_secretion__ppu03070-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9641973
2. PMID:11208795
3. PMID:9882649
4. PMID:17464073
5. PMID:19238379