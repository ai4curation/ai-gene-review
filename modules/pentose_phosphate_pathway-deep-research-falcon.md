---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T12:48:01.117819'
end_time: '2026-07-06T13:13:52.252192'
duration_seconds: 1551.13
template_file: templates/module_research.md.j2
template_variables:
  module_title: Pentose phosphate pathway
  module_summary: A taxon-neutral module for the oxidative and non-oxidative pentose
    phosphate pathway (PPP). The oxidative branch converts glucose 6-phosphate to
    ribulose 5-phosphate while producing NADPH and CO2. The non-oxidative branch interconverts
    ribulose 5-phosphate, ribose 5-phosphate, xylulose 5-phosphate, sedoheptulose
    7-phosphate, glyceraldehyde 3-phosphate, fructose 6-phosphate, and erythrose 4-phosphate
    through epimerase, isomerase, transketolase, and transaldolase reactions. Bacterial
    pathway maps often include adjacent Entner-Doudoroff, gluconate, ribose/PRPP,
    amino-sugar, riboflavin, and MEP-pathway nodes; these share metabolites with the
    PPP but are not strict PPP steps.
  module_outline: "- Pentose phosphate pathway\n  - 1. glucose 6-phosphate oxidation\n\
    \  - Glucose 6-phosphate to 6-phosphoglucono-delta-lactone\n    - Glucose-6-phosphate\
    \ dehydrogenase (molecular player: glucose-6-phosphate dehydrogenase activity;\
    \ activity or role: glucose-6-phosphate dehydrogenase activity)\n  - 2. phosphogluconolactone\
    \ hydrolysis\n  - 6-phosphoglucono-delta-lactone to 6-phosphogluconate\n    -\
    \ 6-phosphogluconolactonase (molecular player: 6-phosphogluconolactonase activity;\
    \ activity or role: 6-phosphogluconolactonase activity)\n  - 3. 6-phosphogluconate\
    \ oxidative decarboxylation\n  - 6-phosphogluconate to ribulose 5-phosphate\n\
    \    - 6-phosphogluconate dehydrogenase (molecular player: phosphogluconate dehydrogenase\
    \ (decarboxylating) activity; activity or role: phosphogluconate dehydrogenase\
    \ (decarboxylating) activity)\n  - 4. ribulose 5-phosphate interconversion\n \
    \ - Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate\n    -\
    \ Alternative versions by product identity: Ribulose 5-phosphate product variants\n\
    \      - Ribose 5-phosphate isomerase route\n        - Ribose-5-phosphate isomerase\
    \ (molecular player: ribose-5-phosphate isomerase activity; activity or role:\
    \ ribose-5-phosphate isomerase activity)\n      - Ribulose-phosphate 3-epimerase\
    \ route\n        - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate\
    \ 3-epimerase activity; activity or role: ribulose-phosphate 3-epimerase activity)\n\
    \  - 5. non-oxidative carbon rearrangement\n  - Reversible sugar-phosphate rearrangements\n\
    \    - Transketolase (molecular player: transketolase activity; activity or role:\
    \ transketolase activity)\n    - Transaldolase (molecular player: transaldolase\
    \ activity; activity or role: transaldolase activity)\n  - 6. adjacent ribose\
    \ and PRPP metabolism\n  - Ribose and PRPP side inputs\n    - Ribokinase (molecular\
    \ player: ribokinase activity; activity or role: ribokinase activity)\n    - Ribose-phosphate\
    \ diphosphokinase / PRPP synthase (molecular player: ribose phosphate diphosphokinase\
    \ activity; activity or role: ribose phosphate diphosphokinase activity)"
  module_connections: '- Glucose 6-phosphate to 6-phosphoglucono-delta-lactone precedes
    6-phosphoglucono-delta-lactone to 6-phosphogluconate: 6-phosphogluconolactone
    produced by G6PD is hydrolyzed by 6-phosphogluconolactonase.

    - 6-phosphoglucono-delta-lactone to 6-phosphogluconate precedes 6-phosphogluconate
    to ribulose 5-phosphate: 6-phosphogluconate enters oxidative decarboxylation to
    ribulose 5-phosphate.

    - 6-phosphogluconate to ribulose 5-phosphate precedes Ribulose 5-phosphate to
    ribose 5-phosphate and xylulose 5-phosphate: Ribulose 5-phosphate is converted
    to ribose 5-phosphate or xylulose 5-phosphate.

    - Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate precedes
    Reversible sugar-phosphate rearrangements: Ribose 5-phosphate and xylulose 5-phosphate
    feed reversible transketolase/transaldolase reactions.

    - Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate feeds into
    Ribose and PRPP side inputs: Ribose 5-phosphate can be diverted to ribose salvage
    and PRPP-dependent biosynthesis.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 53
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 3
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: pentose_phosphate_pathway-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: pentose_phosphate_pathway-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: pentose_phosphate_pathway-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: image-1.png
  path: pentose_phosphate_pathway-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: 'Image artifact created (ID artifact-02): ''Pentose Phosphate Pathway
    Schematic'' ![Pentose Phosphate Pathway Schematic](artifact:artifact-02) Artifact
    IDs that ma'
---

## Question

# Commissioned Review Brief

## Review Topic

Pentose phosphate pathway

## Working Scope

A taxon-neutral module for the oxidative and non-oxidative pentose phosphate pathway (PPP). The oxidative branch converts glucose 6-phosphate to ribulose 5-phosphate while producing NADPH and CO2. The non-oxidative branch interconverts ribulose 5-phosphate, ribose 5-phosphate, xylulose 5-phosphate, sedoheptulose 7-phosphate, glyceraldehyde 3-phosphate, fructose 6-phosphate, and erythrose 4-phosphate through epimerase, isomerase, transketolase, and transaldolase reactions. Bacterial pathway maps often include adjacent Entner-Doudoroff, gluconate, ribose/PRPP, amino-sugar, riboflavin, and MEP-pathway nodes; these share metabolites with the PPP but are not strict PPP steps.

## Provisional Biological Outline

- Pentose phosphate pathway
  - 1. glucose 6-phosphate oxidation
  - Glucose 6-phosphate to 6-phosphoglucono-delta-lactone
    - Glucose-6-phosphate dehydrogenase (molecular player: glucose-6-phosphate dehydrogenase activity; activity or role: glucose-6-phosphate dehydrogenase activity)
  - 2. phosphogluconolactone hydrolysis
  - 6-phosphoglucono-delta-lactone to 6-phosphogluconate
    - 6-phosphogluconolactonase (molecular player: 6-phosphogluconolactonase activity; activity or role: 6-phosphogluconolactonase activity)
  - 3. 6-phosphogluconate oxidative decarboxylation
  - 6-phosphogluconate to ribulose 5-phosphate
    - 6-phosphogluconate dehydrogenase (molecular player: phosphogluconate dehydrogenase (decarboxylating) activity; activity or role: phosphogluconate dehydrogenase (decarboxylating) activity)
  - 4. ribulose 5-phosphate interconversion
  - Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate
    - Alternative versions by product identity: Ribulose 5-phosphate product variants
      - Ribose 5-phosphate isomerase route
        - Ribose-5-phosphate isomerase (molecular player: ribose-5-phosphate isomerase activity; activity or role: ribose-5-phosphate isomerase activity)
      - Ribulose-phosphate 3-epimerase route
        - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity or role: ribulose-phosphate 3-epimerase activity)
  - 5. non-oxidative carbon rearrangement
  - Reversible sugar-phosphate rearrangements
    - Transketolase (molecular player: transketolase activity; activity or role: transketolase activity)
    - Transaldolase (molecular player: transaldolase activity; activity or role: transaldolase activity)
  - 6. adjacent ribose and PRPP metabolism
  - Ribose and PRPP side inputs
    - Ribokinase (molecular player: ribokinase activity; activity or role: ribokinase activity)
    - Ribose-phosphate diphosphokinase / PRPP synthase (molecular player: ribose phosphate diphosphokinase activity; activity or role: ribose phosphate diphosphokinase activity)

## Known Relationships Among Steps

- Glucose 6-phosphate to 6-phosphoglucono-delta-lactone precedes 6-phosphoglucono-delta-lactone to 6-phosphogluconate: 6-phosphogluconolactone produced by G6PD is hydrolyzed by 6-phosphogluconolactonase.
- 6-phosphoglucono-delta-lactone to 6-phosphogluconate precedes 6-phosphogluconate to ribulose 5-phosphate: 6-phosphogluconate enters oxidative decarboxylation to ribulose 5-phosphate.
- 6-phosphogluconate to ribulose 5-phosphate precedes Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate: Ribulose 5-phosphate is converted to ribose 5-phosphate or xylulose 5-phosphate.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate precedes Reversible sugar-phosphate rearrangements: Ribose 5-phosphate and xylulose 5-phosphate feed reversible transketolase/transaldolase reactions.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate feeds into Ribose and PRPP side inputs: Ribose 5-phosphate can be diverted to ribose salvage and PRPP-dependent biosynthesis.

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

Pentose phosphate pathway

## Working Scope

A taxon-neutral module for the oxidative and non-oxidative pentose phosphate pathway (PPP). The oxidative branch converts glucose 6-phosphate to ribulose 5-phosphate while producing NADPH and CO2. The non-oxidative branch interconverts ribulose 5-phosphate, ribose 5-phosphate, xylulose 5-phosphate, sedoheptulose 7-phosphate, glyceraldehyde 3-phosphate, fructose 6-phosphate, and erythrose 4-phosphate through epimerase, isomerase, transketolase, and transaldolase reactions. Bacterial pathway maps often include adjacent Entner-Doudoroff, gluconate, ribose/PRPP, amino-sugar, riboflavin, and MEP-pathway nodes; these share metabolites with the PPP but are not strict PPP steps.

## Provisional Biological Outline

- Pentose phosphate pathway
  - 1. glucose 6-phosphate oxidation
  - Glucose 6-phosphate to 6-phosphoglucono-delta-lactone
    - Glucose-6-phosphate dehydrogenase (molecular player: glucose-6-phosphate dehydrogenase activity; activity or role: glucose-6-phosphate dehydrogenase activity)
  - 2. phosphogluconolactone hydrolysis
  - 6-phosphoglucono-delta-lactone to 6-phosphogluconate
    - 6-phosphogluconolactonase (molecular player: 6-phosphogluconolactonase activity; activity or role: 6-phosphogluconolactonase activity)
  - 3. 6-phosphogluconate oxidative decarboxylation
  - 6-phosphogluconate to ribulose 5-phosphate
    - 6-phosphogluconate dehydrogenase (molecular player: phosphogluconate dehydrogenase (decarboxylating) activity; activity or role: phosphogluconate dehydrogenase (decarboxylating) activity)
  - 4. ribulose 5-phosphate interconversion
  - Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate
    - Alternative versions by product identity: Ribulose 5-phosphate product variants
      - Ribose 5-phosphate isomerase route
        - Ribose-5-phosphate isomerase (molecular player: ribose-5-phosphate isomerase activity; activity or role: ribose-5-phosphate isomerase activity)
      - Ribulose-phosphate 3-epimerase route
        - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity or role: ribulose-phosphate 3-epimerase activity)
  - 5. non-oxidative carbon rearrangement
  - Reversible sugar-phosphate rearrangements
    - Transketolase (molecular player: transketolase activity; activity or role: transketolase activity)
    - Transaldolase (molecular player: transaldolase activity; activity or role: transaldolase activity)
  - 6. adjacent ribose and PRPP metabolism
  - Ribose and PRPP side inputs
    - Ribokinase (molecular player: ribokinase activity; activity or role: ribokinase activity)
    - Ribose-phosphate diphosphokinase / PRPP synthase (molecular player: ribose phosphate diphosphokinase activity; activity or role: ribose phosphate diphosphokinase activity)

## Known Relationships Among Steps

- Glucose 6-phosphate to 6-phosphoglucono-delta-lactone precedes 6-phosphoglucono-delta-lactone to 6-phosphogluconate: 6-phosphogluconolactone produced by G6PD is hydrolyzed by 6-phosphogluconolactonase.
- 6-phosphoglucono-delta-lactone to 6-phosphogluconate precedes 6-phosphogluconate to ribulose 5-phosphate: 6-phosphogluconate enters oxidative decarboxylation to ribulose 5-phosphate.
- 6-phosphogluconate to ribulose 5-phosphate precedes Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate: Ribulose 5-phosphate is converted to ribose 5-phosphate or xylulose 5-phosphate.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate precedes Reversible sugar-phosphate rearrangements: Ribose 5-phosphate and xylulose 5-phosphate feed reversible transketolase/transaldolase reactions.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate feeds into Ribose and PRPP side inputs: Ribose 5-phosphate can be diverted to ribose salvage and PRPP-dependent biosynthesis.

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

# The Pentose Phosphate Pathway: A Comprehensive Review of Mechanism, Variation, and Evolutionary Origins

## 1. Executive Summary

The pentose phosphate pathway (PPP) is a central metabolic route that operates in parallel to glycolysis, converting glucose 6-phosphate into NADPH and various sugar phosphates. The pathway consists of two functionally and thermodynamically distinct branches: an irreversible oxidative branch (oxPPP) that generates two molecules of NADPH per glucose 6-phosphate consumed, and a reversible non-oxidative branch (non-oxPPP) that interconverts three- to seven-carbon sugar phosphates through transketolase and transaldolase reactions (teslaa2023thepentosephosphate pages 3-4, bertels2021thepentosephosphate pages 1-3). The PPP is among the most ancient metabolic pathways, with the non-oxidative branch predating the oxidative branch and potentially originating from prebiotic, non-enzymatic reaction sequences catalyzed by ferrous iron under Archean ocean conditions (piedrafita2021cysteineandiron pages 2-3, seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6). Across the tree of life, the pathway shows remarkable variation: most archaea lack a classical oxidative PPP, many gut bacteria have replaced transaldolase with the sedoheptulose-1,7-bisphosphate bypass pathway, and plants have elaborated the non-oxidative chemistry into the Calvin–Benson cycle with dual compartmentalization between cytosol and plastids (masi2021thepentosephosphate pages 1-2, garschagen2021analternativepentose pages 2-3, sharkey2021pentosephosphatepathway pages 1-4). In mammals, the PPP serves critical functions in redox homeostasis, nucleotide biosynthesis, and immune defense, while dysregulation of PPP enzymes—particularly glucose-6-phosphate dehydrogenase (G6PD)—underlies diseases ranging from hemolytic anemia to cancer (meng2022recentfindingsin pages 1-2, bertels2021thepentosephosphate pages 12-13). This review synthesizes current understanding of the pathway's boundaries, core mechanism, evolutionary origins, lineage-specific variation, and unresolved questions.

## 2. Definition and Biological Boundaries

### 2.1 What the PPP Includes

The pentose phosphate pathway, in its strict definition, encompasses six to seven enzymatic activities organized into two branches. The **oxidative branch** comprises three sequential, essentially irreversible reactions: (i) the oxidation of glucose 6-phosphate to 6-phosphoglucono-δ-lactone by glucose-6-phosphate dehydrogenase (G6PD; EC 1.1.1.49), (ii) the hydrolysis of the lactone to 6-phosphogluconate by 6-phosphogluconolactonase (6PGL; EC 3.1.1.31), and (iii) the oxidative decarboxylation of 6-phosphogluconate to ribulose 5-phosphate by 6-phosphogluconate dehydrogenase (6PGD; EC 1.1.1.44) (berneburg2023nadphproducingenzymesfrom pages 24-26, teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6). The **non-oxidative branch** includes reversible interconversion reactions: (iv) isomerization of ribulose 5-phosphate to ribose 5-phosphate by ribose-5-phosphate isomerase (RPI; EC 5.3.1.6), (v) epimerization of ribulose 5-phosphate to xylulose 5-phosphate by ribulose-phosphate 3-epimerase (RPE; EC 5.1.3.1), and the carbon-rearrangement reactions catalyzed by (vi) transketolase (TKT; EC 2.2.1.1) and (vii) transaldolase (TAL; EC 2.2.1.2) (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3).

The overall stoichiometry of the pathway, when operating in its canonical catabolic mode, can be summarized as: 3 glucose 6-phosphate + 6 NADP⁺ → 2 fructose 6-phosphate + glyceraldehyde 3-phosphate + 3 CO₂ + 6 NADPH (teslaa2023thepentosephosphate pages 3-4).

The following schematic illustrates the core reactions of both branches and their connections to glycolysis:

![Pentose Phosphate Pathway Schematic](artifact:artifact-02)

*Image: Schematic overview of the pentose phosphate pathway showing the oxidative branch that generates NADPH and CO2 and the non-oxidative branch that interconverts pentose phosphates with glycolytic intermediates. Oxidative steps are colored blue and non-oxidative steps green, with enzymes, metabolites, and glycolysis connections clearly labeled.*

### 2.2 Neighboring Pathways That Are Not Part of the PPP

Several metabolic modules share metabolites with the PPP but should be treated as distinct:

- **Glycolysis (Embden-Meyerhof-Parnas pathway):** Provides glucose 6-phosphate as the PPP input and receives fructose 6-phosphate and glyceraldehyde 3-phosphate as non-oxidative PPP outputs, but constitutes a separate pathway (bertels2021thepentosephosphate pages 1-3, bertels2021thepentosephosphate pages 3-4).
- **Entner-Doudoroff pathway:** Shares 6-phosphogluconate as an intermediate but processes it via 2-keto-3-deoxy-6-phosphogluconate rather than through the PPP's oxidative decarboxylation (santanamolina2025chimericoriginsand pages 4-5).
- **PRPP biosynthesis and nucleotide metabolism:** PRPP synthase (ribose-phosphate diphosphokinase; EC 2.7.6.1) converts ribose 5-phosphate to 5-phosphoribosyl-1-pyrophosphate (PRPP), which is essential for purine, pyrimidine, histidine, tryptophan, and NAD biosynthesis. This is a downstream consumer of PPP products, not a PPP step per se (santanamolina2025chimericoriginsand pages 4-5).
- **Ribose salvage:** Ribokinase (EC 2.7.1.15) phosphorylates free ribose to ribose 5-phosphate, providing an exogenous input to the PPP metabolite pool. It is an accessory input, not a core PPP reaction (teslaa2023thepentosephosphate pages 3-4).
- **Calvin-Benson cycle:** In photosynthetic organisms, the non-oxidative PPP chemistry is incorporated into the Calvin cycle with key modifications (replacement of transaldolase by aldolase + SBPase), but the Calvin cycle as a whole encompasses CO₂ fixation by RuBisCO and is best considered a distinct—though overlapping—pathway (sharkey2021pentosephosphatepathway pages 1-4, sharkey2021pentosephosphatepathway pages 4-5).

The complete catalog of PPP enzymes and adjacent accessory reactions is summarized below:

| Branch | Enzyme | EC number | Gene name (E. coli / human) | Reaction catalyzed | Major cofactors / requirements | Step status in canonical PPP | Notes |
|---|---|---|---|---|---|---|---|
| Oxidative PPP | Glucose-6-phosphate dehydrogenase (G6PD) | 1.1.1.49 | **zwf** / **G6PD** | Glucose-6-phosphate + NADP+ → 6-phosphoglucono-δ-lactone + NADPH + H+ | NADP+; catalytic activity depends on oligomeric state in many systems | Obligatory entry step; effectively irreversible | First committed and rate-limiting oxidative PPP step; major control point for NADPH production (teslaa2023thepentosephosphate pages 3-4, meng2022recentfindingsin pages 1-2, meng2022recentfindingsin pages 5-6) |
| Oxidative PPP | 6-Phosphogluconolactonase (6PGL, PGL) | 3.1.1.31 | **pgl** / **PGLS** | 6-Phosphoglucono-δ-lactone + H2O → 6-phosphogluconate | H2O | Obligatory in canonical oxidative PPP; hydrolytic, near-irreversible in pathway context | Accelerates lactone hydrolysis and limits buildup of reactive lactone intermediate (berneburg2023nadphproducingenzymesfrom pages 24-26, seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6) |
| Oxidative PPP | 6-Phosphogluconate dehydrogenase (6PGD) | 1.1.1.44 | **gnd** / **PGD** | 6-Phosphogluconate + NADP+ → ribulose-5-phosphate + CO2 + NADPH | NADP+; divalent cation dependence reported in many organisms | Obligatory in canonical oxidative PPP; irreversible because of decarboxylation | Produces the second NADPH and commits carbon to pentose formation with CO2 loss (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3, seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6) |
| Non-oxidative PPP | Ribose-5-phosphate isomerase (RPI) | 5.3.1.6 | **rpiA, rpiB** / **RPIA** | Ribulose-5-phosphate ⇌ ribose-5-phosphate | None required for chemistry itself | Conditional branch step; reversible | Supplies ribose-5-phosphate for nucleotide synthesis; alternative bacterial isoenzymes exist (RpiA/RpiB) (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3) |
| Non-oxidative PPP | Ribulose-phosphate 3-epimerase (RPE, RuPE) | 5.1.3.1 | **rpe** / **RPE** | Ribulose-5-phosphate ⇌ xylulose-5-phosphate | Often metal-assisted in enzyme family | Conditional branch step; reversible | Generates xylulose-5-phosphate for transketolase reactions (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3) |
| Non-oxidative PPP | Transketolase (TKT, TK) | 2.2.1.1 | **tktA, tktB** / **TKT** | Transfers a 2-carbon ketol unit among sugar phosphates; key reactions include xylulose-5-phosphate + ribose-5-phosphate ⇌ glyceraldehyde-3-phosphate + sedoheptulose-7-phosphate and xylulose-5-phosphate + erythrose-4-phosphate ⇌ fructose-6-phosphate + glyceraldehyde-3-phosphate | Thiamine diphosphate (ThDP/TPP), Mg2+ or similar divalent cation | Core carbon-rearrangement step; reversible | Major connector between pentose phosphates and glycolytic intermediates; key non-oxidative control node (teslaa2023thepentosephosphate pages 3-4, qiao2025thepentosephosphate pages 1-3, sharkey2021pentosephosphatepathway pages 5-7) |
| Non-oxidative PPP | Transaldolase (TAL, TALDO) | 2.2.1.2 | **talA, talB** / **TALDO1** | Sedoheptulose-7-phosphate + glyceraldehyde-3-phosphate ⇌ erythrose-4-phosphate + fructose-6-phosphate | Schiff-base chemistry via catalytic Lys; no external cofactor | Core carbon-rearrangement step; reversible | Canonical non-oxidative PPP enzyme, but absent in some taxa that use bypass routes such as the sedoheptulose-1,7-bisphosphate pathway (teslaa2023thepentosephosphate pages 3-4, garschagen2021analternativepentose pages 1-2, seregina2025ribose5phosphatemetabolismprotects pages 1-3) |
| Adjacent / accessory | Ribokinase | 2.7.1.15 | **rbsK** / **RBKS** | Ribose + ATP → ribose-5-phosphate + ADP | ATP, Mg2+ | Not a PPP step; accessory ribose salvage input | Feeds ribose salvage into the PPP metabolite pool at ribose-5-phosphate; should be treated as adjacent rather than core PPP (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3) |
| Adjacent / accessory | Ribose-phosphate diphosphokinase (PRPP synthase) | 2.7.6.1 | **prs** / **PRPS1, PRPS2** | Ribose-5-phosphate + ATP → 5-phosphoribosyl-1-pyrophosphate (PRPP) + AMP | ATP, Mg2+, inorganic phosphate in many systems | Not a PPP step; downstream biosynthetic branchpoint | Consumes PPP-derived ribose-5-phosphate for nucleotide, histidine, tryptophan, and NAD biosynthesis; best considered a side-output node, not part of the strict PPP (teslaa2023thepentosephosphate pages 3-4, santanamolina2025chimericoriginsand pages 4-5) |


*Table: This table summarizes the canonical oxidative and non-oxidative pentose phosphate pathway enzymes, plus closely adjacent ribose/PRPP nodes often shown on pathway maps. It is useful for separating strict PPP steps from accessory salvage and biosynthetic reactions while showing reactions, cofactors, reversibility, and representative bacterial/human genes.*

## 3. Mechanistic Overview

### 3.1 The Oxidative Branch: NADPH Production and Carbon Commitment

The oxidative branch is a linear, essentially irreversible sequence. **G6PD** catalyzes the first committed step, oxidizing glucose 6-phosphate to 6-phosphoglucono-δ-lactone with concomitant reduction of NADP⁺ to NADPH (teslaa2023thepentosephosphate pages 3-4, qiao2025thepentosephosphate pages 1-3). This enzyme functions as an obligate homodimer or homotetramer; the monomeric form is catalytically inactive (teslaa2023thepentosephosphate pages 6-8). The lactone intermediate is hydrolyzed by **6-phosphogluconolactonase** (6PGL) to yield 6-phosphogluconate (seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6). While this hydrolysis can occur spontaneously, the enzymatic reaction is important to prevent accumulation of the reactive lactone and to channel flux efficiently (berneburg2023nadphproducingenzymesfrom pages 24-26). The final oxidative step, catalyzed by **6-phosphogluconate dehydrogenase** (6PGD), performs an oxidative decarboxylation: 6-phosphogluconate is converted to ribulose 5-phosphate with release of CO₂ and production of a second NADPH (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3). The decarboxylation renders this step irreversible under physiological conditions, committing carbon irretrievably to the pentose phosphate pool.

### 3.2 The Non-Oxidative Branch: Reversible Carbon Rearrangement

The non-oxidative branch is thermodynamically reversible and operates bidirectionally depending on metabolic demand. **Ribose-5-phosphate isomerase** (RPI) and **ribulose-phosphate 3-epimerase** (RPE) interconvert ribulose 5-phosphate with ribose 5-phosphate and xylulose 5-phosphate, respectively (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3). These pentose phosphates then serve as substrates for two carbon-transferring enzymes:

- **Transketolase** (TKT) uses thiamine diphosphate (ThDP) as a cofactor and catalyzes the transfer of a two-carbon glycolaldehyde unit from a ketose donor to an aldose acceptor via a ping-pong mechanism (sharkey2021pentosephosphatepathway pages 5-7). The two canonical transketolase reactions convert xylulose 5-phosphate + ribose 5-phosphate → sedoheptulose 7-phosphate + glyceraldehyde 3-phosphate, and xylulose 5-phosphate + erythrose 4-phosphate → fructose 6-phosphate + glyceraldehyde 3-phosphate (teslaa2023thepentosephosphate pages 3-4, sharkey2021pentosephosphatepathway pages 5-7).

- **Transaldolase** (TAL) catalyzes the transfer of a three-carbon dihydroxyacetone unit from sedoheptulose 7-phosphate to glyceraldehyde 3-phosphate, producing erythrose 4-phosphate and fructose 6-phosphate via Schiff-base chemistry with a catalytic lysine residue (teslaa2023thepentosephosphate pages 3-4).

The net effect of the non-oxidative branch, operating in the catabolic direction, is the recycling of pentose phosphates into glycolytic intermediates (fructose 6-phosphate and glyceraldehyde 3-phosphate), allowing carbon to re-enter glycolysis or be re-oxidized through the oxidative PPP (bertels2021thepentosephosphate pages 1-3).

### 3.3 Regulation

The primary regulatory control point is G6PD, which is regulated at multiple levels:

- **NADPH/NADP⁺ ratio:** The most immediate control mechanism. NADPH is a potent product inhibitor that converts active G6PD dimers to inactive monomers; when NADPH is consumed during oxidative stress, the resulting increase in NADP⁺ concentration rapidly activates the enzyme and drives oxPPP flux (meng2022recentfindingsin pages 5-6, teslaa2023thepentosephosphate pages 4-6).

- **Post-translational modifications (PTMs):** G6PD activity is modulated by phosphorylation at multiple residues (including S40, Y112, Y401, T406, T466) by kinases such as Src family members, SIK3, and polo-like kinase 1 (meng2022recentfindingsin pages 5-6). O-GlcNAcylation at serine 84 dramatically increases activity. Acetylation generally inhibits G6PD, while deacetylation by Sirt2 enhances activity. Ubiquitination and glutarylation also regulate protein stability and function (meng2022recentfindingsin pages 5-6, meng2022recentfindingsin pages 2-5).

- **Transcriptional regulation:** Multiple transcription factors—including Nrf2, NF-κB, c-MYC, p53, STAT3, and TAp73—regulate G6PD expression. The tumor suppressor PTEN negatively regulates G6PD through multiple mechanisms, including inhibition of dimerization (meng2022recentfindingsin pages 2-5, qiao2025thepentosephosphate pages 4-6).

- **Metabolic cross-talk with glycolysis:** During oxidative stress, glycolytic enzymes GAPDH and PKM2 are inactivated by cysteine oxidation, redirecting glucose 6-phosphate toward the PPP. The p53-induced phosphatase TIGAR promotes PPP flux by dephosphorylating fructose 2,6-bisphosphate, reducing phosphofructokinase activity and thus diverting carbon to the PPP (teslaa2023thepentosephosphate pages 4-6).

## 4. Major Molecular Players and Active Assemblies

The enzymes of the PPP and their properties are summarized in the artifact table above (artifact-00). Several features merit emphasis:

**G6PD oligomeric regulation.** Human G6PD is active as a homodimer and most active as a homotetramer. Class I G6PD mutations, which cause the most severe enzyme deficiency, disrupt the dimer interface and the allosteric NADPH-binding site, suggesting that NADPH serves both as a product and as a structural stabilizer (teslaa2023thepentosephosphate pages 6-8).

**Bifunctional enzyme fusions.** In *Plasmodium* species, G6PD and 6PGL are fused into a single bifunctional enzyme called GluPho, representing a lineage-specific domain fusion not seen in mammals or bacteria (berneburg2023nadphproducingenzymesfrom pages 24-26).

**Paralogous enzymes in bacteria.** *Escherichia coli* possesses two transketolase genes (*tktA*, *tktB*) and two transaldolase genes (*talA*, *talB*), providing functional redundancy (seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3, seregina2025ribose5phosphatemetabolismprotects pages 1-3). Similarly, two ribose-5-phosphate isomerase isoforms (RpiA, RpiB) exist in bacteria with partially overlapping function (teslaa2023thepentosephosphate pages 3-4).

**Thiamine dependence of transketolase.** Transketolase requires thiamine diphosphate (ThDP/TPP) as a cofactor, making its activity dependent on vitamin B₁ availability. Thiamine deficiency results in reduced transketolase activity and has been historically associated with Wernicke-Korsakoff syndrome (bertels2021thepentosephosphate pages 12-13, sharkey2021pentosephosphatepathway pages 5-7).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Prebiotic Origins

The PPP has deep prebiotic roots. Nonenzymatic reaction sequences that topologically resemble both glycolysis and the PPP have been demonstrated under simulated Archean ocean conditions, using ferrous iron (the most abundant transition metal in Archean sediments) as catalyst (piedrafita2021cysteineandiron pages 2-3, piedrafita2021cysteineandiron pages 1-2). A rate-limiting step—the conversion of 6-phosphogluconate to ribose 5-phosphate—does not proceed in water alone but is accelerated by the proteinogenic amino acid cysteine in conjunction with iron, forming a ternary complex that enhances the reaction under mild, metabolism-typical conditions (piedrafita2021cysteineandiron pages 2-3, piedrafita2021cysteineandiron pages 1-2). This supports a "metabolism first" model in which non-enzymatic reaction sequences were gradually enzymatized, imprinting their structure on the evolving metabolic network (piedrafita2021cysteineandiron pages 1-2, maeda2021evolutionaryhistoryof pages 5-6).

### 5.2 Ancient Non-Oxidative Branch, Later Oxidative Elaboration

The non-oxidative branch appears to be the more ancient component of the PPP, conserved across archaea, bacteria, and eukaryotes, whereas the oxidative branch emerged later, likely after the Great Oxygenation Event created a need for NADPH-dependent antioxidant defense (seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6, masi2021thepentosephosphate pages 1-2). Most archaea lack a complete oxidative PPP but retain at least partial non-oxidative chemistry, sometimes operating in reverse to synthesize ribose 5-phosphate from fructose 6-phosphate and glyceraldehyde 3-phosphate (seregina2025biosynthesisofribose5phosphate—metabolic pages 3-5, masi2021thepentosephosphate pages 1-2). Some archaea—notably certain haloarchaea such as *Haloferax volcanii*—do possess G6PD and 6PGD, representing exceptions to the general archaeal pattern (bertels2021thepentosephosphate pages 3-4).

### 5.3 Chimeric Eukaryotic Origins

Phylogenetic analysis of eukaryotic central carbon metabolism genes reveals chimeric origins, with PPP enzymes derived from multiple prokaryotic sources. Several PPP enzymes (RPE, RPIA, TKT, PRPS) show topologies consistent with cyanobacterial origin through endosymbiotic gene transfer, while PRPS also shows possible alphaproteobacterial contributions (santanamolina2025chimericoriginsand pages 4-5, santanamolina2025chimericoriginsand pages 5-6). Some enzymes, particularly RPIA, show a eukaryotic cluster branching next to Asgardarchaeota, suggesting an archaeal contribution to certain PPP components in the last eukaryotic common ancestor (LECA) (santanamolina2025chimericoriginsand pages 4-5, santanamolina2025chimericoriginsand pages 3-4).

### 5.4 Lineage-Specific Variation

The variation of the PPP across major taxa is summarized in the following table:

| Lineage/Domain | Oxidative PPP status | Non-oxidative PPP status | Notable variations / alternative routes | Key references |
|---|---|---|---|---|
| **Bacteria (canonical model: _E. coli_)** | Canonical oxPPP present: G6PD (Zwf), 6PGL (Pgl), and 6PGD (Gnd) generate NADPH and ribulose-5-phosphate; branch is effectively irreversible because of decarboxylation | Canonical non-oxPPP present and reversible: Rpi, Rpe, Tkt, Tal interconvert pentose phosphates with F6P/GAP | Standard textbook PPP organization; oxidative and non-oxidative branches can operate together or, under some conditions, non-oxPPP can run in reverse to support ribose-5-phosphate synthesis and stress responses (seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3, seregina2025ribose5phosphatemetabolismprotects pages 1-3) | TeSlaa et al. 2023; Seregina et al. 2025 (teslaa2023thepentosephosphate pages 3-4, seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3, seregina2025ribose5phosphatemetabolismprotects pages 1-3) |
| **Bacteria (gut-associated TAL-lacking lineages, e.g. _Prevotella copri_)** | Often retain oxidative reactions, but pathway usage is coupled to specialized pentose assimilation strategies | Canonical non-oxPPP is incomplete in many taxa because **transaldolase is absent** | Use the **sedoheptulose-1,7-bisphosphate pathway (SBPP)** as a transaldolase bypass: PFK phosphorylates S7P, then aldolase cleaves S1,7BP to connect pentose use with glycolysis; this route is widespread in several gut bacterial phyla (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 1-2) | Garschagen et al. 2021; Seregina et al. 2025 (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 1-2, seregina2025ribose5phosphatemetabolismprotects pages 1-3) |
| **Archaea** | Usually **absent or incomplete**; most archaea lack a classical complete oxPPP, though some enzymes occur in specific groups such as haloarchaea | Non-oxPPP chemistry is more ancient/conserved than oxPPP, but many archaea use incomplete or modified forms rather than the full canonical pathway | Pentose synthesis can proceed through reverse non-oxPPP or alternative routes such as the **ribulose monophosphate (RuMP/RMP) pathway**; haloarchaea are notable exceptions with some oxPPP enzymes (seregina2025biosynthesisofribose5phosphate—metabolic pages 3-5, masi2021thepentosephosphate pages 1-2, bertels2021thepentosephosphate pages 3-4) | Masi et al. 2021; Bertels et al. 2021; Seregina et al. 2025 (seregina2025biosynthesisofribose5phosphate—metabolic pages 3-5, masi2021thepentosephosphate pages 1-2, bertels2021thepentosephosphate pages 3-4) |
| **Eukaryotes (general)** | Present in LECA-derived metabolism but of **chimeric evolutionary origin**; eukaryotic oxPPP enzymes derive from mixed archaeal and bacterial sources depending on enzyme family | Present broadly; non-oxPPP is conserved across eukaryotes but can be retargeted and rewired between compartments | Phylogenetic analyses support mixed ancestry, with contributions from Asgard-related archaeal lineages and bacterial endosymbiotic gene transfer, especially cyanobacterial contributions for several PPP-associated enzymes (santanamolina2025chimericoriginsand pages 4-5, santanamolina2025chimericoriginsand pages 5-6, santanamolina2025chimericoriginsand pages 3-4) | Santana-Molina et al. 2025 (santanamolina2025chimericoriginsand pages 4-5, santanamolina2025chimericoriginsand pages 5-6, santanamolina2025chimericoriginsand pages 3-4) |
| **Mammals** | Canonical oxPPP operates mainly in the **cytosol**; G6PD is the committed/rate-limiting step and a major control point for NADPH supply | Canonical reversible non-oxPPP links ribose production with glycolytic intermediates | PPP usage is highly state- and tissue-dependent, supporting redox buffering, nucleotide synthesis, immune effector function, and cancer metabolism rather than fixed constitutive high flux in all tissues (teslaa2023thepentosephosphate pages 3-4, teslaa2023thepentosephosphate pages 6-8, teslaa2023thepentosephosphate pages 9-11) | TeSlaa et al. 2023; Qiao et al. 2025 (teslaa2023thepentosephosphate pages 3-4, teslaa2023thepentosephosphate pages 6-8, teslaa2023thepentosephosphate pages 9-11) |
| **Plants / photosynthetic eukaryotes** | OxPPP is **compartmentalized**: cytosolic oxPPP runs constitutively at low level, while plastidial/chloroplast oxPPP is strongly regulated and often suppressed in the light but can be activated by stress/H2O2 | Non-oxPPP is split between conventional reactions and the **Calvin-Benson cycle**, which functions as an anabolic PPP-like network in plastids | Multiple G6PDH isoforms exist in cytosol and plastids; chloroplast metabolism replaces the usual transaldolase solution with aldolase + **sedoheptulose-1,7-bisphosphatase (SBPase)** in the Calvin cycle; transport constraints between cytosol and plastid shape flux (sharkey2021pentosephosphatepathway pages 1-4, jiang2022glucose6phosphatedehydrogenasesthe pages 3-5, sharkey2021pentosephosphatepathway pages 7-9, sharkey2021pentosephosphatepathway pages 12-13, sharkey2021pentosephosphatepathway pages 9-12) | Sharkey 2021; Jiang et al. 2022 (sharkey2021pentosephosphatepathway pages 1-4, jiang2022glucose6phosphatedehydrogenasesthe pages 3-5, sharkey2021pentosephosphatepathway pages 7-9, sharkey2021pentosephosphatepathway pages 12-13, sharkey2021pentosephosphatepathway pages 9-12) |
| **Yeasts** | Canonical oxPPP present, but quantitative contribution to glucose catabolism varies markedly by species | Canonical non-oxPPP present; can be supplemented by sedoheptulose-1,7-bisphosphatase-dependent reactions in some yeasts | In _S. cerevisiae_, oxPPP usually carries a relatively small fraction of glucose flux (~2.5% under standard conditions), whereas in _Kluyveromyces lactis_ PPP can contribute up to ~40% of glucose degradation; in _K. lactis_, **GND1, RKI1, and TKL1** are essential under standard conditions, underscoring lineage-specific dependence (bertels2021thepentosephosphate pages 7-8, bertels2025geneticandphysiological pages 1-2, bertels2025geneticandphysiological pages 2-4) | Bertels et al. 2021; Bertels et al. 2025 (bertels2021thepentosephosphate pages 7-8, bertels2025geneticandphysiological pages 1-2, bertels2025geneticandphysiological pages 2-4) |
| **Parasitic protists (e.g. _Plasmodium_)** | OxPPP present, but enzyme architecture can differ from canonical bacterial/metazoan forms | Non-oxPPP present with conventional sugar-phosphate interconversions | _Plasmodium_ encodes a **bifunctional G6PD–6PGL fusion enzyme (GluPho)**, showing lineage-specific domain fusion within the oxidative branch rather than a separate monofunctional enzyme set (berneburg2023nadphproducingenzymesfrom pages 24-26) | Berneburg 2023; TeSlaa et al. 2023 (berneburg2023nadphproducingenzymesfrom pages 24-26, teslaa2023thepentosephosphate pages 3-4) |


*Table: This table summarizes how the pentose phosphate pathway is conserved, modified, or replaced across major lineages, separating the status of oxidative and non-oxidative branches. It is useful for clarifying what is canonical versus lineage-specific, including archaeal losses, bacterial bypasses, plant compartmentation, yeast flux differences, and parasite-specific enzyme fusions.*

Key features of lineage-specific variation include:

- **Bacterial transaldolase bypass (sedoheptulose-1,7-bisphosphate pathway, SBPP):** Many abundant human gut bacteria, including *Prevotella copri* and members of Bacteroidetes, Firmicutes, Proteobacteria, Verrucomicrobia, and Lentisphaerae, lack transaldolase genes entirely. These organisms use the SBPP, in which a pyrophosphate-dependent phosphofructokinase (PPi-PFK) phosphorylates sedoheptulose 7-phosphate to sedoheptulose 1,7-bisphosphate, which is then cleaved by aldolase into erythrose 4-phosphate and dihydroxyacetone phosphate, connecting pentose metabolism with glycolysis (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 1-2).

- **Plant compartmentalization:** In photosynthetic eukaryotes, the PPP is partitioned between cytosol and plastids. *Arabidopsis* possesses six G6PDH isoforms: three plastidial (P1-G6PDH in chloroplasts, P2-G6PDH broadly expressed in plastids, and a catalytically inactive P0-G6PDH that facilitates peroxisomal targeting) and two cytosolic isoforms (G6PD5, G6PD6) that account for 60–80% of total activity (jiang2022glucose6phosphatedehydrogenasesthe pages 3-5, jiang2022glucose6phosphatedehydrogenasesthe pages 2-3). The plastidial oxidative PPP is strongly suppressed in the light via cysteine reduction of the enzyme but can be activated by H₂O₂ under stress conditions; the cytosolic oxidative PPP operates constitutively at approximately 4–5% of the net CO₂ assimilation rate (sharkey2021pentosephosphatepathway pages 7-9, sharkey2021pentosephosphatepathway pages 13-15, sharkey2021pentosephosphatepathway pages 12-13). The Calvin-Benson cycle represents an anabolic modification of the non-oxidative PPP, replacing the transaldolase step with aldolase + sedoheptulose-1,7-bisphosphatase (SBPase), which provides thermodynamic drive toward pentose phosphate production (sharkey2021pentosephosphatepathway pages 1-4, sharkey2021pentosephosphatepathway pages 4-5).

- **Yeast species differences:** In *Saccharomyces cerevisiae*, approximately 2.5% of glucose flux passes through the oxidative PPP under standard conditions, while in the Crabtree-negative yeast *Kluyveromyces lactis*, the PPP contributes up to ~40% of glucose degradation (bertels2021thepentosephosphate pages 7-8, bertels2025geneticandphysiological pages 1-2). This difference has profound genetic consequences: in *K. lactis*, GND1, RKI1, and TKL1 are essential genes under standard growth conditions, whereas their *S. cerevisiae* orthologs are dispensable for viability (bertels2025geneticandphysiological pages 1-2, bertels2025geneticandphysiological pages 2-4). Epistasis analysis in *K. lactis* revealed that lethality of gnd1Δ is caused by toxic accumulation of 6-phosphogluconate and can be rescued by concurrent deletion of ZWF1 (bertels2025geneticandphysiological pages 1-2, bertels2025geneticandphysiological pages 4-7).

- **Phosphoketolase pathway:** Some organisms, particularly bifidobacteria, employ phosphoketolase, which cleaves fructose 6-phosphate or xylulose 5-phosphate to acetyl-phosphate and sugar phosphates (the "bifid shunt"). This represents an alternative non-oxidative glycolytic strategy that can achieve near-theoretical acetyl-CoA yields without carbon loss (hellgren2020promiscuousphosphoketolaseand pages 2-2).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Ordering and Thermodynamic Constraints

Within the oxidative branch, the three steps must occur in strict sequence: the product of G6PD (6-phosphoglucono-δ-lactone) is the substrate for 6PGL, whose product (6-phosphogluconate) is the substrate for 6PGD. The decarboxylation at the 6PGD step releases CO₂ and makes the entire oxidative branch effectively irreversible under cellular conditions (berneburg2023nadphproducingenzymesfrom pages 24-26, seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6). The non-oxidative branch, by contrast, is thermodynamically near-equilibrium and operates bidirectionally, with net direction determined by metabolite concentrations and downstream demand (teslaa2023thepentosephosphate pages 3-4, sharkey2021pentosephosphatepathway pages 4-5).

### 6.2 Tissue-Specific and Physiological Dependencies

The PPP plays distinct roles across tissues in mammals. In immune cells (granulocytes, macrophages), phagocytic stimulation rapidly increases oxidative PPP flux approximately 4-fold to fuel the NADPH oxidase (NOX)-mediated oxidative burst (hogg2023bayesian13cmetabolicflux pages 1-2, hogg2023bayesian13cmetabolicflux pages 15-17). The non-oxidative PPP direction reverses during phagocytosis, shifting from ribose 5-phosphate biosynthesis toward glycolytic intermediate production (hogg2023bayesian13cmetabolicflux pages 1-2). In the intestinal epithelium, transketolase deficiency in epithelial cells causes spontaneous colitis with hyperproliferation and apoptosis, reflecting the tissue's high nucleotide demand (teslaa2023thepentosephosphate pages 9-11). In skeletal muscle, G6PD activity increases with exercise and is important for muscle repair; age-associated loss of muscle mass is accompanied by decreased G6PD activity (garciadominguez2022glucose6pdehydrogenase—an pages 10-12). In skin, G6PD levels decrease in psoriasis and vitiligo (teslaa2023thepentosephosphate pages 9-11).

### 6.3 Disease and Failure Modes

**G6PD deficiency** (OMIM #305900) is the most common human enzymopathy, affecting approximately 1 in 20 people worldwide. The high global frequency likely reflects selective advantage against malaria, as G6PD-deficient erythrocytes are hostile to *Plasmodium* parasites (bertels2021thepentosephosphate pages 12-13). G6PD deficiency causes hemolytic anemia upon oxidative challenge and has been associated with increased susceptibility to bacterial and fungal infections (bertels2021thepentosephosphate pages 12-13, teslaa2023thepentosephosphate pages 9-11).

**Transaldolase deficiency** is a rare autosomal recessive disorder of carbohydrate metabolism causing liver cirrhosis, anemia, thrombocytopenia, cardiac defects, renal malfunction, and neonatal edema (bertels2021thepentosephosphate pages 12-13). **Transketolase deficiency** is associated with Wernicke-Korsakoff syndrome (classically attributed to decreased affinity for the ThDP cofactor, though this mechanism has been questioned) and developmental heart defects (bertels2021thepentosephosphate pages 12-13).

**Cancer metabolism.** G6PD is upregulated in many cancer types. Cancer cells depend on PPP-derived NADPH for redox balance and on ribose 5-phosphate for nucleotide biosynthesis to support proliferation (meng2022recentfindingsin pages 1-2, qiao2025thepentosephosphate pages 4-6). In lung cancer, G6PD ablation significantly suppresses KRAS/LKB1-mutant but not KRAS/p53-mutant tumors, demonstrating that oncogenic context determines PPP dependence (teslaa2023thepentosephosphate pages 6-8). TKT has been shown to promote cancer progression through both metabolic and non-metabolic functions, including promotion of epithelial-mesenchymal transition and immune evasion via upregulation of PD-L1 (qiao2025thepentosephosphate pages 4-6).

## 7. Controversies and Open Questions

Several important questions remain unresolved in PPP biology:

1. **Quantitative flux partitioning in vivo.** While isotope tracing methods using ¹³C- and ²H-labeled glucose have been developed, measuring absolute PPP flux—as opposed to relative flux ratios—remains technically challenging, particularly in intact tissues in vivo (teslaa2023thepentosephosphate pages 4-6, hogg2023bayesian13cmetabolicflux pages 2-3). The fraction of glucose entering the PPP varies widely by tissue, metabolic state, and organism, and generalizations should be made cautiously.

2. **Opposing immunological functions of oxPPP enzymes.** Recent evidence suggests that G6PD and 6PGD may have opposite immunological effects in T cells, but systematic investigation is lacking (teslaa2023thepentosephosphate pages 13-15).

3. **Orphan reactions in the non-oxidative PPP.** Newly discovered reactions, such as sedoheptulose kinase activity (e.g., SHB17/sedoheptulose-1,7-bisphosphatase in yeast), are not fully characterized in terms of their physiological roles across organisms (teslaa2023thepentosephosphate pages 13-15, bertels2021thepentosephosphate pages 7-8).

4. **Lack of specific pharmacological tools.** Many PPP enzymes lack selective, potent inhibitors, which limits the ability to dissect their individual contributions to disease and to develop targeted therapies (teslaa2023thepentosephosphate pages 13-15).

5. **Prebiotic chemistry uncertainties.** While the non-enzymatic origin of PPP-like reactions under Archean conditions is experimentally supported, the pathway by which these reactions were enzymatized and how their topology was "imprinted" on the evolving metabolic network remains speculative (piedrafita2021cysteineandiron pages 2-3, piedrafita2021cysteineandiron pages 1-2).

6. **Species-specific pathway essentiality.** The finding that GND1, RKI1, and TKL1 are essential in *K. lactis* but not in *S. cerevisiae* highlights the danger of extrapolating from a single model organism. The extent to which PPP enzyme essentiality varies across mammalian tissues and disease contexts is not fully mapped (bertels2025geneticandphysiological pages 1-2, bertels2025geneticandphysiological pages 2-4).

7. **Spatial and temporal resolution.** As emphasized by TeSlaa et al. (2023), understanding PPP function requires moving beyond generalizations about ROS and free radicals to develop time-dependent, location-dependent, and molecule-specific models of PPP roles in health and disease (teslaa2023thepentosephosphate pages 13-15).

## 8. Key References

- TeSlaa T, Ralser M, Fan J, Rabinowitz JD. The pentose phosphate pathway in health and disease. *Nature Metabolism* 5:1275–1289, 2023. DOI: 10.1038/s42255-023-00863-2 (teslaa2023thepentosephosphate pages 3-4, teslaa2023thepentosephosphate pages 6-8, teslaa2023thepentosephosphate pages 4-6, teslaa2023thepentosephosphate pages 13-15)
- Qiao J, Yu Z, Zhou H, Wang W, Wu H, Ye J. The pentose phosphate pathway: from mechanisms to implications for gastrointestinal cancers. *Int J Mol Sci* 26:610, 2025. DOI: 10.3390/ijms26020610 (qiao2025thepentosephosphate pages 1-3, qiao2025thepentosephosphate pages 4-6)
- Bertels L-K, Walter S, Heinisch JJ. Genetic and physiological characterization of the pentose phosphate pathway in the yeast *Kluyveromyces lactis*. *Int J Mol Sci* 26:938, 2025. DOI: 10.3390/ijms26030938 (bertels2025geneticandphysiological pages 1-2, bertels2025geneticandphysiological pages 4-7, bertels2025geneticandphysiological pages 2-4)
- Bertels L-K, Murillo LF, Heinisch JJ. The pentose phosphate pathway in yeasts—more than a poor cousin of glycolysis. *Biomolecules* 11:725, 2021. DOI: 10.3390/biom11050725 (bertels2021thepentosephosphate pages 1-3, bertels2021thepentosephosphate pages 3-4, bertels2021thepentosephosphate pages 12-13, bertels2021thepentosephosphate pages 7-8)
- Seregina TA, Shakulov RS, Petrushanko IY, Lobanov KV, Mironov AS. Biosynthesis of ribose-5-phosphate—metabolic regulator of *Escherichia coli* viability. *Cells* 14:1775, 2025. DOI: 10.3390/cells14221775 (seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3, seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6, seregina2025biosynthesisofribose5phosphate—metabolic pages 3-5, seregina2025biosynthesisofribose5phosphate—metabolic pages 8-9)
- Seregina T et al. Ribose-5-phosphate metabolism protects *E. coli* from antibiotic lethality. *mBio* 16, 2025. DOI: 10.1128/mbio.00654-25 (seregina2025ribose5phosphatemetabolismprotects pages 1-3)
- Piedrafita G et al. Cysteine and iron accelerate the formation of ribose-5-phosphate, providing insights into the evolutionary origins of the metabolic network structure. *PLOS Biology* 19:e3001468, 2021. DOI: 10.1371/journal.pbio.3001468 (piedrafita2021cysteineandiron pages 2-3, piedrafita2021cysteineandiron pages 1-2)
- Santana-Molina C, Williams TA, Snel B, Spang A. Chimeric origins and dynamic evolution of central carbon metabolism in eukaryotes. *Nature Ecology & Evolution* 9:613–627, 2025. DOI: 10.1038/s41559-025-02648-0 (santanamolina2025chimericoriginsand pages 4-5, santanamolina2025chimericoriginsand pages 5-6, santanamolina2025chimericoriginsand pages 3-4)
- Garschagen LS, Franke T, Deppenmeier U. An alternative pentose phosphate pathway in human gut bacteria for the degradation of C5 sugars in dietary fibers. *FEBS J* 288:1839–1858, 2021. DOI: 10.1111/febs.15511 (garschagen2021analternativepentose pages 2-3, garschagen2021analternativepentose pages 1-2)
- Sharkey TD. Pentose phosphate pathway reactions in photosynthesizing cells. *Cells* 10:1547, 2021. DOI: 10.3390/cells10061547 (sharkey2021pentosephosphatepathway pages 7-9, sharkey2021pentosephosphatepathway pages 1-4, sharkey2021pentosephosphatepathway pages 4-5, sharkey2021pentosephosphatepathway pages 13-15, sharkey2021pentosephosphatepathway pages 12-13, sharkey2021pentosephosphatepathway pages 9-12, sharkey2021pentosephosphatepathway pages 5-7)
- Meng Q et al. Recent findings in the regulation of G6PD and its role in diseases. *Front Pharmacol* 13, 2022. DOI: 10.3389/fphar.2022.932154 (meng2022recentfindingsin pages 1-2, meng2022recentfindingsin pages 5-6, meng2022recentfindingsin pages 2-5)
- Jiang Z et al. Glucose-6-phosphate dehydrogenases: the hidden players of plant physiology. *Int J Mol Sci* 23:16128, 2022. DOI: 10.3390/ijms232416128 (jiang2022glucose6phosphatedehydrogenasesthe pages 3-5, jiang2022glucose6phosphatedehydrogenasesthe pages 2-3)
- Masi A, Mach RL, Mach-Aigner AR. The pentose phosphate pathway in industrially relevant fungi: crucial insights for bioprocessing. *Appl Microbiol Biotechnol* 105:4017–4031, 2021. DOI: 10.1007/s00253-021-11314-x (masi2021thepentosephosphate pages 1-2)
- Hogg M et al. Bayesian ¹³C-metabolic flux analysis of parallel tracer experiments in granulocytes. *Metabolites* 14:24, 2023. DOI: 10.3390/metabo14010024 (hogg2023bayesian13cmetabolicflux pages 1-2, hogg2023bayesian13cmetabolicflux pages 15-17, hogg2023bayesian13cmetabolicflux pages 2-3)
- Hellgren J et al. Promiscuous phosphoketolase and metabolic rewiring enables novel non-oxidative glycolysis in yeast. *Metab Eng* 62:150–160, 2020. DOI: 10.1016/j.ymben.2020.09.003 (hellgren2020promiscuousphosphoketolaseand pages 2-2)

References

1. (teslaa2023thepentosephosphate pages 3-4): Tara TeSlaa, Markus Ralser, Jing Fan, and Joshua D. Rabinowitz. The pentose phosphate pathway in health and disease. Nature Metabolism, 5:1275-1289, Aug 2023. URL: https://doi.org/10.1038/s42255-023-00863-2, doi:10.1038/s42255-023-00863-2. This article has 619 citations and is from a domain leading peer-reviewed journal.

2. (bertels2021thepentosephosphate pages 1-3): Laura-Katharina Bertels, Lucía Fernández Murillo, and Jürgen J. Heinisch. The pentose phosphate pathway in yeasts–more than a poor cousin of glycolysis. Biomolecules, 11:725, May 2021. URL: https://doi.org/10.3390/biom11050725, doi:10.3390/biom11050725. This article has 138 citations.

3. (piedrafita2021cysteineandiron pages 2-3): Gabriel Piedrafita, Sreejith J. Varma, Cecilia Castro, Christoph B. Messner, Lukasz Szyrwiel, Julian L. Griffin, and Markus Ralser. Cysteine and iron accelerate the formation of ribose-5-phosphate, providing insights into the evolutionary origins of the metabolic network structure. PLOS Biology, 19:e3001468, Dec 2021. URL: https://doi.org/10.1371/journal.pbio.3001468, doi:10.1371/journal.pbio.3001468. This article has 29 citations and is from a highest quality peer-reviewed journal.

4. (seregina2025biosynthesisofribose5phosphate—metabolic pages 5-6): Tatyana A. Seregina, Rustem S. Shakulov, Irina Yu. Petrushanko, Konstantin V. Lobanov, and Alexander S. Mironov. Biosynthesis of ribose-5-phosphate—metabolic regulator of escherichia coli viability. Cells, 14:1775, Nov 2025. URL: https://doi.org/10.3390/cells14221775, doi:10.3390/cells14221775. This article has 6 citations.

5. (masi2021thepentosephosphate pages 1-2): Audrey Masi, Robert L. Mach, and Astrid R. Mach-Aigner. The pentose phosphate pathway in industrially relevant fungi: crucial insights for bioprocessing. Applied Microbiology and Biotechnology, 105:4017-4031, May 2021. URL: https://doi.org/10.1007/s00253-021-11314-x, doi:10.1007/s00253-021-11314-x. This article has 71 citations and is from a domain leading peer-reviewed journal.

6. (garschagen2021analternativepentose pages 2-3): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

7. (sharkey2021pentosephosphatepathway pages 1-4): Thomas D. Sharkey. Pentose phosphate pathway reactions in photosynthesizing cells. Cells, 10:1547, Jun 2021. URL: https://doi.org/10.3390/cells10061547, doi:10.3390/cells10061547. This article has 111 citations.

8. (meng2022recentfindingsin pages 1-2): Qingfei Meng, Yanghe Zhang, Shiming Hao, Huihui Sun, Bin Liu, Honglan Zhou, Yishu Wang, and Zhi-Xiang Xu. Recent findings in the regulation of g6pd and its role in diseases. Frontiers in Pharmacology, Aug 2022. URL: https://doi.org/10.3389/fphar.2022.932154, doi:10.3389/fphar.2022.932154. This article has 114 citations.

9. (bertels2021thepentosephosphate pages 12-13): Laura-Katharina Bertels, Lucía Fernández Murillo, and Jürgen J. Heinisch. The pentose phosphate pathway in yeasts–more than a poor cousin of glycolysis. Biomolecules, 11:725, May 2021. URL: https://doi.org/10.3390/biom11050725, doi:10.3390/biom11050725. This article has 138 citations.

10. (berneburg2023nadphproducingenzymesfrom pages 24-26): NADPH-producing Enzymes from the Pentose Phosphate Pathway of Plasmodium and Leishmania as Targets for New Anti-infective Agents This article has 0 citations.

11. (seregina2025biosynthesisofribose5phosphate—metabolic pages 1-3): Tatyana A. Seregina, Rustem S. Shakulov, Irina Yu. Petrushanko, Konstantin V. Lobanov, and Alexander S. Mironov. Biosynthesis of ribose-5-phosphate—metabolic regulator of escherichia coli viability. Cells, 14:1775, Nov 2025. URL: https://doi.org/10.3390/cells14221775, doi:10.3390/cells14221775. This article has 6 citations.

12. (bertels2021thepentosephosphate pages 3-4): Laura-Katharina Bertels, Lucía Fernández Murillo, and Jürgen J. Heinisch. The pentose phosphate pathway in yeasts–more than a poor cousin of glycolysis. Biomolecules, 11:725, May 2021. URL: https://doi.org/10.3390/biom11050725, doi:10.3390/biom11050725. This article has 138 citations.

13. (santanamolina2025chimericoriginsand pages 4-5): Carlos Santana-Molina, Tom A. Williams, Berend Snel, and Anja Spang. Chimeric origins and dynamic evolution of central carbon metabolism in eukaryotes. Nature Ecology &amp; Evolution, 9:613-627, Mar 2025. URL: https://doi.org/10.1038/s41559-025-02648-0, doi:10.1038/s41559-025-02648-0. This article has 18 citations and is from a highest quality peer-reviewed journal.

14. (sharkey2021pentosephosphatepathway pages 4-5): Thomas D. Sharkey. Pentose phosphate pathway reactions in photosynthesizing cells. Cells, 10:1547, Jun 2021. URL: https://doi.org/10.3390/cells10061547, doi:10.3390/cells10061547. This article has 111 citations.

15. (meng2022recentfindingsin pages 5-6): Qingfei Meng, Yanghe Zhang, Shiming Hao, Huihui Sun, Bin Liu, Honglan Zhou, Yishu Wang, and Zhi-Xiang Xu. Recent findings in the regulation of g6pd and its role in diseases. Frontiers in Pharmacology, Aug 2022. URL: https://doi.org/10.3389/fphar.2022.932154, doi:10.3389/fphar.2022.932154. This article has 114 citations.

16. (qiao2025thepentosephosphate pages 1-3): Jincheng Qiao, Zhengchen Yu, Han Zhou, Wankun Wang, Hao Wu, and Jun Ye. The pentose phosphate pathway: from mechanisms to implications for gastrointestinal cancers. International Journal of Molecular Sciences, 26:610, Jan 2025. URL: https://doi.org/10.3390/ijms26020610, doi:10.3390/ijms26020610. This article has 26 citations.

17. (sharkey2021pentosephosphatepathway pages 5-7): Thomas D. Sharkey. Pentose phosphate pathway reactions in photosynthesizing cells. Cells, 10:1547, Jun 2021. URL: https://doi.org/10.3390/cells10061547, doi:10.3390/cells10061547. This article has 111 citations.

18. (garschagen2021analternativepentose pages 1-2): Laura S. Garschagen, Thomas Franke, and Uwe Deppenmeier. An alternative pentose phosphate pathway in human gut bacteria for the degradation of c5 sugars in dietary fibers. The FEBS Journal, 288:1839-1858, Sep 2021. URL: https://doi.org/10.1111/febs.15511, doi:10.1111/febs.15511. This article has 31 citations.

19. (seregina2025ribose5phosphatemetabolismprotects pages 1-3): Tatyana Seregina, Rustem Shakulov, Giulio Quarta, Konstantin Shatalin, Svetlana Sklyarova, Irina Petrushanko, Artemy P. Fedulov, Alexander V. Ivanov, Vladimir Mitkevich, Alexander Makarov, Alexander S. Mironov, and Evgeny Nudler. Ribose-5-phosphate metabolism protects e. coli from antibiotic lethality. mBio, Jul 2025. URL: https://doi.org/10.1128/mbio.00654-25, doi:10.1128/mbio.00654-25. This article has 9 citations and is from a domain leading peer-reviewed journal.

20. (teslaa2023thepentosephosphate pages 6-8): Tara TeSlaa, Markus Ralser, Jing Fan, and Joshua D. Rabinowitz. The pentose phosphate pathway in health and disease. Nature Metabolism, 5:1275-1289, Aug 2023. URL: https://doi.org/10.1038/s42255-023-00863-2, doi:10.1038/s42255-023-00863-2. This article has 619 citations and is from a domain leading peer-reviewed journal.

21. (teslaa2023thepentosephosphate pages 4-6): Tara TeSlaa, Markus Ralser, Jing Fan, and Joshua D. Rabinowitz. The pentose phosphate pathway in health and disease. Nature Metabolism, 5:1275-1289, Aug 2023. URL: https://doi.org/10.1038/s42255-023-00863-2, doi:10.1038/s42255-023-00863-2. This article has 619 citations and is from a domain leading peer-reviewed journal.

22. (meng2022recentfindingsin pages 2-5): Qingfei Meng, Yanghe Zhang, Shiming Hao, Huihui Sun, Bin Liu, Honglan Zhou, Yishu Wang, and Zhi-Xiang Xu. Recent findings in the regulation of g6pd and its role in diseases. Frontiers in Pharmacology, Aug 2022. URL: https://doi.org/10.3389/fphar.2022.932154, doi:10.3389/fphar.2022.932154. This article has 114 citations.

23. (qiao2025thepentosephosphate pages 4-6): Jincheng Qiao, Zhengchen Yu, Han Zhou, Wankun Wang, Hao Wu, and Jun Ye. The pentose phosphate pathway: from mechanisms to implications for gastrointestinal cancers. International Journal of Molecular Sciences, 26:610, Jan 2025. URL: https://doi.org/10.3390/ijms26020610, doi:10.3390/ijms26020610. This article has 26 citations.

24. (piedrafita2021cysteineandiron pages 1-2): Gabriel Piedrafita, Sreejith J. Varma, Cecilia Castro, Christoph B. Messner, Lukasz Szyrwiel, Julian L. Griffin, and Markus Ralser. Cysteine and iron accelerate the formation of ribose-5-phosphate, providing insights into the evolutionary origins of the metabolic network structure. PLOS Biology, 19:e3001468, Dec 2021. URL: https://doi.org/10.1371/journal.pbio.3001468, doi:10.1371/journal.pbio.3001468. This article has 29 citations and is from a highest quality peer-reviewed journal.

25. (maeda2021evolutionaryhistoryof pages 5-6): Hiroshi A. Maeda and Alisdair R. Fernie. Evolutionary history of plant metabolism. Jun 2021. URL: https://doi.org/10.1146/annurev-arplant-080620-031054, doi:10.1146/annurev-arplant-080620-031054. This article has 138 citations and is from a domain leading peer-reviewed journal.

26. (seregina2025biosynthesisofribose5phosphate—metabolic pages 3-5): Tatyana A. Seregina, Rustem S. Shakulov, Irina Yu. Petrushanko, Konstantin V. Lobanov, and Alexander S. Mironov. Biosynthesis of ribose-5-phosphate—metabolic regulator of escherichia coli viability. Cells, 14:1775, Nov 2025. URL: https://doi.org/10.3390/cells14221775, doi:10.3390/cells14221775. This article has 6 citations.

27. (santanamolina2025chimericoriginsand pages 5-6): Carlos Santana-Molina, Tom A. Williams, Berend Snel, and Anja Spang. Chimeric origins and dynamic evolution of central carbon metabolism in eukaryotes. Nature Ecology &amp; Evolution, 9:613-627, Mar 2025. URL: https://doi.org/10.1038/s41559-025-02648-0, doi:10.1038/s41559-025-02648-0. This article has 18 citations and is from a highest quality peer-reviewed journal.

28. (santanamolina2025chimericoriginsand pages 3-4): Carlos Santana-Molina, Tom A. Williams, Berend Snel, and Anja Spang. Chimeric origins and dynamic evolution of central carbon metabolism in eukaryotes. Nature Ecology &amp; Evolution, 9:613-627, Mar 2025. URL: https://doi.org/10.1038/s41559-025-02648-0, doi:10.1038/s41559-025-02648-0. This article has 18 citations and is from a highest quality peer-reviewed journal.

29. (teslaa2023thepentosephosphate pages 9-11): Tara TeSlaa, Markus Ralser, Jing Fan, and Joshua D. Rabinowitz. The pentose phosphate pathway in health and disease. Nature Metabolism, 5:1275-1289, Aug 2023. URL: https://doi.org/10.1038/s42255-023-00863-2, doi:10.1038/s42255-023-00863-2. This article has 619 citations and is from a domain leading peer-reviewed journal.

30. (jiang2022glucose6phosphatedehydrogenasesthe pages 3-5): Zhengrong Jiang, Ming Wang, Michael Nicolas, Laurent Ogé, Maria-Dolores Pérez-Garcia, Laurent Crespel, Ganghua Li, Yanfeng Ding, José Le Gourrierec, Philippe Grappin, and Soulaiman Sakr. Glucose-6-phosphate dehydrogenases: the hidden players of plant physiology. International Journal of Molecular Sciences, 23:16128, Dec 2022. URL: https://doi.org/10.3390/ijms232416128, doi:10.3390/ijms232416128. This article has 82 citations.

31. (sharkey2021pentosephosphatepathway pages 7-9): Thomas D. Sharkey. Pentose phosphate pathway reactions in photosynthesizing cells. Cells, 10:1547, Jun 2021. URL: https://doi.org/10.3390/cells10061547, doi:10.3390/cells10061547. This article has 111 citations.

32. (sharkey2021pentosephosphatepathway pages 12-13): Thomas D. Sharkey. Pentose phosphate pathway reactions in photosynthesizing cells. Cells, 10:1547, Jun 2021. URL: https://doi.org/10.3390/cells10061547, doi:10.3390/cells10061547. This article has 111 citations.

33. (sharkey2021pentosephosphatepathway pages 9-12): Thomas D. Sharkey. Pentose phosphate pathway reactions in photosynthesizing cells. Cells, 10:1547, Jun 2021. URL: https://doi.org/10.3390/cells10061547, doi:10.3390/cells10061547. This article has 111 citations.

34. (bertels2021thepentosephosphate pages 7-8): Laura-Katharina Bertels, Lucía Fernández Murillo, and Jürgen J. Heinisch. The pentose phosphate pathway in yeasts–more than a poor cousin of glycolysis. Biomolecules, 11:725, May 2021. URL: https://doi.org/10.3390/biom11050725, doi:10.3390/biom11050725. This article has 138 citations.

35. (bertels2025geneticandphysiological pages 1-2): Laura-Katharina Bertels, Stefan Walter, and Jürgen J. Heinisch. Genetic and physiological characterization of the pentose phosphate pathway in the yeast kluyveromyces lactis. International Journal of Molecular Sciences, 26:938, Jan 2025. URL: https://doi.org/10.3390/ijms26030938, doi:10.3390/ijms26030938. This article has 5 citations.

36. (bertels2025geneticandphysiological pages 2-4): Laura-Katharina Bertels, Stefan Walter, and Jürgen J. Heinisch. Genetic and physiological characterization of the pentose phosphate pathway in the yeast kluyveromyces lactis. International Journal of Molecular Sciences, 26:938, Jan 2025. URL: https://doi.org/10.3390/ijms26030938, doi:10.3390/ijms26030938. This article has 5 citations.

37. (jiang2022glucose6phosphatedehydrogenasesthe pages 2-3): Zhengrong Jiang, Ming Wang, Michael Nicolas, Laurent Ogé, Maria-Dolores Pérez-Garcia, Laurent Crespel, Ganghua Li, Yanfeng Ding, José Le Gourrierec, Philippe Grappin, and Soulaiman Sakr. Glucose-6-phosphate dehydrogenases: the hidden players of plant physiology. International Journal of Molecular Sciences, 23:16128, Dec 2022. URL: https://doi.org/10.3390/ijms232416128, doi:10.3390/ijms232416128. This article has 82 citations.

38. (sharkey2021pentosephosphatepathway pages 13-15): Thomas D. Sharkey. Pentose phosphate pathway reactions in photosynthesizing cells. Cells, 10:1547, Jun 2021. URL: https://doi.org/10.3390/cells10061547, doi:10.3390/cells10061547. This article has 111 citations.

39. (bertels2025geneticandphysiological pages 4-7): Laura-Katharina Bertels, Stefan Walter, and Jürgen J. Heinisch. Genetic and physiological characterization of the pentose phosphate pathway in the yeast kluyveromyces lactis. International Journal of Molecular Sciences, 26:938, Jan 2025. URL: https://doi.org/10.3390/ijms26030938, doi:10.3390/ijms26030938. This article has 5 citations.

40. (hellgren2020promiscuousphosphoketolaseand pages 2-2): John Hellgren, Alexei Godina, Jens Nielsen, and Verena Siewers. Promiscuous phosphoketolase and metabolic rewiring enables novel non-oxidative glycolysis in yeast for high-yield production of acetyl-coa derived products. Metabolic Engineering, 62:150-160, Nov 2020. URL: https://doi.org/10.1016/j.ymben.2020.09.003, doi:10.1016/j.ymben.2020.09.003. This article has 60 citations and is from a domain leading peer-reviewed journal.

41. (hogg2023bayesian13cmetabolicflux pages 1-2): Melanie Hogg, Eva-Maria Wolfschmitt, Ulrich Wachter, Fabian Zink, Peter Radermacher, and Josef Albert Vogt. Bayesian 13c-metabolic flux analysis of parallel tracer experiments in granulocytes: a directional shift within the non-oxidative pentose phosphate pathway supports phagocytosis. Metabolites, 14:24, Dec 2023. URL: https://doi.org/10.3390/metabo14010024, doi:10.3390/metabo14010024. This article has 6 citations.

42. (hogg2023bayesian13cmetabolicflux pages 15-17): Melanie Hogg, Eva-Maria Wolfschmitt, Ulrich Wachter, Fabian Zink, Peter Radermacher, and Josef Albert Vogt. Bayesian 13c-metabolic flux analysis of parallel tracer experiments in granulocytes: a directional shift within the non-oxidative pentose phosphate pathway supports phagocytosis. Metabolites, 14:24, Dec 2023. URL: https://doi.org/10.3390/metabo14010024, doi:10.3390/metabo14010024. This article has 6 citations.

43. (garciadominguez2022glucose6pdehydrogenase—an pages 10-12): Esther García-Domínguez, Aitor Carretero, Aurora Viña-Almunia, Julio Domenech-Fernandez, Gloria Olaso-Gonzalez, Jose Viña, and Mari Carmen Gomez-Cabrera. Glucose 6-p dehydrogenase—an antioxidant enzyme with regulatory functions in skeletal muscle during exercise. Cells, 11:3041, Sep 2022. URL: https://doi.org/10.3390/cells11193041, doi:10.3390/cells11193041. This article has 41 citations.

44. (hogg2023bayesian13cmetabolicflux pages 2-3): Melanie Hogg, Eva-Maria Wolfschmitt, Ulrich Wachter, Fabian Zink, Peter Radermacher, and Josef Albert Vogt. Bayesian 13c-metabolic flux analysis of parallel tracer experiments in granulocytes: a directional shift within the non-oxidative pentose phosphate pathway supports phagocytosis. Metabolites, 14:24, Dec 2023. URL: https://doi.org/10.3390/metabo14010024, doi:10.3390/metabo14010024. This article has 6 citations.

45. (teslaa2023thepentosephosphate pages 13-15): Tara TeSlaa, Markus Ralser, Jing Fan, and Joshua D. Rabinowitz. The pentose phosphate pathway in health and disease. Nature Metabolism, 5:1275-1289, Aug 2023. URL: https://doi.org/10.1038/s42255-023-00863-2, doi:10.1038/s42255-023-00863-2. This article has 619 citations and is from a domain leading peer-reviewed journal.

46. (seregina2025biosynthesisofribose5phosphate—metabolic pages 8-9): Tatyana A. Seregina, Rustem S. Shakulov, Irina Yu. Petrushanko, Konstantin V. Lobanov, and Alexander S. Mironov. Biosynthesis of ribose-5-phosphate—metabolic regulator of escherichia coli viability. Cells, 14:1775, Nov 2025. URL: https://doi.org/10.3390/cells14221775, doi:10.3390/cells14221775. This article has 6 citations.

## Artifacts

- [Edison artifact artifact-00](pentose_phosphate_pathway-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](pentose_phosphate_pathway-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](pentose_phosphate_pathway-deep-research-falcon_artifacts/artifact-02.md)
![Image artifact created (ID artifact-02): 'Pentose Phosphate Pathway Schematic' ![Pentose Phosphate Pathway Schematic](artifact:artifact-02) Artifact IDs that ma](pentose_phosphate_pathway-deep-research-falcon_artifacts/image-1.png)

## Citations

1. teslaa2023thepentosephosphate pages 3-4
2. santanamolina2025chimericoriginsand pages 4-5
3. teslaa2023thepentosephosphate pages 6-8
4. berneburg2023nadphproducingenzymesfrom pages 24-26
5. sharkey2021pentosephosphatepathway pages 5-7
6. bertels2021thepentosephosphate pages 1-3
7. meng2022recentfindingsin pages 5-6
8. teslaa2023thepentosephosphate pages 4-6
9. bertels2021thepentosephosphate pages 3-4
10. hellgren2020promiscuousphosphoketolaseand pages 2-2
11. teslaa2023thepentosephosphate pages 9-11
12. bertels2021thepentosephosphate pages 12-13
13. qiao2025thepentosephosphate pages 4-6
14. teslaa2023thepentosephosphate pages 13-15
15. masi2021thepentosephosphate pages 1-2
16. piedrafita2021cysteineandiron pages 2-3
17. garschagen2021analternativepentose pages 2-3
18. sharkey2021pentosephosphatepathway pages 1-4
19. meng2022recentfindingsin pages 1-2
20. sharkey2021pentosephosphatepathway pages 4-5
21. qiao2025thepentosephosphate pages 1-3
22. garschagen2021analternativepentose pages 1-2
23. meng2022recentfindingsin pages 2-5
24. piedrafita2021cysteineandiron pages 1-2
25. maeda2021evolutionaryhistoryof pages 5-6
26. santanamolina2025chimericoriginsand pages 5-6
27. santanamolina2025chimericoriginsand pages 3-4
28. sharkey2021pentosephosphatepathway pages 7-9
29. sharkey2021pentosephosphatepathway pages 12-13
30. sharkey2021pentosephosphatepathway pages 9-12
31. bertels2021thepentosephosphate pages 7-8
32. bertels2025geneticandphysiological pages 1-2
33. bertels2025geneticandphysiological pages 2-4
34. sharkey2021pentosephosphatepathway pages 13-15
35. bertels2025geneticandphysiological pages 4-7
36. Pentose Phosphate Pathway Schematic
37. https://doi.org/10.1038/s42255-023-00863-2,
38. https://doi.org/10.3390/biom11050725,
39. https://doi.org/10.1371/journal.pbio.3001468,
40. https://doi.org/10.3390/cells14221775,
41. https://doi.org/10.1007/s00253-021-11314-x,
42. https://doi.org/10.1111/febs.15511,
43. https://doi.org/10.3390/cells10061547,
44. https://doi.org/10.3389/fphar.2022.932154,
45. https://doi.org/10.1038/s41559-025-02648-0,
46. https://doi.org/10.3390/ijms26020610,
47. https://doi.org/10.1128/mbio.00654-25,
48. https://doi.org/10.1146/annurev-arplant-080620-031054,
49. https://doi.org/10.3390/ijms232416128,
50. https://doi.org/10.3390/ijms26030938,
51. https://doi.org/10.1016/j.ymben.2020.09.003,
52. https://doi.org/10.3390/metabo14010024,
53. https://doi.org/10.3390/cells11193041,