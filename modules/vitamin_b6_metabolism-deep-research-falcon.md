---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T03:24:05.885932'
end_time: '2026-07-07T03:45:44.936552'
duration_seconds: 1299.05
template_file: templates/module_research.md.j2
template_variables:
  module_title: Vitamin B6 metabolism
  module_summary: A bacterial vitamin B6 metabolism module covering DXP-dependent
    de novo formation of pyridoxine 5'-phosphate, oxidation to pyridoxal 5'-phosphate,
    and salvage phosphorylation of B6 vitamers. In Pseudomonas putida KT2440, KEGG
    ppu00750 also includes shared precursor and amino-acid-metabolism nodes; those
    are treated as boundary context unless they directly make or salvage pyridoxal
    5'-phosphate.
  module_outline: "- Vitamin B6 metabolism\n  - 1. de novo pyridoxine 5'-phosphate\
    \ formation\n  - De novo pyridoxine phosphate formation\n    - PdxA 4-hydroxythreonine-4-phosphate\
    \ dehydrogenase (molecular player: PSEPK pdxA; activity or role: 4-hydroxythreonine-4-phosphate\
    \ dehydrogenase activity)\n    - PdxB 4-phosphoerythronate dehydrogenase (molecular\
    \ player: PSEPK pdxB; activity or role: 4-phosphoerythronate dehydrogenase activity)\n\
    \    - PdxJ pyridoxine 5'-phosphate synthase (molecular player: PSEPK pdxJ; activity\
    \ or role: pyridoxine 5'-phosphate synthase activity)\n  - 2. pyridoxal 5'-phosphate\
    \ formation\n  - Pyridoxine phosphate oxidation\n    - PdxH pyridoxamine phosphate\
    \ oxidase (molecular player: PSEPK pdxH; activity or role: pyridoxamine phosphate\
    \ oxidase activity)\n  - 3. vitamin B6 salvage phosphorylation\n  - Vitamin B6\
    \ salvage phosphorylation\n    - PdxY pyridoxal kinase (molecular player: PSEPK\
    \ pdxY; activity or role: pyridoxal kinase activity)\n  - 4. precursor and amino-acid\
    \ side context\n  - Precursor-side and PLP-enzyme context\n    - Epd erythrose-4-phosphate\
    \ dehydrogenase (molecular player: PSEPK epd; activity or role: erythrose-4-phosphate\
    \ dehydrogenase activity)\n    - SerC phosphoserine aminotransferase (molecular\
    \ player: PSEPK serC; activity or role: O-phospho-L-serine:2-oxoglutarate transaminase\
    \ activity)\n    - ThrC threonine synthase (molecular player: PSEPK thrC; activity\
    \ or role: threonine synthase activity)\n    - PP_0662 threonine synthase candidate\
    \ (molecular player: PSEPK PP_0662; activity or role: threonine synthase activity)"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: vitamin_b6_metabolism-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: vitamin_b6_metabolism-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Vitamin B6 metabolism

## Working Scope

A bacterial vitamin B6 metabolism module covering DXP-dependent de novo formation of pyridoxine 5'-phosphate, oxidation to pyridoxal 5'-phosphate, and salvage phosphorylation of B6 vitamers. In Pseudomonas putida KT2440, KEGG ppu00750 also includes shared precursor and amino-acid-metabolism nodes; those are treated as boundary context unless they directly make or salvage pyridoxal 5'-phosphate.

## Provisional Biological Outline

- Vitamin B6 metabolism
  - 1. de novo pyridoxine 5'-phosphate formation
  - De novo pyridoxine phosphate formation
    - PdxA 4-hydroxythreonine-4-phosphate dehydrogenase (molecular player: PSEPK pdxA; activity or role: 4-hydroxythreonine-4-phosphate dehydrogenase activity)
    - PdxB 4-phosphoerythronate dehydrogenase (molecular player: PSEPK pdxB; activity or role: 4-phosphoerythronate dehydrogenase activity)
    - PdxJ pyridoxine 5'-phosphate synthase (molecular player: PSEPK pdxJ; activity or role: pyridoxine 5'-phosphate synthase activity)
  - 2. pyridoxal 5'-phosphate formation
  - Pyridoxine phosphate oxidation
    - PdxH pyridoxamine phosphate oxidase (molecular player: PSEPK pdxH; activity or role: pyridoxamine phosphate oxidase activity)
  - 3. vitamin B6 salvage phosphorylation
  - Vitamin B6 salvage phosphorylation
    - PdxY pyridoxal kinase (molecular player: PSEPK pdxY; activity or role: pyridoxal kinase activity)
  - 4. precursor and amino-acid side context
  - Precursor-side and PLP-enzyme context
    - Epd erythrose-4-phosphate dehydrogenase (molecular player: PSEPK epd; activity or role: erythrose-4-phosphate dehydrogenase activity)
    - SerC phosphoserine aminotransferase (molecular player: PSEPK serC; activity or role: O-phospho-L-serine:2-oxoglutarate transaminase activity)
    - ThrC threonine synthase (molecular player: PSEPK thrC; activity or role: threonine synthase activity)
    - PP_0662 threonine synthase candidate (molecular player: PSEPK PP_0662; activity or role: threonine synthase activity)

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

Vitamin B6 metabolism

## Working Scope

A bacterial vitamin B6 metabolism module covering DXP-dependent de novo formation of pyridoxine 5'-phosphate, oxidation to pyridoxal 5'-phosphate, and salvage phosphorylation of B6 vitamers. In Pseudomonas putida KT2440, KEGG ppu00750 also includes shared precursor and amino-acid-metabolism nodes; those are treated as boundary context unless they directly make or salvage pyridoxal 5'-phosphate.

## Provisional Biological Outline

- Vitamin B6 metabolism
  - 1. de novo pyridoxine 5'-phosphate formation
  - De novo pyridoxine phosphate formation
    - PdxA 4-hydroxythreonine-4-phosphate dehydrogenase (molecular player: PSEPK pdxA; activity or role: 4-hydroxythreonine-4-phosphate dehydrogenase activity)
    - PdxB 4-phosphoerythronate dehydrogenase (molecular player: PSEPK pdxB; activity or role: 4-phosphoerythronate dehydrogenase activity)
    - PdxJ pyridoxine 5'-phosphate synthase (molecular player: PSEPK pdxJ; activity or role: pyridoxine 5'-phosphate synthase activity)
  - 2. pyridoxal 5'-phosphate formation
  - Pyridoxine phosphate oxidation
    - PdxH pyridoxamine phosphate oxidase (molecular player: PSEPK pdxH; activity or role: pyridoxamine phosphate oxidase activity)
  - 3. vitamin B6 salvage phosphorylation
  - Vitamin B6 salvage phosphorylation
    - PdxY pyridoxal kinase (molecular player: PSEPK pdxY; activity or role: pyridoxal kinase activity)
  - 4. precursor and amino-acid side context
  - Precursor-side and PLP-enzyme context
    - Epd erythrose-4-phosphate dehydrogenase (molecular player: PSEPK epd; activity or role: erythrose-4-phosphate dehydrogenase activity)
    - SerC phosphoserine aminotransferase (molecular player: PSEPK serC; activity or role: O-phospho-L-serine:2-oxoglutarate transaminase activity)
    - ThrC threonine synthase (molecular player: PSEPK thrC; activity or role: threonine synthase activity)
    - PP_0662 threonine synthase candidate (molecular player: PSEPK PP_0662; activity or role: threonine synthase activity)

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

# Bacterial Vitamin B6 Metabolism: DXP-Dependent Pyridoxal 5′-Phosphate Biosynthesis, Oxidation, and Salvage Phosphorylation

## 1. Executive Summary

Pyridoxal 5′-phosphate (PLP) is the biologically active form of vitamin B6 and an indispensable cofactor for over 140 distinct enzymatic activities, predominantly in amino acid metabolism. This review focuses on the DXP-dependent (deoxyxylulose 5-phosphate–dependent) module of vitamin B6 metabolism as represented in the gammaproteobacterium *Pseudomonas putida* KT2440 (KEGG pathway ppu00750). The module comprises three functional tiers: (i) de novo formation of pyridoxine 5′-phosphate (PNP) via a multi-step pathway requiring Epd, PdxB, SerC, PdxA, Dxs, and PdxJ; (ii) FMN-dependent oxidation of PNP to PLP by PdxH; and (iii) salvage phosphorylation of imported or recycled B6 vitamers by the kinases PdxK and PdxY. Boundary enzymes such as ThrC (threonine synthase) and the candidate PP_0662 are treated here as precursor-side context rather than core PLP-synthetic machinery. This system is the dominant de novo PLP route in Gram-negative diderm bacteria and has been best characterized in *Escherichia coli* K-12, with assignments in *P. putida* KT2440 resting principally on genome annotation and comparative inference.

## 2. Definition and Biological Boundaries

### 2.1 What is included

Vitamin B6 collectively designates six interconvertible vitamers—pyridoxine (PN), pyridoxamine (PM), pyridoxal (PL), and their 5′-phosphorylated forms PNP, PMP, and PLP (tramonti2021knownsandunknowns pages 4-5). The DXP-dependent metabolism module encompasses the enzymatic steps that produce PNP de novo from central metabolites (erythrose 4-phosphate, pyruvate, glyceraldehyde 3-phosphate), oxidize PNP to PLP, and salvage free vitamers through ATP-dependent phosphorylation. In *P. putida* KT2440, the KEGG map ppu00750 additionally annotates precursor nodes (Epd, SerC, ThrC, PP_0662) and amino-acid-metabolism connections; these are treated as boundary context unless they directly synthesize or salvage PLP.

### 2.2 What should be treated separately

Several neighboring systems are commonly conflated with the B6 module but are mechanistically distinct: (i) the DXP-independent (Pdx1/Pdx2 or PdxS/PdxT) pathway, which produces PLP directly in a single complex and is absent from *P. putida* (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 3-4); (ii) isoprenoid biosynthesis, which also consumes DXP via the MEP pathway but shares only the Dxs-catalyzed precursor step; (iii) thiamine biosynthesis, which intersects through dual-function kinase PdxK (yang1998identificationandfunction pages 5-7); and (iv) PLP-dependent enzyme networks (e.g., amino acid transaminases, decarboxylases), which consume PLP but do not synthesize it. The serine biosynthesis pathway is a notable boundary case because it shares the bifunctional enzyme SerC and the homologous dehydrogenase SerA/PdxB with the PLP pathway (tramonti2021knownsandunknowns pages 7-10, tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 5-7).

## 3. Mechanistic Overview

### 3.1 De novo pyridoxine 5′-phosphate formation

The DXP-dependent pathway converges two metabolic branches onto PdxJ, the PNP synthase. The first branch derives from erythrose 4-phosphate (E4P) of the pentose phosphate pathway and proceeds through four enzymatic steps. Epd (erythrose-4-phosphate dehydrogenase, historically GapB) catalyzes the NAD⁺-dependent oxidation of E4P to 4-phosphoerythronate (zhao1995biochemicalcharacterizationof pages 1-2). PdxB (4-phosphoerythronate dehydrogenase) then oxidizes 4-phosphoerythronate to 2-oxo-3-hydroxy-4-phosphobutanoate, again consuming NAD⁺ (tramonti2021knownsandunknowns pages 5-7). SerC (phosphoserine/phosphohydroxythreonine aminotransferase) transaminates this keto acid to 4-phosphohydroxy-L-threonine using L-glutamate as the amino-group donor—notably requiring PLP itself as a cofactor, so PLP participates in its own biosynthesis (tramonti2021knownsandunknowns pages 7-10). PdxA (4-hydroxythreonine-4-phosphate dehydrogenase) then oxidizes 4-phosphohydroxy-L-threonine to 3-amino-1-hydroxyacetone 1-phosphate (AHP), generating another equivalent of NADH (denise2023pyridoxal5’phosphatesynthesis pages 1-3).

The second branch is simpler: Dxs (1-deoxy-D-xylulose-5-phosphate synthase) condenses pyruvate and D-glyceraldehyde 3-phosphate to yield DXP (tramonti2021knownsandunknowns pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 3-4).

PdxJ then catalyzes the ring-closing condensation of DXP with AHP to form PNP, the first B6 vitamer with the characteristic pyridine ring (tramonti2021knownsandunknowns pages 10-12, tramonti2021knownsandunknowns pages 5-7). PdxJ is the signature enzyme of the DXP-dependent route and serves as the most reliable genomic marker for this pathway (denise2023pyridoxal5’phosphatesynthesis pages 1-3, denise2023pyridoxal5’phosphatesynthesis pages 3-4).

### 3.2 Oxidation of PNP to PLP

PdxH (pyridoxine/pyridoxamine 5′-phosphate oxidase) catalyzes the terminal step of de novo PLP biosynthesis: the FMN-dependent oxidation of PNP to PLP. The enzyme is a 51-kDa homodimer containing one FMN molecule per dimer (zhao1995kineticlimitationand pages 1-2, zhao1995kineticlimitationand pages 5-6). The reaction involves stereospecific removal of the pro-R hydrogen from the C4′ position of PNP, with electron transfer to the FMN isoalloxazine ring, and molecular oxygen serving as the ultimate electron acceptor to produce H₂O₂ (salvo2003structureandmechanism pages 1-2, salvo2003structureandmechanism pages 2-5, salvo2003structureandmechanism pages 5-6). Kinetic parameters reveal a relatively sluggish enzyme: Km ≈ 2 µM for PNP, with kcat values of 0.2–0.8 s⁻¹ (salvo2003structureandmechanism pages 2-5, zhao1995kineticlimitationand pages 1-2). PLP itself acts as a strong competitive inhibitor, providing intrinsic feedback regulation (zhao1995kineticlimitationand pages 2-3).

PdxH is essential for viability in *E. coli* under both aerobic and anaerobic conditions (tramonti2021knownsandunknowns pages 10-12). Under anaerobiosis, an as-yet-unidentified compound must serve as an alternative electron acceptor (tramonti2021knownsandunknowns pages 10-12, zhao1995kineticlimitationand pages 1-2). PdxH also participates in the salvage pathway by oxidizing PMP to PLP (ankisettypalli2016pdxhproteinsof pages 1-3, tramonti2021knownsandunknowns pages 10-12).

### 3.3 Vitamin B6 salvage phosphorylation

Bacteria can acquire free B6 vitamers (PL, PN, PM) from the environment or from intracellular protein turnover. Salvage proceeds through ATP-dependent phosphorylation catalyzed by two kinases with overlapping but distinct specificities. PdxK is a broad-specificity PN/PL/PM kinase that can phosphorylate all three unphosphorylated vitamers (yang1998identificationandfunction pages 1-2, yang1998identificationandfunction pages 3-4). PdxY is a PL-specific kinase with narrower substrate range and substantially lower catalytic activity—recombinant PdxY exhibits only ~1% of the kinase activity of PdxK (tramonti2021knownsandunknowns pages 12-13). Both kinases function solely in the salvage pathway; pdxK pdxY double mutants are not auxotrophic when de novo synthesis is intact (yang1998identificationandfunction pages 3-4).

Intriguingly, the preferred salvage route in *E. coli* appears to be the "detoured" pathway PL → PN → PNP → PLP (via PL reductase and PdxH oxidase) rather than direct PL → PLP phosphorylation by PdxY (tramonti2021knownsandunknowns pages 13-15, ito2022roleofthe pages 17-17). PdxK also possesses hydroxymethylpyrimidine kinase activity relevant to thiamine biosynthesis, revealing cross-talk between the B6 and B1 pathways (yang1998identificationandfunction pages 5-7).

The following table summarizes all molecular players in the module:

| Gene | Enzyme Name | EC Number | Reaction/Function | Pathway Module | Substrates | Products | Key Features |
|---|---|---:|---|---|---|---|---|
| **epd** | Erythrose-4-phosphate dehydrogenase (Epd; historically GapB in *E. coli*) | 1.2.1.- | Oxidizes D-erythrose 4-phosphate to 4-phosphoerythronate; first committed reaction of the E4P-derived branch feeding PLP synthesis | Precursor context / de novo input | D-erythrose 4-phosphate, NAD+ | 4-phosphoerythronate, NADH | Establishes the “serine-like” branch of the DXP-dependent pathway; biochemically validated in *E. coli* and widely used as the corresponding step in engineered PN production systems; in *P. putida* assignment is by comparative annotation/inference rather than pathway-specific experiment (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 7-10, zhao1995biochemicalcharacterizationof pages 1-2, wu2024multiplecofactorengineering pages 3-4) |
| **pdxB** | 4-phosphoerythronate dehydrogenase | 1.1.1.290 | Oxidizes 4-phosphoerythronate to 2-oxo-3-hydroxy-4-phosphobutanoate | De novo | 4-phosphoerythronate, NAD+ | 2-oxo-3-hydroxy-4-phosphobutanoate, NADH | Canonical second step of the DXP-dependent route; homologous to SerA, supporting an evolutionary link to serine biosynthesis; some lineages use non-orthologous replacements (e.g., PdxR) instead of canonical PdxB (tramonti2021knownsandunknowns pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 12-13) |
| **serC** | Phosphoserine/phosphohydroxythreonine aminotransferase | 2.6.1.52 | Transaminates 2-oxo-3-hydroxy-4-phosphobutanoate to 4-phosphohydroxy-L-threonine | De novo / precursor context | 2-oxo-3-hydroxy-4-phosphobutanoate, L-glutamate | 4-phosphohydroxy-L-threonine, 2-oxoglutarate | Shared enzyme between serine biosynthesis and PLP synthesis; requires PLP as cofactor, so PLP participates in its own biosynthetic route; a central example of pathway overlap and gene recruitment (tramonti2021knownsandunknowns pages 7-10, zhao1995biochemicalcharacterizationof pages 1-2, tramonti2021knownsandunknowns pages 12-13) |
| **pdxA** | 4-hydroxythreonine-4-phosphate dehydrogenase | 1.1.1.262 | Oxidizes 4-phosphohydroxy-L-threonine to 3-amino-1-hydroxyacetone 1-phosphate (AHP/PHA) | De novo | 4-phosphohydroxy-L-threonine, NAD+ | 3-amino-1-hydroxyacetone 1-phosphate, NADH | Produces the aminoacetone-phosphate branch substrate used by PdxJ; an NAD+-dependent step and a recurrent engineering bottleneck because vitamin B6 synthesis generates excess NADH (denise2023pyridoxal5’phosphatesynthesis pages 1-3, wu2024multiplecofactorengineering pages 12-14, wu2024multiplecofactorengineering pages 3-4, wu2024multiplecofactorengineering pages 1-3) |
| **dxs** | 1-deoxy-D-xylulose-5-phosphate synthase | 2.2.1.7 | Condenses pyruvate and D-glyceraldehyde 3-phosphate to make DXP | Precursor context / de novo input | Pyruvate, D-glyceraldehyde 3-phosphate | 1-deoxy-D-xylulose 5-phosphate (DXP), CO2 | Supplies the second branch substrate for PdxJ; boundary enzyme because DXP also feeds isoprenoid/thiamine metabolism, but it is part of the PLP module insofar as it directly provides the PdxJ substrate (tramonti2021knownsandunknowns pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 3-4) |
| **pdxJ** | Pyridoxine 5'-phosphate synthase (PNP synthase) | 2.6.99.2 | Condenses DXP with 3-amino-1-hydroxyacetone 1-phosphate to form pyridoxine 5'-phosphate (PNP) | De novo | DXP, 3-amino-1-hydroxyacetone 1-phosphate | Pyridoxine 5'-phosphate (PNP), phosphate, water | Signature enzyme of the DXP-dependent pathway and the clearest genomic marker for this route; obligatory in canonical DXP-dependent de novo synthesis (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 1-3, denise2023pyridoxal5’phosphatesynthesis pages 3-4) |
| **pdxH** | Pyridoxine/pyridoxamine 5'-phosphate oxidase | 1.4.3.5 | Oxidizes PNP to PLP in de novo synthesis and PMP to PLP in salvage | Oxidation / salvage convergence | PNP or PMP, FMN, O2 (aerobic) | PLP, H2O2 | FMN-dependent homodimeric oxidase; terminal step connecting de novo and salvage routes; essential in *E. coli* under aerobic and anaerobic growth, implying an unknown alternative electron acceptor in anoxia; kinetically relatively slow and strongly integrated into vitamer homeostasis (tramonti2021knownsandunknowns pages 10-12, salvo2003structureandmechanism pages 1-2, salvo2003structureandmechanism pages 2-5, zhao1995kineticlimitationand pages 1-2) |
| **pdxY** | Pyridoxal kinase II | 2.7.1.35 | ATP-dependent phosphorylation of pyridoxal (PL) to PLP | Salvage | Pyridoxal, ATP | PLP, ADP | Specialized PL kinase in *E. coli*; narrower substrate specificity than PdxK and much lower recombinant activity, but physiologically contributes to salvage; in *P. putida* likely serves the analogous salvage role by annotation (yang1998identificationandfunction pages 1-2, tramonti2021knownsandunknowns pages 12-13, yang1998identificationandfunction pages 5-7, yang1998identificationandfunction pages 3-4) |
| **pdxK** | Pyridoxal/pyridoxine/pyridoxamine kinase | 2.7.1.35 | ATP-dependent phosphorylation of PL, PN, and PM to PLP, PNP, and PMP, respectively | Salvage | Pyridoxal and/or pyridoxine and/or pyridoxamine, ATP | PLP and/or PNP and/or PMP, ADP | Broad-specificity B6 vitamer kinase; canonical salvage entry point; in some bacteria also linked to metabolic crosstalk with thiamine-related chemistry; together with PdxY defines the kinase arm of salvage (yang1998identificationandfunction pages 1-2, tramonti2021knownsandunknowns pages 4-5, tramonti2021knownsandunknowns pages 12-13, yang1998identificationandfunction pages 5-7, yang1998identificationandfunction pages 3-4) |
| **thrC** | Threonine synthase | 4.2.3.1 | Converts O-phospho-L-homoserine to L-threonine | Precursor context | O-phospho-L-homoserine | L-threonine, phosphate | Not a canonical PLP-biosynthetic enzyme, but relevant boundary context because threonine/homoserine metabolism perturbs PNP homeostasis and Thr-Ile/Val phenotypes in B6-homeostasis mutants; should usually be treated as adjacent metabolism rather than core PLP synthesis (ito2022roleofthe pages 3-4, ito2019conservedpyridoxal5phosphatebinding pages 1-3) |
| **PP_0662** | Threonine synthase candidate | 4.2.3.1 (predicted) | Putative threonine synthase-like activity | Precursor context | Presumably O-phospho-L-homoserine | Presumably L-threonine, phosphate | Included because KEGG/annotation places it near threonine-side context in *P. putida* KT2440; direct evidence linking PP_0662 to PLP metabolism was not found in the retrieved literature, so its relevance to the B6 module remains inferential and boundary-level (ito2022roleofthe pages 3-4, ito2019conservedpyridoxal5phosphatebinding pages 1-3) |


*Table: This table summarizes the core and boundary enzymes relevant to the DXP-dependent vitamin B6 metabolism module in *Pseudomonas putida* KT2440. It distinguishes obligatory de novo and salvage reactions from neighboring precursor-context enzymes, while noting where assignments are directly supported versus inferred by comparative annotation.*

## 4. Major Molecular Players and Active Assemblies

### 4.1 PdxH: the pathway gatekeeper

PdxH occupies a unique position as the convergence point between de novo and salvage routes. Structurally, each subunit contains eight antiparallel β-strands and five α-helices, with two FMN molecules bound at the dimer interface (salvo2003structureandmechanism pages 5-6). Key active-site residues include Arg197, His199, Arg133, Tyr129, Ser137, and Lys72, which form a binding pocket where His199 and Arg197 act as a "clamp" sandwiching the PLP pyridine moiety onto the FMN isoalloxazine ring during catalysis (salvo2003structureandmechanism pages 5-6). Crystal structures also reveal a noncatalytic PLP-binding site approximately 11 Å from the active site, connected by a potential tunnel, whose functional significance remains debated (salvo2003structureandmechanism pages 1-2).

### 4.2 Homeostasis proteins

Beyond the core biosynthetic and salvage enzymes, PLP homeostasis involves several regulatory proteins. YggS/PLPBP is a highly conserved PLP-binding protein that maintains low intracellular PNP levels through an incompletely understood mechanism; its deletion causes PNP hyperaccumulation and pleiotropic metabolic perturbations including inhibition of the glycine cleavage system (ito2022roleofthe pages 9-10, ito2022roleofthe pages 3-4, ito2019conservedpyridoxal5phosphatebinding pages 1-3). YigL has been recently identified as a major PNP/PLP phosphatase in *E. coli* that dephosphorylates PNP (Km ≈ 0.8 mM), providing a complementary homeostatic mechanism that becomes critical under PNP stress conditions (matsuo2024identificationofyigl pages 1-3, matsuo2024identificationofyigl pages 3-5, matsuo2024identificationofyigl pages 7-10). YbhA similarly participates in PLP dephosphorylation, and together YigL and YbhA constitute the primary phosphatases for both PNP and PLP in *E. coli* (matsuo2024identificationofyigl pages 1-3, matsuo2024identificationofyigl pages 3-5).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Two independent de novo routes

A comprehensive genomic survey of 21,114 complete bacterial and archaeal genomes identified 12,319 genomes carrying the DXP-dependent pathway and 5,505 carrying the DXP-independent (PdxS/PdxT) pathway (denise2023pyridoxal5’phosphatesynthesis pages 4-6). The DXP-dependent route is found almost exclusively in Gracilicutes (Gram-negative diderm organisms), with Cyanobacteria as the sole Terrabacteria exception (denise2023pyridoxal5’phosphatesynthesis pages 6-9). The DXP-independent route is the sole de novo pathway in Archaea and predominates in monoderm (Gram-positive) bacteria (denise2023pyridoxal5’phosphatesynthesis pages 4-6, denise2023pyridoxal5’phosphatesynthesis pages 6-9). This distribution correlates with cell-envelope structure: diderm species preferentially use the DXP-dependent route, while monoderm species preferentially use the DXP-independent route (denise2023pyridoxal5’phosphatesynthesis pages 6-9).

| Feature | DXP-Dependent Route | DXP-Independent Route |
|---|---|---|
| Signature genes | **pdxJ** is the clearest signature gene; canonical pathway commonly includes **epd, pdxB, serC, pdxA, dxs, pdxJ, pdxH** (E. coli-type) (tramonti2021knownsandunknowns pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 3-4) | **pdxS + pdxT** in bacteria; homologous **Pdx1/Pdx2** nomenclature is often used across plants/fungi and some comparative discussions (B. subtilis-type) (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 3-4) |
| Number of enzymatic steps | Multi-step pathway, classically ~7 steps from central metabolites to PLP, with PNP as an intermediate before oxidation by PdxH (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 10-12) | Direct de novo PLP synthesis by the PdxS/PdxT system, often described as a one-step or minimal two-protein route from simple precursors to PLP (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 3-4) |
| Key substrates | Two-branch input: **DXP** plus **3-amino-1-hydroxyacetone 1-phosphate (AHP/PHA)**; upstream carbon sources include **erythrose-4-phosphate, pyruvate, and glyceraldehyde-3-phosphate** (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 7-10, denise2023pyridoxal5’phosphatesynthesis pages 3-4) | **Ribose 5-phosphate or ribulose 5-phosphate**, **glyceraldehyde 3-phosphate or dihydroxyacetone phosphate**, and **glutamine** as nitrogen donor (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 3-4) |
| Product | **PNP first, then PLP** after oxidation by **PdxH** (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 3-4) | **PLP directly** (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 3-4) |
| Taxonomic distribution | Found almost exclusively in **Gracilicutes/Gram-negative diderm bacteria**; historically associated strongly with **gammaproteobacteria** (denise2023pyridoxal5’phosphatesynthesis pages 4-6, denise2023pyridoxal5’phosphatesynthesis pages 6-9) | Predominant in **Terrabacteria** and present in **all Archaea**; also present in many bacteria, fungi, and plants (denise2023pyridoxal5’phosphatesynthesis pages 4-6, tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9) |
| Genome count from Denise 2023 study (bacteria/archaea) | **12,319 genomes** carried the DXP-dependent pathway in the expanded genomic survey (denise2023pyridoxal5’phosphatesynthesis pages 4-6) | **5,505 genomes** carried the DXP-independent pathway in the same survey; this is the **only de novo route detected in Archaea** (denise2023pyridoxal5’phosphatesynthesis pages 4-6) |
| Phylogenetic pattern | Strongly associated with **diderm cell-envelope lineages**; distribution is patchier outside Gracilicutes, with Cyanobacteria noted as an exception among Terrabacteria (denise2023pyridoxal5’phosphatesynthesis pages 6-9) | Strongly associated with **monoderm lineages** and archaeal genomes; broader across non-diderm clades and eukaryotic primary literature examples (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9) |
| Known non-orthologous displacements | Documented replacements include **PdxR** replacing canonical **PdxB** in some lineages and **SerC2/sll1559** replacing canonical **SerC** activity in *Synechocystis* (denise2023pyridoxal5’phosphatesynthesis pages 4-6, denise2023pyridoxal5’phosphatesynthesis pages 3-4) | The 2023 survey emphasized multiple pathway holes and probable non-orthologous replacements in PLP synthesis generally, but the retrieved evidence gave more specific named examples for the DXP-dependent route than for canonical PdxS/PdxT replacements (denise2023pyridoxal5’phosphatesynthesis pages 1-3, denise2023pyridoxal5’phosphatesynthesis pages 9-11) |
| Evidence for horizontal transfer | Yes; **dxs, pdxA, pdxJ, pdxR** were reported on plasmids in some taxa (for example *Azospirillum*), consistent with horizontal transfer of the module (denise2023pyridoxal5’phosphatesynthesis pages 9-11) | Yes; **pdxS/pdxT** gene pairs were also identified on plasmids across diverse bacterial and archaeal taxa, supporting mobility of the minimal direct-synthesis module (denise2023pyridoxal5’phosphatesynthesis pages 9-11) |


*Table: This table compares the two known de novo pyridoxal 5'-phosphate biosynthesis strategies across life, highlighting their signature genes, substrates, phylogenetic distributions, and evolutionary features. It is useful for distinguishing the E. coli-type DXP-dependent route from the B. subtilis/PdxS-PdxT-type direct PLP synthesis route.*

### 5.2 Salvage-only organisms and pathway gaps

Approximately 1,900 organisms (~10% of those analyzed) appear to rely solely on salvage pathways without any detectable de novo synthesis genes (denise2023pyridoxal5’phosphatesynthesis pages 1-3, denise2023pyridoxal5’phosphatesynthesis pages 6-9). An additional ~848 genomes lack all detectable PLP synthesis and salvage genes entirely; these include obligate intracellular bacteria such as *Mycoplasma*, *Rickettsia*, and *Chlamydiae*, which presumably import PLP directly via as-yet-unidentified transporters (denise2023pyridoxal5’phosphatesynthesis pages 9-11).

### 5.3 Non-orthologous displacements and horizontal transfer

Significant functional plasticity exists within the DXP-dependent pathway. The canonical NAD⁺-dependent PdxB has been replaced by the FAD-dependent oxidase PdxR in *Sinorhizobium meliloti* (denise2023pyridoxal5’phosphatesynthesis pages 6-9, denise2023pyridoxal5’phosphatesynthesis pages 3-4). In *Synechocystis*, a non-homologous enzyme SerC2 (sll1559) replaces canonical SerC activity (denise2023pyridoxal5’phosphatesynthesis pages 3-4). Both de novo pathways show evidence of horizontal gene transfer: DXP-dependent pathway genes (*dxs*, *pdxA*, *pdxJ*, *pdxR*) and DXP-independent pathway genes (*pdxS/pdxT*) have been found on plasmids across diverse taxa (denise2023pyridoxal5’phosphatesynthesis pages 9-11).

### 5.4 Evolutionary origin

The DXP-dependent pathway likely evolved by gene recruitment from serine biosynthesis. PdxB is homologous to SerA (D-3-phosphoglycerate dehydrogenase), and both pathways share SerC as a common enzyme (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 5-7). A ΔpdxB mutant in *E. coli* retains the ability to slowly synthesize PLP without B6 supplementation, suggesting alternative metabolic routes can partially substitute for canonical pathway components, consistent with evolutionary flexibility in this module (tramonti2021knownsandunknowns pages 12-13). The adaptive laboratory evolution study by He et al. (2024) demonstrated that the promiscuous NAD(P)⁺-dependent succinate semialdehyde dehydrogenase (Sad) can be recruited to substitute for Epd in PLP biosynthesis through various evolutionary mechanisms including active-site mutation and gene amplification (wu2024multiplecofactorengineering pages 3-4).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory ordering

The de novo pathway imposes a strict order of operations. The E4P branch must proceed sequentially through Epd → PdxB → SerC → PdxA to generate AHP. Only then can PdxJ condense AHP with DXP to form PNP. PdxH-catalyzed oxidation to PLP is obligatorily terminal in both de novo and salvage routes (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 10-12).

### 6.2 NAD⁺/NADH cofactor constraint

A critical metabolic constraint of the DXP-dependent pathway is the stoichiometric production of NADH: each molecule of PNP produced generates three molecules of NADH (via Epd, PdxB, and PdxA), and when combined with glycolytic NADH from substrate catabolism, the total can reach approximately seven NADH per PNP from three molecules of glycerol (wu2024multiplecofactorengineering pages 1-3, wu2024multiplecofactorengineering pages 11-12). This creates a substantial reductive burden that depletes NAD⁺ pools and limits biosynthetic flux, making NADH/NAD⁺ balance a primary engineering bottleneck for vitamin B6 production (wu2024multiplecofactorengineering pages 12-14, wu2024multiplecofactorengineering pages 1-3). Multiple cofactor engineering strategies have been developed to address this, including introduction of NADH oxidase (Nox), replacement of GapA with NADPH-dependent alternatives, and rational redesign of PdxA to improve NAD⁺ binding (wu2024multiplecofactorengineering pages 12-14, wu2024multiplecofactorengineering pages 3-4, wu2024multiplecofactorengineering pages 11-12).

### 6.3 PLP and PNP toxicity

Free PLP is inherently toxic due to its reactive aldehyde group, which forms Schiff bases with primary amines and reacts with thiols. PNP can competitively inhibit PLP-dependent enzymes, including the glycine cleavage system (ito2022roleofthe pages 9-10, ito2022roleofthe pages 3-4). The cell manages this through multiple mechanisms: product inhibition of PdxH by PLP (zhao1995kineticlimitationand pages 2-3), dephosphorylation by YigL and YbhA phosphatases (matsuo2024identificationofyigl pages 1-3, matsuo2024identificationofyigl pages 3-5), and homeostatic buffering by the YggS/PLPBP carrier protein (ito2022roleofthe pages 9-10, bjorn2021vitaminb6metabolism pages 22-24).

### 6.4 PdxH essentiality and the anaerobic paradox

PdxH is essential under both aerobic and anaerobic conditions in *E. coli*, yet its characterized mechanism requires O₂ as the terminal electron acceptor. This implies an unidentified alternative electron acceptor must function under anaerobiosis—an unresolved mechanistic question (tramonti2021knownsandunknowns pages 10-12, zhao1995kineticlimitationand pages 1-2).

### 6.5 Application to *P. putida* KT2440

As a member of the Gammaproteobacteria within the Gracilicutes, *P. putida* KT2440 is predicted to employ the DXP-dependent pathway based on its genome annotation, consistent with the strong phylogenomic correlation between this pathway and diderm cell-envelope architecture (denise2023pyridoxal5’phosphatesynthesis pages 4-6, denise2023pyridoxal5’phosphatesynthesis pages 6-9). Genome-scale metabolic models of *P. putida* KT2440 include the PLP synthesis module, though biochemical validation of pathway enzymes has been limited to comparative annotation rather than organism-specific experimentation (tian2024enhancementofvitamin pages 1-2). The candidate gene PP_0662, annotated as a threonine synthase homolog, is positioned in the boundary context of the module; direct evidence linking it to PLP metabolism in *P. putida* is currently absent.

## 7. Controversies and Open Questions

**Vitamin B6 transporters.** Despite decades of research, the identity of B6 vitamer transporters remains unknown in most model bacteria including *E. coli* and *B. subtilis*. Approximately 10% of analyzed organisms appear to rely on salvage without de novo synthesis, and ~848 additional genomes lack all PLP synthesis and salvage genes, yet the transporters serving these organisms are unidentified (denise2023pyridoxal5’phosphatesynthesis pages 1-3, denise2023pyridoxal5’phosphatesynthesis pages 9-11).

**The anaerobic electron acceptor for PdxH.** The essentiality of PdxH under anaerobic conditions despite its O₂-dependent mechanism remains unexplained. Whether an alternative electron acceptor substitutes for O₂ in vivo, or whether the enzyme operates through a modified mechanism under anoxia, is an important open question (tramonti2021knownsandunknowns pages 10-12, zhao1995kineticlimitationand pages 1-2).

**PdxH moonlighting.** Recent work has revealed that PdxH and related PNP oxidase family members catalyze oxidation of damaged NAD(P) forms (6-NADH, 6-NADPH) to NAD(P)⁺, suggesting a broader metabolite-repair function beyond canonical B6 metabolism (salvo2003structureandmechanism pages 1-2). The physiological significance of this moonlighting activity remains to be fully elucidated.

**Molecular function of YggS/PLPBP.** Although deletion of YggS causes PNP accumulation and pleiotropic metabolic phenotypes, the precise biochemical mechanism by which this conserved protein maintains B6 vitamer homeostasis is still unknown (ito2022roleofthe pages 9-10, ito2022roleofthe pages 3-4, ito2019conservedpyridoxal5phosphatebinding pages 1-3).

**Gene identification gaps.** The Denise et al. (2023) genomic survey revealed that many organisms with predicted DXP-dependent pathways are missing identifiable orthologs of one or more pathway genes, either due to sequence divergence preventing homology-based detection or non-orthologous replacements that remain to be characterized (denise2023pyridoxal5’phosphatesynthesis pages 1-3, denise2023pyridoxal5’phosphatesynthesis pages 9-11).

**PLP regulation in *P. putida*.** While the existence of the pathway in *P. putida* KT2440 is well supported by genome annotation, essentially no organism-specific biochemical or regulatory data have been published for this module in this organism. Whether regulation, enzyme kinetics, or pathway integration differ significantly from the *E. coli* paradigm remains untested.

**Metabolic engineering challenges.** The NAD⁺/NADH imbalance inherent to the pathway remains a major constraint for industrial pyridoxine production, though recent cofactor engineering approaches have achieved titers of up to 1.95 g/L in fed-batch fermentation in *E. coli* (tian2024enhancementofvitamin pages 1-2). The optimal NADH/NAD⁺ ratio for maximal vitamin B6 production is still unknown (wu2024multiplecofactorengineering pages 12-14).

## 8. Key References

- Tramonti A, Nardella C, di Salvo ML, et al. Knowns and unknowns of vitamin B6 metabolism in *Escherichia coli*. *EcoSal Plus*. 2021;9(2). doi:10.1128/ecosalplus.esp-0004-2021
- Denise R, Babor J, Gerlt JA, de Crécy-Lagard V. Pyridoxal 5'-phosphate synthesis and salvage in Bacteria and Archaea: predicting pathway variant distributions and holes. *Microbial Genomics*. 2023;9(2). doi:10.1099/mgen.0.000926
- di Salvo ML, Safo MK, Musayev FN, Bossa F, Schirch V. Structure and mechanism of *Escherichia coli* pyridoxine 5′-phosphate oxidase. *BBA - Proteins and Proteomics*. 2003;1647(1-2):76-82. doi:10.1016/s1570-9639(03)00060-8
- Zhao G, Winkler ME. Kinetic limitation and cellular amount of pyridoxine (pyridoxamine) 5'-phosphate oxidase of *Escherichia coli* K-12. *J Bacteriol*. 1995;177(4):883-891. doi:10.1128/jb.177.4.883-891.1995
- Zhao G, Pease AJ, Bharani N, Winkler ME. Biochemical characterization of gapB-encoded erythrose 4-phosphate dehydrogenase of *Escherichia coli* K-12. *J Bacteriol*. 1995;177(10):2804-2812. doi:10.1128/jb.177.10.2804-2812.1995
- Yang Y, Tsui HCT, Man TK, Winkler ME. Identification and function of the pdxY gene, which encodes a novel pyridoxal kinase involved in the salvage pathway of pyridoxal 5′-phosphate biosynthesis in *Escherichia coli* K-12. *J Bacteriol*. 1998;180(7):1814-1821. doi:10.1128/jb.180.7.1814-1821.1998
- Matsuo H, Yamada N, Hemmi H, Ito T. Identification of YigL as a PLP/PNP phosphatase in *Escherichia coli*. *Appl Environ Microbiol*. 2024;90(9). doi:10.1128/aem.01270-24
- Ito T. Role of the conserved pyridoxal 5ʹ-phosphate-binding protein YggS/PLPBP in vitamin B6 and amino acid homeostasis. *Biosci Biotechnol Biochem*. 2022;86(9):1183-1191. doi:10.1093/bbb/zbac113
- Tian Z, Liu L, Wu L, et al. Enhancement of vitamin B6 production driven by omics analysis combined with fermentation optimization. *Microb Cell Fact*. 2024;23(1). doi:10.1186/s12934-024-02405-1
- Wu L, Li J, Zhang Y, et al. Multiple cofactor engineering strategies to enhance pyridoxine production in *Escherichia coli*. *Microorganisms*. 2024;12(5):933. doi:10.3390/microorganisms12050933
- He H, Gómez-Coronado PA, Zarzycki J, et al. Adaptive laboratory evolution recruits the promiscuity of succinate semialdehyde dehydrogenase to repair different metabolic deficiencies. *Nat Commun*. 2024;15. doi:10.1038/s41467-024-53156-x
- Ankisettypalli K, Cheng JJ, Baker EN, Bashiri G. PdxH proteins of mycobacteria are typical members of the classical pyridoxine/pyridoxamine 5′-phosphate oxidase family. *FEBS Lett*. 2016;590(4):453-460. doi:10.1002/1873-3468.12080

References

1. (tramonti2021knownsandunknowns pages 4-5): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

2. (tramonti2021knownsandunknowns pages 10-12): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

3. (denise2023pyridoxal5’phosphatesynthesis pages 3-4): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

4. (yang1998identificationandfunction pages 5-7): Yong Yang, Ho-Ching Tiffany Tsui, Tsz-Kwong Man, and Malcolm E. Winkler. Identification and function of the pdxy gene, which encodes a novel pyridoxal kinase involved in the salvage pathway of pyridoxal 5′-phosphate biosynthesis in escherichia coli k-12. Journal of Bacteriology, 180:1814-1821, Apr 1998. URL: https://doi.org/10.1128/jb.180.7.1814-1821.1998, doi:10.1128/jb.180.7.1814-1821.1998. This article has 141 citations and is from a peer-reviewed journal.

5. (tramonti2021knownsandunknowns pages 7-10): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

6. (tramonti2021knownsandunknowns pages 12-13): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

7. (tramonti2021knownsandunknowns pages 5-7): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

8. (zhao1995biochemicalcharacterizationof pages 1-2): Genshi Zhao, Andrew J. Pease, Nipali Bharani, and M. E. Winkler. Biochemical characterization of gapb-encoded erythrose 4-phosphate dehydrogenase of escherichia coli k-12 and its possible role in pyridoxal 5'-phosphate biosynthesis. Journal of Bacteriology, 177:2804-2812, May 1995. URL: https://doi.org/10.1128/jb.177.10.2804-2812.1995, doi:10.1128/jb.177.10.2804-2812.1995. This article has 117 citations and is from a peer-reviewed journal.

9. (denise2023pyridoxal5’phosphatesynthesis pages 1-3): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

10. (zhao1995kineticlimitationand pages 1-2): Genshi Zhao and M. Winkler. Kinetic limitation and cellular amount of pyridoxine (pyridoxamine) 5'-phosphate oxidase of escherichia coli k-12. Journal of Bacteriology, 177:883-891, Feb 1995. URL: https://doi.org/10.1128/jb.177.4.883-891.1995, doi:10.1128/jb.177.4.883-891.1995. This article has 168 citations and is from a peer-reviewed journal.

11. (zhao1995kineticlimitationand pages 5-6): Genshi Zhao and M. Winkler. Kinetic limitation and cellular amount of pyridoxine (pyridoxamine) 5'-phosphate oxidase of escherichia coli k-12. Journal of Bacteriology, 177:883-891, Feb 1995. URL: https://doi.org/10.1128/jb.177.4.883-891.1995, doi:10.1128/jb.177.4.883-891.1995. This article has 168 citations and is from a peer-reviewed journal.

12. (salvo2003structureandmechanism pages 1-2): Martino L. di Salvo, Martin K. Safo, Faik N. Musayev, Francesco Bossa, and Verne Schirch. Structure and mechanism of escherichia coli pyridoxine 5′-phosphate oxidase. Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics, 1647(1-2):76-82, Apr 2003. URL: https://doi.org/10.1016/s1570-9639(03)00060-8, doi:10.1016/s1570-9639(03)00060-8. This article has 91 citations and is from a peer-reviewed journal.

13. (salvo2003structureandmechanism pages 2-5): Martino L. di Salvo, Martin K. Safo, Faik N. Musayev, Francesco Bossa, and Verne Schirch. Structure and mechanism of escherichia coli pyridoxine 5′-phosphate oxidase. Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics, 1647(1-2):76-82, Apr 2003. URL: https://doi.org/10.1016/s1570-9639(03)00060-8, doi:10.1016/s1570-9639(03)00060-8. This article has 91 citations and is from a peer-reviewed journal.

14. (salvo2003structureandmechanism pages 5-6): Martino L. di Salvo, Martin K. Safo, Faik N. Musayev, Francesco Bossa, and Verne Schirch. Structure and mechanism of escherichia coli pyridoxine 5′-phosphate oxidase. Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics, 1647(1-2):76-82, Apr 2003. URL: https://doi.org/10.1016/s1570-9639(03)00060-8, doi:10.1016/s1570-9639(03)00060-8. This article has 91 citations and is from a peer-reviewed journal.

15. (zhao1995kineticlimitationand pages 2-3): Genshi Zhao and M. Winkler. Kinetic limitation and cellular amount of pyridoxine (pyridoxamine) 5'-phosphate oxidase of escherichia coli k-12. Journal of Bacteriology, 177:883-891, Feb 1995. URL: https://doi.org/10.1128/jb.177.4.883-891.1995, doi:10.1128/jb.177.4.883-891.1995. This article has 168 citations and is from a peer-reviewed journal.

16. (ankisettypalli2016pdxhproteinsof pages 1-3): Karthik Ankisettypalli, Jasmin Jo‐Yu Cheng, Edward N. Baker, and Ghader Bashiri. Pdxh proteins of mycobacteria are typical members of the classical pyridoxine/pyridoxamine 5′‐phosphate oxidase family. FEBS Letters, 590:453-460, Feb 2016. URL: https://doi.org/10.1002/1873-3468.12080, doi:10.1002/1873-3468.12080. This article has 17 citations and is from a peer-reviewed journal.

17. (yang1998identificationandfunction pages 1-2): Yong Yang, Ho-Ching Tiffany Tsui, Tsz-Kwong Man, and Malcolm E. Winkler. Identification and function of the pdxy gene, which encodes a novel pyridoxal kinase involved in the salvage pathway of pyridoxal 5′-phosphate biosynthesis in escherichia coli k-12. Journal of Bacteriology, 180:1814-1821, Apr 1998. URL: https://doi.org/10.1128/jb.180.7.1814-1821.1998, doi:10.1128/jb.180.7.1814-1821.1998. This article has 141 citations and is from a peer-reviewed journal.

18. (yang1998identificationandfunction pages 3-4): Yong Yang, Ho-Ching Tiffany Tsui, Tsz-Kwong Man, and Malcolm E. Winkler. Identification and function of the pdxy gene, which encodes a novel pyridoxal kinase involved in the salvage pathway of pyridoxal 5′-phosphate biosynthesis in escherichia coli k-12. Journal of Bacteriology, 180:1814-1821, Apr 1998. URL: https://doi.org/10.1128/jb.180.7.1814-1821.1998, doi:10.1128/jb.180.7.1814-1821.1998. This article has 141 citations and is from a peer-reviewed journal.

19. (tramonti2021knownsandunknowns pages 13-15): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

20. (ito2022roleofthe pages 17-17): Tomokazu Ito. Role of the conserved pyridoxal 5<tt>ʹ</tt>-phosphate-binding protein yggs/plpbp in vitamin b6 and amino acid homeostasis. Bioscience, Biotechnology, and Biochemistry, 86:1183-1191, Jul 2022. URL: https://doi.org/10.1093/bbb/zbac113, doi:10.1093/bbb/zbac113. This article has 21 citations.

21. (wu2024multiplecofactorengineering pages 3-4): Lijuan Wu, Jinlong Li, Yahui Zhang, Zhizhong Tian, Zhaoxia Jin, Linxia Liu, and Dawei Zhang. Multiple cofactor engineering strategies to enhance pyridoxine production in escherichia coli. Microorganisms, 12:933, May 2024. URL: https://doi.org/10.3390/microorganisms12050933, doi:10.3390/microorganisms12050933. This article has 6 citations.

22. (wu2024multiplecofactorengineering pages 12-14): Lijuan Wu, Jinlong Li, Yahui Zhang, Zhizhong Tian, Zhaoxia Jin, Linxia Liu, and Dawei Zhang. Multiple cofactor engineering strategies to enhance pyridoxine production in escherichia coli. Microorganisms, 12:933, May 2024. URL: https://doi.org/10.3390/microorganisms12050933, doi:10.3390/microorganisms12050933. This article has 6 citations.

23. (wu2024multiplecofactorengineering pages 1-3): Lijuan Wu, Jinlong Li, Yahui Zhang, Zhizhong Tian, Zhaoxia Jin, Linxia Liu, and Dawei Zhang. Multiple cofactor engineering strategies to enhance pyridoxine production in escherichia coli. Microorganisms, 12:933, May 2024. URL: https://doi.org/10.3390/microorganisms12050933, doi:10.3390/microorganisms12050933. This article has 6 citations.

24. (ito2022roleofthe pages 3-4): Tomokazu Ito. Role of the conserved pyridoxal 5<tt>ʹ</tt>-phosphate-binding protein yggs/plpbp in vitamin b6 and amino acid homeostasis. Bioscience, Biotechnology, and Biochemistry, 86:1183-1191, Jul 2022. URL: https://doi.org/10.1093/bbb/zbac113, doi:10.1093/bbb/zbac113. This article has 21 citations.

25. (ito2019conservedpyridoxal5phosphatebinding pages 1-3): Tomokazu Ito, Kana Yamamoto, Ran Hori, Ayako Yamauchi, Diana M. Downs, Hisashi Hemmi, and Tohru Yoshimura. Conserved pyridoxal 5'-phosphate-binding protein yggs impacts amino acid metabolism through pyridoxine 5'-phosphate in <i>escherichia coli</i>. Jun 2019. URL: https://doi.org/10.1128/aem.00430-19, doi:10.1128/aem.00430-19. This article has 49 citations and is from a peer-reviewed journal.

26. (ito2022roleofthe pages 9-10): Tomokazu Ito. Role of the conserved pyridoxal 5<tt>ʹ</tt>-phosphate-binding protein yggs/plpbp in vitamin b6 and amino acid homeostasis. Bioscience, Biotechnology, and Biochemistry, 86:1183-1191, Jul 2022. URL: https://doi.org/10.1093/bbb/zbac113, doi:10.1093/bbb/zbac113. This article has 21 citations.

27. (matsuo2024identificationofyigl pages 1-3): Hinano Matsuo, Naoki Yamada, Hisashi Hemmi, and Tomokazu Ito. Identification of yigl as a plp/pnp phosphatase in <i>escherichia coli</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01270-24, doi:10.1128/aem.01270-24. This article has 2 citations and is from a peer-reviewed journal.

28. (matsuo2024identificationofyigl pages 3-5): Hinano Matsuo, Naoki Yamada, Hisashi Hemmi, and Tomokazu Ito. Identification of yigl as a plp/pnp phosphatase in <i>escherichia coli</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01270-24, doi:10.1128/aem.01270-24. This article has 2 citations and is from a peer-reviewed journal.

29. (matsuo2024identificationofyigl pages 7-10): Hinano Matsuo, Naoki Yamada, Hisashi Hemmi, and Tomokazu Ito. Identification of yigl as a plp/pnp phosphatase in <i>escherichia coli</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01270-24, doi:10.1128/aem.01270-24. This article has 2 citations and is from a peer-reviewed journal.

30. (denise2023pyridoxal5’phosphatesynthesis pages 4-6): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

31. (denise2023pyridoxal5’phosphatesynthesis pages 6-9): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

32. (denise2023pyridoxal5’phosphatesynthesis pages 9-11): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

33. (wu2024multiplecofactorengineering pages 11-12): Lijuan Wu, Jinlong Li, Yahui Zhang, Zhizhong Tian, Zhaoxia Jin, Linxia Liu, and Dawei Zhang. Multiple cofactor engineering strategies to enhance pyridoxine production in escherichia coli. Microorganisms, 12:933, May 2024. URL: https://doi.org/10.3390/microorganisms12050933, doi:10.3390/microorganisms12050933. This article has 6 citations.

34. (bjorn2021vitaminb6metabolism pages 22-24): Richts Björn. Vitamin B6 metabolism and underground metabolic routes in the Gram-positive bacterium Bacillus subtilis. PhD thesis, University Goettingen Repository, 2021. URL: https://doi.org/10.53846/goediss-8736, doi:10.53846/goediss-8736.

35. (tian2024enhancementofvitamin pages 1-2): Zhizhong Tian, Linxia Liu, Lijuan Wu, Zixuan Yang, Yahui Zhang, Liping Du, and Dawei Zhang. Enhancement of vitamin b6 production driven by omics analysis combined with fermentation optimization. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02405-1, doi:10.1186/s12934-024-02405-1. This article has 23 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](vitamin_b6_metabolism-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](vitamin_b6_metabolism-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. tramonti2021knownsandunknowns pages 4-5
2. yang1998identificationandfunction pages 5-7
3. zhao1995biochemicalcharacterizationof pages 1-2
4. tramonti2021knownsandunknowns pages 5-7
5. tramonti2021knownsandunknowns pages 7-10
6. zhao1995kineticlimitationand pages 2-3
7. tramonti2021knownsandunknowns pages 10-12
8. tramonti2021knownsandunknowns pages 12-13
9. yang1998identificationandfunction pages 3-4
10. salvo2003structureandmechanism pages 5-6
11. salvo2003structureandmechanism pages 1-2
12. wu2024multiplecofactorengineering pages 3-4
13. tian2024enhancementofvitamin pages 1-2
14. wu2024multiplecofactorengineering pages 12-14
15. zhao1995kineticlimitationand pages 1-2
16. zhao1995kineticlimitationand pages 5-6
17. salvo2003structureandmechanism pages 2-5
18. ankisettypalli2016pdxhproteinsof pages 1-3
19. yang1998identificationandfunction pages 1-2
20. tramonti2021knownsandunknowns pages 13-15
21. ito2022roleofthe pages 17-17
22. wu2024multiplecofactorengineering pages 1-3
23. ito2022roleofthe pages 3-4
24. ito2022roleofthe pages 9-10
25. matsuo2024identificationofyigl pages 1-3
26. matsuo2024identificationofyigl pages 3-5
27. matsuo2024identificationofyigl pages 7-10
28. wu2024multiplecofactorengineering pages 11-12
29. https://doi.org/10.1128/ecosalplus.esp-0004-2021,
30. https://doi.org/10.1099/mgen.0.000926,
31. https://doi.org/10.1128/jb.180.7.1814-1821.1998,
32. https://doi.org/10.1128/jb.177.10.2804-2812.1995,
33. https://doi.org/10.1128/jb.177.4.883-891.1995,
34. https://doi.org/10.1016/s1570-9639(03
35. https://doi.org/10.1002/1873-3468.12080,
36. https://doi.org/10.1093/bbb/zbac113,
37. https://doi.org/10.3390/microorganisms12050933,
38. https://doi.org/10.1128/aem.00430-19,
39. https://doi.org/10.1128/aem.01270-24,
40. https://doi.org/10.53846/goediss-8736,
41. https://doi.org/10.1186/s12934-024-02405-1,