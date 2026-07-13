---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T04:05:10.698846'
end_time: '2026-07-07T04:36:00.151352'
duration_seconds: 1849.45
template_file: templates/module_research.md.j2
template_variables:
  module_title: NAD biosynthesis and nicotinate metabolism
  module_summary: A bacterial NAD metabolism module covering de novo NAD+ biosynthesis
    from L-aspartate through quinolinate, nicotinate salvage to NAD+, NADP+ formation,
    NAD(H)/NADP(H) redox interconversion, and aerobic nicotinate catabolism. In Pseudomonas
    putida KT2440, KEGG ppu00760 also includes nucleotide hydrolases, NAD-consuming
    enzymes, and central-metabolism spillover nodes; those are tracked as boundary
    context unless they directly form, interconvert, salvage, or catabolize pyridine
    nucleotides/nicotinate.
  module_outline: "- NAD biosynthesis and nicotinate metabolism\n  - 1. de novo NAD+\
    \ biosynthesis from L-aspartate\n  - De novo NAD+ biosynthesis\n    - NadB L-aspartate\
    \ oxidase (molecular player: PSEPK nadB; activity or role: L-aspartate oxidase\
    \ activity)\n    - NadA quinolinate synthase (molecular player: PSEPK nadA; activity\
    \ or role: quinolinate synthetase A activity)\n    - NadC nicotinate-nucleotide\
    \ diphosphorylase (molecular player: PSEPK nadC; activity or role: nicotinate-nucleotide\
    \ diphosphorylase (carboxylating) activity)\n    - NadD nicotinate-nucleotide\
    \ adenylyltransferase (molecular player: PSEPK nadD; activity or role: nicotinate-nucleotide\
    \ adenylyltransferase activity)\n    - NadE NAD+ synthetase (molecular player:\
    \ PSEPK nadE; activity or role: NAD+ synthase (glutamine-hydrolyzing) activity)\n\
    \  - 2. nicotinate salvage to NAD+\n  - Nicotinate salvage to NAD+\n    - PncB\
    \ nicotinate phosphoribosyltransferase (molecular player: PSEPK pncB; activity\
    \ or role: nicotinate phosphoribosyltransferase activity)\n    - PncC nicotinamide-nucleotide\
    \ amidase (molecular player: PSEPK pncC; activity or role: nicotinamide-nucleotide\
    \ amidase activity)\n  - 3. NADP+ formation and NAD(H)/NADP(H) interconversion\n\
    \  - NADP+ formation and transhydrogenase context\n    - NadK NAD+ kinase (molecular\
    \ player: PSEPK nadK; activity or role: NAD+ kinase activity)\n    - SthA soluble\
    \ pyridine nucleotide transhydrogenase (molecular player: PSEPK sthA; activity\
    \ or role: NAD(P)+ transhydrogenase (Si-specific) activity)\n    - PntAA proton-translocating\
    \ NAD(P)+ transhydrogenase subunit alpha (molecular player: PSEPK pntAA; activity\
    \ or role: proton-translocating NAD(P)+ transhydrogenase activity)\n    - PntB\
    \ proton-translocating NAD(P)+ transhydrogenase subunit beta (molecular player:\
    \ PSEPK pntB; activity or role: proton-translocating NAD(P)+ transhydrogenase\
    \ activity)\n    - PntAB proton-translocating NAD(P)+ transhydrogenase alpha part\
    \ 2 (molecular player: PSEPK pntAB; activity or role: proton-translocating NAD(P)+\
    \ transhydrogenase activity)\n  - 4. aerobic nicotinate catabolism\n  - Aerobic\
    \ nicotinate catabolism\n    - NicA nicotinate dehydrogenase small subunit (molecular\
    \ player: PSEPK nicA; activity or role: oxidoreductase activity, acting on CH\
    \ or CH2 groups)\n    - NicB nicotinate dehydrogenase large subunit (molecular\
    \ player: PSEPK nicB; activity or role: oxidoreductase activity, acting on CH\
    \ or CH2 groups)\n    - NicC 6-hydroxynicotinate 3-monooxygenase (molecular player:\
    \ PSEPK nicC; activity or role: 6-hydroxynicotinate 3-monooxygenase activity)\n\
    \    - NicX 2,5-dihydroxypyridine 5,6-dioxygenase (molecular player: PSEPK nicX;\
    \ activity or role: 2,5-dihydroxypyridine 5,6-dioxygenase activity)\n    - NicD\
    \ N-formylmaleamate deformylase (molecular player: PSEPK nicD; activity or role:\
    \ hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)\n   \
    \ - NicF maleamate amidohydrolase (molecular player: PSEPK nicF; activity or role:\
    \ hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)\n   \
    \ - MaiA/NicE maleate isomerase (molecular player: PSEPK maiA; activity or role:\
    \ maleate isomerase activity)\n  - 5. nucleotide and central-metabolism boundary\
    \ context\n  - KEGG side-node context\n    - UshA 5'-nucleotidase/cyclic phosphodiesterase\
    \ (molecular player: PSEPK ushA; activity or role: 5'-nucleotidase activity)\n\
    \    - SurE 5'-nucleotidase (molecular player: PSEPK surE; activity or role: 5'-nucleotidase\
    \ activity)\n    - NudC NAD-capped RNA hydrolase (molecular player: PSEPK nudC;\
    \ activity or role: NADH pyrophosphatase activity)\n    - CobB NAD-dependent protein\
    \ deacylase (molecular player: PSEPK cobB__Q88BY5; activity or role: protein-malonyllysine\
    \ demalonylase activity)"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 59
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 2
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: image-1.png
  path: nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: 'Image artifact created (ID artifact-01): ''Pseudomonas NAD Pathway
    Map'' ![Pseudomonas NAD Pathway Map](artifact:artifact-01) Artifact IDs that may
    be injected in'
---

## Question

# Commissioned Review Brief

## Review Topic

NAD biosynthesis and nicotinate metabolism

## Working Scope

A bacterial NAD metabolism module covering de novo NAD+ biosynthesis from L-aspartate through quinolinate, nicotinate salvage to NAD+, NADP+ formation, NAD(H)/NADP(H) redox interconversion, and aerobic nicotinate catabolism. In Pseudomonas putida KT2440, KEGG ppu00760 also includes nucleotide hydrolases, NAD-consuming enzymes, and central-metabolism spillover nodes; those are tracked as boundary context unless they directly form, interconvert, salvage, or catabolize pyridine nucleotides/nicotinate.

## Provisional Biological Outline

- NAD biosynthesis and nicotinate metabolism
  - 1. de novo NAD+ biosynthesis from L-aspartate
  - De novo NAD+ biosynthesis
    - NadB L-aspartate oxidase (molecular player: PSEPK nadB; activity or role: L-aspartate oxidase activity)
    - NadA quinolinate synthase (molecular player: PSEPK nadA; activity or role: quinolinate synthetase A activity)
    - NadC nicotinate-nucleotide diphosphorylase (molecular player: PSEPK nadC; activity or role: nicotinate-nucleotide diphosphorylase (carboxylating) activity)
    - NadD nicotinate-nucleotide adenylyltransferase (molecular player: PSEPK nadD; activity or role: nicotinate-nucleotide adenylyltransferase activity)
    - NadE NAD+ synthetase (molecular player: PSEPK nadE; activity or role: NAD+ synthase (glutamine-hydrolyzing) activity)
  - 2. nicotinate salvage to NAD+
  - Nicotinate salvage to NAD+
    - PncB nicotinate phosphoribosyltransferase (molecular player: PSEPK pncB; activity or role: nicotinate phosphoribosyltransferase activity)
    - PncC nicotinamide-nucleotide amidase (molecular player: PSEPK pncC; activity or role: nicotinamide-nucleotide amidase activity)
  - 3. NADP+ formation and NAD(H)/NADP(H) interconversion
  - NADP+ formation and transhydrogenase context
    - NadK NAD+ kinase (molecular player: PSEPK nadK; activity or role: NAD+ kinase activity)
    - SthA soluble pyridine nucleotide transhydrogenase (molecular player: PSEPK sthA; activity or role: NAD(P)+ transhydrogenase (Si-specific) activity)
    - PntAA proton-translocating NAD(P)+ transhydrogenase subunit alpha (molecular player: PSEPK pntAA; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntB proton-translocating NAD(P)+ transhydrogenase subunit beta (molecular player: PSEPK pntB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntAB proton-translocating NAD(P)+ transhydrogenase alpha part 2 (molecular player: PSEPK pntAB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
  - 4. aerobic nicotinate catabolism
  - Aerobic nicotinate catabolism
    - NicA nicotinate dehydrogenase small subunit (molecular player: PSEPK nicA; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicB nicotinate dehydrogenase large subunit (molecular player: PSEPK nicB; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicC 6-hydroxynicotinate 3-monooxygenase (molecular player: PSEPK nicC; activity or role: 6-hydroxynicotinate 3-monooxygenase activity)
    - NicX 2,5-dihydroxypyridine 5,6-dioxygenase (molecular player: PSEPK nicX; activity or role: 2,5-dihydroxypyridine 5,6-dioxygenase activity)
    - NicD N-formylmaleamate deformylase (molecular player: PSEPK nicD; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - NicF maleamate amidohydrolase (molecular player: PSEPK nicF; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - MaiA/NicE maleate isomerase (molecular player: PSEPK maiA; activity or role: maleate isomerase activity)
  - 5. nucleotide and central-metabolism boundary context
  - KEGG side-node context
    - UshA 5'-nucleotidase/cyclic phosphodiesterase (molecular player: PSEPK ushA; activity or role: 5'-nucleotidase activity)
    - SurE 5'-nucleotidase (molecular player: PSEPK surE; activity or role: 5'-nucleotidase activity)
    - NudC NAD-capped RNA hydrolase (molecular player: PSEPK nudC; activity or role: NADH pyrophosphatase activity)
    - CobB NAD-dependent protein deacylase (molecular player: PSEPK cobB__Q88BY5; activity or role: protein-malonyllysine demalonylase activity)

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

NAD biosynthesis and nicotinate metabolism

## Working Scope

A bacterial NAD metabolism module covering de novo NAD+ biosynthesis from L-aspartate through quinolinate, nicotinate salvage to NAD+, NADP+ formation, NAD(H)/NADP(H) redox interconversion, and aerobic nicotinate catabolism. In Pseudomonas putida KT2440, KEGG ppu00760 also includes nucleotide hydrolases, NAD-consuming enzymes, and central-metabolism spillover nodes; those are tracked as boundary context unless they directly form, interconvert, salvage, or catabolize pyridine nucleotides/nicotinate.

## Provisional Biological Outline

- NAD biosynthesis and nicotinate metabolism
  - 1. de novo NAD+ biosynthesis from L-aspartate
  - De novo NAD+ biosynthesis
    - NadB L-aspartate oxidase (molecular player: PSEPK nadB; activity or role: L-aspartate oxidase activity)
    - NadA quinolinate synthase (molecular player: PSEPK nadA; activity or role: quinolinate synthetase A activity)
    - NadC nicotinate-nucleotide diphosphorylase (molecular player: PSEPK nadC; activity or role: nicotinate-nucleotide diphosphorylase (carboxylating) activity)
    - NadD nicotinate-nucleotide adenylyltransferase (molecular player: PSEPK nadD; activity or role: nicotinate-nucleotide adenylyltransferase activity)
    - NadE NAD+ synthetase (molecular player: PSEPK nadE; activity or role: NAD+ synthase (glutamine-hydrolyzing) activity)
  - 2. nicotinate salvage to NAD+
  - Nicotinate salvage to NAD+
    - PncB nicotinate phosphoribosyltransferase (molecular player: PSEPK pncB; activity or role: nicotinate phosphoribosyltransferase activity)
    - PncC nicotinamide-nucleotide amidase (molecular player: PSEPK pncC; activity or role: nicotinamide-nucleotide amidase activity)
  - 3. NADP+ formation and NAD(H)/NADP(H) interconversion
  - NADP+ formation and transhydrogenase context
    - NadK NAD+ kinase (molecular player: PSEPK nadK; activity or role: NAD+ kinase activity)
    - SthA soluble pyridine nucleotide transhydrogenase (molecular player: PSEPK sthA; activity or role: NAD(P)+ transhydrogenase (Si-specific) activity)
    - PntAA proton-translocating NAD(P)+ transhydrogenase subunit alpha (molecular player: PSEPK pntAA; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntB proton-translocating NAD(P)+ transhydrogenase subunit beta (molecular player: PSEPK pntB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntAB proton-translocating NAD(P)+ transhydrogenase alpha part 2 (molecular player: PSEPK pntAB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
  - 4. aerobic nicotinate catabolism
  - Aerobic nicotinate catabolism
    - NicA nicotinate dehydrogenase small subunit (molecular player: PSEPK nicA; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicB nicotinate dehydrogenase large subunit (molecular player: PSEPK nicB; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicC 6-hydroxynicotinate 3-monooxygenase (molecular player: PSEPK nicC; activity or role: 6-hydroxynicotinate 3-monooxygenase activity)
    - NicX 2,5-dihydroxypyridine 5,6-dioxygenase (molecular player: PSEPK nicX; activity or role: 2,5-dihydroxypyridine 5,6-dioxygenase activity)
    - NicD N-formylmaleamate deformylase (molecular player: PSEPK nicD; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - NicF maleamate amidohydrolase (molecular player: PSEPK nicF; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - MaiA/NicE maleate isomerase (molecular player: PSEPK maiA; activity or role: maleate isomerase activity)
  - 5. nucleotide and central-metabolism boundary context
  - KEGG side-node context
    - UshA 5'-nucleotidase/cyclic phosphodiesterase (molecular player: PSEPK ushA; activity or role: 5'-nucleotidase activity)
    - SurE 5'-nucleotidase (molecular player: PSEPK surE; activity or role: 5'-nucleotidase activity)
    - NudC NAD-capped RNA hydrolase (molecular player: PSEPK nudC; activity or role: NADH pyrophosphatase activity)
    - CobB NAD-dependent protein deacylase (molecular player: PSEPK cobB__Q88BY5; activity or role: protein-malonyllysine demalonylase activity)

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

# NAD Biosynthesis and Nicotinate Metabolism in *Pseudomonas putida* KT2440: A Systems-Level Review

## 1. Executive Summary

Nicotinamide adenine dinucleotide (NAD+) is a universal redox cofactor and signaling molecule whose intracellular homeostasis is maintained by the interplay of biosynthetic, salvage, interconversion, catabolic, and consuming pathways. In the soil bacterium and metabolic engineering chassis *Pseudomonas putida* KT2440, the NAD metabolism module encompasses: (i) de novo NAD+ biosynthesis from L-aspartate through quinolinate via NadB, NadA, NadC, NadD, and NadE; (ii) nicotinate salvage to NAD+ via PncB, PncC, and shared late-pathway enzymes; (iii) NADP+ formation by NadK and reversible NAD(H)/NADP(H) interconversion by the membrane-bound transhydrogenase PntAB and the soluble transhydrogenase SthA; (iv) aerobic nicotinate catabolism through the *nic* gene cluster (NicA/B → NicC → NicX → NicD → NicF → MaiA), yielding fumarate for entry into the TCA cycle; and (v) a set of boundary enzymes—UshA, SurE, NudC, and CobB—that consume, hydrolyze, or modify pyridine nucleotides but do not directly form, interconvert, or salvage them. This review synthesizes current mechanistic understanding, evolutionary context, regulatory logic, and outstanding questions for each module.

The following pathway diagram provides an overview of the system architecture:

![Pseudomonas NAD Pathway Map](artifact:artifact-01)

*Image: Schematic overview of the NAD biosynthesis and nicotinate metabolism system in Pseudomonas putida KT2440, organized into de novo biosynthesis, salvage, NADP/redox interconversion, and aerobic nicotinate catabolism. Boundary NAD-related enzymes are shown at the periphery to indicate contextual links without implying core pathway membership.*

## 2. Definition and Biological Boundaries

The system reviewed here corresponds to KEGG pathway ppu00760 (nicotinate and nicotinamide metabolism) in *P. putida* KT2440, but is functionally delimited to enzymes that directly form, interconvert, salvage, or catabolize pyridine nucleotides and nicotinate. This scope includes the five de novo biosynthetic enzymes, salvage enzymes, the NAD kinase, transhydrogenases, and the complete aerobic nicotinate degradation pathway (luo2023biosynthesisofnicotinamide pages 2-4, ding2021constructionofan pages 1-2, brickman2018thebordetellabronchiseptica pages 3-3).

**What is excluded or treated as boundary context:** The KEGG map also includes nucleotide hydrolases (UshA, SurE), NAD-capped RNA hydrolases (NudC), NAD-dependent protein deacylases (CobB), and central-metabolism spillover nodes. These enzymes intersect NAD metabolism—they consume NAD+ or process pyridine-containing metabolites—but do not constitute the biosynthetic, salvage, or catabolic core. They are tracked here as boundary context because their primary biological roles lie in nucleotide recycling, epitranscriptomic regulation, and post-translational modification rather than in pyridine nucleotide biosynthesis per se (mickute2023interplaybetweenbacterial pages 1-2, lammers2021posttranslationallysineac(et)ylation pages 11-12, zakataeva2021microbial5′nucleotidasestheir pages 12-14).

**Competing definitions:** Some treatments of "NAD metabolism" encompass all NAD-consuming reactions (e.g., ADP-ribosylation, sirtuin-mediated deacylation, DNA ligase activity), while others restrict the term to biosynthesis and salvage. The present review adopts an intermediate scope anchored on pyridine ring formation, interconversion, and degradation, with NAD-consuming enzymes treated at the boundary.

## 3. Mechanistic Overview

### 3.1 De Novo NAD+ Biosynthesis from L-Aspartate

The bacterial aspartate pathway to NAD+ proceeds through five obligatory enzymatic steps converging at NAD+ (luo2023biosynthesisofnicotinamide pages 2-4, zhu2021metabolicengineeringof pages 1-2, ding2021constructionofan pages 1-2):

**Step 1: NadB (L-aspartate oxidase, EC 1.4.3.16).** NadB is a FAD-bound monomeric enzyme that oxidizes L-aspartate to 2-iminosuccinate (iminoaspartate). It can use molecular oxygen or fumarate as the terminal electron acceptor depending on conditions (zhu2021metabolicengineeringof pages 1-2). The product iminosuccinate is chemically labile and is functionally coupled to the next enzyme.

**Step 2: NadA (quinolinate synthase, EC 2.5.1.72).** NadA is a dimeric protein containing an oxygen-sensitive [4Fe-4S] cluster that catalyzes condensation of iminosuccinate with dihydroxyacetone phosphate (DHAP) to form quinolinate (QA) (zhu2021metabolicengineeringof pages 1-2, zhu2021metabolicengineeringof pages 8-9). The oxygen sensitivity of the iron-sulfur cluster is a notable constraint: under aerobic conditions, NadA activity requires iron-sulfur cluster biogenesis and repair systems. The NadB-NadA pair is sometimes described as a functional complex, and synthetic biology approaches have assembled them into enzyme complexes to improve quinolinate titers (zhu2021metabolicengineeringof pages 8-9).

**Step 3: NadC (quinolinate phosphoribosyltransferase, EC 2.4.2.19).** NadC transfers a phosphoribosyl moiety from PRPP to quinolinate, producing nicotinate mononucleotide (NaMN) with concomitant release of CO₂ and pyrophosphate. This is the convergence point where de novo and salvage routes merge (luo2023biosynthesisofnicotinamide pages 2-4, ding2021constructionofan pages 1-2).

**Step 4: NadD (NaMN adenylyltransferase, EC 2.7.7.18).** NadD adenylylates NaMN using ATP to generate nicotinic acid adenine dinucleotide (NaAD). This is a shared late-pathway step used by both de novo and salvage routes (luo2023biosynthesisofnicotinamide pages 2-4, ding2021constructionofan pages 1-2).

**Step 5: NadE (NAD+ synthetase, EC 6.3.1.5).** NadE catalyzes the final amidation of NaAD to NAD+, using ammonia (often derived from glutamine hydrolysis in glutamine-dependent NadE variants, NadE^Gln). This is the terminal obligatory step in all known bacterial NAD biosynthesis routes (luo2023biosynthesisofnicotinamide pages 2-4, santos2020nad+biosynthesisin pages 6-8, santos2020nad+biosynthesisin pages 1-2).

### 3.2 Nicotinate Salvage to NAD+

Bacteria recycle nicotinate (and nicotinamide) to regenerate NAD+ through the Preiss-Handler salvage pathway (brickman2018thebordetellabronchiseptica pages 2-3, guragain2018thetranscriptionalregulator pages 3-5):

**PncB (nicotinate phosphoribosyltransferase, EC 2.4.2.11)** converts nicotinate to NaMN using PRPP, directly feeding into the shared NadD → NadE late steps (brickman2018thebordetellabronchiseptica pages 2-3, guragain2018thetranscriptionalregulator pages 3-5). In organisms possessing PncA (nicotinamidase), nicotinamide is first deamidated to nicotinate before entering the PncB-catalyzed step (guragain2018thetranscriptionalregulator pages 3-5).

**PncC (nicotinamide-nucleotide amidase, EC 3.5.1.42)** hydrolyzes nicotinamide mononucleotide (NMN) to NaMN and ammonia, providing an alternative entry point that bypasses the nicotinamidase step when NMN is available directly. The salvage pathway shares the NadD and NadE steps with de novo biosynthesis, meaning that these two late enzymes are obligatory regardless of whether the pyridine ring is synthesized de novo or recycled (brickman2018thebordetellabronchiseptica pages 2-3).

### 3.3 NADP+ Formation and Transhydrogenase-Mediated Redox Interconversion

**NadK (NAD+ kinase, EC 2.7.1.23)** phosphorylates NAD+ to NADP+, generating the cellular pool of the anabolic redox cofactor. NadK is essential in all organisms that require NADP(H), as it is the sole known source of the 2'-phosphate group distinguishing NADP from NAD (partipilo2025integratedcontrolof pages 1-6).

The interconversion between NAD(H) and NADP(H) pools in *P. putida* is mediated by two transhydrogenases with distinct biophysical properties and partially overlapping physiological roles (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 15-18):

**PntAB (membrane-bound, proton-translocating transhydrogenase, EC 1.6.1.2)** is a multi-subunit complex (PntAA, PntAB, PntB in KT2440) that couples hydride transfer between NAD(H) and NADP(H) to the proton motive force. PntAB generally favors NADPH generation but operates reversibly in vivo, with directionality shaped by metabolic demands rather than fixed enzyme specificity (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 18-21).

**SthA (soluble pyridine nucleotide transhydrogenase, EC 1.6.1.1)** is a soluble, FAD-containing enzyme that catalyzes reversible hydride transfer between NAD(H) and NADP(H) without coupling to the proton gradient. In *P. putida*, SthA functions as the main sink for excess NADH and is strictly required for growth on acetate as sole carbon source (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 12-15). In wild-type cells, transhydrogenation favors NADH formation over NADPH at a 3.5-fold faster rate (partipilo2025integratedcontrolof pages 6-9).

A critical finding from recent work by Partipilo et al. (2025) is that single deletions of either PntAB or SthA have minimal impact on growth or fitness across diverse metabolic regimes, but the double mutant (ΔpntAB ΔsthA) exhibits 32% lower NAD+ and ATP levels, severe glutathione depletion, and growth defects, demonstrating that the two systems are functionally redundant under many conditions but collectively essential for redox homeostasis (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 15-18, partipilo2025integratedcontrolof pages 9-12). This positions transhydrogenases as dynamic regulators of redox metabolism rather than passive cofactor shuttles.

### 3.4 Aerobic Nicotinate Catabolism

*P. putida* KT2440 can utilize nicotinate as a sole carbon and energy source through the aerobic maleamate pathway encoded by the *nic* gene cluster (brickman2018thebordetellabronchiseptica pages 3-3, xiao2018finrregulatesexpression pages 3-4). The pathway proceeds through seven enzymatic steps:

1. **NicA/NicB** (nicotinate hydroxylase complex): Hydroxylates nicotinate to 6-hydroxynicotinate (6-HNA). NicB2 binds substrate and the MCD cofactor; NicB1 mediates electron transfer to cytochrome c oxidase (brickman2018thebordetellabronchiseptica pages 3-3, brickman2018thebordetellabronchiseptica pages 4-4).
2. **NicC** (6-hydroxynicotinate 3-monooxygenase): Catalyzes oxidative decarboxylation of 6-HNA to 2,5-dihydroxypyridine (2,5-DHP) (brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4).
3. **NicX** (2,5-dihydroxypyridine 5,6-dioxygenase): An Fe²⁺-dependent dioxygenase that performs ring cleavage of 2,5-DHP to yield N-formylmaleamic acid (brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4).
4. **NicD** (N-formylmaleamate deformylase): Hydrolytically removes formate from N-formylmaleamic acid to produce maleamate (brickman2018thebordetellabronchiseptica pages 4-4).
5. **NicF** (maleamate amidohydrolase): Converts maleamate to maleate and ammonia (brickman2018thebordetellabronchiseptica pages 4-4).
6. **MaiA/NicE** (maleate isomerase, EC 5.2.1.1): Isomerizes maleate to fumarate, which enters the TCA cycle (brickman2018thebordetellabronchiseptica pages 4-4).

The *nic* cluster is organized into three NA-inducible operons: *nicAB*, *nicXR*, and *nicCDEFTP* (xiao2018finrregulatesexpression pages 3-4). Transcriptional regulation involves two cooperating regulators: **NicR**, a MarR-family repressor that is derepressed by 6-HNA (the first pathway intermediate), and **FinR**, a LysR-type positive regulator that enhances expression of the *nicC* and *nicX* operons (xiao2018finrregulatesexpression pages 3-4, xiao2018finrregulatesexpression pages 8-10, xiao2018finrregulatesexpression pages 1-2). Deletion of *finR* substantially reduces expression of *nicC* and *nicX* and impairs growth on nicotinate as sole carbon source (xiao2018finrregulatesexpression pages 8-10).

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive reference for all enzymes in the system:

| Gene name | Protein/Enzyme name | EC number | Enzymatic activity/function | Pathway module | Substrate(s) | Product(s) | Key features/notes |
|---|---|---|---|---|---|---|---|
| **nadB** | L-aspartate oxidase | **1.4.3.16** | Oxidizes L-aspartate to iminosuccinate in the first committed step of the bacterial aspartate route to quinolinate | De novo biosynthesis | L-aspartate, FAD; O2 or fumarate as electron acceptor in different systems | 2-iminosuccinate (iminoaspartate) | FAD-bound enzyme; upstream of NadA; product is labile and functionally coupled to quinolinate synthesis (luo2023biosynthesisofnicotinamide pages 2-4, zhu2021metabolicengineeringof pages 1-2, ding2021constructionofan pages 1-2) |
| **nadA** | Quinolinate synthase | **2.5.1.72** | Condenses iminosuccinate with dihydroxyacetone phosphate to form quinolinate | De novo biosynthesis | 2-iminosuccinate, DHAP | Quinolinate (QA) | Oxygen-sensitive **[4Fe-4S]** enzyme; frequently discussed with NadB as a coupled QA-forming module (zhu2021metabolicengineeringof pages 1-2, ding2021constructionofan pages 1-2) |
| **nadC** | Quinolinate phosphoribosyltransferase / nicotinate-nucleotide diphosphorylase (carboxylating) | **2.4.2.19** | Transfers phosphoribosyl group from PRPP to quinolinate to make nicotinate mononucleotide | De novo biosynthesis | Quinolinate, PRPP | NaMN | Entry point from quinolinate into the shared late NAD pathway; also point of convergence with nicotinate salvage (luo2023biosynthesisofnicotinamide pages 2-4, ding2021constructionofan pages 1-2) |
| **nadD** | NaMN adenylyltransferase / nicotinate-nucleotide adenylyltransferase | **2.7.7.18** | Adenylylates NaMN to nicotinic acid adenine dinucleotide | De novo biosynthesis | NaMN, ATP | NaAD, PPi | Shared late step used by both de novo and nicotinate salvage routes (luo2023biosynthesisofnicotinamide pages 2-4, ding2021constructionofan pages 1-2) |
| **nadE** | NAD synthetase | **6.3.1.5** | Amidates NaAD to NAD+ using ammonia, often derived from glutamine hydrolysis | De novo biosynthesis | NaAD, ATP, NH3 or glutamine | NAD+, AMP, PPi | Final obligatory step in bacterial NAD synthesis; subject to feedback and nutritional control via PII in many bacteria (luo2023biosynthesisofnicotinamide pages 2-4, santos2020nad+biosynthesisin pages 6-8, santos2020nad+biosynthesisin pages 1-2, santos2020nad+biosynthesisin pages 4-6) |
| **pncB** | Nicotinate phosphoribosyltransferase | **2.4.2.11** | Converts nicotinate to NaMN in the Preiss-Handler salvage route | Salvage | Nicotinate, PRPP | NaMN | Core nicotinate salvage entry enzyme; often regulated with other NAD salvage genes and repressed by NadR in enterobacteria (brickman2018thebordetellabronchiseptica pages 2-3, guragain2018thetranscriptionalregulator pages 3-5, mao2025cdigmpregulatesbacterial pages 1-2, mao2025cdigmpregulatesbacterial pages 2-5) |
| **pncC** | Nicotinamide-nucleotide amidase | **3.5.1.42** | Hydrolyzes nicotinamide mononucleotide to nicotinate mononucleotide | Salvage | NMN, H2O | NaMN, NH3 | Supports salvage/recycling by funneling amidated pyridine nucleotide intermediates into the nicotinate branch; less directly documented in the retrieved Pseudomonas-focused literature than PncA/PncB (brickman2018thebordetellabronchiseptica pages 2-3, guragain2018thetranscriptionalregulator pages 3-5) |
| **nadK** | NAD kinase | **2.7.1.23** | Phosphorylates NAD+ to NADP+ | NADP formation/interconversion | NAD+, ATP | NADP+, ADP | Canonical source of NADP+ pool; separates biosynthetic/redox-anabolic cofactors from the NAD(H) pool; direct KT2440-specific mechanistic detail was limited in retrieved evidence (partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 9-12) |
| **sthA** | Soluble pyridine nucleotide transhydrogenase | **1.6.1.1** | Reversible hydride transfer between NAD(H) and NADP(H) in the soluble compartment | NADP formation/interconversion | NADH + NADP+ / NADPH + NAD+ | NAD+ + NADPH / NADH + NADP+ | Soluble, FAD-containing transhydrogenase; in **P. putida** acts as a major sink for excess NADH and is critical for acetate growth; direction is condition-dependent rather than fixed (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 15-18, partipilo2025integratedcontrolof pages 12-15) |
| **pntAA** | Proton-translocating transhydrogenase subunit alpha | **1.6.1.2** (complex) | Alpha subunit of membrane transhydrogenase that couples hydride transfer to proton motive force | NADP formation/interconversion | Acts within PntAB complex on NAD(H)/NADP(H) pools | Acts within PntAB complex | Membrane-bound component of energy-linked transhydrogenase; contributes to redox balancing under varying regimes (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 47-51) |
| **pntAB** | Proton-translocating transhydrogenase alpha-associated component / PntAB complex annotation | **1.6.1.2** (complex) | Energy-linked transhydrogenase function interconverting NAD(H) and NADP(H) using proton motive force | NADP formation/interconversion | NADH + NADP+ / NADPH + NAD+ | NAD+ + NADPH / NADH + NADP+ | In KT2440 literature, the membrane transhydrogenase is usually discussed functionally as **PntAB**; generally favors NADPH generation but behaves reversibly in vivo (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 18-21, partipilo2025integratedcontrolof pages 47-51) |
| **pntB** | Proton-translocating transhydrogenase subunit beta | **1.6.1.2** (complex) | Beta subunit of membrane transhydrogenase | NADP formation/interconversion | Acts within PntAB complex | Acts within PntAB complex | PntB carries part of the membrane/catalytic machinery for proton-coupled transhydrogenation; loss is buffered by SthA unless both systems are absent (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 15-18) |
| **nicA** | Nicotinate hydroxylase small subunit | — | Part of the initial nicotinate hydroxylase system converting nicotinate to 6-hydroxynicotinate | Nicotinate catabolism | Nicotinate | 6-hydroxynicotinate (via NicAB complex) | In KT2440 the first step is assigned to **NicA/NicB**; NicA/NicB/NicS are less FinR-responsive than downstream operons (brickman2018thebordetellabronchiseptica pages 3-3, xiao2018finrregulatesexpression pages 3-4, xiao2018finrregulatesexpression pages 2-3) |
| **nicB** | Nicotinate hydroxylase large/electron-transfer subunit | — | Partner subunit in nicotinate hydroxylase complex for initial hydroxylation of nicotinate | Nicotinate catabolism | Nicotinate | 6-hydroxynicotinate (via NicAB complex) | Orthologous systems indicate multi-component hydroxylase organization with substrate-binding and electron-transfer functions split across subunits (brickman2018thebordetellabronchiseptica pages 3-3, brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4) |
| **nicC** | 6-hydroxynicotinate 3-monooxygenase | — | Oxidative decarboxylation of 6-hydroxynicotinate to 2,5-dihydroxypyridine | Nicotinate catabolism | 6-hydroxynicotinate | 2,5-dihydroxypyridine | Key induced step; strongly controlled by FinR and NicR at the **nicCDEFTP** operon (brickman2018thebordetellabronchiseptica pages 3-3, brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4, xiao2018finrregulatesexpression pages 8-10) |
| **nicX** | 2,5-dihydroxypyridine 5,6-dioxygenase | — | Ring-cleavage of 2,5-dihydroxypyridine to N-formylmaleamate | Nicotinate catabolism | 2,5-dihydroxypyridine, O2 | N-formylmaleamate | Fe2+-dependent dioxygenase; central ring-opening step; expression requires FinR-positive input and relief of NicR repression (brickman2018thebordetellabronchiseptica pages 3-3, brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4, xiao2018finrregulatesexpression pages 8-10) |
| **nicD** | N-formylmaleamate deformylase | — | Hydrolytic deformylation of N-formylmaleamate | Nicotinate catabolism | N-formylmaleamate, H2O | Maleamate, formate | Downstream hydrolytic step following NicX-mediated ring cleavage (brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4) |
| **nicF** | Maleamate amidohydrolase | — | Hydrolyzes maleamate to maleate and ammonia | Nicotinate catabolism | Maleamate, H2O | Maleate, NH3 | Produces maleate for final funneling into central metabolism (brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4) |
| **maiA / nicE** | Maleate cis-trans isomerase | **5.2.1.1** | Converts maleate to fumarate | Nicotinate catabolism | Maleate | Fumarate | Final step linking nicotinate catabolism to the TCA cycle; often called **NicE** in nic clusters and **MaiA** in broader maleate metabolism (brickman2018thebordetellabronchiseptica pages 4-4, xiao2018finrregulatesexpression pages 3-4) |
| **ushA** | 5'-nucleotidase / UDP-sugar hydrolase / cyclic phosphodiesterase | **3.1.3.5** (broad family assignment) | Periplasmic broad-specificity phosphatase that dephosphorylates extracellular nucleotides and related metabolites | Boundary context | 5'-nucleotides and other phosphorylated metabolites | Nucleosides + phosphate | Best treated as nucleotide-recycling/periplasmic nutrition context rather than a core pyridine nucleotide interconversion enzyme; may influence precursor availability indirectly (zakataeva2021microbial5′nucleotidasestheir pages 12-14, zakataeva2021microbial5′nucleotidasestheir pages 11-12, zakataeva2021microbial5′nucleotidasestheir pages 1-2) |
| **surE** | Stationary-phase 5'-/3'-nucleotidase family protein | **3.1.3.5** (family-level assignment; variable) | Broad nucleotidase/phosphatase involved in nucleotide pool control and stress survival | Boundary context | AMP and other nucleotide phosphates | Nucleosides + phosphate | Conserved stress-associated phosphatase; affects nucleotide homeostasis but is not a dedicated NAD biosynthetic enzyme (zakataeva2021microbial5′nucleotidasestheir pages 12-14, zakataeva2021microbial5′nucleotidasestheir pages 17-18, zakataeva2021microbial5′nucleotidasestheir pages 11-12) |
| **nudC** | NAD-capped RNA hydrolase / Nudix pyrophosphohydrolase | **3.6.1.-** | Removes NAD, NADH, and dpCoA caps from 5'-capped RNAs; also linked historically to NAD(H) pyrophosphohydrolase activity | Boundary context | NAD-capped RNA, NADH-capped RNA, dpCoA-capped RNA | Monophosphorylated RNA + NMN-related cap products | Boundary enzyme connecting NAD chemistry to epitranscriptomic control and stress responses; not part of bulk NAD biosynthesis or salvage (mickute2023interplaybetweenbacterial pages 1-2, mickute2023interplaybetweenbacterial pages 2-5) |
| **cobB** | NAD-dependent sirtuin deacylase | **3.5.1.98** (deacetylase; broader deacylase activities also reported) | Removes acyl groups from lysine residues using NAD+ as cosubstrate | Boundary context | Acyl-lysine proteins, NAD+ | Deacylated protein, nicotinamide, O-acyl-ADP-ribose | Major NAD-consuming enzyme at pathway boundary; couples protein acylation state to NAD availability and central metabolism (lammers2021posttranslationallysineac(et)ylation pages 11-12, gallegojara2021bacterialsirtuinsoverview pages 2-3, rizo2024bacterialproteinacetylation pages 7-8, gallegojara2021bacterialsirtuinsoverview pages 4-6) |


*Table: This table summarizes the major enzymes and boundary-context proteins in the Pseudomonas putida KT2440 NAD biosynthesis and nicotinate metabolism module, organized by pathway segment. It is useful as a compact reference linking genes, reactions, substrates/products, and system-level notes with supporting citations.*

### 4.1 Boundary Context Enzymes

**UshA (5'-nucleotidase/cyclic phosphodiesterase)** is a periplasmic broad-specificity phosphatase that dephosphorylates extracellular nucleotides and related phosphorylated metabolites, including UDP-sugars and CDP-alcohols. It enables bacterial growth on nucleotides as nutrient sources and participates in purine/pyrimidine salvage, but does not directly participate in pyridine nucleotide biosynthesis (zakataeva2021microbial5′nucleotidasestheir pages 12-14, zakataeva2021microbial5′nucleotidasestheir pages 11-12, zakataeva2021microbial5′nucleotidasestheir pages 1-2).

**SurE (stationary-phase 5'-nucleotidase)** is an evolutionarily conserved phosphatase with 5'- and 3'-nucleotidase activities, critical for stress survival and stationary-phase fitness. It regulates dNTP/NTP pools and enables survival under phosphate limitation (zakataeva2021microbial5′nucleotidasestheir pages 12-14, zakataeva2021microbial5′nucleotidasestheir pages 17-18, zakataeva2021microbial5′nucleotidasestheir pages 11-12).

**NudC (NAD-capped RNA hydrolase)** is a Nudix family pyrophosphohydrolase that removes NAD+, NADH, and dpCoA caps from 5'-capped bacterial RNAs, yielding monophosphorylated RNA and NMN-related products (mickute2023interplaybetweenbacterial pages 1-2, mickute2023interplaybetweenbacterial pages 2-5). NudC associates with RNA degradosome proteins and stress-responsive factors, and its inactivation alters levels of transcripts associated with chemotaxis and flagellar assembly. NudC suppresses flagellar movement and coordinates stress-avoidance behavior in interplay with the DEAD-box RNA helicase CsdA (mickute2023interplaybetweenbacterial pages 1-2). This positions NudC as an epitranscriptomic modulator that intersects NAD metabolism through its cofactor-derived substrate rather than as a core NAD biosynthetic enzyme.

**CobB (NAD-dependent sirtuin deacylase)** is the principal bacterial sirtuin, originally identified in *Salmonella enterica* for its roles in cobalamin biosynthesis and propionate catabolism (lammers2021posttranslationallysineac(et)ylation pages 11-12, gallegojara2021bacterialsirtuinsoverview pages 2-3). CobB catalyzes NAD+-dependent removal of acyl groups (acetyl, succinyl, malonyl, propionyl) from lysine residues in target proteins, consuming NAD+ and producing nicotinamide and O-acyl-ADP-ribose (lammers2021posttranslationallysineac(et)ylation pages 11-12, rizo2024bacterialproteinacetylation pages 7-8, rizo2024bacterialproteinacetylation pages 8-10). Its mechanism involves nucleophilic attack of the acyl-lysine carbonyl oxygen on the C-1' carbon of the NAD+ ribose, followed by nicotinamide release and formation of a C-1'-O-alkylamidate intermediate (lammers2021posttranslationallysineac(et)ylation pages 11-12, rizo2024bacterialproteinacetylation pages 8-10). CobB regulates key metabolic enzymes including acetyl-CoA synthetase (Acs), pyruvate dehydrogenase, and the chemotactic regulator CheY (gallegojara2021bacterialsirtuinsoverview pages 2-3, dash2021proteinacetyltransferasesmediate pages 5-7, gallegojara2021bacterialsirtuinsoverview pages 4-6, gallegojara2021bacterialsirtuinsoverview pages 3-4). Importantly, the nicotinamide product of CobB-mediated deacylation can be recycled back to NAD+ through the salvage pathway, linking protein acylation state to NAD+ homeostasis (gallegojara2021bacterialsirtuinsoverview pages 4-6).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Two Routes to Quinolinate

The deepest division in NAD de novo biosynthesis lies in the choice of precursor amino acid. Most bacteria and plants use the **aspartate route** (NadB/NadA → quinolinate), while mammals, fungi, and some bacteria use the **tryptophan/kynurenine route** (IDO/TDO → kynurenine → 3-hydroxyanthranilic acid → quinolinate via four enzymatic steps) (ding2021constructionofan pages 1-2). Both pathways converge at quinolinate, after which the NadC → NadD → NadE steps are universal. A third, recently described **C3N pathway** from chorismate provides an alternative route to quinolinate that yields extremely high cellular NAD(H) concentrations in *E. coli* (ding2021constructionofan pages 1-2). *P. putida* KT2440 employs the canonical aspartate route.

### 5.2 Conservation of NadE Regulation by PII Signaling

The final biosynthetic enzyme NadE is subject to conserved nutritional regulation across prokaryotes. Santos et al. (2020) identified 19,848 NadE sequences distributed across 1,772 eukaryotes, 17,578 bacteria, and 222 archaea, demonstrating that glutamine-dependent NadE (NadE^Gln) is widespread (santos2020nad+biosynthesisin pages 6-8). The PII signal transduction protein physically interacts with NadE^Gln, relieving NAD+ feedback inhibition. The allosteric effector 2-oxoglutarate (2-OG), a cellular nitrogen-level indicator, inhibits PII-NadE complex formation within physiological concentrations (IC₅₀ shifting from 1 mM to 2.5 mM NAD+ with PII present) (santos2020nad+biosynthesisin pages 4-6). This mechanism is conserved in distantly related bacteria, including β- and γ-Proteobacteria, Firmicutes, Nitrospirae, Actinobacteria, and archaeal phyla (santos2020nad+biosynthesisin pages 4-6).

### 5.3 NadR-Mediated Regulation in Enterobacterales

In *Salmonella* and other Enterobacterales, the trifunctional protein NadR acts as a transcriptional repressor of *nadB*, *nadA*, *pnuC*, and *pncB* while also possessing NMN adenylyltransferase and ribosylnicotinamide kinase activities (mao2025cdigmpregulatesbacterial pages 1-2, mao2025cdigmpregulatesbacterial pages 2-5). Recent work by Mao et al. (2025) demonstrated that c-di-GMP binds NadR with high affinity (K_d = 0.16 µM), inhibiting its DNA-binding activity and thereby derepressing NAD biosynthetic genes. Elevated c-di-GMP increases intracellular NAD+ and NADH levels approximately 1.5-fold and enhances bacterial resistance to DNA damage (mao2025cdigmpregulatesbacterial pages 2-5, mao2025cdigmpregulatesbacterial pages 10-13, mao2025cdigmpregulatesbacterial pages 13-14). Notably, *P. putida* KT2440 lacks the multifunctional NadR found in enterobacteria, and its NAD biosynthetic regulation likely operates through different mechanisms, though this remains incompletely characterized.

### 5.4 Convergent Evolution of Nicotinate Catabolism

Aerobic nicotinate catabolism has evolved independently in prokaryotes and eukaryotes. In *P. putida* KT2440, the *nic* pathway proceeds from nicotinate through 6-HNA → 2,5-DHP → ring cleavage via NicX dioxygenase → N-formylmaleamate → fumarate (brickman2018thebordetellabronchiseptica pages 3-3, brickman2018thebordetellabronchiseptica pages 4-4). In the ascomycete *Aspergillus nidulans*, a completely different eleven-gene (*hxn*) pathway achieves the same outcome through distinct chemistry: after the initial hydroxylation to 6-hydroxynicotinic acid (catalyzed by an independently evolved molybdenum hydroxylase), the fungal pathway produces unique intermediates including 5,6-dihydroxypiperidine-2-one and 3-hydroxypiperidine-2,6-dione, followed by ring opening to α-hydroxyglutaramate—none of which are detected in prokaryotic pathways (bokor2022acompletenicotinate pages 2-3, bokor2021nicotinatedegradationin pages 1-6, bokor2022acompletenicotinate pages 1-2). While both pathways share the 2,5-dihydroxypyridine intermediate, the downstream processing strategies diverge fundamentally: bacteria use extradiol dioxygenase ring cleavage, whereas fungi saturate and oxidize the pyridine ring before hydrolytic C-N bond opening (bokor2022acompletenicotinate pages 7-8, bokor2021nicotinatedegradationin pages 17-20). This represents a striking case of convergent metabolic evolution between prokaryotic and eukaryotic microorganisms (bokor2022acompletenicotinate pages 1-2).

The *nic* gene cluster is not restricted to *P. putida*. Orthologs have been identified in *Bordetella bronchiseptica* (with 41–80% amino acid identity to KT2440 proteins), *Burkholderia gladioli*, and other proteobacteria, where nicotinate catabolism modulates diverse phenotypes including growth, virulence gene regulation, biofilm formation, and mycophagy (brickman2018thebordetellabronchiseptica pages 3-3).

### 5.5 Transhydrogenase Distribution

Comparative genomics indicates that PntAB (membrane-bound transhydrogenase) is more widely distributed across bacterial species than SthA (soluble transhydrogenase), and that transhydrogenase gene neighborhoods are often associated with stress and membrane processes (partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 12-15). The co-occurrence of both systems in *P. putida* enables a particularly robust and flexible redox-balancing capacity that contributes to this organism's stress tolerance and metabolic versatility.

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Ordering

The de novo pathway follows a strict linear sequence: L-Asp → iminosuccinate (NadB) → quinolinate (NadA) → NaMN (NadC) → NaAD (NadD) → NAD+ (NadE). No step can be bypassed, and no alternative enzyme exists for any individual step in *P. putida* (luo2023biosynthesisofnicotinamide pages 2-4, ding2021constructionofan pages 1-2). The NadB product iminosuccinate is chemically unstable, imposing a kinetic coupling requirement with NadA—if NadA activity is insufficient, iminosuccinate decomposes non-productively (zhu2021metabolicengineeringof pages 1-2).

### 6.2 Oxygen Sensitivity of NadA

The [4Fe-4S] cluster of NadA is oxygen-labile, which can limit de novo NAD biosynthesis under conditions of oxidative stress or iron limitation (zhu2021metabolicengineeringof pages 1-2). This creates a paradox: *P. putida* is an obligate aerobe that relies on an oxygen-sensitive enzyme for de novo NAD synthesis, presumably compensated by efficient iron-sulfur cluster biogenesis and the availability of salvage routes.

### 6.3 Transhydrogenase Redundancy and Conditional Essentiality

While single deletions of PntAB or SthA are tolerated, the double mutant is severely compromised, with 32% lower NAD+ levels, depleted ATP, and impaired glutathione maintenance (partipilo2025integratedcontrolof pages 6-9). SthA is conditionally essential for growth on acetate, traced to a transcriptional regulator involved in glyoxylate metabolism (partipilo2025integratedcontrolof pages 1-6). During formate detoxification, both transhydrogenases synergistically channel reducing equivalents from formate oxidation, acting as a "redox safety valve" (partipilo2025integratedcontrolof pages 18-21, partipilo2025integratedcontrolof pages 12-15).

### 6.4 NAD+ as a Hub Metabolite

NAD+ is not merely a redox cofactor but serves as a substrate for multiple consuming reactions: CobB-mediated protein deacylation (producing nicotinamide), NudC-mediated RNA decapping (producing NMN), DNA ligase activity, and poly-ADP-ribosylation in some organisms (lammers2021posttranslationallysineac(et)ylation pages 11-12, mickute2023interplaybetweenbacterial pages 1-2). The nicotinamide product of these reactions can re-enter the salvage pathway, creating a recycling loop. The balance between NAD+ consumption and regeneration must be tightly maintained; PII-NadE signaling provides one conserved mechanism for integrating carbon/nitrogen status with NAD+ supply (santos2020nad+biosynthesisin pages 6-8, santos2020nad+biosynthesisin pages 1-2).

## 7. Controversies and Open Questions

**NadR in *P. putida*:** While the c-di-GMP/NadR regulatory axis has been elegantly characterized in Enterobacterales (mao2025cdigmpregulatesbacterial pages 1-2, mao2025cdigmpregulatesbacterial pages 2-5), *P. putida* KT2440 lacks a clear NadR ortholog with all three functional domains (HTH, NMN-AT, RNam-K). How *P. putida* coordinates NAD biosynthetic gene expression with nutritional status remains an important open question.

**Transhydrogenase directionality:** The traditional model from *E. coli* assigns PntAB as a primary NADPH generator and SthA as an NADPH dissipater. The *P. putida* data from Partipilo et al. (2025) challenge this simple assignment, showing that both enzymes function reversibly with direction determined by metabolic context rather than intrinsic enzyme properties (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 18-21). Whether this flexibility is unique to *P. putida* or a general but under-appreciated bacterial property remains unresolved.

**PncC characterization in *P. putida*:** The specific contribution of PncC (nicotinamide-nucleotide amidase) to NAD salvage in KT2440 is less well documented experimentally than PncB. Its relative importance versus the PncA → PncB route deserves further study.

**Nicotinate catabolism regulation:** The cooperative regulation by NicR (repressor) and FinR (activator) of the *nic* pathway operons has been demonstrated in KT2440 (xiao2018finrregulatesexpression pages 3-4, xiao2018finrregulatesexpression pages 8-10), but the molecular mechanism of how FinR and NicR interact at shared promoter regions—and whether additional regulators participate—remains to be fully elucidated.

**Evolutionary origin of nicotinate catabolism:** The independent evolution of nicotinate degradation in fungi and bacteria, documented through completely different intermediates and enzyme families (bokor2022acompletenicotinate pages 2-3, bokor2021nicotinatedegradationin pages 1-6, bokor2022acompletenicotinate pages 1-2), raises questions about the selective pressures favoring nicotinate catabolism. Whether the primary driver is carbon/nitrogen acquisition, pyridine detoxification, or modulation of intracellular NAD pools remains debated.

**Compartmentalization effects:** In fungi, some nicotinate catabolic steps (e.g., HxnX-catalyzed conversion) occur in peroxisomes (bokor2022acompletenicotinate pages 2-3). In bacteria, all reactions are presumed cytoplasmic, but the periplasmic localization of UshA and the membrane association of PntAB introduce spatial considerations for NAD precursor availability that have not been systematically addressed in *P. putida*.

## 8. Key References

The following sources provide the primary evidentiary basis for this review:

- Luo et al. (2023) *Fermentation* 9:594 — NMN biosynthesis strategies including de novo pathway enzymology (luo2023biosynthesisofnicotinamide pages 2-4)
- Zhu et al. (2021) *Metabolic Engineering* 67:164-172 — NadB/NadA enzyme complex and quinolinate production (zhu2021metabolicengineeringof pages 1-2, zhu2021metabolicengineeringof pages 8-9)
- Ding et al. (2021) *Advanced Science* 8:2004632 — Alternative C3N pathway and de novo NAD biosynthesis routes (ding2021constructionofan pages 1-2)
- Santos et al. (2020) *J. Biol. Chem.* 295:6165-6176 — PII-NadE signaling and evolutionary conservation (santos2020nad+biosynthesisin pages 6-8, santos2020nad+biosynthesisin pages 1-2, santos2020nad+biosynthesisin pages 4-6)
- Mao et al. (2025) *mBio* e0198225 — c-di-GMP regulation of NAD biosynthesis via NadR (mao2025cdigmpregulatesbacterial pages 1-2, mao2025cdigmpregulatesbacterial pages 5-7, mao2025cdigmpregulatesbacterial pages 2-5, mao2025cdigmpregulatesbacterial pages 7-10, mao2025cdigmpregulatesbacterial pages 10-13, mao2025cdigmpregulatesbacterial pages 13-14)
- Partipilo et al. (2025) *bioRxiv* doi:10.1101/2025.11.04.686620 — PntAB/SthA transhydrogenase roles in *P. putida* (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 15-18, partipilo2025integratedcontrolof pages 18-21, partipilo2025integratedcontrolof pages 12-15, partipilo2025integratedcontrolof pages 9-12, partipilo2025integratedcontrolof pages 47-51)
- Xiao et al. (2018) *Appl. Environ. Microbiol.* 84:e01210-18 — FinR/NicR regulation of nicotinate catabolism in KT2440 (xiao2018finrregulatesexpression pages 3-4, xiao2018finrregulatesexpression pages 8-10, xiao2018finrregulatesexpression pages 1-2, xiao2018finrregulatesexpression pages 2-3)
- Brickman & Armstrong (2018) *Mol. Microbiol.* 108:397-409 — Nicotinate degradation pathway and regulation in Bordetella (brickman2018thebordetellabronchiseptica pages 3-3, brickman2018thebordetellabronchiseptica pages 4-4)
- Guragain et al. (2018) *J. Bacteriol.* 200:e00712-17 — BpsR/NicR regulation and nicotinate salvage context (guragain2018thetranscriptionalregulator pages 3-5)
- Bokor et al. (2022) *Commun. Biol.* 5:697 — Complete eukaryotic nicotinate catabolism and convergent evolution (bokor2022acompletenicotinate pages 2-3, bokor2022acompletenicotinate pages 7-8, bokor2022acompletenicotinate pages 1-2)
- Bokor et al. (2021) *bioRxiv* doi:10.1101/2021.08.17.456622 — Novel intermediates in *A. nidulans* nicotinate degradation (bokor2021nicotinatedegradationin pages 1-6, bokor2021nicotinatedegradationin pages 17-20)
- Mickutė et al. (2023) *mSystems* 8:e00718-23 — NudC as NAD-RNA decapping enzyme in stress responses (mickute2023interplaybetweenbacterial pages 1-2, mickute2023interplaybetweenbacterial pages 2-5)
- Gallego-Jara et al. (2021) *Front. Microbiol.* 12:744416 — Bacterial sirtuin CobB overview (gallegojara2021bacterialsirtuinsoverview pages 2-3, gallegojara2021bacterialsirtuinsoverview pages 4-6, gallegojara2021bacterialsirtuinsoverview pages 3-4)
- Rizo & Encarnación-Guevara (2024) *Front. Cell. Infect. Microbiol.* 14:1408947 — CobB structure and mechanism (rizo2024bacterialproteinacetylation pages 7-8, rizo2024bacterialproteinacetylation pages 8-10)
- Lammers (2021) *Front. Microbiol.* 12:757179 — Bacterial protein acylation and CobB biochemistry (lammers2021posttranslationallysineac(et)ylation pages 11-12)
- Parks & Escalante-Semerena (2020) *PNAS* 117:15895-15901 — CobB isoforms and modulation (parks2020modulationofthe pages 1-2)
- Zakataeva (2021) *Appl. Microbiol. Biotechnol.* 105:7661-7681 — Microbial 5'-nucleotidases including UshA and SurE (zakataeva2021microbial5′nucleotidasestheir pages 12-14, zakataeva2021microbial5′nucleotidasestheir pages 17-18, zakataeva2021microbial5′nucleotidasestheir pages 11-12, zakataeva2021microbial5′nucleotidasestheir pages 1-2)

References

1. (luo2023biosynthesisofnicotinamide pages 2-4): Shiqi Luo, Juntao Zhao, Yangyang Zheng, Tao Chen, and Zhiwen Wang. Biosynthesis of nicotinamide mononucleotide: current metabolic engineering strategies, challenges, and prospects. Fermentation, 9:594, Jun 2023. URL: https://doi.org/10.3390/fermentation9070594, doi:10.3390/fermentation9070594. This article has 20 citations.

2. (ding2021constructionofan pages 1-2): Yong Ding, Xinli Li, Geoff P. Horsman, Pengwei Li, Min Wang, Jine Li, Zhilong Zhang, Weifeng Liu, Bian Wu, Yong Tao, and Yihua Chen. Construction of an alternative nad+ de novo biosynthesis pathway. Advanced Science, Mar 2021. URL: https://doi.org/10.1002/advs.202004632, doi:10.1002/advs.202004632. This article has 37 citations and is from a peer-reviewed journal.

3. (brickman2018thebordetellabronchiseptica pages 3-3): Timothy J. Brickman and Sandra K. Armstrong. The bordetella bronchiseptica nic locus encodes a nicotinic acid degradation pathway and the 6‐hydroxynicotinate‐responsive regulator bpsr. Molecular Microbiology, 108:397-409, May 2018. URL: https://doi.org/10.1111/mmi.13943, doi:10.1111/mmi.13943. This article has 14 citations and is from a domain leading peer-reviewed journal.

4. (mickute2023interplaybetweenbacterial pages 1-2): Milda Mickutė, Renatas Krasauskas, Kotryna Kvederavičiūtė, Gytė Tupikaitė, Aleksandr Osipenko, Algirdas Kaupinis, Monika Jazdauskaitė, Raminta Mineikaitė, Mindaugas Valius, Viktoras Masevičius, and Giedrius Vilkaitis. Interplay between bacterial 5′-nad-rna decapping hydrolase nudc and dead-box rna helicase csda in stress responses. mSystems, Oct 2023. URL: https://doi.org/10.1128/msystems.00718-23, doi:10.1128/msystems.00718-23. This article has 4 citations and is from a peer-reviewed journal.

5. (lammers2021posttranslationallysineac(et)ylation pages 11-12): Michael Lammers. Post-translational lysine ac(et)ylation in bacteria: a biochemical, structural, and synthetic biological perspective. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.757179, doi:10.3389/fmicb.2021.757179. This article has 36 citations and is from a peer-reviewed journal.

6. (zakataeva2021microbial5′nucleotidasestheir pages 12-14): Natalia P. Zakataeva. Microbial 5′-nucleotidases: their characteristics, roles in cellular metabolism, and possible practical applications. Applied Microbiology and Biotechnology, 105:7661-7681, Sep 2021. URL: https://doi.org/10.1007/s00253-021-11547-w, doi:10.1007/s00253-021-11547-w. This article has 49 citations and is from a domain leading peer-reviewed journal.

7. (zhu2021metabolicengineeringof pages 1-2): Fayin Zhu, Matthew Peña, and George N. Bennett. Metabolic engineering of escherichia coli for quinolinic acid production by assembling l-aspartate oxidase and quinolinate synthase as an enzyme complex. Metabolic Engineering, 67:164-172, Sep 2021. URL: https://doi.org/10.1016/j.ymben.2021.06.007, doi:10.1016/j.ymben.2021.06.007. This article has 31 citations and is from a domain leading peer-reviewed journal.

8. (zhu2021metabolicengineeringof pages 8-9): Fayin Zhu, Matthew Peña, and George N. Bennett. Metabolic engineering of escherichia coli for quinolinic acid production by assembling l-aspartate oxidase and quinolinate synthase as an enzyme complex. Metabolic Engineering, 67:164-172, Sep 2021. URL: https://doi.org/10.1016/j.ymben.2021.06.007, doi:10.1016/j.ymben.2021.06.007. This article has 31 citations and is from a domain leading peer-reviewed journal.

9. (santos2020nad+biosynthesisin pages 6-8): Adrian Richard Schenberger Santos, Edileusa Cristina Marques Gerhardt, Erick Parize, Fabio Oliveira Pedrosa, Maria Berenice Reynaud Steffens, Leda Satie Chubatsu, Emanuel Maltempi Souza, Luciane Maria Pereira Passaglia, Fernando Hayashi Sant'Anna, Gustavo Antônio de Souza, Luciano Fernandes Huergo, and Karl Forchhammer. Nad+ biosynthesis in bacteria is controlled by global carbon/nitrogen levels via pii signaling. Journal of Biological Chemistry, 295:6165-6176, May 2020. URL: https://doi.org/10.1074/jbc.ra120.012793, doi:10.1074/jbc.ra120.012793. This article has 30 citations and is from a domain leading peer-reviewed journal.

10. (santos2020nad+biosynthesisin pages 1-2): Adrian Richard Schenberger Santos, Edileusa Cristina Marques Gerhardt, Erick Parize, Fabio Oliveira Pedrosa, Maria Berenice Reynaud Steffens, Leda Satie Chubatsu, Emanuel Maltempi Souza, Luciane Maria Pereira Passaglia, Fernando Hayashi Sant'Anna, Gustavo Antônio de Souza, Luciano Fernandes Huergo, and Karl Forchhammer. Nad+ biosynthesis in bacteria is controlled by global carbon/nitrogen levels via pii signaling. Journal of Biological Chemistry, 295:6165-6176, May 2020. URL: https://doi.org/10.1074/jbc.ra120.012793, doi:10.1074/jbc.ra120.012793. This article has 30 citations and is from a domain leading peer-reviewed journal.

11. (brickman2018thebordetellabronchiseptica pages 2-3): Timothy J. Brickman and Sandra K. Armstrong. The bordetella bronchiseptica nic locus encodes a nicotinic acid degradation pathway and the 6‐hydroxynicotinate‐responsive regulator bpsr. Molecular Microbiology, 108:397-409, May 2018. URL: https://doi.org/10.1111/mmi.13943, doi:10.1111/mmi.13943. This article has 14 citations and is from a domain leading peer-reviewed journal.

12. (guragain2018thetranscriptionalregulator pages 3-5): Manita Guragain, Jamie Jennings-Gee, Natalia Cattelan, Mary Finger, Matt S. Conover, Thomas Hollis, and Rajendar Deora. The transcriptional regulator bpsr controls the growth of bordetella bronchiseptica by repressing genes involved in nicotinic acid degradation. Journal of Bacteriology, Jun 2018. URL: https://doi.org/10.1128/jb.00712-17, doi:10.1128/jb.00712-17. This article has 19 citations and is from a peer-reviewed journal.

13. (partipilo2025integratedcontrolof pages 1-6): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

14. (partipilo2025integratedcontrolof pages 6-9): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

15. (partipilo2025integratedcontrolof pages 15-18): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

16. (partipilo2025integratedcontrolof pages 18-21): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

17. (partipilo2025integratedcontrolof pages 12-15): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

18. (partipilo2025integratedcontrolof pages 9-12): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

19. (xiao2018finrregulatesexpression pages 3-4): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

20. (brickman2018thebordetellabronchiseptica pages 4-4): Timothy J. Brickman and Sandra K. Armstrong. The bordetella bronchiseptica nic locus encodes a nicotinic acid degradation pathway and the 6‐hydroxynicotinate‐responsive regulator bpsr. Molecular Microbiology, 108:397-409, May 2018. URL: https://doi.org/10.1111/mmi.13943, doi:10.1111/mmi.13943. This article has 14 citations and is from a domain leading peer-reviewed journal.

21. (xiao2018finrregulatesexpression pages 8-10): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

22. (xiao2018finrregulatesexpression pages 1-2): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

23. (santos2020nad+biosynthesisin pages 4-6): Adrian Richard Schenberger Santos, Edileusa Cristina Marques Gerhardt, Erick Parize, Fabio Oliveira Pedrosa, Maria Berenice Reynaud Steffens, Leda Satie Chubatsu, Emanuel Maltempi Souza, Luciane Maria Pereira Passaglia, Fernando Hayashi Sant'Anna, Gustavo Antônio de Souza, Luciano Fernandes Huergo, and Karl Forchhammer. Nad+ biosynthesis in bacteria is controlled by global carbon/nitrogen levels via pii signaling. Journal of Biological Chemistry, 295:6165-6176, May 2020. URL: https://doi.org/10.1074/jbc.ra120.012793, doi:10.1074/jbc.ra120.012793. This article has 30 citations and is from a domain leading peer-reviewed journal.

24. (mao2025cdigmpregulatesbacterial pages 1-2): Lianying Mao, Jialin Li, Xinyi Huo, Wenguang Yang, Heng Zhang, Chongyi Duan, Xihui Shen, and Lei Zhang. C-di-gmp regulates bacterial nad biosynthesis via targeting the transcriptional repressor nadr. mBio, pages e0198225, Aug 2025. URL: https://doi.org/10.1128/mbio.01982-25, doi:10.1128/mbio.01982-25. This article has 3 citations and is from a domain leading peer-reviewed journal.

25. (mao2025cdigmpregulatesbacterial pages 2-5): Lianying Mao, Jialin Li, Xinyi Huo, Wenguang Yang, Heng Zhang, Chongyi Duan, Xihui Shen, and Lei Zhang. C-di-gmp regulates bacterial nad biosynthesis via targeting the transcriptional repressor nadr. mBio, pages e0198225, Aug 2025. URL: https://doi.org/10.1128/mbio.01982-25, doi:10.1128/mbio.01982-25. This article has 3 citations and is from a domain leading peer-reviewed journal.

26. (partipilo2025integratedcontrolof pages 47-51): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

27. (xiao2018finrregulatesexpression pages 2-3): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

28. (zakataeva2021microbial5′nucleotidasestheir pages 11-12): Natalia P. Zakataeva. Microbial 5′-nucleotidases: their characteristics, roles in cellular metabolism, and possible practical applications. Applied Microbiology and Biotechnology, 105:7661-7681, Sep 2021. URL: https://doi.org/10.1007/s00253-021-11547-w, doi:10.1007/s00253-021-11547-w. This article has 49 citations and is from a domain leading peer-reviewed journal.

29. (zakataeva2021microbial5′nucleotidasestheir pages 1-2): Natalia P. Zakataeva. Microbial 5′-nucleotidases: their characteristics, roles in cellular metabolism, and possible practical applications. Applied Microbiology and Biotechnology, 105:7661-7681, Sep 2021. URL: https://doi.org/10.1007/s00253-021-11547-w, doi:10.1007/s00253-021-11547-w. This article has 49 citations and is from a domain leading peer-reviewed journal.

30. (zakataeva2021microbial5′nucleotidasestheir pages 17-18): Natalia P. Zakataeva. Microbial 5′-nucleotidases: their characteristics, roles in cellular metabolism, and possible practical applications. Applied Microbiology and Biotechnology, 105:7661-7681, Sep 2021. URL: https://doi.org/10.1007/s00253-021-11547-w, doi:10.1007/s00253-021-11547-w. This article has 49 citations and is from a domain leading peer-reviewed journal.

31. (mickute2023interplaybetweenbacterial pages 2-5): Milda Mickutė, Renatas Krasauskas, Kotryna Kvederavičiūtė, Gytė Tupikaitė, Aleksandr Osipenko, Algirdas Kaupinis, Monika Jazdauskaitė, Raminta Mineikaitė, Mindaugas Valius, Viktoras Masevičius, and Giedrius Vilkaitis. Interplay between bacterial 5′-nad-rna decapping hydrolase nudc and dead-box rna helicase csda in stress responses. mSystems, Oct 2023. URL: https://doi.org/10.1128/msystems.00718-23, doi:10.1128/msystems.00718-23. This article has 4 citations and is from a peer-reviewed journal.

32. (gallegojara2021bacterialsirtuinsoverview pages 2-3): Julia Gallego-Jara, Álvaro Ortega, Gema Lozano Terol, Rosa A. Sola Martínez, Manuel Cánovas Díaz, and Teresa de Diego Puente. Bacterial sirtuins overview: an open niche to explore. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.744416, doi:10.3389/fmicb.2021.744416. This article has 26 citations and is from a peer-reviewed journal.

33. (rizo2024bacterialproteinacetylation pages 7-8): Jocelin Rizo and Sergio Encarnación-Guevara. Bacterial protein acetylation: mechanisms, functions, and methods for study. Frontiers in Cellular and Infection Microbiology, Jul 2024. URL: https://doi.org/10.3389/fcimb.2024.1408947, doi:10.3389/fcimb.2024.1408947. This article has 36 citations.

34. (gallegojara2021bacterialsirtuinsoverview pages 4-6): Julia Gallego-Jara, Álvaro Ortega, Gema Lozano Terol, Rosa A. Sola Martínez, Manuel Cánovas Díaz, and Teresa de Diego Puente. Bacterial sirtuins overview: an open niche to explore. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.744416, doi:10.3389/fmicb.2021.744416. This article has 26 citations and is from a peer-reviewed journal.

35. (rizo2024bacterialproteinacetylation pages 8-10): Jocelin Rizo and Sergio Encarnación-Guevara. Bacterial protein acetylation: mechanisms, functions, and methods for study. Frontiers in Cellular and Infection Microbiology, Jul 2024. URL: https://doi.org/10.3389/fcimb.2024.1408947, doi:10.3389/fcimb.2024.1408947. This article has 36 citations.

36. (dash2021proteinacetyltransferasesmediate pages 5-7): Aiswarya Dash and Rahul Modak. Protein acetyltransferases mediate bacterial adaptation to a diverse environment. Sep 2021. URL: https://doi.org/10.1128/jb.00231-21, doi:10.1128/jb.00231-21. This article has 42 citations and is from a peer-reviewed journal.

37. (gallegojara2021bacterialsirtuinsoverview pages 3-4): Julia Gallego-Jara, Álvaro Ortega, Gema Lozano Terol, Rosa A. Sola Martínez, Manuel Cánovas Díaz, and Teresa de Diego Puente. Bacterial sirtuins overview: an open niche to explore. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.744416, doi:10.3389/fmicb.2021.744416. This article has 26 citations and is from a peer-reviewed journal.

38. (mao2025cdigmpregulatesbacterial pages 10-13): Lianying Mao, Jialin Li, Xinyi Huo, Wenguang Yang, Heng Zhang, Chongyi Duan, Xihui Shen, and Lei Zhang. C-di-gmp regulates bacterial nad biosynthesis via targeting the transcriptional repressor nadr. mBio, pages e0198225, Aug 2025. URL: https://doi.org/10.1128/mbio.01982-25, doi:10.1128/mbio.01982-25. This article has 3 citations and is from a domain leading peer-reviewed journal.

39. (mao2025cdigmpregulatesbacterial pages 13-14): Lianying Mao, Jialin Li, Xinyi Huo, Wenguang Yang, Heng Zhang, Chongyi Duan, Xihui Shen, and Lei Zhang. C-di-gmp regulates bacterial nad biosynthesis via targeting the transcriptional repressor nadr. mBio, pages e0198225, Aug 2025. URL: https://doi.org/10.1128/mbio.01982-25, doi:10.1128/mbio.01982-25. This article has 3 citations and is from a domain leading peer-reviewed journal.

40. (bokor2022acompletenicotinate pages 2-3): Eszter Bokor, Judit Ámon, Mónika Varga, András Szekeres, Zsófia Hegedűs, Tamás Jakusch, Zsolt Szakonyi, Michel Flipphi, Csaba Vágvölgyi, Attila Gácser, Claudio Scazzocchio, and Zsuzsanna Hamari. A complete nicotinate degradation pathway in the microbial eukaryote aspergillus nidulans. Communications Biology, Jul 2022. URL: https://doi.org/10.1038/s42003-022-03684-3, doi:10.1038/s42003-022-03684-3. This article has 11 citations and is from a peer-reviewed journal.

41. (bokor2021nicotinatedegradationin pages 1-6): Eszter Bokor, Judit Ámon, Mónika Varga, András Szekeres, Zsófia Hegedűs, Tamás Jakusch, Michel Flipphi, Csaba Vágvölgyi, Attila Gácser, Claudio Scazzocchio, and Zsuzsanna Hamari. Nicotinate degradation in a microbial eukaryote: a novel, complete pathway extant in aspergillus nidulans. bioRxiv, Aug 2021. URL: https://doi.org/10.1101/2021.08.17.456622, doi:10.1101/2021.08.17.456622. This article has 0 citations.

42. (bokor2022acompletenicotinate pages 1-2): Eszter Bokor, Judit Ámon, Mónika Varga, András Szekeres, Zsófia Hegedűs, Tamás Jakusch, Zsolt Szakonyi, Michel Flipphi, Csaba Vágvölgyi, Attila Gácser, Claudio Scazzocchio, and Zsuzsanna Hamari. A complete nicotinate degradation pathway in the microbial eukaryote aspergillus nidulans. Communications Biology, Jul 2022. URL: https://doi.org/10.1038/s42003-022-03684-3, doi:10.1038/s42003-022-03684-3. This article has 11 citations and is from a peer-reviewed journal.

43. (bokor2022acompletenicotinate pages 7-8): Eszter Bokor, Judit Ámon, Mónika Varga, András Szekeres, Zsófia Hegedűs, Tamás Jakusch, Zsolt Szakonyi, Michel Flipphi, Csaba Vágvölgyi, Attila Gácser, Claudio Scazzocchio, and Zsuzsanna Hamari. A complete nicotinate degradation pathway in the microbial eukaryote aspergillus nidulans. Communications Biology, Jul 2022. URL: https://doi.org/10.1038/s42003-022-03684-3, doi:10.1038/s42003-022-03684-3. This article has 11 citations and is from a peer-reviewed journal.

44. (bokor2021nicotinatedegradationin pages 17-20): Eszter Bokor, Judit Ámon, Mónika Varga, András Szekeres, Zsófia Hegedűs, Tamás Jakusch, Michel Flipphi, Csaba Vágvölgyi, Attila Gácser, Claudio Scazzocchio, and Zsuzsanna Hamari. Nicotinate degradation in a microbial eukaryote: a novel, complete pathway extant in aspergillus nidulans. bioRxiv, Aug 2021. URL: https://doi.org/10.1101/2021.08.17.456622, doi:10.1101/2021.08.17.456622. This article has 0 citations.

45. (mao2025cdigmpregulatesbacterial pages 5-7): Lianying Mao, Jialin Li, Xinyi Huo, Wenguang Yang, Heng Zhang, Chongyi Duan, Xihui Shen, and Lei Zhang. C-di-gmp regulates bacterial nad biosynthesis via targeting the transcriptional repressor nadr. mBio, pages e0198225, Aug 2025. URL: https://doi.org/10.1128/mbio.01982-25, doi:10.1128/mbio.01982-25. This article has 3 citations and is from a domain leading peer-reviewed journal.

46. (mao2025cdigmpregulatesbacterial pages 7-10): Lianying Mao, Jialin Li, Xinyi Huo, Wenguang Yang, Heng Zhang, Chongyi Duan, Xihui Shen, and Lei Zhang. C-di-gmp regulates bacterial nad biosynthesis via targeting the transcriptional repressor nadr. mBio, pages e0198225, Aug 2025. URL: https://doi.org/10.1128/mbio.01982-25, doi:10.1128/mbio.01982-25. This article has 3 citations and is from a domain leading peer-reviewed journal.

47. (parks2020modulationofthe pages 1-2): Anastacia R. Parks and Jorge C. Escalante-Semerena. Modulation of the bacterial cobb sirtuin deacylase activity by n-terminal acetylation. Proceedings of the National Academy of Sciences, 117:15895-15901, Jun 2020. URL: https://doi.org/10.1073/pnas.2005296117, doi:10.1073/pnas.2005296117. This article has 25 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon_artifacts/artifact-01.md)
![Image artifact created (ID artifact-01): 'Pseudomonas NAD Pathway Map' ![Pseudomonas NAD Pathway Map](artifact:artifact-01) Artifact IDs that may be injected in](nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon_artifacts/image-1.png)

## Citations

1. zhu2021metabolicengineeringof pages 1-2
2. zhu2021metabolicengineeringof pages 8-9
3. guragain2018thetranscriptionalregulator pages 3-5
4. brickman2018thebordetellabronchiseptica pages 2-3
5. partipilo2025integratedcontrolof pages 1-6
6. partipilo2025integratedcontrolof pages 6-9
7. brickman2018thebordetellabronchiseptica pages 4-4
8. xiao2018finrregulatesexpression pages 3-4
9. xiao2018finrregulatesexpression pages 8-10
10. mickute2023interplaybetweenbacterial pages 1-2
11. gallegojara2021bacterialsirtuinsoverview pages 4-6
12. ding2021constructionofan pages 1-2
13. bokor2022acompletenicotinate pages 1-2
14. brickman2018thebordetellabronchiseptica pages 3-3
15. bokor2022acompletenicotinate pages 2-3
16. luo2023biosynthesisofnicotinamide pages 2-4
17. parks2020modulationofthe pages 1-2
18. partipilo2025integratedcontrolof pages 15-18
19. partipilo2025integratedcontrolof pages 18-21
20. partipilo2025integratedcontrolof pages 12-15
21. partipilo2025integratedcontrolof pages 9-12
22. xiao2018finrregulatesexpression pages 1-2
23. mao2025cdigmpregulatesbacterial pages 1-2
24. mao2025cdigmpregulatesbacterial pages 2-5
25. partipilo2025integratedcontrolof pages 47-51
26. xiao2018finrregulatesexpression pages 2-3
27. mickute2023interplaybetweenbacterial pages 2-5
28. gallegojara2021bacterialsirtuinsoverview pages 2-3
29. rizo2024bacterialproteinacetylation pages 7-8
30. rizo2024bacterialproteinacetylation pages 8-10
31. dash2021proteinacetyltransferasesmediate pages 5-7
32. gallegojara2021bacterialsirtuinsoverview pages 3-4
33. mao2025cdigmpregulatesbacterial pages 10-13
34. mao2025cdigmpregulatesbacterial pages 13-14
35. bokor2021nicotinatedegradationin pages 1-6
36. bokor2022acompletenicotinate pages 7-8
37. bokor2021nicotinatedegradationin pages 17-20
38. mao2025cdigmpregulatesbacterial pages 5-7
39. mao2025cdigmpregulatesbacterial pages 7-10
40. Pseudomonas NAD Pathway Map
41. 4Fe-4S
42. https://doi.org/10.3390/fermentation9070594,
43. https://doi.org/10.1002/advs.202004632,
44. https://doi.org/10.1111/mmi.13943,
45. https://doi.org/10.1128/msystems.00718-23,
46. https://doi.org/10.3389/fmicb.2021.757179,
47. https://doi.org/10.1007/s00253-021-11547-w,
48. https://doi.org/10.1016/j.ymben.2021.06.007,
49. https://doi.org/10.1074/jbc.ra120.012793,
50. https://doi.org/10.1128/jb.00712-17,
51. https://doi.org/10.1101/2025.11.04.686620,
52. https://doi.org/10.1128/aem.01210-18,
53. https://doi.org/10.1128/mbio.01982-25,
54. https://doi.org/10.3389/fmicb.2021.744416,
55. https://doi.org/10.3389/fcimb.2024.1408947,
56. https://doi.org/10.1128/jb.00231-21,
57. https://doi.org/10.1038/s42003-022-03684-3,
58. https://doi.org/10.1101/2021.08.17.456622,
59. https://doi.org/10.1073/pnas.2005296117,