---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:11:40.110860'
end_time: '2026-06-28T19:39:03.649829'
duration_seconds: 1643.54
template_file: templates/module_research.md.j2
template_variables:
  module_title: Fc-gamma receptor signaling pathway module
  module_summary: Fc-gamma receptor signaling couples immune-complex binding to ITAM-containing
    receptor chains, SYK/BTK activation, PLC-gamma and PI3K branches, phagocytosis,
    and inflammatory effector functions.
  module_outline: "- Fc-gamma receptor signaling pathway\n  - 1. fcgamma receptor\
    \ engagement\n  - Fc-gamma receptor engagement\n    - Fc-gamma receptor IIA (molecular\
    \ player: FCGR2A)\n    - Fc-gamma receptor IIIA (molecular player: FCGR3A)\n \
    \   - Fc receptor gamma ITAM subunit (molecular player: FCER1G)\n  - 2. fcgamma\
    \ syk-btk activation\n  - SYK-BTK activation downstream of Fc-gamma receptors\n\
    \    - SYK tyrosine kinase (molecular player: SYK tyrosine kinase family/ortholog\
    \ group)\n    - BTK tyrosine kinase (molecular player: BTK tyrosine kinase family/ortholog\
    \ group)\n  - 3. fcgamma phagocytic output\n  - Fc-gamma phagocytic output\n \
    \   - PLCG2 effector (molecular player: PLCG2)\n    - PI3K gamma catalytic branch\
    \ (molecular player: PI3K gamma catalytic branch family/ortholog group)"
  module_connections: '- Fc-gamma receptor engagement causes SYK-BTK activation downstream
    of Fc-gamma receptors: The initiating event promotes fcgamma syk-btk activation.

    - SYK-BTK activation downstream of Fc-gamma receptors causes Fc-gamma phagocytic
    output: SYK-BTK activation downstream of Fc-gamma receptors leads to fcgamma phagocytic
    output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 3
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: fc_gamma_receptor_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: fc_gamma_receptor_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: fc_gamma_receptor_signaling-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: image-1.png
  path: fc_gamma_receptor_signaling-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: "Image artifact created (ID artifact-02): 'Fc\u03B3R Signaling Module'\
    \ ![Fc\u03B3R Signaling Module](artifact:artifact-02) Artifact IDs that may be\
    \ injected into the answe"
---

## Question

# Commissioned Review Brief

## Review Topic

Fc-gamma receptor signaling pathway module

## Working Scope

Fc-gamma receptor signaling couples immune-complex binding to ITAM-containing receptor chains, SYK/BTK activation, PLC-gamma and PI3K branches, phagocytosis, and inflammatory effector functions.

## Provisional Biological Outline

- Fc-gamma receptor signaling pathway
  - 1. fcgamma receptor engagement
  - Fc-gamma receptor engagement
    - Fc-gamma receptor IIA (molecular player: FCGR2A)
    - Fc-gamma receptor IIIA (molecular player: FCGR3A)
    - Fc receptor gamma ITAM subunit (molecular player: FCER1G)
  - 2. fcgamma syk-btk activation
  - SYK-BTK activation downstream of Fc-gamma receptors
    - SYK tyrosine kinase (molecular player: SYK tyrosine kinase family/ortholog group)
    - BTK tyrosine kinase (molecular player: BTK tyrosine kinase family/ortholog group)
  - 3. fcgamma phagocytic output
  - Fc-gamma phagocytic output
    - PLCG2 effector (molecular player: PLCG2)
    - PI3K gamma catalytic branch (molecular player: PI3K gamma catalytic branch family/ortholog group)

## Known Relationships Among Steps

- Fc-gamma receptor engagement causes SYK-BTK activation downstream of Fc-gamma receptors: The initiating event promotes fcgamma syk-btk activation.
- SYK-BTK activation downstream of Fc-gamma receptors causes Fc-gamma phagocytic output: SYK-BTK activation downstream of Fc-gamma receptors leads to fcgamma phagocytic output.

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

Fc-gamma receptor signaling pathway module

## Working Scope

Fc-gamma receptor signaling couples immune-complex binding to ITAM-containing receptor chains, SYK/BTK activation, PLC-gamma and PI3K branches, phagocytosis, and inflammatory effector functions.

## Provisional Biological Outline

- Fc-gamma receptor signaling pathway
  - 1. fcgamma receptor engagement
  - Fc-gamma receptor engagement
    - Fc-gamma receptor IIA (molecular player: FCGR2A)
    - Fc-gamma receptor IIIA (molecular player: FCGR3A)
    - Fc receptor gamma ITAM subunit (molecular player: FCER1G)
  - 2. fcgamma syk-btk activation
  - SYK-BTK activation downstream of Fc-gamma receptors
    - SYK tyrosine kinase (molecular player: SYK tyrosine kinase family/ortholog group)
    - BTK tyrosine kinase (molecular player: BTK tyrosine kinase family/ortholog group)
  - 3. fcgamma phagocytic output
  - Fc-gamma phagocytic output
    - PLCG2 effector (molecular player: PLCG2)
    - PI3K gamma catalytic branch (molecular player: PI3K gamma catalytic branch family/ortholog group)

## Known Relationships Among Steps

- Fc-gamma receptor engagement causes SYK-BTK activation downstream of Fc-gamma receptors: The initiating event promotes fcgamma syk-btk activation.
- SYK-BTK activation downstream of Fc-gamma receptors causes Fc-gamma phagocytic output: SYK-BTK activation downstream of Fc-gamma receptors leads to fcgamma phagocytic output.

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

# Fc-Gamma Receptor Signaling Pathway Module: A Mechanistic Review

## 1. Executive Summary

Fc-gamma receptor (FcγR) signaling constitutes a critical interface between humoral and innate immunity, translating the recognition of IgG-opsonized targets into phagocytic, cytotoxic, and inflammatory effector programs. The core signaling cascade proceeds through a conserved three-step logic: (i) immune complex engagement of activating FcγRs triggers receptor clustering and immunoreceptor tyrosine-based activation motif (ITAM) phosphorylation by Src-family kinases; (ii) phospho-ITAMs recruit and activate spleen tyrosine kinase (SYK), which together with Bruton's tyrosine kinase (BTK) amplifies the signal through PI3K-dependent lipid signaling; and (iii) downstream effectors including PLCγ2 and PI3K generate second messengers (DAG, IP3, PIP3) that drive calcium mobilization, cytoskeletal remodeling, NADPH oxidase activation, and transcription factor engagement, collectively producing phagocytosis, reactive oxygen species (ROS) production, antibody-dependent cellular cytotoxicity (ADCC), and inflammatory cytokine release (delidakis2022improvingantibodytherapeutics pages 7-9, delidakis2022improvingantibodytherapeutics pages 6-7, uribequerol2020phagocytosisourcurrent pages 5-6). This review examines the boundaries, core mechanism, variation, evolutionary context, constraints, and unresolved questions surrounding this signaling module.

The following diagram illustrates the three-tier organization of the pathway:

![FcγR Signaling Module](artifact:artifact-02)

*Image: Scientific schematic of the Fc-gamma receptor signaling pathway organized as a vertical three-tier flowchart from receptor engagement to SYK-BTK activation and downstream phagocytic and inflammatory outputs. Activating branches are shown in green and inhibitory FcγRIIb-SHIP1 signaling in red.*

## 2. Definition and Biological Boundaries

### 2.1 Scope of the System

The FcγR signaling pathway module encompasses the events that begin with IgG immune complex binding to activating Fc-gamma receptors and terminate with the execution of effector functions including phagocytosis, degranulation, ROS production, ADCC, and cytokine secretion. The system's core is defined by three sequential signaling tiers: receptor engagement and ITAM phosphorylation, proximal kinase activation (SYK-BTK axis), and downstream effector output via PLCγ2 and PI3K branches (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 6-7, laassili2023fcreceptorsact pages 2-3).

The principal molecular players are summarized in the following table:

| Component | Gene Symbol | Signaling Motif/Function | Cell Type Expression | Key Role in Pathway |
|---|---|---|---|---|
| FcγRIIA | **FCGR2A** | Activating Fcγ receptor with an intrinsic cytoplasmic ITAM-like motif | Monocytes, macrophages, neutrophils, platelets, dendritic cells; expression level varies by lineage and activation state (sepulvedadelgado2025acomprehensivereview pages 4-6, delidakis2022improvingantibodytherapeutics pages 9-11, sepulvedadelgado2025acomprehensivereview pages 8-10) | Binds IgG immune complexes, clusters at the membrane, and initiates Src-dependent ITAM phosphorylation leading to SYK recruitment, PI3K/BTK/PLCγ signaling, phagocytosis, ROS production, and inflammatory activation (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 6-7, roeser2023bcellsand pages 6-6) |
| FcγRIIIA | **FCGR3A** | Activating Fcγ receptor lacking its own signaling motif; signals through associated FcRγ ITAM-containing chain | NK cells, monocytes, macrophages, dendritic cells; major receptor for ADCC in NK cells (sepulvedadelgado2025acomprehensivereview pages 4-6, sepulvedadelgado2024acomprehensivereview pages 5-7, sepulvedadelgado2025acomprehensivereview pages 8-10) | Couples immune-complex recognition to FcRγ-dependent ITAM signaling, supporting cytotoxicity in NK cells and inflammatory/phagocytic signaling in myeloid cells (sepulvedadelgado2025acomprehensivereview pages 4-6, delidakis2022improvingantibodytherapeutics pages 7-9, sepulvedadelgado2024acomprehensivereview pages 5-7) |
| FcγRIIb | **FCGR2B** | Inhibitory Fcγ receptor bearing an ITIM | B cells, monocytes/macrophages, some other leukocyte populations; expression can be context- and subset-dependent (sepulvedadelgado2025acomprehensivereview pages 4-6, weerawarna2023lynkinasestructure pages 7-8, sepulvedadelgado2025acomprehensivereview pages 10-12) | Recruits SHIP phosphatases after ITIM phosphorylation, counteracting PI3K-PIP3 accumulation and thereby restraining BTK, PLCγ, Ca²⁺ signaling, and cellular activation (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9, weerawarna2023lynkinasestructure pages 7-8) |
| FcRγ chain | **FCER1G** | Common ITAM-containing signaling adaptor subunit for several activating Fc receptors | Associated with FcγRIIIA and other FcR-family receptors in myeloid and NK cells (sepulvedadelgado2025acomprehensivereview pages 4-6, delidakis2022improvingantibodytherapeutics pages 7-9) | Provides the canonical ITAM that is phosphorylated by Src-family kinases, enabling recruitment of SYK and assembly of proximal Fc receptor signaling complexes (sepulvedadelgado2025acomprehensivereview pages 4-6, delidakis2022improvingantibodytherapeutics pages 7-9, laassili2023fcreceptorsact pages 2-3) |
| Lyn/Src-family kinases | **LYN** (representative; with other Src-family kinases such as HCK/FGR/LCK depending on cell type) | Proximal tyrosine kinases that phosphorylate ITAMs and can also phosphorylate inhibitory motifs; context-dependent activating and inhibitory roles | Broadly used in myeloid cells and other hematopoietic cells; exact family-member usage varies by cell type (uribequerol2020phagocytosisourcurrent pages 5-6, weerawarna2023lynkinasestructure pages 7-8, l’estrangestranieri2024thedualisticrole pages 12-12) | Execute the first obligatory enzymatic step after receptor clustering by phosphorylating ITAM tyrosines; also contribute to inhibitory signaling, including ITAMi and FcγRIIb-linked restraint (uribequerol2020phagocytosisourcurrent pages 5-6, delidakis2022improvingantibodytherapeutics pages 7-9, weerawarna2023lynkinasestructure pages 7-8) |
| SYK tyrosine kinase | **SYK** | SH2-domain tyrosine kinase recruited to phospho-ITAMs | Broadly expressed in myeloid cells and other hematopoietic lineages; central proximal kinase downstream of FcγRs (sepulvedadelgado2024acomprehensivereview pages 10-12, uribequerol2020phagocytosisourcurrent pages 5-6, OpenTargets Search: -SYK,BTK,PLCG2,FCGR2A,FCGR3A) | Binds phosphorylated ITAMs and propagates signaling to PI3K, PLCγ, LAT/adaptor modules, and cytoskeletal pathways, making it a core hub for phagocytosis and inflammatory outputs (sepulvedadelgado2024acomprehensivereview pages 10-12, uribequerol2020phagocytosisourcurrent pages 5-6, laassili2023fcreceptorsact pages 2-3) |
| BTK tyrosine kinase | **BTK** | TEC-family kinase recruited downstream of PI3K-generated PIP3 | Best known in B cells but also active in monocytes/macrophages and other myeloid cells (sepulvedadelgado2024acomprehensivereview pages 10-12, jiang2024theimmunomodulatorymechanisms pages 9-10, jiang2024theimmunomodulatorymechanisms pages 7-9) | Functions downstream of PI3K to amplify FcγR signaling, support PLCγ activation, cytoskeletal remodeling, and cytokine production; BTK inhibition dampens FcγR-driven inflammatory responses (sepulvedadelgado2024acomprehensivereview pages 10-12, jiang2024theimmunomodulatorymechanisms pages 9-10, jiang2024theimmunomodulatorymechanisms pages 7-9) |
| PLCγ2 | **PLCG2** | Phospholipase that hydrolyzes PIP2 to DAG and IP3 | Hematopoietic cells including myeloid cells and microglia; principal PLCγ isoform in many FcR pathways (sepulvedadelgado2024acomprehensivereview pages 10-12, li2022plcγ2impactsmicrogliarelated pages 2-4, li2022plcγ2impactsmicrogliarelated pages 7-9) | Generates DAG and IP3 downstream of SYK/BTK, driving Ca²⁺ mobilization, PKC activation, oxidative burst, and phagocytic/inflammatory effector programs (sepulvedadelgado2024acomprehensivereview pages 10-12, li2022plcγ2impactsmicrogliarelated pages 2-4, uribequerol2020phagocytosisourcurrent pages 5-6) |
| PI3K | **PIK3CG** (PI3Kγ branch emphasized in phagocytes; broader class I PI3Ks also implicated) | Lipid kinase that converts PIP2 to PIP3 at the membrane/phagocytic cup | Widely deployed in phagocytes downstream of FcγRs (uribequerol2020phagocytosisourcurrent pages 5-6, delidakis2022improvingantibodytherapeutics pages 7-9) | Produces PIP3 to recruit PH-domain proteins such as BTK and other effectors, organizes signaling at the phagocytic cup, and supports Rac/myosin-dependent engulfment and cup closure (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9, uribequerol2020phagocytosisourcurrent pages 5-6) |
| SHIP1 | **INPP5D** | 5-phosphatase that opposes PI3K by converting PIP3 to PI(3,4)P2 | Predominantly hematopoietic cells, including myeloid cells and B cells (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9, weerawarna2023lynkinasestructure pages 7-8) | Negative regulator that dampens FcγR signaling downstream of inhibitory receptors or inhibitory ITAM configurations, limiting BTK/PLCγ activation and setting activation thresholds (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9, weerawarna2023lynkinasestructure pages 7-8) |


*Table: This table summarizes the principal receptors, kinases, adaptors, and lipid-signaling enzymes that define the Fc-gamma receptor signaling module. It highlights how activating and inhibitory arms are organized across receptor engagement, proximal kinase activation, and downstream phagocytic and inflammatory outputs.*

### 2.2 Boundaries and Distinctions

Several neighboring pathways share molecular components with FcγR signaling but should be treated as distinct systems. The B cell receptor (BCR) signaling cascade employs the same SYK-BTK-PLCγ2 axis but is initiated by antigen binding to surface immunoglobulin rather than by immune complex engagement of FcγRs (delidakis2022improvingantibodytherapeutics pages 6-7). Similarly, the T cell receptor (TCR) pathway uses the paralogous kinase ZAP-70 rather than SYK, although the ITAM-based logic is conserved (delidakis2022improvingantibodytherapeutics pages 6-7, OpenTargets Search: -SYK,BTK,PLCG2,FCGR2A,FCGR3A). TREM2-DAP12 signaling in microglia also converges on SYK and PLCγ2 but is triggered by lipid ligands rather than IgG, and its biological context (neurodegeneration, microglial homeostasis) is fundamentally different (li2022plcγ2impactsmicrogliarelated pages 2-4). Complement receptor-mediated phagocytosis, while functionally similar to FcγR-driven phagocytosis, uses distinct signaling intermediates and should not be conflated with the ITAM-SYK pathway described here (uribequerol2020phagocytosisourcurrent pages 5-6).

The inhibitory receptor FcγRIIb, which bears an ITIM rather than an ITAM, is best understood as a regulatory counterpart to the activating FcγR module. Its signaling through SHIP phosphatases (INPP5D/SHIP1, INPPL1/SHIP2) opposes PI3K-generated PIP3 accumulation and thereby modulates the activating pathway's output, but its recruitment and signal transduction logic are mechanistically distinct (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9, weerawarna2023lynkinasestructure pages 7-8).

## 3. Mechanistic Overview

### 3.1 Step 1: Fc-Gamma Receptor Engagement

The pathway is initiated when multivalent IgG immune complexes bind to and cluster activating FcγRs on the surface of phagocytes, NK cells, or other effector cells. Two architecturally distinct receptor types can initiate this signal. FcγRIIA (encoded by *FCGR2A*) possesses an intrinsic ITAM-like motif in its own cytoplasmic tail, enabling direct signal transduction without accessory subunits (sepulvedadelgado2025acomprehensivereview pages 4-6, delidakis2022improvingantibodytherapeutics pages 7-9). In contrast, FcγRIIIA (encoded by *FCGR3A*) lacks intrinsic signaling capacity and instead associates with the FcRγ common chain (encoded by *FCER1G*), which provides the canonical ITAM required for downstream signaling (sepulvedadelgado2025acomprehensivereview pages 4-6, sepulvedadelgado2024acomprehensivereview pages 5-7). The high-affinity receptor FcγRI also signals through FcRγ, but it normally binds monomeric IgG and is constitutively internalized without triggering ITAM signaling; cross-linking by multivalent immune complexes is required for productive activation (delidakis2022improvingantibodytherapeutics pages 9-11).

Receptor clustering is obligatory for signal initiation. Upon clustering, Src-family kinases—principally Lyn, Hck, and Fgr in myeloid cells—phosphorylate the two tyrosine residues within each ITAM motif (uribequerol2020phagocytosisourcurrent pages 5-6, vikar2026tyrosinekinasesignaling pages 6-7). This dual phosphorylation is critical: incomplete (mono-)phosphorylation instead triggers inhibitory ITAM signaling (ITAMi), which recruits SHP-1 phosphatase and suppresses activation, thereby setting a threshold for immune activation (delidakis2022improvingantibodytherapeutics pages 7-9).

### 3.2 Step 2: SYK-BTK Kinase Activation

Doubly phosphorylated ITAMs serve as high-affinity docking sites for the tandem SH2 domains of SYK, which binds and becomes catalytically active upon recruitment (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 6-7, uribequerol2020phagocytosisourcurrent pages 5-6). SYK is the obligate proximal kinase in this cascade; its genetic ablation or pharmacological inhibition (e.g., by fostamatinib) abolishes virtually all downstream effector outputs (OpenTargets Search: -SYK,BTK,PLCG2,FCGR2A,FCGR3A). Once active, SYK phosphorylates multiple substrates including the adaptor protein LAT, PI3K regulatory subunits, PLCγ2, and the guanine nucleotide exchange factor Vav (delidakis2022improvingantibodytherapeutics pages 6-7, uribequerol2020phagocytosisourcurrent pages 5-6).

PI3K, activated by SYK, converts the membrane lipid PIP2 to PIP3, which acts as a critical membrane-localized second messenger. PIP3 recruits pleckstrin homology (PH) domain-containing proteins to the membrane, most notably BTK (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9, delidakis2022improvingantibodytherapeutics pages 6-7). BTK is a TEC-family tyrosine kinase that amplifies signaling by further phosphorylating and activating PLCγ2. BTK also contributes to cytoskeletal remodeling through activation of small GTPases Rho and Rac (sepulvedadelgado2024acomprehensivereview pages 10-12). Pharmacological BTK inhibition (e.g., by ibrutinib, acalabrutinib, or the selective inhibitor CGI1746) abolishes FcγRIII-induced production of inflammatory cytokines including TNF-α, IL-1β, and IL-6 in macrophages, confirming BTK's functional importance in myeloid FcγR signaling (jiang2024theimmunomodulatorymechanisms pages 9-10, jiang2024theimmunomodulatorymechanisms pages 7-9).

### 3.3 Step 3: Phagocytic and Inflammatory Output

The convergent output of the SYK-BTK-PI3K axis is mediated primarily through two effector branches:

**PLCγ2 branch:** Activated PLCγ2 hydrolyzes membrane PIP2 into two second messengers—diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3). IP3 binds to IP3 receptors on the endoplasmic reticulum, triggering rapid Ca²⁺ release into the cytoplasm. DAG activates protein kinase C (PKC), which in turn stimulates the NADPH oxidase complex for ROS production and engages the MEK-ERK signaling cascade (sepulvedadelgado2024acomprehensivereview pages 10-12, uribequerol2020phagocytosisourcurrent pages 5-6). Together, Ca²⁺ flux and PKC activation drive transcription factor activation (NFκB, NFAT, AP-1), inflammatory cytokine gene expression, and degranulation (delidakis2022improvingantibodytherapeutics pages 7-9).

**PI3K branch:** PIP3 accumulation at the inner leaflet of the phagocytic cup is essential for phagosome formation. PIP3 recruits and activates the GTPase Rac, which drives actin polymerization and cytoskeletal remodeling required for pseudopod extension around the target particle. PIP3 also regulates myosin contractility and recruits additional FcγRs to the advancing membrane protrusion (uribequerol2020phagocytosisourcurrent pages 5-6, delidakis2022improvingantibodytherapeutics pages 7-9). Closure of the phagocytic cup requires a PI3K-dependent membrane fusion process that ultimately forms the mature phagosome (delidakis2022improvingantibodytherapeutics pages 7-9).

The balance between activating and inhibitory signals determines the magnitude and nature of the cellular response. FcγRIIb, when co-engaged with activating receptors, recruits SHIP1/SHIP2 phosphatases that hydrolyze PIP3 back to PI(3,4)P2, effectively blocking BTK membrane recruitment, PLCγ activation, and Ca²⁺ mobilization (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9, weerawarna2023lynkinasestructure pages 7-8).

## 4. Major Molecular Players and Active Assemblies

### 4.1 Receptor Layer

Human activating FcγRs include FcγRI (CD64), FcγRIIA (CD32A), FcγRIIC (CD32C), FcγRIIIA (CD16A), and FcγRIIIb (CD16B). Their expression patterns vary substantially across cell types: neutrophils express high levels of FcγRIIIb and moderate FcγRIIA; monocytes and macrophages express FcγRI, FcγRIIA, and FcγRIIIA; NK cells express primarily FcγRIIIA; and platelets exclusively express FcγRIIA (delidakis2022improvingantibodytherapeutics pages 9-11, sepulvedadelgado2024acomprehensivereview pages 7-9, sepulvedadelgado2025acomprehensivereview pages 8-10). FcγRIIIb is unique as a GPI-anchored receptor lacking intracellular signaling domains, yet it enhances FcγRIIA-mediated signaling in neutrophils through calcium influx and cooperative receptor dynamics (sepulvedadelgado2024acomprehensivereview pages 9-10, sepulvedadelgado2024acomprehensivereview pages 5-7).

### 4.2 Kinase Cascade

The kinase cascade follows a strict hierarchical order: Src-family kinases (obligatory initiators) → SYK (obligatory proximal hub) → PI3K (conditional amplifier) → BTK (conditional amplifier of PLCγ2) (delidakis2022improvingantibodytherapeutics pages 6-7, uribequerol2020phagocytosisourcurrent pages 5-6). SYK is the non-redundant node; BTK provides amplification but is not absolutely required for all outputs, as some SYK substrates (including PLCγ2 itself) can be phosphorylated directly by SYK (uribequerol2020phagocytosisourcurrent pages 5-6).

### 4.3 Effector Layer

PLCγ2 is the principal phospholipase isoform in hematopoietic cells downstream of FcγRs, while PLCγ1 predominates in T cells and non-hematopoietic contexts (li2022plcγ2impactsmicrogliarelated pages 2-4). The PLCG2 P522R variant, a modest gain-of-function allele (~2–3-fold increased activity), is associated with reduced Alzheimer's disease risk and enhanced microglial phagocytic function, while stronger hypermorphic mutations (S707Y, ~120-fold; L845F, ~60-fold) paradoxically impair phagocytosis and cause immune dysregulation including PLAID/APLAID syndromes and resistance to BTK inhibitors in CLL (tsai2026plcg2signalingand pages 4-5, tsai2026plcg2signalingand pages 1-2, tsai2026plcg2signalingand pages 2-4, li2022plcγ2impactsmicrogliarelated pages 12-12).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Evolutionary Origins

The FCGR gene family originated in the common ancestor of bony fish, coinciding with the emergence of IgG and the adaptive immune system (frampton2024fcgammareceptors pages 1-2). FcR homologs are found in bony fish but not cartilaginous fish, placing the origin of the receptor family after the jawed vertebrate divergence (delidakis2022improvingantibodytherapeutics pages 3-4). The FcγR family as currently defined—with its characteristic Ig-like extracellular domains and ITAM-based signaling—is restricted to mammals, though the intracellular signaling logic (ITAM → SYK) is ancient and shared with many immunoreceptor families across vertebrates (delidakis2022improvingantibodytherapeutics pages 3-4).

Low-affinity FcγR genes appear to have emerged first in mammalian evolution; opossum genomes (~130 million years ago) contain two-domain FcγR genes but lack three-domain (high-affinity) receptors (frampton2024fcgammareceptors pages 1-2). The subsequent evolution of the FCGR locus has been shaped by segmental duplication, with humans acquiring substantially greater receptor diversity than mice through species-specific duplication events (frampton2024fcgammareceptors pages 5-6).

### 5.2 Human versus Mouse Divergence

A critical consideration for the field is that the human and mouse FcγR systems are not orthologous point-for-point. The following table summarizes key differences:

| Feature | Human System | Mouse System | Implication for Cross-Species Studies |
|---|---|---|---|
| Number of **FCGR** genes | Humans have **8 FCGR genes** and a more complex low-affinity receptor locus shaped by segmental duplication and copy-number variation (frampton2024fcgammareceptors pages 5-6, delidakis2022improvingantibodytherapeutics pages 3-4) | Mice have a **simpler FcγR organization** with fewer receptor genes and less direct one-to-one correspondence to the human locus (frampton2024fcgammareceptors pages 5-6) | Mouse models cannot be assumed to recapitulate the full combinatorial diversity, dosage effects, or haplotypic complexity of the human **FCGR** locus (frampton2024fcgammareceptors pages 5-6, delidakis2022improvingantibodytherapeutics pages 3-4) |
| Activating receptors present | Activating receptors include **FcγRI, FcγRIIA, FcγRIIc, FcγRIIIA, and FcγRIIIb**; signaling is split between intrinsic-ITAM and FcRγ-dependent architectures (frampton2024fcgammareceptors pages 5-6, sepulvedadelgado2025acomprehensivereview pages 4-6, delidakis2022improvingantibodytherapeutics pages 7-9) | Activating receptors include **FcγRI, FcγRIII, and FcγRIV**; receptor repertoire differs qualitatively from humans (frampton2024fcgammareceptors pages 5-6) | Functional studies of “activating FcγR signaling” are not directly portable across species because the activating receptor set itself differs (frampton2024fcgammareceptors pages 5-6) |
| Intrinsic ITAM receptor | **FcγRIIA** contains its own intracellular **ITAM-like signaling motif** and can signal without FcRγ as the signaling subunit (sepulvedadelgado2025acomprehensivereview pages 4-6, delidakis2022improvingantibodytherapeutics pages 7-9) | **No true mouse ortholog of human FcγRIIA** is present (frampton2024fcgammareceptors pages 5-6) | Human pathways driven by intrinsic-receptor ITAM signaling, especially platelet and myeloid **FcγRIIA** biology, are poorly modeled in wild-type mice (frampton2024fcgammareceptors pages 5-6, sepulvedadelgado2025acomprehensivereview pages 4-6) |
| GPI-anchored receptor | Humans uniquely express **FcγRIIIb**, a **GPI-anchored** receptor highly expressed on neutrophils and lacking a classical intracellular signaling tail (sepulvedadelgado2024acomprehensivereview pages 5-7) | **No mouse equivalent of FcγRIIIb** is present (frampton2024fcgammareceptors pages 5-6, delidakis2022improvingantibodytherapeutics pages 3-4) | Neutrophil signaling, receptor cooperation, and NET/phagocytosis phenotypes involving **FcγRIIIb** in humans cannot be inferred directly from mouse neutrophil studies (sepulvedadelgado2024acomprehensivereview pages 5-7, sepulvedadelgado2025acomprehensivereview pages 10-12) |
| Inhibitory receptor | Humans have a single canonical inhibitory receptor, **FcγRIIb**, bearing an **ITIM** (sepulvedadelgado2025acomprehensivereview pages 4-6) | Mice likewise have a single inhibitory **FcγRIIb** receptor (frampton2024fcgammareceptors pages 5-6) | The inhibitory arm is the most conceptually conserved part of the FcγR system, but its quantitative balance against activating receptors still differs because the activating repertoires are different (frampton2024fcgammareceptors pages 5-6, sepulvedadelgado2025acomprehensivereview pages 4-6) |
| Mouse-specific receptor **FcγRIV** | **No human ortholog of FcγRIV** has been identified (frampton2024fcgammareceptors pages 5-6) | Mice express **FcγRIV**, which contributes to activating FcγR biology in myeloid cells (frampton2024fcgammareceptors pages 5-6) | Murine phenotypes attributed to activating FcγRs may depend substantially on **FcγRIV**, creating species-specific signaling logic without a direct human counterpart (frampton2024fcgammareceptors pages 5-6) |
| Genomic chromosomal location | Human **FCGR** genes are concentrated at **chromosome 1q23**, with broader homology to other Fc receptor regions and substantial locus complexity (frampton2024fcgammareceptors pages 5-6) | Mouse FcγR genes are distributed on **chromosomes 1 and 3**, corresponding broadly to human **1q23** and **1q21** syntenic relationships (frampton2024fcgammareceptors pages 5-6) | Comparative genetics and transgenic modeling must account for different locus architecture, linkage, and duplication history, not just receptor names (frampton2024fcgammareceptors pages 5-6, frampton2024fcgammareceptors pages 1-2) |


*Table: This table compares the human and mouse Fc-gamma receptor systems with emphasis on receptor repertoire, signaling architecture, and genomic organization. It is useful for interpreting why FcγR signaling results from mouse models may not translate directly to human biology.*

These differences mean that mouse models cannot fully recapitulate human FcγR signaling biology, particularly for FcγRIIA-dependent processes (e.g., platelet activation in heparin-induced thrombocytopenia) and FcγRIIIb-dependent neutrophil functions (frampton2024fcgammareceptors pages 5-6, delidakis2022improvingantibodytherapeutics pages 3-4).

### 5.3 Cell-Type Variation

FcγR signaling outcomes differ substantially across cell types owing to differential receptor expression and co-stimulatory context. In monocytes, FcγRI stimulation triggers transient calcium mobilization via phospholipase D, while FcγRIIA produces prolonged calcium influx via PLCγ; this distinction is lost upon differentiation into macrophages or dendritic cells (delidakis2022improvingantibodytherapeutics pages 9-11). Neutrophils show unique FcγRIIIb-driven signaling in which ERK phosphorylation occurs in the nucleus rather than the cytosol, enabling a shift from a phagocytic to a NETotic phenotype (sepulvedadelgado2025acomprehensivereview pages 10-12). Tissue-resident macrophages express different FcγR levels than splenic or bone-marrow macrophages, with red pulp macrophages showing high FcγRIIa/FcγRIIIa expression that makes them efficient at IgG-opsonized erythrocyte phagocytosis (delidakis2022improvingantibodytherapeutics pages 6-7). FcγRI-mediated antigen internalization leads to more efficient antigen presentation to CD4⁺ T cells compared with FcγRIIA-mediated uptake, suggesting that different receptors route cargo to distinct intracellular processing compartments (delidakis2022improvingantibodytherapeutics pages 9-11).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Ordering

The signaling cascade is strictly ordered: receptor clustering must precede ITAM phosphorylation, which must precede SYK recruitment, which must precede PI3K/BTK activation and PLCγ2 engagement (delidakis2022improvingantibodytherapeutics pages 6-7, uribequerol2020phagocytosisourcurrent pages 5-6). PIP3 generation by PI3K is required before BTK can be recruited to the membrane via its PH domain, establishing a dependency between the lipid kinase and the tyrosine kinase amplification step (sepulvedadelgado2024acomprehensivereview pages 10-12, delidakis2022improvingantibodytherapeutics pages 7-9).

### 6.2 Mutual Exclusivity and Threshold Effects

Activating and inhibitory ITAM signaling (ITAMi) are mutually exclusive outcomes determined by the degree of receptor clustering. High-valency immune complexes produce full ITAM phosphorylation and SYK recruitment; low-valency or monomeric ligand engagement produces incomplete phosphorylation that recruits SHP-1 instead of SYK, actively suppressing downstream signaling (delidakis2022improvingantibodytherapeutics pages 7-9). This threshold mechanism is believed to maintain immune homeostasis and prevent inappropriate activation by circulating monomeric IgG.

### 6.3 Genetic Failure Modes

Loss-of-function mutations in *BTK* cause X-linked agammaglobulinemia, demonstrating the non-redundant role of BTK in BCR-dependent B cell development, while BTK inhibitors approved for CLL/ITP also impair macrophage phagocytosis and inflammatory cytokine production (OpenTargets Search: -SYK,BTK,PLCG2,FCGR2A,FCGR3A, jiang2024theimmunomodulatorymechanisms pages 9-10). SYK deficiency is associated with immunodeficiency with systemic inflammation (OMIM: immunodeficiency 82), confirming its essential role in ITAM signaling across multiple receptor systems (OpenTargets Search: -SYK,BTK,PLCG2,FCGR2A,FCGR3A). PLCG2 gain-of-function mutations cause a spectrum of immunological disease: moderate hyperactivity (P522R) is protective against Alzheimer's disease, while extreme hyperactivity (S707Y, R665W, L845F) causes PLAID/APLAID syndromes characterized by antibody deficiency, cold urticaria, and autoinflammation, paradoxically with impaired rather than enhanced immune effector function (tsai2026plcg2signalingand pages 4-5, tsai2026plcg2signalingand pages 1-2, li2022plcγ2impactsmicrogliarelated pages 12-12). This nonlinear dose-response underscores the importance of signaling calibration in this pathway.

### 6.4 Therapeutic Targeting

The clinical importance of the pathway is evidenced by FDA-approved therapeutics targeting its components. Fostamatinib (a SYK inhibitor) is approved for immune thrombocytopenia (ITP) and has been evaluated in Phase 3 trials for rheumatoid arthritis (OpenTargets Search: -SYK,BTK,PLCG2,FCGR2A,FCGR3A). BTK inhibitors (ibrutinib, acalabrutinib, zanubrutinib) are approved primarily for B cell malignancies but have demonstrated efficacy in FcγR-dependent autoimmune settings, including autoantibody-induced arthritis models where BTK inhibition abolishes FcγRIII-induced cytokine production (jiang2024theimmunomodulatorymechanisms pages 9-10, jiang2024theimmunomodulatorymechanisms pages 7-9).

## 7. Controversies and Open Questions

### 7.1 The ITAMi Paradox

The discovery that ITAM-containing receptors can transmit inhibitory signals under conditions of low clustering (ITAMi) remains incompletely understood. The precise molecular determinants that distinguish activating ITAM from ITAMi signaling—beyond simple phosphorylation stoichiometry—are unclear. Whether ITAMi plays a significant physiological role in vivo, beyond what has been demonstrated in vitro, is an active area of investigation (delidakis2022improvingantibodytherapeutics pages 7-9, l’estrangestranieri2024thedualisticrole pages 12-12).

### 7.2 FcγRI Function

The biological purpose of high-affinity FcγRI remains perplexing. Under steady-state conditions, FcγRI is saturated by circulating monomeric IgG and continuously internalized without productive signaling. How FcγRI transitions from a quiescent, monomeric-IgG-occupied state to a productive signaling state upon immune complex encounter, and why it produces different downstream signals (transient Ca²⁺ via phospholipase D rather than prolonged Ca²⁺ via PLCγ) compared to FcγRIIA, are unresolved (delidakis2022improvingantibodytherapeutics pages 9-11).

### 7.3 FcγRIIIb Signaling Mechanism

FcγRIIIb, as a GPI-anchored receptor, lacks a cytoplasmic signaling domain, yet it modulates neutrophil function. The mechanism by which it cooperates with FcγRIIA—and whether it signals through lateral membrane interactions with ITAM-bearing partners or via lipid raft-mediated signaling—remains incompletely defined. Notably, FcγRIIIb engagement produces nuclear rather than cytoplasmic ERK phosphorylation, an unusual signaling topology whose functional significance is unclear (sepulvedadelgado2024acomprehensivereview pages 9-10, sepulvedadelgado2024acomprehensivereview pages 5-7, sepulvedadelgado2025acomprehensivereview pages 10-12).

### 7.4 Integrated Receptor Signaling

Myeloid cells express multiple FcγRs simultaneously, yet studies typically examine individual receptors in isolation. The integrated signaling output from co-engagement of activating and inhibitory FcγRs, the role of receptor stoichiometry and spatial distribution, and the influence of lipid composition and immune synapse micro-organization on signal quality are poorly understood. Methodological challenges compound this issue: blocking antibodies can alter surface protein distribution, and agonistic anti-FcγR monoclonal antibodies activate receptors with different geometry than natural immune complexes (delidakis2022improvingantibodytherapeutics pages 7-9, delidakis2022improvingantibodytherapeutics pages 9-11).

### 7.5 PLCG2 Dose-Response Paradox

The observation that moderate PLCG2 gain-of-function (P522R, ~2-3-fold) enhances immune function and confers disease protection, while strong gain-of-function (S707Y, ~120-fold) paradoxically impairs phagocytosis and causes immune dysregulation, suggests a bell-shaped dose-response curve for PLCγ2 signaling. The molecular basis for this nonlinearity—whether it reflects substrate depletion, feedback inhibition, or qualitative changes in downstream signaling—is an important open question with therapeutic implications (tsai2026plcg2signalingand pages 4-5, tsai2026plcg2signalingand pages 1-2, tsai2026plcg2signalingand pages 2-4).

### 7.6 Species Extrapolation

The substantial differences between human and mouse FcγR repertoires (humans have FcγRIIA and FcγRIIIb with no mouse orthologs; mice have FcγRIV with no human ortholog) mean that many mechanistic conclusions drawn from mouse models may not directly apply to human biology. This is particularly relevant for therapeutic antibody development, where Fc engineering to optimize FcγR engagement requires human-relevant models (frampton2024fcgammareceptors pages 5-6, delidakis2022improvingantibodytherapeutics pages 3-4).

## 8. Key References

1. Sepúlveda-Delgado J, Llorente L, Hernández-Doño S. A Comprehensive Review of Fc Gamma Receptors and Their Role in Systemic Lupus Erythematosus. *Int J Mol Sci.* 2025;26:1851. doi:10.3390/ijms26051851
2. Delidakis G, Kim JE, George K, Georgiou G. Improving Antibody Therapeutics by Manipulating the Fc Domain. *Annu Rev Biomed Eng.* 2022;24:249-274. doi:10.1146/annurev-bioeng-082721-024500
3. Uribe-Querol E, Rosales C. Phagocytosis: Our Current Understanding of a Universal Biological Process. *Front Immunol.* 2020;11:1066. doi:10.3389/fimmu.2020.01066
4. Frampton S, et al. Fc gamma receptors: Their evolution, genomic architecture, genetic variation, and impact on human disease. *Immunol Rev.* 2024;328:65-97. doi:10.1111/imr.13401
5. Vikár S, Mócsai A. Tyrosine kinase signaling pathways as therapeutic targets in autoimmune subepidermal blistering skin diseases. *Front Immunol.* 2026;17. doi:10.3389/fimmu.2026.1767876
6. Laassili C, et al. Fc receptors act as innate immune receptors during infection? *Front Immunol.* 2023;14. doi:10.3389/fimmu.2023.1188497
7. Jiang Q, et al. The Immunomodulatory Mechanisms of BTK Inhibition in CLL and Beyond. *Cancers.* 2024;16:3574. doi:10.3390/cancers16213574
8. Weerawarna PM, Richardson TI. Lyn Kinase Structure, Regulation, and Involvement in Neurodegenerative Diseases. *Kinases Phosphatases.* 2023;1:23-38. doi:10.3390/kinasesphosphatases1010004
9. L'Estrange-Stranieri E, et al. The dualistic role of Lyn tyrosine kinase in immune cell signaling. *Front Immunol.* 2024;15. doi:10.3389/fimmu.2024.1395427
10. Tsai AP, et al. PLCG2 signaling and genetic resilience in Alzheimer's disease. *Mol Neurodegener.* 2026;21. doi:10.1186/s13024-026-00935-3
11. Li K, et al. PLCγ2 impacts microglia-related effectors revealing variants and pathways important in Alzheimer's disease. *Front Cell Dev Biol.* 2022;10. doi:10.3389/fcell.2022.999061
12. Castelo-Soccio L, et al. Protein kinases: drug targets for immunological disorders. *Nat Rev Immunol.* 2023;23:1-20. doi:10.1038/s41577-023-00877-7
13. Roeser A, Lazarus AH, Mahévas M. B cells and antibodies in refractory immune thrombocytopenia. *Br J Haematol.* 2023;203:43-53. doi:10.1111/bjh.18773

References

1. (delidakis2022improvingantibodytherapeutics pages 7-9): George Delidakis, Jin Eyun Kim, Katia George, and George Georgiou. Improving antibody therapeutics by manipulating the fc domain: immunological and structural considerations. Annual Review of Biomedical Engineering, 24:249-274, Jun 2022. URL: https://doi.org/10.1146/annurev-bioeng-082721-024500, doi:10.1146/annurev-bioeng-082721-024500. This article has 87 citations and is from a domain leading peer-reviewed journal.

2. (delidakis2022improvingantibodytherapeutics pages 6-7): George Delidakis, Jin Eyun Kim, Katia George, and George Georgiou. Improving antibody therapeutics by manipulating the fc domain: immunological and structural considerations. Annual Review of Biomedical Engineering, 24:249-274, Jun 2022. URL: https://doi.org/10.1146/annurev-bioeng-082721-024500, doi:10.1146/annurev-bioeng-082721-024500. This article has 87 citations and is from a domain leading peer-reviewed journal.

3. (uribequerol2020phagocytosisourcurrent pages 5-6): Eileen Uribe-Querol and Carlos Rosales. Phagocytosis: our current understanding of a universal biological process. Frontiers in Immunology, Jun 2020. URL: https://doi.org/10.3389/fimmu.2020.01066, doi:10.3389/fimmu.2020.01066. This article has 983 citations and is from a peer-reviewed journal.

4. (sepulvedadelgado2024acomprehensivereview pages 10-12): Jesús Sepúlveda-Delgado, Luis Llorente, and Susana Hernández-Doño. A comprehensive review of fc gamma receptors and their role in sle. Dec 2024. URL: https://doi.org/10.20944/preprints202412.1473.v1, doi:10.20944/preprints202412.1473.v1.

5. (laassili2023fcreceptorsact pages 2-3): Chaimaa Laassili, Fatiha Ben El Hend, Riad Benzidane, Loubna Oumeslakht, Abdel-Ilah Aziz, Rachid El Fatimy, Armand Bensussan, and Sanae Ben Mkaddem. Fc receptors act as innate immune receptors during infection? Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1188497, doi:10.3389/fimmu.2023.1188497. This article has 14 citations and is from a peer-reviewed journal.

6. (sepulvedadelgado2025acomprehensivereview pages 4-6): Jesús Sepúlveda-Delgado, Luis Llorente, and Susana Hernández-Doño. A comprehensive review of fc gamma receptors and their role in systemic lupus erythematosus. International Journal of Molecular Sciences, 26:1851, Feb 2025. URL: https://doi.org/10.3390/ijms26051851, doi:10.3390/ijms26051851. This article has 21 citations.

7. (delidakis2022improvingantibodytherapeutics pages 9-11): George Delidakis, Jin Eyun Kim, Katia George, and George Georgiou. Improving antibody therapeutics by manipulating the fc domain: immunological and structural considerations. Annual Review of Biomedical Engineering, 24:249-274, Jun 2022. URL: https://doi.org/10.1146/annurev-bioeng-082721-024500, doi:10.1146/annurev-bioeng-082721-024500. This article has 87 citations and is from a domain leading peer-reviewed journal.

8. (sepulvedadelgado2025acomprehensivereview pages 8-10): Jesús Sepúlveda-Delgado, Luis Llorente, and Susana Hernández-Doño. A comprehensive review of fc gamma receptors and their role in systemic lupus erythematosus. International Journal of Molecular Sciences, 26:1851, Feb 2025. URL: https://doi.org/10.3390/ijms26051851, doi:10.3390/ijms26051851. This article has 21 citations.

9. (roeser2023bcellsand pages 6-6): Anaïs Roeser, Alan H. Lazarus, and Matthieu Mahévas. B cells and antibodies in refractory immune thrombocytopenia. British Journal of Haematology, 203:43-53, Apr 2023. URL: https://doi.org/10.1111/bjh.18773, doi:10.1111/bjh.18773. This article has 31 citations and is from a domain leading peer-reviewed journal.

10. (sepulvedadelgado2024acomprehensivereview pages 5-7): Jesús Sepúlveda-Delgado, Luis Llorente, and Susana Hernández-Doño. A comprehensive review of fc gamma receptors and their role in sle. Dec 2024. URL: https://doi.org/10.20944/preprints202412.1473.v1, doi:10.20944/preprints202412.1473.v1.

11. (weerawarna2023lynkinasestructure pages 7-8): Pathum M. Weerawarna and Timothy I. Richardson. Lyn kinase structure, regulation, and involvement in neurodegenerative diseases: a mini review. Kinases and Phosphatases, 1:23-38, Jan 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010004, doi:10.3390/kinasesphosphatases1010004. This article has 18 citations.

12. (sepulvedadelgado2025acomprehensivereview pages 10-12): Jesús Sepúlveda-Delgado, Luis Llorente, and Susana Hernández-Doño. A comprehensive review of fc gamma receptors and their role in systemic lupus erythematosus. International Journal of Molecular Sciences, 26:1851, Feb 2025. URL: https://doi.org/10.3390/ijms26051851, doi:10.3390/ijms26051851. This article has 21 citations.

13. (l’estrangestranieri2024thedualisticrole pages 12-12): Elan L’Estrange-Stranieri, Timothy A. Gottschalk, Mark D. Wright, and Margaret L. Hibbs. The dualistic role of lyn tyrosine kinase in immune cell signaling: implications for systemic lupus erythematosus. Frontiers in Immunology, Jun 2024. URL: https://doi.org/10.3389/fimmu.2024.1395427, doi:10.3389/fimmu.2024.1395427. This article has 21 citations and is from a peer-reviewed journal.

14. (OpenTargets Search: -SYK,BTK,PLCG2,FCGR2A,FCGR3A): Open Targets Query (-SYK,BTK,PLCG2,FCGR2A,FCGR3A, 27 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

15. (jiang2024theimmunomodulatorymechanisms pages 9-10): Qu Jiang, Yayi Peng, Carmen Diana Herling, and Marco Herling. The immunomodulatory mechanisms of btk inhibition in cll and beyond. Cancers, 16:3574, Oct 2024. URL: https://doi.org/10.3390/cancers16213574, doi:10.3390/cancers16213574. This article has 17 citations.

16. (jiang2024theimmunomodulatorymechanisms pages 7-9): Qu Jiang, Yayi Peng, Carmen Diana Herling, and Marco Herling. The immunomodulatory mechanisms of btk inhibition in cll and beyond. Cancers, 16:3574, Oct 2024. URL: https://doi.org/10.3390/cancers16213574, doi:10.3390/cancers16213574. This article has 17 citations.

17. (li2022plcγ2impactsmicrogliarelated pages 2-4): Kezhong Li, Beibei Ran, Yu Wang, Lulu Liu, and Wei-dong Li. Plcγ2 impacts microglia-related effectors revealing variants and pathways important in alzheimer’s disease. Frontiers in Cell and Developmental Biology, Sep 2022. URL: https://doi.org/10.3389/fcell.2022.999061, doi:10.3389/fcell.2022.999061. This article has 22 citations.

18. (li2022plcγ2impactsmicrogliarelated pages 7-9): Kezhong Li, Beibei Ran, Yu Wang, Lulu Liu, and Wei-dong Li. Plcγ2 impacts microglia-related effectors revealing variants and pathways important in alzheimer’s disease. Frontiers in Cell and Developmental Biology, Sep 2022. URL: https://doi.org/10.3389/fcell.2022.999061, doi:10.3389/fcell.2022.999061. This article has 22 citations.

19. (vikar2026tyrosinekinasesignaling pages 6-7): Simon Vikár and Attila Mócsai. Tyrosine kinase signaling pathways as therapeutic targets in autoimmune subepidermal blistering skin diseases (pemphigoid diseases). Frontiers in Immunology, Mar 2026. URL: https://doi.org/10.3389/fimmu.2026.1767876, doi:10.3389/fimmu.2026.1767876. This article has 0 citations and is from a peer-reviewed journal.

20. (sepulvedadelgado2024acomprehensivereview pages 7-9): Jesús Sepúlveda-Delgado, Luis Llorente, and Susana Hernández-Doño. A comprehensive review of fc gamma receptors and their role in sle. Dec 2024. URL: https://doi.org/10.20944/preprints202412.1473.v1, doi:10.20944/preprints202412.1473.v1.

21. (sepulvedadelgado2024acomprehensivereview pages 9-10): Jesús Sepúlveda-Delgado, Luis Llorente, and Susana Hernández-Doño. A comprehensive review of fc gamma receptors and their role in sle. Dec 2024. URL: https://doi.org/10.20944/preprints202412.1473.v1, doi:10.20944/preprints202412.1473.v1.

22. (tsai2026plcg2signalingand pages 4-5): Andy P. Tsai, Amara K. Martin, Andrew Mi, Ava E. Yeh, Eduardo Ramirez Lopez, and Tony Wyss-Coray. Plcg2 signaling and genetic resilience in alzheimer’s disease. Molecular Neurodegeneration, Mar 2026. URL: https://doi.org/10.1186/s13024-026-00935-3, doi:10.1186/s13024-026-00935-3. This article has 0 citations and is from a highest quality peer-reviewed journal.

23. (tsai2026plcg2signalingand pages 1-2): Andy P. Tsai, Amara K. Martin, Andrew Mi, Ava E. Yeh, Eduardo Ramirez Lopez, and Tony Wyss-Coray. Plcg2 signaling and genetic resilience in alzheimer’s disease. Molecular Neurodegeneration, Mar 2026. URL: https://doi.org/10.1186/s13024-026-00935-3, doi:10.1186/s13024-026-00935-3. This article has 0 citations and is from a highest quality peer-reviewed journal.

24. (tsai2026plcg2signalingand pages 2-4): Andy P. Tsai, Amara K. Martin, Andrew Mi, Ava E. Yeh, Eduardo Ramirez Lopez, and Tony Wyss-Coray. Plcg2 signaling and genetic resilience in alzheimer’s disease. Molecular Neurodegeneration, Mar 2026. URL: https://doi.org/10.1186/s13024-026-00935-3, doi:10.1186/s13024-026-00935-3. This article has 0 citations and is from a highest quality peer-reviewed journal.

25. (li2022plcγ2impactsmicrogliarelated pages 12-12): Kezhong Li, Beibei Ran, Yu Wang, Lulu Liu, and Wei-dong Li. Plcγ2 impacts microglia-related effectors revealing variants and pathways important in alzheimer’s disease. Frontiers in Cell and Developmental Biology, Sep 2022. URL: https://doi.org/10.3389/fcell.2022.999061, doi:10.3389/fcell.2022.999061. This article has 22 citations.

26. (frampton2024fcgammareceptors pages 1-2): Sarah Frampton, Rosanna Smith, Lili Ferson, Jane Gibson, Edward J. Hollox, Mark S. Cragg, and Jonathan C. Strefford. Fc gamma receptors: their evolution, genomic architecture, genetic variation, and impact on human disease. Immunological Reviews, 328:65-97, Sep 2024. URL: https://doi.org/10.1111/imr.13401, doi:10.1111/imr.13401. This article has 36 citations and is from a domain leading peer-reviewed journal.

27. (delidakis2022improvingantibodytherapeutics pages 3-4): George Delidakis, Jin Eyun Kim, Katia George, and George Georgiou. Improving antibody therapeutics by manipulating the fc domain: immunological and structural considerations. Annual Review of Biomedical Engineering, 24:249-274, Jun 2022. URL: https://doi.org/10.1146/annurev-bioeng-082721-024500, doi:10.1146/annurev-bioeng-082721-024500. This article has 87 citations and is from a domain leading peer-reviewed journal.

28. (frampton2024fcgammareceptors pages 5-6): Sarah Frampton, Rosanna Smith, Lili Ferson, Jane Gibson, Edward J. Hollox, Mark S. Cragg, and Jonathan C. Strefford. Fc gamma receptors: their evolution, genomic architecture, genetic variation, and impact on human disease. Immunological Reviews, 328:65-97, Sep 2024. URL: https://doi.org/10.1111/imr.13401, doi:10.1111/imr.13401. This article has 36 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](fc_gamma_receptor_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](fc_gamma_receptor_signaling-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](fc_gamma_receptor_signaling-deep-research-falcon_artifacts/artifact-02.md)
![Image artifact created (ID artifact-02): 'FcγR Signaling Module' ![FcγR Signaling Module](artifact:artifact-02) Artifact IDs that may be injected into the answe](fc_gamma_receptor_signaling-deep-research-falcon_artifacts/image-1.png)

## Citations

1. delidakis2022improvingantibodytherapeutics pages 6-7
2. uribequerol2020phagocytosisourcurrent pages 5-6
3. delidakis2022improvingantibodytherapeutics pages 9-11
4. delidakis2022improvingantibodytherapeutics pages 7-9
5. sepulvedadelgado2024acomprehensivereview pages 10-12
6. frampton2024fcgammareceptors pages 1-2
7. delidakis2022improvingantibodytherapeutics pages 3-4
8. frampton2024fcgammareceptors pages 5-6
9. sepulvedadelgado2024acomprehensivereview pages 5-7
10. sepulvedadelgado2025acomprehensivereview pages 4-6
11. sepulvedadelgado2025acomprehensivereview pages 10-12
12. laassili2023fcreceptorsact pages 2-3
13. sepulvedadelgado2025acomprehensivereview pages 8-10
14. roeser2023bcellsand pages 6-6
15. weerawarna2023lynkinasestructure pages 7-8
16. jiang2024theimmunomodulatorymechanisms pages 9-10
17. jiang2024theimmunomodulatorymechanisms pages 7-9
18. vikar2026tyrosinekinasesignaling pages 6-7
19. sepulvedadelgado2024acomprehensivereview pages 7-9
20. sepulvedadelgado2024acomprehensivereview pages 9-10
21. FcγR Signaling Module
22. https://doi.org/10.1146/annurev-bioeng-082721-024500,
23. https://doi.org/10.3389/fimmu.2020.01066,
24. https://doi.org/10.20944/preprints202412.1473.v1,
25. https://doi.org/10.3389/fimmu.2023.1188497,
26. https://doi.org/10.3390/ijms26051851,
27. https://doi.org/10.1111/bjh.18773,
28. https://doi.org/10.3390/kinasesphosphatases1010004,
29. https://doi.org/10.3389/fimmu.2024.1395427,
30. https://doi.org/10.3390/cancers16213574,
31. https://doi.org/10.3389/fcell.2022.999061,
32. https://doi.org/10.3389/fimmu.2026.1767876,
33. https://doi.org/10.1186/s13024-026-00935-3,
34. https://doi.org/10.1111/imr.13401,