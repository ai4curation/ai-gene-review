---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T01:17:13.021985'
end_time: '2026-07-07T01:42:29.856851'
duration_seconds: 1516.83
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Terpenoid backbone biosynthesis
  module_summary: A bacterial terpenoid-backbone biosynthesis module centered on the
    methylerythritol phosphate (MEP/DOXP) pathway from pyruvate and glyceraldehyde
    3-phosphate to isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP),
    followed by prenyl-diphosphate synthases that extend these C5 units into geranyl,
    farnesyl, octaprenyl, and undecaprenyl diphosphates. In Pseudomonas putida KT2440,
    KEGG ppu00900 also pulls in thiolase/mevalonate-route-like entries and UbiX flavin
    prenyltransferase chemistry; those are treated as boundary or downstream uses
    rather than evidence for a strict mevalonate pathway.
  module_outline: "- Terpenoid backbone biosynthesis\n  - 1. DXP formation\n  - 1-deoxy-D-xylulose\
    \ 5-phosphate formation\n    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular\
    \ player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase\
    \ activity)\n  - 2. MEP formation\n  - DXP reductoisomerization\n    - Dxr 1-deoxy-D-xylulose-5-phosphate\
    \ reductoisomerase (molecular player: PSEPK dxr; activity or role: 1-deoxy-D-xylulose-5-phosphate\
    \ reductoisomerase activity)\n  - 3. CDP-ME formation\n  - MEP cytidylyltransferase\
    \ step\n    - IspD MEP cytidylyltransferase (molecular player: PSEPK ispD; activity\
    \ or role: 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase activity)\n\
    \  - 4. CDP-ME phosphorylation\n  - CDP-ME kinase step\n    - IspE CDP-ME kinase\
    \ (molecular player: PSEPK ispE; activity or role: 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol\
    \ kinase activity)\n  - 5. MEcPP formation\n  - MEcPP synthase step\n    - IspF\
    \ MEcPP synthase (molecular player: PSEPK ispF; activity or role: 2-C-methyl-D-erythritol\
    \ 2,4-cyclodiphosphate synthase activity)\n  - 6. HMBPP formation\n  - HMBPP synthase\
    \ step\n    - IspG HMBPP synthase (molecular player: PSEPK ispG; activity or role:\
    \ 4-hydroxy-3-methylbut-2-enyl-diphosphate synthase activity (flavodoxin))\n \
    \ - 7. IPP and DMAPP formation\n  - HMBPP reductase step\n    - IspH HMBPP reductase\
    \ (molecular player: PSEPK ispH; activity or role: 4-hydroxy-3-methylbut-2-enyl\
    \ diphosphate reductase activity)\n  - 8. short-chain prenyl diphosphate synthesis\n\
    \  - Farnesyl diphosphate synthesis\n    - IspA farnesyl diphosphate synthase\
    \ (molecular player: PSEPK ispA; activity or role: (2E,6E)-farnesyl diphosphate\
    \ synthase activity)\n  - 9. ubiquinone-side-chain precursor synthesis\n  - Octaprenyl\
    \ diphosphate synthesis\n    - IspB octaprenyl diphosphate synthase (molecular\
    \ player: PSEPK ispB; activity or role: all-trans-octaprenyl-diphosphate synthase\
    \ activity)\n  - 10. undecaprenyl carrier-lipid precursor synthesis\n  - Undecaprenyl\
    \ diphosphate synthesis\n    - UppS undecaprenyl diphosphate synthase (molecular\
    \ player: PSEPK uppS; activity or role: ditrans,polycis-undecaprenyl-diphosphate\
    \ synthase [(2E,6E)-farnesyl-diphosphate specific] activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00900
  pathway_id: ppu00900
  pathway_name: Terpenoid backbone biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00900 with 14 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '17'
  candidate_genes: '- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase
    (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC
    2.2.1.7; primary bucket kegg:ppu00730)

    - ispA: PP_0528 | Q88QG6 | Farnesyl diphosphate synthase (EC 2.5.1.1, EC 2.5.1.10)
    (EC 2.5.1.1; 2.5.1.10; primary bucket kegg:ppu00900)

    - ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129;
    primary bucket kegg:ppu00627)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - ispH: PP_0606 | Q88Q89 | 4-hydroxy-3-methylbut-2-enyl diphosphate reductase
    (HMBPP reductase) (EC 1.17.7.4) (EC 1.17.7.4; primary bucket kegg:ppu00900)

    - ispB: PP_0687 | Q88Q11 | Octaprenyl diphosphate synthase (EC 2.5.1.90) (All-trans-octaprenyl-diphosphate
    synthase) (Octaprenyl pyrophosphate synthase) (EC 2.5.1.90; primary bucket kegg:ppu00900)

    - ispE: PP_0723 | Q88PX5 | 4-diphosphocytidyl-2-C-methyl-D-erythritol kinase (CMK)
    (EC 2.7.1.148) (4-(cytidine-5''-diphospho)-2-C-methyl-D-erythritol kinase) (EC
    2.7.1.148; primary bucket kegg:ppu00900)

    - ispG: PP_0853 | Q88PJ7 | 4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase
    (flavodoxin) (EC 1.17.7.3) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase)
    (EC 1.17.7.3; primary bucket kegg:ppu00900)

    - uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate
    specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl
    diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase)
    (EC 2.5.1.31; primary bucket kegg:ppu00900)

    - dxr: PP_1597 | Q88MH4 | 1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXP
    reductoisomerase) (EC 1.1.1.267) (1-deoxyxylulose-5-phosphate reductoisomerase)
    (2-C-methyl-D-erythritol 4-phosphate synthase) (EC 1.1.1.267; primary bucket kegg:ppu00900)

    - ispD: PP_1614 | Q88MF7 | 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase
    (EC 2.7.7.60) (4-diphosphocytidyl-2C-methyl-D-erythritol synthase) (MEP cytidylyltransferase)
    (MCT) (EC 2.7.7.60; primary bucket kegg:ppu00900)

    - ispF: PP_1618 | Q88MF3 | 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase
    (MECDP-synthase) (MECPP-synthase) (MECPS) (EC 4.6.1.12) (EC 4.6.1.12; primary
    bucket kegg:ppu00900)

    - fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__terpenoid_backbone_biosynthesis__ppu00900-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__terpenoid_backbone_biosynthesis__ppu00900-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Terpenoid backbone biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00900
- Resolved ID: ppu00900
- Resolved name: Terpenoid backbone biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00900 with 14 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 17

- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary bucket kegg:ppu00730)
- ispA: PP_0528 | Q88QG6 | Farnesyl diphosphate synthase (EC 2.5.1.1, EC 2.5.1.10) (EC 2.5.1.1; 2.5.1.10; primary bucket kegg:ppu00900)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- ispH: PP_0606 | Q88Q89 | 4-hydroxy-3-methylbut-2-enyl diphosphate reductase (HMBPP reductase) (EC 1.17.7.4) (EC 1.17.7.4; primary bucket kegg:ppu00900)
- ispB: PP_0687 | Q88Q11 | Octaprenyl diphosphate synthase (EC 2.5.1.90) (All-trans-octaprenyl-diphosphate synthase) (Octaprenyl pyrophosphate synthase) (EC 2.5.1.90; primary bucket kegg:ppu00900)
- ispE: PP_0723 | Q88PX5 | 4-diphosphocytidyl-2-C-methyl-D-erythritol kinase (CMK) (EC 2.7.1.148) (4-(cytidine-5'-diphospho)-2-C-methyl-D-erythritol kinase) (EC 2.7.1.148; primary bucket kegg:ppu00900)
- ispG: PP_0853 | Q88PJ7 | 4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (flavodoxin) (EC 1.17.7.3) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase) (EC 1.17.7.3; primary bucket kegg:ppu00900)
- uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase) (EC 2.5.1.31; primary bucket kegg:ppu00900)
- dxr: PP_1597 | Q88MH4 | 1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXP reductoisomerase) (EC 1.1.1.267) (1-deoxyxylulose-5-phosphate reductoisomerase) (2-C-methyl-D-erythritol 4-phosphate synthase) (EC 1.1.1.267; primary bucket kegg:ppu00900)
- ispD: PP_1614 | Q88MF7 | 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase (EC 2.7.7.60) (4-diphosphocytidyl-2C-methyl-D-erythritol synthase) (MEP cytidylyltransferase) (MCT) (EC 2.7.7.60; primary bucket kegg:ppu00900)
- ispF: PP_1618 | Q88MF3 | 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (MECDP-synthase) (MECPP-synthase) (MECPS) (EC 4.6.1.12) (EC 4.6.1.12; primary bucket kegg:ppu00900)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)

## Generic Module Context

### Working Scope

A bacterial terpenoid-backbone biosynthesis module centered on the methylerythritol phosphate (MEP/DOXP) pathway from pyruvate and glyceraldehyde 3-phosphate to isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), followed by prenyl-diphosphate synthases that extend these C5 units into geranyl, farnesyl, octaprenyl, and undecaprenyl diphosphates. In Pseudomonas putida KT2440, KEGG ppu00900 also pulls in thiolase/mevalonate-route-like entries and UbiX flavin prenyltransferase chemistry; those are treated as boundary or downstream uses rather than evidence for a strict mevalonate pathway.

### Provisional Biological Outline

- Terpenoid backbone biosynthesis
  - 1. DXP formation
  - 1-deoxy-D-xylulose 5-phosphate formation
    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
  - 2. MEP formation
  - DXP reductoisomerization
    - Dxr 1-deoxy-D-xylulose-5-phosphate reductoisomerase (molecular player: PSEPK dxr; activity or role: 1-deoxy-D-xylulose-5-phosphate reductoisomerase activity)
  - 3. CDP-ME formation
  - MEP cytidylyltransferase step
    - IspD MEP cytidylyltransferase (molecular player: PSEPK ispD; activity or role: 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase activity)
  - 4. CDP-ME phosphorylation
  - CDP-ME kinase step
    - IspE CDP-ME kinase (molecular player: PSEPK ispE; activity or role: 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase activity)
  - 5. MEcPP formation
  - MEcPP synthase step
    - IspF MEcPP synthase (molecular player: PSEPK ispF; activity or role: 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase activity)
  - 6. HMBPP formation
  - HMBPP synthase step
    - IspG HMBPP synthase (molecular player: PSEPK ispG; activity or role: 4-hydroxy-3-methylbut-2-enyl-diphosphate synthase activity (flavodoxin))
  - 7. IPP and DMAPP formation
  - HMBPP reductase step
    - IspH HMBPP reductase (molecular player: PSEPK ispH; activity or role: 4-hydroxy-3-methylbut-2-enyl diphosphate reductase activity)
  - 8. short-chain prenyl diphosphate synthesis
  - Farnesyl diphosphate synthesis
    - IspA farnesyl diphosphate synthase (molecular player: PSEPK ispA; activity or role: (2E,6E)-farnesyl diphosphate synthase activity)
  - 9. ubiquinone-side-chain precursor synthesis
  - Octaprenyl diphosphate synthesis
    - IspB octaprenyl diphosphate synthase (molecular player: PSEPK ispB; activity or role: all-trans-octaprenyl-diphosphate synthase activity)
  - 10. undecaprenyl carrier-lipid precursor synthesis
  - Undecaprenyl diphosphate synthesis
    - UppS undecaprenyl diphosphate synthase (molecular player: PSEPK uppS; activity or role: ditrans,polycis-undecaprenyl-diphosphate synthase [(2E,6E)-farnesyl-diphosphate specific] activity)

### Known Relationships Among Steps

No explicit connections.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

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

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Terpenoid backbone biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00900
- Resolved ID: ppu00900
- Resolved name: Terpenoid backbone biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00900 with 14 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 17

- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary bucket kegg:ppu00730)
- ispA: PP_0528 | Q88QG6 | Farnesyl diphosphate synthase (EC 2.5.1.1, EC 2.5.1.10) (EC 2.5.1.1; 2.5.1.10; primary bucket kegg:ppu00900)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- ispH: PP_0606 | Q88Q89 | 4-hydroxy-3-methylbut-2-enyl diphosphate reductase (HMBPP reductase) (EC 1.17.7.4) (EC 1.17.7.4; primary bucket kegg:ppu00900)
- ispB: PP_0687 | Q88Q11 | Octaprenyl diphosphate synthase (EC 2.5.1.90) (All-trans-octaprenyl-diphosphate synthase) (Octaprenyl pyrophosphate synthase) (EC 2.5.1.90; primary bucket kegg:ppu00900)
- ispE: PP_0723 | Q88PX5 | 4-diphosphocytidyl-2-C-methyl-D-erythritol kinase (CMK) (EC 2.7.1.148) (4-(cytidine-5'-diphospho)-2-C-methyl-D-erythritol kinase) (EC 2.7.1.148; primary bucket kegg:ppu00900)
- ispG: PP_0853 | Q88PJ7 | 4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (flavodoxin) (EC 1.17.7.3) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase) (EC 1.17.7.3; primary bucket kegg:ppu00900)
- uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase) (EC 2.5.1.31; primary bucket kegg:ppu00900)
- dxr: PP_1597 | Q88MH4 | 1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXP reductoisomerase) (EC 1.1.1.267) (1-deoxyxylulose-5-phosphate reductoisomerase) (2-C-methyl-D-erythritol 4-phosphate synthase) (EC 1.1.1.267; primary bucket kegg:ppu00900)
- ispD: PP_1614 | Q88MF7 | 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase (EC 2.7.7.60) (4-diphosphocytidyl-2C-methyl-D-erythritol synthase) (MEP cytidylyltransferase) (MCT) (EC 2.7.7.60; primary bucket kegg:ppu00900)
- ispF: PP_1618 | Q88MF3 | 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (MECDP-synthase) (MECPP-synthase) (MECPS) (EC 4.6.1.12) (EC 4.6.1.12; primary bucket kegg:ppu00900)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)

## Generic Module Context

### Working Scope

A bacterial terpenoid-backbone biosynthesis module centered on the methylerythritol phosphate (MEP/DOXP) pathway from pyruvate and glyceraldehyde 3-phosphate to isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), followed by prenyl-diphosphate synthases that extend these C5 units into geranyl, farnesyl, octaprenyl, and undecaprenyl diphosphates. In Pseudomonas putida KT2440, KEGG ppu00900 also pulls in thiolase/mevalonate-route-like entries and UbiX flavin prenyltransferase chemistry; those are treated as boundary or downstream uses rather than evidence for a strict mevalonate pathway.

### Provisional Biological Outline

- Terpenoid backbone biosynthesis
  - 1. DXP formation
  - 1-deoxy-D-xylulose 5-phosphate formation
    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
  - 2. MEP formation
  - DXP reductoisomerization
    - Dxr 1-deoxy-D-xylulose-5-phosphate reductoisomerase (molecular player: PSEPK dxr; activity or role: 1-deoxy-D-xylulose-5-phosphate reductoisomerase activity)
  - 3. CDP-ME formation
  - MEP cytidylyltransferase step
    - IspD MEP cytidylyltransferase (molecular player: PSEPK ispD; activity or role: 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase activity)
  - 4. CDP-ME phosphorylation
  - CDP-ME kinase step
    - IspE CDP-ME kinase (molecular player: PSEPK ispE; activity or role: 4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase activity)
  - 5. MEcPP formation
  - MEcPP synthase step
    - IspF MEcPP synthase (molecular player: PSEPK ispF; activity or role: 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase activity)
  - 6. HMBPP formation
  - HMBPP synthase step
    - IspG HMBPP synthase (molecular player: PSEPK ispG; activity or role: 4-hydroxy-3-methylbut-2-enyl-diphosphate synthase activity (flavodoxin))
  - 7. IPP and DMAPP formation
  - HMBPP reductase step
    - IspH HMBPP reductase (molecular player: PSEPK ispH; activity or role: 4-hydroxy-3-methylbut-2-enyl diphosphate reductase activity)
  - 8. short-chain prenyl diphosphate synthesis
  - Farnesyl diphosphate synthesis
    - IspA farnesyl diphosphate synthase (molecular player: PSEPK ispA; activity or role: (2E,6E)-farnesyl diphosphate synthase activity)
  - 9. ubiquinone-side-chain precursor synthesis
  - Octaprenyl diphosphate synthesis
    - IspB octaprenyl diphosphate synthase (molecular player: PSEPK ispB; activity or role: all-trans-octaprenyl-diphosphate synthase activity)
  - 10. undecaprenyl carrier-lipid precursor synthesis
  - Undecaprenyl diphosphate synthesis
    - UppS undecaprenyl diphosphate synthase (molecular player: PSEPK uppS; activity or role: ditrans,polycis-undecaprenyl-diphosphate synthase [(2E,6E)-farnesyl-diphosphate specific] activity)

### Known Relationships Among Steps

No explicit connections.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

# Terpenoid Backbone Biosynthesis in *Pseudomonas putida* KT2440: A Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 (NCBI taxon 160488) exclusively employs the methylerythritol phosphate (MEP/DOXP) pathway for terpenoid backbone biosynthesis and does not possess a native mevalonate (MVA) pathway (wang2022engineeringisoprenoidsproduction pages 4-6, wang2022engineeringisoprenoidsproduction pages 3-4). The KEGG entry ppu00900 maps 14 primary genes to this pathway; however, the candidate gene list of 17 includes six thiolase/acetyl-CoA acetyltransferase genes that are artifacts of broad EC-number mapping to mevalonate-like steps and one flavin prenyltransferase (UbiX) that belongs to the ubiquinone biosynthesis boundary. The seven core MEP enzymes (DXS through IspH), three prenyl diphosphate synthases (IspA, IspB, UppS), and isopentenyl diphosphate isomerase (IDI) are all genomically present and supported by direct or strong indirect evidence from KT2440 engineering studies. The principal curation actions recommended are: (i) removal of six thiolase entries from the terpenoid backbone module, (ii) reclassification of UbiX as a ubiquinone-pathway boundary enzyme, and (iii) addition of IDI (idi, likely PP_0854) to the candidate list as a gap fill.

## 2. Target-Organism Pathway Definition

### 2.1 Biochemical Scope

Terpenoid backbone biosynthesis in KT2440 encompasses the seven-step MEP pathway converting pyruvate and glyceraldehyde 3-phosphate (GAP) to isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), followed by prenyl diphosphate chain elongation to farnesyl diphosphate (FPP, C15), octaprenyl diphosphate (C40, for ubiquinone), and undecaprenyl diphosphate (C55, for cell-wall lipid carrier) (hernandezarranz2019engineeringpseudomonasputida pages 1-2). The organism is an obligate aerobe that uses the Entner–Doudoroff pathway as its primary glycolytic route, making its pyruvate and GAP pools qualitatively different from *E. coli* (wang2022engineeringisoprenoidsproduction pages 6-9).

### 2.2 Pathway Boundaries

The following should be kept **separate** from this module:

- **Ubiquinone biosynthesis** (KEGG ppu00130): UbiX (PP_0548) and the downstream prenylation/modification steps belong here, not in terpenoid backbone (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7).
- **Fatty acid β-oxidation** (KEGG ppu00071, ppu00592): All thiolase candidates (PP_0582, PP_2215, PP_3355, PP_3754/bktB, PP_4636/yqeF, PP_2051/fadA) function in fatty acid catabolism (thompson2020fattyacidand pages 7-9, thompson2020fattyacidand pages 5-7).
- **PHA biosynthesis** (ppu00650 area): PHA synthase genes (phaABC) share acetyl-CoA as a precursor with the heterologous MVA pathway but are not terpenoid pathway genes (wang2022engineeringisoprenoidsproduction pages 6-9).
- **Thiamine biosynthesis** (ppu00730): DXS (PP_0527) also feeds DXP into thiamine and pyridoxal biosynthesis, constituting a shared node but a separate pathway.

### 2.3 Alternate Names and Database Definitions

The pathway is variably called the MEP pathway, DOXP pathway, non-mevalonate pathway, or Rohmer pathway. KEGG map00900 ("Terpenoid backbone biosynthesis") is a composite map encompassing both MVA and MEP routes plus prenyl elongation; only the MEP-specific portion is biologically relevant to KT2440.

## 3. Expected Step Model

The following table summarizes each module step and its recommended status in KT2440:

| Step Number | Step Name | Assigned Gene(s) | Recommended Status | Rationale |
|---|---|---|---|---|
| 1 | DXP formation | dxs (PP_0527) | covered | Native DXS is directly supported in *P. putida* KT2440 by overexpression studies showing strong lycopene increases; identified as a major/rate-limiting MEP control point (hernandezarranz2019engineeringpseudomonasputida pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| 2 | MEP formation | dxr (PP_1597) | covered | DXR is part of the native MEP route and co-overexpression with DXS increased lycopene up to ~50-fold, providing direct KT2440 support (hernandezarranz2019engineeringpseudomonasputida pages 9-10, hernandezarranz2019engineeringpseudomonasputida pages 10-11) |
| 3 | CDP-ME formation | ispD (PP_1614) | covered | No step-specific perturbation found, but KT2440 clearly uses a complete endogenous MEP pathway rather than a native MVA pathway; ispD is expected as part of that complete route (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| 4 | CDP-ME phosphorylation | ispE (PP_0723) | covered | Canonical central MEP-pathway step inferred from the experimentally supported presence of the full native MEP pathway in KT2440 (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| 5 | MEcPP formation | ispF (PP_1618) | covered | Canonical central MEP-pathway step inferred from the experimentally supported presence of the full native MEP pathway in KT2440 (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| 6 | HMBPP formation | ispG (PP_0853) | covered | Canonical late MEP-pathway step inferred from the experimentally supported presence of the full native MEP pathway in KT2440 (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| 7 | IPP and DMAPP formation | ispH (PP_0606) | covered | Canonical terminal MEP-pathway reductase step inferred from the experimentally supported presence of the full native MEP pathway in KT2440 (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| 8 | IPP/DMAPP interconversion | idi (PP_0854; missing from candidate list) | gap | Engineering work in KT2440 discusses endogenous *idi* among MEP-pathway genes, indicating the function is expected/present, but it was omitted from the 17-gene candidate set; this is a metadata gap rather than a biological absence (hernandezarranz2019engineeringpseudomonasputida pages 1-2, hernandezarranz2019engineeringpseudomonasputida pages 4-6) |
| 9 | FPP synthesis | ispA (PP_0528) | covered | Direct CRISPRi/proteomics evidence in KT2440 supports ispA as the native FPP synthase; perturbation affected native isoprenoid/ubiquinol metabolism (carruthers*2025automationandmachine pages 11-14) |
| 10 | Octaprenyl-PP synthesis | ispB (PP_0687) | covered | Appropriate downstream prenyl-chain elongation step for ubiquinone side-chain synthesis; function supported by conserved prenylquinone biosynthesis literature (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7) |
| 11 | Undecaprenyl-PP synthesis | uppS (PP_1595) | covered | Appropriate downstream terpenoid-output step producing the lipid carrier precursor for cell-envelope biosynthesis; not part of core MEP chemistry but valid pathway output (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7) |
| 12 | Acetyl-CoA condensation (mevalonate-like) | PP_0582, PP_2215, PP_3355, bktB/PP_3754, yqeF/PP_4636, fadA-like thiolases | not_expected_in_target_taxon | KT2440 does not have a native mevalonate pathway; thiolase candidates are better explained as fatty-acid/butyrate catabolic enzymes, with bktB directly supported for butyrate catabolism by RB-TnSeq (wang2022engineeringisoprenoidsproduction pages 3-4, wang2022engineeringisoprenoidsproduction pages 4-6, thompson2020fattyacidand pages 7-9) |
| 13 | UbiX prenylation | ubiX (PP_0548) | module_needs_revision | UbiX is a flavin prenyltransferase that supplies prenylated FMN for UbiD in ubiquinone biosynthesis; it is a boundary/downstream ubiquinone enzyme, not a terpenoid-backbone core step (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7) |


*Table: This table summarizes recommended coverage statuses for each terpenoid-backbone module step in *Pseudomonas putida* KT2440. It is useful for manual pathway satisfiability review because it separates well-supported core MEP steps from metadata gaps, non-native mevalonate-like assignments, and boundary enzymes.*

### Key Observations on the Step Model

**DXS is rate-limiting.** Overexpression of endogenous *dxs* in KT2440 led to a 15–25-fold increase in lycopene production using a chromosomally integrated reporter (hernandezarranz2019engineeringpseudomonasputida pages 4-6). Co-overexpression of *dxs* and *dxr* yielded a ~50-fold increase, the most successful single strategy tested (hernandezarranz2019engineeringpseudomonasputida pages 9-10, hernandezarranz2019engineeringpseudomonasputida pages 10-11). This is distinct from *E. coli*, where heterologous MVA pathway expression typically outperforms DXS upregulation (hernandezarranz2019engineeringpseudomonasputida pages 10-11).

**IDI is missing from the candidate list.** Hernandez-Arranz et al. (2019) cloned and overexpressed the endogenous *idi* gene from KT2440, confirming its presence in the genome (hernandezarranz2019engineeringpseudomonasputida pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2). KEGG annotates *idi* as PP_0854, adjacent to *ispG* (PP_0853). Its omission from the 17-gene candidate set represents a metadata gap.

**IspA perturbation has been directly tested.** CRISPRi-mediated downregulation of *ispA* (PP_0528) disrupted ubiquinol biosynthesis—an essential component of the electron transport chain—and significantly increased cioA levels while downregulating native isoprenoid biosynthesis (carruthers*2025automationandmachine pages 11-14). This provides direct functional confirmation in KT2440.

## 4. Candidate Genes and Evidence

The comprehensive assessment of all 17 candidate genes is provided below:

| Gene Name | Locus Tag | UniProt ID | Proposed Function | Evidence Type | Confidence Level | Curation Assessment | Notes |
|---|---|---|---|---|---|---|---|
| dxs | PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase; first committed MEP-step enzyme | Direct engineering/overexpression in *P. putida* KT2440 | High | covered | Native MEP-pathway gene; DXS overexpression increased lycopene ~15–25-fold and was identified as a major/rate-limiting control point; should be retained as core pathway support (hernandezarranz2019engineeringpseudomonasputida pages 1-2, hernandezarranz2019engineeringpseudomonasputida pages 4-6) |
| ispA | PP_0528 | Q88QG6 | Farnesyl diphosphate synthase (FPP synthase) | Direct CRISPRi/proteomics phenotype in *P. putida* KT2440 | High | covered | Downregulation of ispA altered native isoprenoid/ubiquinol biosynthesis in CRISPRi screens, supporting assignment as the native FPP synthase; relevant downstream prenyl-PP step (carruthers*2025automationandmachine pages 11-14) |
| ubiX | PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX; generates prenylated FMN cofactor for UbiD | Functional inference from conserved ubiquinone pathway literature | Medium | not_expected_in_target_taxon | Best treated as boundary/downstream ubiquinone-biosynthesis enzyme, not terpenoid-backbone core chemistry; annotation in ppu00900 is likely pathway bleed-through (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7) |
| PP_0582 | PP_0582 | Q88QB2 | Thiolase family protein; likely acyl-CoA/ketothiolase-related metabolism | Family-level annotation only; no direct terpene evidence | Low | candidate_uncertain | No evidence for native mevalonate-pathway role in KT2440; likely over-propagated into ppu00900 and more plausibly linked to fatty-acid-related metabolism than terpenoid backbone synthesis (wang2022engineeringisoprenoidsproduction pages 3-4, wang2022engineeringisoprenoidsproduction pages 4-6) |
| ispH | PP_0606 | Q88Q89 | HMBPP reductase; final MEP step to IPP/DMAPP | Strong pathway inference from native MEP pathway established in *P. putida* | High | covered | Core MEP-pathway enzyme expected in KT2440 because the organism natively uses the MEP rather than MVA route; no specific gene-level perturbation found, but assignment is standard and coherent (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| ispB | PP_0687 | Q88Q11 | Octaprenyl diphosphate synthase; ubiquinone side-chain precursor synthesis | Conserved-function inference from prenylquinone literature | High | covered | Appropriate downstream extension enzyme for CoQ/ubiquinone tail synthesis; part of terpenoid-backbone output space but functionally adjacent to ubiquinone biosynthesis (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7) |
| ispE | PP_0723 | Q88PX5 | CDP-ME kinase (MEP pathway) | Strong pathway inference from native MEP pathway established in *P. putida* | High | covered | Canonical central MEP-step enzyme; expected as part of complete endogenous MEP route in KT2440 (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| ispG | PP_0853 | Q88PJ7 | HMBPP synthase (MEP pathway) | Strong pathway inference from native MEP pathway established in *P. putida* | High | covered | Canonical late MEP-pathway enzyme; assignment consistent with complete native MEP route and terpene-engineering literature in KT2440 (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| uppS | PP_1595 | Q88MH6 | Undecaprenyl diphosphate synthase; bactoprenol/lipid-carrier precursor | Conserved-function inference | High | covered | Valid terpenoid-backbone output enzyme but biologically belongs at cell-envelope/lipid-carrier boundary rather than central MEP chemistry; should be kept separate from mevalonate-like annotations (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7) |
| dxr | PP_1597 | Q88MH4 | DXP reductoisomerase; second MEP-step enzyme | Direct engineering/overexpression in *P. putida* KT2440 | High | covered | Co-overexpression with DXS boosted lycopene about 50-fold, strongly supporting native pathway role and importance for precursor flux (hernandezarranz2019engineeringpseudomonasputida pages 1-2, hernandezarranz2019engineeringpseudomonasputida pages 9-10, hernandezarranz2019engineeringpseudomonasputida pages 10-11) |
| ispD | PP_1614 | Q88MF7 | MEP cytidylyltransferase | Strong pathway inference from native MEP pathway established in *P. putida* | High | covered | Canonical central MEP enzyme; expected in KT2440 given experimentally supported native MEP use (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| ispF | PP_1618 | Q88MF3 | MEcPP synthase | Strong pathway inference from native MEP pathway established in *P. putida* | High | covered | Canonical central MEP enzyme; assignment is pathway-complete and consistent with KT2440 terpene engineering results (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| fadA | PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase; fatty-acid β-oxidation | Functional genomics/RB-TnSeq in *P. putida* fatty-acid catabolism | High | not_expected_in_target_taxon | Candidate list likely reflects over-annotation; KT2440 thiolases are tied to fatty-acid catabolism, and no native MVA pathway is present (wang2022engineeringisoprenoidsproduction pages 3-4, thompson2020fattyacidand pages 5-7) |
| PP_2215 | PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase/thiolase; short-chain fatty-acid catabolism-associated | RB-TnSeq and prior expression data discussed in *P. putida* | Medium | not_expected_in_target_taxon | One of several thiolases induced during butanol/butyrate metabolism, but only bktB showed strong fitness phenotype; no support for mevalonate-pathway interpretation (thompson2020fattyacidand pages 7-9) |
| PP_3355 | PP_3355 | Q88HK1 | Beta-ketothiolase-like protein; likely fatty-acid-related metabolism | Family-level annotation only; no direct terpene evidence | Low | candidate_uncertain | No direct evidence connecting this paralog to terpenoid backbone synthesis; likely another over-propagated thiolase annotation requiring separation from MVA-like steps (wang2022engineeringisoprenoidsproduction pages 3-4, wang2022engineeringisoprenoidsproduction pages 4-6) |
| bktB | PP_3754 | Q88GH0 | Beta-ketothiolase; major thiolase for butyrate catabolism | Direct RB-TnSeq functional evidence in *P. putida* KT2440 | High | not_expected_in_target_taxon | Strong fitness defect during butyrate utilization identifies BktB as the main terminal thiolase in butyrate catabolism, arguing against use as evidence for a native mevalonate route (thompson2020fattyacidand pages 7-9) |
| yqeF | PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase/thiolase; likely short-chain fatty-acid catabolism-associated | RB-TnSeq context from *P. putida* short-chain metabolism | Medium | not_expected_in_target_taxon | Mentioned among thiolases upregulated during butanol metabolism, but lacked the strong phenotype seen for bktB; no evidence for terpenoid-backbone role (thompson2020fattyacidand pages 7-9) |


*Table: This table summarizes all 17 candidate genes from KEGG ppu00900 for *Pseudomonas putida* KT2440, separating high-confidence core MEP/prenyl-synthase genes from likely boundary enzymes and over-annotated thiolases. It is useful for manual satisfiability review and annotation curation because it distinguishes pathway coverage from false-positive mevalonate-like assignments.*

### 4.1 High-Confidence Core MEP Genes (Direct KT2440 Evidence)

**dxs (PP_0527):** 1-Deoxy-D-xylulose-5-phosphate synthase. Confirmed rate-limiting by Hernandez-Arranz et al. (2019), who achieved a 15–25-fold lycopene increase via IPTG-controlled overexpression (hernandezarranz2019engineeringpseudomonasputida pages 4-6). Excessive overexpression caused growth defects due to pyruvate/GAP depletion, indicating metabolic competition with central carbon metabolism (hernandezarranz2019engineeringpseudomonasputida pages 4-6). Note that *dxs* also feeds DXP into thiamine and pyridoxal biosynthesis (primary bucket kegg:ppu00730), so its annotation overlaps multiple pathways.

**dxr (PP_1597):** DXP reductoisomerase. Co-overexpression with DXS achieved the highest lycopene boost (~50-fold) among all single strategies tested in KT2440 (hernandezarranz2019engineeringpseudomonasputida pages 9-10, hernandezarranz2019engineeringpseudomonasputida pages 10-11).

**ispA (PP_0528):** Farnesyl diphosphate synthase. CRISPRi knockdown in KT2440 isoprenol production campaigns confirmed its role: downregulation disrupted ubiquinol biosynthesis and modulated electron transport chain composition (carruthers*2025automationandmachine pages 11-14). Located immediately downstream of *dxs* in the genome.

### 4.2 High-Confidence Core MEP Genes (Genomic/Pathway Inference)

**ispD (PP_1614), ispE (PP_0723), ispF (PP_1618), ispG (PP_0853), ispH (PP_0606):** These five genes encode the remaining canonical MEP pathway enzymes (steps 3–7). While none has been individually perturbed and characterized in KT2440, their presence and function are strongly inferred from the fact that the complete MEP pathway is the sole endogenous route for IPP/DMAPP synthesis (wang2022engineeringisoprenoidsproduction pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2), and multiple engineering studies have successfully used this native pathway as a starting point for terpenoid production.

### 4.3 Downstream Prenyl Diphosphate Synthases

**ispB (PP_0687):** Octaprenyl diphosphate synthase. Provides the prenyl side chain for ubiquinone (CoQ-8 in *E. coli*; *P. putida* likely produces a CoQ with equivalent chain length). The gene is essential in *E. coli*, and a similar essentiality is expected in the obligate aerobe KT2440 (kawamukai2018biosynthesisandapplications pages 5-7).

**uppS (PP_1595):** Undecaprenyl diphosphate synthase. Produces the C55 lipid carrier precursor required for peptidoglycan biosynthesis. This is a universal bacterial essential gene and is appropriately included in the terpenoid backbone pathway as a downstream output.

### 4.4 Boundary Enzyme

**ubiX (PP_0548):** Flavin prenyltransferase. UbiX generates the prenylated FMN cofactor required by UbiD to catalyze the decarboxylation step in ubiquinone biosynthesis (pierrel2022recentadvancesin pages 3-4, kawamukai2018biosynthesisandapplications pages 5-7). While it uses a prenyl diphosphate substrate (DMAP), its biological function is squarely within ubiquinone biosynthesis. Its presence in ppu00900 appears to be pathway "bleed-through" from the KEGG composite map. Its primary bucket (kegg:ppu00627) is more appropriate.

### 4.5 Over-Annotated Thiolases (No Terpenoid Backbone Role)

Six candidate genes encode thiolase-family proteins that were mapped to terpenoid backbone biosynthesis presumably because of their EC numbers (EC 2.3.1.9, EC 2.3.1.16), which overlap with acetoacetyl-CoA thiolase—the first step of the mevalonate pathway. However, KT2440 does not possess a native MVA pathway (wang2022engineeringisoprenoidsproduction pages 4-6, wang2022engineeringisoprenoidsproduction pages 3-4). All heterologous MVA pathway genes (AtoB, HMGS, HMGR, MK, PMK, PMD) had to be introduced for isoprenol production, confirming the absence of endogenous MVA enzymes (wang2022engineeringisoprenoidsproduction pages 3-4, wang2022engineeringisoprenoidsproduction pages 6-9).

**bktB (PP_3754):** The best-characterized thiolase. RB-TnSeq analysis in KT2440 demonstrated a strong fitness defect during growth on butyrate, establishing it as the main thiolase for butyrate catabolism (thompson2020fattyacidand pages 7-9). Its genomic context (flanked by regulatory elements PP_3753 and PP_3756) supports its role in short-chain fatty acid metabolism.

**PP_2215 and yqeF (PP_4636):** Both were upregulated during butanol/butyrate growth but showed no strong fitness phenotype in RB-TnSeq, suggesting redundancy with bktB (thompson2020fattyacidand pages 7-9).

**fadA (PP_2051):** Part of the β-oxidation operon PP_2047–PP_2051; PP_2137 (a nearby fadA homolog) serves as the primary long-chain thiolase for C8+ fatty acids (thompson2020fattyacidand pages 5-7).

**PP_0582 and PP_3355:** Family-level annotations only. No functional data connect these to terpenoid metabolism. They likely represent additional fatty acid catabolic paralogs.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Metadata Gap: IDI

Isopentenyl diphosphate isomerase (*idi*, likely PP_0854) is present in the KT2440 genome and has been used in engineering studies (hernandezarranz2019engineeringpseudomonasputida pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 1-2), but it was not included in the 17-gene candidate list. Co-overexpression of IDI with DXS did not significantly improve lycopene accumulation beyond DXS alone, suggesting that IPP/DMAPP imbalance is not a major bottleneck under the conditions tested (hernandezarranz2019engineeringpseudomonasputida pages 4-6). Nevertheless, IDI is a standard component of the terpenoid backbone biosynthesis pathway and should be added to the module.

### 5.2 Over-Annotated Thiolases

The six thiolase genes (PP_0582, PP_2215, PP_3355, bktB/PP_3754, yqeF/PP_4636, fadA/PP_2051) represent the most significant annotation problem. Their inclusion in ppu00900 stems from the KEGG composite map architecture, which overlays both MVA and MEP pathways onto a single map. Because KT2440 lacks a native MVA pathway, the acetoacetyl-CoA thiolase step is biologically absent, and these genes should be removed from the terpenoid backbone module for this organism.

### 5.3 Boundary Enzyme: UbiX

UbiX (PP_0548) should be reassigned to the ubiquinone biosynthesis pathway module. Its inclusion here inflates the apparent gene count of the terpenoid backbone module and may confuse satisfiability assessments.

### 5.4 Species-Specific Considerations

Engineering results from *E. coli* cannot be directly extrapolated to KT2440 due to fundamental differences in central carbon metabolism. For example, *P. putida* routes threefold more carbon flux from acetyl-CoA to the TCA cycle compared with *E. coli*, limiting acetyl-CoA availability for heterologous MVA pathway operation (wang2022engineeringisoprenoidsproduction pages 6-9). Additionally, the native PHA synthesis cycle acts as a carbon sink from acetyl-CoA; deletion of *phaABC* improved isoprenol production by ~24% (wang2022engineeringisoprenoidsproduction pages 6-9). The Entner–Doudoroff glycolytic mode also affects pyruvate and GAP availability differently than the Embden–Meyerhof–Parnas pathway used by *E. coli*.

## 6. Module and GO-Curation Recommendations

### 6.1 Step-Level Coverage Recommendations

- **Steps 1–7 (DXP through IPP/DMAPP via MEP):** Mark as **covered**. Direct experimental support from KT2440 for DXS and DXR; strong genomic inference for IspD, IspE, IspF, IspG, IspH.
- **Step 8 (IPP/DMAPP interconversion):** Mark as **gap** (metadata gap, not biological gap). Add *idi* (PP_0854) to the candidate gene list.
- **Steps 9–11 (FPP, octaprenyl-PP, undecaprenyl-PP synthesis):** Mark as **covered**. IspA has direct CRISPRi evidence; IspB and UppS are inferred from conserved function.
- **Step 12 (Acetyl-CoA condensation / mevalonate-like):** Mark as **not_expected_in_target_taxon**. Remove all six thiolase candidates from the terpenoid backbone module.
- **Step 13 (UbiX prenylation):** Mark as **module_needs_revision**. Reassign to ubiquinone biosynthesis.

### 6.2 Module Boundary Revisions

The generic module boundaries defined by KEGG map00900 are inappropriate for KT2440 because they include mevalonate pathway steps that are not present in this organism. A taxon-aware module for gammaproteobacteria lacking the MVA pathway should restrict the terpenoid backbone to MEP steps + prenyl diphosphate synthases only.

### 6.3 GO Term Considerations

No new GO terms appear necessary. The existing GO annotations for MEP pathway activities (GO:0016114 terpenoid biosynthetic process; GO:0019288 isopentenyl diphosphate biosynthetic process, methylerythritol 4-phosphate pathway) are appropriate for KT2440. However, GO annotations linking thiolase genes to terpenoid biosynthesis in KT2440 should be reviewed and corrected if present.

## 7. Genes to Promote to Full Review

The following genes merit priority full-review consideration:

1. **dxs (PP_0527):** Rate-limiting enzyme with direct engineering evidence and dual-pathway involvement (MEP + thiamine). Understanding its regulation and metabolic control is critical for accurate module annotation.

2. **ispA (PP_0528):** Direct CRISPRi phenotype data available; its perturbation has pleiotropic effects on electron transport chain composition (carruthers*2025automationandmachine pages 11-14). Understanding whether it supplies FPP for multiple downstream pathways (ubiquinone, menaquinone, undecaprenyl) is relevant.

3. **bktB (PP_3754):** Should be formally reassigned to fatty acid catabolism modules with documentation of the RB-TnSeq functional evidence (thompson2020fattyacidand pages 7-9).

4. **idi (PP_0854, not currently in candidate list):** Should be added and reviewed for inclusion in the module.

## 8. Key References

1. **Hernandez-Arranz S, Perez-Gil J, Marshall-Sabey D, Rodriguez-Concepcion M.** Engineering *Pseudomonas putida* for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. *Microbial Cell Factories* 18:152, 2019. DOI: 10.1186/s12934-019-1204-z (hernandezarranz2019engineeringpseudomonasputida pages 1-2, hernandezarranz2019engineeringpseudomonasputida pages 4-6, hernandezarranz2019engineeringpseudomonasputida pages 6-8, hernandezarranz2019engineeringpseudomonasputida pages 10-11, hernandezarranz2019engineeringpseudomonasputida pages 9-10, hernandezarranz2019engineeringpseudomonasputida pages 2-4, hernandezarranz2019engineeringpseudomonasputida pages 8-9)

2. **Wang X, Baidoo EEK, Kakumanu R, Xie S, Mukhopadhyay A, Lee TS.** Engineering isoprenoids production in metabolically versatile microbial host *Pseudomonas putida*. *Biotechnology for Biofuels and Bioproducts* 15:137, 2022. DOI: 10.1186/s13068-022-02235-6 (wang2022engineeringisoprenoidsproduction pages 4-6, wang2022engineeringisoprenoidsproduction pages 3-4, wang2022engineeringisoprenoidsproduction pages 1-3, wang2022engineeringisoprenoidsproduction pages 6-9)

3. **Carruthers DN*, Kinnunen PC*, et al.** Automation and machine learning drive rapid optimization of isoprenol production in *Pseudomonas putida*. *Nature Communications*, 2025. DOI: 10.1038/s41467-025-66304-8 (carruthers*2025automationandmachine pages 5-8, carruthers*2025automationandmachine pages 1-5, carruthers*2025automationandmachine pages 8-11, carruthers*2025automationandmachine pages 11-14)

4. **Thompson MG, Incha MR, Pearson AN, et al.** Fatty acid and alcohol metabolism in *Pseudomonas putida*: functional analysis using random barcode transposon sequencing. *Applied and Environmental Microbiology* 86:e01665-20, 2020. DOI: 10.1128/aem.01665-20 (thompson2020fattyacidand pages 7-9, thompson2020fattyacidand pages 5-7, thompson2020fattyacidand pages 9-12)

5. **Pierrel F, Burgardt A, Lee JH, Pelosi L, Wendisch VF.** Recent advances in the metabolic pathways and microbial production of coenzyme Q. *World Journal of Microbiology & Biotechnology* 38:64, 2022. DOI: 10.1007/s11274-022-03242-3 (pierrel2022recentadvancesin pages 3-4)

6. **Kawamukai M.** Biosynthesis and applications of prenylquinones. *Bioscience, Biotechnology, and Biochemistry* 82:963–977, 2018. DOI: 10.1080/09168451.2018.1433020 (kawamukai2018biosynthesisandapplications pages 5-7)

7. **Carruthers DN, Lee TS.** Diversifying isoprenoid platforms via atypical carbon substrates and non-model microorganisms. *Frontiers in Microbiology* 12:791089, 2021. DOI: 10.3389/fmicb.2021.791089 (carruthers2021diversifyingisoprenoidplatforms pages 5-6, carruthers2021diversifyingisoprenoidplatforms pages 3-5)


References

1. (wang2022engineeringisoprenoidsproduction pages 4-6): Xi Wang, Edward E. K. Baidoo, Ramu Kakumanu, Silvia Xie, Aindrila Mukhopadhyay, and Taek Soon Lee. Engineering isoprenoids production in metabolically versatile microbial host pseudomonas putida. Biotechnology for Biofuels and Bioproducts, Dec 2022. URL: https://doi.org/10.1186/s13068-022-02235-6, doi:10.1186/s13068-022-02235-6. This article has 30 citations and is from a domain leading peer-reviewed journal.

2. (wang2022engineeringisoprenoidsproduction pages 3-4): Xi Wang, Edward E. K. Baidoo, Ramu Kakumanu, Silvia Xie, Aindrila Mukhopadhyay, and Taek Soon Lee. Engineering isoprenoids production in metabolically versatile microbial host pseudomonas putida. Biotechnology for Biofuels and Bioproducts, Dec 2022. URL: https://doi.org/10.1186/s13068-022-02235-6, doi:10.1186/s13068-022-02235-6. This article has 30 citations and is from a domain leading peer-reviewed journal.

3. (hernandezarranz2019engineeringpseudomonasputida pages 1-2): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

4. (wang2022engineeringisoprenoidsproduction pages 6-9): Xi Wang, Edward E. K. Baidoo, Ramu Kakumanu, Silvia Xie, Aindrila Mukhopadhyay, and Taek Soon Lee. Engineering isoprenoids production in metabolically versatile microbial host pseudomonas putida. Biotechnology for Biofuels and Bioproducts, Dec 2022. URL: https://doi.org/10.1186/s13068-022-02235-6, doi:10.1186/s13068-022-02235-6. This article has 30 citations and is from a domain leading peer-reviewed journal.

5. (pierrel2022recentadvancesin pages 3-4): Fabien Pierrel, Arthur Burgardt, Jin-Ho Lee, Ludovic Pelosi, and Volker F. Wendisch. Recent advances in the metabolic pathways and microbial production of coenzyme q. World Journal of Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1007/s11274-022-03242-3, doi:10.1007/s11274-022-03242-3. This article has 31 citations and is from a peer-reviewed journal.

6. (kawamukai2018biosynthesisandapplications pages 5-7): Makoto Kawamukai. Biosynthesis and applications of prenylquinones. Bioscience, Biotechnology, and Biochemistry, 82:963-977, Jun 2018. URL: https://doi.org/10.1080/09168451.2018.1433020, doi:10.1080/09168451.2018.1433020. This article has 82 citations.

7. (thompson2020fattyacidand pages 7-9): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

8. (thompson2020fattyacidand pages 5-7): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

9. (hernandezarranz2019engineeringpseudomonasputida pages 4-6): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

10. (hernandezarranz2019engineeringpseudomonasputida pages 9-10): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

11. (hernandezarranz2019engineeringpseudomonasputida pages 10-11): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

12. (carruthers*2025automationandmachine pages 11-14): David N. Carruthers*, Patrick C. Kinnunen*, Yuerong Li, Yan Chen, Jennifer W. Gin, Ian S. Yunus, William R. Galliard, Stephen Tan, Paul D. Adams, Anup K. Singh, Jess Sustarich, Christopher J. Petzold, Aindrila Mukhopadhyay, Hector Garcia Martin, and Taek Soon Lee. Automation and machine learning drive rapid optimization of isoprenol production in pseudomonas putida. Unknown journal, Jun 2025. URL: https://doi.org/10.21203/rs.3.rs-6846062/v1, doi:10.21203/rs.3.rs-6846062/v1.

13. (hernandezarranz2019engineeringpseudomonasputida pages 6-8): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

14. (hernandezarranz2019engineeringpseudomonasputida pages 2-4): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

15. (hernandezarranz2019engineeringpseudomonasputida pages 8-9): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

16. (wang2022engineeringisoprenoidsproduction pages 1-3): Xi Wang, Edward E. K. Baidoo, Ramu Kakumanu, Silvia Xie, Aindrila Mukhopadhyay, and Taek Soon Lee. Engineering isoprenoids production in metabolically versatile microbial host pseudomonas putida. Biotechnology for Biofuels and Bioproducts, Dec 2022. URL: https://doi.org/10.1186/s13068-022-02235-6, doi:10.1186/s13068-022-02235-6. This article has 30 citations and is from a domain leading peer-reviewed journal.

17. (carruthers*2025automationandmachine pages 5-8): David N. Carruthers*, Patrick C. Kinnunen*, Yuerong Li, Yan Chen, Jennifer W. Gin, Ian S. Yunus, William R. Galliard, Stephen Tan, Paul D. Adams, Anup K. Singh, Jess Sustarich, Christopher J. Petzold, Aindrila Mukhopadhyay, Hector Garcia Martin, and Taek Soon Lee. Automation and machine learning drive rapid optimization of isoprenol production in pseudomonas putida. Unknown journal, Jun 2025. URL: https://doi.org/10.21203/rs.3.rs-6846062/v1, doi:10.21203/rs.3.rs-6846062/v1.

18. (carruthers*2025automationandmachine pages 1-5): David N. Carruthers*, Patrick C. Kinnunen*, Yuerong Li, Yan Chen, Jennifer W. Gin, Ian S. Yunus, William R. Galliard, Stephen Tan, Paul D. Adams, Anup K. Singh, Jess Sustarich, Christopher J. Petzold, Aindrila Mukhopadhyay, Hector Garcia Martin, and Taek Soon Lee. Automation and machine learning drive rapid optimization of isoprenol production in pseudomonas putida. Unknown journal, Jun 2025. URL: https://doi.org/10.21203/rs.3.rs-6846062/v1, doi:10.21203/rs.3.rs-6846062/v1.

19. (carruthers*2025automationandmachine pages 8-11): David N. Carruthers*, Patrick C. Kinnunen*, Yuerong Li, Yan Chen, Jennifer W. Gin, Ian S. Yunus, William R. Galliard, Stephen Tan, Paul D. Adams, Anup K. Singh, Jess Sustarich, Christopher J. Petzold, Aindrila Mukhopadhyay, Hector Garcia Martin, and Taek Soon Lee. Automation and machine learning drive rapid optimization of isoprenol production in pseudomonas putida. Unknown journal, Jun 2025. URL: https://doi.org/10.21203/rs.3.rs-6846062/v1, doi:10.21203/rs.3.rs-6846062/v1.

20. (thompson2020fattyacidand pages 9-12): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

21. (carruthers2021diversifyingisoprenoidplatforms pages 5-6): David N. Carruthers and Taek Soon Lee. Diversifying isoprenoid platforms via atypical carbon substrates and non-model microorganisms. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.791089, doi:10.3389/fmicb.2021.791089. This article has 19 citations and is from a peer-reviewed journal.

22. (carruthers2021diversifyingisoprenoidplatforms pages 3-5): David N. Carruthers and Taek Soon Lee. Diversifying isoprenoid platforms via atypical carbon substrates and non-model microorganisms. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.791089, doi:10.3389/fmicb.2021.791089. This article has 19 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__terpenoid_backbone_biosynthesis__ppu00900-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__terpenoid_backbone_biosynthesis__ppu00900-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. hernandezarranz2019engineeringpseudomonasputida pages 1-2
2. wang2022engineeringisoprenoidsproduction pages 6-9
3. hernandezarranz2019engineeringpseudomonasputida pages 4-6
4. hernandezarranz2019engineeringpseudomonasputida pages 10-11
5. thompson2020fattyacidand pages 7-9
6. kawamukai2018biosynthesisandapplications pages 5-7
7. thompson2020fattyacidand pages 5-7
8. pierrel2022recentadvancesin pages 3-4
9. wang2022engineeringisoprenoidsproduction pages 4-6
10. wang2022engineeringisoprenoidsproduction pages 3-4
11. hernandezarranz2019engineeringpseudomonasputida pages 9-10
12. hernandezarranz2019engineeringpseudomonasputida pages 6-8
13. hernandezarranz2019engineeringpseudomonasputida pages 2-4
14. hernandezarranz2019engineeringpseudomonasputida pages 8-9
15. wang2022engineeringisoprenoidsproduction pages 1-3
16. thompson2020fattyacidand pages 9-12
17. carruthers2021diversifyingisoprenoidplatforms pages 5-6
18. carruthers2021diversifyingisoprenoidplatforms pages 3-5
19. (2E,6E)-farnesyl-diphosphate specific
20. https://doi.org/10.1186/s13068-022-02235-6,
21. https://doi.org/10.1186/s12934-019-1204-z,
22. https://doi.org/10.1007/s11274-022-03242-3,
23. https://doi.org/10.1080/09168451.2018.1433020,
24. https://doi.org/10.1128/aem.01665-20,
25. https://doi.org/10.21203/rs.3.rs-6846062/v1,
26. https://doi.org/10.3389/fmicb.2021.791089,