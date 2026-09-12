---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T18:32:42.843063'
end_time: '2026-06-28T19:00:28.327876'
duration_seconds: 1665.48
template_file: templates/module_research.md.j2
template_variables:
  module_title: Nodal signaling pathway module
  module_summary: Nodal/TGF-beta family ligands use EGF-CFC co-receptors and activin-class
    receptors to activate SMAD2/3 transcriptional programs for embryonic axis formation
    and cell-fate decisions.
  module_outline: "- Nodal signaling pathway\n  - 1. nodal coreceptor engagement\n\
    \  - Nodal coreceptor engagement\n    - Nodal ligand (molecular player: Nodal\
    \ ligand family/ortholog group)\n    - CRIPTO co-receptor (molecular player: CRIPTO)\n\
    \  - 2. nodal receptor activation\n  - Nodal receptor activation\n    - ACVR1B\
    \ type I receptor (molecular player: ACVR1B)\n    - ACVR2B type II receptor (molecular\
    \ player: ACVR2B)\n  - 3. nodal smad output\n  - Nodal SMAD output\n    - SMAD2\
    \ transcriptional effector (molecular player: SMAD2)\n    - SMAD3 transcriptional\
    \ effector (molecular player: SMAD3)\n    - SMAD4 common mediator (molecular player:\
    \ SMAD4)"
  module_connections: '- Nodal coreceptor engagement causes Nodal receptor activation:
    The initiating event promotes nodal receptor activation.

    - Nodal receptor activation causes Nodal SMAD output: Nodal receptor activation
    leads to nodal smad output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 3
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: nodal_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: nodal_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: nodal_signaling-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: image-1.png
  path: nodal_signaling-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: 'Image artifact created (ID artifact-02): ''Nodal Signaling Pathway
    Module'' ![Nodal Signaling Pathway Module](artifact:artifact-02) Artifact IDs
    that may be injec'
---

## Question

# Commissioned Review Brief

## Review Topic

Nodal signaling pathway module

## Working Scope

Nodal/TGF-beta family ligands use EGF-CFC co-receptors and activin-class receptors to activate SMAD2/3 transcriptional programs for embryonic axis formation and cell-fate decisions.

## Provisional Biological Outline

- Nodal signaling pathway
  - 1. nodal coreceptor engagement
  - Nodal coreceptor engagement
    - Nodal ligand (molecular player: Nodal ligand family/ortholog group)
    - CRIPTO co-receptor (molecular player: CRIPTO)
  - 2. nodal receptor activation
  - Nodal receptor activation
    - ACVR1B type I receptor (molecular player: ACVR1B)
    - ACVR2B type II receptor (molecular player: ACVR2B)
  - 3. nodal smad output
  - Nodal SMAD output
    - SMAD2 transcriptional effector (molecular player: SMAD2)
    - SMAD3 transcriptional effector (molecular player: SMAD3)
    - SMAD4 common mediator (molecular player: SMAD4)

## Known Relationships Among Steps

- Nodal coreceptor engagement causes Nodal receptor activation: The initiating event promotes nodal receptor activation.
- Nodal receptor activation causes Nodal SMAD output: Nodal receptor activation leads to nodal smad output.

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

Nodal signaling pathway module

## Working Scope

Nodal/TGF-beta family ligands use EGF-CFC co-receptors and activin-class receptors to activate SMAD2/3 transcriptional programs for embryonic axis formation and cell-fate decisions.

## Provisional Biological Outline

- Nodal signaling pathway
  - 1. nodal coreceptor engagement
  - Nodal coreceptor engagement
    - Nodal ligand (molecular player: Nodal ligand family/ortholog group)
    - CRIPTO co-receptor (molecular player: CRIPTO)
  - 2. nodal receptor activation
  - Nodal receptor activation
    - ACVR1B type I receptor (molecular player: ACVR1B)
    - ACVR2B type II receptor (molecular player: ACVR2B)
  - 3. nodal smad output
  - Nodal SMAD output
    - SMAD2 transcriptional effector (molecular player: SMAD2)
    - SMAD3 transcriptional effector (molecular player: SMAD3)
    - SMAD4 common mediator (molecular player: SMAD4)

## Known Relationships Among Steps

- Nodal coreceptor engagement causes Nodal receptor activation: The initiating event promotes nodal receptor activation.
- Nodal receptor activation causes Nodal SMAD output: Nodal receptor activation leads to nodal smad output.

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

# The Nodal Signaling Pathway Module: A Review of Core Mechanisms, Variation, and Open Questions

## 1. Executive Summary

The Nodal signaling pathway is a TGF-β superfamily cascade that emerged during bilaterian evolution and plays indispensable roles in vertebrate embryonic axis formation, germ-layer specification, left-right asymmetry determination, and pluripotency maintenance (kholtei2025nodalsignalinga pages 1-3, kholtei2025nodalsignalinga pages 3-4). The pathway module can be decomposed into three obligatory steps: (i) engagement of the Nodal–GDF1/3 ligand complex with activin-class type II receptors and EGF-CFC co-receptors; (ii) trans-phosphorylation and activation of type I receptors (principally ALK4/ACVR1B); and (iii) phosphorylation of the receptor-regulated SMADs (SMAD2/3), their heterocomplex formation with SMAD4, nuclear translocation, and partnership with context-specific transcription cofactors (FoxH1, Mixer, Eomes) to activate target gene programs (preiss2022regulationofnodal pages 1-2, kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 6-8). What distinguishes Nodal from other activin-class ligands—most notably Activin A itself—is its obligate requirement for a GPI-anchored EGF-CFC co-receptor (Cripto-1/TDGF1 in mammals, One-eyed pinhead in zebrafish) and its sensitivity to the secreted inhibitor Lefty, which constitutes a reaction-diffusion feedback loop critical for spatial patterning (kholtei2025nodalsignalinga pages 22-24, kholtei2025nodalsignalinga pages 3-4).

The following schematic diagram illustrates the three core steps of the Nodal signaling module:

![Nodal Signaling Pathway Module](artifact:artifact-02)

*Image: Schematic overview of canonical Nodal signaling from extracellular ligand/coreceptor engagement through activin-class receptor activation to SMAD2/3-dependent nuclear transcriptional output. The diagram emphasizes Cripto/TDGF1-mediated assembly of the Nodal receptor complex, extracellular inhibition by Lefty and Cerberus/DAN factors, and downstream control of developmental gene programs.*

## 2. Definition and Biological Boundaries

### What is included

The Nodal signaling module encompasses the minimal set of molecular events from extracellular ligand presentation through intracellular SMAD-dependent transcriptional activation. Core components include: Nodal-family ligands (and their GDF1/GDF3/Vg1 heterodimer partners), the EGF-CFC co-receptors (Cripto-1/TDGF1, Cryptic/CFC1, or Oep), activin-class type I receptors (ACVR1B/ALK4, and in some contexts ACVR1C/ALK7), type II receptors (ACVR2A and ACVR2B), the receptor-regulated SMADs (SMAD2 and SMAD3), the common mediator SMAD4, and the principal transcription cofactors that partner with nuclear SMAD complexes (kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 6-8). The pathway's extracellular negative regulators—Lefty proteins, Cerberus/DAN-family antagonists, and Dand5—are essential for confining signaling domains and should be considered integral to the module's regulatory architecture (kholtei2025nodalsignalinga pages 18-20, kholtei2025nodalsignalinga pages 6-8).

### Neighboring pathways that should be distinguished

Several related processes are often conflated with Nodal signaling but operate through partially or fully distinct mechanisms:

- **Activin signaling.** While Activin A signals through the same type I (ALK4) and type II (ACVR2A/B) receptors and activates the same SMAD2/3 effectors, it does **not** require EGF-CFC co-receptors and is **not** inhibited by Lefty proteins (kholtei2025nodalsignalinga pages 3-4). These distinctions make Activin signaling a distinct module that shares downstream machinery but diverges at the ligand-engagement step.

- **BMP signaling.** BMP/GDF/AMH subfamily members activate SMAD1/5/8 rather than SMAD2/3, utilizing distinct type I receptors (ALK2, ALK3, ALK6) and representing a fundamentally different intracellular output (kholtei2025nodalsignalinga pages 3-4).

- **Non-canonical Cripto-1 signaling.** Cripto-1 has functions independent of Nodal, including interaction with GRP78 to activate Src/PI3K/AKT and MAPK signaling, enhancement of Wnt/β-catenin signaling through LRP5/6, and inhibition of TGF-β1 and Activin signaling (arboretto2021newinsightsinto pages 2-4, pawlak2022tgf‐βsuperfamilyco‐receptors pages 10-12, arboretto2021newinsightsinto pages 10-11). These activities are biologically important, particularly in cancer, but lie outside the canonical Nodal–SMAD2/3 module.

## 3. Mechanistic Overview

The best current model for the Nodal signaling cascade, supported by structural modeling, surface plasmon resonance, and genetic evidence, proceeds through three sequential, obligatory steps (chu2025cripto‐1actsas pages 12-13, chu2025cripto‐1actsas pages 1-2, preiss2022regulationofnodal pages 1-2). The following table summarizes these steps:

| Step Number | Step Name | Key Events | Molecular Players | Obligatory vs Conditional | Evidence/Notes |
|---|---|---|---|---|---|
| 1 | Nodal coreceptor engagement | Secreted Nodal, often functioning as a Nodal–GDF3/GDF1 heterodimer, first engages activin-class type II receptor(s); the EGF-CFC co-receptor (Cripto/TDGF1, Cryptic/CFC1, or Oep depending on species) bridges Nodal to the type I receptor ALK4/ACVR1B, enabling assembly of a signaling-competent complex. This differs from canonical Activin signaling, where the ligand itself can bridge receptors without EGF-CFC assistance. | Nodal; GDF3/GDF1; ACVR2B/ActRIIB (and ACVR2A in some contexts); Cripto/TDGF1, Cryptic/CFC1, Oep; ACVR1B/ALK4 (sometimes ALK7/ACVR1C in specific contexts) | **Obligatory** for canonical Nodal signaling through ALK4 in vertebrate embryos; **conditional/lineage-specific** variation in use of ALK7 and in EGF-CFC dependence outside vertebrates or in noncanonical assay systems | Structural and cell-based work supports a model in which Nodal binds type II receptor and Cripto acts as a molecular bridge to ALK4 via distinct domains; endogenous Nodal ligands are frequently Nodal–GDF3/GDF1 heterodimers, which are more potent and required for efficient secretion/signaling in several systems (chu2025cripto‐1actsas pages 12-13, chu2025cripto‐1actsas pages 1-2, kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 3-4) |
| 2 | Nodal receptor activation | Assembly of the receptor complex allows the constitutively active type II receptor kinase to phosphorylate the GS domain of the type I receptor, generating an active activin-class receptor complex, typically conceptualized as a heterotetrameric signaling assembly. Receptor abundance can also shape ligand distribution by hindering diffusion and restricting signaling range. | ACVR2B/ActRIIB, ACVR2A/ActRIIA; ACVR1B/ALK4; EGF-CFC co-receptor; Nodal–GDF3/GDF1 ligand complex | **Obligatory** for canonical signaling; receptor composition shows **conditional** redundancy and species-specific paralog use (e.g., zebrafish Acvr1b-a/Acvr1b-b) | In zebrafish, Acvr1b-a and Acvr1b-b act redundantly as major type I mediators of Nodal signaling, while Acvr2-family receptors are partly redundant and can have Nodal-independent developmental roles. Type I receptors and co-receptors also modulate Nodal spread, indicating that receptor engagement is both a signaling and gradient-shaping step (preiss2022regulationofnodal pages 1-2, preiss2022regulationofnodal pages 4-5, preiss2022regulationofnodal pages 18-19, preiss2022regulationofnodal pages 11-13, preiss2022regulationofnodal pages 5-6) |
| 3 | Nodal SMAD output | Activated type I receptor phosphorylates SMAD2 and SMAD3 at the C-terminal SSXS motif; phosphorylated SMAD2/3 recruit SMAD4, accumulate in the nucleus, and cooperate with transcription factors/cofactors such as FoxH1, Mixer, and Eomes to activate context-specific target genes controlling pluripotency, mesendoderm specification, organizer function, and left-right patterning. | SMAD2; SMAD3; SMAD4; FoxH1; Mixer; Eomes; target loci including mesoderm/endoderm regulators | **Obligatory** for canonical transcriptional output; partner choice is **conditional** on cell state, developmental stage, and chromatin context | Nuclear SMAD2/3-SMAD4 complexes are the canonical effectors of Nodal signaling. FoxH1 is a central DNA-binding cofactor for many embryonic Nodal responses, while Eomes and Mixer help specify endoderm/mesendoderm programs. Current reviews emphasize that SMAD partner switching underlies the transition from pluripotency maintenance to lineage induction (kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 11-12, kholtei2025nodalsignalinga pages 9-11) |


*Table: This table summarizes the three obligatory mechanistic steps in the Nodal signaling module, from ligand/coreceptor engagement to receptor activation and SMAD-dependent transcriptional output. It is useful as a compact pathway scaffold for interpreting species variation, regulatory boundaries, and experimental evidence.*

### Step 1: Coreceptor Engagement

Nodal ligands are secreted as pro-proteins, frequently forming heterodimers with GDF1/GDF3/Vg1 family members. In zebrafish, Gdf3 is maternally provided and binds to Nodal ligands to generate heterodimers that are more potent and secreted more efficiently than Nodal homodimers; notably, the Gdf3 monomer alone is retained in the endoplasmic reticulum (kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 3-4). Once secreted, the Nodal–GDF heterodimer is processed extracellularly by proprotein convertases Furin and Pace4, which excise the mature domains from prodomains (kholtei2025nodalsignalinga pages 4-6).

The mature Nodal ligand first binds to the constitutively active type II receptor ACVR2B (ActRIIB) on the cell surface. Critically, Nodal cannot independently recruit the type I receptor ALK4 (ACVR1B) and requires the GPI-anchored EGF-CFC co-receptor Cripto-1 (TDGF1) to bridge this interaction. Recent structural work using AlphaFold3 modeling and SPR-based analyses has clarified that Cripto-1 uses its EGF-like domain to bind Nodal at a conserved epitope containing fucosylated threonine 88, while its CFC domain binds ALK4, thereby bringing the type I receptor into proximity with the Nodal-bound type II receptor to form a 2:2:2 stoichiometric signaling complex (chu2025cripto‐1actsas pages 12-13, chu2025cripto‐1actsas pages 1-2, chu2025cripto‐1actsas pages 10-12). This "molecular bridge" mechanism is unique within the TGF-β superfamily: most other family members directly bridge both receptor types without co-receptor assistance (chu2025cripto‐1actsas pages 12-13).

### Step 2: Receptor Activation

Upon assembly of the ternary ligand–co-receptor–receptor complex, the constitutively active type II receptor kinase phosphorylates the GS domain of the type I receptor ALK4, activating its kinase function (preiss2022regulationofnodal pages 1-2, arboretto2021newinsightsinto pages 1-2). In zebrafish, two paralogous type I receptors—Acvr1b-a and Acvr1b-b—redundantly serve as the major Nodal signal transducers; loss of either alone produces no obvious phenotype, but combined loss phenocopies Nodal loss-of-function (preiss2022regulationofnodal pages 4-5, preiss2022regulationofnodal pages 1-2). The type II receptors (Acvr2 family) function partly redundantly, and evidence suggests they have some Nodal-independent developmental roles (preiss2022regulationofnodal pages 1-2).

A key finding is that receptor abundance directly modulates Nodal ligand distribution: feedback-regulated type I receptors and co-receptors hinder Nodal diffusion, with overexpression of the co-receptor Oep reducing Nodal diffusivity by over 90%, causing ligands to form membrane-associated clusters (preiss2021functionalcharacterizationof pages 27-31, preiss2022regulationofnodal pages 18-19, preiss2021functionalcharacterizationof pages 54-60). This receptor-mediated regulation of morphogen spread provides a mechanism for spatially restricting Nodal signaling during germ-layer patterning (preiss2021functionalcharacterizationof pages 147-149, preiss2022regulationofnodal pages 1-2).

### Step 3: SMAD Output

Activated ALK4 phosphorylates the C-terminal SSXS motif of SMAD2 and SMAD3, the receptor-regulated SMADs for this pathway branch (preiss2022regulationofnodal pages 1-2, kholtei2025nodalsignalinga pages 6-8). Phosphorylated SMAD2/3 recruit the common mediator SMAD4, and the resulting heteromeric complexes (heterodimers or heterotrimers) translocate to the nucleus where they partner with context-specific DNA-binding transcription cofactors—principally FoxH1, Mixer, and Eomes—to activate target gene programs (kholtei2025nodalsignalinga pages 6-8). SMAD4 activity is further regulated through monoubiquitination by Ectodermin (which limits responsiveness) and deubiquitination by FAM/Usp9x (which promotes signal transduction) (kholtei2025nodalsignalinga pages 6-8).

A critical insight from recent work is that the transcriptional outcome of SMAD2/3 activation depends on cofactor context: during pluripotency maintenance, SMAD2/3 complexes with NANOG, OCT4, and SOX2 to sustain the pluripotency network; during gastrulation, SMAD2/3 shifts partners to FoxH1 for mesoderm gene activation and to EOMES for definitive endoderm specification (kholtei2025nodalsignalinga pages 11-12). This partner-switching mechanism underlies the transition from self-renewal to lineage commitment.

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive inventory of the molecular components that define the Nodal signaling module:

| Component | Gene Name(s)/Aliases | Protein Type/Function | Role in Nodal Signaling | Key Model Organisms |
|---|---|---|---|---|
| Nodal ligand family | **NODAL** (mammals); **ndr1/squint**, **ndr2/cyclops**, **southpaw/spaw** (zebrafish); **Xnr1-6** / Xenopus nodal-related genes | Secreted TGF-β family morphogens | Core pathway ligands. Nodal-family ligands specify mesendoderm, pattern the embryonic axis, and establish left-right asymmetry by activating Activin-class receptors and SMAD2/3. In many vertebrate contexts, endogenous high-activity ligands are Nodal-GDF heterodimers rather than Nodal homodimers. (kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 8-9, kholtei2025nodalsignalinga pages 3-4) | Mouse, human, zebrafish, Xenopus, chick; spiralians for asymmetry studies |
| GDF1/GDF3/Vg1 heterodimer partner | **GDF1** (mouse); **GDF3** (zebrafish); **Vg1/GDF1/3** family | Secreted TGF-β family ligand partner | Forms Nodal-GDF1/3 heterodimers that increase secretion, potency, and/or signaling range. GDF3 is often retained in the ER unless heterodimerized with Nodal; heterodimers are considered major endogenous Nodal ligands in vertebrates. (kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 3-4) | Mouse, zebrafish, Xenopus |
| EGF-CFC co-receptors | **TDGF1/CRIPTO-1/CR-1**, **CFC1/Cryptic**, **oep/one-eyed pinhead** | GPI-anchored EGF-CFC family co-receptors | Obligatory co-receptors for canonical vertebrate Nodal signaling. Cripto/Oep binds Nodal with its EGF-like domain and ALK4 with its CFC domain, bridging ligand to type I receptor and enabling SMAD2/3 activation. EGF-CFC dependence appears strongest in vertebrates and is evolutionarily derived. (chu2025cripto‐1actsas pages 12-13, chu2025cripto‐1actsas pages 1-2, chu2025cripto‐1actsas pages 10-12, truchadogarcia2023asmallchange pages 2-3, truchadogarcia2023asmallchange pages 1-2) | Human, mouse, zebrafish, Xenopus |
| Type I receptors | **ACVR1B/ALK4/ActRIB**; **ACVR1C/ALK7**; zebrafish **acvr1b-a**, **acvr1b-b** | Transmembrane serine/threonine kinase receptors (type I) | Activated by type II receptors after assembly of the Nodal receptor complex. ALK4 is the best-supported core type I receptor; ALK7 can support signaling in some contexts. In zebrafish, Acvr1b-a and Acvr1b-b act redundantly as major Nodal receptors during early embryogenesis. (arboretto2021newinsightsinto pages 1-2, pawlak2022tgf‐βsuperfamilyco‐receptors pages 10-12, preiss2022regulationofnodal pages 1-2, preiss2022regulationofnodal pages 4-5, preiss2022regulationofnodal pages 5-6) | Mouse, human, zebrafish, Xenopus |
| Type II receptors | **ACVR2A/ActRIIA**, **ACVR2B/ActRIIB**; zebrafish **acvr2a-a**, **acvr2a-b**, **acvr2b-a**, **acvr2b-b** | Transmembrane serine/threonine kinase receptors (type II) | Bind Nodal-family ligands and phosphorylate type I receptors in the assembled receptor complex. ACVR2B is a major Nodal-binding receptor; in zebrafish, Acvr2 family members contribute redundantly and partly independently of Nodal to early patterning. (chu2025cripto‐1actsas pages 1-2, preiss2022regulationofnodal pages 1-2, preiss2022regulationofnodal pages 11-13, preiss2022regulationofnodal pages 5-6) | Mouse, human, zebrafish, Xenopus |
| SMAD2 | **SMAD2** | Receptor-regulated SMAD (R-SMAD) transcriptional effector | Phosphorylated downstream of activated ALK4/7, then complexes with SMAD4 and enters the nucleus. Central for pluripotency maintenance and mesendoderm induction; partner switching from NANOG/OCT4/SOX2 to FOXH1/EOMES contributes to lineage transition. (kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 11-12, kholtei2025nodalsignalinga pages 9-11, kholtei2025nodalsignalinga pages 15-17) | Mouse, human, zebrafish, Xenopus |
| SMAD3 | **SMAD3** | Receptor-regulated SMAD (R-SMAD) transcriptional effector | Works with SMAD2 downstream of Nodal/Activin receptors to regulate transcription. Most developmental Nodal literature treats SMAD2/3 jointly; distinct division of labor remains less clearly resolved than for SMAD2. (kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 3-4) | Mouse, human, zebrafish, Xenopus |
| SMAD4 | **SMAD4** | Common-mediator SMAD (co-SMAD) | Forms heteromeric complexes with phosphorylated SMAD2/3 and is required for nuclear signal transduction to target genes. Its activity is modulated by ubiquitination/deubiquitination mechanisms in developmental contexts. (arboretto2021newinsightsinto pages 1-2, preiss2022regulationofnodal pages 1-2, kholtei2025nodalsignalinga pages 6-8) | Broadly conserved across vertebrates |
| Transcription cofactor | **FOXH1/Fast1/FoxH1** | Forkhead transcription factor | Canonical DNA-binding SMAD cofactor for many Nodal target enhancers; mediates autoregulation and mesoderm/endoderm gene activation downstream of SMAD2/3-SMAD4 complexes. (kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 15-17) | Mouse, zebrafish, Xenopus |
| Transcription cofactor | **Mixer/Mix/Mixl1 family** | Homeobox transcription factor/cofactor | Cooperates with SMAD2/3-SMAD4 in endomesodermal transcriptional programs, especially endoderm-associated gene activation. (kholtei2025nodalsignalinga pages 6-8) | Xenopus, zebrafish, mouse |
| Transcription cofactor | **EOMES/Eomesodermin** | T-box transcription factor | Cooperates with SMAD2/3 in the shift from pluripotency to definitive endoderm specification; a key context-setting factor for Nodal output during gastrulation. (kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 11-12) | Mouse, human, zebrafish |
| Extracellular inhibitor | **LEFTY1**, **LEFTY2** | Secreted atypical TGF-β family antagonists | Induced by Nodal and inhibit Nodal extracellularly by binding ligand and/or interfering with ligand-coreceptor-receptor interactions. Diffuse faster than Nodal and form a reaction-diffusion negative-feedback system that restricts signaling domains; notably do **not** inhibit Activin equivalently. (kholtei2025nodalsignalinga pages 22-24, kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 3-4) | Mouse, zebrafish, frog, chick, human systems |
| Extracellular inhibitor | **Cerberus/Cer1/Cerl**, DAN-family antagonists; zebrafish **Charon**; Xenopus **Coco** | Secreted extracellular antagonists | Bind Nodal-family ligands and inhibit receptor engagement. Important pathway modulators but best treated as regulators of the module rather than core signal-transducing components. (kholtei2025nodalsignalinga pages 6-8) | Mouse, Xenopus, zebrafish |
| Extracellular inhibitor | **Dand5/Cerl2/Coco/Charon** | Secreted DAN-family antagonist | Left-right patterning regulator that suppresses Nodal/GDF1 activity, especially on the right side of the embryo; helps confine laterality signals before left LPM amplification. (kholtei2025nodalsignalinga pages 18-20) | Mouse, zebrafish, Xenopus |
| Proprotein convertase | **FURIN** | Proprotein convertase subtilisin/kexin family protease | Processes secreted Nodal-GDF heterodimer precursors by cleaving prodomains to release mature ligands; extracellular processing is emphasized in recent syntheses. (kholtei2025nodalsignalinga pages 4-6) | Mouse, zebrafish, vertebrates broadly |
| Proprotein convertase | **PACE4/PCSK6** | Proprotein convertase subtilisin/kexin family protease | Functions with Furin in proteolytic maturation of Nodal-family precursors; contributes to generating active extracellular ligand. (kholtei2025nodalsignalinga pages 4-6) | Mouse, zebrafish, vertebrates broadly |


*Table: This table summarizes the main ligands, co-receptors, receptors, SMAD effectors, cofactors, and extracellular regulators that define the Nodal signaling module. It is useful for distinguishing obligatory signal-transduction components from important modulators and for tracking organism-specific naming conventions.*

### Ligand complexity

The endogenous signaling ligand in many vertebrate contexts is not the Nodal homodimer but rather the Nodal–GDF3 (or Nodal–GDF1/Vg1) heterodimer, which enables more rapid and potent SMAD2/3 activation, particularly at low Nodal concentrations (kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 3-4). Heterodimerization is also required for efficient GDF3 secretion, as GDF3 monomers are retained in the ER—a mechanism also observed for some BMP ligands (kholtei2025nodalsignalinga pages 4-6).

### Extracellular regulation

The Nodal–Lefty system constitutes a reaction-diffusion network: Lefty proteins, induced by Nodal itself, diffuse faster than Nodal ligands (demonstrated in zebrafish, frog, chick, mouse, and human cell systems) and inhibit signaling by binding Nodal ligands and interfering with EGF-CFC co-receptor interactions (kholtei2025nodalsignalinga pages 22-24, kholtei2025nodalsignalinga pages 6-8). This creates a spatial pattern where Nodal activity is confined near its source while Lefty expands outward to set signaling boundaries. Cerberus/DAN-family antagonists (Dand5/Cerl2/Charon/Coco) provide additional layer regulation, particularly in left-right patterning where Dand5 suppresses Nodal activity on the right side of the embryo through heparan sulfate proteoglycan-mediated immobilization (kholtei2025nodalsignalinga pages 18-20, kholtei2025nodalsignalinga pages 6-8).

## 5. Evolutionary and Cell-Biological Variation

### Deep evolutionary origins

Nodal genes are found exclusively in Bilateria and have not been identified in pre-bilaterian clades (kholtei2025nodalsignalinga pages 3-4). Within bilaterians, Nodal orthologs are widespread in deuterostomes and have also been found in lophotrochozoans (spiralians), but are notably absent from Ecdysozoa (insects, nematodes), suggesting independent loss in that clade (truchadogarcia2023asmallchange pages 2-3, kholtei2025nodalsignalinga pages 3-4). The associated signaling components—EGF-CFC co-receptors, Lefty inhibitors, GDF1/3 heterodimerization partners—all appeared during bilaterian evolution (kholtei2025nodalsignalinga pages 3-4).

### EGF-CFC co-receptor evolution

EGF-CFC proteins were previously thought to be deuterostome-specific, but orthologs have been identified in gastropod mollusks, annelids, and brachiopods, providing the first evidence of their presence in non-deuterostomes (truchadogarcia2023asmallchange pages 2-3). All EGF-CFC orthologs share a conserved structure with EGF-like, CFC, and GPI-anchoring domains (truchadogarcia2023asmallchange pages 3-6). However, a key functional residue—threonine 88 (T88), which is critical for Nodal-Cripto interaction—is conserved only in deuterostomes; spiralian orthologs have variable residues (leucine/arginine in gastropods, methionine/isoleucine in annelids) at this position (truchadogarcia2023asmallchange pages 3-6). A single amino acid change (L56T) in the chordate ancestor appears to have been a key gain-of-function event that allowed EGF-CFC to participate in Nodal pathway regulation and left-right asymmetry (truchadogarcia2023asmallchange pages 1-2, truchadogarcia2023asmallchange pages 10-11). Functional experiments in gastropods demonstrate that EGF-CFC does not regulate left-right asymmetry in snails, despite being present, whereas injection of the chordate version into zebrafish can rescue left-right patterning defects (truchadogarcia2023asmallchange pages 1-2).

### Species-specific variation

Across vertebrates, the Nodal pathway is highly conserved in its core mechanism but shows lineage-specific elaboration in gene number and deployment:

- **Mouse:** A single Nodal gene; two EGF-CFC genes (Cripto/Tdgf1 and Cryptic/Cfc1); canonical roles in gastrulation, left-right patterning, and pluripotency maintenance of the postimplantation epiblast (truchadogarcia2023asmallchange pages 1-2, kholtei2025nodalsignalinga pages 8-9, kholtei2025nodalsignalinga pages 15-17).
- **Zebrafish:** Multiple Nodal paralogs (ndr1/Squint, ndr2/Cyclops, and Southpaw for left-right patterning); a single EGF-CFC gene (oep); duplicated type I receptors Acvr1b-a and Acvr1b-b acting redundantly (truchadogarcia2023asmallchange pages 1-2, preiss2022regulationofnodal pages 4-5, preiss2022regulationofnodal pages 1-2).
- **Xenopus:** Multiple Nodal-related genes (Xnr1-6) (truchadogarcia2023asmallchange pages 15-15).
- **Spiralians:** In gastropods, Nodal regulates shell chirality through asymmetric expression, but operates independently of EGF-CFC co-receptors (truchadogarcia2023asmallchange pages 2-3).
- **Annelids:** Activin/Nodal signaling mediates dorsal-ventral axis formation, with the organizing signal required through the 16-cell stage in Chaetopterus (truchadogarcia2023asmallchange pages 2-3).

### Cell-type and stage-specific variation

Nodal's transcriptional outputs are context-dependent. In the peri-implantation epiblast, Nodal/Activin signaling maintains pluripotency by driving SMAD2/3 interaction with NANOG and OCT4 at pluripotency gene promoters (kholtei2025nodalsignalinga pages 11-12, kholtei2025nodalsignalinga pages 9-11). During gastrulation, a partner switch occurs: SMAD2/3 disengages from pluripotency factors and binds FoxH1 for mesoderm specification and EOMES for endoderm commitment (kholtei2025nodalsignalinga pages 11-12). High or sustained Nodal signaling preferentially induces endoderm, while lower or shorter exposure suffices for mesodermal gene expression, consistent with a concentration- and duration-dependent morphogen model (kholtei2025nodalsignalinga pages 12-14, kholtei2025nodalsignalinga pages 14-15).

## 6. Constraints, Dependencies, and Failure Modes

### Ordered steps and obligatory dependencies

The pathway proceeds in a strict sequence: ligand processing → co-receptor/receptor engagement → type I receptor phosphorylation → SMAD2/3 phosphorylation → nuclear translocation → cofactor-dependent transcription. Each step is prerequisite for the next. Loss of any core component—Nodal, the EGF-CFC co-receptor, or SMAD2—results in failure of mesendoderm specification and gastrulation arrest in mouse embryos (kholtei2025nodalsignalinga pages 9-11, kholtei2025nodalsignalinga pages 15-17).

### Mutually exclusive or compartment-specific events

Nodal signaling is spatially restricted by multiple mechanisms: (i) receptor- and co-receptor-mediated diffusion hindrance, which limits ligand spread to approximately one order of magnitude below free diffusivity (~40 μm²/s) (preiss2022regulationofnodal pages 18-19); (ii) the Nodal-Lefty reaction-diffusion system, in which faster-diffusing Lefty creates an inhibitory field surrounding the Nodal signaling domain (kholtei2025nodalsignalinga pages 22-24); and (iii) localized expression of Nodal itself, often reinforced by positive autoregulation through FOXH1-dependent enhancers (kholtei2025nodalsignalinga pages 15-17).

### Stage-specific requirements

Nodal is dispensable for preimplantation pluripotency establishment, where BMP4 and LIF are primary regulators, but is required for postimplantation epiblast pluripotency maintenance and gastrulation (kholtei2025nodalsignalinga pages 8-9, kholtei2025nodalsignalinga pages 9-11). In left-right patterning, Nodal signaling at the left-right organizer precedes and is required for asymmetric Nodal expression in the left lateral plate mesoderm; Lefty1 expression at the midline prevents rightward spread (kholtei2025nodalsignalinga pages 18-20).

### Failure modes

Loss of Nodal or SMAD2 eliminates definitive endoderm and head/trunk mesoderm-derived tissues (kidney, heart, blood, liver, pancreas, notochord) (kholtei2025nodalsignalinga pages 14-15). Loss of Lefty leads to bilateral and precocious Nodal expression, resulting in expanded mesendoderm at the expense of ectoderm (kholtei2025nodalsignalinga pages 18-20). Mutations in EGF-CFC co-receptors (oep in zebrafish, Cripto in mouse) phenocopy Nodal loss-of-function for EGF-CFC-dependent functions while leaving Activin signaling intact (truchadogarcia2023asmallchange pages 1-2).

## 7. Controversies and Open Questions

### Unresolved structural biology

Despite the recent AlphaFold3 models of the Nodal–Cripto-1–ALK4 ternary complex (chu2025cripto‐1actsas pages 1-2), the precise structure of the endogenous Nodal–GDF3 heterodimer in complex with its full receptor assembly remains experimentally unresolved. Whether and how the EGF-CFC co-receptor guides Nodal processing at the cell surface has not been confirmed in vivo (kholtei2025nodalsignalinga pages 4-6).

### SMAD2 versus SMAD3 division of labor

The developmental Nodal literature predominantly treats SMAD2 and SMAD3 as a combined entity. While genetic evidence in mouse clearly demonstrates essential roles for SMAD2 (e.g., in definitive endoderm formation and diapause maintenance), the specific and potentially distinct contributions of SMAD3 to Nodal-driven developmental programs remain incompletely resolved (kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 3-4).

### Mechanism of pluripotency-to-lineage transition

How SMAD2/3 partner-switching occurs—shifting from NANOG/OCT4 to FOXH1/EOMES—is poorly understood at the epigenetic and chromatin level. The molecular mechanisms underlying the synergistic cooperation between Nodal/Activin signaling and other pathways (FGF, BMP) before gastrulation remain poorly defined (kholtei2025nodalsignalinga pages 12-14, kholtei2025nodalsignalinga pages 11-12).

### Cross-species comparability

There is disagreement in the literature regarding LEFTY1 expression in the human anterior visceral endoderm equivalent, with some studies detecting it and others not (kholtei2025nodalsignalinga pages 17-18). More broadly, much of our mechanistic understanding derives from zebrafish and mouse, and caution is warranted when generalizing to other vertebrates or to the diverse spiralian taxa where Nodal functions independently of EGF-CFC co-receptors (truchadogarcia2023asmallchange pages 10-11, truchadogarcia2023asmallchange pages 2-3).

### Nodal in cancer

Nodal and Cripto-1 are re-expressed in many human tumors and cancer stem cells, correlating with worse prognosis (arboretto2021newinsightsinto pages 2-4, arboretto2021newinsightsinto pages 11-13, arboretto2021newinsightsinto pages 4-5). Cripto-1 promotes tumor progression through both canonical SMAD2/3 activation and non-canonical pathways including Src/PI3K/AKT, MAPK, and Wnt/β-catenin signaling, as well as through interaction with GRP78 (arboretto2021newinsightsinto pages 2-4, pawlak2022tgf‐βsuperfamilyco‐receptors pages 24-25, rashwan2025insilicoprediction pages 2-3, pawlak2022tgf‐βsuperfamilyco‐receptors pages 10-12). However, the extent to which Nodal-dependent SMAD2/3 signaling (as opposed to SMAD-independent Cripto-1 signaling) drives cancer phenotypes remains an area of active investigation, and therapeutic strategies targeting these interactions are still in preclinical stages (arboretto2021newinsightsinto pages 7-8, arboretto2021newinsightsinto pages 10-11).

### Novel biological roles

Recent work has uncovered an unexpected role for Nodal/Smad2 signaling in sustaining embryonic diapause (developmental pausing) by repressing Pparg-mediated lipid metabolism, expanding the known functions of this pathway beyond classical morphogen patterning. Nodal signaling appears indispensable for the transcriptional and metabolic reprogramming that enables paused embryonic stem cells and blastocysts to survive unfavorable conditions.

## 8. Key References

The evidence synthesized in this review draws primarily from the following sources:

- Kholtei JE, Codina-Tobias M, Schier AF. *Nodal Signaling: A Paradigm for TGFβ Signaling in Embryonic Development.* Annual Review of Cell and Developmental Biology (2025). DOI: 10.1146/annurev-cellbio-112122-030209 (kholtei2025nodalsignalinga pages 4-6, kholtei2025nodalsignalinga pages 6-8, kholtei2025nodalsignalinga pages 1-3, kholtei2025nodalsignalinga pages 18-20, kholtei2025nodalsignalinga pages 22-24, kholtei2025nodalsignalinga pages 3-4, kholtei2025nodalsignalinga pages 11-12, kholtei2025nodalsignalinga pages 8-9, kholtei2025nodalsignalinga pages 9-11, kholtei2025nodalsignalinga pages 17-18, kholtei2025nodalsignalinga pages 15-17, kholtei2025nodalsignalinga pages 12-14, kholtei2025nodalsignalinga pages 14-15)
- Chu KY, Crawford AN, Krah BS, et al. *Cripto-1 acts as a molecular bridge linking Nodal to ALK4 via distinct structural domains.* Protein Science (2025). DOI: 10.1002/pro.70034 (chu2025cripto‐1actsas pages 12-13, chu2025cripto‐1actsas pages 1-2, chu2025cripto‐1actsas pages 10-12)
- Preiß H, Kögler AC, Mörsdorf D, et al. *Regulation of Nodal signaling propagation by receptor interactions and positive feedback.* eLife (2022). DOI: 10.7554/elife.66397 (preiss2022regulationofnodal pages 1-2, preiss2022regulationofnodal pages 4-5, preiss2022regulationofnodal pages 18-19, preiss2022regulationofnodal pages 11-13, preiss2022regulationofnodal pages 5-6)
- Truchado-García M, Perry KJ, Cavodeassi F, et al. *A Single Residue in EGF-CFC Drives Bilaterian Asymmetry.* Molecular Biology and Evolution (2023). DOI: 10.1093/molbev/msac270 (truchadogarcia2023asmallchange pages 2-3, truchadogarcia2023asmallchange pages 1-2, truchadogarcia2023asmallchange pages 3-6, truchadogarcia2023asmallchange pages 10-11)
- Arboretto P, Cillo M, Leonardi A. *New Insights into Cancer Targeted Therapy: Nodal and Cripto-1 as Attractive Candidates.* International Journal of Molecular Sciences (2021). DOI: 10.3390/ijms22157838 (arboretto2021newinsightsinto pages 1-2, arboretto2021newinsightsinto pages 2-4, arboretto2021newinsightsinto pages 7-8, arboretto2021newinsightsinto pages 10-11, arboretto2021newinsightsinto pages 11-13, arboretto2021newinsightsinto pages 4-5)
- Pawlak JB, Blobe GC. *TGF-β superfamily co-receptors in cancer.* Developmental Dynamics (2022). DOI: 10.1002/dvdy.338 (pawlak2022tgf‐βsuperfamilyco‐receptors pages 10-12, pawlak2022tgf‐βsuperfamilyco‐receptors pages 24-25)
- Liu S, Ren J, Hu Y, et al. *TGFβ family signaling in human stem cell self-renewal and differentiation.* Cell Regeneration (2024). DOI: 10.1186/s13619-024-00207-9 (liu2024tgfβfamilysignaling pages 2-5)
- Preiß H. *Functional characterization of Nodal receptors during early embryonic development in zebrafish.* Universität Tübingen dissertation (2021). DOI: 10.15496/publikation-54015 (preiss2021functionalcharacterizationof pages 27-31, preiss2021functionalcharacterizationof pages 147-149, preiss2021functionalcharacterizationof pages 54-60)
- Rashwan ME, Ahmed MR, Elfiky AA. *In silico prediction of GRP78-CRIPTO binding sites to improve therapeutic targeting in glioblastoma.* Scientific Reports (2025). DOI: 10.1038/s41598-025-00125-z (rashwan2025insilicoprediction pages 2-3)

References

1. (kholtei2025nodalsignalinga pages 1-3): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (kholtei2025nodalsignalinga pages 3-4): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (preiss2022regulationofnodal pages 1-2): Hannes Preiß, Anna C Kögler, David Mörsdorf, Daniel Čapek, Gary H Soh, Katherine W Rogers, Hernán Morales-Navarrete, María Almuedo-Castillo, and Patrick Müller. Regulation of nodal signaling propagation by receptor interactions and positive feedback. eLife, Sep 2022. URL: https://doi.org/10.7554/elife.66397, doi:10.7554/elife.66397. This article has 20 citations and is from a domain leading peer-reviewed journal.

4. (kholtei2025nodalsignalinga pages 4-6): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

5. (kholtei2025nodalsignalinga pages 6-8): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (kholtei2025nodalsignalinga pages 22-24): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

7. (kholtei2025nodalsignalinga pages 18-20): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (arboretto2021newinsightsinto pages 2-4): Paola Arboretto, Michele Cillo, and Antonio Leonardi. New insights into cancer targeted therapy: nodal and cripto-1 as attractive candidates. International Journal of Molecular Sciences, 22:7838, Jul 2021. URL: https://doi.org/10.3390/ijms22157838, doi:10.3390/ijms22157838. This article has 3 citations.

9. (pawlak2022tgf‐βsuperfamilyco‐receptors pages 10-12): John B. Pawlak and Gerard C. Blobe. <scp>tgf</scp>‐β superfamily co‐receptors in cancer. Apr 2022. URL: https://doi.org/10.1002/dvdy.338, doi:10.1002/dvdy.338. This article has 90 citations and is from a peer-reviewed journal.

10. (arboretto2021newinsightsinto pages 10-11): Paola Arboretto, Michele Cillo, and Antonio Leonardi. New insights into cancer targeted therapy: nodal and cripto-1 as attractive candidates. International Journal of Molecular Sciences, 22:7838, Jul 2021. URL: https://doi.org/10.3390/ijms22157838, doi:10.3390/ijms22157838. This article has 3 citations.

11. (chu2025cripto‐1actsas pages 12-13): Kit‐Yee Chu, Amberly N. Crawford, Bradon S. Krah, Vijayalakshmi Thamilselvan, Anjali Malik, Nina A. Aitas, and Erik Martinez‐Hackert. Cripto‐1 acts as a molecular bridge linking nodal to alk4 via distinct structural domains. Protein Science : A Publication of the Protein Society, Jan 2025. URL: https://doi.org/10.1002/pro.70034, doi:10.1002/pro.70034. This article has 4 citations.

12. (chu2025cripto‐1actsas pages 1-2): Kit‐Yee Chu, Amberly N. Crawford, Bradon S. Krah, Vijayalakshmi Thamilselvan, Anjali Malik, Nina A. Aitas, and Erik Martinez‐Hackert. Cripto‐1 acts as a molecular bridge linking nodal to alk4 via distinct structural domains. Protein Science : A Publication of the Protein Society, Jan 2025. URL: https://doi.org/10.1002/pro.70034, doi:10.1002/pro.70034. This article has 4 citations.

13. (preiss2022regulationofnodal pages 4-5): Hannes Preiß, Anna C Kögler, David Mörsdorf, Daniel Čapek, Gary H Soh, Katherine W Rogers, Hernán Morales-Navarrete, María Almuedo-Castillo, and Patrick Müller. Regulation of nodal signaling propagation by receptor interactions and positive feedback. eLife, Sep 2022. URL: https://doi.org/10.7554/elife.66397, doi:10.7554/elife.66397. This article has 20 citations and is from a domain leading peer-reviewed journal.

14. (preiss2022regulationofnodal pages 18-19): Hannes Preiß, Anna C Kögler, David Mörsdorf, Daniel Čapek, Gary H Soh, Katherine W Rogers, Hernán Morales-Navarrete, María Almuedo-Castillo, and Patrick Müller. Regulation of nodal signaling propagation by receptor interactions and positive feedback. eLife, Sep 2022. URL: https://doi.org/10.7554/elife.66397, doi:10.7554/elife.66397. This article has 20 citations and is from a domain leading peer-reviewed journal.

15. (preiss2022regulationofnodal pages 11-13): Hannes Preiß, Anna C Kögler, David Mörsdorf, Daniel Čapek, Gary H Soh, Katherine W Rogers, Hernán Morales-Navarrete, María Almuedo-Castillo, and Patrick Müller. Regulation of nodal signaling propagation by receptor interactions and positive feedback. eLife, Sep 2022. URL: https://doi.org/10.7554/elife.66397, doi:10.7554/elife.66397. This article has 20 citations and is from a domain leading peer-reviewed journal.

16. (preiss2022regulationofnodal pages 5-6): Hannes Preiß, Anna C Kögler, David Mörsdorf, Daniel Čapek, Gary H Soh, Katherine W Rogers, Hernán Morales-Navarrete, María Almuedo-Castillo, and Patrick Müller. Regulation of nodal signaling propagation by receptor interactions and positive feedback. eLife, Sep 2022. URL: https://doi.org/10.7554/elife.66397, doi:10.7554/elife.66397. This article has 20 citations and is from a domain leading peer-reviewed journal.

17. (kholtei2025nodalsignalinga pages 11-12): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

18. (kholtei2025nodalsignalinga pages 9-11): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

19. (chu2025cripto‐1actsas pages 10-12): Kit‐Yee Chu, Amberly N. Crawford, Bradon S. Krah, Vijayalakshmi Thamilselvan, Anjali Malik, Nina A. Aitas, and Erik Martinez‐Hackert. Cripto‐1 acts as a molecular bridge linking nodal to alk4 via distinct structural domains. Protein Science : A Publication of the Protein Society, Jan 2025. URL: https://doi.org/10.1002/pro.70034, doi:10.1002/pro.70034. This article has 4 citations.

20. (arboretto2021newinsightsinto pages 1-2): Paola Arboretto, Michele Cillo, and Antonio Leonardi. New insights into cancer targeted therapy: nodal and cripto-1 as attractive candidates. International Journal of Molecular Sciences, 22:7838, Jul 2021. URL: https://doi.org/10.3390/ijms22157838, doi:10.3390/ijms22157838. This article has 3 citations.

21. (preiss2021functionalcharacterizationof pages 27-31): Hannes Preiß. Functional characterization of nodal receptors during early embryonic development in zebrafish. ArXiv, Dec 2021. URL: https://doi.org/10.15496/publikation-54015, doi:10.15496/publikation-54015. This article has 0 citations.

22. (preiss2021functionalcharacterizationof pages 54-60): Hannes Preiß. Functional characterization of nodal receptors during early embryonic development in zebrafish. ArXiv, Dec 2021. URL: https://doi.org/10.15496/publikation-54015, doi:10.15496/publikation-54015. This article has 0 citations.

23. (preiss2021functionalcharacterizationof pages 147-149): Hannes Preiß. Functional characterization of nodal receptors during early embryonic development in zebrafish. ArXiv, Dec 2021. URL: https://doi.org/10.15496/publikation-54015, doi:10.15496/publikation-54015. This article has 0 citations.

24. (kholtei2025nodalsignalinga pages 8-9): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

25. (truchadogarcia2023asmallchange pages 2-3): Marta Truchado-García, Kimberly J Perry, Florencia Cavodeassi, Nathan J Kenny, Jonathan Q Henry, and Cristina Grande. A small change with a twist ending: a single residue in egf-cfc drives bilaterian asymmetry. Molecular Biology and Evolution, Dec 2023. URL: https://doi.org/10.1093/molbev/msac270, doi:10.1093/molbev/msac270. This article has 4 citations and is from a highest quality peer-reviewed journal.

26. (truchadogarcia2023asmallchange pages 1-2): Marta Truchado-García, Kimberly J Perry, Florencia Cavodeassi, Nathan J Kenny, Jonathan Q Henry, and Cristina Grande. A small change with a twist ending: a single residue in egf-cfc drives bilaterian asymmetry. Molecular Biology and Evolution, Dec 2023. URL: https://doi.org/10.1093/molbev/msac270, doi:10.1093/molbev/msac270. This article has 4 citations and is from a highest quality peer-reviewed journal.

27. (kholtei2025nodalsignalinga pages 15-17): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

28. (truchadogarcia2023asmallchange pages 3-6): Marta Truchado-García, Kimberly J Perry, Florencia Cavodeassi, Nathan J Kenny, Jonathan Q Henry, and Cristina Grande. A small change with a twist ending: a single residue in egf-cfc drives bilaterian asymmetry. Molecular Biology and Evolution, Dec 2023. URL: https://doi.org/10.1093/molbev/msac270, doi:10.1093/molbev/msac270. This article has 4 citations and is from a highest quality peer-reviewed journal.

29. (truchadogarcia2023asmallchange pages 10-11): Marta Truchado-García, Kimberly J Perry, Florencia Cavodeassi, Nathan J Kenny, Jonathan Q Henry, and Cristina Grande. A small change with a twist ending: a single residue in egf-cfc drives bilaterian asymmetry. Molecular Biology and Evolution, Dec 2023. URL: https://doi.org/10.1093/molbev/msac270, doi:10.1093/molbev/msac270. This article has 4 citations and is from a highest quality peer-reviewed journal.

30. (truchadogarcia2023asmallchange pages 15-15): Marta Truchado-García, Kimberly J Perry, Florencia Cavodeassi, Nathan J Kenny, Jonathan Q Henry, and Cristina Grande. A small change with a twist ending: a single residue in egf-cfc drives bilaterian asymmetry. Molecular Biology and Evolution, Dec 2023. URL: https://doi.org/10.1093/molbev/msac270, doi:10.1093/molbev/msac270. This article has 4 citations and is from a highest quality peer-reviewed journal.

31. (kholtei2025nodalsignalinga pages 12-14): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

32. (kholtei2025nodalsignalinga pages 14-15): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

33. (kholtei2025nodalsignalinga pages 17-18): Jakob El Kholtei, Mireia Codina-Tobias, and Alexander F. Schier. Nodal signaling: a paradigm for tgfβ signaling in embryonic development. Annual review of cell and developmental biology, Aug 2025. URL: https://doi.org/10.1146/annurev-cellbio-112122-030209, doi:10.1146/annurev-cellbio-112122-030209. This article has 4 citations and is from a domain leading peer-reviewed journal.

34. (arboretto2021newinsightsinto pages 11-13): Paola Arboretto, Michele Cillo, and Antonio Leonardi. New insights into cancer targeted therapy: nodal and cripto-1 as attractive candidates. International Journal of Molecular Sciences, 22:7838, Jul 2021. URL: https://doi.org/10.3390/ijms22157838, doi:10.3390/ijms22157838. This article has 3 citations.

35. (arboretto2021newinsightsinto pages 4-5): Paola Arboretto, Michele Cillo, and Antonio Leonardi. New insights into cancer targeted therapy: nodal and cripto-1 as attractive candidates. International Journal of Molecular Sciences, 22:7838, Jul 2021. URL: https://doi.org/10.3390/ijms22157838, doi:10.3390/ijms22157838. This article has 3 citations.

36. (pawlak2022tgf‐βsuperfamilyco‐receptors pages 24-25): John B. Pawlak and Gerard C. Blobe. <scp>tgf</scp>‐β superfamily co‐receptors in cancer. Apr 2022. URL: https://doi.org/10.1002/dvdy.338, doi:10.1002/dvdy.338. This article has 90 citations and is from a peer-reviewed journal.

37. (rashwan2025insilicoprediction pages 2-3): Mahmoud E. Rashwan, Mahrous R. Ahmed, and Abdo A. Elfiky. In silico prediction of grp78-cripto binding sites to improve therapeutic targeting in glioblastoma. Scientific Reports, May 2025. URL: https://doi.org/10.1038/s41598-025-00125-z, doi:10.1038/s41598-025-00125-z. This article has 4 citations and is from a peer-reviewed journal.

38. (arboretto2021newinsightsinto pages 7-8): Paola Arboretto, Michele Cillo, and Antonio Leonardi. New insights into cancer targeted therapy: nodal and cripto-1 as attractive candidates. International Journal of Molecular Sciences, 22:7838, Jul 2021. URL: https://doi.org/10.3390/ijms22157838, doi:10.3390/ijms22157838. This article has 3 citations.

39. (liu2024tgfβfamilysignaling pages 2-5): Sijia Liu, Jiang Ren, Yanmei Hu, Fangfang Zhou, and Long Zhang. Tgfβ family signaling in human stem cell self-renewal and differentiation. Cell Regeneration, Nov 2024. URL: https://doi.org/10.1186/s13619-024-00207-9, doi:10.1186/s13619-024-00207-9. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](nodal_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](nodal_signaling-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](nodal_signaling-deep-research-falcon_artifacts/artifact-02.md)
![Image artifact created (ID artifact-02): 'Nodal Signaling Pathway Module' ![Nodal Signaling Pathway Module](artifact:artifact-02) Artifact IDs that may be injec](nodal_signaling-deep-research-falcon_artifacts/image-1.png)

## Citations

1. kholtei2025nodalsignalinga pages 3-4
2. kholtei2025nodalsignalinga pages 4-6
3. preiss2022regulationofnodal pages 1-2
4. kholtei2025nodalsignalinga pages 6-8
5. kholtei2025nodalsignalinga pages 11-12
6. kholtei2025nodalsignalinga pages 18-20
7. truchadogarcia2023asmallchange pages 2-3
8. truchadogarcia2023asmallchange pages 3-6
9. truchadogarcia2023asmallchange pages 1-2
10. truchadogarcia2023asmallchange pages 15-15
11. preiss2022regulationofnodal pages 18-19
12. kholtei2025nodalsignalinga pages 22-24
13. kholtei2025nodalsignalinga pages 15-17
14. kholtei2025nodalsignalinga pages 14-15
15. kholtei2025nodalsignalinga pages 17-18
16. rashwan2025insilicoprediction pages 2-3
17. kholtei2025nodalsignalinga pages 1-3
18. arboretto2021newinsightsinto pages 2-4
19. arboretto2021newinsightsinto pages 10-11
20. preiss2022regulationofnodal pages 4-5
21. preiss2022regulationofnodal pages 11-13
22. preiss2022regulationofnodal pages 5-6
23. kholtei2025nodalsignalinga pages 9-11
24. arboretto2021newinsightsinto pages 1-2
25. preiss2021functionalcharacterizationof pages 27-31
26. preiss2021functionalcharacterizationof pages 54-60
27. preiss2021functionalcharacterizationof pages 147-149
28. kholtei2025nodalsignalinga pages 8-9
29. truchadogarcia2023asmallchange pages 10-11
30. kholtei2025nodalsignalinga pages 12-14
31. arboretto2021newinsightsinto pages 11-13
32. arboretto2021newinsightsinto pages 4-5
33. arboretto2021newinsightsinto pages 7-8
34. Nodal Signaling Pathway Module
35. https://doi.org/10.1146/annurev-cellbio-112122-030209,
36. https://doi.org/10.7554/elife.66397,
37. https://doi.org/10.3390/ijms22157838,
38. https://doi.org/10.1002/dvdy.338,
39. https://doi.org/10.1002/pro.70034,
40. https://doi.org/10.15496/publikation-54015,
41. https://doi.org/10.1093/molbev/msac270,
42. https://doi.org/10.1038/s41598-025-00125-z,
43. https://doi.org/10.1186/s13619-024-00207-9,