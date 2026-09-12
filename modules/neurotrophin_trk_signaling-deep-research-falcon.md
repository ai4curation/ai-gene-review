---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T17:05:12.243601'
end_time: '2026-06-28T17:26:13.476919'
duration_seconds: 1261.23
template_file: templates/module_research.md.j2
template_variables:
  module_title: Neurotrophin TRK receptor signaling pathway module
  module_summary: Neurotrophins activate TRK receptor tyrosine kinases, engaging Ras-MAPK,
    PI3K-AKT, and PLC-gamma branches that regulate neuronal survival, differentiation,
    and plasticity.
  module_outline: "- Neurotrophin TRK receptor signaling pathway\n  - 1. neurotrophin-trk\
    \ ligation\n  - Neurotrophin engages TRK receptor\n    - NGF ligand (molecular\
    \ player: NGF)\n    - BDNF ligand (molecular player: BDNF)\n    - NTRK1/TRKA receptor\
    \ (molecular player: NTRK1/TRKA receptor family/ortholog group)\n    - NTRK2/TRKB\
    \ receptor (molecular player: NTRK2/TRKB receptor family/ortholog group)\n  -\
    \ 2. trk adaptor recruitment\n  - TRK adaptor recruitment\n    - GRB2 adaptor\
    \ (molecular player: GRB2 adaptor family/ortholog group)\n    - PI3K p85 adaptor\
    \ (molecular player: PI3K p85 adaptor family/ortholog group)\n  - 3. neuronal\
    \ survival output\n  - Neuronal survival and differentiation output\n    - TRKA\
    \ kinase output (molecular player: TRKA kinase output family/ortholog group)\n\
    \    - TRKB kinase output (molecular player: TRKB kinase output family/ortholog\
    \ group)"
  module_connections: '- Neurotrophin engages TRK receptor causes TRK adaptor recruitment:
    The initiating event promotes trk adaptor recruitment.

    - TRK adaptor recruitment causes Neuronal survival and differentiation output:
    TRK adaptor recruitment leads to neuronal survival output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: neurotrophin_trk_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: neurotrophin_trk_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Neurotrophin TRK receptor signaling pathway module

## Working Scope

Neurotrophins activate TRK receptor tyrosine kinases, engaging Ras-MAPK, PI3K-AKT, and PLC-gamma branches that regulate neuronal survival, differentiation, and plasticity.

## Provisional Biological Outline

- Neurotrophin TRK receptor signaling pathway
  - 1. neurotrophin-trk ligation
  - Neurotrophin engages TRK receptor
    - NGF ligand (molecular player: NGF)
    - BDNF ligand (molecular player: BDNF)
    - NTRK1/TRKA receptor (molecular player: NTRK1/TRKA receptor family/ortholog group)
    - NTRK2/TRKB receptor (molecular player: NTRK2/TRKB receptor family/ortholog group)
  - 2. trk adaptor recruitment
  - TRK adaptor recruitment
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)
  - 3. neuronal survival output
  - Neuronal survival and differentiation output
    - TRKA kinase output (molecular player: TRKA kinase output family/ortholog group)
    - TRKB kinase output (molecular player: TRKB kinase output family/ortholog group)

## Known Relationships Among Steps

- Neurotrophin engages TRK receptor causes TRK adaptor recruitment: The initiating event promotes trk adaptor recruitment.
- TRK adaptor recruitment causes Neuronal survival and differentiation output: TRK adaptor recruitment leads to neuronal survival output.

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

Neurotrophin TRK receptor signaling pathway module

## Working Scope

Neurotrophins activate TRK receptor tyrosine kinases, engaging Ras-MAPK, PI3K-AKT, and PLC-gamma branches that regulate neuronal survival, differentiation, and plasticity.

## Provisional Biological Outline

- Neurotrophin TRK receptor signaling pathway
  - 1. neurotrophin-trk ligation
  - Neurotrophin engages TRK receptor
    - NGF ligand (molecular player: NGF)
    - BDNF ligand (molecular player: BDNF)
    - NTRK1/TRKA receptor (molecular player: NTRK1/TRKA receptor family/ortholog group)
    - NTRK2/TRKB receptor (molecular player: NTRK2/TRKB receptor family/ortholog group)
  - 2. trk adaptor recruitment
  - TRK adaptor recruitment
    - GRB2 adaptor (molecular player: GRB2 adaptor family/ortholog group)
    - PI3K p85 adaptor (molecular player: PI3K p85 adaptor family/ortholog group)
  - 3. neuronal survival output
  - Neuronal survival and differentiation output
    - TRKA kinase output (molecular player: TRKA kinase output family/ortholog group)
    - TRKB kinase output (molecular player: TRKB kinase output family/ortholog group)

## Known Relationships Among Steps

- Neurotrophin engages TRK receptor causes TRK adaptor recruitment: The initiating event promotes trk adaptor recruitment.
- TRK adaptor recruitment causes Neuronal survival and differentiation output: TRK adaptor recruitment leads to neuronal survival output.

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

# Neurotrophin–TRK Receptor Signaling Pathway: A Mechanistic Review

## 1. Executive Summary

Neurotrophin signaling through tropomyosin receptor kinase (Trk) receptors constitutes a fundamental signaling module in vertebrate neurobiology, governing neuronal survival, differentiation, axon growth, synaptic plasticity, and memory formation. The core system comprises four neurotrophins (NGF, BDNF, NT-3, NT-4/5) that engage three Trk receptor tyrosine kinases (TrkA/NTRK1, TrkB/NTRK2, TrkC/NTRK3) with defined selectivity, augmented by the low-affinity p75 neurotrophin receptor (p75NTR/NGFR). Ligand binding triggers receptor dimerization, trans-autophosphorylation, and recruitment of adaptor proteins—principally SHC, GRB2, and FRS2—to phosphotyrosine docking sites on the receptor intracellular domain. These adaptors nucleate three canonical downstream cascades: Ras-MAPK (via GRB2-SOS), PI3K-AKT (via p85/p110 recruitment through GAB1/IRS intermediaries), and PLCγ1-Ca²⁺/PKC (via direct PLCγ1 docking) (enkavi2026moleculardeterminantsof pages 5-6, enkavi2026moleculardeterminantsof pages 3-5). The system is conserved across vertebrates, with neurotrophins showing high sequence identity from fish to mammals, while its evolutionary roots extend to invertebrate neurotrophin-like molecules (carrillomunoz2025neurotrophinsandtheir pages 2-4, carrillomunoz2025neurotrophinsandtheir pages 4-6). Clinical exploitation of TRK biology has advanced rapidly, with FDA-approved TRK inhibitors (larotrectinib, entrectinib, repotrectinib) transforming the treatment of NTRK fusion-positive cancers (yang2023safetyofcurrent pages 1-3, yang2023safetyofcurrent pages 18-22). Key unresolved questions include the structural basis of ligand bias across Trk subtypes, the relative contributions of surface versus endosomal signaling, and the functional significance of truncated receptor isoforms.

## 2. Definition and Biological Boundaries

### What the system includes

The neurotrophin–Trk signaling pathway, as defined here, encompasses the molecular events from neurotrophin–Trk receptor engagement at the cell surface through the three principal intracellular signaling branches (Ras-MAPK, PI3K-AKT, PLCγ-Ca²⁺/PKC), their immediate effectors, and the specialized endosomal signaling compartment that sustains long-distance retrograde signaling in neurons (enkavi2026moleculardeterminantsof pages 3-5, moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2). The pathway includes the co-receptor p75NTR insofar as it modulates Trk ligand selectivity and affinity, though p75NTR-autonomous signaling (e.g., ceramide generation, JNK-dependent apoptosis) represents a related but mechanistically distinct pathway (enkavi2026moleculardeterminantsof pages 2-3, numakawa2022theroleof pages 2-4).

### Neighboring systems to distinguish

Several signaling modules are frequently conflated with neurotrophin–Trk signaling but should be treated as distinct entities:

- **p75NTR-dependent apoptotic signaling**: When p75NTR engages pro-neurotrophins (proNGF, proBDNF) in complex with sortilin, it activates JNK and caspase cascades independently of Trk activity (enkavi2026moleculardeterminantsof pages 2-3).
- **GDNF/RET signaling**: Although RET shares downstream GRB2-mediated Ras-MAPK activation with Trk receptors, it couples to a distinct receptor complex (GFRα/RET) and employs partially different adaptor logic (enkavi2026moleculardeterminantsof pages 5-6).
- **Generic RTK-Ras-MAPK cascades**: The Ras-MAPK module downstream of Trk overlaps extensively with EGFR, FGFR, and other RTK signaling, but the upstream receptor architecture, adaptor preferences (especially FRS2 competition with SHC), and neuronal-specific outputs are Trk-distinctive (enkavi2026moleculardeterminantsof pages 5-6).
- **NTRK fusion oncoproteins**: While these chimeric proteins retain the Trk kinase domain and activate the same downstream cascades, they are constitutively active, ligand-independent, and typically lack the extracellular neurotrophin-binding domain. Their biology is better classified under oncogenic kinase signaling than under physiological neurotrophin signaling (yang2023safetyofcurrent pages 1-3, bungaro2024ntrk123biologydetection pages 1-2).

## 3. Mechanistic Overview

### 3.1. Neurotrophin–Trk Ligation

Neurotrophins are secreted as homodimers that bind to the second immunoglobulin-like domain (Ig2) on the Trk receptor extracellular domain with defined selectivity: NGF binds TrkA, BDNF and NT-4/5 bind TrkB, and NT-3 preferentially binds TrkC but can also activate TrkA and TrkB under certain conditions (harun2025modulationofbdnftrkb pages 4-6, enkavi2026moleculardeterminantsof pages 2-3). Recent structural and functional studies indicate that Trk receptors may exist as preformed inactive dimers prior to ligand binding; neurotrophin binding stabilizes the dimer conformation and induces structural rearrangements that relieve autoinhibition of the intracellular kinase domain (enkavi2026moleculardeterminantsof pages 5-6, enkavi2026moleculardeterminantsof pages 3-5).

The co-receptor p75NTR shapes ligand selectivity in an important and receptor-specific manner: for TrkA, p75NTR enhances NGF specificity while reducing NT-3 responsiveness; for TrkB, p75NTR restricts activation primarily to BDNF; for TrkC, the modulatory effect is less clearly defined (enkavi2026moleculardeterminantsof pages 2-3). This co-receptor function ensures that neuronal survival in the peripheral nervous system is tightly coupled to the availability of the appropriate growth factor in the target field.

### 3.2. Receptor Activation and Phosphotyrosine Docking Sites

Ligand-stabilized dimerization brings the intracellular kinase domains into proximity, enabling trans-autophosphorylation at activation-loop tyrosines (Y674/Y675 in TrkA numbering), which fully activates catalytic function (forsell2024positiveallostericmodulators pages 4-6, enkavi2026moleculardeterminantsof pages 3-5). The activated kinase then phosphorylates additional tyrosine residues on the receptor intracellular domain, creating specific docking sites for adaptor proteins:

- **Y490/Y496 (TrkA) / Y516 (TrkB) / Y522 (TrkC)**: Juxtamembrane phosphotyrosines that recruit the SHC adaptor protein, initiating the Ras-MAPK branch. FRS2 competes with SHC for this same docking site but supports prolonged ERK activation through distinct downstream wiring involving GRB2 and SHP-2 (enkavi2026moleculardeterminantsof pages 5-6, enkavi2026moleculardeterminantsof pages 3-5).
- **Y751 (TrkA numbering)**: Recruits the PI3K p85 regulatory subunit, though PI3K can also be engaged indirectly through GRB2-linked adaptor proteins GAB1 and IRS-1/2 (forsell2024positiveallostericmodulators pages 4-6, enkavi2026moleculardeterminantsof pages 5-6).
- **Y785 (TrkA) / Y817 (TrkB) / Y823 (TrkC)**: C-terminal phosphotyrosines that recruit PLCγ1, initiating the calcium/PKC signaling branch (enkavi2026moleculardeterminantsof pages 5-6, forsell2024positiveallostericmodulators pages 4-6).

### 3.3. Adaptor Recruitment

**SHC and GRB2**: The SHC adaptor protein binds via its PTB domain to the juxtamembrane phosphotyrosine and is itself phosphorylated by Trk kinase at Tyr317 and Tyr239/Tyr240. Phosphorylated SHC recruits GRB2 through the GRB2 SH2 domain, which recognizes the pYVNV motif. GRB2 is a non-enzymatic adaptor with a characteristic SH2-SH3-SH3 architecture: its central SH2 domain binds phosphotyrosines on activated receptors or adaptors, while its flanking SH3 domains constitutively associate with the proline-rich regions of the guanine nucleotide exchange factor SOS (wang2024theconfigurationof pages 2-4, wang2024theconfigurationof pages 1-2, wang2024theconfigurationof pages 12-14). The assembly of the Shc-GRB2-SOS complex favors dimeric GRB2, which binds Shc phosphotyrosines with higher affinity than monomeric GRB2 (wang2024theconfigurationof pages 12-14). Membrane-recruited SOS then catalyzes GDP-to-GTP exchange on Ras, committing the signal to the Raf-MEK-ERK1/2 cascade (wang2024theconfigurationof pages 2-4, enkavi2026moleculardeterminantsof pages 3-5).

**FRS2**: This lipid-anchored adaptor competes with SHC for the same juxtamembrane phosphotyrosine site but generates a qualitatively different signal: recruitment of both GRB2 and SHP-2 phosphatase produces a more sustained ERK activation, which is associated with differentiation rather than acute proliferative responses (enkavi2026moleculardeterminantsof pages 5-6).

**PI3K p85**: The p85 regulatory subunit of class IA PI3K is recruited to phosphotyrosine motifs on the receptor or on adaptor intermediaries (GAB1, IRS-1/2). Upon recruitment, the p85-p110 heterodimer positions the p110 catalytic subunit at the plasma membrane, where it phosphorylates phosphatidylinositol (4,5)-bisphosphate (PIP2) to generate PIP3. PIP3 then recruits PDK1 and AKT/PKB to the membrane for activation (enkavi2026moleculardeterminantsof pages 5-6, forsell2024positiveallostericmodulators pages 4-6).

### 3.4. The Three Canonical Downstream Branches

The following table summarizes the three canonical branches, their initiating events, temporal dynamics, and functional outputs:

| Signaling Branch | Initiating Phosphotyrosine Site | Key Adaptors/Intermediaries | Core Kinase Cascade | Primary Biological Outcomes | Temporal Dynamics | Obligatoriness / Conditionality for Neuronal Functions | Clinical / Therapeutic Relevance |
|---|---|---|---|---|---|---|---|
| Ras-MAPK | Juxtamembrane Trk phosphotyrosines that recruit Shc: TrkA Y496, TrkB Y516, TrkC Y522; older numbering schemes often reference Y490-class docking sites (enkavi2026moleculardeterminantsof pages 3-5, forsell2024positiveallostericmodulators pages 4-6) | Shc → GRB2 → SOS; FRS2 can compete with Shc at the docking site and support prolonged ERK signaling; SHP2 contributes in FRS2-containing assemblies (enkavi2026moleculardeterminantsof pages 3-5, enkavi2026moleculardeterminantsof pages 5-6, wang2024theconfigurationof pages 12-14) | Ras-GTP → Raf → MEK1/2 → ERK1/2 (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) | Neurite outgrowth, differentiation, transcriptional reprogramming, survival support, growth-promoting signaling (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5, enkavi2026moleculardeterminantsof pages 2-3) | Typically rapid and early after receptor activation; can be transient via Shc-GRB2-SOS or more sustained when FRS2 scaffolding predominates (enkavi2026moleculardeterminantsof pages 5-6) | Often close to obligatory for classical trophic differentiation/outgrowth programs, but the duration and amplitude needed are context-specific; prolonged ERK signaling is especially associated with differentiation rather than merely acute survival (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) | Central to oncogenic NTRK fusion signaling and therefore indirectly targeted by TRK inhibitors; pathway-shape and adaptor usage may influence resistance and signaling bias in tumors and neurons (yang2023safetyofcurrent pages 1-3, yang2023safetyofcurrent pages 18-22, yang2023safetyofcurrent pages 17-18) |
| PI3K-AKT | Commonly linked to Trk phosphotyrosines through receptor/adaptor assemblies; older literature often cites Y751-class recruitment logic, while recent syntheses emphasize recruitment through GRB2-linked adaptors such as GAB1 and IRS proteins (forsell2024positiveallostericmodulators pages 4-6, enkavi2026moleculardeterminantsof pages 5-6) | PI3K regulatory subunit p85/p110 complex, GAB1, IRS-1/2, GRB2-associated adaptors; PDK1 and mTOR function downstream of PIP3-AKT signaling (enkavi2026moleculardeterminantsof pages 5-6, kim2024theroleof pages 1-2, carrillomunoz2025neurotrophinsandtheir pages 4-6) | PI3K converts PIP2 to PIP3 → PDK1 / AKT activation → mTOR and downstream survival/growth effectors (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) | Anti-apoptotic signaling, metabolic support, protein synthesis, neuronal survival, growth, structural plasticity (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5, moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3) | Usually activated early, but can remain engaged over longer periods through endosomal signaling and coupling to mTOR/protein synthesis programs (moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2, moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3) | Frequently obligatory for robust survival signaling, but conditional for specific long-distance axon-to-soma responses; for example, some retrograde BDNF/TrkB transport steps appear less dependent on axonal PI3K than on PLCγ, whereas somatodendritic growth outputs can still require PI3K/mTOR (moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2, moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3) | Major survival branch downstream of native Trk receptors and oncogenic TRK fusions; therapeutically relevant to resistance, neuroprotection, synaptic plasticity, and candidate Trk agonist/PAM development (yang2023safetyofcurrent pages 1-3, yang2023safetyofcurrent pages 18-22, forsell2024positiveallostericmodulators pages 4-6, forsell2024positiveallostericmodulators pages 15-17) |
| PLCγ-Ca2+/PKC | C-terminal PLCγ docking phosphotyrosines: classically TrkA Y785 and TrkB Y817; broader Trk C-terminal phosphosite clusters also contribute in some summaries (enkavi2026moleculardeterminantsof pages 5-6, forsell2024positiveallostericmodulators pages 4-6) | PLCγ1, IP3, DAG, intracellular Ca2+ stores, calcineurin, dynamin-dependent endocytic machinery, PKC (moyaalvarado2024plcγca2+pathwayregulates pages 7-10, bazzari2022bdnftherapeuticmechanisms pages 4-5) | PLCγ1 hydrolyzes PIP2 → IP3 + DAG → Ca2+ release and PKC activation (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) | Calcium signaling, synaptic plasticity, dendritic branching, receptor endocytosis, signaling endosome formation, long-distance axonal signaling to CREB in the soma (moyaalvarado2024plcγca2+pathwayregulates pages 2-3, moyaalvarado2024plcγca2+pathwayregulates pages 6-7, moyaalvarado2024plcγca2+pathwayregulates pages 7-10) | Rapid local Ca2+ transients in axons followed by slower endocytosis-dependent retrograde signaling; particularly important for spatially organized signaling from axon terminals (moyaalvarado2024plcγca2+pathwayregulates pages 1-2, moyaalvarado2024plcγca2+pathwayregulates pages 7-10) | Strongly conditional: not universally required for all Trk outputs, but specifically obligatory for some axonal BDNF/TrkB long-distance signaling events, including TrkB endocytosis, signaling endosome formation, nuclear CREB activation, and dendritic arborization driven by axonal stimulation (moyaalvarado2024plcγca2+pathwayregulates pages 2-3, moyaalvarado2024plcγca2+pathwayregulates pages 6-7, moyaalvarado2024plcγca2+pathwayregulates pages 1-2, moyaalvarado2024plcγca2+pathwayregulates pages 7-10) | Especially relevant to plasticity-oriented and compartmentalized Trk biology; mutations affecting the PLCγ docking interaction impair learning/LTP-related outputs, and this branch is a key consideration in efforts to bias Trk agonism therapeutically (moyaalvarado2024plcγca2+pathwayregulates pages 15-16, enkavi2026moleculardeterminantsof pages 8-9, maher2024atemporal(phospho)proteomic pages 2-3) |


*Table: This table compares the three canonical downstream branches of neurotrophin-TRK signaling by docking site, intermediaries, dynamics, and functional logic. It is useful for distinguishing which outputs are broadly trophic versus specifically required for compartmentalized neuronal plasticity and long-distance signaling.*

**Ras-MAPK branch**: Following SOS-mediated Ras-GTP loading, Ras activates the serine/threonine kinase Raf, which phosphorylates and activates MEK1/2, which in turn phosphorylates and activates ERK1/2. ERK1/2 translocates to the nucleus where it phosphorylates transcription factors that drive differentiation, survival, and growth programs (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5). The duration of ERK activation is a critical determinant of biological outcome: transient ERK activation (typically via SHC) supports acute survival, while sustained activation (often via FRS2) promotes differentiation (enkavi2026moleculardeterminantsof pages 5-6).

**PI3K-AKT branch**: AKT/PKB, once activated by PDK1-dependent phosphorylation at the PIP3-enriched membrane, phosphorylates numerous substrates that promote cell survival (BAD, Forkhead transcription factors), metabolism, protein synthesis via mTOR, and growth (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5). In neurons, this pathway is frequently obligatory for robust survival signaling (moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3).

**PLCγ-Ca²⁺/PKC branch**: PLCγ1 docking at C-terminal phosphotyrosines leads to its phosphorylation and activation, whereupon it hydrolyzes PIP2 into inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG). IP3 triggers calcium release from intracellular stores; DAG activates protein kinase C (PKC) isoforms (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5). Recent work has established that this branch plays a specialized and critical role in regulating TrkB receptor endocytosis and the formation of signaling endosomes required for long-distance axonal retrograde signaling (moyaalvarado2024plcγca2+pathwayregulates pages 2-3, moyaalvarado2024plcγca2+pathwayregulates pages 6-7, moyaalvarado2024plcγca2+pathwayregulates pages 1-2).

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive summary of the principal ligands, receptors, adaptors, and kinase modules in the pathway:

| Component | Gene/Protein Name | Primary Ligand or Function | Key Phosphorylation Sites (if applicable) | Primary Downstream Pathway | Biological Output |
|---|---|---|---|---|---|
| NGF | NGF | Canonical high-affinity ligand for TrkA; supports sympathetic and sensory neuron trophic signaling | N/A | Initiates TrkA signaling into Ras-MAPK, PI3K-AKT, PLCγ branches via receptor activation | Neuronal survival, differentiation, axon growth; context-dependent pain signaling (forsell2024positiveallostericmodulators pages 4-6, enkavi2026moleculardeterminantsof pages 2-3) |
| BDNF | BDNF | Canonical high-affinity ligand for TrkB; principal neurotrophin in many CNS circuits | N/A | Initiates TrkB signaling into Ras-MAPK, PI3K-AKT, PLCγ; can drive signaling endosome formation | Survival, synaptic plasticity, dendritic growth, memory-related transcription (harun2025modulationofbdnftrkb pages 4-6, moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2) |
| NT-3 | NTF3 / NT-3 | Preferred ligand for TrkC; can show conditional cross-reactivity depending on receptor context | N/A | Primarily activates TrkC signaling; can favor survival pathways in some contexts | Differentiation, survival, developmental patterning (enkavi2026moleculardeterminantsof pages 2-3, ateaque2023neurotrophinsignallingin pages 4-5) |
| NT-4/5 | NTF4 / NT-4/5 | TrkB ligand with signaling outputs partially distinct from BDNF | N/A | TrkB activation, often with relatively strong PI3K-AKT/anti-apoptotic signaling bias | Neuronal survival, maintenance, plasticity (enkavi2026moleculardeterminantsof pages 2-3, numakawa2022theroleof pages 2-4) |
| TrkA | NTRK1 / TrkA | RTK for NGF; prototypic neurotrophin receptor in PNS trophic signaling | Activation loop Y674/Y675; docking site Y490; additional Y751, Y785 commonly used as pathway-coupling sites | Ras-MAPK, PI3K-AKT, PLCγ | Survival, neurite outgrowth, differentiation; dependence receptor behavior in some peripheral neurons without ligand (forsell2024positiveallostericmodulators pages 4-6, enkavi2026moleculardeterminantsof pages 2-3) |
| TrkB | NTRK2 / TrkB | RTK for BDNF and NT-4/5; major CNS neurotrophin receptor | Activation loop Y674/Y675; juxtamembrane docking site Y516; PLCγ docking site Y817; Y490/Y785 frequently used in older numbering conventions | Ras-MAPK, PI3K-AKT, PLCγ; signaling endosome-mediated long-distance signaling | Synaptic plasticity, dendritic arborization, survival, memory-related gene expression (harun2025modulationofbdnftrkb pages 4-6, moyaalvarado2024plcγca2+pathwayregulates pages 2-3) |
| TrkC | NTRK3 / TrkC | RTK for NT-3; often associated with differentiation/favorable developmental programs | Juxtamembrane docking site Y522; analogous activation-loop phosphotyrosines as in Trk family | Ras-MAPK, PI3K-AKT, PLCγ | Differentiation and survival; context-dependent lineage specification (enkavi2026moleculardeterminantsof pages 5-6, siddi2026epigeneticregulationof pages 2-4) |
| p75NTR | NGFR / p75NTR | Low-affinity neurotrophin receptor and Trk coreceptor; shapes ligand selectivity and signaling context | No canonical Trk-like activation-loop phosphotyrosines | Modulates TrkA/TrkB specificity; can also signal independently | Enhances NGF specificity for TrkA, restricts TrkB activation largely to BDNF, regulates apoptosis/plasticity depending on context (enkavi2026moleculardeterminantsof pages 2-3, numakawa2022theroleof pages 2-4) |
| SHC | SHC1 (and family adaptors) | Phosphotyrosine adaptor docking to activated Trk juxtamembrane sites | SHC Tyr317 and Tyr239/Tyr240 classically support GRB2 binding; recruited to TrkA Y496 / TrkB Y516 / TrkC Y522 region | Ras-MAPK and also PI3K-linked signaling through adaptor scaffolds | Couples activated Trk receptors to GRB2-SOS and broader trophic signaling complexes (enkavi2026moleculardeterminantsof pages 3-5, wang2024theconfigurationof pages 12-14) |
| GRB2 | GRB2 | Adaptor linking phospho-SHC/RTKs to SOS via SH2-SH3 domain architecture | Not a main phospho-acceptor in core model; SH2 binds phosphotyrosines, SH3 binds SOS proline-rich motifs | Ras-MAPK; can also support PI3K pathway assembly indirectly | Membrane recruitment of SOS, promotion of Ras-GTP loading and signal propagation (wang2024theconfigurationof pages 2-4, wang2024theconfigurationof pages 1-2) |
| SOS | SOS1 / SOS2 | Ras guanine nucleotide exchange factor recruited by GRB2 | N/A in core pathway summary | Ras-MAPK | Converts Ras-GDP to Ras-GTP, initiating kinase cascade toward ERK (wang2024theconfigurationof pages 2-4, enkavi2026moleculardeterminantsof pages 3-5) |
| FRS2 | FRS2 | Alternative adaptor competing with SHC at Trk phosphotyrosine docking sites; recruits GRB2 and SHP2 | Phosphorylated after receptor engagement; specific sites not resolved in retrieved evidence | Sustained Ras-MAPK / ERK signaling | Prolonged ERK activation and signaling diversification downstream of Trk receptors (enkavi2026moleculardeterminantsof pages 5-6) |
| PI3K | PIK3R1/PIK3R2 (p85), PIK3CA/CB/CD (p110) | Lipid kinase recruited through adaptor complexes and/or receptor phosphotyrosines; converts PIP2 to PIP3 | Recruitment often associated with receptor/adaptor phosphotyrosines including Y751-type docking logic; p85 is regulatory subunit | PI3K-AKT | Survival, metabolism, growth, mTOR coupling, structural plasticity (forsell2024positiveallostericmodulators pages 4-6, carrillomunoz2025neurotrophinsandtheir pages 4-6) |
| PLCγ1 | PLCG1 | Binds activated Trk C-terminal phosphotyrosines and hydrolyzes PIP2 to IP3 + DAG | TrkA Y785 / TrkB Y817 class docking; receptor C-terminal phosphotyrosines reported as Y785/817/823 family positions in retrieved evidence | PLCγ-Ca2+ and PKC signaling | Calcium mobilization, endocytosis/signaling endosome formation, plasticity, dendritic growth (enkavi2026moleculardeterminantsof pages 5-6, moyaalvarado2024plcγca2+pathwayregulates pages 7-10) |
| Ras | HRAS / KRAS / NRAS | Small GTPase activated by SOS at plasma membrane/endosomal membranes | GDP-GTP cycle rather than canonical phosphorylation | Ras-MAPK | Commits signal to Raf-MEK-ERK cascade controlling growth and differentiation (wang2024theconfigurationof pages 2-4, enkavi2026moleculardeterminantsof pages 3-5) |
| Raf | ARAF / BRAF / RAF1 | Ser/Thr kinase activated downstream of Ras-GTP | Activating phosphorylation not specified in retrieved evidence | MAPK cascade | Propagates signal from Ras to MEK, supporting differentiation and growth programs (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) |
| MEK | MAP2K1 / MAP2K2 | Dual-specificity kinase downstream of Raf | Activating phosphorylation by Raf; precise sites not specified in retrieved evidence | MAPK cascade | Phosphorylates ERK1/2 to relay trophic signals (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) |
| ERK1/2 | MAPK3 / MAPK1 | Terminal kinase module of canonical Ras-MAPK branch | TEY-motif activation is canonical, but exact sites not specified in retrieved evidence | MAPK effector arm | Differentiation, neurite outgrowth, transcriptional reprogramming, survival support (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) |
| AKT/PKB | AKT1 / AKT2 / AKT3 | Ser/Thr kinase activated downstream of PI3K-PIP3 and PDK1 | Activated after PI3K-dependent membrane recruitment; exact sites not specified in retrieved evidence | PI3K-AKT | Anti-apoptotic signaling, metabolism, growth, mTOR activation, neuronal survival (enkavi2026moleculardeterminantsof pages 5-6, bazzari2022bdnftherapeuticmechanisms pages 4-5) |
| PKC | PRKC family | DAG/Ca2+-responsive kinase downstream of PLCγ | Isoform-specific activation rather than single shared phosphosite in this summary | PLCγ-PKC | Cytoskeletal remodeling, excitability/plasticity, endocytic and transcriptional responses (bazzari2022bdnftherapeuticmechanisms pages 4-5, moyaalvarado2024plcγca2+pathwayregulates pages 7-10) |


*Table: This table summarizes the principal ligands, receptors, adaptors, and kinase modules in neurotrophin-TRK signaling, with emphasis on docking phosphotyrosines, pathway branch points, and biological outputs. It is useful as a compact map of how NGF/BDNF/NT-3/NT-4 cues are translated into survival, differentiation, and plasticity responses.*

### 4.1. Signaling Endosomes: A Specialized Signaling Compartment

A distinctive feature of neurotrophin–Trk signaling in neurons is the signaling endosome, a specialized endocytic organelle that sustains active Trk signaling during dynein-dependent retrograde transport from axon terminals to the cell body (moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2, moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3). After BDNF binds TrkB at distal axons, the receptor-ligand complex is internalized via clathrin-mediated endocytosis into signaling endosomes that continue to activate downstream cascades during transit. Upon arrival at the soma, these endosomes coordinate CREB phosphorylation and mTOR-dependent protein synthesis, inducing dendritic growth and expression of plasticity-related genes such as Arc (moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2, moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3).

The formation of these signaling endosomes is critically regulated by the PLCγ-Ca²⁺ pathway: axonal BDNF stimulation activates PLCγ, which generates IP3-dependent calcium waves that promote TrkB endocytosis through calcineurin-mediated dephosphorylation of dynamin 1 (moyaalvarado2024plcγca2+pathwayregulates pages 1-2, moyaalvarado2024plcγca2+pathwayregulates pages 7-10). The small GTPase Rab10 has been identified as a critical regulator of TrkB sorting into retrograde signaling endosomes, defining a novel class of axonal organelles that are rapidly mobilized toward the axon terminal upon BDNF stimulation (moyaalvarado2024plcγca2+pathwayregulates pages 2-3). This system allows neurons to fine-tune retrograde signaling depending on BDNF availability at the synapse.

## 5. Evolutionary and Cell-Biological Variation

### 5.1. Evolutionary Conservation

The neurotrophin–Trk signaling system is deeply conserved across vertebrates. Neurotrophin genes are proposed to have arisen through whole-genome duplications near the root of vertebrate evolution, giving rise to the four mammalian family members (NGF, BDNF, NT-3, NT-4/5) and their cognate receptors (TrkA, TrkB, TrkC) (carrillomunoz2025neurotrophinsandtheir pages 4-6). In jawless vertebrates (lampreys), ancestral Trk receptors (Lf-Trk1 and Lf-Trk2) are proposed orthologs of TrkA/C and TrkB, respectively (carrillomunoz2025neurotrophinsandtheir pages 4-6). Fish neurotrophins show remarkable sequence conservation with mammalian counterparts: BDNF shares ~90% amino acid identity between fish and humans, while NGF shows ~67% identity (carrillomunoz2025neurotrophinsandtheir pages 4-6). Fish also possess additional neurotrophins (NT-6, NT-7) that exhibit structural similarity to mammalian NGF, representing lineage-specific elaborations (carrillomunoz2025neurotrophinsandtheir pages 4-6).

Neurotrophin-like molecules and Trk-related receptors have been identified in invertebrates, including *Drosophila*, indicating that the basic neurotrophin system predates the vertebrate radiation and may represent a common mechanism for nervous system formation across diverse phyla (forsell2024positiveallostericmodulators pages 15-17). The p75NTR co-receptor has been traced to a pre-bilaterian ancestor (designated PITA, "p75NTR Is The TNFR Ancestor"), which gave rise to the entire tumor necrosis factor receptor (TNFR) superfamily (carrillomunoz2025neurotrophinsandtheir pages 2-4, forsell2024positiveallostericmodulators pages 15-17). This suggests that the p75NTR lineage is more ancient than the Trk receptors, with the Trk-neurotrophin system evolving as a later vertebrate specialization layered onto a pre-existing p75NTR-based signaling framework.

### 5.2. Cell-Type and Tissue-Specific Variation

Neurotrophin–Trk signaling shows substantial variation across cell types and developmental contexts:

**PNS versus CNS**: TrkA and TrkC function as dependence receptors in peripheral sympathetic and sensory neurons, triggering apoptosis in the absence of their ligands; this mechanism ensures that only neurons receiving target-derived trophic support survive during development. TrkB, predominant in the CNS, does not exhibit this dependence receptor behavior, reflecting the different survival strategies of central versus peripheral neurons (enkavi2026moleculardeterminantsof pages 2-3).

**Neuronal subtypes**: In the developing visual cortex, BDNF and NT-4 exhibit layer-specific effects despite both activating TrkB: BDNF promotes dendritic growth preferentially in layer 4 pyramidal neurons, while NT-4 is more effective in layers 5 and 6, indicating that ligand identity carries information beyond simple receptor activation (numakawa2022theroleof pages 2-4).

**Truncated TrkB isoforms**: TrkB exists in multiple splice variants, including full-length TrkB-FL and truncated forms TrkB-T1 and TrkB-T2 that lack the intracellular kinase domain. TrkB-T1 is expressed at levels >100-fold higher than TrkB-FL in glial cells, where it functions as both a dominant-negative inhibitor of TrkB-FL signaling and an independent receptor that induces IP3-mediated calcium signaling, supporting neuroglial communication and astrocyte morphogenesis (bazzari2022bdnftherapeuticmechanisms pages 2-4). Imbalance between TrkB-FL and TrkB-T1 is observed in CNS injury and neuropathic pain models, and TrkB-T1 deletion in ALS mice delays motor neuron degeneration (numakawa2022theroleof pages 2-4).

**Dose- and duration-dependent signaling**: Saturating BDNF concentrations cause prolonged TrkB downregulation lasting at least 50 hours, while lower physiological concentrations allow receptor re-activation within 24 hours, suggesting that ligand concentration encodes qualitatively different signaling programs (ateaque2023neurotrophinsignallingin pages 4-5). At the level of ERK activation, transient TrkB engagement promotes neurite elongation and spine head enlargement, while sustained activation promotes neurite branching and spine neck elongation (numakawa2022theroleof pages 2-4).

**Non-neuronal contexts**: Trk receptors and their neurotrophin ligands are expressed in diverse non-nervous tissues including the immune, cardiovascular, musculoskeletal, and reproductive systems (carrillomunoz2025neurotrophinsandtheir pages 2-4). In cancer, the NGF/TrkA and BDNF/TrkB axes modulate the tumor microenvironment through effects on macrophage polarization, angiogenesis, and immune cell trafficking (siddi2026epigeneticregulationof pages 2-4).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1. Obligatory Sequence of Events

The pathway follows a strict temporal order: (1) neurotrophin binding → (2) receptor dimerization/stabilization → (3) activation-loop trans-autophosphorylation → (4) docking-site phosphorylation → (5) adaptor recruitment → (6) downstream cascade activation (enkavi2026moleculardeterminantsof pages 3-5). Steps 1–4 are obligatory and sequential; step 5 introduces branching, as different adaptors compete for overlapping or distinct docking sites.

### 6.2. Mutually Exclusive Adaptor Competitions

SHC and FRS2 compete for the same juxtamembrane phosphotyrosine, making their recruitment mutually exclusive at any given receptor molecule. The cellular outcome depends on the relative stoichiometry of these adaptors: SHC-dominated signaling produces transient ERK activation, while FRS2-dominated signaling produces sustained ERK activation and differentiation (enkavi2026moleculardeterminantsof pages 5-6).

### 6.3. Compartment-Specific Signaling

PLCγ activity in axons is specifically required for TrkB endocytosis and signaling endosome formation; the same pathway operating in the cell body does not contribute to long-distance retrograde signaling effects (moyaalvarado2024plcγca2+pathwayregulates pages 2-3, moyaalvarado2024plcγca2+pathwayregulates pages 6-7). PI3K activity, while essential for somatic survival signaling, appears less critical for axonal retrograde transport of BDNF-TrkB endosomes than the PLCγ-Ca²⁺ pathway (moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3, moyaalvarado2024plcγca2+pathwayregulates pages 6-7).

### 6.4. Negative Feedback and Pathway Termination

SPROUTY2 (SPRY2) acts as a potent negative regulator of Trk-mediated Ras-MAPK signaling by binding to GRB2 during RTK activation and inhibiting the GRB2-SOS complex, thereby attenuating downstream ERK cascade activity (wang2024theconfigurationof pages 2-4). The GRB2-Cbl complex provides additional negative feedback through receptor ubiquitination and degradation (wang2024theconfigurationof pages 14-15). Receptor downregulation following ligand stimulation represents a major pathway termination mechanism, with kinetics that depend on ligand concentration and receptor recycling rates (ateaque2023neurotrophinsignallingin pages 4-5).

### 6.5. Disease-Associated Failure Modes

**NTRK gene fusions**: Chromosomal rearrangements that fuse the Trk kinase domain to a constitutive dimerization partner generate ligand-independent, constitutively active oncoproteins. These fusions occur across >20 tumor types with varying frequency—high in rare tumors such as breast secretory carcinomas and infantile fibrosarcomas (>90%), but rare (<1%) in common cancers (yang2023safetyofcurrent pages 1-3, bungaro2024ntrk123biologydetection pages 1-2). First-generation TRK inhibitors larotrectinib and entrectinib achieve 57–75% overall response rates across tumor types, but acquired resistance emerges through on-target kinase domain mutations (e.g., solvent front mutations G595R in NTRK1, G623R in NTRK3) and off-target pathway bypass mechanisms (yang2023safetyofcurrent pages 1-3, yang2023safetyofcurrent pages 18-22). The second-generation TRK inhibitor repotrectinib, with its compact macrocyclic structure, retains activity against solvent front mutations and achieved a 53% response rate in TKI-pretreated patients with these resistance mutations (yang2023safetyofcurrent pages 18-22, yang2023safetyofcurrent pages 17-18).

**Neurodegeneration**: Reduced BDNF/TrkB signaling is consistently associated with Alzheimer's disease, depression, and age-related cognitive decline. However, BDNF itself has poor bioavailability and pharmacological properties, and exogenous BDNF administration risks off-target p75NTR activation. This has motivated development of selective TrkB agonist antibodies and positive allosteric modulators (PAMs) such as ACD856 and E2511, both of which have entered clinical Phase 1 studies (forsell2024positiveallostericmodulators pages 4-6, numakawa2022theroleof pages 2-4).

## 7. Controversies and Open Questions

### 7.1. Ligand Bias and Allosteric Modulation

Different neurotrophins binding the same Trk receptor can preferentially activate distinct downstream pathways (ligand bias), but the structural basis of this phenomenon remains incompletely understood. Evidence shows that NT-4 on TrkB preferentially activates PI3K/AKT for anti-apoptotic signaling, while BDNF engages broader pathway activation (enkavi2026moleculardeterminantsof pages 2-3). Point mutations in neurotrophins can produce ligands with similar Trk phosphorylation but distinct biological effects, suggesting that receptor conformational states, rather than simple phosphorylation levels, encode signaling specificity (enkavi2026moleculardeterminantsof pages 8-9). Allosteric modulation through juxtamembrane and transmembrane domains is emerging as a key mechanism for expanding signaling diversity, but full-length Trk receptor structures that would resolve this question remain unavailable (enkavi2026moleculardeterminantsof pages 2-3, enkavi2026moleculardeterminantsof pages 8-9).

### 7.2. Surface Versus Endosomal Signaling

While the signaling endosome model is well-supported for long-distance axonal retrograde signaling, the relative contributions of surface-initiated versus endosome-sustained signaling for local effects (e.g., spine remodeling, local translation) remain debated. Some evidence suggests that endocytosis per se is not required for all Trk-dependent outputs, while other studies demonstrate that endosomal Trk signaling generates qualitatively distinct transcriptional programs compared to surface signaling (moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2, moyaalvarado2024plcγca2+pathwayregulates pages 6-7).

### 7.3. Species and Model System Comparisons

Much of our mechanistic understanding derives from rodent models, particularly sympathetic and dorsal root ganglion neurons for TrkA/NGF and hippocampal/cortical neurons for TrkB/BDNF. Recent work in human iPSC-derived neurons has revealed potentially important differences, including distinct ligand selectivity profiles and receptor downregulation kinetics in human TrkB and TrkC that may not fully recapitulate rodent biology (ateaque2023neurotrophinsignallingin pages 4-5). Care is warranted in extrapolating from one system to another.

### 7.4. Truncated Receptor Function

Whether truncated TrkB-T1 functions purely as a dominant-negative regulator and BDNF scavenger, or also transduces meaningful independent signals in glia and neurons, remains under investigation. Evidence for IP3-mediated calcium signaling via TrkB-T1 in astrocytes supports a signaling function (bazzari2022bdnftherapeuticmechanisms pages 2-4), but the in vivo physiological significance relative to TrkB-FL is not fully resolved.

### 7.5. Integration with Other Signaling Systems

Beyond the three canonical branches, Trk receptors also couple to JAK/STAT3, Rho family GTPases, and potentially other signaling systems (siddi2026epigeneticregulationof pages 2-4). The extent to which these represent obligatory versus accessory pathways, and how they intersect with canonical branches, are areas of active investigation.

## 8. Key References

The evidence supporting this review derives from the following primary sources and authoritative reviews:

- **Enkavi (2026)**, FEBS Open Bio 16:252–267 — Comprehensive structural review of Trk receptor signal transduction mechanisms (enkavi2026moleculardeterminantsof pages 5-6, enkavi2026moleculardeterminantsof pages 3-5, enkavi2026moleculardeterminantsof pages 2-3, enkavi2026moleculardeterminantsof pages 8-9)
- **Ateaque, Merkouris & Barde (2023)**, Front. Mol. Neurosci. 16:1225373 — Neurotrophin signaling in human neurons with emphasis on TrkB/TrkC selectivity (ateaque2023neurotrophinsignallingin pages 4-5)
- **Moya-Alvarado et al. (2024)**, Front. Mol. Neurosci. 17:1009404 — PLCγ-Ca²⁺ regulation of TrkB endocytosis and long-distance BDNF signaling (moyaalvarado2024plcγca2+pathwayregulates pages 2-3, moyaalvarado2024plcγca2+pathwayregulates pages 6-7, moyaalvarado2024plcγca2+pathwayregulates pages 1-2, moyaalvarado2024plcγca2+pathwayregulates pages 7-10)
- **Moya-Alvarado et al. (2023)**, eLife 12:e77455 — BDNF/TrkB signaling endosomes coordinating CREB/mTOR activation (moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2, moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3)
- **Wang et al. (2024)**, Biomolecules 14:259 — GRB2 structure, configuration, and function in signal transduction (wang2024theconfigurationof pages 2-4, wang2024theconfigurationof pages 14-15, wang2024theconfigurationof pages 12-14, wang2024theconfigurationof pages 1-2, wang2024theconfigurationof pages 11-12)
- **Harun et al. (2025)**, Biomedicines 13:2931 — BDNF/TrkB signaling pathway mechanisms in Alzheimer's disease (harun2025modulationofbdnftrkb pages 4-6)
- **Forsell et al. (2024)**, Pharmaceuticals 17:997 — Positive allosteric modulators of Trk receptors (forsell2024positiveallostericmodulators pages 4-6, forsell2024positiveallostericmodulators pages 15-17)
- **Bazzari & Bazzari (2022)**, Int. J. Mol. Sci. 23:8417 — BDNF therapeutic mechanisms in neuropsychiatric disorders (bazzari2022bdnftherapeuticmechanisms pages 4-5, bazzari2022bdnftherapeuticmechanisms pages 2-4)
- **Kim et al. (2024)**, Neuropsychopharmacology 49:227–245 — Neurotrophic factors in psychiatric treatments (kim2024theroleof pages 1-2)
- **Yang & Laetsch (2023)**, Expert Opin. Drug Saf. 22:1073–1089 — Safety of TRK inhibitors for NTRK fusion-positive cancers (yang2023safetyofcurrent pages 1-3, yang2023safetyofcurrent pages 10-11, yang2023safetyofcurrent pages 18-22, yang2023safetyofcurrent pages 17-18, yang2023safetyofcurrent pages 13-14)
- **Carrillo-Muñoz et al. (2025)**, Fish Physiol. Biochem. 51 — Neurotrophins and receptors in fish peripheral tissues (carrillomunoz2025neurotrophinsandtheir pages 2-4, carrillomunoz2025neurotrophinsandtheir pages 4-6)
- **Numakawa & Odaka (2022)**, Int. J. Mol. Sci. 23:7726 — Neurotrophin signaling in age-related cognitive decline (numakawa2022theroleof pages 2-4)
- **Siddi et al. (2026)**, Int. J. Mol. Sci. 27:3238 — Epigenetic regulation of Trk receptors in neuroblastoma (siddi2026epigeneticregulationof pages 2-4)
- **Maher et al. (2024)**, Sci. Data 11 — Temporal phosphoproteomics of Trk signaling in neuroblastoma (maher2024atemporal(phospho)proteomic pages 2-3)
- **Bungaro & Garbo (2024)**, Precis. Cancer Med. 6:3 — NTRK biology, detection, and therapy (bungaro2024ntrk123biologydetection pages 1-2)
- **Malagrinò et al. (2024)**, Biochem. Biophys. Rep. 39:101803 — GRB2 as a dynamic adaptor protein (malagrino2024grb2adynamic pages 2-3)

References

1. (enkavi2026moleculardeterminantsof pages 5-6): Giray Enkavi. Molecular determinants of signal transduction in tropomyosin receptor kinases. FEBS Open Bio, 16:252-267, Oct 2026. URL: https://doi.org/10.1002/2211-5463.70135, doi:10.1002/2211-5463.70135. This article has 1 citations and is from a peer-reviewed journal.

2. (enkavi2026moleculardeterminantsof pages 3-5): Giray Enkavi. Molecular determinants of signal transduction in tropomyosin receptor kinases. FEBS Open Bio, 16:252-267, Oct 2026. URL: https://doi.org/10.1002/2211-5463.70135, doi:10.1002/2211-5463.70135. This article has 1 citations and is from a peer-reviewed journal.

3. (carrillomunoz2025neurotrophinsandtheir pages 2-4): Aldo Isaac Carrillo-Muñoz, Sharet Y. R-Jaimes, Guadalupe C. Hernández-Hernández, and Francisco Castelán. Neurotrophins and their receptors in the peripheral nervous system and non-nervous tissue of fish. Fish Physiology and Biochemistry, Jan 2025. URL: https://doi.org/10.1007/s10695-025-01453-7, doi:10.1007/s10695-025-01453-7. This article has 0 citations and is from a peer-reviewed journal.

4. (carrillomunoz2025neurotrophinsandtheir pages 4-6): Aldo Isaac Carrillo-Muñoz, Sharet Y. R-Jaimes, Guadalupe C. Hernández-Hernández, and Francisco Castelán. Neurotrophins and their receptors in the peripheral nervous system and non-nervous tissue of fish. Fish Physiology and Biochemistry, Jan 2025. URL: https://doi.org/10.1007/s10695-025-01453-7, doi:10.1007/s10695-025-01453-7. This article has 0 citations and is from a peer-reviewed journal.

5. (yang2023safetyofcurrent pages 1-3): Adeline T. Yang and Theodore Willis Laetsch. Safety of current treatment options for ntrk fusion-positive cancers. Expert Opinion on Drug Safety, 22:1073-1089, Oct 2023. URL: https://doi.org/10.1080/14740338.2023.2274426, doi:10.1080/14740338.2023.2274426. This article has 12 citations and is from a peer-reviewed journal.

6. (yang2023safetyofcurrent pages 18-22): Adeline T. Yang and Theodore Willis Laetsch. Safety of current treatment options for ntrk fusion-positive cancers. Expert Opinion on Drug Safety, 22:1073-1089, Oct 2023. URL: https://doi.org/10.1080/14740338.2023.2274426, doi:10.1080/14740338.2023.2274426. This article has 12 citations and is from a peer-reviewed journal.

7. (moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2): Guillermo Moya-Alvarado, Reynaldo Tiburcio-Felix, María Raquel Ibáñez, Alejandro A Aguirre-Soto, Miguel V Guerra, Chengbiao Wu, William C Mobley, Eran Perlson, and Francisca C Bronfman. Bdnf/trkb signaling endosomes in axons coordinate creb/mtor activation and protein synthesis in the cell body to induce dendritic growth in cortical neurons. Feb 2023. URL: https://doi.org/10.7554/elife.77455, doi:10.7554/elife.77455. This article has 98 citations and is from a domain leading peer-reviewed journal.

8. (enkavi2026moleculardeterminantsof pages 2-3): Giray Enkavi. Molecular determinants of signal transduction in tropomyosin receptor kinases. FEBS Open Bio, 16:252-267, Oct 2026. URL: https://doi.org/10.1002/2211-5463.70135, doi:10.1002/2211-5463.70135. This article has 1 citations and is from a peer-reviewed journal.

9. (numakawa2022theroleof pages 2-4): Tadahiro Numakawa and Haruki Odaka. The role of neurotrophin signaling in age-related cognitive decline and cognitive diseases. Jul 2022. URL: https://doi.org/10.3390/ijms23147726, doi:10.3390/ijms23147726. This article has 83 citations.

10. (bungaro2024ntrk123biologydetection pages 1-2): Maristella Bungaro and Edoardo Garbo. Ntrk1/2/3: biology, detection and therapy. Precision Cancer Medicine, 6:3-3, Sep 2024. URL: https://doi.org/10.21037/pcm-23-19, doi:10.21037/pcm-23-19. This article has 11 citations.

11. (harun2025modulationofbdnftrkb pages 4-6): Zairin Zulaikha Harun, Auji Abdul Azhar, Yun-Jin Kim, Farah Wahida Ibrahim, Min-Hwei Ng, Jen-Kit Tan, and Yogeswaran Lokanathan. Modulation of bdnf/trkb signalling pathway in alzheimer’s disease: mechanistic insights and the role of stem cell therapy. Biomedicines, 13(12):2931, Nov 2025. URL: https://doi.org/10.3390/biomedicines13122931, doi:10.3390/biomedicines13122931. This article has 4 citations.

12. (forsell2024positiveallostericmodulators pages 4-6): Pontus Forsell, Cristina Parrado Fernández, Boel Nilsson, Johan Sandin, Gunnar Nordvall, and Märta Segerdahl. Positive allosteric modulators of trk receptors for the treatment of alzheimer’s disease. Pharmaceuticals, 17:997, Jul 2024. URL: https://doi.org/10.3390/ph17080997, doi:10.3390/ph17080997. This article has 10 citations.

13. (wang2024theconfigurationof pages 2-4): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

14. (wang2024theconfigurationof pages 1-2): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

15. (wang2024theconfigurationof pages 12-14): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

16. (bazzari2022bdnftherapeuticmechanisms pages 4-5): Amjad H. Bazzari and Firas H. Bazzari. Bdnf therapeutic mechanisms in neuropsychiatric disorders. International Journal of Molecular Sciences, 23:8417, Jul 2022. URL: https://doi.org/10.3390/ijms23158417, doi:10.3390/ijms23158417. This article has 105 citations.

17. (yang2023safetyofcurrent pages 17-18): Adeline T. Yang and Theodore Willis Laetsch. Safety of current treatment options for ntrk fusion-positive cancers. Expert Opinion on Drug Safety, 22:1073-1089, Oct 2023. URL: https://doi.org/10.1080/14740338.2023.2274426, doi:10.1080/14740338.2023.2274426. This article has 12 citations and is from a peer-reviewed journal.

18. (kim2024theroleof pages 1-2): Jihye Kim, Michelle J. He, Alina K. Widmann, and Francis S. Lee. The role of neurotrophic factors in novel, rapid psychiatric treatments. Neuropsychopharmacology, 49:227-245, Sep 2024. URL: https://doi.org/10.1038/s41386-023-01717-x, doi:10.1038/s41386-023-01717-x. This article has 52 citations and is from a highest quality peer-reviewed journal.

19. (moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3): Guillermo Moya-Alvarado, Reynaldo Tiburcio-Felix, María Raquel Ibáñez, Alejandro A Aguirre-Soto, Miguel V Guerra, Chengbiao Wu, William C Mobley, Eran Perlson, and Francisca C Bronfman. Bdnf/trkb signaling endosomes in axons coordinate creb/mtor activation and protein synthesis in the cell body to induce dendritic growth in cortical neurons. Feb 2023. URL: https://doi.org/10.7554/elife.77455, doi:10.7554/elife.77455. This article has 98 citations and is from a domain leading peer-reviewed journal.

20. (forsell2024positiveallostericmodulators pages 15-17): Pontus Forsell, Cristina Parrado Fernández, Boel Nilsson, Johan Sandin, Gunnar Nordvall, and Märta Segerdahl. Positive allosteric modulators of trk receptors for the treatment of alzheimer’s disease. Pharmaceuticals, 17:997, Jul 2024. URL: https://doi.org/10.3390/ph17080997, doi:10.3390/ph17080997. This article has 10 citations.

21. (moyaalvarado2024plcγca2+pathwayregulates pages 7-10): Guillermo Moya-Alvarado, Xavier Valero-Peña, Alejandro Aguirre-Soto, Fernando J. Bustos, Oscar M. Lazo, and Francisca C. Bronfman. Plc-γ-ca2+ pathway regulates axonal trkb endocytosis and is required for long-distance propagation of bdnf signaling. Frontiers in Molecular Neuroscience, Apr 2024. URL: https://doi.org/10.3389/fnmol.2024.1009404, doi:10.3389/fnmol.2024.1009404. This article has 17 citations.

22. (moyaalvarado2024plcγca2+pathwayregulates pages 2-3): Guillermo Moya-Alvarado, Xavier Valero-Peña, Alejandro Aguirre-Soto, Fernando J. Bustos, Oscar M. Lazo, and Francisca C. Bronfman. Plc-γ-ca2+ pathway regulates axonal trkb endocytosis and is required for long-distance propagation of bdnf signaling. Frontiers in Molecular Neuroscience, Apr 2024. URL: https://doi.org/10.3389/fnmol.2024.1009404, doi:10.3389/fnmol.2024.1009404. This article has 17 citations.

23. (moyaalvarado2024plcγca2+pathwayregulates pages 6-7): Guillermo Moya-Alvarado, Xavier Valero-Peña, Alejandro Aguirre-Soto, Fernando J. Bustos, Oscar M. Lazo, and Francisca C. Bronfman. Plc-γ-ca2+ pathway regulates axonal trkb endocytosis and is required for long-distance propagation of bdnf signaling. Frontiers in Molecular Neuroscience, Apr 2024. URL: https://doi.org/10.3389/fnmol.2024.1009404, doi:10.3389/fnmol.2024.1009404. This article has 17 citations.

24. (moyaalvarado2024plcγca2+pathwayregulates pages 1-2): Guillermo Moya-Alvarado, Xavier Valero-Peña, Alejandro Aguirre-Soto, Fernando J. Bustos, Oscar M. Lazo, and Francisca C. Bronfman. Plc-γ-ca2+ pathway regulates axonal trkb endocytosis and is required for long-distance propagation of bdnf signaling. Frontiers in Molecular Neuroscience, Apr 2024. URL: https://doi.org/10.3389/fnmol.2024.1009404, doi:10.3389/fnmol.2024.1009404. This article has 17 citations.

25. (moyaalvarado2024plcγca2+pathwayregulates pages 15-16): Guillermo Moya-Alvarado, Xavier Valero-Peña, Alejandro Aguirre-Soto, Fernando J. Bustos, Oscar M. Lazo, and Francisca C. Bronfman. Plc-γ-ca2+ pathway regulates axonal trkb endocytosis and is required for long-distance propagation of bdnf signaling. Frontiers in Molecular Neuroscience, Apr 2024. URL: https://doi.org/10.3389/fnmol.2024.1009404, doi:10.3389/fnmol.2024.1009404. This article has 17 citations.

26. (enkavi2026moleculardeterminantsof pages 8-9): Giray Enkavi. Molecular determinants of signal transduction in tropomyosin receptor kinases. FEBS Open Bio, 16:252-267, Oct 2026. URL: https://doi.org/10.1002/2211-5463.70135, doi:10.1002/2211-5463.70135. This article has 1 citations and is from a peer-reviewed journal.

27. (maher2024atemporal(phospho)proteomic pages 2-3): Stephanie Maher, Kieran Wynne, Vadim Zhernovkov, and Melinda Halasz. A temporal (phospho-)proteomic dataset of neurotrophic receptor tyrosine kinase signalling in neuroblastoma. Scientific Data, Oct 2024. URL: https://doi.org/10.1038/s41597-024-03965-y, doi:10.1038/s41597-024-03965-y. This article has 5 citations and is from a peer-reviewed journal.

28. (ateaque2023neurotrophinsignallingin pages 4-5): Sarah Ateaque, Spyros Merkouris, and Yves-Alain Barde. Neurotrophin signalling in the human nervous system. Frontiers in Molecular Neuroscience, Jul 2023. URL: https://doi.org/10.3389/fnmol.2023.1225373, doi:10.3389/fnmol.2023.1225373. This article has 47 citations.

29. (siddi2026epigeneticregulationof pages 2-4): Carlotta Siddi, Jihane Balla, Paola Fadda, and Simona Dedoni. Epigenetic regulation of trk receptors and neurotrophic signalling in neuroblastoma: mechanisms, plasticity, and therapeutic opportunities. International Journal of Molecular Sciences, 27:3238, Apr 2026. URL: https://doi.org/10.3390/ijms27073238, doi:10.3390/ijms27073238. This article has 1 citations.

30. (bazzari2022bdnftherapeuticmechanisms pages 2-4): Amjad H. Bazzari and Firas H. Bazzari. Bdnf therapeutic mechanisms in neuropsychiatric disorders. International Journal of Molecular Sciences, 23:8417, Jul 2022. URL: https://doi.org/10.3390/ijms23158417, doi:10.3390/ijms23158417. This article has 105 citations.

31. (wang2024theconfigurationof pages 14-15): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

32. (wang2024theconfigurationof pages 11-12): Dingyi Wang, Guoxia Liu, Yuxin Meng, Hongjie Chen, Zu Ye, and Ji Jing. The configuration of grb2 in protein interaction and signal transduction. Biomolecules, 14:259, Feb 2024. URL: https://doi.org/10.3390/biom14030259, doi:10.3390/biom14030259. This article has 55 citations.

33. (yang2023safetyofcurrent pages 10-11): Adeline T. Yang and Theodore Willis Laetsch. Safety of current treatment options for ntrk fusion-positive cancers. Expert Opinion on Drug Safety, 22:1073-1089, Oct 2023. URL: https://doi.org/10.1080/14740338.2023.2274426, doi:10.1080/14740338.2023.2274426. This article has 12 citations and is from a peer-reviewed journal.

34. (yang2023safetyofcurrent pages 13-14): Adeline T. Yang and Theodore Willis Laetsch. Safety of current treatment options for ntrk fusion-positive cancers. Expert Opinion on Drug Safety, 22:1073-1089, Oct 2023. URL: https://doi.org/10.1080/14740338.2023.2274426, doi:10.1080/14740338.2023.2274426. This article has 12 citations and is from a peer-reviewed journal.

35. (malagrino2024grb2adynamic pages 2-3): Francesca Malagrinò, Elena Puglisi, Livia Pagano, Carlo Travaglini-Allocatelli, and Angelo Toto. Grb2: a dynamic adaptor protein orchestrating cellular signaling in health and disease. Sep 2024. URL: https://doi.org/10.1016/j.bbrep.2024.101803, doi:10.1016/j.bbrep.2024.101803. This article has 23 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](neurotrophin_trk_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](neurotrophin_trk_signaling-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. enkavi2026moleculardeterminantsof pages 2-3
2. enkavi2026moleculardeterminantsof pages 5-6
3. wang2024theconfigurationof pages 12-14
4. moyaalvarado2023bdnftrkbsignalingendosomes pages 2-3
5. carrillomunoz2025neurotrophinsandtheir pages 4-6
6. forsell2024positiveallostericmodulators pages 15-17
7. numakawa2022theroleof pages 2-4
8. bazzari2022bdnftherapeuticmechanisms pages 2-4
9. ateaque2023neurotrophinsignallingin pages 4-5
10. carrillomunoz2025neurotrophinsandtheir pages 2-4
11. siddi2026epigeneticregulationof pages 2-4
12. enkavi2026moleculardeterminantsof pages 3-5
13. wang2024theconfigurationof pages 2-4
14. wang2024theconfigurationof pages 14-15
15. enkavi2026moleculardeterminantsof pages 8-9
16. harun2025modulationofbdnftrkb pages 4-6
17. kim2024theroleof pages 1-2
18. yang2023safetyofcurrent pages 1-3
19. yang2023safetyofcurrent pages 18-22
20. moyaalvarado2023bdnftrkbsignalingendosomes pages 1-2
21. forsell2024positiveallostericmodulators pages 4-6
22. wang2024theconfigurationof pages 1-2
23. bazzari2022bdnftherapeuticmechanisms pages 4-5
24. yang2023safetyofcurrent pages 17-18
25. wang2024theconfigurationof pages 11-12
26. yang2023safetyofcurrent pages 10-11
27. yang2023safetyofcurrent pages 13-14
28. https://doi.org/10.1002/2211-5463.70135,
29. https://doi.org/10.1007/s10695-025-01453-7,
30. https://doi.org/10.1080/14740338.2023.2274426,
31. https://doi.org/10.7554/elife.77455,
32. https://doi.org/10.3390/ijms23147726,
33. https://doi.org/10.21037/pcm-23-19,
34. https://doi.org/10.3390/biomedicines13122931,
35. https://doi.org/10.3390/ph17080997,
36. https://doi.org/10.3390/biom14030259,
37. https://doi.org/10.3390/ijms23158417,
38. https://doi.org/10.1038/s41386-023-01717-x,
39. https://doi.org/10.3389/fnmol.2024.1009404,
40. https://doi.org/10.1038/s41597-024-03965-y,
41. https://doi.org/10.3389/fnmol.2023.1225373,
42. https://doi.org/10.3390/ijms27073238,
43. https://doi.org/10.1016/j.bbrep.2024.101803,