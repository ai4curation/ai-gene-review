---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T19:11:34.734318'
end_time: '2026-07-06T19:41:26.787817'
duration_seconds: 1792.05
template_file: templates/module_research.md.j2
template_variables:
  module_title: Pentose and glucuronate interconversions
  module_summary: A boundary module for the sugar-acid and pentose interconversion
    reactions grouped by bacterial KEGG pentose/glucuronate maps. The map connects
    phosphorylated pentose metabolism, UDP-glucose/UDP-glucuronate generation, and
    uronate or aldarate degradation side chemistry. Organism-level curation should
    distinguish strict pentose-phosphate reactions, nucleotide-sugar biosynthesis,
    and candidate uronate-catabolic dehydratase/aldolase/dehydrogenase steps rather
    than treating every mapped enzyme as evidence for one complete linear pathway.
  module_outline: "- Pentose and glucuronate interconversions\n  - 1. pentose-phosphate\
    \ interconversion\n  - Ribulose 5-phosphate to xylulose 5-phosphate\n    - Ribulose-phosphate\
    \ 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity\
    \ or role: ribulose-phosphate 3-epimerase activity)\n  - 2. UDP-glucose supply\n\
    \  - Glucose 1-phosphate to UDP-glucose\n    - UDP-glucose pyrophosphorylase (molecular\
    \ player: UTP:glucose-1-phosphate uridylyltransferase activity; activity or role:\
    \ UTP:glucose-1-phosphate uridylyltransferase activity)\n  - 3. UDP-glucuronate\
    \ formation\n  - UDP-glucose to UDP-glucuronate\n    - UDP-glucose 6-dehydrogenase\
    \ (molecular player: UDP-glucose 6-dehydrogenase activity; activity or role: UDP-glucose\
    \ 6-dehydrogenase activity)\n  - 4. 2,5-dioxovalerate oxidation\n  - 2,5-dioxovalerate\
    \ oxidation\n    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate\
    \ dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase\
    \ (NADP+) activity)"
  module_connections: '- Glucose 1-phosphate to UDP-glucose feeds into UDP-glucose
    to UDP-glucuronate: UDP-glucose is the substrate for UDP-glucose 6-dehydrogenase.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 54
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: pentose_glucuronate_interconversions-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: pentose_glucuronate_interconversions-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Pentose and glucuronate interconversions

## Working Scope

A boundary module for the sugar-acid and pentose interconversion reactions grouped by bacterial KEGG pentose/glucuronate maps. The map connects phosphorylated pentose metabolism, UDP-glucose/UDP-glucuronate generation, and uronate or aldarate degradation side chemistry. Organism-level curation should distinguish strict pentose-phosphate reactions, nucleotide-sugar biosynthesis, and candidate uronate-catabolic dehydratase/aldolase/dehydrogenase steps rather than treating every mapped enzyme as evidence for one complete linear pathway.

## Provisional Biological Outline

- Pentose and glucuronate interconversions
  - 1. pentose-phosphate interconversion
  - Ribulose 5-phosphate to xylulose 5-phosphate
    - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity or role: ribulose-phosphate 3-epimerase activity)
  - 2. UDP-glucose supply
  - Glucose 1-phosphate to UDP-glucose
    - UDP-glucose pyrophosphorylase (molecular player: UTP:glucose-1-phosphate uridylyltransferase activity; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)
  - 3. UDP-glucuronate formation
  - UDP-glucose to UDP-glucuronate
    - UDP-glucose 6-dehydrogenase (molecular player: UDP-glucose 6-dehydrogenase activity; activity or role: UDP-glucose 6-dehydrogenase activity)
  - 4. 2,5-dioxovalerate oxidation
  - 2,5-dioxovalerate oxidation
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

## Known Relationships Among Steps

- Glucose 1-phosphate to UDP-glucose feeds into UDP-glucose to UDP-glucuronate: UDP-glucose is the substrate for UDP-glucose 6-dehydrogenase.

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

Pentose and glucuronate interconversions

## Working Scope

A boundary module for the sugar-acid and pentose interconversion reactions grouped by bacterial KEGG pentose/glucuronate maps. The map connects phosphorylated pentose metabolism, UDP-glucose/UDP-glucuronate generation, and uronate or aldarate degradation side chemistry. Organism-level curation should distinguish strict pentose-phosphate reactions, nucleotide-sugar biosynthesis, and candidate uronate-catabolic dehydratase/aldolase/dehydrogenase steps rather than treating every mapped enzyme as evidence for one complete linear pathway.

## Provisional Biological Outline

- Pentose and glucuronate interconversions
  - 1. pentose-phosphate interconversion
  - Ribulose 5-phosphate to xylulose 5-phosphate
    - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity or role: ribulose-phosphate 3-epimerase activity)
  - 2. UDP-glucose supply
  - Glucose 1-phosphate to UDP-glucose
    - UDP-glucose pyrophosphorylase (molecular player: UTP:glucose-1-phosphate uridylyltransferase activity; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)
  - 3. UDP-glucuronate formation
  - UDP-glucose to UDP-glucuronate
    - UDP-glucose 6-dehydrogenase (molecular player: UDP-glucose 6-dehydrogenase activity; activity or role: UDP-glucose 6-dehydrogenase activity)
  - 4. 2,5-dioxovalerate oxidation
  - 2,5-dioxovalerate oxidation
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

## Known Relationships Among Steps

- Glucose 1-phosphate to UDP-glucose feeds into UDP-glucose to UDP-glucuronate: UDP-glucose is the substrate for UDP-glucose 6-dehydrogenase.

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

# Pentose and Glucuronate Interconversions: A Review of Scope, Mechanism, and Variation

## 1. Executive Summary

The KEGG "pentose and glucuronate interconversions" map (ko00040) aggregates three functionally distinct metabolic sub-modules under a single heading: (i) pentose-phosphate interconversion reactions centered on ribulose-phosphate 3-epimerase and the non-oxidative pentose phosphate pathway (PPP); (ii) nucleotide-sugar biosynthesis connecting glucose-1-phosphate via UDP-glucose pyrophosphorylase (GalU) and UDP-glucose 6-dehydrogenase (UGDH) to the UDP-glucuronate hub; and (iii) uronate and pentose catabolism through oxidative non-phosphorylative routes including Weimberg, Dahms, and related pathways that process sugar acids via dehydratase–aldolase–dehydrogenase cascades. A critical principle for organism-level curation is that the presence of enzymes mapping to a single KEGG entry does not demonstrate a complete linear pathway: the sub-modules operate under different regulatory logics, occupy different cellular compartments, and vary independently across lineages. This review explains how the parts fit together, where they diverge, and what curation pitfalls arise from treating the map as a unified pathway.

## 2. Definition and Biological Boundaries

### 2.1 What the system includes

The pentose and glucuronate interconversion module, as defined by KEGG map ko00040, encompasses reactions that interconvert pentose sugars, uronic acids, and their phosphorylated or nucleotide-activated derivatives. The obligatory core consists of three biochemically separable reaction clusters:

**Sub-module 1: Pentose-phosphate interconversion.** The reversible epimerization of ribulose-5-phosphate (Ru5P) to xylulose-5-phosphate (Xu5P) by ribulose-phosphate 3-epimerase (RPE, EC 5.1.3.1) represents the canonical pentose-phosphate interconversion step. RPE is a highly conserved metalloenzyme adopting a TIM-barrel fold, with 64–90% sequence identity across photosynthetic organisms, and an acid-base catalytic mechanism operating through a cis-ene-diolate intermediate stabilized by conserved His/Asp residues and a divalent metal ion (meloni2023ribulose15bisphosphateregenerationin pages 4-5). This enzyme is amphibolic: in the Calvin-Benson-Bassham cycle it generates Xu5P for ribulose-1,5-bisphosphate regeneration, while in the non-oxidative PPP it equilibrates C5 sugar phosphates for nucleotide and amino acid biosynthesis (meloni2023ribulose15bisphosphateregenerationin pages 4-5, meloni2023ribulose15bisphosphateregenerationin pages 1-2).

**Sub-module 2: Nucleotide-sugar biosynthesis (UDP-glucose → UDP-glucuronate axis).** UDP-glucose pyrophosphorylase (GalU/UGPase, EC 2.7.7.9) catalyzes the reversible formation of UDP-glucose from glucose-1-phosphate and UTP (choi2025uridineasa pages 6-7, choi2025uridineasa pages 7-8). This activated sugar nucleotide is then irreversibly oxidized to UDP-glucuronate by UGDH (EC 1.1.1.22), an NAD⁺-dependent cytosolic oxidoreductase that functions optimally as a homohexamer (trimer of dimers) (zimmer2021integrationofsugar pages 1-2, zimmer2021integrationofsugar pages 10-11). The UDP-glucose → UDP-glucuronate conversion is the metabolic commitment step that diverts hexose carbon from glycogen synthesis and glycolysis toward uronic acid-dependent biosynthetic pathways including glycosaminoglycan synthesis, proteoglycan assembly, glucuronidation reactions, and plant cell-wall polysaccharide biosynthesis (zimmer2021integrationofsugar pages 1-2, choi2025uridineasa pages 7-8).

**Sub-module 3: Uronate catabolism and non-phosphorylative pentose degradation.** This sub-module encompasses the degradation of free uronic acids (D-glucuronate, D-galacturonate) and the oxidative non-phosphorylative catabolism of pentoses via the Weimberg and Dahms pathways. In the Weimberg pathway, pentoses are oxidized to pentonic acids, dehydrated to 2-keto-3-deoxy-pentonate (KDP), and then further dehydrated to α-ketoglutarate semialdehyde (2,5-dioxovalerate), which is oxidized to α-ketoglutarate by 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2). In the Dahms variant, KDP is instead cleaved by an aldolase to pyruvate and glycolaldehyde (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10).

### 2.2 What should be treated separately

Several neighboring pathways are often confused with the pentose/glucuronate interconversion module:

- **The oxidative pentose phosphate pathway** (glucose-6-phosphate dehydrogenase, 6-phosphogluconate dehydrogenase) generates NADPH and feeds C5 intermediates into the non-oxidative PPP but is mechanistically and regulatorily distinct from the interconversion reactions per se.
- **Glycosaminoglycan biosynthesis** and **proteoglycan assembly** in the Golgi consume UDP-glucuronate and UDP-xylose but are downstream biosynthetic pathways, not interconversion chemistry.
- **Glucuronidation** (UDP-glucuronosyltransferases in the ER) represents a disposal pathway for xenobiotics and endogenous substrates using UDP-glucuronate as a donor, but is a phase II metabolic detoxification process.
- **The Leloir pathway of galactose metabolism** shares UDP-glucose as an intermediate but proceeds through UDP-galactose 4-epimerase rather than UGDH.

## 3. Mechanistic Overview

### 3.1 The obligatory UDP-glucose → UDP-glucuronate axis

The best-characterized obligatory sequence in the nucleotide-sugar sub-module proceeds as follows: glucose-1-phosphate is activated to UDP-glucose by GalU/UGPase, consuming UTP (choi2025uridineasa pages 6-7). UDP-glucose is then oxidized by UGDH through a two-step NAD⁺-dependent mechanism involving covalent thiohemiacetal and thioester enzyme intermediates at the active-site cysteine (Cys276), with Lys220 and Asp280 serving as critical catalytic residues (zimmer2021integrationofsugar pages 10-11). The hexameric enzyme samples three conformational sub-states: an active hexamer (E), an inactive hexamer (E*), and a UDP-xylose-inhibited hexamer (EΩ), with an allosteric switch centered on the Thr131 loop and α6 helix controlling transitions between these states (zimmer2021integrationofsugar pages 4-6). An intrinsically disordered C-terminal tail (residues 465–494) further modulates the enzyme's energetic landscape and correlates with UDP-xylose affinity (zimmer2021integrationofsugar pages 4-6).

UDP-glucuronate produced by UGDH serves as the substrate for UDP-glucuronate decarboxylase (UXS1, EC 4.1.1.35), which catalyzes an irreversible decarboxylation to generate UDP-xylose (li2023comprehensiveanalysisof pages 1-2, zimmer2021integrationofsugar pages 6-7). Crucially, UDP-xylose acts as a potent allosteric inhibitor of UGDH, binding at the UDP-glucose site and stabilizing the inactive EΩ state (zimmer2021integrationofsugar pages 6-7). This creates a negative feedback circuit: UGDH makes UDP-glucuronate, UXS converts it to UDP-xylose, and UDP-xylose inhibits UGDH. Loss of UXS1 causes approximately 70-fold accumulation of UDP-glucuronate in cell models, demonstrating the importance of this regulatory circuit (doshi2023identifyingvulnerabilitiesin pages 78-84).

### 3.2 Conditional and accessory steps

The pentose-phosphate interconversion catalyzed by RPE is a conditional step in this system: it is obligatory for organisms that rely on the non-oxidative PPP for pentose sugar utilization (and is core to the Calvin cycle in autotrophs) but is not part of the nucleotide-sugar biosynthesis axis (meloni2023ribulose15bisphosphateregenerationin pages 4-5, garschagen2021analternativepentose pages 3-5). Similarly, the uronate catabolic enzymes are conditional: 2,5-dioxovalerate dehydrogenase is obligatory only for organisms that route pentose carbon through the complete Weimberg pathway to α-ketoglutarate, and is dispensable in organisms that use the Dahms aldolytic cleavage instead (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2).

## 4. Major Molecular Players and Active Assemblies

The following table summarizes the principal enzymes, organized by functional sub-module:

| Enzyme | EC number | Reaction catalyzed | Sub-module | Structural features | Evolutionary conservation | Regulatory / systems features |
|---|---|---|---|---|---|---|
| Ribulose-phosphate 3-epimerase (RPE; ribulose-5-phosphate 3-epimerase) | 5.1.3.1 | Ribulose-5-phosphate ⇌ xylulose-5-phosphate | Pentose-phosphate interconversion | Highly conserved metalloenzyme; TIM-barrel / (β/α)8-barrel fold; active site uses conserved His/Asp residues and a metal ion to stabilize a cis-ene-diolate intermediate; domain closure reported in structural studies (meloni2023ribulose15bisphosphateregenerationin pages 4-5, meloni2023ribulose15bisphosphateregenerationin pages 12-12, meloni2023ribulose15bisphosphateregenerationin pages 11-12) | Broadly distributed across bacteria, archaea, and eukaryotes; amphibolic enzyme in photosynthetic eukaryotes and core PPP enzyme in bacteria; high sequence conservation in photosynthetic lineages (meloni2023ribulose15bisphosphateregenerationin pages 4-5, sutter2020pentosedegradationin pages 1-2, sutter2020pentosedegradationin pages 10-13) | Reversible node linking non-oxidative PPP to Calvin-cycle-like chemistry and alternative SBPP routing; oxidative damage sensitivity has been noted in some systems, with manganese protection reported; indispensable in alternative transaldolase-bypass pentose metabolism because it supplies Xu5P from Ru5P (meloni2023ribulose15bisphosphateregenerationin pages 4-5, meloni2023ribulose15bisphosphateregenerationin pages 12-12, garschagen2021analternativepentose pages 3-5, garschagen2021analternativepentose pages 8-10) |
| UDP-glucose pyrophosphorylase (GalU / UGPase) | 2.7.7.9 | Glucose-1-phosphate + UTP ⇌ UDP-glucose + PPi | Nucleotide-sugar biosynthesis (UDP-glucose supply) | Exact quaternary structure varies by lineage; catalyzes uridylyl transfer to form activated sugar nucleotide; central entry point from hexose-phosphate metabolism into UDP-sugar pools (choi2025uridineasa pages 6-7, choi2025uridineasa pages 7-8) | Widespread across bacteria and eukaryotes, but the physiological outputs differ by lineage: bacterial envelope/exopolysaccharide metabolism versus eukaryotic glycosylation and storage pathways (choi2025uridineasa pages 6-7, choi2025uridineasa pages 7-8) | Functionally couples central carbon metabolism to nucleotide-sugar biosynthesis; in bacteria often inferred to affect cell-envelope and virulence traits, but organism-specific evidence is required; should be treated as evidence for UDP-glucose supply, not by itself for complete glucuronate or uronate pathways (choi2025uridineasa pages 6-7, choi2025uridineasa pages 7-8) |
| UDP-glucose 6-dehydrogenase (UGDH) | 1.1.1.22 | UDP-glucose + 2 NAD+ + H2O → UDP-glucuronate + 2 NADH + 2 H+ | Nucleotide-sugar biosynthesis (UDP-glucose → UDP-glucuronate axis) | Cytosolic oxidoreductase; maximal activity as homohexamer (trimer of dimers); dynamic equilibrium among dimer/tetramer/hexamer states; catalytic cysteine-dependent two-step oxidation via thiohemiacetal and thioester intermediates; allosteric switch centered on Thr131 loop/α6 helix; intrinsically disordered C-terminal tail modulates conformational landscape (zimmer2021integrationofsugar pages 10-11, zimmer2021integrationofsugar pages 2-4, zimmer2021integrationofsugar pages 4-6) | Broadly conserved in animals and many bacteria; essential for UDP-glucuronate supply to glycosaminoglycans/proteoglycans in metazoans and for downstream sugar-acid pathways more generally (zimmer2021integrationofsugar pages 1-2, zhang2023udpglucuronatemetabolismcontrols pages 1-2, hengel2020lossoffunctionmutationsin pages 1-2) | Regulated by substrate/cofactor supply, product inhibition, and strong feedback by UDP-xylose; negative cooperativity, hysteresis, and assembly-state control are documented; clinically relevant missense variants disrupt stability/oligomerization/activity; in mammalian liver, UDP-glucuronate made by UGDH directly inhibits RIPK1 signaling, linking this metabolic step to NASH pathology (zimmer2021integrationofsugar pages 9-10, zimmer2021integrationofsugar pages 6-7, zhang2023udpglucuronatemetabolismcontrols pages 8-9, hengel2020lossoffunctionmutationsin pages 8-8, zimmer2021integrationofsugar pages 2-4) |
| UDP-glucuronate decarboxylase (UXS / UDP-xylose synthase) | 4.1.1.35 | UDP-glucuronate → UDP-xylose + CO2 | Nucleotide-sugar biosynthesis / branch from UDP-glucuronate | Multiple isoforms in plants; both membrane-associated/Golgi-localized and cytosolic forms described depending on lineage/protein; NtUXS16 localized to medial Golgi with unusual topology relative to classic type II Golgi proteins (li2023comprehensiveanalysisof pages 9-12, li2023comprehensiveanalysisof pages 1-2) | Conserved in eukaryotic glycan/cell-wall pathways; in animals and plants it drains UDP-glucuronate toward UDP-xylose-dependent glycoconjugate synthesis (li2023comprehensiveanalysisof pages 9-12, li2023comprehensiveanalysisof pages 1-2, zimmer2021integrationofsugar pages 6-7) | Major control point for UDP-glucuronate partitioning; product UDP-xylose is a potent allosteric inhibitor of UGDH, so UXS creates a feedback branch that both consumes UDP-glucuronate and generates the UGDH inhibitor; loss of UXS activity causes large UDP-glucuronate accumulation in cell models (doshi2023identifyingvulnerabilitiesin pages 147-152, zimmer2021integrationofsugar pages 6-7, doshi2023identifyingvulnerabilitiesin pages 78-84) |
| Xylose dehydrogenase (XylB/XylD-type, depending lineage) | 1.1.1.- | D-xylose + NAD(P)+ → D-xylonolactone (then hydrolyzed to D-xylonate) | Uronate/pentose catabolism (non-phosphorylative pathways) | Oxidative entry enzyme of Weimberg/Dahms pathways; distinct from phosphorylative xylose isomerase route; cofactor-dependent soluble dehydrogenase (francois2020engineeringmicrobialpathways pages 4-5, kopp2020enzymologyofalternative pages 10-12, kopp2020enzymologyofalternative pages 8-10) | Found in diverse bacteria and some archaea/fungi engineered or naturally using oxidative pentose catabolism; not universal among pentose utilizers (francois2020engineeringmicrobialpathways pages 4-5, kopp2020enzymologyofalternative pages 8-10, kopp2020enzymologyofalternative pages 10-12) | Entry step for oxidative pentose catabolism; pathway performance can be constrained by dehydrogenase product inhibition and NAD+ recycling; presence indicates non-phosphorylative potential but not necessarily whether carbon flows through Weimberg, Dahms, or other KDP-processing variants (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 10-12) |
| Xylonate dehydratase | 4.2.1.- | D-xylonate → 2-keto-3-deoxy-D-xylonate (KDX/KDP) | Uronate/pentose catabolism (non-phosphorylative pathways) | Family diversity is high: bacterial and archaeal enzymes belong to different superfamilies (IlvD/EDD versus enolase-type solutions in some systems); often a pathway bottleneck in reconstructions and engineering (kopp2020enzymologyofalternative pages 10-12) | Distributed across oxidative pentose pathways in bacteria and archaea, but homologous replacements occur; enzyme family usage is not strictly conserved across domains (kopp2020enzymologyofalternative pages 8-10, kopp2020enzymologyofalternative pages 10-12) | Frequently rate-limiting in vitro and in vivo pathway optimization; sensitive balancing against upstream/downstream activities is required; should be interpreted as evidence for oxidative pentose chemistry, not automatically for full α-ketoglutarate-yielding flux (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 10-12) |
| 2-keto-3-deoxy-pentonate dehydratase (KDP dehydratase; KdxD/KdpD) | 4.2.1.- | 2-keto-3-deoxy-pentonate → 2,5-dioxovalerate / α-ketoglutarate semialdehyde + H2O | Uronate/pentose catabolism (Weimberg branch) | Biochemically characterized D- and L-stereospecific enzymes exist; Mg2+ dependence/stability effects reported for some D-KdpD enzymes; catalytically distinct from the alternative KDP aldolases of Dahms-type pathways (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10, watanabe2019novelnonphosphorylativepathway pages 1-2) | Present in bacteria and archaea using Weimberg-type oxidative pentose degradation, but not in organisms routing KDP primarily through aldol cleavage; lineage-specific replacements and stereochemical specialization occur (ren2022structureandfunction pages 1-2, watanabe2019novelnonphosphorylativepathway pages 1-2, kopp2020enzymologyofalternative pages 10-12) | Key branch-defining enzyme: its presence favors α-ketoglutarate-semialdehyde / 2,5-dioxovalerate production rather than direct pyruvate + glycolaldehyde formation; enzyme identity is therefore crucial for curation of pathway completeness (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) |
| 2,5-dioxovalerate dehydrogenase (α-ketoglutarate semialdehyde dehydrogenase) | 1.2.1.26 | 2,5-dioxovalerate / α-ketoglutarate semialdehyde + NAD(P)+ + H2O → α-ketoglutarate + NAD(P)H + H+ | Uronate/pentose catabolism (terminal oxidative step of Weimberg-like routes) | Soluble aldehyde dehydrogenase-type enzyme acting downstream of KDP dehydratase; completes conversion of oxidative pentose intermediates into TCA-cycle carbon (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2) | Occurs in organisms using Weimberg-type routes; absent or dispensable in Dahms-type cleavage routes that stop at pyruvate/glycolaldehyde (francois2020engineeringmicrobialpathways pages 4-5, kopp2020enzymologyofalternative pages 8-10, watanabe2019novelnonphosphorylativepathway pages 1-2) | Obligatory for full Weimberg flux to α-ketoglutarate; if missing, KDP chemistry may instead feed Dahms or alternative non-phosphorylative branches, so annotation should not infer this step from upstream oxidative enzymes alone (francois2020engineeringmicrobialpathways pages 4-5, watanabe2019novelnonphosphorylativepathway pages 1-2) |
| KDP aldolase (Dahms-pathway comparator) | 4.1.2.- | 2-keto-3-deoxy-pentonate → pyruvate + glycolaldehyde | Uronate/pentose catabolism (Dahms branch; included as branch-defining comparator) | Aldolase distinct from KDP dehydratase; determines cleavage rather than oxidation of KDP intermediate (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) | Present in bacteria using Dahms-type oxidative pentose degradation; not a universal companion to oxidative entry enzymes (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10, watanabe2019novelnonphosphorylativepathway pages 1-2) | Important for curation because the same upstream xylose dehydrogenase/xylonate dehydratase pair can feed either Dahms or Weimberg outcomes; downstream gene content is therefore decisive (francois2020engineeringmicrobialpathways pages 4-5, kopp2020enzymologyofalternative pages 8-10) |


*Table: This table organizes the principal enzymes in pentose and glucuronate interconversions into pentose-phosphate, nucleotide-sugar, and non-phosphorylative catabolic sub-modules. It highlights why pathway curation should distinguish shared entry reactions from branch-defining downstream enzymes and regulatory nodes.*

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Variation across pentose metabolic route types

A striking feature of the pentose/glucuronate interconversion map is the diversity of route types that different organisms employ to metabolize pentoses. The following table compares the major pathway variants:

| Pathway type | Domain / lineage distribution | Key distinguishing enzymes | End-product entering central metabolism | RPE involved? | Key references |
|---|---|---|---|---|---|
| Phosphorylative / isomerase | Common in bacteria; also present in some archaea such as *Halorhabdus* via likely horizontal acquisition; functionally connected to the non-oxidative pentose phosphate pathway (PPP) rather than oxidative pentose degradation (sutter2020pentosedegradationin pages 1-2, sutter2020pentosedegradationin pages 10-13, kopp2020enzymologyofalternative pages 8-10) | Xylose isomerase, xylulokinase, ribose-5-phosphate isomerase, ribulose-5-phosphate 3-epimerase, transketolase, transaldolase (or alternatives) (sutter2020pentosedegradationin pages 1-2, sutter2020pentosedegradationin pages 10-13, meloni2023ribulose15bisphosphateregenerationin pages 4-5) | D-xylulose-5-phosphate (or equivalent pentose phosphates), then glycolytic intermediates via PPP (sutter2020pentosedegradationin pages 10-13, ren2022structureandfunction pages 1-2) | Yes; RPE converts ribulose-5-phosphate to xylulose-5-phosphate and is a core PPP node (meloni2023ribulose15bisphosphateregenerationin pages 4-5, sutter2020pentosedegradationin pages 10-13) | Sutter 2020; Meloni 2023 (sutter2020pentosedegradationin pages 1-2, sutter2020pentosedegradationin pages 10-13, meloni2023ribulose15bisphosphateregenerationin pages 4-5) |
| Phosphorylative / oxo-reductive | Characteristic of fungi and yeasts; less typical for bacteria; presented as the major alternative to the bacterial isomerase route in lignocellulose-utilizing eukaryotic microbes (kopp2020enzymologyofalternative pages 8-10) | Xylose reductase, xylitol dehydrogenase, xylulokinase; downstream non-oxidative PPP enzymes including transketolase/transaldolase and usually RPE indirectly through PPP equilibration (kopp2020enzymologyofalternative pages 8-10) | D-xylulose-5-phosphate feeding PPP and glycolysis (kopp2020enzymologyofalternative pages 8-10) | Usually yes indirectly, because carbon enters the PPP as xylulose-5-phosphate and equilibrates through RPE-containing pentose-phosphate interconversion reactions; however RPE is not the pathway-defining entry enzyme (meloni2023ribulose15bisphosphateregenerationin pages 4-5, kopp2020enzymologyofalternative pages 8-10) | Kopp 2020; Zhao 2020 (kopp2020enzymologyofalternative pages 8-10) |
| Weimberg oxidative | Found in diverse bacteria and some archaea; also introduced into fungi by engineering; often used in biomass-conversion studies (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10, kopp2020enzymologyofalternative pages 10-12) | Pentose dehydrogenase, lactonase, pentonate dehydratase, 2-keto-3-deoxy-pentonate dehydratase, 2,5-dioxovalerate / α-ketoglutarate semialdehyde dehydrogenase (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 10-12) | α-Ketoglutarate via α-ketoglutarate semialdehyde / 2,5-dioxovalerate (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) | No for the core route; this pathway bypasses pentose-phosphate interconversion at entry and oxidizes free pentoses directly (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2) | Francois 2020; Ren 2022; Kopp 2020 (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 10-12) |
| Dahms oxidative | Found in bacteria using oxidative non-phosphorylative pentose catabolism; often discussed with Weimberg because both share upstream oxidation steps but diverge at the KDP intermediate (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) | Pentose dehydrogenase, lactonase, pentonate dehydratase, 2-keto-3-deoxy-pentonate aldolase (instead of KDP dehydratase) (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) | Pyruvate + glycolaldehyde (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) | No for the core route; carbon does not first pass through ribulose-5-phosphate / xylulose-5-phosphate PPP interconversion (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) | Ren 2022; Kopp 2020; Domingues 2021 (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10) |
| Novel non-phosphorylative Route III | Reported in bacteria such as *Herbaspirillum huttiense*; distinct from canonical Weimberg and Dahms routes and not evolutionarily identical to analogous archaeal pathways (watanabe2019novelnonphosphorylativepathway pages 1-2, watanabe2019novelnonphosphorylativepathway pages 6-7) | Aldose 1-dehydrogenase, lactonase, acid-sugar dehydratase, then dehydrogenase and hydrolase steps acting on 2-keto-3-deoxypentonate (KDP) (watanabe2019novelnonphosphorylativepathway pages 1-2, watanabe2019novelnonphosphorylativepathway pages 6-7) | Mixed outputs: α-ketoglutarate, pyruvate, and glycolate depending branch chemistry (watanabe2019novelnonphosphorylativepathway pages 1-2, watanabe2019novelnonphosphorylativepathway pages 6-7) | No for the defining catabolic route; pathway is built around oxidative KDP chemistry rather than PPP epimerization (watanabe2019novelnonphosphorylativepathway pages 1-2, watanabe2019novelnonphosphorylativepathway pages 6-7) | Watanabe 2019 (watanabe2019novelnonphosphorylativepathway pages 1-2, watanabe2019novelnonphosphorylativepathway pages 6-7) |
| Sedoheptulose-1,7-bisphosphate pathway (SBPP) | Found in gut bacteria lacking transaldolase, notably *Prevotella copri*; distributed across several bacterial phyla; resembles regenerative Calvin-cycle chemistry more than canonical bacterial PPP wiring (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 12-13, garschagen2021analternativepentose pages 1-2, garschagen2021analternativepentose pages 10-12) | Ribose-5-phosphate isomerase, ribulose-5-phosphate 3-epimerase, transketolase, PPi-dependent or ATP-dependent phosphofructokinase acting on sedoheptulose-7-phosphate, fructose-bisphosphate aldolase (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 3-5, garschagen2021analternativepentose pages 8-10) | Glyceraldehyde-3-phosphate + dihydroxyacetone phosphate / erythrose-4-phosphate equivalents linking to glycolysis and biosynthesis (garschagen2021analternativepentose pages 3-5, garschagen2021analternativepentose pages 12-13) | Yes; RPE is essential because it generates xylulose-5-phosphate from ribulose-5-phosphate upstream of transketolase and the SBPP bypass (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 3-5, garschagen2021analternativepentose pages 8-10) | Garschagen 2021 (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 3-5, garschagen2021analternativepentose pages 12-13, garschagen2021analternativepentose pages 1-2) |


*Table: This table compares the major pentose metabolic route types across lineages and highlights the enzymes and outputs that distinguish them. It is useful for showing why a single KEGG pentose/glucuronate map can conflate PPP interconversion, oxidative pentose degradation, and lineage-specific bypass solutions.*

### 5.2 Cross-domain variation in pentose degradation

In bacteria, pentoses are most commonly phosphorylated to D-xylulose-5-phosphate through isomerase-kinase sequences that feed the non-oxidative PPP (sutter2020pentosedegradationin pages 1-2, kopp2020enzymologyofalternative pages 8-10). Many archaea, by contrast, employ oxidative non-phosphorylative pathways that produce α-ketoglutarate (as in *Haloferax volcanii* and *Sulfolobus* species) (sutter2020pentosedegradationin pages 1-2, kopp2020enzymologyofalternative pages 8-10, watanabe2019novelnonphosphorylativepathway pages 1-2). A notable exception is the haloarchaeal genus *Halorhabdus*, which uses bacterial-type phosphorylative pentose degradation pathways, likely acquired through horizontal gene transfer from bacteria (sutter2020pentosedegradationin pages 1-2, sutter2020pentosedegradationin pages 10-13). This acquisition may be explained by incomplete gluconeogenesis in *Halorhabdus* species that prevents effective anabolic utilization of α-ketoglutarate (sutter2020pentosedegradationin pages 13-14).

Importantly, functionally analogous enzymes in bacterial and archaeal oxidative pentose pathways often belong to different protein superfamilies: the xylonate dehydratase of *Caulobacter crescentus* belongs to the IlvD/EDD superfamily, while that of *H. volcanii* belongs to the enolase superfamily (kopp2020enzymologyofalternative pages 10-12). This convergent evolution underscores that pathway annotation should not assume homology from functional analogy across domains.

### 5.3 Alternative PPP configurations in gut bacteria

A significant recent discovery is the sedoheptulose-1,7-bisphosphate pathway (SBPP) in gut bacteria lacking transaldolase, including the abundant human commensal *Prevotella copri* (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 1-2). In the SBPP, RPE and ribose-5-phosphate isomerase operate normally, but the missing transaldolase reaction is bypassed by pyrophosphate-dependent phosphofructokinase (PPi-PFK) and fructose-bisphosphate aldolase acting on sedoheptulose-7-phosphate (garschagen2021analternativepentose pages 3-5, garschagen2021analternativepentose pages 12-13). This pathway is distributed across multiple bacterial phyla including Bacteroidetes, Firmicutes, Proteobacteria, Verrucomicrobia, and Lentisphaerae (garschagen2021analternativepentose pages 1-2, garschagen2021analternativepentose pages 10-12), demonstrating that the canonical non-oxidative PPP wiring assumed in KEGG is not universal even among bacteria.

### 5.4 UGDH: compartment-specific and tissue-specific variation in eukaryotes

In mammals, UGDH is a cytosolic enzyme that is ubiquitously expressed but shows particularly high levels in liver, kidney, prostate, and mammary glands (zimmer2021integrationofsugar pages 1-2). UDP-glucuronate produced by UGDH feeds three spatially distinct downstream pathways: hyaluronan synthesis at the plasma membrane, proteoglycan and UDP-xylose synthesis in the Golgi apparatus (requiring transport by SLC35 family nucleotide sugar transporters), and hormone glucuronidation in the endoplasmic reticulum (zimmer2021integrationofsugar pages 1-2, maszczakseneczko2022deliveryofnucleotide pages 29-30, maszczakseneczko2022deliveryofnucleotide pages 2-3). UXS1 exists as both membrane-bound Golgi-localized isoforms and cytoplasmic forms depending on the lineage and gene, with plant UXS proteins showing particularly diverse subcellular distributions (li2023comprehensiveanalysisof pages 9-12, li2023comprehensiveanalysisof pages 1-2).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordered dependencies

The UDP-glucose → UDP-glucuronate conversion is strictly ordered: GalU must first produce UDP-glucose before UGDH can act (choi2025uridineasa pages 6-7, choi2025uridineasa pages 7-8). UGDH itself requires NAD⁺ as a cofactor, meaning that the cellular NAD⁺/NADH ratio constrains flux through this step, and high UGDH activity can itself influence cofactor ratios (zimmer2021integrationofsugar pages 7-9). In the non-phosphorylative pentose pathways, the sequential dehydrogenase → lactonase → dehydratase order is obligatory, and the dehydratase step is frequently rate-limiting, creating a bottleneck that constrains overall pathway flux (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 10-12).

### 6.2 Mutually exclusive branch points

The KDP intermediate represents a critical metabolic branch point: it can be processed by either KDP dehydratase (Weimberg route, yielding 2,5-dioxovalerate → α-ketoglutarate) or by KDP aldolase (Dahms route, yielding pyruvate + glycolaldehyde) (ren2022structureandfunction pages 1-2, kopp2020enzymologyofalternative pages 8-10). The downstream gene content therefore determines which outcome predominates, and annotation of upstream oxidative enzymes alone cannot distinguish between these fundamentally different fates.

### 6.3 Disease-associated failure modes

Loss-of-function mutations in UGDH cause recessive developmental epileptic encephalopathy (Jamuar Syndrome) in humans, with 23 coding variants identified that impair UGDH stability, hexameric oligomerization, or catalytic activity (hengel2020lossoffunctionmutationsin pages 8-8, hengel2020lossoffunctionmutationsin pages 1-2). Mutations at residues near the NAD-binding site (Y14, I42, A44) impair cofactor reduction; mutations in the central domain (I255, G271, M306) disrupt homo-dimerization; and mutations at the dimer-dimer interface (I116, R393, A410) affect protein stability (hengel2020lossoffunctionmutationsin pages 2-3). The A44V mutant shows ~50% of wild-type Vmax and exists primarily as dimers/monomers rather than active hexamers (hengel2020lossoffunctionmutationsin pages 4-5). Clinical severity correlates with residual UGDH activity, and complete knockout is likely embryonic lethal (hengel2020lossoffunctionmutationsin pages 8-8).

In a distinct pathological context, UGDH is progressively reduced in nonalcoholic steatohepatitis (NASH) livers, where decreased UDP-glucuronate levels permit aberrant RIPK1 kinase activation. UDP-glucuronate directly binds the RIPK1 kinase domain with high affinity (ΔG = −60.3 kCal/mol), covering the ATP-binding site and forming critical interactions with D156 in the DFG motif (zhang2023udpglucuronatemetabolismcontrols pages 8-9, zhang2023udpglucuronatemetabolismcontrols pages 1-2, zhang2023udpglucuronatemetabolismcontrols pages 9-11). Hepatocyte-specific UGDH deletion accelerates NASH liver damage, while restoring UDP-glucuronate levels—even after disease onset—improves outcomes (zhang2023udpglucuronatemetabolismcontrols pages 1-2, zhang2023udpglucuronatemetabolismcontrols pages 5-7).

### 6.4 Compartment specificity

Nucleotide sugar transport across Golgi membranes represents a physical constraint on pathway flux: UDP-glucuronate, UDP-xylose, and other nucleotide sugars (~550–650 Da, doubly charged) cannot freely diffuse across membranes and require SLC35 family transporters for delivery to Golgi-lumenal glycosyltransferases (maszczakseneczko2022deliveryofnucleotide pages 2-3, maszczakseneczko2022deliveryofnucleotide pages 29-30). A human Golgi transporter with dual specificity for UDP-glucuronic acid and UDP-N-acetylgalactosamine has been identified, and the *C. elegans* SQV-7 protein also transports UDP-glucuronic acid (maszczakseneczko2022deliveryofnucleotide pages 26-27). This transport step creates a physical separation between cytosolic UDP-glucuronate production (by UGDH) and its lumenal consumption (by glycosyltransferases), adding a regulatory layer not visible in pathway maps.

## 7. Controversies and Open Questions

**7.1 Annotation conflation.** The most important practical concern for the field is that the KEGG pentose and glucuronate interconversion map aggregates functionally independent sub-modules. Automated pathway annotation tools often score an organism as having "the pentose and glucuronate interconversion pathway" based on detection of any combination of mapped enzymes, without distinguishing whether the organism possesses a complete linear pathway or merely independent segments. For example, an organism encoding RPE (pentose-phosphate interconversion) and GalU (UDP-glucose supply) but lacking UGDH and uronate catabolic enzymes would be incorrectly scored as possessing the same pathway as one with a complete Weimberg cascade (francois2020engineeringmicrobialpathways pages 4-5, ren2022structureandfunction pages 1-2).

**7.2 Enzyme family convergence.** The xylonate dehydratases in bacterial and archaeal oxidative pentose pathways belong to different superfamilies (IlvD/EDD vs. enolase), and the broader pattern of convergent evolution in sugar-acid dehydratases complicates homology-based annotation (kopp2020enzymologyofalternative pages 10-12). Phylogenetic analysis indicates that alternative sugar pathways do not originate from a single ancestor but evolved from combinations of a small number of ancestral enzyme folds (kopp2020enzymologyofalternative pages 12-14).

**7.3 Novel pathway routes.** The discovery of Route III non-phosphorylative pentose metabolism in *Herbaspirillum huttiense*, producing α-ketoglutarate, pyruvate, and glycolate through dehydrogenase and hydrolase steps acting on KDP, indicates that the catalogue of pentose catabolic variants is still incomplete (watanabe2019novelnonphosphorylativepathway pages 1-2, watanabe2019novelnonphosphorylativepathway pages 6-7). The Route II pathway of D-arabinose metabolism in this bacterium was shown to be evolutionarily unrelated to the analogous pathway in archaea (watanabe2019novelnonphosphorylativepathway pages 1-2).

**7.4 UGDH signaling functions.** The discovery that UDP-glucuronate directly inhibits RIPK1 kinase in hepatocytes (zhang2023udpglucuronatemetabolismcontrols pages 8-9, zhang2023udpglucuronatemetabolismcontrols pages 1-2) raises the question of whether metabolite-mediated signaling is a general property of nucleotide sugar intermediates or a specific adaptation of the UGDH pathway node. UGDH can also translocate to the nucleus where it interacts with HuR to relieve UDP-glucose inhibition (zimmer2021integrationofsugar pages 7-9), suggesting moonlighting functions beyond simple metabolic catalysis.

**7.5 Incomplete understanding of UDP-glucuronate transport.** While several SLC35 family members have been characterized for transport of other nucleotide sugars, the identity of the primary mammalian UDP-glucuronate transporter remains incompletely resolved, with evidence for multi-substrate specificity among several SLC35 family members (maszczakseneczko2022deliveryofnucleotide pages 29-30, maszczakseneczko2022deliveryofnucleotide pages 26-27, maszczakseneczko2022deliveryofnucleotide pages 21-23).

## 8. Key References

- Zimmer BM, Barycki JJ, Simpson MA. Integration of Sugar Metabolism and Proteoglycan Synthesis by UDP-glucose Dehydrogenase. *J Histochem Cytochem.* 2021;69:13-23. doi:10.1369/0022155420947500
- Zhang T, Zhang N, Xing J, et al. UDP-glucuronate metabolism controls RIPK1-driven liver damage in nonalcoholic steatohepatitis. *Nat Commun.* 2023;14. doi:10.1038/s41467-023-38371-2
- Hengel H, Bosso-Lefèvre C, Grady G, et al. Loss-of-function mutations in UDP-Glucose 6-Dehydrogenase cause recessive developmental epileptic encephalopathy. *Nat Commun.* 2020;11. doi:10.1038/s41467-020-14360-7
- Meloni M, Gurrieri L, Fermani S, et al. Ribulose-1,5-bisphosphate regeneration in the Calvin-Benson-Bassham cycle. *Front Plant Sci.* 2023;14. doi:10.3389/fpls.2023.1130430
- Garschagen LS, Franke T, Deppenmeier U. An alternative pentose phosphate pathway in human gut bacteria for the degradation of C5 sugars in dietary fibers. *FEBS J.* 2021;288:1839-1858. doi:10.1111/febs.15511
- Kopp D, Bergquist PL, Sunna A. Enzymology of Alternative Carbohydrate Catabolic Pathways. *Catalysts.* 2020;10:1231. doi:10.3390/catal10111231
- Watanabe S, Fukumori F, Nishiwaki H, et al. Novel non-phosphorylative pathway of pentose metabolism from bacteria. *Sci Rep.* 2019;9. doi:10.1038/s41598-018-36774-6
- Sutter JM, Johnsen U, Reinhardt A, Schönheit P. Pentose degradation in archaea: Halorhabdus species degrade D-xylose, L-arabinose and D-ribose via bacterial-type pathways. *Extremophiles.* 2020;24:759-772. doi:10.1007/s00792-020-01192-y
- Ren Y, Eronen V, Andberg M, et al. Structure and function of aldopentose catabolism enzymes involved in oxidative non-phosphorylative pathways. *Biotechnol Biofuels Bioproducts.* 2022;15. doi:10.1186/s13068-022-02252-5
- Francois JM, Alkim C, Morin N. Engineering microbial pathways for production of bio-based chemicals from lignocellulosic sugars. *Biotechnol Biofuels.* 2020;13. doi:10.1186/s13068-020-01744-6
- Maszczak-Seneczko D, Wiktor M, Skurska E, et al. Delivery of Nucleotide Sugars to the Mammalian Golgi: A Very Well (un)Explained Story. *Int J Mol Sci.* 2022;23:8648. doi:10.3390/ijms23158648
- Li Z, Chen R, Wen Y, et al. Comprehensive analysis of the UDP-glucuronate decarboxylase (UXS) gene family in tobacco. *BMC Plant Biol.* 2023;23. doi:10.1186/s12870-023-04575-3
- Choi KM, Berard BA, Yoon JH, Kim D. Uridine as a hub in cancer metabolism and RNA biology. *Exp Mol Med.* 2025. doi:10.1038/s12276-025-01402-7
- Shen L, Kohlhaas M, Enoki J, et al. A combined experimental and modelling approach for the Weimberg pathway optimisation. *Nat Commun.* 2020;11. doi:10.1038/s41467-020-14830-y
- Price MN, Deutschbauer AM, Arkin AP. Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. *PLoS Genet.* 2022;18:e1010156. doi:10.1371/journal.pgen.1010156

References

1. (meloni2023ribulose15bisphosphateregenerationin pages 4-5): Maria Meloni, Libero Gurrieri, Simona Fermani, Lauren Velie, Francesca Sparla, Pierre Crozet, Julien Henri, and Mirko Zaffagnini. Ribulose-1,5-bisphosphate regeneration in the calvin-benson-bassham cycle: focus on the last three enzymatic steps that allow the formation of rubisco substrate. Frontiers in Plant Science, Feb 2023. URL: https://doi.org/10.3389/fpls.2023.1130430, doi:10.3389/fpls.2023.1130430. This article has 51 citations.

2. (meloni2023ribulose15bisphosphateregenerationin pages 1-2): Maria Meloni, Libero Gurrieri, Simona Fermani, Lauren Velie, Francesca Sparla, Pierre Crozet, Julien Henri, and Mirko Zaffagnini. Ribulose-1,5-bisphosphate regeneration in the calvin-benson-bassham cycle: focus on the last three enzymatic steps that allow the formation of rubisco substrate. Frontiers in Plant Science, Feb 2023. URL: https://doi.org/10.3389/fpls.2023.1130430, doi:10.3389/fpls.2023.1130430. This article has 51 citations.

3. (choi2025uridineasa pages 6-7): Kyoung-Min Choi, Brennon A Berard, Je-Hyun Yoon, and Dohoon Kim. Uridine as a hub in cancer metabolism and rna biology. Experimental & molecular medicine, Aug 2025. URL: https://doi.org/10.1038/s12276-025-01402-7, doi:10.1038/s12276-025-01402-7. This article has 10 citations and is from a peer-reviewed journal.

4. (choi2025uridineasa pages 7-8): Kyoung-Min Choi, Brennon A Berard, Je-Hyun Yoon, and Dohoon Kim. Uridine as a hub in cancer metabolism and rna biology. Experimental & molecular medicine, Aug 2025. URL: https://doi.org/10.1038/s12276-025-01402-7, doi:10.1038/s12276-025-01402-7. This article has 10 citations and is from a peer-reviewed journal.

5. (zimmer2021integrationofsugar pages 1-2): Brenna M. Zimmer, Joseph J. Barycki, and Melanie A. Simpson. Integration of sugar metabolism and proteoglycan synthesis by udp-glucose dehydrogenase. Journal of Histochemistry & Cytochemistry, 69:13-23, Aug 2021. URL: https://doi.org/10.1369/0022155420947500, doi:10.1369/0022155420947500. This article has 55 citations and is from a peer-reviewed journal.

6. (zimmer2021integrationofsugar pages 10-11): Brenna M. Zimmer, Joseph J. Barycki, and Melanie A. Simpson. Integration of sugar metabolism and proteoglycan synthesis by udp-glucose dehydrogenase. Journal of Histochemistry & Cytochemistry, 69:13-23, Aug 2021. URL: https://doi.org/10.1369/0022155420947500, doi:10.1369/0022155420947500. This article has 55 citations and is from a peer-reviewed journal.

7. (francois2020engineeringmicrobialpathways pages 4-5): Jean Marie Francois, Ceren Alkim, and Nicolas Morin. Engineering microbial pathways for production of bio-based chemicals from lignocellulosic sugars: current status and perspectives. Biotechnology for Biofuels, Jul 2020. URL: https://doi.org/10.1186/s13068-020-01744-6, doi:10.1186/s13068-020-01744-6. This article has 132 citations.

8. (ren2022structureandfunction pages 1-2): Yaxin Ren, Veikko Eronen, Martina Blomster Andberg, Anu Koivula, and Nina Hakulinen. Structure and function of aldopentose catabolism enzymes involved in oxidative non-phosphorylative pathways. Biotechnology for Biofuels and Bioproducts, Dec 2022. URL: https://doi.org/10.1186/s13068-022-02252-5, doi:10.1186/s13068-022-02252-5. This article has 11 citations and is from a domain leading peer-reviewed journal.

9. (kopp2020enzymologyofalternative pages 8-10): Dominik Kopp, Peter L. Bergquist, and Anwar Sunna. Enzymology of alternative carbohydrate catabolic pathways. Catalysts, 10:1231, Oct 2020. URL: https://doi.org/10.3390/catal10111231, doi:10.3390/catal10111231. This article has 15 citations.

10. (zimmer2021integrationofsugar pages 4-6): Brenna M. Zimmer, Joseph J. Barycki, and Melanie A. Simpson. Integration of sugar metabolism and proteoglycan synthesis by udp-glucose dehydrogenase. Journal of Histochemistry & Cytochemistry, 69:13-23, Aug 2021. URL: https://doi.org/10.1369/0022155420947500, doi:10.1369/0022155420947500. This article has 55 citations and is from a peer-reviewed journal.

11. (li2023comprehensiveanalysisof pages 1-2): Zhimin Li, Runping Chen, Yufang Wen, Hanxiang Liu, Yangyang Chen, Xiaoyu Wu, Youxin Yang, Xinru Wu, Yong Zhou, and Jianping Liu. Comprehensive analysis of the udp-glucuronate decarboxylase (uxs) gene family in tobacco and functional characterization of ntuxs16 in golgi apparatus in arabidopsis. BMC Plant Biology, Nov 2023. URL: https://doi.org/10.1186/s12870-023-04575-3, doi:10.1186/s12870-023-04575-3. This article has 2 citations and is from a peer-reviewed journal.

12. (zimmer2021integrationofsugar pages 6-7): Brenna M. Zimmer, Joseph J. Barycki, and Melanie A. Simpson. Integration of sugar metabolism and proteoglycan synthesis by udp-glucose dehydrogenase. Journal of Histochemistry & Cytochemistry, 69:13-23, Aug 2021. URL: https://doi.org/10.1369/0022155420947500, doi:10.1369/0022155420947500. This article has 55 citations and is from a peer-reviewed journal.

13. (doshi2023identifyingvulnerabilitiesin pages 78-84): Identifying vulnerabilities in sugar nucleotide metabolism of cancer cells This article has 0 citations.

14. (garschagen2021analternativepentose pages 3-5): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

15. (meloni2023ribulose15bisphosphateregenerationin pages 12-12): Maria Meloni, Libero Gurrieri, Simona Fermani, Lauren Velie, Francesca Sparla, Pierre Crozet, Julien Henri, and Mirko Zaffagnini. Ribulose-1,5-bisphosphate regeneration in the calvin-benson-bassham cycle: focus on the last three enzymatic steps that allow the formation of rubisco substrate. Frontiers in Plant Science, Feb 2023. URL: https://doi.org/10.3389/fpls.2023.1130430, doi:10.3389/fpls.2023.1130430. This article has 51 citations.

16. (meloni2023ribulose15bisphosphateregenerationin pages 11-12): Maria Meloni, Libero Gurrieri, Simona Fermani, Lauren Velie, Francesca Sparla, Pierre Crozet, Julien Henri, and Mirko Zaffagnini. Ribulose-1,5-bisphosphate regeneration in the calvin-benson-bassham cycle: focus on the last three enzymatic steps that allow the formation of rubisco substrate. Frontiers in Plant Science, Feb 2023. URL: https://doi.org/10.3389/fpls.2023.1130430, doi:10.3389/fpls.2023.1130430. This article has 51 citations.

17. (sutter2020pentosedegradationin pages 1-2): Jan-Moritz Sutter, Ulrike Johnsen, Andreas Reinhardt, and Peter Schönheit. Pentose degradation in archaea: halorhabdus species degrade d-xylose, l-arabinose and d-ribose via bacterial-type pathways. Extremophiles, 24:759-772, Aug 2020. URL: https://doi.org/10.1007/s00792-020-01192-y, doi:10.1007/s00792-020-01192-y. This article has 13 citations and is from a peer-reviewed journal.

18. (sutter2020pentosedegradationin pages 10-13): Jan-Moritz Sutter, Ulrike Johnsen, Andreas Reinhardt, and Peter Schönheit. Pentose degradation in archaea: halorhabdus species degrade d-xylose, l-arabinose and d-ribose via bacterial-type pathways. Extremophiles, 24:759-772, Aug 2020. URL: https://doi.org/10.1007/s00792-020-01192-y, doi:10.1007/s00792-020-01192-y. This article has 13 citations and is from a peer-reviewed journal.

19. (garschagen2021analternativepentose pages 8-10): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

20. (zimmer2021integrationofsugar pages 2-4): Brenna M. Zimmer, Joseph J. Barycki, and Melanie A. Simpson. Integration of sugar metabolism and proteoglycan synthesis by udp-glucose dehydrogenase. Journal of Histochemistry & Cytochemistry, 69:13-23, Aug 2021. URL: https://doi.org/10.1369/0022155420947500, doi:10.1369/0022155420947500. This article has 55 citations and is from a peer-reviewed journal.

21. (zhang2023udpglucuronatemetabolismcontrols pages 1-2): Tao Zhang, Na Zhang, Jing Xing, Shuhua Zhang, Yulu Chen, Daichao Xu, and Jinyang Gu. Udp-glucuronate metabolism controls ripk1-driven liver damage in nonalcoholic steatohepatitis. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38371-2, doi:10.1038/s41467-023-38371-2. This article has 26 citations and is from a highest quality peer-reviewed journal.

22. (hengel2020lossoffunctionmutationsin pages 1-2): Holger Hengel, Célia Bosso-Lefèvre, George Grady, Emmanuelle Szenker-Ravi, Hankun Li, Sarah Pierce, Élise Lebigot, Thong-Teck Tan, Michelle Y. Eio, Gunaseelan Narayanan, Kagistia Hana Utami, Monica Yau, Nader Handal, Werner Deigendesch, Reinhard Keimer, Hiyam M. Marzouqa, Meral Gunay-Aygun, Michael J. Muriello, Helene Verhelst, Sarah Weckhuysen, Sonal Mahida, Sakkubai Naidu, Terrence G. Thomas, Jiin Ying Lim, Ee Shien Tan, Damien Haye, Michèl A. A. P. Willemsen, Renske Oegema, Wendy G. Mitchell, Tyler Mark Pierson, Marisa V. Andrews, Marcia C. Willing, Lance H. Rodan, Tahsin Stefan Barakat, Marjon van Slegtenhorst, Ralitza H. Gavrilova, Diego Martinelli, Tal Gilboa, Abdullah M. Tamim, Mais O. Hashem, Moeenaldeen D. AlSayed, Maha M. Abdulrahim, Mohammed Al-Owain, Ali Awaji, Adel A. H. Mahmoud, Eissa A. Faqeih, Ali Al Asmari, Sulwan M. Algain, Lamyaa A. Jad, Hesham M. Aldhalaan, Ingo Helbig, David A. Koolen, Angelika Riess, Ingeborg Kraegeloh-Mann, Peter Bauer, Suleyman Gulsuner, Hannah Stamberger, Alvin Yu Jin Ng, Sha Tang, Sumanty Tohari, Boris Keren, Laura E. Schultz-Rogers, Eric W. Klee, Sabina Barresi, Marco Tartaglia, Hagar Mor-Shaked, Sateesh Maddirevula, Amber Begtrup, Aida Telegrafi, Rolph Pfundt, Rebecca Schüle, Brian Ciruna, Carine Bonnard, Mahmoud A. Pouladi, James C. Stewart, Adam Claridge-Chang, Dirk J. Lefeber, Fowzan S. Alkuraya, Ajay S. Mathuru, Byrappa Venkatesh, Joseph J. Barycki, Melanie A. Simpson, Saumya S. Jamuar, Ludger Schöls, and Bruno Reversade. Loss-of-function mutations in udp-glucose 6-dehydrogenase cause recessive developmental epileptic encephalopathy. Nature Communications, Jan 2020. URL: https://doi.org/10.1038/s41467-020-14360-7, doi:10.1038/s41467-020-14360-7. This article has 59 citations and is from a highest quality peer-reviewed journal.

23. (zimmer2021integrationofsugar pages 9-10): Brenna M. Zimmer, Joseph J. Barycki, and Melanie A. Simpson. Integration of sugar metabolism and proteoglycan synthesis by udp-glucose dehydrogenase. Journal of Histochemistry & Cytochemistry, 69:13-23, Aug 2021. URL: https://doi.org/10.1369/0022155420947500, doi:10.1369/0022155420947500. This article has 55 citations and is from a peer-reviewed journal.

24. (zhang2023udpglucuronatemetabolismcontrols pages 8-9): Tao Zhang, Na Zhang, Jing Xing, Shuhua Zhang, Yulu Chen, Daichao Xu, and Jinyang Gu. Udp-glucuronate metabolism controls ripk1-driven liver damage in nonalcoholic steatohepatitis. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38371-2, doi:10.1038/s41467-023-38371-2. This article has 26 citations and is from a highest quality peer-reviewed journal.

25. (hengel2020lossoffunctionmutationsin pages 8-8): Holger Hengel, Célia Bosso-Lefèvre, George Grady, Emmanuelle Szenker-Ravi, Hankun Li, Sarah Pierce, Élise Lebigot, Thong-Teck Tan, Michelle Y. Eio, Gunaseelan Narayanan, Kagistia Hana Utami, Monica Yau, Nader Handal, Werner Deigendesch, Reinhard Keimer, Hiyam M. Marzouqa, Meral Gunay-Aygun, Michael J. Muriello, Helene Verhelst, Sarah Weckhuysen, Sonal Mahida, Sakkubai Naidu, Terrence G. Thomas, Jiin Ying Lim, Ee Shien Tan, Damien Haye, Michèl A. A. P. Willemsen, Renske Oegema, Wendy G. Mitchell, Tyler Mark Pierson, Marisa V. Andrews, Marcia C. Willing, Lance H. Rodan, Tahsin Stefan Barakat, Marjon van Slegtenhorst, Ralitza H. Gavrilova, Diego Martinelli, Tal Gilboa, Abdullah M. Tamim, Mais O. Hashem, Moeenaldeen D. AlSayed, Maha M. Abdulrahim, Mohammed Al-Owain, Ali Awaji, Adel A. H. Mahmoud, Eissa A. Faqeih, Ali Al Asmari, Sulwan M. Algain, Lamyaa A. Jad, Hesham M. Aldhalaan, Ingo Helbig, David A. Koolen, Angelika Riess, Ingeborg Kraegeloh-Mann, Peter Bauer, Suleyman Gulsuner, Hannah Stamberger, Alvin Yu Jin Ng, Sha Tang, Sumanty Tohari, Boris Keren, Laura E. Schultz-Rogers, Eric W. Klee, Sabina Barresi, Marco Tartaglia, Hagar Mor-Shaked, Sateesh Maddirevula, Amber Begtrup, Aida Telegrafi, Rolph Pfundt, Rebecca Schüle, Brian Ciruna, Carine Bonnard, Mahmoud A. Pouladi, James C. Stewart, Adam Claridge-Chang, Dirk J. Lefeber, Fowzan S. Alkuraya, Ajay S. Mathuru, Byrappa Venkatesh, Joseph J. Barycki, Melanie A. Simpson, Saumya S. Jamuar, Ludger Schöls, and Bruno Reversade. Loss-of-function mutations in udp-glucose 6-dehydrogenase cause recessive developmental epileptic encephalopathy. Nature Communications, Jan 2020. URL: https://doi.org/10.1038/s41467-020-14360-7, doi:10.1038/s41467-020-14360-7. This article has 59 citations and is from a highest quality peer-reviewed journal.

26. (li2023comprehensiveanalysisof pages 9-12): Zhimin Li, Runping Chen, Yufang Wen, Hanxiang Liu, Yangyang Chen, Xiaoyu Wu, Youxin Yang, Xinru Wu, Yong Zhou, and Jianping Liu. Comprehensive analysis of the udp-glucuronate decarboxylase (uxs) gene family in tobacco and functional characterization of ntuxs16 in golgi apparatus in arabidopsis. BMC Plant Biology, Nov 2023. URL: https://doi.org/10.1186/s12870-023-04575-3, doi:10.1186/s12870-023-04575-3. This article has 2 citations and is from a peer-reviewed journal.

27. (doshi2023identifyingvulnerabilitiesin pages 147-152): Identifying vulnerabilities in sugar nucleotide metabolism of cancer cells This article has 0 citations.

28. (kopp2020enzymologyofalternative pages 10-12): Dominik Kopp, Peter L. Bergquist, and Anwar Sunna. Enzymology of alternative carbohydrate catabolic pathways. Catalysts, 10:1231, Oct 2020. URL: https://doi.org/10.3390/catal10111231, doi:10.3390/catal10111231. This article has 15 citations.

29. (watanabe2019novelnonphosphorylativepathway pages 1-2): Seiya Watanabe, Fumiyasu Fukumori, Hisashi Nishiwaki, Yasuhiro Sakurai, Kunihiko Tajima, and Yasuo Watanabe. Novel non-phosphorylative pathway of pentose metabolism from bacteria. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-36774-6, doi:10.1038/s41598-018-36774-6. This article has 72 citations and is from a peer-reviewed journal.

30. (watanabe2019novelnonphosphorylativepathway pages 6-7): Seiya Watanabe, Fumiyasu Fukumori, Hisashi Nishiwaki, Yasuhiro Sakurai, Kunihiko Tajima, and Yasuo Watanabe. Novel non-phosphorylative pathway of pentose metabolism from bacteria. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-36774-6, doi:10.1038/s41598-018-36774-6. This article has 72 citations and is from a peer-reviewed journal.

31. (garschagen2021analternativepentose pages 2-3): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

32. (garschagen2021analternativepentose pages 12-13): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

33. (garschagen2021analternativepentose pages 1-2): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

34. (garschagen2021analternativepentose pages 10-12): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

35. (sutter2020pentosedegradationin pages 13-14): Jan-Moritz Sutter, Ulrike Johnsen, Andreas Reinhardt, and Peter Schönheit. Pentose degradation in archaea: halorhabdus species degrade d-xylose, l-arabinose and d-ribose via bacterial-type pathways. Extremophiles, 24:759-772, Aug 2020. URL: https://doi.org/10.1007/s00792-020-01192-y, doi:10.1007/s00792-020-01192-y. This article has 13 citations and is from a peer-reviewed journal.

36. (maszczakseneczko2022deliveryofnucleotide pages 29-30): Dorota Maszczak-Seneczko, Maciej Wiktor, Edyta Skurska, Wojciech Wiertelak, and Mariusz Olczak. Delivery of nucleotide sugars to the mammalian golgi: a very well (un)explained story. International Journal of Molecular Sciences, 23:8648, Aug 2022. URL: https://doi.org/10.3390/ijms23158648, doi:10.3390/ijms23158648. This article has 27 citations.

37. (maszczakseneczko2022deliveryofnucleotide pages 2-3): Dorota Maszczak-Seneczko, Maciej Wiktor, Edyta Skurska, Wojciech Wiertelak, and Mariusz Olczak. Delivery of nucleotide sugars to the mammalian golgi: a very well (un)explained story. International Journal of Molecular Sciences, 23:8648, Aug 2022. URL: https://doi.org/10.3390/ijms23158648, doi:10.3390/ijms23158648. This article has 27 citations.

38. (zimmer2021integrationofsugar pages 7-9): Brenna M. Zimmer, Joseph J. Barycki, and Melanie A. Simpson. Integration of sugar metabolism and proteoglycan synthesis by udp-glucose dehydrogenase. Journal of Histochemistry & Cytochemistry, 69:13-23, Aug 2021. URL: https://doi.org/10.1369/0022155420947500, doi:10.1369/0022155420947500. This article has 55 citations and is from a peer-reviewed journal.

39. (hengel2020lossoffunctionmutationsin pages 2-3): Holger Hengel, Célia Bosso-Lefèvre, George Grady, Emmanuelle Szenker-Ravi, Hankun Li, Sarah Pierce, Élise Lebigot, Thong-Teck Tan, Michelle Y. Eio, Gunaseelan Narayanan, Kagistia Hana Utami, Monica Yau, Nader Handal, Werner Deigendesch, Reinhard Keimer, Hiyam M. Marzouqa, Meral Gunay-Aygun, Michael J. Muriello, Helene Verhelst, Sarah Weckhuysen, Sonal Mahida, Sakkubai Naidu, Terrence G. Thomas, Jiin Ying Lim, Ee Shien Tan, Damien Haye, Michèl A. A. P. Willemsen, Renske Oegema, Wendy G. Mitchell, Tyler Mark Pierson, Marisa V. Andrews, Marcia C. Willing, Lance H. Rodan, Tahsin Stefan Barakat, Marjon van Slegtenhorst, Ralitza H. Gavrilova, Diego Martinelli, Tal Gilboa, Abdullah M. Tamim, Mais O. Hashem, Moeenaldeen D. AlSayed, Maha M. Abdulrahim, Mohammed Al-Owain, Ali Awaji, Adel A. H. Mahmoud, Eissa A. Faqeih, Ali Al Asmari, Sulwan M. Algain, Lamyaa A. Jad, Hesham M. Aldhalaan, Ingo Helbig, David A. Koolen, Angelika Riess, Ingeborg Kraegeloh-Mann, Peter Bauer, Suleyman Gulsuner, Hannah Stamberger, Alvin Yu Jin Ng, Sha Tang, Sumanty Tohari, Boris Keren, Laura E. Schultz-Rogers, Eric W. Klee, Sabina Barresi, Marco Tartaglia, Hagar Mor-Shaked, Sateesh Maddirevula, Amber Begtrup, Aida Telegrafi, Rolph Pfundt, Rebecca Schüle, Brian Ciruna, Carine Bonnard, Mahmoud A. Pouladi, James C. Stewart, Adam Claridge-Chang, Dirk J. Lefeber, Fowzan S. Alkuraya, Ajay S. Mathuru, Byrappa Venkatesh, Joseph J. Barycki, Melanie A. Simpson, Saumya S. Jamuar, Ludger Schöls, and Bruno Reversade. Loss-of-function mutations in udp-glucose 6-dehydrogenase cause recessive developmental epileptic encephalopathy. Nature Communications, Jan 2020. URL: https://doi.org/10.1038/s41467-020-14360-7, doi:10.1038/s41467-020-14360-7. This article has 59 citations and is from a highest quality peer-reviewed journal.

40. (hengel2020lossoffunctionmutationsin pages 4-5): Holger Hengel, Célia Bosso-Lefèvre, George Grady, Emmanuelle Szenker-Ravi, Hankun Li, Sarah Pierce, Élise Lebigot, Thong-Teck Tan, Michelle Y. Eio, Gunaseelan Narayanan, Kagistia Hana Utami, Monica Yau, Nader Handal, Werner Deigendesch, Reinhard Keimer, Hiyam M. Marzouqa, Meral Gunay-Aygun, Michael J. Muriello, Helene Verhelst, Sarah Weckhuysen, Sonal Mahida, Sakkubai Naidu, Terrence G. Thomas, Jiin Ying Lim, Ee Shien Tan, Damien Haye, Michèl A. A. P. Willemsen, Renske Oegema, Wendy G. Mitchell, Tyler Mark Pierson, Marisa V. Andrews, Marcia C. Willing, Lance H. Rodan, Tahsin Stefan Barakat, Marjon van Slegtenhorst, Ralitza H. Gavrilova, Diego Martinelli, Tal Gilboa, Abdullah M. Tamim, Mais O. Hashem, Moeenaldeen D. AlSayed, Maha M. Abdulrahim, Mohammed Al-Owain, Ali Awaji, Adel A. H. Mahmoud, Eissa A. Faqeih, Ali Al Asmari, Sulwan M. Algain, Lamyaa A. Jad, Hesham M. Aldhalaan, Ingo Helbig, David A. Koolen, Angelika Riess, Ingeborg Kraegeloh-Mann, Peter Bauer, Suleyman Gulsuner, Hannah Stamberger, Alvin Yu Jin Ng, Sha Tang, Sumanty Tohari, Boris Keren, Laura E. Schultz-Rogers, Eric W. Klee, Sabina Barresi, Marco Tartaglia, Hagar Mor-Shaked, Sateesh Maddirevula, Amber Begtrup, Aida Telegrafi, Rolph Pfundt, Rebecca Schüle, Brian Ciruna, Carine Bonnard, Mahmoud A. Pouladi, James C. Stewart, Adam Claridge-Chang, Dirk J. Lefeber, Fowzan S. Alkuraya, Ajay S. Mathuru, Byrappa Venkatesh, Joseph J. Barycki, Melanie A. Simpson, Saumya S. Jamuar, Ludger Schöls, and Bruno Reversade. Loss-of-function mutations in udp-glucose 6-dehydrogenase cause recessive developmental epileptic encephalopathy. Nature Communications, Jan 2020. URL: https://doi.org/10.1038/s41467-020-14360-7, doi:10.1038/s41467-020-14360-7. This article has 59 citations and is from a highest quality peer-reviewed journal.

41. (zhang2023udpglucuronatemetabolismcontrols pages 9-11): Tao Zhang, Na Zhang, Jing Xing, Shuhua Zhang, Yulu Chen, Daichao Xu, and Jinyang Gu. Udp-glucuronate metabolism controls ripk1-driven liver damage in nonalcoholic steatohepatitis. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38371-2, doi:10.1038/s41467-023-38371-2. This article has 26 citations and is from a highest quality peer-reviewed journal.

42. (zhang2023udpglucuronatemetabolismcontrols pages 5-7): Tao Zhang, Na Zhang, Jing Xing, Shuhua Zhang, Yulu Chen, Daichao Xu, and Jinyang Gu. Udp-glucuronate metabolism controls ripk1-driven liver damage in nonalcoholic steatohepatitis. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38371-2, doi:10.1038/s41467-023-38371-2. This article has 26 citations and is from a highest quality peer-reviewed journal.

43. (maszczakseneczko2022deliveryofnucleotide pages 26-27): Dorota Maszczak-Seneczko, Maciej Wiktor, Edyta Skurska, Wojciech Wiertelak, and Mariusz Olczak. Delivery of nucleotide sugars to the mammalian golgi: a very well (un)explained story. International Journal of Molecular Sciences, 23:8648, Aug 2022. URL: https://doi.org/10.3390/ijms23158648, doi:10.3390/ijms23158648. This article has 27 citations.

44. (kopp2020enzymologyofalternative pages 12-14): Dominik Kopp, Peter L. Bergquist, and Anwar Sunna. Enzymology of alternative carbohydrate catabolic pathways. Catalysts, 10:1231, Oct 2020. URL: https://doi.org/10.3390/catal10111231, doi:10.3390/catal10111231. This article has 15 citations.

45. (maszczakseneczko2022deliveryofnucleotide pages 21-23): Dorota Maszczak-Seneczko, Maciej Wiktor, Edyta Skurska, Wojciech Wiertelak, and Mariusz Olczak. Delivery of nucleotide sugars to the mammalian golgi: a very well (un)explained story. International Journal of Molecular Sciences, 23:8648, Aug 2022. URL: https://doi.org/10.3390/ijms23158648, doi:10.3390/ijms23158648. This article has 27 citations.

## Artifacts

- [Edison artifact artifact-00](pentose_glucuronate_interconversions-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](pentose_glucuronate_interconversions-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. choi2025uridineasa pages 6-7
2. zimmer2021integrationofsugar pages 10-11
3. zimmer2021integrationofsugar pages 4-6
4. zimmer2021integrationofsugar pages 6-7
5. doshi2023identifyingvulnerabilitiesin pages 78-84
6. kopp2020enzymologyofalternative pages 10-12
7. kopp2020enzymologyofalternative pages 8-10
8. sutter2020pentosedegradationin pages 13-14
9. zimmer2021integrationofsugar pages 1-2
10. zimmer2021integrationofsugar pages 7-9
11. hengel2020lossoffunctionmutationsin pages 2-3
12. hengel2020lossoffunctionmutationsin pages 4-5
13. hengel2020lossoffunctionmutationsin pages 8-8
14. maszczakseneczko2022deliveryofnucleotide pages 26-27
15. kopp2020enzymologyofalternative pages 12-14
16. watanabe2019novelnonphosphorylativepathway pages 1-2
17. choi2025uridineasa pages 7-8
18. francois2020engineeringmicrobialpathways pages 4-5
19. ren2022structureandfunction pages 1-2
20. li2023comprehensiveanalysisof pages 1-2
21. garschagen2021analternativepentose pages 3-5
22. sutter2020pentosedegradationin pages 1-2
23. sutter2020pentosedegradationin pages 10-13
24. garschagen2021analternativepentose pages 8-10
25. zimmer2021integrationofsugar pages 2-4
26. zhang2023udpglucuronatemetabolismcontrols pages 1-2
27. hengel2020lossoffunctionmutationsin pages 1-2
28. zimmer2021integrationofsugar pages 9-10
29. zhang2023udpglucuronatemetabolismcontrols pages 8-9
30. li2023comprehensiveanalysisof pages 9-12
31. doshi2023identifyingvulnerabilitiesin pages 147-152
32. watanabe2019novelnonphosphorylativepathway pages 6-7
33. garschagen2021analternativepentose pages 2-3
34. garschagen2021analternativepentose pages 12-13
35. garschagen2021analternativepentose pages 1-2
36. garschagen2021analternativepentose pages 10-12
37. maszczakseneczko2022deliveryofnucleotide pages 29-30
38. maszczakseneczko2022deliveryofnucleotide pages 2-3
39. zhang2023udpglucuronatemetabolismcontrols pages 9-11
40. zhang2023udpglucuronatemetabolismcontrols pages 5-7
41. maszczakseneczko2022deliveryofnucleotide pages 21-23
42. https://doi.org/10.3389/fpls.2023.1130430,
43. https://doi.org/10.1038/s12276-025-01402-7,
44. https://doi.org/10.1369/0022155420947500,
45. https://doi.org/10.1186/s13068-020-01744-6,
46. https://doi.org/10.1186/s13068-022-02252-5,
47. https://doi.org/10.3390/catal10111231,
48. https://doi.org/10.1186/s12870-023-04575-3,
49. https://doi.org/10.1111/febs.15511,
50. https://doi.org/10.1007/s00792-020-01192-y,
51. https://doi.org/10.1038/s41467-023-38371-2,
52. https://doi.org/10.1038/s41467-020-14360-7,
53. https://doi.org/10.1038/s41598-018-36774-6,
54. https://doi.org/10.3390/ijms23158648,