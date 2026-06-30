---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T16:43:21.867689'
end_time: '2026-06-28T17:05:10.271512'
duration_seconds: 1308.4
template_file: templates/module_research.md.j2
template_variables:
  module_title: FGFR signaling pathway module
  module_summary: FGF ligands and heparan sulfate cofactor activate FGFR receptor
    tyrosine kinases, recruiting FRS2/GRB2/SOS, PI3K, PLCG, and MAPK outputs for development,
    angiogenesis, and tissue repair.
  module_outline: "- FGFR signaling pathway\n  - 1. fgf ligand binds fgfr\n  - FGF\
    \ ligand binds FGFR\n    - FGF2 ligand (molecular player: FGF2; activity or role:\
    \ signaling receptor binding)\n    - FGFR1 receptor kinase (molecular player:\
    \ FGFR1 receptor kinase family/ortholog group; activity or role: transmembrane\
    \ receptor protein tyrosine kinase activity)\n  - 2. frs2/grb2 scaffold assembly\n\
    \  - FRS2/GRB2 scaffold assembly\n    - FRS2 adaptor (molecular player: FRS2)\n\
    \    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)\n \
    \ - 3. mapk and pi3k output\n  - MAPK and PI3K output\n    - SOS1 Ras GEF (molecular\
    \ player: SOS1; activity or role: guanyl-nucleotide exchange factor activity)\n\
    \    - PIK3R1 p85 adaptor (molecular player: PIK3R1 p85 adaptor family/ortholog\
    \ group)"
  module_connections: '- FGF ligand binds FGFR causes FRS2/GRB2 scaffold assembly:
    The initiating event promotes frs2/grb2 scaffold assembly.

    - FRS2/GRB2 scaffold assembly causes MAPK and PI3K output: FRS2/GRB2 scaffold
    assembly leads to mapk and pi3k output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 50
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 3
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: fgfr_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: fgfr_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: fgfr_signaling-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: image-1.png
  path: fgfr_signaling-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: 'Image artifact created (ID artifact-02): ''FGFR Signaling Pathway
    Module'' ![FGFR Signaling Pathway Module](artifact:artifact-02) Artifact IDs that
    may be injecte'
---

## Question

# Commissioned Review Brief

## Review Topic

FGFR signaling pathway module

## Working Scope

FGF ligands and heparan sulfate cofactor activate FGFR receptor tyrosine kinases, recruiting FRS2/GRB2/SOS, PI3K, PLCG, and MAPK outputs for development, angiogenesis, and tissue repair.

## Provisional Biological Outline

- FGFR signaling pathway
  - 1. fgf ligand binds fgfr
  - FGF ligand binds FGFR
    - FGF2 ligand (molecular player: FGF2; activity or role: signaling receptor binding)
    - FGFR1 receptor kinase (molecular player: FGFR1 receptor kinase family/ortholog group; activity or role: transmembrane receptor protein tyrosine kinase activity)
  - 2. frs2/grb2 scaffold assembly
  - FRS2/GRB2 scaffold assembly
    - FRS2 adaptor (molecular player: FRS2)
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
  - 3. mapk and pi3k output
  - MAPK and PI3K output
    - SOS1 Ras GEF (molecular player: SOS1; activity or role: guanyl-nucleotide exchange factor activity)
    - PIK3R1 p85 adaptor (molecular player: PIK3R1 p85 adaptor family/ortholog group)

## Known Relationships Among Steps

- FGF ligand binds FGFR causes FRS2/GRB2 scaffold assembly: The initiating event promotes frs2/grb2 scaffold assembly.
- FRS2/GRB2 scaffold assembly causes MAPK and PI3K output: FRS2/GRB2 scaffold assembly leads to mapk and pi3k output.

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

FGFR signaling pathway module

## Working Scope

FGF ligands and heparan sulfate cofactor activate FGFR receptor tyrosine kinases, recruiting FRS2/GRB2/SOS, PI3K, PLCG, and MAPK outputs for development, angiogenesis, and tissue repair.

## Provisional Biological Outline

- FGFR signaling pathway
  - 1. fgf ligand binds fgfr
  - FGF ligand binds FGFR
    - FGF2 ligand (molecular player: FGF2; activity or role: signaling receptor binding)
    - FGFR1 receptor kinase (molecular player: FGFR1 receptor kinase family/ortholog group; activity or role: transmembrane receptor protein tyrosine kinase activity)
  - 2. frs2/grb2 scaffold assembly
  - FRS2/GRB2 scaffold assembly
    - FRS2 adaptor (molecular player: FRS2)
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
  - 3. mapk and pi3k output
  - MAPK and PI3K output
    - SOS1 Ras GEF (molecular player: SOS1; activity or role: guanyl-nucleotide exchange factor activity)
    - PIK3R1 p85 adaptor (molecular player: PIK3R1 p85 adaptor family/ortholog group)

## Known Relationships Among Steps

- FGF ligand binds FGFR causes FRS2/GRB2 scaffold assembly: The initiating event promotes frs2/grb2 scaffold assembly.
- FRS2/GRB2 scaffold assembly causes MAPK and PI3K output: FRS2/GRB2 scaffold assembly leads to mapk and pi3k output.

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

# The FGFR Signaling Pathway Module: A Review of Core Mechanisms, Variation, and Open Questions

## 1. Executive Summary

The fibroblast growth factor receptor (FGFR) signaling pathway is a conserved receptor tyrosine kinase (RTK) system in which secreted FGF ligands, in cooperation with heparan sulfate (HS) proteoglycan cofactors, activate one of four transmembrane FGFRs (FGFR1–4) to drive cell proliferation, differentiation, survival, migration, angiogenesis, and tissue repair (edirisinghe2024decodingfgffgfrsignaling pages 1-3, xie2020fgffgfrsignalingin pages 1-2). The intracellular signal is relayed through a mandatory FRS2α scaffold that recruits the GRB2–SOS1 complex to activate the RAS–RAF–MEK–ERK (MAPK) cascade, the GRB2–GAB1 axis to engage PI3K–AKT, and a parallel branch in which PLCγ binds directly to phosphorylated FGFR to hydrolyze PIP₂ into DAG and IP₃ (ferguson2021fibroblastgrowthfactor pages 3-5, liu2026fgffamilyin pages 3-4, tome2023fibroblastgrowthfactor pages 2-4). An elaborate set of negative regulators—including Sprouty (SPRY) proteins, SEF/IL17RD, DUSP6, CBL-mediated ubiquitination, and receptor endocytosis—shapes signal amplitude, duration, and spatial range (szybowska2021negativeregulationof pages 15-17, ferguson2021fibroblastgrowthfactor pages 5-7, ornitz2022newdevelopmentsin pages 18-20). Recent cryo-EM structural work has overturned the longstanding symmetric FGFR dimerization paradigm, establishing an asymmetric 1:2 FGF–FGFR model in which a single HS chain recruits a secondary receptor molecule (chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2). Dysregulation of this pathway by gene amplification, activating mutations, or fusions occurs in approximately 7% of human tumors and has led to the clinical development of selective FGFR inhibitors (OpenTargets Search: -FGFR1,FGFR2,FGFR3,FGFR4).

The following figure provides a schematic overview of the canonical FGFR signaling module:

![FGFR Signaling Pathway Module](artifact:artifact-02)

*Image: Schematic of canonical FGFR signaling showing FGF-HSPG-dependent asymmetric FGFR dimerization, FRS2α scaffold assembly, and three principal downstream branches to MAPK, PI3K-AKT-mTOR, and PLCγ-PKC-Ca2+ signaling, together with key negative regulators. The diagram should emphasize pathway topology, compartment organization, and labeled molecular interactions in a publication-ready scientific style.*

---

## 2. Definition and Biological Boundaries

### 2.1 What the system includes

The FGFR signaling pathway module, as defined for this review, encompasses: (i) the 18 secreted signaling FGF ligands (canonical paracrine FGFs and endocrine FGFs; excluding the four intracellular FGFs/iFGFs that regulate voltage-gated sodium channels rather than acting through FGFRs); (ii) the four receptor tyrosine kinases FGFR1–4; (iii) obligate cofactors, namely heparan sulfate proteoglycans (HSPGs) for canonical FGFs and α/βKlotho coreceptors for endocrine FGFs (FGF19, FGF21, FGF23); (iv) the proximal adaptor/scaffold complex centered on FRS2α, GRB2, and SOS1; and (v) the three principal downstream effector branches: RAS–MAPK, PI3K–AKT, and PLCγ–PKC/Ca²⁺ (liu2026fgffamilyin pages 3-4, edirisinghe2024decodingfgffgfrsignaling pages 1-3, zheng2022signalingpathwayand pages 2-5).

### 2.2 Neighboring systems that should be treated separately

Several related systems are frequently conflated with FGFR signaling but are mechanistically distinct. The RAS–MAPK cascade is shared with many other RTKs (EGFR, PDGFR, VEGFR, etc.) and should not be equated with FGFR-specific signaling; the distinctive feature of the FGFR module is its reliance on FRS2α as a constitutive, FGFR-selective scaffold, rather than pan-RTK adaptors such as SHC1 (ferguson2021fibroblastgrowthfactor pages 3-5). FGFRL1 (also called FGFR5) is sometimes listed alongside FGFR1–4, but it lacks a functional tyrosine kinase domain and instead acts as a decoy receptor that attenuates FGF signaling (liu2026fgffamilyin pages 4-6, ferguson2021fibroblastgrowthfactor pages 2-3). Intracellular FGFs (iFGFs: FGF11–14) do not signal through FGFRs and are functionally a separate system (edirisinghe2024decodingfgffgfrsignaling pages 1-3). The JAK–STAT branch, while reported downstream of FGFR in some tumor contexts, is less universally established as a core FGFR output and is best treated as context-dependent rather than constitutive (zheng2022signalingpathwayand pages 2-5).

---

## 3. Mechanistic Overview

### 3.1 Step 1: FGF ligand binding and cofactor-assisted receptor engagement

Canonical FGF signaling is initiated when a secreted FGF ligand binds the extracellular domain of an FGFR, an event that is obligatorily facilitated by HSPGs at the cell surface (sobhani2021targetingaberrantfgfr pages 2-3, edirisinghe2024decodingfgffgfrsignaling pages 1-3). HSPGs stabilize the FGF–FGFR interaction, protect ligands from degradation, constrain diffusion gradients, and are required for productive receptor dimerization (sobhani2021targetingaberrantfgfr pages 2-3, chen2023structuralbasisfor pages 2-3). For the endocrine FGF subfamily (FGF19/21/23), which have evolutionarily reduced HS-binding affinity to enable systemic circulation, α- or βKlotho coreceptors substitute as stabilizers of the primary FGF–FGFR complex, although HS remains required for receptor dimerization even in this context (ferguson2021fibroblastgrowthfactor pages 5-7, chen2023structuralbasisfor pages 1-2).

### 3.2 Step 2: Receptor dimerization and trans-autophosphorylation

FGF–HS binding triggers FGFR dimerization and conformational changes that lead to trans-autophosphorylation of seven key tyrosine residues within the intracellular kinase domain (liu2026fgffamilyin pages 3-4, margiotta2021allgoodthings pages 4-6). A landmark 2023 cryo-EM study by Chen et al. in *Nature* revealed that FGFR dimerization follows an asymmetric mechanism: a single HS chain enables FGF and its primary FGFR (FGFR_P) to jointly recruit a secondary lone FGFR chain (FGFR_S), yielding a 1:2:1:1 FGF–FGFR–Klotho–HS quaternary complex (chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2). This overturns the previous symmetric 2:2:2 paradigm and has important implications for drug design (chen2023structuralbasisfor pages 18-26). The asymmetric interface promotes formation of an intracellular kinase domain complex that mediates activation-loop tyrosine transphosphorylation (chen2023structuralbasisfor pages 1-2).

### 3.3 Step 3: FRS2α phosphorylation and scaffold assembly

FRS2α is a ~80 kDa lipid-anchored adaptor protein that constitutively binds to the FGFR juxtamembrane region through its phosphotyrosine-binding (PTB) domain; this constitutive association distinguishes FGFR signaling from many other RTK pathways (ferguson2021fibroblastgrowthfactor pages 3-5, klimaschewski2021fibroblastgrowthfactor pages 2-4). Upon receptor activation, FRS2α is phosphorylated at multiple tyrosine residues, creating docking sites for downstream adaptors: Y196, Y306, Y349, and Y392 recruit GRB2, while Y346 recruits the tyrosine phosphatase SHP2/PTPN11 (ferguson2021fibroblastgrowthfactor pages 3-5). Recent interactome studies using APEX2 proximity labeling have expanded the known FRS2 signalosome to over 100 interacting proteins, including regulators of actin cytoskeleton remodeling (WASF2/WAVE2), tight junction proteins (TJP1/TJP2), and translation initiation factors, suggesting that FRS2 integrates FGFR signaling well beyond the canonical MAPK and PI3K outputs (kopp2025proteomicanalysisreveals pages 21-23, kopp2025proteomicanalysisreveals pages 19-21, kopp2025proteomicanalysisreveals pages 16-19).

### 3.4 Step 4: MAPK output via GRB2–SOS1–RAS

The dominant downstream output of the FGFR–FRS2 signalosome is activation of the RAS–RAF–MEK–ERK cascade. Phospho-FRS2 recruits GRB2, which in turn binds SOS1, a guanine nucleotide exchange factor that activates RAS by promoting GDP–GTP exchange (tome2023fibroblastgrowthfactor pages 2-4, zheng2022signalingpathwayand pages 2-5). The activated RAS–MAPK pathway drives cell proliferation, differentiation, and many developmental responses downstream of FGFR (liu2026fgffamilyin pages 3-4, sobhani2021targetingaberrantfgfr pages 2-3).

### 3.5 Step 5: PI3K–AKT output via GRB2–GAB1

In parallel, GRB2 recruits the scaffolding adaptor GAB1, which in turn recruits the p85 regulatory subunit of PI3K (PIK3R1), activating the PI3K–AKT–mTOR cascade (tome2023fibroblastgrowthfactor pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 1-3, sobhani2021targetingaberrantfgfr pages 2-3). In some contexts, the p85 subunit can bind FGFR independently of FRS2, providing an alternative route to PI3K engagement (ferguson2021fibroblastgrowthfactor pages 5-7). The PI3K–AKT branch supports cell survival, anti-apoptotic signaling, metabolic regulation, and angiogenesis (sobhani2021targetingaberrantfgfr pages 2-3).

### 3.6 Step 6: PLCγ–PKC/Ca²⁺ output

PLCγ (primarily PLCγ1) is recruited directly to phosphorylated FGFR—notably at Y766—independently of the FRS2 scaffold (ferguson2021fibroblastgrowthfactor pages 3-5, liu2026fgffamilyin pages 3-4). Upon activation, PLCγ hydrolyzes PIP₂ to generate diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP₃), which respectively activate PKC and mobilize intracellular calcium stores (liu2026fgffamilyin pages 3-4, klimaschewski2021fibroblastgrowthfactor pages 2-4). Hydrogen-deuterium exchange mass spectrometry has shown that PLCγ1 is relatively inert toward its substrate until bound to the FGFR1 kinase domain, whereupon conformational shifts prime it for membrane engagement and catalytic activity (klimaschewski2021fibroblastgrowthfactor pages 2-4).

The stepwise signaling cascade is summarized in the following table:

| Step number | Event name | Key molecules involved | Obligatory vs conditional | Output/consequence |
|---|---|---|---|---|
| 1 | Ligand engagement and cofactor-assisted receptor binding | Canonical/paracrine FGFs (e.g., FGF1, FGF2), FGFR1-4 ectodomains, heparan sulfate proteoglycans (HSPGs); endocrine FGFs additionally require α/βKlotho with residual HS dependence | Obligatory for canonical signaling; Klotho is conditional and mainly required for endocrine FGF signaling | Stabilization of high-affinity FGF-FGFR complexes, restriction/specification of ligand diffusion and receptor selectivity, priming for receptor dimerization (edirisinghe2024decodingfgffgfrsignaling pages 1-3, zheng2022signalingpathwayand pages 2-5, chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2) |
| 2 | FGFR dimerization and trans-autophosphorylation | FGFR1-4, ligand-bound receptor complexes, HS; intracellular kinase domains and activation-loop tyrosines | Obligatory | Formation of active receptor dimers and phosphotyrosine docking sites; current structural work supports an asymmetric dimerization model rather than a strictly symmetric one (ferguson2021fibroblastgrowthfactor pages 3-5, chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2, chen2023structuralbasisfor pages 18-26) |
| 3 | FRS2 phosphorylation and scaffold assembly | FRS2α/PTB domain, FGFR juxtamembrane region, phospho-FRS2 sites, GRB2, SHP2/PTPN11, GAB1 | Largely obligatory for the major FRS2-dependent MAPK branch; not the only possible proximal route in all contexts | Assembly of the proximal FGFR signalosome; creates binding platform for GRB2, SHP2, and GAB1 and helps specify sustained FGFR signaling (ferguson2021fibroblastgrowthfactor pages 3-5, klimaschewski2021fibroblastgrowthfactor pages 2-4, sobhani2021targetingaberrantfgfr pages 2-3) |
| 4 | GRB2-SOS recruitment and RAS-MAPK activation | Phospho-FRS2, GRB2, SOS1, RAS, RAF, MEK, ERK/MAPK; FRS2 GRB2-binding sites include Y196, Y306, Y349, Y392 | Core/near-obligatory for the canonical proliferative and developmental output, but strength and duration are context dependent | RAS activation and propagation through RAF-MEK-ERK, driving proliferation, differentiation, migration, and many developmental responses (ferguson2021fibroblastgrowthfactor pages 3-5, sobhani2021targetingaberrantfgfr pages 2-3, tome2023fibroblastgrowthfactor pages 2-4) |
| 5 | GAB1 recruitment and PI3K-AKT activation | FRS2-GRB2 complex, GAB1, PI3K (including PIK3R1/p85), AKT | Conditional/context dependent; common but not universal in all FGFR outputs | PI3K-AKT signaling supporting survival, metabolism, anti-apoptotic responses, and angiogenic programs (sobhani2021targetingaberrantfgfr pages 2-3, tome2023fibroblastgrowthfactor pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 1-3, ferguson2021fibroblastgrowthfactor pages 5-7) |
| 6 | PLCγ recruitment and PKC/Ca2+ activation | FGFR phosphotyrosines including receptor Y766, PLCγ1, PIP2, DAG, IP3, PKC, intracellular Ca2+ stores | Conditional; prominent in some cell types and receptor contexts | PIP2 hydrolysis to DAG and IP3, PKC activation, Ca2+ mobilization, and effects on motility, secretion, branching, and other context-specific programs (ferguson2021fibroblastgrowthfactor pages 3-5, liu2026fgffamilyin pages 3-4, ferguson2021fibroblastgrowthfactor pages 5-7, klimaschewski2021fibroblastgrowthfactor pages 2-4) |
| 7 | JAK-STAT engagement | FGFR-associated signaling complexes, JAKs, STATs | Conditional and less universally established than MAPK/PI3K/PLCγ branches | Transcriptional responses linked in some systems to invasion, inflammatory-like signaling, and tumor progression; should be treated as context-specific rather than a universal core branch (edirisinghe2024decodingfgffgfrsignaling pages 1-3, zheng2022signalingpathwayand pages 2-5) |
| 8 | Negative feedback, attenuation, and signal termination | SPRY1/2/4, SPREDs, SEF/IL17RD, DUSP6/MKP3, PTPRG and other phosphatases, CBL, ubiquitination machinery, endocytosis/lysosomal sorting, ERK feedback phosphorylation of FGFR1 S777 and FRS2 threonines | Obligatory for physiological signal shaping and termination, though exact regulators used are context dependent | Restriction of signal amplitude, duration, and spatial spread via inhibition of GRB2-SOS/RAS-ERK signaling, ERK dephosphorylation, receptor dephosphorylation, receptor/FRS2 ubiquitination, internalization, recycling, or degradation (szybowska2021negativeregulationof pages 15-17, ferguson2021fibroblastgrowthfactor pages 5-7, szybowska2021negativeregulationof pages 8-10, szybowska2021negativeregulationof pages 10-11, margiotta2021allgoodthings pages 4-6, szybowska2021negativeregulationof pages 7-8, ornitz2022newdevelopmentsin pages 18-20) |


*Table: This table summarizes the canonical sequence of FGFR signal transduction from ligand binding to downstream outputs and termination. It highlights which steps are core versus context-dependent and links each stage to supporting evidence.*

---

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive catalog of the core molecular players in the FGFR signaling module, their functional roles, binding partners, and regulatory features:

| Component name | Type/Class | Key function in FGFR signaling | Binding partners | Key regulatory features |
|---|---|---|---|---|
| FGF1 | Canonical/paracrine FGF ligand | Broad FGFR agonist; can activate multiple FGFR isoforms and drive proliferation, survival, migration, and repair programs | FGFR1-4 ectodomains; heparan sulfate proteoglycans (HSPGs) | High HS dependence typical of canonical FGFs; unusually broad receptor promiscuity relative to many other FGFs; activity shaped by tissue distribution and local HS composition (sobhani2021targetingaberrantfgfr pages 2-3, nguyen2024thecomplexityand pages 4-6, zheng2022signalingpathwayand pages 1-2) |
| FGF2 | Canonical/paracrine FGF ligand | Prototypic FGFR ligand in development, angiogenesis, tissue repair, and many experimental systems; initiates receptor dimerization and downstream MAPK/PI3K/PLCγ outputs | FGFR1-4 (context dependent), HSPGs | Stabilized by HSPGs, which protect ligand and strengthen receptor binding; biological effects are context dependent, including isoform- and dose/schedule-specific effects in bone and other tissues (sobhani2021targetingaberrantfgfr pages 2-3, tome2023fibroblastgrowthfactor pages 2-4, liu2026fgffamilyin pages 6-8) |
| FGFR1 | Receptor tyrosine kinase | Signal-transducing receptor that dimerizes upon FGF-HS binding and phosphorylates FRS2, PLCγ, and other effectors | FGF ligands, HSPGs, FRS2, PLCγ1, PIK3R1/p85, Klotho (for endocrine FGFs in some contexts) | Extracellular IgI-IgIII domains plus acid box; IgIIIb/IIIc splice variants alter ligand specificity; ERK feedback phosphorylation at S777 dampens signaling; targeted by phosphatases, endocytosis, and CBL-mediated downregulation (sobhani2021targetingaberrantfgfr pages 2-3, zheng2022signalingpathwayand pages 1-2, ornitz2022newdevelopmentsin pages 18-20) |
| FGFR2 | Receptor tyrosine kinase | Major epithelial and developmental FGFR; mediates canonical FGF responses in morphogenesis and tissue patterning | FGF ligands, HSPGs, FRS2; epithelial splice programs controlled by ESRP1/2 | IgIIIb/IIIc alternative splicing is especially important for epithelial-mesenchymal paracrine signaling; strongly linked to tissue-specific ligand recognition and developmental specificity (ferguson2021fibroblastgrowthfactor pages 2-3, nguyen2024thecomplexityand pages 4-6) |
| FGFR3 | Receptor tyrosine kinase | Mediates growth and differentiation signaling, especially in skeletal and epithelial contexts; can signal constitutively when mutated | FGF ligands, HSPGs, FRS2, PLCγ1 | Subject to phosphatase and CBL control; activating mutations can produce ligand-independent signaling in disease; splice variants alter ligand preference (sobhani2021targetingaberrantfgfr pages 2-3, zheng2022signalingpathwayand pages 1-2, szybowska2021negativeregulationof pages 7-8) |
| FGFR4 | Receptor tyrosine kinase | Canonical FGFR lacking IIIb/IIIc alternative splice pair; participates in both paracrine and endocrine FGF signaling | Select FGF ligands, HSPGs, Klotho complexes (context dependent) | Structurally distinct from FGFR1-3, including hinge-region C552; tends to recycle more than FGFR1-3 after endocytosis; has narrower ligand selectivity in many summaries (nguyen2024thecomplexityand pages 6-8, margiotta2021allgoodthings pages 4-6) |
| Heparan sulfate proteoglycans (HSPGs) | Cell-surface/ECM glycan cofactors | Essential cofactors for canonical/paracrine FGF signaling; stabilize ligand-receptor complexes, constrain diffusion, and help drive receptor dimerization/activation | Canonical FGFs, FGFR ectodomains, ECM/cell surface | HS sulfation pattern helps encode ligand specificity and signaling range; 2023 cryo-EM supports a central role for a single HS chain in asymmetric receptor recruitment and activation (edirisinghe2024decodingfgffgfrsignaling pages 1-3, chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2) |
| α/βKlotho | Coreceptors for endocrine FGFs | Confer high-affinity binding and specificity for endocrine FGFs (FGF19/21/23 family), stabilizing primary FGF-FGFR complexes | Endocrine FGFs, FGFR1-4 (isoform/context dependent) | Not generally required for canonical paracrine FGFs; in the asymmetric model Klotho stabilizes the primary ternary complex but does not itself recruit the secondary FGFR chain (ferguson2021fibroblastgrowthfactor pages 5-7, chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2) |
| FRS2 (FRS2α) | Lipid-anchored adaptor/scaffold | Principal proximal FGFR docking protein; couples activated FGFR to RAS-MAPK and PI3K-AKT pathways | FGFR juxtamembrane region, GRB2, SHP2/PTPN11, GAB1, SOS1 indirectly | Constitutively bound to the FGFR juxtamembrane region via its PTB domain; key phosphotyrosines include Y196, Y306, Y349, Y392 for GRB2 recruitment and Y346 for SHP2 recruitment; also participates in negative regulation via CBL-linked ubiquitination; interactome extends to cytoskeletal and junctional proteins (ferguson2021fibroblastgrowthfactor pages 3-5, klimaschewski2021fibroblastgrowthfactor pages 2-4, kopp2025proteomicanalysisreveals pages 16-19) |
| GRB2 | Adaptor protein | Connects phospho-FRS2 and related docking proteins to SOS1 and GAB1, enabling RAS and PI3K pathway activation | FRS2, SOS1, GAB1, SPRY proteins | Central node for branch selection between MAPK and PI3K outputs; can be sequestered by SPRY proteins to attenuate signaling (sobhani2021targetingaberrantfgfr pages 2-3, szybowska2021negativeregulationof pages 8-10, tome2023fibroblastgrowthfactor pages 2-4) |
| SOS1 | Ras guanine nucleotide exchange factor (GEF) | Activates RAS by promoting GDP-GTP exchange downstream of GRB2-FRS2 complexes | GRB2, RAS | Recruitment is conditional on scaffold assembly downstream of receptor activation; a major route to RAF-MEK-ERK activation (tome2023fibroblastgrowthfactor pages 2-4, zheng2022signalingpathwayand pages 2-5) |
| SHP2/PTPN11 | Tyrosine phosphatase/adaptor | Promotes efficient propagation of RAS-MAPK signaling from the FRS2 complex and contributes to scaffold organization | FRS2, GRB2-associated complexes | Functions as both catalytic phosphatase and signaling adaptor; role can be context dependent, and some summaries also describe inhibitory actions at particular pathway levels or settings (sobhani2021targetingaberrantfgfr pages 2-3, liu2026fgffamilyin pages 4-6, ferguson2021fibroblastgrowthfactor pages 3-5) |
| GAB1 | Adaptor/scaffold | Links GRB2-FRS2 complexes to PI3K-AKT activation downstream of FGFRs | GRB2, PIK3R1/p85, FRS2-associated complexes | Recruitment is conditional and branch-specific; helps determine strength of survival/anti-apoptotic signaling (tome2023fibroblastgrowthfactor pages 2-4, edirisinghe2024decodingfgffgfrsignaling pages 1-3, sobhani2021targetingaberrantfgfr pages 2-3) |
| PIK3R1/p85 | Regulatory subunit of class IA PI3K | Recruits/activates PI3K signaling downstream of FGFR, leading to AKT activation | GAB1, phosphotyrosine-containing complexes; in some contexts can bind FGFR more directly | Participation varies by cell type and receptor context; supports survival, metabolism, and angiogenic outputs (ferguson2021fibroblastgrowthfactor pages 3-5, ferguson2021fibroblastgrowthfactor pages 5-7) |
| PLCγ1 | Phospholipase effector enzyme | Binds activated FGFR and hydrolyzes PIP2 to IP3 and DAG, triggering Ca2+ release and PKC signaling | Phospho-FGFR (notably FGFR Y766 in many models), membrane PIP2 | Direct receptor effector rather than FRS2-dependent branch; contributes to migration, morphogenesis, and context-specific signaling outputs (ferguson2021fibroblastgrowthfactor pages 3-5, liu2026fgffamilyin pages 3-4, klimaschewski2021fibroblastgrowthfactor pages 2-4) |
| RAS-RAF-MEK-ERK cascade | Kinase cascade / MAPK module | Major proliferative and differentiation output downstream of FGFR-FRS2-GRB2-SOS signaling | RAS with RAF; RAF with MEK; MEK with ERK; scaffold/adaptor support from FRS2 complex | Often the dominant FGFR output; subject to strong feedback inhibition through SPRY proteins, DUSP6, and ERK-dependent phosphorylation of FGFR1/FRS2 (liu2026fgffamilyin pages 3-4, szybowska2021negativeregulationof pages 15-17, ornitz2022newdevelopmentsin pages 18-20) |
| SPRY (SPRY1/2/4) | Feedback inhibitor family | Negative regulators of RTK/FGFR signaling, especially the RAS-MAPK branch | GRB2, CBL, PP2A, RAF (context dependent) | Induced by FGF signaling; can bind GRB2 to block GRB2-SOS recruitment, directly inhibit RAF, and interface with CBL/PP2A; major feedback brake on ERK output (szybowska2021negativeregulationof pages 15-17, ferguson2021fibroblastgrowthfactor pages 5-7, szybowska2021negativeregulationof pages 8-10) |
| SEF / IL17RD | Transmembrane feedback inhibitor | Attenuates FGFR signaling at receptor-proximal and MAPK-pathway levels | FGFR, RAS/MAPK pathway components | Can interfere with FGFR phosphorylation/dimerization and suppress MEK/ERK and AKT outputs; conserved developmental feedback regulator, though exact mechanism varies by system (liu2026fgffamilyin pages 4-6, szybowska2021negativeregulationof pages 10-11) |
| CBL | E3 ubiquitin ligase | Terminates/prolimits FGFR signaling by ubiquitinating FGFRs and FRS2-containing complexes | FRS2-GRB2 complexes, activated FGFRs, endocytic machinery | Promotes internalization, lysosomal/proteasomal routing, and signal termination; a core regulator of receptor lifetime and signaling duration (ferguson2021fibroblastgrowthfactor pages 5-7, margiotta2021allgoodthings pages 4-6, szybowska2021negativeregulationof pages 7-8) |
| DUSP6 (MKP3) | Dual-specificity MAPK phosphatase | Dephosphorylates ERK1/2 to terminate MAPK output downstream of FGFR | ERK1/2 | Induced as an FGF-responsive negative feedback gene; a key mechanism for restricting duration and spatial spread of ERK signaling (szybowska2021negativeregulationof pages 8-10, ornitz2022newdevelopmentsin pages 18-20) |


*Table: This table summarizes the major molecular components of the FGFR signaling module, their mechanistic roles, key interaction partners, and principal modes of regulation. It is useful as a compact map linking ligand binding, receptor activation, scaffold assembly, downstream signaling, and pathway shutdown.*

### 4.1 The FGFR receptor family

FGFR1–4 are single-pass transmembrane proteins sharing a conserved architecture: an extracellular domain with three immunoglobulin-like subdomains (IgI, IgII, IgIII), an acid box between IgI and IgII that functions in autoinhibition, a transmembrane helix, and a split intracellular tyrosine kinase domain (sobhani2021targetingaberrantfgfr pages 2-3, zheng2022signalingpathwayand pages 1-2, tome2023fibroblastgrowthfactor pages 1-2). A critical source of signaling diversity arises from alternative splicing of the IgIII domain in FGFR1–3, generating IgIIIb and IgIIIc isoforms with distinct ligand-binding specificities (ferguson2021fibroblastgrowthfactor pages 2-3, nguyen2024thecomplexityand pages 4-6). FGFR4 lacks this alternative splicing and has only the IIIc-equivalent isoform (nguyen2024thecomplexityand pages 6-8). N-glycosylation patterns on the FGFR ectodomain further regulate receptor function and ligand recognition (nguyen2024thecomplexityand pages 6-8).

### 4.2 Negative regulatory apparatus

Signal termination and shaping rely on multiple overlapping mechanisms. SPRY proteins (SPRY1/2/4) are FGF-inducible feedback inhibitors that translocate to the plasma membrane and bind GRB2 to prevent its association with FRS2 or SHP2, thereby blocking RAS-MAPK activation; SPRY2 also directly inhibits RAF (szybowska2021negativeregulationof pages 8-10). DUSP6 (MKP3) is an ERK-specific phosphatase induced by FGF signaling through the ETS2/CIC transcriptional axis, providing a delayed negative feedback loop (ornitz2022newdevelopmentsin pages 18-20). CBL, an E3 ubiquitin ligase, mono- and polyubiquitinates FGFRs and FRS2 within the signalosome complex, targeting them for endocytosis and lysosomal/proteasomal degradation (ferguson2021fibroblastgrowthfactor pages 5-7, szybowska2021negativeregulationof pages 7-8). SEF/IL17RD, initially identified as a zebrafish feedback inhibitor, attenuates FGFR signaling at multiple levels including receptor phosphorylation/dimerization and downstream MEK activation (szybowska2021negativeregulationof pages 10-11). Direct ERK-mediated feedback phosphorylation of FGFR1 at S777 and of FRS2 at eight threonine residues provides additional attenuation (ferguson2021fibroblastgrowthfactor pages 5-7, szybowska2021negativeregulationof pages 10-11). The phosphatase PTPRG accounts for approximately 80% of phosphatase activity toward FGFR1 during early activation (szybowska2021negativeregulationof pages 7-8).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Evolutionary origin and conservation

FGF-like domains are found in choanoflagellates, suggesting pre-metazoan origins, but bona fide secreted FGF signaling through FGFRs likely originated in the common ancestor of cnidarians and bilaterians (shalaeva2021structuralandfunctional pages 15-17). Cnidarians possess FGF8/17/18 subfamily members and numerous diverged FGF genes, while protostomes acquired additional repertoire including FGF9/16/20 and likely FGF1/2 subfamilies (shalaeva2021structuralandfunctional pages 15-17). The FGF23 endocrine subfamily has evolutionarily conserved functions extending to *C. elegans* and *Drosophila* (shalaeva2021structuralandfunctional pages 15-17). The role of FGF signaling in tissue regeneration appears deeply conserved: FGF signaling is required for posterior regeneration in the annelid worm *Alitta virens*, resembling vertebrate appendage regeneration and suggesting this function predates the bilaterian ancestor (shalaeva2021structuralandfunctional pages 15-17). However, invertebrate model organisms show notable variation: *Drosophila* has two FGFRs (Heartless and Breathless) and three FGF ligands, while *C. elegans* has a single FGFR (EGL-15) and two FGF ligands, indicating significant lineage-specific losses and expansions.

### 5.2 Vertebrate gene family expansion

The vertebrate FGF/FGFR system has expanded dramatically relative to invertebrates. The human genome encodes 22 FGF family members (18 secreted signaling ligands plus 4 intracellular iFGFs) and 4 FGFRs, with additional diversity generated by alternative splicing of the IgIIIb/IIIc exons in FGFR1–3 (sobhani2021targetingaberrantfgfr pages 2-3, ferguson2021fibroblastgrowthfactor pages 2-3). This expansion is attributed to whole-genome duplication events in early vertebrate evolution. The ancestral roles of FGFR signaling in mesoderm induction and cell proliferation are likely best represented by the broadly expressed members FGF2 (among ligands) and FGFR1 (among receptors), which retain the widest expression patterns and functional versatility.

### 5.3 Tissue-specific isoform variation

Alternative splicing of the IgIII domain generates a fundamental axis of signaling specificity: IIIb isoforms are expressed in epithelial cells under control of the splicing regulators ESRP1 and ESRP2, while IIIc isoforms predominate in mesenchymal cells (ferguson2021fibroblastgrowthfactor pages 2-3). Crucially, epithelial IIIb receptors preferentially bind ligands produced by mesenchymal cells, and mesenchymal IIIc receptors bind epithelial-derived ligands, establishing a reciprocal paracrine signaling circuit that is essential for tissue patterning during development and wound repair (nguyen2024thecomplexityand pages 4-6). This isoform-switching mechanism also contributes to epithelial-mesenchymal transition (EMT) in cancer progression (nguyen2024thecomplexityand pages 4-6). FGF signaling outputs are further modulated by cell-type-specific expression of individual FGFRs: FGFR1 predominates in many mesenchymal contexts, FGFR2 is the major epithelial FGFR, and FGFR3 has prominent roles in skeletal and urothelial tissues (sobhani2021targetingaberrantfgfr pages 2-3, liu2023fgfrfamiliesbiological pages 2-4).

### 5.4 Context-dependent signaling outputs

The biological outcome of FGFR activation is highly context-dependent. In developing tissues, FGF signaling drives cell proliferation and fate specification; the same pathway in adult tissues supports homeostasis and repair (liu2023fgfrfamiliesbiological pages 2-4, liu2026fgffamilyin pages 6-8). Even for the same ligand, dosing kinetics alter outcome: continuous FGF2 treatment inhibits osteoblast differentiation, while intermittent treatment stimulates bone formation (liu2026fgffamilyin pages 6-8). Different FGF2 isoforms (secreted low-molecular-weight vs. nuclear high-molecular-weight) produce opposing skeletal phenotypes (liu2026fgffamilyin pages 6-8).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory ordering of events

The signaling cascade follows a strict ordering: (1) ligand–cofactor–receptor engagement must precede (2) receptor dimerization and kinase activation, which must precede (3) FRS2 phosphorylation and scaffold assembly, which must precede (4) MAPK and PI3K output. Genetic ablation of the FGFR juxtamembrane region (which eliminates FRS2 binding) disrupts developmental transcriptional regulation and actin cytoskeletal arrangements, phenocopying complete loss of FGF signaling in lens induction, and this defect can be rescued by constitutively active KRAS—placing RAS activation downstream of and dependent on the FRS2 scaffold (ferguson2021fibroblastgrowthfactor pages 3-5, klimaschewski2021fibroblastgrowthfactor pages 2-4).

### 6.2 Mutually exclusive and branch-specific constraints

PLCγ binds directly to phosphorylated FGFR (Y766), independently of FRS2, creating a mechanistic bifurcation where the FRS2-dependent MAPK/PI3K branches and the PLCγ branch are recruited through distinct receptor phosphotyrosines (ferguson2021fibroblastgrowthfactor pages 3-5, liu2026fgffamilyin pages 3-4). SPRY proteins can sequester GRB2 away from the FRS2 complex, making GRB2–SOS recruitment and SPRY-mediated inhibition mutually exclusive for a given GRB2 molecule (szybowska2021negativeregulationof pages 8-10). FGFR1–3 undergo lysosomal degradation upon CBL-mediated ubiquitination, while FGFR4 preferentially recycles to the plasma membrane, creating receptor-specific differences in signal duration and cell-surface availability (margiotta2021allgoodthings pages 4-6).

### 6.3 Disease-associated failure modes

FGFR genetic alterations—amplification, activating point mutations, and chromosomal fusions/rearrangements—are found in approximately 7.1% of tumors across cancer types (OpenTargets Search: -FGFR1,FGFR2,FGFR3,FGFR4). Germline gain-of-function mutations in FGFRs cause skeletal dysplasia syndromes (e.g., achondroplasia from FGFR3 mutations, craniosynostosis syndromes from FGFR2 mutations including Pfeiffer syndrome) and developmental disorders (Hartsfield syndrome from FGFR1 mutations, hypogonadotropic hypogonadism from FGFR1 loss-of-function mutations) (OpenTargets Search: -FGFR1,FGFR2,FGFR3,FGFR4). Loss of negative regulators such as SPRY2 can produce sustained ERK activation, contributing to pathological states including thanatophoric dysplasia (szybowska2021negativeregulationof pages 15-17). Constitutive FGFR3 activation through point mutations occurs in approximately 70% of non-muscle-invasive bladder cancers (OpenTargets Search: -FGFR1,FGFR2,FGFR3,FGFR4).

---

## 7. Controversies and Open Questions

### 7.1 Symmetric vs. asymmetric dimerization

The 2023 cryo-EM structures by Chen et al. demonstrate asymmetric FGFR dimerization mediated by a single HS chain and overturn the prior symmetric 2:2:2 paradigm (chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2). However, earlier crystallographic and biochemical studies supported symmetric models where two 1:1:1 ternary complexes associate through direct receptor–receptor contacts (szybowska2021thecanonicalfgffgfr pages 2-4). Whether the asymmetric model is universal for all FGF–FGFR combinations, or whether both modes coexist depending on HS composition and cellular context, remains an active area of investigation (szybowska2021thecanonicalfgffgfr pages 2-4).

### 7.2 FRS2-independent signaling routes

While FRS2 is the dominant FGFR proximal adaptor, SHC1 has been established as a collaborator with FRS2 and SHP2 in recruiting GRB2 during FGF-induced lens development, and deletion of SHC1 exacerbates the phenotype caused by FRS2/SHP2 loss (ferguson2021fibroblastgrowthfactor pages 3-5). Whether SHC1 represents an accessory or alternative route to GRB2 recruitment in other developmental and physiological contexts is not fully resolved.

### 7.3 The breadth of the FRS2 interactome

Recent proximity labeling studies have identified over 100 FRS2-associated proteins, many involved in actin cytoskeleton remodeling, cell junction assembly, and translational regulation—functions not previously attributed to canonical FGFR signaling (kopp2025proteomicanalysisreveals pages 21-23, kopp2025proteomicanalysisreveals pages 19-21, kopp2025proteomicanalysisreveals pages 23-25). The functional significance of these novel FRS2 interactions for normal physiology and cancer biology is largely unexplored.

### 7.4 Pathway quantitative dynamics

The relative contribution of each downstream branch (MAPK, PI3K, PLCγ) varies by cell type, receptor isoform, and ligand identity, but quantitative models that predict branch selection and output strength from known inputs are lacking. The role of signal duration versus amplitude in determining biological outcome—a critical question for therapeutic targeting—remains insufficiently characterized, particularly in vivo.

### 7.5 Cross-species extrapolation

Much of the mechanistic knowledge of FGFR signaling derives from mammalian cell lines and mouse genetics, with limited validation in human primary cells and tissues. Invertebrate model organisms (*Drosophila*, *C. elegans*) have highly reduced FGF/FGFR complements and may use qualitatively different signaling logic, making direct extrapolation between systems hazardous (shalaeva2021structuralandfunctional pages 15-17). Notably, some annelid lineages have completely lost FGF ligands, demonstrating that the pathway is dispensable in some evolutionary contexts despite its deep conservation in others (shalaeva2021structuralandfunctional pages 15-17).

---

## 8. Key References

The following references provide primary and review-level support for the claims in this review:

- **Ornitz DM, Itoh N** (2022). New developments in the biology of fibroblast growth factors. *WIREs Mechanisms of Disease*, e1549. DOI: 10.1002/wsbm.1549 — Comprehensive review of the FGF field (ornitz2022newdevelopmentsin pages 18-20).

- **Chen L et al.** (2023). Structural basis for FGF hormone signalling. *Nature*, 618:862-870. DOI: 10.1038/s41586-023-06155-9 — Cryo-EM structures establishing asymmetric FGFR dimerization (chen2023structuralbasisfor pages 2-3, chen2023structuralbasisfor pages 1-2, chen2023structuralbasisfor pages 18-26).

- **Ferguson HR, Smith MP, Francavilla C** (2021). Fibroblast Growth Factor Receptors (FGFRs) and Noncanonical Partners in Cancer Signaling. *Cells*, 10:1201. DOI: 10.3390/cells10051201 — Detailed coverage of canonical and noncanonical FGFR signaling (ferguson2021fibroblastgrowthfactor pages 3-5, ferguson2021fibroblastgrowthfactor pages 5-7).

- **Edirisinghe O et al.** (2024). Decoding FGF/FGFR Signaling. *Biomolecules*, 14:1622. DOI: 10.3390/biom14121622 — Comprehensive recent review of FGF/FGFR biology (edirisinghe2024decodingfgffgfrsignaling pages 1-3).

- **Szybowska P et al.** (2021). Negative Regulation of FGFR Signaling. *Cells*, 10:1342. DOI: 10.3390/cells10061342 — Detailed review of negative feedback mechanisms (szybowska2021negativeregulationof pages 15-17, szybowska2021negativeregulationof pages 8-10, szybowska2021negativeregulationof pages 10-11, szybowska2021negativeregulationof pages 7-8).

- **Liu Q et al.** (2023). FGFR families: biological functions and therapeutic interventions in tumors. *MedComm*, 4:e367. DOI: 10.1002/mco2.367 — FGFR family functions and therapeutic agents (liu2023fgfrfamiliesbiological pages 2-4).

- **Katoh M et al.** (2024). FGFR-targeted therapeutics: clinical activity, mechanisms of resistance and new directions. *Nature Reviews Clinical Oncology*, 21:312-329. DOI: 10.1038/s41571-024-00869-z — Authoritative review of FGFR-targeted therapeutics.

- **Kopp LL et al.** (2026). FRS2 interactome mapping reveals novel candidate interactors. *bioRxiv*. DOI: 10.1101/2025.09.23.678042 — FRS2 interactome characterization (kopp2025proteomicanalysisreveals pages 21-23, kopp2025proteomicanalysisreveals pages 19-21, kopp2025proteomicanalysisreveals pages 16-19).

- **Xie Y et al.** (2020). FGF/FGFR signaling in health and disease. *Signal Transduction and Targeted Therapy*, 5. DOI: 10.1038/s41392-020-00222-7 — Major review with 1,082 citations covering FGF/FGFR in development and disease (xie2020fgffgfrsignalingin pages 1-2).

- **Liu X et al.** (2026). FGF family in health and disease. *Molecular Biomedicine*, 7. DOI: 10.1186/s43556-026-00429-0 — Recent integrative review of FGF system (liu2026fgffamilyin pages 3-4, liu2026fgffamilyin pages 4-6, liu2026fgffamilyin pages 6-8).

- **Nguyen AL, Facey COB, Boman BM** (2024). The Complexity and Significance of FGF Signaling. *Cancers*, 17:82. DOI: 10.3390/cancers17010082 — FGFR structure, isoform specificity, and cancer relevance (nguyen2024thecomplexityand pages 4-6, nguyen2024thecomplexityand pages 6-8).

- **Shalaeva AY et al.** (2021). FGF Signaling Pathway in Regeneration of *Alitta virens*. *Genes*, 12:788. DOI: 10.3390/genes12060788 — Evolutionary conservation of FGF in annelid regeneration (shalaeva2021structuralandfunctional pages 15-17).

- **Sobhani N et al.** (2021). Targeting Aberrant FGFR Signaling to Overcome CDK4/6 Inhibitor Resistance. *Cells*, 10:293. DOI: 10.3390/cells10020293 — FGFR pathway architecture and breast cancer (sobhani2021targetingaberrantfgfr pages 2-3).

- **Tomé D et al.** (2023). Fibroblast growth factor signaling in axons. *Cell Communication and Signaling*, 21. DOI: 10.1186/s12964-023-01284-0 — FGF signaling in nervous system contexts (tome2023fibroblastgrowthfactor pages 2-4).

- **Klimaschewski L, Claus P** (2021). Fibroblast Growth Factor Signalling in the Diseased Nervous System. *Molecular Neurobiology*, 58:3884-3902. DOI: 10.1007/s12035-021-02367-0 — FRS2 characterization and neuronal FGF signaling (klimaschewski2021fibroblastgrowthfactor pages 2-4).

References

1. (edirisinghe2024decodingfgffgfrsignaling pages 1-3): Oshadi Edirisinghe, Gaëtane Ternier, Zeina Alraawi, and Thallapuranam Krishnaswamy Suresh Kumar. Decoding fgf/fgfr signaling: insights into biological functions and disease relevance. Biomolecules, 14:1622, Dec 2024. URL: https://doi.org/10.3390/biom14121622, doi:10.3390/biom14121622. This article has 49 citations.

2. (xie2020fgffgfrsignalingin pages 1-2): Yangli Xie, N. Su, Jing Yang, Q. Tan, Shuo Huang, M. Jin, Z. Ni, Bin Zhang, Dali Zhang, F. Luo, Hangang Chen, Xianding Sun, Jian Q. Feng, H. Qi, and Lin Chen. Fgf/fgfr signaling in health and disease. Signal Transduction and Targeted Therapy, Sep 2020. URL: https://doi.org/10.1038/s41392-020-00222-7, doi:10.1038/s41392-020-00222-7. This article has 1082 citations and is from a peer-reviewed journal.

3. (ferguson2021fibroblastgrowthfactor pages 3-5): Harriet R. Ferguson, Michael P. Smith, and Chiara Francavilla. Fibroblast growth factor receptors (fgfrs) and noncanonical partners in cancer signaling. Cells, 10:1201, May 2021. URL: https://doi.org/10.3390/cells10051201, doi:10.3390/cells10051201. This article has 145 citations.

4. (liu2026fgffamilyin pages 3-4): Xiaoyu Liu, Meiling Jing, Yueyi Yang, Qiaoqiao Jin, Bo Feng, Pengfei Zhang, Chenguang Niu, Xuchen Hu, and Zhengwei Huang. Fgf family in health and disease. Molecular Biomedicine, Mar 2026. URL: https://doi.org/10.1186/s43556-026-00429-0, doi:10.1186/s43556-026-00429-0. This article has 1 citations and is from a peer-reviewed journal.

5. (tome2023fibroblastgrowthfactor pages 2-4): Diogo Tomé, Marta S. Dias, Joana Correia, and Ramiro D. Almeida. Fibroblast growth factor signaling in axons: from development to disease. Cell Communication and Signaling : CCS, Oct 2023. URL: https://doi.org/10.1186/s12964-023-01284-0, doi:10.1186/s12964-023-01284-0. This article has 41 citations.

6. (szybowska2021negativeregulationof pages 15-17): Patrycja Szybowska, Michal Kostas, Jørgen Wesche, Ellen Margrethe Haugsten, and Antoni Wiedlocha. Negative regulation of fgfr (fibroblast growth factor receptor) signaling. Cells, 10:1342, May 2021. URL: https://doi.org/10.3390/cells10061342, doi:10.3390/cells10061342. This article has 60 citations.

7. (ferguson2021fibroblastgrowthfactor pages 5-7): Harriet R. Ferguson, Michael P. Smith, and Chiara Francavilla. Fibroblast growth factor receptors (fgfrs) and noncanonical partners in cancer signaling. Cells, 10:1201, May 2021. URL: https://doi.org/10.3390/cells10051201, doi:10.3390/cells10051201. This article has 145 citations.

8. (ornitz2022newdevelopmentsin pages 18-20): D. Ornitz and N. Itoh. New developments in the biology of fibroblast growth factors. WIREs mechanisms of disease, pages e1549, Feb 2022. URL: https://doi.org/10.1002/wsbm.1549, doi:10.1002/wsbm.1549. This article has 163 citations.

9. (chen2023structuralbasisfor pages 2-3): Lingfeng Chen, Li-li Fu, Jingchuan Sun, Zhiqiang Huang, Mingzhen Fang, Allen P. Zinkle, Xin Liu, Junliang Lu, Zixiang Pan, Yang Wang, Guang Liang, Xiaokun Li, Gaozhi Chen, and M. Mohammadi. Structural basis for fgf hormone signalling. Nature, 618:862-870, Jun 2023. URL: https://doi.org/10.1038/s41586-023-06155-9, doi:10.1038/s41586-023-06155-9. This article has 136 citations and is from a highest quality peer-reviewed journal.

10. (chen2023structuralbasisfor pages 1-2): Lingfeng Chen, Li-li Fu, Jingchuan Sun, Zhiqiang Huang, Mingzhen Fang, Allen P. Zinkle, Xin Liu, Junliang Lu, Zixiang Pan, Yang Wang, Guang Liang, Xiaokun Li, Gaozhi Chen, and M. Mohammadi. Structural basis for fgf hormone signalling. Nature, 618:862-870, Jun 2023. URL: https://doi.org/10.1038/s41586-023-06155-9, doi:10.1038/s41586-023-06155-9. This article has 136 citations and is from a highest quality peer-reviewed journal.

11. (OpenTargets Search: -FGFR1,FGFR2,FGFR3,FGFR4): Open Targets Query (-FGFR1,FGFR2,FGFR3,FGFR4, 22 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (zheng2022signalingpathwayand pages 2-5): Jia Zheng, Wei Zhang, Linfeng Li, Yi He, Yue Wei, Yongjun Dang, Shenyou Nie, and Zufeng Guo. Signaling pathway and small-molecule drug discovery of fgfr: a comprehensive review. Frontiers in Chemistry, Apr 2022. URL: https://doi.org/10.3389/fchem.2022.860985, doi:10.3389/fchem.2022.860985. This article has 79 citations.

13. (liu2026fgffamilyin pages 4-6): Xiaoyu Liu, Meiling Jing, Yueyi Yang, Qiaoqiao Jin, Bo Feng, Pengfei Zhang, Chenguang Niu, Xuchen Hu, and Zhengwei Huang. Fgf family in health and disease. Molecular Biomedicine, Mar 2026. URL: https://doi.org/10.1186/s43556-026-00429-0, doi:10.1186/s43556-026-00429-0. This article has 1 citations and is from a peer-reviewed journal.

14. (ferguson2021fibroblastgrowthfactor pages 2-3): Harriet R. Ferguson, Michael P. Smith, and Chiara Francavilla. Fibroblast growth factor receptors (fgfrs) and noncanonical partners in cancer signaling. Cells, 10:1201, May 2021. URL: https://doi.org/10.3390/cells10051201, doi:10.3390/cells10051201. This article has 145 citations.

15. (sobhani2021targetingaberrantfgfr pages 2-3): Navid Sobhani, Anne Fassl, Giuseppina Mondani, Daniele Generali, and Tobias Otto. Targeting aberrant fgfr signaling to overcome cdk4/6 inhibitor resistance in breast cancer. Cells, 10:293, Feb 2021. URL: https://doi.org/10.3390/cells10020293, doi:10.3390/cells10020293. This article has 58 citations.

16. (margiotta2021allgoodthings pages 4-6): Azzurra Margiotta. All good things must end: termination of receptor tyrosine kinase signal. International Journal of Molecular Sciences, 22:6342, Jun 2021. URL: https://doi.org/10.3390/ijms22126342, doi:10.3390/ijms22126342. This article has 17 citations.

17. (chen2023structuralbasisfor pages 18-26): Lingfeng Chen, Li-li Fu, Jingchuan Sun, Zhiqiang Huang, Mingzhen Fang, Allen P. Zinkle, Xin Liu, Junliang Lu, Zixiang Pan, Yang Wang, Guang Liang, Xiaokun Li, Gaozhi Chen, and M. Mohammadi. Structural basis for fgf hormone signalling. Nature, 618:862-870, Jun 2023. URL: https://doi.org/10.1038/s41586-023-06155-9, doi:10.1038/s41586-023-06155-9. This article has 136 citations and is from a highest quality peer-reviewed journal.

18. (klimaschewski2021fibroblastgrowthfactor pages 2-4): Lars Klimaschewski and Peter Claus. Fibroblast growth factor signalling in the diseased nervous system. Molecular Neurobiology, 58:3884-3902, Apr 2021. URL: https://doi.org/10.1007/s12035-021-02367-0, doi:10.1007/s12035-021-02367-0. This article has 143 citations and is from a peer-reviewed journal.

19. (kopp2025proteomicanalysisreveals pages 21-23): Levi Luca Kopp, Dejana Versamento, Bernard Ciraulo, Marc Thomas Schönholzer, Dina Hochuli, Meng-Syuan Lin, and Martin Baumgartner. Fibroblast growth factor receptor substrate 2 interactome mapping reveals novel candidate interactors associated with migration and invasion. bioRxiv, May 2026. URL: https://doi.org/10.1101/2025.09.23.678042, doi:10.1101/2025.09.23.678042. This article has 0 citations.

20. (kopp2025proteomicanalysisreveals pages 19-21): Levi Luca Kopp, Dejana Versamento, Bernard Ciraulo, Marc Thomas Schönholzer, Dina Hochuli, Meng-Syuan Lin, and Martin Baumgartner. Fibroblast growth factor receptor substrate 2 interactome mapping reveals novel candidate interactors associated with migration and invasion. bioRxiv, May 2026. URL: https://doi.org/10.1101/2025.09.23.678042, doi:10.1101/2025.09.23.678042. This article has 0 citations.

21. (kopp2025proteomicanalysisreveals pages 16-19): Levi Luca Kopp, Dejana Versamento, Bernard Ciraulo, Marc Thomas Schönholzer, Dina Hochuli, Meng-Syuan Lin, and Martin Baumgartner. Fibroblast growth factor receptor substrate 2 interactome mapping reveals novel candidate interactors associated with migration and invasion. bioRxiv, May 2026. URL: https://doi.org/10.1101/2025.09.23.678042, doi:10.1101/2025.09.23.678042. This article has 0 citations.

22. (szybowska2021negativeregulationof pages 8-10): Patrycja Szybowska, Michal Kostas, Jørgen Wesche, Ellen Margrethe Haugsten, and Antoni Wiedlocha. Negative regulation of fgfr (fibroblast growth factor receptor) signaling. Cells, 10:1342, May 2021. URL: https://doi.org/10.3390/cells10061342, doi:10.3390/cells10061342. This article has 60 citations.

23. (szybowska2021negativeregulationof pages 10-11): Patrycja Szybowska, Michal Kostas, Jørgen Wesche, Ellen Margrethe Haugsten, and Antoni Wiedlocha. Negative regulation of fgfr (fibroblast growth factor receptor) signaling. Cells, 10:1342, May 2021. URL: https://doi.org/10.3390/cells10061342, doi:10.3390/cells10061342. This article has 60 citations.

24. (szybowska2021negativeregulationof pages 7-8): Patrycja Szybowska, Michal Kostas, Jørgen Wesche, Ellen Margrethe Haugsten, and Antoni Wiedlocha. Negative regulation of fgfr (fibroblast growth factor receptor) signaling. Cells, 10:1342, May 2021. URL: https://doi.org/10.3390/cells10061342, doi:10.3390/cells10061342. This article has 60 citations.

25. (nguyen2024thecomplexityand pages 4-6): Anh L. Nguyen, Caroline O. B. Facey, and Bruce M. Boman. The complexity and significance of fibroblast growth factor (fgf) signaling for fgf-targeted cancer therapies. Cancers, 17:82, Dec 2024. URL: https://doi.org/10.3390/cancers17010082, doi:10.3390/cancers17010082. This article has 16 citations.

26. (zheng2022signalingpathwayand pages 1-2): Jia Zheng, Wei Zhang, Linfeng Li, Yi He, Yue Wei, Yongjun Dang, Shenyou Nie, and Zufeng Guo. Signaling pathway and small-molecule drug discovery of fgfr: a comprehensive review. Frontiers in Chemistry, Apr 2022. URL: https://doi.org/10.3389/fchem.2022.860985, doi:10.3389/fchem.2022.860985. This article has 79 citations.

27. (liu2026fgffamilyin pages 6-8): Xiaoyu Liu, Meiling Jing, Yueyi Yang, Qiaoqiao Jin, Bo Feng, Pengfei Zhang, Chenguang Niu, Xuchen Hu, and Zhengwei Huang. Fgf family in health and disease. Molecular Biomedicine, Mar 2026. URL: https://doi.org/10.1186/s43556-026-00429-0, doi:10.1186/s43556-026-00429-0. This article has 1 citations and is from a peer-reviewed journal.

28. (nguyen2024thecomplexityand pages 6-8): Anh L. Nguyen, Caroline O. B. Facey, and Bruce M. Boman. The complexity and significance of fibroblast growth factor (fgf) signaling for fgf-targeted cancer therapies. Cancers, 17:82, Dec 2024. URL: https://doi.org/10.3390/cancers17010082, doi:10.3390/cancers17010082. This article has 16 citations.

29. (tome2023fibroblastgrowthfactor pages 1-2): Diogo Tomé, Marta S. Dias, Joana Correia, and Ramiro D. Almeida. Fibroblast growth factor signaling in axons: from development to disease. Cell Communication and Signaling : CCS, Oct 2023. URL: https://doi.org/10.1186/s12964-023-01284-0, doi:10.1186/s12964-023-01284-0. This article has 41 citations.

30. (shalaeva2021structuralandfunctional pages 15-17): Alexandra Y. Shalaeva, Roman P. Kostyuchenko, and Vitaly V. Kozin. Structural and functional characterization of the fgf signaling pathway in regeneration of the polychaete worm alitta virens (annelida, errantia). Genes, 12:788, May 2021. URL: https://doi.org/10.3390/genes12060788, doi:10.3390/genes12060788. This article has 12 citations.

31. (liu2023fgfrfamiliesbiological pages 2-4): Qing Liu, Jiyu Huang, Weiwei Yan, Zhen Liu, Shu Liu, and Weiyi Fang. Fgfr families: biological functions and therapeutic interventions in tumors. MedComm, Sep 2023. URL: https://doi.org/10.1002/mco2.367, doi:10.1002/mco2.367. This article has 70 citations.

32. (szybowska2021thecanonicalfgffgfr pages 2-4): Patrycja Szybowska, Ellen Margrethe Haugsten, and Antoni Wiedlocha. The canonical fgf-fgfr signaling system at the molecular level. Postępy Higieny i Medycyny Doświadczalnej, 75:711-719, Jan 2021. URL: https://doi.org/10.2478/ahem-2021-0024, doi:10.2478/ahem-2021-0024. This article has 1 citations.

33. (kopp2025proteomicanalysisreveals pages 23-25): Levi Luca Kopp, Dejana Versamento, Bernard Ciraulo, Marc Thomas Schönholzer, Dina Hochuli, Meng-Syuan Lin, and Martin Baumgartner. Fibroblast growth factor receptor substrate 2 interactome mapping reveals novel candidate interactors associated with migration and invasion. bioRxiv, May 2026. URL: https://doi.org/10.1101/2025.09.23.678042, doi:10.1101/2025.09.23.678042. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](fgfr_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](fgfr_signaling-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](fgfr_signaling-deep-research-falcon_artifacts/artifact-02.md)
![Image artifact created (ID artifact-02): 'FGFR Signaling Pathway Module' ![FGFR Signaling Pathway Module](artifact:artifact-02) Artifact IDs that may be injecte](fgfr_signaling-deep-research-falcon_artifacts/image-1.png)

## Citations

1. ferguson2021fibroblastgrowthfactor pages 3-5
2. edirisinghe2024decodingfgffgfrsignaling pages 1-3
3. zheng2022signalingpathwayand pages 2-5
4. chen2023structuralbasisfor pages 18-26
5. chen2023structuralbasisfor pages 1-2
6. ferguson2021fibroblastgrowthfactor pages 5-7
7. sobhani2021targetingaberrantfgfr pages 2-3
8. klimaschewski2021fibroblastgrowthfactor pages 2-4
9. nguyen2024thecomplexityand pages 6-8
10. szybowska2021negativeregulationof pages 8-10
11. ornitz2022newdevelopmentsin pages 18-20
12. szybowska2021negativeregulationof pages 10-11
13. szybowska2021negativeregulationof pages 7-8
14. shalaeva2021structuralandfunctional pages 15-17
15. ferguson2021fibroblastgrowthfactor pages 2-3
16. nguyen2024thecomplexityand pages 4-6
17. liu2026fgffamilyin pages 6-8
18. margiotta2021allgoodthings pages 4-6
19. szybowska2021negativeregulationof pages 15-17
20. szybowska2021thecanonicalfgffgfr pages 2-4
21. liu2023fgfrfamiliesbiological pages 2-4
22. xie2020fgffgfrsignalingin pages 1-2
23. tome2023fibroblastgrowthfactor pages 2-4
24. liu2026fgffamilyin pages 3-4
25. chen2023structuralbasisfor pages 2-3
26. liu2026fgffamilyin pages 4-6
27. kopp2025proteomicanalysisreveals pages 21-23
28. kopp2025proteomicanalysisreveals pages 19-21
29. kopp2025proteomicanalysisreveals pages 16-19
30. zheng2022signalingpathwayand pages 1-2
31. tome2023fibroblastgrowthfactor pages 1-2
32. kopp2025proteomicanalysisreveals pages 23-25
33. FGFR Signaling Pathway Module
34. https://doi.org/10.3390/biom14121622,
35. https://doi.org/10.1038/s41392-020-00222-7,
36. https://doi.org/10.3390/cells10051201,
37. https://doi.org/10.1186/s43556-026-00429-0,
38. https://doi.org/10.1186/s12964-023-01284-0,
39. https://doi.org/10.3390/cells10061342,
40. https://doi.org/10.1002/wsbm.1549,
41. https://doi.org/10.1038/s41586-023-06155-9,
42. https://doi.org/10.3389/fchem.2022.860985,
43. https://doi.org/10.3390/cells10020293,
44. https://doi.org/10.3390/ijms22126342,
45. https://doi.org/10.1007/s12035-021-02367-0,
46. https://doi.org/10.1101/2025.09.23.678042,
47. https://doi.org/10.3390/cancers17010082,
48. https://doi.org/10.3390/genes12060788,
49. https://doi.org/10.1002/mco2.367,
50. https://doi.org/10.2478/ahem-2021-0024,