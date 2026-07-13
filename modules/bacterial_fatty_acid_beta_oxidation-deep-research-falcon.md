---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T22:31:12.173000'
end_time: '2026-07-06T23:01:49.472579'
duration_seconds: 1837.3
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial fatty acid beta-oxidation and acyl-CoA activation
  module_summary: A bacterial fatty-acid degradation boundary module covering activation
    of free fatty acids to acyl-CoA thioesters, the FAD-dependent acyl-CoA dehydrogenase
    step, hydration and oxidation of enoyl/hydroxyacyl-CoA intermediates, and thiolytic
    cleavage to acetyl-CoA plus a shortened acyl-CoA. For Pseudomonas putida KT2440,
    KEGG ppu00071 also includes alkane/rubredoxin electron-transfer nodes and specialized
    CoA-thioester dehydrogenase paralogs; those should be treated as boundary context
    until module-level evidence resolves their role in fatty-acid degradation.
  module_outline: "- Bacterial fatty acid beta-oxidation and acyl-CoA activation\n\
    \  - 1. fatty-acid activation to acyl-CoA\n  - Fatty acid to fatty acyl-CoA\n\
    \    - Long-chain fatty acid-CoA ligase (molecular player: long-chain fatty acid-CoA\
    \ ligase activity; activity or role: long-chain fatty acid-CoA ligase activity)\n\
    \  - 2. FAD-dependent acyl-CoA dehydrogenation\n  - Fatty acyl-CoA to trans-2-enoyl-CoA\n\
    \    - Long-chain fatty acyl-CoA dehydrogenase (molecular player: long-chain fatty\
    \ acyl-CoA dehydrogenase activity; activity or role: long-chain fatty acyl-CoA\
    \ dehydrogenase activity)\n    - Medium-chain fatty acyl-CoA dehydrogenase (molecular\
    \ player: medium-chain fatty acyl-CoA dehydrogenase activity; activity or role:\
    \ medium-chain fatty acyl-CoA dehydrogenase activity)\n    - Acyl-CoA dehydrogenase-family\
    \ activity (molecular player: acyl-CoA dehydrogenase activity; activity or role:\
    \ acyl-CoA dehydrogenase activity)\n  - 3. enoyl-CoA hydration\n  - trans-2-enoyl-CoA\
    \ to 3-hydroxyacyl-CoA\n    - Enoyl-CoA hydratase (molecular player: enoyl-CoA\
    \ hydratase activity; activity or role: enoyl-CoA hydratase activity)\n  - 4.\
    \ 3-hydroxyacyl-CoA oxidation\n  - 3-hydroxyacyl-CoA to 3-ketoacyl-CoA\n    -\
    \ 3-hydroxyacyl-CoA dehydrogenase (molecular player: (3S)-3-hydroxyacyl-CoA dehydrogenase\
    \ (NAD+) activity; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+)\
    \ activity)\n    - Long-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player:\
    \ long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or\
    \ role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)\n  -\
    \ 5. thiolytic cleavage to acetyl-CoA\n  - 3-ketoacyl-CoA to acetyl-CoA plus shortened\
    \ acyl-CoA\n    - Acetyl-CoA C-acyltransferase / beta-ketothiolase (molecular\
    \ player: acetyl-CoA C-acyltransferase activity; activity or role: acetyl-CoA\
    \ C-acyltransferase activity)\n  - 6. boundary alkane/rubredoxin electron transfer\n\
    \  - Alkane oxidation electron-transfer side nodes\n    - Rubredoxin-NAD+ reductase\
    \ (molecular player: rubredoxin-NAD+ reductase activity; activity or role: rubredoxin-NAD+\
    \ reductase activity)"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 57
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: bacterial_fatty_acid_beta_oxidation-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: bacterial_fatty_acid_beta_oxidation-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial fatty acid beta-oxidation and acyl-CoA activation

## Working Scope

A bacterial fatty-acid degradation boundary module covering activation of free fatty acids to acyl-CoA thioesters, the FAD-dependent acyl-CoA dehydrogenase step, hydration and oxidation of enoyl/hydroxyacyl-CoA intermediates, and thiolytic cleavage to acetyl-CoA plus a shortened acyl-CoA. For Pseudomonas putida KT2440, KEGG ppu00071 also includes alkane/rubredoxin electron-transfer nodes and specialized CoA-thioester dehydrogenase paralogs; those should be treated as boundary context until module-level evidence resolves their role in fatty-acid degradation.

## Provisional Biological Outline

- Bacterial fatty acid beta-oxidation and acyl-CoA activation
  - 1. fatty-acid activation to acyl-CoA
  - Fatty acid to fatty acyl-CoA
    - Long-chain fatty acid-CoA ligase (molecular player: long-chain fatty acid-CoA ligase activity; activity or role: long-chain fatty acid-CoA ligase activity)
  - 2. FAD-dependent acyl-CoA dehydrogenation
  - Fatty acyl-CoA to trans-2-enoyl-CoA
    - Long-chain fatty acyl-CoA dehydrogenase (molecular player: long-chain fatty acyl-CoA dehydrogenase activity; activity or role: long-chain fatty acyl-CoA dehydrogenase activity)
    - Medium-chain fatty acyl-CoA dehydrogenase (molecular player: medium-chain fatty acyl-CoA dehydrogenase activity; activity or role: medium-chain fatty acyl-CoA dehydrogenase activity)
    - Acyl-CoA dehydrogenase-family activity (molecular player: acyl-CoA dehydrogenase activity; activity or role: acyl-CoA dehydrogenase activity)
  - 3. enoyl-CoA hydration
  - trans-2-enoyl-CoA to 3-hydroxyacyl-CoA
    - Enoyl-CoA hydratase (molecular player: enoyl-CoA hydratase activity; activity or role: enoyl-CoA hydratase activity)
  - 4. 3-hydroxyacyl-CoA oxidation
  - 3-hydroxyacyl-CoA to 3-ketoacyl-CoA
    - 3-hydroxyacyl-CoA dehydrogenase (molecular player: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
    - Long-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
  - 5. thiolytic cleavage to acetyl-CoA
  - 3-ketoacyl-CoA to acetyl-CoA plus shortened acyl-CoA
    - Acetyl-CoA C-acyltransferase / beta-ketothiolase (molecular player: acetyl-CoA C-acyltransferase activity; activity or role: acetyl-CoA C-acyltransferase activity)
  - 6. boundary alkane/rubredoxin electron transfer
  - Alkane oxidation electron-transfer side nodes
    - Rubredoxin-NAD+ reductase (molecular player: rubredoxin-NAD+ reductase activity; activity or role: rubredoxin-NAD+ reductase activity)

## Known Relationships Among Steps

No explicit connections.

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

Bacterial fatty acid beta-oxidation and acyl-CoA activation

## Working Scope

A bacterial fatty-acid degradation boundary module covering activation of free fatty acids to acyl-CoA thioesters, the FAD-dependent acyl-CoA dehydrogenase step, hydration and oxidation of enoyl/hydroxyacyl-CoA intermediates, and thiolytic cleavage to acetyl-CoA plus a shortened acyl-CoA. For Pseudomonas putida KT2440, KEGG ppu00071 also includes alkane/rubredoxin electron-transfer nodes and specialized CoA-thioester dehydrogenase paralogs; those should be treated as boundary context until module-level evidence resolves their role in fatty-acid degradation.

## Provisional Biological Outline

- Bacterial fatty acid beta-oxidation and acyl-CoA activation
  - 1. fatty-acid activation to acyl-CoA
  - Fatty acid to fatty acyl-CoA
    - Long-chain fatty acid-CoA ligase (molecular player: long-chain fatty acid-CoA ligase activity; activity or role: long-chain fatty acid-CoA ligase activity)
  - 2. FAD-dependent acyl-CoA dehydrogenation
  - Fatty acyl-CoA to trans-2-enoyl-CoA
    - Long-chain fatty acyl-CoA dehydrogenase (molecular player: long-chain fatty acyl-CoA dehydrogenase activity; activity or role: long-chain fatty acyl-CoA dehydrogenase activity)
    - Medium-chain fatty acyl-CoA dehydrogenase (molecular player: medium-chain fatty acyl-CoA dehydrogenase activity; activity or role: medium-chain fatty acyl-CoA dehydrogenase activity)
    - Acyl-CoA dehydrogenase-family activity (molecular player: acyl-CoA dehydrogenase activity; activity or role: acyl-CoA dehydrogenase activity)
  - 3. enoyl-CoA hydration
  - trans-2-enoyl-CoA to 3-hydroxyacyl-CoA
    - Enoyl-CoA hydratase (molecular player: enoyl-CoA hydratase activity; activity or role: enoyl-CoA hydratase activity)
  - 4. 3-hydroxyacyl-CoA oxidation
  - 3-hydroxyacyl-CoA to 3-ketoacyl-CoA
    - 3-hydroxyacyl-CoA dehydrogenase (molecular player: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
    - Long-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
  - 5. thiolytic cleavage to acetyl-CoA
  - 3-ketoacyl-CoA to acetyl-CoA plus shortened acyl-CoA
    - Acetyl-CoA C-acyltransferase / beta-ketothiolase (molecular player: acetyl-CoA C-acyltransferase activity; activity or role: acetyl-CoA C-acyltransferase activity)
  - 6. boundary alkane/rubredoxin electron transfer
  - Alkane oxidation electron-transfer side nodes
    - Rubredoxin-NAD+ reductase (molecular player: rubredoxin-NAD+ reductase activity; activity or role: rubredoxin-NAD+ reductase activity)

## Known Relationships Among Steps

No explicit connections.

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

# Bacterial Fatty Acid β-Oxidation and Acyl-CoA Activation: A Review-Style Synthesis

## 1. Executive Summary

Bacterial fatty acid β-oxidation is a conserved, iterative catabolic pathway that degrades fatty acyl-CoA thioesters by successive removal of two-carbon (acetyl-CoA) units. The system comprises an obligatory activation step (fatty acid → acyl-CoA, catalyzed by FadD), followed by a four-reaction spiral: FAD-dependent dehydrogenation (FadE), enoyl-CoA hydration, 3-hydroxyacyl-CoA oxidation (NAD⁺-dependent), and thiolytic cleavage (FadA). In *Escherichia coli*, the hydratase, dehydrogenase, and accessory isomerase/epimerase activities are consolidated within the multifunctional FadB subunit of the FadBA heterotetrameric complex (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5). The pathway is transcriptionally governed by the dual-function regulator FadR, which represses *fad* genes in the absence of long-chain acyl-CoA effectors and simultaneously activates fatty acid biosynthesis genes (pavoncello2022degradationofexogenous pages 15-17, cronan2021theescherichiacoli pages 13-18, cronan2021theescherichiacoli pages 1-4). Across bacterial lineages, the core enzymatic logic is highly conserved, but gene organization, paralog number, substrate specificity, and regulatory architecture vary dramatically—from the single polycistronic *fadXDEBA* operon of *Staphylococcus aureus* (menjivar2025characterizingthestaphylococcus pages 2-5) to the massively redundant β-oxidation gene repertoire of *Cupriavidus necator* H16 (strittmatter2022insightsintothe pages 1-2, strittmatter2023mediumchainlengthfattyacid pages 13-15). In *Pseudomonas putida* KT2440, the KEGG pathway ppu00071 additionally includes alkane monooxygenase (AlkB) and rubredoxin/rubredoxin reductase electron-transfer nodes; these are mechanistically upstream of and distinct from the β-oxidation spiral itself, serving to convert alkanes into fatty acid substrates that then enter β-oxidation (williams2022anoverviewof pages 1-2, groves2023structureandfunction pages 1-3).

## 2. Definition and Biological Boundaries

### 2.1 What is included

The β-oxidation module, as defined here, encompasses: (i) activation of free fatty acids to acyl-CoA thioesters by long-chain acyl-CoA synthetase (FadD); (ii) the four-step degradative spiral (dehydrogenation → hydration → oxidation → thiolysis); and (iii) auxiliary enzymes required for processing unsaturated fatty acids (FadH 2,4-dienoyl-CoA reductase; FadB isomerase/epimerase activities) (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 7-9). In *E. coli*, the core genes are *fadD*, *fadE*, *fadB*, *fadA*, with secondary/backup functions provided by *fadI*, *fadJ*, and the *ato* system for short-chain fatty acids (pavoncello2022degradationofexogenous pages 11-13, pavoncello2022degradationofexogenous pages 13-15).

### 2.2 What should be treated separately

Several neighboring processes are frequently conflated with β-oxidation but should be treated as boundary context:

- **Fatty acid transport (FadL)**: The outer membrane β-barrel transporter FadL mediates import of long-chain fatty acids (>C12) across the outer membrane of Gram-negative bacteria via a ligand-gated lateral-diffusion mechanism (waters2024bacterialacquisitionof pages 7-9, pavoncello2022degradationofexogenous pages 2-5). While FadL function is coupled to FadD-mediated activation (approximately 98% of imported fatty acids are immediately thioesterified), transport per se is not a catalytic step of the β-oxidation spiral (pavoncello2022degradationofexogenous pages 2-5, pavoncello2022degradationofexogenous pages 5-7).

- **Alkane oxidation (AlkB/AlkG/AlkT)**: In *Pseudomonas putida* GPo1 and related strains, the AlkB alkane monooxygenase system hydroxylates medium-chain alkanes to alcohols, which are subsequently oxidized to fatty acids and then activated for β-oxidation. The electron-transfer chain (NADH → AlkT rubredoxin reductase → AlkG rubredoxin → AlkB diiron active site) is mechanistically and genetically distinct from the β-oxidation cycle (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, groves2023structureandfunction pages 1-3). Its inclusion in KEGG ppu00071 reflects substrate-feeding relationships rather than shared catalytic mechanism.

- **Fatty acid biosynthesis (fab genes)**: Although FadR coordinately regulates both *fad* and *fab* gene sets, the biosynthetic pathway operates through type II fatty acid synthase (FAS II) and uses distinct chemistry (malonyl-CoA condensation, ACP-linked intermediates) (cronan2021theescherichiacoli pages 13-18, pavoncello2022degradationofexogenous pages 17-19).

- **Polyhydroxyalkanoate (PHA) biosynthesis**: In *P. putida* KT2440, β-oxidation intermediates—particularly trans-2-enoyl-CoA—are diverted by (R)-specific enoyl-CoA hydratases (PhaJ1, PhaJ4, MaoC) toward PHA monomer synthesis. This is a metabolic branch point, not part of β-oxidation itself (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3).

## 3. Mechanistic Overview

### 3.1 Step 1: Fatty acid activation to acyl-CoA

Free fatty acids are activated by the inner membrane-associated acyl-CoA synthetase FadD through a two-step ATP-dependent reaction. The fatty acid first reacts with ATP to form a fatty acyl-AMP intermediate, which is then thioesterified with coenzyme A to produce fatty acyl-CoA (pavoncello2022degradationofexogenous pages 2-5). This activation is obligatory: it traps the substrate metabolically, prevents efflux, and generates the thioester bond that drives subsequent chemistry. In *E. coli*, FadD processes a broader substrate spectrum than FadL admits, allowing it to activate both exogenous (imported) and endogenous fatty acids (pavoncello2022degradationofexogenous pages 2-5, pavoncello2022degradationofexogenous pages 5-7). This step consumes the equivalent of two high-energy phosphate bonds (ATP → AMP + PPi).

### 3.2 Step 2: FAD-dependent acyl-CoA dehydrogenation

The acyl-CoA dehydrogenase FadE catalyzes the α,β-dehydrogenation of fatty acyl-CoA to trans-2-enoyl-CoA, using FAD as a prosthetic group (pavoncello2022degradationofexogenous pages 5-7, wang2025pseudomonasaeruginosaacylcoa pages 1-2). *E. coli* FadE is an 89 kDa (814-residue) protein, notably larger than mammalian acyl-CoA dehydrogenases, with additional N-terminal and C-terminal domains whose precise functions remain under investigation (pavoncello2022degradationofexogenous pages 11-13). A critical open question is the identity of the physiological electron acceptor for the reduced FADH₂ in bacterial FadE. Unlike mitochondrial acyl-CoA dehydrogenases that transfer electrons via electron-transfer flavoprotein (ETF) to ETF:ubiquinone oxidoreductase, *E. coli* FadE has no confirmed ETF partner, and the natural redox partner has not been definitively identified (sirithanakorn2024evidenceforendogenous pages 11-12, sirithanakorn2024evidenceforendogenous pages 1-2). Structurally, *E. coli* FadE resembles peroxisomal acyl-CoA oxidase 1 (ACOX-1), which directly transfers electrons to O₂ to produce H₂O₂ (sirithanakorn2024evidenceforendogenous pages 11-12). Recent work by Sirithanakorn and Imlay (2024) demonstrated that FadE-driven β-oxidation amplifies intracellular H₂O₂ formation in *E. coli*, suggesting that side reactions with O₂ are physiologically significant during high metabolic flux (sirithanakorn2024evidenceforendogenous pages 6-8, sirithanakorn2024evidenceforendogenous pages 1-2, sirithanakorn2024evidenceforendogenous pages 2-4).

### 3.3 Step 3: Enoyl-CoA hydration

The trans-2-enoyl-CoA produced by FadE is hydrated to (S)-3-hydroxyacyl-CoA by the enoyl-CoA hydratase activity of FadB. In *E. coli*, FadB is part of the FadBA heterotetrameric trifunctional enzyme (TFE) complex comprising two FadB (78 kDa) and two FadA (42 kDa) subunits (pavoncello2022degradationofexogenous pages 5-7). The hydratase activity is stereospecific, producing the (S)-3-hydroxy isomer required for the subsequent NAD⁺-dependent oxidation.

### 3.4 Step 4: 3-Hydroxyacyl-CoA oxidation

The (S)-3-hydroxyacyl-CoA is oxidized to 3-ketoacyl-CoA by the NAD⁺-dependent 3-hydroxyacyl-CoA dehydrogenase activity, also residing within FadB (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5). This step generates NADH, which feeds into the electron transport chain for oxidative phosphorylation.

### 3.5 Step 5: Thiolytic cleavage

FadA (3-ketoacyl-CoA thiolase) catalyzes CoA-dependent thiolytic cleavage of 3-ketoacyl-CoA, releasing one molecule of acetyl-CoA and a fatty acyl-CoA shortened by two carbons (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5). The shortened acyl-CoA re-enters the cycle at Step 2. Acetyl-CoA is channeled to the TCA cycle (or glyoxylate shunt, when fatty acids are the sole carbon source) for complete oxidation and biosynthetic precursor generation.

### 3.6 Auxiliary enzymes for unsaturated fatty acids

Degradation of unsaturated fatty acids requires additional enzymatic activities beyond the core four-step spiral:

- For **odd-positioned double bonds** (e.g., oleic acid, C18:1Δ9): FadB provides cis-Δ3-trans-Δ2-enoyl-CoA isomerase activity, repositioning and reconfiguring the double bond so the intermediate can re-enter at the hydratase step. FadB also provides 3-hydroxyacyl-CoA epimerase activity for stereochemical correction (pavoncello2022degradationofexogenous pages 7-9, pavoncello2022degradationofexogenous pages 5-7).

- For **even-positioned double bonds**: β-oxidation cycles generate 2-trans,4-cis-dienoyl-CoA intermediates that cannot be processed by FadB alone. FadH (2,4-dienoyl-CoA reductase), an NADPH-dependent iron-sulfur flavoprotein, reduces this intermediate to 3-trans-enoyl-CoA, which is then isomerized by FadB to re-enter the standard cycle (pavoncello2022degradationofexogenous pages 7-9, pavoncello2022degradationofexogenous pages 22-23).

The following table summarizes the complete enzymatic repertoire of the pathway:

| Step Number | Reaction Name | E. coli Gene(s) | Enzyme Name | EC Number (where known) | Cofactors | Reaction Description | Notes on Variation |
|---|---|---|---|---|---|---|---|
| 1 | Fatty acid activation to acyl-CoA | **fadD** | Long-chain fatty acyl-CoA synthetase / acyl-CoA ligase | **EC 6.2.1.3** | ATP, CoA, Mg²⁺ | Activates free fatty acids by ATP-dependent thioesterification to fatty acyl-CoA, coupling uptake and metabolic trapping before β-oxidation. In Gram-negative bacteria this step is functionally coupled to FadL-mediated uptake. (pavoncello2022degradationofexogenous pages 2-5, waters2024bacterialacquisitionof pages 7-9, pavoncello2022degradationofexogenous pages 5-7) | In *E. coli*, FadD handles a broader substrate spectrum than FadL uptake alone. Many bacteria encode multiple FadD homologs with chain-length or pathway specialization; in *S. aureus* annotation of fadD/fadE homologs is swapped relative to *E. coli* conventions. (waters2024bacterialacquisitionof pages 7-9, menjivar2025characterizingthestaphylococcus pages 2-5) |
| 2 | FAD-dependent acyl-CoA dehydrogenation | **fadE** | Acyl-CoA dehydrogenase (fatty acyl-CoA dehydrogenase) | **EC 1.3.8.-** | FAD | Oxidizes fatty acyl-CoA to trans-2-enoyl-CoA, introducing the 2,3-double bond that commits substrate to the β-oxidation spiral. Reduced flavin is reoxidized by transfer of electrons to the respiratory chain, though the precise natural partner in *E. coli* remains unresolved. (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5, sirithanakorn2024evidenceforendogenous pages 6-8, sirithanakorn2024evidenceforendogenous pages 11-12, sirithanakorn2024evidenceforendogenous pages 2-4) | Chain-length specificity varies strongly across bacteria. *P. aeruginosa* has FadE1 preferring long-chain acyl-CoAs and FadE2 restricted to medium-chain substrates, with specificity set by the substrate-pocket architecture. *E. coli* FadE can also generate ROS/H₂O₂ as a side reaction during high flux. (wang2025pseudomonasaeruginosaacylcoa pages 3-5, wang2025pseudomonasaeruginosaacylcoa pages 1-2, wang2025pseudomonasaeruginosaacylcoa pages 5-6, sirithanakorn2024evidenceforendogenous pages 6-8, sirithanakorn2024evidenceforendogenous pages 1-2) |
| 3 | Enoyl-CoA hydration | **fadB** | Enoyl-CoA hydratase activity within FadB | **EC 4.2.1.17** | H₂O | Hydrates trans-2-enoyl-CoA to 3-hydroxyacyl-CoA as part of the trifunctional FadBA complex. In *E. coli* this activity resides in FadB rather than a separate enzyme. (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5) | FadB is part of the FadBA heterotetramer in *E. coli*. Some bacteria instead use paralogous systems such as FadIJ; *S. aureus* FadB also contains the crotonase domain but with domain orientation differing from *E. coli*. In *P. putida*, β-oxidation intermediates may also be diverted by PhaJ hydratases toward PHA biosynthesis. (pavoncello2022degradationofexogenous pages 11-13, liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3, menjivar2025characterizingthestaphylococcus pages 10-12, menjivar2025characterizingthestaphylococcus pages 8-10) |
| 4 | 3-Hydroxyacyl-CoA oxidation | **fadB** | 3-Hydroxyacyl-CoA dehydrogenase activity within FadB | **EC 1.1.1.35** | NAD⁺ | Oxidizes 3-hydroxyacyl-CoA to 3-ketoacyl-CoA, generating NADH in each β-oxidation round. (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5) | In *E. coli* this activity is fused with hydratase and accessory isomerase/epimerase functions in FadB. *S. aureus* encodes a bifunctional FadB with different domain arrangement; diverse proteobacteria and actinobacteria frequently expand this enzyme family into multiple paralogs. (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3, pavoncello2022degradationofexogenous pages 11-13, menjivar2025characterizingthestaphylococcus pages 10-12, menjivar2025characterizingthestaphylococcus pages 8-10) |
| 5 | Thiolytic cleavage to acetyl-CoA + shortened acyl-CoA | **fadA** | 3-Ketoacyl-CoA thiolase / acetyl-CoA C-acyltransferase | **EC 2.3.1.16** | CoA | Cleaves 3-ketoacyl-CoA thiolytically to release one acetyl-CoA and an acyl-CoA shortened by two carbons, enabling iterative cycling. (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5) | In *E. coli*, FadA partners with FadB in the FadBA complex. Backup or alternate thiolases occur in many bacteria, e.g. FadI in the FadIJ system and multiple thiolase paralogs in *Cupriavidus* and mycobacteria. (pavoncello2022degradationofexogenous pages 11-13, strittmatter2022insightsintothe pages 1-2) |
| 6 | Boundary: alkane/rubredoxin electron transfer feeding fatty acid degradation | **alkB, alkG, alkT** (canonical in alkane degraders; not part of core *E. coli* fad set) | Alkane monooxygenase (AlkB), rubredoxin (AlkG), rubredoxin reductase (AlkT) | AlkB **EC 1.14.15.3**; AlkG/AlkT electron-transfer proteins | NADH, FAD/FMNs in reductase, rubredoxin Fe center, O₂ | Oxidizes alkanes to alcohols/fatty-acid precursors before β-oxidation. Electrons flow **NADH → AlkT → AlkG → AlkB diiron center**, enabling oxygen activation and alkane hydroxylation. This is upstream of, not part of, the canonical β-oxidation spiral. (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, groves2023structureandfunction pages 1-3, landa2023exploringnovelalkanedegradation pages 1-2) | In *Pseudomonas putida* GPo1 and related systems, alkane oxidation products are further processed to fatty acids and then activated for β-oxidation. Electron-transfer architectures vary: separate AlkG/AlkT proteins, fused rubredoxin-AlkB proteins, or other fused redox modules. In KT2440-derived octane catabolism, host rubredoxin/rubredoxin reductase can supply the missing electron-transfer functions. (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, williams2022analkanemonooxygenase pages 7-10, landa2023exploringnovelalkanedegradation pages 1-2) |
| Aux | Unsaturated fatty acid auxiliary reduction | **fadH** | 2,4-Dienoyl-CoA reductase | **EC 1.3.1.34** | NADPH, Fe-S/flavin prosthetic groups | Reduces 2-trans,4-cis-dienoyl-CoA intermediates formed during degradation of unsaturated fatty acids with even-position double bonds, converting them into intermediates that can re-enter the main β-oxidation cycle. (pavoncello2022degradationofexogenous pages 7-9, pavoncello2022degradationofexogenous pages 22-23) | Required only for subsets of unsaturated fatty acids; not used in every β-oxidation round. This is a key example of substrate-conditional accessory chemistry layered onto the canonical spiral. (pavoncello2022degradationofexogenous pages 7-9) |
| Aux | Unsaturated fatty acid isomerization/epimerization | **fadB** | cis-Δ3-trans-Δ2-enoyl-CoA isomerase; 3-hydroxyacyl-CoA epimerase | Isomerase **EC 5.3.3.8**; epimerase often not separately assigned in pathway summaries | none specified beyond enzyme-bound chemistry | Repositions and/or stereochemically edits intermediates generated from unsaturated fatty acids so they can re-enter the standard hydratase/dehydrogenase sequence. FadB converts cis-Δ3 to trans-Δ2 enoyl-CoA and performs 3-hydroxyacyl epimerization. (pavoncello2022degradationofexogenous pages 7-9, pavoncello2022degradationofexogenous pages 22-23, pavoncello2022degradationofexogenous pages 5-7) | These activities illustrate why FadB is more than a simple hydratase/dehydrogenase. Accessory reactions are essential for odd-position unsaturations and for handling stereochemical mismatches generated during UFA catabolism. (pavoncello2022degradationofexogenous pages 7-9, pavoncello2022degradationofexogenous pages 5-7) |
| Aux | Secondary/backup β-oxidation complex | **fadI, fadJ** | FadI thiolase-like subunit; FadJ multifunctional FadB-like subunit | not firmly standardized across all annotations | FAD/NAD⁺/CoA as appropriate to embedded activities | Provides an alternative β-oxidation module in *E. coli*, especially associated with long-chain fatty acid conditions and backup function when the primary FadBA route is impaired. (pavoncello2022degradationofexogenous pages 11-13, pavoncello2022degradationofexogenous pages 13-15) | FadIJ preferentially handles medium/long-chain substrates relative to the core FadBA system and exemplifies enzyme redundancy. Analogous proliferation of FadBA-like paralogs is even more extensive in *Pseudomonas* and *Cupriavidus*. (pavoncello2022degradationofexogenous pages 11-13, strittmatter2023mediumchainlengthfattyacid pages 13-15) |
| Aux | Short-chain fatty acid entry/auxiliary degradation system | **atoD, atoA, atoB, atoE** with **fadE/fadB** contribution | AtoDA CoA-transferase/thiolase system; AtoB thiolase; AtoE transporter | variable by subunit; often summarized functionally rather than as one EC | CoA; pathway-specific cofactors | Supports short-chain fatty acid utilization in *E. coli*. SCFAs can enter via Ato components and then rely on FadE/FadB steps for complete oxidation, indicating that short-chain catabolism sits at the edge of the canonical fad module rather than fully within it. (pavoncello2022degradationofexogenous pages 9-11, strittmatter2023mediumchainlengthfattyacid pages 13-15) | Useful boundary case: *E. coli* partitions SCFA and LCFA metabolism across partially distinct genetic modules (ato vs fad), whereas other bacteria may use different acyl-CoA synthetases or β-oxidation operons for chain-length specialization. (pavoncello2022degradationofexogenous pages 9-11, strittmatter2023mediumchainlengthfattyacid pages 13-15) |


*Table: This table summarizes the canonical and auxiliary enzymes that define bacterial fatty acid β-oxidation, anchored to the E. coli fad system while highlighting key variants and boundary modules. It is useful for separating the core β-oxidation spiral from accessory unsaturated-fatty-acid chemistry, short-chain entry routes, and upstream alkane oxidation systems.*

## 4. Major Molecular Players and Active Assemblies

### 4.1 The FadBA trifunctional enzyme complex

The FadBA complex is the central catalytic assembly of bacterial β-oxidation. In *E. coli*, it forms an α₂β₂ heterotetramer where FadB contributes five enzymatic activities (enoyl-CoA hydratase, 3-hydroxyacyl-CoA dehydrogenase, cis-Δ3-trans-Δ2-enoyl-CoA isomerase, 3-hydroxyacyl-CoA epimerase, and an additional hydratase activity) and FadA provides thiolase activity (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 22-23). This consolidation of activities into a single complex likely improves catalytic efficiency through substrate channeling.

### 4.2 The FadIJ secondary complex

*E. coli* encodes a secondary β-oxidation system, FadIJ, where FadI is a FadA-like thiolase and FadJ is a FadB homolog (~35% sequence identity to FadB) (pavoncello2022degradationofexogenous pages 11-13). FadIJ is induced by long-chain fatty acids in an FadR-dependent manner and preferentially metabolizes medium/long-chain substrates. It serves as a backup system when FadBA is impaired (pavoncello2022degradationofexogenous pages 11-13).

### 4.3 FadR regulatory circuit

FadR is a dimeric winged helix-turn-helix transcription factor present at 300–400 molecules per cell in minimal media (cronan2021theescherichiacoli pages 4-7). It binds to the promoter regions of all *fad* genes (fadL, fadD, fadE, fadBA, fadIJ, fadH, fadM), blocking RNA polymerase access (pavoncello2022degradationofexogenous pages 15-17). Long-chain acyl-CoA thioesters (≥C14) bind to FadR's C-terminal domain, causing a conformational change that spreads the N-terminal DNA-binding domains by ~7 Å and abolishes DNA binding (cronan2021theescherichiacoli pages 1-4). FadR simultaneously serves as an activator of fatty acid biosynthesis genes (*fabA*, *fabB*, and more weakly other *fab* genes), creating a metabolic switch between catabolism and anabolism (cronan2021theescherichiacoli pages 13-18, pavoncello2022degradationofexogenous pages 17-19, cronan2021theescherichiacoli pages 4-7). Additional regulatory layers include cAMP-CRP catabolite repression and ArcAB anaerobic repression (pavoncello2022degradationofexogenous pages 13-15).

### 4.4 Acyl-CoA dehydrogenase diversity

Recent structural work on *Pseudomonas aeruginosa* FadE1 and FadE2 has revealed the molecular basis of chain-length specificity in bacterial acyl-CoA dehydrogenases (wang2025pseudomonasaeruginosaacylcoa pages 3-5, wang2025pseudomonasaeruginosaacylcoa pages 1-2, wang2025pseudomonasaeruginosaacylcoa pages 5-6). Both are FAD-dependent dimeric enzymes belonging to the ACAD superfamily, but FadE1 possesses a deep substrate cavity accommodating long-chain (C16–C18) acyl-CoAs, while FadE2's cavity is blocked by three residues (Met130, Glu296, Gln303), restricting it to medium-chain substrates (≤C10) (wang2025pseudomonasaeruginosaacylcoa pages 5-6). Engineering these selectivity-filter residues inverts the substrate preferences of the two enzymes, demonstrating that substrate specificity is encoded by a small number of structural determinants (wang2025pseudomonasaeruginosaacylcoa pages 5-6). A fadE1 mutant showed impaired virulence in an infection model, underscoring the physiological importance of chain-length-specific β-oxidation (wang2025pseudomonasaeruginosaacylcoa pages 1-2).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Variation across bacterial lineages

The core four-step β-oxidation spiral is conserved across all domains of life, consistent with an ancient metabolic origin likely predating the divergence of bacteria and archaea (pavoncello2022degradationofexogenous pages 5-7). However, gene organization, paralog number, and regulatory logic vary extensively:

| Organism | Gene Organization | Key fad Genes/Operons | Regulatory System | Number of Paralogs | Notable Features |
|---|---|---|---|---|---|
| *Escherichia coli* | fad genes are scattered across the chromosome and mostly transcribed independently; main paired operons are **fadBA** and **fadIJ**; **fadIJ** lies near **fadL** in reverse orientation (pavoncello2022degradationofexogenous pages 13-15) | **fadL, fadD, fadE, fadBA, fadIJ, fadH, fadM**; **fadBA** is the primary multifunctional β-oxidation system, **fadIJ** is a secondary/backup system, and **fadH** supports unsaturated FA degradation (pavoncello2022degradationofexogenous pages 15-17, pavoncello2022degradationofexogenous pages 13-15, pavoncello2022degradationofexogenous pages 11-13, pavoncello2022degradationofexogenous pages 7-9) | **FadR** represses fad genes and is relieved by long-chain acyl-CoA thioesters; additional control by **cAMP-CRP** and **ArcAB** (pavoncello2022degradationofexogenous pages 15-17, pavoncello2022degradationofexogenous pages 13-15, cronan2021theescherichiacoli pages 13-18, cronan2021theescherichiacoli pages 1-4) | Moderate redundancy: one main **FadBA** system plus secondary **FadIJ**; separate **ato** system contributes to SCFA utilization (pavoncello2022degradationofexogenous pages 11-13) | Canonical reference system; FadB combines hydratase/dehydrogenase plus isomerase/epimerase functions; unsaturated FAs require accessory chemistry such as **FadH** (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 11-13, pavoncello2022degradationofexogenous pages 7-9) |
| *Pseudomonas aeruginosa* | expanded β-oxidation gene repertoire with multiple homologous modules rather than a single dominant operon pair (pavoncello2022degradationofexogenous pages 11-13) | **FadE1** and **FadE2** are key ACADs; at least **5 FadBA homolog** pairs have been noted in the lineage (wang2025pseudomonasaeruginosaacylcoa pages 3-5, wang2025pseudomonasaeruginosaacylcoa pages 1-2, pavoncello2022degradationofexogenous pages 11-13) | fatty-acid responsive control is present, but the retrieved evidence here emphasizes enzyme specialization more than a single master regulator equivalent to *E. coli* FadR (wang2025pseudomonasaeruginosaacylcoa pages 3-5, wang2025pseudomonasaeruginosaacylcoa pages 1-2) | High redundancy: multiple **FadBA** homologs and at least two specialized **FadE** enzymes (wang2025pseudomonasaeruginosaacylcoa pages 3-5, pavoncello2022degradationofexogenous pages 11-13) | **FadE1** prefers long-chain acyl-CoAs, whereas **FadE2** is restricted to medium-chain substrates; substrate selectivity is structurally encoded by the binding pocket (wang2025pseudomonasaeruginosaacylcoa pages 3-5, wang2025pseudomonasaeruginosaacylcoa pages 1-2, wang2025pseudomonasaeruginosaacylcoa pages 5-6) |
| *Pseudomonas putida* KT2440 | evidence supports at least two β-oxidation machineries (**βI** and **βII**) in the pseudomonad lineage, with broad redundancy and links to other lipid-conversion routes (pavoncello2022degradationofexogenous pages 11-13) | core activities include **fadD, fadE, fadB, fadA**; β-oxidation intermediates are diverted by **phaJ1, phaJ4, maoC** toward PHA synthesis (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3) | not resolved here as a single regulator; control is intertwined with carbon source usage and pathway competition; alkane-utilization context adds additional regulation outside the core fad module (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3, williams2022anoverviewof pages 1-2) | Redundant hydratases and β-oxidation enzymes; at least three **PhaJ** homologs linked to diversion from β-oxidation into storage polymer synthesis (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3) | β-oxidation is tightly connected to **mcl-PHA** biosynthesis; **PhaJ4** is the main monomer supplier on C8/C10 FAs; KEGG **ppu00071** boundary context is justified because alkane oxidation feeds fatty acids into β-oxidation but is mechanistically upstream, not part of the core spiral (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3, palaciosferrer2026redirectinglinearhydrocarbon pages 1-2, williams2022anoverviewof pages 1-2, groves2023structureandfunction pages 1-3) |
| *Cupriavidus necator* H16 | multiple operons are deployed depending on substrate chain length; long-chain and medium-chain/dicarboxylate catabolism use overlapping but distinct gene sets (strittmatter2022insightsintothe pages 1-2, strittmatter2023mediumchainlengthfattyacid pages 13-15) | LCFA-associated operons include **A0459-A0464** and **A1526-A1531**; MCFA-responsive clusters include **B1187-B1192** and **B0751-B0759**; distinct activation and thiolase genes are recruited for dicarboxylates (strittmatter2022insightsintothe pages 1-2, strittmatter2023mediumchainlengthfattyacid pages 13-15) | lacks obvious *E. coli*-type **FadR** or *B. subtilis*-type **YsiA** homolog control for LCFA degradation in the cited data (strittmatter2023mediumchainlengthfattyacid pages 13-15) | Very high redundancy: numerous homologous acyl-CoA ligases, dehydrogenases, and thiolases can compensate for deletions (strittmatter2022insightsintothe pages 1-2, strittmatter2023mediumchainlengthfattyacid pages 13-15) | Strong substrate specialization by chain length and by mono- vs dicarboxylate chemistry; deletion of major operons often has limited phenotype because alternative paralogs substitute (strittmatter2022insightsintothe pages 1-2, strittmatter2023mediumchainlengthfattyacid pages 13-15) |
| *Staphylococcus aureus* | single polycistronic **fadXDEBA** operon rather than scattered genes (menjivar2025characterizingthestaphylococcus pages 2-5, menjivar2025characterizingthestaphylococcus pages 1-2, menjivar2025characterizingthestaphylococcus pages 5-8) | **fadXDEBA** encodes a complete pathway; **FadX** is a putative acyl-CoA transferase/accessory factor; **FadB** contains the overlooked crotonase domain needed for pathway completeness (menjivar2025characterizingthestaphylococcus pages 2-5, menjivar2025characterizingthestaphylococcus pages 10-12, menjivar2025characterizingthestaphylococcus pages 1-2) | strong catabolite repression by **CcpA**; derepressed when preferred carbon sources are absent or **ccpA** is lost (menjivar2025characterizingthestaphylococcus pages 2-5, menjivar2025characterizingthestaphylococcus pages 10-12) | Low apparent redundancy relative to proteobacterial examples; pathway is concentrated in one operon (menjivar2025characterizingthestaphylococcus pages 2-5, menjivar2025characterizingthestaphylococcus pages 5-8) | Historical genome annotations swapped **fadD** and **fadE** functional assignments relative to *E. coli*; **FadB** domain order is opposite that of *E. coli* (menjivar2025characterizingthestaphylococcus pages 2-5, menjivar2025characterizingthestaphylococcus pages 10-12, menjivar2025characterizingthestaphylococcus pages 8-10) |
| *Mycobacterium tuberculosis* | highly expanded lipid-catabolic genome with many fad-family enzymes distributed across the chromosome rather than a single compact canonical fad module (pavoncello2022degradationofexogenous pages 11-13) | multiple **FadA-like thiolases** are present and have been classified into several families; many individual roles remain unresolved (pavoncello2022degradationofexogenous pages 11-13) | regulatory architecture is more distributed and lipid-responsive, but the present evidence mainly supports gene-family expansion rather than a single simplified regulator model (pavoncello2022degradationofexogenous pages 11-13) | Very high redundancy, especially among **FadA-like thiolases** (pavoncello2022degradationofexogenous pages 11-13) | Expansion is consistent with adaptation to diverse host lipids and complex acyl substrates; family proliferation complicates assignment of ancestral/core roles (pavoncello2022degradationofexogenous pages 11-13) |
| *Bacillus subtilis* | not presented here as a canonical fad-model β-oxidizer; included mainly as a regulatory contrast for Gram-positive lipid control (waters2024bacterialacquisitionof pages 12-14) | β-oxidation genes are not the focus of the cited evidence; comparison centers on global fatty-acid homeostasis regulators rather than a defined fad operon set (waters2024bacterialacquisitionof pages 12-14) | **FapR** senses malonyl-CoA and controls fatty-acid homeostasis; this differs from the acyl-CoA-sensing **FadR** logic of *E. coli* (waters2024bacterialacquisitionof pages 12-14) | Not established in the cited evidence for β-oxidation-specific paralogs (waters2024bacterialacquisitionof pages 12-14) | Useful comparator showing that Gram-positive bacteria can regulate lipid metabolism without the *E. coli*-style FadR module; included to frame lineage-specific regulatory divergence (waters2024bacterialacquisitionof pages 12-14) |


*Table: This table compares how core β-oxidation systems are organized and regulated across representative bacterial lineages. It highlights where the canonical *E. coli* model generalizes well and where lineage-specific paralog expansion, operon structure, or regulatory rewiring make it a poor proxy.*

Key observations include:

- **Gene organization**: *E. coli* *fad* genes are scattered around the chromosome and independently transcribed, except *fadBA* and *fadIJ* operons (pavoncello2022degradationofexogenous pages 13-15). In contrast, *S. aureus* consolidates all pathway genes into a single *fadXDEBA* polycistronic operon (menjivar2025characterizingthestaphylococcus pages 2-5, menjivar2025characterizingthestaphylococcus pages 1-2).

- **Paralog expansion**: *C. necator* H16 possesses an exceptionally high number of β-oxidation paralogs, with multiple operons (A0459-A0464, A1526-A1531, B1187-B1192, B0751-B0759) expressed differentially depending on substrate chain length (strittmatter2022insightsintothe pages 1-2, strittmatter2023mediumchainlengthfattyacid pages 13-15). Deletion of major operons often yields minimal growth defects because alternative paralogs compensate (strittmatter2023mediumchainlengthfattyacid pages 13-15). *P. aeruginosa* encodes at least five FadBA homolog pairs (pavoncello2022degradationofexogenous pages 11-13).

- **Regulatory divergence**: FadR-type acyl-CoA-dependent regulation is characteristic of γ-proteobacteria but is not universal. *S. aureus* uses CcpA-mediated catabolite repression (menjivar2025characterizingthestaphylococcus pages 2-5, menjivar2025characterizingthestaphylococcus pages 10-12). *B. subtilis* employs FapR (sensing malonyl-CoA) for fatty acid homeostasis, a fundamentally different sensing logic (waters2024bacterialacquisitionof pages 12-14). *M. tuberculosis* encodes FadR orthologs, one of which is functional in *E. coli* (cronan2021theescherichiacoli pages 13-18). *C. necator* H16 lacks obvious FadR or YsiA homologs (strittmatter2023mediumchainlengthfattyacid pages 13-15).

### 5.2 Lateral gene transfer

Phylogenetic analysis of the 2,4-dienoyl-CoA reductase (DECR) in *Leishmania* parasites provides direct evidence for lateral gene transfer (LGT) of β-oxidation components from bacteria to eukaryotes. The *Leishmania* DECR shows close homology to bacterial NADPH-dependent reductases rather than to mammalian equivalents, and phylogenetic analysis supports at least two independent LGT events from different bacterial lineages into ancestral trypanosomatids (semini2020leishmaniaencodesa pages 3-4, semini2020leishmaniaencodesa pages 2-3, semini2020leishmaniaencodesa pages 1-2). The gene is retained in intracellular parasites (*Leishmania*, *T. cruzi*) but lost in exclusively extracellular species (*T. brucei*), suggesting selective retention linked to intracellular survival and access to host-derived polyunsaturated fatty acids (semini2020leishmaniaencodesa pages 2-3, semini2020leishmaniaencodesa pages 1-2).

### 5.3 The *Pseudomonas putida* KT2440 context

In *P. putida* KT2440, β-oxidation serves dual roles: energy generation and provision of (R)-3-hydroxyacyl-CoA precursors for medium-chain-length PHA biosynthesis. Three PhaJ homologs (PhaJ1, PhaJ4, MaoC) divert trans-2-enoyl-CoA intermediates from the β-oxidation cycle toward PHA monomer supply, with PhaJ4 being the primary contributor for C8 and C10 substrates (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3). Remarkably, deletion of all three PhaJ homologs still permits PHA accumulation at ~10.7% cell dry weight, indicating additional, non-specific enzymatic routes can supply monomers (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3).

The KEGG pathway ppu00071 includes alkane/rubredoxin nodes because *P. putida* strains that acquire alkane-degradation capacity (via ICE elements bearing *alkB*) use the AlkB monooxygenase system to convert alkanes to fatty acids, which then enter β-oxidation (palaciosferrer2026redirectinglinearhydrocarbon pages 1-2, groves2023structureandfunction pages 1-3). In *P. putida* KT2440 derivatives that have acquired alkane-degradation genes, host rubredoxin and rubredoxin reductase can substitute for the missing AlkG/AlkT electron-transfer proteins from the canonical OCT operon, enabling octane metabolism (williams2022anoverviewof pages 1-2, groves2023structureandfunction pages 1-3). The fatty acids produced (e.g., octanoate from octane) are activated by acyl-CoA synthetases and metabolized via β-oxidation and the glyoxylate shunt (palaciosferrer2026redirectinglinearhydrocarbon pages 1-2, palaciosferrer2026redirectinglinearhydrocarbon pages 7-11).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory ordering

The pathway has strict sequential constraints: activation must precede dehydrogenation (free fatty acids are not substrates for FadE); hydration requires the trans-2-enoyl-CoA product of FadE; and thiolysis requires the 3-keto intermediate generated by the NAD⁺-dependent oxidation (pavoncello2022degradationofexogenous pages 5-7, pavoncello2022degradationofexogenous pages 2-5). Auxiliary reactions for unsaturated fatty acids are conditional—they are invoked only when the substrate contains pre-existing double bonds at specific positions (pavoncello2022degradationofexogenous pages 7-9).

### 6.2 Cofactor requirements and energetics

Each full turn of the β-oxidation spiral produces one FADH₂ (from FadE), one NADH (from FadB dehydrogenase), and one acetyl-CoA, at the cost of one CoA consumed in the thiolysis step. The initial activation consumes the equivalent of two ATP (ATP → AMP + PPi) per fatty acid molecule. The reduced cofactors must be reoxidized by the electron transport chain, making aerobic respiration the typical context for high-flux β-oxidation (pavoncello2022degradationofexogenous pages 5-7). Under anaerobic conditions, *E. coli* can perform β-oxidation but uses different acyl-CoA dehydrogenase isoforms (YdiO rather than FadE/YafH) that are not under FadR regulation (cronan2021theescherichiacoli pages 13-18, strittmatter2022insightsintothe pages 1-2).

### 6.3 Reactive oxygen species generation

A recently characterized failure mode involves FadE-dependent ROS generation. During high-flux fatty acid catabolism, the FadE flavin can transfer electrons to molecular oxygen, producing superoxide and H₂O₂ (sirithanakorn2024evidenceforendogenous pages 6-8, sirithanakorn2024evidenceforendogenous pages 2-4). This is physiologically manageable in wild-type cells with intact catalase and peroxidase defenses, but becomes growth-limiting in scavenging-deficient mutants (sirithanakorn2024evidenceforendogenous pages 1-2). Excess superoxide can inactivate aconitase of the TCA cycle, potentially stalling acetyl-CoA metabolism and creating a feedback bottleneck during intense β-oxidation (sirithanakorn2024evidenceforendogenous pages 12-14).

### 6.4 Substrate channeling and compartmentalization

Unlike eukaryotic β-oxidation, which is compartmentalized in mitochondria and peroxisomes, bacterial β-oxidation occurs in the cytoplasm, with the FadBA complex presumably associated with the inner membrane via FadE interactions. The physical coupling of FadL-mediated uptake, FadD activation, and the FadEBA complex suggests a degree of spatial organization, though formal evidence for a membrane-associated metabolon remains limited (pavoncello2022degradationofexogenous pages 2-5, pavoncello2022degradationofexogenous pages 5-7).

## 7. Controversies and Open Questions

### 7.1 The FadE electron acceptor problem

Perhaps the most significant unresolved mechanistic question is the identity of the physiological electron acceptor for *E. coli* FadE. Unlike well-characterized mitochondrial acyl-CoA dehydrogenases that use ETF as an obligate partner, no ETF has been definitively assigned to *E. coli* FadE (sirithanakorn2024evidenceforendogenous pages 11-12, sirithanakorn2024evidenceforendogenous pages 1-2). The C-terminal domain of FadE has been speculated to function as a flavoprotein domain involved in electron transfer to the respiratory chain (pavoncello2022degradationofexogenous pages 11-13), but in vitro reconstitution of the full catalytic cycle remains to be achieved (sirithanakorn2024evidenceforendogenous pages 12-14). This gap is consequential because it directly relates to the ROS-generation side reaction and to energetic coupling of β-oxidation with respiration.

### 7.2 Gene annotation inconsistencies

Mis-annotation of *fad* genes across bacterial genomes is a persistent problem. In *S. aureus*, the genes annotated as *fadD* and *fadE* are functionally swapped relative to *E. coli* conventions—*SAUSA300_0228* (labeled *fadE*) actually encodes the acyl-CoA synthetase (FadD function) and *SAUSA300_0227* (labeled *fadD*) encodes the acyl-CoA dehydrogenase (FadE function) (menjivar2025characterizingthestaphylococcus pages 2-5). Additionally, a crotonase domain in *S. aureus* FadB was historically overlooked because its domain orientation differs from *E. coli* FadB (menjivar2025characterizingthestaphylococcus pages 10-12, menjivar2025characterizingthestaphylococcus pages 8-10). These annotation errors have led to incorrect assumptions about pathway completeness in Gram-positive organisms.

### 7.3 Paralog redundancy and functional assignment

In organisms with extensive β-oxidation gene families (*C. necator*, *P. aeruginosa*, *M. tuberculosis*), assigning specific physiological roles to individual paralogs remains challenging. Deletion of individual genes often produces no detectable phenotype due to functional compensation (strittmatter2022insightsintothe pages 1-2, strittmatter2023mediumchainlengthfattyacid pages 13-15). This redundancy may reflect adaptation to diverse fatty acid substrates encountered in complex environments, but it complicates genetic analysis and makes it difficult to identify which paralogs represent ancestral core functions versus later elaborations.

### 7.4 Boundary between β-oxidation and alkane oxidation

The inclusion of alkane monooxygenase (AlkB) and rubredoxin electron-transfer components in KEGG fatty acid degradation pathways (e.g., ppu00071) creates a boundary ambiguity. These enzymes catalyze the initial hydroxylation of alkanes to alcohols—a reaction that is mechanistically unrelated to the CoA-dependent thioester chemistry of β-oxidation (williams2022anoverviewof pages 1-2, groves2023structureandfunction pages 1-3). Their inclusion reflects metabolic connectivity (alkane oxidation produces fatty acid substrates for β-oxidation) rather than enzymatic homology. The diversity of AlkB electron-transfer architectures—separate proteins, rubredoxin-fused AlkB, and ferredoxin-reductase-fused AlkB variants—further underscores that these are distinct molecular systems (williams2022anoverviewof pages 2-4, williams2022analkanemonooxygenase pages 7-10, williams2022anoverviewof pages 4-5).

### 7.5 Reverse β-oxidation as a biotechnology platform

The reverse β-oxidation (rBOX) pathway has emerged as a powerful metabolic engineering platform, exploiting the thermodynamic reversibility of β-oxidation enzymes for iterative carbon-chain elongation. rBOX uses only four core enzymes, requires no ATP, and can produce diverse products from C3 to C16+ with various functional groups (tarasava2022reverseβoxidationpathways pages 3-4, tarasava2022reverseβoxidationpathways pages 1-2, tarasava2022reverseβoxidationpathways pages 2-3). Recent advances include growth-coupled rBOX for fatty alcohol fermentation in *E. coli*, achieving titers of 2.5 g/L through adaptive evolution (keasling2026growthcoupledreverseβoxidation pages 1-5). The success of rBOX demonstrates that β-oxidation enzymology is inherently bidirectional and that the directionality in vivo is imposed by thermodynamic driving forces (cofactor ratios, product removal) rather than by intrinsic enzyme irreversibility.

## 8. Key References

The following references provide the primary evidentiary basis for this review:

1. Pavoncello V, Barras F, Bouveret E. Degradation of Exogenous Fatty Acids in *Escherichia coli*. *Biomolecules*. 2022;12:1019. doi:10.3390/biom12081019.
2. Cronan JE. The *Escherichia coli* FadR Transcription Factor: Too Much of a Good Thing? *Mol Microbiol*. 2021;115:1080-1085. doi:10.1111/mmi.14663.
3. Wang M, et al. *Pseudomonas aeruginosa* Acyl-CoA Dehydrogenases and Structure-Guided Inversion of Their Substrate Specificity. *Nat Commun*. 2025;16. doi:10.1038/s41467-025-57532-z.
4. Sirithanakorn C, Imlay JA. Evidence for Endogenous Hydrogen Peroxide Production by *E. coli* Fatty Acyl-CoA Dehydrogenase. *PLoS ONE*. 2024;19:e0309988. doi:10.1371/journal.pone.0309988.
5. Menjivar C, et al. Characterizing the *Staphylococcus aureus* Fatty Acid Degradation Operon. *J Bacteriol*. 2025:e0008925. doi:10.1128/jb.00089-25.
6. Strittmatter CS, et al. Medium-Chain-Length Fatty Acid Catabolism in *Cupriavidus necator* H16. *Appl Environ Microbiol*. 2023;89. doi:10.1128/aem.01428-22.
7. Williams SC, Austin RN. An Overview of the Electron-Transfer Proteins That Activate Alkane Monooxygenase (AlkB). *Front Microbiol*. 2022;13. doi:10.3389/fmicb.2022.845551.
8. Liu S, et al. β-Oxidation–Polyhydroxyalkanoates Synthesis Relationship in *Pseudomonas putida* KT2440 Revisited. *Appl Microbiol Biotechnol*. 2023;107:1863-1874. doi:10.1007/s00253-023-12413-7.
9. Waters JK, Eijkelkamp BA. Bacterial Acquisition of Host Fatty Acids Has Far-Reaching Implications on Virulence. *Microbiol Mol Biol Rev*. 2024;88. doi:10.1128/mmbr.00126-24.
10. Semini G, et al. *Leishmania* Encodes a Bacterium-like 2,4-Dienoyl-Coenzyme A Reductase Required for Fatty Acid β-Oxidation. *mBio*. 2020;11. doi:10.1128/mbio.01057-20.
11. Tarasava K, et al. Reverse β-Oxidation Pathways for Efficient Chemical Production. *J Ind Microbiol Biotechnol*. 2022;49. doi:10.1093/jimb/kuac003.
12. Groves JT, Feng L, Austin RN. Structure and Function of Alkane Monooxygenase (AlkB). *Acc Chem Res*. 2023;56:3665-3675. doi:10.1021/acs.accounts.3c00590.

References

1. (pavoncello2022degradationofexogenous pages 5-7): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

2. (pavoncello2022degradationofexogenous pages 2-5): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

3. (pavoncello2022degradationofexogenous pages 15-17): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

4. (cronan2021theescherichiacoli pages 13-18): John E. Cronan. The <i>escherichia coli</i> fadr transcription factor: too much of a good thing? Dec 2021. URL: https://doi.org/10.1111/mmi.14663, doi:10.1111/mmi.14663. This article has 45 citations and is from a domain leading peer-reviewed journal.

5. (cronan2021theescherichiacoli pages 1-4): John E. Cronan. The <i>escherichia coli</i> fadr transcription factor: too much of a good thing? Dec 2021. URL: https://doi.org/10.1111/mmi.14663, doi:10.1111/mmi.14663. This article has 45 citations and is from a domain leading peer-reviewed journal.

6. (menjivar2025characterizingthestaphylococcus pages 2-5): Cindy Menjivar, Z. DeMars, Richard E. Wiemels, Ronan K. Carroll, and Jeffrey L. Bose. Characterizing the staphylococcus aureus fatty acid degradation operon. Journal of bacteriology, pages e0008925, Jul 2025. URL: https://doi.org/10.1128/jb.00089-25, doi:10.1128/jb.00089-25. This article has 5 citations and is from a peer-reviewed journal.

7. (strittmatter2022insightsintothe pages 1-2): Carl Simon Strittmatter, Jessica Eggers, Vanessa Biesgen, Jan-Niklas Hengsbach, Akihiro Sakatoku, Dirk Albrecht, Katharina Riedel, and Alexander Steinbüchel. Insights into the degradation of medium-chain-length dicarboxylic acids in cupriavidus necator h16 reveal β-oxidation differences between dicarboxylic acids and fatty acids. Jan 2022. URL: https://doi.org/10.1128/aem.01873-21, doi:10.1128/aem.01873-21. This article has 18 citations and is from a peer-reviewed journal.

8. (strittmatter2023mediumchainlengthfattyacid pages 13-15): Carl Simon Strittmatter, Anja Poehlein, Axel Himmelbach, Rolf Daniel, and Alexander Steinbüchel. Medium-chain-length fatty acid catabolism in cupriavidus necator h16: transcriptome sequencing reveals differences from long-chain-length fatty acid β-oxidation and involvement of several homologous genes. Jan 2023. URL: https://doi.org/10.1128/aem.01428-22, doi:10.1128/aem.01428-22. This article has 16 citations and is from a peer-reviewed journal.

9. (williams2022anoverviewof pages 1-2): Shoshana C. Williams and Rachel Narehood Austin. An overview of the electron-transfer proteins that activate alkane monooxygenase (alkb). Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2022.845551, doi:10.3389/fmicb.2022.845551. This article has 43 citations and is from a peer-reviewed journal.

10. (groves2023structureandfunction pages 1-3): John T. Groves, Liang Feng, and Rachel Narehood Austin. Structure and function of alkane monooxygenase (alkb). Accounts of chemical research, 56:3665-3675, Nov 2023. URL: https://doi.org/10.1021/acs.accounts.3c00590, doi:10.1021/acs.accounts.3c00590. This article has 42 citations and is from a domain leading peer-reviewed journal.

11. (pavoncello2022degradationofexogenous pages 7-9): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

12. (pavoncello2022degradationofexogenous pages 11-13): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

13. (pavoncello2022degradationofexogenous pages 13-15): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

14. (waters2024bacterialacquisitionof pages 7-9): Jack K. Waters and Bart A. Eijkelkamp. Bacterial acquisition of host fatty acids has far-reaching implications on virulence. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00126-24, doi:10.1128/mmbr.00126-24. This article has 12 citations and is from a domain leading peer-reviewed journal.

15. (williams2022anoverviewof pages 2-4): Shoshana C. Williams and Rachel Narehood Austin. An overview of the electron-transfer proteins that activate alkane monooxygenase (alkb). Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2022.845551, doi:10.3389/fmicb.2022.845551. This article has 43 citations and is from a peer-reviewed journal.

16. (pavoncello2022degradationofexogenous pages 17-19): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

17. (liu2023βoxidation–polyhydroxyalkanoatessynthesisrelationship pages 1-3): Si Liu, Tanja Narancic, Jia-Lynn Tham, and Kevin E. O’Connor. Β-oxidation–polyhydroxyalkanoates synthesis relationship in pseudomonas putida kt2440 revisited. Applied Microbiology and Biotechnology, 107:1863-1874, Feb 2023. URL: https://doi.org/10.1007/s00253-023-12413-7, doi:10.1007/s00253-023-12413-7. This article has 37 citations and is from a domain leading peer-reviewed journal.

18. (wang2025pseudomonasaeruginosaacylcoa pages 1-2): Meng Wang, Prasanthi Medarametla, Thales Kronenberger, Tomas Deingruber, Paul Brear, Wendy Figueroa, Pok-Man Ho, Thomas Krueger, James C. Pearce, Antti Poso, James G. Wakefield, David R. Spring, and Martin Welch. Pseudomonas aeruginosa acyl-coa dehydrogenases and structure-guided inversion of their substrate specificity. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-57532-z, doi:10.1038/s41467-025-57532-z. This article has 15 citations and is from a highest quality peer-reviewed journal.

19. (sirithanakorn2024evidenceforendogenous pages 11-12): Chaiyos Sirithanakorn and James A. Imlay. Evidence for endogenous hydrogen peroxide production by e. coli fatty acyl-coa dehydrogenase. PLOS ONE, 19:e0309988, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0309988, doi:10.1371/journal.pone.0309988. This article has 5 citations and is from a peer-reviewed journal.

20. (sirithanakorn2024evidenceforendogenous pages 1-2): Chaiyos Sirithanakorn and James A. Imlay. Evidence for endogenous hydrogen peroxide production by e. coli fatty acyl-coa dehydrogenase. PLOS ONE, 19:e0309988, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0309988, doi:10.1371/journal.pone.0309988. This article has 5 citations and is from a peer-reviewed journal.

21. (sirithanakorn2024evidenceforendogenous pages 6-8): Chaiyos Sirithanakorn and James A. Imlay. Evidence for endogenous hydrogen peroxide production by e. coli fatty acyl-coa dehydrogenase. PLOS ONE, 19:e0309988, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0309988, doi:10.1371/journal.pone.0309988. This article has 5 citations and is from a peer-reviewed journal.

22. (sirithanakorn2024evidenceforendogenous pages 2-4): Chaiyos Sirithanakorn and James A. Imlay. Evidence for endogenous hydrogen peroxide production by e. coli fatty acyl-coa dehydrogenase. PLOS ONE, 19:e0309988, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0309988, doi:10.1371/journal.pone.0309988. This article has 5 citations and is from a peer-reviewed journal.

23. (pavoncello2022degradationofexogenous pages 22-23): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

24. (wang2025pseudomonasaeruginosaacylcoa pages 3-5): Meng Wang, Prasanthi Medarametla, Thales Kronenberger, Tomas Deingruber, Paul Brear, Wendy Figueroa, Pok-Man Ho, Thomas Krueger, James C. Pearce, Antti Poso, James G. Wakefield, David R. Spring, and Martin Welch. Pseudomonas aeruginosa acyl-coa dehydrogenases and structure-guided inversion of their substrate specificity. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-57532-z, doi:10.1038/s41467-025-57532-z. This article has 15 citations and is from a highest quality peer-reviewed journal.

25. (wang2025pseudomonasaeruginosaacylcoa pages 5-6): Meng Wang, Prasanthi Medarametla, Thales Kronenberger, Tomas Deingruber, Paul Brear, Wendy Figueroa, Pok-Man Ho, Thomas Krueger, James C. Pearce, Antti Poso, James G. Wakefield, David R. Spring, and Martin Welch. Pseudomonas aeruginosa acyl-coa dehydrogenases and structure-guided inversion of their substrate specificity. Nature Communications, Mar 2025. URL: https://doi.org/10.1038/s41467-025-57532-z, doi:10.1038/s41467-025-57532-z. This article has 15 citations and is from a highest quality peer-reviewed journal.

26. (menjivar2025characterizingthestaphylococcus pages 10-12): Cindy Menjivar, Z. DeMars, Richard E. Wiemels, Ronan K. Carroll, and Jeffrey L. Bose. Characterizing the staphylococcus aureus fatty acid degradation operon. Journal of bacteriology, pages e0008925, Jul 2025. URL: https://doi.org/10.1128/jb.00089-25, doi:10.1128/jb.00089-25. This article has 5 citations and is from a peer-reviewed journal.

27. (menjivar2025characterizingthestaphylococcus pages 8-10): Cindy Menjivar, Z. DeMars, Richard E. Wiemels, Ronan K. Carroll, and Jeffrey L. Bose. Characterizing the staphylococcus aureus fatty acid degradation operon. Journal of bacteriology, pages e0008925, Jul 2025. URL: https://doi.org/10.1128/jb.00089-25, doi:10.1128/jb.00089-25. This article has 5 citations and is from a peer-reviewed journal.

28. (landa2023exploringnovelalkanedegradation pages 1-2): Mirna Vázquez Rosas Landa, Valerie De Anda, Robin R. Rohwer, Angelina Angelova, Georgia Waldram, Tony Gutierrez, and Brett J. Baker. Exploring novel alkane-degradation pathways in uncultured bacteria from the north atlantic ocean. Oct 2023. URL: https://doi.org/10.1128/msystems.00619-23, doi:10.1128/msystems.00619-23. This article has 22 citations and is from a peer-reviewed journal.

29. (williams2022analkanemonooxygenase pages 7-10): Shoshana C. Williams, Dahlia Luongo, Marina Orman, Christina L. Vizcarra, and Rachel N. Austin. An alkane monooxygenase (alkb) family in which all electron transfer partners are covalently bound to the oxygen-activating hydroxylase. Mar 2022. URL: https://doi.org/10.1016/j.jinorgbio.2021.111707, doi:10.1016/j.jinorgbio.2021.111707. This article has 30 citations and is from a peer-reviewed journal.

30. (pavoncello2022degradationofexogenous pages 9-11): Viola Pavoncello, Frédéric Barras, and Emmanuelle Bouveret. Degradation of exogenous fatty acids in escherichia coli. Biomolecules, 12:1019, Jul 2022. URL: https://doi.org/10.3390/biom12081019, doi:10.3390/biom12081019. This article has 94 citations.

31. (cronan2021theescherichiacoli pages 4-7): John E. Cronan. The <i>escherichia coli</i> fadr transcription factor: too much of a good thing? Dec 2021. URL: https://doi.org/10.1111/mmi.14663, doi:10.1111/mmi.14663. This article has 45 citations and is from a domain leading peer-reviewed journal.

32. (palaciosferrer2026redirectinglinearhydrocarbon pages 1-2): Rocío Palacios-Ferrer, María T. Manoli, Patricia Godoy, Antonio Delgado, Auxiliadora Prieto, and Juan L. Ramos. Redirecting linear hydrocarbon metabolism toward polyhydroxyalkanoate biosynthesis. Microbial Cell Factories, Jan 2026. URL: https://doi.org/10.1186/s12934-025-02914-7, doi:10.1186/s12934-025-02914-7. This article has 0 citations and is from a peer-reviewed journal.

33. (menjivar2025characterizingthestaphylococcus pages 1-2): Cindy Menjivar, Z. DeMars, Richard E. Wiemels, Ronan K. Carroll, and Jeffrey L. Bose. Characterizing the staphylococcus aureus fatty acid degradation operon. Journal of bacteriology, pages e0008925, Jul 2025. URL: https://doi.org/10.1128/jb.00089-25, doi:10.1128/jb.00089-25. This article has 5 citations and is from a peer-reviewed journal.

34. (menjivar2025characterizingthestaphylococcus pages 5-8): Cindy Menjivar, Z. DeMars, Richard E. Wiemels, Ronan K. Carroll, and Jeffrey L. Bose. Characterizing the staphylococcus aureus fatty acid degradation operon. Journal of bacteriology, pages e0008925, Jul 2025. URL: https://doi.org/10.1128/jb.00089-25, doi:10.1128/jb.00089-25. This article has 5 citations and is from a peer-reviewed journal.

35. (waters2024bacterialacquisitionof pages 12-14): Jack K. Waters and Bart A. Eijkelkamp. Bacterial acquisition of host fatty acids has far-reaching implications on virulence. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00126-24, doi:10.1128/mmbr.00126-24. This article has 12 citations and is from a domain leading peer-reviewed journal.

36. (semini2020leishmaniaencodesa pages 3-4): Geo Semini, Daniel Paape, Daniel Paape, Martin Blume, Martin Blume, M. F. Sernee, Diego Peres-Alonso, Diego Peres-Alonso, S. Calvignac‐Spencer, Jörg Döllinger, Stefan Jehle, Eleanor C. Saunders, M. McConville, Toni Aebischer, and Toni Aebischer. <i>leishmania</i> encodes a bacterium-like 2,4-dienoyl-coenzyme a reductase that is required for fatty acid β-oxidation and intracellular parasite survival. Jun 2020. URL: https://doi.org/10.1128/mbio.01057-20, doi:10.1128/mbio.01057-20. This article has 18 citations and is from a domain leading peer-reviewed journal.

37. (semini2020leishmaniaencodesa pages 2-3): Geo Semini, Daniel Paape, Daniel Paape, Martin Blume, Martin Blume, M. F. Sernee, Diego Peres-Alonso, Diego Peres-Alonso, S. Calvignac‐Spencer, Jörg Döllinger, Stefan Jehle, Eleanor C. Saunders, M. McConville, Toni Aebischer, and Toni Aebischer. <i>leishmania</i> encodes a bacterium-like 2,4-dienoyl-coenzyme a reductase that is required for fatty acid β-oxidation and intracellular parasite survival. Jun 2020. URL: https://doi.org/10.1128/mbio.01057-20, doi:10.1128/mbio.01057-20. This article has 18 citations and is from a domain leading peer-reviewed journal.

38. (semini2020leishmaniaencodesa pages 1-2): Geo Semini, Daniel Paape, Daniel Paape, Martin Blume, Martin Blume, M. F. Sernee, Diego Peres-Alonso, Diego Peres-Alonso, S. Calvignac‐Spencer, Jörg Döllinger, Stefan Jehle, Eleanor C. Saunders, M. McConville, Toni Aebischer, and Toni Aebischer. <i>leishmania</i> encodes a bacterium-like 2,4-dienoyl-coenzyme a reductase that is required for fatty acid β-oxidation and intracellular parasite survival. Jun 2020. URL: https://doi.org/10.1128/mbio.01057-20, doi:10.1128/mbio.01057-20. This article has 18 citations and is from a domain leading peer-reviewed journal.

39. (palaciosferrer2026redirectinglinearhydrocarbon pages 7-11): Rocío Palacios-Ferrer, María T. Manoli, Patricia Godoy, Antonio Delgado, Auxiliadora Prieto, and Juan L. Ramos. Redirecting linear hydrocarbon metabolism toward polyhydroxyalkanoate biosynthesis. Microbial Cell Factories, Jan 2026. URL: https://doi.org/10.1186/s12934-025-02914-7, doi:10.1186/s12934-025-02914-7. This article has 0 citations and is from a peer-reviewed journal.

40. (sirithanakorn2024evidenceforendogenous pages 12-14): Chaiyos Sirithanakorn and James A. Imlay. Evidence for endogenous hydrogen peroxide production by e. coli fatty acyl-coa dehydrogenase. PLOS ONE, 19:e0309988, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0309988, doi:10.1371/journal.pone.0309988. This article has 5 citations and is from a peer-reviewed journal.

41. (williams2022anoverviewof pages 4-5): Shoshana C. Williams and Rachel Narehood Austin. An overview of the electron-transfer proteins that activate alkane monooxygenase (alkb). Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2022.845551, doi:10.3389/fmicb.2022.845551. This article has 43 citations and is from a peer-reviewed journal.

42. (tarasava2022reverseβoxidationpathways pages 3-4): Katia Tarasava, Seung Hwan Lee, Jing Chen, Michael Köpke, Michael C Jewett, and Ramon Gonzalez. Reverse β-oxidation pathways for efficient chemical production. Journal of Industrial Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1093/jimb/kuac003, doi:10.1093/jimb/kuac003. This article has 55 citations and is from a peer-reviewed journal.

43. (tarasava2022reverseβoxidationpathways pages 1-2): Katia Tarasava, Seung Hwan Lee, Jing Chen, Michael Köpke, Michael C Jewett, and Ramon Gonzalez. Reverse β-oxidation pathways for efficient chemical production. Journal of Industrial Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1093/jimb/kuac003, doi:10.1093/jimb/kuac003. This article has 55 citations and is from a peer-reviewed journal.

44. (tarasava2022reverseβoxidationpathways pages 2-3): Katia Tarasava, Seung Hwan Lee, Jing Chen, Michael Köpke, Michael C Jewett, and Ramon Gonzalez. Reverse β-oxidation pathways for efficient chemical production. Journal of Industrial Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1093/jimb/kuac003, doi:10.1093/jimb/kuac003. This article has 55 citations and is from a peer-reviewed journal.

45. (keasling2026growthcoupledreverseβoxidation pages 1-5): Jay Keasling, Bridgie Cawthon, Aidan Cowan, Zen Yoshikawa, Kenneth Low, Justin Baerwald, Matthew Incha, Jennifer Gin, Yan Chen, Christopher Petzold, Edward Baidoo, Emine Akyuz Turumtay, and Adam Feist. Growth-coupled reverse β-oxidation enables redox-balanced fatty-alcohol fermentation and strain evolution. Unknown journal, Mar 2026. URL: https://doi.org/10.21203/rs.3.rs-8340431/v1, doi:10.21203/rs.3.rs-8340431/v1.

## Artifacts

- [Edison artifact artifact-00](bacterial_fatty_acid_beta_oxidation-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](bacterial_fatty_acid_beta_oxidation-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. menjivar2025characterizingthestaphylococcus pages 2-5
2. pavoncello2022degradationofexogenous pages 2-5
3. pavoncello2022degradationofexogenous pages 11-13
4. sirithanakorn2024evidenceforendogenous pages 11-12
5. pavoncello2022degradationofexogenous pages 5-7
6. pavoncello2022degradationofexogenous pages 7-9
7. cronan2021theescherichiacoli pages 4-7
8. pavoncello2022degradationofexogenous pages 15-17
9. cronan2021theescherichiacoli pages 1-4
10. pavoncello2022degradationofexogenous pages 13-15
11. wang2025pseudomonasaeruginosaacylcoa pages 5-6
12. wang2025pseudomonasaeruginosaacylcoa pages 1-2
13. strittmatter2023mediumchainlengthfattyacid pages 13-15
14. waters2024bacterialacquisitionof pages 12-14
15. cronan2021theescherichiacoli pages 13-18
16. sirithanakorn2024evidenceforendogenous pages 1-2
17. sirithanakorn2024evidenceforendogenous pages 12-14
18. strittmatter2022insightsintothe pages 1-2
19. williams2022anoverviewof pages 1-2
20. groves2023structureandfunction pages 1-3
21. waters2024bacterialacquisitionof pages 7-9
22. williams2022anoverviewof pages 2-4
23. pavoncello2022degradationofexogenous pages 17-19
24. sirithanakorn2024evidenceforendogenous pages 6-8
25. sirithanakorn2024evidenceforendogenous pages 2-4
26. pavoncello2022degradationofexogenous pages 22-23
27. wang2025pseudomonasaeruginosaacylcoa pages 3-5
28. menjivar2025characterizingthestaphylococcus pages 10-12
29. menjivar2025characterizingthestaphylococcus pages 8-10
30. landa2023exploringnovelalkanedegradation pages 1-2
31. williams2022analkanemonooxygenase pages 7-10
32. pavoncello2022degradationofexogenous pages 9-11
33. palaciosferrer2026redirectinglinearhydrocarbon pages 1-2
34. menjivar2025characterizingthestaphylococcus pages 1-2
35. menjivar2025characterizingthestaphylococcus pages 5-8
36. semini2020leishmaniaencodesa pages 3-4
37. semini2020leishmaniaencodesa pages 2-3
38. semini2020leishmaniaencodesa pages 1-2
39. palaciosferrer2026redirectinglinearhydrocarbon pages 7-11
40. williams2022anoverviewof pages 4-5
41. https://doi.org/10.3390/biom12081019,
42. https://doi.org/10.1111/mmi.14663,
43. https://doi.org/10.1128/jb.00089-25,
44. https://doi.org/10.1128/aem.01873-21,
45. https://doi.org/10.1128/aem.01428-22,
46. https://doi.org/10.3389/fmicb.2022.845551,
47. https://doi.org/10.1021/acs.accounts.3c00590,
48. https://doi.org/10.1128/mmbr.00126-24,
49. https://doi.org/10.1007/s00253-023-12413-7,
50. https://doi.org/10.1038/s41467-025-57532-z,
51. https://doi.org/10.1371/journal.pone.0309988,
52. https://doi.org/10.1128/msystems.00619-23,
53. https://doi.org/10.1016/j.jinorgbio.2021.111707,
54. https://doi.org/10.1186/s12934-025-02914-7,
55. https://doi.org/10.1128/mbio.01057-20,
56. https://doi.org/10.1093/jimb/kuac003,
57. https://doi.org/10.21203/rs.3.rs-8340431/v1,