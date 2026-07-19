---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:48:12.847438'
end_time: '2026-07-18T17:07:59.503128'
duration_seconds: 1186.66
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: MEP isoprenoid precursor biosynthesis
  module_summary: The bacterial methylerythritol phosphate (MEP/DOXP) route converts
    pyruvate and glyceraldehyde 3-phosphate through seven reactions into isopentenyl
    diphosphate (IPP) and dimethylallyl diphosphate (DMAPP). DXS forms the shared
    branch-point metabolite DXP, Dxr commits DXP to the MEP route, IspD-IspG build
    HMBPP, and IspH produces the two universal five-carbon isoprenoid precursors.
    DXP use in thiamine or pyridoxal-phosphate biosynthesis and downstream prenyl-diphosphate
    elongation are outside this module.
  module_outline: "- MEP isoprenoid precursor biosynthesis\n  - 1. DXP formation from\
    \ pyruvate and glyceraldehyde 3-phosphate\n  - DXS-dependent DXP formation\n \
    \   - DXP synthase activity (molecular player: DXP synthase family; activity or\
    \ role: 1-deoxy-D-xylulose-5-phosphate synthase activity)\n  - 2. Commitment of\
    \ DXP to MEP\n  - Dxr-dependent MEP formation\n    - DXP reductoisomerase activity\
    \ (molecular player: DXP reductoisomerase family; activity or role: 1-deoxy-D-xylulose-5-phosphate\
    \ reductoisomerase activity)\n  - 3. CDP-ME formation\n  - IspD-dependent CDP-ME\
    \ formation\n    - MEP cytidylyltransferase activity (molecular player: IspD MEP\
    \ cytidylyltransferase family; activity or role: 2-C-methyl-D-erythritol 4-phosphate\
    \ cytidylyltransferase activity)\n  - 4. CDP-ME 2-phosphate formation\n  - IspE-dependent\
    \ CDP-ME 2-phosphate formation\n    - CDP-ME kinase activity (molecular player:\
    \ IspE CDP-ME kinase family; activity or role: 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol\
    \ kinase activity)\n  - 5. ME-CPP formation\n  - IspF-dependent ME-CPP formation\n\
    \    - ME-CPP synthase activity (molecular player: IspF ME-CPP synthase family;\
    \ activity or role: 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase activity)\n\
    \  - 6. HMBPP formation\n  - IspG-dependent HMBPP formation\n    - Flavodoxin-coupled\
    \ HMBPP synthase activity (molecular player: IspG HMBPP synthase family; activity\
    \ or role: 4-hydroxy-3-methylbut-2-enyl-diphosphate synthase activity (flavodoxin))\n\
    \  - 7. IPP and DMAPP formation\n  - IspH-dependent IPP and DMAPP formation\n\
    \    - HMBPP reductase activity (molecular player: IspH HMBPP reductase family;\
    \ activity or role: 4-hydroxy-3-methylbut-2-enyl diphosphate reductase activity)"
  module_connections: '- DXS-dependent DXP formation feeds into Dxr-dependent MEP
    formation: DXS supplies DXP to the committed MEP reaction.

    - Dxr-dependent MEP formation feeds into IspD-dependent CDP-ME formation: Dxr
    supplies MEP to IspD.

    - IspD-dependent CDP-ME formation feeds into IspE-dependent CDP-ME 2-phosphate
    formation: IspD supplies CDP-ME to IspE.

    - IspE-dependent CDP-ME 2-phosphate formation feeds into IspF-dependent ME-CPP
    formation: IspE supplies CDP-ME 2-phosphate to IspF.

    - IspF-dependent ME-CPP formation feeds into IspG-dependent HMBPP formation: IspF
    supplies ME-CPP to IspG.

    - IspG-dependent HMBPP formation feeds into IspH-dependent IPP and DMAPP formation:
    IspG supplies HMBPP to the terminal IspH reaction.'
  pathway_query: ppu00900
  pathway_id: ppu00900
  pathway_name: Terpenoid backbone biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00900 with 14 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '17'
  candidate_genes: '- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase
    (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC
    2.2.1.7; primary bucket kegg:ppu00730)

    - ispA: PP_0528 | Q88QG6 | Farnesyl diphosphate synthase (EC 2.5.1.1, EC 2.5.1.10)
    (EC 2.5.1.1; 2.5.1.10; primary bucket kegg:ppu00900)

    - ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129;
    primary bucket kegg:ppu00627)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - ispH: PP_0606 | Q88Q89 | 4-hydroxy-3-methylbut-2-enyl diphosphate reductase
    (HMBPP reductase) (EC 1.17.7.4) (EC 1.17.7.4; primary bucket kegg:ppu00900)

    - ispB: PP_0687 | Q88Q11 | Octaprenyl diphosphate synthase (EC 2.5.1.90) (All-trans-octaprenyl-diphosphate
    synthase) (Octaprenyl pyrophosphate synthase) (EC 2.5.1.90; primary bucket kegg:ppu00900)

    - ispE: PP_0723 | Q88PX5 | 4-diphosphocytidyl-2-C-methyl-D-erythritol kinase (CMK)
    (EC 2.7.1.148) (4-(cytidine-5''-diphospho)-2-C-methyl-D-erythritol kinase) (EC
    2.7.1.148; primary bucket kegg:ppu00900)

    - ispG: PP_0853 | Q88PJ7 | 4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase
    (flavodoxin) (EC 1.17.7.3) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase)
    (EC 1.17.7.3; primary bucket kegg:ppu00900)

    - uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate
    specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl
    diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase)
    (EC 2.5.1.31; primary bucket kegg:ppu00900)

    - dxr: PP_1597 | Q88MH4 | 1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXP
    reductoisomerase) (EC 1.1.1.267) (1-deoxyxylulose-5-phosphate reductoisomerase)
    (2-C-methyl-D-erythritol 4-phosphate synthase) (EC 1.1.1.267; primary bucket kegg:ppu00900)

    - ispD: PP_1614 | Q88MF7 | 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase
    (EC 2.7.7.60) (4-diphosphocytidyl-2C-methyl-D-erythritol synthase) (MEP cytidylyltransferase)
    (MCT) (EC 2.7.7.60; primary bucket kegg:ppu00900)

    - ispF: PP_1618 | Q88MF3 | 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase
    (MECDP-synthase) (MECPP-synthase) (MECPS) (EC 4.6.1.12) (EC 4.6.1.12; primary
    bucket kegg:ppu00900)

    - fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__mep_isoprenoid_precursor_biosynthesis__ppu00900-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__mep_isoprenoid_precursor_biosynthesis__ppu00900-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

MEP isoprenoid precursor biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00900
- Resolved ID: ppu00900
- Resolved name: Terpenoid backbone biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00900 with 14 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 17

- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary bucket kegg:ppu00730)
- ispA: PP_0528 | Q88QG6 | Farnesyl diphosphate synthase (EC 2.5.1.1, EC 2.5.1.10) (EC 2.5.1.1; 2.5.1.10; primary bucket kegg:ppu00900)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- ispH: PP_0606 | Q88Q89 | 4-hydroxy-3-methylbut-2-enyl diphosphate reductase (HMBPP reductase) (EC 1.17.7.4) (EC 1.17.7.4; primary bucket kegg:ppu00900)
- ispB: PP_0687 | Q88Q11 | Octaprenyl diphosphate synthase (EC 2.5.1.90) (All-trans-octaprenyl-diphosphate synthase) (Octaprenyl pyrophosphate synthase) (EC 2.5.1.90; primary bucket kegg:ppu00900)
- ispE: PP_0723 | Q88PX5 | 4-diphosphocytidyl-2-C-methyl-D-erythritol kinase (CMK) (EC 2.7.1.148) (4-(cytidine-5'-diphospho)-2-C-methyl-D-erythritol kinase) (EC 2.7.1.148; primary bucket kegg:ppu00900)
- ispG: PP_0853 | Q88PJ7 | 4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (flavodoxin) (EC 1.17.7.3) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase) (EC 1.17.7.3; primary bucket kegg:ppu00900)
- uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase) (EC 2.5.1.31; primary bucket kegg:ppu00900)
- dxr: PP_1597 | Q88MH4 | 1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXP reductoisomerase) (EC 1.1.1.267) (1-deoxyxylulose-5-phosphate reductoisomerase) (2-C-methyl-D-erythritol 4-phosphate synthase) (EC 1.1.1.267; primary bucket kegg:ppu00900)
- ispD: PP_1614 | Q88MF7 | 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase (EC 2.7.7.60) (4-diphosphocytidyl-2C-methyl-D-erythritol synthase) (MEP cytidylyltransferase) (MCT) (EC 2.7.7.60; primary bucket kegg:ppu00900)
- ispF: PP_1618 | Q88MF3 | 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (MECDP-synthase) (MECPP-synthase) (MECPS) (EC 4.6.1.12) (EC 4.6.1.12; primary bucket kegg:ppu00900)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)

## Generic Module Context

### Working Scope

The bacterial methylerythritol phosphate (MEP/DOXP) route converts pyruvate and glyceraldehyde 3-phosphate through seven reactions into isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP). DXS forms the shared branch-point metabolite DXP, Dxr commits DXP to the MEP route, IspD-IspG build HMBPP, and IspH produces the two universal five-carbon isoprenoid precursors. DXP use in thiamine or pyridoxal-phosphate biosynthesis and downstream prenyl-diphosphate elongation are outside this module.

### Provisional Biological Outline

- MEP isoprenoid precursor biosynthesis
  - 1. DXP formation from pyruvate and glyceraldehyde 3-phosphate
  - DXS-dependent DXP formation
    - DXP synthase activity (molecular player: DXP synthase family; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
  - 2. Commitment of DXP to MEP
  - Dxr-dependent MEP formation
    - DXP reductoisomerase activity (molecular player: DXP reductoisomerase family; activity or role: 1-deoxy-D-xylulose-5-phosphate reductoisomerase activity)
  - 3. CDP-ME formation
  - IspD-dependent CDP-ME formation
    - MEP cytidylyltransferase activity (molecular player: IspD MEP cytidylyltransferase family; activity or role: 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase activity)
  - 4. CDP-ME 2-phosphate formation
  - IspE-dependent CDP-ME 2-phosphate formation
    - CDP-ME kinase activity (molecular player: IspE CDP-ME kinase family; activity or role: 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase activity)
  - 5. ME-CPP formation
  - IspF-dependent ME-CPP formation
    - ME-CPP synthase activity (molecular player: IspF ME-CPP synthase family; activity or role: 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase activity)
  - 6. HMBPP formation
  - IspG-dependent HMBPP formation
    - Flavodoxin-coupled HMBPP synthase activity (molecular player: IspG HMBPP synthase family; activity or role: 4-hydroxy-3-methylbut-2-enyl-diphosphate synthase activity (flavodoxin))
  - 7. IPP and DMAPP formation
  - IspH-dependent IPP and DMAPP formation
    - HMBPP reductase activity (molecular player: IspH HMBPP reductase family; activity or role: 4-hydroxy-3-methylbut-2-enyl diphosphate reductase activity)

### Known Relationships Among Steps

- DXS-dependent DXP formation feeds into Dxr-dependent MEP formation: DXS supplies DXP to the committed MEP reaction.
- Dxr-dependent MEP formation feeds into IspD-dependent CDP-ME formation: Dxr supplies MEP to IspD.
- IspD-dependent CDP-ME formation feeds into IspE-dependent CDP-ME 2-phosphate formation: IspD supplies CDP-ME to IspE.
- IspE-dependent CDP-ME 2-phosphate formation feeds into IspF-dependent ME-CPP formation: IspE supplies CDP-ME 2-phosphate to IspF.
- IspF-dependent ME-CPP formation feeds into IspG-dependent HMBPP formation: IspF supplies ME-CPP to IspG.
- IspG-dependent HMBPP formation feeds into IspH-dependent IPP and DMAPP formation: IspG supplies HMBPP to the terminal IspH reaction.

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

# Commissioned Module/Pathway/Taxon Review: MEP Isoprenoid Precursor Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00900` — "Terpenoid backbone biosynthesis"
**Module scope:** MEP/DOXP route from pyruvate + glyceraldehyde-3-phosphate → IPP + DMAPP (seven committed steps)

---

## 1. Executive Summary

The methylerythritol phosphate (MEP/DOXP) module for isoprenoid precursor biosynthesis is **complete and fully satisfiable** in *Pseudomonas putida* KT2440. All seven committed enzymatic steps — DXS, Dxr, IspD, IspE, IspF, IspG, and IspH — are encoded by **single-copy, unambiguously assigned genes**, each mapping to exactly one distinct KEGG Orthology (KO) identifier with no paralog ambiguity. KT2440 produces the universal five-carbon precursors isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP) **exclusively via the MEP route**; it does not encode the mevalonate (MVA) pathway. Every one of the seven module steps should therefore be marked **covered**.

The candidate gene list supplied for bucket `ppu00900` is substantially **over-inclusive** and requires organism-aware revision. Two categories of genes are misassigned relative to the true MEP module. First, **five acetyl-CoA acetyltransferase / thiolase genes** (PP_0582, PP_2215, PP_3355, PP_3754/*bktB*, PP_4636/*yqeF*) plus a 3-ketoacyl-CoA thiolase (PP_2051/*fadA*) map only to the top acetyl-CoA node of KEGG map00900 (the MVA branch). Because KT2440 lacks all downstream MVA enzymes (HMG-CoA synthase, HMG-CoA reductase, mevalonate kinase, phosphomevalonate kinase, and diphosphomevalonate decarboxylase are all absent), these thiolases are **over-propagated MVA-node annotations** with no role in isoprenoid precursor synthesis — they should be marked **not_expected_in_target_taxon** for this module. Second, several genes in the bucket (*ispA*, *ispB*, *uppS*, *ubiX*) are **downstream prenyl-diphosphate elongation / ubiquinone / cell-envelope enzymes** that belong to neighboring pathways and should be kept separate from the seven-step MEP core.

A notable curation correction emerged during the investigation: **KT2440 encodes no isopentenyl-diphosphate isomerase (IDI; EC 5.3.3.2)** of either type I (K01823) or type II (K02066). An early hypothesis that two type-II IDI paralogs existed was **refuted** — the K02066 hits (PP_0142, PP_0959) were a KO collision with the MlaE phospholipid ABC-transporter permease, not IDI. The absence of IDI is **expected biology, not a gap**: bacterial IspH produces both IPP and DMAPP directly, so a dedicated isomerase is dispensable. Overall, the bucket `ppu00900` conflates three distinct biological processes (MEP core, MVA node, and downstream prenyl elongation) and should be revised to the canonical 7-step MEP module (KEGG **M00096** / MetaCyc **NONMEVIPP-PWY**).

---

## 2. Target-Organism Pathway Definition

### 2.1 What the module includes

The MEP isoprenoid precursor module in *P. putida* KT2440 comprises exactly seven biochemical reactions converting the central-metabolism substrates **pyruvate** and **D-glyceraldehyde 3-phosphate** into the two universal C5 isoprenoid building blocks, **IPP** and **DMAPP**:

1. **DXP formation** — condensation of pyruvate + G3P to 1-deoxy-D-xylulose 5-phosphate (DXP) by DXS.
2. **Commitment to MEP** — reductoisomerization of DXP to 2-C-methyl-D-erythritol 4-phosphate (MEP) by Dxr (the committed, rate-influencing step).
3. **CDP-ME formation** — cytidylylation of MEP to 4-diphosphocytidyl-2-C-methyl-D-erythritol (CDP-ME) by IspD.
4. **CDP-ME 2-phosphate formation** — ATP-dependent phosphorylation by IspE.
5. **ME-CPP formation** — cyclization to 2-C-methyl-D-erythritol 2,4-cyclodiphosphate (ME-CPP) by IspF.
6. **HMBPP formation** — flavodoxin-coupled reductive ring opening to (E)-4-hydroxy-3-methylbut-2-enyl diphosphate (HMBPP) by IspG.
7. **IPP + DMAPP formation** — terminal reductive dehydroxylation by IspH, yielding **both** IPP and DMAPP in a single branch point.

This process is directly supported for *P. putida* by [PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/): *"In P. putida and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway."*

### 2.2 What must be kept separate

The following neighboring processes are **outside** the MEP core module and should not be counted toward its satisfiability, even though the current bucket lists their genes:

| Neighboring process | Genes in bucket | KO / EC | Why separate |
|---|---|---|---|
| Mevalonate (MVA) node | PP_0582, PP_2215, PP_3355, PP_3754 (*bktB*), PP_4636 (*yqeF*), PP_2051 (*fadA*) | K00626 / K00632 (EC 2.3.1.9 / 2.3.1.16) | Acetyl-CoA thiolases; only map to the MVA top node, which has no downstream in KT2440 |
| Prenyl-diphosphate elongation | *ispA* (PP_0528) | K13789 (EC 2.5.1.1/2.5.1.10) | Farnesyl-PP synthase; **consumes** IPP/DMAPP, downstream of module |
| Ubiquinone biosynthesis | *ispB* (PP_0687), *ubiX* (PP_0548) | K02523 / K03186 | Octaprenyl-PP synthase & flavin prenyltransferase; ubiquinone map ppu00130/ppu00627 |
| Cell-envelope (peptidoglycan carrier) | *uppS* (PP_1595) | K00806 (EC 2.5.1.31) | Undecaprenyl-PP synthase; downstream prenyl elongation |

### 2.3 Alternate names and database definitions

- **KEGG:** map00900 "Terpenoid backbone biosynthesis" (the bucket) is a broad overview map that fuses MEP, MVA, IDI, and prenyl-transferase steps. The specific MEP sub-module is **KEGG module M00096** ("C5 isoprenoid biosynthesis, non-mevalonate pathway").
- **MetaCyc:** **NONMEVIPP-PWY** ("methylerythritol phosphate pathway I").
- **Synonyms:** MEP pathway = DOXP pathway = non-mevalonate pathway = Rohmer pathway.

---

## 3. Expected Step Model

```
   pyruvate + D-glyceraldehyde-3-P
             │
             ▼   [1] DXS  (dxs, PP_0527, K01662, EC 2.2.1.7)
            DXP
             │
             ▼   [2] Dxr  (dxr, PP_1597, K00099, EC 1.1.1.267)   ← committed step
            MEP
             │
             ▼   [3] IspD (ispD, PP_1614, K00991, EC 2.7.7.60)
           CDP-ME
             │
             ▼   [4] IspE (ispE, PP_0723, K00919, EC 2.7.1.148)
        CDP-ME-2-P
             │
             ▼   [5] IspF (ispF, PP_1618, K01770, EC 4.6.1.12)
           ME-CPP
             │
             ▼   [6] IspG (ispG, PP_0853, K03526, EC 1.17.7.3)  [flavodoxin-coupled]
           HMBPP
             │
             ▼   [7] IspH (ispH, PP_0606, K03527, EC 1.17.7.4)
       ┌─────┴─────┐
      IPP        DMAPP        ← IspH yields BOTH; no IDI required
```

**Key architectural note:** Because IspH produces both IPP and DMAPP directly, the isopentenyl-diphosphate isomerase (IDI) that shuttles between them is **not obligatory** in MEP-only organisms. Its absence in KT2440 is fully consistent with a complete, functional module.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence MEP core genes (all "covered")

All seven core genes are Swiss-Prot reviewed and map cleanly to single KOs. Their annotations are **homology-based** (UniProt Protein Existence level 3, "inferred from homology") with **no ECO:0000269 experimental evidence tags** at the individual-protein level, but pathway-level functional support exists for the entry steps (see §4.2).

| Step | Gene | Locus | UniProt | KO | EC | Assignment confidence |
|---|---|---|---|---|---|---|
| 1 | *dxs* | PP_0527 | Q88QG7 | K01662 | 2.2.1.7 | High — single copy, distinct KO |
| 2 | *dxr* | PP_1597 | Q88MH4 | K00099 | 1.1.1.267 | High — single copy, distinct KO |
| 3 | *ispD* | PP_1614 | Q88MF7 | K00991 | 2.7.7.60 | High — single copy, distinct KO |
| 4 | *ispE* | PP_0723 | Q88PX5 | K00919 | 2.7.1.148 | High — single copy, distinct KO |
| 5 | *ispF* | PP_1618 | Q88MF3 | K01770 | 4.6.1.12 | High — single copy, distinct KO |
| 6 | *ispG* | PP_0853 | Q88PJ7 | K03526 | 1.17.7.3 | High — single copy, distinct KO |
| 7 | *ispH* | PP_0606 | Q88Q89 | K03527 | 1.17.7.4 | High — single copy, distinct KO |

This complement, confirmed as finding F001, represents an unambiguous, single-copy assignment of every committed MEP step. Each step maps to exactly one gene with one distinct KO — there is no paralog ambiguity anywhere in the core module, and every gene is present in both the KEGG genome ppu and the matching UniProt candidate list.

**Genomic context** reinforces these assignments and matches the canonical Gram-negative MEP layout (finding F004): *dxs* (PP_0527)–*ispA* (PP_0528) are adjacent (likely operon); *dxr* (PP_1597) sits beside *uppS* (PP_1595); *ispD* (PP_1614) and *ispF* (PP_1618) lie in one ~5-gene window (the classic *ispDF* region); *ispE*, *ispG*, and *ispH* are dispersed singletons. This dispersed-but-conserved arrangement is typical of β/γ-proteobacteria and lends structural credibility to the annotations.

### 4.2 Functional / flux evidence

Direct experimental support in KT2440 exists at the **pathway level** for the two entry enzymes. [PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/) engineered KT2440 for isoprenoid (lycopene) production and reported: *"we compared lycopene production in cells expressing the Myxococcus xanthus MVA pathway genes or endogenous MEP pathway genes (dxs, dxr, idi)."* Overexpression of endogenous *dxs* and *dxr* increased isoprenoid flux, demonstrating these are the operative MEP enzymes in the strain. (Note the paper's use of "idi" — see §5.3 for the correction on IDI.)

### 4.3 Low-confidence / misassigned genes in the bucket

| Gene | Locus | Bucket EC | True role | Recommended call |
|---|---|---|---|---|
| PP_0582 | — | EC 2.3.1.9 (K00626) | Thiolase (fatty-acid/β-oxidation or PHA metabolism) | not_expected (MVA over-annotation) |
| PP_2215 | — | EC 2.3.1.9 (K00626) | Acetyl-CoA acetyltransferase | not_expected (MVA over-annotation) |
| PP_3355 | — | β-ketothiolase (K00626) | Thiolase | not_expected (MVA over-annotation) |
| *bktB* (PP_3754) | — | EC 2.3.1.16/2.3.1.9 | β-ketothiolase (PHA / polyketide metabolism) | not_expected (MVA over-annotation) |
| *yqeF* (PP_4636) | — | EC 2.3.1.9 (K00626) | Acetyl-CoA acetyltransferase | not_expected (MVA over-annotation) |
| *fadA* (PP_2051) | — | EC 2.3.1.16 (K00632) | 3-ketoacyl-CoA thiolase (β-oxidation) | not_expected (belongs to ppu00592/fatty-acid) |
| *ispA* | PP_0528 | EC 2.5.1.1/2.5.1.10 | Farnesyl-PP synthase (downstream) | keep separate (prenyl elongation) |
| *ispB* | PP_0687 | EC 2.5.1.90 | Octaprenyl-PP synthase (ubiquinone) | keep separate (ubiquinone) |
| *uppS* | PP_1595 | EC 2.5.1.31 | Undecaprenyl-PP synthase (cell envelope) | keep separate (prenyl elongation) |
| *ubiX* | PP_0548 | EC 2.5.1.129 | Flavin prenyltransferase (ubiquinone) | keep separate (ubiquinone) |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 No true gaps in the MEP core

Every one of the seven committed MEP steps is covered by a dedicated, single-copy gene. There are **no missing steps** and **no paralog ambiguities** within the core module. This is a clean, textbook Gram-negative MEP complement (finding F006).

### 5.2 Over-annotation: MVA thiolase node

The single largest curation issue is the presence of **six acetyl-CoA thiolase / acetyltransferase genes** in the `ppu00900` bucket (finding F002). These enzymes (EC 2.3.1.9 / 2.3.1.16) catalyze the acetoacetyl-CoA-forming first step of the MVA pathway *and* the reverse thiolytic step of fatty-acid β-oxidation and PHA metabolism. In KEGG map00900 they attach to the **top acetyl-CoA node of the MVA branch**. Because KT2440 lacks every downstream MVA enzyme —

| MVA enzyme | KO | Status in ppu |
|---|---|---|
| HMG-CoA synthase | K01641 | ABSENT |
| HMG-CoA reductase | K00021 | ABSENT |
| Mevalonate kinase | K00869 | ABSENT |
| Phosphomevalonate kinase | K00938 | ABSENT |
| Diphosphomevalonate decarboxylase | K01597 | ABSENT |

— these thiolases **cannot** be feeding an isoprenoid route. Their true physiological roles lie in central carbon / fatty-acid / polyhydroxyalkanoate metabolism (a hallmark of *P. putida*'s metabolic versatility). They are **over-propagated MVA-node annotations** and should be marked **not_expected_in_target_taxon** for this module. This is directly supported by [PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/): *"whereas other bacteria synthesize the same precursors from acetyl-CoA using the unrelated mevalonate (MVA) pathway"* — the MVA route is precisely the alternative that KT2440 does **not** use.

### 5.3 Correction: IDI is absent, and that is expected (not a gap)

An early iteration hypothesized that KT2440 carried two type-II IDI paralogs (PP_0142, PP_0959) based on KEGG K02066 hits. **This was refuted** (finding F005). Authoritative multi-resource negatives establish that KT2440 encodes **no IDI of any type**:

- UniProt proteome UP000000556: **0 entries** for EC 5.3.3.2, **0** for gene:*idi*, **0** for gene:*fni*.
- InterPro: **0** type-I IDI (IPR011876), **0** type-II FMN IDI (IPR011179).
- KEGG: only type-I IDI (K01823) is a listed IDI ortholog, and it is **ABSENT** in ppu.
- The K02066 hits (PP_0142, PP_0959) are a **KO collision** — K02066 is the **MlaE** phospholipid/cholesterol ABC-transporter permease (ppu02010, ABC transporters), not IDI.

This absence is **biologically expected, not a gap**: bacterial IspH generates both IPP and DMAPP directly, so IDI is dispensable in MEP-only organisms. (The *"idi"* referenced in [PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/) most plausibly refers to a heterologous/engineered isomerase used in the lycopene-production construct rather than a genuine endogenous KT2440 gene; the endogenous proteome contains none.) This correction should be propagated so the module is **not** flagged as needing an IDI step.

### 5.4 Evidence caveat

All seven core annotations rest on **homology (UniProt PE=3)** with no protein-level experimental characterization in KT2440 (finding F004). Functional support is pathway-level and limited to *dxs*/*dxr* overexpression phenotypes. This is a strong-but-not-airtight footing: the enzyme families are highly conserved and the gene neighborhoods are canonical, so transfer of function from characterized orthologs (*E. coli*, other pseudomonads) is **strong**, but no crystal structure or in-vitro assay of the KT2440 enzymes themselves has been performed.

---

## 6. Module and GO-Curation Recommendations

### 6.1 Per-step satisfiability calls

| Module step | Gene | Call |
|---|---|---|
| 1. DXP formation | *dxs* PP_0527 | **covered** |
| 2. Commitment to MEP | *dxr* PP_1597 | **covered** |
| 3. CDP-ME formation | *ispD* PP_1614 | **covered** |
| 4. CDP-ME-2-P formation | *ispE* PP_0723 | **covered** |
| 5. ME-CPP formation | *ispF* PP_1618 | **covered** |
| 6. HMBPP formation | *ispG* PP_0853 | **covered** |
| 7. IPP + DMAPP formation | *ispH* PP_0606 | **covered** |
| (IDI, optional) | — | **not_expected_in_target_taxon** |
| MVA thiolase node (×6 genes) | PP_0582/2215/3355/3754/4636/2051 | **not_expected_in_target_taxon** |

**Module verdict: fully satisfiable (7/7 covered).**

### 6.2 Bucket revision (module_needs_revision)

Bucket `kegg:ppu00900` conflates **three distinct biological processes** and should be revised:

1. **MEP core (keep):** the 7 genes above → align to KEGG **M00096** / MetaCyc **NONMEVIPP-PWY**.
2. **MVA node (remove from this module):** 6 thiolase genes → reassign to their true fatty-acid/PHA/central-carbon buckets (e.g., ppu00592, ppu00071, ppu00650).
3. **Downstream prenyl elongation / ubiquinone (keep separate):** *ispA* (K13789), *ispB* (K02523), *uppS* (K00806), *ubiX* (K03186).

**Recommendation:** create/adopt a dedicated 7-step MEP module document rather than curating against the broad `ppu00900` overview map.

### 6.3 GO-term considerations

No new GO term requests appear necessary — all seven activities have established GO molecular-function terms (e.g., 1-deoxy-D-xylulose-5-phosphate synthase activity, GO:0008661; DXP reductoisomerase activity, GO:0030604). Curators should ensure the KT2440 gene products carry **homology-based (ISS/ISO)** evidence codes, not experimental (EXP/IDA) codes, reflecting the PE=3 status. The MVA thiolases should **not** carry any isoprenoid-biosynthesis GO annotation.

---

## 7. Genes to Promote to Full Review

Priority for full `fetch-gene` review, ranked by curation impact:

1. **PP_0142 and PP_0959 (highest priority)** — must be re-annotated away from any IDI/K02066 isoprenoid role and confirmed as **MlaE** ABC-transporter permease. These are active mis-annotation risks that could wrongly satisfy a phantom IDI step.
2. **The six thiolase genes** (PP_0582, PP_2215, PP_3355, PP_3754/*bktB*, PP_4636/*yqeF*, PP_2051/*fadA*) — promote to confirm their true fatty-acid/PHA/central-carbon roles and formally strip the MVA/isoprenoid over-annotation.
3. ***dxr* PP_1597 and *dxs* PP_0527** — the two steps with pathway-level functional evidence; worth a full review to attach the [PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/) flux data as supporting evidence and to consider promoting their evidence code.
4. ***ispG* PP_0853 and *ispH* PP_0606** — the two Fe-S / flavodoxin-coupled steps; worth confirming the electron-donor (flavodoxin/ferredoxin) partners are present in KT2440, since these are the most cofactor-dependent steps.

---

## 8. Evidence Base and Key References

**[PMID: 31500633](https://pubmed.ncbi.nlm.nih.gov/31500633/)** — *Engineering Pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors.* This is the anchor reference for the entire review. It establishes directly that (a) *P. putida* makes IPP/DMAPP from pyruvate and G3P via the MEP pathway (*"In P. putida and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway"*), which anchors the covered calls for all seven steps; (b) the MVA route is the alternative that other bacteria — but not KT2440 — use (*"whereas other bacteria synthesize the same precursors from acetyl-CoA using the unrelated mevalonate (MVA) pathway"*), which supports the not_expected calls for the six thiolases; and (c) endogenous *dxs* and *dxr* are functionally operative and flux-relevant (*"endogenous MEP pathway genes (dxs, dxr, idi)"*), providing the only pathway-level functional evidence in the review.

**Authoritative database resources consulted (negatives and mappings):**
- **KEGG GENOME ppu** — KO-to-gene mapping for all seven MEP steps; confirmed absence of type-I IDI (K01823) and all five downstream MVA enzymes (K01641, K00021, K00869, K00938, K01597).
- **UniProt proteome UP000000556** (taxon 160488) — Swiss-Prot reviewed entries with PE=3 for all seven core genes; zero hits for EC 5.3.3.2 / gene:idi / gene:fni.
- **InterPro** — zero hits for type-I (IPR011876) and type-II (IPR011179) IDI domains, confirming true IDI absence.
- **KEGG module M00096 / MetaCyc NONMEVIPP-PWY** — canonical 7-step MEP module definitions used as the reference for bucket revision.

---

## 9. Limitations and Knowledge Gaps

1. **No protein-level experimental evidence in KT2440.** All seven core annotations are homology inferences (PE=3). No in-vitro enzyme assays or structures exist for the KT2440 proteins themselves. Transfer from characterized orthologs is strong given conservation and canonical gene neighborhoods, but is formally indirect.
2. **Functional flux evidence is limited to entry steps.** Only *dxs*/*dxr* have phenotypic (lycopene-flux) support. Steps 3–7 (IspD–IspH) rest on sequence/annotation alone.
3. **Electron-donor partners for IspG/IspH not verified here.** These enzymes require flavodoxin/ferredoxin and reductase partners; their presence and pairing in KT2440 was not independently confirmed.
4. **Thiolase true functions not individually resolved.** The six thiolases were ruled out of the MEP/MVA module by pathway logic, but each one's precise physiological substrate (β-oxidation vs PHA vs other) was not individually established.
5. **Single-paper direct literature base.** Direct target-organism literature was limited to one engineering study; deeper strain-specific characterization literature may exist but was not exhaustively surveyed.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Re-annotate PP_0142 / PP_0959** in the curation database from IDI/K02066 to MlaE ABC-transporter permease, closing the mis-annotation loophole that could falsely satisfy an IDI step.
2. **Formally reassign the six thiolase genes** out of `ppu00900` to their correct fatty-acid/PHA/central-carbon buckets and strip isoprenoid GO annotations.
3. **Adopt KEGG M00096 / MetaCyc NONMEVIPP-PWY as the module reference** instead of the broad overview map `ppu00900`; split the bucket into MEP-core, MVA-node, and prenyl-elongation sub-groups.
4. **Targeted knockout / complementation** of *ispD–ispH* in KT2440 to convert the homology-based (PE=3) annotations into experimental evidence, if strain-engineering resources permit.
5. **Verify IspG/IspH electron-donor partners** (flavodoxin, flavodoxin reductase, ferredoxin) are encoded and expressed, since these are the module's most cofactor-dependent steps.
6. **Expert/literature check** on whether any recent *P. putida* KT2440 proteomics or Tn-seq essentiality dataset provides direct evidence for the mid-pathway MEP genes, which would upgrade their confidence.

---

*Report prepared for manual module satisfiability and gene-annotation curation. All satisfiability calls, over-annotation flags, and the IDI correction are ready for propagation to the module document for KEGG bucket `ppu00900` → revised MEP module (M00096) in P. putida KT2440.*


## Artifacts

- [OpenScientist final report](PSEPK__mep_isoprenoid_precursor_biosynthesis__ppu00900-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__mep_isoprenoid_precursor_biosynthesis__ppu00900-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31500633