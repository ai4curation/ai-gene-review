---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T18:04:39.066598'
end_time: '2026-06-28T18:30:13.794651'
duration_seconds: 1534.73
template_file: templates/module_research.md.j2
template_variables:
  module_title: IL-6 signaling pathway module
  module_summary: IL-6 engages IL6R and gp130/IL6ST receptor complexes, activating
    JAK kinases and STAT3-centered transcriptional programs that control inflammation,
    acute-phase responses, and differentiation.
  module_outline: "- IL-6 signaling pathway\n  - 1. il6 receptor engagement\n  - IL-6\
    \ receptor engagement\n    - IL-6 cytokine (molecular player: IL6)\n    - IL6\
    \ receptor alpha (molecular player: IL6 receptor alpha family/ortholog group)\n\
    \    - gp130 signal transducer (molecular player: gp130 signal transducer family/ortholog\
    \ group)\n  - 2. il6 jak activation\n  - IL-6 JAK activation\n    - JAK1 kinase\
    \ (molecular player: JAK1 kinase family/ortholog group)\n    - JAK2 kinase (molecular\
    \ player: JAK2 kinase family/ortholog group)\n  - 3. stat3 inflammatory output\n\
    \  - STAT3 inflammatory output\n    - STAT3 transcription factor (molecular player:\
    \ STAT3 transcription factor family/ortholog group)\n    - gp130 signaling scaffold\
    \ (molecular player: gp130 signaling scaffold family/ortholog group)"
  module_connections: '- IL-6 receptor engagement causes IL-6 JAK activation: The
    initiating event promotes il6 jak activation.

    - IL-6 JAK activation causes STAT3 inflammatory output: IL-6 JAK activation leads
    to stat3 inflammatory output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: il6_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: il6_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: il6_signaling-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Commissioned Review Brief

## Review Topic

IL-6 signaling pathway module

## Working Scope

IL-6 engages IL6R and gp130/IL6ST receptor complexes, activating JAK kinases and STAT3-centered transcriptional programs that control inflammation, acute-phase responses, and differentiation.

## Provisional Biological Outline

- IL-6 signaling pathway
  - 1. il6 receptor engagement
  - IL-6 receptor engagement
    - IL-6 cytokine (molecular player: IL6)
    - IL6 receptor alpha (molecular player: IL6 receptor alpha family/ortholog group)
    - gp130 signal transducer (molecular player: gp130 signal transducer family/ortholog group)
  - 2. il6 jak activation
  - IL-6 JAK activation
    - JAK1 kinase (molecular player: JAK1 kinase family/ortholog group)
    - JAK2 kinase (molecular player: JAK2 kinase family/ortholog group)
  - 3. stat3 inflammatory output
  - STAT3 inflammatory output
    - STAT3 transcription factor (molecular player: STAT3 transcription factor family/ortholog group)
    - gp130 signaling scaffold (molecular player: gp130 signaling scaffold family/ortholog group)

## Known Relationships Among Steps

- IL-6 receptor engagement causes IL-6 JAK activation: The initiating event promotes il6 jak activation.
- IL-6 JAK activation causes STAT3 inflammatory output: IL-6 JAK activation leads to stat3 inflammatory output.

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

IL-6 signaling pathway module

## Working Scope

IL-6 engages IL6R and gp130/IL6ST receptor complexes, activating JAK kinases and STAT3-centered transcriptional programs that control inflammation, acute-phase responses, and differentiation.

## Provisional Biological Outline

- IL-6 signaling pathway
  - 1. il6 receptor engagement
  - IL-6 receptor engagement
    - IL-6 cytokine (molecular player: IL6)
    - IL6 receptor alpha (molecular player: IL6 receptor alpha family/ortholog group)
    - gp130 signal transducer (molecular player: gp130 signal transducer family/ortholog group)
  - 2. il6 jak activation
  - IL-6 JAK activation
    - JAK1 kinase (molecular player: JAK1 kinase family/ortholog group)
    - JAK2 kinase (molecular player: JAK2 kinase family/ortholog group)
  - 3. stat3 inflammatory output
  - STAT3 inflammatory output
    - STAT3 transcription factor (molecular player: STAT3 transcription factor family/ortholog group)
    - gp130 signaling scaffold (molecular player: gp130 signaling scaffold family/ortholog group)

## Known Relationships Among Steps

- IL-6 receptor engagement causes IL-6 JAK activation: The initiating event promotes il6 jak activation.
- IL-6 JAK activation causes STAT3 inflammatory output: IL-6 JAK activation leads to stat3 inflammatory output.

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

# The IL-6 Signaling Pathway Module: A Review of Receptor Engagement, JAK Activation, and STAT3-Centered Transcriptional Programs

## 1. Executive Summary

Interleukin-6 (IL-6) is a pleiotropic cytokine that sits at the nexus of inflammation, immunity, acute-phase responses, and tissue homeostasis. IL-6 signals through a receptor system comprising the ligand-binding IL-6 receptor alpha (IL-6R/IL-6Rα) and the signal-transducing beta-receptor glycoprotein 130 (gp130, encoded by *IL6ST*), which upon dimerization activates Janus kinases (principally JAK1, with contributions from JAK2 and TYK2) and the transcription factor STAT3 (lv2024thejakstatpathway pages 11-12, sarapultsev2023jakstatsignalingin pages 4-5). Three mechanistically distinct signaling modes—classical signaling, trans-signaling, and cluster signaling—determine the cellular reach and functional outcome of IL-6 activity (rosejohn2023targetingil6transsignalling pages 1-2, schumertl2025il6signalingin pages 1-3). The pathway is negatively regulated by a rapid SOCS3-mediated feedback loop, by protein tyrosine phosphatases, and by PIAS proteins (millrine2022makingsenseof pages 5-6, xue2023evolvingcognitionof pages 2-3). Dysregulation of the IL-6/JAK/STAT3 axis underlies diverse pathologies from rheumatoid arthritis and inflammatory bowel disease to cancer and cytokine storm syndromes, and it is the target of multiple approved biologics and small-molecule inhibitors (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9). This review synthesizes the current mechanistic understanding of the pathway, its evolutionary context, variation across cell types, structural underpinnings, and outstanding controversies.

---

## 2. Definition and Biological Boundaries

### 2.1 What the system includes

The IL-6 signaling pathway module, as defined here, encompasses: (i) the IL-6 cytokine; (ii) the IL-6R alpha chain (membrane-bound and soluble forms); (iii) the shared signal-transducing receptor gp130/IL6ST; (iv) the receptor-associated JAK kinases (JAK1, JAK2, TYK2); (v) the STAT3 transcription factor as the principal downstream effector; and (vi) the intrinsic negative regulators SOCS3, PIAS proteins, and relevant phosphatases (schumertl2025il6signalingin pages 1-3, millrine2022makingsenseof pages 5-6, xue2023evolvingcognitionof pages 2-3).

### 2.2 What should be treated separately

Several neighboring systems are frequently confused with the IL-6/STAT3 module:

- **The broader IL-6 cytokine family**: gp130 serves as a shared signal-transducing receptor for IL-6, IL-11, IL-27, leukemia inhibitory factor (LIF), oncostatin M (OSM), ciliary neurotrophic factor (CNTF), cardiotrophin-1, and cardiotrophin-like cytokine factor 1 (CLCF1) (zhou2023structuralinsightsinto pages 1-1, metcalfe2023structuresofthe pages 1-2). Each uses gp130 in distinct heteromeric or homomeric complexes and engages partially overlapping but non-identical JAK/STAT programs. IL-11 signaling, for instance, also signals through gp130 homodimers but uses IL-11Rα rather than IL-6Rα and has distinct structural assembly dynamics (metcalfe2023structuresofthe pages 3-5, metcalfe2023structuresofthe pages 1-2).

- **Non-STAT3 outputs of gp130**: gp130 also signals through the SHP2/Ras/MAPK cascade and the PI3K/Akt pathway (schumertl2025il6signalingin pages 1-3, millrine2022makingsenseof pages 2-4). These are accessory branches of gp130 signaling, not core components of the IL-6/STAT3 module per se, although they contribute critically to pleiotropy.

- **STAT3 activation by non-IL-6 stimuli**: STAT3 can be activated by numerous cytokines (IL-10, IL-21, IL-23), growth factors (EGF, PDGF), and oncogenic kinases independent of IL-6 (sarapultsev2023jakstatsignalingin pages 4-5).

### 2.3 Competing definitions

The literature occasionally conflates the "IL-6 pathway" with the entire gp130 cytokine family signaling network. Strictly, the IL-6 pathway refers to signaling initiated specifically by the IL-6 cytokine, while the gp130 pathway encompasses all cytokines signaling through this shared receptor (millrine2022makingsenseof pages 5-6, millrine2022makingsenseof pages 1-2).

---

## 3. Mechanistic Overview

### 3.1 Step 1: IL-6 receptor engagement

IL-6 signaling is initiated when the four-helix bundle cytokine IL-6 binds to IL-6Rα at a site designated "Site I" (rosejohn2023targetingil6transsignalling pages 1-2, lv2024thejakstatpathway pages 11-12). This binary complex then engages gp130 at two additional sites: Site II (the interface between IL-6/IL-6Rα and the cytokine-binding homology region of gp130, domains D2–D3) and Site III (the interface between IL-6 and the Ig-like domain D1 of a second gp130 molecule) (rosejohn2023targetingil6transsignalling pages 4-5, lv2024thejakstatpathway pages 11-12). The mature signaling complex assembles with 2:2:2 stoichiometry (two molecules each of IL-6, IL-6Rα, and gp130) forming a hexameric assembly with two-fold symmetry (lv2024thejakstatpathway pages 11-12).

This receptor engagement step can occur through three distinct modes, summarized below.

| Mode | Receptor Configuration | Cell Types Affected | Key Biological Outcomes | Primary Pathological Associations |
|---|---|---|---|---|
| Classical signaling | IL-6 binds membrane-bound IL-6R (mIL-6R) on the target cell, then recruits and dimerizes gp130 to activate intracellular JAK/STAT, MAPK, PI3K, and related pathways (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5, schumertl2025il6signalingin pages 1-3) | Restricted to cells expressing mIL-6R, including hepatocytes, monocytes/macrophages, subsets of T cells, megakaryocytes, and some epithelial/mesenchymal populations (schumertl2025il6signalingin pages 3-5, millrine2022makingsenseof pages 4-5, schumertl2025il6signalingin pages 1-3) | Acute-phase response, tissue regeneration, immune homeostasis, and context-dependent anti-inflammatory or protective functions; can also contribute to acute inflammatory responses depending on tissue state (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5) | Less strongly linked to chronic pathology than trans-signaling; implicated in homeostatic and regenerative physiology and in some acute inflammatory settings (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5) |
| Trans-signaling | IL-6 first complexes with soluble IL-6R (sIL-6R), generated by proteolytic shedding or alternative splicing; the IL-6:sIL-6R complex then engages gp130 on cells that do not express mIL-6R (rosejohn2023targetingil6transsignalling pages 1-2, rosejohn2023targetingil6transsignalling pages 2-3, millrine2022makingsenseof pages 4-5, schumertl2025il6signalingin pages 1-3) | Broadly extends IL-6 responsiveness to most gp130-positive cells, including endothelial cells, fibroblasts, smooth muscle cells, and many stromal/parenchymal cells otherwise insensitive to classical signaling (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 2-3, millrine2022makingsenseof pages 4-5) | Predominantly pro-inflammatory signaling, amplification of leukocyte recruitment, vascular activation, tissue injury responses, and sustained inflammatory gene programs; may produce stronger or longer signaling in some settings (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, rosejohn2023targetingil6transsignalling pages 3-4, song2023experimentbasedcomputationalmodel pages 1-2) | Strongly associated with chronic inflammation, autoimmunity, inflammatory bowel disease, cancer-associated inflammation, endotheliopathy, and other disease-driving inflammatory states (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5) |
| Cluster signaling | A donor/transmitter cell presents a preformed membrane IL-6:mIL-6R complex to gp130 on a neighboring responder cell; signaling is therefore juxtacrine or trans-presented rather than mediated by free sIL-6R (rosejohn2023targetingil6transsignalling pages 1-2, rosejohn2023targetingil6transsignalling pages 2-3, millrine2022makingsenseof pages 4-5, schumertl2025il6signalingin pages 1-3) | Best described for dendritic cell-to-T cell communication, particularly gp130-expressing T cells receiving IL-6 cues from IL-6R-bearing antigen-presenting cells (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5) | Promotes STAT3 signaling in neighboring T cells and is required or important for generation of pathogenic TH17 responses in current models (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5) | Most closely linked to pathogenic TH17 biology and neuroinflammatory/autoimmune contexts such as multiple sclerosis models; currently less broadly established than classical or trans-signaling (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5) |


*Table: This table compares the three mechanistically distinct modes of IL-6 signaling by receptor architecture, cellular reach, biological output, and disease relevance. It is useful for separating the core IL-6 pathway from its context-specific signaling variants.*

In **classical signaling**, IL-6 binds membrane-bound IL-6R on cells that express it (hepatocytes, monocytes/macrophages, certain T cell subsets, megakaryocytes), immediately recruiting gp130 on the same cell surface (schumertl2025il6signalingin pages 3-5, rosejohn2023targetingil6transsignalling pages 1-2). In **trans-signaling**, IL-6 binds soluble IL-6R (sIL-6R)—generated by ADAM17-mediated ectodomain shedding or alternative mRNA splicing—and the resulting IL-6/sIL-6R complex activates gp130 on cells that lack membrane IL-6R, vastly expanding the range of IL-6-responsive cells (rosejohn2023targetingil6transsignalling pages 2-3, rosejohn2023targetingil6transsignalling pages 3-4). In **cluster signaling** (also termed trans-presentation), dendritic cells or other transmitter cells present preformed IL-6/membrane-IL-6R complexes to gp130-expressing T cells through juxtacrine contact, a mechanism critical for pathogenic Th17 cell generation (rosejohn2023targetingil6transsignalling pages 1-2, millrine2022makingsenseof pages 4-5).

### 3.2 Step 2: JAK activation

gp130 is a type I cytokine receptor that lacks intrinsic kinase activity. Instead, JAK kinases are constitutively associated with the intracellular domain of gp130 through conserved Box1 and Box2 motifs (lv2024thejakstatpathway pages 11-12, lv2024thejakstatpathway pages 12-15). The FERM-SH2 holodomain of JAKs binds these motifs: Box1 engages the F2 subdomain of JAK, while Box2 engages the SH2-like domain (lv2024thejakstatpathway pages 12-15). Cryo-EM structural studies have revealed that the six extracellular domains of gp130 (D1–D6) undergo a characteristic acute bend between D4 and D5 that brings the juxtamembrane D6 domains of the two gp130 molecules within approximately 19 Å of each other—close enough to enable JAK transphosphorylation (zhou2023structuralinsightsinto pages 1-1, lv2024thejakstatpathway pages 11-12). Upon cytokine-induced gp130 homodimerization, this proximity triggers transphosphorylation of receptor-associated JAKs, relieving autoinhibition of the kinase domain (lv2024thejakstatpathway pages 12-15).

JAK1 is considered the primary kinase for IL-6 signaling through gp130, with JAK2 and TYK2 serving as partner or accessory kinases (sarapultsev2023jakstatsignalingin pages 4-5). Activated JAKs phosphorylate specific tyrosine residues on the gp130 intracellular domain, creating phosphotyrosine docking sites for SH2 domain-containing signaling proteins, most importantly STAT3 (sarapultsev2023jakstatsignalingin pages 4-5, morelli2024socs1andsocs3 pages 3-5).

### 3.3 Step 3: STAT3 activation and transcriptional output

STAT3 is recruited to phosphotyrosine residues on the activated gp130 cytoplasmic tail via its SH2 domain (sarapultsev2023jakstatsignalingin pages 4-5). Once docked, STAT3 is itself phosphorylated on Tyr705 by the receptor-associated JAKs. Phosphorylated STAT3 dissociates from the receptor, forms homodimers (or, in some contexts, STAT3-STAT1 heterodimers), and translocates to the nucleus where it activates transcription of target genes including acute-phase proteins (CRP, serum amyloid A, haptoglobin), anti-apoptotic genes (*BCL2L1*, *MCL1*), cell cycle regulators (*CCND1*, *MYC*), and the negative feedback regulator *SOCS3* (schumertl2025il6signalingin pages 3-5, sarapultsev2023jakstatsignalingin pages 4-5, chakraborty2022areviewon pages 2-5).

Beyond STAT3, gp130 also activates STAT1 (particularly through IL-27 or through specific STAT-binding site configurations), and the SHP2/Ras/ERK and PI3K/Akt cascades—together accounting for the remarkable pleiotropy of IL-6 (schumertl2025il6signalingin pages 1-3, millrine2022makingsenseof pages 9-11, millrine2022makingsenseof pages 2-4).

### 3.4 Negative regulation

The IL-6/JAK/STAT3 axis is tightly controlled by three classes of negative regulators:

**SOCS3** constitutes the most important pathway-specific feedback brake. SOCS3 expression is rapidly induced by STAT3 itself, creating a classical negative feedback loop (millrine2022makingsenseof pages 5-6, chakraborty2022areviewon pages 2-5). SOCS3 acts through multiple mechanisms: its kinase inhibitory region (KIR) functions as a pseudosubstrate to block JAK catalytic activity; its SH2 domain binds phosphotyrosine 757 (human) / 759 (mouse) on gp130 to sterically prevent STAT recruitment; and its SOCS box recruits Elongin BC–Cullin5 E3 ubiquitin ligase complexes to target signaling proteins for proteasomal degradation (morelli2024socs1andsocs3 pages 3-5, low2022thesuppressorof pages 2-3, morelli2024socs1andsocs3 pages 2-3). SOCS3 inhibits JAK1, JAK2, and TYK2 but does not affect JAK3 due to JAK3's lack of the GQM (Glycine-Glutamine-Methionine) motif recognized by SOCS3 (millrine2022makingsenseof pages 5-6).

**PIAS proteins** act in the nucleus to inhibit activated STAT dimers by preventing their DNA binding or blocking dimerization (xue2023evolvingcognitionof pages 2-3, xue2023evolvingcognitionof pages 1-2).

**Protein tyrosine phosphatases** (including CD45/PTPRC and SHP2) dephosphorylate JAKs at receptors or STAT dimers directly, terminating the signal (millrine2022makingsenseof pages 5-6, xue2023evolvingcognitionof pages 2-3).

---

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive summary of all principal molecular components of the IL-6/JAK/STAT3 pathway, including their domain architectures, pathway roles, and clinical significance.

| Component | Gene/Protein | Domain Architecture/Key Features | Role in Pathway | Clinical/Genetic Significance |
|---|---|---|---|---|
| IL-6 cytokine | **IL6** / interleukin-6 | Four-helix bundle cytokine; engages IL-6R at site I, then gp130 at sites II/III to form a higher-order signaling complex; functions in classical, trans-, and cluster signaling modes (rosejohn2023targetingil6transsignalling pages 1-2, lv2024thejakstatpathway pages 11-12, zhou2023structuralinsightsinto pages 1-1) | Initiating ligand that triggers assembly of IL-6R–gp130 receptor complexes and downstream JAK/STAT3, MAPK, and PI3K signaling (schumertl2025il6signalingin pages 3-5, schumertl2025il6signalingin pages 1-3, sarapultsev2023jakstatsignalingin pages 4-5) | Central inflammatory mediator and drug target in RA, Castleman disease, COVID-19-associated hyperinflammation, atherosclerosis, and asthma; Open Targets links IL6 to rheumatoid arthritis, asthma, immune system disorder, atherosclerosis, and aortic stenosis (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9, OpenTargets Search: -IL6,IL6R,IL6ST,JAK1,JAK2,STAT3) |
| IL-6R alpha | **IL6R** / IL-6 receptor alpha | Ligand-binding alpha receptor; exists as membrane IL-6R and soluble sIL-6R generated by shedding or alternative splicing; does not signal alone and requires gp130 (rosejohn2023targetingil6transsignalling pages 1-2, rosejohn2023targetingil6transsignalling pages 2-3, schumertl2025il6signalingin pages 1-3) | Confers ligand specificity by binding IL-6; membrane IL-6R mediates classical signaling, while sIL-6R enables trans-signaling on gp130-positive IL-6R-negative cells (schumertl2025il6signalingin pages 3-5, millrine2022makingsenseof pages 4-5, rosejohn2023targetingil6transsignalling pages 3-4) | Therapeutically targeted by tocilizumab and sarilumab; major determinant of whether IL-6 responses are restricted or broadly propagated across tissues; Open Targets strongly links IL6R to RA and other inflammatory disease (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9, OpenTargets Search: -IL6,IL6R,IL6ST,JAK1,JAK2,STAT3) |
| gp130 / IL6ST | **IL6ST** / gp130 | Shared signal-transducing beta receptor of the IL-6 cytokine family; extracellular domains D1–D6 with acute bend between D4–D5 bringing juxtamembrane domains close; intracellular Box1/Box2 motifs recruit JAKs and C-terminal tyrosines recruit STAT3/SHP2/SOCS3 (lv2024thejakstatpathway pages 12-15, zhou2023structuralinsightsinto pages 1-1, lv2024thejakstatpathway pages 11-12, metcalfe2023structuresofthe pages 3-5) | Obligatory signaling scaffold that homodimerizes or heterodimerizes after ligand engagement to position receptor-associated JAKs for activation and create phosphotyrosine docking sites for STAT3 and SHP2 (lv2024thejakstatpathway pages 11-12, lv2024thejakstatpathway pages 12-15, sarapultsev2023jakstatsignalingin pages 4-5) | **IL6ST** variants cause strikingly diverse phenotypes: complete biallelic loss can cause extended Stüve-Wiedemann syndrome; selective loss-of-function causes dominant or recessive hyper-IgE syndrome and IL-11-related craniosynostosis/dental anomalies; somatic gain-of-function variants drive inflammatory hepatocellular adenoma, with ~60% of IHCA harboring in-frame **IL6ST** deletions (chen2024thehumangp130 pages 1-2, chen2024thehumangp130 pages 6-8, arlabosse2023newdominantnegativeil6st pages 1-2, chen2024thehumangp130 pages 5-6, chen2024thehumangp130 pages 2-4) |
| JAK1 | **JAK1** / Janus kinase 1 | Non-receptor tyrosine kinase with N-terminal FERM-SH2 receptor-binding module and C-terminal pseudokinase/kinase domains; associates constitutively with Box1/Box2 motifs of cytokine receptors (lv2024thejakstatpathway pages 11-12, lv2024thejakstatpathway pages 12-15) | Major gp130-associated kinase in IL-6 signaling; transphosphorylates partner JAKs, phosphorylates receptor tails, and promotes STAT3 recruitment and activation (lv2024thejakstatpathway pages 12-15, sarapultsev2023jakstatsignalingin pages 4-5) | Central therapeutic node for jakinibs; approved/clinically used JAK1-directed or JAK1-containing inhibitors include tofacitinib, baricitinib, filgotinib, and upadacitinib; Open Targets links JAK1 to RA, asthma, atherosclerosis, and immune disorders (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10, OpenTargets Search: -IL6,IL6R,IL6ST,JAK1,JAK2,STAT3) |
| JAK2 | **JAK2** / Janus kinase 2 | Same core JAK architecture as JAK1; receptor-associated kinase activated by cytokine-induced receptor apposition and transphosphorylation (lv2024thejakstatpathway pages 11-12, sarapultsev2023jakstatsignalingin pages 4-5) | Participates with JAK1 and/or TYK2 in propagating gp130 signals and can contribute to STAT3 phosphorylation downstream of IL-6 (sarapultsev2023jakstatsignalingin pages 4-5, millrine2022makingsenseof pages 5-6) | Important downstream therapeutic target in inflammatory disease and malignancy; part of baricitinib activity and broader JAK inhibition strategies; Open Targets links JAK2 to RA, asthma, immune disorders, atherosclerosis, and aortic stenosis (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10, OpenTargets Search: -IL6,IL6R,IL6ST,JAK1,JAK2,STAT3) |
| TYK2 | **TYK2** / tyrosine kinase 2 | JAK family kinase with FERM-SH2 receptor-binding module and catalytic C-terminus; can associate with gp130-family receptors and is susceptible to SOCS3-mediated control (sarapultsev2023jakstatsignalingin pages 4-5, morelli2024socs1andsocs3 pages 2-3) | Accessory/partner kinase in gp130 signaling, contributing with JAK1/JAK2 to receptor phosphorylation and STAT activation in some cellular contexts (sarapultsev2023jakstatsignalingin pages 4-5, millrine2022makingsenseof pages 5-6) | Not as central as JAK1 for canonical IL-6 responses but mechanistically relevant for pathway robustness and cytokine-family crosstalk; included among kinases inhibited by SOCS3 in gp130 pathways (millrine2022makingsenseof pages 5-6, morelli2024socs1andsocs3 pages 2-3) |
| STAT3 | **STAT3** / signal transducer and activator of transcription 3 | Latent cytoplasmic transcription factor with N-terminal domain, coiled-coil domain, DNA-binding domain, linker, SH2 domain, and C-terminal transactivation tail; recruited to phosphotyrosines on gp130 and activated by tyrosine phosphorylation (sarapultsev2023jakstatsignalingin pages 4-5, philips2022thejakstatpathway pages 4-6) | Principal transcriptional effector of IL-6 signaling; after phosphorylation it dimerizes, translocates to the nucleus, and induces acute-phase, inflammatory, survival, and differentiation programs including **SOCS3** (schumertl2025il6signalingin pages 3-5, sarapultsev2023jakstatsignalingin pages 4-5, morelli2024socs1andsocs3 pages 2-3) | Gain or sustained activation is linked to chronic inflammation, fibrosis, angiogenesis, and cancer; dominant-negative **STAT3** variants classically cause hyper-IgE syndrome, providing a human genetic benchmark for IL-6/STAT3 function; Open Targets strongly links STAT3 to immune disorders and RA (philips2022thejakstatpathway pages 4-6, chen2024thehumangp130 pages 1-2, arlabosse2023newdominantnegativeil6st pages 1-2, OpenTargets Search: -IL6,IL6R,IL6ST,JAK1,JAK2,STAT3) |
| SOCS3 | **SOCS3** / suppressor of cytokine signaling 3 | Inducible feedback inhibitor with N-terminal kinase inhibitory region (KIR), central SH2 domain, and C-terminal SOCS box that recruits E3 ubiquitin ligase machinery; binds gp130 pY757 and inhibits JAK catalytic function (morelli2024socs1andsocs3 pages 3-5, low2022thesuppressorof pages 2-3, morelli2024socs1andsocs3 pages 2-3) | Canonical negative-feedback brake on IL-6 signaling; induced by STATs, then blocks JAK1/JAK2/TYK2 activity, interferes with signaling complex function, and can target components for degradation (millrine2022makingsenseof pages 5-6, xue2023evolvingcognitionof pages 2-3, morelli2024socs1andsocs3 pages 3-5, morelli2024socs1andsocs3 pages 2-3) | Loss or insufficiency prolongs IL-6-driven STAT1/STAT3 activation; central determinant of pathway duration and cytokine specificity in gp130 signaling; therapeutically relevant as an endogenous JAK checkpoint (millrine2022makingsenseof pages 5-6, morelli2024socs1andsocs3 pages 3-5) |
| PIAS | **PIAS family** / protein inhibitors of activated STATs | Nuclear STAT antagonists; inhibit signaling by blocking STAT dimer function and/or DNA binding rather than receptor-proximal kinase activation (xue2023evolvingcognitionof pages 2-3, xue2023evolvingcognitionof pages 1-2, park2023exploringthejakstat pages 5-7) | Downstream negative regulators that restrain transcriptional output of activated STATs after nuclear entry, complementing SOCS- and phosphatase-based control (xue2023evolvingcognitionof pages 2-3, xue2023evolvingcognitionof pages 1-2) | Important conceptual regulators of JAK/STAT specificity, though less IL-6-selective than SOCS3; dysregulation may alter amplitude and persistence of STAT-dependent inflammatory transcription (xue2023evolvingcognitionof pages 2-3, xue2023evolvingcognitionof pages 1-2) |
| SHP2 | **PTPN11** / SHP2 phosphatase | SH2 domain-containing phosphatase/adaptor engaged downstream of gp130 phosphotyrosines; couples receptor activation to the Ras/MAPK cascade and participates in non-STAT outputs (arlabosse2023newdominantnegativeil6st pages 7-8, millrine2022makingsenseof pages 2-4) | Accessory signal transducer branching IL-6 responses beyond STAT3 toward MAPK/ERK signaling; helps explain pleiotropy and context-dependent outputs of gp130 signaling (schumertl2025il6signalingin pages 1-3, millrine2022makingsenseof pages 2-4) | Distinguishes IL-6/JAK/STAT3 module from the broader gp130 network by linking the receptor to parallel pathways; truncating **IL6ST** variants can disrupt SHP2/SOCS3 interaction motifs and alter signaling balance (arlabosse2023newdominantnegativeil6st pages 7-8, millrine2022makingsenseof pages 2-4) |


*Table: This table summarizes the main proteins that make up the IL-6/IL6R/gp130/JAK/STAT3 module, emphasizing structural features, pathway roles, and clinically important genetic or pharmacologic associations. It is useful as a compact reference for connecting receptor biochemistry to disease mechanisms and therapeutic targeting.*

### 4.1 The hexameric signaling complex

Recent cryo-EM studies have provided unprecedented structural insight into the IL-6:IL-6Rα:gp130 hexameric complex. Zhou et al. (2023) determined structures of five gp130-family signaling complexes, revealing that all share a common architectural principle: acute bends in the signaling receptors bring membrane-proximal domains within ~30 Å, though with distinct inter-receptor distances and orientations across different cytokine complexes (zhou2023structuralinsightsinto pages 1-1). For the IL-6 complex specifically, the D3 domains of gp130 pairs are separated by approximately 80 Å, but the sharp D4–D5 bend brings the D6 juxtamembrane domains to approximately 19 Å apart, a spacing proposed to be critical for JAK transphosphorylation (lv2024thejakstatpathway pages 11-12).

Gardner et al. (2024) solved cryo-EM structures at 3.1 Å resolution revealing that disease-associated gp130 mutations increase flexibility and distance between extracellular domains, but these distances are minimized as the transmembrane helix exits the membrane, suggesting a "dimmer switch" mode of signal transmission where geometry stringency at the membrane dictates signaling output (gardner2024structuralinsightsinto pages 1-2). Metcalfe et al. (2023) further demonstrated that the membrane-proximal D4–D6 domains of gp130 are dynamic and that deletion of any one of these domains renders gp130 non-functional, underscoring their critical role in signal transduction (metcalfe2023structuresofthe pages 3-5).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Evolutionary conservation of the JAK-STAT pathway

The JAK-STAT pathway is widely conserved across metazoans and represents one of the most ancient signal transduction cascades (philips2022thejakstatpathway pages 4-6). In *Drosophila melanogaster*, the pathway is simplified to three cytokine-like ligands (Unpaired, Upd2, Upd3), one receptor (Domeless), one JAK (Hopscotch), and one STAT (Stat92E) (philips2022thejakstatpathway pages 4-6). In *Caenorhabditis elegans*, a comparable simplified pathway exists. The negative regulatory architecture is also conserved, with *Drosophila* possessing single orthologs of SOCS and PIAS proteins (Socs36E and dPIAS, respectively), compared to multiple family members in mammals (philips2022thejakstatpathway pages 4-6). The JAK-STAT pathway in insects functions in antiviral defense, developmental patterning, and persistent viral infection management (philips2022thejakstatpathway pages 4-6).

### 5.2 IL-6 specifically: vertebrate elaboration

While the core JAK-STAT signaling module is ancient, IL-6 itself and the IL-6-specific receptor system represent a vertebrate-lineage elaboration. In teleost fish, IL-6 orthologs share only 23–30% amino acid identity with mammalian IL-6, though intra-teleost conservation is high (e.g., 91% identity between blunt snout bream and grass carp IL-6) (wang2022classicalsignalingand pages 2-4). Despite this sequence divergence, the fundamental signaling architecture is conserved: teleost IL-6 activates STAT3 phosphorylation through both classical signaling and trans-signaling (wang2022classicalsignalingand pages 2-4, wang2022classicalsignalingand pages 11-12). However, notable differences exist in pathway wiring. In grass carp primary hepatocytes, IL-6 activates JAK/STAT3 but not MEK/ERK pathways, with evidence suggesting that strong STAT3 activation may suppress ERK phosphorylation to prevent over-immunity—a regulatory balance that differs from the typically concurrent pathway activation seen in mammalian cells (wang2022classicalsignalingand pages 11-12).

### 5.3 Cell-type and tissue variation in mammals

IL-6 signaling output varies dramatically across cell types, primarily due to differential expression of membrane IL-6R. Classical signaling is restricted to IL-6R-expressing cells (hepatocytes, monocytes/macrophages, certain T cell subsets, megakaryocytes, and some mesenchymal populations), while trans-signaling extends responsiveness to essentially all gp130-expressing cells, including endothelial cells, fibroblasts, smooth muscle cells, and most epithelial lineages (schumertl2025il6signalingin pages 3-5, millrine2022makingsenseof pages 4-5). This distribution creates a fundamental division: classical signaling governs homeostatic and acute-phase responses, while trans-signaling mediates broader inflammatory pathology (rosejohn2023targetingil6transsignalling pages 1-2, rosejohn2023targetingil6transsignalling pages 3-4). Cluster signaling represents a specialized cell-contact-dependent mode operating at the immunological synapse between dendritic cells and T cells (millrine2022makingsenseof pages 4-5).

The downstream signaling quality also varies: while STAT3 is the dominant STAT activated by IL-6, cells with different STAT expression profiles or epigenetic landscapes may engage STAT1 or STAT3/STAT1 heterodimers with distinct transcriptional consequences (millrine2022makingsenseof pages 9-11, millrine2022makingsenseof pages 5-6).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory sequence of events

The signaling cascade follows a strict order: (i) IL-6 must bind IL-6Rα before the complex can engage gp130; (ii) gp130 homodimerization is an absolute requirement for intracellular signaling; (iii) JAK transphosphorylation depends on the geometric proximity of intracellular domains within the dimerized complex; (iv) STAT3 recruitment requires prior JAK-mediated phosphorylation of gp130 tyrosines (lv2024thejakstatpathway pages 11-12, lv2024thejakstatpathway pages 12-15, sarapultsev2023jakstatsignalingin pages 4-5). The SOCS3 feedback loop then operates with a characteristic delay, creating a transient signaling window.

### 6.2 Failure modes revealed by human genetics

A comprehensive taxonomy of 59 rare *IL6ST* pathogenic variants, classified by Chen et al. (2024) into six functional classes, provides a genetic blueprint for pathway failure modes (chen2024thehumangp130 pages 1-2):

- **Class I** (biallelic complete loss-of-function): Ablation of all gp130-dependent cytokine signaling causes extended Stüve-Wiedemann Syndrome, a severe multi-system disorder. *IL6ST* knockout in mice is embryonically lethal (chen2024thehumangp130 pages 2-4).
- **Classes II–III** (selective loss-of-function): Biallelic or monoallelic dominant-negative variants selectively impair IL-6 and IL-11 signaling while preserving LIF, OSM, and IL-27 responses, causing autosomal recessive or dominant hyper-IgE syndrome (HIES) with recurrent infections, atopy, and skeletal abnormalities (arlabosse2023newdominantnegativeil6st pages 1-2, chen2024thehumangp130 pages 5-6).
- **Class IV** (cytokine-specific): Biallelic variants exclusively impairing IL-11 signaling cause craniosynostosis and dental anomalies without immune dysfunction (chen2024thehumangp130 pages 5-6).
- **Classes V–VI** (gain-of-function): Somatic mosaic activating mutations cause constitutive STAT3 activation—in hepatocytes producing inflammatory hepatocellular adenoma (~60% of IHCA cases), and in hematopoietic cells causing immune dysregulation syndrome (chen2024thehumangp130 pages 6-8).

Common non-coding *IL6ST* variants (e.g., rs7731626) are associated with risk of immune-mediated disorders including Crohn's disease, ulcerative colitis, and rheumatoid arthritis, reflecting a spectrum from monogenic to complex disease associations (chen2024thehumangp130 pages 5-5, chen2024thehumangp130 pages 12-13).

Dominant-negative *STAT3* variants classically cause hyper-IgE syndrome, phenocopying many features of selective *IL6ST* loss-of-function and confirming that STAT3 is the essential transcriptional effector of the IL-6/gp130 pathway for immune function (arlabosse2023newdominantnegativeil6st pages 1-2, arlabosse2023newdominantnegativeil6st pages 7-8).

### 6.3 Disease associations from OpenTargets

OpenTargets database analysis reveals that all major pathway components (IL6, IL6R, IL6ST, JAK1, JAK2, STAT3) have strong disease associations across immune system disorders, rheumatoid arthritis, atherosclerosis, and asthma, with IL6R showing the highest association scores for rheumatoid arthritis (score 0.75) and JAK2 for immune system disorders (score 0.92) (OpenTargets Search: -IL6,IL6R,IL6ST,JAK1,JAK2,STAT3).

---

## 7. Therapeutic Targeting

The IL-6 signaling pathway has become one of the most tractable cytokine systems for therapeutic intervention, with agents targeting different nodes of the cascade.

| Agent Name | Target | Mechanism | Approved Indications | Development Status |
|---|---|---|---|---|
| Tocilizumab | IL-6R | Humanized monoclonal antibody against soluble and membrane IL-6R; blocks IL-6 receptor engagement and downstream gp130/JAK/STAT signaling (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 13-14) | Rheumatoid arthritis, Castleman disease, systemic juvenile idiopathic arthritis, giant cell arteritis, neuromyelitis optica spectrum disorder, severe COVID-19 pneumonia (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 13-14) | Approved and in clinical use (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9) |
| Sarilumab | IL-6Rα | Fully human monoclonal antibody against IL-6R; blocks receptor-mediated IL-6 signaling (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 13-14) | Rheumatoid arthritis (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 13-14) | Approved; phase III efficacy established in RA (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 13-14) |
| Siltuximab | IL-6 | Chimeric monoclonal antibody binding IL-6 and preventing IL-6:IL-6R complex formation (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9, lv2024thejakstatpathway pages 3-4) | Idiopathic multicentric Castleman disease / Castleman disease (US and EU) (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9) | Approved (rosejohn2023targetingil6transsignalling pages 5-7, schumertl2025il6signalingin pages 7-9) |
| Olokizumab | IL-6 | Monoclonal antibody against IL-6; blocks cytokine engagement with IL-6R (schumertl2025il6signalingin pages 13-14, lv2024thejakstatpathway pages 3-4, schumertl2025il6signalingin pages 9-10) | Reported as approved for clinical use in Russia; studied for rheumatoid arthritis (schumertl2025il6signalingin pages 13-14, schumertl2025il6signalingin pages 9-10) | In clinical development globally; not approved in US/EU per reviewed sources (schumertl2025il6signalingin pages 13-14, schumertl2025il6signalingin pages 9-10) |
| Satralizumab | IL-6R | Monoclonal antibody targeting IL-6R; suppresses IL-6 receptor signaling (schumertl2025il6signalingin pages 13-14) | Neuromyelitis optica spectrum disorder; also studied in myasthenia gravis (schumertl2025il6signalingin pages 13-14) | Approved for NMOSD; additional clinical evaluation in other autoimmune disease (schumertl2025il6signalingin pages 13-14) |
| Olamkicept / sgp130Fc | IL-6 trans-signaling complex (IL-6:sIL-6R) | Soluble gp130-Fc fusion protein; selectively neutralizes IL-6 trans-signaling while sparing classical signaling (rosejohn2023targetingil6transsignalling pages 5-7, rosejohn2023targetingil6transsignalling pages 4-5, schumertl2025il6signalingin pages 9-10) | No fully established approved indication reported in the cited reviews; investigated for inflammatory bowel disease (schumertl2025il6signalingin pages 9-10) | In clinical development; phase II IBD data reported with clinical response/remission (schumertl2025il6signalingin pages 9-10) |
| Tofacitinib | JAK1/JAK3 | Small-molecule JAK inhibitor acting downstream of IL-6/gp130 signaling to suppress STAT activation (schumertl2025il6signalingin pages 7-9, rosejohn2023targetingil6transsignalling pages 4-5, schumertl2025il6signalingin pages 9-10) | Rheumatoid arthritis, ulcerative colitis, psoriatic arthritis, alopecia areata (lv2024thejakstatpathway pages 3-4, schumertl2025il6signalingin pages 9-10) | Approved; first FDA approval for RA in 2012 (lv2024thejakstatpathway pages 3-4, schumertl2025il6signalingin pages 9-10) |
| Baricitinib | JAK1/JAK2 | Small-molecule JAK inhibitor that blocks downstream cytokine signaling including IL-6 outputs (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10) | Rheumatoid arthritis, atopic dermatitis (schumertl2025il6signalingin pages 9-10) | Approved; Europe 2017 for RA, later for atopic dermatitis (schumertl2025il6signalingin pages 9-10) |
| Filgotinib | JAK1 | JAK1-selective inhibitor reducing signaling downstream of IL-6 and other cytokines (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10) | Rheumatoid arthritis and ulcerative colitis / colitis ulcerosa (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10) | Approved in some jurisdictions; in clinical use where authorized (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10) |
| Upadacitinib | JAK1 | JAK1-selective inhibitor that suppresses IL-6-driven JAK/STAT signaling downstream of the receptor (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10) | Rheumatoid arthritis, ulcerative colitis, Crohn's disease, and other inflammatory diseases (schumertl2025il6signalingin pages 9-10) | Approved and in expanding clinical use (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10) |
| Ruxolitinib | JAK1/JAK2 | Small-molecule JAK1/JAK2 inhibitor acting downstream of cytokine receptors including gp130-associated signaling (lv2024thejakstatpathway pages 3-4) | Myelofibrosis (lv2024thejakstatpathway pages 3-4) | Approved by FDA in 2011; not IL-6-specific but relevant downstream pathway inhibitor (lv2024thejakstatpathway pages 3-4) |


*Table: This table summarizes major approved and in-development drugs that target the IL-6 signaling axis at the ligand, receptor, trans-signaling, or downstream JAK level. It is useful for comparing where each agent acts in the pathway and how mature its clinical deployment is.*

Key developments include the selective trans-signaling inhibitor olamkicept (sgp130Fc), which represents a mechanistically novel approach that blocks pro-inflammatory trans-signaling while preserving beneficial classical signaling. Phase II trials in inflammatory bowel disease have shown clinical response in 44% and remission in 19% of patients (schumertl2025il6signalingin pages 9-10). JAK1-selective inhibitors such as upadacitinib and filgotinib have achieved broad clinical use across multiple inflammatory diseases, with JAK1 playing the dominant role in IL-6-induced biologic responses (schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10). Over 10 small-molecule JAK inhibitors have received FDA approval, with more than 40 additional inhibitors at various stages of clinical development (lv2024thejakstatpathway pages 3-4).

---

## 8. Controversies and Open Questions

### 8.1 The pleiotropy problem

A central unresolved question is how IL-6, signaling through a single receptor system with shared intracellular cascades across all three modes, generates such diverse biological outcomes ranging from immune activation to tissue regeneration to metabolic regulation (millrine2022makingsenseof pages 1-2). Classical and trans-signaling activate qualitatively identical intracellular pathways (JAK/STAT, MAPK, PI3K, YAP) through the same gp130 homodimer, yet produce functionally distinct—even opposing—outcomes (schumertl2025il6signalingin pages 1-3, rosejohn2023targetingil6transsignalling pages 3-4). Quantitative differences in signal amplitude, duration, and spatial context (e.g., reduced internalization and prolonged signaling in trans-signaling compared to classical signaling) may partially explain this divergence, but the full mechanistic basis remains incompletely understood (rosejohn2023targetingil6transsignalling pages 3-4).

### 8.2 STAT3 versus STAT1 cross-regulation

While STAT3 is the dominant transcription factor activated by IL-6, STAT1 is also engaged in context-dependent ways. In rheumatoid arthritis models, STAT1 generally opposes disease pathology while STAT3 promotes leukocyte recruitment and joint destruction (millrine2022makingsenseof pages 9-11). Strikingly, when STAT1 is absent, IL-6 and IL-27 induce very similar transcriptional programs, suggesting that differences in STAT activation thresholds rather than qualitative pathway differences may be the key determinant of cytokine specificity (millrine2022makingsenseof pages 4-5). The mechanisms governing this cross-regulation—including STAT heterodimerization, competition for receptor docking sites, and epigenetic priming of STAT-responsive enhancers—remain actively debated (millrine2022makingsenseof pages 9-11, millrine2022makingsenseof pages 5-6).

### 8.3 The classic/trans-signaling dichotomy

While the framework assigning anti-inflammatory/regenerative functions to classical signaling and pro-inflammatory/pathological functions to trans-signaling has been highly influential and therapeutically productive, multiple authors caution that this distinction is not absolute (millrine2022makingsenseof pages 4-5). The boundaries between these modes in vivo are likely more fluid than in vitro experiments suggest, and there may be pathological contexts where classical signaling contributes to disease or where trans-signaling serves protective functions.

### 8.4 Structural mechanisms of signal transmission

Despite recent cryo-EM advances, the precise molecular mechanism by which extracellular complex formation is transmitted across the membrane to activate intracellular JAKs remains incompletely resolved. The transmembrane and intracellular domains of gp130 were not resolved in the cryo-EM structures, with a ~15 Å gap observed between the C-terminal density and the detergent micelle (zhou2023structuralinsightsinto pages 9-10). Whether signaling depends on precise geometric positioning (a "dimmer switch" model) or on more binary dimerization events remains an active area of investigation (gardner2024structuralinsightsinto pages 1-2).

### 8.5 Clinical translation challenges

Despite therapeutic successes, global IL-6 blockade (by anti-IL-6 or anti-IL-6R antibodies) suppresses both beneficial classical signaling and pathological trans-signaling, potentially compromising host defense and acute-phase responses. The development of selective trans-signaling inhibitors like olamkicept represents an attempt to address this limitation, but clinical data remain limited (schumertl2025il6signalingin pages 9-10). Additionally, the lack of FDA-approved direct STAT3 inhibitors, despite extensive preclinical work, highlights the difficulty of targeting transcription factors pharmacologically (schumertl2025il6signalingin pages 7-9).

---

## 9. Key References

The following primary sources were most extensively utilized in this review:

1. Rose-John S, Jenkins BJ, Garbers C, Moll JM, Scheller J. Targeting IL-6 trans-signalling: past, present and future prospects. *Nat Rev Immunol.* 2023;23:666-681. doi:10.1038/s41577-023-00856-y (rosejohn2023targetingil6transsignalling pages 1-2, rosejohn2023targetingil6transsignalling pages 2-3, rosejohn2023targetingil6transsignalling pages 4-5, rosejohn2023targetingil6transsignalling pages 3-4, rosejohn2023targetingil6transsignalling pages 5-7)

2. Schumertl T, Lokau J, Garbers C. IL-6 signaling in immunopathology: from basic biology to selective therapeutic intervention. *ImmunoTargets Ther.* 2025;14:681-695. doi:10.2147/itt.s485684 (schumertl2025il6signalingin pages 3-5, schumertl2025il6signalingin pages 1-3, schumertl2025il6signalingin pages 7-9, schumertl2025il6signalingin pages 9-10)

3. Lv Y, Qi J, Babon JJ, et al. The JAK-STAT pathway: from structural biology to cytokine engineering. *Signal Transduct Target Ther.* 2024;9. doi:10.1038/s41392-024-01934-w (lv2024thejakstatpathway pages 11-12, lv2024thejakstatpathway pages 12-15, lv2024thejakstatpathway pages 3-4)

4. Philips RL, Wang Y, Cheon HJ, et al. The JAK-STAT pathway at 30: much learned, much more to do. *Cell.* 2022;185:3857-3876. doi:10.1016/j.cell.2022.09.023 (philips2022thejakstatpathway pages 4-6)

5. Millrine D, Jenkins RH, Hughes STO, Jones SA. Making sense of IL-6 signalling cues in pathophysiology. *FEBS Lett.* 2022;596:567-588. doi:10.1002/1873-3468.14201 (millrine2022makingsenseof pages 4-5, millrine2022makingsenseof pages 5-6, millrine2022makingsenseof pages 9-11, millrine2022makingsenseof pages 1-2, millrine2022makingsenseof pages 2-4)

6. Chen Y-H, van Zon S, Adams A, et al. The human GP130 cytokine receptor and its expression—an atlas and functional taxonomy of genetic variants. *J Clin Immunol.* 2024;44. doi:10.1007/s10875-023-01603-7 (chen2024thehumangp130 pages 1-2, chen2024thehumangp130 pages 6-8, chen2024thehumangp130 pages 5-6, chen2024thehumangp130 pages 2-4, chen2024thehumangp130 pages 5-5, chen2024thehumangp130 pages 12-13)

7. Zhou Y, Stevis PE, Cao J, et al. Structural insights into the assembly of gp130 family cytokine signaling complexes. *Sci Adv.* 2023;9:eade4395. doi:10.1126/sciadv.ade4395 (zhou2023structuralinsightsinto pages 1-1, zhou2023structuralinsightsinto pages 9-10, zhou2023structuralinsightsinto pages 11-12, zhou2023structuralinsightsinto pages 6-7)

8. Xue C, Yao Q, Gu X-Y, et al. Evolving cognition of the JAK-STAT signaling pathway: autoimmune disorders and cancer. *Signal Transduct Target Ther.* 2023;8. doi:10.1038/s41392-023-01468-7 (xue2023evolvingcognitionof pages 2-3, xue2023evolvingcognitionof pages 1-2)

9. Morelli M, Madonna S, Albanesi C. SOCS1 and SOCS3 as key checkpoint molecules in the immune responses associated to skin inflammation and malignant transformation. *Front Immunol.* 2024;15. doi:10.3389/fimmu.2024.1393799 (morelli2024socs1andsocs3 pages 3-5, morelli2024socs1andsocs3 pages 2-3)

10. Gardner S, Jin Y, Fyfe PK, et al. Structural insights into IL-11-mediated signalling and human IL6ST variant-associated immunodeficiency. *Nat Commun.* 2024;15. doi:10.1038/s41467-024-46235-6 (gardner2024structuralinsightsinto pages 1-2)

11. Metcalfe RD, et al. Structures of the interleukin 11 signalling complex reveal gp130 dynamics and the inhibitory mechanism of a cytokine variant. *Nat Commun.* 2023;14. doi:10.1038/s41467-023-42754-w (metcalfe2023structuresofthe pages 3-5, metcalfe2023structuresofthe pages 1-2)

12. Wang J, Sun Q, Zhang J, et al. Classical signaling and trans-signaling pathways stimulated by *Megalobrama amblycephala* IL-6 and IL-6R. *Int J Mol Sci.* 2022;23:2019. doi:10.3390/ijms23042019 (wang2022classicalsignalingand pages 2-4, wang2022classicalsignalingand pages 11-12)

13. Arlabosse T, et al. New dominant-negative IL6ST variants expand the immunological and clinical spectrum of GP130-dependent hyper-IgE syndrome. *J Clin Immunol.* 2023;43:1566-1580. doi:10.1007/s10875-023-01517-4 (arlabosse2023newdominantnegativeil6st pages 1-2, arlabosse2023newdominantnegativeil6st pages 7-8)

References

1. (lv2024thejakstatpathway pages 11-12): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

2. (sarapultsev2023jakstatsignalingin pages 4-5): Alexey Sarapultsev, Evgenii Gusev, M. Komelkova, Irina Utepova, Shanshan Luo, and Desheng Hu. Jak-stat signaling in inflammation and stress-related diseases: implications for therapeutic interventions. Molecular Biomedicine, Nov 2023. URL: https://doi.org/10.1186/s43556-023-00151-1, doi:10.1186/s43556-023-00151-1. This article has 234 citations and is from a peer-reviewed journal.

3. (rosejohn2023targetingil6transsignalling pages 1-2): Stefan Rose-John, Brendan J. Jenkins, Christoph Garbers, Jens M. Moll, and Jürgen Scheller. Targeting il-6 trans-signalling: past, present and future prospects. Nature Reviews Immunology, 23:666-681, Apr 2023. URL: https://doi.org/10.1038/s41577-023-00856-y, doi:10.1038/s41577-023-00856-y. This article has 530 citations and is from a highest quality peer-reviewed journal.

4. (schumertl2025il6signalingin pages 1-3): Tim Schumertl, Juliane Lokau, and Christoph Garbers. Il-6 signaling in immunopathology: from basic biology to selective therapeutic intervention. ImmunoTargets and Therapy, 14:681-695, Jul 2025. URL: https://doi.org/10.2147/itt.s485684, doi:10.2147/itt.s485684. This article has 21 citations.

5. (millrine2022makingsenseof pages 5-6): David Millrine, Robert H. Jenkins, Stuart T. O. Hughes, and Simon A. Jones. Making sense of il‐6 signalling cues in pathophysiology. FEBS Letters, 596:567-588, Oct 2022. URL: https://doi.org/10.1002/1873-3468.14201, doi:10.1002/1873-3468.14201. This article has 37 citations and is from a peer-reviewed journal.

6. (xue2023evolvingcognitionof pages 2-3): Chen Xue, Q. Yao, Xin-yu Gu, Qing-miao Shi, Xin Yuan, Qingfei Chu, Zhengyi Bao, Juan-fen Lu, and Lan-Ju Li. Evolving cognition of the jak-stat signaling pathway: autoimmune disorders and cancer. Signal Transduction and Targeted Therapy, May 2023. URL: https://doi.org/10.1038/s41392-023-01468-7, doi:10.1038/s41392-023-01468-7. This article has 775 citations and is from a peer-reviewed journal.

7. (rosejohn2023targetingil6transsignalling pages 5-7): Stefan Rose-John, Brendan J. Jenkins, Christoph Garbers, Jens M. Moll, and Jürgen Scheller. Targeting il-6 trans-signalling: past, present and future prospects. Nature Reviews Immunology, 23:666-681, Apr 2023. URL: https://doi.org/10.1038/s41577-023-00856-y, doi:10.1038/s41577-023-00856-y. This article has 530 citations and is from a highest quality peer-reviewed journal.

8. (schumertl2025il6signalingin pages 7-9): Tim Schumertl, Juliane Lokau, and Christoph Garbers. Il-6 signaling in immunopathology: from basic biology to selective therapeutic intervention. ImmunoTargets and Therapy, 14:681-695, Jul 2025. URL: https://doi.org/10.2147/itt.s485684, doi:10.2147/itt.s485684. This article has 21 citations.

9. (zhou2023structuralinsightsinto pages 1-1): Yi Zhou, Panayiotis E. Stevis, Jing Cao, Kei Saotome, Jiaxi Wu, Arielle Glatman Zaretsky, Sokol Haxhinasto, George D. Yancopoulos, Andrew J. Murphy, Mark W. Sleeman, William C. Olson, and Matthew C. Franklin. Structural insights into the assembly of gp130 family cytokine signaling complexes. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade4395, doi:10.1126/sciadv.ade4395. This article has 58 citations and is from a highest quality peer-reviewed journal.

10. (metcalfe2023structuresofthe pages 1-2): Riley D. Metcalfe, Eric Hanssen, Ka Yee Fung, Kaheina Aizel, Clara C. Kosasih, Courtney O. Zlatic, Larissa Doughty, Craig J. Morton, Andrew P. Leis, Michael W. Parker, Paul R. Gooley, Tracy L. Putoczki, and Michael D. W. Griffin. Structures of the interleukin 11 signalling complex reveal gp130 dynamics and the inhibitory mechanism of a cytokine variant. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42754-w, doi:10.1038/s41467-023-42754-w. This article has 33 citations and is from a highest quality peer-reviewed journal.

11. (metcalfe2023structuresofthe pages 3-5): Riley D. Metcalfe, Eric Hanssen, Ka Yee Fung, Kaheina Aizel, Clara C. Kosasih, Courtney O. Zlatic, Larissa Doughty, Craig J. Morton, Andrew P. Leis, Michael W. Parker, Paul R. Gooley, Tracy L. Putoczki, and Michael D. W. Griffin. Structures of the interleukin 11 signalling complex reveal gp130 dynamics and the inhibitory mechanism of a cytokine variant. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42754-w, doi:10.1038/s41467-023-42754-w. This article has 33 citations and is from a highest quality peer-reviewed journal.

12. (millrine2022makingsenseof pages 2-4): David Millrine, Robert H. Jenkins, Stuart T. O. Hughes, and Simon A. Jones. Making sense of il‐6 signalling cues in pathophysiology. FEBS Letters, 596:567-588, Oct 2022. URL: https://doi.org/10.1002/1873-3468.14201, doi:10.1002/1873-3468.14201. This article has 37 citations and is from a peer-reviewed journal.

13. (millrine2022makingsenseof pages 1-2): David Millrine, Robert H. Jenkins, Stuart T. O. Hughes, and Simon A. Jones. Making sense of il‐6 signalling cues in pathophysiology. FEBS Letters, 596:567-588, Oct 2022. URL: https://doi.org/10.1002/1873-3468.14201, doi:10.1002/1873-3468.14201. This article has 37 citations and is from a peer-reviewed journal.

14. (rosejohn2023targetingil6transsignalling pages 4-5): Stefan Rose-John, Brendan J. Jenkins, Christoph Garbers, Jens M. Moll, and Jürgen Scheller. Targeting il-6 trans-signalling: past, present and future prospects. Nature Reviews Immunology, 23:666-681, Apr 2023. URL: https://doi.org/10.1038/s41577-023-00856-y, doi:10.1038/s41577-023-00856-y. This article has 530 citations and is from a highest quality peer-reviewed journal.

15. (schumertl2025il6signalingin pages 3-5): Tim Schumertl, Juliane Lokau, and Christoph Garbers. Il-6 signaling in immunopathology: from basic biology to selective therapeutic intervention. ImmunoTargets and Therapy, 14:681-695, Jul 2025. URL: https://doi.org/10.2147/itt.s485684, doi:10.2147/itt.s485684. This article has 21 citations.

16. (millrine2022makingsenseof pages 4-5): David Millrine, Robert H. Jenkins, Stuart T. O. Hughes, and Simon A. Jones. Making sense of il‐6 signalling cues in pathophysiology. FEBS Letters, 596:567-588, Oct 2022. URL: https://doi.org/10.1002/1873-3468.14201, doi:10.1002/1873-3468.14201. This article has 37 citations and is from a peer-reviewed journal.

17. (rosejohn2023targetingil6transsignalling pages 2-3): Stefan Rose-John, Brendan J. Jenkins, Christoph Garbers, Jens M. Moll, and Jürgen Scheller. Targeting il-6 trans-signalling: past, present and future prospects. Nature Reviews Immunology, 23:666-681, Apr 2023. URL: https://doi.org/10.1038/s41577-023-00856-y, doi:10.1038/s41577-023-00856-y. This article has 530 citations and is from a highest quality peer-reviewed journal.

18. (rosejohn2023targetingil6transsignalling pages 3-4): Stefan Rose-John, Brendan J. Jenkins, Christoph Garbers, Jens M. Moll, and Jürgen Scheller. Targeting il-6 trans-signalling: past, present and future prospects. Nature Reviews Immunology, 23:666-681, Apr 2023. URL: https://doi.org/10.1038/s41577-023-00856-y, doi:10.1038/s41577-023-00856-y. This article has 530 citations and is from a highest quality peer-reviewed journal.

19. (song2023experimentbasedcomputationalmodel pages 1-2): Min Song, Youli Wang, Brian H. Annex, and Aleksander S. Popel. Experiment-based computational model predicts that il-6 classic and trans-signaling exhibit similar potency in inducing downstream signaling in endothelial cells. NPJ Systems Biology and Applications, Sep 2023. URL: https://doi.org/10.1038/s41540-023-00308-2, doi:10.1038/s41540-023-00308-2. This article has 15 citations.

20. (lv2024thejakstatpathway pages 12-15): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

21. (morelli2024socs1andsocs3 pages 3-5): Martina Morelli, Stefania Madonna, and Cristina Albanesi. Socs1 and socs3 as key checkpoint molecules in the immune responses associated to skin inflammation and malignant transformation. Frontiers in Immunology, Jun 2024. URL: https://doi.org/10.3389/fimmu.2024.1393799, doi:10.3389/fimmu.2024.1393799. This article has 40 citations and is from a peer-reviewed journal.

22. (chakraborty2022areviewon pages 2-5): Rajdeep Chakraborty, Charbel Darido, Aziz Alnakli, Honghua Hu, and Karen Vickery. A review on the dual role of socs3 in cancer. Research in Oncology, 0:1-9, Apr 2022. URL: https://doi.org/10.21608/resoncol.2022.114548.1159, doi:10.21608/resoncol.2022.114548.1159. This article has 7 citations.

23. (millrine2022makingsenseof pages 9-11): David Millrine, Robert H. Jenkins, Stuart T. O. Hughes, and Simon A. Jones. Making sense of il‐6 signalling cues in pathophysiology. FEBS Letters, 596:567-588, Oct 2022. URL: https://doi.org/10.1002/1873-3468.14201, doi:10.1002/1873-3468.14201. This article has 37 citations and is from a peer-reviewed journal.

24. (low2022thesuppressorof pages 2-3): Zheng Yao Low, Ashley Jia Wen Yip, Vincent T. K. Chow, and Sunil K. Lal. The suppressor of cytokine signalling family of proteins and their potential impact on covid‐19 disease progression. Reviews in Medical Virology, Sep 2022. URL: https://doi.org/10.1002/rmv.2300, doi:10.1002/rmv.2300. This article has 24 citations and is from a peer-reviewed journal.

25. (morelli2024socs1andsocs3 pages 2-3): Martina Morelli, Stefania Madonna, and Cristina Albanesi. Socs1 and socs3 as key checkpoint molecules in the immune responses associated to skin inflammation and malignant transformation. Frontiers in Immunology, Jun 2024. URL: https://doi.org/10.3389/fimmu.2024.1393799, doi:10.3389/fimmu.2024.1393799. This article has 40 citations and is from a peer-reviewed journal.

26. (xue2023evolvingcognitionof pages 1-2): Chen Xue, Q. Yao, Xin-yu Gu, Qing-miao Shi, Xin Yuan, Qingfei Chu, Zhengyi Bao, Juan-fen Lu, and Lan-Ju Li. Evolving cognition of the jak-stat signaling pathway: autoimmune disorders and cancer. Signal Transduction and Targeted Therapy, May 2023. URL: https://doi.org/10.1038/s41392-023-01468-7, doi:10.1038/s41392-023-01468-7. This article has 775 citations and is from a peer-reviewed journal.

27. (OpenTargets Search: -IL6,IL6R,IL6ST,JAK1,JAK2,STAT3): Open Targets Query (-IL6,IL6R,IL6ST,JAK1,JAK2,STAT3, 38 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

28. (chen2024thehumangp130 pages 1-2): Yin-Huai Chen, Sarah van Zon, Alex Adams, Dirk Schmidt-Arras, Arian D. J. Laurence, and Holm H. Uhlig. The human gp130 cytokine receptor and its expression—an atlas and functional taxonomy of genetic variants. Journal of Clinical Immunology, Dec 2024. URL: https://doi.org/10.1007/s10875-023-01603-7, doi:10.1007/s10875-023-01603-7. This article has 11 citations and is from a domain leading peer-reviewed journal.

29. (chen2024thehumangp130 pages 6-8): Yin-Huai Chen, Sarah van Zon, Alex Adams, Dirk Schmidt-Arras, Arian D. J. Laurence, and Holm H. Uhlig. The human gp130 cytokine receptor and its expression—an atlas and functional taxonomy of genetic variants. Journal of Clinical Immunology, Dec 2024. URL: https://doi.org/10.1007/s10875-023-01603-7, doi:10.1007/s10875-023-01603-7. This article has 11 citations and is from a domain leading peer-reviewed journal.

30. (arlabosse2023newdominantnegativeil6st pages 1-2): Tiphaine Arlabosse, Marie Materna, Orbicia Riccio, Caroline Schnider, Federica Angelini, Matthieu Perreau, Isabelle Rochat, Andrea Superti-Furga, Belinda Campos-Xavier, Sébastien Héritier, Anaïs Pereira, Caroline Deswarte, Romain Lévy, Marco Distefano, Jacinta Bustamante, Marie Roelens, Raphaël Borie, Mathilde Le Brun, Bruno Crestani, Jean-Laurent Casanova, Anne Puel, Michaël Hofer, Claire Fieschi, Katerina Theodoropoulou, Vivien Béziat, and Fabio Candotti. New dominant-negative il6st variants expand the immunological and clinical spectrum of gp130-dependent hyper-ige syndrome. Journal of Clinical Immunology, 43:1566-1580, Jun 2023. URL: https://doi.org/10.1007/s10875-023-01517-4, doi:10.1007/s10875-023-01517-4. This article has 20 citations and is from a domain leading peer-reviewed journal.

31. (chen2024thehumangp130 pages 5-6): Yin-Huai Chen, Sarah van Zon, Alex Adams, Dirk Schmidt-Arras, Arian D. J. Laurence, and Holm H. Uhlig. The human gp130 cytokine receptor and its expression—an atlas and functional taxonomy of genetic variants. Journal of Clinical Immunology, Dec 2024. URL: https://doi.org/10.1007/s10875-023-01603-7, doi:10.1007/s10875-023-01603-7. This article has 11 citations and is from a domain leading peer-reviewed journal.

32. (chen2024thehumangp130 pages 2-4): Yin-Huai Chen, Sarah van Zon, Alex Adams, Dirk Schmidt-Arras, Arian D. J. Laurence, and Holm H. Uhlig. The human gp130 cytokine receptor and its expression—an atlas and functional taxonomy of genetic variants. Journal of Clinical Immunology, Dec 2024. URL: https://doi.org/10.1007/s10875-023-01603-7, doi:10.1007/s10875-023-01603-7. This article has 11 citations and is from a domain leading peer-reviewed journal.

33. (schumertl2025il6signalingin pages 9-10): Tim Schumertl, Juliane Lokau, and Christoph Garbers. Il-6 signaling in immunopathology: from basic biology to selective therapeutic intervention. ImmunoTargets and Therapy, 14:681-695, Jul 2025. URL: https://doi.org/10.2147/itt.s485684, doi:10.2147/itt.s485684. This article has 21 citations.

34. (philips2022thejakstatpathway pages 4-6): Rachael L. Philips, Yuxin Wang, HyeonJoo Cheon, Yuka Kanno, Massimo Gadina, Vittorio Sartorelli, Curt M. Horvath, James E. Darnell, George R. Stark, and John J. O’Shea. The jak-stat pathway at 30: much learned, much more to do. Cell, 185:3857-3876, Oct 2022. URL: https://doi.org/10.1016/j.cell.2022.09.023, doi:10.1016/j.cell.2022.09.023. This article has 730 citations and is from a highest quality peer-reviewed journal.

35. (park2023exploringthejakstat pages 5-7): Hyunjung Park, Sangjik Lee, Jaehun Lee, Hyuk Moon, and Simon Weonsang Ro. Exploring the jak/stat signaling pathway in hepatocellular carcinoma: unraveling signaling complexity and therapeutic implications. Sep 2023. URL: https://doi.org/10.3390/ijms241813764, doi:10.3390/ijms241813764. This article has 66 citations.

36. (arlabosse2023newdominantnegativeil6st pages 7-8): Tiphaine Arlabosse, Marie Materna, Orbicia Riccio, Caroline Schnider, Federica Angelini, Matthieu Perreau, Isabelle Rochat, Andrea Superti-Furga, Belinda Campos-Xavier, Sébastien Héritier, Anaïs Pereira, Caroline Deswarte, Romain Lévy, Marco Distefano, Jacinta Bustamante, Marie Roelens, Raphaël Borie, Mathilde Le Brun, Bruno Crestani, Jean-Laurent Casanova, Anne Puel, Michaël Hofer, Claire Fieschi, Katerina Theodoropoulou, Vivien Béziat, and Fabio Candotti. New dominant-negative il6st variants expand the immunological and clinical spectrum of gp130-dependent hyper-ige syndrome. Journal of Clinical Immunology, 43:1566-1580, Jun 2023. URL: https://doi.org/10.1007/s10875-023-01517-4, doi:10.1007/s10875-023-01517-4. This article has 20 citations and is from a domain leading peer-reviewed journal.

37. (gardner2024structuralinsightsinto pages 1-2): Scott Gardner, Yibo Jin, Paul K. Fyfe, Tomas B. Voisin, Junel Sotolongo Bellón, Elizabeth Pohler, Jacob Piehler, Ignacio Moraga, and Doryen Bubeck. Structural insights into il-11-mediated signalling and human il6st variant-associated immunodeficiency. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46235-6, doi:10.1038/s41467-024-46235-6. This article has 15 citations and is from a highest quality peer-reviewed journal.

38. (wang2022classicalsignalingand pages 2-4): Jixiu Wang, Qianhui Sun, Jian Zhang, Huanling Wang, and Hong Liu. Classical signaling and trans-signaling pathways stimulated by megalobrama amblycephala il-6 and il-6r. International Journal of Molecular Sciences, 23:2019, Feb 2022. URL: https://doi.org/10.3390/ijms23042019, doi:10.3390/ijms23042019. This article has 27 citations.

39. (wang2022classicalsignalingand pages 11-12): Jixiu Wang, Qianhui Sun, Jian Zhang, Huanling Wang, and Hong Liu. Classical signaling and trans-signaling pathways stimulated by megalobrama amblycephala il-6 and il-6r. International Journal of Molecular Sciences, 23:2019, Feb 2022. URL: https://doi.org/10.3390/ijms23042019, doi:10.3390/ijms23042019. This article has 27 citations.

40. (chen2024thehumangp130 pages 5-5): Yin-Huai Chen, Sarah van Zon, Alex Adams, Dirk Schmidt-Arras, Arian D. J. Laurence, and Holm H. Uhlig. The human gp130 cytokine receptor and its expression—an atlas and functional taxonomy of genetic variants. Journal of Clinical Immunology, Dec 2024. URL: https://doi.org/10.1007/s10875-023-01603-7, doi:10.1007/s10875-023-01603-7. This article has 11 citations and is from a domain leading peer-reviewed journal.

41. (chen2024thehumangp130 pages 12-13): Yin-Huai Chen, Sarah van Zon, Alex Adams, Dirk Schmidt-Arras, Arian D. J. Laurence, and Holm H. Uhlig. The human gp130 cytokine receptor and its expression—an atlas and functional taxonomy of genetic variants. Journal of Clinical Immunology, Dec 2024. URL: https://doi.org/10.1007/s10875-023-01603-7, doi:10.1007/s10875-023-01603-7. This article has 11 citations and is from a domain leading peer-reviewed journal.

42. (schumertl2025il6signalingin pages 13-14): Tim Schumertl, Juliane Lokau, and Christoph Garbers. Il-6 signaling in immunopathology: from basic biology to selective therapeutic intervention. ImmunoTargets and Therapy, 14:681-695, Jul 2025. URL: https://doi.org/10.2147/itt.s485684, doi:10.2147/itt.s485684. This article has 21 citations.

43. (lv2024thejakstatpathway pages 3-4): You Lv, Jianxun Qi, Jeff J. Babon, Longxing Cao, Guohuang Fan, Jiajia Lang, Jin Zhang, Pengbing Mi, B. Kobe, and Faming Wang. The jak-stat pathway: from structural biology to cytokine engineering. Signal Transduction and Targeted Therapy, Aug 2024. URL: https://doi.org/10.1038/s41392-024-01934-w, doi:10.1038/s41392-024-01934-w. This article has 137 citations and is from a peer-reviewed journal.

44. (zhou2023structuralinsightsinto pages 9-10): Yi Zhou, Panayiotis E. Stevis, Jing Cao, Kei Saotome, Jiaxi Wu, Arielle Glatman Zaretsky, Sokol Haxhinasto, George D. Yancopoulos, Andrew J. Murphy, Mark W. Sleeman, William C. Olson, and Matthew C. Franklin. Structural insights into the assembly of gp130 family cytokine signaling complexes. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade4395, doi:10.1126/sciadv.ade4395. This article has 58 citations and is from a highest quality peer-reviewed journal.

45. (zhou2023structuralinsightsinto pages 11-12): Yi Zhou, Panayiotis E. Stevis, Jing Cao, Kei Saotome, Jiaxi Wu, Arielle Glatman Zaretsky, Sokol Haxhinasto, George D. Yancopoulos, Andrew J. Murphy, Mark W. Sleeman, William C. Olson, and Matthew C. Franklin. Structural insights into the assembly of gp130 family cytokine signaling complexes. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade4395, doi:10.1126/sciadv.ade4395. This article has 58 citations and is from a highest quality peer-reviewed journal.

46. (zhou2023structuralinsightsinto pages 6-7): Yi Zhou, Panayiotis E. Stevis, Jing Cao, Kei Saotome, Jiaxi Wu, Arielle Glatman Zaretsky, Sokol Haxhinasto, George D. Yancopoulos, Andrew J. Murphy, Mark W. Sleeman, William C. Olson, and Matthew C. Franklin. Structural insights into the assembly of gp130 family cytokine signaling complexes. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade4395, doi:10.1126/sciadv.ade4395. This article has 58 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](il6_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](il6_signaling-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](il6_signaling-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. sarapultsev2023jakstatsignalingin pages 4-5
2. lv2024thejakstatpathway pages 11-12
3. lv2024thejakstatpathway pages 12-15
4. millrine2022makingsenseof pages 5-6
5. zhou2023structuralinsightsinto pages 1-1
6. gardner2024structuralinsightsinto pages 1-2
7. metcalfe2023structuresofthe pages 3-5
8. philips2022thejakstatpathway pages 4-6
9. wang2022classicalsignalingand pages 2-4
10. wang2022classicalsignalingand pages 11-12
11. millrine2022makingsenseof pages 4-5
12. lv2024thejakstatpathway pages 3-4
13. millrine2022makingsenseof pages 1-2
14. millrine2022makingsenseof pages 9-11
15. zhou2023structuralinsightsinto pages 9-10
16. xue2023evolvingcognitionof pages 2-3
17. metcalfe2023structuresofthe pages 1-2
18. millrine2022makingsenseof pages 2-4
19. song2023experimentbasedcomputationalmodel pages 1-2
20. chakraborty2022areviewon pages 2-5
21. low2022thesuppressorof pages 2-3
22. xue2023evolvingcognitionof pages 1-2
23. park2023exploringthejakstat pages 5-7
24. zhou2023structuralinsightsinto pages 11-12
25. zhou2023structuralinsightsinto pages 6-7
26. https://doi.org/10.1038/s41392-024-01934-w,
27. https://doi.org/10.1186/s43556-023-00151-1,
28. https://doi.org/10.1038/s41577-023-00856-y,
29. https://doi.org/10.2147/itt.s485684,
30. https://doi.org/10.1002/1873-3468.14201,
31. https://doi.org/10.1038/s41392-023-01468-7,
32. https://doi.org/10.1126/sciadv.ade4395,
33. https://doi.org/10.1038/s41467-023-42754-w,
34. https://doi.org/10.1038/s41540-023-00308-2,
35. https://doi.org/10.3389/fimmu.2024.1393799,
36. https://doi.org/10.21608/resoncol.2022.114548.1159,
37. https://doi.org/10.1002/rmv.2300,
38. https://doi.org/10.1007/s10875-023-01603-7,
39. https://doi.org/10.1007/s10875-023-01517-4,
40. https://doi.org/10.1016/j.cell.2022.09.023,
41. https://doi.org/10.3390/ijms241813764,
42. https://doi.org/10.1038/s41467-024-46235-6,
43. https://doi.org/10.3390/ijms23042019,