---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T16:43:21.867681'
end_time: '2026-06-28T17:04:54.748567'
duration_seconds: 1292.88
template_file: templates/module_research.md.j2
template_variables:
  module_title: PDGFR signaling pathway module
  module_summary: Platelet-derived growth factor ligands activate PDGFR receptor tyrosine
    kinases, recruiting SH2 adaptors and lipid-kinase branches that control mesenchymal
    proliferation, migration, and survival.
  module_outline: "- PDGFR signaling pathway\n  - 1. pdgf ligand-receptor engagement\n\
    \  - PDGF ligand engages PDGFR\n    - PDGFB ligand (molecular player: PDGFB)\n\
    \    - PDGFRB receptor (molecular player: PDGFRB receptor family/ortholog group)\n\
    \  - 2. phosphotyrosine adaptor assembly\n  - PDGFR adaptor assembly\n    - GRB2\
    \ adaptor (molecular player: GRB2 adaptor family/ortholog group)\n    - PI3K p85\
    \ adaptor (molecular player: PI3K p85 adaptor family/ortholog group)\n  - 3. growth\
    \ and migration output\n  - PI3K/MAPK motility output\n    - PI3K catalytic subunit\
    \ (molecular player: PI3K catalytic subunit family/ortholog group)\n    - PDGFR\
    \ receptor scaffold (molecular player: PDGFR receptor scaffold family/ortholog\
    \ group)"
  module_connections: '- PDGF ligand engages PDGFR causes PDGFR adaptor assembly:
    The initiating event promotes phosphotyrosine adaptor assembly.

    - PDGFR adaptor assembly causes PI3K/MAPK motility output: PDGFR adaptor assembly
    leads to growth and migration output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 63
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: pdgfr_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: pdgfr_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: pdgfr_signaling-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Commissioned Review Brief

## Review Topic

PDGFR signaling pathway module

## Working Scope

Platelet-derived growth factor ligands activate PDGFR receptor tyrosine kinases, recruiting SH2 adaptors and lipid-kinase branches that control mesenchymal proliferation, migration, and survival.

## Provisional Biological Outline

- PDGFR signaling pathway
  - 1. pdgf ligand-receptor engagement
  - PDGF ligand engages PDGFR
    - PDGFB ligand (molecular player: PDGFB)
    - PDGFRB receptor (molecular player: PDGFRB receptor family/ortholog group)
  - 2. phosphotyrosine adaptor assembly
  - PDGFR adaptor assembly
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)
  - 3. growth and migration output
  - PI3K/MAPK motility output
    - PI3K catalytic subunit (molecular player: PI3K catalytic subunit family/ortholog group)
    - PDGFR receptor scaffold (molecular player: PDGFR receptor scaffold family/ortholog group)

## Known Relationships Among Steps

- PDGF ligand engages PDGFR causes PDGFR adaptor assembly: The initiating event promotes phosphotyrosine adaptor assembly.
- PDGFR adaptor assembly causes PI3K/MAPK motility output: PDGFR adaptor assembly leads to growth and migration output.

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

PDGFR signaling pathway module

## Working Scope

Platelet-derived growth factor ligands activate PDGFR receptor tyrosine kinases, recruiting SH2 adaptors and lipid-kinase branches that control mesenchymal proliferation, migration, and survival.

## Provisional Biological Outline

- PDGFR signaling pathway
  - 1. pdgf ligand-receptor engagement
  - PDGF ligand engages PDGFR
    - PDGFB ligand (molecular player: PDGFB)
    - PDGFRB receptor (molecular player: PDGFRB receptor family/ortholog group)
  - 2. phosphotyrosine adaptor assembly
  - PDGFR adaptor assembly
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)
  - 3. growth and migration output
  - PI3K/MAPK motility output
    - PI3K catalytic subunit (molecular player: PI3K catalytic subunit family/ortholog group)
    - PDGFR receptor scaffold (molecular player: PDGFR receptor scaffold family/ortholog group)

## Known Relationships Among Steps

- PDGF ligand engages PDGFR causes PDGFR adaptor assembly: The initiating event promotes phosphotyrosine adaptor assembly.
- PDGFR adaptor assembly causes PI3K/MAPK motility output: PDGFR adaptor assembly leads to growth and migration output.

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

# The PDGFR Signaling Pathway Module: A Concise Review

## 1. Executive Summary

The platelet-derived growth factor receptor (PDGFR) signaling module is a prototypical receptor tyrosine kinase (RTK) cascade that governs mesenchymal cell proliferation, migration, and survival. The system comprises four PDGF ligand genes (PDGFA, PDGFB, PDGFC, PDGFD) that form five dimeric ligands, two receptor tyrosine kinases (PDGFRα and PDGFRβ), and a phosphotyrosine-driven adaptor network that branches into PI3K/AKT, RAS/MAPK, PLCγ, and Src-family kinase effector cascades (solinc2022theplateletderivedgrowth pages 3-4, kadrmas2020geneticanalysesin pages 1-2, zhao2026pdgfsignalingin pages 3-5). The pathway is essential for pericyte recruitment, vascular smooth muscle cell biology, organ morphogenesis, wound healing, and connective tissue homeostasis (jung2025rolesofpdgfpdgfr pages 1-2, solinc2022theplateletderivedgrowth pages 7-8). Dysregulation underlies fibrotic diseases, atherosclerosis, and a defined spectrum of neoplastic and developmental disorders (guerit2021pdgfreceptormutations pages 1-2). This review synthesizes the current mechanistic understanding, cell-type variation, evolutionary context, and outstanding controversies of the PDGFR signaling module.

## 2. Definition and Biological Boundaries

### 2.1 Scope

The PDGFR signaling module, as defined here, encompasses: (i) ligand–receptor engagement and receptor dimerization; (ii) receptor trans-autophosphorylation and phosphotyrosine-driven assembly of SH2-domain adaptors; and (iii) the immediate downstream kinase branches—PI3K/AKT, RAS/MAPK, PLCγ, and Src—that collectively drive growth, motility, and survival outputs in mesenchymal lineage cells (solinc2022theplateletderivedgrowth pages 3-4, zhao2026pdgfsignalingin pages 3-5).

### 2.2 Neighboring pathways to distinguish

Several signaling systems overlap with PDGFR signaling and are frequently discussed alongside it but should be treated as distinct modules:

- **VEGF/VEGFR signaling:** PDGFs and VEGFs share a common cystine-knot growth factor superfamily and their receptors belong to related RTK subfamilies (class III and class V, respectively) (rauniyar2023expansionandcollapse pages 3-6, rauniyar2023expansionandcollapse pages 1-3). However, VEGFR signaling operates predominantly in endothelial cells, whereas PDGFR signaling is mesenchymal-centric.
- **KIT/SCF signaling:** c-KIT is a class III RTK structurally related to PDGFRs and often co-targeted by the same tyrosine kinase inhibitors (e.g., imatinib), but its biology is centered on hematopoiesis and melanocyte development.
- **TGF-β/Smad signaling:** Although TGF-β and PDGF pathways converge on fibroblast-to-myofibroblast transition and fibrosis, TGF-β signals through serine/threonine kinase receptors and Smad transcription factors, making it mechanistically distinct.
- **FGF/FGFR signaling:** FGFRs share downstream effectors (GRB2, PI3K) with PDGFRs and can crosstalk via heterotypic receptor interactions, but FGFR biology is distinct in cell-type expression and developmental context.

### 2.3 Competing definitions

Some authors define the "PDGF pathway" broadly to include autocrine and paracrine loops in the tumor microenvironment, stromal–epithelial crosstalk, and non-coding RNA regulatory layers (ma2024targetingpdgfpdgfrsignaling pages 4-6, ma2024targetingpdgfpdgfrsignaling pages 18-19). Others use a narrower biochemical definition restricted to receptor–adaptor–effector wiring. This review adopts an intermediate scope: we include the core biochemical cascade and its principal cell-biological outputs but treat tumor microenvironment biology and non-coding RNA regulation as contextual extensions.

## 3. Mechanistic Overview

### 3.1 Step 1: Ligand–receptor engagement and dimerization

Four PDGF genes encode polypeptide chains that dimerize to form five biologically active ligands: the homodimers PDGF-AA, PDGF-BB, PDGF-CC, and PDGF-DD, plus the heterodimer PDGF-AB (solinc2022theplateletderivedgrowth pages 3-4, kadrmas2020geneticanalysesin pages 1-2, kalra2021roleofpdgfab pages 3-5). PDGF-CC and PDGF-DD are secreted as latent pro-forms requiring proteolytic cleavage for activation (solinc2022theplateletderivedgrowth pages 3-4, jung2025rolesofpdgfpdgfr pages 1-2). Two receptor chains, PDGFRα and PDGFRβ, can form three dimer species: αα, αβ, and ββ. Ligand binding specificity is determined by which PDGF chains engage which receptor chain: PDGFRα binds PDGF-A, PDGF-B, and PDGF-C with high affinity, while PDGFRβ binds PDGF-B and PDGF-D chains (solinc2022theplateletderivedgrowth pages 3-4, jung2025rolesofpdgfpdgfr pages 1-2). PDGF-BB is the universal ligand capable of activating all three receptor dimer combinations, whereas PDGF-AA exclusively activates PDGFRαα homodimers (kadrmas2020geneticanalysesin pages 1-2, kadrmas2020geneticanalysesin pages 4-5).

The following table summarizes PDGF ligand–receptor binding specificity:

| Ligand | Receptor Dimers Activated | Primary Cell Targets | Key Biological Functions |
|---|---|---|---|
| PDGF-AA | **PDGFRαα only**; high-affinity activation of PDGFRα; does **not** appreciably activate PDGFRββ (solinc2022theplateletderivedgrowth pages 3-4, kadrmas2020geneticanalysesin pages 1-2, kadrmas2020geneticanalysesin pages 4-5, jung2025rolesofpdgfpdgfr pages 1-2) | PDGFRα-expressing mesenchymal cells, including fibroblast-lineage/interstitial stromal cells and other non-vascular mesenchyme (kalra2021roleofpdgfab pages 3-5, guerit2021pdgfreceptormutations pages 1-2) | Mesenchymal proliferation, migration, developmental patterning, stromal expansion, wound-healing responses (rogers2020theemergingcomplexity pages 3-4, zhao2026pdgfsignalingin pages 3-5, kalra2021roleofpdgfab pages 3-5, guerit2021pdgfreceptormutations pages 1-2) |
| PDGF-AB | **PDGFRαα, PDGFRαβ**; primarily activates α-containing dimers; weak/inefficient for PDGFRββ compared with PDGF-BB (solinc2022theplateletderivedgrowth pages 3-4, kadrmas2020geneticanalysesin pages 1-2, kadrmas2020geneticanalysesin pages 4-5) | Mixed α/β-expressing mesenchymal cells, including stromal progenitors and activated fibroblast-like cells (kalra2021roleofpdgfab pages 3-5, jung2025rolesofpdgfpdgfr pages 1-2) | Growth and migration outputs similar to PDGF-AA but with broader receptor usage; supports mesenchymal motility and proliferative signaling (kadrmas2020geneticanalysesin pages 1-2, zhao2026pdgfsignalingin pages 3-5, solinc2022theplateletderivedgrowth pages 3-4) |
| PDGF-BB | **PDGFRαα, PDGFRαβ, PDGFRββ**; universal/high-affinity ligand for both receptors (solinc2022theplateletderivedgrowth pages 3-4, rogers2020theemergingcomplexity pages 3-4, kadrmas2020geneticanalysesin pages 1-2, solinc2022theplateletderivedgrowth pages 7-8) | Pericytes, vascular smooth muscle cells, mesangial cells, fibroblasts, hepatic stellate cells, pulmonary arterial smooth muscle cells (jung2025rolesofpdgfpdgfr pages 1-2, jung2025rolesofpdgfpdgfr pages 3-4, solinc2022theplateletderivedgrowth pages 7-8, solinc2022theplateletderivedgrowth pages 4-7, kalra2021roleofpdgfab pages 3-5) | Canonical pericyte recruitment and vessel stabilization; mesenchymal proliferation, survival, migration; vascular remodeling; fibrosis; smooth-muscle expansion in PAH and injury responses (jung2025rolesofpdgfpdgfr pages 1-2, solinc2022theplateletderivedgrowth pages 7-8, solinc2022theplateletderivedgrowth pages 4-7, ma2024targetingpdgfpdgfrsignaling pages 4-6, kalra2021roleofpdgfab pages 3-5) |
| PDGF-CC | **PDGFRαα, PDGFRαβ** after **proteolytic activation** from a latent dimeric form (solinc2022theplateletderivedgrowth pages 3-4, jung2025rolesofpdgfpdgfr pages 1-2) | PDGFRα-expressing stromal cells, fibroblast/myofibroblast precursors, CNS-associated mesenchymal cells (jung2025rolesofpdgfpdgfr pages 1-2, kalra2021roleofpdgfab pages 3-5) | Tissue repair and remodeling; profibrotic signaling in some contexts; implicated in neurovascular injury/stroke responses through PDGFRα pathways (jung2025rolesofpdgfpdgfr pages 1-2, solinc2022theplateletderivedgrowth pages 7-8) |
| PDGF-DD | **PDGFRββ** and, in many reviews, **PDGFRαβ** after **proteolytic activation** from a latent dimeric form; high affinity for PDGFRβ chains (solinc2022theplateletderivedgrowth pages 3-4, jung2025rolesofpdgfpdgfr pages 1-2) | Pericytes, vascular smooth muscle cells, other PDGFRβ+ mural/mesenchymal cells (jung2025rolesofpdgfpdgfr pages 1-2, solinc2022theplateletderivedgrowth pages 7-8, solinc2022theplateletderivedgrowth pages 4-7) | Pericyte support, angiogenesis, vascular stability, neurovascular integrity, mural-cell survival/migration, remodeling in vascular disease (jung2025rolesofpdgfpdgfr pages 1-2, solinc2022theplateletderivedgrowth pages 7-8, solinc2022theplateletderivedgrowth pages 4-7) |


*Table: This table summarizes the main PDGF dimer ligands, the PDGFR dimers they activate, and the principal mesenchymal cell targets and biological outputs associated with each ligand. It is useful for distinguishing the broader receptor usage of PDGF-BB from the more restricted or latent activation properties of PDGF-AA, PDGF-CC, and PDGF-DD.*

Structurally, each PDGF molecule within a dimer contacts one PDGFR molecule, primarily through immunoglobulin-like domains D2 and D3 of the extracellular region (rogers2020theemergingcomplexity pages 3-4, rogers2020theemergingcomplexity pages 1-3). Receptor dimerization is further stabilized by direct D4–D5 contacts between receptor protomers (rogers2020theemergingcomplexity pages 3-4). Computer modeling predicts two transmembrane domain states: an inactive near-parallel conformation without ligand, and an active right-handed conformation induced by ligand binding that transmits the signal to intracellular kinase domains (rogers2020theemergingcomplexity pages 3-4). Additionally, autoinhibitory sequences in the juxtamembrane domain and C-terminal tail maintain the receptor in an inactive state in the absence of ligand (rogers2020theemergingcomplexity pages 12-14).

### 3.2 Step 2: Receptor autophosphorylation and phosphotyrosine adaptor assembly

Upon dimerization, trans-autophosphorylation occurs on multiple tyrosine residues within the intracellular domain—eleven sites on PDGFRα and thirteen on PDGFRβ have been identified (rogers2020theemergingcomplexity pages 3-4). These phosphotyrosines create docking sites for SH2 domain-containing adaptor and effector proteins that initiate downstream signaling cascades (zhao2026pdgfsignalingin pages 3-5).

Key phosphotyrosine–adaptor relationships on PDGFRβ include: SHP2 (PTPN11) binds Y763 and Y1009 via its tandem SH2 domains, serving both catalytic and scaffolding functions to promote RAS/MAPK signaling (pierotti2026regulationandactivity pages 4-4, pierotti2026regulationandactivity pages 2-3). GRB2 binds directly to Y716 on PDGFRβ and is also recruited indirectly through SHP2-mediated phosphorylation of Y580 (pierotti2026regulationandactivity pages 4-4, wang2024theconfigurationof pages 9-11). PI3K p85 regulatory subunit binds Y740 and Y751, activating the PI3K/AKT survival and motility axis (zhao2026pdgfsignalingin pages 3-5, perezbaena2023theroleof pages 2-4). PLCγ binds Y1009 and Y1021, triggering calcium mobilization and PKC activation (zhao2026pdgfsignalingin pages 3-5, rogers2020theemergingcomplexity pages 6-8). Src family kinases bind Y579 and Y581, driving cytoskeletal remodeling (zhao2026pdgfsignalingin pages 3-5). Abl2 binds Y771, contributing to actin dynamics and cell edge regulation (wu2021plateletderivedgrowthfactor pages 1-5).

The following table summarizes the major SH2-domain effectors recruited to PDGFRβ:

| Effector Protein | PDGFRβ Binding Site(s) | Domain Used | Downstream Pathway | Cellular Output |
|---|---|---|---|---|
| SHP2 (PTPN11) | Y763, Y1009 | Tandem SH2 domains, especially N-SH2 for receptor docking | Promotes RAS/MAPK signaling; phosphorylated SHP2 recruits GRB2/SOS to sustain ERK activation | Mitogenic signaling, signal propagation, proliferation/migration support (pierotti2026regulationandactivity pages 4-4, pierotti2026regulationandactivity pages 2-3) |
| GRB2 | Y716 directly on PDGFRβ; also indirect recruitment via SHP2 pY580 | SH2 domain binds phosphotyrosine; SH3 domains recruit SOS | RAS/RAF/MEK/ERK (MAPK) via SOS-mediated Ras activation | Proliferation, survival, migration, transcriptional responses (wang2024theconfigurationof pages 2-4, wang2024theconfigurationof pages 1-2, wang2024theconfigurationof pages 9-11, wang2024theconfigurationof pages 18-19, pierotti2026regulationandactivity pages 4-4) |
| PI3K p85 | Y740, Y751 | SH2 domains of p85 regulatory subunit | PI3K/AKT signaling | Survival, growth, chemotaxis, polarity, motility, focal adhesion remodeling (zhao2026pdgfsignalingin pages 3-5, perezbaena2023theroleof pages 2-4) |
| PLCγ | Y1009, Y1021 | SH2 domains | PLCγ/PKC/Ca2+ signaling | Calcium flux, PKC activation, motility and cytoskeletal regulation; contributes to migration outputs (zhao2026pdgfsignalingin pages 3-5, rogers2020theemergingcomplexity pages 6-8) |
| Src family kinases | Y579, Y581 | SH2 domain-mediated phosphotyrosine recognition | Src-centered signaling integrated with Akt and cytoskeletal pathways | Cytoskeletal remodeling, chemotaxis, migration, membrane ruffling/motility (zhao2026pdgfsignalingin pages 3-5) |
| Abl2 | Y771 | SH2 domain | Abl-family cytoskeletal signaling downstream of PDGFRβ | Actin remodeling, cell edge dynamics, motility regulation (wu2021plateletderivedgrowthfactor pages 1-5) |
| RasGAP | Not specified in the retrieved evidence; classically binds phosphotyrosine docking sites on activated PDGFRβ | SH2 domains | Negative regulation of Ras signaling | Signal attenuation/tuning of proliferation and migration outputs; site assignment unresolved here (zhao2026pdgfsignalingin pages 3-5) |


*Table: This table summarizes major SH2-domain effectors recruited to phosphorylated PDGFRβ, their reported docking sites, and the main downstream pathways they control. It is useful for connecting receptor phosphotyrosines to specific growth, survival, and motility outputs in the PDGFR signaling module.*

### 3.3 Step 3: Growth and migration output via PI3K/MAPK branches

The GRB2 adaptor is a critical node in PDGFR-driven proliferative signaling. GRB2 has a central SH2 domain flanked by two SH3 domains (wang2024theconfigurationof pages 1-2). The SH2 domain recognizes the pYxNx consensus motif on activated RTKs, while the N-terminal SH3 domain constitutively binds the RAS guanine nucleotide exchange factor SOS, recruiting it to the plasma membrane (wang2024theconfigurationof pages 2-4, wang2024theconfigurationof pages 1-2). SOS catalyzes GDP-to-GTP exchange on RAS, initiating the RAF→MEK→ERK cascade that drives transcriptional programs for cell proliferation, differentiation, and survival (wang2024theconfigurationof pages 2-4). The C-terminal SH3 domain of GRB2 binds GAB1, which recruits PI3K for PI3K/AKT-dependent survival signaling, creating a secondary amplification loop (wang2024theconfigurationof pages 2-4, perezbaena2023theroleof pages 2-4).

The PI3K/AKT and Src-AKT signaling cascades are critical for chemotaxis and mesenchymal stem cell migration, with inhibition of either Src or AKT significantly reducing homing efficiency (zhao2026pdgfsignalingin pages 3-5). PI3K/AKT and PLCγ pathways coordinate to regulate small GTPases and focal adhesion dynamics, promoting pseudopodia formation and cell polarity essential for directional migration (zhao2026pdgfsignalingin pages 3-5). PDGFRβ signaling additionally activates JAK/STAT pathways, calcium entry mechanisms via STIM1/Orai1 and TRPC channels, and Cyclin D1 expression promoting cell cycle progression (solinc2022theplateletderivedgrowth pages 4-7).

### 3.4 Obligatory versus conditional steps

Ligand binding, receptor dimerization, and trans-autophosphorylation represent obligatory sequential steps (rogers2020theemergingcomplexity pages 3-4, rogers2020theemergingcomplexity pages 1-3). The subsequent adaptor assembly is conditional on the specific phosphotyrosine sites occupied and the repertoire of SH2-domain proteins expressed in a given cell type. The PI3K and RAS/MAPK branches are the most consistently engaged across cell types, while PLCγ and Src recruitment provide context-dependent amplification of motility and cytoskeletal outputs (zhao2026pdgfsignalingin pages 3-5).

## 4. Major Molecular Players and Active Assemblies

### 4.1 PDGF ligands

PDGF-A and PDGF-B are the most widely expressed ligands and have been studied most extensively (kadrmas2020geneticanalysesin pages 1-2). PDGF-B, produced by endothelial cells, is the canonical signal for pericyte recruitment during angiogenesis (jung2025rolesofpdgfpdgfr pages 1-2, solinc2022theplateletderivedgrowth pages 7-8). PDGF-CC and PDGF-DD are later-discovered members that are secreted as latent dimers requiring proteolytic activation, adding a layer of spatial and temporal regulation (solinc2022theplateletderivedgrowth pages 3-4, jung2025rolesofpdgfpdgfr pages 1-2).

### 4.2 PDGF receptors

PDGFRα (encoded by PDGFRA) and PDGFRβ (encoded by PDGFRB) are class III RTKs characterized by five extracellular immunoglobulin-like domains, a single transmembrane helix, and an intracellular split kinase domain (kalra2021roleofpdgfab pages 3-5, solinc2022theplateletderivedgrowth pages 3-4). PDGFRα is predominantly expressed on interstitial fibroblasts, oligodendrocyte precursor cells, and various mesenchymal progenitors, while PDGFRβ marks pericytes, vascular smooth muscle cells, mesangial cells, and hepatic stellate cells (kalra2021roleofpdgfab pages 3-5, jung2025rolesofpdgfpdgfr pages 2-3, guerit2021pdgfreceptormutations pages 1-2).

### 4.3 Key adaptors

**GRB2** (Growth factor receptor-bound protein 2): A 25-kDa non-enzymatic adaptor with the SH3-SH2-SH3 "sandwich" architecture (wang2024theconfigurationof pages 1-2). GRB2 is the principal link between PDGFRβ and RAS activation. Its monomer-dimer equilibrium determines normal versus oncogenic function (wang2024theconfigurationof pages 19-21). Post-translational modifications, including SUMOylation at Lys56, modulate its ability to recruit SOS and enhance ERK activation (wang2024theconfigurationof pages 18-19).

**PI3K p85 regulatory subunit:** Contains two SH2 domains that bind phosphotyrosines Y740 and Y751 on PDGFRβ, relieving autoinhibition of the catalytic p110 subunit and enabling phosphoinositide 3,4,5-trisphosphate (PIP3) production at the membrane (zhao2026pdgfsignalingin pages 3-5, perezbaena2023theroleof pages 2-4). GAB1, recruited via GRB2, provides an additional docking platform for PI3K, amplifying PI3K signaling downstream of multiple RTKs including PDGFR (perezbaena2023theroleof pages 12-13, perezbaena2023theroleof pages 2-4).

**SHP2 (PTPN11):** A protein tyrosine phosphatase that paradoxically functions as a positive mediator of RAS/MAPK signaling downstream of PDGFR. SHP2 binds PDGFRβ at Y763 and Y1009 through its N-SH2 domain, becomes phosphorylated at Y542 and Y580, and then recruits GRB2/SOS to sustain ERK activation (pierotti2026regulationandactivity pages 4-4, pierotti2026regulationandactivity pages 2-3). SHP2 thus functions simultaneously as an enzyme and as a scaffold/adaptor in PDGFR signaling.

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Evolutionary origins

The PDGF/VEGF growth factor superfamily traces to an ancestral cystine-knot growth factor gene present in the common ancestor of Vertebrata and Cnidaria (rauniyar2023expansionandcollapse pages 1-3). The proto-PDGF/VEGF gene duplication that separated PDGF and VEGF lineages occurred prior to the first vertebrate genome duplication (VGD1), while further diversification of PDGF-A, PDGF-B, PDGF-C, and PDGF-D was facilitated by the second vertebrate genome duplication (VGD2) (rauniyar2023expansionandcollapse pages 14-15). PDGFs as distinct from VEGFs appear to have first emerged in the chordate lineage after divergence from echinoderms (rauniyar2023expansionandcollapse pages 3-6). Invertebrate PDGF/VEGF-like factors (PVFs), such as those in *Drosophila melanogaster* (PVF-1, PVF-2, PVF-3), signal through a single receptor, PVR (PDGF/VEGF receptor), which combines functions split between PDGFRs and VEGFRs in vertebrates (rauniyar2023expansionandcollapse pages 3-6, rauniyar2023expansionandcollapse pages 1-3). PDGFs are present in cephalochordates (lancelets), among the simplest organisms with a pressurized vascular system (rauniyar2023expansionandcollapse pages 14-15).

The receptor tyrosine kinases of the PDGFR/VEGFR family split into class III (PDGFRα, PDGFRβ, c-KIT, FLT3, CSF1R) and class V (VEGFR1-3) RTKs before the chordate–tunicate divergence (rauniyar2023expansionandcollapse pages 3-6). This deep evolutionary split means that PDGFRα and PDGFRβ, as they exist in vertebrates, are products of vertebrate-specific genome duplications layered onto an ancient single-receptor ancestor.

### 5.2 Cell-type and tissue variation

The two PDGF receptor paralogs show striking differences in tissue distribution and developmental function:

- **PDGFRα** controls development of lungs, intestine, skin, testis, kidneys, bones, and neuroprotective tissues; its deletion in mice causes defects in the gastrointestinal tract, CNS, skeleton, and multiple other organs (solinc2022theplateletderivedgrowth pages 3-4, guerit2021pdgfreceptormutations pages 1-2). In the CNS, PDGFRα is the canonical marker of oligodendrocyte precursor cells and is critical for myelination (jung2025rolesofpdgfpdgfr pages 2-3).
- **PDGFRβ** is essential for early hematopoiesis and blood vessel formation; its deletion causes embryonic lethality due to vascular hemorrhage from loss of pericytes and vascular smooth muscle cells (kalra2021roleofpdgfab pages 3-5, solinc2022theplateletderivedgrowth pages 3-4, guerit2021pdgfreceptormutations pages 1-2). PDGFRβ is the primary receptor mediating PDGF-BB-driven pericyte recruitment to stabilize newly formed capillaries (solinc2022theplateletderivedgrowth pages 7-8, jung2025rolesofpdgfpdgfr pages 1-2).

In adult pathophysiology, PDGFR signaling varies markedly by tissue context. In the liver, PDGF-BB drives hepatic stellate cell activation and liver fibrosis (jung2025rolesofpdgfpdgfr pages 3-4). In the lungs, PDGF signaling promotes pulmonary arterial smooth muscle cell proliferation in pulmonary arterial hypertension (PAH) and fibroblast-to-myofibroblast transition in idiopathic pulmonary fibrosis (jung2025rolesofpdgfpdgfr pages 3-4, solinc2022theplateletderivedgrowth pages 7-8). In the heart, PDGFRα+ cells differentiate into myofibroblasts during cardiac injury, while PDGFRβ signaling is critical for coronary pericyte homeostasis (kalra2021roleofpdgfab pages 3-5). In the vasculature, PDGF-BB stimulates vascular smooth muscle cell phenotype switching from contractile to synthetic states, contributing to atherosclerosis and restenosis (ma2024targetingpdgfpdgfrsignaling pages 4-6).

An important cell-type distinction is that PDGFR signaling in chondrocytes regulates proliferation and anti-apoptosis but does not promote terminal differentiation, playing a supportive rather than instructive role in cartilage repair (zhao2026pdgfsignalingin pages 2-3). In synovial fibroblasts, PDGFRβ has "double-edged sword" properties—promoting both beneficial matrix synthesis and pathological synovial activation (zhao2026pdgfsignalingin pages 2-3).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordered events

The pathway enforces a strict sequence: ligand binding → receptor dimerization → D4-D5 extracellular contact → transmembrane conformational change → juxtamembrane release of autoinhibition → trans-autophosphorylation → SH2-domain adaptor recruitment → downstream kinase activation (rogers2020theemergingcomplexity pages 3-4, rogers2020theemergingcomplexity pages 12-14). Disruption at any step blocks downstream signaling. PI3K-mediated phosphorylation is itself required for efficient PDGFRβ internalization, creating a feed-forward dependency between signaling and trafficking (rogers2020theemergingcomplexity pages 4-6).

### 6.2 Signal attenuation and termination

PDGFR signaling is tightly regulated by multiple negative-feedback mechanisms:

- **Cbl E3 ubiquitin ligases:** c-Cbl and Cbl-b cooperatively bind activated PDGFRs and catalyze polyubiquitination, targeting receptors for endocytic internalization and degradation. For PDGFRβ specifically, Cbl-b is essential for c-Cbl binding, as c-Cbl cannot bind PDGFRβ directly (tang2022negativeregulationof pages 2-3, rogers2020theemergingcomplexity pages 11-12, rogers2020theemergingcomplexity pages 10-11).
- **Receptor internalization:** PDGFRs internalize primarily via clathrin-mediated endocytosis, driven by a 14-amino-acid internalization motif with di-leucine sequences. PDGFRβ half-life after activation is approximately 90 minutes (rogers2020theemergingcomplexity pages 6-8, rogers2020theemergingcomplexity pages 12-14, rogers2020theemergingcomplexity pages 4-6).
- **Endosomal signaling and sorting:** PDGFRβ continues to signal from endosomes by recruiting Shc, GRB2, PI3K, and PLCγ, with the balance between degradation and recycling determining signal duration. TC-PTP (T-cell protein tyrosine phosphatase) loss hyperphosphorylates Y1021, activating PKCα-dependent receptor recycling rather than degradation (rogers2020theemergingcomplexity pages 6-8).
- **Protein tyrosine phosphatases:** PTP1B dephosphorylates PDGFR at the endoplasmic reticulum, inactivating the receptor. Src-like adaptor protein (Slap) blocks Src-mediated signaling from PDGFR (margiotta2021allgoodthings pages 6-7).
- **SOCS proteins** add polyubiquitin chains to target receptors for proteasomal degradation (margiotta2021allgoodthings pages 6-7).

### 6.3 Mutually exclusive events and constraints

The choice between receptor degradation and recycling represents a critical branch point regulated by phosphatase activity. When TC-PTP is present, it dephosphorylates specific sites favoring degradation; when absent, PKCα signaling routes receptors to recycling pathways (rogers2020theemergingcomplexity pages 6-8). This demonstrates that signal termination is not a single mechanism but a regulated decision.

### 6.4 Failure modes and disease

Dysregulation of PDGFR signaling causes a defined spectrum of human diseases. The following table summarizes major disease associations:

| Disease | Gene Affected | Mutation Type | Key Mutations | Therapeutic Response |
|---|---|---|---|---|
| Gastrointestinal stromal tumors (GIST) | **PDGFRA** | Gain-of-function | **D842V**; additional activating mutations in **exons 12, 14, and 18** | **Imatinib** active in some PDGFRA-mutant GISTs, but **D842V is typically imatinib-resistant**; **avapritinib** is active against PDGFRA activation-loop mutants including D842V (guerit2021pdgfreceptormutations pages 8-9, guerit2021pdgfreceptormutations pages 11-12, guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 2-5) |
| Infantile myofibromatosis | **PDGFRB** | Gain-of-function | **R561C** (most common familial germline variant); **P584R**; **W566R**; also **S493C** reported | Frequently **imatinib-responsive**; literature supports imatinib-sensitive activating PDGFRB variants and clinical benefit in some patients (guerit2021pdgfreceptormutations pages 8-9, guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 2-5, guerit2021pdgfreceptormutations pages 5-6, guerit2021pdgfreceptormutations pages 12-13) |
| Primary familial brain calcification (IBGC/Fahr disease) | **PDGFRB**, **PDGFB** | Loss-of-function | **PDGFRB L658P, R987W, R695C**; pathogenic **PDGFB** variants also implicated | **No established targeted PDGFR therapy**; disease is associated with reduced PDGF-B/PDGFRβ signaling rather than kinase activation (guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 6-8, guerit2021pdgfreceptormutations pages 12-13, OpenTargets Search: -PDGFRB,PDGFRA,PDGFB) |
| Kosaki overgrowth syndrome | **PDGFRB** | Gain-of-function | Overlaps with infantile myofibromatosis-associated activating variants; exact variants vary by case | **Imatinib** has mechanistic and case-based rationale for some activating variants; syndrome may include vascular complications (guerit2021pdgfreceptormutations pages 11-12, guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 5-6, guerit2021pdgfreceptormutations pages 12-13, OpenTargets Search: -PDGFRB,PDGFRA,PDGFB) |
| Penttinen syndrome | **PDGFRB** | Gain-of-function | **N666S**, **V665A** | Activating variants are considered potentially **imatinib-sensitive**, although phenotype severity and treatment experience vary (guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 6-8, guerit2021pdgfreceptormutations pages 12-13) |
| Myeloid neoplasms with eosinophilia | **PDGFRA**, **PDGFRB** | Chromosomal rearrangements / fusion-driven activation | Various **gene fusions/rearrangements** | Classically **imatinib-sensitive**, especially for fusion-driven PDGF receptor activation (guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 10-11) |
| Myxoid glioneuronal tumors | **PDGFRA** | Gain-of-function | **K385I**, **K385L** | Preclinical evidence supports suppression by **imatinib, dasatinib, and avapritinib** (guerit2021pdgfreceptormutations pages 11-12, guerit2021pdgfreceptormutations pages 10-11) |


*Table: This table summarizes major diseases linked to PDGFRA, PDGFRB, and PDGFB pathway mutations, highlighting whether variants are activating or loss-of-function and noting current therapeutic implications. It is useful for connecting pathway biology to clinically important human disorders.*

Gain-of-function PDGFRA mutations in the activation loop (D842V), juxtamembrane domain, and extracellular domain drive gastrointestinal stromal tumors (5–10% of GISTs), inflammatory fibroid polyps, and myxoid glioneuronal tumors (guerit2021pdgfreceptormutations pages 8-9, guerit2021pdgfreceptormutations pages 11-12, guerit2021pdgfreceptormutations pages 2-5). Gain-of-function PDGFRB mutations, particularly the recurrent R561C variant in the juxtamembrane domain, cause autosomal-dominant infantile myofibromatosis through constitutive receptor activation; a "two-hit model" has been proposed wherein weak germline gain-of-function mutations require somatic second hits for disease development (guerit2021pdgfreceptormutations pages 2-5, guerit2021pdgfreceptormutations pages 5-6). More potent activating PDGFRB variants (N666S, V665A) cause severe Penttinen premature aging syndrome and overlap with Kosaki overgrowth syndrome (guerit2021pdgfreceptormutations pages 6-8). Conversely, loss-of-function PDGFRB mutations (L658P, R987W, R695C) impair PDGF-B/PDGFRβ signaling and cause primary familial brain calcification (Fahr disease), with mutations in PDGFB itself also causing this condition through deficient pericyte support of brain vasculature (guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 6-8, OpenTargets Search: -PDGFRB,PDGFRA,PDGFB). Chromosomal rearrangements creating PDGFRA or PDGFRB fusion genes drive myeloid neoplasms with eosinophilia, which are characteristically imatinib-sensitive (guerit2021pdgfreceptormutations pages 1-2).

In non-neoplastic disease, excessive PDGF signaling drives fibrosis across multiple organs through transformation of quiescent fibroblasts and pericytes into collagen-producing myofibroblasts (jung2025rolesofpdgfpdgfr pages 1-2, jung2025rolesofpdgfpdgfr pages 3-4, solinc2022theplateletderivedgrowth pages 7-8). PDGF-BB is a potent mitogen for hepatic stellate cells, pulmonary arterial smooth muscle cells, and cardiac fibroblasts (jung2025rolesofpdgfpdgfr pages 3-4, solinc2022theplateletderivedgrowth pages 4-7). In pulmonary arterial hypertension, PDGF-BB stimulates proliferation and migration of pulmonary arterial SMCs through MAPK and AKT pathways (solinc2022theplateletderivedgrowth pages 4-7). In Alzheimer's disease, PDGFRβ signaling deficiency causes pericyte loss, blood-brain barrier disruption, and neurovascular degeneration (jung2025rolesofpdgfpdgfr pages 2-3).

## 7. Controversies and Open Questions

### 7.1 Receptor activation mechanism

Despite decades of study, the precise mechanism by which ligand binding propagates through the transmembrane domain to activate the kinase remains incompletely understood. The two-state model of transmembrane helix conformation (inactive parallel versus active right-handed) is based primarily on computational modeling, and direct structural evidence for full-length activated PDGFR dimers is still lacking (rogers2020theemergingcomplexity pages 3-4, rogers2020theemergingcomplexity pages 1-3). The roles of D4-D5 extracellular contacts versus transmembrane helix interactions in stabilizing active dimers remain debated.

### 7.2 Endosomal versus surface signaling

Whether PDGFR signals predominantly from the plasma membrane or from endosomes remains an area of active investigation. Evidence shows PDGFRβ recruits adaptors at endosomes and that dynamin-dependent internalization is required for STAT3 activation, but the quantitative contribution of endosomal signaling to overall output is uncertain (rogers2020theemergingcomplexity pages 6-8, rogers2020theemergingcomplexity pages 4-6). The distinction between lysosomal and proteasomal degradation pathways for activated PDGFRs also remains debated (rogers2020theemergingcomplexity pages 6-8).

### 7.3 PDGFRα versus PDGFRβ signaling specificity

While PDGFRα and PDGFRβ share similar intracellular domain architecture and recruit overlapping sets of SH2-domain effectors, they produce different biological outcomes. Whether this reflects intrinsic differences in kinase activity, phosphosite usage, or simply differences in cellular context remains an important open question (kalra2021roleofpdgfab pages 3-5, jung2025rolesofpdgfpdgfr pages 2-3, solinc2022theplateletderivedgrowth pages 3-4). Rogers and Fantauzzo (2020) specifically highlighted critical gaps in knowledge regarding the commonalities and differences between PDGFRα and PDGFRβ signaling (rogers2020theemergingcomplexity pages 3-4).

### 7.4 Heterodimer biology

The PDGFRαβ heterodimer is the least characterized receptor species. Its formation is driven by PDGF-BB and PDGF-AB, but its signaling properties and biological functions remain poorly understood compared to the homodimers (solinc2022theplateletderivedgrowth pages 3-4, kadrmas2020geneticanalysesin pages 1-2).

### 7.5 Ligand–receptor cross-reactivity

Recent work has challenged the canonical model of PDGF ligand specificity, demonstrating that PDGF-AB can robustly activate PDGFRβ homodimers and that PDGFRα is capable of eliciting biological responses previously attributed exclusively to PDGFRβ, such as circular dorsal ruffle formation (kadrmas2020geneticanalysesin pages 1-2, kadrmas2020geneticanalysesin pages 7-9). These findings suggest the ligand–receptor interaction rules may be more promiscuous than textbook models indicate.

### 7.6 Therapeutic challenges

While tyrosine kinase inhibitors (imatinib, dasatinib, avapritinib) have demonstrated efficacy against specific PDGFR-driven conditions, the broad expression of PDGFRs in normal mesenchymal tissues creates challenges for therapeutic specificity. The PDGFRA D842V mutation in GIST is resistant to imatinib but sensitive to avapritinib (guerit2021pdgfreceptormutations pages 8-9). In pulmonary arterial hypertension, clinical trials with imatinib showed beneficial effects but were discontinued due to adverse events including subdural hematomas, highlighting the tension between efficacy and safety (solinc2022theplateletderivedgrowth pages 7-8). Novel delivery strategies including intratracheal administration, nanoparticle formulations, and aptamer-based targeting are under experimental evaluation (solinc2022theplateletderivedgrowth pages 7-8).

### 7.7 Pericyte plasticity

Whether pericytes genuinely transdifferentiate into myofibroblasts during fibrosis or whether apparent pericyte-to-myofibroblast transition reflects selection of pre-existing subpopulations remains contested. Organ-specific differences in pericyte populations and variability in fate-mapping strategies may account for conflicting observations across different tissue contexts (solinc2022theplateletderivedgrowth pages 7-8).

## 8. Key References

The following references are among the most directly relevant primary and review sources informing this synthesis:

1. Rogers MA, Fantauzzo KA. "The emerging complexity of PDGFRs: activation, internalization and signal attenuation." *Biochem Soc Trans.* 2020;48:1167–1176. doi:10.1042/BST20200004 (rogers2020theemergingcomplexity pages 3-4, rogers2020theemergingcomplexity pages 1-3, rogers2020theemergingcomplexity pages 11-12, rogers2020theemergingcomplexity pages 6-8, rogers2020theemergingcomplexity pages 12-14, rogers2020theemergingcomplexity pages 4-6, rogers2020theemergingcomplexity pages 10-11)

2. Jung SC, Kang D, Ko EA. "Roles of PDGF/PDGFR signaling in various organs." *Korean J Physiol Pharmacol.* 2025;29:139–155. doi:10.4196/kjpp.24.309 (jung2025rolesofpdgfpdgfr pages 1-2, jung2025rolesofpdgfpdgfr pages 2-3, jung2025rolesofpdgfpdgfr pages 3-4)

3. Guérit E, Arts F, Dachy G, et al. "PDGF receptor mutations in human diseases." *Cell Mol Life Sci.* 2021;78:3867–3881. doi:10.1007/s00018-020-03753-y (guerit2021pdgfreceptormutations pages 1-2, guerit2021pdgfreceptormutations pages 8-9, guerit2021pdgfreceptormutations pages 11-12, guerit2021pdgfreceptormutations pages 6-8, guerit2021pdgfreceptormutations pages 2-5, guerit2021pdgfreceptormutations pages 5-6, guerit2021pdgfreceptormutations pages 12-13, guerit2021pdgfreceptormutations pages 10-11)

4. Solinc J, Ribot J, Soubrier F, et al. "The platelet-derived growth factor pathway in pulmonary arterial hypertension." *Life.* 2022;12:658. doi:10.3390/life12050658 (solinc2022theplateletderivedgrowth pages 3-4, solinc2022theplateletderivedgrowth pages 7-8, solinc2022theplateletderivedgrowth pages 4-7)

5. Wang D, Liu G, Meng Y, et al. "The configuration of GRB2 in protein interaction and signal transduction." *Biomolecules.* 2024;14:259. doi:10.3390/biom14030259 (wang2024theconfigurationof pages 2-4, wang2024theconfigurationof pages 1-2, wang2024theconfigurationof pages 19-21, wang2024theconfigurationof pages 9-11, wang2024theconfigurationof pages 18-19, wang2024theconfigurationof pages 12-14, wang2024theconfigurationof pages 4-5, wang2024theconfigurationof pages 11-12)

6. Kadrmas JL, Beckerle MC, Yoshigi M. "Genetic analyses in mouse fibroblast and melanoma cells demonstrate novel roles for PDGF-AB ligand and PDGF receptor alpha." *Sci Rep.* 2020;10. doi:10.1038/s41598-020-75774-3 (kadrmas2020geneticanalysesin pages 2-4, kadrmas2020geneticanalysesin pages 1-2, kadrmas2020geneticanalysesin pages 4-5, kadrmas2020geneticanalysesin pages 7-9)

7. Pierotti CL, Köhn M. "Regulation and activity of the phosphatase SHP2." *Biochem J.* 2026;54:15–24. doi:10.1042/BST20253102 (pierotti2026regulationandactivity pages 4-4, pierotti2026regulationandactivity pages 2-3)

8. Tang R, Langdon WY, Zhang J. "Negative regulation of receptor tyrosine kinases by ubiquitination: key roles of the Cbl family." *Front Endocrinol.* 2022;13. doi:10.3389/fendo.2022.971162 (tang2022negativeregulationof pages 2-3)

9. Rauniyar K, Bokharaie H, Jeltsch M. "Expansion and collapse of VEGF diversity in major clades of the animal kingdom." *Angiogenesis.* 2023;26:437–461. doi:10.1007/s10456-023-09874-9 (rauniyar2023expansionandcollapse pages 3-6, rauniyar2023expansionandcollapse pages 14-15, rauniyar2023expansionandcollapse pages 1-3)

10. Wu K, Wu H, Lyu W, et al. "Platelet-derived growth factor receptor beta activates Abl2 via direct binding and phosphorylation." *J Biol Chem.* 2021;297:100883. doi:10.1016/j.jbc.2021.100883 (wu2021plateletderivedgrowthfactor pages 1-5)

11. Kalra K, Eberhard J, Farbehi N, et al. "Role of PDGF-A/B ligands in cardiac repair after myocardial infarction." *Front Cell Dev Biol.* 2021;9. doi:10.3389/fcell.2021.669188 (kalra2021roleofpdgfab pages 3-5)

12. Zhao QQ, Che F, Liu W, et al. "PDGF signaling in cartilage regeneration: molecular mechanisms and cellular effects." *Front Cell Dev Biol.* 2026;14. doi:10.3389/fcell.2026.1778703 (zhao2026pdgfsignalingin pages 3-5, zhao2026pdgfsignalingin pages 2-3)

13. Pérez-Baena MJ, Cordero-Pérez FJ, Pérez-Losada J, Holgado-Madruga M. "The role of GAB1 in cancer." *Cancers.* 2023;15:4179. doi:10.3390/cancers15164179 (perezbaena2023theroleof pages 12-13, perezbaena2023theroleof pages 2-4)

14. Margiotta A. "All good things must end: termination of receptor tyrosine kinase signal." *Int J Mol Sci.* 2021;22:6342. doi:10.3390/ijms22126342 (margiotta2021allgoodthings pages 6-7)

15. Ma CN, Shi SR, Zhang XY, et al. "Targeting PDGF/PDGFR signaling pathway by microRNA, lncRNA, and circRNA for therapy of vascular diseases." *Biomolecules.* 2024;14:1446. doi:10.3390/biom14111446 (ma2024targetingpdgfpdgfrsignaling pages 4-6, ma2024targetingpdgfpdgfrsignaling pages 18-19)

16. de Villenfagne L, Sablon A, Demoulin JB. "PDGFRA K385 mutants in myxoid glioneuronal tumors promote receptor dimerization and oncogenic signaling." *Sci Rep.* 2024;14. doi:10.1038/s41598-024-57859-5

References

1. (solinc2022theplateletderivedgrowth pages 3-4): Julien Solinc, Jonathan Ribot, Florent Soubrier, Catherine Pavoine, France Dierick, and Sophie Nadaud. The platelet-derived growth factor pathway in pulmonary arterial hypertension: still an interesting target? Life, 12:658, Apr 2022. URL: https://doi.org/10.3390/life12050658, doi:10.3390/life12050658. This article has 38 citations.

2. (kadrmas2020geneticanalysesin pages 1-2): Julie L. Kadrmas, Mary C. Beckerle, and Masaaki Yoshigi. Genetic analyses in mouse fibroblast and melanoma cells demonstrate novel roles for pdgf-ab ligand and pdgf receptor alpha. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-75774-3, doi:10.1038/s41598-020-75774-3. This article has 11 citations and is from a peer-reviewed journal.

3. (zhao2026pdgfsignalingin pages 3-5): Qiang-qiang Zhao, Feihong Che, Weiwen Liu, Chengyu Hou, Lijuan Yu, Yonghui Hou, and Liangliang Xu. Pdgf signaling in cartilage regeneration: molecular mechanisms and cellular effects. Frontiers in Cell and Developmental Biology, Feb 2026. URL: https://doi.org/10.3389/fcell.2026.1778703, doi:10.3389/fcell.2026.1778703. This article has 1 citations.

4. (jung2025rolesofpdgfpdgfr pages 1-2): Sung-Cherl Jung, Dawon Kang, and Eun-A Ko. Roles of pdgf/pdgfr signaling in various organs. The Korean Journal of Physiology & Pharmacology : Official Journal of the Korean Physiological Society and the Korean Society of Pharmacology, 29:139-155, Oct 2025. URL: https://doi.org/10.4196/kjpp.24.309, doi:10.4196/kjpp.24.309. This article has 26 citations.

5. (solinc2022theplateletderivedgrowth pages 7-8): Julien Solinc, Jonathan Ribot, Florent Soubrier, Catherine Pavoine, France Dierick, and Sophie Nadaud. The platelet-derived growth factor pathway in pulmonary arterial hypertension: still an interesting target? Life, 12:658, Apr 2022. URL: https://doi.org/10.3390/life12050658, doi:10.3390/life12050658. This article has 38 citations.

6. (guerit2021pdgfreceptormutations pages 1-2): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

7. (rauniyar2023expansionandcollapse pages 3-6): Khushbu Rauniyar, Honey Bokharaie, and Michael Jeltsch. Expansion and collapse of vegf diversity in major clades of the animal kingdom. Angiogenesis, 26:437-461, Apr 2023. URL: https://doi.org/10.1007/s10456-023-09874-9, doi:10.1007/s10456-023-09874-9. This article has 21 citations and is from a domain leading peer-reviewed journal.

8. (rauniyar2023expansionandcollapse pages 1-3): Khushbu Rauniyar, Honey Bokharaie, and Michael Jeltsch. Expansion and collapse of vegf diversity in major clades of the animal kingdom. Angiogenesis, 26:437-461, Apr 2023. URL: https://doi.org/10.1007/s10456-023-09874-9, doi:10.1007/s10456-023-09874-9. This article has 21 citations and is from a domain leading peer-reviewed journal.

9. (ma2024targetingpdgfpdgfrsignaling pages 4-6): Chao-Nan Ma, Shan-Rui Shi, Xue-Ying Zhang, Guo-Song Xin, Xiang Zou, Wen-Lan Li, and Shou-Dong Guo. Targeting pdgf/pdgfr signaling pathway by microrna, lncrna, and circrna for therapy of vascular diseases: a narrow review. Biomolecules, 14:1446, Nov 2024. URL: https://doi.org/10.3390/biom14111446, doi:10.3390/biom14111446. This article has 17 citations.

10. (ma2024targetingpdgfpdgfrsignaling pages 18-19): Chao-Nan Ma, Shan-Rui Shi, Xue-Ying Zhang, Guo-Song Xin, Xiang Zou, Wen-Lan Li, and Shou-Dong Guo. Targeting pdgf/pdgfr signaling pathway by microrna, lncrna, and circrna for therapy of vascular diseases: a narrow review. Biomolecules, 14:1446, Nov 2024. URL: https://doi.org/10.3390/biom14111446, doi:10.3390/biom14111446. This article has 17 citations.

11. (kalra2021roleofpdgfab pages 3-5): Kunal Kalra, Joerg Eberhard, Nona Farbehi, James J. Chong, and Munira Xaymardan. Role of pdgf-a/b ligands in cardiac repair after myocardial infarction. Frontiers in Cell and Developmental Biology, Aug 2021. URL: https://doi.org/10.3389/fcell.2021.669188, doi:10.3389/fcell.2021.669188. This article has 68 citations.

12. (kadrmas2020geneticanalysesin pages 4-5): Julie L. Kadrmas, Mary C. Beckerle, and Masaaki Yoshigi. Genetic analyses in mouse fibroblast and melanoma cells demonstrate novel roles for pdgf-ab ligand and pdgf receptor alpha. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-75774-3, doi:10.1038/s41598-020-75774-3. This article has 11 citations and is from a peer-reviewed journal.

13. (rogers2020theemergingcomplexity pages 3-4): Madison A. Rogers and Katherine A. Fantauzzo. The emerging complexity of pdgfrs: activation, internalization and signal attenuation. Biochemical Society transactions, 48:1167-1176, May 2020. URL: https://doi.org/10.1042/bst20200004, doi:10.1042/bst20200004. This article has 46 citations and is from a peer-reviewed journal.

14. (jung2025rolesofpdgfpdgfr pages 3-4): Sung-Cherl Jung, Dawon Kang, and Eun-A Ko. Roles of pdgf/pdgfr signaling in various organs. The Korean Journal of Physiology & Pharmacology : Official Journal of the Korean Physiological Society and the Korean Society of Pharmacology, 29:139-155, Oct 2025. URL: https://doi.org/10.4196/kjpp.24.309, doi:10.4196/kjpp.24.309. This article has 26 citations.

15. (solinc2022theplateletderivedgrowth pages 4-7): Julien Solinc, Jonathan Ribot, Florent Soubrier, Catherine Pavoine, France Dierick, and Sophie Nadaud. The platelet-derived growth factor pathway in pulmonary arterial hypertension: still an interesting target? Life, 12:658, Apr 2022. URL: https://doi.org/10.3390/life12050658, doi:10.3390/life12050658. This article has 38 citations.

16. (rogers2020theemergingcomplexity pages 1-3): Madison A. Rogers and Katherine A. Fantauzzo. The emerging complexity of pdgfrs: activation, internalization and signal attenuation. Biochemical Society transactions, 48:1167-1176, May 2020. URL: https://doi.org/10.1042/bst20200004, doi:10.1042/bst20200004. This article has 46 citations and is from a peer-reviewed journal.

17. (rogers2020theemergingcomplexity pages 12-14): Madison A. Rogers and Katherine A. Fantauzzo. The emerging complexity of pdgfrs: activation, internalization and signal attenuation. Biochemical Society transactions, 48:1167-1176, May 2020. URL: https://doi.org/10.1042/bst20200004, doi:10.1042/bst20200004. This article has 46 citations and is from a peer-reviewed journal.

18. (pierotti2026regulationandactivity pages 4-4): Catia L. Pierotti and Maja Köhn. Regulation and activity of the phosphatase shp2: sh2 domains, dephosphorylation activity, and beyond. Biochemical Journal, 54:15-24, Jan 2026. URL: https://doi.org/10.1042/bst20253102, doi:10.1042/bst20253102. This article has 2 citations and is from a domain leading peer-reviewed journal.

19. (pierotti2026regulationandactivity pages 2-3): Catia L. Pierotti and Maja Köhn. Regulation and activity of the phosphatase shp2: sh2 domains, dephosphorylation activity, and beyond. Biochemical Journal, 54:15-24, Jan 2026. URL: https://doi.org/10.1042/bst20253102, doi:10.1042/bst20253102. This article has 2 citations and is from a domain leading peer-reviewed journal.

20. (wang2024theconfigurationof pages 9-11): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

21. (perezbaena2023theroleof pages 2-4): Manuel Jesús Pérez-Baena, Francisco Josué Cordero-Pérez, Jesús Pérez-Losada, and Marina Holgado-Madruga. The role of gab1 in cancer. Cancers, 15:4179, Aug 2023. URL: https://doi.org/10.3390/cancers15164179, doi:10.3390/cancers15164179. This article has 28 citations.

22. (rogers2020theemergingcomplexity pages 6-8): Madison A. Rogers and Katherine A. Fantauzzo. The emerging complexity of pdgfrs: activation, internalization and signal attenuation. Biochemical Society transactions, 48:1167-1176, May 2020. URL: https://doi.org/10.1042/bst20200004, doi:10.1042/bst20200004. This article has 46 citations and is from a peer-reviewed journal.

23. (wu2021plateletderivedgrowthfactor pages 1-5): Kuanlin Wu, Hanzhi Wu, Wanqing Lyu, Youngjoo Kim, Cristina M. Furdui, Karen S. Anderson, and Anthony J. Koleske. Platelet-derived growth factor receptor beta activates abl2 via direct binding and phosphorylation. Journal of Biological Chemistry, 297:100883, Jul 2021. URL: https://doi.org/10.1016/j.jbc.2021.100883, doi:10.1016/j.jbc.2021.100883. This article has 6 citations and is from a domain leading peer-reviewed journal.

24. (wang2024theconfigurationof pages 2-4): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

25. (wang2024theconfigurationof pages 1-2): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

26. (wang2024theconfigurationof pages 18-19): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

27. (jung2025rolesofpdgfpdgfr pages 2-3): Sung-Cherl Jung, Dawon Kang, and Eun-A Ko. Roles of pdgf/pdgfr signaling in various organs. The Korean Journal of Physiology & Pharmacology : Official Journal of the Korean Physiological Society and the Korean Society of Pharmacology, 29:139-155, Oct 2025. URL: https://doi.org/10.4196/kjpp.24.309, doi:10.4196/kjpp.24.309. This article has 26 citations.

28. (wang2024theconfigurationof pages 19-21): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

29. (perezbaena2023theroleof pages 12-13): Manuel Jesús Pérez-Baena, Francisco Josué Cordero-Pérez, Jesús Pérez-Losada, and Marina Holgado-Madruga. The role of gab1 in cancer. Cancers, 15:4179, Aug 2023. URL: https://doi.org/10.3390/cancers15164179, doi:10.3390/cancers15164179. This article has 28 citations.

30. (rauniyar2023expansionandcollapse pages 14-15): Khushbu Rauniyar, Honey Bokharaie, and Michael Jeltsch. Expansion and collapse of vegf diversity in major clades of the animal kingdom. Angiogenesis, 26:437-461, Apr 2023. URL: https://doi.org/10.1007/s10456-023-09874-9, doi:10.1007/s10456-023-09874-9. This article has 21 citations and is from a domain leading peer-reviewed journal.

31. (zhao2026pdgfsignalingin pages 2-3): Qiang-qiang Zhao, Feihong Che, Weiwen Liu, Chengyu Hou, Lijuan Yu, Yonghui Hou, and Liangliang Xu. Pdgf signaling in cartilage regeneration: molecular mechanisms and cellular effects. Frontiers in Cell and Developmental Biology, Feb 2026. URL: https://doi.org/10.3389/fcell.2026.1778703, doi:10.3389/fcell.2026.1778703. This article has 1 citations.

32. (rogers2020theemergingcomplexity pages 4-6): Madison A. Rogers and Katherine A. Fantauzzo. The emerging complexity of pdgfrs: activation, internalization and signal attenuation. Biochemical Society transactions, 48:1167-1176, May 2020. URL: https://doi.org/10.1042/bst20200004, doi:10.1042/bst20200004. This article has 46 citations and is from a peer-reviewed journal.

33. (tang2022negativeregulationof pages 2-3): Rong Tang, Wallace Y. Langdon, and Jian Zhang. Negative regulation of receptor tyrosine kinases by ubiquitination: key roles of the cbl family of e3 ubiquitin ligases. Frontiers in Endocrinology, Jul 2022. URL: https://doi.org/10.3389/fendo.2022.971162, doi:10.3389/fendo.2022.971162. This article has 43 citations.

34. (rogers2020theemergingcomplexity pages 11-12): Madison A. Rogers and Katherine A. Fantauzzo. The emerging complexity of pdgfrs: activation, internalization and signal attenuation. Biochemical Society transactions, 48:1167-1176, May 2020. URL: https://doi.org/10.1042/bst20200004, doi:10.1042/bst20200004. This article has 46 citations and is from a peer-reviewed journal.

35. (rogers2020theemergingcomplexity pages 10-11): Madison A. Rogers and Katherine A. Fantauzzo. The emerging complexity of pdgfrs: activation, internalization and signal attenuation. Biochemical Society transactions, 48:1167-1176, May 2020. URL: https://doi.org/10.1042/bst20200004, doi:10.1042/bst20200004. This article has 46 citations and is from a peer-reviewed journal.

36. (margiotta2021allgoodthings pages 6-7): Azzurra Margiotta. All good things must end: termination of receptor tyrosine kinase signal. International Journal of Molecular Sciences, 22:6342, Jun 2021. URL: https://doi.org/10.3390/ijms22126342, doi:10.3390/ijms22126342. This article has 17 citations.

37. (guerit2021pdgfreceptormutations pages 8-9): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

38. (guerit2021pdgfreceptormutations pages 11-12): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

39. (guerit2021pdgfreceptormutations pages 2-5): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

40. (guerit2021pdgfreceptormutations pages 5-6): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

41. (guerit2021pdgfreceptormutations pages 12-13): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

42. (guerit2021pdgfreceptormutations pages 6-8): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

43. (OpenTargets Search: -PDGFRB,PDGFRA,PDGFB): Open Targets Query (-PDGFRB,PDGFRA,PDGFB, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

44. (guerit2021pdgfreceptormutations pages 10-11): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 157 citations and is from a domain leading peer-reviewed journal.

45. (kadrmas2020geneticanalysesin pages 7-9): Julie L. Kadrmas, Mary C. Beckerle, and Masaaki Yoshigi. Genetic analyses in mouse fibroblast and melanoma cells demonstrate novel roles for pdgf-ab ligand and pdgf receptor alpha. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-75774-3, doi:10.1038/s41598-020-75774-3. This article has 11 citations and is from a peer-reviewed journal.

46. (wang2024theconfigurationof pages 12-14): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

47. (wang2024theconfigurationof pages 4-5): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

48. (wang2024theconfigurationof pages 11-12): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

49. (kadrmas2020geneticanalysesin pages 2-4): Julie L. Kadrmas, Mary C. Beckerle, and Masaaki Yoshigi. Genetic analyses in mouse fibroblast and melanoma cells demonstrate novel roles for pdgf-ab ligand and pdgf receptor alpha. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-75774-3, doi:10.1038/s41598-020-75774-3. This article has 11 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](pdgfr_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](pdgfr_signaling-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](pdgfr_signaling-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. guerit2021pdgfreceptormutations pages 1-2
2. rogers2020theemergingcomplexity pages 3-4
3. rogers2020theemergingcomplexity pages 12-14
4. zhao2026pdgfsignalingin pages 3-5
5. wu2021plateletderivedgrowthfactor pages 1-5
6. wang2024theconfigurationof pages 1-2
7. wang2024theconfigurationof pages 2-4
8. solinc2022theplateletderivedgrowth pages 4-7
9. kadrmas2020geneticanalysesin pages 1-2
10. wang2024theconfigurationof pages 19-21
11. wang2024theconfigurationof pages 18-19
12. rauniyar2023expansionandcollapse pages 1-3
13. rauniyar2023expansionandcollapse pages 14-15
14. rauniyar2023expansionandcollapse pages 3-6
15. jung2025rolesofpdgfpdgfr pages 2-3
16. jung2025rolesofpdgfpdgfr pages 3-4
17. kalra2021roleofpdgfab pages 3-5
18. ma2024targetingpdgfpdgfrsignaling pages 4-6
19. zhao2026pdgfsignalingin pages 2-3
20. rogers2020theemergingcomplexity pages 4-6
21. rogers2020theemergingcomplexity pages 6-8
22. margiotta2021allgoodthings pages 6-7
23. guerit2021pdgfreceptormutations pages 6-8
24. guerit2021pdgfreceptormutations pages 8-9
25. solinc2022theplateletderivedgrowth pages 7-8
26. tang2022negativeregulationof pages 2-3
27. solinc2022theplateletderivedgrowth pages 3-4
28. jung2025rolesofpdgfpdgfr pages 1-2
29. ma2024targetingpdgfpdgfrsignaling pages 18-19
30. kadrmas2020geneticanalysesin pages 4-5
31. rogers2020theemergingcomplexity pages 1-3
32. pierotti2026regulationandactivity pages 4-4
33. pierotti2026regulationandactivity pages 2-3
34. wang2024theconfigurationof pages 9-11
35. perezbaena2023theroleof pages 2-4
36. perezbaena2023theroleof pages 12-13
37. rogers2020theemergingcomplexity pages 11-12
38. rogers2020theemergingcomplexity pages 10-11
39. guerit2021pdgfreceptormutations pages 11-12
40. guerit2021pdgfreceptormutations pages 2-5
41. guerit2021pdgfreceptormutations pages 5-6
42. guerit2021pdgfreceptormutations pages 12-13
43. guerit2021pdgfreceptormutations pages 10-11
44. kadrmas2020geneticanalysesin pages 7-9
45. wang2024theconfigurationof pages 12-14
46. wang2024theconfigurationof pages 4-5
47. wang2024theconfigurationof pages 11-12
48. kadrmas2020geneticanalysesin pages 2-4
49. https://doi.org/10.3390/life12050658,
50. https://doi.org/10.1038/s41598-020-75774-3,
51. https://doi.org/10.3389/fcell.2026.1778703,
52. https://doi.org/10.4196/kjpp.24.309,
53. https://doi.org/10.1007/s00018-020-03753-y,
54. https://doi.org/10.1007/s10456-023-09874-9,
55. https://doi.org/10.3390/biom14111446,
56. https://doi.org/10.3389/fcell.2021.669188,
57. https://doi.org/10.1042/bst20200004,
58. https://doi.org/10.1042/bst20253102,
59. https://doi.org/10.3390/biom14030259,
60. https://doi.org/10.3390/cancers15164179,
61. https://doi.org/10.1016/j.jbc.2021.100883,
62. https://doi.org/10.3389/fendo.2022.971162,
63. https://doi.org/10.3390/ijms22126342,