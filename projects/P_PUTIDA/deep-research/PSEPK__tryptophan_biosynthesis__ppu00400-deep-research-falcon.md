---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T19:33:28.923506'
end_time: '2026-07-05T19:55:21.688967'
duration_seconds: 1312.77
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-tryptophan biosynthesis (microbial)
  module_summary: 'De novo biosynthesis of L-tryptophan from chorismate, the branch-point
    precursor of the aromatic amino acids. Five enzymatic activities convert chorismate
    to L-tryptophan, drawing in L-glutamine (amide nitrogen), PRPP (5-phospho-alpha-D-ribose
    1-diphosphate), and L-serine, and releasing pyruvate, CO2 and glyceraldehyde 3-phosphate
    along the way. The pathway is the classic textbook microbial operon (the trp operon)
    and is notable for extensive enzyme fusion and channeling: anthranilate synthase
    is a glutamine amidotransferase built from a synthase component (TrpE) and a glutaminase
    component (TrpD/TrpG), the latter frequently fused to anthranilate phosphoribosyltransferase
    in enteric bacteria; phosphoribosylanthranilate isomerase (TrpF) is often fused
    to indole-3-glycerol-phosphate synthase (TrpC); and the terminal tryptophan synthase
    is an alpha-2-beta-2 complex in which indole produced at the TrpA (alpha) active
    site is channeled through an intramolecular tunnel to the TrpB (beta) active site,
    where it condenses with L-serine, so free indole is not released. The pathway
    is feedback-regulated by L-tryptophan, classically at anthranilate synthase and,
    in many bacteria, also transcriptionally via attenuation and the TrpR repressor.'
  module_outline: "- L-tryptophan biosynthesis\n  - 1. chorismate to anthranilate\
    \ (anthranilate synthase)\n  - Chorismate to anthranilate (anthranilate synthase,\
    \ alternative architectures)\n    - Alternative versions by enzyme architecture:\
    \ Anthranilate synthase subunit architecture\n      - Two-component anthranilate\
    \ synthase (TrpE + TrpD/TrpG)\n        - trpE: anthranilate synthase component\
    \ I (synthase subunit) (molecular player: anthranilate synthase component I (TrpE);\
    \ activity or role: anthranilate synthase activity)\n        - trpD_1/trpG: glutamine\
    \ amidotransferase component of anthranilate synthase (molecular player: anthranilate\
    \ synthase glutamine amidotransferase component (TrpG/TrpD); activity or role:\
    \ anthranilate synthase activity)\n      - Single-protein anthranilate synthase\
    \ (TrpED, alphaproteobacterial clade)\n        - trpED: single-protein anthranilate\
    \ synthase (molecular player: single-protein anthranilate synthase (TrpED clade);\
    \ activity or role: anthranilate synthase activity)\n  - 2. anthranilate phosphoribosyltransferase\
    \ (TrpD2)\n  - Anthranilate to N-(5'-phosphoribosyl)-anthranilate\n    - trpD_2:\
    \ anthranilate phosphoribosyltransferase (molecular player: anthranilate phosphoribosyltransferase\
    \ activity; activity or role: anthranilate phosphoribosyltransferase activity)\n\
    \  - 3. phosphoribosylanthranilate isomerase (TrpF)\n  - PRA to CdRP\n    - PRAI/trpF:\
    \ phosphoribosylanthranilate isomerase (molecular player: phosphoribosylanthranilate\
    \ isomerase activity; activity or role: phosphoribosylanthranilate isomerase activity)\n\
    \  - 4. indole-3-glycerol-phosphate synthase (TrpC)\n  - CdRP to indole-3-glycerol\
    \ phosphate\n    - IGPS/trpC: indole-3-glycerol-phosphate synthase (molecular\
    \ player: indole-3-glycerol-phosphate synthase activity; activity or role: indole-3-glycerol-phosphate\
    \ synthase activity)\n  - 5. tryptophan synthase complex (TrpA + TrpB, channeled)\n\
    \  - Indole-3-glycerol phosphate + L-serine to L-tryptophan\n    - trpA: tryptophan\
    \ synthase alpha subunit (indole-3-glycerol-phosphate lyase) (molecular player:\
    \ tryptophan synthase alpha chain (TrpA); activity or role: tryptophan synthase\
    \ activity)\n    - trpB: tryptophan synthase beta subunit (molecular player: tryptophan\
    \ synthase beta chain (TrpB); activity or role: tryptophan synthase activity)"
  module_connections: '- Chorismate to anthranilate (anthranilate synthase, alternative
    architectures) feeds into Anthranilate to N-(5''-phosphoribosyl)-anthranilate:
    Anthranilate feeds the phosphoribosyltransferase step.

    - Anthranilate to N-(5''-phosphoribosyl)-anthranilate precedes PRA to CdRP

    - PRA to CdRP precedes CdRP to indole-3-glycerol phosphate

    - CdRP to indole-3-glycerol phosphate precedes Indole-3-glycerol phosphate + L-serine
    to L-tryptophan'
  pathway_query: ppu00400
  pathway_id: ppu00400
  pathway_name: Phenylalanine, tyrosine and tryptophan biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00400 with 20 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '28'
  candidate_genes: '- aroE__Q88RQ5: PP_0074 | Q88RQ5 | Shikimate dehydrogenase (NADP(+))
    (SDH) (EC 1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00999)

    - trpA: PP_0082 | Q88RP7 | Tryptophan synthase alpha chain (EC 4.2.1.20) (EC 4.2.1.20;
    primary bucket kegg:ppu00400)

    - trpB: PP_0083 | Q88RP6 | Tryptophan synthase beta chain (EC 4.2.1.20) (EC 4.2.1.20;
    primary bucket kegg:ppu00400)

    - trpE: PP_0417 | Q88QS1 | Anthranilate synthase component 1 (EC 4.1.3.27) (EC
    4.1.3.27; primary bucket kegg:ppu00400)

    - pabA: PP_0420 | Q88QR8 | Aminodeoxychorismate synthase / para-aminobenzoate
    synthase multi-enzyme complex (EC 2.6.1.85) (EC 2.6.1.85; primary bucket kegg:ppu00400)

    - trpD: PP_0421 | Q88QR7 | Anthranilate phosphoribosyltransferase (EC 2.4.2.18)
    (EC 2.4.2.18; primary bucket kegg:ppu00400)

    - trpC: PP_0422 | Q88QR6 | Indole-3-glycerol phosphate synthase (IGPS) (EC 4.1.1.48)
    (EC 4.1.1.48; primary bucket kegg:ppu00400)

    - aroQ1: PP_0560 | Q88QD4 | 3-dehydroquinate dehydratase 1 (3-dehydroquinase 1)
    (EC 4.2.1.10) (Type II DHQase 1) (EC 4.2.1.10; primary bucket kegg:ppu00400)

    - hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9)
    (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)

    - pheA: PP_1769 | Q88M06 | Bifunctional chorismate mutase/prephenate dehydratase
    (EC 4.2.1.51) (EC 5.4.99.5) (Chorismate mutase-prephenate dehydratase) (p-protein)
    (EC 4.2.1.51; 5.4.99.5; primary bucket kegg:ppu00400)

    - aroA: PP_1770 | Q88M05 | 3-phosphoshikimate 1-carboxyvinyltransferase (EC 2.5.1.19)
    (5-enolpyruvylshikimate-3-phosphate synthase) (EPSP synthase) (EPSPS) (EC 2.5.1.19;
    primary bucket kegg:ppu00401)

    - aroC: PP_1830 | Q88LU7 | Chorismate synthase (CS) (EC 4.2.3.5) (5-enolpyruvylshikimate-3-phosphate
    phospholyase) (EC 4.2.3.5; primary bucket kegg:ppu00400)

    - aroH: PP_1866 | Q88LR3 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54)
    (EC 2.5.1.54; primary bucket kegg:ppu00400)

    - tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - trpF: PP_1995 | Q88LE0 | N-(5''-phosphoribosyl)anthranilate isomerase (PRAI)
    (EC 5.3.1.24) (EC 5.3.1.24; primary bucket kegg:ppu00400)

    - aroF-I: PP_2324 | Q88KG6 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54)
    (EC 2.5.1.54; primary bucket kegg:ppu00400)

    - aroE__Q88K85: PP_2406 | Q88K85 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC
    1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00400)

    - aroQ2: PP_2407 | Q88K84 | 3-dehydroquinate dehydratase 2 (3-dehydroquinase 2)
    (EC 4.2.1.10) (Type II DHQase 2) (EC 4.2.1.10; primary bucket kegg:ppu00400)

    - quiC1: PP_2554 | Q88JU3 | 3-dehydroshikimate dehydratase (DSD) (EC 4.2.1.118)
    (EC 4.2.1.118; primary bucket kegg:ppu00400)

    - aroE__Q88IJ7: PP_3002 | Q88IJ7 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC
    1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00999)

    - aroQ-III: PP_3003 | Q88IJ6 | 3-dehydroquinate dehydratase (3-dehydroquinase)
    (EC 4.2.1.10) (Type II DHQase) (EC 4.2.1.10; primary bucket kegg:ppu00400)

    - aroF-II: PP_3080 | Q88IB9 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC
    2.5.1.54) (EC 2.5.1.54; primary bucket kegg:ppu00400)

    - quiA: PP_3569 | Q88GZ6 | Quinate dehydrogenase (Quinone) (EC 1.1.5.8) (EC 1.1.5.8;
    primary bucket kegg:ppu00400)

    - amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - PP_3768: PP_3768 | Q88GF6 | Shikimate 5-dehydrogenase (EC 1.1.1.-) (EC 1.1.1.-;
    primary bucket kegg:ppu00999)

    - phhA: PP_4490 | Q88EH3 | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase)
    (EC 1.14.16.1; primary bucket kegg:ppu00360)

    - aroB: PP_5078 | Q88CV2 | 3-dehydroquinate synthase (DHQS) (EC 4.2.3.4) (EC 4.2.3.4;
    primary bucket kegg:ppu00400)

    - aroK: PP_5079 | Q88CV1 | Shikimate kinase (SK) (EC 2.7.1.71) (EC 2.7.1.71; primary
    bucket kegg:ppu00400)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-tryptophan biosynthesis (microbial) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00400
- Resolved ID: ppu00400
- Resolved name: Phenylalanine, tyrosine and tryptophan biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00400 with 20 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 28

- aroE__Q88RQ5: PP_0074 | Q88RQ5 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00999)
- trpA: PP_0082 | Q88RP7 | Tryptophan synthase alpha chain (EC 4.2.1.20) (EC 4.2.1.20; primary bucket kegg:ppu00400)
- trpB: PP_0083 | Q88RP6 | Tryptophan synthase beta chain (EC 4.2.1.20) (EC 4.2.1.20; primary bucket kegg:ppu00400)
- trpE: PP_0417 | Q88QS1 | Anthranilate synthase component 1 (EC 4.1.3.27) (EC 4.1.3.27; primary bucket kegg:ppu00400)
- pabA: PP_0420 | Q88QR8 | Aminodeoxychorismate synthase / para-aminobenzoate synthase multi-enzyme complex (EC 2.6.1.85) (EC 2.6.1.85; primary bucket kegg:ppu00400)
- trpD: PP_0421 | Q88QR7 | Anthranilate phosphoribosyltransferase (EC 2.4.2.18) (EC 2.4.2.18; primary bucket kegg:ppu00400)
- trpC: PP_0422 | Q88QR6 | Indole-3-glycerol phosphate synthase (IGPS) (EC 4.1.1.48) (EC 4.1.1.48; primary bucket kegg:ppu00400)
- aroQ1: PP_0560 | Q88QD4 | 3-dehydroquinate dehydratase 1 (3-dehydroquinase 1) (EC 4.2.1.10) (Type II DHQase 1) (EC 4.2.1.10; primary bucket kegg:ppu00400)
- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)
- pheA: PP_1769 | Q88M06 | Bifunctional chorismate mutase/prephenate dehydratase (EC 4.2.1.51) (EC 5.4.99.5) (Chorismate mutase-prephenate dehydratase) (p-protein) (EC 4.2.1.51; 5.4.99.5; primary bucket kegg:ppu00400)
- aroA: PP_1770 | Q88M05 | 3-phosphoshikimate 1-carboxyvinyltransferase (EC 2.5.1.19) (5-enolpyruvylshikimate-3-phosphate synthase) (EPSP synthase) (EPSPS) (EC 2.5.1.19; primary bucket kegg:ppu00401)
- aroC: PP_1830 | Q88LU7 | Chorismate synthase (CS) (EC 4.2.3.5) (5-enolpyruvylshikimate-3-phosphate phospholyase) (EC 4.2.3.5; primary bucket kegg:ppu00400)
- aroH: PP_1866 | Q88LR3 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) (EC 2.5.1.54; primary bucket kegg:ppu00400)
- tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- trpF: PP_1995 | Q88LE0 | N-(5'-phosphoribosyl)anthranilate isomerase (PRAI) (EC 5.3.1.24) (EC 5.3.1.24; primary bucket kegg:ppu00400)
- aroF-I: PP_2324 | Q88KG6 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) (EC 2.5.1.54; primary bucket kegg:ppu00400)
- aroE__Q88K85: PP_2406 | Q88K85 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00400)
- aroQ2: PP_2407 | Q88K84 | 3-dehydroquinate dehydratase 2 (3-dehydroquinase 2) (EC 4.2.1.10) (Type II DHQase 2) (EC 4.2.1.10; primary bucket kegg:ppu00400)
- quiC1: PP_2554 | Q88JU3 | 3-dehydroshikimate dehydratase (DSD) (EC 4.2.1.118) (EC 4.2.1.118; primary bucket kegg:ppu00400)
- aroE__Q88IJ7: PP_3002 | Q88IJ7 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00999)
- aroQ-III: PP_3003 | Q88IJ6 | 3-dehydroquinate dehydratase (3-dehydroquinase) (EC 4.2.1.10) (Type II DHQase) (EC 4.2.1.10; primary bucket kegg:ppu00400)
- aroF-II: PP_3080 | Q88IB9 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) (EC 2.5.1.54; primary bucket kegg:ppu00400)
- quiA: PP_3569 | Q88GZ6 | Quinate dehydrogenase (Quinone) (EC 1.1.5.8) (EC 1.1.5.8; primary bucket kegg:ppu00400)
- amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- PP_3768: PP_3768 | Q88GF6 | Shikimate 5-dehydrogenase (EC 1.1.1.-) (EC 1.1.1.-; primary bucket kegg:ppu00999)
- phhA: PP_4490 | Q88EH3 | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase) (EC 1.14.16.1; primary bucket kegg:ppu00360)
- aroB: PP_5078 | Q88CV2 | 3-dehydroquinate synthase (DHQS) (EC 4.2.3.4) (EC 4.2.3.4; primary bucket kegg:ppu00400)
- aroK: PP_5079 | Q88CV1 | Shikimate kinase (SK) (EC 2.7.1.71) (EC 2.7.1.71; primary bucket kegg:ppu00400)

## Generic Module Context

### Working Scope

De novo biosynthesis of L-tryptophan from chorismate, the branch-point precursor of the aromatic amino acids. Five enzymatic activities convert chorismate to L-tryptophan, drawing in L-glutamine (amide nitrogen), PRPP (5-phospho-alpha-D-ribose 1-diphosphate), and L-serine, and releasing pyruvate, CO2 and glyceraldehyde 3-phosphate along the way. The pathway is the classic textbook microbial operon (the trp operon) and is notable for extensive enzyme fusion and channeling: anthranilate synthase is a glutamine amidotransferase built from a synthase component (TrpE) and a glutaminase component (TrpD/TrpG), the latter frequently fused to anthranilate phosphoribosyltransferase in enteric bacteria; phosphoribosylanthranilate isomerase (TrpF) is often fused to indole-3-glycerol-phosphate synthase (TrpC); and the terminal tryptophan synthase is an alpha-2-beta-2 complex in which indole produced at the TrpA (alpha) active site is channeled through an intramolecular tunnel to the TrpB (beta) active site, where it condenses with L-serine, so free indole is not released. The pathway is feedback-regulated by L-tryptophan, classically at anthranilate synthase and, in many bacteria, also transcriptionally via attenuation and the TrpR repressor.

### Provisional Biological Outline

- L-tryptophan biosynthesis
  - 1. chorismate to anthranilate (anthranilate synthase)
  - Chorismate to anthranilate (anthranilate synthase, alternative architectures)
    - Alternative versions by enzyme architecture: Anthranilate synthase subunit architecture
      - Two-component anthranilate synthase (TrpE + TrpD/TrpG)
        - trpE: anthranilate synthase component I (synthase subunit) (molecular player: anthranilate synthase component I (TrpE); activity or role: anthranilate synthase activity)
        - trpD_1/trpG: glutamine amidotransferase component of anthranilate synthase (molecular player: anthranilate synthase glutamine amidotransferase component (TrpG/TrpD); activity or role: anthranilate synthase activity)
      - Single-protein anthranilate synthase (TrpED, alphaproteobacterial clade)
        - trpED: single-protein anthranilate synthase (molecular player: single-protein anthranilate synthase (TrpED clade); activity or role: anthranilate synthase activity)
  - 2. anthranilate phosphoribosyltransferase (TrpD2)
  - Anthranilate to N-(5'-phosphoribosyl)-anthranilate
    - trpD_2: anthranilate phosphoribosyltransferase (molecular player: anthranilate phosphoribosyltransferase activity; activity or role: anthranilate phosphoribosyltransferase activity)
  - 3. phosphoribosylanthranilate isomerase (TrpF)
  - PRA to CdRP
    - PRAI/trpF: phosphoribosylanthranilate isomerase (molecular player: phosphoribosylanthranilate isomerase activity; activity or role: phosphoribosylanthranilate isomerase activity)
  - 4. indole-3-glycerol-phosphate synthase (TrpC)
  - CdRP to indole-3-glycerol phosphate
    - IGPS/trpC: indole-3-glycerol-phosphate synthase (molecular player: indole-3-glycerol-phosphate synthase activity; activity or role: indole-3-glycerol-phosphate synthase activity)
  - 5. tryptophan synthase complex (TrpA + TrpB, channeled)
  - Indole-3-glycerol phosphate + L-serine to L-tryptophan
    - trpA: tryptophan synthase alpha subunit (indole-3-glycerol-phosphate lyase) (molecular player: tryptophan synthase alpha chain (TrpA); activity or role: tryptophan synthase activity)
    - trpB: tryptophan synthase beta subunit (molecular player: tryptophan synthase beta chain (TrpB); activity or role: tryptophan synthase activity)

### Known Relationships Among Steps

- Chorismate to anthranilate (anthranilate synthase, alternative architectures) feeds into Anthranilate to N-(5'-phosphoribosyl)-anthranilate: Anthranilate feeds the phosphoribosyltransferase step.
- Anthranilate to N-(5'-phosphoribosyl)-anthranilate precedes PRA to CdRP
- PRA to CdRP precedes CdRP to indole-3-glycerol phosphate
- CdRP to indole-3-glycerol phosphate precedes Indole-3-glycerol phosphate + L-serine to L-tryptophan

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

L-tryptophan biosynthesis (microbial) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00400
- Resolved ID: ppu00400
- Resolved name: Phenylalanine, tyrosine and tryptophan biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00400 with 20 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 28

- aroE__Q88RQ5: PP_0074 | Q88RQ5 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00999)
- trpA: PP_0082 | Q88RP7 | Tryptophan synthase alpha chain (EC 4.2.1.20) (EC 4.2.1.20; primary bucket kegg:ppu00400)
- trpB: PP_0083 | Q88RP6 | Tryptophan synthase beta chain (EC 4.2.1.20) (EC 4.2.1.20; primary bucket kegg:ppu00400)
- trpE: PP_0417 | Q88QS1 | Anthranilate synthase component 1 (EC 4.1.3.27) (EC 4.1.3.27; primary bucket kegg:ppu00400)
- pabA: PP_0420 | Q88QR8 | Aminodeoxychorismate synthase / para-aminobenzoate synthase multi-enzyme complex (EC 2.6.1.85) (EC 2.6.1.85; primary bucket kegg:ppu00400)
- trpD: PP_0421 | Q88QR7 | Anthranilate phosphoribosyltransferase (EC 2.4.2.18) (EC 2.4.2.18; primary bucket kegg:ppu00400)
- trpC: PP_0422 | Q88QR6 | Indole-3-glycerol phosphate synthase (IGPS) (EC 4.1.1.48) (EC 4.1.1.48; primary bucket kegg:ppu00400)
- aroQ1: PP_0560 | Q88QD4 | 3-dehydroquinate dehydratase 1 (3-dehydroquinase 1) (EC 4.2.1.10) (Type II DHQase 1) (EC 4.2.1.10; primary bucket kegg:ppu00400)
- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)
- pheA: PP_1769 | Q88M06 | Bifunctional chorismate mutase/prephenate dehydratase (EC 4.2.1.51) (EC 5.4.99.5) (Chorismate mutase-prephenate dehydratase) (p-protein) (EC 4.2.1.51; 5.4.99.5; primary bucket kegg:ppu00400)
- aroA: PP_1770 | Q88M05 | 3-phosphoshikimate 1-carboxyvinyltransferase (EC 2.5.1.19) (5-enolpyruvylshikimate-3-phosphate synthase) (EPSP synthase) (EPSPS) (EC 2.5.1.19; primary bucket kegg:ppu00401)
- aroC: PP_1830 | Q88LU7 | Chorismate synthase (CS) (EC 4.2.3.5) (5-enolpyruvylshikimate-3-phosphate phospholyase) (EC 4.2.3.5; primary bucket kegg:ppu00400)
- aroH: PP_1866 | Q88LR3 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) (EC 2.5.1.54; primary bucket kegg:ppu00400)
- tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- trpF: PP_1995 | Q88LE0 | N-(5'-phosphoribosyl)anthranilate isomerase (PRAI) (EC 5.3.1.24) (EC 5.3.1.24; primary bucket kegg:ppu00400)
- aroF-I: PP_2324 | Q88KG6 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) (EC 2.5.1.54; primary bucket kegg:ppu00400)
- aroE__Q88K85: PP_2406 | Q88K85 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00400)
- aroQ2: PP_2407 | Q88K84 | 3-dehydroquinate dehydratase 2 (3-dehydroquinase 2) (EC 4.2.1.10) (Type II DHQase 2) (EC 4.2.1.10; primary bucket kegg:ppu00400)
- quiC1: PP_2554 | Q88JU3 | 3-dehydroshikimate dehydratase (DSD) (EC 4.2.1.118) (EC 4.2.1.118; primary bucket kegg:ppu00400)
- aroE__Q88IJ7: PP_3002 | Q88IJ7 | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) (EC 1.1.1.25; primary bucket kegg:ppu00999)
- aroQ-III: PP_3003 | Q88IJ6 | 3-dehydroquinate dehydratase (3-dehydroquinase) (EC 4.2.1.10) (Type II DHQase) (EC 4.2.1.10; primary bucket kegg:ppu00400)
- aroF-II: PP_3080 | Q88IB9 | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) (EC 2.5.1.54; primary bucket kegg:ppu00400)
- quiA: PP_3569 | Q88GZ6 | Quinate dehydrogenase (Quinone) (EC 1.1.5.8) (EC 1.1.5.8; primary bucket kegg:ppu00400)
- amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- PP_3768: PP_3768 | Q88GF6 | Shikimate 5-dehydrogenase (EC 1.1.1.-) (EC 1.1.1.-; primary bucket kegg:ppu00999)
- phhA: PP_4490 | Q88EH3 | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase) (EC 1.14.16.1; primary bucket kegg:ppu00360)
- aroB: PP_5078 | Q88CV2 | 3-dehydroquinate synthase (DHQS) (EC 4.2.3.4) (EC 4.2.3.4; primary bucket kegg:ppu00400)
- aroK: PP_5079 | Q88CV1 | Shikimate kinase (SK) (EC 2.7.1.71) (EC 2.7.1.71; primary bucket kegg:ppu00400)

## Generic Module Context

### Working Scope

De novo biosynthesis of L-tryptophan from chorismate, the branch-point precursor of the aromatic amino acids. Five enzymatic activities convert chorismate to L-tryptophan, drawing in L-glutamine (amide nitrogen), PRPP (5-phospho-alpha-D-ribose 1-diphosphate), and L-serine, and releasing pyruvate, CO2 and glyceraldehyde 3-phosphate along the way. The pathway is the classic textbook microbial operon (the trp operon) and is notable for extensive enzyme fusion and channeling: anthranilate synthase is a glutamine amidotransferase built from a synthase component (TrpE) and a glutaminase component (TrpD/TrpG), the latter frequently fused to anthranilate phosphoribosyltransferase in enteric bacteria; phosphoribosylanthranilate isomerase (TrpF) is often fused to indole-3-glycerol-phosphate synthase (TrpC); and the terminal tryptophan synthase is an alpha-2-beta-2 complex in which indole produced at the TrpA (alpha) active site is channeled through an intramolecular tunnel to the TrpB (beta) active site, where it condenses with L-serine, so free indole is not released. The pathway is feedback-regulated by L-tryptophan, classically at anthranilate synthase and, in many bacteria, also transcriptionally via attenuation and the TrpR repressor.

### Provisional Biological Outline

- L-tryptophan biosynthesis
  - 1. chorismate to anthranilate (anthranilate synthase)
  - Chorismate to anthranilate (anthranilate synthase, alternative architectures)
    - Alternative versions by enzyme architecture: Anthranilate synthase subunit architecture
      - Two-component anthranilate synthase (TrpE + TrpD/TrpG)
        - trpE: anthranilate synthase component I (synthase subunit) (molecular player: anthranilate synthase component I (TrpE); activity or role: anthranilate synthase activity)
        - trpD_1/trpG: glutamine amidotransferase component of anthranilate synthase (molecular player: anthranilate synthase glutamine amidotransferase component (TrpG/TrpD); activity or role: anthranilate synthase activity)
      - Single-protein anthranilate synthase (TrpED, alphaproteobacterial clade)
        - trpED: single-protein anthranilate synthase (molecular player: single-protein anthranilate synthase (TrpED clade); activity or role: anthranilate synthase activity)
  - 2. anthranilate phosphoribosyltransferase (TrpD2)
  - Anthranilate to N-(5'-phosphoribosyl)-anthranilate
    - trpD_2: anthranilate phosphoribosyltransferase (molecular player: anthranilate phosphoribosyltransferase activity; activity or role: anthranilate phosphoribosyltransferase activity)
  - 3. phosphoribosylanthranilate isomerase (TrpF)
  - PRA to CdRP
    - PRAI/trpF: phosphoribosylanthranilate isomerase (molecular player: phosphoribosylanthranilate isomerase activity; activity or role: phosphoribosylanthranilate isomerase activity)
  - 4. indole-3-glycerol-phosphate synthase (TrpC)
  - CdRP to indole-3-glycerol phosphate
    - IGPS/trpC: indole-3-glycerol-phosphate synthase (molecular player: indole-3-glycerol-phosphate synthase activity; activity or role: indole-3-glycerol-phosphate synthase activity)
  - 5. tryptophan synthase complex (TrpA + TrpB, channeled)
  - Indole-3-glycerol phosphate + L-serine to L-tryptophan
    - trpA: tryptophan synthase alpha subunit (indole-3-glycerol-phosphate lyase) (molecular player: tryptophan synthase alpha chain (TrpA); activity or role: tryptophan synthase activity)
    - trpB: tryptophan synthase beta subunit (molecular player: tryptophan synthase beta chain (TrpB); activity or role: tryptophan synthase activity)

### Known Relationships Among Steps

- Chorismate to anthranilate (anthranilate synthase, alternative architectures) feeds into Anthranilate to N-(5'-phosphoribosyl)-anthranilate: Anthranilate feeds the phosphoribosyltransferase step.
- Anthranilate to N-(5'-phosphoribosyl)-anthranilate precedes PRA to CdRP
- PRA to CdRP precedes CdRP to indole-3-glycerol phosphate
- CdRP to indole-3-glycerol phosphate precedes Indole-3-glycerol phosphate + L-serine to L-tryptophan

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

# L-Tryptophan Biosynthesis in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

The de novo L-tryptophan biosynthetic pathway from chorismate is fully satisfiable in *Pseudomonas putida* KT2440 (NCBI taxon 160488). All five catalytic steps converting chorismate to L-tryptophan are encoded by seven genes organized in a characteristic *Pseudomonas*-type split operon arrangement that differs markedly from the contiguous *E. coli trp* operon. Direct experimental evidence from KT2440—including transposon auxotroph mapping, RT-PCR operon analysis, site-directed knockouts, and metabolic engineering—confirms the roles of trpE (PP_0417), trpG (PP_0420, locally annotated as pabA), trpD (PP_0421), trpC (PP_0422), trpF (PP_1995), trpA (PP_0082), and trpB (PP_0083) (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 4-6). A key curation issue is that PP_0420 is annotated as **pabA** in the candidate metadata, but the primary literature identifies it as **trpG** based on its operon context within the trpGDC cluster (molinahenares2009functionalanalysisof pages 2-4).

Of the 28 candidate genes provided, only 7 belong to the core tryptophan biosynthetic module (chorismate → L-tryptophan). The remaining candidates represent shared shikimate pathway enzymes (upstream precursor supply), phenylalanine/tyrosine branch enzymes, catabolic quinate-pathway enzymes, or genes with no functional connection to tryptophan biosynthesis. This review recommends that the L-tryptophan module boundary be drawn strictly at chorismate → L-tryptophan, with the upstream shikimate pathway treated as a separate shared module.

## 2. Target-Organism Pathway Definition

### 2.1 Biochemical Scope

The L-tryptophan biosynthesis pathway encompasses five enzymatic steps converting chorismate—the branch-point precursor shared by all three aromatic amino acids—to L-tryptophan. The pathway consumes L-glutamine (amide nitrogen donor at step 1), PRPP (phosphoribosyl donor at step 2), and L-serine (condensation partner at step 5), while releasing pyruvate, CO₂, and glyceraldehyde-3-phosphate as by-products (molinahenares2009functionalanalysisof pages 2-4).

### 2.2 Pathway Boundaries

The tryptophan-specific pathway begins at **chorismate** and ends at **L-tryptophan**. The upstream shikimate pathway (from PEP + E4P through DAHP, 3-dehydroquinate, 3-dehydroshikimate, shikimate, shikimate-3-phosphate, EPSP, to chorismate) is shared with phenylalanine and tyrosine biosynthesis and should be maintained as a separate module. The neighboring phenylalanine/tyrosine branch (via PheA/chorismate mutase and TyrA/prephenate dehydrogenase) is explicitly a competing pathway, not part of tryptophan biosynthesis (molinahenares2009functionalanalysisof pages 6-7, kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5).

### 2.3 Database Definitions

- **KEGG ppu00400**: "Phenylalanine, tyrosine and tryptophan biosynthesis" — this broad map encompasses the entire aromatic amino acid pathway including the shikimate pathway and all three branch points. For module curation, the tryptophan-specific portion should be delineated as chorismate → L-tryptophan only.
- **KEGG Module M00023**: L-Tryptophan biosynthesis, chorismate ⇒ tryptophan — this is the appropriate narrow module definition.

### 2.4 Regulatory Features Unique to *Pseudomonas*

Unlike *E. coli*, which uses the TrpR repressor and transcriptional attenuation, *P. putida* KT2440 employs a **positive regulatory** mechanism via **TrpI** (PP_0084), a LysR-family transcriptional activator. TrpI activates transcription of the trpBA operon in response to indole-3-glycerol phosphate (I3GP), which serves as the inducer molecule (xie2003ancientoriginof pages 5-6, matulis2022developmentandcharacterization pages 2-4). This regulatory paradigm is conserved across fluorescent pseudomonads including *P. aeruginosa* and *P. entomophila* (xie2003ancientoriginof pages 5-6). A TrpI insertion mutant in KT2440 does not exhibit tryptophan auxotrophy, consistent with its role as an activator rather than an essential biosynthetic enzyme (molinahenares2009functionalanalysisof pages 2-4).

## 3. Expected Step Model

All five catalytic steps of the chorismate-to-L-tryptophan pathway are present and experimentally validated in *P. putida* KT2440. The module step satisfiability assessment is summarized below:

| Step number | Reaction | Expected enzyme/gene | KT2440 gene assignment | Evidence type | Module status |
|---|---|---|---|---|---|
| 1 | Chorismate → anthranilate | Anthranilate synthase, component I + glutamine amidotransferase subunit (TrpE + TrpG) | **trpE** = PP_0417; **trpG** = PP_0420 (locally annotated as **pabA**, but KT2440 literature places PP_0420 in the **trpGDC** operon) | Direct in *P. putida* KT2440: auxotroph mapping for **trpE**, operon/transcription evidence for **trpGDC**, pathway reconstruction and gene organization (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 4-6) | **covered** |
| 2 | Anthranilate → N-(5'-phosphoribosyl)anthranilate (PRA) | Anthranilate phosphoribosyltransferase (TrpD) | **trpD** = PP_0421 | Direct in KT2440: auxotroph mapping, precursor-feeding phenotype, and functional confirmation from **trpDC** deletion used to accumulate anthranilate (molinahenares2009functionalanalysisof pages 2-4, kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5, molinahenares2009functionalanalysisof pages 4-6) | **covered** |
| 3 | PRA → 1-(o-carboxyphenylamino)-1-deoxyribulose-5-phosphate (CdRP) | Phosphoribosylanthranilate isomerase (TrpF) | **trpF** = PP_1995 | Direct in KT2440: targeted knockout caused tryptophan auxotrophy; RT-PCR supported monocistronic organization (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6) | **covered** |
| 4 | CdRP → indole-3-glycerol phosphate (I3GP) | Indole-3-glycerol phosphate synthase (TrpC) | **trpC** = PP_0422 | Direct in KT2440: auxotroph mapping, trpGDC operon evidence, and **trpDC** deletion experiments (molinahenares2009functionalanalysisof pages 2-4, kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5, molinahenares2009functionalanalysisof pages 4-6) | **covered** |
| 5 | I3GP + L-serine → L-tryptophan | Tryptophan synthase α/β complex (TrpA + TrpB) | **trpA** = PP_0082; **trpB** = PP_0083 | Direct in KT2440: auxotroph mapping for **trpA**, RT-PCR-supported **trpAB** operon, and conserved functional assignment in KT2440/Pseudomonas studies (molinahenares2009functionalanalysisof pages 2-4, matulis2022developmentandcharacterization pages 2-4, molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 4-6) | **covered** |
| Regulatory component | Regulation of terminal trp genes (not a catalytic step) | LysR-family regulator TrpI | **trpI** = PP_0084 | Mixed evidence: direct KT2440 genomic/operon context and non-auxotrophic mutant behavior; regulatory mechanism supported by KT2440 biosensor study and broader *Pseudomonas* literature (matulis2022developmentandcharacterization pages 2-4, molinahenares2009functionalanalysisof pages 2-4, xie2003ancientoriginof pages 5-6) | **regulatory component; not counted toward catalytic step coverage** |


*Table: This table summarizes whether each catalytic step of chorismate-to-L-tryptophan biosynthesis is satisfied in *Pseudomonas putida* KT2440, with the best-supported gene assignments and evidence types. It is useful for deciding module coverage and for flagging the key curation issue that PP_0420 is best treated as trpG rather than pabA in this pathway context.*

### 3.1 Gene Organization

The tryptophan biosynthesis genes in *P. putida* KT2440 are distributed across three unlinked chromosomal loci, in contrast to the single contiguous *trp* operon of *E. coli* (molinahenares2009functionalanalysisof pages 4-6, molinahenares2009functionalanalysisof pages 2-4):

**Locus 1 (PP_0082–PP_0084):** Contains the **trpAB** operon (PP_0082 = trpA, PP_0083 = trpB), where trpA and trpB overlap by one nucleotide and are co-transcribed as confirmed by RT-PCR. The **trpI** gene (PP_0084) is divergently transcribed from trpAB and encodes the LysR-family positive transcriptional regulator.

**Locus 2 (PP_0417–PP_0422):** Contains two transcriptional units: (a) monocistronic **trpE** (PP_0417), encoding anthranilate synthase component I, separated from the next cluster by two genes of unknown function (PP_0418, PP_0419); and (b) the **trpGDC** operon (PP_0420 = trpG, PP_0421 = trpD, PP_0422 = trpC), where trpG-trpD are separated by 9 nucleotides and trpD-trpC overlap by 6 nucleotides, confirmed as a single polycistronic transcript by RT-PCR.

**Locus 3 (PP_1995):** Contains the monocistronic **trpF** gene, unlinked to other trp genes, flanked by truA (pseudouridine synthase) and accD (acetyl-CoA carboxylase subunit). RT-PCR confirmed that trpF does not co-transcribe with flanking genes.

This split-operon architecture is conserved across all sequenced *Pseudomonas* species, with amino acid sequence identity of pathway enzymes ranging from 71–97% among *Pseudomonas* spp. (molinahenares2009functionalanalysisof pages 4-6).

### 3.2 Enzyme Architecture Notes

In *P. putida* KT2440, several features distinguish the enzyme architecture from the *E. coli* paradigm:

- **Anthranilate synthase** is a **two-component enzyme** (TrpE + TrpG), where the subunits are encoded on separate transcriptional units (monocistronic trpE vs. the trpGDC operon). There is no evidence for a single-protein TrpED fusion in this organism (molinahenares2009functionalanalysisof pages 2-4).
- **TrpF (PRAI)** and **TrpC (IGPS)** are encoded as **separate, non-fused proteins** on different loci (PP_1995 and PP_0422 respectively), in contrast to the bifunctional TrpC(F) fusion found in *E. coli* (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6).
- **TrpD** (anthranilate phosphoribosyltransferase) is a stand-alone enzyme encoded within the trpGDC operon; it is not fused to the glutaminase domain as it is in some enteric bacteria (kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 1-2).

## 4. Candidate Genes and Evidence

### 4.1 Core Tryptophan Biosynthesis Genes (High Confidence)

The following table provides detailed evidence for the seven core biosynthetic genes and the regulatory gene:

| Gene name | Locus tag (PP number) | UniProt ID | EC number | Enzymatic function | Pathway step | Evidence type (direct/homology) | Curation notes |
|---|---|---|---|---|---|---|---|
| trpE | PP_0417 | Q88QS1 | 4.1.3.27 | Anthranilate synthase component I (synthase subunit); converts chorismate toward anthranilate using ammonia supplied by TrpG | Chorismate → anthranilate | Direct in *P. putida* KT2440: mutant auxotrophy, insertion mapping, RT-PCR-defined transcription unit (molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6) | High-confidence core trp gene. Monocistronic transcription unit. Located in the PP_0417–PP_0422 trp region but separated from trpGDC by PP_0418-PP_0419. Candidate metadata assignment is correct. |
| trpG (often misannotated as pabA) | PP_0420 | Q88QR8 | 2.6.1.85 domain-level glutamine amidotransferase function within anthranilate synthase complex | Anthranilate synthase glutamine amidotransferase small subunit; supplies ammonia from glutamine to TrpE | Chorismate → anthranilate | Direct for pathway placement in KT2440 from operon structure and pathway reconstruction; assigned as trpG in KT2440 literature (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6) | Important curation issue: local metadata labels PP_0420 as **pabA**, but KT2440 literature identifies it as **trpG** in the **trpGDC operon**. Should be treated as the tryptophan-pathway amidotransferase here, not generic pABA synthase. Promote for full review. |
| trpD | PP_0421 | Q88QR7 | 2.4.2.18 | Anthranilate phosphoribosyltransferase | Anthranilate → N-(5'-phosphoribosyl)-anthranilate (PRA) | Direct in KT2440: auxotrophic mutant mapping, precursor-feeding phenotype, RT-PCR operon evidence, deletion engineering for anthranilate accumulation (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 4-6, kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5) | High-confidence core trp gene in trpGDC operon. Kuepper et al. deleted trpDC to accumulate anthranilate, functionally confirming role in downstream conversion of anthranilate. |
| trpC | PP_0422 | Q88QR6 | 4.1.1.48 | Indole-3-glycerol phosphate synthase | 1-(O-carboxyphenylamino)-1-deoxyribulose-5-phosphate → indole-3-glycerol phosphate | Direct in KT2440: auxotrophic mutant mapping, RT-PCR operon evidence, trpDC deletion engineering (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 4-6, kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5) | High-confidence core trp gene in trpGDC operon. Not fused to trpF in KT2440; should remain separate from generic fused TrpCF architectures. |
| trpF | PP_1995 | Q88LE0 | 5.3.1.24 | N-(5'-phosphoribosyl)anthranilate isomerase (PRAI) | PRA → CdRP / 1-(O-carboxyphenylamino)-1-deoxyribulose-5-phosphate | Direct in KT2440: targeted knockout gave tryptophan auxotrophy; RT-PCR consistent with monocistronic unit (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6) | High-confidence core trp gene. Unlinked monocistronic gene, flanked by truA and accD. Local brief listed PP_1995 correctly even though one Molina-Henares excerpt had a likely typo for locus number. |
| trpA | PP_0082 | Q88RP7 | 4.2.1.20 | Tryptophan synthase alpha chain; cleaves indole-3-glycerol phosphate to indole in the αβ complex | Indole-3-glycerol phosphate + L-serine → L-tryptophan | Direct in KT2440: auxotrophic mutant mapping, RT-PCR operon evidence; biosensor paper also supports assignment (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 4-6, matulis2022developmentandcharacterization pages 2-4) | High-confidence core trp gene. In trpAB operon, overlapping trpB by 1 nt. Terminal step should be curated as TrpA+TrpB complex, not independent full activity. |
| trpB | PP_0083 | Q88RP6 | 4.2.1.20 | Tryptophan synthase beta chain; condenses indole with L-serine to form L-tryptophan | Indole-3-glycerol phosphate + L-serine → L-tryptophan | Direct in KT2440 from operon organization and functional assignment; supported by biosensor/regulatory study (molinahenares2009functionalanalysisof pages 2-4, matulis2022developmentandcharacterization pages 2-4, molinahenares2009functionalanalysisof pages 4-6) | High-confidence core trp gene. In trpAB operon with trpA. Curate as obligate partner in tryptophan synthase complex rather than stand-alone terminal enzyme. |
| trpI | PP_0084 | not provided in candidate metadata; newer locus mapping PP_RS00430 reported | No EC (regulator) | LysR-family transcriptional regulator controlling trpAB expression in fluorescent pseudomonads | Regulation of terminal trp genes, not a catalytic biosynthetic step | Direct/strong species-transfer mix: KT2440 genomic organization and non-auxotrophic mutant noted; KT2440 biosensor study supports TrpI-regulated inducible system; mechanism inferred from Pseudomonas literature (molinahenares2009functionalanalysisof pages 2-4, matulis2022developmentandcharacterization pages 2-4, xie2003ancientoriginof pages 5-6) | Regulatory gene, not part of satisfiability for catalytic module steps. Divergently transcribed from trpAB. Distinct from *E. coli* TrpR-style regulation; should not be annotated as pathway enzyme. |


*Table: This table summarizes the experimentally supported tryptophan biosynthesis genes and regulator in *Pseudomonas putida* KT2440, mapping each to pathway step, operon context, and curation concerns. It is useful for deciding which candidate genes should satisfy module steps and which annotations, especially PP_0420/pabA vs trpG, need correction.*

### 4.2 Full Candidate Gene Assessment

The complete assessment of all 28 candidate genes from the local metadata is provided below, classifying each gene by its relevance to the core L-tryptophan biosynthesis module:

| Gene name | Locus tag | Function | Module step relevance | Recommended module status | Brief rationale |
|---|---|---|---|---|---|
| aroE__Q88RQ5 | PP_0074 | Shikimate dehydrogenase (AroE paralog) | shared shikimate pathway | candidate_uncertain | Upstream aromatic-pathway enzyme, not tryptophan-specific; KT2440 has multiple aroE-like paralogs, so assignment to the Trp-feeding route is uncertain without gene-level evidence (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| trpA | PP_0082 | Tryptophan synthase alpha chain | core trp biosynthesis | covered | Directly supported in KT2440 by auxotroph mapping and RT-PCR; part of trpAB operon for terminal tryptophan synthase step (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 4-6). |
| trpB | PP_0083 | Tryptophan synthase beta chain | core trp biosynthesis | covered | Directly supported in KT2440 as trpAB operon member; completes indole + serine condensation to tryptophan with TrpA (molinahenares2009functionalanalysisof pages 2-4, matulis2022developmentandcharacterization pages 2-4, molinahenares2009functionalanalysisof pages 4-6). |
| trpE | PP_0417 | Anthranilate synthase component I | core trp biosynthesis | covered | Direct experimental support in KT2440 from auxotroph analysis; monocistronic unit upstream of trpGDC cluster (molinahenares2009functionalanalysisof pages 1-2, molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6). |
| pabA | PP_0420 | Annotated aminodeoxychorismate synthase / glutamine amidotransferase | core trp biosynthesis | covered | Important curation issue: KT2440 literature identifies PP_0420 as trpG, the anthranilate synthase amidotransferase subunit in the trpGDC operon, not primarily a folate-pathway pabA assignment for this module (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6). |
| trpD | PP_0421 | Anthranilate phosphoribosyltransferase | core trp biosynthesis | covered | Directly supported by auxotroph mapping, precursor-feeding phenotype, and engineered trpDC deletion causing anthranilate accumulation (molinahenares2009functionalanalysisof pages 2-4, kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5, molinahenares2009functionalanalysisof pages 4-6). |
| trpC | PP_0422 | Indole-3-glycerol phosphate synthase | core trp biosynthesis | covered | Directly supported in KT2440 by mutant mapping and trpDC deletion experiments; part of trpGDC operon (molinahenares2009functionalanalysisof pages 2-4, kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5, molinahenares2009functionalanalysisof pages 4-6). |
| aroQ1 | PP_0560 | 3-dehydroquinate dehydratase 1 | shared shikimate pathway | candidate_uncertain | Shared upstream shikimate-step enzyme; multiple aroQ paralogs in KT2440 mean no single paralog can be confidently assigned as the module-satisfying copy from current evidence (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| hisC | PP_0967 | Histidinol-phosphate aminotransferase | not tryptophan-specific | not_expected_in_target_taxon | Histidine-pathway aminotransferase; not part of de novo tryptophan biosynthesis module in KT2440 (molinahenares2009functionalanalysisof pages 4-6). |
| pheA | PP_1769 | Chorismate mutase/prephenate dehydratase | phe-tyr branch | not_expected_in_target_taxon | Directs chorismate into phenylalanine branch, competing with trp flux; deletion used to increase anthranilate in KT2440, confirming it is neighboring but outside core trp module (kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5). |
| aroA | PP_1770 | EPSP synthase | shared shikimate pathway | covered | Canonical shared shikimate-pathway enzyme upstream of chorismate; relevant if pathway boundary includes chorismate supply, but not trp-specific (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| aroC | PP_1830 | Chorismate synthase | shared shikimate pathway | covered | Produces chorismate, the branch-point precursor for tryptophan; shared with phenylalanine/tyrosine and should be boundary-marked as upstream shared metabolism (molinahenares2009functionalanalysisof pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 2-4). |
| aroH | PP_1866 | DAHP synthase | shared shikimate pathway | candidate_uncertain | One of multiple DAHP synthase paralogs feeding the shikimate pathway; relevant only if module includes precursor supply, with paralog ambiguity unresolved here (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| tyrB | PP_1972 | Aromatic aminotransferase | phe-tyr branch | not_expected_in_target_taxon | Aromatic aminotransferase implicated in Phe/Tyr metabolism, not in core chorismate-to-tryptophan conversion; KT2440 also has aminotransferase redundancy (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 7-8). |
| trpF | PP_1995 | Phosphoribosylanthranilate isomerase | core trp biosynthesis | covered | Directly supported by targeted knockout causing tryptophan auxotrophy; monocistronic and unlinked from other trp genes (molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 4-6). |
| aroF-I | PP_2324 | DAHP synthase | shared shikimate pathway | candidate_uncertain | Shared entry-point enzyme for aromatic amino acid biosynthesis; one of several DAHP synthase paralogs in KT2440, so specific assignment to Trp-feeding flux is uncertain (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| aroE__Q88K85 | PP_2406 | Shikimate dehydrogenase (AroE paralog) | shared shikimate pathway | candidate_uncertain | Shared shikimate-pathway enzyme, but presence of multiple aroE-like genes creates paralog ambiguity for module curation (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| aroQ2 | PP_2407 | 3-dehydroquinate dehydratase 2 | shared shikimate pathway | candidate_uncertain | Shared upstream enzyme with paralog ambiguity; evidence supports pathway class but not unique assignment (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| quiC1 | PP_2554 | 3-dehydroshikimate dehydratase | catabolic | not_expected_in_target_taxon | Diverts 3-dehydroshikimate toward quinate/protocatechuate-related chemistry, not canonical chorismate/tryptophan biosynthesis; likely over-propagated from broad KEGG map (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| aroE__Q88IJ7 | PP_3002 | Shikimate dehydrogenase (AroE paralog) | shared shikimate pathway | candidate_uncertain | Another shikimate dehydrogenase-like paralog; likely relevant to aromatic precursor metabolism but uncertain as the principal biosynthetic copy for this module (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| aroQ-III | PP_3003 | 3-dehydroquinate dehydratase 3 | shared shikimate pathway | candidate_uncertain | Third aroQ-like gene; illustrates strong paralog ambiguity for early shikimate steps in KT2440 (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| aroF-II | PP_3080 | DAHP synthase | shared shikimate pathway | candidate_uncertain | Additional DAHP synthase paralog; candidate for chorismate supply but not tryptophan-specific and unresolved versus aroH/aroF-I (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| quiA | PP_3569 | Quinate dehydrogenase | catabolic | not_expected_in_target_taxon | Quinate-utilization enzyme associated with aromatic compound metabolism, not de novo tryptophan biosynthesis; should be excluded from core module satisfiability (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| amaC | PP_3590 | Aminotransferase | phe-tyr branch | not_expected_in_target_taxon | Second aromatic aminotransferase-like gene; aminotransferase redundancy in KT2440 relates to Phe/Tyr metabolism rather than core Trp pathway (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 7-8). |
| PP_3768 | PP_3768 | Putative shikimate 5-dehydrogenase | shared shikimate pathway | candidate_uncertain | Possible additional shikimate-pathway redox enzyme, but broad annotation and lack of direct evidence make this a weak module candidate (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| phhA | PP_4490 | Phenylalanine-4-hydroxylase | phe-tyr branch | not_expected_in_target_taxon | Functions in phenylalanine-to-tyrosine interconversion, not tryptophan biosynthesis; explicitly discussed as Phe/Tyr branch metabolism in KT2440 (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 2-4). |
| aroB | PP_5078 | 3-dehydroquinate synthase | shared shikimate pathway | covered | Core shared shikimate-pathway enzyme upstream of chorismate; highlighted as a bottleneck in KT2440 aromatic-pathway engineering, supporting functional relevance (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |
| aroK | PP_5079 | Shikimate kinase | shared shikimate pathway | covered | Canonical shared shikimate-pathway enzyme required for chorismate formation; relevant to precursor supply but not tryptophan-specific (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6). |


*Table: This table assesses all 28 local candidate genes for their specific relevance to the L-tryptophan biosynthesis module in Pseudomonas putida KT2440. It separates direct core trp genes from shared shikimate enzymes, neighboring phenylalanine/tyrosine branch genes, and likely over-annotated catabolic genes to support module curation.*

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Critical Annotation Issue: PP_0420 (pabA vs. trpG)

The most significant curation issue is the annotation of **PP_0420** as **pabA** (aminodeoxychorismate synthase component, EC 2.6.1.85) in the candidate metadata. The primary literature consistently identifies this gene as **trpG**, the glutamine amidotransferase (small subunit) component of anthranilate synthase, based on: (a) its position in the trpGDC operon confirmed by RT-PCR (molinahenares2009functionalanalysisof pages 2-4); (b) its functional context in tryptophan biosynthesis pathway reconstruction (molinahenares2009functionalanalysisof pages 4-6); and (c) its use as trpG in metabolic engineering constructs (trpES40F**G**) for anthranilate overproduction (kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 1-2). While the glutamine amidotransferase domains of TrpG and PabA are homologous (xie2003ancientoriginof pages 3-4), the operon context and functional studies in KT2440 strongly support assignment as **trpG** for the tryptophan module. Whether PP_0420 also contributes to folate (pABA) biosynthesis remains an open question, but its primary physiological role appears to be in tryptophan biosynthesis.

### 5.2 Paralog Ambiguity in Shared Shikimate Pathway

*P. putida* KT2440 harbors extensive paralog families for early shikimate pathway enzymes:

- **DAHP synthase**: Three paralogs (aroH/PP_1866, aroF-I/PP_2324, aroF-II/PP_3080). Feedback inhibition specificity by each aromatic amino acid is not individually resolved in the published KT2440 literature, although metabolic engineering studies have used heterologous feedback-resistant aroGD146N from *E. coli* to bypass native regulation (kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5, camposmagana2025combinatorialengineeringpinpoints pages 2-4).
- **3-Dehydroquinate dehydratase (aroQ)**: Three paralogs (aroQ1/PP_0560, aroQ2/PP_2407, aroQ-III/PP_3003), all type II DHQases.
- **Shikimate dehydrogenase (aroE)**: Three paralogs (PP_0074, PP_2406, PP_3002) plus a putative variant (PP_3768). The canonical biosynthetic aroE has not been definitively assigned among these paralogs in KT2440 specifically.

These paralogs create genuine uncertainty for module curation of the upstream shikimate pathway. However, since the tryptophan module boundary should be drawn at chorismate, this paralog ambiguity does not affect tryptophan module satisfiability.

### 5.3 Genes Likely Over-Propagated into the Module

Several candidate genes appear to be artifacts of the broad KEGG ppu00400 map rather than genuine tryptophan pathway components:

- **quiC1** (PP_2554, 3-dehydroshikimate dehydratase, EC 4.2.1.118): Diverts 3-dehydroshikimate toward protocatechuate; this is a catabolic/peripheral enzyme, not a biosynthetic shikimate pathway step.
- **quiA** (PP_3569, quinate dehydrogenase, EC 1.1.5.8): Part of quinate catabolism, not aromatic amino acid biosynthesis.
- **phhA** (PP_4490, phenylalanine-4-hydroxylase, EC 1.14.16.1): Converts phenylalanine to tyrosine; this is part of phenylalanine catabolism/tyrosine salvage, not tryptophan biosynthesis (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 2-4).
- **hisC** (PP_0967, histidinol-phosphate aminotransferase): Histidine pathway enzyme with no documented role in tryptophan biosynthesis.
- **tyrB** (PP_1972) and **amaC** (PP_3590): Aromatic aminotransferases involved in phenylalanine/tyrosine transamination. KT2440 has at least five enzymes with aromatic aminotransferase activity (molinahenares2009functionalanalysisof pages 6-7); none are required for the chorismate-to-tryptophan module.

### 5.4 Boundary Genes of Note

- **pheA** (PP_1769, chorismate mutase/prephenate dehydratase): Not part of tryptophan biosynthesis but a direct competitor for the chorismate precursor. Its deletion was used in KT2440 metabolic engineering to increase flux toward anthranilate/tryptophan (kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 3-5). It should be annotated as a neighboring pathway gene, not a tryptophan module member.
- **aroA** (PP_1770, EPSP synthase) and **aroC** (PP_1830, chorismate synthase): These are the final two steps producing chorismate. They are shared by all aromatic amino acid branches and should be assigned to the upstream shikimate/chorismate supply module, not the tryptophan-specific module.

## 6. Module and GO-Curation Recommendations

### 6.1 Module Step Status Summary

| Module step | Status | Gene(s) |
|---|---|---|
| Chorismate → anthranilate | **covered** | trpE (PP_0417) + trpG (PP_0420) |
| Anthranilate → PRA | **covered** | trpD (PP_0421) |
| PRA → CdRP | **covered** | trpF (PP_1995) |
| CdRP → I3GP | **covered** | trpC (PP_0422) |
| I3GP + Ser → Trp | **covered** | trpA (PP_0082) + trpB (PP_0083) |

**All catalytic steps are covered with direct experimental evidence from *P. putida* KT2440.** No gaps, no steps absent, and no lineage-specific alternatives are needed.

### 6.2 Recommended Annotation Corrections

1. **PP_0420 should be re-annotated as trpG** (or at minimum dual-annotated as trpG/pabA) for tryptophan module purposes. The current pabA annotation is misleading in the context of this module. The EC assignment of 2.6.1.85 (aminodeoxychorismate synthase) is incorrect for the tryptophan pathway context; the correct activity is the glutamine amidotransferase component of anthranilate synthase (part of EC 4.1.3.27).

2. **Upstream shikimate genes** (aroB, aroK, aroE, aroQ, aroA, aroC, aroH, aroF-I, aroF-II) should be separated into a distinct "chorismate biosynthesis" or "shikimate pathway" module, not bundled with the tryptophan-specific module.

3. **Remove from tryptophan module**: quiC1, quiA, phhA, hisC, tyrB, amaC, pheA, PP_3768 — these are either competing/neighboring pathways, catabolic enzymes, or unrelated aminotransferases.

### 6.3 GO Term Considerations

- The TrpE + TrpG complex should be annotated with GO:0004049 (anthranilate synthase activity) as a complex, not individual subunits.
- TrpI (PP_0084) should carry regulatory GO annotations (e.g., GO:0006355 — regulation of transcription, DNA-templated) but should not be tagged with any biosynthetic process GO term as a catalytic contributor.

## 7. Genes to Promote to Full Review

1. **PP_0420 (pabA/trpG)**: Highest priority for full review due to the annotation discrepancy between pabA and trpG. Needs resolution of whether this gene has dual physiological roles (both tryptophan and folate biosynthesis) or is primarily a trpG in KT2440.

2. **PP_0084 (trpI)**: Merits review as a regulatory component. The TrpI/I3GP-responsive system has been developed as a biosensor tool (matulis2022developmentandcharacterization pages 2-4), and understanding its regulatory scope would clarify whether it controls additional genes beyond trpAB.

3. **DAHP synthase paralogs** (PP_1866/aroH, PP_2324/aroF-I, PP_3080/aroF-II): If the upstream shikimate module is curated separately, these three paralogs need individual functional assignment to determine which is inhibited by tryptophan vs. phenylalanine vs. tyrosine in KT2440.

## 8. Key References

1. **Molina-Henares et al. (2009)** — "Functional analysis of aromatic biosynthetic pathways in *Pseudomonas putida* KT2440." *Microbial Biotechnology* 2:91–100. DOI: 10.1111/j.1751-7915.2008.00062.x. **Primary reference** for trp gene organization, auxotroph characterization, and operon analysis in KT2440 (molinahenares2009functionalanalysisof pages 4-6, molinahenares2009functionalanalysisof pages 2-4, molinahenares2009functionalanalysisof pages 1-2).

2. **Kuepper et al. (2015)** — "Metabolic engineering of *Pseudomonas putida* KT2440 to produce anthranilate from glucose." *Frontiers in Microbiology* 6:1310. DOI: 10.3389/fmicb.2015.01310. Functional confirmation of trpDC deletion and anthranilate accumulation (kuepper2015metabolicengineeringof pages 2-3, kuepper2015metabolicengineeringof pages 1-2, kuepper2015metabolicengineeringof pages 3-5).

3. **Matulis et al. (2022)** — "Development and characterization of indole-responsive whole-cell biosensor based on the inducible gene expression system from *Pseudomonas putida* KT2440." *International Journal of Molecular Sciences* 23:4649. DOI: 10.3390/ijms23094649. TrpI regulatory characterization and trpAB expression system (matulis2022developmentandcharacterization pages 2-4).

4. **Xie et al. (2003)** — "Ancient origin of the tryptophan operon and the dynamics of evolutionary change." *Microbiology and Molecular Biology Reviews* 67:303–342. DOI: 10.1128/mmbr.67.3.303-342.2003. Comprehensive review of trp operon evolution and nomenclature including *Pseudomonas* (xie2003ancientoriginof pages 3-4, xie2003ancientoriginof pages 5-6).

5. **Campos-Magaña et al. (2025)** — "Combinatorial engineering pinpoints shikimate pathway bottlenecks in para-aminobenzoic acid production in *Pseudomonas putida*." *Journal of Biological Engineering* 19. DOI: 10.1186/s13036-025-00553-5. Shikimate pathway gene characterization in KT2440 (camposmagana2025combinatorialengineeringpinpoints pages 2-4, camposmagana2025combinatorialengineeringpinpoints pages 4-6).

6. **Schmidt et al. (2022)** — "Nitrogen metabolism in *Pseudomonas putida*: Functional analysis using random barcode transposon sequencing." *Applied and Environmental Microbiology* 88. DOI: 10.1128/aem.02430-21. RB-TnSeq fitness data for amino acid biosynthesis genes (schmidt2022nitrogenmetabolismin pages 2-4).

7. **Eng et al. (2021)** — "Engineering *Pseudomonas putida* for efficient aromatic conversion to bioproduct using high throughput screening in a bioreactor." *Metabolic Engineering* 66:229–238. DOI: 10.1016/j.ymben.2021.04.015. Fitness data showing trp biosynthesis gene transposon mutants have decreased fitness under bioreactor conditions (eng2021engineeringpseudomonasputida pages 3-4).

8. **Yu et al. (2016)** — "Metabolic engineering of *Pseudomonas putida* KT2440 for the production of para-hydroxy benzoic acid." *Frontiers in Bioengineering and Biotechnology* 4:90. DOI: 10.3389/fbioe.2016.00090. Confirms trpE as a competing chorismate-consuming branch via deletion strategy.

9. **Essar et al. (1990)** — "DNA sequences and characterization of four early genes of the tryptophan pathway in *Pseudomonas aeruginosa*" and companion paper on "*P. putida* trpE and trpGDC." *Journal of Bacteriology* 172:853–866, 867–883. Foundational characterization of *Pseudomonas* trp gene sequences (molinahenares2009functionalanalysisof pages 9-10, molinahenares2009functionalanalysisof pages 4-6).

References

1. (molinahenares2009functionalanalysisof pages 2-4): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

2. (molinahenares2009functionalanalysisof pages 1-2): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

3. (molinahenares2009functionalanalysisof pages 4-6): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

4. (molinahenares2009functionalanalysisof pages 6-7): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

5. (kuepper2015metabolicengineeringof pages 2-3): Jannis Kuepper, Jasmin Dickler, Michael Biggel, Swantje Behnken, Gernot Jäger, Nick Wierckx, and Lars M. Blank. Metabolic engineering of pseudomonas putida kt2440 to produce anthranilate from glucose. Frontiers in Microbiology, Nov 2015. URL: https://doi.org/10.3389/fmicb.2015.01310, doi:10.3389/fmicb.2015.01310. This article has 66 citations and is from a peer-reviewed journal.

6. (kuepper2015metabolicengineeringof pages 3-5): Jannis Kuepper, Jasmin Dickler, Michael Biggel, Swantje Behnken, Gernot Jäger, Nick Wierckx, and Lars M. Blank. Metabolic engineering of pseudomonas putida kt2440 to produce anthranilate from glucose. Frontiers in Microbiology, Nov 2015. URL: https://doi.org/10.3389/fmicb.2015.01310, doi:10.3389/fmicb.2015.01310. This article has 66 citations and is from a peer-reviewed journal.

7. (xie2003ancientoriginof pages 5-6): Gary Xie, Nemat O. Keyhani, Carol A. Bonner, and Roy A. Jensen. Ancient origin of the tryptophan operon and the dynamics of evolutionary change. Microbiology and Molecular Biology Reviews, 67:303-342, Sep 2003. URL: https://doi.org/10.1128/mmbr.67.3.303-342.2003, doi:10.1128/mmbr.67.3.303-342.2003. This article has 191 citations and is from a domain leading peer-reviewed journal.

8. (matulis2022developmentandcharacterization pages 2-4): Paulius Matulis, Ingrida Kutraite, Ernesta Augustiniene, Egle Valanciene, Ilona Jonuskiene, and Naglis Malys. Development and characterization of indole-responsive whole-cell biosensor based on the inducible gene expression system from pseudomonas putida kt2440. International Journal of Molecular Sciences, 23:4649, Apr 2022. URL: https://doi.org/10.3390/ijms23094649, doi:10.3390/ijms23094649. This article has 8 citations.

9. (kuepper2015metabolicengineeringof pages 1-2): Jannis Kuepper, Jasmin Dickler, Michael Biggel, Swantje Behnken, Gernot Jäger, Nick Wierckx, and Lars M. Blank. Metabolic engineering of pseudomonas putida kt2440 to produce anthranilate from glucose. Frontiers in Microbiology, Nov 2015. URL: https://doi.org/10.3389/fmicb.2015.01310, doi:10.3389/fmicb.2015.01310. This article has 66 citations and is from a peer-reviewed journal.

10. (camposmagana2025combinatorialengineeringpinpoints pages 2-4): Marco A Campos-Magaña, Sara Moreno-Paz, Maria Martin-Pascual, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering pinpoints shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. Journal of Biological Engineering, Sep 2025. URL: https://doi.org/10.1186/s13036-025-00553-5, doi:10.1186/s13036-025-00553-5. This article has 0 citations and is from a peer-reviewed journal.

11. (camposmagana2025combinatorialengineeringpinpoints pages 4-6): Marco A Campos-Magaña, Sara Moreno-Paz, Maria Martin-Pascual, Vitor AP Martins dos Santos, Luis Garcia-Morales, and Maria Suarez-Diez. Combinatorial engineering pinpoints shikimate pathway bottlenecks in para-aminobenzoic acid production in pseudomonas putida. Journal of Biological Engineering, Sep 2025. URL: https://doi.org/10.1186/s13036-025-00553-5, doi:10.1186/s13036-025-00553-5. This article has 0 citations and is from a peer-reviewed journal.

12. (molinahenares2009functionalanalysisof pages 7-8): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

13. (xie2003ancientoriginof pages 3-4): Gary Xie, Nemat O. Keyhani, Carol A. Bonner, and Roy A. Jensen. Ancient origin of the tryptophan operon and the dynamics of evolutionary change. Microbiology and Molecular Biology Reviews, 67:303-342, Sep 2003. URL: https://doi.org/10.1128/mmbr.67.3.303-342.2003, doi:10.1128/mmbr.67.3.303-342.2003. This article has 191 citations and is from a domain leading peer-reviewed journal.

14. (schmidt2022nitrogenmetabolismin pages 2-4): Matthias Schmidt, Allison N. Pearson, Matthew R. Incha, Mitchell G. Thompson, Edward E. K. Baidoo, Ramu Kakumanu, Aindrila Mukhopadhyay, Patrick M. Shih, Adam M. Deutschbauer, Lars M. Blank, and Jay D. Keasling. Nitrogen metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Applied and Environmental Microbiology, Apr 2022. URL: https://doi.org/10.1128/aem.02430-21, doi:10.1128/aem.02430-21. This article has 36 citations and is from a peer-reviewed journal.

15. (eng2021engineeringpseudomonasputida pages 3-4): Thomas Eng, Deepanwita Banerjee, Andrew K. Lau, Emily Bowden, Robin A. Herbert, Jessica Trinh, Jan-Philip Prahl, Adam Deutschbauer, Deepti Tanjore, and Aindrila Mukhopadhyay. Engineering pseudomonas putida for efficient aromatic conversion to bioproduct using high throughput screening in a bioreactor. Metabolic Engineering, 66:229-238, Jul 2021. URL: https://doi.org/10.1016/j.ymben.2021.04.015, doi:10.1016/j.ymben.2021.04.015. This article has 49 citations and is from a domain leading peer-reviewed journal.

16. (molinahenares2009functionalanalysisof pages 9-10): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. molinahenares2009functionalanalysisof pages 2-4
2. xie2003ancientoriginof pages 5-6
3. molinahenares2009functionalanalysisof pages 4-6
4. xie2003ancientoriginof pages 3-4
5. molinahenares2009functionalanalysisof pages 6-7
6. matulis2022developmentandcharacterization pages 2-4
7. schmidt2022nitrogenmetabolismin pages 2-4
8. eng2021engineeringpseudomonasputida pages 3-4
9. molinahenares2009functionalanalysisof pages 1-2
10. kuepper2015metabolicengineeringof pages 2-3
11. kuepper2015metabolicengineeringof pages 3-5
12. kuepper2015metabolicengineeringof pages 1-2
13. camposmagana2025combinatorialengineeringpinpoints pages 2-4
14. camposmagana2025combinatorialengineeringpinpoints pages 4-6
15. molinahenares2009functionalanalysisof pages 7-8
16. molinahenares2009functionalanalysisof pages 9-10
17. https://doi.org/10.1111/j.1751-7915.2008.00062.x,
18. https://doi.org/10.3389/fmicb.2015.01310,
19. https://doi.org/10.1128/mmbr.67.3.303-342.2003,
20. https://doi.org/10.3390/ijms23094649,
21. https://doi.org/10.1186/s13036-025-00553-5,
22. https://doi.org/10.1128/aem.02430-21,
23. https://doi.org/10.1016/j.ymben.2021.04.015,