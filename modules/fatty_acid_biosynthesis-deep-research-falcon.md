---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T21:40:46.784681'
end_time: '2026-07-06T22:06:52.741724'
duration_seconds: 1565.96
template_file: templates/module_research.md.j2
template_variables:
  module_title: Type-II fatty acid biosynthesis module
  module_summary: A bacterial type-II fatty acid synthesis boundary module covering
    formation of malonyl-CoA and malonyl-ACP, iterative acyl-ACP chain elongation,
    reduction and dehydration steps, enoyl-ACP reduction, and the unsaturated fatty-acid
    branch. For Pseudomonas putida KT2440, KEGG ppu00061 also pulls in acyl-CoA ligases
    and weak SDR/aromatic-catabolism side candidates that should be reviewed as boundary
    context rather than assumed core FAS-II enzymes.
  module_outline: "- Type-II fatty acid biosynthesis module\n  - 1. acetyl-CoA carboxylase\
    \ / malonyl-CoA formation\n  - Acetyl-CoA to malonyl-CoA\n    - Acetyl-CoA carboxylase\
    \ (molecular player: acetyl-CoA carboxylase activity; activity or role: acetyl-CoA\
    \ carboxylase activity)\n    - Biotin carboxylase (molecular player: biotin carboxylase\
    \ activity; activity or role: biotin carboxylase activity)\n  - 2. malonyl-ACP\
    \ formation\n  - Malonyl-CoA to malonyl-ACP\n    - Malonyl CoA-acyl carrier protein\
    \ transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase\
    \ activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)\n\
    \  - 3. acyl-ACP condensation\n  - 3-oxoacyl-ACP synthesis\n    - 3-oxoacyl-[acyl-carrier-protein]\
    \ synthase (molecular player: 3-oxoacyl-[acyl-carrier-protein] synthase activity;\
    \ activity or role: 3-oxoacyl-[acyl-carrier-protein] synthase activity)\n  - 4.\
    \ beta-ketoacyl-ACP reduction\n  - 3-oxoacyl-ACP to 3-hydroxyacyl-ACP\n    - 3-oxoacyl-[acyl-carrier-protein]\
    \ reductase (NADPH) (molecular player: 3-oxoacyl-[acyl-carrier-protein] reductase\
    \ (NADPH) activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] reductase\
    \ (NADPH) activity)\n  - 5. beta-hydroxyacyl-ACP dehydration\n  - 3-hydroxyacyl-ACP\
    \ to enoyl-ACP\n    - 3-hydroxyacyl-[acyl-carrier-protein] dehydratase (molecular\
    \ player: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity; activity\
    \ or role: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity)\n  - 6.\
    \ enoyl-ACP reduction\n  - Enoyl-ACP to acyl-ACP\n    - Enoyl-[acyl-carrier-protein]\
    \ reductase (NADH) (molecular player: enoyl-[acyl-carrier-protein] reductase (NADH)\
    \ activity; activity or role: enoyl-[acyl-carrier-protein] reductase (NADH) activity)\n\
    \  - 7. unsaturated fatty acid branch\n  - Unsaturated fatty acid branch\n   \
    \ - Trans-2-decenoyl-acyl-carrier-protein isomerase (molecular player: trans-2-decenoyl-acyl-carrier-protein\
    \ isomerase activity; activity or role: trans-2-decenoyl-acyl-carrier-protein\
    \ isomerase activity)"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 63
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: fatty_acid_biosynthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: fatty_acid_biosynthesis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Type-II fatty acid biosynthesis module

## Working Scope

A bacterial type-II fatty acid synthesis boundary module covering formation of malonyl-CoA and malonyl-ACP, iterative acyl-ACP chain elongation, reduction and dehydration steps, enoyl-ACP reduction, and the unsaturated fatty-acid branch. For Pseudomonas putida KT2440, KEGG ppu00061 also pulls in acyl-CoA ligases and weak SDR/aromatic-catabolism side candidates that should be reviewed as boundary context rather than assumed core FAS-II enzymes.

## Provisional Biological Outline

- Type-II fatty acid biosynthesis module
  - 1. acetyl-CoA carboxylase / malonyl-CoA formation
  - Acetyl-CoA to malonyl-CoA
    - Acetyl-CoA carboxylase (molecular player: acetyl-CoA carboxylase activity; activity or role: acetyl-CoA carboxylase activity)
    - Biotin carboxylase (molecular player: biotin carboxylase activity; activity or role: biotin carboxylase activity)
  - 2. malonyl-ACP formation
  - Malonyl-CoA to malonyl-ACP
    - Malonyl CoA-acyl carrier protein transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)
  - 3. acyl-ACP condensation
  - 3-oxoacyl-ACP synthesis
    - 3-oxoacyl-[acyl-carrier-protein] synthase (molecular player: 3-oxoacyl-[acyl-carrier-protein] synthase activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] synthase activity)
  - 4. beta-ketoacyl-ACP reduction
  - 3-oxoacyl-ACP to 3-hydroxyacyl-ACP
    - 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) (molecular player: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity)
  - 5. beta-hydroxyacyl-ACP dehydration
  - 3-hydroxyacyl-ACP to enoyl-ACP
    - 3-hydroxyacyl-[acyl-carrier-protein] dehydratase (molecular player: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity; activity or role: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity)
  - 6. enoyl-ACP reduction
  - Enoyl-ACP to acyl-ACP
    - Enoyl-[acyl-carrier-protein] reductase (NADH) (molecular player: enoyl-[acyl-carrier-protein] reductase (NADH) activity; activity or role: enoyl-[acyl-carrier-protein] reductase (NADH) activity)
  - 7. unsaturated fatty acid branch
  - Unsaturated fatty acid branch
    - Trans-2-decenoyl-acyl-carrier-protein isomerase (molecular player: trans-2-decenoyl-acyl-carrier-protein isomerase activity; activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)

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

Type-II fatty acid biosynthesis module

## Working Scope

A bacterial type-II fatty acid synthesis boundary module covering formation of malonyl-CoA and malonyl-ACP, iterative acyl-ACP chain elongation, reduction and dehydration steps, enoyl-ACP reduction, and the unsaturated fatty-acid branch. For Pseudomonas putida KT2440, KEGG ppu00061 also pulls in acyl-CoA ligases and weak SDR/aromatic-catabolism side candidates that should be reviewed as boundary context rather than assumed core FAS-II enzymes.

## Provisional Biological Outline

- Type-II fatty acid biosynthesis module
  - 1. acetyl-CoA carboxylase / malonyl-CoA formation
  - Acetyl-CoA to malonyl-CoA
    - Acetyl-CoA carboxylase (molecular player: acetyl-CoA carboxylase activity; activity or role: acetyl-CoA carboxylase activity)
    - Biotin carboxylase (molecular player: biotin carboxylase activity; activity or role: biotin carboxylase activity)
  - 2. malonyl-ACP formation
  - Malonyl-CoA to malonyl-ACP
    - Malonyl CoA-acyl carrier protein transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)
  - 3. acyl-ACP condensation
  - 3-oxoacyl-ACP synthesis
    - 3-oxoacyl-[acyl-carrier-protein] synthase (molecular player: 3-oxoacyl-[acyl-carrier-protein] synthase activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] synthase activity)
  - 4. beta-ketoacyl-ACP reduction
  - 3-oxoacyl-ACP to 3-hydroxyacyl-ACP
    - 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) (molecular player: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity)
  - 5. beta-hydroxyacyl-ACP dehydration
  - 3-hydroxyacyl-ACP to enoyl-ACP
    - 3-hydroxyacyl-[acyl-carrier-protein] dehydratase (molecular player: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity; activity or role: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity)
  - 6. enoyl-ACP reduction
  - Enoyl-ACP to acyl-ACP
    - Enoyl-[acyl-carrier-protein] reductase (NADH) (molecular player: enoyl-[acyl-carrier-protein] reductase (NADH) activity; activity or role: enoyl-[acyl-carrier-protein] reductase (NADH) activity)
  - 7. unsaturated fatty acid branch
  - Unsaturated fatty acid branch
    - Trans-2-decenoyl-acyl-carrier-protein isomerase (molecular player: trans-2-decenoyl-acyl-carrier-protein isomerase activity; activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)

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


# The Type-II Fatty Acid Biosynthesis (FAS-II) Module: A Comprehensive Review

## 1. Executive Summary

Type-II fatty acid synthesis (FAS-II) is the dissociable, multi-enzyme pathway by which bacteria, plant plastids, and mitochondria synthesize fatty acids de novo. Unlike the type-I system of animal cytoplasm and fungi—where all catalytic domains reside on a single megasynthase polypeptide—FAS-II distributes its reactions across discrete, individually encoded enzymes that share a common carrier protein, acyl carrier protein (ACP) (bibens2023areviewof pages 1-2, wedan2024mitochondrialfattyacid pages 1-2). The pathway comprises an upstream malonyl-CoA generating step catalyzed by acetyl-CoA carboxylase (ACC), a malonyl-CoA→malonyl-ACP transfer step (FabD), and an iterative four-reaction elongation cycle (condensation, β-keto reduction, dehydration, enoyl reduction), each turn of which adds two carbons to the growing acyl-ACP chain (bibens2023areviewof pages 2-5, mansilla2025fattyacidsynthesis pages 2-4). A conditional branch diverts intermediates toward unsaturated fatty acids (UFAs) in many Proteobacteria and some other lineages. The system is conserved across virtually all Bacteria, is a validated antimicrobial drug target, and presents important boundary-definition challenges when automated pathway annotation (e.g., KEGG) is applied to metabolically versatile organisms such as *Pseudomonas putida* KT2440. This review synthesizes recent mechanistic, evolutionary, and comparative data to delineate the system's core, its variants, its boundaries, and its open questions.

## 2. Definition and Biological Boundaries

### 2.1 What is included

The FAS-II module is defined as the set of ACP-dependent enzymatic reactions that convert acetyl-CoA (via malonyl-CoA/malonyl-ACP) into long-chain acyl-ACP products, which then serve as substrates for phospholipid, lipopolysaccharide, and lipoprotein biosynthesis. The core module includes eleven proteins described in *E. coli*: ACC (AccABCD), FabD, FabH, FabG, FabA, FabZ, FabI, FabB, FabF, and the ACP (bibens2023areviewof pages 37-38, bibens2023areviewof pages 1-2). In organisms with alternative enoyl-ACP reductases, FabK, FabL, or FabV replace or supplement FabI (hopf2022bacterialenoylreductasesthe pages 17-19, bibens2023areviewof pages 19-22).

### 2.2 What should be treated separately

Several enzyme classes frequently co-annotated with FAS-II in KEGG pathway maps are not core FAS-II components:

- **Acyl-CoA ligases / fatty acyl-CoA synthetases** (e.g., FadD homologs in *P. putida* KT2440: PP_0763, PP_4549, PP_4550) catalyze CoA-thioester activation of free fatty acids for β-oxidation (catabolism), not for ACP-dependent biosynthesis. They differ in chain-length preference—PP_0763 prefers C5–C10, PP_4549 accepts C6–C18, and PP_4550 prefers C6–C12—and their deletion causes FFA accumulation rather than biosynthetic failure (valencia2022engineeringpseudomonasputida pages 1-3, thompson2020fattyacidand pages 5-7).

- **SDR-family oxidoreductases** annotated in ppu00061 that belong to the short-chain dehydrogenase/reductase superfamily are often not FabG-type ketoacyl-ACP reductases. SDR membership alone is insufficient for FAS-II assignment because the superfamily encompasses thousands of proteins with only 15–30% sequence identity and diverse functions spanning steroid metabolism, xenobiotic detoxification, and aromatic catabolism (cross2021insightsintoacinetobacter pages 1-2, cross2021insightsintoacinetobacter pages 9-10).

- **β-Oxidation enzymes**, PHA synthesis enzymes (PhaG, PhaJ), and aromatic-catabolism oxidoreductases operate on CoA-linked rather than ACP-linked intermediates and should be recognized as neighboring pathways that share the acetyl-CoA/malonyl-CoA node but not the carrier chemistry of FAS-II (thompson2020fattyacidand pages 1-2, thompson2020fattyacidand pages 2-5).

## 3. Mechanistic Overview

### 3.1 Malonyl-CoA formation (Step 1)

Acetyl-CoA carboxylase (ACC) is a multisubunit biotin-dependent enzyme that catalyzes the committed step of fatty acid synthesis. The reaction proceeds in two half-reactions: (i) AccC (biotin carboxylase) uses ATP to carboxylate biotin covalently attached to AccB (biotin carboxyl carrier protein); (ii) the carboxybiotin intermediate translocates to the AccA/AccD carboxyltransferase, which transfers the carboxyl group to acetyl-CoA, producing malonyl-CoA (ito2025optimizationofmalonyl pages 4-5, mansilla2025fattyacidsynthesis pages 2-4, ito2025optimizationofmalonyl pages 2-4). This step is rate-limiting and subject to feedback regulation; in Gram-positive bacteria, malonyl-CoA levels directly control FapR-mediated transcription of FAS-II genes (mansilla2025fattyacidsynthesis pages 9-10, mansilla2025fattyacidsynthesis pages 10-12).

### 3.2 Malonyl-ACP formation (Step 2)

FabD (malonyl-CoA:ACP transacylase, EC 2.3.1.39) transfers the malonyl group from CoA to the 4′-phosphopantetheine thiol of holo-ACP, producing malonyl-ACP—the universal two-carbon donor for all subsequent elongation cycles (bibens2023areviewof pages 2-5, ostroumova2023lipidcentricapproachesin pages 8-10, ostroumova2023lipidcentricapproachesin pages 6-8). This step commits the malonyl unit to the ACP-dependent pathway and is considered obligatory in canonical FAS-II.

### 3.3 Condensation initiation (Step 3a)

The first condensation reaction is catalyzed by FabH (β-ketoacyl-ACP synthase III, KAS III), which condenses an acyl-CoA primer (typically acetyl-CoA) with malonyl-ACP, releasing CO₂ and CoA and producing acetoacetyl-ACP (bibens2023areviewof pages 2-5, mansilla2025fattyacidsynthesis pages 2-4). Crucially, this is the only condensation step that uses an acyl-CoA rather than an acyl-ACP substrate, bridging CoA-based metabolism with the ACP-based elongation cycle.

However, initiation is not universally FabH-dependent. In *Pseudomonas putida* F1, FabB (KAS I) can initiate FAS via malonyl-ACP decarboxylation, generating acetyl-ACP as a primer. This activity is significantly more efficient in *P. putida* FabB than in *E. coli* FabB, and neither of the two *P. putida* FabH paralogs (FabH1, FabH2) is essential for growth (guo2024diversityinfatty pages 4-6, guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 6-8). A dedicated malonyl-ACP decarboxylase family (MadA) also promotes FabH-independent initiation in some Proteobacteria (guo2024diversityinfatty pages 10-11).

### 3.4 Iterative elongation cycle (Steps 3b–6)

After initiation, each elongation round proceeds through four obligatory reactions:

1. **Condensation** (FabB/FabF, KAS I/II): acyl-ACP + malonyl-ACP → β-ketoacyl-ACP + ACP + CO₂. FabB and FabF extend the chain by two carbons per cycle. FabF typically handles bulk saturated elongation, while FabB has specialized roles in UFA synthesis (bibens2023areviewof pages 2-5, mansilla2025fattyacidsynthesis pages 6-9).

2. **β-Keto reduction** (FabG, EC 1.1.1.100): β-ketoacyl-ACP + NADPH → β-hydroxyacyl-ACP. FabG is a tetrameric SDR-family enzyme with a Rossmann fold. It is highly conserved and generally the only validated ketoacyl-ACP reductase in a given genome (cross2021insightsintoacinetobacter pages 5-6, bibens2023areviewof pages 14-16).

3. **Dehydration** (FabZ/FabA, EC 4.2.1.59): β-hydroxyacyl-ACP → trans-2-enoyl-ACP + H₂O. FabZ is the general dehydratase; FabA additionally catalyzes the isomerization of trans-2-decenoyl-ACP to cis-3-decenoyl-ACP, branching the pathway toward UFAs (ostroumova2023lipidcentricapproachesin pages 8-10, ostroumova2023lipidcentricapproachesin pages 6-8, dong2021acrypticlongchain pages 8-10).

4. **Enoyl reduction** (FabI/FabK/FabL/FabV): trans-2-enoyl-ACP + NAD(P)H → acyl-ACP. This thermodynamically favorable step drives the cycle forward and is the most commonly targeted step for antimicrobial inhibition (bibens2023areviewof pages 2-5, bibens2023areviewof pages 19-22).

### 3.5 Unsaturated fatty acid branch (Step 7)

In organisms such as *E. coli* and *Pseudomonas* spp. that lack aerobic desaturases for their membrane lipids, UFA synthesis is accomplished by an anaerobic branch pathway. FabA acts as a bifunctional dehydratase/isomerase: after dehydrating β-hydroxydecanoyl-ACP to trans-2-decenoyl-ACP, it isomerizes the product to cis-3-decenoyl-ACP. FabB then specifically elongates this cis-unsaturated intermediate, committing it to UFA synthesis. If cis-3-decenoyl-ACP is not elongated efficiently, it can re-isomerize to the trans form and re-enter the saturated pathway, providing a regulatory mechanism for UFA/SFA ratio control (dong2021acrypticlongchain pages 8-10).

In *P. putida* F1, the UFA branch involves additional complexity: FabF1 can elongate palmitoleyl-ACP (C16:1) to cis-vaccenoyl-ACP (C18:1), whereas FabB and FabF2 cannot perform this specific elongation (dong2021acrypticlongchain pages 8-10, dong2021acrypticlongchain pages 4-6). FabF2 is normally cryptic, under repression by a TetR-family regulator (Pput_2425), and becomes derepressed only when FabB function is lost, providing a suppressor mechanism for UFA synthesis (dong2021acrypticlongchain pages 6-8, dong2021acrypticlongchain pages 10-11).

## 4. Major Molecular Players and Active Assemblies

The following table summarizes all core FAS-II enzymes, their reactions, protein families, cofactor requirements, essentiality, and major lineage-specific variants:

| Enzyme Name | Gene(s) | EC Number | Reaction | Protein Family | Cofactors | Essentiality | Lineage Variants |
|---|---|---|---|---|---|---|---|
| Acetyl-CoA carboxylase (ACC; core) | **accA, accB, accC, accD** | 6.4.1.2 | Acetyl-CoA + HCO3− + ATP → malonyl-CoA via biotin carboxylation and carboxyl transfer | Multisubunit biotin-dependent carboxylase: AccC biotin carboxylase, AccB biotin carboxyl carrier protein, AccA/AccD carboxyltransferase | ATP, bicarbonate, biotin | Usually essential because malonyl-CoA supply gates FAS-II flux; expression/function also tied to membrane lipid homeostasis | Canonical bacterial form is multisubunit AccABCD; some proteobacteria/eukaryotes use fused-domain ACC proteins; step is core to FAS-II input but not itself an elongation-cycle enzyme (ito2025optimizationofmalonyl pages 4-5, mansilla2025fattyacidsynthesis pages 2-4, ito2025optimizationofmalonyl pages 2-4) |
| Malonyl-CoA:ACP transacylase (FabD; core) | **fabD** | 2.3.1.39 | Malonyl-CoA + holo-ACP → malonyl-ACP + CoA | Hot-dog/fatty-acid biosynthesis transacylase class | ACP prosthetic 4′-phosphopantetheine; CoA substrate/product | Generally essential in canonical bacterial FAS-II because malonyl-ACP is the committed elongation donor | Core in most bacteria; reduced FabD activity can influence exogenous fatty-acid bypass phenotypes in some Gram-positives, which is relevant to antibiotic resistance debates (bibens2023areviewof pages 2-5, ostroumova2023lipidcentricapproachesin pages 8-10, bibens2023areviewof pages 37-38, ostroumova2023lipidcentricapproachesin pages 11-12) |
| β-Ketoacyl-ACP synthase III (FabH; core initiation enzyme in many bacteria) | **fabH**; some taxa encode paralogs | 2.3.1.180 | Primer formation: acyl-CoA/acetyl-CoA + malonyl-ACP → β-ketoacyl-ACP + CO2 + CoA | Condensing enzyme, KAS III thiolase-like family | Usually none beyond catalytic Cys-His-Asn network; uses acyl-CoA and malonyl-ACP | Often essential for initiation in the canonical model, but not universally: some Proteobacteria can initiate by FabB/malonyl-ACP decarboxylation routes | Multiple FabH paralogs occur; in **Pseudomonas putida** F1 neither FabH1 nor FabH2 is strictly essential because FabB can initiate synthesis (bibens2023areviewof pages 2-5, mansilla2025fattyacidsynthesis pages 2-4, guo2024diversityinfatty pages 4-6, guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 6-8) |
| 3-Oxoacyl-ACP reductase (FabG; core) | **fabG** | 1.1.1.100 | β-ketoacyl-ACP + NADPH → β-hydroxyacyl-ACP + NADP+ | Short-chain dehydrogenase/reductase (SDR), usually tetrameric Rossmann-fold enzyme | Usually NADPH; some FabG-like proteins in other contexts prefer NADH | Commonly essential; often the only clearly validated FAS-II ketoacyl reductase in a genome | Classical low-molecular-weight FabG is core; high-molecular-weight FabG-like proteins and unrelated SDRs may be present but are often boundary/auxiliary rather than core FAS-II enzymes; catalytic-triad assignments remain under debate in E. coli FabG (cross2021insightsintoacinetobacter pages 5-6, bibens2023areviewof pages 14-16, cross2021insightsintoacinetobacter pages 4-5, hu2021escherichiacolifabg pages 7-8, cross2021insightsintoacinetobacter pages 1-2) |
| β-Hydroxyacyl-ACP dehydratase/isomerase (FabA; conditional core for UFA branch) | **fabA** | 4.2.1.59 / 5.3.3.14 | Dehydrates β-hydroxyacyl-ACP to trans-2-enoyl-ACP and, uniquely, isomerizes trans-2-decenoyl-ACP to cis-3-decenoyl-ACP | FabA/FabZ dehydratase fold; bifunctional dehydratase-isomerase | None | Essential only in organisms using the FabA/FabB anaerobic unsaturated-fatty-acid branch; not required in taxa that use desaturases or alternative routes | Core for the classical Enterobacterales-type UFA branch; in Pseudomonas the FabA branch feeds multiple KAS enzymes and strongly influences UFA/SFA ratios (ostroumova2023lipidcentricapproachesin pages 6-8, dong2021acrypticlongchain pages 8-10) |
| β-Hydroxyacyl-ACP dehydratase (FabZ; core) | **fabZ** | 4.2.1.59 | β-hydroxyacyl-ACP → trans-2-enoyl-ACP + H2O | FabA/FabZ dehydratase family | None | Usually essential for saturated-chain elongation in many bacteria, though precise essentiality can be context- and lineage-dependent | FabZ is the general dehydratase in many bacteria; FabA can overlap in dehydration chemistry but is specialized for UFA isomerization in FabA/FabB systems (bibens2023areviewof pages 2-5, ostroumova2023lipidcentricapproachesin pages 8-10, mansilla2025fattyacidsynthesis pages 6-9) |
| Enoyl-ACP reductase I (FabI; core in many lineages) | **fabI**; **inhA** in mycobacteria | 1.3.1.9 | trans-2-enoyl-ACP + NAD(P)H → acyl-ACP + NAD(P)+ | SDR enoyl reductase | Usually NADH in many annotated systems; literature often treats ENRs as nicotinamide-dependent with lineage-specific preferences | Often essential where it is the sole ENR; major validated drug target (triclosan; InhA targeted by isoniazid in mycobacteria) | Most widespread bacterial ENR; may occur alone or alongside FabK/L/V; mycobacterial homolog is InhA (hopf2022bacterialenoylreductasesthe pages 17-19, bibens2023areviewof pages 19-22, hopf2022bacterialenoylreductasesthe pages 2-4, hopf2022bacterialenoylreductasesthe pages 1-2) |
| Enoyl-ACP reductase II (FabK; variant ENR) | **fabK** | 1.3.1.9 | Same net ENR reaction as FabI | Non-SDR FMN-dependent TIM-barrel reductase | FMN; nicotinamide reductant input via mechanism distinct from FabI | Essential when sole ENR (e.g., some streptococci) but absent from many bacteria | Found in organisms such as **Streptococcus pneumoniae**, **C. difficile**, **Porphyromonas gingivalis**, and some **Enterococcus**; associated with intrinsic triclosan resistance relative to FabI systems (hopf2022bacterialenoylreductasesthe pages 17-19, bibens2023areviewof pages 19-22, hopf2022bacterialenoylreductasesthe pages 2-4, hopf2022bacterialenoylreductasesthe pages 15-17, hopf2022bacterialenoylreductasesthe pages 13-15) |
| Enoyl-ACP reductase III (FabL; variant ENR) | **fabL** (e.g., **ygaA** in B. subtilis) | 1.3.1.9 | Same net ENR reaction as FabI | SDR enoyl reductase, related to FabI | Nicotinamide cofactor | Can be important or essential depending on redundancy with FabI or other ENRs | First characterized in **Bacillus subtilis**; often co-occurs with FabI and contributes to triclosan resistance phenotypes (hopf2022bacterialenoylreductasesthe pages 17-19, hopf2022bacterialenoylreductasesthe pages 15-17, hopf2022bacterialenoylreductasesthe pages 13-15, hopf2022bacterialenoylreductasesthe pages 12-13) |
| Enoyl-ACP reductase V (FabV; variant ENR) | **fabV** | 1.3.1.9 | Same net ENR reaction as FabI | Distinct long SDR-like ENR class with PRK13656-associated domain architecture | Nicotinamide cofactor | Essential when sole ENR; otherwise can supplement FabI | Present in **Vibrio cholerae**, **Yersinia pestis**, **Pseudomonas aeruginosa**, **Burkholderia mallei**, among others; some species encode both FabI and FabV (hopf2022bacterialenoylreductasesthe pages 17-19, bibens2023areviewof pages 19-22, hopf2022bacterialenoylreductasesthe pages 12-13) |
| β-Ketoacyl-ACP synthase I (FabB; core elongation enzyme; conditional initiation/UFA enzyme) | **fabB** | 2.3.1.41 | Condenses acyl-ACP with malonyl-ACP to extend chains by 2 carbons; in some Proteobacteria also supports initiation via malonyl-ACP decarboxylation-linked chemistry | Condensing enzyme, KAS I family | None | Essential in organisms whose UFA branch depends on FabB; may also become initiation-essential in lineages where FabB substitutes for FabH | Canonical role is elongation of cis-3-decenoyl-ACP in UFA synthesis; in **P. putida** F1 FabB also initiates FAS and can be more important than FabH for primer formation (bibens2023areviewof pages 2-5, guo2024diversityinfatty pages 4-6, guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 2-4, dong2021acrypticlongchain pages 8-10) |
| β-Ketoacyl-ACP synthase II (FabF; core elongation enzyme) | **fabF**; paralogs in some taxa | 2.3.1.41 | Condenses acyl-ACP with malonyl-ACP during iterative elongation | Condensing enzyme, KAS II family | None | Usually important for bulk elongation and chain-length distribution; absolute essentiality varies by lineage and redundancy | FabF commonly handles saturated elongation; lineage-specific paralogs exist. In **P. putida** F1, FabF1 and FabF2 have distinct roles: FabF1 can elongate C16:1 to C18:1, whereas FabF2 is weaker and can cryptically support UFA synthesis when derepressed (bibens2023areviewof pages 2-5, mansilla2025fattyacidsynthesis pages 6-9, dong2021acrypticlongchain pages 8-10, dong2021acrypticlongchain pages 6-8, dong2021acrypticlongchain pages 10-11, dong2021acrypticlongchain pages 4-6) |
| Acyl carrier protein (ACP; core carrier) | **acpP** (typical bacterial ACP gene) | Not an EC-classified catalyst | Covalently carries malonyl and growing acyl intermediates via 4′-phosphopantetheine thioesters and shuttles them among FAS-II enzymes | ACP carrier-protein family | 4′-Phosphopantetheine prosthetic group attached to holo-ACP | Essential scaffold for all ACP-dependent bacterial FAS-II reactions | Universally required in canonical bacterial FAS-II, plastid FAS-II, and mtFAS; distinct from archaeal ACP-independent fatty-acid synthesis recently described (ostroumova2023lipidcentricapproachesin pages 8-10, bibens2023areviewof pages 38-39, wedan2024mitochondrialfattyacid pages 1-2, schmerling2024denovosynthesisof pages 1-4, schmerling2024denovosynthesisof pages 4-7) |


*Table: This table summarizes the core bacterial FAS-II enzymes, their reactions, families, cofactors, essentiality, and major lineage variants. It is useful for distinguishing universally conserved steps from lineage-specific replacements or conditional branches such as alternate enoyl reductases and the FabA/FabB unsaturated-fatty-acid pathway.*

## 5. Boundary Context: Non-Core Enzymes in *Pseudomonas putida* KT2440 KEGG ppu00061

When the KEGG pathway ppu00061 (fatty acid biosynthesis) is applied to *P. putida* KT2440, several genes are included that do not belong to the core ACP-dependent FAS-II module. These include acyl-CoA ligases involved in catabolic β-oxidation entry, SDR-family proteins with functions unrelated to ketoacyl-ACP reduction, and aromatic-catabolism oxidoreductases whose carbon flux converges on acetyl-CoA. The following table clarifies these boundary assignments:

| Gene Locus | Annotation | True Function | Chain-Length Preference | Core FAS-II? | Notes |
|---|---|---|---|---|---|
| PP_0763 | Fatty acyl-CoA ligase / acyl-CoA synthetase | Activates free fatty acids for β-oxidation; catabolic entry step rather than ACP-dependent de novo synthesis | Shorter-chain bias, especially C5-C10 | No | Identified in KT2440 engineering and fitness studies as part of fatty-acid degradation control; deletion helps accumulate FFAs rather than synthesize them (valencia2022engineeringpseudomonasputida pages 1-3, thompson2020fattyacidand pages 5-7) |
| PP_4549 | FadD1-like fatty acyl-CoA ligase | Major fatty-acid catabolic CoA ligase for β-oxidation initiation | Broad C6-C18 range; important for medium/long chains | No | Strong evidence from RB-TnSeq and engineering work places this enzyme in uptake/activation for degradation, not the ACP-based FAS-II cycle (valencia2022engineeringpseudomonasputida pages 1-3, thompson2020fattyacidand pages 5-7) |
| PP_4550 | Fatty acyl-CoA ligase / acyl-CoA synthetase paralog | Catabolic FA activation feeding β-oxidation | Medium-chain bias, about C6-C12 | No | Used with PP_0763 and PP_4549 to tune FFA accumulation and chain length in KT2440; boundary enzyme often captured in KEGG lipid maps because it handles fatty-acid pool interconversion (valencia2022engineeringpseudomonasputida pages 1-3) |
| PP_2213 | Acyl-CoA ligase | Activates branched-chain acid/alcohol-derived substrates for catabolism, especially 2-methylbutyrate-related metabolism | Branched short-chain substrate preference inferred | No | Included here as boundary context: clearly part of degradative CoA activation logic, not canonical FAS-II elongation (thompson2020fattyacidand pages 14-17) |
| PP_1635 | Putative acetyl-CoA synthetase regulator-associated gene | Regulatory/context role in acetate and short-chain carbon metabolism rather than FAS-II catalysis | Not established for FAS-II substrates | No | Cofitness with PP_1695 links it to acetyl-CoA/acetate control; relevant to precursor economy but not a core FAS-II enzyme (thompson2020fattyacidand pages 12-14) |
| PP_1695 | Putative acetyl-CoA synthetase regulator-associated gene | Regulatory/context role in acetate metabolism | Not established for FAS-II substrates | No | Another boundary-context gene that can appear near lipid/acetyl-CoA maps but lacks evidence for ACP-dependent fatty-acid elongation chemistry (thompson2020fattyacidand pages 12-14) |
| PP_3839 | Oxidoreductase/paralog in short-chain alcohol oxidation network | Alcohol oxidation and detoxification context feeding catabolic metabolism, not FAS-II | Short-chain alcohol-associated | No | Illustrates why oxidoreductases in KT2440 can be misread as lipid-biosynthetic; function is tied to alcohol catabolism with PedF rather than fatty-acyl-ACP reduction (thompson2020fattyacidand pages 9-12) |
| PedE / PedH | PQQ-dependent alcohol dehydrogenases | Periplasmic oxidation of alcohols; catabolic/detoxification functions that can feed fatty-acid/alcohol utilization networks | Broad alcohol substrate range | No | Important context enzymes in KT2440 carbon metabolism; not part of ACP-based fatty-acid synthesis even though downstream products may intersect β-oxidation or ester metabolism (thompson2020fattyacidand pages 9-12, thompson2020fattyacidand pages 14-17) |
| PP_0256 | Oxidoreductase (formate-responsive) | C1 detoxification/oxidation context, not fatty-acid synthesis | Not applicable | No | Example of broad-substrate oxidoreductases in KT2440 whose annotations can blur pathway boundaries; no evidence for core FAS-II role (turlin2023 source summarized in search results; no context ID available for direct citation, so included conservatively without mechanistic claim) |
| PP_4596 | Oxidoreductase (formate-responsive) | C1 detoxification/oxidation context, not fatty-acid synthesis | Not applicable | No | Similar to PP_0256: relevant to redox metabolism but not supported as a core FAS-II enzyme in the evidence assembled here; KEGG inclusion would be boundary/contextual rather than mechanistic core |
| Unspecified SDR-family candidates in ppu00061 | Short-chain dehydrogenase/reductase (SDR) family proteins | Annotation alone is insufficient; many SDRs are not FabG-like FAS-II reductases and instead serve catabolic, detoxification, or specialized metabolic roles | Often unknown until tested | Usually No | SDR superfamily membership is not enough to call a protein a FabG/FAS-II enzyme; biochemical assignment is difficult because structurally similar SDRs perform many functions (cross2021insightsintoacinetobacter pages 9-10, cross2021insightsintoacinetobacter pages 1-2) |
| Aromatic-catabolism-side oxidoreductase candidates | Aryl/alcohol/aldehyde metabolism enzymes | Catabolism of aromatics or associated intermediates; indirect relevance only through acetyl-CoA/redox supply | Substrate-specific, not FA-chain specific | No | In KT2440, pathway maps can pull in enzymes from aromatic and alcohol catabolism because carbon ultimately converges on acetyl-CoA or CoA esters, but these are neighboring systems rather than the FAS-II module itself (thompson2020fattyacidand pages 1-2, thompson2020fattyacidand pages 9-12, thompson2020fattyacidand pages 17-19) |


*Table: This table distinguishes non-core enzymes that KEGG ppu00061 may include around the Pseudomonas putida KT2440 fatty acid biosynthesis map. It is useful for separating true ACP-dependent FAS-II components from acyl-CoA ligases and broad oxidoreductases involved in fatty-acid degradation, alcohol metabolism, or other boundary pathways.*

Genome-wide functional profiling via RB-TnSeq in *P. putida* KT2440 has been particularly valuable for resolving these boundary assignments: fitness data on 13 different fatty acid substrates demonstrated specific chain-length preferences among paralogous fad genes, confirming that acyl-CoA ligases such as FadD1 (PP_4549) function in catabolism rather than biosynthesis (thompson2020fattyacidand pages 1-2, thompson2020fattyacidand pages 2-5, thompson2020fattyacidand pages 5-7).

## 6. Evolutionary and Cell-Biological Variation

### 6.1 Conservation across Bacteria

The FAS-II elongation cycle (FabG → FabZ → FabI → FabB/FabF) is nearly universal in Bacteria, making it one of the most deeply conserved metabolic modules. Acetyl-CoA carboxylase and ACP are likewise found across all bacterial phyla examined (bibens2023areviewof pages 1-2, mansilla2025fattyacidsynthesis pages 2-4). However, major variation exists in three areas:

**Enoyl-ACP reductase diversity.** While FabI (an SDR-family enzyme with a Rossmann fold) was initially considered the sole bacterial ENR, at least four structurally distinct ENR classes are now recognized: FabI, FabK (FMN-dependent TIM-barrel enzyme), FabL (SDR-related, first found in *B. subtilis*), and FabV (distinct long SDR-like class first found in *V. cholerae*). Some organisms encode only one ENR type (e.g., *S. pneumoniae* has only FabK; *Y. pestis* has only FabV), while others encode multiple (e.g., *P. aeruginosa* has both FabI and FabV; *B. subtilis* has FabI and FabL) (hopf2022bacterialenoylreductasesthe pages 17-19, bibens2023areviewof pages 19-22, hopf2022bacterialenoylreductasesthe pages 2-4, hopf2022bacterialenoylreductasesthe pages 15-17, hopf2022bacterialenoylreductasesthe pages 13-15, hopf2022bacterialenoylreductasesthe pages 12-13). Novel ENR types continue to be discovered from metagenomic surveys (hopf2022bacterialenoylreductasesthe pages 1-2).

**UFA synthesis strategies.** The FabA/FabB anaerobic branch is characteristic of many Gammaproteobacteria, but alternative UFA synthesis mechanisms include oxygen-dependent membrane desaturases (as in *B. subtilis* and many other Gram-positives) and lineage-specific variations in KAS enzyme substrate specificity (mansilla2025fattyacidsynthesis pages 6-9, dong2021acrypticlongchain pages 8-10).

**FAS initiation.** The canonical FabH-dependent initiation is not universal. *P. putida* uses FabB-mediated malonyl-ACP decarboxylation for initiation, and MadA-family decarboxylases provide yet another alternative in some Proteobacteria (guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 10-11).

### 6.2 Eukaryotic homologs: mtFAS and plastid FAS-II

Mitochondrial fatty acid synthesis (mtFAS) is orthologous to bacterial FAS-II, involving 6–7 discrete gene products catalyzing the same stepwise two-carbon extension chemistry. mtFAS is highly conserved throughout the eukaryotic kingdom and was first described in yeasts (wedan2024mitochondrialfattyacid pages 1-2). Plant plastids also harbor a complete FAS-II system inherited from the cyanobacterial endosymbiont, providing the primary source of de novo fatty acids in plant cells.

### 6.3 Archaea: a fundamentally different system

Archaea lack the canonical ACP-dependent FAS-II system. Recent work has demonstrated that Archaea such as *Sulfolobus acidocaldarius* and *Haloferax volcanii* synthesize fatty acids de novo through an ACP-independent pathway using CoA-linked intermediates. This archaeal FAS complex comprises a ketothiolase/DUF35 complex, a ketoacyl-CoA reductase, a hydroxyacyl-CoA dehydratase, and an enoyl-CoA reductase, organized into a stable protein complex mediated by the DUF35 domain protein (schmerling2024denovosynthesisof pages 1-4, schmerling2024denovosynthesisof pages 4-7, schmerling2024denovosynthesisof pages 7-9). Phylogenetic analysis reveals this capability is widespread across archaeal phyla, with frequent horizontal gene transfer events between archaeal and bacterial lineages (schmerling2024denovosynthesisof pages 9-11). These findings illuminate the "lipid divide" between archaeal isoprenoid-based and bacterial fatty acid-based membrane lipids, and they are abundant in Asgardarchaeota genomes—the presumed archaeal ancestor of eukaryotes (schmerling2024denovosynthesisof pages 11-14).

## 7. Constraints, Dependencies, and Failure Modes

### 7.1 Obligatory ordering

The elongation cycle must proceed in strict order: condensation → β-keto reduction → dehydration → enoyl reduction. Each intermediate is ACP-tethered and must be processed by the next enzyme before the subsequent step can occur. The decarboxylative condensation is thermodynamically driven by CO₂ release, while the enoyl reduction step (FabI) drives the cycle forward by rendering the last step essentially irreversible under physiological conditions (bibens2023areviewof pages 2-5, mansilla2025fattyacidsynthesis pages 6-9).

### 7.2 ACP dependence

All core FAS-II intermediates are covalently attached to ACP via the 4′-phosphopantetheine prosthetic group. This carrier dependency is what distinguishes FAS-II biosynthetic reactions from the CoA-linked reactions of β-oxidation and the recently described archaeal FAS. The ACP-binding surfaces on FabG and other FAS-II enzymes (e.g., conserved Arg residues at the active-site entrance) are critical for substrate recognition and catalysis (cross2021insightsintoacinetobacter pages 4-5).

### 7.3 Regulatory feedback

In *B. subtilis*, the FapR repressor senses malonyl-CoA (and malonyl-ACP) levels to coordinate transcription of FAS-II genes (fabHAB, fabF, fabI, fabD, plsX, plsC). Malonyl-CoA binding causes a disorder-to-order transition in FapR, converting an open ligand-binding groove into a narrow tunnel and preventing DNA binding, thereby derepressing FAS-II gene expression when the malonyl-CoA building block is available (mansilla2025fattyacidsynthesis pages 9-10, mansilla2025fattyacidsynthesis pages 10-12). In *Pseudomonas*, the DesT regulator controls fabA expression, modulating UFA synthesis in response to acyl-CoA pool composition (dong2021acrypticlongchain pages 8-10). Long-chain acyl-ACP accumulation inhibits FAS-II when phospholipid synthesis is disrupted, although the specific enzyme(s) targeted by this product inhibition remain incompletely defined (mansilla2025fattyacidsynthesis pages 10-12).

### 7.4 Exogenous fatty acid bypass

A critical constraint for antimicrobial targeting is that some Gram-positive bacteria (notably *S. aureus*) can bypass FAS-II inhibition by incorporating exogenous fatty acids from the host environment via the PlsX/PlsY/PlsC acyltransferase pathway. Mutations in FabD that reduce its activity can promote this bypass, effectively rendering FAS-II inhibitors less effective in vivo (ostroumova2023lipidcentricapproachesin pages 11-12).

## 8. Controversies and Open Questions

### 8.1 FabG catalytic mechanism

FabG has long been assigned the classical SDR catalytic triad of Ser-Tyr-Lys (S138-Y151-K155 in *E. coli*). However, Hu et al. (2021) demonstrated that *E. coli* FabG mutants lacking all three triad residues retain enzymatic activity, challenging the canonical SDR active-site model and suggesting that FabG may operate through a non-classical catalytic mechanism (hu2021escherichiacolifabg pages 7-8). This finding has broad implications for inhibitor design targeting FabG.

### 8.2 FAS-II as an antibiotic target: still viable?

The discovery that Gram-positive pathogens can scavenge host fatty acids raised concerns about FAS-II as a drug target (ostroumova2023lipidcentricapproachesin pages 11-12). However, FabI inhibitors (triclosan, isoniazid/InhA, and clinical candidates afabicin and CG400549) remain under active development, particularly for *S. aureus* and *M. tuberculosis* (bibens2023areviewof pages 1-2, bibens2023areviewof pages 37-38). The debate continues over whether the fatty acid–rich host milieu makes certain FAS-II targets ineffective in vivo, and the answer appears to be pathogen- and context-dependent.

### 8.3 Initiation pathway diversity

The extent to which FabH-independent initiation (via FabB decarboxylation or MadA) occurs beyond the Pseudomonas genus remains incompletely mapped. The functional consequences for chain-length control and primer specificity are still being elucidated (guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 10-11).

### 8.4 Annotation challenges in metabolically versatile organisms

In organisms like *P. putida* KT2440, KEGG pathway maps (ppu00061) include acyl-CoA ligases, SDR-family proteins, and aromatic-catabolism enzymes that are not part of core FAS-II but are co-annotated because they handle fatty acid or CoA-ester substrates. Genome-wide fitness profiling (RB-TnSeq) has proven essential for disambiguating biosynthetic from catabolic functions, revealing that many paralogs have specific chain-length preferences and operate in β-oxidation rather than de novo synthesis (thompson2020fattyacidand pages 1-2, thompson2020fattyacidand pages 2-5, thompson2020fattyacidand pages 17-19). SDR superfamily membership, in particular, is not diagnostic for FAS-II function because these enzymes perform diverse roles across all domains of life (cross2021insightsintoacinetobacter pages 1-2).

### 8.5 Archaeal FAS and the lipid divide

The discovery of ACP-independent de novo fatty acid synthesis in Archaea challenges the assumption that FAS-II is the universal template for fatty acid biosynthesis across prokaryotes. Whether the archaeal system represents an independent invention or shares deep ancestry with bacterial FAS-II remains unresolved, though phylogenetic evidence favors an archaeal heritage for the DUF35-associated ketothiolase complex, with evidence of horizontal gene transfer between domains (schmerling2024denovosynthesisof pages 1-4, schmerling2024denovosynthesisof pages 9-11).

## 9. Key References

1. Bibens L, Becker JP, Dassonville-Klimpt A, Sonnet P. A review of fatty acid biosynthesis enzyme inhibitors as promising antimicrobial drugs. *Pharmaceuticals*. 2023;16(3):425. doi:10.3390/ph16030425.

2. Mansilla MC, de Mendoza D. Fatty acid synthesis and utilization in gram-positive bacteria: insights from *Bacillus subtilis*. *Microbiol Mol Biol Rev*. 2025;89(2). doi:10.1128/mmbr.00069-23.

3. Hopf FSM, Roth CD, de Souza EV, et al. Bacterial enoyl-reductases: the ever-growing list of Fabs, their mechanisms and inhibition. *Front Microbiol*. 2022;13:891610. doi:10.3389/fmicb.2022.891610.

4. Guo Q, Zhong C, Dong H, Cronan JE, Wang H. Diversity in fatty acid elongation enzymes: the FabB long-chain β-ketoacyl-ACP synthase I initiates fatty acid synthesis in *Pseudomonas putida* F1. *J Biol Chem*. 2024;300(2):105600. doi:10.1016/j.jbc.2023.105600.

5. Dong H, Ma J, Chen Q, et al. A cryptic long-chain 3-ketoacyl-ACP synthase in the *Pseudomonas putida* F1 unsaturated fatty acid synthesis pathway. *J Biol Chem*. 2021;297(2):100920. doi:10.1016/j.jbc.2021.100920.

6. Cross EM, Adams FG, Waters JK, et al. Insights into *Acinetobacter baumannii* fatty acid synthesis 3-oxoacyl-ACP reductases. *Sci Rep*. 2021;11:7945. doi:10.1038/s41598-021-86400-1.

7. Hu Z, Ma J, Chen Y, et al. *Escherichia coli* FabG 3-ketoacyl-ACP reductase proteins lacking the assigned catalytic triad residues are active enzymes. *J Biol Chem*. 2021;296:100365. doi:10.1016/j.jbc.2021.100365.

8. Thompson MG, Incha MR, Pearson AN, et al. Fatty acid and alcohol metabolism in *Pseudomonas putida*: functional analysis using random barcode transposon sequencing. *Appl Environ Microbiol*. 2020;86(21). doi:10.1128/aem.01665-20.

9. Valencia LE, Incha MR, Schmidt M, et al. Engineering *Pseudomonas putida* KT2440 for chain length tailored free fatty acid and oleochemical production. *Commun Biol*. 2022;5:1438. doi:10.1038/s42003-022-04336-2.

10. Wedan RJ, Longenecker JZ, Nowinski SM. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. *Cell Metab*. 2024;36(1):36-47. doi:10.1016/j.cmet.2023.11.017.

11. Schmerling C, Zhou X, Görs PE, et al. De novo synthesis of fatty acids in Archaea via an archaeal fatty acid synthase complex. *bioRxiv*. 2024. doi:10.1101/2024.07.05.601840.

12. Ostroumova OS, Efimova SS. Lipid-centric approaches in combating infectious diseases. *Antibiotics*. 2023;12(12):1716. doi:10.3390/antibiotics12121716.

13. Ito S, Nishikawa S, Terasaka N, Fujishima K. Optimization of malonyl coenzyme A biosensors in a reconstituted cell-free system for detecting acetyl-CoA carboxylase activity. *ACS Synth Biol*. 2025. doi:10.1021/acssynbio.5c00361.


References

1. (bibens2023areviewof pages 1-2): Laurie Bibens, Jean-Paul Becker, Alexandra Dassonville-Klimpt, and Pascal Sonnet. A review of fatty acid biosynthesis enzyme inhibitors as promising antimicrobial drugs. Pharmaceuticals, 16:425, Mar 2023. URL: https://doi.org/10.3390/ph16030425, doi:10.3390/ph16030425. This article has 70 citations.

2. (wedan2024mitochondrialfattyacid pages 1-2): Riley J. Wedan, Jacob Z. Longenecker, and Sara M. Nowinski. Mitochondrial fatty acid synthesis is an emergent central regulator of mammalian oxidative metabolism. Cell Metabolism, 36:36-47, Jan 2024. URL: https://doi.org/10.1016/j.cmet.2023.11.017, doi:10.1016/j.cmet.2023.11.017. This article has 90 citations and is from a highest quality peer-reviewed journal.

3. (bibens2023areviewof pages 2-5): Laurie Bibens, Jean-Paul Becker, Alexandra Dassonville-Klimpt, and Pascal Sonnet. A review of fatty acid biosynthesis enzyme inhibitors as promising antimicrobial drugs. Pharmaceuticals, 16:425, Mar 2023. URL: https://doi.org/10.3390/ph16030425, doi:10.3390/ph16030425. This article has 70 citations.

4. (mansilla2025fattyacidsynthesis pages 2-4): María Cecilia Mansilla and Diego de Mendoza. Fatty acid synthesis and utilization in gram-positive bacteria: insights from <i>bacillus subtilis</i>. Microbiology and Molecular Biology Reviews, Jun 2025. URL: https://doi.org/10.1128/mmbr.00069-23, doi:10.1128/mmbr.00069-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

5. (bibens2023areviewof pages 37-38): Laurie Bibens, Jean-Paul Becker, Alexandra Dassonville-Klimpt, and Pascal Sonnet. A review of fatty acid biosynthesis enzyme inhibitors as promising antimicrobial drugs. Pharmaceuticals, 16:425, Mar 2023. URL: https://doi.org/10.3390/ph16030425, doi:10.3390/ph16030425. This article has 70 citations.

6. (hopf2022bacterialenoylreductasesthe pages 17-19): Fernanda S. M. Hopf, Candida D. Roth, Eduardo V. de Souza, Luiza Galina, Alexia M. Czeczot, Pablo Machado, Luiz A. Basso, and Cristiano V. Bizarro. Bacterial enoyl-reductases: the ever-growing list of fabs, their mechanisms and inhibition. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.891610, doi:10.3389/fmicb.2022.891610. This article has 28 citations and is from a peer-reviewed journal.

7. (bibens2023areviewof pages 19-22): Laurie Bibens, Jean-Paul Becker, Alexandra Dassonville-Klimpt, and Pascal Sonnet. A review of fatty acid biosynthesis enzyme inhibitors as promising antimicrobial drugs. Pharmaceuticals, 16:425, Mar 2023. URL: https://doi.org/10.3390/ph16030425, doi:10.3390/ph16030425. This article has 70 citations.

8. (valencia2022engineeringpseudomonasputida pages 1-3): Luis E. Valencia, Matthew R. Incha, Matthias Schmidt, Allison N. Pearson, Mitchell G. Thompson, Jacob B. Roberts, Marina Mehling, Kevin Yin, Ning Sun, Asun Oka, Patrick M. Shih, Lars M. Blank, John Gladden, and Jay D. Keasling. Engineering pseudomonas putida kt2440 for chain length tailored free fatty acid and oleochemical production. Communications Biology, Dec 2022. URL: https://doi.org/10.1038/s42003-022-04336-2, doi:10.1038/s42003-022-04336-2. This article has 23 citations and is from a peer-reviewed journal.

9. (thompson2020fattyacidand pages 5-7): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

10. (cross2021insightsintoacinetobacter pages 1-2): Emily M. Cross, Felise G. Adams, Jack K. Waters, David Aragão, Bart A. Eijkelkamp, and Jade K. Forwood. Insights into acinetobacter baumannii fatty acid synthesis 3-oxoacyl-acp reductases. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-86400-1, doi:10.1038/s41598-021-86400-1. This article has 26 citations and is from a peer-reviewed journal.

11. (cross2021insightsintoacinetobacter pages 9-10): Emily M. Cross, Felise G. Adams, Jack K. Waters, David Aragão, Bart A. Eijkelkamp, and Jade K. Forwood. Insights into acinetobacter baumannii fatty acid synthesis 3-oxoacyl-acp reductases. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-86400-1, doi:10.1038/s41598-021-86400-1. This article has 26 citations and is from a peer-reviewed journal.

12. (thompson2020fattyacidand pages 1-2): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

13. (thompson2020fattyacidand pages 2-5): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

14. (ito2025optimizationofmalonyl pages 4-5): Shohei Ito, Shota Nishikawa, Naohiro Terasaka, and Kosuke Fujishima. Optimization of malonyl coenzyme a biosensors in a reconstituted cell-free system for detecting acetyl-coa carboxylase activity. ACS synthetic biology, Jul 2025. URL: https://doi.org/10.1021/acssynbio.5c00361, doi:10.1021/acssynbio.5c00361. This article has 4 citations and is from a domain leading peer-reviewed journal.

15. (ito2025optimizationofmalonyl pages 2-4): Shohei Ito, Shota Nishikawa, Naohiro Terasaka, and Kosuke Fujishima. Optimization of malonyl coenzyme a biosensors in a reconstituted cell-free system for detecting acetyl-coa carboxylase activity. ACS synthetic biology, Jul 2025. URL: https://doi.org/10.1021/acssynbio.5c00361, doi:10.1021/acssynbio.5c00361. This article has 4 citations and is from a domain leading peer-reviewed journal.

16. (mansilla2025fattyacidsynthesis pages 9-10): María Cecilia Mansilla and Diego de Mendoza. Fatty acid synthesis and utilization in gram-positive bacteria: insights from <i>bacillus subtilis</i>. Microbiology and Molecular Biology Reviews, Jun 2025. URL: https://doi.org/10.1128/mmbr.00069-23, doi:10.1128/mmbr.00069-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

17. (mansilla2025fattyacidsynthesis pages 10-12): María Cecilia Mansilla and Diego de Mendoza. Fatty acid synthesis and utilization in gram-positive bacteria: insights from <i>bacillus subtilis</i>. Microbiology and Molecular Biology Reviews, Jun 2025. URL: https://doi.org/10.1128/mmbr.00069-23, doi:10.1128/mmbr.00069-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

18. (ostroumova2023lipidcentricapproachesin pages 8-10): OS Ostroumova and SS Efimova. Lipid-centric approaches in combating infectious diseases: antibacterials, antifungals and antivirals with lipid-associated mechanisms of action. Antibiotics, Dec 2023. URL: https://doi.org/10.3390/antibiotics12121716, doi:10.3390/antibiotics12121716. This article has 6 citations.

19. (ostroumova2023lipidcentricapproachesin pages 6-8): OS Ostroumova and SS Efimova. Lipid-centric approaches in combating infectious diseases: antibacterials, antifungals and antivirals with lipid-associated mechanisms of action. Antibiotics, Dec 2023. URL: https://doi.org/10.3390/antibiotics12121716, doi:10.3390/antibiotics12121716. This article has 6 citations.

20. (guo2024diversityinfatty pages 4-6): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

21. (guo2024diversityinfatty pages 1-2): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

22. (guo2024diversityinfatty pages 2-4): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

23. (guo2024diversityinfatty pages 6-8): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

24. (guo2024diversityinfatty pages 10-11): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

25. (mansilla2025fattyacidsynthesis pages 6-9): María Cecilia Mansilla and Diego de Mendoza. Fatty acid synthesis and utilization in gram-positive bacteria: insights from <i>bacillus subtilis</i>. Microbiology and Molecular Biology Reviews, Jun 2025. URL: https://doi.org/10.1128/mmbr.00069-23, doi:10.1128/mmbr.00069-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

26. (cross2021insightsintoacinetobacter pages 5-6): Emily M. Cross, Felise G. Adams, Jack K. Waters, David Aragão, Bart A. Eijkelkamp, and Jade K. Forwood. Insights into acinetobacter baumannii fatty acid synthesis 3-oxoacyl-acp reductases. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-86400-1, doi:10.1038/s41598-021-86400-1. This article has 26 citations and is from a peer-reviewed journal.

27. (bibens2023areviewof pages 14-16): Laurie Bibens, Jean-Paul Becker, Alexandra Dassonville-Klimpt, and Pascal Sonnet. A review of fatty acid biosynthesis enzyme inhibitors as promising antimicrobial drugs. Pharmaceuticals, 16:425, Mar 2023. URL: https://doi.org/10.3390/ph16030425, doi:10.3390/ph16030425. This article has 70 citations.

28. (dong2021acrypticlongchain pages 8-10): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

29. (dong2021acrypticlongchain pages 4-6): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

30. (dong2021acrypticlongchain pages 6-8): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

31. (dong2021acrypticlongchain pages 10-11): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

32. (ostroumova2023lipidcentricapproachesin pages 11-12): OS Ostroumova and SS Efimova. Lipid-centric approaches in combating infectious diseases: antibacterials, antifungals and antivirals with lipid-associated mechanisms of action. Antibiotics, Dec 2023. URL: https://doi.org/10.3390/antibiotics12121716, doi:10.3390/antibiotics12121716. This article has 6 citations.

33. (cross2021insightsintoacinetobacter pages 4-5): Emily M. Cross, Felise G. Adams, Jack K. Waters, David Aragão, Bart A. Eijkelkamp, and Jade K. Forwood. Insights into acinetobacter baumannii fatty acid synthesis 3-oxoacyl-acp reductases. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-86400-1, doi:10.1038/s41598-021-86400-1. This article has 26 citations and is from a peer-reviewed journal.

34. (hu2021escherichiacolifabg pages 7-8): Zhe Hu, Jincheng Ma, Yicai Chen, Wenhua Tong, Lei Zhu, Haihong Wang, and John E. Cronan. Escherichia coli fabg 3-ketoacyl-acp reductase proteins lacking the assigned catalytic triad residues are active enzymes. The Journal of Biological Chemistry, 296:100365, Feb 2021. URL: https://doi.org/10.1016/j.jbc.2021.100365, doi:10.1016/j.jbc.2021.100365. This article has 22 citations.

35. (hopf2022bacterialenoylreductasesthe pages 2-4): Fernanda S. M. Hopf, Candida D. Roth, Eduardo V. de Souza, Luiza Galina, Alexia M. Czeczot, Pablo Machado, Luiz A. Basso, and Cristiano V. Bizarro. Bacterial enoyl-reductases: the ever-growing list of fabs, their mechanisms and inhibition. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.891610, doi:10.3389/fmicb.2022.891610. This article has 28 citations and is from a peer-reviewed journal.

36. (hopf2022bacterialenoylreductasesthe pages 1-2): Fernanda S. M. Hopf, Candida D. Roth, Eduardo V. de Souza, Luiza Galina, Alexia M. Czeczot, Pablo Machado, Luiz A. Basso, and Cristiano V. Bizarro. Bacterial enoyl-reductases: the ever-growing list of fabs, their mechanisms and inhibition. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.891610, doi:10.3389/fmicb.2022.891610. This article has 28 citations and is from a peer-reviewed journal.

37. (hopf2022bacterialenoylreductasesthe pages 15-17): Fernanda S. M. Hopf, Candida D. Roth, Eduardo V. de Souza, Luiza Galina, Alexia M. Czeczot, Pablo Machado, Luiz A. Basso, and Cristiano V. Bizarro. Bacterial enoyl-reductases: the ever-growing list of fabs, their mechanisms and inhibition. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.891610, doi:10.3389/fmicb.2022.891610. This article has 28 citations and is from a peer-reviewed journal.

38. (hopf2022bacterialenoylreductasesthe pages 13-15): Fernanda S. M. Hopf, Candida D. Roth, Eduardo V. de Souza, Luiza Galina, Alexia M. Czeczot, Pablo Machado, Luiz A. Basso, and Cristiano V. Bizarro. Bacterial enoyl-reductases: the ever-growing list of fabs, their mechanisms and inhibition. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.891610, doi:10.3389/fmicb.2022.891610. This article has 28 citations and is from a peer-reviewed journal.

39. (hopf2022bacterialenoylreductasesthe pages 12-13): Fernanda S. M. Hopf, Candida D. Roth, Eduardo V. de Souza, Luiza Galina, Alexia M. Czeczot, Pablo Machado, Luiz A. Basso, and Cristiano V. Bizarro. Bacterial enoyl-reductases: the ever-growing list of fabs, their mechanisms and inhibition. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.891610, doi:10.3389/fmicb.2022.891610. This article has 28 citations and is from a peer-reviewed journal.

40. (bibens2023areviewof pages 38-39): Laurie Bibens, Jean-Paul Becker, Alexandra Dassonville-Klimpt, and Pascal Sonnet. A review of fatty acid biosynthesis enzyme inhibitors as promising antimicrobial drugs. Pharmaceuticals, 16:425, Mar 2023. URL: https://doi.org/10.3390/ph16030425, doi:10.3390/ph16030425. This article has 70 citations.

41. (schmerling2024denovosynthesisof pages 1-4): Christian Schmerling, Xiaoxiao Zhou, Paul E. Görs, Stephan Köstlbacher, Till Kessenbrock, David Podlesainski, David Sybers, Kun Wang, Ann-Christin Lindås, Jacky L. Snoep, Eveline Peeters, Markus Kaiser, Thijs J.G. Ettema, Sven W. Meckelmann, Christopher Bräsen, and Bettina Siebers. <i>de novo</i>synthesis of fatty acids in archaea via an archaeal fatty acid synthase complex. BioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.05.601840, doi:10.1101/2024.07.05.601840. This article has 4 citations.

42. (schmerling2024denovosynthesisof pages 4-7): Christian Schmerling, Xiaoxiao Zhou, Paul E. Görs, Stephan Köstlbacher, Till Kessenbrock, David Podlesainski, David Sybers, Kun Wang, Ann-Christin Lindås, Jacky L. Snoep, Eveline Peeters, Markus Kaiser, Thijs J.G. Ettema, Sven W. Meckelmann, Christopher Bräsen, and Bettina Siebers. <i>de novo</i>synthesis of fatty acids in archaea via an archaeal fatty acid synthase complex. BioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.05.601840, doi:10.1101/2024.07.05.601840. This article has 4 citations.

43. (thompson2020fattyacidand pages 14-17): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

44. (thompson2020fattyacidand pages 12-14): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

45. (thompson2020fattyacidand pages 9-12): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

46. (thompson2020fattyacidand pages 17-19): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

47. (schmerling2024denovosynthesisof pages 7-9): Christian Schmerling, Xiaoxiao Zhou, Paul E. Görs, Stephan Köstlbacher, Till Kessenbrock, David Podlesainski, David Sybers, Kun Wang, Ann-Christin Lindås, Jacky L. Snoep, Eveline Peeters, Markus Kaiser, Thijs J.G. Ettema, Sven W. Meckelmann, Christopher Bräsen, and Bettina Siebers. <i>de novo</i>synthesis of fatty acids in archaea via an archaeal fatty acid synthase complex. BioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.05.601840, doi:10.1101/2024.07.05.601840. This article has 4 citations.

48. (schmerling2024denovosynthesisof pages 9-11): Christian Schmerling, Xiaoxiao Zhou, Paul E. Görs, Stephan Köstlbacher, Till Kessenbrock, David Podlesainski, David Sybers, Kun Wang, Ann-Christin Lindås, Jacky L. Snoep, Eveline Peeters, Markus Kaiser, Thijs J.G. Ettema, Sven W. Meckelmann, Christopher Bräsen, and Bettina Siebers. <i>de novo</i>synthesis of fatty acids in archaea via an archaeal fatty acid synthase complex. BioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.05.601840, doi:10.1101/2024.07.05.601840. This article has 4 citations.

49. (schmerling2024denovosynthesisof pages 11-14): Christian Schmerling, Xiaoxiao Zhou, Paul E. Görs, Stephan Köstlbacher, Till Kessenbrock, David Podlesainski, David Sybers, Kun Wang, Ann-Christin Lindås, Jacky L. Snoep, Eveline Peeters, Markus Kaiser, Thijs J.G. Ettema, Sven W. Meckelmann, Christopher Bräsen, and Bettina Siebers. <i>de novo</i>synthesis of fatty acids in archaea via an archaeal fatty acid synthase complex. BioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.05.601840, doi:10.1101/2024.07.05.601840. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](fatty_acid_biosynthesis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](fatty_acid_biosynthesis-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. guo2024diversityinfatty pages 10-11
2. dong2021acrypticlongchain pages 8-10
3. valencia2022engineeringpseudomonasputida pages 1-3
4. thompson2020fattyacidand pages 14-17
5. thompson2020fattyacidand pages 12-14
6. thompson2020fattyacidand pages 9-12
7. hopf2022bacterialenoylreductasesthe pages 1-2
8. wedan2024mitochondrialfattyacid pages 1-2
9. schmerling2024denovosynthesisof pages 9-11
10. schmerling2024denovosynthesisof pages 11-14
11. cross2021insightsintoacinetobacter pages 4-5
12. mansilla2025fattyacidsynthesis pages 10-12
13. ostroumova2023lipidcentricapproachesin pages 11-12
14. hu2021escherichiacolifabg pages 7-8
15. cross2021insightsintoacinetobacter pages 1-2
16. bibens2023areviewof pages 1-2
17. bibens2023areviewof pages 2-5
18. mansilla2025fattyacidsynthesis pages 2-4
19. bibens2023areviewof pages 37-38
20. hopf2022bacterialenoylreductasesthe pages 17-19
21. bibens2023areviewof pages 19-22
22. thompson2020fattyacidand pages 5-7
23. cross2021insightsintoacinetobacter pages 9-10
24. thompson2020fattyacidand pages 1-2
25. thompson2020fattyacidand pages 2-5
26. ito2025optimizationofmalonyl pages 4-5
27. ito2025optimizationofmalonyl pages 2-4
28. mansilla2025fattyacidsynthesis pages 9-10
29. ostroumova2023lipidcentricapproachesin pages 8-10
30. ostroumova2023lipidcentricapproachesin pages 6-8
31. guo2024diversityinfatty pages 4-6
32. guo2024diversityinfatty pages 1-2
33. guo2024diversityinfatty pages 2-4
34. guo2024diversityinfatty pages 6-8
35. mansilla2025fattyacidsynthesis pages 6-9
36. cross2021insightsintoacinetobacter pages 5-6
37. bibens2023areviewof pages 14-16
38. dong2021acrypticlongchain pages 4-6
39. dong2021acrypticlongchain pages 6-8
40. dong2021acrypticlongchain pages 10-11
41. hopf2022bacterialenoylreductasesthe pages 2-4
42. hopf2022bacterialenoylreductasesthe pages 15-17
43. hopf2022bacterialenoylreductasesthe pages 13-15
44. hopf2022bacterialenoylreductasesthe pages 12-13
45. bibens2023areviewof pages 38-39
46. schmerling2024denovosynthesisof pages 1-4
47. schmerling2024denovosynthesisof pages 4-7
48. thompson2020fattyacidand pages 17-19
49. schmerling2024denovosynthesisof pages 7-9
50. acyl-carrier-protein
51. https://doi.org/10.3390/ph16030425,
52. https://doi.org/10.1016/j.cmet.2023.11.017,
53. https://doi.org/10.1128/mmbr.00069-23,
54. https://doi.org/10.3389/fmicb.2022.891610,
55. https://doi.org/10.1038/s42003-022-04336-2,
56. https://doi.org/10.1128/aem.01665-20,
57. https://doi.org/10.1038/s41598-021-86400-1,
58. https://doi.org/10.1021/acssynbio.5c00361,
59. https://doi.org/10.3390/antibiotics12121716,
60. https://doi.org/10.1016/j.jbc.2023.105600,
61. https://doi.org/10.1016/j.jbc.2021.100920,
62. https://doi.org/10.1016/j.jbc.2021.100365,
63. https://doi.org/10.1101/2024.07.05.601840,