---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T13:55:25.047559'
end_time: '2026-07-25T14:12:39.915294'
duration_seconds: 1034.87
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: APS-dependent assimilatory sulfate reduction
  module_summary: A reusable pathway that converts sulfate to sulfide through adenosine
    5'-phosphosulfate (APS) and sulfite. The module contains sulfate activation by
    ATP sulfurylase, thioredoxin-dependent APS reduction, and assimilatory sulfite
    reduction. It represents the direct APS branch rather than the alternative APS-kinase/PAPS-reductase
    route. Sulfate import is upstream, whereas siroheme synthesis and incorporation
    of sulfide into cysteine are supporting or downstream biology outside the pathway
    boundary.
  module_outline: "- APS-dependent assimilatory sulfate reduction\n  - 1. sulfate\
    \ activation\n  - Sulfate activation to APS\n    - CysD/CysN ATP sulfurylase (molecular\
    \ player: proteobacterial CysD/CysN ATP sulfurylase; activity or role: sulfate\
    \ adenylyltransferase (ATP) activity)\n  - 2. APS reduction\n  - APS reduction\
    \ to sulfite\n    - Thioredoxin-dependent APS reductase (molecular player: CysH\
    \ APS reductases; activity or role: adenylyl-sulfate reductase (thioredoxin) activity)\n\
    \  - 3. sulfite reduction\n  - Assimilatory reduction of sulfite to sulfide\n\
    \    - Alternative versions by immediate electron-transfer system: Sulfite-reductase\
    \ electron-donor architecture\n      - Ferredoxin/Fpr-fed CysI route\n       \
    \ - Ferredoxin-dependent CysI activity (molecular player: ferredoxin-dependent\
    \ assimilatory CysI proteins; activity or role: sulfite reductase (ferredoxin)\
    \ activity)\n        - Fpr electron supply (molecular player: bacterial type-1\
    \ ferredoxin--NADP reductases; activity or role: ferredoxin-NADP+ reductase activity)\n\
    \      - CysJ/CysI NADPH-dependent route\n        - CysJ/CysI NADPH sulfite reductase\
    \ (molecular player: CysJ/CysI sulfite reductase complex; activity or role: sulfite\
    \ reductase (NADPH) activity)"
  module_connections: '- Sulfate activation to APS feeds into APS reduction to sulfite:
    ATP sulfurylase supplies APS to CysH.

    - APS reduction to sulfite feeds into Assimilatory reduction of sulfite to sulfide:
    CysH supplies sulfite to the terminal sulfite-reduction system.'
  pathway_query: ppu00920
  pathway_id: ppu00920
  pathway_name: Sulfur metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00920 with 33 primary genes; module
    area: energy_respiration_inorganic_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '54'
  candidate_genes: '- PP_0053: PP_0053 | Q88RS6 | Sulfide:quinone oxidoreductase (primary
    bucket kegg:ppu00920)

    - PP_0170: PP_0170 | Q88RG0 | ABC transporter, periplasmic binding protein (primary
    bucket kegg:ppu00920)

    - PP_0171: PP_0171 | Q88RF9 | ABC transporter, ATP-binding protein (primary bucket
    kegg:ppu00920)

    - PP_0172: PP_0172 | Q88RF8 | ABC transporter, permease protein (primary bucket
    kegg:ppu00920)

    - PP_0207: PP_0207 | Q88RC5 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - PP_0208: PP_0208 | Q88RC4 | Nitrate ABC transporter, permease protein (primary
    bucket kegg:ppu00920)

    - tauB-I: PP_0209 | Q88RC3 | ATP-binding taurine transporter subunit (EC 3.6.3.36)
    (EC 3.6.3.36; primary bucket kegg:ppu00920)

    - PP_0228: PP_0228 | Q88RA5 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - tauD: PP_0230 | Q88RA3 | Alpha-ketoglutarate-dependent taurine dioxygenase (EC
    1.14.11.17) (EC 1.14.11.17; primary bucket kegg:ppu00430)

    - tauC: PP_0231 | Q88RA2 | Taurine ABC transporter permease subunit (EC 3.6.3.36)
    (EC 3.6.3.36; primary bucket kegg:ppu00920)

    - tauB: PP_0232 | Q88RA1 | Taurine import ATP-binding protein TauB (EC 7.6.2.7)
    (EC 7.6.2.7; primary bucket kegg:ppu00920)

    - tauA: PP_0233 | Q88RA0 | Taurine ABC transporter periplasmic binding subunit
    (primary bucket kegg:ppu00920)

    - ssuE: PP_0236 | Q88R97 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase)
    (EC 1.5.1.38; primary bucket kegg:ppu00740)

    - ssuA: PP_0237 | Q88R96 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - ssuD: PP_0238 | Q88R95 | Alkanesulfonate monooxygenase (EC 1.14.14.5) (FMNH2-dependent
    aliphatic sulfonate monooxygenase) (EC 1.14.14.5; primary bucket kegg:ppu00920)

    - ssuC: PP_0239 | Q88R94 | Aliphatic sulfonate ABC transporter-permease subunit
    / transport of isethionate (primary bucket kegg:ppu00920)

    - ssuB: PP_0240 | Q88R93 | Aliphatic sulfonates import ATP-binding protein SsuB
    (EC 7.6.2.14) (EC 7.6.2.14; primary bucket kegg:ppu00920)

    - cysQ: PP_0261 | Q88R73 | 3''(2''),5''-bisphosphate nucleotidase CysQ (EC 3.1.3.7)
    (3''(2''),5-bisphosphonucleoside 3''(2'')-phosphohydrolase) (3''-phosphoadenosine
    5''-phosphate phosphatase) (PAP phosphatase) (EC 3.1.3.7; primary bucket kegg:ppu00920)

    - PP_0368: PP_0368 | Q88QW6 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC
    1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)

    - PP_0370: PP_0370 | Q88QW4 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC
    1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)

    - glpE: PP_0398 | Q88QT9 | Thiosulfate sulfurtransferase GlpE (EC 2.8.1.1) (EC
    2.8.1.1; primary bucket kegg:ppu00920)

    - metB: PP_0659 | Q88Q39 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)

    - cysE: PP_0840 | Q88PL0 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - PP_0860: PP_0860 | Q88PJ0 | Sulfite reductase, flavoprotein component (primary
    bucket kegg:ppu01320)

    - PP_1110: PP_1110 | Q88NU4 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - cysD: PP_1303 | Q88NA9 | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4)
    (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4;
    primary bucket kegg:ppu00261)

    - cysNC: PP_1304 | Q88NA8 | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4)
    (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4;
    primary bucket kegg:ppu00261)

    - PP_1703: PP_1703 | Q88M71 | Assimilatory nitrate reductase/sulfite reductase
    (EC 1.7.99.4) (EC 1.7.99.4; primary bucket kegg:ppu01320)

    - metZ: PP_2001 | Q88LD4 | O-succinylhomoserine sulfhydrylase (OSH sulfhydrylase)
    (OSHS sulfhydrylase) (EC 2.5.1.-) (EC 2.5.1.-; primary bucket kegg:ppu00270)

    - PP_2048: PP_2048 | Q88L87 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC
    1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)

    - cysH: PP_2328 | Q88KG2 | Adenosine 5''-phosphosulfate reductase (APS reductase)
    (EC 1.8.4.10) (5''-adenylylsulfate reductase) (Thioredoxin-dependent 5''-adenylylsulfate
    reductase) (EC 1.8.4.10; primary bucket kegg:ppu01320)

    - cysI: PP_2371 | Q88KB9 | Sulphite reductase hemoprotein, beta subunit (primary
    bucket kegg:ppu01320)

    - PP_2677: PP_2677 | Q88JH2 | Quinoprotein dehydrogenase-associated SoxYZ-like
    carrier (primary bucket kegg:ppu01320)

    - msuE: PP_2764 | Q88J85 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase)
    (EC 1.5.1.38; primary bucket kegg:ppu00740)

    - PP_2765: PP_2765 | Q88J84 | Sulfonate monooxygenase MsuD (primary bucket kegg:ppu00920)

    - PP_2795: PP_2795 | Q88J54 | AMP-binding domain protein (primary bucket kegg:ppu00920)

    - PP_3136: PP_3136 | Q88I65 | Serine acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - PP_3217: PP_3217 | Q88HY6 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - PP_3219: PP_3219 | Q88HY4 | Alkansulfonate monooxygenase (primary bucket kegg:ppu00920)

    - PP_3228: PP_3228 | Q88HX5 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - PP_3229: PP_3229 | Q88HX4 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - PP_3528: PP_3528 | Q88H37 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - PP_3553: PP_3553 | Q88H12 | AMP-binding domain protein (primary bucket kegg:ppu00920)

    - PP_3554: PP_3554 | Q88H11 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC
    1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)

    - PP_3822: PP_3822 | Q88GA3 | Cytochrome c family protein (primary bucket kegg:ppu01320)

    - sbp-I: PP_4305 | Q88EZ5 | Sulfate ABC transporter (primary bucket kegg:ppu00920)

    - cysK: PP_4571 | Q88E95 | Cysteine synthase (EC 2.5.1.47) (EC 2.5.1.47; primary
    bucket kegg:ppu01320)

    - rhdA: PP_4907 | Q88DC0 | Sulfurtransferase (primary bucket kegg:ppu04122)

    - metXS: PP_5097 | Q88CT3 | Homoserine O-succinyltransferase (HST) (EC 2.3.1.46)
    (Homoserine transsuccinylase) (HTS) (EC 2.3.1.46; primary bucket kegg:ppu00270)

    - sseA: PP_5118 | Q88CR2 | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) (EC
    2.8.1.2; primary bucket kegg:ppu04122)

    - cysA: PP_5168 | Q88CL2 | Sulfate/thiosulfate import ATP-binding protein CysA
    (EC 7.3.2.3) (Sulfate-transporting ATPase) (EC 7.3.2.3; primary bucket kegg:ppu00920)

    - cysW: PP_5169 | Q88CL1 | Sulfate transport system permease protein CysW (primary
    bucket kegg:ppu00920)

    - cysU: PP_5170 | Q88CL0 | Sulfate transport system permease protein CysT (primary
    bucket kegg:ppu00920)

    - sbp-II: PP_5171 | Q88CK9 | Sulfate ABC transporter (primary bucket kegg:ppu00920)'
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
  path: PSEPK__aps_dependent_assimilatory_sulfate_reduction__ppu00920-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__aps_dependent_assimilatory_sulfate_reduction__ppu00920-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

APS-dependent assimilatory sulfate reduction in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00920
- Resolved ID: ppu00920
- Resolved name: Sulfur metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00920 with 33 primary genes; module area: energy_respiration_inorganic_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 54

- PP_0053: PP_0053 | Q88RS6 | Sulfide:quinone oxidoreductase (primary bucket kegg:ppu00920)
- PP_0170: PP_0170 | Q88RG0 | ABC transporter, periplasmic binding protein (primary bucket kegg:ppu00920)
- PP_0171: PP_0171 | Q88RF9 | ABC transporter, ATP-binding protein (primary bucket kegg:ppu00920)
- PP_0172: PP_0172 | Q88RF8 | ABC transporter, permease protein (primary bucket kegg:ppu00920)
- PP_0207: PP_0207 | Q88RC5 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- PP_0208: PP_0208 | Q88RC4 | Nitrate ABC transporter, permease protein (primary bucket kegg:ppu00920)
- tauB-I: PP_0209 | Q88RC3 | ATP-binding taurine transporter subunit (EC 3.6.3.36) (EC 3.6.3.36; primary bucket kegg:ppu00920)
- PP_0228: PP_0228 | Q88RA5 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- tauD: PP_0230 | Q88RA3 | Alpha-ketoglutarate-dependent taurine dioxygenase (EC 1.14.11.17) (EC 1.14.11.17; primary bucket kegg:ppu00430)
- tauC: PP_0231 | Q88RA2 | Taurine ABC transporter permease subunit (EC 3.6.3.36) (EC 3.6.3.36; primary bucket kegg:ppu00920)
- tauB: PP_0232 | Q88RA1 | Taurine import ATP-binding protein TauB (EC 7.6.2.7) (EC 7.6.2.7; primary bucket kegg:ppu00920)
- tauA: PP_0233 | Q88RA0 | Taurine ABC transporter periplasmic binding subunit (primary bucket kegg:ppu00920)
- ssuE: PP_0236 | Q88R97 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- ssuA: PP_0237 | Q88R96 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- ssuD: PP_0238 | Q88R95 | Alkanesulfonate monooxygenase (EC 1.14.14.5) (FMNH2-dependent aliphatic sulfonate monooxygenase) (EC 1.14.14.5; primary bucket kegg:ppu00920)
- ssuC: PP_0239 | Q88R94 | Aliphatic sulfonate ABC transporter-permease subunit / transport of isethionate (primary bucket kegg:ppu00920)
- ssuB: PP_0240 | Q88R93 | Aliphatic sulfonates import ATP-binding protein SsuB (EC 7.6.2.14) (EC 7.6.2.14; primary bucket kegg:ppu00920)
- cysQ: PP_0261 | Q88R73 | 3'(2'),5'-bisphosphate nucleotidase CysQ (EC 3.1.3.7) (3'(2'),5-bisphosphonucleoside 3'(2')-phosphohydrolase) (3'-phosphoadenosine 5'-phosphate phosphatase) (PAP phosphatase) (EC 3.1.3.7; primary bucket kegg:ppu00920)
- PP_0368: PP_0368 | Q88QW6 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)
- PP_0370: PP_0370 | Q88QW4 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)
- glpE: PP_0398 | Q88QT9 | Thiosulfate sulfurtransferase GlpE (EC 2.8.1.1) (EC 2.8.1.1; primary bucket kegg:ppu00920)
- metB: PP_0659 | Q88Q39 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)
- cysE: PP_0840 | Q88PL0 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- PP_0860: PP_0860 | Q88PJ0 | Sulfite reductase, flavoprotein component (primary bucket kegg:ppu01320)
- PP_1110: PP_1110 | Q88NU4 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- cysD: PP_1303 | Q88NA9 | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4; primary bucket kegg:ppu00261)
- cysNC: PP_1304 | Q88NA8 | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4; primary bucket kegg:ppu00261)
- PP_1703: PP_1703 | Q88M71 | Assimilatory nitrate reductase/sulfite reductase (EC 1.7.99.4) (EC 1.7.99.4; primary bucket kegg:ppu01320)
- metZ: PP_2001 | Q88LD4 | O-succinylhomoserine sulfhydrylase (OSH sulfhydrylase) (OSHS sulfhydrylase) (EC 2.5.1.-) (EC 2.5.1.-; primary bucket kegg:ppu00270)
- PP_2048: PP_2048 | Q88L87 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)
- cysH: PP_2328 | Q88KG2 | Adenosine 5'-phosphosulfate reductase (APS reductase) (EC 1.8.4.10) (5'-adenylylsulfate reductase) (Thioredoxin-dependent 5'-adenylylsulfate reductase) (EC 1.8.4.10; primary bucket kegg:ppu01320)
- cysI: PP_2371 | Q88KB9 | Sulphite reductase hemoprotein, beta subunit (primary bucket kegg:ppu01320)
- PP_2677: PP_2677 | Q88JH2 | Quinoprotein dehydrogenase-associated SoxYZ-like carrier (primary bucket kegg:ppu01320)
- msuE: PP_2764 | Q88J85 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- PP_2765: PP_2765 | Q88J84 | Sulfonate monooxygenase MsuD (primary bucket kegg:ppu00920)
- PP_2795: PP_2795 | Q88J54 | AMP-binding domain protein (primary bucket kegg:ppu00920)
- PP_3136: PP_3136 | Q88I65 | Serine acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- PP_3217: PP_3217 | Q88HY6 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- PP_3219: PP_3219 | Q88HY4 | Alkansulfonate monooxygenase (primary bucket kegg:ppu00920)
- PP_3228: PP_3228 | Q88HX5 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- PP_3229: PP_3229 | Q88HX4 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- PP_3528: PP_3528 | Q88H37 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- PP_3553: PP_3553 | Q88H12 | AMP-binding domain protein (primary bucket kegg:ppu00920)
- PP_3554: PP_3554 | Q88H11 | 3-methylmercaptopropionyl-CoA dehydrogenase (EC 1.3.99.41) (EC 1.3.99.41; primary bucket kegg:ppu00920)
- PP_3822: PP_3822 | Q88GA3 | Cytochrome c family protein (primary bucket kegg:ppu01320)
- sbp-I: PP_4305 | Q88EZ5 | Sulfate ABC transporter (primary bucket kegg:ppu00920)
- cysK: PP_4571 | Q88E95 | Cysteine synthase (EC 2.5.1.47) (EC 2.5.1.47; primary bucket kegg:ppu01320)
- rhdA: PP_4907 | Q88DC0 | Sulfurtransferase (primary bucket kegg:ppu04122)
- metXS: PP_5097 | Q88CT3 | Homoserine O-succinyltransferase (HST) (EC 2.3.1.46) (Homoserine transsuccinylase) (HTS) (EC 2.3.1.46; primary bucket kegg:ppu00270)
- sseA: PP_5118 | Q88CR2 | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) (EC 2.8.1.2; primary bucket kegg:ppu04122)
- cysA: PP_5168 | Q88CL2 | Sulfate/thiosulfate import ATP-binding protein CysA (EC 7.3.2.3) (Sulfate-transporting ATPase) (EC 7.3.2.3; primary bucket kegg:ppu00920)
- cysW: PP_5169 | Q88CL1 | Sulfate transport system permease protein CysW (primary bucket kegg:ppu00920)
- cysU: PP_5170 | Q88CL0 | Sulfate transport system permease protein CysT (primary bucket kegg:ppu00920)
- sbp-II: PP_5171 | Q88CK9 | Sulfate ABC transporter (primary bucket kegg:ppu00920)

## Generic Module Context

### Working Scope

A reusable pathway that converts sulfate to sulfide through adenosine 5'-phosphosulfate (APS) and sulfite. The module contains sulfate activation by ATP sulfurylase, thioredoxin-dependent APS reduction, and assimilatory sulfite reduction. It represents the direct APS branch rather than the alternative APS-kinase/PAPS-reductase route. Sulfate import is upstream, whereas siroheme synthesis and incorporation of sulfide into cysteine are supporting or downstream biology outside the pathway boundary.

### Provisional Biological Outline

- APS-dependent assimilatory sulfate reduction
  - 1. sulfate activation
  - Sulfate activation to APS
    - CysD/CysN ATP sulfurylase (molecular player: proteobacterial CysD/CysN ATP sulfurylase; activity or role: sulfate adenylyltransferase (ATP) activity)
  - 2. APS reduction
  - APS reduction to sulfite
    - Thioredoxin-dependent APS reductase (molecular player: CysH APS reductases; activity or role: adenylyl-sulfate reductase (thioredoxin) activity)
  - 3. sulfite reduction
  - Assimilatory reduction of sulfite to sulfide
    - Alternative versions by immediate electron-transfer system: Sulfite-reductase electron-donor architecture
      - Ferredoxin/Fpr-fed CysI route
        - Ferredoxin-dependent CysI activity (molecular player: ferredoxin-dependent assimilatory CysI proteins; activity or role: sulfite reductase (ferredoxin) activity)
        - Fpr electron supply (molecular player: bacterial type-1 ferredoxin--NADP reductases; activity or role: ferredoxin-NADP+ reductase activity)
      - CysJ/CysI NADPH-dependent route
        - CysJ/CysI NADPH sulfite reductase (molecular player: CysJ/CysI sulfite reductase complex; activity or role: sulfite reductase (NADPH) activity)

### Known Relationships Among Steps

- Sulfate activation to APS feeds into APS reduction to sulfite: ATP sulfurylase supplies APS to CysH.
- APS reduction to sulfite feeds into Assimilatory reduction of sulfite to sulfide: CysH supplies sulfite to the terminal sulfite-reduction system.

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

# Module Review: APS-dependent Assimilatory Sulfate Reduction in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI txid 160488; proteome UP000000556)
**Module scope:** sulfate → APS → sulfite → sulfide (direct APS branch)
**Local bucket reviewed:** KEGG `ppu00920` "Sulfur metabolism" (54 candidate genes)

---

## 1. Executive summary

The APS-dependent assimilatory sulfate-reduction module is **satisfiable and essentially complete** in *P. putida* KT2440. All three catalytic steps map to real, confidently annotated KT2440 genes:

1. **Sulfate activation → APS:** ATP sulfurylase **CysD (PP_1303) + CysNC (PP_1304)**.
2. **APS reduction → sulfite:** **CysH (PP_2328)**, UniProt-annotated *adenosine 5'-phosphosulfate reductase*, **EC 1.8.4.10** (thioredoxin-dependent, 4Fe-4S). This is the APS-reducing (plant/cyanobacterial-type) enzyme, confirming the module's **direct-APS scope** rather than the PAPS-reductase route.
3. **Sulfite reduction → sulfide:** siroheme hemoprotein **CysI (PP_2371)**, fed by the **ferredoxin/FprA route**.

Two curation-critical points emerge from species-specific evidence:

- The sulfite-reduction step in *P. putida* operates via the **Ferredoxin/Fpr-fed CysI route**, with **FprA = PP_1638** (adjacent to its regulator *finR* = PP_1637) supplying electrons. FprA is **missing from the candidate metadata** — a genuine electron-supply gap. The CysJ/CysI NADPH architecture is **not** the operational route here.
- The bucket is dominated (~30/54) by **organosulfur-scavenging and cysteine/methionine-synthesis genes that lie outside the module boundary**, and it contains at least one **over-propagated annotation (PP_1703)** that is actually a molybdopterin nitrate reductase.

Evidence transfer is **strong**: the key phenotypic study (PMID 23794620) uses *P. putida* strains (DSM 3601, and references S-313) and cites KT2440 locus tags (finR = PP1637), so conclusions transfer directly to KT2440.

---

## 2. Target-organism pathway definition

**Included (module boundary):** the two-electron activation of inorganic sulfate to APS (ATP sulfurylase), the two-electron reduction of APS to sulfite (APS reductase), and the six-electron reduction of sulfite to sulfide (assimilatory sulfite reductase) — plus the immediate electron-transfer architecture for the sulfite step.

**Kept separate (neighboring pathways / overview maps):**
- **Sulfate import** (upstream): CysA/CysW/CysU + Sbp ABC transporter.
- **Siroheme biosynthesis** (supporting cofactor): CysG.
- **Sulfide → cysteine/methionine incorporation** (downstream): CysK, CysE/SAT, Met enzymes.
- **Organosulfur scavenging** (sulfate-starvation stimulon): sulfonatases (Ssu/Msu), taurine system (Tau), arylsulfatases, sulfurtransferases.
- **Broad overview map:** KEGG `ppu00920` "Sulfur metabolism" is an *overview* map, not the module; it aggregates dissimilatory, organosulfur and trafficking reactions that do not belong to the APS assimilatory branch.

**Alternate names / DB definitions:** "assimilatory sulfate reduction (APS route)"; KEGG module **M00176** ("Assimilatory sulfate reduction, sulfate ⇒ H2S"); MetaCyc **PWY-5340**/**SO4ASSIM-PWY** ("sulfate reduction I / assimilatory"). Note KEGG M00176 as drawn includes CysC/CysH (PAPS or APS variant) — curators must disambiguate the APS vs PAPS branch (see §5).

---

## 3. Expected step model and satisfiability status

| Step | Expected activity | KT2440 gene(s) | Status |
|------|-------------------|----------------|--------|
| 1. Sulfate activation | sulfate adenylyltransferase (ATP), EC 2.7.7.4 → APS | **CysD PP_1303 + CysNC PP_1304** | **covered** |
| 2. APS reduction | adenylyl-sulfate reductase (thioredoxin), EC 1.8.4.10 → sulfite | **CysH PP_2328** | **covered** (direct-APS confirmed) |
| 3. Sulfite reduction | assimilatory sulfite reductase → sulfide | **CysI PP_2371** (siroheme hemoprotein) | **covered** |
| 3a. Electron supply (Fpr-fed CysI route) | ferredoxin–NADP+ reductase | **FprA PP_1638** (fpr-I) | **covered but GAP in metadata** (not in candidate list) |
| 3b. Alternative (CysJ/CysI NADPH route) | NADPH sulfite reductase flavoprotein | (PP_0860 not a canonical CysJ) | **not the operational route** |

**Supporting cast present (outside strict boundary, confirms function):** thioredoxin donors **TrxA (PP_5215) / TrxB (PP_0786)** for CysH; siroheme synthase **CysG (PP_3999)** for CysI; master regulator **CysB (PP_2327)** adjacent to *cysH*; regulator **FinR (PP_1637)** adjacent to *fprA*.

---

## 4. Candidate genes and evidence (high-confidence, in-module)

- **CysD — PP_1303 (Q88NA9).** ATP sulfurylase small subunit, EC 2.7.7.4. *Evidence: direct* — transposon insertions in *cysD* dominate sulfate-assimilation-defective *P. putida* mutants (PMID 23794620). Caveat: locally bucketed to ppu00261; should be tagged to the APS module.
- **CysNC — PP_1304 (Q88NA8).** ATP sulfurylase large subunit (GTPase), EC 2.7.7.4; **bifunctional CysN–CysC fusion** (InterPro APS_kinase_dom IPR059117; Pfam PF01583 APS_kinase + CysN GTP-binding + SO4_adenylTrfase_lsu; 633 aa). *Evidence: direct genetics* (PMID 23794620) + domain analysis. **Caveat:** the fused CysC (APS kinase) domain confers PAPS-forming capacity, but this does **not** re-route assimilation through PAPS because CysH is an APS reductase (EC 1.8.4.10). The APS-kinase activity most likely serves PAPS demand for sulfotransfer/other reactions, not the reductive assimilatory flux.
- **CysH — PP_2328 (Q88KG2).** Adenosine 5'-phosphosulfate reductase, **EC 1.8.4.10**, 4Fe-4S, thioredoxin-dependent, 244 aa. *Evidence: UniProt annotation + enzyme-family diagnostics.* This is the pivotal gene fixing the module identity to the **direct APS branch** (vs *E. coli* PAPS reductase EC 1.8.4.8). Thioredoxin donors TrxA/TrxB present.
- **CysI — PP_2371 (Q88KB9).** Assimilatory sulfite reductase hemoprotein (beta), **siroheme + 4Fe-4S**, 550 aa. Terminal enzyme of the module; electron donor is ferredoxin (FprA route). *Evidence: UniProt cofactor annotation + Pseudomonad physiology* (PMID 23794620).
- **FprA — PP_1638 (Q88MD5, fpr-I).** Ferredoxin–NADP+ reductase; FinR-regulated; supplies electrons to CysI. *Evidence: direct* — *fprA* is necessary for effective sulfate assimilation and its overexpression complements the *finR* mutant sulfur phenotype (PMID 23794620). **Not currently in the candidate list.**

**Supporting/regulatory (record for context):** CysB (PP_2327), FinR (PP_1637), CysG (PP_3999), TrxA (PP_5215), TrxB (PP_0786). **Upstream transport (separate module):** CysA (PP_5168), CysW (PP_5169), CysU/CysT (PP_5170), Sbp (PP_5171, PP_4305). **Downstream C/Met synthesis (separate):** CysK (PP_4571), CysE/SAT paralogs (PP_0840, PP_0228, PP_1110, PP_3136), MetB (PP_0659), MetZ (PP_2001), MetXS (PP_5097). **Tangential:** CysQ/PAP phosphatase (PP_0261) recycles PAP (relevant to PAPS/sulfotransfer housekeeping, not a core reductive step).

---

## 5. Gaps, ambiguities, and likely over-annotations

- **GAP — FprA (PP_1638) absent from candidate metadata.** The module explicitly lists an "Fpr electron supply" role; PP_1638 fills it and must be added. Paralog PP_4646 (fpr-II) is a lower-priority backup.
- **Over-annotation — PP_1703 (Q88M71) "assimilatory nitrate reductase/sulfite reductase" (EC 1.7.99.4).** Domain architecture is a **molybdopterin oxidoreductase (nitrate reductase, NapA/Nas-like)** fused to a CysJ-like FAD/NAD diaphorase, 1341 aa, **no siroheme**. It cannot perform assimilatory sulfite reduction (which requires siroheme). **Recommendation: strip the "sulfite reductase" label; reassign to nitrogen (nitrate/nitrite) assimilation.** Do **not** count toward module satisfiability.
- **Ambiguous — PP_0860 (Q88PJ0) "sulfite reductase flavoprotein component" (putative CysJ).** 849 aa flavoprotein carrying a **PepSY-associated transmembrane domain (PF03929)** on an FNR-like FAD/NAD module — not the canonical soluble *E. coli* CysJ (599 aa, no TM). Given that *P. putida* relies on FprA/ferredoxin for sulfite reduction (PMID 23794620), PP_0860 is unlikely to be the operational sulfite-reductase flavoprotein. **candidate_uncertain**; promote to full review.
- **No canonical CysJ in the genome (decisive).** A proteome-wide UniProt search of KT2440 returns **zero genes named *cysJ***; the only "sulfite reductase flavoprotein" is PP_0860 (non-canonical, above) and the only EC 1.8.1.2 (NADPH sulfite reductase) entry is the mis-annotated PP_1703. The absence of a bona fide CysJ NADPH-diaphorase means the **CysJ/CysI NADPH complex does not exist in KT2440**, leaving the ferredoxin/FprA-fed CysI route as the only viable sulfite-reduction architecture.
- **CysNC PAPS ambiguity.** The CysC (APS-kinase) domain means KEGG M00176's "PAPS" nodes may spuriously appear covered. Curators should record that assimilation is APS-direct (CysH EC 1.8.4.10) despite PAPS-forming capability.
- **Boundary over-inclusion (~30 genes).** Organosulfur scavenging (SsuABCDE PP_0236–0240 + paralogs PP_2764/2765, PP_3217/3219/3228/3229/3528/3553/3554; TauABCD PP_0209/0230–0233; sulfonate-binding proteins; 3-methylmercaptopropionyl-CoA dehydrogenases PP_0368/0370/2048/3554 [DMSP/methanethiol catabolism]; AMP-binding PP_2795/3553), sulfurtransferases (GlpE PP_0398, RhdA PP_4907, SseA PP_5118), sulfide:quinone oxidoreductase (PP_0053), cytochrome c (PP_3822), SoxYZ-like (PP_2677) — all belong to **sulfate-starvation/organosulfur or sulfur-trafficking** processes, not APS reduction (PMID 10482527, PMID 8800815). Keep out of module.

---

## 6. Module and GO-curation recommendations

**Per-step status labels:**
- Step 1 (sulfate activation) → **covered** (CysD PP_1303 + CysNC PP_1304).
- Step 2 (APS reduction) → **covered** (CysH PP_2328, EC 1.8.4.10).
- Step 3 (sulfite reduction) → **covered** via **Ferredoxin/Fpr-fed CysI route** (CysI PP_2371 + FprA PP_1638).
- Step 3, CysJ/CysI NADPH alternative → **not_expected_in_target_taxon** (genome has **no gene named *cysJ*** and no canonical soluble CysJ flavoprotein; physiology is Fpr/ferredoxin-dependent).
- Electron-supply sub-role → **module_needs_revision**: add FprA (PP_1638) to the candidate set.

**Module boundary:** current generic boundary is correct in intent; the *local bucket* (KEGG overview map) is too broad. Recommend restricting the module gene set to CysDN, CysH, CysI (+FprA), and explicitly excluding transport, siroheme synthesis, cysteine/methionine synthesis, and organosulfur scavenging.

**GO annotations to assert (with evidence codes):**
- CysH PP_2328 → GO:0033741 *adenylyl-sulfate reductase (thioredoxin) activity* (from EC 1.8.4.10).
- CysI PP_2371 → GO:0009337/GO:0004783-type *sulfite reductase (ferredoxin) activity* (GO:0050311) rather than NADPH (GO:0004783), consistent with the Fpr-fed route.
- FprA PP_1638 → GO:0004324 *ferredoxin-NADP+ reductase activity*; annotate involvement in GO:0000103 *assimilatory sulfate reduction* (IMP, PMID 23794620).
- **GO-term request check:** if the module ontology lacks a distinct "sulfite reductase (ferredoxin), assimilatory, Fpr-fed" node, a term/relationship request may be warranted to separate it from the NADPH CysJ/CysI complex.
- Remove/repair PP_1703 sulfite-reductase GO terms (reassign to nitrate/nitrite reductase, GO:0008940/GO:0042128).

---

## 7. Genes to promote to full `fetch-gene` review

1. **FprA PP_1638 (fpr-I)** — add as the module electron-supply gene (highest priority; currently missing).
2. **CysH PP_2328** — confirm EC 1.8.4.10 vs 1.8.4.8 and thioredoxin dependence; anchors module identity.
3. **CysI PP_2371** — confirm ferredoxin (not NADPH) electron acceptor; terminal enzyme.
4. **CysNC PP_1304** — document the CysN–CysC fusion and clarify PAPS vs APS routing.
5. **PP_0860** — resolve whether it is a functional CysJ or a mis-labelled membrane flavoprotein (candidate_uncertain).
6. **PP_1703** — correct over-propagated "sulfite reductase" annotation → nitrate reductase.

---

## 8. Key references

- Lewis TA, Glassing A, Harper J, Franklin MJ. *Role for ferredoxin:NAD(P)H oxidoreductase (FprA) in sulfate assimilation and siderophore biosynthesis in Pseudomonads.* **PMID 23794620** (2013). *Direct P. putida evidence:* cysD/cysNC/cysG essential; fprA required; finR = PP1637; complementation by fprA or E. coli cysJI.
- Vermeij P, Kertesz MA. *Pathways of assimilative sulfur metabolism in Pseudomonas putida.* **PMID 10482527** (1999). Cysteine/methionine routing; ssuD required for organosulfur (methanesulfonate) use.
- Beil S, Kertesz MA, Leisinger T, Cook AM. *The assimilation of sulfur from multiple sources and its correlation with expression of the sulfate-starvation-induced stimulon in Pseudomonas putida S-313.* **PMID 8800815** (1996). Organosulfur scavenging is a sulfate-limitation response.
- Bick JA, et al. *Regulation of the plant-type 5'-adenylyl sulfate reductase by oxidative stress.* **PMID 11467967** (2001). APS-reductase (EC 1.8.4.x) family reference for the direct-APS branch.
- UniProt/InterPro (2026): Q88KG2 (CysH), Q88NA9 (CysD), Q88NA8 (CysNC), Q88KB9 (CysI), Q88MD5 (FprA/PP_1638), Q88M71 (PP_1703), Q88PJ0 (PP_0860), Q88FT3 (CysG), Q88KG3 (CysB) — annotation/domain evidence.

---

### Uncertainty & species-transfer notes
- **Direct (KT2440/P. putida) experimental:** essentiality of cysD, cysNC, cysG and requirement of fprA for sulfate assimilation (PMID 23794620); organosulfur scavenging physiology (PMIDs 10482527, 8800815).
- **Homology/annotation-based (this review):** CysH EC assignment (direct-APS), CysNC fusion, PP_1703 mis-annotation, PP_0860 non-canonical CysJ, FprA=PP_1638 locus assignment (inferred from finR=PP1637 adjacency).
- **Open questions for experts:** Does CysI in KT2440 accept electrons exclusively from ferredoxin, or can PP_0860 act as an NADPH flavoprotein partner under some conditions? Is fpr-II (PP_4646) redundant with fpr-I for sulfite reduction? Is APS-kinase (CysC domain of CysNC) ever used for assimilation, or solely for PAPS/sulfotransfer?


## Artifacts

- [OpenScientist final report](PSEPK__aps_dependent_assimilatory_sulfate_reduction__ppu00920-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__aps_dependent_assimilatory_sulfate_reduction__ppu00920-deep-research-openscientist_artifacts/final_report.pdf)