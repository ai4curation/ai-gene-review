---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T19:42:11.786452'
end_time: '2026-07-20T20:02:01.384429'
duration_seconds: 1189.6
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Folate one-carbon carrier-state interconversion
  module_summary: 'A taxon-neutral module for interconversion of the substituted tetrahydrofolate
    carrier states 5,10-methylene-THF, 5,10-methenyl-THF, 10-formyl-THF, 5-methyl-THF,
    and the salvaged 5-formyl-THF pool. The module separates four chemically distinct
    transformations: pyridine-nucleotide-linked oxidation of 5,10-methylene-THF to
    5,10-methenyl-THF, hydrolysis of 5,10-methenyl-THF to 10-formyl-THF, reduction
    of 5,10-methylene-THF to 5-methyl-THF, and ATP-dependent salvage of 5-formyl-THF
    to 5,10-methenyl-THF. Fused FolD/MTHFD architectures and NAD(H)- versus NADP(H)-linked
    variants are represented as alternative implementations of the same carrier-state
    conversions. The dehydrogenase and cyclohydrolase operations form the required
    coupled core; MTHFR reduction and 5-formyl-THF salvage are independent optional
    branches. Upstream one-carbon loading by serine hydroxymethyltransferase, glycine
    cleavage, or formate-tetrahydrofolate ligase and downstream use by purine, thymidylate,
    or methionine synthesis are outside this module.'
  module_outline: "- Folate one-carbon carrier-state interconversion\n  - Required\
    \ core 5,10-methylene-THF and 5,10-methenyl-THF redox interconversion\n  - 5,10-methylene-THF\
    \ to 5,10-methenyl-THF redox\n    - Alternative versions by redox cofactor and\
    \ enzyme architecture: Pyridine-nucleotide-linked dehydrogenase variants\n   \
    \   - NADP-linked bifunctional FolD reaction\n        - Bacterial FolD NADP-linked\
    \ dehydrogenase (molecular player: bifunctional FolD enzymes; activity or role:\
    \ methylenetetrahydrofolate dehydrogenase (NADP+) activity)\n      - NADP-linked\
    \ monofunctional MtdA reaction\n        - Monofunctional MtdA NADP-linked dehydrogenase\
    \ (molecular player: MtdA (Methylorubrum extorquens AM1); activity or role: methylenetetrahydrofolate\
    \ dehydrogenase (NADP+) activity)\n      - NADP-linked cytosolic MTHFD1 reaction\n\
    \        - Cytosolic MTHFD1 NADP-linked dehydrogenase (molecular player: eukaryotic\
    \ cytosolic MTHFD1 enzymes; activity or role: methylenetetrahydrofolate dehydrogenase\
    \ (NADP+) activity)\n      - NAD-linked MTHFD2 reaction\n        - NAD-linked\
    \ methylenetetrahydrofolate dehydrogenase (molecular player: mitochondrial MTHFD2\
    \ enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NAD+) activity)\n\
    \  - Required core 5,10-methenyl-THF and 10-formyl-THF hydrolytic interconversion\n\
    \  - 5,10-methenyl-THF to 10-formyl-THF hydrolysis\n    - Alternative versions\
    \ by fused versus monofunctional enzyme architecture: Methenyltetrahydrofolate\
    \ cyclohydrolase architecture variants\n      - Fused FolD/MTHFD cyclohydrolase\
    \ reaction\n        - Fused FolD/MTHFD methenyltetrahydrofolate cyclohydrolase\
    \ (molecular player: FolD/MTHFD methenyltetrahydrofolate cyclohydrolases; activity\
    \ or role: methenyltetrahydrofolate cyclohydrolase activity)\n      - Monofunctional\
    \ FchA cyclohydrolase reaction\n        - Monofunctional FchA methenyltetrahydrofolate\
    \ cyclohydrolase (molecular player: monofunctional FchA cyclohydrolases; activity\
    \ or role: methenyltetrahydrofolate cyclohydrolase activity)\n  - Optional 5,10-methylene-THF\
    \ reduction to 5-methyl-THF branch\n  - 5,10-methylene-THF to 5-methyl-THF reduction\n\
    \    - Alternative versions by pyridine-nucleotide specificity and enzyme architecture:\
    \ Methylenetetrahydrofolate reductase cofactor variants\n      - NADH-linked compact\
    \ MetF reaction\n        - NADH-linked methylenetetrahydrofolate reductase (molecular\
    \ player: compact bacterial MetF enzymes; activity or role: methylenetetrahydrofolate\
    \ reductase (NADH) activity)\n      - NADH-linked regulatory MTHFR reaction\n\
    \        - Regulatory-architecture NADH methylenetetrahydrofolate reductase (molecular\
    \ player: MTHFR2 (Arabidopsis thaliana); activity or role: methylenetetrahydrofolate\
    \ reductase (NADH) activity)\n      - NADPH-linked regulatory MTHFR reaction\n\
    \        - NADPH-linked methylenetetrahydrofolate reductase (molecular player:\
    \ MTHFR (human); activity or role: methylenetetrahydrofolate reductase (NADPH)\
    \ activity)\n  - Optional 5-formyl-THF salvage to 5,10-methenyl-THF branch\n \
    \ - 5-formyl-THF salvage\n    - 5-Formyltetrahydrofolate cyclo-ligase (molecular\
    \ player: Fau/MTHFS 5-formyltetrahydrofolate cyclo-ligases; activity or role:\
    \ 5-formyltetrahydrofolate cyclo-ligase activity)"
  module_connections: '- 5,10-methylene-THF to 5,10-methenyl-THF redox feeds into
    5,10-methenyl-THF to 10-formyl-THF hydrolysis: 5,10-methenyl-THF produced by the
    dehydrogenase reaction is the cyclohydrolase substrate; the two activities are
    often fused but are chemically distinct.

    - 5-formyl-THF salvage feeds into 5,10-methenyl-THF to 10-formyl-THF hydrolysis:
    Salvaged 5,10-methenyl-THF rejoins the methenyl/formyl carrier-state interconversion.'
  pathway_query: ppu00670
  pathway_id: ppu00670
  pathway_name: One carbon pool by folate
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00670 with 14 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '31'
  candidate_genes: '- glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1
    (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - purU-I: PP_0327 | Q88R07 | Formyltetrahydrofolate deformylase (EC 3.5.1.10)
    (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)

    - glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine
    methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - PP_0708: PP_0708 | Q88PZ0 | Betaine-aldehyde dehydrogenase (primary bucket kegg:ppu00670)

    - gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

    - gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase
    (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket
    kegg:ppu00785)

    - purU-II: PP_1367 | Q88N49 | Formyltetrahydrofolate deformylase (EC 3.5.1.10)
    (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)

    - purN: PP_1664 | Q88MB0 | Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2)
    (5''-phosphoribosylglycinamide transformylase) (GAR transformylase) (GART) (EC
    2.1.2.2; primary bucket kegg:ppu00670)

    - purU-III: PP_1943 | Q88LI9 | Formyltetrahydrofolate deformylase (EC 3.5.1.10)
    (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)

    - folD1: PP_1945 | Q88LI7 | Bifunctional protein FolD 1 [Includes: Methylenetetrahydrofolate
    dehydrogenase (EC 1.5.1.5); Methenyltetrahydrofolate cyclohydrolase (EC 3.5.4.9)]
    (EC 1.5.1.5; 3.5.4.9; primary bucket kegg:ppu00670)

    - folD2: PP_2265 | Q88KM5 | Bifunctional protein FolD 2 [Includes: Methylenetetrahydrofolate
    dehydrogenase (EC 1.5.1.5); Methenyltetrahydrofolate cyclohydrolase (EC 3.5.4.9)]
    (EC 1.5.1.5; 3.5.4.9; primary bucket kegg:ppu00670)

    - metH: PP_2375 | Q88KB5 | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine
    methyltransferase) (EC 2.1.1.13; primary bucket kegg:ppu04980)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)

    - folM: PP_4632 | Q88E36 | Dihydromonapterin reductase (EC 1.5.1.3) (EC 1.5.1.50)
    (Dihydrofolate reductase) (EC 1.5.1.3; 1.5.1.50; primary bucket kegg:ppu00670)

    - PP_4638: PP_4638 | Q88E30 | Methylenetetrahydrofolate reductase (primary bucket
    kegg:ppu00670)

    - purH: PP_4822 | Q88DK3 | Bifunctional purine biosynthesis protein PurH [Includes:
    Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR
    transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)]
    (EC 2.1.2.3; 3.5.4.10; primary bucket kegg:ppu00670)

    - metK: PP_4967 | Q88D60 | S-adenosylmethionine synthase (AdoMet synthase) (EC
    2.5.1.6) (MAT) (Methionine adenosyltransferase) (EC 2.5.1.6; primary bucket kegg:ppu00999)

    - ahcY: PP_4976 | A0A140FWS3 | Adenosylhomocysteinase (EC 3.13.2.1) (S-adenosyl-L-homocysteine
    hydrolase) (AdoHcyase) (EC 3.13.2.1; primary bucket kegg:ppu00670)

    - metF: PP_4977 | Q88D51 | Methylenetetrahydrofolate reductase (EC 1.5.1.54) (EC
    1.5.1.54; primary bucket kegg:ppu00670)

    - betB: PP_5063 | Q88CW7 | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8)
    (EC 1.2.1.8; primary bucket kegg:ppu00670)

    - betA: PP_5064 | Q88CW6 | Oxygen-dependent choline dehydrogenase (CDH) (CHD)
    (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) (EC 1.1.99.1;
    1.2.1.8; primary bucket kegg:ppu00670)

    - folA: PP_5132 | Q88CP8 | Dihydrofolate reductase (EC 1.5.1.3) (EC 1.5.1.3; primary
    bucket kegg:ppu04981)

    - thyA: PP_5141 | Q88CN9 | Thymidylate synthase (TS) (TSase) (EC 2.1.1.45) (EC
    2.1.1.45; primary bucket kegg:ppu04981)

    - gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase
    (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket
    kegg:ppu00785)

    - gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

    - fau: PP_5203 | Q88CH8 | 5-formyltetrahydrofolate cyclo-ligase (EC 6.3.3.2) (EC
    6.3.3.2; primary bucket kegg:ppu04981)

    - lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Folate one-carbon carrier-state interconversion in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00670
- Resolved ID: ppu00670
- Resolved name: One carbon pool by folate
- Source: KEGG

Resolved local bucket kegg:ppu00670 with 14 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 31

- glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- purU-I: PP_0327 | Q88R07 | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)
- glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- PP_0708: PP_0708 | Q88PZ0 | Betaine-aldehyde dehydrogenase (primary bucket kegg:ppu00670)
- gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket kegg:ppu00785)
- purU-II: PP_1367 | Q88N49 | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)
- purN: PP_1664 | Q88MB0 | Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2) (5'-phosphoribosylglycinamide transformylase) (GAR transformylase) (GART) (EC 2.1.2.2; primary bucket kegg:ppu00670)
- purU-III: PP_1943 | Q88LI9 | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)
- folD1: PP_1945 | Q88LI7 | Bifunctional protein FolD 1 [Includes: Methylenetetrahydrofolate dehydrogenase (EC 1.5.1.5); Methenyltetrahydrofolate cyclohydrolase (EC 3.5.4.9)] (EC 1.5.1.5; 3.5.4.9; primary bucket kegg:ppu00670)
- folD2: PP_2265 | Q88KM5 | Bifunctional protein FolD 2 [Includes: Methylenetetrahydrofolate dehydrogenase (EC 1.5.1.5); Methenyltetrahydrofolate cyclohydrolase (EC 3.5.4.9)] (EC 1.5.1.5; 3.5.4.9; primary bucket kegg:ppu00670)
- metH: PP_2375 | Q88KB5 | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) (EC 2.1.1.13; primary bucket kegg:ppu04980)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)
- folM: PP_4632 | Q88E36 | Dihydromonapterin reductase (EC 1.5.1.3) (EC 1.5.1.50) (Dihydrofolate reductase) (EC 1.5.1.3; 1.5.1.50; primary bucket kegg:ppu00670)
- PP_4638: PP_4638 | Q88E30 | Methylenetetrahydrofolate reductase (primary bucket kegg:ppu00670)
- purH: PP_4822 | Q88DK3 | Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)] (EC 2.1.2.3; 3.5.4.10; primary bucket kegg:ppu00670)
- metK: PP_4967 | Q88D60 | S-adenosylmethionine synthase (AdoMet synthase) (EC 2.5.1.6) (MAT) (Methionine adenosyltransferase) (EC 2.5.1.6; primary bucket kegg:ppu00999)
- ahcY: PP_4976 | A0A140FWS3 | Adenosylhomocysteinase (EC 3.13.2.1) (S-adenosyl-L-homocysteine hydrolase) (AdoHcyase) (EC 3.13.2.1; primary bucket kegg:ppu00670)
- metF: PP_4977 | Q88D51 | Methylenetetrahydrofolate reductase (EC 1.5.1.54) (EC 1.5.1.54; primary bucket kegg:ppu00670)
- betB: PP_5063 | Q88CW7 | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8) (EC 1.2.1.8; primary bucket kegg:ppu00670)
- betA: PP_5064 | Q88CW6 | Oxygen-dependent choline dehydrogenase (CDH) (CHD) (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) (EC 1.1.99.1; 1.2.1.8; primary bucket kegg:ppu00670)
- folA: PP_5132 | Q88CP8 | Dihydrofolate reductase (EC 1.5.1.3) (EC 1.5.1.3; primary bucket kegg:ppu04981)
- thyA: PP_5141 | Q88CN9 | Thymidylate synthase (TS) (TSase) (EC 2.1.1.45) (EC 2.1.1.45; primary bucket kegg:ppu04981)
- gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket kegg:ppu00785)
- gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- fau: PP_5203 | Q88CH8 | 5-formyltetrahydrofolate cyclo-ligase (EC 6.3.3.2) (EC 6.3.3.2; primary bucket kegg:ppu04981)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

## Generic Module Context

### Working Scope

A taxon-neutral module for interconversion of the substituted tetrahydrofolate carrier states 5,10-methylene-THF, 5,10-methenyl-THF, 10-formyl-THF, 5-methyl-THF, and the salvaged 5-formyl-THF pool. The module separates four chemically distinct transformations: pyridine-nucleotide-linked oxidation of 5,10-methylene-THF to 5,10-methenyl-THF, hydrolysis of 5,10-methenyl-THF to 10-formyl-THF, reduction of 5,10-methylene-THF to 5-methyl-THF, and ATP-dependent salvage of 5-formyl-THF to 5,10-methenyl-THF. Fused FolD/MTHFD architectures and NAD(H)- versus NADP(H)-linked variants are represented as alternative implementations of the same carrier-state conversions. The dehydrogenase and cyclohydrolase operations form the required coupled core; MTHFR reduction and 5-formyl-THF salvage are independent optional branches. Upstream one-carbon loading by serine hydroxymethyltransferase, glycine cleavage, or formate-tetrahydrofolate ligase and downstream use by purine, thymidylate, or methionine synthesis are outside this module.

### Provisional Biological Outline

- Folate one-carbon carrier-state interconversion
  - Required core 5,10-methylene-THF and 5,10-methenyl-THF redox interconversion
  - 5,10-methylene-THF to 5,10-methenyl-THF redox
    - Alternative versions by redox cofactor and enzyme architecture: Pyridine-nucleotide-linked dehydrogenase variants
      - NADP-linked bifunctional FolD reaction
        - Bacterial FolD NADP-linked dehydrogenase (molecular player: bifunctional FolD enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NADP+) activity)
      - NADP-linked monofunctional MtdA reaction
        - Monofunctional MtdA NADP-linked dehydrogenase (molecular player: MtdA (Methylorubrum extorquens AM1); activity or role: methylenetetrahydrofolate dehydrogenase (NADP+) activity)
      - NADP-linked cytosolic MTHFD1 reaction
        - Cytosolic MTHFD1 NADP-linked dehydrogenase (molecular player: eukaryotic cytosolic MTHFD1 enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NADP+) activity)
      - NAD-linked MTHFD2 reaction
        - NAD-linked methylenetetrahydrofolate dehydrogenase (molecular player: mitochondrial MTHFD2 enzymes; activity or role: methylenetetrahydrofolate dehydrogenase (NAD+) activity)
  - Required core 5,10-methenyl-THF and 10-formyl-THF hydrolytic interconversion
  - 5,10-methenyl-THF to 10-formyl-THF hydrolysis
    - Alternative versions by fused versus monofunctional enzyme architecture: Methenyltetrahydrofolate cyclohydrolase architecture variants
      - Fused FolD/MTHFD cyclohydrolase reaction
        - Fused FolD/MTHFD methenyltetrahydrofolate cyclohydrolase (molecular player: FolD/MTHFD methenyltetrahydrofolate cyclohydrolases; activity or role: methenyltetrahydrofolate cyclohydrolase activity)
      - Monofunctional FchA cyclohydrolase reaction
        - Monofunctional FchA methenyltetrahydrofolate cyclohydrolase (molecular player: monofunctional FchA cyclohydrolases; activity or role: methenyltetrahydrofolate cyclohydrolase activity)
  - Optional 5,10-methylene-THF reduction to 5-methyl-THF branch
  - 5,10-methylene-THF to 5-methyl-THF reduction
    - Alternative versions by pyridine-nucleotide specificity and enzyme architecture: Methylenetetrahydrofolate reductase cofactor variants
      - NADH-linked compact MetF reaction
        - NADH-linked methylenetetrahydrofolate reductase (molecular player: compact bacterial MetF enzymes; activity or role: methylenetetrahydrofolate reductase (NADH) activity)
      - NADH-linked regulatory MTHFR reaction
        - Regulatory-architecture NADH methylenetetrahydrofolate reductase (molecular player: MTHFR2 (Arabidopsis thaliana); activity or role: methylenetetrahydrofolate reductase (NADH) activity)
      - NADPH-linked regulatory MTHFR reaction
        - NADPH-linked methylenetetrahydrofolate reductase (molecular player: MTHFR (human); activity or role: methylenetetrahydrofolate reductase (NADPH) activity)
  - Optional 5-formyl-THF salvage to 5,10-methenyl-THF branch
  - 5-formyl-THF salvage
    - 5-Formyltetrahydrofolate cyclo-ligase (molecular player: Fau/MTHFS 5-formyltetrahydrofolate cyclo-ligases; activity or role: 5-formyltetrahydrofolate cyclo-ligase activity)

### Known Relationships Among Steps

- 5,10-methylene-THF to 5,10-methenyl-THF redox feeds into 5,10-methenyl-THF to 10-formyl-THF hydrolysis: 5,10-methenyl-THF produced by the dehydrogenase reaction is the cyclohydrolase substrate; the two activities are often fused but are chemically distinct.
- 5-formyl-THF salvage feeds into 5,10-methenyl-THF to 10-formyl-THF hydrolysis: Salvaged 5,10-methenyl-THF rejoins the methenyl/formyl carrier-state interconversion.

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

# Species-Aware Review: Folate One-Carbon Carrier-State Interconversion in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module area:** cofactors_vitamins_redox
**Local bucket:** kegg:ppu00670 "One carbon pool by folate" (31 candidate genes)
**Generic module:** Folate one-carbon carrier-state interconversion (4 chemically distinct reactions)

---

## 1. Executive Summary

The folate carrier-state interconversion module is **fully satisfiable (covered)** in *P. putida* KT2440. All four reactions of the generic module have high-confidence encoding:

- **Required core** (methylene-THF⇌methenyl-THF redox + methenyl-THF→10-formyl-THF hydrolysis): **redundantly covered** by two genuinely bifunctional FolD paralogs, **folD1/PP_1945** and **folD2/PP_2265** (both carry the complete NADP-linked dehydrogenase EC 1.5.1.5 + cyclohydrolase EC 3.5.4.9 domain architecture).
- **Optional MTHFR branch** (methylene-THF→5-methyl-THF): **covered** by compact NADH-type **metF/PP_4977** (EC 1.5.1.54), with a second, architecturally distinct MTHFR-family paralog **PP_4638** (candidate_uncertain).
- **Optional 5-formyl-THF salvage branch**: **covered** by **fau/PP_5203** (EC 6.3.3.2).

The dominant curation issue is **not a gap but over-inclusion**: the KEGG ppu00670 bucket returns exactly the 31 candidates, but only 4–5 of them are true carrier-state-interconversion genes. The other ~24 are upstream one-carbon **loading** enzymes (glyA SHMT, glycine-cleavage system), **downstream use** enzymes (purN, purH, thyA, metH, metK, ahcY), folate-pool **regeneration** (folA, folM), a 10-formyl-THF **drain** (purU ×3), and **osmolyte/sulfur** enzymes (betA, betB, PP_0708, PP_4594) that are not folate carrier-state reactions at all. KT2440 uses the fused FolD architecture exclusively; no MtdA/FchA split or eukaryotic MTHFD is expected. Evidence is homology-based (PE3) for the core genes, with protein-level evidence (PE1) only for two of the peripheral PurU deformylases.

---

## 2. Target-Organism Pathway Definition

**Included process (this module):** the interconversion of substituted-THF carrier states — 5,10-methylene-THF, 5,10-methenyl-THF, 10-formyl-THF, 5-methyl-THF, and the salvaged 5-formyl-THF pool — via four chemically distinct transformations:

1. NAD(P)-linked oxidation of 5,10-methylene-THF → 5,10-methenyl-THF (dehydrogenase).
2. Hydrolysis of 5,10-methenyl-THF → 10-formyl-THF (cyclohydrolase). *(Coupled with #1 as the required core.)*
3. Reduction of 5,10-methylene-THF → 5-methyl-THF (MTHFR). *(Optional branch.)*
4. ATP-dependent salvage of 5-formyl-THF → 5,10-methenyl-THF (cyclo-ligase). *(Optional branch.)*

**Neighboring pathways to keep separate** (present in KEGG ppu00670 but **outside** this module):
- **One-carbon loading:** serine hydroxymethyltransferase (glyA1/glyA2), glycine cleavage system (gcvT/P/H-I&II, lpd/lpdG/lpdV), and formate–THF ligase (Fhs — not encoded in KT2440). → KEGG ppu00260/ppu00630/ppu00785.
- **One-carbon use:** purine synthesis (purN, purH), thymidylate synthase (thyA), methionine synthase (metH) and the SAM/methionine cycle (metK, ahcY). → KEGG ppu00230/ppu00240/ppu00270/ppu00450/ppu00920.
- **Folate/pterin pool regeneration:** DHFR (folA), dihydromonapterin reductase (folM). → folate biosynthesis ppu00790.
- **Osmolyte and sulfur metabolism:** choline→glycine-betaine oxidation (betA, betB, PP_0708) and cystathionine γ-synthase (PP_4594). → glycine-betaine biosynthesis / cysteine-methionine metabolism; erroneously mapped here.

**Alternate names / database definitions:** KEGG map 00670 "One carbon pool by folate"; the module core overlaps MetaCyc "folate transformations" / "5,10-methylenetetrahydrofolate interconversion"; the fused enzyme is annotated FolD (bacterial) or D/C domain of MTHFD1 (eukaryotic). Note the EC-number mismatch in the local metadata for FolD: the dehydrogenase should read EC **1.5.1.5** (NADP+) and cyclohydrolase EC **3.5.4.9**, as confirmed in UniProt.

---

## 3. Expected Step Model (with target-taxon status)

| Module step | Reaction | Expected enzyme family | KT2440 status | Gene(s) |
|---|---|---|---|---|
| Core dehydrogenase | 5,10-CH₂-THF → 5,10-CH⁺-THF (NADP⁺) | Bifunctional FolD | **covered** | folD1/PP_1945, folD2/PP_2265 |
| Core cyclohydrolase | 5,10-CH⁺-THF → 10-CHO-THF | Bifunctional FolD (fused) | **covered** | folD1/PP_1945, folD2/PP_2265 |
| MTHFR branch (optional) | 5,10-CH₂-THF → 5-CH₃-THF | Compact NADH MetF | **covered** | metF/PP_4977 |
| MTHFR branch alt. architecture | (regulatory-architecture MTHFR) | MTHFR + extra domain | **candidate_uncertain** | PP_4638 |
| 5-formyl-THF salvage (optional) | 5-CHO-THF → 5,10-CH⁺-THF (ATP) | Fau/MTHFS cyclo-ligase | **covered** | fau/PP_5203 |
| MtdA monofunctional dehydrogenase | (methylotroph alternative) | MtdA | **not_expected_in_target_taxon** | — |
| FchA monofunctional cyclohydrolase | (Clostridial alternative) | FchA | **not_expected_in_target_taxon** | — |
| Eukaryotic MTHFD1/MTHFD2 | (eukaryotic/mitochondrial) | multidomain | **not_expected_in_target_taxon** | — |

---

## 4. Candidate Genes and Evidence

### 4A. True module members (high confidence)

- **folD1 / PP_1945 (Q88LI7, 291 aa, PE3, score 3).** Bifunctional FolD. InterPro IPR000672 THF_DH/CycHdrlase; Pfam PF00763 + PF02882 (both catalytic and NAD(P)-binding domains). UniProt "includes" both EC 1.5.1.5 and EC 3.5.4.9. Covers core dehydrogenase **and** cyclohydrolase. *Caveat:* homology-based; not experimentally characterized in KT2440.
- **folD2 / PP_2265 (Q88KM5, 284 aa, PE3, score 3).** Second bifunctional FolD with identical domain content. Provides redundancy. *Curation note:* two full-length FolD paralogs — treat both as covered; a later demonstration that one is dominant does not create a gap.
- **metF / PP_4977 (Q88D51, 295 aa, PE3, EC 1.5.1.54).** Compact bacterial MTHFR — InterPro IPR004620 (bacterial-MTHFR signature), Pfam PF02219, FAD flavoprotein, NAD-linked. Matches the "NADH-linked compact MetF" module variant. Genomically clustered with metH-cycle genes (metK PP_4967, ahcY PP_4976) consistent with a methionine-synthesis role.
- **fau / PP_5203 (Q88CH8, 202 aa, PE3, EC 6.3.3.2).** 5-formyltetrahydrofolate cyclo-ligase; Pfam PF01812. Covers the optional salvage branch (recycles the "folate trap" metabolite 5-CHO-THF back to 5,10-CH⁺-THF). *Caveat:* the local metadata lists its primary bucket as ppu04981 (folate biosynthesis map), a minor cross-mapping discrepancy; function is unambiguous.

### 4B. Ambiguous / promote to review

- **PP_4638 (Q88E30, 495 aa, PE3, no EC, no gene symbol).** Genuine MTHFR-catalytic domain (Pfam PF02219 / IPR003171; SUPFAM SSF51730; FAD flavoprotein) **fused to a C-terminal DUF5981** (Pfam PF12225 / IPR022026). It **lacks** the bacterial-MTHFR signature IPR004620 that metF carries. This is the module's "regulatory-architecture MTHFR" alternative implementation — a real second MTHFR-family protein, but its true substrate/cofactor and whether it reduces 5,10-methylene-THF are unconfirmed. **Do not** silently merge with metF or dismiss as noise.

### 4C. Adjacent (present in KEGG map, outside module)

- **purU-I/PP_0327 (Q88R07, PE1), purU-II/PP_1367 (Q88N49, PE3), purU-III/PP_1943 (Q88LI9, PE1)** — formyltetrahydrofolate deformylase, EC 3.5.1.10 (10-CHO-THF → formate + THF). A **drain** of the formyl pool, not a carrier-state interconversion. Triplication with two PE1 (protein-level) copies signals physiologically important formate/one-carbon overflow in *P. putida*. purU-III is genomically adjacent to folD1. → adjacent module, not this one.
- **glyA1/PP_0322, glyA2/PP_0671** (SHMT, EC 2.1.2.1) — one-carbon **loading**. Excluded.
- **gcvT/P/H-I & II (PP_0986/0988/0989, PP_5192/5193/5194), lpd/lpdG/lpdV (PP_5366/4187/4404)** — glycine cleavage system + shared E3 dihydrolipoyl dehydrogenase — one-carbon **loading**. Excluded (lpd genes are broadly shared with 2-oxo-acid dehydrogenases; classic over-propagation into folate maps).
- **purN/PP_1664 (EC 2.1.2.2), purH/PP_4822 (EC 2.1.2.3/3.5.4.10)** — 10-CHO-THF-dependent purine synthesis; **downstream use**. Excluded.
- **thyA/PP_5141 (EC 2.1.1.45)** — thymidylate synthase, consumes 5,10-CH₂-THF; **downstream use**. Excluded.
- **metH/PP_2375 (EC 2.1.1.13), metK/PP_4967 (EC 2.5.1.6), ahcY/PP_4976 (EC 3.13.2.1)** — cobalamin-dependent methionine synthase + SAM/SAH cycle; **downstream use** of 5-CH₃-THF. Excluded.
- **folA/PP_5132 (EC 1.5.1.3), folM/PP_4632 (EC 1.5.1.3/1.5.1.50)** — DHFR / dihydromonapterin reductase; **folate/pterin pool regeneration**. Excluded.
- **betA/PP_5064, betB/PP_5063, PP_0708 (betaine-aldehyde DH), PP_4594 (cystathionine γ-synthase)** — glycine-betaine osmolyte biosynthesis and sulfur-amino-acid metabolism; **not folate reactions**. Clear over-inclusion by the KEGG bucket.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

- **No true gaps.** Every required and optional module reaction is encoded.
- **Over-annotation into the bucket (primary issue):** ~24 of 31 candidates are loading/use/regeneration/osmolyte genes. betA/betB/PP_0708/PP_4594 are the most clear-cut misassignments to a folate carrier-state module. The lpd/lpdG/lpdV E3 subunits are generically shared and should not anchor any folate-specific claim.
- **Paralog ambiguity:** two FolD copies and three PurU copies. FolD redundancy is benign for satisfiability; PurU triplication is a boundary question (drain vs core).
- **PP_4638:** distinct-architecture MTHFR-family protein without EC assignment — the single genuine "candidate_uncertain" for the in-module steps.
- **Metadata EC discrepancy:** FolD dehydrogenase EC should be 1.5.1.5 (NADP+), matching UniProt; some local strings blur EC granularity. fau's primary-bucket cross-mapping (ppu04981 vs ppu00670) is a minor inconsistency.
- **Evidence depth:** core-module conclusions rest on **homology (PE3)**, not KT2440 biochemistry. Only PurU-I and PurU-III carry protein-level evidence, and that is presence, not mechanism.
- **PP_4638 is uncharacterizable by transfer:** of 1,230 UniProt proteins carrying the DUF5981 domain (PF12225), **zero are reviewed/experimentally characterized**, so no functionally validated homolog exists for the MTHFR+DUF5981 architecture anywhere. Its EC-less annotation therefore cannot be resolved by homology alone.
- **No alternative formyl-pool entry:** proteome UP000000556 encodes **no formate–tetrahydrofolate ligase Fhs (EC 6.3.4.3)**. The only routes into the 10-formyl-THF/methenyl-THF pool are the FolD core and fau salvage; purU drains it to formate. This makes the FolD core effectively non-redundant at the pathway level (redundant only in gene copy number).
- **MTHFR branch is B12-coupled:** KT2440 encodes **only cobalamin-dependent MetH (EC 2.1.1.13)** and **no cobalamin-independent MetE (EC 2.1.1.14)**, so the optional 5-methyl-THF branch product is consumed exclusively via a B12-dependent step (context for whether the metF/PP_4638 branch is conditionally essential).

---

## 6. Module and GO-Curation Recommendations

**Per-step module status:**
- Core dehydrogenase (5,10-CH₂-THF→CH⁺-THF): **covered** (folD1, folD2).
- Core cyclohydrolase (CH⁺-THF→10-CHO-THF): **covered** (folD1, folD2).
- MTHFR branch: **covered** (metF); PP_4638 **candidate_uncertain**.
- 5-formyl-THF salvage branch: **covered** (fau).
- MtdA / FchA / eukaryotic MTHFD variants: **not_expected_in_target_taxon**.

**Boundary / module-document recommendations:**
- Flag the local bucket as **module_needs_revision at the bucket level**: kegg:ppu00670 conflates loading + interconversion + use + salvage + osmolyte metabolism. For this module only folD1/folD2, metF (+PP_4638), and fau should be scored as members.
- Consider a **separate "10-formyl-THF drain / formate generation" annotation** for purU-I/II/III rather than counting them in carrier-state interconversion.
- Record **Fhs (formate–THF ligase) as not_expected_in_target_taxon** for the loading side; note there is no alternative ATP-dependent formate entry into the formyl pool in KT2440.
- Recommend GO assignments: folD1/folD2 → GO:0004488 (methylenetetrahydrofolate dehydrogenase (NADP+)) **and** GO:0004477 (methenyltetrahydrofolate cyclohydrolase); metF → GO:0004489 (methylenetetrahydrofolate reductase [NAD(P)H]); fau → GO:0030272 (5-formyltetrahydrofolate cyclo-ligase). **Do not** propagate a methylenetetrahydrofolate-reductase GO to PP_4638 without functional review; a "MTHFR-domain, function-uncertain" hold is appropriate. No new GO term request is obviously required.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_4638 (Q88E30)** — highest priority. Resolve whether the MTHFR+DUF5981 fusion is a bona fide second methylenetetrahydrofolate reductase (cofactor? activity?) or a divergent flavoenzyme; determines whether the MTHFR step has one or two implementations.
2. **folD1/PP_1945 vs folD2/PP_2265** — confirm both are functional (not one pseudogene/paralog-subfunctionalized); check expression/essentiality context and which is the housekeeping copy.
3. **metF/PP_4977** — confirm NADH vs NADPH preference and operon context to lock the "compact MetF (NADH)" variant assignment.
4. **purU-I/II/III (PP_0327/PP_1367/PP_1943)** — clarify boundary role (formate overflow) and whether they warrant a separate module; leverage the existing PE1 evidence.

---

## 8. Key References

- Belda E, *et al.* (2016) The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis. *Environ Microbiol* 18:3403–3424. **PMID 26913973.** (KT2440 re-annotation; basis for gene calls.)
- Aluri S, *et al.* (2016) Physiological role of FolD, FchA and Fhs from *Clostridium perfringens* in a heterologous *E. coli* model. *FEBS J*/**PMID 26531681.** (Fused FolD vs split monofunctional FolD-dehydrogenase + FchA-cyclohydrolase architectures — supports "not_expected" call for FchA in *P. putida*.)
- Eadsforth TC, *et al.* (2012) *Acinetobacter baumannii* FolD ligand complexes. **PMID 23050773.** (Bifunctional dehydrogenase/cyclohydrolase FolD is widely distributed in Gram-negative bacteria — transfer to *P. putida* strong.)
- Goenrich M, *et al.* (2002) Methylene-THF dehydrogenase FolD from *Hyphomicrobium* / MtdA in methylotrophs. **PMID 11889483.** (Distinguishes classical bifunctional FolD from methylotroph-specific MtdA.)
- Pawelek PD & MacKenzie RE (1998) Cyclohydrolase is rate-limiting in bifunctional D/C enzymes. **PMID 9454603.** (Mechanistic coupling of the two core activities.)
- Sah S, *et al.* (2020) Monomeric NADH-oxidizing MetF/MTHFR from *Mycobacterium smegmatis*. **PMID 32253341.** (Bacterial MetF diversity, relevant to metF variant assignment.)

*Evidence transfer note:* All core in-target conclusions are **inferred from homology/domain architecture (UniProt/InterPro PE3)** plus the KT2440 re-annotation genome; they are **not** backed by direct KT2440 enzymology. Cross-organism enzyme references (Gram-negative FolD, bacterial MetF) transfer **strongly** to *P. putida* on sequence/domain grounds. PP_4638's activity is the one substantive open question.


## Artifacts

- [OpenScientist final report](PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist_artifacts/final_report.pdf)