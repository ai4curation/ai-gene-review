---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T16:43:21.867728'
end_time: '2026-06-28T17:13:30.749352'
duration_seconds: 1808.88
template_file: templates/module_research.md.j2
template_variables:
  module_title: VEGFR signaling pathway module
  module_summary: VEGF ligands activate endothelial VEGF receptor tyrosine kinases,
    coupling receptor phosphorylation to PLC-gamma, PI3K, and migration programs that
    drive vascular growth and permeability.
  module_outline: "- VEGFR signaling pathway\n  - 1. vegf ligand-receptor engagement\n\
    \  - VEGF ligand engages VEGFR\n    - VEGFA ligand (molecular player: VEGFA)\n\
    \    - KDR/VEGFR2 receptor (molecular player: KDR/VEGFR2 receptor family/ortholog\
    \ group)\n    - FLT1/VEGFR1 receptor (molecular player: FLT1/VEGFR1 receptor family/ortholog\
    \ group)\n  - 2. phospholipase and lipid kinase recruitment\n  - PLC/PI3K recruitment\n\
    \    - PLCG1 effector (molecular player: PLCG1)\n    - PI3K p85 adaptor (molecular\
    \ player: PI3K p85 adaptor family/ortholog group)\n  - 3. angiogenic output\n\
    \  - Endothelial angiogenic output\n    - VEGFR2 kinase output (molecular player:\
    \ VEGFR2 kinase output family/ortholog group)\n    - PI3K catalytic branch (molecular\
    \ player: PI3K catalytic branch family/ortholog group)"
  module_connections: '- VEGF ligand engages VEGFR causes PLC/PI3K recruitment: The
    initiating event promotes phospholipase and lipid kinase recruitment.

    - PLC/PI3K recruitment causes Endothelial angiogenic output: PLC/PI3K recruitment
    leads to angiogenic output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 47
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: vegfr_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: vegfr_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: vegfr_signaling-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Commissioned Review Brief

## Review Topic

VEGFR signaling pathway module

## Working Scope

VEGF ligands activate endothelial VEGF receptor tyrosine kinases, coupling receptor phosphorylation to PLC-gamma, PI3K, and migration programs that drive vascular growth and permeability.

## Provisional Biological Outline

- VEGFR signaling pathway
  - 1. vegf ligand-receptor engagement
  - VEGF ligand engages VEGFR
    - VEGFA ligand (molecular player: VEGFA)
    - KDR/VEGFR2 receptor (molecular player: KDR/VEGFR2 receptor family/ortholog group)
    - FLT1/VEGFR1 receptor (molecular player: FLT1/VEGFR1 receptor family/ortholog group)
  - 2. phospholipase and lipid kinase recruitment
  - PLC/PI3K recruitment
    - PLCG1 effector (molecular player: PLCG1)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)
  - 3. angiogenic output
  - Endothelial angiogenic output
    - VEGFR2 kinase output (molecular player: VEGFR2 kinase output family/ortholog group)
    - PI3K catalytic branch (molecular player: PI3K catalytic branch family/ortholog group)

## Known Relationships Among Steps

- VEGF ligand engages VEGFR causes PLC/PI3K recruitment: The initiating event promotes phospholipase and lipid kinase recruitment.
- PLC/PI3K recruitment causes Endothelial angiogenic output: PLC/PI3K recruitment leads to angiogenic output.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Commissioned Review Brief

## Review Topic

VEGFR signaling pathway module

## Working Scope

VEGF ligands activate endothelial VEGF receptor tyrosine kinases, coupling receptor phosphorylation to PLC-gamma, PI3K, and migration programs that drive vascular growth and permeability.

## Provisional Biological Outline

- VEGFR signaling pathway
  - 1. vegf ligand-receptor engagement
  - VEGF ligand engages VEGFR
    - VEGFA ligand (molecular player: VEGFA)
    - KDR/VEGFR2 receptor (molecular player: KDR/VEGFR2 receptor family/ortholog group)
    - FLT1/VEGFR1 receptor (molecular player: FLT1/VEGFR1 receptor family/ortholog group)
  - 2. phospholipase and lipid kinase recruitment
  - PLC/PI3K recruitment
    - PLCG1 effector (molecular player: PLCG1)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)
  - 3. angiogenic output
  - Endothelial angiogenic output
    - VEGFR2 kinase output (molecular player: VEGFR2 kinase output family/ortholog group)
    - PI3K catalytic branch (molecular player: PI3K catalytic branch family/ortholog group)

## Known Relationships Among Steps

- VEGF ligand engages VEGFR causes PLC/PI3K recruitment: The initiating event promotes phospholipase and lipid kinase recruitment.
- PLC/PI3K recruitment causes Endothelial angiogenic output: PLC/PI3K recruitment leads to angiogenic output.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

# VEGFR Signaling Pathway Module: A Comprehensive Review

## 1. Executive Summary

The vascular endothelial growth factor receptor (VEGFR) signaling pathway constitutes a central regulatory axis governing vascular development, homeostasis, and pathological angiogenesis. This system comprises five principal VEGF ligands (VEGF-A, VEGF-B, VEGF-C, VEGF-D, and PlGF) that activate three receptor tyrosine kinases (VEGFR1/FLT1, VEGFR2/KDR, and VEGFR3/FLT4) along with neuropilin co-receptors (NRP1, NRP2) (perezgutierrez2023biologyandtherapeutic pages 5-6, lee2025vascularendothelialgrowth pages 3-4). The core signaling module centers on VEGF-A binding to VEGFR2, which triggers receptor dimerization and trans-autophosphorylation at multiple tyrosine residues, recruiting PLCγ1 and PI3K effectors that drive endothelial cell proliferation, migration, survival, and vascular permeability (shah2025targetingvascularendothelial pages 4-6, perezgutierrez2023biologyandtherapeutic pages 6-7). VEGFR1 primarily functions as a high-affinity decoy receptor that sequesters VEGF-A to modulate VEGFR2 signaling intensity, while VEGFR3 predominantly governs lymphangiogenesis (shaik2020structuralbasisfor pages 4-6, perezgutierrez2023biologyandtherapeutic pages 7-8). The evolutionary roots of VEGF/VEGFR signaling trace to cnidarian PDGF/VEGF-like growth factors, with extensive diversification through vertebrate whole-genome duplications (rauniyar2023expansionandcollapse pages 3-6, rauniyar2023expansionandcollapse pages 1-3). Despite decades of research and the clinical success of anti-VEGF therapies, significant controversies remain regarding intracrine versus paracrine signaling modes, the signaling capacity of VEGFR1, the role of receptor trafficking in signal specification, and vascular bed-specific pathway utilization.

## 2. Definition and Biological Boundaries

### 2.1 Scope of the System

The VEGFR signaling pathway module encompasses the molecular events from extracellular VEGF ligand engagement through receptor activation to the immediate downstream effector cascades that specify endothelial angiogenic responses. The system includes: (i) VEGF ligand–receptor engagement, wherein VEGF-A binds VEGFR2/KDR to initiate signaling; (ii) phospholipase and lipid kinase recruitment, specifically PLCγ1 and PI3K pathway activation downstream of receptor phosphorylation; and (iii) the angiogenic output programs controlling endothelial proliferation, migration, survival, tube formation, and vascular permeability (perezgutierrez2023biologyandtherapeutic pages 3-5, shah2025targetingvascularendothelial pages 4-6).

The VEGF ligand family includes VEGF-A (the principal angiogenic ligand, with multiple splice isoforms including VEGF-A121, VEGF-A165, VEGF-A189, and anti-angiogenic VEGF165b), VEGF-B, VEGF-C, VEGF-D, and PlGF, each with distinct receptor binding specificities (perezgutierrez2023biologyandtherapeutic pages 5-6, lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 4-6). Additionally, viral VEGF-E and snake venom VEGF-F represent co-opted VEGFR2-selective ligands (shaik2020structuralbasisfor pages 4-6, rauniyar2023expansionandcollapse pages 8-11).

The following table summarizes the VEGF ligand family and their receptor-binding properties:

| Ligand | Molecular Weight | Receptor Binding Partners | Co-receptors | Primary Biological Function |
|---|---:|---|---|---|
| VEGF-A (canonical family; major isoforms include VEGF-A121, VEGF-A165, VEGF-A189; anti-angiogenic splice variant VEGF165b also described) | ~45 kDa homodimer; VEGF-A165 protomer is 165 aa (lee2025vascularendothelialgrowth pages 3-4, perezgutierrez2023biologyandtherapeutic pages 3-5) | VEGFR1 and VEGFR2; can signal through VEGFR1/VEGFR2 heterodimers; VEGFR2 is the dominant pro-angiogenic signaling receptor (lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6, brogowska2023vascularendothelialgrowth pages 9-11) | NRP1 and NRP2, especially for heparin-binding isoforms such as VEGF-A165 (perezgutierrez2023biologyandtherapeutic pages 5-6, shaik2020structuralbasisfor pages 1-4) | Principal driver of vasculogenesis and angiogenesis; promotes endothelial proliferation, migration, survival, sprouting, and vascular permeability (perezgutierrez2023biologyandtherapeutic pages 3-5, patel2023molecularmechanismsand pages 2-4) |
| VEGF-B (VEGF-B167, VEGF-B186) | Not consistently specified in retrieved evidence; secreted VEGF-family homodimer (lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 1-4) | Binds selectively/exclusively to VEGFR1 (lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6) | Can engage NRP1/NRP2 in VEGF co-receptor complexes, but VEGFR1 is the principal signaling receptor assignment in the retrieved evidence (lee2025vascularendothelialgrowth pages 6-7, perezgutierrez2023biologyandtherapeutic pages 5-6) | More associated with tissue protection, endothelial survival, and metabolic regulation than with strong canonical angiogenic signaling (lee2025vascularendothelialgrowth pages 3-4) |
| VEGF-C | Mature processed form; exact molecular weight not consistently specified in retrieved evidence (perezgutierrez2023biologyandtherapeutic pages 5-6, lee2025vascularendothelialgrowth pages 3-4) | Primarily VEGFR3; also binds VEGFR2, typically with stronger functional emphasis on VEGFR3; can contribute via VEGFR2/VEGFR3 heterodimers (lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 4-6, lee2025vascularendothelialgrowth pages 15-16) | NRP2 is classically associated with lymphatic VEGF signaling; neuropilin co-receptors are broadly involved in VEGF receptor complex formation (lee2025vascularendothelialgrowth pages 6-7, perezgutierrez2023biologyandtherapeutic pages 5-6) | Central regulator of lymphangiogenesis; also contributes to developmental and sprouting angiogenesis, particularly in tip cells and lymphatic endothelium (lee2025vascularendothelialgrowth pages 3-4, perezgutierrez2023biologyandtherapeutic pages 7-8, lee2025vascularendothelialgrowth pages 15-16) |
| VEGF-D | Mature processed form; exact molecular weight not consistently specified in retrieved evidence (perezgutierrez2023biologyandtherapeutic pages 5-6, lee2025vascularendothelialgrowth pages 3-4) | Primarily VEGFR3 and also VEGFR2 (lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 4-6) | NRP2/neuropilin-associated receptor complexes are implicated broadly, though the retrieved evidence emphasizes receptor specificity more than co-receptor specificity (lee2025vascularendothelialgrowth pages 6-7, perezgutierrez2023biologyandtherapeutic pages 5-6) | Lymphangiogenesis and, in some contexts, angiogenesis; supports lymphatic endothelial proliferation, migration, and remodeling (lee2025vascularendothelialgrowth pages 3-4, perezgutierrez2023biologyandtherapeutic pages 7-8) |
| PlGF (placental growth factor) | Exact molecular weight not consistently specified in retrieved evidence (lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 1-4) | Binds selectively/exclusively to VEGFR1 (lee2025vascularendothelialgrowth pages 3-4, shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6) | NRP1 can bind longer heparin-binding PlGF isoforms such as PLGF2; soluble VEGFR1 also binds PlGF (sarabipour2025impactofligand pages 1-4, perezgutierrez2023biologyandtherapeutic pages 5-6) | Modulates angiogenesis mainly by VEGFR1-centered signaling and by redistributing VEGF-A availability; important in inflammation and pathological angiogenesis (shaik2020structuralbasisfor pages 4-6, perezgutierrez2023biologyandtherapeutic pages 5-6) |
| VEGF-E (viral VEGF) | Viral VEGF-family protein; exact molecular weight not consistently specified in retrieved evidence (shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6) | Selectively binds VEGFR2 (shaik2020structuralbasisfor pages 4-6) | Not clearly defined in retrieved evidence (shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6) | Potent VEGFR2 agonist used by viruses to co-opt host angiogenic signaling; strongly pro-angiogenic/vascular remodeling activity inferred from VEGFR2 selectivity (shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6) |
| VEGF-F (snake venom VEGF) | Venom-derived VEGF-family protein; exact molecular weight not consistently specified in retrieved evidence (shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6) | Selectively binds VEGFR2 (shaik2020structuralbasisfor pages 4-6) | Not clearly defined in retrieved evidence (shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6) | Venom-associated vascular factor that promotes vasodilation/vascular permeability and VEGFR2-driven angiogenic-like responses (shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 4-6, rauniyar2023expansionandcollapse pages 8-11) |


*Table: This table summarizes the major VEGF ligand family members, their receptor-binding specificities, co-receptor usage, and dominant biological functions. It is useful for distinguishing the VEGFR2-centered angiogenic ligands from VEGFR1- and VEGFR3-biased ligands, as well as from viral and venom-derived VEGF mimetics.*

### 2.2 Boundaries and Neighboring Pathways

Several related but distinct systems should be delineated from the core VEGFR module. The Notch-DLL4 pathway operates as a lateral inhibition mechanism that restricts tip cell formation and is coupled to, but not part of, the core VEGFR2 signaling cascade (perezgutierrez2023biologyandtherapeutic pages 7-8, perezgutierrez2023biologyandtherapeutic pages 3-5). Similarly, angiopoietin-Tie2 signaling governs vessel maturation and stabilization as a complementary but mechanistically independent axis. The PDGF-PDGFR pathway, though sharing evolutionary origins with VEGF/VEGFR, operates primarily on pericytes and smooth muscle cells rather than endothelial cells (rauniyar2023expansionandcollapse pages 1-3). VEGFR3-driven lymphangiogenesis, while sharing receptor family membership, constitutes a functionally separable program primarily active in lymphatic rather than blood vascular endothelium (perezgutierrez2023biologyandtherapeutic pages 7-8, lee2025vascularendothelialgrowth pages 15-16).

## 3. Mechanistic Overview

### 3.1 Step 1: VEGF Ligand–Receptor Engagement

VEGF-A, a 45-kDa homodimeric glycoprotein, is the predominant ligand driving angiogenic VEGFR2 signaling (lee2025vascularendothelialgrowth pages 3-4). VEGF-A binds with high affinity to both VEGFR1 (~2–10 pM Kd) and VEGFR2 (~100–400 pM Kd), but productive signaling occurs primarily through VEGFR2 (shaik2020structuralbasisfor pages 4-6). All three VEGFRs share a conserved architecture: seven extracellular immunoglobulin-like (Ig) domains, a single transmembrane domain, a juxtamembrane region, and a split tyrosine kinase domain with a flexible C-terminal tail (shaik2020structuralbasisfor pages 6-7). VEGF-A contacts VEGFR2 primarily through extracellular Ig domains D2 and D3, with D2 mediating hydrophobic interactions and D3 contributing hydrophilic contacts (shaik2020structuralbasisfor pages 6-7). For the longer VEGF-A165 isoform, the heparin-binding domain (HBD, residues 111–165) additionally engages VEGFR2 domain D1, and this interaction is critical for full mitogenic potency (shaik2020structuralbasisfor pages 6-7).

Neuropilin-1 (NRP1) functions as a non-kinase co-receptor that enhances VEGF-A165 binding to VEGFR2 by engaging the heparin-binding domain present in longer VEGF-A isoforms, thereby stabilizing productive signaling complexes at the cell surface (sarabipour2025impactofligand pages 1-4, lee2025vascularendothelialgrowth pages 6-7, perezgutierrez2023biologyandtherapeutic pages 5-6).

The following table compares the three VEGF receptors:

| Feature | VEGFR1/FLT1 | VEGFR2/KDR | VEGFR3/FLT4 |
|---|---|---|---|
| Size (amino acids) | 1312 aa (shaik2020structuralbasisfor pages 4-6) | 1337 aa (shaik2020structuralbasisfor pages 4-6) | 1363 aa (shaik2020structuralbasisfor pages 4-6) |
| Molecular weight | ~180 kDa glycoprotein (shaik2020structuralbasisfor pages 4-6, brogowska2023vascularendothelialgrowth pages 9-11) | ~200–230 kDa glycoprotein (shaik2020structuralbasisfor pages 4-6, brogowska2023vascularendothelialgrowth pages 9-11) | ~195 kDa; extracellularly cleaved into disulfide-linked heterodimeric subunits (perezgutierrez2023biologyandtherapeutic pages 5-6, shaik2020structuralbasisfor pages 4-6) |
| VEGF-A binding affinity | High affinity for VEGF-A; ~2–10 pM and higher than VEGFR2; often acts as VEGF sink/decoy (shaik2020structuralbasisfor pages 4-6, lee2025vascularendothelialgrowth pages 3-4) | Lower affinity than VEGFR1; ~100–400 pM, but principal pro-angiogenic signal-transducing receptor for VEGF-A (shaik2020structuralbasisfor pages 4-6, brogowska2023vascularendothelialgrowth pages 9-11) | Not a primary VEGF-A receptor; primarily responds to VEGF-C/VEGF-D, though VEGFR2/VEGFR3 heterodimers can modulate blood vascular development (lee2025vascularendothelialgrowth pages 3-4, lee2025vascularendothelialgrowth pages 15-16) |
| Kinase activity | Weak kinase activity; ~10-fold lower than VEGFR2 in endothelial cells; limited signaling due in part to inhibitory juxtamembrane features (shaik2020structuralbasisfor pages 4-6, lee2025vascularendothelialgrowth pages 3-4, perezgutierrez2023biologyandtherapeutic pages 5-6) | Strong kinase activity; dominant endothelial signaling receptor coupling to PLCγ, PI3K/AKT, ERK/MAPK, permeability and migration pathways (shah2025targetingvascularendothelial pages 4-6, patel2023molecularmechanismsand pages 2-4) | Active RTK for lymphatic signaling; promotes proliferation, migration and survival mainly in lymphatic endothelium, including PI3K/AKT outputs (perezgutierrez2023biologyandtherapeutic pages 7-8, lee2025vascularendothelialgrowth pages 15-16) |
| Primary ligands | VEGF-A, VEGF-B, PlGF; also bound by soluble VEGFR1 through retained extracellular domains D2-D3 (perezgutierrez2023biologyandtherapeutic pages 5-6, lee2025vascularendothelialgrowth pages 3-4) | VEGF-A is the principal ligand; also binds VEGF-C and VEGF-D, and selectively viral VEGF-E / venom VEGF-F in comparative studies (shaik2020structuralbasisfor pages 4-6, perezgutierrez2023biologyandtherapeutic pages 3-5) | VEGF-C and VEGF-D are primary ligands; highest functional emphasis on VEGF-C/D-driven lymphangiogenic signaling (perezgutierrez2023biologyandtherapeutic pages 5-6, lee2025vascularendothelialgrowth pages 3-4, lee2025vascularendothelialgrowth pages 15-16) |
| Expression pattern | Endothelial cells but also many non-endothelial cells; very low surface fraction and rapid internalization/recycling in HUVECs; enriched in stalk cells and in some tissue-protective/non-angiogenic contexts (sarabipour2024traffickingdynamicsof pages 1-2, lee2025vascularendothelialgrowth pages 3-4, lee2025vascularendothelialgrowth pages 14-15) | Predominantly endothelial; major receptor in vascular endothelium and tip cells; trafficking altered by ligand binding with increased internalization of ligand-bound receptor (sarabipour2025impactofligand pages 1-4, sarabipour2024traffickingdynamicsof pages 1-2, perezgutierrez2023biologyandtherapeutic pages 7-8) | Mainly lymphatic endothelial cells in adults; also present in some quiescent vascular ECs and highly expressed in angiogenic tip cells during development/sprouting (perezgutierrez2023biologyandtherapeutic pages 7-8, lee2025vascularendothelialgrowth pages 14-15, lee2025vascularendothelialgrowth pages 15-16) |
| Key functions | VEGF sequestration/decoy function, modulation of VEGFR2 signaling, tissue protection/metabolic regulation, some context-dependent signaling, control of ischemia-driven angiogenesis via full-length vs soluble isoform balance (bundalo2024redirectingfulllengthflt1 pages 1-5, lee2025vascularendothelialgrowth pages 3-4) | Core driver of angiogenesis: endothelial proliferation, migration, survival, sprouting, permeability, junction remodeling, and tip-cell signaling (perezgutierrez2023biologyandtherapeutic pages 3-5, patel2023molecularmechanismsand pages 2-4, nan2023molecularmechanismof pages 2-4, shah2025targetingvascularendothelial pages 4-6) | Central regulator of lymphangiogenesis; also contributes to early blood vascular development and can sustain angiogenesis via VEGFR2/3 heterodimers (perezgutierrez2023biologyandtherapeutic pages 7-8, lee2025vascularendothelialgrowth pages 14-15, lee2025vascularendothelialgrowth pages 15-16) |
| Soluble isoform | Yes; sFLT1/sVEGFR1 generated by alternative polyadenylation/splicing, lacks transmembrane and kinase domains, retains ligand binding and acts as potent extracellular decoy (bundalo2024redirectingfulllengthflt1 pages 1-5, shaik2020structuralbasisfor pages 4-6, perezgutierrez2023biologyandtherapeutic pages 5-6) | No major physiologic soluble isoform emphasized in the retrieved evidence (brogowska2023vascularendothelialgrowth pages 9-11, shah2025targetingvascularendothelial pages 4-6) | Yes; soluble VEGFR3 reported, binds VEGF-C and VEGF-D (shaik2020structuralbasisfor pages 6-7) |
| Knockout phenotype in mice | Vegfr1/Flt1 null mice are embryonic lethal with hypervascularization; kinase-dead Vegfr1 mice develop relatively normally, supporting a predominant decoy role in development (shaik2020structuralbasisfor pages 4-6, wang2024flt1inactivationpromotes pages 1-5) | Vegfr2/Kdr loss causes early embryonic lethality with failure of vasculogenesis/angiogenesis; mutation of Tyr1173/1175 phenocopies severe developmental failure, underscoring essential signaling function (perezgutierrez2023biologyandtherapeutic pages 6-7) | Essential for lymphatic vessel development; ligand-binding and kinase domains are required for lymphatic but not blood vessel development in mouse studies summarized in review literature (lee2025vascularendothelialgrowth pages 15-16) |


*Table: This table compares VEGFR1/FLT1, VEGFR2/KDR, and VEGFR3/FLT4 across core structural, biochemical, and biological features. It is useful for distinguishing the decoy-biased FLT1 receptor, the dominant angiogenic KDR receptor, and the lymphangiogenic FLT4 receptor.*

### 3.2 Step 2: Receptor Phosphorylation and Effector Recruitment

Ligand binding induces VEGFR2 dimerization and trans-autophosphorylation at multiple tyrosine residues, each serving as a docking site for specific downstream effectors (shah2025targetingvascularendothelial pages 4-6, shaik2020structuralbasisfor pages 10-12). This creates a phosphotyrosine-based signaling platform that recruits PLCγ1, PI3K adaptors, and Src-family kinases.

**Y1175 (Y1173 in mouse) → PLCγ1–PKC–ERK axis.** This is the obligatory mitogenic pathway. Phosphorylated Y1175 recruits PLCγ1, which hydrolyzes phosphatidylinositol 4,5-bisphosphate (PIP2) to generate inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) (shah2025targetingvascularendothelial pages 4-6, sjoberg2023endothelialvegfr2plcγsignaling pages 1-2). IP3 triggers intracellular Ca²⁺ release while DAG activates PKCβ, the major PKC isoform in VEGF-induced mitogenesis (perezgutierrez2023biologyandtherapeutic pages 6-7). PKC then activates the Raf–MEK–ERK cascade, with ERK translocating to the nucleus to phosphorylate transcription factors governing proliferation and differentiation genes (shah2025targetingvascularendothelial pages 4-6). The essentiality of this site is demonstrated by the finding that Tyr1173→Phe mutation in mice causes embryonic lethality phenocopying complete VEGFR2 deletion (perezgutierrez2023biologyandtherapeutic pages 6-7).

**Y1175/PLCγ → eNOS/Src pathway for permeability.** A recent study by Sjöberg et al. (2023) identified a clinically relevant PLCγ pathway downstream of VEGFR2 pY1173 that destabilizes the endothelial barrier. Ca²⁺/PKC-dependent activation of eNOS (phosphorylation at S1177) leads to tyrosine nitration and activation of Src, which phosphorylates VE-cadherin at Y685, causing junctional disassembly and increased vascular permeability (sjoberg2023endothelialvegfr2plcγsignaling pages 1-2, sjoberg2023endothelialvegfr2plcγsignaling pages 2-4).

**Y801 → PI3K/AKT → eNOS.** Juxtamembrane Y801 phosphorylation stimulates maximal kinase activity and couples to PI3K/AKT signaling, promoting eNOS activation and nitric oxide release for endothelial survival and vascular tone regulation (shah2025targetingvascularendothelial pages 4-6, shaik2020structuralbasisfor pages 10-12, shah2025targetingvascularendothelial pages 6-8).

**Y951 (Y949 in mouse) → TSAd/Src → migration/permeability.** This site recruits TSAd (T cell-specific adaptor), coupling VEGFR2 to Src family kinases that drive endothelial migration and junctional remodeling (shaik2020structuralbasisfor pages 10-12, perezgutierrez2023biologyandtherapeutic pages 6-7).

**Y1214 (Y1212 in mouse) → p38 MAPK.** This site preferentially engages the p38 MAPK branch, mediating stress-response and migration-associated signaling distinct from the canonical PLCγ–ERK module (li2025advancesinthe pages 4-5, shaik2020structuralbasisfor pages 10-12).

**Y1054/Y1059 → kinase activation.** Activation loop phosphorylation at these residues is required for maximal VEGFR2 catalytic activity; Y1059 is additionally linked to cytosolic Ca²⁺ flux and MAPK activation (shaik2020structuralbasisfor pages 10-12).

The following table provides a comprehensive summary of VEGFR2 phosphorylation sites and their downstream signaling:

| Phosphorylation Site | Downstream Effector | Signaling Cascade | Biological Output |
|---|---|---|---|
| Y801 | PI3K, AKT, eNOS | VEGFR2 pY801 promotes PKC-PI3K-AKT signaling, leading to eNOS activation and nitric oxide production | Endothelial survival, nitric oxide release, support of permeability-related responses (shah2025targetingvascularendothelial pages 4-6, shah2025targetingvascularendothelial pages 6-8, shaik2020structuralbasisfor pages 10-12) |
| Y951 (human) / Y949 (mouse) | TSAd, Src family kinases | pY951/pY949 recruits TSAd and couples VEGFR2 to Src signaling; this branch also contributes to junctional remodeling and permeability control | Endothelial migration, vascular permeability, barrier destabilization (shaik2020structuralbasisfor pages 10-12, perezgutierrez2023biologyandtherapeutic pages 6-7, lee2025vascularendothelialgrowth pages 11-12) |
| Y1054 / Y1059 | Kinase domain activation machinery; Ca2+-linked signaling from Y1059 | Activation-loop phosphorylation enhances receptor catalytic activity; Y1059 is linked to cytosolic Ca2+ flux and MAPK activation | Maximal VEGFR2 kinase activation, proliferation-associated signaling, propagation of downstream cascades (shaik2020structuralbasisfor pages 10-12) |
| Y1175 (human) / Y1173 (mouse) | PLCγ1 | pY1175/pY1173 recruits PLCγ1, driving PIP2 hydrolysis to IP3 and DAG, followed by PKC activation, Raf-MEK-ERK signaling, Ca2+ mobilization, and eNOS/Src coupling | Core mitogenic signaling, endothelial proliferation, differentiation, permeability, VE-cadherin phosphorylation/internalization, angiogenic activity (shah2025targetingvascularendothelial pages 4-6, li2025advancesinthe pages 4-5, perezgutierrez2023biologyandtherapeutic pages 6-7, sjoberg2023endothelialvegfr2plcγsignaling pages 1-2, sjoberg2023endothelialvegfr2plcγsignaling pages 2-4) |
| Y1214 (human) / Y1212 (mouse) | p38 MAPK pathway components | pY1214/pY1212 preferentially engages the p38 MAPK branch rather than the canonical PLCγ-ERK module | Endothelial migration/stress-response signaling and non-mitogenic angiogenic outputs (shaik2020structuralbasisfor pages 10-12, li2025advancesinthe pages 4-5) |
| Y1319 | Not clearly assigned in the cited sources | Listed as a VEGFR2 phosphosite in structural/signaling summaries, but the present source set does not define a specific obligate effector complex for this residue | Likely contributes to signaling integration, but mechanism remains insufficiently resolved in these sources (shaik2020structuralbasisfor pages 10-12, lee2025vascularendothelialgrowth pages 11-12) |


*Table: This table summarizes the major VEGFR2 phosphotyrosine sites emphasized in recent reviews and primary literature, linking each residue to known downstream effectors, pathway branches, and endothelial outputs. It is useful for distinguishing obligatory mitogenic signaling via Y1175/Y1173 from migration, permeability, and kinase-activation branches mediated by other sites.*

### 3.3 Step 3: Angiogenic Output Programs

The convergence of PLCγ–PKC–ERK, PI3K–AKT, and Src-family kinase pathways produces the integrated angiogenic response:

**Proliferation** is driven primarily through PLCγ1-PKCβ-Raf-MEK-ERK signaling downstream of pY1175, with activated ERK phosphorylating transcription factors ETS, Elf-1, and NFAT for endothelial lineage commitment (shah2025targetingvascularendothelial pages 4-6, perezgutierrez2023biologyandtherapeutic pages 6-7).

**Migration** requires FAK activation downstream of VEGFR2, which recruits Src family kinases and assembles focal adhesion complexes linking the extracellular matrix to the cytoskeleton. FAK activates Rho-family GTPases CDC42 and RAC1, promoting cytoskeletal rearrangement essential for directional migration (shah2025targetingvascularendothelial pages 6-8, shah2025targetingvascularendothelial pages 4-6).

**Survival** is mediated through the TSAd–Src–PI3K–AKT pathway, where AKT phosphorylates regulators of protein synthesis, apoptosis, and cell growth (shah2025targetingvascularendothelial pages 6-8, patel2023molecularmechanismsand pages 2-4).

**Vascular permeability** is controlled through the pY1175/PLCγ/eNOS/Src cascade, which leads to VE-cadherin phosphorylation and internalization. VEGFR2 activation triggers SRC-mediated phosphorylation of VAV2, activating RAC1 and PAK, which phosphorylate VE-cadherin at S665, recruiting β-arrestin2 and promoting VE-cadherin endocytosis to disrupt adherens junctions (sjoberg2023endothelialvegfr2plcγsignaling pages 2-4, nan2023molecularmechanismof pages 2-4, nan2023molecularmechanismof pages 4-6).

**Tip-stalk cell specification** integrates VEGFR signaling with Notch lateral inhibition. VEGF-A-activated tip cells upregulate DLL4, which activates NOTCH1 in adjacent stalk cells, suppressing VEGFR2/VEGFR3 expression and promoting VEGFR1 expression to dampen stalk cell VEGF sensitivity (perezgutierrez2023biologyandtherapeutic pages 7-8, lee2025vascularendothelialgrowth pages 14-15, perezgutierrez2023biologyandtherapeutic pages 3-5).

## 4. Major Molecular Players and Active Assemblies

### 4.1 VEGFR1/FLT1: The Decoy-Signaling Paradox

VEGFR1 exhibits the highest VEGF-A binding affinity among VEGFRs but has approximately 10-fold lower tyrosine kinase activity than VEGFR2 in endothelial cells (shaik2020structuralbasisfor pages 4-6). Mice with kinase-dead VEGFR1 develop relatively normally, establishing that its kinase function is dispensable for embryonic vascular development, while complete FLT1 knockout causes embryonic lethality due to endothelial overgrowth—confirming the essential decoy function (shaik2020structuralbasisfor pages 4-6, lee2025vascularendothelialgrowth pages 3-4). The low kinase activity is attributed to an inhibitory sequence in the juxtamembrane region (lee2025vascularendothelialgrowth pages 3-4).

Soluble VEGFR1 (sFLT1), generated through alternative polyadenylation in intron 13, retains the extracellular VEGF-binding domain but lacks transmembrane and intracellular regions (bundalo2024redirectingfulllengthflt1 pages 1-5). sFLT1 sequesters VEGF-A extracellularly and forms non-signaling homo- and heterodimers with membrane-bound receptors (bundalo2024redirectingfulllengthflt1 pages 1-5, shaik2020structuralbasisfor pages 4-6). A recent study demonstrated that sFLT1 is sufficient for developmental vasculogenesis, whereas full-length FLT1 specifically controls ischemia-driven angiogenesis, revealing isoform-specific functional partitioning (bundalo2024redirectingfulllengthflt1 pages 1-5).

VEGFR1 trafficking differs markedly from VEGFR2: VEGFR1 has faster internalization and recycling rates, maintaining a very low surface fraction, while NRP1 maintains high surface levels (sarabipour2024traffickingdynamicsof pages 1-2). This differential trafficking creates a "reservoir effect" where intracellular VEGFR1 competes substantially with VEGFR2 for ligand inside the cell despite minimal competition at the surface (sarabipour2025impactofligand pages 1-4).

### 4.2 VEGFR2/KDR: The Principal Angiogenic Receptor

VEGFR2 is a 1337-amino acid (~200–230 kDa) glycoprotein that serves as the dominant pro-angiogenic signaling receptor (shaik2020structuralbasisfor pages 4-6, brogowska2023vascularendothelialgrowth pages 9-11). Its trafficking is uniquely regulated by ligand binding, with increased internalization of ligand-bound receptor through clathrin-dependent endocytosis (sarabipour2025impactofligand pages 1-4, perezgutierrez2023biologyandtherapeutic pages 7-8). Both surface and endosomal VEGFR2 populations contribute to signaling, with clathrin-dependent internalization playing important roles in intracellular VEGFR2 activation (perezgutierrez2023biologyandtherapeutic pages 7-8).

VEGFR2 functions within a mechanosensory complex alongside VE-cadherin and PECAM1 at adherens junctions, where it transduces biochemical signals in response to both ligand stimulation and mechanical forces (nan2023molecularmechanismof pages 7-8). This dual sensing capacity integrates chemical and mechanical cues for coordinated vascular remodeling.

### 4.3 VEGFR3/FLT4: Lymphangiogenic and Developmental Roles

VEGFR3, primarily activated by VEGF-C and VEGF-D, is the central regulator of lymphangiogenesis (perezgutierrez2023biologyandtherapeutic pages 7-8, lee2025vascularendothelialgrowth pages 15-16). However, VEGFR3 also sustains angiogenesis in tip cells even when VEGFR2 is inhibited, and VEGFR2/VEGFR3 heterodimers on tip cell filopodia mediate responses to both VEGF-A and VEGF-C (lee2025vascularendothelialgrowth pages 14-15). The ligand-binding and kinase domains of VEGFR3 are essential for lymphatic but not blood vessel development, indicating distinct signaling requirements for these two vascular networks (lee2025vascularendothelialgrowth pages 15-16).

### 4.4 Neuropilin Co-receptors

NRP1 and NRP2 are non-tyrosine kinase co-receptors that lack catalytic activity but enhance VEGF signaling through their extracellular domains (lee2025vascularendothelialgrowth pages 6-7, perezgutierrez2023biologyandtherapeutic pages 5-6). Both VEGFR1 and VEGFR2 form complexes with neuropilins, which facilitate VEGF-VEGFR interactions and enhance signaling potential (lee2025vascularendothelialgrowth pages 6-7). NRP1 is particularly important for VEGF-A165-mediated signaling in blood vascular endothelium, while NRP2 is classically associated with lymphatic VEGF signaling (perezgutierrez2023biologyandtherapeutic pages 5-6).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep Evolutionary Origins

VEGFs and PDGFs form a conserved subgroup within the cystine knot growth factor superfamily. The phylogenetically oldest PDGF/VEGF-like growth factor likely featured a C-terminus with a BR3P signature, a hallmark of modern lymphangiogenic growth factors VEGF-C and VEGF-D (rauniyar2023expansionandcollapse pages 1-3). The least complex animals with PDGF/VEGF-like molecules are Cnidaria (jellyfish and corals), whose VEGFs resemble modern VEGF-C more than VEGF-A, frequently lacking cysteine residues for intermolecular disulfide bonds found in mammalian versions (rauniyar2023expansionandcollapse pages 3-6).

VEGFRs belong to the "longDE" clade of receptor tyrosine kinases, characterized by a fast-evolving insertion in the kinase domain D–E helix loop that facilitates downstream intracellular signaling upon extracellular ligand activation (yeung2021evolutionoffunctional pages 7-9). Within the tyrosine kinome classification, VEGFRs belong to the FPVR (Fibroblast, Platelet-derived, Vascular, and growth factor Receptors) subgroup along with PDGFRs and FGFRs, sharing conserved autoinhibitory interactions (yeung2021evolutionoffunctional pages 9-10). The FPVR subgroup, whose constituent receptor tyrosine kinase families split before the chordates/tunicates divergence into class III and class V RTKs, has been heavily influenced by both whole-genome and small-scale duplication events (yeung2021evolutionoffunctional pages 9-10).

### 5.2 Vertebrate Diversification

Vertebrate whole-genome duplications played a major role in expanding PDGF/VEGF diversity, but several limited duplications are also necessary to account for the temporal pattern of emergence (rauniyar2023expansionandcollapse pages 1-3). The emergence of VEGF-A-like proteins is observed in Echinodermata, Cephalochordata, and most Tunicata (rauniyar2023expansionandcollapse pages 3-6). PDGFs likely appeared first in the chordate lineage after divergence from echinoderms (rauniyar2023expansionandcollapse pages 3-6). Some younger VEGF genes show lineage-specific losses: VEGF-B appears completely absent in birds, and PlGF is absent in amphibia (rauniyar2023expansionandcollapse pages 1-3). In contrast, fish show extensive PDGF/VEGF gene duplications beyond the known teleost-specific whole-genome duplication, with VEGF-C duplications particularly prominent in Holostei fishes (rauniyar2023expansionandcollapse pages 8-11).

### 5.3 Model Organism Variation

In zebrafish, FLT1 functions similarly to the mammalian decoy receptor. Zebrafish flt1 mutants display enhanced coronary revascularization and endocardial expansion following cardiac injury, with enhanced endothelial MAPK/ERK signaling—demonstrating conserved VEGFR1 decoy function across vertebrates (wang2024flt1inactivationpromotes pages 1-5). In *Drosophila*, a single PDGF/VEGF receptor-related gene (Pvr) functions with multiple PVF ligands, representing the ancestral state before the VEGFR/PDGFR split.

### 5.4 Non-Endothelial VEGFR Signaling

Emerging evidence reveals that VEGFR signaling operates beyond the vascular endothelium. In hypothalamic tanycytes, VEGFR1 and VEGFR2 show striking spatial compartmentalization: VEGFR2 is enriched in arcuate nucleus tanycytes while VEGFR1 is confined to ventromedial/dorsomedial tanycytes, with neither expressed in median eminence tanycytes—despite these cells producing abundant VEGF-A (desruelle2026compartmentalizedvegfreceptor pages 2-5). This compartmentalized non-endothelial VEGF signaling axis is developmentally programmed and age-dependent. Autocrine VEGF-A signaling also occurs in tumor cells, where intracrine signaling mediates cancer cell migration and invasion through NRP1-dependent mechanisms (patel2023molecularmechanismsand pages 4-6).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Sequential Dependencies

The signaling cascade follows a strict hierarchy: (i) ligand binding must precede receptor dimerization; (ii) dimerization is prerequisite for trans-autophosphorylation; (iii) activation loop phosphorylation (Y1054/Y1059) is required for maximal kinase activity before productive phosphorylation of downstream docking sites (shaik2020structuralbasisfor pages 10-12). The Y1175–PLCγ1 interaction is obligatory for the mitogenic response—this single phosphosite controls the branch point between proliferative ERK signaling and permeability-regulating eNOS/Src signaling (perezgutierrez2023biologyandtherapeutic pages 6-7, sjoberg2023endothelialvegfr2plcγsignaling pages 1-2).

### 6.2 Cell-Type and Context Specificity

VEGFR1-VEGFR2 heterodimers are more prevalent in neuronal cells, while VEGFR2 homodimers dominate in endothelial cells, suggesting differential signaling complex assembly across cell types (lee2025vascularendothelialgrowth pages 6-7). In angiogenic sprouting, tip cells express high VEGFR2 and VEGFR3 but low VEGFR1, while stalk cells show the inverse pattern—a distribution enforced by Notch-mediated lateral inhibition (lee2025vascularendothelialgrowth pages 14-15). VEGFR1 signaling through paracrine release of tissue-specific growth factors may operate in a vascular bed-specific manner (perezgutierrez2023biologyandtherapeutic pages 7-8).

### 6.3 Negative Regulation and Failure Modes

VE-PTP (vascular endothelial protein tyrosine phosphatase) negatively controls VEGFR2 phosphorylation at endothelial junctions to prevent excessive signaling (lee2025vascularendothelialgrowth pages 11-12). Excessive VEGF-A can paradoxically impair regeneration—constitutive overexpression of VEGF-A in zebrafish stimulates cardiomyocyte cell cycle re-entry while blocking cardiac regeneration, highlighting the importance of dosage control (wang2024flt1inactivationpromotes pages 1-5). Loss of VEGFR2 causes early embryonic lethality with complete failure of vasculogenesis, while VEGFR1 deletion causes death from vascular overgrowth—demonstrating that the system requires balanced positive (VEGFR2) and negative (VEGFR1) regulation (perezgutierrez2023biologyandtherapeutic pages 6-7, shaik2020structuralbasisfor pages 4-6).

## 7. Controversies and Open Questions

### 7.1 VEGFR1: Pure Decoy or Context-Dependent Signaler?

Although VEGFR1 kinase-dead mice develop normally, suggesting a predominantly decoy function, there is growing evidence for VEGFR1 signaling in specific contexts, particularly in macrophages, some tumor cells, and during tissue protection (perezgutierrez2023biologyandtherapeutic pages 5-6, lee2025vascularendothelialgrowth pages 3-4). The balance between full-length FLT1 and sFLT1 isoforms has been shown to differentially control developmental versus ischemia-driven angiogenesis, adding complexity to the simple decoy model (bundalo2024redirectingfulllengthflt1 pages 1-5).

### 7.2 Intracellular Trafficking and Endosomal Signaling

VEGFR2 continues to signal from endosomal compartments after internalization, and most ligand-receptor complexes for both VEGFR1 and VEGFR2 are intracellular rather than surface-located (sarabipour2025impactofligand pages 1-4, perezgutierrez2023biologyandtherapeutic pages 7-8). The differential trafficking of VEGFR1 (fast internalization/recycling, very low surface fraction) versus VEGFR2 (ligand-dependent increased internalization) creates a "reservoir effect" where intracellular receptor-receptor competition may substantially influence signaling outcomes (sarabipour2025impactofligand pages 1-4, sarabipour2024traffickingdynamicsof pages 1-2). How surface versus endosomal signaling complexes specify qualitatively different outputs remains incompletely understood.

### 7.3 Intracrine and Autocrine VEGF Signaling

Evidence supports cell-autonomous VEGF signaling modes in both endothelial and tumor cells (patel2023molecularmechanismsand pages 4-6). The molecular mechanisms by which intracellularly produced VEGF-A engages VEGFRs without secretion remain poorly defined, and the physiological significance of intracrine signaling versus classical paracrine VEGF signaling continues to be debated.

### 7.4 Non-Endothelial VEGFR Functions

The discovery of spatially compartmentalized VEGFR expression in hypothalamic tanycytes and other non-endothelial cells raises important questions about central nervous system effects of systemic anti-VEGF therapies (desruelle2026compartmentalizedvegfreceptor pages 2-5). The extent to which VEGFR signaling mechanisms characterized in endothelial cells apply to neurons, glia, and other non-vascular cell types is an active area of investigation.

### 7.5 Cross-Species Extrapolation

Much mechanistic understanding derives from mouse genetics and human endothelial cell culture, but the VEGF/VEGFR system varies considerably across vertebrate lineages—with lineage-specific gene losses (VEGF-B absent in birds, PlGF absent in amphibia) and duplications (extensive in fish) (rauniyar2023expansionandcollapse pages 1-3). Caution is warranted when extrapolating findings across species, particularly regarding the balance between VEGFR1 decoy function and VEGFR2 signaling.

## 8. Key References

The following sources provide the primary basis for this review:

- Pérez-Gutiérrez L, Ferrara N. Biology and therapeutic targeting of vascular endothelial growth factor A. *Nature Reviews Molecular Cell Biology* 24:816–834, 2023. DOI: 10.1038/s41580-023-00631-w (perezgutierrez2023biologyandtherapeutic pages 5-6, perezgutierrez2023biologyandtherapeutic pages 3-5, perezgutierrez2023biologyandtherapeutic pages 6-7, perezgutierrez2023biologyandtherapeutic pages 7-8)
- Lee C, et al. Vascular endothelial growth factor signaling in health and disease. *Signal Transduction and Targeted Therapy*, 2025. DOI: 10.1038/s41392-025-02249-0 (lee2025vascularendothelialgrowth pages 3-4, lee2025vascularendothelialgrowth pages 6-7, lee2025vascularendothelialgrowth pages 11-12, lee2025vascularendothelialgrowth pages 14-15, lee2025vascularendothelialgrowth pages 15-16)
- Shah FH, et al. Targeting VEGFR-2: structural biology, functional insights, and therapeutic resistance. *Archives of Pharmacal Research* 48:404–425, 2025. DOI: 10.1007/s12272-025-01545-1 (shah2025targetingvascularendothelial pages 4-6, shah2025targetingvascularendothelial pages 6-8)
- Sjöberg E, et al. Endothelial VEGFR2-PLCγ signaling regulates vascular permeability and antitumor immunity through eNOS/Src. *Journal of Clinical Investigation* 133, 2023. DOI: 10.1172/JCI161366 (sjoberg2023endothelialvegfr2plcγsignaling pages 1-2, sjoberg2023endothelialvegfr2plcγsignaling pages 2-4)
- Patel SA, et al. Molecular mechanisms and future implications of VEGF/VEGFR in cancer therapy. *Clinical Cancer Research* 29:30–39, 2023. DOI: 10.1158/1078-0432.CCR-22-1366 (patel2023molecularmechanismsand pages 2-4, patel2023molecularmechanismsand pages 4-6)
- Shaik F, et al. Structural basis for VEGFR activation and implications for disease therapy. *Biomolecules* 10:1673, 2020. DOI: 10.3390/biom10121673 (shaik2020structuralbasisfor pages 1-4, shaik2020structuralbasisfor pages 6-7, shaik2020structuralbasisfor pages 4-6, shaik2020structuralbasisfor pages 10-12, shaik2020structuralbasisfor pages 18-20)
- Sarabipour S, et al. Impact of ligand binding on VEGFR1, VEGFR2, and NRP1 localization. *PLOS Computational Biology* 21, 2025. DOI: 10.1101/2024.09.29.615728 (sarabipour2025impactofligand pages 1-4)
- Sarabipour S, et al. Trafficking dynamics of VEGFR1, VEGFR2, and NRP1 in human endothelial cells. *PLOS Computational Biology* 20, 2024. DOI: 10.1101/2022.09.30.510412 (sarabipour2024traffickingdynamicsof pages 1-2)
- Rauniyar K, et al. Expansion and collapse of VEGF diversity in major clades of the animal kingdom. *Angiogenesis* 26:437–461, 2023. DOI: 10.1007/s10456-023-09874-9 (rauniyar2023expansionandcollapse pages 3-6, rauniyar2023expansionandcollapse pages 1-3, rauniyar2023expansionandcollapse pages 8-11)
- Yeung W, et al. Evolution of functional diversity in the holozoan tyrosine kinome. *Molecular Biology and Evolution* 38:5625–5639, 2021. DOI: 10.1093/molbev/msab272 (yeung2021evolutionoffunctional pages 9-10, yeung2021evolutionoffunctional pages 7-9)
- Bundalo M, et al. Redirecting full-length FLT1 expression towards its soluble isoform promotes postischemic angiogenesis. *bioRxiv*, 2024. DOI: 10.1101/2024.09.19.613989 (bundalo2024redirectingfulllengthflt1 pages 1-5)
- Wang ZY, et al. flt1 inactivation promotes zebrafish cardiac regeneration. *Development*, 2024. DOI: 10.1101/2024.09.11.612516 (wang2024flt1inactivationpromotes pages 1-5)
- Nan W, et al. Molecular mechanism of VE-cadherin in regulating endothelial cell behaviour during angiogenesis. *Frontiers in Physiology*, 2023. DOI: 10.3389/fphys.2023.1234104 (nan2023molecularmechanismof pages 2-4, nan2023molecularmechanismof pages 4-6, nan2023molecularmechanismof pages 7-8)
- Li H, Huang X. Advances in the molecular signaling mechanisms of VEGF/VEGFR2 in fundus neovascularization disease. *Experimental and Therapeutic Medicine* 30:1–13, 2025. DOI: 10.3892/etm.2025.12893 (li2025advancesinthe pages 4-5)
- Brogowska KK, et al. Vascular endothelial growth factor ligands and receptors in breast cancer. *Journal of Clinical Medicine* 12:2412, 2023. DOI: 10.3390/jcm12062412 (brogowska2023vascularendothelialgrowth pages 9-11)
- Desruelle O, et al. Compartmentalized VEGF receptor expression in hypothalamic tanycytes. *Fluids and Barriers of the CNS* 23:45, 2026. DOI: 10.1186/s12987-026-00774-w (desruelle2026compartmentalizedvegfreceptor pages 2-5)


References

1. (perezgutierrez2023biologyandtherapeutic pages 5-6): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 496 citations and is from a domain leading peer-reviewed journal.

2. (lee2025vascularendothelialgrowth pages 3-4): Chunsik Lee, Myung-Jin Kim, Anil Kumar, Han-Woong Lee, Yunlong Yang, and Yonghwan Kim. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy, May 2025. URL: https://doi.org/10.1038/s41392-025-02249-0, doi:10.1038/s41392-025-02249-0. This article has 340 citations and is from a peer-reviewed journal.

3. (shah2025targetingvascularendothelial pages 4-6): Fahad Hassan Shah, Yoon Seok Nam, Jun Young Bang, In Seo Hwang, Dae Hong Kim, Minkyoung Ki, and Heon-Woo Lee. Targeting vascular endothelial growth receptor-2 (vegfr-2): structural biology, functional insights, and therapeutic resistance. Archives of Pharmacal Research, 48:404-425, May 2025. URL: https://doi.org/10.1007/s12272-025-01545-1, doi:10.1007/s12272-025-01545-1. This article has 91 citations and is from a peer-reviewed journal.

4. (perezgutierrez2023biologyandtherapeutic pages 6-7): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 496 citations and is from a domain leading peer-reviewed journal.

5. (shaik2020structuralbasisfor pages 4-6): Faheem Shaik, Gary Cuthbert, Shervanthi Homer-Vanniasinkam, Stephen Muench, Sreenivasan Ponnambalam, and Michael Harrison. Structural basis for vascular endothelial growth factor receptor activation and implications for disease therapy. Biomolecules, 10:1673, Dec 2020. URL: https://doi.org/10.3390/biom10121673, doi:10.3390/biom10121673. This article has 127 citations.

6. (perezgutierrez2023biologyandtherapeutic pages 7-8): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 496 citations and is from a domain leading peer-reviewed journal.

7. (rauniyar2023expansionandcollapse pages 3-6): Khushbu Rauniyar, Honey Bokharaie, and Michael Jeltsch. Expansion and collapse of vegf diversity in major clades of the animal kingdom. Angiogenesis, 26:437-461, Apr 2023. URL: https://doi.org/10.1007/s10456-023-09874-9, doi:10.1007/s10456-023-09874-9. This article has 21 citations and is from a domain leading peer-reviewed journal.

8. (rauniyar2023expansionandcollapse pages 1-3): Khushbu Rauniyar, Honey Bokharaie, and Michael Jeltsch. Expansion and collapse of vegf diversity in major clades of the animal kingdom. Angiogenesis, 26:437-461, Apr 2023. URL: https://doi.org/10.1007/s10456-023-09874-9, doi:10.1007/s10456-023-09874-9. This article has 21 citations and is from a domain leading peer-reviewed journal.

9. (perezgutierrez2023biologyandtherapeutic pages 3-5): Lorena Pérez-Gutiérrez and Napoleone Ferrara. Biology and therapeutic targeting of vascular endothelial growth factor a. Nature Reviews Molecular Cell Biology, 24:816-834, Jul 2023. URL: https://doi.org/10.1038/s41580-023-00631-w, doi:10.1038/s41580-023-00631-w. This article has 496 citations and is from a domain leading peer-reviewed journal.

10. (rauniyar2023expansionandcollapse pages 8-11): Khushbu Rauniyar, Honey Bokharaie, and Michael Jeltsch. Expansion and collapse of vegf diversity in major clades of the animal kingdom. Angiogenesis, 26:437-461, Apr 2023. URL: https://doi.org/10.1007/s10456-023-09874-9, doi:10.1007/s10456-023-09874-9. This article has 21 citations and is from a domain leading peer-reviewed journal.

11. (shaik2020structuralbasisfor pages 1-4): Faheem Shaik, Gary Cuthbert, Shervanthi Homer-Vanniasinkam, Stephen Muench, Sreenivasan Ponnambalam, and Michael Harrison. Structural basis for vascular endothelial growth factor receptor activation and implications for disease therapy. Biomolecules, 10:1673, Dec 2020. URL: https://doi.org/10.3390/biom10121673, doi:10.3390/biom10121673. This article has 127 citations.

12. (brogowska2023vascularendothelialgrowth pages 9-11): Klaudia Katarzyna Brogowska, Monika Zajkowska, and Barbara Mroczko. Vascular endothelial growth factor ligands and receptors in breast cancer. Journal of Clinical Medicine, 12:2412, Mar 2023. URL: https://doi.org/10.3390/jcm12062412, doi:10.3390/jcm12062412. This article has 71 citations.

13. (patel2023molecularmechanismsand pages 2-4): Sonia A. Patel, Monique B. Nilsson, Xiuning Le, Tina Cascone, Rakesh K. Jain, and John V. Heymach. Molecular mechanisms and future implications of vegf/vegfr in cancer therapy. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:30-39, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-1366, doi:10.1158/1078-0432.ccr-22-1366. This article has 522 citations.

14. (lee2025vascularendothelialgrowth pages 6-7): Chunsik Lee, Myung-Jin Kim, Anil Kumar, Han-Woong Lee, Yunlong Yang, and Yonghwan Kim. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy, May 2025. URL: https://doi.org/10.1038/s41392-025-02249-0, doi:10.1038/s41392-025-02249-0. This article has 340 citations and is from a peer-reviewed journal.

15. (lee2025vascularendothelialgrowth pages 15-16): Chunsik Lee, Myung-Jin Kim, Anil Kumar, Han-Woong Lee, Yunlong Yang, and Yonghwan Kim. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy, May 2025. URL: https://doi.org/10.1038/s41392-025-02249-0, doi:10.1038/s41392-025-02249-0. This article has 340 citations and is from a peer-reviewed journal.

16. (sarabipour2025impactofligand pages 1-4): Sarvenaz Sarabipour, Karina Kinghorn, Kaitlyn M Quigley, Anita Kovacs-Kasa, Brian H Annex, Victoria L Bautch, and Feilim Mac Gabhann. Impact of ligand binding on vegfr1, vegfr2, and nrp1 localization in human endothelial cells. PLOS Computational Biology, Oct 2025. URL: https://doi.org/10.1101/2024.09.29.615728, doi:10.1101/2024.09.29.615728. This article has 2 citations and is from a highest quality peer-reviewed journal.

17. (shaik2020structuralbasisfor pages 6-7): Faheem Shaik, Gary Cuthbert, Shervanthi Homer-Vanniasinkam, Stephen Muench, Sreenivasan Ponnambalam, and Michael Harrison. Structural basis for vascular endothelial growth factor receptor activation and implications for disease therapy. Biomolecules, 10:1673, Dec 2020. URL: https://doi.org/10.3390/biom10121673, doi:10.3390/biom10121673. This article has 127 citations.

18. (sarabipour2024traffickingdynamicsof pages 1-2): Sarvenaz Sarabipour, Karina Kinghorn, Kaitlyn M Quigley, Anita Kovacs-Kasa, Brian H Annex, Victoria L Bautch, and Feilim Mac Gabhann. Trafficking dynamics of vegfr1, vegfr2, and nrp1 in human endothelial cells. PLOS Computational Biology, Oct 2024. URL: https://doi.org/10.1101/2022.09.30.510412, doi:10.1101/2022.09.30.510412. This article has 20 citations and is from a highest quality peer-reviewed journal.

19. (lee2025vascularendothelialgrowth pages 14-15): Chunsik Lee, Myung-Jin Kim, Anil Kumar, Han-Woong Lee, Yunlong Yang, and Yonghwan Kim. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy, May 2025. URL: https://doi.org/10.1038/s41392-025-02249-0, doi:10.1038/s41392-025-02249-0. This article has 340 citations and is from a peer-reviewed journal.

20. (bundalo2024redirectingfulllengthflt1 pages 1-5): Maja Bundalo, Sandra Vorlova, Jessica Ulrich, Ruggero Barbieri, Leon Richter, Leonie Höna, Manuel Egg, Julian Bock, Sarah Schäfer, Núria Amézaga Solé, Annabelle Rosa, Giuseppe Rizzo, Clemént Cochain, Wolfgang Kastenmüller, Erik Henke, Boris V. Skryabin, Timofey S. Rozhdestvensky, Moritz Wildgruber, Kristina Lorenz, Michaela Kuhn, and Alma Zernecke. Redirecting full-length flt1 expression towards its soluble isoform promotes postischemic angiogenesis. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.19.613989, doi:10.1101/2024.09.19.613989. This article has 0 citations.

21. (nan2023molecularmechanismof pages 2-4): Weijin Nan, Yuxi He, Shurong Wang, and Yan Zhang. Molecular mechanism of ve-cadherin in regulating endothelial cell behaviour during angiogenesis. Frontiers in Physiology, Aug 2023. URL: https://doi.org/10.3389/fphys.2023.1234104, doi:10.3389/fphys.2023.1234104. This article has 82 citations.

22. (wang2024flt1inactivationpromotes pages 1-5): Zhenyu Wang, Armaan Mehra, Quian-Chen Wang, Savita Gupta, Agatha Ribeiro da Silva, Thomas Juan, Stephan Gunther, Jan Detleffsen, Mario Looso, Didier Y.R. Stainier, and Ruben Marin-Juez. Flt1 inactivation promotes zebrafish cardiac regeneration by enhancing endothelial activity and limiting the fibrotic response. Development (Cambridge, England), Sep 2024. URL: https://doi.org/10.1101/2024.09.11.612516, doi:10.1101/2024.09.11.612516. This article has 11 citations.

23. (shaik2020structuralbasisfor pages 10-12): Faheem Shaik, Gary Cuthbert, Shervanthi Homer-Vanniasinkam, Stephen Muench, Sreenivasan Ponnambalam, and Michael Harrison. Structural basis for vascular endothelial growth factor receptor activation and implications for disease therapy. Biomolecules, 10:1673, Dec 2020. URL: https://doi.org/10.3390/biom10121673, doi:10.3390/biom10121673. This article has 127 citations.

24. (sjoberg2023endothelialvegfr2plcγsignaling pages 1-2): Elin Sjöberg, Marit Melssen, Mark Richards, Yindi Ding, Catarina Chanoca, Dongying Chen, Emmanuel Nwadozi, Sagnik Pal, Dominic T. Love, Takeshi Ninchoji, Masabumi Shibuya, Michael Simons, Anna Dimberg, and Lena Claesson-Welsh. Endothelial vegfr2-plcγ signaling regulates vascular permeability and antitumor immunity through enos/src. Journal of Clinical Investigation, Oct 2023. URL: https://doi.org/10.1172/jci161366, doi:10.1172/jci161366. This article has 55 citations and is from a highest quality peer-reviewed journal.

25. (sjoberg2023endothelialvegfr2plcγsignaling pages 2-4): Elin Sjöberg, Marit Melssen, Mark Richards, Yindi Ding, Catarina Chanoca, Dongying Chen, Emmanuel Nwadozi, Sagnik Pal, Dominic T. Love, Takeshi Ninchoji, Masabumi Shibuya, Michael Simons, Anna Dimberg, and Lena Claesson-Welsh. Endothelial vegfr2-plcγ signaling regulates vascular permeability and antitumor immunity through enos/src. Journal of Clinical Investigation, Oct 2023. URL: https://doi.org/10.1172/jci161366, doi:10.1172/jci161366. This article has 55 citations and is from a highest quality peer-reviewed journal.

26. (shah2025targetingvascularendothelial pages 6-8): Fahad Hassan Shah, Yoon Seok Nam, Jun Young Bang, In Seo Hwang, Dae Hong Kim, Minkyoung Ki, and Heon-Woo Lee. Targeting vascular endothelial growth receptor-2 (vegfr-2): structural biology, functional insights, and therapeutic resistance. Archives of Pharmacal Research, 48:404-425, May 2025. URL: https://doi.org/10.1007/s12272-025-01545-1, doi:10.1007/s12272-025-01545-1. This article has 91 citations and is from a peer-reviewed journal.

27. (li2025advancesinthe pages 4-5): Huan Li and Xiong Huang. Advances in the molecular signaling mechanisms of vegf/vegfr2 in fundus neovascularization disease (review). Experimental and Therapeutic Medicine, 30:1-13, May 2025. URL: https://doi.org/10.3892/etm.2025.12893, doi:10.3892/etm.2025.12893. This article has 11 citations and is from a peer-reviewed journal.

28. (lee2025vascularendothelialgrowth pages 11-12): Chunsik Lee, Myung-Jin Kim, Anil Kumar, Han-Woong Lee, Yunlong Yang, and Yonghwan Kim. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy, May 2025. URL: https://doi.org/10.1038/s41392-025-02249-0, doi:10.1038/s41392-025-02249-0. This article has 340 citations and is from a peer-reviewed journal.

29. (nan2023molecularmechanismof pages 4-6): Weijin Nan, Yuxi He, Shurong Wang, and Yan Zhang. Molecular mechanism of ve-cadherin in regulating endothelial cell behaviour during angiogenesis. Frontiers in Physiology, Aug 2023. URL: https://doi.org/10.3389/fphys.2023.1234104, doi:10.3389/fphys.2023.1234104. This article has 82 citations.

30. (nan2023molecularmechanismof pages 7-8): Weijin Nan, Yuxi He, Shurong Wang, and Yan Zhang. Molecular mechanism of ve-cadherin in regulating endothelial cell behaviour during angiogenesis. Frontiers in Physiology, Aug 2023. URL: https://doi.org/10.3389/fphys.2023.1234104, doi:10.3389/fphys.2023.1234104. This article has 82 citations.

31. (yeung2021evolutionoffunctional pages 7-9): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

32. (yeung2021evolutionoffunctional pages 9-10): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

33. (desruelle2026compartmentalizedvegfreceptor pages 2-5): Ombeline Desruelle, Manon Leclerc, Sreekala Nampoothiri, Daniela Fernandois, Claude-Alain Maurage, Markus Schwaninger, Vincent Prevot, and Ines Martinez-Corral. Compartmentalized vegf receptor expression in hypothalamic tanycytes reveals a novel non-endothelial axis of vegf signaling. Fluids and Barriers of the CNS, Feb 2026. URL: https://doi.org/10.1186/s12987-026-00774-w, doi:10.1186/s12987-026-00774-w. This article has 0 citations and is from a peer-reviewed journal.

34. (patel2023molecularmechanismsand pages 4-6): Sonia A. Patel, Monique B. Nilsson, Xiuning Le, Tina Cascone, Rakesh K. Jain, and John V. Heymach. Molecular mechanisms and future implications of vegf/vegfr in cancer therapy. Clinical cancer research : an official journal of the American Association for Cancer Research, 29:30-39, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-1366, doi:10.1158/1078-0432.ccr-22-1366. This article has 522 citations.

35. (shaik2020structuralbasisfor pages 18-20): Faheem Shaik, Gary Cuthbert, Shervanthi Homer-Vanniasinkam, Stephen Muench, Sreenivasan Ponnambalam, and Michael Harrison. Structural basis for vascular endothelial growth factor receptor activation and implications for disease therapy. Biomolecules, 10:1673, Dec 2020. URL: https://doi.org/10.3390/biom10121673, doi:10.3390/biom10121673. This article has 127 citations.

## Artifacts

- [Edison artifact artifact-00](vegfr_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](vegfr_signaling-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](vegfr_signaling-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. lee2025vascularendothelialgrowth pages 3-4
2. shaik2020structuralbasisfor pages 4-6
3. rauniyar2023expansionandcollapse pages 1-3
4. shaik2020structuralbasisfor pages 6-7
5. perezgutierrez2023biologyandtherapeutic pages 6-7
6. lee2025vascularendothelialgrowth pages 15-16
7. shah2025targetingvascularendothelial pages 4-6
8. shaik2020structuralbasisfor pages 10-12
9. sarabipour2024traffickingdynamicsof pages 1-2
10. sarabipour2025impactofligand pages 1-4
11. perezgutierrez2023biologyandtherapeutic pages 7-8
12. nan2023molecularmechanismof pages 7-8
13. lee2025vascularendothelialgrowth pages 14-15
14. lee2025vascularendothelialgrowth pages 6-7
15. perezgutierrez2023biologyandtherapeutic pages 5-6
16. rauniyar2023expansionandcollapse pages 3-6
17. yeung2021evolutionoffunctional pages 7-9
18. yeung2021evolutionoffunctional pages 9-10
19. rauniyar2023expansionandcollapse pages 8-11
20. desruelle2026compartmentalizedvegfreceptor pages 2-5
21. patel2023molecularmechanismsand pages 4-6
22. lee2025vascularendothelialgrowth pages 11-12
23. li2025advancesinthe pages 4-5
24. brogowska2023vascularendothelialgrowth pages 9-11
25. perezgutierrez2023biologyandtherapeutic pages 3-5
26. shaik2020structuralbasisfor pages 1-4
27. patel2023molecularmechanismsand pages 2-4
28. nan2023molecularmechanismof pages 2-4
29. shah2025targetingvascularendothelial pages 6-8
30. nan2023molecularmechanismof pages 4-6
31. shaik2020structuralbasisfor pages 18-20
32. https://doi.org/10.1038/s41580-023-00631-w,
33. https://doi.org/10.1038/s41392-025-02249-0,
34. https://doi.org/10.1007/s12272-025-01545-1,
35. https://doi.org/10.3390/biom10121673,
36. https://doi.org/10.1007/s10456-023-09874-9,
37. https://doi.org/10.3390/jcm12062412,
38. https://doi.org/10.1158/1078-0432.ccr-22-1366,
39. https://doi.org/10.1101/2024.09.29.615728,
40. https://doi.org/10.1101/2022.09.30.510412,
41. https://doi.org/10.1101/2024.09.19.613989,
42. https://doi.org/10.3389/fphys.2023.1234104,
43. https://doi.org/10.1101/2024.09.11.612516,
44. https://doi.org/10.1172/jci161366,
45. https://doi.org/10.3892/etm.2025.12893,
46. https://doi.org/10.1093/molbev/msab272,
47. https://doi.org/10.1186/s12987-026-00774-w,