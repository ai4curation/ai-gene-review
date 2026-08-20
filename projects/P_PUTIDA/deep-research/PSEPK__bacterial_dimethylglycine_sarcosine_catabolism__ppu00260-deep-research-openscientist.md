---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T00:24:03.915744'
end_time: '2026-08-13T00:49:54.915068'
duration_seconds: 1551.0
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial dimethylglycine and sarcosine catabolism
  module_summary: A reusable two-step bacterial module for sequential N-demethylation
    of dimethylglycine to sarcosine and then glycine. The first reaction may be performed
    by a Pseudomonas-type DgcAB membrane-associated flavin/iron-sulfur system or a
    single-chain dimethylglycine dehydrogenase. The second reaction may use a tetrahydrofolate-coupled
    SoxBDAG heterotetramer or a monomeric sarcosine oxidase. Upstream glycine-betaine
    demethylation and downstream glycine cleavage or serine conversion are outside
    the module boundary.
  module_outline: "- Bacterial dimethylglycine and sarcosine catabolism\n  - 1. dimethylglycine\
    \ demethylation to sarcosine\n  - Dimethylglycine conversion to sarcosine\n  \
    \  - Alternative versions by enzyme architecture: Dimethylglycine dehydrogenase\
    \ architecture\n      - Pseudomonas-type DgcAB system\n        - DgcAB dimethylglycine\
    \ demethylation (molecular player: Pseudomonas-type DgcAB dimethylglycine dehydrogenase;\
    \ activity or role: dimethylglycine demethylation to sarcosine)\n      - Single-chain\
    \ dimethylglycine dehydrogenase\n        - Single-chain dimethylglycine dehydrogenase\
    \ activity (molecular player: DdhC (Chromohalobacter salexigens); activity or\
    \ role: dimethylglycine dehydrogenase activity)\n  - 2. sarcosine demethylation\
    \ to glycine\n  - Sarcosine conversion to glycine\n    - Alternative versions\
    \ by enzyme architecture: Sarcosine oxidase architecture\n      - Tetrahydrofolate-coupled\
    \ SoxABDG heterotetramer\n        - SoxABDG sarcosine oxidase activity (molecular\
    \ player: tetrameric sarcosine oxidase complex; activity or role: sarcosine oxidase\
    \ activity)\n      - Monomeric sarcosine oxidase\n        - Monomeric sarcosine\
    \ oxidase activity (molecular player: monomeric sarcosine oxidase (Arthrobacter\
    \ sp. TE1826); activity or role: sarcosine oxidase activity)"
  module_connections: '- Dimethylglycine conversion to sarcosine feeds into Sarcosine
    conversion to glycine: Sarcosine formed by dimethylglycine demethylation is the
    substrate of sarcosine oxidase.'
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
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_dimethylglycine_sarcosine_catabolism__ppu00260-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_dimethylglycine_sarcosine_catabolism__ppu00260-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial dimethylglycine and sarcosine catabolism in Pseudomonas putida KT2440

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

A reusable two-step bacterial module for sequential N-demethylation of dimethylglycine to sarcosine and then glycine. The first reaction may be performed by a Pseudomonas-type DgcAB membrane-associated flavin/iron-sulfur system or a single-chain dimethylglycine dehydrogenase. The second reaction may use a tetrahydrofolate-coupled SoxBDAG heterotetramer or a monomeric sarcosine oxidase. Upstream glycine-betaine demethylation and downstream glycine cleavage or serine conversion are outside the module boundary.

### Provisional Biological Outline

- Bacterial dimethylglycine and sarcosine catabolism
  - 1. dimethylglycine demethylation to sarcosine
  - Dimethylglycine conversion to sarcosine
    - Alternative versions by enzyme architecture: Dimethylglycine dehydrogenase architecture
      - Pseudomonas-type DgcAB system
        - DgcAB dimethylglycine demethylation (molecular player: Pseudomonas-type DgcAB dimethylglycine dehydrogenase; activity or role: dimethylglycine demethylation to sarcosine)
      - Single-chain dimethylglycine dehydrogenase
        - Single-chain dimethylglycine dehydrogenase activity (molecular player: DdhC (Chromohalobacter salexigens); activity or role: dimethylglycine dehydrogenase activity)
  - 2. sarcosine demethylation to glycine
  - Sarcosine conversion to glycine
    - Alternative versions by enzyme architecture: Sarcosine oxidase architecture
      - Tetrahydrofolate-coupled SoxABDG heterotetramer
        - SoxABDG sarcosine oxidase activity (molecular player: tetrameric sarcosine oxidase complex; activity or role: sarcosine oxidase activity)
      - Monomeric sarcosine oxidase
        - Monomeric sarcosine oxidase activity (molecular player: monomeric sarcosine oxidase (Arthrobacter sp. TE1826); activity or role: sarcosine oxidase activity)

### Known Relationships Among Steps

- Dimethylglycine conversion to sarcosine feeds into Sarcosine conversion to glycine: Sarcosine formed by dimethylglycine demethylation is the substrate of sarcosine oxidase.

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

# Module/Pathway Review: Bacterial Dimethylglycine and Sarcosine Catabolism in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00260 "Glycine, serine and threonine metabolism"
**Module reviewed:** Two-step N-demethylation of dimethylglycine (DMG) → sarcosine → glycine
**Module area:** amino_acid_metabolism

---

## 1. Executive Summary

The two-step catabolic module — sequential N-demethylation of **dimethylglycine (DMG) → sarcosine → glycine** — is **fully satisfiable (COVERED)** in *Pseudomonas putida* KT2440. Both reactions are encoded within a single, synteny-conserved genomic cluster spanning **PP_0310–PP_0326**, which is directly orthologous to the experimentally characterized glycine-betaine catabolic system of *P. aeruginosa* (the *gbcAB*/*dgcAB*/*soxBDAG* loci). Step 1 (DMG → sarcosine) is performed by a **two-subunit, ETF-linked dimethylglycine dehydrogenase, DgcAB** (PP_0310/PP_0311) together with a dedicated electron-transfer flavoprotein EtfAB (PP_0312/PP_0313). Step 2 (sarcosine → glycine) is performed by a **tetrahydrofolate (THF)-coupled heterotetrameric sarcosine oxidase, SoxABDG** (PP_0323–PP_0326). A separate **monomeric sarcosine oxidase, PP_3775** (382 aa), provides an independent second route for step 2. Upstream, KT2440 supplies the module's ultimate substrate via choline → glycine betaine conversion by *betBA* (PP_5064/PP_5063).

The evidence for module satisfiability is **strong by synteny, orthology, and subunit-size transfer**, but it is important for curators to note that it is **not yet backed by KT2440-specific biochemical or mutant experiments**. The direct functional data come from *P. aeruginosa* (Wargo, Willsey) and from *Corynebacterium*/generic bacterial sarcosine oxidase biochemistry (Jorns). Transfer from *P. aeruginosa* is judged **strong** because of near-perfect gene order conservation and matching subunit architecture; transfer from *Corynebacterium* is **moderate** and used only to establish enzyme architecture (heterotetramer vs. monomer), not physiological role.

Two curation-critical caveats emerge. First, the **transcriptional regulators** that gate this module in *P. aeruginosa* — the AraC-family activators **GbdR** (induces *gbcAB*/*dgcAB*) and **SouR** (induces the *sox* operon) — have **no named ortholog** among the 66 candidate genes and are not annotated by name at either the *bet* locus or the catabolic cluster in KT2440; they are trans-encoded and currently unresolved. Second, the candidate list is dominated by **neighboring-pathway genes** of the broad KEGG ppu00260 overview map. Only ~14 of the 66 candidates have any plausible module role; three genes carrying a primary ppu00260 bucket — **PP_4421, PP_4423, PP_4432** — appear to be **over-propagated bucket assignments** with no DMG/sarcosine function. The single-chain dimethylglycine dehydrogenase alternative (DdhC of *Chromohalobacter salexigens*) is **not expected** in this taxon; KT2440 uses the two-subunit DgcAB architecture.

---

## 2. Target-Organism Pathway Definition

### 2.1 Exact biochemical process included in the module

The module comprises exactly two oxidative N-demethylation reactions:

1. **DMG → sarcosine** (removal of one N-methyl group from dimethylglycine), catalyzed by an ETF-coupled dimethylglycine dehydrogenase (EC 1.5.8.-).
2. **Sarcosine (N-methylglycine) → glycine** (removal of the final N-methyl group), catalyzed by sarcosine oxidase (EC 1.5.3.1 for the classical oxidase; EC 1.5.3.24 for the 5,10-methylenetetrahydrofolate-forming heterotetramer).

Both reactions release a one-carbon unit. In the THF-coupled heterotetrameric sarcosine oxidase, the released C1 is captured as **5,10-methylene-tetrahydrofolate**; H₂O₂ is co-produced.

### 2.2 Neighboring pathways to keep separate

The following processes are **outside the module boundary** and should be kept distinct during curation, even though many of their genes appear in the ppu00260 bucket:

- **Upstream glycine-betaine demethylation** (glycine betaine → DMG), catalyzed by the Rieske-type glycine-betaine monooxygenase GbcAB (PP_0315/PP_0316). This is the *feeder* reaction, not part of the two-step module itself.
- **Choline → glycine betaine** (BetA/BetB; PP_5064/PP_5063) — an upstream supply route.
- **Downstream glycine disposal**: the glycine cleavage system (GcvP/H/T + Lpd) and serine hydroxymethyltransferase (GlyA), which consume glycine and the C1 units. These are explicitly outside the module.
- **Threonine biosynthesis** (ThrB, Hom, ThrC), **serine biosynthesis** (SerA/SerB/SerC), and various **serine/threonine dehydratases** (TdcG, IlvA paralogs) — these share the ppu00260 overview map but have no mechanistic connection to DMG/sarcosine catabolism.

### 2.3 Alternate names and database definitions

- KEGG map **ppu00260** = "Glycine, serine and threonine metabolism" — a **broad overview map**, not a module. The DMG/sarcosine steps are a small sub-portion.
- The *P. aeruginosa* orthologs are named after **glycine betaine catabolism** (*gbc*, *dgc*, *sox*, *sou*).
- The heterotetrameric enzyme is variously called **"tetrameric sarcosine oxidase" (TSOX)**, "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming)" (EC 1.5.3.24), or **SoxBDAG/SoxABDG**.
- The single-domain enzyme is called **monomeric sarcosine oxidase (MSOX)** (EC 1.5.3.1).

---

## 3. Expected Step Model

```
   choline
     │  betA/betB (PP_5064 / PP_5063)      [upstream supply — outside module]
     ▼
 glycine betaine (GB)
     │  gbcAB (PP_0315 / PP_0316)          [feeder — outside module boundary]
     ▼
 dimethylglycine (DMG)
     │                                     ┌─────────────────────────────┐
     │  STEP 1: DMG → sarcosine            │  MODULE STEP 1              │
     │  dgcA/dgcB (PP_0310 / PP_0311)      │  ETF-linked DgcAB           │
     │  + EtfAB (PP_0312 / PP_0313)        │  EC 1.5.8.-                 │
     ▼                                     └─────────────────────────────┘
   sarcosine (N-methylglycine)
     │                                     ┌─────────────────────────────┐
     │  STEP 2: sarcosine → glycine        │  MODULE STEP 2              │
     │  ROUTE A: soxABDG                   │  THF-coupled heterotetramer │
     │           (PP_0323–PP_0326)         │  EC 1.5.3.24                │
     │  ROUTE B: PP_3775 (monomeric MSOX)  │  EC 1.5.3.1                 │
     ▼                                     └─────────────────────────────┘
   glycine  (+ 5,10-CH2-THF, H2O2)
     │  glyA (PP_0322), gcv system         [downstream sink — outside module]
     ▼
 one-carbon / central metabolism
```

Both module steps have candidate genes; step 2 has **two independent architectures** encoded. The C1 by-products are disposed of by a conserved downstream signature: **PP_0327 (purU, formyltetrahydrofolate deformylase)** and **PP_0328 (formaldehyde dehydrogenase)**, immediately downstream of *soxG*.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence module genes (the PP_0310–PP_0326 cluster)

| Gene | Locus | UniProt | Role in module | Architecture evidence | Curation status |
|------|-------|---------|----------------|-----------------------|-----------------|
| dgcA | PP_0310 | Q88R24 | DMG → sarcosine, catalytic subunit | 686 aa flavoprotein | **Covered** (Step 1) |
| dgcB | PP_0311 | Q88R23 | DMG → sarcosine, catalytic subunit | 650 aa flavoprotein | **Covered** (Step 1) |
| PP_0312 | PP_0312 | Q88R22 | ETF α (electron acceptor) | 410 aa | Covered (Step 1 partner) |
| PP_0313 | PP_0313 | Q88R21 | ETF β (electron acceptor) | 256 aa | Covered (Step 1 partner) |
| gbcA | PP_0315 | Q88R19 | GB → DMG (feeder, Rieske oxygenase) | EC 1.13.-.- | Outside module (upstream) |
| gbcB | PP_0316 | Q88R18 | GB → DMG (feeder, reductase) | EC 1.13.-.- | Outside module (upstream) |
| ltaE | PP_0321 | Q88R13 | L-threonine aldolase | EC 4.1.2.48 | Boundary/co-located, not a demethylase |
| glyA1 | PP_0322 | Q88R12 | SHMT (consumes 5,10-CH2-THF) | EC 2.1.2.1 | Boundary (C1 coupling), outside module |
| soxB | PP_0323 | Q88R11 | Sarcosine oxidase β subunit | 416 aa; EC 1.5.3.24 | **Covered** (Step 2, Route A) |
| soxD | PP_0324 | Q88R10 | Sarcosine oxidase δ subunit | 111 aa | **Covered** (Step 2, Route A) |
| soxA | PP_0325 | Q88R09 | Sarcosine oxidase α subunit | 1004 aa; EC 1.5.3.1 | **Covered** (Step 2, Route A) |
| soxG | PP_0326 | Q88R08 | Sarcosine oxidase γ subunit | 210 aa | **Covered** (Step 2, Route A) |
| PP_3775 | PP_3775 | Q88GE9 | Monomeric sarcosine oxidase | 382 aa; EC 1.5.3.1 | **Covered** (Step 2, Route B) |

### 4.2 Step 1 — DMG → sarcosine (DgcAB + ETF)

Direct KT2440 proteome data (UP000000556) show that **DgcA (PP_0310, 686 aa)** and **DgcB (PP_0311, 650 aa)** are two large flavoprotein subunits, immediately followed by a dedicated **EtfA (PP_0312, 410 aa)** and **EtfB (PP_0313, 256 aa)**. This is the **two-component, "Pseudomonas-type" ETF-coupled dimethylglycine dehydrogenase** (EC 1.5.8.-), NOT a single polypeptide. The functional assignment transfers from *P. aeruginosa*, where mutations in *dgcAB* (PA5398–PA5399) abolish conversion of DMG to sarcosine [PMID: 17951379]. Because KT2440 encodes the two-subunit architecture with a dedicated ETF, the **single-chain dimethylglycine dehydrogenase alternative** (DdhC of *Chromohalobacter salexigens*) is **not expected** in this taxon.

### 4.3 Step 2 — sarcosine → glycine (SoxABDG heterotetramer)

The KT2440 gene order **glyA1(PP_0322)–soxB(PP_0323)–soxD(PP_0324)–soxA(PP_0325)–soxG(PP_0326)** reproduces the characterized *Corynebacterium* heterotetrameric sarcosine oxidase operon *glyA-soxBDAG* [PMID: 7543100]. This (αβγδ) enzyme carries both covalent and noncovalent FAD and **oxidatively demethylates sarcosine to glycine, H₂O₂, and 5,10-CH₂-tetrahydrofolate in an H₄folate/O₂-dependent reaction**. UniProt annotations are consistent: soxB (Q88R11) carries EC 1.5.3.24, "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming)." Subunit sizes match the characterized TSOX profile: KT2440 SoxA (1004 aa) vs. TSOX α (967 aa); SoxB (416 aa) vs. TSOX β (405 aa) [PMID: 7543100]. Functional role transfers from *P. aeruginosa*, where *soxBDAG* is required for sarcosine catabolism [PMID: 17951379].

### 4.4 Step 2, Route B — monomeric sarcosine oxidase (PP_3775)

**PP_3775 (Q88GE9, 382 aa)** is annotated as a standalone monomeric sarcosine oxidase (EC 1.5.3.1). Its size matches the MSOX class ("approximately 388 residues") [PMID: 7543100], and it lies outside the *soxABDG* operon. KT2440 therefore encodes **both** sarcosine-oxidase architectures — the THF-coupled heterotetramer and a standalone monomeric oxidase — giving redundancy for module step 2.

### 4.5 Upstream supply (outside module but relevant)

**BetB (PP_5063)** and **BetA (PP_5064)** convert choline to glycine betaine, the ultimate substrate feeding the pathway; KT2440 *betBA* is functionally required for choline → glycine betaine transformation [PMID: 17116241]. **GbcAB (PP_0315/PP_0316)** then demethylates glycine betaine to DMG (feeder reaction).

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Regulatory gap (module gating, trans-encoded)

The module is transcriptionally gated in *P. aeruginosa* by two AraC-family regulators: **GbdR** (PA5380), required for growth on GB/DMG and for induction of *gbcA/gbcB/dgcAB* [PMID: 17951379], and **SouR** (PA4184), the sarcosine-specific activator of the *sox* operon, required for appreciable growth on sarcosine as C/N source [PMID: 26503852]. A direct UniProt scan of KT2440 found **no named GbdR or SouR ortholog** among the 66 candidates. The *bet* neighborhood (PP_5058–PP_5068) and the catabolic cluster (PP_0308–PP_0328) contain **no AraC-family regulator** — intervening ORFs are chemotaxis MCPs (PP_0317, PP_0320) and hypotheticals. A genome-wide scan returned ~10 AraC-family regulators (e.g., PP_0298, PP_3665, PP_3659, PP_4508, PP_4511, PP_4852, PP_3149, PP_2425, PP_2173, PP_0876), none named *gbdR*/*souR*. **Regulation is trans-encoded and unresolved** — a real curation gap.

### 5.2 Likely over-propagated ppu00260 assignments

Three genes carry a primary bucket of kegg:ppu00260 but have no plausible DMG/sarcosine role and are not in the catabolic cluster:

| Gene | Locus | Annotation | Assessment |
|------|-------|-----------|------------|
| PP_4421 | PP_4421 | Aminotransferase (EC 2.6.1.-, broad) | Over-propagated; broad EC, no module role |
| PP_4423 | PP_4423 | Succinylglutamate desuccinylase / aspartoacylase domain | Over-propagated; no module role |
| PP_4432 | PP_4432 | Xaa-Pro aminopeptidase | Over-propagated; no module role |

These appear to be **over-inclusive bucket assignments** and should be **excluded from the module**.

### 5.3 Neighboring-pathway genes (majority of candidates)

Of the 66 candidates, the majority belong to separable neighboring processes of the broad ppu00260 map: threonine biosynthesis (*thrB* PP_0121, *hom* PP_1470, *thrC* PP_1471, PP_0662, PP_0664), serine biosynthesis (*serA* PP_5155, *serB* PP_4909, *serC* PP_1768), the glycine cleavage system (*gcvP1/H1/T-I* PP_0986–0989, *gcvP2/H2/T* PP_5192–5194, *lpd* PP_5366), serine/threonine dehydratases (*tdcG* PP_0297/0987/3144, *ilvA* PP_3446/5149, PP_3191/PP_4430/PP_2930), and phospholipid/one-carbon side reactions. **None of these are module enzymes.**

### 5.4 Paralog/architecture ambiguity to flag

- **glyA1 (PP_0322)** is physically embedded in the *sox* operon and functionally coupled to sarcosine oxidase (it consumes the 5,10-CH₂-THF product), but it is a **boundary/one-carbon enzyme**, not a demethylation step [PMID: 7543100]. **glyA2 (PP_0671)** is a second SHMT paralog elsewhere in the genome — do not conflate.
- **SoxB shares homology** with the N-terminal half of dimethylglycine dehydrogenase and with monomeric sarcosine oxidases [PMID: 7543100]; this homology is the root cause of potential annotation over-propagation between DgcAB, SoxB, and PP_3775. Curators should keep the **operon context** as the deciding feature.

---

## 6. Module and GO-Curation Recommendations

### 6.1 Module step status

| Module step | Status | Basis |
|-------------|--------|-------|
| Step 1: DMG → sarcosine | **covered** | DgcAB (PP_0310/PP_0311) + EtfAB (PP_0312/PP_0313); orthology + synteny + subunit sizes |
| Step 2: sarcosine → glycine (Route A, heterotetramer) | **covered** | SoxABDG (PP_0323–PP_0326); operon architecture + EC 1.5.3.24 |
| Step 2: sarcosine → glycine (Route B, monomeric) | **covered (redundant)** | PP_3775 (382 aa, EC 1.5.3.1) |
| Single-chain DMG dehydrogenase alternative | **not_expected_in_target_taxon** | KT2440 uses two-subunit DgcAB, not DdhC-type |
| Module regulation (GbdR/SouR) | **candidate_uncertain / gap** | No named ortholog in candidate list; trans-encoded, unannotated |

**Overall module verdict: COVERED.**

### 6.2 Module boundary recommendations

- The generic module boundary (DMG → sarcosine → glycine, excluding upstream GB demethylation and downstream glycine cleavage/serine conversion) is **correct for this organism** — no boundary revision needed for the core two steps.
- Recommend **explicitly documenting the two alternative architectures for step 2** (heterotetramer SoxABDG vs. monomeric MSOX) as both are realized in KT2440.
- Recommend **noting the trans-encoded regulatory dependency** (GbdR/SouR-type) as a module annotation, even though the regulators are outside the operon.

### 6.3 GO-curation

- Assign SoxABDG subunits to GO "sarcosine oxidase activity" and the 5,10-methylenetetrahydrofolate-forming reaction; DgcAB to dimethylglycine dehydrogenase activity (ETF-coupled).
- Flag PP_4421/PP_4423/PP_4432 for **removal of ppu00260 module association** (retain their genuine independent annotations).
- No new GO term request appears strictly necessary; existing EC 1.5.8.-, 1.5.3.1, and 1.5.3.24 terms cover the reactions.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Prioritized for full individual review:

1. **PP_0310 (dgcA)** and **PP_0311 (dgcB)** — confirm ETF-coupled DMG dehydrogenase catalytic assignment and EC 1.5.8.- refinement.
2. **PP_0323–PP_0326 (soxBDAG)** — confirm heterotetramer stoichiometry and the EC 1.5.3.24 (THF-forming) designation vs. generic 1.5.3.1.
3. **PP_3775** — confirm genuine monomeric sarcosine oxidase and rule out over-propagation from operon homology.
4. **Candidate regulator search** — promote a targeted review to identify the KT2440 GbdR/SouR functional equivalents among the ~10 AraC-family regulators (start with those genomically or regulon-linked; e.g., PP_0298 lies near the cluster).
5. **PP_4421, PP_4423, PP_4432** — promote for **de-association** review (confirm they should be dropped from the module bucket).

---

## 8. Mechanistic Model and Interpretation

The KT2440 locus reconstructs, almost gene-for-gene, the *P. aeruginosa* glycine-betaine catabolic devolution: choline → glycine betaine (BetBA) → DMG (GbcAB) → sarcosine (DgcAB+ETF) → glycine (SoxABDG). The clustering of *ltaE* and *glyA1* within the *sox* region is not incidental — SHMT (GlyA1) directly recycles the 5,10-CH₂-THF released by the THF-coupled sarcosine oxidase, tying the demethylation module to one-carbon metabolism. The conserved downstream **purU (PP_0327)** and **formaldehyde dehydrogenase (PP_0328)** provide a disposal route for excess C1 units and formaldehyde, reproducing the syntenic *purU* signature reported downstream of the *Corynebacterium sox* operon [PMID: 7543100]. This C1-disposal signature strengthens confidence that the KT2440 cluster is a bona fide, coordinately organized demethylation pathway rather than a fortuitous gene neighborhood.

The redundancy at step 2 (heterotetramer + monomeric MSOX) suggests the organism can process sarcosine under multiple conditions, but only the operon-embedded SoxABDG is expected to be co-regulated with the upstream steps. The monomeric PP_3775 likely serves a distinct or overlapping physiological niche and may respond to a different (possibly SouR-like) signal.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | How it supports the review |
|------|-----------------|----------------------------|
| [PMID: 17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/) | Two gene clusters + regulator for *P. aeruginosa* glycine betaine catabolism | Direct functional proof that *dgcAB* converts DMG→sarcosine and *soxBDAG* is required for sarcosine catabolism; establishes GbdR as activator. Primary orthology source (transfer to KT2440 **strong**). |
| [PMID: 7543100](https://pubmed.ncbi.nlm.nih.gov/7543100/) | Sequence analysis of sarcosine oxidase and nearby genes | Defines the *glyA-soxBDAG* heterotetramer operon, the THF/O₂-dependent reaction, subunit sizes, MSOX size class, and the downstream *purU* signature (transfer **moderate**, architecture only). |
| [PMID: 26503852](https://pubmed.ncbi.nlm.nih.gov/26503852/) | Sarcosine catabolism regulated by SouR | Establishes SouR as the sarcosine-specific *sox* operon activator, required for growth on sarcosine — basis for the regulatory gap. |
| [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/) | Choline-O-sulphate utilization in *P. putida* | Direct KT2440 evidence that *betBA* produces glycine betaine — the upstream substrate feeding the module (transfer **direct**). |
| [PMID: 19103776](https://pubmed.ncbi.nlm.nih.gov/19103776/) | GbdR regulates *plcH*/*pchP* | Corroborates GbdR as an AraC-family regulator responsive to choline catabolites, informing the regulator search. |
| [PMID: 29703733](https://pubmed.ncbi.nlm.nih.gov/29703733/) | Glycine betaine monooxygenase (Rieske-type) | Characterizes the GbcAB-type oxygenase mechanism (upstream feeder). |
| [PMID: 10689197](https://pubmed.ncbi.nlm.nih.gov/10689197/) | Stachydrine catabolism in *S. meliloti* | Comparative context for betaine N-demethylation via Rieske-type systems in other bacteria. |

**Strongest transfer:** *P. aeruginosa* (near-identical gene order and architecture). **Direct KT2440 evidence:** limited to *betBA* function and to genomic/proteomic locus data. **No KT2440-specific mutant or enzymatic data** exist for *dgcAB* or *soxBDAG* themselves.

---

## 10. Limitations and Knowledge Gaps

1. **No KT2440-specific functional experiments** for the core module enzymes (DgcAB, SoxABDG). All catalytic assignments rest on orthology/synteny to *P. aeruginosa* and architecture transfer from *Corynebacterium*. Confidence is high but not experimentally proven in the target strain.
2. **Regulators unresolved.** The GbdR/SouR functional equivalents in KT2440 are not identified by name; whether the module is inducible in KT2440 as in *P. aeruginosa* is inferred, not shown.
3. **Redundancy physiology unknown.** The relative contribution of SoxABDG vs. monomeric PP_3775 to sarcosine catabolism in KT2440 is undetermined.
4. **EC precision.** Whether the KT2440 heterotetramer is strictly the 5,10-CH₂-THF-forming enzyme (EC 1.5.3.24) versus the generic oxidase (EC 1.5.3.1) is inferred from soxB annotation and homology.
5. **Bucket noise.** The ppu00260 candidate list conflates the module with a large overview map; curators must apply operon/synteny filters manually.

---

## 11. Proposed Follow-up Experiments and Curation Actions

1. **Growth phenotyping:** Test KT2440 growth on DMG and on sarcosine as sole C/N sources; construct *dgcAB* and *soxABDG* deletion mutants to confirm each step (mirrors the *P. aeruginosa* experiments).
2. **Regulator identification:** Use transcriptomics (RNA-seq on GB/DMG/sarcosine) plus promoter-reporter assays to identify which of the ~10 KT2440 AraC-family regulators activate the cluster; test PP_0298 first (proximity to the cluster).
3. **Enzymology:** Purify SoxABDG and confirm THF-dependence and 5,10-CH₂-THF production (distinguishing EC 1.5.3.24 from 1.5.3.1); assay PP_3775 for THF-independent sarcosine oxidase activity.
4. **Curation actions:** Mark module steps 1 and 2 as **covered**; mark the single-chain DMG dehydrogenase alternative as **not_expected_in_target_taxon**; document dual step-2 architectures; flag PP_4421/PP_4423/PP_4432 for de-association from the module; add a trans-encoded-regulator note.
5. **Promote to `fetch-gene` review:** PP_0310, PP_0311, PP_0323–PP_0326, PP_3775, and a regulator-candidate review.

---

## 12. Key References

- Wargo MJ, et al. *Identification of two gene clusters and a transcriptional regulator required for Pseudomonas aeruginosa glycine betaine catabolism.* [PMID: 17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/)
- Chlumsky LJ, Zhang L, Jorns MS. *Sequence analysis of sarcosine oxidase and nearby genes reveals homologies with key enzymes of folate one-carbon metabolism.* [PMID: 7543100](https://pubmed.ncbi.nlm.nih.gov/7543100/)
- Willsey GG, Wargo MJ. *Sarcosine Catabolism in Pseudomonas aeruginosa Is Transcriptionally Regulated by SouR.* [PMID: 26503852](https://pubmed.ncbi.nlm.nih.gov/26503852/)
- Galvão TC, et al. *Uncoupling of choline-O-sulphate utilization from osmoprotection in Pseudomonas putida.* [PMID: 17116241](https://pubmed.ncbi.nlm.nih.gov/17116241/)
- Wargo MJ, et al. *GbdR regulates Pseudomonas aeruginosa plcH and pchP transcription in response to choline catabolites.* [PMID: 19103776](https://pubmed.ncbi.nlm.nih.gov/19103776/)
- *Glycine Betaine Monooxygenase, an Unusual Rieske-Type Oxygenase System.* [PMID: 29703733](https://pubmed.ncbi.nlm.nih.gov/29703733/)
- *The stachydrine catabolism region in Sinorhizobium meliloti.* [PMID: 10689197](https://pubmed.ncbi.nlm.nih.gov/10689197/)


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_dimethylglycine_sarcosine_catabolism__ppu00260-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_dimethylglycine_sarcosine_catabolism__ppu00260-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17951379
2. PMID:7543100
3. PMID:17116241
4. PMID:26503852
5. PMID:19103776
6. PMID:29703733
7. PMID:10689197