---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T02:05:17.175481'
end_time: '2026-07-07T02:26:32.333713'
duration_seconds: 1275.16
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Thiamine biosynthesis
  module_summary: A bacterial thiamine diphosphate biosynthesis module covering formation
    of the hydroxymethylpyrimidine and thiazole moieties, condensation to thiamine
    monophosphate, and phosphorylation to the active thiamine diphosphate cofactor.
    In Pseudomonas putida KT2440, KEGG ppu00730 also includes shared precursor, sulfur-transfer,
    thiamine-salvage, nucleotide, and ribosome-side entries; those are treated as
    support or boundary context rather than all being strict thiamine-biosynthetic
    enzymes.
  module_outline: "- Thiamine biosynthesis\n  - 1. DXP precursor supply\n  - 1-deoxy-D-xylulose\
    \ 5-phosphate supply\n    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular\
    \ player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase\
    \ activity)\n  - 2. HMP-P formation\n  - Hydroxymethylpyrimidine phosphate formation\n\
    \    - ThiC phosphomethylpyrimidine synthase (molecular player: PSEPK thiC; activity\
    \ or role: phosphomethylpyrimidine synthase activity)\n  - 3. HMP phosphorylation\n\
    \  - Hydroxymethylpyrimidine phosphorylation\n    - ThiD hydroxymethylpyrimidine\
    \ kinase (molecular player: PSEPK thiD; activity or role: hydroxymethylpyrimidine\
    \ kinase activity)\n    - ThiD phosphomethylpyrimidine kinase (molecular player:\
    \ PSEPK thiD; activity or role: phosphomethylpyrimidine kinase activity)\n  -\
    \ 4. glyoxyl imine supply\n  - Glycine oxidation for thiazole synthesis\n    -\
    \ ThiO glycine oxidase (molecular player: PSEPK thiO; activity or role: glycine\
    \ oxidase activity)\n  - 5. sulfur transfer to the thiazole branch\n  - ThiS sulfur-carrier\
    \ charging\n    - ThiI sulfurtransferase (molecular player: PSEPK thiI; activity\
    \ or role: tRNA-uracil-4 sulfurtransferase activity)\n  - 6. thiazole phosphate\
    \ formation\n  - Thiazole phosphate formation\n    - ThiG thiazole synthase (molecular\
    \ player: PSEPK thiG; activity or role: thiazole synthase activity)\n  - 7. thiamine\
    \ monophosphate formation\n  - Thiamine monophosphate formation\n    - ThiE thiamine-phosphate\
    \ synthase (molecular player: PSEPK thiE; activity or role: thiamine-phosphate\
    \ diphosphorylase activity)\n  - 8. thiamine diphosphate formation\n  - Thiamine\
    \ diphosphate formation\n    - ThiL thiamine-phosphate kinase (molecular player:\
    \ PSEPK thiL; activity or role: thiamine-phosphate kinase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00730
  pathway_id: ppu00730
  pathway_name: Thiamine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00730 with 13 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '13'
  candidate_genes: '- thiL: PP_0519 | Q88QH4 | Thiamine-monophosphate kinase (TMP
    kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) (EC 2.7.4.16; primary bucket
    kegg:ppu00730)

    - dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7)
    (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary
    bucket kegg:ppu00730)

    - thiO: PP_0612 | Q88Q83 | Glycine oxidase (GO) (EC 1.4.3.19) (EC 1.4.3.19; primary
    bucket kegg:ppu00730)

    - iscS: PP_0842 | Q88PK8 | Cysteine desulfurase IscS (EC 2.8.1.7) (EC 2.8.1.7;
    primary bucket kegg:ppu00730)

    - adk: PP_1506 | P0A136 | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase)
    (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase) (EC 2.7.4.3; primary
    bucket kegg:ppu00730)

    - iscS-II: PP_2435 | Q88K56 | cysteine desulfurase (EC 2.8.1.7) (EC 2.8.1.7; primary
    bucket kegg:ppu00730)

    - PP_3186: PP_3186 | Q88I16 | Aminopyrimidine aminohydrolase (EC 3.5.99.2) (EC
    3.5.99.2; primary bucket kegg:ppu00730)

    - thiD: PP_4782 | Q88DP2 | hydroxymethylpyrimidine kinase (EC 2.7.1.49) (EC 2.7.1.49;
    primary bucket kegg:ppu00730)

    - thiE: PP_4783 | Q88DP1 | Thiamine-phosphate synthase (TP synthase) (TPS) (EC
    2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphorylase) (TMP-PPase)
    (EC 2.5.1.3; primary bucket kegg:ppu00730)

    - rsgA: PP_4903 | Q88DC4 | Small ribosomal subunit biogenesis GTPase RsgA (EC
    3.6.1.-) (EC 3.6.1.-; primary bucket kegg:ppu00730)

    - thiC: PP_4922 | Q88DA5 | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine
    phosphate synthase) (HMP-P synthase) (HMP-phosphate synthase) (HMPP synthase)
    (Thiamine biosynthesis protein ThiC) (EC 4.1.99.17; primary bucket kegg:ppu00730)

    - thiI: PP_5045 | Q88CY4 | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier
    protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine
    synthase) (EC 2.8.1.4; primary bucket kegg:ppu00730)

    - thiG: PP_5104 | Q88CS6 | Thiazole synthase (EC 2.8.1.10) (EC 2.8.1.10; primary
    bucket kegg:ppu00730)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Thiamine biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00730
- Resolved ID: ppu00730
- Resolved name: Thiamine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00730 with 13 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 13

- thiL: PP_0519 | Q88QH4 | Thiamine-monophosphate kinase (TMP kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) (EC 2.7.4.16; primary bucket kegg:ppu00730)
- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary bucket kegg:ppu00730)
- thiO: PP_0612 | Q88Q83 | Glycine oxidase (GO) (EC 1.4.3.19) (EC 1.4.3.19; primary bucket kegg:ppu00730)
- iscS: PP_0842 | Q88PK8 | Cysteine desulfurase IscS (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- adk: PP_1506 | P0A136 | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase) (EC 2.7.4.3; primary bucket kegg:ppu00730)
- iscS-II: PP_2435 | Q88K56 | cysteine desulfurase (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- PP_3186: PP_3186 | Q88I16 | Aminopyrimidine aminohydrolase (EC 3.5.99.2) (EC 3.5.99.2; primary bucket kegg:ppu00730)
- thiD: PP_4782 | Q88DP2 | hydroxymethylpyrimidine kinase (EC 2.7.1.49) (EC 2.7.1.49; primary bucket kegg:ppu00730)
- thiE: PP_4783 | Q88DP1 | Thiamine-phosphate synthase (TP synthase) (TPS) (EC 2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphorylase) (TMP-PPase) (EC 2.5.1.3; primary bucket kegg:ppu00730)
- rsgA: PP_4903 | Q88DC4 | Small ribosomal subunit biogenesis GTPase RsgA (EC 3.6.1.-) (EC 3.6.1.-; primary bucket kegg:ppu00730)
- thiC: PP_4922 | Q88DA5 | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine phosphate synthase) (HMP-P synthase) (HMP-phosphate synthase) (HMPP synthase) (Thiamine biosynthesis protein ThiC) (EC 4.1.99.17; primary bucket kegg:ppu00730)
- thiI: PP_5045 | Q88CY4 | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine synthase) (EC 2.8.1.4; primary bucket kegg:ppu00730)
- thiG: PP_5104 | Q88CS6 | Thiazole synthase (EC 2.8.1.10) (EC 2.8.1.10; primary bucket kegg:ppu00730)

## Generic Module Context

### Working Scope

A bacterial thiamine diphosphate biosynthesis module covering formation of the hydroxymethylpyrimidine and thiazole moieties, condensation to thiamine monophosphate, and phosphorylation to the active thiamine diphosphate cofactor. In Pseudomonas putida KT2440, KEGG ppu00730 also includes shared precursor, sulfur-transfer, thiamine-salvage, nucleotide, and ribosome-side entries; those are treated as support or boundary context rather than all being strict thiamine-biosynthetic enzymes.

### Provisional Biological Outline

- Thiamine biosynthesis
  - 1. DXP precursor supply
  - 1-deoxy-D-xylulose 5-phosphate supply
    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
  - 2. HMP-P formation
  - Hydroxymethylpyrimidine phosphate formation
    - ThiC phosphomethylpyrimidine synthase (molecular player: PSEPK thiC; activity or role: phosphomethylpyrimidine synthase activity)
  - 3. HMP phosphorylation
  - Hydroxymethylpyrimidine phosphorylation
    - ThiD hydroxymethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: hydroxymethylpyrimidine kinase activity)
    - ThiD phosphomethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: phosphomethylpyrimidine kinase activity)
  - 4. glyoxyl imine supply
  - Glycine oxidation for thiazole synthesis
    - ThiO glycine oxidase (molecular player: PSEPK thiO; activity or role: glycine oxidase activity)
  - 5. sulfur transfer to the thiazole branch
  - ThiS sulfur-carrier charging
    - ThiI sulfurtransferase (molecular player: PSEPK thiI; activity or role: tRNA-uracil-4 sulfurtransferase activity)
  - 6. thiazole phosphate formation
  - Thiazole phosphate formation
    - ThiG thiazole synthase (molecular player: PSEPK thiG; activity or role: thiazole synthase activity)
  - 7. thiamine monophosphate formation
  - Thiamine monophosphate formation
    - ThiE thiamine-phosphate synthase (molecular player: PSEPK thiE; activity or role: thiamine-phosphate diphosphorylase activity)
  - 8. thiamine diphosphate formation
  - Thiamine diphosphate formation
    - ThiL thiamine-phosphate kinase (molecular player: PSEPK thiL; activity or role: thiamine-phosphate kinase activity)

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

Thiamine biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00730
- Resolved ID: ppu00730
- Resolved name: Thiamine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00730 with 13 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 13

- thiL: PP_0519 | Q88QH4 | Thiamine-monophosphate kinase (TMP kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) (EC 2.7.4.16; primary bucket kegg:ppu00730)
- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary bucket kegg:ppu00730)
- thiO: PP_0612 | Q88Q83 | Glycine oxidase (GO) (EC 1.4.3.19) (EC 1.4.3.19; primary bucket kegg:ppu00730)
- iscS: PP_0842 | Q88PK8 | Cysteine desulfurase IscS (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- adk: PP_1506 | P0A136 | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase) (EC 2.7.4.3; primary bucket kegg:ppu00730)
- iscS-II: PP_2435 | Q88K56 | cysteine desulfurase (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- PP_3186: PP_3186 | Q88I16 | Aminopyrimidine aminohydrolase (EC 3.5.99.2) (EC 3.5.99.2; primary bucket kegg:ppu00730)
- thiD: PP_4782 | Q88DP2 | hydroxymethylpyrimidine kinase (EC 2.7.1.49) (EC 2.7.1.49; primary bucket kegg:ppu00730)
- thiE: PP_4783 | Q88DP1 | Thiamine-phosphate synthase (TP synthase) (TPS) (EC 2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphorylase) (TMP-PPase) (EC 2.5.1.3; primary bucket kegg:ppu00730)
- rsgA: PP_4903 | Q88DC4 | Small ribosomal subunit biogenesis GTPase RsgA (EC 3.6.1.-) (EC 3.6.1.-; primary bucket kegg:ppu00730)
- thiC: PP_4922 | Q88DA5 | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine phosphate synthase) (HMP-P synthase) (HMP-phosphate synthase) (HMPP synthase) (Thiamine biosynthesis protein ThiC) (EC 4.1.99.17; primary bucket kegg:ppu00730)
- thiI: PP_5045 | Q88CY4 | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine synthase) (EC 2.8.1.4; primary bucket kegg:ppu00730)
- thiG: PP_5104 | Q88CS6 | Thiazole synthase (EC 2.8.1.10) (EC 2.8.1.10; primary bucket kegg:ppu00730)

## Generic Module Context

### Working Scope

A bacterial thiamine diphosphate biosynthesis module covering formation of the hydroxymethylpyrimidine and thiazole moieties, condensation to thiamine monophosphate, and phosphorylation to the active thiamine diphosphate cofactor. In Pseudomonas putida KT2440, KEGG ppu00730 also includes shared precursor, sulfur-transfer, thiamine-salvage, nucleotide, and ribosome-side entries; those are treated as support or boundary context rather than all being strict thiamine-biosynthetic enzymes.

### Provisional Biological Outline

- Thiamine biosynthesis
  - 1. DXP precursor supply
  - 1-deoxy-D-xylulose 5-phosphate supply
    - Dxs 1-deoxy-D-xylulose-5-phosphate synthase (molecular player: PSEPK dxs; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
  - 2. HMP-P formation
  - Hydroxymethylpyrimidine phosphate formation
    - ThiC phosphomethylpyrimidine synthase (molecular player: PSEPK thiC; activity or role: phosphomethylpyrimidine synthase activity)
  - 3. HMP phosphorylation
  - Hydroxymethylpyrimidine phosphorylation
    - ThiD hydroxymethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: hydroxymethylpyrimidine kinase activity)
    - ThiD phosphomethylpyrimidine kinase (molecular player: PSEPK thiD; activity or role: phosphomethylpyrimidine kinase activity)
  - 4. glyoxyl imine supply
  - Glycine oxidation for thiazole synthesis
    - ThiO glycine oxidase (molecular player: PSEPK thiO; activity or role: glycine oxidase activity)
  - 5. sulfur transfer to the thiazole branch
  - ThiS sulfur-carrier charging
    - ThiI sulfurtransferase (molecular player: PSEPK thiI; activity or role: tRNA-uracil-4 sulfurtransferase activity)
  - 6. thiazole phosphate formation
  - Thiazole phosphate formation
    - ThiG thiazole synthase (molecular player: PSEPK thiG; activity or role: thiazole synthase activity)
  - 7. thiamine monophosphate formation
  - Thiamine monophosphate formation
    - ThiE thiamine-phosphate synthase (molecular player: PSEPK thiE; activity or role: thiamine-phosphate diphosphorylase activity)
  - 8. thiamine diphosphate formation
  - Thiamine diphosphate formation
    - ThiL thiamine-phosphate kinase (molecular player: PSEPK thiL; activity or role: thiamine-phosphate kinase activity)

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

# Thiamine Biosynthesis in *Pseudomonas putida* KT2440: A Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 (NCBI taxon 160488; proteome UP000000556) encodes a complete de novo thiamine diphosphate (TPP/ThDP) biosynthesis pathway. Of the 13 genes listed in KEGG ppu00730, seven represent the canonical de novo core (thiC, thiD, thiE, thiG, thiO, thiL, and dxs), two provide essential sulfur-relay support (iscS, thiI), one functions in thiamine salvage (PP_3186/TenA-like), and three are boundary or over-annotated entries that should not be treated as pathway-specific (adk, rsgA, iscS-II). The most important finding for annotation curation is that ThiS (sulfur carrier protein) and ThiF (ThiS adenylyltransferase), which are essential components of the thiazole sulfur-transfer step in all characterized bacterial thiamine pathways, are absent from the 13-gene candidate list, representing a metadata gap rather than a biological absence. Direct biochemical evidence from KT2440 exists only for ThiO (glycine oxidase, purified and characterized) and Dxs (functionally characterized in isoprenoid engineering contexts); all other assignments rest on strong sequence homology and comparative genetics from *E. coli*, *B. subtilis*, and *P. aeruginosa*.

## 2. Target-Organism Pathway Definition

### Pathway Boundaries

The thiamine diphosphate biosynthesis module encompasses: (i) the formation of the hydroxymethylpyrimidine phosphate (HMP-P) moiety from 5-aminoimidazole ribonucleotide (AIR), (ii) the formation of the thiazole phosphate (THZ-P) moiety from 1-deoxy-D-xylulose 5-phosphate (DXP), glycine-derived dehydroglycine, and a sulfur atom delivered via thiocarboxylated ThiS, (iii) the condensation of HMP-PP and THZ-P to form thiamine monophosphate (TMP), and (iv) phosphorylation of TMP to yield the active cofactor thiamine diphosphate (ThDP/TPP) (park2003biosynthesisofthe pages 1-2, horn1993structuralgenesfor pages 1-3, godoi2006structureofthe pages 1-1).

### Neighboring Pathways to Keep Separate

- **MEP/isoprenoid pathway**: Shares DXP synthase (Dxs) as a precursor-supply enzyme but is a distinct metabolic module (hernandezarranz2019engineeringpseudomonasputida pages 8-9, hernandezarranz2019engineeringpseudomonasputida pages 1-2).
- **Purine biosynthesis**: Provides AIR, the substrate for ThiC; should be treated as upstream context.
- **Fe-S cluster biogenesis / tRNA thiolation**: Shares IscS and ThiI with the thiamine sulfur relay, but these represent independent metabolic functions (lauhon2000theiscsgene pages 1-1, das2021themultifacetedbacterial pages 11-12).
- **Thiamine salvage**: Includes TenA-like aminopyrimidine aminohydrolase (PP_3186) and potentially thiamine kinase/transport functions; should be distinguished from de novo biosynthesis.
- **General nucleotide metabolism**: Adk (adenylate kinase) and RsgA (ribosome biogenesis GTPase) appear in KEGG ppu00730 but are housekeeping functions, not thiamine-specific.

### Alternate Names and Database Definitions

KEGG ppu00730 corresponds to "Thiamine metabolism," which encompasses both biosynthesis and salvage. MetaCyc uses "thiamine diphosphate biosynthesis I (E. coli)" as the canonical bacterial pathway. The pathway is also referenced as vitamin B1 biosynthesis. In the iJN1462 genome-scale metabolic model of KT2440, thiamine biosynthetic reactions are included within the cofactor/prosthetic group subsystem.

## 3. Expected Step Model

The canonical bacterial de novo thiamine diphosphate biosynthesis pathway comprises eight biochemical steps organized into two converging branches:

**Pyrimidine branch:**
- **Step 1** (DXP supply): Dxs catalyzes formation of 1-deoxy-D-xylulose 5-phosphate from pyruvate and glyceraldehyde-3-phosphate (godoi2006structureofthe pages 1-1).
- **Step 2** (HMP-P formation): ThiC converts AIR to hydroxymethylpyrimidine phosphate (horn1993structuralgenesfor pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7).
- **Step 3** (HMP-PP formation): ThiD phosphorylates HMP-P to HMP-PP (horn1993structuralgenesfor pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7).

**Thiazole branch:**
- **Step 4** (Dehydroglycine supply): ThiO oxidizes glycine to the imine/dehydroglycine intermediate (equar2015purificationandproperties pages 1-2, park2003biosynthesisofthe pages 1-2).
- **Step 5** (Sulfur transfer): IscS mobilizes sulfur from cysteine → ThiI transfers persulfide → ThiF adenylates ThiS → ThiS-thiocarboxylate serves as the sulfur donor (lauhon2000theiscsgene pages 1-1, park2003biosynthesisofthe pages 1-2, park2003biosynthesisofthe pages 6-8).
- **Step 6** (THZ-P formation): ThiG assembles the thiazole ring from DXP, dehydroglycine, and ThiS-COSH (park2003biosynthesisofthe pages 1-2, park2003biosynthesisofthe pages 6-8, park2003biosynthesisofthe pages 8-9).

**Coupling and activation:**
- **Step 7** (TMP formation): ThiE condenses HMP-PP and THZ-P to form TMP (horn1993structuralgenesfor pages 1-3, godoi2006structureofthe pages 1-1).
- **Step 8** (TPP formation): ThiL phosphorylates TMP to TPP (horn1993structuralgenesfor pages 1-3, godoi2006structureofthe pages 1-1).

Note that *P. putida* KT2440, like *B. subtilis* and unlike *E. coli*, uses ThiO (glycine oxidase) rather than ThiH (tyrosine lyase) for the dehydroglycine supply step, consistent with the Pseudomonadota ThiO-type pathway variant (park2003biosynthesisofthe pages 1-2).

## 4. Candidate Genes and Evidence

The following table provides the comprehensive assessment of all 13 candidate genes from KEGG ppu00730:

| Gene Name | Locus Tag | UniProt ID | Proposed Function | Module Role (core de novo / support / salvage / boundary) | Evidence Type | Confidence | Curation Notes |
|---|---|---|---|---|---|---|---|
| thiL | PP_0519 | Q88QH4 | Thiamine-monophosphate kinase; converts TMP to TPP | core de novo | homology, pathway database | high | Fits terminal activation step of thiamine biosynthesis; no direct KT2440 biochemistry located, but role is canonical and strongly conserved in bacteria (horn1993structuralgenesfor pages 1-3, godoi2006structureofthe pages 1-1) |
| dxs | PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase; supplies DXP precursor for thiazole branch and MEP pathway | support | direct biochemistry/physiology in KT2440, homology | high | Shared precursor-supply enzyme rather than thiamine-specific enzyme; experimentally manipulated in KT2440 for MEP/isoprenoid flux, confirming active DXP synthesis in the target strain (hernandezarranz2019engineeringpseudomonasputida pages 8-9, hernandezarranz2019engineeringpseudomonasputida pages 2-4, hernandezarranz2019engineeringpseudomonasputida pages 1-2, godoi2006structureofthe pages 1-1) |
| thiO | PP_0612 | Q88Q83 | Glycine oxidase; provides dehydroglycine/glyoxyl imine for thiazole synthesis | core de novo | direct biochemistry in KT2440 | high | Best direct evidence in this module: purified and characterized from KT2440; distinctive monomeric glycine-preferring enzyme, supporting assignment to thiazole branch step 4 (equar2015purificationandproperties pages 1-2, equar2015purificationandproperties pages 2-4, equar2015purificationandproperties pages 4-5) |
| iscS | PP_0842 | Q88PK8 | Cysteine desulfurase; mobilizes sulfur for ThiS thiocarboxylation and thiazole sulfur incorporation | support | homology, comparative biochemistry, pathway database | high | Strong support role in thiamine sulfur relay, but primary biology is broader sulfur trafficking/Fe-S/tRNA pathways; should not be treated as thiamine-specific core enzyme (lauhon2000theiscsgene pages 1-1, das2021themultifacetedbacterial pages 11-12, equar2015purificationandproperties pages 2-4) |
| adk | PP_1506 | P0A136 | Adenylate kinase; interconverts ATP/ADP/AMP | boundary | pathway database only | low | General nucleotide homeostasis enzyme; inclusion in KEGG map reflects metabolic context, not a dedicated thiamine-biosynthetic step; likely over-propagated for this module (horn1993structuralgenesfor pages 1-3) |
| iscS-II | PP_2435 | Q88K56 | Second cysteine desulfurase; possible backup sulfur donor | support | homology, genomic annotation | low-medium | Presence suggests possible redundancy in sulfur mobilization, but no thiamine-specific evidence for KT2440 was found; keep as candidate support only, not covered core step (das2021themultifacetedbacterial pages 11-12) |
| PP_3186 | PP_3186 | Q88I16 | Aminopyrimidine aminohydrolase (TenA-like); salvage of thiamine pyrimidine intermediates | salvage | homology, pathway database | medium | Better viewed as salvage/boundary component than de novo biosynthesis; likely relevant to aminopyrimidine salvage rather than required core pathway satisfiability (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 6-7) |
| thiD | PP_4782 | Q88DP2 | Hydroxymethylpyrimidine/HMP-P kinase; phosphorylates HMP branch intermediates | core de novo | homology, pathway database | high | Canonical pyrimidine-branch enzyme; assignment is strong by conserved pathway logic even without direct KT2440 assay (horn1993structuralgenesfor pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7) |
| thiE | PP_4783 | Q88DP1 | Thiamine-phosphate synthase; condenses HMP-PP and thiazole-P to TMP | core de novo | homology, comparative genetics, pathway database | high | Highly conserved central condensation step; P. aeruginosa deletion data support essentiality of orthologous function under thiamine-free conditions, strengthening transfer to KT2440 (horn1993structuralgenesfor pages 1-3, kim2022pharmacologicalperturbationof pages 5-6) |
| rsgA | PP_4903 | Q88DC4 | Small ribosomal subunit biogenesis GTPase | boundary | pathway database only | low | No specific role in thiamine biosynthesis; likely a KEGG map passenger or annotation spillover from broad metabolism context; should be excluded from core module coverage (molina‐henares2010identificationofconditionally pages 2-3) |
| thiC | PP_4922 | Q88DA5 | HMP-P synthase; forms hydroxymethylpyrimidine phosphate from AIR | core de novo | homology, comparative genetics, pathway database | high | Canonical entry point to pyrimidine branch; P. aeruginosa mutant evidence supports orthologous importance in de novo thiamine synthesis (horn1993structuralgenesfor pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7, kim2022pharmacologicalperturbationof pages 5-6) |
| thiI | PP_5045 | Q88CY4 | ThiS sulfurtransferase/tRNA sulfurtransferase; mediates sulfur relay to ThiS and also functions in tRNA thiolation | support | homology, comparative biochemistry | high | Dual-function enzyme shared between thiamine sulfur transfer and tRNA modification; important support role but not exclusive to thiamine pathway, so curate as support rather than core de novo catalyst (lauhon2000theiscsgene pages 1-1, das2021themultifacetedbacterial pages 11-12) |
| thiG | PP_5104 | Q88CS6 | Thiazole synthase; assembles thiazole phosphate ring | core de novo | homology, comparative genetics, pathway database | high | Canonical thiazole-branch enzyme; strong conserved assignment, and P. aeruginosa knockout evidence supports necessity of orthologous function for de novo thiamine production (park2003biosynthesisofthe pages 1-2, park2003biosynthesisofthe pages 6-8, kim2022pharmacologicalperturbationof pages 5-6) |


*Table: This table assesses the 13 KEGG ppu00730 candidate genes for thiamine metabolism in Pseudomonas putida KT2440, distinguishing core de novo enzymes from support, salvage, and boundary genes. It is useful for module satisfiability review and for flagging likely over-annotations such as adk and rsgA.*

### Genes with Direct KT2440 Evidence

**ThiO (PP_0612)**: This is the only candidate gene with direct biochemical characterization from *P. putida* KT2440. Equar et al. (2015) purified and characterized the recombinant glycine oxidase (GOPP), demonstrating it is a monomeric 43.5 kDa FAD-containing flavoprotein with glycine-preferring substrate specificity and optimal activity at pH 8.5 and 40°C (equar2015purificationandproperties pages 1-2, equar2015purificationandproperties pages 2-4, equar2015purificationandproperties pages 4-5). This distinguishes it from the homotetrameric, D-proline-preferring homologs in *B. subtilis* (GOBS) and *Geobacillus kaustophilus* (GOGK), confirming a lineage-specific structural and kinetic variant.

**Dxs (PP_0527)**: While not characterized specifically for thiamine production in KT2440, this enzyme has been extensively studied in the context of isoprenoid/MEP pathway engineering. Overexpression of *dxs* in KT2440 leads to a 25-fold increase in lycopene accumulation, confirming active DXP synthase function (hernandezarranz2019engineeringpseudomonasputida pages 8-9, hernandezarranz2019engineeringpseudomonasputida pages 2-4, hernandezarranz2019engineeringpseudomonasputida pages 1-2). DXP is the shared precursor for both the MEP pathway and thiazole ring biosynthesis (godoi2006structureofthe pages 1-1).

### Genes with Strong Homology-Based Evidence

**ThiC (PP_4922)**, **ThiD (PP_4782)**, **ThiE (PP_4783)**, **ThiG (PP_5104)**, and **ThiL (PP_0519)** are all assigned by strong sequence conservation across γ-proteobacteria. In the closely related species *P. aeruginosa*, deletion mutants of thiC, thiE, and thiG are viable only with exogenous thiamine supplementation, confirming essentiality of orthologous functions for de novo TPP synthesis (kim2022pharmacologicalperturbationof pages 5-6). Transfer of this essentiality evidence to KT2440 is strong given the phylogenetic proximity within the Pseudomonadaceae.

### Support and Sulfur-Relay Genes

**IscS (PP_0842)**: The role of IscS as the master sulfur mobilizer for thiamine biosynthesis is well established in *E. coli*, where *iscS* deletion mutants are thiamine auxotrophs requiring exogenous thiazole precursor supplementation (lauhon2000theiscsgene pages 1-1). IscS initiates the sulfur cascade: L-cysteine → IscS persulfide → ThiI → ThiS-thiocarboxylate (lauhon2000theiscsgene pages 1-1, das2021themultifacetedbacterial pages 11-12). However, IscS serves multiple pathways (Fe-S clusters, tRNA thiolation, molybdopterin, biotin, lipoic acid) and should not be classified as a thiamine-specific enzyme.

**ThiI (PP_5045)**: A bifunctional protein that acts both in tRNA s4U thiolation and in thiamine-related sulfur transfer to ThiS. ThiI accepts persulfide from IscS and mediates its transfer to the ThiS sulfur carrier protein (lauhon2000theiscsgene pages 1-1, das2021themultifacetedbacterial pages 11-12). This dual function is conserved across bacteria.

**IscS-II (PP_2435)**: The second cysteine desulfurase may provide functional redundancy. In *E. coli*, IscS is the primary contributor and neither of the remaining NifS-like paralogs can complement *iscS* deletion (lauhon2000theiscsgene pages 1-1). The specific contribution of IscS-II to thiamine biosynthesis in KT2440 is uncertain.

### Salvage Pathway Gene

**PP_3186 (TenA-like)**: Annotated as an aminopyrimidine aminohydrolase (EC 3.5.99.2), this enzyme functions in the thiamine salvage pathway by cleaving aminopyrimidine from degraded thiamine or analogs, enabling reuse of the pyrimidine moiety. This is a salvage function, not part of the minimal de novo module.

### Boundary/Over-Annotated Genes

**Adk (PP_1506)**: Adenylate kinase is a ubiquitous housekeeping enzyme for nucleotide homeostasis. Its inclusion in KEGG ppu00730 reflects the ATP/ADP requirements of pathway kinases rather than a thiamine-specific catalytic role.

**RsgA (PP_4903)**: A small ribosomal subunit biogenesis GTPase with no established connection to thiamine metabolism. Its presence in the candidate list likely reflects KEGG map proximity or broad EC grouping and represents a clear over-annotation for this module.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

The module step coverage assessment is summarized below:

| Step Number | Step Name | Key Enzyme(s) | Candidate Gene(s) in KT2440 | Status | Notes |
|---|---|---|---|---|---|
| 1 | DXP precursor supply | Dxs | PP_0527 (dxs) | covered | Shared precursor step with the MEP/isoprenoid pathway; active DXP synthesis is supported in KT2440 by metabolic engineering studies, but this is a boundary/shared step rather than thiamine-specific catalysis (hernandezarranz2019engineeringpseudomonasputida pages 8-9, hernandezarranz2019engineeringpseudomonasputida pages 1-2) |
| 2 | HMP-P formation | ThiC | PP_4922 (thiC) | covered | Canonical pyrimidine-branch enzyme for HMP-P synthesis; assignment is strong by conserved bacterial pathway logic and comparative genetics (horn1993structuralgenesfor pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7, kim2022pharmacologicalperturbationof pages 5-6) |
| 3 | HMP phosphorylation | ThiD | PP_4782 (thiD) | covered | ThiD is the expected HMP/HMP-P kinase in the de novo branch and is commonly bifunctional in bacteria (horn1993structuralgenesfor pages 1-3, maupinfurlow2018vitaminb1(thiamine) pages 4-7) |
| 4 | Glyoxyl imine supply | ThiO | PP_0612 (thiO) | covered | Strongest direct KT2440 evidence in the module: purified and biochemically characterized glycine oxidase that supplies the thiazole branch precursor (equar2015purificationandproperties pages 1-2, equar2015purificationandproperties pages 2-4, equar2015purificationandproperties pages 4-5) |
| 5 | Sulfur transfer to thiazole branch | IscS, ThiI, ThiF, ThiS | PP_0842 (iscS), PP_5045 (thiI); ThiF not in candidate list; ThiS not in candidate list | candidate_uncertain | IscS and ThiI fit the canonical sulfur relay, but ThiF and ThiS are expected yet absent from the local candidate list; this indicates likely incomplete metadata or pathway-bucket under-capture rather than a biologically real absence (lauhon2000theiscsgene pages 1-1, park2003biosynthesisofthe pages 1-2, park2003biosynthesisofthe pages 6-8, iyer2006theprokaryoticantecedents pages 10-11) |
| 6 | Thiazole phosphate formation | ThiG | PP_5104 (thiG) | covered | Canonical thiazole synthase; conserved assignment is strong and orthologous function is supported by comparative bacterial genetics (park2003biosynthesisofthe pages 1-2, park2003biosynthesisofthe pages 6-8, kim2022pharmacologicalperturbationof pages 5-6) |
| 7 | TMP formation | ThiE | PP_4783 (thiE) | covered | ThiE catalyzes condensation of HMP-PP and thiazole phosphate to TMP; highly conserved core step (horn1993structuralgenesfor pages 1-3, kim2022pharmacologicalperturbationof pages 5-6) |
| 8 | TPP formation | ThiL | PP_0519 (thiL) | covered | Expected terminal activation step converting TMP to TPP; strong conserved bacterial assignment (horn1993structuralgenesfor pages 1-3, godoi2006structureofthe pages 1-1) |
| S1 | Thiamine salvage | TenA-like aminopyrimidine aminohydrolase | PP_3186 | covered | Best treated as salvage/context rather than part of the minimal de novo module; supports aminopyrimidine salvage (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 6-7) |
| S2 | Sulfur mobilization support | IscS, IscS-II | PP_0842 (iscS), PP_2435 (iscS-II) | boundary | Sulfur mobilization is broader than thiamine alone; iscS is credible support for the pathway, while iscS-II remains ambiguous for thiamine-specific participation (lauhon2000theiscsgene pages 1-1, das2021themultifacetedbacterial pages 11-12) |
| B1 | General nucleotide metabolism | Adenylate kinase | PP_1506 (adk) | not_expected | Housekeeping nucleotide homeostasis enzyme; not part of the thiamine diphosphate biosynthetic core (horn1993structuralgenesfor pages 1-3) |
| B2 | Ribosome biogenesis | RsgA | PP_4903 (rsgA) | not_expected | Ribosome biogenesis GTPase; likely KEGG map spillover/over-annotation for this module (molina‐henares2010identificationofconditionally pages 2-3) |


*Table: This table summarizes stepwise coverage of thiamine diphosphate biosynthesis in Pseudomonas putida KT2440, distinguishing core covered steps from uncertain sulfur-transfer components and non-core boundary genes. It is useful for module satisfiability and annotation curation.*

### Critical Gap: ThiS and ThiF

The most significant annotation gap is the absence of **ThiS** (sulfur carrier protein) and **ThiF** (ThiS adenylyltransferase) from the 13-gene candidate list. In all characterized bacterial thiamine biosynthesis systems, ThiF adenylates the C-terminal carboxylate of ThiS, which is subsequently thiocarboxylated through the IscS→ThiI sulfur relay to form ThiS-COSH, the ultimate sulfur donor for thiazole ring formation (park2003biosynthesisofthe pages 1-2, park2003biosynthesisofthe pages 6-8, iyer2006theprokaryoticantecedents pages 10-11). ThiS is the most strongly conserved partner of ThiG (approximately 80% co-occurrence in gene neighborhoods) (iyer2006theprokaryoticantecedents pages 9-10). In the KT2440 genome, *thiS* is expected to be encoded in the vicinity of *thiG* (PP_5104), likely at locus PP_5103 based on typical *thiCEFSGH* operon organization in γ-proteobacteria. Similarly, *thiF* should be present in the thiamine gene cluster. Their absence from the KEGG candidate list likely reflects metadata under-capture or non-assignment of separate KEGG orthologs rather than true biological absence.

### Likely Over-Annotations

- **adk (PP_1506)**: Should be excluded from the thiamine-specific module; it is a general nucleotide metabolism enzyme.
- **rsgA (PP_4903)**: Should be excluded; it is a ribosome biogenesis factor with no thiamine-specific function.
- **iscS-II (PP_2435)**: Ambiguous for thiamine; no evidence supports a specific thiamine role distinct from the primary IscS.

### Paralog Ambiguity

The presence of two cysteine desulfurases (*iscS* PP_0842 and *iscS-II* PP_2435) creates paralog ambiguity. In *E. coli*, only IscS is required for thiamine biosynthesis, and the other NifS-like paralogs cannot substitute (lauhon2000theiscsgene pages 1-1). Whether IscS-II in KT2440 has any thiamine-relevant function remains experimentally unresolved.

### Absence of Thiamine Auxotrophs in KT2440 Screens

A genome-wide mini-Tn5 mutant library screen of KT2440 identified 48 conditionally essential genes for growth on glucose minimal medium, including auxotrophs for biotin, nicotinic acid, and vitamin B12, but no thiamine auxotrophs were reported (molina‐henares2010identificationofconditionally pages 12-13, molina‐henares2010identificationofconditionally pages 1-2, molina‐henares2010identificationofconditionally pages 4-6). This is notable and could reflect: (i) incomplete library coverage of thiamine loci, (ii) functional redundancy between salvage and de novo pathways under the screening conditions, or (iii) the possibility that trace thiamine contamination was present. By contrast, *P. aeruginosa* thiamine biosynthesis deletion mutants (*ΔthiG*, *ΔthiE*, *ΔthiC*) are strictly dependent on exogenous thiamine (kim2022pharmacologicalperturbationof pages 5-6), confirming that de novo synthesis is essential in the absence of salvage in this closely related species.

## 6. Module and GO-Curation Recommendations

### Step Coverage Status

| Step | Status | Recommendation |
|------|--------|----------------|
| DXP precursor supply (Dxs) | **covered** | Mark as shared/boundary; not thiamine-specific |
| HMP-P formation (ThiC) | **covered** | Core de novo |
| HMP phosphorylation (ThiD) | **covered** | Core de novo |
| Glyoxyl imine supply (ThiO) | **covered** | Core de novo; best direct evidence |
| Sulfur transfer (IscS + ThiI + ThiF + ThiS) | **candidate_uncertain** | IscS and ThiI present; ThiF and ThiS need to be added from genome |
| THZ-P formation (ThiG) | **covered** | Core de novo |
| TMP formation (ThiE) | **covered** | Core de novo |
| TPP formation (ThiL) | **covered** | Core de novo |

### Specific Recommendations

1. **Add ThiS and ThiF to the module**: These should be recovered from the KT2440 genome annotation (expected near PP_5104/thiG). Their absence from the KEGG candidate list is a metadata deficiency, not a biological gap.
2. **Remove adk and rsgA from the core module**: These are general housekeeping enzymes with no thiamine-specific catalytic role and should be excluded or explicitly marked as "not_expected_in_target_module."
3. **Reclassify iscS and thiI as support/sulfur-relay**: These are genuine participants in the thiamine sulfur cascade but serve multiple pathways; they should be flagged as "shared_support" rather than dedicated thiamine enzymes.
4. **Reclassify PP_3186 as salvage**: The TenA-like aminopyrimidine aminohydrolase belongs to the thiamine salvage sub-module, not the de novo core.
5. **Reclassify iscS-II as ambiguous/candidate_uncertain**: No direct evidence supports a thiamine-specific role.
6. **TPP riboswitch annotation**: In *Pseudomonas* species, thiamine biosynthesis and transport genes are typically regulated by TPP-sensing riboswitches (kim2022pharmacologicalperturbationof pages 4-5, sudarsan2005thiaminepyrophosphateriboswitches pages 1-2). Annotation of TPP riboswitches upstream of *thiC*, *thiD*/*thiE*, and potential transport operons in KT2440 would improve regulatory context for this module.

### GO Term Considerations

- ThiO should carry GO:0008125 (glycine oxidase activity) and GO:0009228 (thiamine biosynthetic process), supported by direct biochemical evidence from KT2440 (equar2015purificationandproperties pages 1-2, equar2015purificationandproperties pages 2-4).
- ThiI should carry both GO:0004814-related tRNA thiolation terms and GO:0009228 (thiamine biosynthetic process) to reflect its bifunctional nature.
- Dxs should carry GO:0008661 (1-deoxy-D-xylulose-5-phosphate synthase activity) but should not be annotated exclusively to thiamine biosynthesis, as its primary metabolic role is MEP/isoprenoid pathway supply (hernandezarranz2019engineeringpseudomonasputida pages 8-9, hernandezarranz2019engineeringpseudomonasputida pages 1-2).

## 7. Genes to Promote to Full Review

The following genes warrant deeper investigation:

1. **ThiS and ThiF (expected PP_5103 vicinity)**: Priority for recovery and formal inclusion. Confirm locus tags, verify operon structure adjacent to *thiG*, and ensure proper KEGG/UniProt annotation.
2. **ThiO (PP_0612)**: Already biochemically characterized from KT2440 (equar2015purificationandproperties pages 1-2, equar2015purificationandproperties pages 2-4, equar2015purificationandproperties pages 4-5) — valuable for cross-referencing GO annotations with the unique monomeric structure and glycine-preferring specificity distinct from *B. subtilis*.
3. **ThiC (PP_4922)**: Central to the pyrimidine branch; warrants a full review given its S-adenosylmethionine radical enzyme mechanism and potential oxygen sensitivity, which may affect KT2440 performance under different growth conditions.
4. **IscS (PP_0842)**: Given its role at the top of the sulfur cascade for thiamine, tRNA, Fe-S, and multiple other pathways, a full review would clarify how sulfur partitioning is regulated in KT2440.

## 8. Key References

- Equar MY, Tani Y, Mihara H (2015). "Purification and Properties of Glycine Oxidase from *Pseudomonas putida* KT2440." *J Nutr Sci Vitaminol* 61(6):506–10. DOI: 10.3177/jnsv.61.506 (equar2015purificationandproperties pages 1-2, equar2015purificationandproperties pages 2-4, equar2015purificationandproperties pages 4-5)
- Lauhon CT, Kambampati R (2000). "The *iscS* gene in *Escherichia coli* is required for the biosynthesis of 4-thiouridine, thiamin, and NAD." *J Biol Chem* 275:20096–20103. DOI: 10.1074/jbc.M002680200 (lauhon2000theiscsgene pages 1-1)
- Park J-H et al. (2003). "Biosynthesis of the thiazole moiety of thiamin pyrophosphate (vitamin B1)." *Biochemistry* 42(42):12430–8. DOI: 10.1021/bi034902z (park2003biosynthesisofthe pages 1-2, park2003biosynthesisofthe pages 6-8, park2003biosynthesisofthe pages 8-9)
- Van Horn PB et al. (1993). "Structural genes for thiamine biosynthetic enzymes (thiCEFGH) in *Escherichia coli* K-12." *J Bacteriol* 175:982–992. DOI: 10.1128/jb.175.4.982-992.1993 (horn1993structuralgenesfor pages 1-3)
- Molina-Henares MA et al. (2010). "Identification of conditionally essential genes for growth of *Pseudomonas putida* KT2440 on minimal medium." *Environ Microbiol* 12:1468–1485. DOI: 10.1111/j.1462-2920.2010.02166.x (molina‐henares2010identificationofconditionally pages 12-13, molina‐henares2010identificationofconditionally pages 1-2, molina‐henares2010identificationofconditionally pages 4-6)
- Kim HJ et al. (2022). "Pharmacological perturbation of thiamine metabolism sensitizes *Pseudomonas aeruginosa* to multiple antibacterial agents." *Cell Chem Biol* 29:1317–1324.e5. DOI: 10.1016/j.chembiol.2022.07.001 (kim2022pharmacologicalperturbationof pages 4-5, kim2022pharmacologicalperturbationof pages 3-4, kim2022pharmacologicalperturbationof pages 5-6, kim2022pharmacologicalperturbationof pages 6-7, kim2022pharmacologicalperturbationof pages 1-3)
- Hernandez-Arranz S et al. (2019). "Engineering *Pseudomonas putida* for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors." *Microb Cell Fact* 18. DOI: 10.1186/s12934-019-1204-z (hernandezarranz2019engineeringpseudomonasputida pages 8-9, hernandezarranz2019engineeringpseudomonasputida pages 2-4, hernandezarranz2019engineeringpseudomonasputida pages 1-2)
- Das M et al. (2021). "The multifaceted bacterial cysteine desulfurases: from metabolism to pathogenesis." *Antioxidants* 10:997. DOI: 10.3390/antiox10070997 (das2021themultifacetedbacterial pages 11-12)
- Maupin-Furlow JA (2018). "Vitamin B1 (Thiamine) Metabolism and Regulation in Archaea." *B Group Vitamins*. DOI: 10.5772/intechopen.77170 (maupinfurlow2018vitaminb1(thiamine) pages 4-7)
- Godoi PHC et al. (2006). "Structure of the Thiazole Biosynthetic Enzyme THI1 from *Arabidopsis thaliana*." *J Biol Chem* 281:30957–30966. DOI: 10.1074/jbc.M604469200 (godoi2006structureofthe pages 1-1)
- Iyer LM et al. (2006). "The prokaryotic antecedents of the ubiquitin-signaling system." *Genome Biol* 7:R60. DOI: 10.1186/gb-2006-7-7-r60 (iyer2006theprokaryoticantecedents pages 9-10, iyer2006theprokaryoticantecedents pages 10-11)
- Sudarsan N et al. (2005). "Thiamine pyrophosphate riboswitches are targets for the antimicrobial compound pyrithiamine." *Chem Biol* 12(12):1325–35. DOI: 10.1016/j.chembiol.2005.10.007 (sudarsan2005thiaminepyrophosphateriboswitches pages 1-2)
- Nogales J et al. (2020). "High-quality genome-scale metabolic modelling of *Pseudomonas putida* highlights its broad metabolic capabilities." *Environ Microbiol* 22:255–269. DOI: 10.1111/1462-2920.14843
- Belda E et al. (2016). "The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis." *Environ Microbiol* 18(10):3403–3424. DOI: 10.1111/1462-2920.13230
- Nelson KE et al. (2002). "Complete genome sequence and comparative analysis of the metabolically versatile *Pseudomonas putida* KT2440." *Environ Microbiol* 4(12):799–808. DOI: 10.1046/j.1462-2920.2002.00366.x

References

1. (park2003biosynthesisofthe pages 1-2): Joo-Heon Park, Pieter C. Dorrestein, Huili Zhai, Cynthia Kinsland, Fred W. McLafferty, and Tadhg P. Begley. Biosynthesis of the thiazole moiety of thiamin pyrophosphate (vitamin b1). Biochemistry, 42 42:12430-8, Sep 2003. URL: https://doi.org/10.1021/bi034902z, doi:10.1021/bi034902z. This article has 161 citations and is from a peer-reviewed journal.

2. (horn1993structuralgenesfor pages 1-3): P. B. V. Horn, Allyson D. Backstrom, Valley Stewart, and T. Begley. Structural genes for thiamine biosynthetic enzymes (thicefgh) in escherichia coli k-12. Journal of Bacteriology, 175:982-992, Feb 1993. URL: https://doi.org/10.1128/jb.175.4.982-992.1993, doi:10.1128/jb.175.4.982-992.1993. This article has 167 citations and is from a peer-reviewed journal.

3. (godoi2006structureofthe pages 1-1): Paulo H.C. Godoi, Rodrigo S. Galhardo, Douglas D. Luche, Marie-Anne Van Sluys, Carlos F.M. Menck, and Glaucius Oliva. Structure of the thiazole biosynthetic enzyme thi1 from arabidopsis thaliana*. Journal of Biological Chemistry, 281:30957-30966, Oct 2006. URL: https://doi.org/10.1074/jbc.m604469200, doi:10.1074/jbc.m604469200. This article has 76 citations and is from a domain leading peer-reviewed journal.

4. (hernandezarranz2019engineeringpseudomonasputida pages 8-9): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

5. (hernandezarranz2019engineeringpseudomonasputida pages 1-2): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

6. (lauhon2000theiscsgene pages 1-1): Charles T. Lauhon and Ravi Kambampati. The iscs gene in escherichia coli is required for the biosynthesis of 4-thiouridine, thiamin, and nad*. The Journal of Biological Chemistry, 275:20096-20103, Jun 2000. URL: https://doi.org/10.1074/jbc.m002680200, doi:10.1074/jbc.m002680200. This article has 265 citations.

7. (das2021themultifacetedbacterial pages 11-12): Mayashree Das, Arshiya Dewan, Somnath Shee, and Amit Singh. The multifaceted bacterial cysteine desulfurases: from metabolism to pathogenesis. Antioxidants, 10:997, Jun 2021. URL: https://doi.org/10.3390/antiox10070997, doi:10.3390/antiox10070997. This article has 39 citations.

8. (maupinfurlow2018vitaminb1(thiamine) pages 4-7): Julie A. Maupin-Furlow. Vitamin b1 (thiamine) metabolism and regulation in archaea. B Group Vitamins - Current Uses and Perspectives, Sep 2018. URL: https://doi.org/10.5772/intechopen.77170, doi:10.5772/intechopen.77170. This article has 22 citations.

9. (equar2015purificationandproperties pages 1-2): Messele Yohannes EQUAR, Yasushi TANI, and Hisaaki MIHARA. Purification and properties of glycine oxidase from pseudomonas putida kt2440. Journal of nutritional science and vitaminology, 61 6:506-10, Jan 2015. URL: https://doi.org/10.3177/jnsv.61.506, doi:10.3177/jnsv.61.506. This article has 12 citations and is from a peer-reviewed journal.

10. (park2003biosynthesisofthe pages 6-8): Joo-Heon Park, Pieter C. Dorrestein, Huili Zhai, Cynthia Kinsland, Fred W. McLafferty, and Tadhg P. Begley. Biosynthesis of the thiazole moiety of thiamin pyrophosphate (vitamin b1). Biochemistry, 42 42:12430-8, Sep 2003. URL: https://doi.org/10.1021/bi034902z, doi:10.1021/bi034902z. This article has 161 citations and is from a peer-reviewed journal.

11. (park2003biosynthesisofthe pages 8-9): Joo-Heon Park, Pieter C. Dorrestein, Huili Zhai, Cynthia Kinsland, Fred W. McLafferty, and Tadhg P. Begley. Biosynthesis of the thiazole moiety of thiamin pyrophosphate (vitamin b1). Biochemistry, 42 42:12430-8, Sep 2003. URL: https://doi.org/10.1021/bi034902z, doi:10.1021/bi034902z. This article has 161 citations and is from a peer-reviewed journal.

12. (hernandezarranz2019engineeringpseudomonasputida pages 2-4): Sofía Hernandez-Arranz, Jordi Perez-Gil, Dominic Marshall-Sabey, and Manuel Rodriguez-Concepcion. Engineering pseudomonas putida for isoprenoid production by manipulating endogenous and shunt pathways supplying precursors. Microbial Cell Factories, Sep 2019. URL: https://doi.org/10.1186/s12934-019-1204-z, doi:10.1186/s12934-019-1204-z. This article has 41 citations and is from a peer-reviewed journal.

13. (equar2015purificationandproperties pages 2-4): Messele Yohannes EQUAR, Yasushi TANI, and Hisaaki MIHARA. Purification and properties of glycine oxidase from pseudomonas putida kt2440. Journal of nutritional science and vitaminology, 61 6:506-10, Jan 2015. URL: https://doi.org/10.3177/jnsv.61.506, doi:10.3177/jnsv.61.506. This article has 12 citations and is from a peer-reviewed journal.

14. (equar2015purificationandproperties pages 4-5): Messele Yohannes EQUAR, Yasushi TANI, and Hisaaki MIHARA. Purification and properties of glycine oxidase from pseudomonas putida kt2440. Journal of nutritional science and vitaminology, 61 6:506-10, Jan 2015. URL: https://doi.org/10.3177/jnsv.61.506, doi:10.3177/jnsv.61.506. This article has 12 citations and is from a peer-reviewed journal.

15. (molina‐henares2010identificationofconditionally pages 2-3): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

16. (molina‐henares2010identificationofconditionally pages 6-7): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

17. (kim2022pharmacologicalperturbationof pages 5-6): Hyung Jun Kim, Yingying Li, Michael Zimmermann, Yunmi Lee, Hui Wen Lim, Alvin Swee Leong Tan, Inhee Choi, Yoonae Ko, Sangchul Lee, Jeong Jea Seo, Mooyoung Seo, Hee Kyoung Jeon, Jonathan Cechetto, Joey Kuok Hoong Yam, Liang Yang, Uwe Sauer, Soojin Jang, and Kevin Pethe. Pharmacological perturbation of thiamine metabolism sensitizes pseudomonas aeruginosa to multiple antibacterial agents. Aug 2022. URL: https://doi.org/10.1016/j.chembiol.2022.07.001, doi:10.1016/j.chembiol.2022.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

18. (iyer2006theprokaryoticantecedents pages 10-11): Lakshminarayan M Iyer, A Maxwell Burroughs, and L Aravind. The prokaryotic antecedents of the ubiquitin-signaling system and the early evolution of ubiquitin-like β-grasp domains. Genome Biology, 7:R60-R60, Jul 2006. URL: https://doi.org/10.1186/gb-2006-7-7-r60, doi:10.1186/gb-2006-7-7-r60. This article has 220 citations and is from a highest quality peer-reviewed journal.

19. (iyer2006theprokaryoticantecedents pages 9-10): Lakshminarayan M Iyer, A Maxwell Burroughs, and L Aravind. The prokaryotic antecedents of the ubiquitin-signaling system and the early evolution of ubiquitin-like β-grasp domains. Genome Biology, 7:R60-R60, Jul 2006. URL: https://doi.org/10.1186/gb-2006-7-7-r60, doi:10.1186/gb-2006-7-7-r60. This article has 220 citations and is from a highest quality peer-reviewed journal.

20. (molina‐henares2010identificationofconditionally pages 12-13): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

21. (molina‐henares2010identificationofconditionally pages 1-2): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

22. (molina‐henares2010identificationofconditionally pages 4-6): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

23. (kim2022pharmacologicalperturbationof pages 4-5): Hyung Jun Kim, Yingying Li, Michael Zimmermann, Yunmi Lee, Hui Wen Lim, Alvin Swee Leong Tan, Inhee Choi, Yoonae Ko, Sangchul Lee, Jeong Jea Seo, Mooyoung Seo, Hee Kyoung Jeon, Jonathan Cechetto, Joey Kuok Hoong Yam, Liang Yang, Uwe Sauer, Soojin Jang, and Kevin Pethe. Pharmacological perturbation of thiamine metabolism sensitizes pseudomonas aeruginosa to multiple antibacterial agents. Aug 2022. URL: https://doi.org/10.1016/j.chembiol.2022.07.001, doi:10.1016/j.chembiol.2022.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

24. (sudarsan2005thiaminepyrophosphateriboswitches pages 1-2): Narasimhan Sudarsan, Smadar Cohen-Chalamish, Shingo Nakamura, Gail Mitchell Emilsson, and Ronald R. Breaker. Thiamine pyrophosphate riboswitches are targets for the antimicrobial compound pyrithiamine. Chemistry & biology, 12 12:1325-35, Dec 2005. URL: https://doi.org/10.1016/j.chembiol.2005.10.007, doi:10.1016/j.chembiol.2005.10.007. This article has 365 citations.

25. (kim2022pharmacologicalperturbationof pages 3-4): Hyung Jun Kim, Yingying Li, Michael Zimmermann, Yunmi Lee, Hui Wen Lim, Alvin Swee Leong Tan, Inhee Choi, Yoonae Ko, Sangchul Lee, Jeong Jea Seo, Mooyoung Seo, Hee Kyoung Jeon, Jonathan Cechetto, Joey Kuok Hoong Yam, Liang Yang, Uwe Sauer, Soojin Jang, and Kevin Pethe. Pharmacological perturbation of thiamine metabolism sensitizes pseudomonas aeruginosa to multiple antibacterial agents. Aug 2022. URL: https://doi.org/10.1016/j.chembiol.2022.07.001, doi:10.1016/j.chembiol.2022.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

26. (kim2022pharmacologicalperturbationof pages 6-7): Hyung Jun Kim, Yingying Li, Michael Zimmermann, Yunmi Lee, Hui Wen Lim, Alvin Swee Leong Tan, Inhee Choi, Yoonae Ko, Sangchul Lee, Jeong Jea Seo, Mooyoung Seo, Hee Kyoung Jeon, Jonathan Cechetto, Joey Kuok Hoong Yam, Liang Yang, Uwe Sauer, Soojin Jang, and Kevin Pethe. Pharmacological perturbation of thiamine metabolism sensitizes pseudomonas aeruginosa to multiple antibacterial agents. Aug 2022. URL: https://doi.org/10.1016/j.chembiol.2022.07.001, doi:10.1016/j.chembiol.2022.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

27. (kim2022pharmacologicalperturbationof pages 1-3): Hyung Jun Kim, Yingying Li, Michael Zimmermann, Yunmi Lee, Hui Wen Lim, Alvin Swee Leong Tan, Inhee Choi, Yoonae Ko, Sangchul Lee, Jeong Jea Seo, Mooyoung Seo, Hee Kyoung Jeon, Jonathan Cechetto, Joey Kuok Hoong Yam, Liang Yang, Uwe Sauer, Soojin Jang, and Kevin Pethe. Pharmacological perturbation of thiamine metabolism sensitizes pseudomonas aeruginosa to multiple antibacterial agents. Aug 2022. URL: https://doi.org/10.1016/j.chembiol.2022.07.001, doi:10.1016/j.chembiol.2022.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. godoi2006structureofthe pages 1-1
2. park2003biosynthesisofthe pages 1-2
3. horn1993structuralgenesfor pages 1-3
4. das2021themultifacetedbacterial pages 11-12
5. kim2022pharmacologicalperturbationof pages 5-6
6. lauhon2000theiscsgene pages 1-1
7. iyer2006theprokaryoticantecedents pages 9-10
8. sudarsan2005thiaminepyrophosphateriboswitches pages 1-2
9. hernandezarranz2019engineeringpseudomonasputida pages 8-9
10. hernandezarranz2019engineeringpseudomonasputida pages 1-2
11. equar2015purificationandproperties pages 1-2
12. park2003biosynthesisofthe pages 6-8
13. park2003biosynthesisofthe pages 8-9
14. hernandezarranz2019engineeringpseudomonasputida pages 2-4
15. equar2015purificationandproperties pages 2-4
16. equar2015purificationandproperties pages 4-5
17. iyer2006theprokaryoticantecedents pages 10-11
18. kim2022pharmacologicalperturbationof pages 4-5
19. kim2022pharmacologicalperturbationof pages 3-4
20. kim2022pharmacologicalperturbationof pages 6-7
21. kim2022pharmacologicalperturbationof pages 1-3
22. https://doi.org/10.1021/bi034902z,
23. https://doi.org/10.1128/jb.175.4.982-992.1993,
24. https://doi.org/10.1074/jbc.m604469200,
25. https://doi.org/10.1186/s12934-019-1204-z,
26. https://doi.org/10.1074/jbc.m002680200,
27. https://doi.org/10.3390/antiox10070997,
28. https://doi.org/10.5772/intechopen.77170,
29. https://doi.org/10.3177/jnsv.61.506,
30. https://doi.org/10.1111/j.1462-2920.2010.02166.x,
31. https://doi.org/10.1016/j.chembiol.2022.07.001,
32. https://doi.org/10.1186/gb-2006-7-7-r60,
33. https://doi.org/10.1016/j.chembiol.2005.10.007,