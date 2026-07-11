---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T17:37:50.350799'
end_time: '2026-07-06T18:07:39.847977'
duration_seconds: 1789.5
template_file: templates/module_research.md.j2
template_variables:
  module_title: L-histidine biosynthesis (microbial)
  module_summary: 'De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose
    1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten
    enzymatic activities that is broadly conserved across bacteria, archaea, fungi,
    and plants, and is the canonical microbial route. The pathway is metabolically
    unusual in that its purine-like intermediates connect it to nucleotide metabolism:
    the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide
    ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring
    of ATP back into the nucleotide pool. Several activities are commonly fused or
    bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase,
    and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in
    enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two
    successive NAD+-dependent oxidations through a histidinal intermediate. The pathway
    is energetically expensive and is tightly regulated, classically by feedback inhibition
    of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.'
  module_outline: "- L-histidine biosynthesis\n  - 1. PRPP supply (shared, not histidine-specific)\n\
    \  - Ribose-5-phosphate to PRPP\n    - prs: ribose-phosphate diphosphokinase (molecular\
    \ player: ribose phosphate diphosphokinase activity; activity or role: ribose\
    \ phosphate diphosphokinase activity)\n  - 2. first committed step\n  - PRPP to\
    \ phosphoribosyl-ATP\n    - hisG: ATP phosphoribosyltransferase (molecular player:\
    \ ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase\
    \ activity)\n  - 3. pyrophosphohydrolase (often HisIE bifunctional)\n  - Phosphoribosyl-ATP\
    \ to phosphoribosyl-AMP\n    - hisE: phosphoribosyl-ATP diphosphatase (molecular\
    \ player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP\
    \ diphosphatase activity)\n  - 4. cyclohydrolase (often HisIE bifunctional)\n\
    \  - Phosphoribosyl-AMP to ProFAR\n    - hisI: phosphoribosyl-AMP cyclohydrolase\
    \ (molecular player: phosphoribosyl-AMP cyclohydrolase (HisI / HisIE); activity\
    \ or role: phosphoribosyl-AMP cyclohydrolase activity)\n  - 5. amino-isomerase\n\
    \  - ProFAR to PRFAR\n    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide\
    \ isomerase activity; activity or role: ProFAR isomerase activity)\n  - 6. imidazole-glycerol-phosphate\
    \ synthase (glutamine amidotransferase)\n  - PRFAR to imidazole-glycerol-phosphate\
    \ + AICAR\n    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate\
    \ synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate\
    \ synthase activity)\n    - hisH: IGP synthase, glutamine amidotransferase subunit\
    \ (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit\
    \ HisH; activity or role: imidazoleglycerol-phosphate synthase activity)\n  -\
    \ 7. dehydratase\n  - IGP to imidazole-acetol phosphate\n    - hisB: imidazoleglycerol-phosphate\
    \ dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity;\
    \ activity or role: imidazoleglycerol-phosphate dehydratase activity)\n  - 8.\
    \ transaminase\n  - Imidazole-acetol phosphate to L-histidinol phosphate\n   \
    \ - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate\
    \ aminotransferase activity; activity or role: histidinol-phosphate aminotransferase\
    \ activity)\n  - 9. phosphatase\n  - L-histidinol phosphate to L-histidinol\n\
    \    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase\
    \ activity; activity or role: histidinol-phosphatase activity)\n  - 10. terminal\
    \ bifunctional dehydrogenase\n  - L-histidinol to L-histidine\n    - hisD: histidinol\
    \ dehydrogenase (molecular player: histidinol dehydrogenase activity; activity\
    \ or role: histidinol dehydrogenase activity)"
  module_connections: '- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP:
    PRPP from the diphosphokinase feeds the first committed step.

    - PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP

    - Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR

    - Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR

    - ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR

    - PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol
    phosphate

    - IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol
    phosphate

    - Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate
    to L-histidinol

    - L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 49
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: histidine_biosynthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: histidine_biosynthesis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

L-histidine biosynthesis (microbial)

## Working Scope

De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten enzymatic activities that is broadly conserved across bacteria, archaea, fungi, and plants, and is the canonical microbial route. The pathway is metabolically unusual in that its purine-like intermediates connect it to nucleotide metabolism: the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring of ATP back into the nucleotide pool. Several activities are commonly fused or bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase, and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two successive NAD+-dependent oxidations through a histidinal intermediate. The pathway is energetically expensive and is tightly regulated, classically by feedback inhibition of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.

## Provisional Biological Outline

- L-histidine biosynthesis
  - 1. PRPP supply (shared, not histidine-specific)
  - Ribose-5-phosphate to PRPP
    - prs: ribose-phosphate diphosphokinase (molecular player: ribose phosphate diphosphokinase activity; activity or role: ribose phosphate diphosphokinase activity)
  - 2. first committed step
  - PRPP to phosphoribosyl-ATP
    - hisG: ATP phosphoribosyltransferase (molecular player: ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase activity)
  - 3. pyrophosphohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-ATP to phosphoribosyl-AMP
    - hisE: phosphoribosyl-ATP diphosphatase (molecular player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP diphosphatase activity)
  - 4. cyclohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-AMP to ProFAR
    - hisI: phosphoribosyl-AMP cyclohydrolase (molecular player: phosphoribosyl-AMP cyclohydrolase (HisI / HisIE); activity or role: phosphoribosyl-AMP cyclohydrolase activity)
  - 5. amino-isomerase
  - ProFAR to PRFAR
    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity; activity or role: ProFAR isomerase activity)
  - 6. imidazole-glycerol-phosphate synthase (glutamine amidotransferase)
  - PRFAR to imidazole-glycerol-phosphate + AICAR
    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate synthase activity)
    - hisH: IGP synthase, glutamine amidotransferase subunit (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit HisH; activity or role: imidazoleglycerol-phosphate synthase activity)
  - 7. dehydratase
  - IGP to imidazole-acetol phosphate
    - hisB: imidazoleglycerol-phosphate dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity; activity or role: imidazoleglycerol-phosphate dehydratase activity)
  - 8. transaminase
  - Imidazole-acetol phosphate to L-histidinol phosphate
    - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate aminotransferase activity; activity or role: histidinol-phosphate aminotransferase activity)
  - 9. phosphatase
  - L-histidinol phosphate to L-histidinol
    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase activity; activity or role: histidinol-phosphatase activity)
  - 10. terminal bifunctional dehydrogenase
  - L-histidinol to L-histidine
    - hisD: histidinol dehydrogenase (molecular player: histidinol dehydrogenase activity; activity or role: histidinol dehydrogenase activity)

## Known Relationships Among Steps

- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP: PRPP from the diphosphokinase feeds the first committed step.
- PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP
- Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR
- Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR
- ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR
- PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol phosphate
- IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol phosphate
- Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate to L-histidinol
- L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine

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

L-histidine biosynthesis (microbial)

## Working Scope

De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten enzymatic activities that is broadly conserved across bacteria, archaea, fungi, and plants, and is the canonical microbial route. The pathway is metabolically unusual in that its purine-like intermediates connect it to nucleotide metabolism: the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring of ATP back into the nucleotide pool. Several activities are commonly fused or bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase, and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two successive NAD+-dependent oxidations through a histidinal intermediate. The pathway is energetically expensive and is tightly regulated, classically by feedback inhibition of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.

## Provisional Biological Outline

- L-histidine biosynthesis
  - 1. PRPP supply (shared, not histidine-specific)
  - Ribose-5-phosphate to PRPP
    - prs: ribose-phosphate diphosphokinase (molecular player: ribose phosphate diphosphokinase activity; activity or role: ribose phosphate diphosphokinase activity)
  - 2. first committed step
  - PRPP to phosphoribosyl-ATP
    - hisG: ATP phosphoribosyltransferase (molecular player: ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase activity)
  - 3. pyrophosphohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-ATP to phosphoribosyl-AMP
    - hisE: phosphoribosyl-ATP diphosphatase (molecular player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP diphosphatase activity)
  - 4. cyclohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-AMP to ProFAR
    - hisI: phosphoribosyl-AMP cyclohydrolase (molecular player: phosphoribosyl-AMP cyclohydrolase (HisI / HisIE); activity or role: phosphoribosyl-AMP cyclohydrolase activity)
  - 5. amino-isomerase
  - ProFAR to PRFAR
    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity; activity or role: ProFAR isomerase activity)
  - 6. imidazole-glycerol-phosphate synthase (glutamine amidotransferase)
  - PRFAR to imidazole-glycerol-phosphate + AICAR
    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate synthase activity)
    - hisH: IGP synthase, glutamine amidotransferase subunit (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit HisH; activity or role: imidazoleglycerol-phosphate synthase activity)
  - 7. dehydratase
  - IGP to imidazole-acetol phosphate
    - hisB: imidazoleglycerol-phosphate dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity; activity or role: imidazoleglycerol-phosphate dehydratase activity)
  - 8. transaminase
  - Imidazole-acetol phosphate to L-histidinol phosphate
    - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate aminotransferase activity; activity or role: histidinol-phosphate aminotransferase activity)
  - 9. phosphatase
  - L-histidinol phosphate to L-histidinol
    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase activity; activity or role: histidinol-phosphatase activity)
  - 10. terminal bifunctional dehydrogenase
  - L-histidinol to L-histidine
    - hisD: histidinol dehydrogenase (molecular player: histidinol dehydrogenase activity; activity or role: histidinol dehydrogenase activity)

## Known Relationships Among Steps

- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP: PRPP from the diphosphokinase feeds the first committed step.
- PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP
- Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR
- Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR
- ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR
- PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol phosphate
- IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol phosphate
- Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate to L-histidinol
- L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine

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

# De Novo Biosynthesis of L-Histidine in Microorganisms: A Comprehensive Review

## 1. Executive Summary

L-Histidine biosynthesis is one of the most ancient, metabolically expensive, and tightly regulated amino acid biosynthetic pathways. The canonical route proceeds through ten enzymatic activities, converting 5-phospho-α-D-ribose 1-diphosphate (PRPP) and ATP into L-histidine via a largely linear sequence. The pathway is broadly conserved across bacteria, archaea, fungi, and plants, and is notable for its intimate connection to purine nucleotide metabolism: the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide ribonucleotide), recycling the adenine ring of ATP back into the purine biosynthesis pool (wu2020highlyefficientproduction pages 11-14, wu2020highlyefficientproduction pages 4-8). Several enzymatic activities are commonly fused or bifunctional across lineages, the first committed enzyme (HisG, ATP phosphoribosyltransferase) exists in structurally distinct long-form and short-form architectures with fundamentally different allosteric regulatory strategies, and the terminal enzyme HisD performs two successive NAD⁺-dependent oxidations through a histidinal intermediate (duca2023theoperonas pages 5-6, khajeaian2022exploringtheevolution pages 25-32, gu2023peroxisomalcompartmentalizationof pages 8-9). The pathway has emerged as both a model system for understanding protein evolution—particularly through the paralogous TIM-barrel enzymes HisA and HisF—and as a target for antimicrobial drug discovery and metabolic engineering for industrial histidine production.

## 2. Definition and Biological Boundaries

### 2.1 Scope of the System

The histidine biosynthetic pathway is defined as the set of enzymatic reactions that convert PRPP and ATP to L-histidine through ten catalytic steps. The pathway proper begins with the first committed step catalyzed by ATP phosphoribosyltransferase (HisG) and terminates with the four-electron oxidation of L-histidinol to L-histidine by histidinol dehydrogenase (HisD) (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2). PRPP supply, catalyzed by ribose-phosphate diphosphokinase (Prs), is a shared upstream precursor step that also feeds purine, pyrimidine, NAD, and tryptophan biosynthesis, and is therefore not considered histidine-specific (schwentner2019modularsystemsmetabolic pages 2-4).

### 2.2 Neighboring Pathways That Should Be Treated Separately

Several processes interface with histidine biosynthesis but are distinct systems:

- **De novo purine biosynthesis**: Connected through the AICAR intermediate produced at step 5 and through the shared precursor PRPP. AICAR feeds back into the purine pathway via PurH, PurA, and PurB to regenerate ATP (wu2020highlyefficientproduction pages 11-14, malykh2018specificfeaturesof pages 12-13, wu2020highlyefficientproduction pages 4-8).
- **Histidine catabolism (Hut system)**: The histidine utilization pathway, which degrades histidine to glutamate and formamide for use as carbon and nitrogen sources, operates under distinct regulation and should not be conflated with biosynthesis.
- **Histidine decarboxylation**: The conversion of histidine to histamine by histidine decarboxylase (HDC) is a downstream catabolic/signaling process.
- **Tryptophan biosynthesis**: Although the TIM-barrel isomerases HisA and TrpF catalyze analogous Amadori rearrangements on related substrates, tryptophan biosynthesis is a separate pathway (lundin2020mutationalpathwaysand pages 1-2, romerorivera2022complexloopdynamics pages 1-2).

## 3. Mechanistic Overview

The ten enzymatic activities of the pathway proceed in an obligate linear sequence, with no known bypass or shortcut reactions. The following table summarizes all steps:

| Step Number | Gene(s) | Enzyme Name | EC Number | Reaction (Substrate → Product) | Key Features/Notes |
|---|---|---|---|---|---|
| 0 (precursor) | **prs** | Ribose-phosphate diphosphokinase (PRPP synthetase) | 2.7.6.1 | Ribose-5-phosphate + ATP → PRPP + AMP | Supplies PRPP, a shared precursor for histidine, purine, pyrimidine, NAD, and tryptophan metabolism; not histidine-specific but functionally upstream of the committed step (wu2020highlyefficientproduction pages 4-8, schwentner2019modularsystemsmetabolic pages 2-4) |
| 1 | **hisG** | ATP phosphoribosyltransferase (ATP-PRT) | 2.4.2.17 | PRPP + ATP → N1-(5-phosphoribosyl)-ATP (PR-ATP/PRATP) + PPi | First committed and flux-controlling step; major feedback-control point. Exists as long-form **HisG<sub>L</sub>** or short-form **HisG<sub>S</sub>** with regulatory **HisZ**; inhibited by histidine, AMP/ADP, PR-ATP, and in some systems AICAR (wu2020highlyefficientproduction pages 4-8, read2021allostericinhibitionof pages 6-11, read2021allostericinhibitionof pages 1-6, read2023crystalstructuresteadystate pages 1-2) |
| 2 | **hisE** (often fused with **hisI**) | Phosphoribosyl-ATP diphosphatase | 3.6.1.31 | PR-ATP → Phosphoribosyl-AMP (PR-AMP) + Pi | In many bacteria and archaea occurs as bifunctional **HisIE** with step 3; part of the conserved linear core following the committed step (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 8-10) |
| 3 | **hisI** (often fused with **hisE**) | Phosphoribosyl-AMP cyclohydrolase | 3.5.4.19 | PR-AMP → ProFAR | Often encoded as bifunctional **HisIE**; some lineages carry minimized or structurally divergent HisE moieties while retaining overall pathway function (duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 8-10) |
| 4 | **hisA** | ProFAR isomerase | 5.3.1.16 | ProFAR → PRFAR | TIM-barrel enzyme; paralog of **HisF** and classic model for gene duplication/divergence and enzyme evolvability. In some taxa related enzymes show bifunctionality with TrpF-like activity (PriA family is outside the canonical route) (nagarajan2020thetimbarrel pages 8-11, lundin2020mutationalpathwaysand pages 1-2, romerorivera2022complexloopdynamics pages 1-2, duca2023theoperonas pages 12-14) |
| 5 | **hisF** + **hisH** | Imidazole glycerol phosphate synthase (cyclase subunit **HisF** + glutamine amidase subunit **HisH**) | 4.3.2.10 | PRFAR + glutamine → Imidazole glycerol phosphate (IGP) + AICAR + glutamate | Metabolically unusual step linking histidine and purine metabolism: the adenine-derived portion is recovered as **AICAR**, which re-enters purine/ATP metabolism. **HisF** is a TIM-barrel paralog of **HisA**; **HisH/HisF** form a heterodimeric glutamine amidotransferase complex (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 5-6, wu2020highlyefficientproduction pages 4-8) |
| 6 | **hisB** | Imidazoleglycerol-phosphate dehydratase (IGPD) | 4.2.1.19 | IGP → Imidazole acetol-phosphate (IAP) + H2O | In enterobacteria, the N-terminal region of **HisB** is dehydratase and the C-terminal region carries histidinol-phosphate phosphatase activity, making **HisB/HisNB** bifunctional; in other organisms the phosphatase is separate (**hisN**) (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 5-6) |
| 7 | **hisC** | Histidinol-phosphate aminotransferase | 2.6.1.9 | IAP + L-glutamate → L-histidinol-phosphate + 2-oxoglutarate | PLP-dependent transamination step introducing the amino group en route to histidinol phosphate; part of the canonical linear core in bacteria and archaea (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2) |
| 8 | **hisN** (or C-terminal phosphatase domain of **hisB** in enterobacteria) | Histidinol-phosphate phosphatase | 3.1.3.15 | L-histidinol-phosphate + H2O → L-histidinol + Pi | Separate **HisN** in many microbes; fused with **HisB** as bifunctional **HisNB/HisB** in enterobacteria and some other bacteria. Gene fusion patterns vary markedly across lineages (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 5-6, duca2021thehistidinebiosynthetic pages 8-10) |
| 9 | **hisD** | Histidinol dehydrogenase | 1.1.1.23 | L-histidinol + 2 NAD+ → L-histidine + 2 NADH + 2 H+ | Catalyzes two successive NAD+-dependent oxidations via a histidinal intermediate. Terminal step is energetically/redox sensitive; in fission yeast ortholog **His2** can be peroxisome-localized with dedicated NADH/NAD+ recycling to support productivity (duca2023theoperonas pages 5-6, gu2023peroxisomalcompartmentalizationof pages 8-9, gu2023peroxisomalcompartmentalizationof pages 1-2) |


*Table: This table summarizes the precursor supply and ten canonical enzymatic activities of microbial L-histidine biosynthesis, including common gene fusions and the purine-pathway connection through AICAR. It is useful as a compact map of pathway order, enzymes, and lineage-dependent architectural variants.*

### 3.1 The First Committed Step: HisG

The reaction catalyzed by HisG—the Mg²⁺-dependent condensation of ATP and PRPP to form N1-(5-phosphoribosyl)-ATP (PRATP) and pyrophosphate—is the flux-controlling step of the pathway and the primary point of regulation (read2021allostericinhibitionof pages 1-6, read2023crystalstructuresteadystate pages 1-2). This enzyme exists in two structurally distinct architectures:

**Long-form HisG (HisG_L)**: Found in *E. coli*, *Salmonella*, *Mycobacterium*, and many other bacteria, the long form consists of 280–310 amino acids organized in three domains. Domains I and II form the catalytic core, while domain III contains an ACT regulatory domain that binds histidine as an allosteric inhibitor. HisG_L functions as a homohexamer, and the ACT domain mediates negative feedback regulation directly within the single polypeptide chain (khajeaian2022exploringtheevolution pages 25-32).

**Short-form HisG (HisG_S)**: Found in organisms including *Acinetobacter baumannii*, *Lactococcus lactis*, and *Aquifex aeolicus*, this form is approximately 80 residues shorter (205–220 amino acids) and completely lacks the ACT regulatory domain. Instead, HisG_S associates non-covalently with a regulatory protein called HisZ—a catalytically inactive paralog of histidyl-tRNA synthetase—to form a hetero-octameric holoenzyme with a tetrameric HisZ core sandwiched between two HisG_S dimers (read2023crystalstructuresteadystate pages 1-2, khajeaian2022exploringtheevolution pages 25-32, fisher2022allostericrescueof pages 1-2). HisZ serves a dual role: it allosterically activates HisG_S catalysis (producing up to 95-fold catalytic activation in *A. baumannii*) and mediates allosteric inhibition when histidine binds to HisZ (read2021allostericinhibitionof pages 6-11, fisher2022allostericrescueof pages 1-2). HisG_S alone is catalytically active but insensitive to histidine inhibition (read2021allostericinhibitionof pages 6-11, read2021allostericinhibitionof pages 1-6). The two forms share only approximately 25% sequence identity despite comparable catalytic core structures (khajeaian2022exploringtheevolution pages 25-32).

Recent work has revealed a possible third "super-long" architecture in *Leuconostoc mesenteroides*, where HisZ and HisG_S appear to have fused into a single reading frame, though this form has proven difficult to reconstitute as an active enzyme (khajeaian2022exploringtheevolution pages 5-8).

### 3.2 Steps 2–4: Ring Opening and Isomerization

The pyrophosphohydrolase (HisE) and cyclohydrolase (HisI) activities sequentially remove pyrophosphate from PRATP and then open the purine ring to generate ProFAR. These two activities are frequently encoded by a single bifunctional gene (*hisIE*) in many bacteria and archaea (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 8-10). In some lineages (e.g., Chlorobi and Rhodothermota), the HisE moiety is "minimized" to only 19–25 residues compared to the canonical *E. coli*-type sequence, while the HisI moiety remains intact, representing a case of convergent functional streamlining (duca2021thehistidinebiosynthetic pages 8-10).

ProFAR isomerase (HisA) then catalyzes the Amadori rearrangement of ProFAR to PRFAR. HisA is a (βα)₈ TIM-barrel enzyme with multiple catalytic loops that undergo conformational transitions on the millisecond timescale (nagarajan2020thetimbarrel pages 8-11, romerorivera2022complexloopdynamics pages 1-2).

### 3.3 Step 5: The Metabolic Crossroads—IGPS

Imidazole glycerol phosphate synthase (IGPS) is a bienzyme complex consisting of the cyclase subunit HisF and the glutamine amidotransferase subunit HisH. This heterodimeric complex cleaves PRFAR using ammonia derived from glutamine hydrolysis by HisH, producing imidazole glycerol phosphate (IGP) and releasing AICAR (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2). This step is metabolically pivotal because it recycles the adenine-derived portion of the original ATP substrate back into the purine nucleotide pool as AICAR. AICAR is subsequently converted to IMP and then to AMP/ATP via the enzymes PurH and PurA/PurB, creating a metabolic link that makes histidine biosynthesis both energetically expensive and deeply integrated with nucleotide metabolism (wu2020highlyefficientproduction pages 11-14, wu2020highlyefficientproduction pages 4-8).

HisF is a TIM-barrel enzyme paralogous to HisA, and ammonia is believed to be channeled from the HisH active site through the interior of the HisF barrel to the cyclase active site (nagarajan2020thetimbarrel pages 8-11, duca2021thehistidinebiosynthetic pages 5-6).

### 3.4 Steps 6–8: Dehydration, Transamination, and Dephosphorylation

The dehydratase HisB removes water from IGP to form imidazole acetol-phosphate. In enteric bacteria, HisB is a bifunctional enzyme: the N-terminal region carries dehydratase activity (IGPD) while the C-terminal region encodes histidinol-phosphate phosphatase activity, creating the fused *hisNB* gene (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 5-6). In many other organisms, the phosphatase is encoded separately by *hisN*. The distribution of the bifunctional *hisNB* originated in γ-proteobacteria and was horizontally transferred to other microbial groups (duca2021thehistidinebiosynthetic pages 5-6).

Histidinol-phosphate aminotransferase (HisC), a PLP-dependent enzyme, introduces the α-amino group using glutamate as the nitrogen donor, converting imidazole acetol-phosphate to L-histidinol-phosphate. The phosphatase (HisN or the C-terminal domain of HisB) then cleaves the phosphate ester to yield L-histidinol (duca2023theoperonas pages 5-6, duca2021thehistidinebiosynthetic pages 1-2).

### 3.5 Step 9: Terminal Oxidation by HisD

Histidinol dehydrogenase (HisD) catalyzes the final step: two successive NAD⁺-dependent oxidations that convert L-histidinol to L-histidine via a histidinal (histidinaldehyde) intermediate. The first half-reaction (histidinol → histidinal) is relatively fast but thermodynamically unfavorable, while the second oxidation (histidinal → histidine) is slower but essentially irreversible (gu2023peroxisomalcompartmentalizationof pages 8-9). This two-step oxidation makes the reaction sensitive to NAD⁺ availability. In the fission yeast *Schizosaccharomyces japonicus*, the HisD ortholog (His2) is compartmentalized within peroxisomes along with a dedicated NADH/NAD⁺ recycling enzyme (Gpd2), which maintains high local NAD⁺ concentrations to support efficient catalysis (gu2023peroxisomalcompartmentalizationof pages 8-9, gu2023peroxisomalcompartmentalizationof pages 1-2, gu2023peroxisomalcompartmentalizationof pages 5-6). This compartmentalization imposes constraints on peroxisome size, as larger peroxisomes accumulate enzymes but cannot efficiently sustain both histidine and lysine biosynthetic reactions simultaneously (gu2023peroxisomalcompartmentalizationof pages 1-2).

## 4. Regulation

### 4.1 Feedback Inhibition of HisG

The primary regulatory mechanism is allosteric feedback inhibition of HisG by the end product L-histidine. In *E. coli*, HisG is subject to at least four types of inhibition: (1) noncompetitive feedback inhibition by histidine itself; (2) mutual inhibition by ppGpp; (3) competitive inhibition by AMP or ADP; and (4) competitive product inhibition by PRATP (wu2020highlyefficientproduction pages 4-8, malykh2018specificfeaturesof pages 1-2). In the short-form enzyme from *A. baumannii*, histidine acts as a noncompetitive inhibitor with an IC₅₀ of 135 ± 3 µM and a Hill coefficient of 1.52, indicating positive cooperativity, and only the HisZ-bound holoenzyme complex is sensitive to histidine inhibition (read2021allostericinhibitionof pages 6-11).

Additionally, AICAR has been shown to inhibit HisG as a structural analog of AMP, creating a secondary feedback loop whereby the pathway's own intermediate (AICAR) controls its own rate of formation (malykh2018specificfeaturesof pages 12-13, malykh2018specificfeaturesof pages 1-2, malykh2018specificfeaturesof pages 13-14). This AICAR-mediated inhibition is a significant bottleneck during histidine overproduction in engineered strains (malykh2018specificfeaturesof pages 1-2).

### 4.2 Transcriptional Regulation

In *E. coli* and *Salmonella enterica*, the *his* operon is regulated by transcription attenuation via the leader peptide HisL. When sufficient charged histidyl-tRNAs are present, fast translation of the leader peptide results in formation of a transcription terminator stem-loop structure, attenuating transcription of the downstream biosynthetic genes. Under histidine starvation, ribosome stalling at the His-rich codons of HisL allows formation of an anti-terminator structure, permitting read-through transcription of the operon (wu2020highlyefficientproduction pages 4-8, wu2020highlyefficientproduction pages 8-11). In *Corynebacterium glutamicum*, histidine biosynthesis is regulated by a T-box-mediated attenuation mechanism (schwentner2019modularsystemsmetabolic pages 2-4).

Recent work has shown that ribosome inhibitors can increase expression of the histidine operon in *Salmonella*, with consequences extending to bacterial morphology—slow translation of HisL activates the histidine operon and induces filamentation, potentially serving as an acid-stress survival strategy.

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep Evolutionary Origin

Histidine biosynthesis is ancient, likely predating the last universal common ancestor (LUCA), with evidence from archaeal, bacterial, and eukaryotic genomes supporting its conservation across all three domains of life (duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 2-3). The pathway itself—the chemical transformations and the order of steps—is identically conserved across all organisms capable of synthesizing histidine (duca2023theoperonas pages 5-6). However, the genomic organization, gene structures, and regulatory strategies vary extensively.

### 5.2 Gene Organization Across Lineages

In enterobacteria such as *E. coli* and *S. enterica*, all eight histidine biosynthetic genes are organized in a single compact operon (*hisGDC(NB)HAF(IE)*) (duca2023theoperonas pages 5-6). The "piecewise" construction model proposes that scattered monofunctional genes progressively clustered into suboperons (*hisGDC*, *hisBHAF*, *hisIE*) in proteobacterial ancestors, eventually forming compact operons with fused and overlapping genes (duca2021thehistidinebiosynthetic pages 2-3). In contrast, organisms like *Aquifex aeolicus* have *his* genes dispersed throughout the genome rather than organized in operons (khajeaian2022exploringtheevolution pages 15-19). In the Bacteroidota-Rhodothermota-Balneolota-Chlorobiota superphylum, diverse arrangements are observed, including compact operons, suboperons, and regulons, with the organization in the common ancestor likely consisting of genes scattered throughout the chromosome (duca2021thehistidinebiosynthetic pages 5-6, duca2021thehistidinebiosynthetic pages 8-10).

### 5.3 Gene Fusions and Bifunctional Enzymes

Gene fusions are a hallmark of the pathway's evolutionary elaboration. In prokaryotes, common fusions include *hisIE* (pyrophosphohydrolase/cyclohydrolase), *hisNB* (phosphatase/dehydratase in γ-proteobacteria), and in some archaea *hisHF* (duca2021thehistidinebiosynthetic pages 1-2). In eukaryotes, even more extensive fusions occur: the yeast *HIS4* gene encodes a trifunctional enzyme (corresponding to HisI, HisE, and HisD activities), and *HIS7* encodes a bifunctional enzyme corresponding to HisH and HisF (duca2021thehistidinebiosynthetic pages 1-2). The distribution of the bifunctional *hisNB* originated in γ-proteobacteria and was horizontally transferred to some members of other bacterial groups including Bacteroidetes (duca2021thehistidinebiosynthetic pages 5-6).

### 5.4 HisA and HisF: Paradigms of Protein Evolution

HisA (ProFAR isomerase) and HisF (IGPS cyclase subunit) are paralogous TIM-barrel enzymes that share approximately 25% sequence homology and strikingly similar three-dimensional structures (RMSD 1.5–2 Å) (nagarajan2020thetimbarrel pages 8-11). Both possess two-fold internal symmetry in their C-terminal loops, consistent with an evolutionary model in which an ancestral half-barrel (encoding a single βα module) underwent gene duplication and fusion to form a closed (βα)₈ barrel, followed by a second gene duplication event that gave rise to the divergent HisA and HisF paralogs (nagarajan2020thetimbarrel pages 8-11, duca2021thehistidinebiosynthetic pages 5-6, duca2023theoperonas pages 12-14).

These enzymes have become important model systems for studying enzyme specificity evolution. HisA catalyzes the Amadori rearrangement of ProFAR, while TrpF catalyzes an analogous reaction on a different substrate in tryptophan biosynthesis. Laboratory evolution experiments in *Salmonella enterica* over 3,000 generations have produced specialist variants of both enzymes and PriA-like bifunctional enzymes from ancestral HisA, with promiscuous TrpF activity detectable in specialist HisA enzymes (romerorivera2022complexloopdynamics pages 1-2). Among 16 single mutations identified that conferred TrpF activity on HisA, only three maintained the original HisA activity, and in all 12 lineages evolved toward improved TrpF activity, the original HisA activity was completely lost, indicating strong functional trade-offs that favor gene duplication and divergence over maintenance of bifunctional generalists (lundin2020mutationalpathwaysand pages 1-2).

Computational studies have revealed that multiple long catalytic loops (loops 1, 3, 4, 5, and 6) undergo conformational transitions on the millisecond or slower timescale, with loops 3 and 4 of HisA and PriA acting as "gripper loops" that facilitate substrate isomerization, hinting at convergent evolution across different (βα)₈-barrel scaffolds (romerorivera2022complexloopdynamics pages 1-2).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligate Step Order

All ten enzymatic reactions must proceed in strict linear sequence; no alternative branching or bypass reactions are known. The pathway consumes one ATP (consumed at step 1), one PRPP, one glutamine (at step 5), one glutamate (at step 7, as amino donor for transaminase), and two NAD⁺ (at step 9), making it one of the most energetically costly amino acid biosynthetic routes (wu2020highlyefficientproduction pages 1-4, schwentner2019modularsystemsmetabolic pages 1-2).

### 6.2 Metabolic Interdependencies

The AICAR recycling requirement creates a critical dependency on the purine biosynthetic pathway. Flux balance analysis has identified ATP regeneration from AICAR as a crucial step for histidine production; failure to recycle AICAR results in both AICAR accumulation (which inhibits HisG) and ATP depletion (schwentner2019modularsystemsmetabolic pages 7-9, schwentner2019modularsystemsmetabolic pages 1-2, malykh2018specificfeaturesof pages 12-13). PRPP allocation is another constraint, as it must be partitioned among histidine, purine, pyrimidine, tryptophan, and NAD biosynthesis (schwentner2019modularsystemsmetabolic pages 2-4).

### 6.3 Energetic and Redox Constraints

Insufficient ATP regeneration capacity prevents maintenance of a balanced energy state during histidine overproduction, and inadequate C1 unit supply limits pathway flux (schwentner2019modularsystemsmetabolic pages 1-2). The terminal HisD reaction requires NAD⁺; in organisms with compartmentalized biosynthesis (e.g., fission yeast peroxisomes), dedicated NADH/NAD⁺ recycling is essential for optimal productivity (gu2023peroxisomalcompartmentalizationof pages 8-9, gu2023peroxisomalcompartmentalizationof pages 1-2).

## 7. Current Applications

### 7.1 Metabolic Engineering for Industrial Production

L-Histidine is a functional amino acid with therapeutic and nutritional applications that has historically been one of the few amino acids not produced on a large scale by microbial fermentation. Recent metabolic engineering advances have changed this landscape:

| Host Organism | Key Engineering Strategies | Titer (g/L) | Yield (g/g or mol/mol) | Productivity (g/L/h) | Reference |
|---|---|---:|---|---:|---|
| *Escherichia coli* | Removed transcription attenuation; introduced feedback-resistant **HisG**; optimized chromosomal expression of **his** genes; strengthened PRPP supply; rerouted purine metabolism and improved AICAR-to-ATP recycling; enhanced glutamate supply and histidine export | 66.5 | 0.23 g/g glucose | 1.5 | Wu et al., 2020, *ACS Synthetic Biology*, doi:10.1021/acssynbio.0c00163 (wu2020highlyefficientproduction pages 4-8, wu2020highlyefficientproduction pages 1-4, wu2020highlyefficientproduction pages 11-14) |
| *Corynebacterium glutamicum* | Modular systems metabolic engineering; feedback-resistant **hisG**; improved ATP regeneration from AICAR via **purA/purB**; strengthened C1 supply with glycine cleavage system; redirected carbon flux to oxidative PPP | NR | 0.093 mol/mol glucose | NR | Schwentner et al., 2019, *Biotechnology for Biofuels*, doi:10.1186/s13068-019-1410-2 (schwentner2019modularsystemsmetabolic pages 7-9, schwentner2019modularsystemsmetabolic pages 1-2) |
| *Corynebacterium glutamicum* | Earlier intermediate engineered strain with feedback-resistant **HisG** plus promoter/translational optimization; managed PRPP allocation and purine/histidine coupling through AICAR recycling | NR | 0.065 ± 0.004 mol/mol glucose | NR | Schwentner et al., 2019, *Biotechnology for Biofuels*, doi:10.1186/s13068-019-1410-2 (schwentner2019modularsystemsmetabolic pages 2-4) |
| *Escherichia coli* | Addressed AICAR-mediated feedback bottleneck by overexpressing **purH** and **purA** to improve AICAR-to-ATP conversion; deleted **pitA** to alter phosphate/metal transport; used feedback-resistant **HisG** background | NR | NR | NR | Malykh et al., 2018, *Microbial Cell Factories*, doi:10.1186/s12934-018-0890-2 (malykh2018specificfeaturesof pages 1-2, malykh2018specificfeaturesof pages 13-14) |


*Table: This table summarizes representative metabolic engineering achievements for microbial L-histidine overproduction, highlighting the main interventions used to relieve pathway regulation and improve precursor, energy, and AICAR recycling. It is useful for comparing how *E. coli* and *C. glutamicum* strains were optimized and what production metrics were reported.*

The highest reported titer of 66.5 g/L histidine was achieved through systematic engineering of *E. coli*, combining removal of transcription attenuation, introduction of feedback-resistant HisG mutants (e.g., HisG^{cgl}S143F), chromosome-based optimization of *his* gene expression, strengthening of PRPP supply, rerouting of purine nucleotide metabolism, and enhancement of glutamate supply and histidine export (wu2020highlyefficientproduction pages 1-4, wu2020highlyefficientproduction pages 11-14, wu2020highlyefficientproduction pages 8-11). In *C. glutamicum*, modular systems metabolic engineering combined with systems metabolic profiling and flux balance analysis achieved yields of 0.093 mol/mol glucose by addressing ATP regeneration, C1 supply, and carbon flux distribution bottlenecks (schwentner2019modularsystemsmetabolic pages 7-9, schwentner2019modularsystemsmetabolic pages 1-2).

### 7.2 Antimicrobial Drug Target

The histidine biosynthetic pathway is absent in mammals, making it an attractive target for antimicrobial drug development. ATP phosphoribosyltransferase from *A. baumannii* (AbATPPRT) has been identified as a promising antibiotic target, as HisG_S is necessary for bacterial persistence during pneumonia infection. Allosteric inhibition strategies using dipeptides (His-Pro) and heterologous HisZ proteins have been explored as foundations for inhibitor design (read2021allostericinhibitionof pages 15-20, read2021allostericinhibitionof pages 28-32). In *M. tuberculosis*, a novel approach has demonstrated that metabolic *activation*—rather than inhibition—can be bactericidal: engineered ATP-PRT variants resistant to allosteric inhibition by histidine cause supraphysiological pathway activation, leading to nutrient and energy depletion that significantly reduced infections in human macrophages and in a mouse model (carvalho2026activationoflhistidine pages 1-2). For fungal pathogens, deletion of *hisB* (IGPD) in *Aspergillus* causes histidine auxotrophy and reduced virulence in pulmonary, systemic, and corneal infection models (srivastava2021currentpromisingtherapeutic pages 1-3).

## 8. Controversies and Open Questions

Several important questions remain unresolved:

1. **Ancestral gene organization**: Whether the LUCA possessed *his* genes organized in operons or as scattered genes remains debated. The "piecewise" model of progressive operon assembly is supported by comparative genomics but not definitively proven (duca2021thehistidinebiosynthetic pages 2-3, duca2023theoperonas pages 5-6).

2. **Functional significance of gene fusions**: While bifunctional enzymes like HisIE and HisNB are common, whether gene fusions primarily serve to coordinate enzyme stoichiometry, enable substrate channeling, or simply reflect selfish operon dynamics remains unclear (duca2021thehistidinebiosynthetic pages 1-2, duca2021thehistidinebiosynthetic pages 8-10).

3. **HisA/TrpF evolutionary trajectory**: The strong functional trade-off between HisA and TrpF activities in experimental evolution suggests that gene duplication-divergence is the primary path to new enzyme functions, but naturally bifunctional PriA enzymes exist in some organisms, complicating the picture (lundin2020mutationalpathwaysand pages 1-2, romerorivera2022complexloopdynamics pages 1-2).

4. **Ammonia channeling in IGPS**: The precise mechanism by which ammonia is transferred from HisH to the HisF active site—whether through a pre-formed tunnel or a dynamically assembled channel—continues to be investigated with structural and computational approaches (duca2021thehistidinebiosynthetic pages 5-6).

5. **Allosteric mechanism diversity**: The discovery of the "super-long" form of ATP-PRT in *Leuconostoc mesenteroides*, which combines HisZ and HisG_S in a single reading frame yet lacks detectable activity, raises questions about the functional constraints on enzyme architecture evolution (khajeaian2022exploringtheevolution pages 5-8).

6. **AICAR as a broader metabolic signal**: AICAR's role extends beyond simple feedback inhibition of HisG; evidence suggests it may influence the PhoBR two-component system controlling the Pho regulon, potentially linking histidine biosynthesis to phosphate homeostasis (malykh2018specificfeaturesof pages 13-14).

7. **Role of loop dynamics in enzyme evolution**: How the complex, interdependent motions of multiple slow loops on TIM-barrel enzymes determine catalytic specificity and evolvability remains an active area of computational and experimental investigation (romerorivera2022complexloopdynamics pages 1-2).

## 9. Key References

- Del Duca S et al. (2023) "The operon as a conundrum of gene dynamics and biochemical constraints: what we have learned from histidine biosynthesis." *Genes* 14:949. doi:10.3390/genes14040949
- Del Duca S et al. (2021) "The histidine biosynthetic genes in the superphylum Bacteroidota-Rhodothermota-Balneolota-Chlorobiota." *Microorganisms* 9:1439. doi:10.3390/microorganisms9071439
- Wu H et al. (2020) "Highly efficient production of L-histidine from glucose by metabolically engineered *Escherichia coli*." *ACS Synthetic Biology* 9:1813–1822. doi:10.1021/acssynbio.0c00163
- Read BJ et al. (2023) "Crystal structure, steady-state, and pre-steady-state kinetics of *Acinetobacter baumannii* ATP phosphoribosyltransferase." *Biochemistry* 63:230–240. doi:10.1021/acs.biochem.3c00551
- Fisher G et al. (2022) "Allosteric rescue of catalytically impaired ATP phosphoribosyltransferase variants." *Nature Communications* 13:article. doi:10.1038/s41467-022-34960-9
- Romero-Rivera A et al. (2022) "Complex loop dynamics underpin activity, specificity, and evolvability in the (βα)₈ barrel enzymes of histidine and tryptophan biosynthesis." *JACS Au* 2:943–960. doi:10.1021/jacsau.2c00063
- Lundin E et al. (2020) "Mutational pathways and trade-offs between HisA and TrpF functions." *Frontiers in Microbiology* 11:588235. doi:10.3389/fmicb.2020.588235
- Schwentner A et al. (2019) "Modular systems metabolic engineering enables balancing of relevant pathways for L-histidine production with *Corynebacterium glutamicum*." *Biotechnology for Biofuels* 12:article. doi:10.1186/s13068-019-1410-2
- Malykh EA et al. (2018) "Specific features of L-histidine production by *E. coli* concerned with feedback control of AICAR formation." *Microbial Cell Factories* 17:article. doi:10.1186/s12934-018-0890-2
- Gu Y et al. (2023) "Peroxisomal compartmentalization of amino acid biosynthesis reactions imposes an upper limit on compartment size." *Nature Communications* 14:article. doi:10.1038/s41467-023-41347-x
- De Carvalho LP et al. (2026) "Activation of L-histidine biosynthesis as a new antibiotic strategy against *Mycobacterium tuberculosis*." *Nature Communications* 17:article. doi:10.1038/s41467-026-70510-3
- Read BJ et al. (2021) "Allosteric inhibition of *Acinetobacter baumannii* ATP phosphoribosyltransferase by protein:dipeptide and protein:protein interactions." *ACS Infectious Diseases* 8:197–209. doi:10.1021/acsinfecdis.1c00539

References

1. (wu2020highlyefficientproduction pages 11-14): Heyun Wu, Daoguang Tian, Xiaoguang Fan, Weiming Fan, Yue Zhang, Shuai Jiang, Chenhui Wen, Qian Ma, Ning Chen, and Xixian Xie. Highly efficient production of l-histidine from glucose by metabolically engineered escherichia coli. ACS synthetic biology, 9:1813-1822, May 2020. URL: https://doi.org/10.1021/acssynbio.0c00163, doi:10.1021/acssynbio.0c00163. This article has 70 citations and is from a domain leading peer-reviewed journal.

2. (wu2020highlyefficientproduction pages 4-8): Heyun Wu, Daoguang Tian, Xiaoguang Fan, Weiming Fan, Yue Zhang, Shuai Jiang, Chenhui Wen, Qian Ma, Ning Chen, and Xixian Xie. Highly efficient production of l-histidine from glucose by metabolically engineered escherichia coli. ACS synthetic biology, 9:1813-1822, May 2020. URL: https://doi.org/10.1021/acssynbio.0c00163, doi:10.1021/acssynbio.0c00163. This article has 70 citations and is from a domain leading peer-reviewed journal.

3. (duca2023theoperonas pages 5-6): Sara Del Duca, Giulia Semenzato, Antonia Esposito, Pietro Liò, and Renato Fani. The operon as a conundrum of gene dynamics and biochemical constraints: what we have learned from histidine biosynthesis. Genes, 14:949, Apr 2023. URL: https://doi.org/10.3390/genes14040949, doi:10.3390/genes14040949. This article has 12 citations.

4. (khajeaian2022exploringtheevolution pages 25-32): Parastoo Khajeaian. Exploring the evolution and function of the first enzyme in histidine biosynthesis. ArXiv, 2022. URL: https://doi.org/10.26686/wgtn.19709419, doi:10.26686/wgtn.19709419. This article has 1 citations.

5. (gu2023peroxisomalcompartmentalizationof pages 8-9): Ying Gu, Sara Alam, and Snezhana Oliferenko. Peroxisomal compartmentalization of amino acid biosynthesis reactions imposes an upper limit on compartment size. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41347-x, doi:10.1038/s41467-023-41347-x. This article has 18 citations and is from a highest quality peer-reviewed journal.

6. (duca2021thehistidinebiosynthetic pages 1-2): Sara Del Duca, Christopher Riccardi, Alberto Vassallo, Giulia Fontana, Lara Mitia Castronovo, Sofia Chioccioli, and Renato Fani. The histidine biosynthetic genes in the superphylum bacteroidota-rhodothermota-balneolota-chlorobiota: insights into the evolution of gene structure and organization. Microorganisms, 9:1439, Jul 2021. URL: https://doi.org/10.3390/microorganisms9071439, doi:10.3390/microorganisms9071439. This article has 8 citations.

7. (schwentner2019modularsystemsmetabolic pages 2-4): Andreas Schwentner, André Feith, Eugenia Münch, Judith Stiefelmaier, Ira Lauer, Lorenzo Favilli, Christoph Massner, Johannes Öhrlein, Bastian Grund, Andrea Hüser, Ralf Takors, and Bastian Blombach. Modular systems metabolic engineering enables balancing of relevant pathways for l-histidine production with corynebacterium glutamicum. Biotechnology for Biofuels, Mar 2019. URL: https://doi.org/10.1186/s13068-019-1410-2, doi:10.1186/s13068-019-1410-2. This article has 43 citations.

8. (malykh2018specificfeaturesof pages 12-13): Evgeniya A. Malykh, Ivan A. Butov, Anna B. Ravcheeva, Alexander A. Krylov, Sergey V. Mashko, and Nataliya V. Stoynova. Specific features of l-histidine production by escherichia coli concerned with feedback control of aicar formation and inorganic phosphate/metal transport. Microbial Cell Factories, Mar 2018. URL: https://doi.org/10.1186/s12934-018-0890-2, doi:10.1186/s12934-018-0890-2. This article has 31 citations and is from a peer-reviewed journal.

9. (lundin2020mutationalpathwaysand pages 1-2): Erik Lundin, Joakim Näsvall, and Dan I. Andersson. Mutational pathways and trade-offs between hisa and trpf functions: implications for evolution via gene duplication and divergence. Frontiers in Microbiology, Oct 2020. URL: https://doi.org/10.3389/fmicb.2020.588235, doi:10.3389/fmicb.2020.588235. This article has 8 citations and is from a peer-reviewed journal.

10. (romerorivera2022complexloopdynamics pages 1-2): Adrian Romero-Rivera, Marina Corbella, Antonietta Parracino, Wayne M. Patrick, and Shina Caroline Lynn Kamerlin. Complex loop dynamics underpin activity, specificity, and evolvability in the (βα)8 barrel enzymes of histidine and tryptophan biosynthesis. JACS Au, 2:943-960, Apr 2022. URL: https://doi.org/10.1021/jacsau.2c00063, doi:10.1021/jacsau.2c00063. This article has 35 citations and is from a peer-reviewed journal.

11. (read2021allostericinhibitionof pages 6-11): Benjamin J. Read, Gemma Fisher, Oliver L. R. Wissett, Teresa F. G. Machado, John Nicholson, John B. O. Mitchell, and Rafael G. da Silva. Allosteric inhibition of acinetobacter baumannii atp phosphoribosyltransferase by protein:dipeptide and protein:protein interactions. ACS infectious diseases, 8:197-209, Dec 2021. URL: https://doi.org/10.1021/acsinfecdis.1c00539, doi:10.1021/acsinfecdis.1c00539. This article has 7 citations and is from a peer-reviewed journal.

12. (read2021allostericinhibitionof pages 1-6): Benjamin J. Read, Gemma Fisher, Oliver L. R. Wissett, Teresa F. G. Machado, John Nicholson, John B. O. Mitchell, and Rafael G. da Silva. Allosteric inhibition of acinetobacter baumannii atp phosphoribosyltransferase by protein:dipeptide and protein:protein interactions. ACS infectious diseases, 8:197-209, Dec 2021. URL: https://doi.org/10.1021/acsinfecdis.1c00539, doi:10.1021/acsinfecdis.1c00539. This article has 7 citations and is from a peer-reviewed journal.

13. (read2023crystalstructuresteadystate pages 1-2): Benjamin J. Read, Andrew F. Cadzow, Magnus S. Alphey, John B. O. Mitchell, and Rafael G. da Silva. Crystal structure, steady-state, and pre-steady-state kinetics of acinetobacter baumannii atp phosphoribosyltransferase. Biochemistry, 63:230-240, Dec 2023. URL: https://doi.org/10.1021/acs.biochem.3c00551, doi:10.1021/acs.biochem.3c00551. This article has 4 citations and is from a peer-reviewed journal.

14. (duca2021thehistidinebiosynthetic pages 8-10): Sara Del Duca, Christopher Riccardi, Alberto Vassallo, Giulia Fontana, Lara Mitia Castronovo, Sofia Chioccioli, and Renato Fani. The histidine biosynthetic genes in the superphylum bacteroidota-rhodothermota-balneolota-chlorobiota: insights into the evolution of gene structure and organization. Microorganisms, 9:1439, Jul 2021. URL: https://doi.org/10.3390/microorganisms9071439, doi:10.3390/microorganisms9071439. This article has 8 citations.

15. (nagarajan2020thetimbarrel pages 8-11): Deepesh Nagarajan and Neha Nanajkar. The tim barrel fold. WikiJournal of Science, 3:4, Jan 2020. URL: https://doi.org/10.15347/wjs/2020.004, doi:10.15347/wjs/2020.004. This article has 2 citations.

16. (duca2023theoperonas pages 12-14): Sara Del Duca, Giulia Semenzato, Antonia Esposito, Pietro Liò, and Renato Fani. The operon as a conundrum of gene dynamics and biochemical constraints: what we have learned from histidine biosynthesis. Genes, 14:949, Apr 2023. URL: https://doi.org/10.3390/genes14040949, doi:10.3390/genes14040949. This article has 12 citations.

17. (duca2021thehistidinebiosynthetic pages 5-6): Sara Del Duca, Christopher Riccardi, Alberto Vassallo, Giulia Fontana, Lara Mitia Castronovo, Sofia Chioccioli, and Renato Fani. The histidine biosynthetic genes in the superphylum bacteroidota-rhodothermota-balneolota-chlorobiota: insights into the evolution of gene structure and organization. Microorganisms, 9:1439, Jul 2021. URL: https://doi.org/10.3390/microorganisms9071439, doi:10.3390/microorganisms9071439. This article has 8 citations.

18. (gu2023peroxisomalcompartmentalizationof pages 1-2): Ying Gu, Sara Alam, and Snezhana Oliferenko. Peroxisomal compartmentalization of amino acid biosynthesis reactions imposes an upper limit on compartment size. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41347-x, doi:10.1038/s41467-023-41347-x. This article has 18 citations and is from a highest quality peer-reviewed journal.

19. (fisher2022allostericrescueof pages 1-2): Gemma Fisher, Marina Corbella, Magnus S. Alphey, John Nicholson, Benjamin J. Read, Shina C. L. Kamerlin, and Rafael G. da Silva. Allosteric rescue of catalytically impaired atp phosphoribosyltransferase variants links protein dynamics to active-site electrostatic preorganisation. Nature Communications, Dec 2022. URL: https://doi.org/10.1038/s41467-022-34960-9, doi:10.1038/s41467-022-34960-9. This article has 19 citations and is from a highest quality peer-reviewed journal.

20. (khajeaian2022exploringtheevolution pages 5-8): Parastoo Khajeaian. Exploring the evolution and function of the first enzyme in histidine biosynthesis. ArXiv, 2022. URL: https://doi.org/10.26686/wgtn.19709419, doi:10.26686/wgtn.19709419. This article has 1 citations.

21. (gu2023peroxisomalcompartmentalizationof pages 5-6): Ying Gu, Sara Alam, and Snezhana Oliferenko. Peroxisomal compartmentalization of amino acid biosynthesis reactions imposes an upper limit on compartment size. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41347-x, doi:10.1038/s41467-023-41347-x. This article has 18 citations and is from a highest quality peer-reviewed journal.

22. (malykh2018specificfeaturesof pages 1-2): Evgeniya A. Malykh, Ivan A. Butov, Anna B. Ravcheeva, Alexander A. Krylov, Sergey V. Mashko, and Nataliya V. Stoynova. Specific features of l-histidine production by escherichia coli concerned with feedback control of aicar formation and inorganic phosphate/metal transport. Microbial Cell Factories, Mar 2018. URL: https://doi.org/10.1186/s12934-018-0890-2, doi:10.1186/s12934-018-0890-2. This article has 31 citations and is from a peer-reviewed journal.

23. (malykh2018specificfeaturesof pages 13-14): Evgeniya A. Malykh, Ivan A. Butov, Anna B. Ravcheeva, Alexander A. Krylov, Sergey V. Mashko, and Nataliya V. Stoynova. Specific features of l-histidine production by escherichia coli concerned with feedback control of aicar formation and inorganic phosphate/metal transport. Microbial Cell Factories, Mar 2018. URL: https://doi.org/10.1186/s12934-018-0890-2, doi:10.1186/s12934-018-0890-2. This article has 31 citations and is from a peer-reviewed journal.

24. (wu2020highlyefficientproduction pages 8-11): Heyun Wu, Daoguang Tian, Xiaoguang Fan, Weiming Fan, Yue Zhang, Shuai Jiang, Chenhui Wen, Qian Ma, Ning Chen, and Xixian Xie. Highly efficient production of l-histidine from glucose by metabolically engineered escherichia coli. ACS synthetic biology, 9:1813-1822, May 2020. URL: https://doi.org/10.1021/acssynbio.0c00163, doi:10.1021/acssynbio.0c00163. This article has 70 citations and is from a domain leading peer-reviewed journal.

25. (duca2021thehistidinebiosynthetic pages 2-3): Sara Del Duca, Christopher Riccardi, Alberto Vassallo, Giulia Fontana, Lara Mitia Castronovo, Sofia Chioccioli, and Renato Fani. The histidine biosynthetic genes in the superphylum bacteroidota-rhodothermota-balneolota-chlorobiota: insights into the evolution of gene structure and organization. Microorganisms, 9:1439, Jul 2021. URL: https://doi.org/10.3390/microorganisms9071439, doi:10.3390/microorganisms9071439. This article has 8 citations.

26. (khajeaian2022exploringtheevolution pages 15-19): Parastoo Khajeaian. Exploring the evolution and function of the first enzyme in histidine biosynthesis. ArXiv, 2022. URL: https://doi.org/10.26686/wgtn.19709419, doi:10.26686/wgtn.19709419. This article has 1 citations.

27. (wu2020highlyefficientproduction pages 1-4): Heyun Wu, Daoguang Tian, Xiaoguang Fan, Weiming Fan, Yue Zhang, Shuai Jiang, Chenhui Wen, Qian Ma, Ning Chen, and Xixian Xie. Highly efficient production of l-histidine from glucose by metabolically engineered escherichia coli. ACS synthetic biology, 9:1813-1822, May 2020. URL: https://doi.org/10.1021/acssynbio.0c00163, doi:10.1021/acssynbio.0c00163. This article has 70 citations and is from a domain leading peer-reviewed journal.

28. (schwentner2019modularsystemsmetabolic pages 1-2): Andreas Schwentner, André Feith, Eugenia Münch, Judith Stiefelmaier, Ira Lauer, Lorenzo Favilli, Christoph Massner, Johannes Öhrlein, Bastian Grund, Andrea Hüser, Ralf Takors, and Bastian Blombach. Modular systems metabolic engineering enables balancing of relevant pathways for l-histidine production with corynebacterium glutamicum. Biotechnology for Biofuels, Mar 2019. URL: https://doi.org/10.1186/s13068-019-1410-2, doi:10.1186/s13068-019-1410-2. This article has 43 citations.

29. (schwentner2019modularsystemsmetabolic pages 7-9): Andreas Schwentner, André Feith, Eugenia Münch, Judith Stiefelmaier, Ira Lauer, Lorenzo Favilli, Christoph Massner, Johannes Öhrlein, Bastian Grund, Andrea Hüser, Ralf Takors, and Bastian Blombach. Modular systems metabolic engineering enables balancing of relevant pathways for l-histidine production with corynebacterium glutamicum. Biotechnology for Biofuels, Mar 2019. URL: https://doi.org/10.1186/s13068-019-1410-2, doi:10.1186/s13068-019-1410-2. This article has 43 citations.

30. (read2021allostericinhibitionof pages 15-20): Benjamin J. Read, Gemma Fisher, Oliver L. R. Wissett, Teresa F. G. Machado, John Nicholson, John B. O. Mitchell, and Rafael G. da Silva. Allosteric inhibition of acinetobacter baumannii atp phosphoribosyltransferase by protein:dipeptide and protein:protein interactions. ACS infectious diseases, 8:197-209, Dec 2021. URL: https://doi.org/10.1021/acsinfecdis.1c00539, doi:10.1021/acsinfecdis.1c00539. This article has 7 citations and is from a peer-reviewed journal.

31. (read2021allostericinhibitionof pages 28-32): Benjamin J. Read, Gemma Fisher, Oliver L. R. Wissett, Teresa F. G. Machado, John Nicholson, John B. O. Mitchell, and Rafael G. da Silva. Allosteric inhibition of acinetobacter baumannii atp phosphoribosyltransferase by protein:dipeptide and protein:protein interactions. ACS infectious diseases, 8:197-209, Dec 2021. URL: https://doi.org/10.1021/acsinfecdis.1c00539, doi:10.1021/acsinfecdis.1c00539. This article has 7 citations and is from a peer-reviewed journal.

32. (carvalho2026activationoflhistidine pages 1-2): Luiz Pedro de Carvalho, Debbie Hunt, Joao Pisco, Angela Rodgers, Cesira de Chiara, Anisha Zaveri, Kamila Pacholarz, Dimitrios Evangelopoulos, Acely Garza-Garcia, Sabine Ehrt, Dirk Schnappinger, Perdita Barran, and Maximiliano Gutierrez. Activation of l-histidine biosynthesis as a new antibiotic strategy against mycobacterium tuberculosis. Nature Communications, Mar 2026. URL: https://doi.org/10.1038/s41467-026-70510-3, doi:10.1038/s41467-026-70510-3. This article has 0 citations and is from a highest quality peer-reviewed journal.

33. (srivastava2021currentpromisingtherapeutic pages 1-3): Shweta Srivastava, Neha Shree Maurya, Shikha Kushwah, and Ashutosh Mani. Current promising therapeutic targets for aspergillosis treatment. Journal of Pure and Applied Microbiology, pages 484-499, Apr 2021. URL: https://doi.org/10.22207/jpam.15.2.09, doi:10.22207/jpam.15.2.09. This article has 2 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](histidine_biosynthesis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](histidine_biosynthesis-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. schwentner2019modularsystemsmetabolic pages 2-4
2. khajeaian2022exploringtheevolution pages 25-32
3. khajeaian2022exploringtheevolution pages 5-8
4. duca2021thehistidinebiosynthetic pages 8-10
5. duca2021thehistidinebiosynthetic pages 5-6
6. gu2023peroxisomalcompartmentalizationof pages 8-9
7. gu2023peroxisomalcompartmentalizationof pages 1-2
8. read2021allostericinhibitionof pages 6-11
9. malykh2018specificfeaturesof pages 1-2
10. duca2023theoperonas pages 5-6
11. duca2021thehistidinebiosynthetic pages 2-3
12. khajeaian2022exploringtheevolution pages 15-19
13. duca2021thehistidinebiosynthetic pages 1-2
14. nagarajan2020thetimbarrel pages 8-11
15. romerorivera2022complexloopdynamics pages 1-2
16. lundin2020mutationalpathwaysand pages 1-2
17. schwentner2019modularsystemsmetabolic pages 1-2
18. carvalho2026activationoflhistidine pages 1-2
19. srivastava2021currentpromisingtherapeutic pages 1-3
20. malykh2018specificfeaturesof pages 13-14
21. wu2020highlyefficientproduction pages 11-14
22. wu2020highlyefficientproduction pages 4-8
23. malykh2018specificfeaturesof pages 12-13
24. read2021allostericinhibitionof pages 1-6
25. read2023crystalstructuresteadystate pages 1-2
26. duca2023theoperonas pages 12-14
27. fisher2022allostericrescueof pages 1-2
28. gu2023peroxisomalcompartmentalizationof pages 5-6
29. wu2020highlyefficientproduction pages 8-11
30. wu2020highlyefficientproduction pages 1-4
31. schwentner2019modularsystemsmetabolic pages 7-9
32. read2021allostericinhibitionof pages 15-20
33. read2021allostericinhibitionof pages 28-32
34. (5-phosphoribosylamino)methylideneamino
35. https://doi.org/10.1021/acssynbio.0c00163,
36. https://doi.org/10.3390/genes14040949,
37. https://doi.org/10.26686/wgtn.19709419,
38. https://doi.org/10.1038/s41467-023-41347-x,
39. https://doi.org/10.3390/microorganisms9071439,
40. https://doi.org/10.1186/s13068-019-1410-2,
41. https://doi.org/10.1186/s12934-018-0890-2,
42. https://doi.org/10.3389/fmicb.2020.588235,
43. https://doi.org/10.1021/jacsau.2c00063,
44. https://doi.org/10.1021/acsinfecdis.1c00539,
45. https://doi.org/10.1021/acs.biochem.3c00551,
46. https://doi.org/10.15347/wjs/2020.004,
47. https://doi.org/10.1038/s41467-022-34960-9,
48. https://doi.org/10.1038/s41467-026-70510-3,
49. https://doi.org/10.22207/jpam.15.2.09,