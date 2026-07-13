---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T02:40:43.711209'
end_time: '2026-07-07T03:06:39.945233'
duration_seconds: 1556.23
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Riboflavin biosynthesis
  module_summary: A bacterial riboflavin, FMN, and FAD biosynthesis module covering
    conversion of GTP and ribulose 5-phosphate into riboflavin, followed by phosphorylation
    and adenylylation to the major flavin cofactors. In Pseudomonas putida KT2440,
    KEGG ppu00740 also includes FMN-dependent side chemistry and broad flavin metabolism
    entries; those are treated as boundary context unless they directly catalyze riboflavin,
    FMN, or FAD formation.
  module_outline: "- Riboflavin biosynthesis\n  - 1. GTP-derived pyrimidine precursor\
    \ formation\n  - GTP cyclohydrolase II step\n    - RibA GTP cyclohydrolase II\
    \ (molecular player: PSEPK ribA; activity or role: GTP cyclohydrolase II activity)\n\
    \    - RibAB-I GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-I;\
    \ activity or role: GTP cyclohydrolase II activity)\n    - RibAB-II GTP cyclohydrolase\
    \ II candidate (molecular player: PSEPK ribAB-II; activity or role: GTP cyclohydrolase\
    \ II activity)\n  - 2. pyrimidine deamination and reduction\n  - RibD deaminase\
    \ and reductase steps\n    - RibD riboflavin-specific deaminase (molecular player:\
    \ PSEPK ribD; activity or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase\
    \ activity)\n    - RibD riboflavin-pathway reductase (molecular player: PSEPK\
    \ ribD; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil reductase activity)\n\
    \  - 3. ribulose-phosphate branch\n  - DHBP synthase step\n    - RibB DHBP synthase\
    \ (molecular player: PSEPK ribB; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate\
    \ synthase activity)\n    - RibAB-I DHBP synthase (molecular player: PSEPK ribAB-I;\
    \ activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)\n\
    \    - RibAB-II DHBP synthase (molecular player: PSEPK ribAB-II; activity or role:\
    \ 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)\n  - 4. lumazine formation\n\
    \  - Lumazine synthase step\n    - RibH lumazine synthase (molecular player: PSEPK\
    \ ribH; activity or role: 6,7-dimethyl-8-ribityllumazine synthase activity)\n\
    \  - 5. riboflavin formation\n  - Riboflavin synthase step\n    - RibE riboflavin\
    \ synthase (molecular player: PSEPK ribE; activity or role: riboflavin synthase\
    \ activity)\n    - RibC riboflavin synthase candidate (molecular player: PSEPK\
    \ ribC; activity or role: riboflavin synthase activity)\n  - 6. FMN and FAD formation\n\
    \  - Riboflavin phosphorylation and FMN adenylylation\n    - RibF riboflavin kinase\
    \ (molecular player: PSEPK ribF; activity or role: riboflavin kinase activity)\n\
    \    - RibF FMN adenylyltransferase (molecular player: PSEPK ribF; activity or\
    \ role: FMN adenylyltransferase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00740
  pathway_id: ppu00740
  pathway_name: Riboflavin metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00740 with 14 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '15'
  candidate_genes: '- ssuE: PP_0236 | Q88R97 | FMN reductase (NADPH) (EC 1.5.1.38)
    (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)

    - ribD: PP_0514 | Q88QH9 | Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine
    deaminase (DRAP deaminase) (EC 3.5.4.26) (Riboflavin-specific deaminase); 5-amino-6-(5-phosphoribosylamino)uracil
    reductase (EC 1.1.1.193) (HTP reductase)] (EC 1.1.1.193; 3.5.4.26; primary bucket
    kegg:ppu00740)

    - ribE: PP_0515 | Q88QH8 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary
    bucket kegg:ppu00740)

    - ribAB-I: PP_0516 | Q88QH7 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - ribH: PP_0517 | Q88QH6 | 6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase)
    (LS) (Lumazine synthase) (EC 2.5.1.78) (EC 2.5.1.78; primary bucket kegg:ppu00740)

    - ribA: PP_0522 | Q88QH1 | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase
    II) (EC 3.5.4.25; primary bucket kegg:ppu00740)

    - ribB: PP_0530 | Q88QG4 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129;
    primary bucket kegg:ppu00627)

    - ribF: PP_0602 | Q88Q93 | Riboflavin biosynthesis protein [Includes: Riboflavin
    kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2.7.7.2) (FAD
    pyrophosphorylase) (FAD synthase)] (EC 2.7.1.26; 2.7.7.2; primary bucket kegg:ppu00740)

    - bluB: PP_1674 | Q88MA0 | 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79)
    (EC 1.13.11.79; primary bucket kegg:ppu00740)

    - msuE: PP_2764 | Q88J85 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase)
    (EC 1.5.1.38; primary bucket kegg:ppu00740)

    - ribC: PP_2916 | Q88IT3 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary
    bucket kegg:ppu00740)

    - ribAB-II: PP_3813 | Q88GB1 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - nudF: PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose
    diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphoribose pyrophosphatase)
    (EC 3.6.1.13; primary bucket kegg:ppu00740)

    - had: PP_5231 | Q88CF0 | (S)-2-haloacid dehalogenase (EC 3.8.1.-) (EC 3.8.1.-;
    primary bucket kegg:ppu00740)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Riboflavin biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00740
- Resolved ID: ppu00740
- Resolved name: Riboflavin metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00740 with 14 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 15

- ssuE: PP_0236 | Q88R97 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- ribD: PP_0514 | Q88QH9 | Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine deaminase (DRAP deaminase) (EC 3.5.4.26) (Riboflavin-specific deaminase); 5-amino-6-(5-phosphoribosylamino)uracil reductase (EC 1.1.1.193) (HTP reductase)] (EC 1.1.1.193; 3.5.4.26; primary bucket kegg:ppu00740)
- ribE: PP_0515 | Q88QH8 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary bucket kegg:ppu00740)
- ribAB-I: PP_0516 | Q88QH7 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- ribH: PP_0517 | Q88QH6 | 6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase) (LS) (Lumazine synthase) (EC 2.5.1.78) (EC 2.5.1.78; primary bucket kegg:ppu00740)
- ribA: PP_0522 | Q88QH1 | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II) (EC 3.5.4.25; primary bucket kegg:ppu00740)
- ribB: PP_0530 | Q88QG4 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- ribF: PP_0602 | Q88Q93 | Riboflavin biosynthesis protein [Includes: Riboflavin kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2.7.7.2) (FAD pyrophosphorylase) (FAD synthase)] (EC 2.7.1.26; 2.7.7.2; primary bucket kegg:ppu00740)
- bluB: PP_1674 | Q88MA0 | 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79) (EC 1.13.11.79; primary bucket kegg:ppu00740)
- msuE: PP_2764 | Q88J85 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- ribC: PP_2916 | Q88IT3 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary bucket kegg:ppu00740)
- ribAB-II: PP_3813 | Q88GB1 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- nudF: PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphoribose pyrophosphatase) (EC 3.6.1.13; primary bucket kegg:ppu00740)
- had: PP_5231 | Q88CF0 | (S)-2-haloacid dehalogenase (EC 3.8.1.-) (EC 3.8.1.-; primary bucket kegg:ppu00740)

## Generic Module Context

### Working Scope

A bacterial riboflavin, FMN, and FAD biosynthesis module covering conversion of GTP and ribulose 5-phosphate into riboflavin, followed by phosphorylation and adenylylation to the major flavin cofactors. In Pseudomonas putida KT2440, KEGG ppu00740 also includes FMN-dependent side chemistry and broad flavin metabolism entries; those are treated as boundary context unless they directly catalyze riboflavin, FMN, or FAD formation.

### Provisional Biological Outline

- Riboflavin biosynthesis
  - 1. GTP-derived pyrimidine precursor formation
  - GTP cyclohydrolase II step
    - RibA GTP cyclohydrolase II (molecular player: PSEPK ribA; activity or role: GTP cyclohydrolase II activity)
    - RibAB-I GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-I; activity or role: GTP cyclohydrolase II activity)
    - RibAB-II GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-II; activity or role: GTP cyclohydrolase II activity)
  - 2. pyrimidine deamination and reduction
  - RibD deaminase and reductase steps
    - RibD riboflavin-specific deaminase (molecular player: PSEPK ribD; activity or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase activity)
    - RibD riboflavin-pathway reductase (molecular player: PSEPK ribD; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil reductase activity)
  - 3. ribulose-phosphate branch
  - DHBP synthase step
    - RibB DHBP synthase (molecular player: PSEPK ribB; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-I DHBP synthase (molecular player: PSEPK ribAB-I; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-II DHBP synthase (molecular player: PSEPK ribAB-II; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
  - 4. lumazine formation
  - Lumazine synthase step
    - RibH lumazine synthase (molecular player: PSEPK ribH; activity or role: 6,7-dimethyl-8-ribityllumazine synthase activity)
  - 5. riboflavin formation
  - Riboflavin synthase step
    - RibE riboflavin synthase (molecular player: PSEPK ribE; activity or role: riboflavin synthase activity)
    - RibC riboflavin synthase candidate (molecular player: PSEPK ribC; activity or role: riboflavin synthase activity)
  - 6. FMN and FAD formation
  - Riboflavin phosphorylation and FMN adenylylation
    - RibF riboflavin kinase (molecular player: PSEPK ribF; activity or role: riboflavin kinase activity)
    - RibF FMN adenylyltransferase (molecular player: PSEPK ribF; activity or role: FMN adenylyltransferase activity)

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

Riboflavin biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00740
- Resolved ID: ppu00740
- Resolved name: Riboflavin metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00740 with 14 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 15

- ssuE: PP_0236 | Q88R97 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- ribD: PP_0514 | Q88QH9 | Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine deaminase (DRAP deaminase) (EC 3.5.4.26) (Riboflavin-specific deaminase); 5-amino-6-(5-phosphoribosylamino)uracil reductase (EC 1.1.1.193) (HTP reductase)] (EC 1.1.1.193; 3.5.4.26; primary bucket kegg:ppu00740)
- ribE: PP_0515 | Q88QH8 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary bucket kegg:ppu00740)
- ribAB-I: PP_0516 | Q88QH7 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- ribH: PP_0517 | Q88QH6 | 6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase) (LS) (Lumazine synthase) (EC 2.5.1.78) (EC 2.5.1.78; primary bucket kegg:ppu00740)
- ribA: PP_0522 | Q88QH1 | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II) (EC 3.5.4.25; primary bucket kegg:ppu00740)
- ribB: PP_0530 | Q88QG4 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- ribF: PP_0602 | Q88Q93 | Riboflavin biosynthesis protein [Includes: Riboflavin kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2.7.7.2) (FAD pyrophosphorylase) (FAD synthase)] (EC 2.7.1.26; 2.7.7.2; primary bucket kegg:ppu00740)
- bluB: PP_1674 | Q88MA0 | 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79) (EC 1.13.11.79; primary bucket kegg:ppu00740)
- msuE: PP_2764 | Q88J85 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- ribC: PP_2916 | Q88IT3 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary bucket kegg:ppu00740)
- ribAB-II: PP_3813 | Q88GB1 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- nudF: PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphoribose pyrophosphatase) (EC 3.6.1.13; primary bucket kegg:ppu00740)
- had: PP_5231 | Q88CF0 | (S)-2-haloacid dehalogenase (EC 3.8.1.-) (EC 3.8.1.-; primary bucket kegg:ppu00740)

## Generic Module Context

### Working Scope

A bacterial riboflavin, FMN, and FAD biosynthesis module covering conversion of GTP and ribulose 5-phosphate into riboflavin, followed by phosphorylation and adenylylation to the major flavin cofactors. In Pseudomonas putida KT2440, KEGG ppu00740 also includes FMN-dependent side chemistry and broad flavin metabolism entries; those are treated as boundary context unless they directly catalyze riboflavin, FMN, or FAD formation.

### Provisional Biological Outline

- Riboflavin biosynthesis
  - 1. GTP-derived pyrimidine precursor formation
  - GTP cyclohydrolase II step
    - RibA GTP cyclohydrolase II (molecular player: PSEPK ribA; activity or role: GTP cyclohydrolase II activity)
    - RibAB-I GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-I; activity or role: GTP cyclohydrolase II activity)
    - RibAB-II GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-II; activity or role: GTP cyclohydrolase II activity)
  - 2. pyrimidine deamination and reduction
  - RibD deaminase and reductase steps
    - RibD riboflavin-specific deaminase (molecular player: PSEPK ribD; activity or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase activity)
    - RibD riboflavin-pathway reductase (molecular player: PSEPK ribD; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil reductase activity)
  - 3. ribulose-phosphate branch
  - DHBP synthase step
    - RibB DHBP synthase (molecular player: PSEPK ribB; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-I DHBP synthase (molecular player: PSEPK ribAB-I; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-II DHBP synthase (molecular player: PSEPK ribAB-II; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
  - 4. lumazine formation
  - Lumazine synthase step
    - RibH lumazine synthase (molecular player: PSEPK ribH; activity or role: 6,7-dimethyl-8-ribityllumazine synthase activity)
  - 5. riboflavin formation
  - Riboflavin synthase step
    - RibE riboflavin synthase (molecular player: PSEPK ribE; activity or role: riboflavin synthase activity)
    - RibC riboflavin synthase candidate (molecular player: PSEPK ribC; activity or role: riboflavin synthase activity)
  - 6. FMN and FAD formation
  - Riboflavin phosphorylation and FMN adenylylation
    - RibF riboflavin kinase (molecular player: PSEPK ribF; activity or role: riboflavin kinase activity)
    - RibF FMN adenylyltransferase (molecular player: PSEPK ribF; activity or role: FMN adenylyltransferase activity)

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

# Riboflavin Biosynthesis in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 (NCBI Taxon 160488) encodes a complete riboflavin, FMN, and FAD biosynthetic pathway. The core pathway from GTP and ribulose-5-phosphate to riboflavin, and thence to FMN and FAD, is fully satisfiable by seven high-confidence genes. However, a critical curation issue pervades the candidate gene list: **two genes annotated as bifunctional ribBA (DHBP synthase / GTP cyclohydrolase II) — PP_0516 (ribAB-I) and PP_3813 (ribAB-II) — are actually ribBX variants that lack GTP cyclohydrolase II activity** (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8). This misannotation, documented experimentally for PP_0516 and PP_3813 by Brutinel et al. (2013), affects approximately 40% of annotated ribBA genes across Proteobacteria and represents the most significant annotation error in this module. The true GTP cyclohydrolase II is encoded by the monofunctional ribA gene (PP_0522). Of the 15 candidate genes assigned to KEGG ppu00740, only 8 are core riboflavin/FMN/FAD biosynthesis enzymes; 6 are boundary genes belonging to adjacent pathways (sulfur metabolism, cobalamin biosynthesis, ubiquinone biosynthesis, or general nucleotide housekeeping), and 1 (had, PP_5231) has no clear biochemical connection to riboflavin metabolism.

## 2. Target-Organism Pathway Definition

**Pathway scope.** The riboflavin biosynthesis module in *P. putida* KT2440 encompasses the de novo conversion of one molecule of GTP and two molecules of ribulose-5-phosphate into one molecule of riboflavin, followed by its sequential phosphorylation to FMN and adenylylation to FAD (jimeneznava2026biosynthesisregulationand pages 19-20, abbas2011geneticcontrolof pages 1-2, jimeneznava2026biosynthesisregulationand pages 4-6). This corresponds to KEGG module M00125 (riboflavin biosynthesis) and the FMN/FAD formation steps within KEGG ppu00740.

**Neighboring pathways to keep separate.** The following should be treated as boundary context, not core module steps:
- **Cobalamin (B12) biosynthesis**: BluB (PP_1674) catalyzes the oxygen-dependent fragmentation of FMN to produce 5,6-dimethylbenzimidazole (DMB), the lower ligand of vitamin B12 (abbas2011geneticcontrolof pages 6-7, deptula2015blubcobt2fusionenzyme pages 1-2). While BluB uses FMN as substrate, this reaction belongs to the cobalamin pathway.
- **Ubiquinone biosynthesis**: UbiX (PP_0548) is a flavin prenyltransferase that converts FMN to prenylated FMN (prFMN), a novel cofactor required by UbiD-family decarboxylases in ubiquinone and related pathways (weber2017requirementofa pages 18-20, lin2015isofunctionalenzymespad1 pages 1-2).
- **Sulfur metabolism**: SsuE (PP_0236) and MsuE (PP_2764) are NADPH-dependent FMN reductases that provide FMNH₂ to two-component monooxygenase systems for alkanesulfonate and methanesulfonate desulfonation, respectively (kahnert2000thessulocus pages 3-4, kahnert2000thessulocus pages 8-8, kahnert2000thessulocus pages 1-1).
- **Nucleotide housekeeping**: NudF (PP_4919), an ADP-ribose pyrophosphatase of the Nudix superfamily, catalyzes hydrolysis of ADP-ribose and has no direct role in riboflavin or flavin cofactor formation.

**Alternate names and database definitions.** KEGG ppu00740 is labeled "Riboflavin metabolism" and includes both de novo biosynthesis and broader flavin-utilizing enzymes. MetaCyc pathway PWY-6168 ("Flavin Biosynthesis I — bacteria and plants") more precisely defines the core biosynthetic module.

## 3. Expected Step Model

The riboflavin, FMN, and FAD biosynthesis pathway in *P. putida* KT2440 proceeds through the following enzymatic steps. In Gram-negative bacteria, the standard nomenclature uses ribA (GTP cyclohydrolase II), ribB (DHBP synthase), ribD (bifunctional deaminase/reductase), ribH (lumazine synthase), ribE (riboflavin synthase), and ribF (bifunctional riboflavin kinase/FMN adenylyltransferase) (jimeneznava2026biosynthesisregulationand pages 19-20, brutinel2013descriptionofa pages 3-4).

**Gene organization.** Comparative genomics indicates that *P. putida* maintains a conserved riboflavin operon with the structure **ybaD–ribD–ribE2–ribBA(ribBX)–ribH–nusB**, plus additional single-copy genes including **ribA** (or ribBA), **ribE**, and **ribB** at separate chromosomal loci (vitreschak2002regulationofriboflavin pages 3-4). The RFN (FMN riboswitch) element regulates the single ribB gene in Pseudomonas species, providing translational control in response to flavin levels (vitreschak2002regulationofriboflavin pages 8-10, vitreschak2002regulationofriboflavin pages 6-8).

The following table summarizes the module step satisfiability assessment:

| Step Number | Step Name | Expected Enzyme/Activity | Gene(s) Covering Step | Status | Confidence Level | Notes |
|---|---|---|---|---|---|---|
| 1 | GTP cyclohydrolase II (GTP → DARPP) | GTP cyclohydrolase II, EC 3.5.4.25 | **ribA** (PP_0522) | covered | high | Best-supported true step 1 enzyme in KT2440. **ribAB-I/PP_0516** and **ribAB-II/PP_3813** are ribBX-like proteins that lack GTP cyclohydrolase II activity despite common ribBA-style annotation; they should **not** be used to satisfy this step (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8, brutinel2013descriptionofa pages 5-6, vitreschak2002regulationofriboflavin pages 3-4) |
| 2 | Pyrimidine deamination and reduction (DARPP → ArPP → ArP) | Bifunctional deaminase/reductase, EC 3.5.4.26 + EC 1.1.1.193 | **ribD** (PP_0514) | covered | high | Canonical Gram-negative riboflavin-pathway enzyme for the deamination/reduction segment; present in the conserved Pseudomonas riboflavin gene cluster (jimeneznava2026biosynthesisregulationand pages 19-20, vitreschak2002regulationofriboflavin pages 3-4) |
| 3 | DHBP synthase (Ru5P → DHBP) | 3,4-dihydroxy-2-butanone 4-phosphate synthase, EC 4.1.99.12 | **ribB** (PP_0530); **ribAB-I/ribBX** NTD (PP_0516); **ribAB-II/ribBX** NTD (PP_3813) | covered | high | Step is multiply covered. PP_0516 and PP_3813 retain DHBP synthase activity through their N-terminal domains even though their C-terminal domains are not functional GTP cyclohydrolase II enzymes (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8, brutinel2013descriptionofa pages 5-6, brutinel2013descriptionofa pages 8-9) |
| 4 | Lumazine synthase (DHBP + ArP → DMRL) | 6,7-dimethyl-8-ribityllumazine synthase, EC 2.5.1.78 | **ribH** (PP_0517) | covered | high | Canonical lumazine synthase in the main riboflavin operon architecture reported for Pseudomonas (jimeneznava2026biosynthesisregulationand pages 19-20, vitreschak2002regulationofriboflavin pages 3-4) |
| 5 | Riboflavin synthase (2 DMRL → RF + ArP) | Riboflavin synthase, EC 2.5.1.9 | **ribE** (PP_0515); **ribC** (PP_2916) | covered | high | The operon-associated **ribE/PP_0515** is the strongest default assignment; **ribC/PP_2916** is a plausible paralog/redundant copy. Presence of ribE paralogy is consistent with proteobacterial gene organization summaries (vitreschak2002regulationofriboflavin pages 3-4, vitreschak2002regulationofriboflavin pages 8-10) |
| 6a | Riboflavin kinase (RF → FMN) | Riboflavin kinase, EC 2.7.1.26 | **ribF** (PP_0602) | covered | high | In Gram-negative bacteria, ribF encodes the bifunctional enzyme carrying the RF kinase activity needed for FMN formation (jimeneznava2026biosynthesisregulationand pages 19-20) |
| 6b | FMN adenylyltransferase (FMN → FAD) | FMN adenylyltransferase / FAD synthase, EC 2.7.7.2 | **ribF** (PP_0602) | covered | high | Same bifunctional **ribF** gene covers the FAD-forming step in Gram-negative bacteria (jimeneznava2026biosynthesisregulationand pages 19-20) |
| 7 | Deformylation step (AFRPP → DARoPP) | Formamidase-like deformylation activity or equivalent RibD-handled chemistry | No dedicated **brbF**-like candidate identified in KT2440; likely handled by standard **ribD**-centered pathway logic | candidate_uncertain | low | A dedicated BrbF-type formamidase has been discovered in some bacteria, but no clear KT2440 homolog is established from the current candidate set. For KT2440, the classical RibD-centered route remains the most likely explanation; this step should be flagged for curation attention rather than marked absent with high confidence (yurgel2022anovelformamidase pages 1-3, yurgel2022anovelformamidase pages 3-4, yurgel2022anovelformamidase pages 4-7, jimeneznava2026biosynthesisregulationand pages 19-20) |


*Table: This table summarizes which enzymatic steps of riboflavin, FMN, and FAD biosynthesis are satisfied in Pseudomonas putida KT2440 and which require curation caution. It is especially useful for distinguishing true step coverage from over-propagated ribBA/ribBX annotations.*

## 4. Candidate Genes and Evidence

The complete assessment of all 15 candidate genes mapped to KEGG ppu00740 is presented below:

| Gene Name | Locus Tag | UniProt ID | Annotated Function / EC | Pathway Role Assessment | Evidence Type | Module Step Status | Key Notes / Caveats |
|---|---|---|---|---|---|---|---|
| ssuE | PP_0236 | Q88R97 | FMN reductase (NADPH), EC 1.5.1.38 | boundary-adjacent pathway | homology-based; related Pseudomonas experimental literature | boundary_context | Sulfur-scavenging flavin reductase of the ssu desulfonation system; uses FMN as cosubstrate source, not a riboflavin/FM N/FAD biosynthetic step (kahnert2000thessulocus pages 3-4, kahnert2000thessulocus pages 8-8, maren2001sulfateesterutilization pages 52-57) |
| ribD | PP_0514 | Q88QH9 | Diaminohydroxyphosphoribosylaminopyrimidine deaminase / 5-amino-6-(5-phosphoribosylamino)uracil reductase, EC 3.5.4.26 + 1.1.1.193 | core riboflavin biosynthesis | homology-based; operon-context; pathway-conserved | covered | Canonical bifunctional step 2 enzyme in Gram-negative bacteria; located in conserved Pseudomonas riboflavin operon context (jimeneznava2026biosynthesisregulationand pages 19-20, vitreschak2002regulationofriboflavin pages 3-4) |
| ribE | PP_0515 | Q88QH8 | Riboflavin synthase, EC 2.5.1.9 | core riboflavin biosynthesis | homology-based; operon-context | covered | Likely the operon-associated ribE2-type riboflavin synthase in the conserved ybaD-ribD-ribE2-ribBA-ribH-nusB cluster; high-confidence step 5 gene (vitreschak2002regulationofriboflavin pages 3-4) |
| ribAB-I | PP_0516 | Q88QH7 | Annotated 3,4-dihydroxy-2-butanone 4-phosphate synthase; often misannotated as bifunctional ribBA, EC 4.1.99.12 only | core riboflavin biosynthesis | direct experimental in P. putida / proteobacterial ribBX study | over-propagated annotation | Critical curation point: PP_0516 is ribBX, not true bifunctional ribBA. Has DHBP synthase activity but lacks GTP cyclohydrolase II catalytic residues/activity; CTD is regulatory/noncanonical (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8, brutinel2013descriptionofa pages 5-6) |
| ribH | PP_0517 | Q88QH6 | 6,7-dimethyl-8-ribityllumazine synthase, EC 2.5.1.78 | core riboflavin biosynthesis | homology-based; operon-context | covered | Canonical lumazine synthase for step 4; located in conserved riboflavin operon neighborhood in Pseudomonas (jimeneznava2026biosynthesisregulationand pages 19-20, vitreschak2002regulationofriboflavin pages 3-4) |
| ribA | PP_0522 | Q88QH1 | GTP cyclohydrolase II, EC 3.5.4.25 | core riboflavin biosynthesis | homology-based; comparative genomics | covered | Best candidate for the true step 1 GTP cyclohydrolase II in KT2440; required because ribBX paralogs lack this activity (jimeneznava2026biosynthesisregulationand pages 19-20, brutinel2013descriptionofa pages 5-6, vitreschak2002regulationofriboflavin pages 3-4) |
| ribB | PP_0530 | Q88QG4 | 3,4-dihydroxy-2-butanone 4-phosphate synthase, EC 4.1.99.12 | core riboflavin biosynthesis | homology-based; comparative genomics | covered | Canonical monofunctional DHBP synthase for step 3; expected in proteobacterial architecture alongside ribA and ribBX-like paralogs (jimeneznava2026biosynthesisregulationand pages 19-20, vitreschak2002regulationofriboflavin pages 3-4) |
| ubiX | PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX, EC 2.5.1.129 | boundary-adjacent pathway | homology-based; experimental function in bacteria | boundary_context | Uses FMN to generate prenylated FMN (prFMN) for UbiD-type decarboxylases in ubiquinone/related pathways; not part of riboflavin, FMN, or FAD formation module (weber2017requirementofa pages 18-20, lin2015isofunctionalenzymespad1 pages 1-2) |
| ribF | PP_0602 | Q88Q93 | Bifunctional riboflavin kinase / FMN adenylyltransferase, EC 2.7.1.26 + 2.7.7.2 | FMN-FAD formation | homology-based; pathway-conserved | covered | High-confidence step 6 enzyme converting riboflavin to FMN then FAD; the expected Gram-negative counterpart of Gram-positive RibC/RibFC (jimeneznava2026biosynthesisregulationand pages 19-20) |
| bluB | PP_1674 | Q88MA0 | 5,6-dimethylbenzimidazole synthase, EC 1.13.11.79 | boundary-adjacent pathway | homology-based; experimental function in bacteria | boundary_context | Converts reduced FMN to DMB, the lower ligand precursor for cobalamin (B12), linking flavin metabolism to B12 biosynthesis rather than core riboflavin synthesis (abbas2011geneticcontrolof pages 6-7, deptula2015blubcobt2fusionenzyme pages 1-2) |
| msuE | PP_2764 | Q88J85 | FMN reductase (NADPH), EC 1.5.1.38 | boundary-adjacent pathway | homology-based; related Pseudomonas experimental literature | boundary_context | Sulfur-metabolism flavin reductase associated with methanesulfonate/alkanesulfonate utilization systems; not a biosynthetic enzyme for riboflavin/FM N/FAD (kahnert2000thessulocus pages 3-4, kahnert2000thessulocus pages 4-6) |
| ribC | PP_2916 | Q88IT3 | Riboflavin synthase, EC 2.5.1.9 | core riboflavin biosynthesis | homology-based; comparative genomics | candidate_uncertain | Likely paralogous riboflavin synthase outside the main operon; plausible backup or condition-specific enzyme, but specific KT2440 functional partitioning versus PP_0515 is unresolved (vitreschak2002regulationofriboflavin pages 8-10, vitreschak2002regulationofriboflavin pages 3-4) |
| ribAB-II | PP_3813 | Q88GB1 | Annotated 3,4-dihydroxy-2-butanone 4-phosphate synthase; often misannotated as bifunctional ribBA, EC 4.1.99.12 only | core riboflavin biosynthesis | direct experimental in P. putida / proteobacterial ribBX study | over-propagated annotation | Second ribBX paralog. Same key caveat as PP_0516: DHBP synthase-compatible N-terminus but no true GTP cyclohydrolase II activity; should not cover step 1 (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8) |
| nudF | PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase, EC 3.6.1.13 | not core riboflavin | database annotation; superfamily-level homology | boundary_context | Nudix housekeeping hydrolase acting on ADP-ribose-related metabolites; no evidence it catalyzes a core riboflavin/FM N/FAD biosynthetic reaction in KT2440 (jimeneznava2026biosynthesisregulationand pages 19-20) |
| had | PP_5231 | Q88CF0 | (S)-2-haloacid dehalogenase, EC 3.8.1.- | not core riboflavin | database annotation | over-propagated annotation | No clear biochemical connection to riboflavin biosynthesis or flavin cofactor assembly; likely inclusion from broad KEGG map context rather than pathway-specific role (jimeneznava2026biosynthesisregulationand pages 19-20) |


*Table: This table summarizes all 15 candidate genes mapped to KEGG ppu00740 in Pseudomonas putida KT2440 and distinguishes core riboflavin/FM N/FAD biosynthesis genes from adjacent flavin-using functions and likely over-propagated annotations. It is especially useful for curation because it highlights the critical ribBX misannotation affecting PP_0516 and PP_3813.*

### 4.1 High-Confidence Core Genes

**ribA (PP_0522, Q88QH1) — GTP cyclohydrolase II (EC 3.5.4.25).** This is the sole true GTP cyclohydrolase II in *P. putida* KT2440 and is essential for catalyzing the first committed step of riboflavin biosynthesis: the hydrolysis of GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5′-phosphate (DARPP) with release of formate and pyrophosphate (jimeneznava2026biosynthesisregulationand pages 4-6, abbas2011geneticcontrolof pages 6-7). Its essentiality is reinforced by the fact that neither ribBX paralog (PP_0516 or PP_3813) can substitute for this function (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8). Evidence type: homology-based with strong support from the Brutinel et al. (2013) complementation study in P. putida.

**ribD (PP_0514, Q88QH9) — bifunctional deaminase/reductase (EC 3.5.4.26 + EC 1.1.1.193).** This enzyme catalyzes two sequential reactions in the pyrimidine branch: deamination of DARPP and reduction of the resulting intermediate to 5-amino-6-ribitylamino-2,4(1H,3H)-pyrimidinedione 5′-phosphate (ArPP → ArP) (jimeneznava2026biosynthesisregulationand pages 19-20, hubenthal2024influenceofantimicrobial pages 29-31). Located in the conserved riboflavin operon, its annotation is well-supported. Evidence type: homology-based; operon context conserved across Pseudomonas species (vitreschak2002regulationofriboflavin pages 3-4).

**ribB (PP_0530, Q88QG4) — DHBP synthase (EC 4.1.99.12).** This monofunctional enzyme catalyzes the conversion of ribulose-5-phosphate to 3,4-dihydroxy-2-butanone 4-phosphate (DHBP), the second precursor entering the riboflavin pathway (brutinel2013descriptionofa pages 3-4). In Pseudomonas, the single ribB gene is typically regulated by an upstream FMN riboswitch (RFN element), providing feedback control (vitreschak2002regulationofriboflavin pages 8-10, vitreschak2002regulationofriboflavin pages 6-8). Evidence type: homology-based with strong conservation; the RFN-element regulation of single ribB genes is well documented.

**ribH (PP_0517, Q88QH6) — lumazine synthase (EC 2.5.1.78).** Catalyzes the condensation of DHBP and ArP to form 6,7-dimethyl-8-ribityllumazine (DMRL). Located within the core riboflavin operon (jimeneznava2026biosynthesisregulationand pages 19-20, vitreschak2002regulationofriboflavin pages 3-4). Evidence type: homology-based; operon context.

**ribE (PP_0515, Q88QH8) — riboflavin synthase (EC 2.5.1.9).** Catalyzes the dismutation of two molecules of DMRL to produce one molecule of riboflavin and one molecule of ArP, which is recycled back as a lumazine synthase substrate (abbas2011geneticcontrolof pages 10-11, abbas2011geneticcontrolof pages 9-10). This gene corresponds to the ribE2-type paralog present in the conserved Pseudomonas riboflavin operon (vitreschak2002regulationofriboflavin pages 3-4). Evidence type: homology-based; operon context.

**ribF (PP_0602, Q88Q93) — bifunctional riboflavin kinase / FMN adenylyltransferase (EC 2.7.1.26 + EC 2.7.7.2).** This Gram-negative–specific bifunctional enzyme converts riboflavin to FMN (riboflavin kinase activity) and then FMN to FAD (FMN adenylyltransferase/FAD synthase activity) (jimeneznava2026biosynthesisregulationand pages 19-20). Evidence type: homology-based; the bifunctional ribF is the canonical Gram-negative enzyme for FMN/FAD formation.

### 4.2 Paralog Ambiguity and Over-Propagated Annotations

**ribAB-I / ribBX (PP_0516, Q88QH7) and ribAB-II / ribBX (PP_3813, Q88GB1) — DHBP synthase only, NOT bifunctional ribBA.** This is the single most important curation finding in this review. Both PP_0516 and PP_3813 are annotated as "3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12)" in the provided metadata, which is accurate for their N-terminal domains. However, these genes are frequently misannotated in automated pipelines as bifunctional ribBA (DHBP synthase / GTP cyclohydrolase II), because the C-terminal domain retains the overall fold of GTP cyclohydrolase II while having lost all catalytic residues (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 5-6).

Brutinel et al. (2013) experimentally demonstrated that ribBX from *P. putida* KT2440 (PP_0516 and PP_3813 were both tested) complements an *E. coli* ribB mutant but fails to complement a ribA mutant, confirming the absence of GTP cyclohydrolase II activity (brutinel2013descriptionofa pages 7-8, brutinel2013descriptionofa pages 4-5). Structural modeling shows that critical active-site residues (Cys54, Cys65, Cys67, Arg94, Tyr105 in E. coli numbering) are absent, and arginine residues protrude into the former substrate-binding pocket (brutinel2013descriptionofa pages 6-7, brutinel2013descriptionofa pages 5-6). The C-terminal domain (RibBX-CTD) appears to function as a regulatory element that modulates DHBP synthase activity, though the regulatory mechanism and effector molecules remain unknown (brutinel2013descriptionofa pages 8-9).

This misannotation is pervasive: approximately 40% of the 2,173 annotated ribBA genes in Proteobacteria are actually ribBX variants (brutinel2013descriptionofa pages 1-2). The RibBX variant evolved independently at least twice within Proteobacteria, and high conservation of the C-terminal domain under purifying selection indicates an important, undiscovered regulatory function (brutinel2013descriptionofa pages 8-9).

**ribC (PP_2916, Q88IT3) — riboflavin synthase (EC 2.5.1.9).** This is a second riboflavin synthase paralog outside the main riboflavin operon. Proteobacterial genomes commonly harbor ribE paralogs, and their differential regulation may relate to condition-specific flavin demands (vitreschak2002regulationofriboflavin pages 8-10, brutinel2013descriptionofa pages 3-4). No direct experimental evidence establishes functional partitioning between PP_0515 (ribE) and PP_2916 (ribC) in KT2440. Status: candidate_uncertain — likely functional but its specific biological role versus ribE is unresolved.

### 4.3 Boundary/Adjacent Pathway Genes

**ssuE (PP_0236, Q88R97) and msuE (PP_2764, Q88J85) — FMN reductases (EC 1.5.1.38).** These are NADPH-dependent FMN reductases functioning as components of two-component monooxygenase systems for organosulfur metabolism (kahnert2000thessulocus pages 3-4, kahnert2000thessulocus pages 8-8, kahnert2000thessulocus pages 1-1). SsuE provides reduced FMNH₂ to SsuD for alkanesulfonate desulfonation, and is required specifically for aromatic sulfonate utilization in *P. putida* (maren2001sulfateesterutilization pages 52-57, maren2001sulfateesterutilization pages 60-64). MsuE serves a parallel role in methanesulfonate metabolism (maren2001sulfateesterutilization pages 48-52, kahnert2000thessulocus pages 4-6). These enzymes consume FMN as a substrate but do not participate in riboflavin, FMN, or FAD biosynthesis. Their inclusion in KEGG ppu00740 reflects FMN-utilizing chemistry, not biosynthetic pathway membership.

**bluB (PP_1674, Q88MA0) — 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79).** BluB catalyzes the unprecedented fragmentation and contraction of bound FMNH₂ to yield 5,6-dimethylbenzimidazole (DMB) and D-erythrose 4-phosphate (abbas2011geneticcontrolof pages 6-7). DMB is the lower ligand of active vitamin B12 (cobalamin), making BluB a critical enzyme at the interface of flavin and cobalamin metabolism (deptula2015blubcobt2fusionenzyme pages 1-2). While BluB uses an FMN-derived substrate, it belongs functionally to the cobalamin biosynthesis pathway and should be treated as boundary context for the riboflavin module.

**ubiX (PP_0548, Q88QE6) — flavin prenyltransferase (EC 2.5.1.129).** UbiX catalyzes the prenylation of FMN to produce prenylated FMN (prFMN), a novel cofactor required by UbiD-family decarboxylases in ubiquinone biosynthesis (weber2017requirementofa pages 18-20, lin2015isofunctionalenzymespad1 pages 1-2). This enzyme is part of the ubiquinone/menaquinone pathway, not riboflavin biosynthesis. Its primary bucket assignment should be kegg:ppu00627 (aminobenzoate degradation) or the ubiquinone pathway, not ppu00740.

**nudF (PP_4919, Q88DA8) — ADP-ribose pyrophosphatase (EC 3.6.1.13).** A Nudix superfamily hydrolase that cleaves ADP-ribose. While ADP-ribose contains an adenine-ribose moiety, NudF acts on nucleotide metabolites rather than on riboflavin pathway intermediates. Its inclusion in ppu00740 reflects the broad KEGG map definition rather than pathway-specific function.

**had (PP_5231, Q88CF0) — (S)-2-haloacid dehalogenase (EC 3.8.1.-).** This enzyme has no established biochemical connection to riboflavin, FMN, or FAD biosynthesis. Its inclusion in the KEGG riboflavin metabolism map is likely an artifact of broad EC-class or GO-term mapping. This gene should be excluded from the riboflavin module.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Over-Propagated Annotations (Action Required)
- **PP_0516 (ribAB-I) and PP_3813 (ribAB-II)**: The GTP cyclohydrolase II annotation component is experimentally disproven for these ribBX-type genes in *P. putida* (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8). Automated pipelines propagate this error because the RibBX-CTD retains the overall fold of RibA. These annotations should be corrected to indicate DHBP synthase activity only (N-terminal domain), with the C-terminal domain annotated as a regulatory domain of unknown mechanism.
- **had (PP_5231)**: No evidence supports inclusion in the riboflavin module. Likely over-propagated from broad KEGG map context.

### 5.2 Ambiguities Requiring Attention
- **ribC (PP_2916) vs. ribE (PP_0515)**: Both encode riboflavin synthase. No published data distinguish their regulatory or functional roles in KT2440. Condition-specific expression studies would resolve this.
- **Deformylation step**: A novel formamidase (BrbF) required for riboflavin biosynthesis has been identified in alpha-proteobacteria such as *Sinorhizobium meliloti* (yurgel2022anovelformamidase pages 1-3, yurgel2022anovelformamidase pages 3-4, yurgel2022anovelformamidase pages 4-7). No clear BrbF ortholog has been identified in KT2440. The deformylation of AFRPP to DARoPP may proceed through the standard RibD-mediated chemistry in gamma-proteobacteria, or an unrecognized enzyme may be involved.

### 5.3 Regulatory Considerations
In most proteobacteria, the riboflavin operon itself is not regulated by the FMN riboswitch (RFN element); instead, individual genes like ribB carry upstream RFN elements for translational control (vitreschak2002regulationofriboflavin pages 8-10, vitreschak2002regulationofriboflavin pages 6-8). *P. aeruginosa* is a notable exception where an RFN element was inserted into the riboflavin operon (vitreschak2002regulationofriboflavin pages 1-2). The regulatory architecture in KT2440 likely resembles the typical Pseudomonas pattern with RFN control of single ribB.

## 6. Module and GO-Curation Recommendations

### Module Step Status Recommendations

| Step | Status | Recommendation |
|------|--------|----------------|
| GTP cyclohydrolase II | covered | Mark covered by ribA (PP_0522) ONLY. Remove ribAB-I/ribAB-II from step 1 coverage. |
| Pyrimidine deamination/reduction | covered | ribD (PP_0514) — no changes needed. |
| DHBP synthase | covered | ribB (PP_0530) is primary; PP_0516 and PP_3813 NTDs provide redundant DHBP synthase capacity. |
| Lumazine synthase | covered | ribH (PP_0517) — no changes needed. |
| Riboflavin synthase | covered | ribE (PP_0515) is primary; ribC (PP_2916) is candidate_uncertain backup. |
| Riboflavin kinase + FAD synthase | covered | ribF (PP_0602) — no changes needed. |
| Deformylation (if applicable) | candidate_uncertain | Flag for future investigation; likely covered by RibD chemistry. |

### Boundary Genes: Module Boundary Corrections
- **ssuE, msuE**: Should be excluded from core riboflavin module; reassign to sulfur metabolism modules.
- **bluB**: Should be excluded from core riboflavin module; reassign to cobalamin biosynthesis.
- **ubiX**: Primary bucket should be ubiquinone biosynthesis (ppu00130), not riboflavin metabolism.
- **nudF**: Should be excluded or flagged as peripheral nucleotide housekeeping.
- **had**: Should be removed from the riboflavin module entirely.

### GO Term Recommendations
- For PP_0516 and PP_3813: Remove GO:0003935 (GTP cyclohydrolase II activity) if present. Retain GO:0016830 or the appropriate term for DHBP synthase activity. Consider requesting a new GO term for "RibBX-CTD regulatory domain activity" or annotating the C-terminal domain with a regulatory process term.
- For the riboflavin module: Consider adding a note that the deformylation step (AFRPP → DARoPP) may not require a dedicated formamidase in gamma-proteobacteria.

## 7. Genes to Promote to Full Review

1. **ribAB-I / ribBX (PP_0516)** — Highest priority. The annotation correction from bifunctional ribBA to monofunctional ribBX has direct evidence from *P. putida* KT2440 (brutinel2013descriptionofa pages 7-8). The regulatory function of the C-terminal domain and its effectors remain unknown and represent an open research question (brutinel2013descriptionofa pages 8-9).

2. **ribAB-II / ribBX (PP_3813)** — Same priority as PP_0516. Second ribBX paralog with confirmed absence of GTP cyclohydrolase II activity.

3. **ribC (PP_2916)** — Medium priority. Functional partitioning with ribE (PP_0515) is unresolved. Expression profiling or gene deletion studies in KT2440 would clarify whether ribC serves a condition-specific role.

4. **ribA (PP_0522)** — Medium priority. As the sole GTP cyclohydrolase II, its essentiality in KT2440 should be experimentally confirmed (analogous to the inability to delete ribA in *S. oneidensis* MR-1) (brutinel2013descriptionofa pages 4-5).

## 8. Key References

1. Brutinel ED, Dean AM, Gralnick JA. "Description of a riboflavin biosynthetic gene variant prevalent in the phylum Proteobacteria." *J Bacteriol.* 2013;195(24):5479-5486. doi:10.1128/JB.00651-13 — **Direct experimental evidence for ribBX in P. putida KT2440 (PP_0516, PP_3813).**

2. Vitreschak AG, Rodionov DA, Mironov AA, Gelfand MS. "Regulation of riboflavin biosynthesis and transport genes in bacteria by transcriptional and translational attenuation." *Nucleic Acids Res.* 2002;30(14):3141-3151. doi:10.1093/nar/gkf433 — **Comprehensive operon organization and RFN regulation across proteobacteria including P. putida.**

3. Abbas CA, Sibirny AA. "Genetic control of biosynthesis and transport of riboflavin and flavin nucleotides and construction of robust biotechnological producers." *Microbiol Mol Biol Rev.* 2011;75(2):321-360. doi:10.1128/MMBR.00030-10 — **Authoritative review of riboflavin pathway enzymology and BluB function.**

4. Jiménez-Nava RA, Chávez-Camarillo GM, Cristiani-Urbina E. "Biosynthesis, regulation, and biotechnological production strategies of riboflavin (vitamin B2) and its derivatives: A review." *Pharmaceuticals.* 2026;19(3):389. doi:10.3390/ph19030389 — **Recent comprehensive review of riboflavin biosynthesis and gene nomenclature.**

5. Kahnert A, Vermeij P, Wietek C, et al. "The ssu locus plays a key role in organosulfur metabolism in *Pseudomonas putida* S-313." *J Bacteriol.* 2000;182(10):2869-2878. doi:10.1128/JB.182.10.2869-2878.2000 — **Direct experimental characterization of SsuE FMN reductase in P. putida.**

6. Yurgel SN, et al. "A novel formamidase is required for riboflavin biosynthesis in invasive bacteria." *J Biol Chem.* 2022;298(9):102377. doi:10.1016/j.jbc.2022.102377 — **Discovery of BrbF formamidase step; relevant for evaluating deformylation gap in KT2440.**

7. Deptula P, et al. "BluB/CobT2 fusion enzyme activity reveals mechanisms responsible for production of active form of vitamin B12 by *Propionibacterium freudenreichii*." *Microb Cell Fact.* 2015;14:186. doi:10.1186/s12934-015-0363-9 — **BluB functional characterization linking FMN to DMB synthesis.**

8. Lin F, et al. "Isofunctional enzymes PAD1 and UbiX catalyze formation of a novel cofactor required by ferulic acid decarboxylase and 4-hydroxy-3-polyprenylbenzoic acid decarboxylase." *ACS Chem Biol.* 2015;10(4):1137-1144. doi:10.1021/cb5008103 — **UbiX function as flavin prenyltransferase.**

---

**Summary of Key Findings for Curation:**
- All six core riboflavin/FMN/FAD biosynthetic steps are satisfiable in KT2440.
- The ribBX misannotation (PP_0516 and PP_3813 annotated as bifunctional ribBA but lacking GTP cyclohydrolase II activity) is the most critical annotation error to correct, supported by direct experimental evidence from *P. putida* (brutinel2013descriptionofa pages 2-3, brutinel2013descriptionofa pages 7-8).
- Six of 15 candidate genes are boundary genes that use flavin cofactors or substrates but do not catalyze riboflavin/FMN/FAD formation (kahnert2000thessulocus pages 3-4, abbas2011geneticcontrolof pages 6-7, weber2017requirementofa pages 18-20).
- The had gene (PP_5231) has no identifiable role in riboflavin metabolism and should be excluded.
- Paralog ambiguity between ribE (PP_0515) and ribC (PP_2916) remains unresolved for KT2440 specifically.


References

1. (brutinel2013descriptionofa pages 2-3): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

2. (brutinel2013descriptionofa pages 7-8): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

3. (jimeneznava2026biosynthesisregulationand pages 19-20): Raziel Arturo Jiménez-Nava, Griselda Ma. Chávez-Camarillo, and Eliseo Cristiani-Urbina. Biosynthesis, regulation, and biotechnological production strategies of riboflavin (vitamin b2) and its derivatives: a review. Pharmaceuticals, 19:389, Feb 2026. URL: https://doi.org/10.3390/ph19030389, doi:10.3390/ph19030389. This article has 0 citations.

4. (abbas2011geneticcontrolof pages 1-2): Charles A. Abbas and Andriy A. Sibirny. Genetic control of biosynthesis and transport of riboflavin and flavin nucleotides and construction of robust biotechnological producers. Microbiology and Molecular Biology Reviews, 75:321-360, Jun 2011. URL: https://doi.org/10.1128/mmbr.00030-10, doi:10.1128/mmbr.00030-10. This article has 498 citations and is from a domain leading peer-reviewed journal.

5. (jimeneznava2026biosynthesisregulationand pages 4-6): Raziel Arturo Jiménez-Nava, Griselda Ma. Chávez-Camarillo, and Eliseo Cristiani-Urbina. Biosynthesis, regulation, and biotechnological production strategies of riboflavin (vitamin b2) and its derivatives: a review. Pharmaceuticals, 19:389, Feb 2026. URL: https://doi.org/10.3390/ph19030389, doi:10.3390/ph19030389. This article has 0 citations.

6. (abbas2011geneticcontrolof pages 6-7): Charles A. Abbas and Andriy A. Sibirny. Genetic control of biosynthesis and transport of riboflavin and flavin nucleotides and construction of robust biotechnological producers. Microbiology and Molecular Biology Reviews, 75:321-360, Jun 2011. URL: https://doi.org/10.1128/mmbr.00030-10, doi:10.1128/mmbr.00030-10. This article has 498 citations and is from a domain leading peer-reviewed journal.

7. (deptula2015blubcobt2fusionenzyme pages 1-2): Paulina Deptula, Petri Kylli, Bhawani Chamlagain, Liisa Holm, Risto Kostiainen, Vieno Piironen, Kirsi Savijoki, and Pekka Varmanen. Blub/cobt2 fusion enzyme activity reveals mechanisms responsible for production of active form of vitamin b12 by propionibacterium freudenreichii. Microbial Cell Factories, Nov 2015. URL: https://doi.org/10.1186/s12934-015-0363-9, doi:10.1186/s12934-015-0363-9. This article has 85 citations and is from a peer-reviewed journal.

8. (weber2017requirementofa pages 18-20): Heike E. Weber, Manuela Gottardi, Christine Brückner, Mislav Oreb, Eckhard Boles, and Joanna Tripp. Requirement of a functional flavin mononucleotide prenyltransferase for the activity of a bacterial decarboxylase in a heterologous muconic acid pathway in saccharomyces cerevisiae. Applied and Environmental Microbiology, May 2017. URL: https://doi.org/10.1128/aem.03472-16, doi:10.1128/aem.03472-16. This article has 32 citations and is from a peer-reviewed journal.

9. (lin2015isofunctionalenzymespad1 pages 1-2): Fengming Lin, Kyle L. Ferguson, David R. Boyer, Xiaoxia Nina Lin, and E. Neil G. Marsh. Isofunctional enzymes pad1 and ubix catalyze formation of a novel cofactor required by ferulic acid decarboxylase and 4-hydroxy-3-polyprenylbenzoic acid decarboxylase. ACS chemical biology, 10 4:1137-44, Feb 2015. URL: https://doi.org/10.1021/cb5008103, doi:10.1021/cb5008103. This article has 124 citations and is from a domain leading peer-reviewed journal.

10. (kahnert2000thessulocus pages 3-4): Antje Kahnert, Paul Vermeij, Claudia Wietek, Peter James, Thomas Leisinger, and Michael A. Kertesz. The ssu locus plays a key role in organosulfur metabolism in pseudomonas putidas-313. Journal of Bacteriology, 182:2869-2878, May 2000. URL: https://doi.org/10.1128/jb.182.10.2869-2878.2000, doi:10.1128/jb.182.10.2869-2878.2000. This article has 124 citations and is from a peer-reviewed journal.

11. (kahnert2000thessulocus pages 8-8): Antje Kahnert, Paul Vermeij, Claudia Wietek, Peter James, Thomas Leisinger, and Michael A. Kertesz. The ssu locus plays a key role in organosulfur metabolism in pseudomonas putidas-313. Journal of Bacteriology, 182:2869-2878, May 2000. URL: https://doi.org/10.1128/jb.182.10.2869-2878.2000, doi:10.1128/jb.182.10.2869-2878.2000. This article has 124 citations and is from a peer-reviewed journal.

12. (kahnert2000thessulocus pages 1-1): Antje Kahnert, Paul Vermeij, Claudia Wietek, Peter James, Thomas Leisinger, and Michael A. Kertesz. The ssu locus plays a key role in organosulfur metabolism in pseudomonas putidas-313. Journal of Bacteriology, 182:2869-2878, May 2000. URL: https://doi.org/10.1128/jb.182.10.2869-2878.2000, doi:10.1128/jb.182.10.2869-2878.2000. This article has 124 citations and is from a peer-reviewed journal.

13. (brutinel2013descriptionofa pages 3-4): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

14. (vitreschak2002regulationofriboflavin pages 3-4): A. Vitreschak, D. Rodionov, A. Mironov, and M. Gelfand. Regulation of riboflavin biosynthesis and transport genes in bacteria by transcriptional and translational attenuation. Nucleic acids research, 30 14:3141-51, Jul 2002. URL: https://doi.org/10.1093/nar/gkf433, doi:10.1093/nar/gkf433. This article has 437 citations and is from a highest quality peer-reviewed journal.

15. (vitreschak2002regulationofriboflavin pages 8-10): A. Vitreschak, D. Rodionov, A. Mironov, and M. Gelfand. Regulation of riboflavin biosynthesis and transport genes in bacteria by transcriptional and translational attenuation. Nucleic acids research, 30 14:3141-51, Jul 2002. URL: https://doi.org/10.1093/nar/gkf433, doi:10.1093/nar/gkf433. This article has 437 citations and is from a highest quality peer-reviewed journal.

16. (vitreschak2002regulationofriboflavin pages 6-8): A. Vitreschak, D. Rodionov, A. Mironov, and M. Gelfand. Regulation of riboflavin biosynthesis and transport genes in bacteria by transcriptional and translational attenuation. Nucleic acids research, 30 14:3141-51, Jul 2002. URL: https://doi.org/10.1093/nar/gkf433, doi:10.1093/nar/gkf433. This article has 437 citations and is from a highest quality peer-reviewed journal.

17. (brutinel2013descriptionofa pages 5-6): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

18. (brutinel2013descriptionofa pages 8-9): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

19. (yurgel2022anovelformamidase pages 1-3): Svetlana N. Yurgel, Skylar A. Johnson, Jennifer Rice, Na Sa, Clayton Bailes, John Baumgartner, Josh E. Pitzer, R. Martin Roop, and Sanja Roje. A novel formamidase is required for riboflavin biosynthesis in invasive bacteria. Journal of Biological Chemistry, 298:102377, Sep 2022. URL: https://doi.org/10.1016/j.jbc.2022.102377, doi:10.1016/j.jbc.2022.102377. This article has 5 citations and is from a domain leading peer-reviewed journal.

20. (yurgel2022anovelformamidase pages 3-4): Svetlana N. Yurgel, Skylar A. Johnson, Jennifer Rice, Na Sa, Clayton Bailes, John Baumgartner, Josh E. Pitzer, R. Martin Roop, and Sanja Roje. A novel formamidase is required for riboflavin biosynthesis in invasive bacteria. Journal of Biological Chemistry, 298:102377, Sep 2022. URL: https://doi.org/10.1016/j.jbc.2022.102377, doi:10.1016/j.jbc.2022.102377. This article has 5 citations and is from a domain leading peer-reviewed journal.

21. (yurgel2022anovelformamidase pages 4-7): Svetlana N. Yurgel, Skylar A. Johnson, Jennifer Rice, Na Sa, Clayton Bailes, John Baumgartner, Josh E. Pitzer, R. Martin Roop, and Sanja Roje. A novel formamidase is required for riboflavin biosynthesis in invasive bacteria. Journal of Biological Chemistry, 298:102377, Sep 2022. URL: https://doi.org/10.1016/j.jbc.2022.102377, doi:10.1016/j.jbc.2022.102377. This article has 5 citations and is from a domain leading peer-reviewed journal.

22. (maren2001sulfateesterutilization pages 52-57): Antje Maren Kahnert. Sulfate ester utilization in pseudomonas. Text, 2001. URL: https://doi.org/10.3929/ethz-a-004281617, doi:10.3929/ethz-a-004281617. This article has 0 citations and is from a peer-reviewed journal.

23. (kahnert2000thessulocus pages 4-6): Antje Kahnert, Paul Vermeij, Claudia Wietek, Peter James, Thomas Leisinger, and Michael A. Kertesz. The ssu locus plays a key role in organosulfur metabolism in pseudomonas putidas-313. Journal of Bacteriology, 182:2869-2878, May 2000. URL: https://doi.org/10.1128/jb.182.10.2869-2878.2000, doi:10.1128/jb.182.10.2869-2878.2000. This article has 124 citations and is from a peer-reviewed journal.

24. (hubenthal2024influenceofantimicrobial pages 29-31): Anna Hübenthal. Influence of antimicrobial compounds and the rna-binding protein ribr on the activity of b vitamin-responsive bacterial riboswitches. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00034817, doi:10.11588/heidok.00034817. This article has 0 citations and is from a peer-reviewed journal.

25. (abbas2011geneticcontrolof pages 10-11): Charles A. Abbas and Andriy A. Sibirny. Genetic control of biosynthesis and transport of riboflavin and flavin nucleotides and construction of robust biotechnological producers. Microbiology and Molecular Biology Reviews, 75:321-360, Jun 2011. URL: https://doi.org/10.1128/mmbr.00030-10, doi:10.1128/mmbr.00030-10. This article has 498 citations and is from a domain leading peer-reviewed journal.

26. (abbas2011geneticcontrolof pages 9-10): Charles A. Abbas and Andriy A. Sibirny. Genetic control of biosynthesis and transport of riboflavin and flavin nucleotides and construction of robust biotechnological producers. Microbiology and Molecular Biology Reviews, 75:321-360, Jun 2011. URL: https://doi.org/10.1128/mmbr.00030-10, doi:10.1128/mmbr.00030-10. This article has 498 citations and is from a domain leading peer-reviewed journal.

27. (brutinel2013descriptionofa pages 4-5): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

28. (brutinel2013descriptionofa pages 6-7): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

29. (brutinel2013descriptionofa pages 1-2): Evan D. Brutinel, Antony M. Dean, and Jeffrey A. Gralnick. Description of a riboflavin biosynthetic gene variant prevalent in the phylum proteobacteria. Journal of Bacteriology, 195:5479-5486, Dec 2013. URL: https://doi.org/10.1128/jb.00651-13, doi:10.1128/jb.00651-13. This article has 36 citations and is from a peer-reviewed journal.

30. (maren2001sulfateesterutilization pages 60-64): Antje Maren Kahnert. Sulfate ester utilization in pseudomonas. Text, 2001. URL: https://doi.org/10.3929/ethz-a-004281617, doi:10.3929/ethz-a-004281617. This article has 0 citations and is from a peer-reviewed journal.

31. (maren2001sulfateesterutilization pages 48-52): Antje Maren Kahnert. Sulfate ester utilization in pseudomonas. Text, 2001. URL: https://doi.org/10.3929/ethz-a-004281617, doi:10.3929/ethz-a-004281617. This article has 0 citations and is from a peer-reviewed journal.

32. (vitreschak2002regulationofriboflavin pages 1-2): A. Vitreschak, D. Rodionov, A. Mironov, and M. Gelfand. Regulation of riboflavin biosynthesis and transport genes in bacteria by transcriptional and translational attenuation. Nucleic acids research, 30 14:3141-51, Jul 2002. URL: https://doi.org/10.1093/nar/gkf433, doi:10.1093/nar/gkf433. This article has 437 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. vitreschak2002regulationofriboflavin pages 3-4
2. jimeneznava2026biosynthesisregulationand pages 19-20
3. brutinel2013descriptionofa pages 3-4
4. brutinel2013descriptionofa pages 8-9
5. brutinel2013descriptionofa pages 1-2
6. abbas2011geneticcontrolof pages 6-7
7. vitreschak2002regulationofriboflavin pages 1-2
8. brutinel2013descriptionofa pages 7-8
9. brutinel2013descriptionofa pages 4-5
10. brutinel2013descriptionofa pages 2-3
11. abbas2011geneticcontrolof pages 1-2
12. jimeneznava2026biosynthesisregulationand pages 4-6
13. weber2017requirementofa pages 18-20
14. kahnert2000thessulocus pages 3-4
15. kahnert2000thessulocus pages 8-8
16. kahnert2000thessulocus pages 1-1
17. vitreschak2002regulationofriboflavin pages 8-10
18. vitreschak2002regulationofriboflavin pages 6-8
19. brutinel2013descriptionofa pages 5-6
20. yurgel2022anovelformamidase pages 1-3
21. yurgel2022anovelformamidase pages 3-4
22. yurgel2022anovelformamidase pages 4-7
23. maren2001sulfateesterutilization pages 52-57
24. kahnert2000thessulocus pages 4-6
25. hubenthal2024influenceofantimicrobial pages 29-31
26. abbas2011geneticcontrolof pages 10-11
27. abbas2011geneticcontrolof pages 9-10
28. brutinel2013descriptionofa pages 6-7
29. maren2001sulfateesterutilization pages 60-64
30. maren2001sulfateesterutilization pages 48-52
31. Includes: Diaminohydroxyphosphoribosylaminopyrimidine deaminase (DRAP deaminase) (EC 3.5.4.26) (Riboflavin-specific deaminase); 5-amino-6-(5-phosphoribosylamino)uracil reductase (EC 1.1.1.193) (HTP reductase)
32. Includes: Riboflavin kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2.7.7.2) (FAD pyrophosphorylase) (FAD synthase)
33. https://doi.org/10.1128/jb.00651-13,
34. https://doi.org/10.3390/ph19030389,
35. https://doi.org/10.1128/mmbr.00030-10,
36. https://doi.org/10.1186/s12934-015-0363-9,
37. https://doi.org/10.1128/aem.03472-16,
38. https://doi.org/10.1021/cb5008103,
39. https://doi.org/10.1128/jb.182.10.2869-2878.2000,
40. https://doi.org/10.1093/nar/gkf433,
41. https://doi.org/10.1016/j.jbc.2022.102377,
42. https://doi.org/10.3929/ethz-a-004281617,
43. https://doi.org/10.11588/heidok.00034817,