---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T13:15:28.914459'
end_time: '2026-08-08T13:37:26.059437'
duration_seconds: 1317.15
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: "Glycine cleavage system (glycine decarboxylase complex) \u2014 nonketotic\
    \ hyperglycinemia"
  module_summary: "The glycine cleavage system (GCS, glycine decarboxylase complex)\
    \ is the mitochondrial multienzyme system that carries out the major route of\
    \ glycine catabolism, degrading glycine to CO2 and ammonia while transferring\
    \ a one-carbon (methylene) unit to tetrahydrofolate \u2014 thereby coupling glycine\
    \ breakdown to folate/one-carbon metabolism. It comprises four components acting\
    \ on a lipoyl-swinging-arm relay: the P-protein (GLDC, glycine decarboxylase)\
    \ is a pyridoxal-5'-phosphate enzyme that decarboxylates glycine and transfers\
    \ the residual aminomethyl group to the lipoic-acid arm of the H-protein (GCSH),\
    \ a small non-catalytic lipoylated carrier; the T-protein (AMT, aminomethyltransferase)\
    \ then releases ammonia from the aminomethyl-dihydrolipoyl H-protein and transfers\
    \ the methylene carbon to tetrahydrofolate, forming 5,10-methylenetetrahydrofolate;\
    \ and the L-protein (DLD, dihydrolipoyl dehydrogenase \u2014 the same flavoenzyme\
    \ shared with the pyruvate, 2-oxoglutarate and branched-chain 2-oxoacid dehydrogenase\
    \ complexes) reoxidises the H-protein dihydrolipoyl group, reducing NAD+ to NADH\
    \ and regenerating the oxidised lipoyl arm. Inherited deficiency causes nonketotic\
    \ hyperglycinemia (glycine encephalopathy) \u2014 neonatal seizures, encephalopathy\
    \ and a raised CSF:plasma glycine ratio: most cases are due to GLDC (~80%), fewer\
    \ to AMT (~20%), and GCSH deficiency is rare."
  module_outline: "- Glycine cleavage system\n  - 1. glycine cleavage complex (P-H-T-L)\n\
    \  - glycine cleavage complex (GLDC-P / GCSH-H / AMT-T / DLD-L)\n    - GLDC: P-protein\
    \ (glycine decarboxylase) (molecular player: Glycine decarboxylase / glycine dehydrogenase\
    \ family (GLDC); activity or role: glycine dehydrogenase (decarboxylating) activity)\n\
    \    - GCSH: H-protein (lipoyl-bearing carrier) (molecular player: Glycine cleavage\
    \ H-protein family (GCSH); activity or role: lipoic acid binding)\n    - AMT:\
    \ T-protein (aminomethyltransferase) (molecular player: Aminomethyltransferase\
    \ (glycine cleavage T-protein) family (AMT); activity or role: aminomethyltransferase\
    \ activity)\n    - DLD: L-protein (dihydrolipoyl dehydrogenase, shared E3) (molecular\
    \ player: Dihydrolipoyl dehydrogenase / disulfide oxidoreductase family (DLD);\
    \ activity or role: dihydrolipoyl dehydrogenase (NADH) activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00260
  pathway_id: ppu00260
  pathway_name: Glycine, serine and threonine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00260 with 16 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '66'
  candidate_genes: '- trpA: PP_0082 | Q88RP7 | Tryptophan synthase alpha chain (EC
    4.2.1.20) (EC 4.2.1.20; primary bucket kegg:ppu00400)

    - trpB: PP_0083 | Q88RP6 | Tryptophan synthase beta chain (EC 4.2.1.20) (EC 4.2.1.20;
    primary bucket kegg:ppu00400)

    - thrB: PP_0121 | Q88RK8 | Homoserine kinase (HK) (HSK) (EC 2.7.1.39) (EC 2.7.1.39;
    primary bucket kegg:ppu00260)

    - tdcG-I: PP_0297 | Q88R37 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00270)

    - dgcA: PP_0310 | Q88R24 | Dimethylglycine dehydrogenase subunit (EC 1.5.8.-)
    (EC 1.5.8.-; primary bucket kegg:ppu00260)

    - dgcB: PP_0311 | Q88R23 | Dimethylglycine dehydrogenase subunit (EC 1.5.8.-)
    (EC 1.5.8.-; primary bucket kegg:ppu00260)

    - PP_0312: PP_0312 | Q88R22 | Electron transfer flavoprotein, alpha subunit (primary
    bucket kegg:ppu00260)

    - PP_0313: PP_0313 | Q88R21 | Electron transfer flavoprotein beta subunit (primary
    bucket kegg:ppu00260)

    - gbcA: PP_0315 | Q88R19 | Glycine-betaine dioxygenase subunit (EC 1.13.-.-) (EC
    1.13.-.-; primary bucket kegg:ppu00260)

    - gbcB: PP_0316 | Q88R18 | Glycine-betaine dioxygenase subunit (EC 1.13.-.-) (EC
    1.13.-.-; primary bucket kegg:ppu00260)

    - ltaE: PP_0321 | Q88R13 | L-threonine aldolase (EC 4.1.2.48) (EC 4.1.2.48; primary
    bucket kegg:ppu00260)

    - glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine
    methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - soxB: PP_0323 | Q88R11 | Sarcosine oxidase subunit beta (EC 1.5.3.24) (Sarcosine
    oxidase (5,10-methylenetetrahydrofolate-forming) subunit beta) (Tetrameric sarcosine
    oxidase subunit beta) (EC 1.5.3.24; primary bucket kegg:ppu00260)

    - soxD: PP_0324 | Q88R10 | Sarcosine oxidase subunit delta (EC 1.5.3.1) (EC 1.5.3.1;
    primary bucket kegg:ppu00260)

    - soxA: PP_0325 | Q88R09 | Sarcosine oxidase subunit alpha (EC 1.5.3.1) (EC 1.5.3.1;
    primary bucket kegg:ppu00260)

    - soxG: PP_0326 | Q88R08 | Sarcosine oxidase subunit gamma (EC 1.5.3.1) (EC 1.5.3.1;
    primary bucket kegg:ppu00260)

    - PP_0488: PP_0488 | Q88QK2 | NADP-dependent dehydrogenase HI_1430 (EC 1.1.1.-)
    (EC 1.1.1.-; primary bucket kegg:ppu00240)

    - PP_0662: PP_0662 | Q88Q36 | Threonine synthase (primary bucket kegg:ppu00750)

    - PP_0664: PP_0664 | Q88Q34 | homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3;
    primary bucket kegg:ppu00300)

    - glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine
    methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - PP_0708: PP_0708 | Q88PZ0 | Betaine-aldehyde dehydrogenase (primary bucket kegg:ppu00670)

    - pcs: PP_0731 | Q88PW7 | Phosphatidylcholine synthase (EC 2.7.8.24) (EC 2.7.8.24;
    primary bucket kegg:ppu00564)

    - hprA: PP_0762 | Q88PT6 | Glycerate dehydrogenase (primary bucket kegg:ppu00680)

    - gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

    - tdcG-II: PP_0987 | Q88P66 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00270)

    - gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase
    (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket
    kegg:ppu00785)

    - ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate
    reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81;
    primary bucket kegg:ppu00030)

    - hom: PP_1470 | Q88MU8 | Homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary
    bucket kegg:ppu00300)

    - thrC: PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) (EC 4.2.3.1; primary
    bucket kegg:ppu00750)

    - serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine
    aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)

    - asd__Q88LE4: PP_1989 | Q88LE4 | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase)
    (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenase) (EC 1.2.1.11;
    primary bucket kegg:ppu00261)

    - PP_2533: PP_2533 | Q88JW4 | D-isomer specific 2-hydroxyacid dehydrogenase family
    protein (primary bucket kegg:ppu00680)

    - PP_2800: PP_2800 | Q88J49 | Diaminobutyrate-2-oxoglutarate transaminase (primary
    bucket kegg:ppu00975)

    - PP_2930: PP_2930 | Q88IR9 | L-serine ammonia-lyase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00290)

    - tdcG-III: PP_3144 | Q88I57 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00270)

    - garK: PP_3178 | Q88I24 | Glycerate kinase (EC 2.7.1.165) (EC 2.7.1.165; primary
    bucket kegg:ppu00561)

    - PP_3191: PP_3191 | Q88I11 | Threonine ammonia-lyase / dehydratase (EC 4.3.1.19)
    (EC 4.3.1.19; primary bucket kegg:ppu00290)

    - ilvA-I: PP_3446 | Q88HB4 | L-threonine dehydratase (EC 4.3.1.19) (Threonine
    deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)

    - pssA: PP_3664 | Q88GQ4 | CDP-diacylglycerol--serine O-phosphatidyltransferase
    (EC 2.7.8.8) (EC 2.7.8.8; primary bucket kegg:ppu00564)

    - creA: PP_3667 | Q88GQ1 | Creatinase (EC 3.5.3.3) (EC 3.5.3.3; primary bucket
    kegg:ppu00330)

    - alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10)
    (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)

    - PP_3775: PP_3775 | Q88GE9 | Sarcosine oxidase (EC 1.5.3.1) (EC 1.5.3.1; primary
    bucket kegg:ppu00260)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - pvdH: PP_4223 | Q88F75 | Diaminobutyrate-2-oxoglutarate transaminase (EC 2.6.1.76)
    (EC 2.6.1.76; primary bucket kegg:ppu00975)

    - ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81;
    primary bucket kegg:ppu00561)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - PP_4421: PP_4421 | Q88EN3 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00260)

    - PP_4423: PP_4423 | Q88EN1 | Succinylglutamate desuccinylase/Aspartoacylase catalytic
    domain-containing protein (primary bucket kegg:ppu00260)

    - PP_4430: PP_4430 | Q88EM4 | Threonine dehydratase (EC 4.3.1.19) (EC 4.3.1.19;
    primary bucket kegg:ppu00290)

    - PP_4432: PP_4432 | Q88EM2 | Xaa-Pro aminopeptidase (primary bucket kegg:ppu00260)

    - PP_4473: PP_4473 | Q88EI9 | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) (EC
    2.7.2.4; primary bucket kegg:ppu00261)

    - PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)

    - PP_4677: PP_4677 | Q88DZ1 | CDP-diacylglycerol--serine O-phosphatidyltransferase
    (EC 2.7.8.8) (Phosphatidylserine synthase) (EC 2.7.8.8; primary bucket kegg:ppu00564)

    - ydfG: PP_4862 | Q88DG3 | 3-hydroxy acid dehydrogenase, NADP-dependent / malonic
    semialdehyde reductase (EC 1.1.1.276, EC 1.1.1.298) (EC 1.1.1.276; 1.1.1.298;
    primary bucket kegg:ppu00240)

    - serB: PP_4909 | Q88DB8 | Phosphoserine phosphatase (EC 3.1.3.3) (O-phosphoserine
    phosphohydrolase) (EC 3.1.3.3; primary bucket kegg:ppu00680)

    - PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3;
    primary bucket kegg:ppu00350)

    - gpmI: PP_5056 | Q88CX4 | 2,3-bisphosphoglycerate-independent phosphoglycerate
    mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4.2.12) (EC
    5.4.2.12; primary bucket kegg:ppu00680)

    - betB: PP_5063 | Q88CW7 | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8)
    (EC 1.2.1.8; primary bucket kegg:ppu00670)

    - betA: PP_5064 | Q88CW6 | Oxygen-dependent choline dehydrogenase (CDH) (CHD)
    (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) (EC 1.1.99.1;
    1.2.1.8; primary bucket kegg:ppu00670)

    - ilvA-II: PP_5149 | Q88CN1 | L-threonine dehydratase (EC 4.3.1.19) (Threonine
    deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)

    - serA: PP_5155 | Q88CM5 | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC
    1.1.1.95) (2-oxoglutarate reductase) (EC 1.1.1.399; 1.1.1.95; primary bucket kegg:ppu00680)

    - gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase
    (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket
    kegg:ppu00785)

    - gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__glycine_cleavage_system__ppu00260-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__glycine_cleavage_system__ppu00260-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Glycine cleavage system (glycine decarboxylase complex) — nonketotic hyperglycinemia in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00260
- Resolved ID: ppu00260
- Resolved name: Glycine, serine and threonine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00260 with 16 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 66

- trpA: PP_0082 | Q88RP7 | Tryptophan synthase alpha chain (EC 4.2.1.20) (EC 4.2.1.20; primary bucket kegg:ppu00400)
- trpB: PP_0083 | Q88RP6 | Tryptophan synthase beta chain (EC 4.2.1.20) (EC 4.2.1.20; primary bucket kegg:ppu00400)
- thrB: PP_0121 | Q88RK8 | Homoserine kinase (HK) (HSK) (EC 2.7.1.39) (EC 2.7.1.39; primary bucket kegg:ppu00260)
- tdcG-I: PP_0297 | Q88R37 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00270)
- dgcA: PP_0310 | Q88R24 | Dimethylglycine dehydrogenase subunit (EC 1.5.8.-) (EC 1.5.8.-; primary bucket kegg:ppu00260)
- dgcB: PP_0311 | Q88R23 | Dimethylglycine dehydrogenase subunit (EC 1.5.8.-) (EC 1.5.8.-; primary bucket kegg:ppu00260)
- PP_0312: PP_0312 | Q88R22 | Electron transfer flavoprotein, alpha subunit (primary bucket kegg:ppu00260)
- PP_0313: PP_0313 | Q88R21 | Electron transfer flavoprotein beta subunit (primary bucket kegg:ppu00260)
- gbcA: PP_0315 | Q88R19 | Glycine-betaine dioxygenase subunit (EC 1.13.-.-) (EC 1.13.-.-; primary bucket kegg:ppu00260)
- gbcB: PP_0316 | Q88R18 | Glycine-betaine dioxygenase subunit (EC 1.13.-.-) (EC 1.13.-.-; primary bucket kegg:ppu00260)
- ltaE: PP_0321 | Q88R13 | L-threonine aldolase (EC 4.1.2.48) (EC 4.1.2.48; primary bucket kegg:ppu00260)
- glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- soxB: PP_0323 | Q88R11 | Sarcosine oxidase subunit beta (EC 1.5.3.24) (Sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) subunit beta) (Tetrameric sarcosine oxidase subunit beta) (EC 1.5.3.24; primary bucket kegg:ppu00260)
- soxD: PP_0324 | Q88R10 | Sarcosine oxidase subunit delta (EC 1.5.3.1) (EC 1.5.3.1; primary bucket kegg:ppu00260)
- soxA: PP_0325 | Q88R09 | Sarcosine oxidase subunit alpha (EC 1.5.3.1) (EC 1.5.3.1; primary bucket kegg:ppu00260)
- soxG: PP_0326 | Q88R08 | Sarcosine oxidase subunit gamma (EC 1.5.3.1) (EC 1.5.3.1; primary bucket kegg:ppu00260)
- PP_0488: PP_0488 | Q88QK2 | NADP-dependent dehydrogenase HI_1430 (EC 1.1.1.-) (EC 1.1.1.-; primary bucket kegg:ppu00240)
- PP_0662: PP_0662 | Q88Q36 | Threonine synthase (primary bucket kegg:ppu00750)
- PP_0664: PP_0664 | Q88Q34 | homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary bucket kegg:ppu00300)
- glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- PP_0708: PP_0708 | Q88PZ0 | Betaine-aldehyde dehydrogenase (primary bucket kegg:ppu00670)
- pcs: PP_0731 | Q88PW7 | Phosphatidylcholine synthase (EC 2.7.8.24) (EC 2.7.8.24; primary bucket kegg:ppu00564)
- hprA: PP_0762 | Q88PT6 | Glycerate dehydrogenase (primary bucket kegg:ppu00680)
- gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- tdcG-II: PP_0987 | Q88P66 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00270)
- gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket kegg:ppu00785)
- ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81; primary bucket kegg:ppu00030)
- hom: PP_1470 | Q88MU8 | Homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary bucket kegg:ppu00300)
- thrC: PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) (EC 4.2.3.1; primary bucket kegg:ppu00750)
- serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)
- asd__Q88LE4: PP_1989 | Q88LE4 | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase) (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenase) (EC 1.2.1.11; primary bucket kegg:ppu00261)
- PP_2533: PP_2533 | Q88JW4 | D-isomer specific 2-hydroxyacid dehydrogenase family protein (primary bucket kegg:ppu00680)
- PP_2800: PP_2800 | Q88J49 | Diaminobutyrate-2-oxoglutarate transaminase (primary bucket kegg:ppu00975)
- PP_2930: PP_2930 | Q88IR9 | L-serine ammonia-lyase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00290)
- tdcG-III: PP_3144 | Q88I57 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00270)
- garK: PP_3178 | Q88I24 | Glycerate kinase (EC 2.7.1.165) (EC 2.7.1.165; primary bucket kegg:ppu00561)
- PP_3191: PP_3191 | Q88I11 | Threonine ammonia-lyase / dehydratase (EC 4.3.1.19) (EC 4.3.1.19; primary bucket kegg:ppu00290)
- ilvA-I: PP_3446 | Q88HB4 | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)
- pssA: PP_3664 | Q88GQ4 | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (EC 2.7.8.8; primary bucket kegg:ppu00564)
- creA: PP_3667 | Q88GQ1 | Creatinase (EC 3.5.3.3) (EC 3.5.3.3; primary bucket kegg:ppu00330)
- alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10) (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)
- PP_3775: PP_3775 | Q88GE9 | Sarcosine oxidase (EC 1.5.3.1) (EC 1.5.3.1; primary bucket kegg:ppu00260)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- pvdH: PP_4223 | Q88F75 | Diaminobutyrate-2-oxoglutarate transaminase (EC 2.6.1.76) (EC 2.6.1.76; primary bucket kegg:ppu00975)
- ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81; primary bucket kegg:ppu00561)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- PP_4421: PP_4421 | Q88EN3 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00260)
- PP_4423: PP_4423 | Q88EN1 | Succinylglutamate desuccinylase/Aspartoacylase catalytic domain-containing protein (primary bucket kegg:ppu00260)
- PP_4430: PP_4430 | Q88EM4 | Threonine dehydratase (EC 4.3.1.19) (EC 4.3.1.19; primary bucket kegg:ppu00290)
- PP_4432: PP_4432 | Q88EM2 | Xaa-Pro aminopeptidase (primary bucket kegg:ppu00260)
- PP_4473: PP_4473 | Q88EI9 | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) (EC 2.7.2.4; primary bucket kegg:ppu00261)
- PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)
- PP_4677: PP_4677 | Q88DZ1 | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) (Phosphatidylserine synthase) (EC 2.7.8.8; primary bucket kegg:ppu00564)
- ydfG: PP_4862 | Q88DG3 | 3-hydroxy acid dehydrogenase, NADP-dependent / malonic semialdehyde reductase (EC 1.1.1.276, EC 1.1.1.298) (EC 1.1.1.276; 1.1.1.298; primary bucket kegg:ppu00240)
- serB: PP_4909 | Q88DB8 | Phosphoserine phosphatase (EC 3.1.3.3) (O-phosphoserine phosphohydrolase) (EC 3.1.3.3; primary bucket kegg:ppu00680)
- PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00350)
- gpmI: PP_5056 | Q88CX4 | 2,3-bisphosphoglycerate-independent phosphoglycerate mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4.2.12) (EC 5.4.2.12; primary bucket kegg:ppu00680)
- betB: PP_5063 | Q88CW7 | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8) (EC 1.2.1.8; primary bucket kegg:ppu00670)
- betA: PP_5064 | Q88CW6 | Oxygen-dependent choline dehydrogenase (CDH) (CHD) (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) (EC 1.1.99.1; 1.2.1.8; primary bucket kegg:ppu00670)
- ilvA-II: PP_5149 | Q88CN1 | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) (EC 4.3.1.19; primary bucket kegg:ppu00290)
- serA: PP_5155 | Q88CM5 | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC 1.1.1.95) (2-oxoglutarate reductase) (EC 1.1.1.399; 1.1.1.95; primary bucket kegg:ppu00680)
- gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket kegg:ppu00785)
- gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

## Generic Module Context

### Working Scope

The glycine cleavage system (GCS, glycine decarboxylase complex) is the mitochondrial multienzyme system that carries out the major route of glycine catabolism, degrading glycine to CO2 and ammonia while transferring a one-carbon (methylene) unit to tetrahydrofolate — thereby coupling glycine breakdown to folate/one-carbon metabolism. It comprises four components acting on a lipoyl-swinging-arm relay: the P-protein (GLDC, glycine decarboxylase) is a pyridoxal-5'-phosphate enzyme that decarboxylates glycine and transfers the residual aminomethyl group to the lipoic-acid arm of the H-protein (GCSH), a small non-catalytic lipoylated carrier; the T-protein (AMT, aminomethyltransferase) then releases ammonia from the aminomethyl-dihydrolipoyl H-protein and transfers the methylene carbon to tetrahydrofolate, forming 5,10-methylenetetrahydrofolate; and the L-protein (DLD, dihydrolipoyl dehydrogenase — the same flavoenzyme shared with the pyruvate, 2-oxoglutarate and branched-chain 2-oxoacid dehydrogenase complexes) reoxidises the H-protein dihydrolipoyl group, reducing NAD+ to NADH and regenerating the oxidised lipoyl arm. Inherited deficiency causes nonketotic hyperglycinemia (glycine encephalopathy) — neonatal seizures, encephalopathy and a raised CSF:plasma glycine ratio: most cases are due to GLDC (~80%), fewer to AMT (~20%), and GCSH deficiency is rare.

### Provisional Biological Outline

- Glycine cleavage system
  - 1. glycine cleavage complex (P-H-T-L)
  - glycine cleavage complex (GLDC-P / GCSH-H / AMT-T / DLD-L)
    - GLDC: P-protein (glycine decarboxylase) (molecular player: Glycine decarboxylase / glycine dehydrogenase family (GLDC); activity or role: glycine dehydrogenase (decarboxylating) activity)
    - GCSH: H-protein (lipoyl-bearing carrier) (molecular player: Glycine cleavage H-protein family (GCSH); activity or role: lipoic acid binding)
    - AMT: T-protein (aminomethyltransferase) (molecular player: Aminomethyltransferase (glycine cleavage T-protein) family (AMT); activity or role: aminomethyltransferase activity)
    - DLD: L-protein (dihydrolipoyl dehydrogenase, shared E3) (molecular player: Dihydrolipoyl dehydrogenase / disulfide oxidoreductase family (DLD); activity or role: dihydrolipoyl dehydrogenase (NADH) activity)

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

# Glycine Cleavage System (Glycine Decarboxylase Complex) in *Pseudomonas putida* KT2440 — Module/Pathway/Taxon Review

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00260 — Glycine, serine and threonine metabolism (GCS genes primarily bucketed under ppu00785)
**Review focus:** Glycine cleavage system (GCS); generic module framed around human nonketotic hyperglycinemia (NKH)

---

## 1. Executive Summary

The glycine cleavage system (GCS, also called the glycine decarboxylase complex, GDC) is **fully satisfiable in the genome of *P. putida* KT2440**. All four catalytic/structural components — the P-protein (glycine decarboxylase), the H-protein (lipoyl-bearing carrier), the T-protein (aminomethyltransferase), and the L-protein (dihydrolipoyl dehydrogenase, shared E3) — are encoded. Notably, the P/H/T core is **duplicated** across two paralogous *gcv* operons: operon 1 at PP_0986–PP_0989 (gcvT-I, gcvP1, gcvH1, interleaved with a serine dehydratase) and operon 2 at PP_5192–PP_5194 (gcvP2, gcvH2, gcvT). The L-protein is not dedicated to the GCS; instead it is supplied *in trans* by one of three annotated dihydrolipoyl dehydrogenases (EC 1.8.1.4) that moonlight across the 2-oxoacid dehydrogenase complexes and the GCS. This architecture closely mirrors the *gcs1*/*gcs2* arrangement experimentally characterized in *Pseudomonas aeruginosa* PAO1.

The evidence base is predominantly **homology-based** (all *gcv* genes are UniProt PE3 "inferred from homology"; no strain-specific experimental characterization exists for KT2440 GCS proteins). The strongest transferable experimental support comes from the closely related *P. aeruginosa* PAO1, where the GCS is regulated by GcsR (PA2449), a TyrR-like enhancer-binding protein, and from *P. putida* itself for the shared E3/dihydrolipoamide dehydrogenase. We identified a positional candidate regulator in KT2440 — a TyrR-like HTH protein PP_0997 adjacent to *gcv* operon 1 — and confirmed that the H-protein lipoylation machinery (lipA, lipB) is encoded.

For curation, the practical conclusions are: (i) mark the GCS module **covered** in KT2440; (ii) resolve L-protein **paralog ambiguity** (lpdG PP_4187 is the best-supported general E3, with lpd PP_5366 and lpdV PP_4404 as alternatives); (iii) keep the **choline/betaine → dimethylglycine → sarcosine → glycine** catabolic cluster (PP_0310–PP_0326) and serine hydroxymethyltransferase (glyA1/glyA2) **separate** as upstream glycine feeders, not GCS components; and (iv) flag the generic module as **needs_revision** because its "nonketotic hyperglycinemia / glycine encephalopathy" disease framing is a human inborn-error concept with no counterpart in a soil bacterium.

---

## 2. Target-Organism Pathway Definition

**Included process.** The GCS in *P. putida* KT2440 is the multienzyme system that catabolizes glycine by oxidative decarboxylation, coupling glycine breakdown to one-carbon (folate) metabolism. The net reaction is:

```
glycine + THF + NAD+  →  CO2 + NH3 + 5,10-methylene-THF + NADH
```

The reaction proceeds through a lipoyl-swinging-arm relay across four components:

1. **P-protein (GcvP; EC 1.4.4.2):** a PLP-dependent enzyme that decarboxylates glycine and transfers the residual aminomethyl group to the lipoyl arm of the H-protein.
2. **H-protein (GcvH):** a small, non-catalytic lipoylated carrier that shuttles the aminomethyl/methylene intermediate between components.
3. **T-protein (GcvT; EC 2.1.2.10):** releases ammonia from the aminomethyl-dihydrolipoyl-H-protein and transfers the one-carbon unit to tetrahydrofolate, forming 5,10-methylene-THF.
4. **L-protein (Lpd/DLD; EC 1.8.1.4):** reoxidizes the dihydrolipoyl H-protein, reducing NAD+ to NADH and regenerating the oxidized lipoyl arm. This flavoenzyme is shared with the pyruvate, 2-oxoglutarate, and branched-chain 2-oxoacid dehydrogenase complexes.

**In a bacterium such as KT2440, the GCS is cytoplasmic** (there are no mitochondria). Functionally, the system provides (a) a route for glycine catabolism / use of glycine as a carbon and nitrogen source, and (b) a major source of C1 units for folate-dependent biosynthesis. In *Pseudomonas*, the duplicated operon (the regulated *gcs2*-type copy) is coupled with serine hydroxymethyltransferase and serine dehydratase to convert glycine → serine → pyruvate, feeding central metabolism.

**Neighboring pathways to keep separate.**
- **KEGG ppu00260 (Glycine, serine and threonine metabolism)** is a broad *overview bucket*, not the GCS module. It contains threonine biosynthesis (thrB, thrC, hom), serine biosynthesis (serA, serB, serC), threonine/serine dehydratases, and many enzymes unrelated to glycine cleavage. The GCS proper is a distinct sub-module (KEGG maps the *gcv* genes to ppu00785).
- **Choline/glycine-betaine catabolism (PP_0310–PP_0326):** betaine → dimethylglycine → sarcosine → glycine. This *produces* glycine feeding into the GCS; it is upstream and lineage-specific, not part of the GCS.
- **Serine hydroxymethyltransferase (glyA1 PP_0322, glyA2 PP_0671; EC 2.1.2.1):** interconverts serine and glycine + 5,10-methylene-THF; a partner of, but distinct from, the GCS.
- **Lipoate biosynthesis/attachment (lipA, lipB):** required to activate the H-protein, but an accessory pathway.

**Alternate names / database definitions.** GCS = glycine decarboxylase complex (GDC) = glycine synthase (the reaction is reversible). Components: P-protein = GLDC/GcvP; H-protein = GCSH/GcvH; T-protein = AMT/GcvT; L-protein = DLD/Lpd/E3. The generic "nonketotic hyperglycinemia" label is a **human clinical framing** and should not be used as the module name for a bacterial taxon.

---

## 3. Expected Step Model

| Step | Component | Activity (EC) | Expected in KT2440? | Status |
|------|-----------|---------------|---------------------|--------|
| S1 | P-protein (GcvP) | glycine dehydrogenase (decarboxylating) 1.4.4.2 | Yes | **Covered** (duplicated) |
| S2 | H-protein (GcvH) | lipoyl-bearing carrier / lipoic acid binding | Yes | **Covered** (duplicated) |
| S3 | T-protein (GcvT) | aminomethyltransferase 2.1.2.10 | Yes | **Covered** (duplicated) |
| S4 | L-protein (Lpd/DLD) | dihydrolipoyl dehydrogenase 1.8.1.4 | Yes (shared, *in trans*) | **Covered, paralog-ambiguous** |
| A1 | Lipoylation (LipA/LipB) | lipoyl synthase 2.8.1.8 / octanoyltransferase 2.3.1.181 | Yes | **Covered (accessory)** |
| R1 | Transcriptional regulator (GcsR-type) | TyrR-like EBP | Likely (positional candidate PP_0997) | **Candidate_uncertain** |

All four core steps are encoded; the module is genome-supportable. The only genuine ambiguity is *which* dihydrolipoyl dehydrogenase serves the GCS H-protein.

---

## 4. Candidate Genes and Evidence

### 4.1 GCS core — operon 1 (PP_0986–PP_0989)

| Gene | Locus | UniProt | Role | Evidence |
|------|-------|---------|------|----------|
| gcvT-I | PP_0986 | Q88P67 | T-protein, aminomethyltransferase (EC 2.1.2.10) | Homology (PE3) |
| (tdcG-II) | PP_0987 | Q88P66 | L-serine dehydratase (EC 4.3.1.17) — *interleaved, not GCS* | Homology |
| gcvP1 | PP_0988 | Q88P65 | P-protein, glycine dehydrogenase (EC 1.4.4.2) | Homology (PE3) |
| gcvH1 | PP_0989 | Q88P64 | H-protein, lipoyl carrier | Homology (PE3) |

The gene order (T–serine dehydratase–P–H) and the interleaved serine dehydratase parallel the *P. aeruginosa gcs2* operon (gcvH2-gcvP2-glyA2-sdaA-gcvT2), which forms a glycine → pyruvate pathway ([PMID: 27303730](https://pubmed.ncbi.nlm.nih.gov/27303730/)).

### 4.2 GCS core — operon 2 (PP_5192–PP_5194)

| Gene | Locus | UniProt | Role | Evidence |
|------|-------|---------|------|----------|
| gcvP2 | PP_5192 | Q88CI9 | P-protein 2 (EC 1.4.4.2) | Homology (PE3) |
| gcvH2 | PP_5193 | Q88CI8 | H-protein 2 | Homology (PE3) |
| gcvT | PP_5194 | Q88CI7 | T-protein (EC 2.1.2.10) | Homology (PE3) |

A complete second P/H/T set. The duplication is a genuine feature and closely matches the two-operon organization documented in *P. aeruginosa*.

### 4.3 L-protein candidates (shared E3, EC 1.8.1.4)

| Gene | Locus | UniProt | Evidence tier | Note |
|------|-------|---------|---------------|------|
| lpdG | PP_4187 | Q88FB1 | **PE1 (protein level)** | Strongest experimentally supported general/GCS E3 |
| lpd | PP_5366 | Q88C17 | PE3 (homology) | General E3 candidate |
| lpdV | PP_4404 | Q88EP9 | PE3 (homology) | Branched-chain 2-oxoacid dehydrogenase E3 |

No *gcv*-linked dedicated L-protein exists; the E3 is recruited *in trans*. In *P. putida*, the dihydrolipoamide dehydrogenase (E3) is experimentally established to serve both the α-keto acid dehydrogenase complexes and the GCS H-protein ([PMID: 15826505](https://pubmed.ncbi.nlm.nih.gov/15826505/)). **lpdG (PP_4187, PE1)** is the best-supported general E3 and the leading GCS L-protein candidate; **lpdV** is most likely dedicated to the branched-chain complex.

### 4.4 Accessory and regulatory genes

| Gene | Locus | UniProt | Role | Evidence |
|------|-------|---------|------|----------|
| lipA | PP_4800 | Q88DM5 | Lipoyl synthase (EC 2.8.1.8) | Homology |
| lipB | PP_4801 | Q88DM4 | Octanoyltransferase (EC 2.3.1.181) | Homology |
| (lipA-2) | PP_4797 | — | Second predicted lipoyl synthase | Prediction |
| glyA1 | PP_0322 | Q88R12 | SHMT 1 (EC 2.1.2.1) — *partner, feeder* | Homology |
| glyA2 | PP_0671 | Q88Q27 | SHMT 2 (EC 2.1.2.1) — *partner, feeder* | Homology |
| PP_0997 (candidate GcsR) | PP_0997 | Q88P56 | TyrR-like HTH regulator, adjacent to operon 1 | Positional inference |

### 4.5 Upstream glycine-feeder cluster (PP_0310–PP_0326) — NOT GCS

This cluster encodes the choline/glycine-betaine catabolic route:
- **dgcA/dgcB (PP_0310/PP_0311):** dimethylglycine dehydrogenase subunits (EC 1.5.8.-)
- **PP_0312/PP_0313:** electron transfer flavoprotein α/β
- **gbcA/gbcB (PP_0315/PP_0316):** glycine-betaine demethylase/dioxygenase (EC 1.13.-.-)
- **ltaE (PP_0321):** L-threonine aldolase (EC 4.1.2.48)
- **soxBDAG (PP_0323–PP_0326):** heterotetrameric sarcosine oxidase (α/β/γ/δ)
- **PP_3775:** additional sarcosine oxidase (EC 1.5.3.1)

These convert betaine → dimethylglycine → sarcosine → glycine, generating the substrate that feeds the GCS. They belong to the *P. aeruginosa* GbdR regulon ([PMID: 24097953](https://pubmed.ncbi.nlm.nih.gov/24097953/)) and are **upstream feeders**, not GCS components.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 L-protein paralog ambiguity (highest-priority ambiguity)
Three EC 1.8.1.4 genes are annotated and none is physically linked to a *gcv* operon. The GCS must borrow one of them. Curation should not assign a single locus with certainty. Recommended interim assignment: **lpdG (PP_4187)** as the general/GCS E3 (PE1 support), with lpd and lpdV noted as alternatives. This is a **candidate_uncertain** designation for the specific gene, though the *step* is **covered**.

### 5.2 Duplicated P/H/T — which operon is "the" GCS?
Both operons appear complete. In *P. aeruginosa* the two copies are differentially regulated (one glycine-inducible via GcsR). In KT2440 the functional division of labor is unverified. Both should be recorded as covering the core steps; a note that duplication may reflect distinct regulatory/physiological roles is warranted.

### 5.3 Broad EC/GO and over-propagation risks
- **ppu00260 bucket over-inclusion:** The 66-gene candidate list is dominated by threonine/serine metabolism, betaine catabolism, phospholipid synthesis (pssA, pcs, PP_4677), and glyoxylate/glycerate enzymes that are *not* GCS. Many carry broad or partial EC numbers (e.g., EC 1.13.-.-, EC 1.1.1.-, EC 2.6.1.-). These should not be mapped to the GCS module.
- **"Betaine aldehyde dehydrogenase" duplications** (betA/betB/PP_0708) and multiple serine dehydratases (tdcG-I/II/III) reflect the overview-map nature of ppu00260, not GCS membership.
- **Regulator naming gap:** No gene is annotated *gcsR/gcvA/gcvR/gcvB* by name; PP_0997 is a positional inference only.

### 5.4 Disease-framing mismatch (module_needs_revision)
The generic module is framed around **nonketotic hyperglycinemia / glycine encephalopathy** — a human autosomal-recessive inborn error (GLDC ~80%, AMT ~20%, GCSH rare; [PMID: 33791923](https://pubmed.ncbi.nlm.nih.gov/33791923/)). This clinical concept has **no counterpart in *P. putida***. The bacterial module should be re-scoped as "glycine cleavage / glycine catabolism and one-carbon provision," dropping the disease framing.

---

## 6. Module and GO-Curation Recommendations

| Module step / element | Recommended status | Rationale |
|-----------------------|--------------------|-----------|
| P-protein (S1) | **covered** | gcvP1 + gcvP2 encoded |
| H-protein (S2) | **covered** | gcvH1 + gcvH2 encoded; lipoylation machinery present |
| T-protein (S3) | **covered** | gcvT-I + gcvT encoded |
| L-protein (S4) | **covered** (step); **candidate_uncertain** (specific gene) | Shared E3 in trans; lpdG best candidate |
| Lipoylation accessory | **covered** | lipA/lipB present |
| GcsR-type regulator | **candidate_uncertain** | PP_0997 positional candidate only |
| Choline/betaine→glycine cluster | **not part of module** (separate feeder module) | Upstream glycine source |
| Disease framing | **module_needs_revision** | NKH is human-specific; not applicable to bacteria |

**Module boundary corrections.**
- Split the module cleanly from the broad KEGG ppu00260 overview map. The GCS module should contain only P/H/T/L + lipoylation accessory (+ regulator).
- Create or reference a **separate upstream module** for choline/glycine-betaine/sarcosine catabolism (the GbdR-type regulon) as the glycine-feeder route.
- SHMT (glyA1/glyA2) and serine dehydratase should be represented as **partner/adjacent** steps, not GCS core.

**GO considerations.** Core GO annotations apply well: glycine dehydrogenase (decarboxylating) activity (GO:0004375), aminomethyltransferase activity (GO:0004047), dihydrolipoyl dehydrogenase activity (GO:0004148), lipoic acid binding, and glycine catabolic process (GO:0006546) / glycine cleavage. No new GO term requests appear necessary. A curation note should record that the L-protein GO annotation is shared/moonlighting and should not imply a dedicated GCS-only gene.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **lpdG (PP_4187, Q88FB1)** — PE1 evidence; resolve whether it is the physiological GCS E3. Highest priority.
2. **PP_0997 (Q88P56)** — candidate GcsR/TyrR-like regulator adjacent to *gcv* operon 1; confirm whether it activates the GCS operon.
3. **gcvP1/gcvH1/gcvT-I (PP_0986–0989)** and **gcvP2/gcvH2/gcvT (PP_5192–5194)** — confirm operon structure, promoter architecture, and any functional divergence between the two copies.
4. **lpd (PP_5366) and lpdV (PP_4404)** — clarify complex-specific assignments to rule in/out as GCS E3.

---

## 8. Key Findings (Detailed)

### F001 — A complete, duplicated GCS
UniProt/KEGG verification confirms all four GCS components are present. Operon 1 (PP_0986–PP_0989) carries gcvT-I (T), gcvP1 (P), and gcvH1 (H), interleaved with a serine dehydratase (PP_0987). Operon 2 (PP_5192–PP_5194) carries gcvP2 (P), gcvH2 (H), and gcvT (T). The shared L-protein is supplied in trans (lpd, lpdG, lpdV). All *gcv* genes are UniProt PE3 (inferred from homology) — there is no strain-specific experimental characterization. This mirrors the *P. aeruginosa gcs1/gcs2* arrangement in which the *gcs2* operon (gcvH2-gcvP2-glyA2-sdaA-gcvT2) is regulated by GcsR and converts glycine to pyruvate. The paper reports: "GcsR binds to an 18-bp consensus sequence (TGTAACG-N4-CGTTCCG) upstream of the gcs2 operon, consisting of the gcvH2, gcvP2, glyA2, sdaA, and gcvT2 genes" ([PMID: 27303730](https://pubmed.ncbi.nlm.nih.gov/27303730/)).

### F002 — L-protein is a shared, moonlighting subunit with paralog ambiguity
Three dihydrolipoyl dehydrogenase (EC 1.8.1.4) genes are annotated: lpd (PP_5366, PE3), lpdG (PP_4187, PE1 "evidence at protein level"), and lpdV (PP_4404, PE3). No *gcv*-linked dedicated L-protein exists. In *P. putida*, the E3 is experimentally established to serve both the 2-oxoacid dehydrogenase complexes and the GCS H-protein: "Dihydrolipoamide dehydrogenase (E3) catalyzes the reoxidation of dihydrolipoyl moiety of the acyltransferase components of three alpha-keto acid dehydrogenase complexes and of the hydrogen-carrier protein of the glycine cleavage system" ([PMID: 15826505](https://pubmed.ncbi.nlm.nih.gov/15826505/)). lpdV is the branched-chain 2-oxoacid dehydrogenase E3; lpdG (PE1) is the strongest experimentally supported general/GCS E3 candidate.

### F003 — Betaine/sarcosine cluster is a lineage-specific glycine feeder; NKH framing not applicable
The PP_0310–PP_0326 cluster (dgcAB, ETF α/β, gbcAB, ltaE, soxBDAG) encodes the choline/glycine-betaine catabolic route (betaine → dimethylglycine → sarcosine → glycine) that generates glycine feeding into the GCS. In *P. aeruginosa* this is the GbdR regulon: "The GbdR regulon includes the genes encoding GB, dimethylglycine, sarcosine, glycine, and serine catabolic enzymes and the BetX and CbcXWV quaternary amine transport proteins" ([PMID: 24097953](https://pubmed.ncbi.nlm.nih.gov/24097953/)). Heterotetrameric sarcosine oxidase (αβγδ, matching soxABGD) "catalyzes the oxidation of sarcosine (N-methylglycine) to yield hydrogen peroxide, glycine and formaldehyde. In the presence of tetrahydrofolate, the oxidation of sarcosine is coupled to the formation of 5,10-methylenetetrahydrofolate" ([PMID: 16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/)). These are upstream feeder steps, not GCS components. The "nonketotic hyperglycinemia" framing is a human inborn error with no counterpart in *P. putida*.

### F004 — Lipoylation machinery and a candidate regulator are present
The H-protein lipoylation machinery is encoded: lipA (PP_4800, lipoyl synthase, EC 2.8.1.8) and lipB (PP_4801, octanoyltransferase, EC 2.3.1.181), plus a second predicted lipoyl synthase (PP_4797). SHMT is duplicated (glyA1, glyA2), matching the two *gcv* operons. No gene is named gcvA/gcvR/gcvB/gcsR, but a TyrR-like HTH regulator PP_0997 lies immediately adjacent to operon 1, making it the strongest positional candidate for the GcsR-type activator: "GcsR belongs to a family of transcriptional regulators known as TyrR-like enhancer-binding proteins (EBPs) ... GcsR is the founding member of a new class of TyrR-like EBPs that function in the regulation of" glycine cleavage ([PMID: 27303730](https://pubmed.ncbi.nlm.nih.gov/27303730/)).

---

## 9. Mechanistic Model / Interpretation

```
    Upstream feeders (KEEP SEPARATE)                    GCS CORE MODULE
 ┌─────────────────────────────────────┐        ┌──────────────────────────────────┐
 choline/betaine
   │ betB/betA
   ▼                                                 glycine
 dimethylglycine ──dgcAB──►                           │  P-protein (gcvP1/gcvP2)
 sarcosine ──soxBDAG──► glycine ───────────────►      │  + PLP, − CO2
   (+ 5,10-CH2-THF)                                   ▼
                                                 aminomethyl–[Lip]–H-protein (gcvH1/H2)
 serine ◄──glyA1/glyA2 (SHMT)──► glycine              │  T-protein (gcvT-I/gcvT)
   (+ 5,10-CH2-THF)                                   │  + THF, − NH3
                                                      ▼
                                                 5,10-methylene-THF  +  dihydrolipoyl-H
                                                                          │ L-protein
                                                                          │ (lpdG / lpd / lpdV)
                                                                          ▼  + NAD+
                                                          oxidized-[Lip]-H  +  NADH

 Regulator: PP_0997 (TyrR-like, candidate GcsR) ── activates operon 1
 Lipoylation: lipA + lipB activate the H-protein lipoyl arm
```

The KT2440 GCS is best understood as a **genomically redundant, regulator-controlled glycine catabolic hub**. Two complete P/H/T operons provide the enzymatic core; a single shared, moonlighting E3 closes the redox cycle; lipoylation enzymes activate the H-protein swinging arm; and a TyrR-like regulator (by analogy to *P. aeruginosa* GcsR) likely gates expression in response to glycine availability. The system is embedded in a larger glycine economy in which choline/betaine catabolism and SHMT supply glycine and one-carbon units. The human disease framing (NKH) is biologically irrelevant here and should be removed from the bacterial module.

---

## 10. Evidence Base

| PMID | How it supports the review |
|------|----------------------------|
| [27303730](https://pubmed.ncbi.nlm.nih.gov/27303730/) | Documents a duplicated *gcs2* operon (gcvH2-gcvP2-glyA2-sdaA-gcvT2) in *P. aeruginosa* and establishes GcsR as a TyrR-like enhancer-binding protein regulating the GCS — supports both the two-operon architecture and the PP_0997 regulator hypothesis in KT2440. |
| [23457254](https://pubmed.ncbi.nlm.nih.gov/23457254/) | PA2449 (GcsR) is essential for glycine assimilation and controls a glycine cleavage system, SHMT, and serine dehydratase in *P. aeruginosa* — supports the coupled glycine→pyruvate module logic seen in KT2440 operon 1. |
| [15826505](https://pubmed.ncbi.nlm.nih.gov/15826505/) | Establishes, using *P. putida* E3, that one shared dihydrolipoyl dehydrogenase serves the 2-oxoacid dehydrogenases and the GCS H-protein — direct support for the moonlighting L-protein. |
| [24097953](https://pubmed.ncbi.nlm.nih.gov/24097953/) | Defines the GbdR regulon (dimethylglycine, sarcosine, glycine, serine catabolic enzymes) — supports treating PP_0310–PP_0326 as an upstream glycine feeder distinct from the GCS. |
| [16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/) | Defines the heterotetrameric sarcosine oxidase reaction producing glycine + 5,10-methylene-THF — supports the soxBDAG feeder assignment. |
| [33791923](https://pubmed.ncbi.nlm.nih.gov/33791923/) | Describes human classic NKH genetics (GLDC/AMT) — confirms the disease concept is human-specific and does not transfer to bacteria. |

**Species-transfer assessment.** Regulatory and paralog inferences derive from *P. aeruginosa* PAO1, a congener with strong but not identical physiology — transfer is **moderate-to-strong** for the two-operon architecture and GcsR concept, but the specific KT2440 regulator (PP_0997) and operon division of labor remain unverified. The E3 moonlighting evidence is from *P. putida* itself — transfer is **strong**. All KT2440 *gcv* gene calls are homology-based (PE3); no direct KT2440 experiments exist.

---

## 11. Limitations and Knowledge Gaps

1. **No direct KT2440 experiments.** Every *gcv* gene is UniProt PE3 (homology-inferred). Enzyme activities, operon boundaries, and regulation are predicted, not measured, in KT2440.
2. **L-protein identity unresolved.** Which of lpd/lpdG/lpdV physiologically serves the GCS is not established for KT2440; only lpdG has protein-level evidence, and its complex specificity is not directly demonstrated for the GCS.
3. **Regulator unconfirmed.** PP_0997 is a positional/homology candidate for a GcsR-type activator; no binding-site or expression data exist for KT2440.
4. **Operon division of labor unknown.** The physiological roles/conditions distinguishing operon 1 vs. operon 2 are inferred from *P. aeruginosa*, not measured.
5. **Module framing.** The commissioned module inherits a human disease scope that is inapplicable and could mis-guide bacterial curation if not revised.

---

## 12. Proposed Follow-up Experiments / Actions (Curation)

1. **Promote lpdG (PP_4187) to full review** and cross-reference the 2-oxoacid dehydrogenase and GCS modules; annotate the L-protein step as "shared E3 (moonlighting)" rather than assigning a dedicated gene.
2. **Promote PP_0997 to full review** as candidate GcsR; check for the *P. aeruginosa* GcsR 18-bp consensus (TGTAACG-N4-CGTTCCG) upstream of PP_0986.
3. **Re-scope the module**: rename away from "nonketotic hyperglycinemia"; define scope as bacterial glycine cleavage / glycine catabolism + C1 provision. Mark `module_needs_revision`.
4. **Split feeder module**: create/reference a separate choline-betaine-sarcosine → glycine catabolic module for PP_0310–PP_0326; keep it out of the GCS core.
5. **Record duplication**: annotate both operons (PP_0986–0989 and PP_5192–5194) as covering P/H/T, with a note on potential regulatory divergence.
6. **Experimental resolution (wet-lab, if pursued):** glycine-inducible RT-qPCR of both operons; ΔlpdG/Δlpd/ΔlpdV complementation for GCS activity; ΔPP_0997 to test regulation; in vitro GCS reconstitution to confirm the physiological E3.

---

## 13. Key References

- Sarwar Z. et al. *GcsR, a TyrR-Like Enhancer-Binding Protein, Regulates Expression of the Glycine Cleavage System in Pseudomonas aeruginosa PAO1.* [PMID: 27303730](https://pubmed.ncbi.nlm.nih.gov/27303730/)
- Lundgren B.R. et al. *Gene PA2449 is essential for glycine metabolism and pyocyanin biosynthesis in Pseudomonas aeruginosa PAO1.* [PMID: 23457254](https://pubmed.ncbi.nlm.nih.gov/23457254/)
- *Asparagine-473 residue is important to the efficient function of human dihydrolipoamide dehydrogenase* (P. putida E3 context). [PMID: 15826505](https://pubmed.ncbi.nlm.nih.gov/15826505/)
- Hampel K.J. et al. *Characterization of the GbdR regulon in Pseudomonas aeruginosa.* [PMID: 24097953](https://pubmed.ncbi.nlm.nih.gov/24097953/)
- *Heterotetrameric sarcosine oxidase: structure of a diflavin metalloenzyme at 1.85 Å resolution.* [PMID: 16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/)
- *Genotypic and phenotypic features in Turkish patients with classic nonketotic hyperglycinemia.* [PMID: 33791923](https://pubmed.ncbi.nlm.nih.gov/33791923/)

---

*Prepared as a species-aware module review to support manual satisfiability and gene-annotation curation. Direct KT2440 evidence is homology-based (UniProt PE3); mechanistic and regulatory inferences are transferred from P. aeruginosa (moderate-strong) and P. putida E3 studies (strong), with uncertainties flagged above.*


## Artifacts

- [OpenScientist final report](PSEPK__glycine_cleavage_system__ppu00260-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__glycine_cleavage_system__ppu00260-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27303730
2. PMID:15826505
3. PMID:24097953
4. PMID:33791923
5. PMID:16820168
6. PMID:23457254