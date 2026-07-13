---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T12:48:01.117819'
end_time: '2026-07-06T13:13:05.327020'
duration_seconds: 1504.21
template_file: templates/module_pathway_taxon_research.md.j2
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
  pathway_query: ppu00030
  pathway_id: ppu00030
  pathway_name: Pentose phosphate pathway
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00030 with 19 primary genes; module
    area: central_carbon.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '36'
  candidate_genes: '- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1)
    (EC 5.1.3.1; primary bucket kegg:ppu00040)

    - prs: PP_0722 | Q88PX6 | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1)
    (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate
    synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase)
    (PRPPase) (EC 2.7.6.1; primary bucket kegg:ppu00030)

    - trxB: PP_0786 | Q88PR2 | Thioredoxin reductase (EC 1.8.1.9) (EC 1.8.1.9; primary
    bucket kegg:ppu00030)

    - edd: PP_1010 | Q88P43 | Phosphogluconate dehydratase (EC 4.2.1.12) (EC 4.2.1.12;
    primary bucket kegg:ppu00030)

    - zwfA: PP_1022 | Q88P31 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49)
    (EC 1.1.1.49; primary bucket kegg:ppu00480)

    - pgl: PP_1023 | Q88P30 | 6-phosphogluconolactonase (6PGL) (EC 3.1.1.31) (EC 3.1.1.31;
    primary bucket kegg:ppu00030)

    - eda: PP_1024 | Q88P29 | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14)
    (EC 4.1.2.14; primary bucket kegg:ppu00030)

    - ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate
    reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81;
    primary bucket kegg:ppu00030)

    - gcd: PP_1444 | Q88MX4 | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) (EC
    1.1.5.2; primary bucket kegg:ppu00030)

    - PP_1661: PP_1661 | Q88MB3 | Dehydrogenase subunit (primary bucket kegg:ppu00030)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9)
    (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - ppgL: PP_2021 | Q88LB4 | L-alpha-hydroxyglutaric acid gamma-lactonase (primary
    bucket kegg:ppu00030)

    - tal: PP_2168 | Q88KX1 | Transaldolase (EC 2.2.1.2) (EC 2.2.1.2; primary bucket
    kegg:ppu00710)

    - rbsK: PP_2458 | Q88K34 | Ribokinase (RK) (EC 2.7.1.15) (EC 2.7.1.15; primary
    bucket kegg:ppu00030)

    - PP_2744: PP_2744 | Q88JA5 | ribose-phosphate diphosphokinase (EC 2.7.6.1) (EC
    2.7.6.1; primary bucket kegg:ppu00030)

    - ptxD: PP_3376 | Q88HI1 | Phosphonate dehydrogenase (EC 1.20.1.1) (EC 1.20.1.1;
    primary bucket kegg:ppu00480)

    - kguK: PP_3378 | Q88HH9 | 2-ketogluconokinase (EC 2.7.1.13) (EC 2.7.1.13; primary
    bucket kegg:ppu00030)

    - PP_3382: PP_3382 | Q88HH6 | Gluconate 2-dehydrogenase cytochrome c subunit (EC
    1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)

    - PP_3383: PP_3383 | Q88HH5 | Gluconate 2-dehydrogenase flavoprotein subunit (EC
    1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)

    - PP_3384: PP_3384 | Q88HH4 | Gluconate 2-dehydrogenase gamma subunit (EC 1.1.99.3)
    (EC 1.1.99.3; primary bucket kegg:ppu00030)

    - gnuK: PP_3416 | Q88HE4 | Gluconokinase (EC 2.7.1.12) (EC 2.7.1.12; primary bucket
    kegg:ppu00030)

    - PP_3443: PP_3443 | Q88HB7 | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.59)
    (EC 1.2.1.59; primary bucket kegg:ppu00030)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - adhB: PP_3623 | Q88GU4 | Alcohol dehydrogenase cytochrome c subunit (primary
    bucket kegg:ppu00030)

    - zwfB: PP_4042 | Q88FP7 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49)
    (EC 1.1.1.49; primary bucket kegg:ppu00480)

    - gntZ: PP_4043 | Q88FP6 | 6-phosphogluconate dehydrogenase, decarboxylating (EC
    1.1.1.44) (EC 1.1.1.44; primary bucket kegg:ppu00480)

    - ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81;
    primary bucket kegg:ppu00561)

    - phnN: PP_4469 | Q88EJ3 | Ribose 1,5-bisphosphate phosphokinase PhnN (EC 2.7.4.23)
    (Ribose 1,5-bisphosphokinase) (EC 2.7.4.23; primary bucket kegg:ppu00030)

    - pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9)
    (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC
    4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)

    - tktA: PP_4965 | Q88D62 | Transketolase (EC 2.2.1.1) (EC 2.2.1.1; primary bucket
    kegg:ppu00710)

    - fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1)
    (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11;
    primary bucket kegg:ppu00710)

    - rpiA: PP_5150 | Q88CN0 | Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase
    A) (PRI) (EC 5.3.1.6; primary bucket kegg:ppu00710)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

    - zwf: PP_5351 | Q88C32 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49)
    (EC 1.1.1.49; primary bucket kegg:ppu00480)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Pentose phosphate pathway in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00030
- Resolved ID: ppu00030
- Resolved name: Pentose phosphate pathway
- Source: KEGG

Resolved local bucket kegg:ppu00030 with 19 primary genes; module area: central_carbon.

## Candidate Genes From Local Metadata

Candidate gene count: 36

- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1) (EC 5.1.3.1; primary bucket kegg:ppu00040)
- prs: PP_0722 | Q88PX6 | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase) (PRPPase) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- trxB: PP_0786 | Q88PR2 | Thioredoxin reductase (EC 1.8.1.9) (EC 1.8.1.9; primary bucket kegg:ppu00030)
- edd: PP_1010 | Q88P43 | Phosphogluconate dehydratase (EC 4.2.1.12) (EC 4.2.1.12; primary bucket kegg:ppu00030)
- zwfA: PP_1022 | Q88P31 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)
- pgl: PP_1023 | Q88P30 | 6-phosphogluconolactonase (6PGL) (EC 3.1.1.31) (EC 3.1.1.31; primary bucket kegg:ppu00030)
- eda: PP_1024 | Q88P29 | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) (EC 4.1.2.14; primary bucket kegg:ppu00030)
- ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81; primary bucket kegg:ppu00030)
- gcd: PP_1444 | Q88MX4 | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) (EC 1.1.5.2; primary bucket kegg:ppu00030)
- PP_1661: PP_1661 | Q88MB3 | Dehydrogenase subunit (primary bucket kegg:ppu00030)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- ppgL: PP_2021 | Q88LB4 | L-alpha-hydroxyglutaric acid gamma-lactonase (primary bucket kegg:ppu00030)
- tal: PP_2168 | Q88KX1 | Transaldolase (EC 2.2.1.2) (EC 2.2.1.2; primary bucket kegg:ppu00710)
- rbsK: PP_2458 | Q88K34 | Ribokinase (RK) (EC 2.7.1.15) (EC 2.7.1.15; primary bucket kegg:ppu00030)
- PP_2744: PP_2744 | Q88JA5 | ribose-phosphate diphosphokinase (EC 2.7.6.1) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- ptxD: PP_3376 | Q88HI1 | Phosphonate dehydrogenase (EC 1.20.1.1) (EC 1.20.1.1; primary bucket kegg:ppu00480)
- kguK: PP_3378 | Q88HH9 | 2-ketogluconokinase (EC 2.7.1.13) (EC 2.7.1.13; primary bucket kegg:ppu00030)
- PP_3382: PP_3382 | Q88HH6 | Gluconate 2-dehydrogenase cytochrome c subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- PP_3383: PP_3383 | Q88HH5 | Gluconate 2-dehydrogenase flavoprotein subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- PP_3384: PP_3384 | Q88HH4 | Gluconate 2-dehydrogenase gamma subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- gnuK: PP_3416 | Q88HE4 | Gluconokinase (EC 2.7.1.12) (EC 2.7.1.12; primary bucket kegg:ppu00030)
- PP_3443: PP_3443 | Q88HB7 | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.59) (EC 1.2.1.59; primary bucket kegg:ppu00030)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- adhB: PP_3623 | Q88GU4 | Alcohol dehydrogenase cytochrome c subunit (primary bucket kegg:ppu00030)
- zwfB: PP_4042 | Q88FP7 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)
- gntZ: PP_4043 | Q88FP6 | 6-phosphogluconate dehydrogenase, decarboxylating (EC 1.1.1.44) (EC 1.1.1.44; primary bucket kegg:ppu00480)
- ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81; primary bucket kegg:ppu00561)
- phnN: PP_4469 | Q88EJ3 | Ribose 1,5-bisphosphate phosphokinase PhnN (EC 2.7.4.23) (Ribose 1,5-bisphosphokinase) (EC 2.7.4.23; primary bucket kegg:ppu00030)
- pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)
- tktA: PP_4965 | Q88D62 | Transketolase (EC 2.2.1.1) (EC 2.2.1.1; primary bucket kegg:ppu00710)
- fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11; primary bucket kegg:ppu00710)
- rpiA: PP_5150 | Q88CN0 | Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase A) (PRI) (EC 5.3.1.6; primary bucket kegg:ppu00710)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)
- zwf: PP_5351 | Q88C32 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)

## Generic Module Context

### Working Scope

A taxon-neutral module for the oxidative and non-oxidative pentose phosphate pathway (PPP). The oxidative branch converts glucose 6-phosphate to ribulose 5-phosphate while producing NADPH and CO2. The non-oxidative branch interconverts ribulose 5-phosphate, ribose 5-phosphate, xylulose 5-phosphate, sedoheptulose 7-phosphate, glyceraldehyde 3-phosphate, fructose 6-phosphate, and erythrose 4-phosphate through epimerase, isomerase, transketolase, and transaldolase reactions. Bacterial pathway maps often include adjacent Entner-Doudoroff, gluconate, ribose/PRPP, amino-sugar, riboflavin, and MEP-pathway nodes; these share metabolites with the PPP but are not strict PPP steps.

### Provisional Biological Outline

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

### Known Relationships Among Steps

- Glucose 6-phosphate to 6-phosphoglucono-delta-lactone precedes 6-phosphoglucono-delta-lactone to 6-phosphogluconate: 6-phosphogluconolactone produced by G6PD is hydrolyzed by 6-phosphogluconolactonase.
- 6-phosphoglucono-delta-lactone to 6-phosphogluconate precedes 6-phosphogluconate to ribulose 5-phosphate: 6-phosphogluconate enters oxidative decarboxylation to ribulose 5-phosphate.
- 6-phosphogluconate to ribulose 5-phosphate precedes Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate: Ribulose 5-phosphate is converted to ribose 5-phosphate or xylulose 5-phosphate.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate precedes Reversible sugar-phosphate rearrangements: Ribose 5-phosphate and xylulose 5-phosphate feed reversible transketolase/transaldolase reactions.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate feeds into Ribose and PRPP side inputs: Ribose 5-phosphate can be diverted to ribose salvage and PRPP-dependent biosynthesis.

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

Pentose phosphate pathway in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00030
- Resolved ID: ppu00030
- Resolved name: Pentose phosphate pathway
- Source: KEGG

Resolved local bucket kegg:ppu00030 with 19 primary genes; module area: central_carbon.

## Candidate Genes From Local Metadata

Candidate gene count: 36

- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1) (EC 5.1.3.1; primary bucket kegg:ppu00040)
- prs: PP_0722 | Q88PX6 | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase) (PRPPase) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- trxB: PP_0786 | Q88PR2 | Thioredoxin reductase (EC 1.8.1.9) (EC 1.8.1.9; primary bucket kegg:ppu00030)
- edd: PP_1010 | Q88P43 | Phosphogluconate dehydratase (EC 4.2.1.12) (EC 4.2.1.12; primary bucket kegg:ppu00030)
- zwfA: PP_1022 | Q88P31 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)
- pgl: PP_1023 | Q88P30 | 6-phosphogluconolactonase (6PGL) (EC 3.1.1.31) (EC 3.1.1.31; primary bucket kegg:ppu00030)
- eda: PP_1024 | Q88P29 | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) (EC 4.1.2.14; primary bucket kegg:ppu00030)
- ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81; primary bucket kegg:ppu00030)
- gcd: PP_1444 | Q88MX4 | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) (EC 1.1.5.2; primary bucket kegg:ppu00030)
- PP_1661: PP_1661 | Q88MB3 | Dehydrogenase subunit (primary bucket kegg:ppu00030)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- ppgL: PP_2021 | Q88LB4 | L-alpha-hydroxyglutaric acid gamma-lactonase (primary bucket kegg:ppu00030)
- tal: PP_2168 | Q88KX1 | Transaldolase (EC 2.2.1.2) (EC 2.2.1.2; primary bucket kegg:ppu00710)
- rbsK: PP_2458 | Q88K34 | Ribokinase (RK) (EC 2.7.1.15) (EC 2.7.1.15; primary bucket kegg:ppu00030)
- PP_2744: PP_2744 | Q88JA5 | ribose-phosphate diphosphokinase (EC 2.7.6.1) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- ptxD: PP_3376 | Q88HI1 | Phosphonate dehydrogenase (EC 1.20.1.1) (EC 1.20.1.1; primary bucket kegg:ppu00480)
- kguK: PP_3378 | Q88HH9 | 2-ketogluconokinase (EC 2.7.1.13) (EC 2.7.1.13; primary bucket kegg:ppu00030)
- PP_3382: PP_3382 | Q88HH6 | Gluconate 2-dehydrogenase cytochrome c subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- PP_3383: PP_3383 | Q88HH5 | Gluconate 2-dehydrogenase flavoprotein subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- PP_3384: PP_3384 | Q88HH4 | Gluconate 2-dehydrogenase gamma subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- gnuK: PP_3416 | Q88HE4 | Gluconokinase (EC 2.7.1.12) (EC 2.7.1.12; primary bucket kegg:ppu00030)
- PP_3443: PP_3443 | Q88HB7 | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.59) (EC 1.2.1.59; primary bucket kegg:ppu00030)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- adhB: PP_3623 | Q88GU4 | Alcohol dehydrogenase cytochrome c subunit (primary bucket kegg:ppu00030)
- zwfB: PP_4042 | Q88FP7 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)
- gntZ: PP_4043 | Q88FP6 | 6-phosphogluconate dehydrogenase, decarboxylating (EC 1.1.1.44) (EC 1.1.1.44; primary bucket kegg:ppu00480)
- ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81; primary bucket kegg:ppu00561)
- phnN: PP_4469 | Q88EJ3 | Ribose 1,5-bisphosphate phosphokinase PhnN (EC 2.7.4.23) (Ribose 1,5-bisphosphokinase) (EC 2.7.4.23; primary bucket kegg:ppu00030)
- pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)
- tktA: PP_4965 | Q88D62 | Transketolase (EC 2.2.1.1) (EC 2.2.1.1; primary bucket kegg:ppu00710)
- fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11; primary bucket kegg:ppu00710)
- rpiA: PP_5150 | Q88CN0 | Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase A) (PRI) (EC 5.3.1.6; primary bucket kegg:ppu00710)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)
- zwf: PP_5351 | Q88C32 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)

## Generic Module Context

### Working Scope

A taxon-neutral module for the oxidative and non-oxidative pentose phosphate pathway (PPP). The oxidative branch converts glucose 6-phosphate to ribulose 5-phosphate while producing NADPH and CO2. The non-oxidative branch interconverts ribulose 5-phosphate, ribose 5-phosphate, xylulose 5-phosphate, sedoheptulose 7-phosphate, glyceraldehyde 3-phosphate, fructose 6-phosphate, and erythrose 4-phosphate through epimerase, isomerase, transketolase, and transaldolase reactions. Bacterial pathway maps often include adjacent Entner-Doudoroff, gluconate, ribose/PRPP, amino-sugar, riboflavin, and MEP-pathway nodes; these share metabolites with the PPP but are not strict PPP steps.

### Provisional Biological Outline

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

### Known Relationships Among Steps

- Glucose 6-phosphate to 6-phosphoglucono-delta-lactone precedes 6-phosphoglucono-delta-lactone to 6-phosphogluconate: 6-phosphogluconolactone produced by G6PD is hydrolyzed by 6-phosphogluconolactonase.
- 6-phosphoglucono-delta-lactone to 6-phosphogluconate precedes 6-phosphogluconate to ribulose 5-phosphate: 6-phosphogluconate enters oxidative decarboxylation to ribulose 5-phosphate.
- 6-phosphogluconate to ribulose 5-phosphate precedes Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate: Ribulose 5-phosphate is converted to ribose 5-phosphate or xylulose 5-phosphate.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate precedes Reversible sugar-phosphate rearrangements: Ribose 5-phosphate and xylulose 5-phosphate feed reversible transketolase/transaldolase reactions.
- Ribulose 5-phosphate to ribose 5-phosphate and xylulose 5-phosphate feeds into Ribose and PRPP side inputs: Ribose 5-phosphate can be diverted to ribose salvage and PRPP-dependent biosynthesis.

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

# Pentose Phosphate Pathway in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

The pentose phosphate pathway (PPP) in *Pseudomonas putida* KT2440 is fully encoded and experimentally validated, but operates in a fundamentally different metabolic context than the textbook linear pathway. In this organism, the PPP does not function as an isolated module; rather, it is tightly integrated into the **EDEMP cycle**—a cyclic metabolic architecture that merges the Entner-Doudoroff (ED) pathway, gluconeogenic reactions of the Embden-Meyerhof-Parnas (EMP) pathway, and both oxidative and non-oxidative branches of the PPP (nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5). *P. putida* KT2440 lacks phosphofructokinase and therefore cannot run canonical forward glycolysis; instead, the EDEMP cycle recycles approximately 10% of ED-derived triose phosphates back to glucose-6-phosphate, enabling iterative NADPH generation through the oxidative PPP (nikel2016fromdirtto pages 3-5).

All six expected core PPP steps are covered by identified candidate genes with high confidence. However, the KEGG map ppu00030 inflates the pathway with 19 primary genes that include peripheral glucose oxidation enzymes (gcd, gnuK, kguK, gluconate 2-dehydrogenase subunits), ED pathway enzymes (edd, eda), and PRPP/ribose salvage enzymes that are biologically legitimate neighbors but not strict PPP transformations. Of the 36 candidate genes evaluated, only **10 genes** represent true core PPP steps, while the remainder belong to peripheral oxidation, ED, EDEMP coupling, or unrelated pathways.

A notable organism-specific feature is the presence of **three glucose-6-phosphate dehydrogenase (G6PDH) isozymes** encoded by *zwfA* (PP_1022), *zwfB* (PP_4042), and *zwfC* (PP_5351), with distinct cofactor specificities that enable flexible NADPH/NADH production depending on carbon source (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 4-6).

## 2. Target-Organism Pathway Definition

### 2.1. Biochemical process included

The pentose phosphate pathway in *P. putida* KT2440 comprises: (i) the **oxidative branch**, converting glucose-6-phosphate (G6P) to ribulose-5-phosphate (Ru5P) via 6-phosphogluconolactone and 6-phosphogluconate, generating NADPH and CO₂; and (ii) the **non-oxidative branch**, interconverting C3–C7 sugar phosphates through transketolase and transaldolase reactions to produce ribose-5-phosphate (R5P), erythrose-4-phosphate (E4P), fructose-6-phosphate (F6P), and glyceraldehyde-3-phosphate (GAP) (nikel2016fromdirtto pages 5-6).

Critically, the 6-phosphogluconate (6PG) node is a **branch point** in *P. putida*: carbon can flow either through Gnd (6-phosphogluconate dehydrogenase) into the oxidative PPP, or through Edd/Eda into the ED pathway. During glucose growth, over 50% of carbon at 6PG enters the ED pathway while approximately one-third cycles through Gnd back into the non-oxidative PPP (dvorak2024syntheticallyprimedadaptationof pages 3-4). Under oxidative stress, the PPP contribution increases dramatically, with the cyclic operation generating NADPH fluxes exceeding biosynthetic demands by approximately 50% (nikel2020redoxstressreshapes pages 1-4).

### 2.2. Neighboring pathways to keep separate

- **Entner-Doudoroff (ED) pathway**: Shares the 6PG intermediate but is functionally distinct (edd, eda). Should be a separate module.
- **Peripheral glucose oxidation**: Periplasmic conversion of glucose → gluconate → 2-ketogluconate (gcd, gluconate 2-dehydrogenase, gnuK, kguK). These feed carbon into the 6PG node but are not PPP reactions (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3).
- **PRPP/nucleotide biosynthesis**: Ribose-phosphate pyrophosphokinase (prs, PP_2744) drains R5P; this is a biosynthetic consumer, not a PPP step.
- **Amino sugar and polysaccharide metabolism**: pgm, algC, cpsG are phosphoglucomutase/phosphomannomutase enzymes for cell wall precursors.
- **EDEMP gluconeogenic coupling**: pgi1/pgi2, fba, fbp operate the gluconeogenic return from triose phosphates to hexose phosphates, enabling the EDEMP cycle (nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 3-4).

### 2.3. Alternate names and database definitions

The KEGG module ppu00030 is titled "Pentose phosphate pathway" but effectively represents a broader carbohydrate metabolism overview that includes the ED pathway, gluconate metabolism, and PRPP synthesis. BioCyc/MetaCyc treats the PPP as separate "pentose phosphate pathway (oxidative branch)" and "pentose phosphate pathway (non-oxidative branch)" modules, which more accurately delineate the core chemistry.

## 3. Expected Step Model

The following table provides a step-by-step satisfiability assessment for the PPP in *P. putida* KT2440:

| Step number | Step name | Expected reaction | Gene(s) covering step | Step status | Notes |
|---|---|---|---|---|---|
| 1 | Glucose 6-phosphate oxidation | G6P → 6-phosphoglucono-δ-lactone (6PGL) | **zwfA** (PP_1022), **zwfB** (PP_4042), **zwfC/zwf** (PP_5351) | covered | Strongest step in the module: KT2440 encodes three G6PDH isozymes with direct biochemical/genetic evidence; ZwfA provides most activity during glycolytic growth, ZwfB is also physiologically relevant, and ZwfC is weakly expressed/minor under tested conditions. This is the entry point to the oxidative PPP and part of the cyclic EDEMP architecture rather than a purely linear PPP in this organism (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 4-6, nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5) |
| 2 | Phosphogluconolactone hydrolysis | 6PGL → 6-phosphogluconate (6PG) | **pgl** (PP_1023) | covered | High-confidence assignment from conserved function plus species-specific operon/regulatory context: **zwfA-pgl-eda** is part of the HexR-regulated upper sugar catabolic region. Direct KT2440 enzyme biochemistry was not retrieved here, but the assignment is strongly supported by operon structure and flux logic (dvorak2024syntheticallyprimedadaptationof pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 3-4) |
| 3 | 6-Phosphogluconate oxidative decarboxylation | 6PG → ribulose-5-phosphate (Ru5P) + CO2 | **gntZ** (PP_4043) | covered | True oxidative PPP step, supported by flux/genetic evidence. Important curation note: in *P. putida* KT2440 this step competes directly with the Entner-Doudoroff branch at the 6PG node via **edd/eda**; therefore presence of **gntZ** should not be interpreted as evidence for a stand-alone linear oxidative PPP. The balance between PPP and ED flux is condition-dependent (dvorak2023genomicandmetabolic pages 22-26, dvorak2024syntheticallyprimedadaptationof pages 3-4, dvorak2024syntheticallyprimedadaptationof pages 5-6, nikel2020redoxstressreshapes pages 6-9, i.2021reconfigurationofmetabolic pages 5-7) |
| 4a | Ribulose-5-phosphate isomerization | Ru5P ↔ ribose-5-phosphate (R5P) | **rpiA** (PP_5150) | covered | Standard non-oxidative PPP step; supported in KT2440 by pathway context and flux studies, though direct biochemical characterization in this strain was not retrieved. No major ambiguity from current evidence (dvorak2023genomicandmetabolic pages 45-48, nikel2016fromdirtto pages 5-6) |
| 4b | Ribulose-phosphate epimerization | Ru5P ↔ xylulose-5-phosphate (Xu5P) | **rpe** (PP_0415) | covered | Standard non-oxidative PPP step; supported by pathway context and flux analysis in KT2440. As with **rpiA**, evidence is mainly species-aware inference/flux support rather than direct purified-enzyme work in KT2440 (dvorak2023genomicandmetabolic pages 45-48, nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 4-5) |
| 5 | Non-oxidative carbon rearrangement | Reversible transfer reactions among Xu5P, R5P, S7P, E4P, F6P, GAP | **tktA** (PP_4965), **tal** (PP_2168) | covered | High-confidence non-oxidative PPP coverage. Flux and engineering studies support operation of these reactions in KT2440, and **tal** is especially important during engineered xylose assimilation. In the native organism these reactions feed the cyclic EDEMP network, helping recycle carbon between ED products and hexose phosphates (nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 3-4, dvorak2023genomicandmetabolic pages 45-48, dvorak2024syntheticallyprimedadaptationof pages 4-5) |
| 6 | Adjacent ribose/PRPP metabolism | Ribose → R5P; R5P → PRPP | **rbsK** (PP_2458), **prs** (PP_0722), **PP_2744** | module_needs_revision | These reactions are legitimate neighbors of PPP metabolite pools but are not strict core PPP transformations. **rbsK** is ribose salvage feeding R5P; **prs** and likely **PP_2744** are PRPP synthase functions draining R5P into nucleotide/phosphoribosyl metabolism. They should be separated from core PPP satisfiability or represented as optional side-input/output steps (volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 4-6) |
| Boundary note A | EDEMP coupling | PPP operates with ED and partial EMP/gluconeogenic reactions | Core PPP plus **edd**, **eda**, **pgi1/pgi2**, **fba**, **fbp**, **PP_3443** | module_needs_revision | In KT2440 the PPP does not behave as an isolated textbook pathway: it operates cyclically as part of the EDEMP cycle, which recycles part of the ED-derived triose phosphates back to hexose phosphates for NADPH production and precursor balancing. This means module logic should explicitly note dependence on ED-linked carbon recycling rather than assuming a linear bacterial PPP alone (nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5, dvorak2024syntheticallyprimedadaptationof pages 3-4, chavarria2016ametabolicwidget pages 10-12, chavarria2016ametabolicwidget pages 12-13) |
| Boundary note B | Canonical glycolysis expectation | Phosphofructokinase-dependent EMP glycolysis | No canonical **pfkA/pfkB** in KT2440 | not_expected_in_target_taxon | *P. putida* KT2440 lacks phosphofructokinase and therefore does not run a canonical forward EMP glycolysis; upper sugar metabolism instead relies on ED-centered cyclic operation with gluconeogenic reactions reconnecting to PPP. Any module assuming classical glycolysis support for PPP should be revised for this taxon (nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5, nguyen2019criticallyreevaluatingcarbohydrate pages 15-21) |
| Boundary note C | Regulatory architecture | HexR control of upper sugar catabolism | **HexR-regulated zwfA-pgl-eda and edd-glk regions** | covered | While not a catalytic step, HexR is a key organism-specific regulatory feature shaping PPP/ED deployment. It represses the upper sugar catabolic operons and its removal derepresses oxidative PPP and ED functions, a point relevant to species-aware pathway annotation and interpretation of condition-specific fluxes (volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 9-11, dvorak2024syntheticallyprimedadaptationof pages 5-6) |
| Boundary note D | KEGG bucket inflation | Peripheral glucose oxidation and ED feeder reactions often co-listed with PPP | **gcd**, **gnuK**, **kguK**, **PP_3382-PP_3384**, **ptxD**; also **edd/eda** | module_needs_revision | Many genes in KEGG ppu00030 for KT2440 belong to peripheral glucose oxidation or the ED pathway, not to strict PPP chemistry. They feed carbon into the 6PG node and are biologically important, but they should not be allowed to satisfy core oxidative/non-oxidative PPP steps. Recommended split: core PPP vs ED/peripheral oxidation sidecar module (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3, nguyen2021theanoxicelectrode‐driven pages 5-7) |


*Table: This table assesses whether each expected pentose phosphate pathway step is satisfied in Pseudomonas putida KT2440 and highlights organism-specific module revisions. It is useful for separating core PPP coverage from adjacent ED, peripheral glucose oxidation, and ribose/PRPP reactions.*

## 4. Candidate Genes and Evidence

The comprehensive assessment of all 36 candidate genes is presented below:

| Gene name | Locus tag | UniProt ID | EC number | Functional role | Module step assignment | Evidence type | Confidence | Curation notes |
|---|---|---|---|---|---|---|---|---|
| rpe | PP_0415 | Q88QS3 | 5.1.3.1 | Ribulose-phosphate 3-epimerase | Core non-oxidative PPP: Ru5P ↔ Xu5P | Flux/genome context in *P. putida*; mostly homology-backed (dvorak2023genomicandmetabolic pages 45-48, nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 4-5) | High | True PPP gene; candidate should be promoted for full review because direct KT2440 biochemical validation was not found. |
| prs | PP_0722 | Q88PX6 | 2.7.6.1 | PRPP synthase | Adjacent ribose/PRPP metabolism, not core PPP | Database/genome inference | Medium | Not a strict PPP step; relevant as R5P sink into nucleotide biosynthesis. Likely over-included if module is strict PPP. |
| trxB | PP_0786 | Q88PR2 | 1.8.1.9 | Thioredoxin reductase | None / redox housekeeping | Database inference | Low | Not a PPP enzyme. Inclusion in ppu00030 is likely over-annotation from NADPH/redox association. |
| edd | PP_1010 | Q88P43 | 4.2.1.12 | 6-phosphogluconate dehydratase | ED branch from 6PG, not strict PPP | Direct genetic/flux evidence in *P. putida* (dvorak2024syntheticallyprimedadaptationof pages 5-6, dvorak2023genomicandmetabolic pages 22-26, dvorak2024syntheticallyprimedadaptationof pages 3-4) | High | Important pathway-neighbor in KT2440; belongs to ED arm of EDEMP, not to strict PPP. |
| zwfA | PP_1022 | Q88P31 | 1.1.1.49 | G6PDH isozyme A | Core oxidative PPP: G6P → 6PGL | Direct genetics/biochemistry in KT2440 (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 4-6) | High | True PPP gene; principal G6PDH during glycolytic growth; HexR-regulated with pgl/eda operon context. |
| pgl | PP_1023 | Q88P30 | 3.1.1.31 | 6-phosphogluconolactonase | Core oxidative PPP: 6PGL → 6PG | Operon/flux evidence in *P. putida*; no direct enzyme study retrieved (dvorak2024syntheticallyprimedadaptationof pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 3-4) | High | True PPP gene; strong assignment from conserved operon with zwfA and flux studies. |
| eda | PP_1024 | Q88P29 | 4.1.2.14 | KDPG aldolase | ED pathway terminal split, not strict PPP | Direct genetics/operon context in *P. putida* (dvorak2024syntheticallyprimedadaptationof pages 5-6) | High | ED enzyme, not PPP proper; included because ED and PPP are cyclically connected in KT2440. |
| ghrB | PP_1261 | Q88NF1 | 1.1.1.215 / 1.1.1.79 / 1.1.1.81 | 2-ketoaldonate/hydroxypyruvate-glyoxylate reductase | None / peripheral carbonyl metabolism | Database inference | Low | Not a canonical PPP component; likely over-annotation for this module. |
| gcd | PP_1444 | Q88MX4 | 1.1.5.2 | PQQ-dependent periplasmic glucose dehydrogenase | Peripheral glucose oxidation feeding 6PG/ED | Direct physiology/regulatory evidence in KT2440 (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3, nguyen2021theanoxicelectrode‐driven pages 5-7) | High | Not strict PPP; major upstream feeder to gluconate/2KG routes. Important for pathway-boundary notes. |
| PP_1661 | PP_1661 | Q88MB3 | — | Dehydrogenase subunit | Peripheral oxidation candidate | Database inference only | Low | Likely not a core PPP enzyme; exact role in ppu00030 unclear and should not satisfy PPP steps without more evidence. |
| cpsG | PP_1777 | Q88LZ9 | 5.4.2.8 | Phosphomannomutase | None / mannose-polysaccharide metabolism | Database inference | Low | Not a PPP enzyme. Keep separate under amino sugar/exopolysaccharide metabolism. |
| pgi1 | PP_1808 | Q88LW9 | 5.3.1.9 | Glucose-6-phosphate isomerase 1 | EDEMP gluconeogenic recycling: G6P ↔ F6P | Indirect pathway evidence in KT2440 (nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5, dvorak2024syntheticallyprimedadaptationof pages 3-4) | Medium | Not a strict PPP step, but functionally important for EDEMP connection recycling triose/hexose phosphates. Paralog ambiguity with pgi2. |
| ppgL | PP_2021 | Q88LB4 | — | Lactonase-family protein | Unclear; possible peripheral lactone hydrolysis | Database inference | Low | Not established as PPP lactonase in KT2440; pgl already covers 6PGL hydrolysis. Likely over-annotation. |
| tal | PP_2168 | Q88KX1 | 2.2.1.2 | Transaldolase | Core non-oxidative PPP carbon rearrangement | Flux/engineering evidence in KT2440 (dvorak2023genomicandmetabolic pages 45-48, nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 4-5) | High | True PPP gene; activity is a major determinant during engineered xylose use; valuable full review candidate. |
| rbsK | PP_2458 | Q88K34 | 2.7.1.15 | Ribokinase | Adjacent ribose salvage input to R5P | Indirect physiological/genetic evidence via G6PDH studies on ribose use (volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 4-6) | Medium | Not core PPP, but legitimate side-input to PPP metabolite pool. Keep separate from core satisfiability. |
| PP_2744 | PP_2744 | Q88JA5 | 2.7.6.1 | PRPP synthase-like paralog | Adjacent ribose/PRPP metabolism | Database inference | Low | Paralog of PRPP synthase; needs specific review before annotation. Not core PPP. |
| ptxD | PP_3376 | Q88HI1 | 1.20.1.1 | Phosphonate dehydrogenase / likely 2K6PG reductase-associated candidate in peripheral glucose oxidation locus | Peripheral 2KG assimilation, not core PPP | Gene-context inference; no direct KT2440 confirmation retrieved (chen2024gnurrepressesthe pages 1-3) | Medium | Not PPP proper. Annotation as phosphonate dehydrogenase may miss role in 2-keto-6-phosphogluconate reduction; merits full review. |
| kguK | PP_3378 | Q88HH9 | 2.7.1.13 | 2-ketogluconokinase | Peripheral 2KG route feeding 6PG/ED | Direct physiology/regulatory evidence in KT2440 (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3) | High | Not strict PPP; genuine feeder from 2-ketogluconate to 2K6PG/6PG branch. |
| PP_3382 | PP_3382 | Q88HH6 | 1.1.99.3 | Gluconate 2-dehydrogenase cytochrome c subunit | Peripheral oxidation: gluconate → 2-ketogluconate | Direct pathway/regulatory evidence at operon level (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3) | High | Peripheral glucose oxidation, not PPP. |
| PP_3383 | PP_3383 | Q88HH5 | 1.1.99.3 | Gluconate 2-dehydrogenase flavoprotein subunit | Peripheral oxidation: gluconate → 2-ketogluconate | Direct pathway/regulatory evidence at operon level (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3) | High | Peripheral glucose oxidation, not PPP. |
| PP_3384 | PP_3384 | Q88HH4 | 1.1.99.3 | Gluconate 2-dehydrogenase gamma subunit | Peripheral oxidation: gluconate → 2-ketogluconate | Direct pathway/regulatory evidence at operon level (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3) | High | Peripheral glucose oxidation, not PPP. |
| gnuK | PP_3416 | Q88HE4 | 2.7.1.12 | Gluconokinase | Peripheral gluconate route to 6PG | Direct physiology/regulatory evidence in KT2440 (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3, nguyen2021theanoxicelectrode‐driven pages 5-7) | High | Not strict PPP; major feeder into 6PG node. |
| PP_3443 | PP_3443 | Q88HB7 | 1.2.1.59 | GAPDH | EDEMP/gluconeogenic recycling and fructose metabolic widget | Direct experiment in KT2440 (chavarria2016ametabolicwidget pages 10-12, chavarria2016ametabolicwidget pages 12-13, chavarria2016ametabolicwidget pages 9-10, chavarria2016ametabolicwidget pages 5-6) | High | Not PPP proper; important for EDEMP linkage and PEP supply during fructose utilization. |
| pgm | PP_3578 | Q88GY7 | 5.4.2.2 | Phosphoglucomutase | None / glycogen & hexose-phosphate interconversion | Database inference | Low | Not a PPP enzyme. |
| adhB | PP_3623 | Q88GU4 | — | Alcohol dehydrogenase cytochrome c subunit | None / alcohol oxidation | Database inference | Low | Not a PPP enzyme; likely over-propagated from broad KEGG map adjacency. |
| zwfB | PP_4042 | Q88FP7 | 1.1.1.49 | G6PDH isozyme B | Core oxidative PPP: G6P → 6PGL | Direct genetics/biochemistry in KT2440 (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 4-6, shah2022glucose6phosphatedehydrogenasezwfa pages 5-8) | High | True PPP gene; dual-cofactor enzyme with substantial physiological role, especially alongside zwfA. |
| gntZ | PP_4043 | Q88FP6 | 1.1.1.44 | 6-phosphogluconate dehydrogenase (decarboxylating) | Core oxidative PPP: 6PG → Ru5P + CO2 + NADPH | Flux/genetic evidence in KT2440 (dvorak2023genomicandmetabolic pages 22-26, dvorak2024syntheticallyprimedadaptationof pages 3-4) | High | True PPP gene; cotranscribed with zwfB. At 6PG node, competes with ED branch via Edd. |
| ttuD | PP_4300 | Q88F00 | 1.1.1.81 | Hydroxypyruvate reductase | None / serine-glyoxylate metabolism | Database inference | Low | Not a PPP enzyme. |
| phnN | PP_4469 | Q88EJ3 | 2.7.4.23 | Ribose 1,5-bisphosphokinase | Phosphonate metabolism, not PPP | Database inference | Low | Not a PPP enzyme; ribose-containing substrate may have caused over-association. |
| pgi2 | PP_4701 | Q88DW7 | 5.3.1.9 | Glucose-6-phosphate isomerase 2 | EDEMP gluconeogenic recycling: G6P ↔ F6P | Indirect pathway evidence in KT2440 (nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5, dvorak2024syntheticallyprimedadaptationof pages 3-4) | Medium | Not a strict PPP step; paralog ambiguity with pgi1 unresolved here. Promote for detailed review if module includes EDEMP functions. |
| fba | PP_4960 | Q88D67 | 4.1.2.13 | Fructose-bisphosphate aldolase | EDEMP gluconeogenic recycling | Indirect pathway evidence in KT2440 (dvorak2024syntheticallyprimedadaptationof pages 3-4) | Medium | Not strict PPP; supports cyclic reconnection of ED products to hexose phosphates. |
| tktA | PP_4965 | Q88D62 | 2.2.1.1 | Transketolase | Core non-oxidative PPP carbon rearrangement | Flux/engineering evidence in KT2440 (dvorak2023genomicandmetabolic pages 45-48, nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 4-5) | High | True PPP gene; central to non-oxidative branch and engineered pentose assimilation. |
| fbp | PP_5040 | Q88CY9 | 3.1.3.11 | Fructose-1,6-bisphosphatase class 1 | EDEMP gluconeogenic recycling | Indirect pathway evidence in KT2440 (nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 3-4) | Medium | Not strict PPP; one of the defining reactions enabling EDEMP cycle closure. |
| rpiA | PP_5150 | Q88CN0 | 5.3.1.6 | Ribose-5-phosphate isomerase A | Core non-oxidative PPP: Ru5P ↔ R5P | Flux/genome context in *P. putida* (dvorak2023genomicandmetabolic pages 45-48, nikel2016fromdirtto pages 5-6) | High | True PPP gene; direct biochemical evidence not retrieved, but assignment is standard and strongly supported. |
| algC | PP_5288 | Q88C93 | 5.4.2.2 / 5.4.2.8 | Phosphomannomutase/phosphoglucomutase | None / envelope polysaccharide precursor metabolism | Database inference | Low | Not a PPP enzyme. |
| zwfC (listed as zwf) | PP_5351 | Q88C32 | 1.1.1.49 | G6PDH isozyme C | Core oxidative PPP: G6P → 6PGL | Direct KT2440 genetics/biochemistry shows very low expression and little phenotype (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 9-11) | Medium | True G6PDH family member but likely minor/cryptic under tested conditions; should not be primary satisfier if zwfA/zwfB present. |


*Table: This table summarizes the 36 candidate genes associated with KEGG ppu00030 in Pseudomonas putida KT2440, separating true core PPP enzymes from ED-pathway, peripheral glucose oxidation, ribose/PRPP, EDEMP-linkage, and likely over-annotated genes. It is useful for manual module satisfiability decisions and prioritizing genes for full curation review.*

### 4.1. High-confidence core PPP genes

**Glucose-6-phosphate dehydrogenase isozymes (Step 1).** *P. putida* KT2440 encodes three G6PDH isozymes: ZwfA (PP_1022, family I), ZwfB (PP_4042, family II), and ZwfC (PP_5351, family III). Direct biochemical characterization in KT2440 has shown that these isozymes have distinct cofactor specificities (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 7-9). ZwfA carries the predominant G6PDH activity during glycolytic growth on glucose and is essential for glucose utilization, as demonstrated by deletion studies (volke2021cofactorspecificityof pages 4-6). ZwfB generates primarily NADH rather than NADPH and shows dual cofactor specificity; it is cotranscribed with *gntZ* (6-phosphogluconate dehydrogenase) (volke2021cofactorspecificityof pages 9-11, shah2022glucose6phosphatedehydrogenasezwfa pages 5-8). ZwfC has the highest NADP⁺ specificity among the three isozymes but is poorly transcribed under tested conditions and its deletion shows negligible growth effects (volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 9-11). The *zwfA-pgl-eda* operon is regulated by the HexR repressor (volke2021cofactorspecificityof pages 9-11, dvorak2024syntheticallyprimedadaptationof pages 5-6).

**6-Phosphogluconolactonase (Step 2).** Pgl (PP_1023) is encoded within the *zwfA-pgl-eda* operon and its assignment is strongly supported by conserved operon structure and 13C flux studies, though direct enzyme purification from KT2440 was not retrieved in this review (dvorak2024syntheticallyprimedadaptationof pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 3-4).

**6-Phosphogluconate dehydrogenase (Step 3).** GntZ (PP_4043) catalyzes the oxidative decarboxylation of 6PG to Ru5P, producing NADPH and CO₂. It is cotranscribed with *zwfB* and represents the branch point between the oxidative PPP and the ED pathway. Flux analysis demonstrates that Gnd is not essential for xylose growth (unlike Edd), though its deletion reduces growth rate (dvorak2024syntheticallyprimedadaptationof pages 5-6, dvorak2023genomicandmetabolic pages 22-26).

**Non-oxidative branch enzymes (Steps 4–5).** Ribose-5-phosphate isomerase (RpiA, PP_5150), ribulose-phosphate 3-epimerase (Rpe, PP_0415), transketolase (TktA, PP_4965), and transaldolase (Tal, PP_2168) are all encoded in the KT2440 genome and supported by 13C flux analysis and metabolic engineering studies (dvorak2023genomicandmetabolic pages 45-48, nikel2016fromdirtto pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 4-5). Transaldolase activity has been specifically shown to be a key determinant of xylose utilization rate in engineered *P. putida* strains, with higher Tal activity correlating with faster growth on xylose (dvorak2023genomicandmetabolic pages 45-48).

### 4.2. Peripheral and adjacent genes in the candidate list

**Peripheral glucose oxidation cluster.** Gcd (PP_1444), GnuK (PP_3416), KguK (PP_3378), and the gluconate 2-dehydrogenase complex (PP_3382/3383/3384) constitute the three-pronged periplasmic glucose oxidation system characteristic of *Pseudomonas*. Approximately 90% of glucose is oxidized to gluconate by Gcd in the periplasm; gluconate is phosphorylated by GnuK to 6PG, while a fraction is further oxidized to 2-ketogluconate by the Gad complex and then phosphorylated by KguK (chen2024gnurrepressesthe pages 1-3, weimer2020industrialbiotechnologyof pages 1-3). These are biologically important but belong to peripheral glucose oxidation, not PPP proper.

**PP_3443 (GAPDH).** This glyceraldehyde-3-phosphate dehydrogenase is regulated by the Cra protein and is specifically important for fructose metabolism, maintaining PEP levels for the PTS-dependent fructose uptake system (chavarria2016ametabolicwidget pages 10-12, chavarria2016ametabolicwidget pages 5-6, chavarria2016ametabolicwidget pages 3-5). It functions within the EDEMP cycle context but is not a PPP enzyme.

**PtxD (PP_3376).** Annotated as phosphonate dehydrogenase (EC 1.20.1.1), this gene is located in the 2-ketogluconate metabolism locus. Evidence from the Chen et al. (2024) regulatory study suggests functional involvement in 2-keto-6-phosphogluconate reduction, but direct biochemical confirmation in KT2440 was not retrieved (chen2024gnurrepressesthe pages 1-3).

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1. Over-annotations in ppu00030

Several genes in the candidate list are clearly not PPP enzymes and represent KEGG map adjacency artifacts:
- **trxB** (PP_0786, thioredoxin reductase): A redox housekeeping enzyme; its inclusion likely results from NADPH association in broad pathway maps.
- **ghrB** (PP_1261), **ttuD** (PP_4300): Hydroxypyruvate/glyoxylate reductases unrelated to PPP chemistry.
- **adhB** (PP_3623): Alcohol dehydrogenase cytochrome c subunit; peripheral oxidation enzyme.
- **phnN** (PP_4469): Ribose 1,5-bisphosphokinase involved in phosphonate metabolism.
- **ppgL** (PP_2021): A lactonase-family protein; the PPP lactonase function is already covered by pgl (PP_1023).
- **cpsG** (PP_1777), **pgm** (PP_3578), **algC** (PP_5288): Phosphoglucomutase/phosphomannomutase enzymes belonging to exopolysaccharide and glycogen metabolism.

### 5.2. Paralog ambiguity

- **pgi1** (PP_1808) vs. **pgi2** (PP_4701): Two glucose-6-phosphate isomerases are present. Their relative contributions to the EDEMP cycle have not been fully resolved in KT2440.
- **prs** (PP_0722) vs. **PP_2744**: Two PRPP synthase-like genes; their distinct physiological roles are not characterized.
- **Three Zwf isozymes**: While their cofactor specificities are characterized (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 2-4), ZwfC's physiological significance remains unclear given its low expression.

### 5.3. No true gaps in core PPP

All six core PPP steps have at least one high-confidence gene assignment. There are no missing enzymatic steps. The organism's unusual metabolic architecture (EDEMP cycle, lack of phosphofructokinase) does not create gaps but does require organism-specific interpretation of how the pathway operates.

## 6. Module and GO-Curation Recommendations

### 6.1. Step status summary
- **Steps 1–5 (all core PPP steps): COVERED** with high confidence.
- **Step 6 (ribose/PRPP side inputs): module_needs_revision** — these are legitimate metabolic neighbors but should not be used to satisfy core PPP steps.

### 6.2. Module boundary revisions needed

1. **Split peripheral glucose oxidation from PPP**: gcd, gnuK, kguK, PP_3382-3384, ptxD, and PP_1661 should be assigned to a separate "peripheral glucose oxidation" or "gluconate metabolism" module rather than ppu00030.
2. **Separate ED pathway**: edd and eda should be in a dedicated ED pathway module. The 6PG branch point should be annotated as a shared node.
3. **Create EDEMP cycle annotation**: The cyclic connection between PPP, ED, and gluconeogenic EMP reactions (pgi, fba, fbp, PP_3443) is a defining feature of *P. putida* central carbon metabolism that deserves explicit annotation, potentially as an organism-specific metabolic cycle module (nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5).
4. **Remove non-PPP enzymes**: trxB, ghrB, ttuD, adhB, phnN, ppgL, cpsG, pgm, algC should be excluded from PPP module satisfiability.

### 6.3. GO term considerations
- The three G6PDH isozymes may benefit from GO annotations specifying cofactor preference (NAD⁺ vs. NADP⁺) given the documented biochemical differences (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 7-9).
- A GO-based "EDEMP cycle" process term does not currently exist but would accurately capture the cyclic metabolic architecture specific to *Pseudomonas* and related organisms.

## 7. Genes to Promote to Full Review

The following genes merit priority for full fetch-gene review:

1. **zwfA (PP_1022)**: Principal G6PDH with direct biochemical characterization; most important oxidative PPP entry point.
2. **zwfB (PP_4042)**: Second G6PDH isozyme with unique dual cofactor properties; cotranscribed with gntZ.
3. **gntZ (PP_4043)**: 6-Phosphogluconate dehydrogenase at the critical 6PG branch point between PPP and ED.
4. **tal (PP_2168)**: Transaldolase identified as rate-limiting for engineered xylose assimilation.
5. **tktA (PP_4965)**: Transketolase; core non-oxidative PPP enzyme implicated in metabolic engineering.
6. **ptxD (PP_3376)**: Annotation ambiguity between phosphonate dehydrogenase and possible 2K6PG reductase function warrants resolution.
7. **pgl (PP_1023)**: Operon-based assignment is strong but direct enzyme characterization in KT2440 would increase confidence.

## 8. Key References

The following publications provide the most direct evidence for this review:

- **Volke, Olavarría & Nikel (2021)** *mSystems* 6:e00014-21 — Definitive characterization of three G6PDH isozymes in *P. putida* KT2440, including cofactor specificities, knockout phenotypes, and evolutionary context (volke2021cofactorspecificityof pages 11-13, volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 4-6).
- **Nikel, Fuhrer, Chavarría et al. (2021)** *ISME J* 15:1751-1766 — 13C flux analysis demonstrating cyclic PPP operation under oxidative stress with NADPH surplus exceeding biosynthetic demand by ~50% (i.2021reconfigurationofmetabolic pages 5-7, nikel2020redoxstressreshapes pages 1-4).
- **Nikel, Chavarría, Danchin & de Lorenzo (2016)** *Curr Opin Chem Biol* 34:20-29 — Seminal description of the EDEMP cycle concept integrating ED, EMP, and PP pathways in *P. putida* (nikel2016fromdirtto pages 5-6, nikel2016fromdirtto pages 3-5).
- **Dvořák, Burýšková et al. (2024)** *Nat Commun* 15:2666 — Xylose adaptation study providing flux analysis of PPP operation, HexR regulation, and transaldolase importance (dvorak2024syntheticallyprimedadaptationof pages 3-4, dvorak2024syntheticallyprimedadaptationof pages 5-6, dvorak2024syntheticallyprimedadaptationof pages 4-5).
- **Chen, Ma et al. (2024)** *Microb Biotechnol* 17:e70059 — GnuR regulon definition clarifying peripheral glucose/gluconate oxidation pathways and their feeding into the ED/PPP node (chen2024gnurrepressesthe pages 1-3).
- **Chavarría, Goñi-Moreno, de Lorenzo & Nikel (2016)** *mSystems* 1:e00154-16 — Characterization of PP_3443 GAPDH as Cra-regulated metabolic widget for fructose metabolism (chavarria2016ametabolicwidget pages 10-12, chavarria2016ametabolicwidget pages 5-6, chavarria2016ametabolicwidget pages 3-5).
- **Weimer, Kohlstedt, Volke, Nikel & Wittmann (2020)** *Appl Microbiol Biotechnol* 104:7745-7766 — Comprehensive review of *P. putida* industrial biotechnology including central carbon metabolism overview (weimer2020industrialbiotechnologyof pages 1-3).
- **Shah, Kasarlawar & Phale (2022)** *Microbiol Spectrum* 10:e03818-22 — Comparative characterization of Zwf isozymes in *Pseudomonas bharatica* CSV86, providing cross-species context for G6PDH multiplicity (shah2022glucose6phosphatedehydrogenasezwfa pages 8-11, shah2022glucose6phosphatedehydrogenasezwfa pages 5-8).
- **Wilkes, Mendonca & Aristilde (2019)** *Appl Environ Microbiol* 85:e02084-18 — 13C flux analysis of the cyclic metabolic network in *P. protegens* Pf-5, illustrating the conserved Pseudomonas EDEMP architecture (wilkes2019acyclicmetabolic pages 9-12).

References

1. (nikel2016fromdirtto pages 5-6): Pablo I Nikel, Max Chavarría, Antoine Danchin, and Víctor de Lorenzo. From dirt to industrial applications: pseudomonas putida as a synthetic biology chassis for hosting harsh biochemical reactions. Current opinion in chemical biology, 34:20-29, Oct 2016. URL: https://doi.org/10.1016/j.cbpa.2016.05.011, doi:10.1016/j.cbpa.2016.05.011. This article has 270 citations and is from a peer-reviewed journal.

2. (nikel2016fromdirtto pages 3-5): Pablo I Nikel, Max Chavarría, Antoine Danchin, and Víctor de Lorenzo. From dirt to industrial applications: pseudomonas putida as a synthetic biology chassis for hosting harsh biochemical reactions. Current opinion in chemical biology, 34:20-29, Oct 2016. URL: https://doi.org/10.1016/j.cbpa.2016.05.011, doi:10.1016/j.cbpa.2016.05.011. This article has 270 citations and is from a peer-reviewed journal.

3. (volke2021cofactorspecificityof pages 11-13): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 42 citations and is from a peer-reviewed journal.

4. (volke2021cofactorspecificityof pages 2-4): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 42 citations and is from a peer-reviewed journal.

5. (volke2021cofactorspecificityof pages 4-6): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 42 citations and is from a peer-reviewed journal.

6. (dvorak2024syntheticallyprimedadaptationof pages 3-4): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

7. (nikel2020redoxstressreshapes pages 1-4): Pablo I. Nikel, Tobias Fuhrer, Max Chavarría, Alberto Sánchez-Pascuala, Uwe Sauer, and Víctor de Lorenzo. Redox stress reshapes carbon fluxes of pseudomonas putida for cytosolic glucose oxidation and nadph generation. bioRxiv, Jun 2020. URL: https://doi.org/10.1101/2020.06.13.149542, doi:10.1101/2020.06.13.149542. This article has 11 citations.

8. (chen2024gnurrepressesthe pages 1-3): Wenbo Chen, Rao Ma, Yong Feng, Yunzhu Xiao, Agnieszka Sekowska, Antoine Danchin, and Conghui You. Gnur represses the expression of glucose and gluconate catabolism in pseudomonas putida kt2440. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70059, doi:10.1111/1751-7915.70059. This article has 2 citations and is from a peer-reviewed journal.

9. (weimer2020industrialbiotechnologyof pages 1-3): Anna Weimer, Michael Kohlstedt, Daniel C. Volke, Pablo I. Nikel, and Christoph Wittmann. Industrial biotechnology of pseudomonas putida: advances and prospects. Applied Microbiology and Biotechnology, 104:7745-7766, Aug 2020. URL: https://doi.org/10.1007/s00253-020-10811-9, doi:10.1007/s00253-020-10811-9. This article has 359 citations and is from a domain leading peer-reviewed journal.

10. (volke2021cofactorspecificityof pages 7-9): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 42 citations and is from a peer-reviewed journal.

11. (volke2021cofactorspecificityof pages 9-11): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 42 citations and is from a peer-reviewed journal.

12. (dvorak2024syntheticallyprimedadaptationof pages 5-6): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

13. (dvorak2023genomicandmetabolic pages 22-26): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Genomic and metabolic plasticity drive alternative scenarios for adapting pseudomonas putida to non-native substrate d-xylose. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.19.541448, doi:10.1101/2023.05.19.541448. This article has 0 citations.

14. (nikel2020redoxstressreshapes pages 6-9): Pablo I. Nikel, Tobias Fuhrer, Max Chavarría, Alberto Sánchez-Pascuala, Uwe Sauer, and Víctor de Lorenzo. Redox stress reshapes carbon fluxes of pseudomonas putida for cytosolic glucose oxidation and nadph generation. bioRxiv, Jun 2020. URL: https://doi.org/10.1101/2020.06.13.149542, doi:10.1101/2020.06.13.149542. This article has 11 citations.

15. (i.2021reconfigurationofmetabolic pages 5-7): Pablo I. Nikel, Tobias Fuhrer, Max Chavarria, Alberto Sanchez-Pascuala, Uwe Sauer, and Victor de Lorenzo. Reconfiguration of metabolic fluxes in pseudomonas putida as a response to sub-lethal oxidative stress. The ISME Journal, 15:1751-1766, Jan 2021. URL: https://doi.org/10.1038/s41396-020-00884-9, doi:10.1038/s41396-020-00884-9. This article has 165 citations.

16. (dvorak2023genomicandmetabolic pages 45-48): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Genomic and metabolic plasticity drive alternative scenarios for adapting pseudomonas putida to non-native substrate d-xylose. bioRxiv, May 2023. URL: https://doi.org/10.1101/2023.05.19.541448, doi:10.1101/2023.05.19.541448. This article has 0 citations.

17. (dvorak2024syntheticallyprimedadaptationof pages 4-5): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

18. (chavarria2016ametabolicwidget pages 10-12): Max Chavarría, Ángel Goñi-Moreno, Víctor de Lorenzo, and Pablo I. Nikel. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in pseudomonas putida. mSystems, Dec 2016. URL: https://doi.org/10.1128/msystems.00154-16, doi:10.1128/msystems.00154-16. This article has 42 citations and is from a peer-reviewed journal.

19. (chavarria2016ametabolicwidget pages 12-13): Max Chavarría, Ángel Goñi-Moreno, Víctor de Lorenzo, and Pablo I. Nikel. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in pseudomonas putida. mSystems, Dec 2016. URL: https://doi.org/10.1128/msystems.00154-16, doi:10.1128/msystems.00154-16. This article has 42 citations and is from a peer-reviewed journal.

20. (nguyen2019criticallyreevaluatingcarbohydrate pages 15-21): Austin Nguyen. Critically re-evaluating carbohydrate metabolism in pseudomonas aeruginosa. Unknown, Sep 2019. URL: https://doi.org/10.11575/prism/37096, doi:10.11575/prism/37096. This article has 1 citations.

21. (nguyen2021theanoxicelectrode‐driven pages 5-7): Anh Vu Nguyen, Bin Lai, Lorenz Adrian, and Jens O. Krömer. The anoxic electrode‐driven fructose catabolism of pseudomonas putida kt2440. Microbial Biotechnology, 14:1784-1796, Jun 2021. URL: https://doi.org/10.1111/1751-7915.13862, doi:10.1111/1751-7915.13862. This article has 13 citations and is from a peer-reviewed journal.

22. (chavarria2016ametabolicwidget pages 9-10): Max Chavarría, Ángel Goñi-Moreno, Víctor de Lorenzo, and Pablo I. Nikel. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in pseudomonas putida. mSystems, Dec 2016. URL: https://doi.org/10.1128/msystems.00154-16, doi:10.1128/msystems.00154-16. This article has 42 citations and is from a peer-reviewed journal.

23. (chavarria2016ametabolicwidget pages 5-6): Max Chavarría, Ángel Goñi-Moreno, Víctor de Lorenzo, and Pablo I. Nikel. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in pseudomonas putida. mSystems, Dec 2016. URL: https://doi.org/10.1128/msystems.00154-16, doi:10.1128/msystems.00154-16. This article has 42 citations and is from a peer-reviewed journal.

24. (shah2022glucose6phosphatedehydrogenasezwfa pages 5-8): Bhavik A. Shah, Sravanti T. Kasarlawar, and Prashant S. Phale. Glucose-6-phosphate dehydrogenase, zwfa, a dual cofactor-specific isozyme is predominantly involved in the glucose metabolism of pseudomonas bharatica csv86 <sup>t</sup>. Dec 2022. URL: https://doi.org/10.1128/spectrum.03818-22, doi:10.1128/spectrum.03818-22. This article has 10 citations and is from a domain leading peer-reviewed journal.

25. (chavarria2016ametabolicwidget pages 3-5): Max Chavarría, Ángel Goñi-Moreno, Víctor de Lorenzo, and Pablo I. Nikel. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in pseudomonas putida. mSystems, Dec 2016. URL: https://doi.org/10.1128/msystems.00154-16, doi:10.1128/msystems.00154-16. This article has 42 citations and is from a peer-reviewed journal.

26. (shah2022glucose6phosphatedehydrogenasezwfa pages 8-11): Bhavik A. Shah, Sravanti T. Kasarlawar, and Prashant S. Phale. Glucose-6-phosphate dehydrogenase, zwfa, a dual cofactor-specific isozyme is predominantly involved in the glucose metabolism of pseudomonas bharatica csv86 <sup>t</sup>. Dec 2022. URL: https://doi.org/10.1128/spectrum.03818-22, doi:10.1128/spectrum.03818-22. This article has 10 citations and is from a domain leading peer-reviewed journal.

27. (wilkes2019acyclicmetabolic pages 9-12): Rebecca A. Wilkes, Caroll M. Mendonca, and Ludmilla Aristilde. A cyclic metabolic network in pseudomonas protegens pf-5 prioritizes the entner-doudoroff pathway and exhibits substrate hierarchy during carbohydrate co-utilization. Applied and Environmental Microbiology, Jan 2019. URL: https://doi.org/10.1128/aem.02084-18, doi:10.1128/aem.02084-18. This article has 35 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. nikel2016fromdirtto pages 3-5
2. nikel2016fromdirtto pages 5-6
3. dvorak2024syntheticallyprimedadaptationof pages 3-4
4. nikel2020redoxstressreshapes pages 1-4
5. dvorak2024syntheticallyprimedadaptationof pages 5-6
6. chen2024gnurrepressesthe pages 1-3
7. volke2021cofactorspecificityof pages 4-6
8. dvorak2023genomicandmetabolic pages 45-48
9. weimer2020industrialbiotechnologyof pages 1-3
10. wilkes2019acyclicmetabolic pages 9-12
11. volke2021cofactorspecificityof pages 11-13
12. volke2021cofactorspecificityof pages 2-4
13. volke2021cofactorspecificityof pages 7-9
14. volke2021cofactorspecificityof pages 9-11
15. dvorak2023genomicandmetabolic pages 22-26
16. nikel2020redoxstressreshapes pages 6-9
17. dvorak2024syntheticallyprimedadaptationof pages 4-5
18. chavarria2016ametabolicwidget pages 10-12
19. chavarria2016ametabolicwidget pages 12-13
20. nguyen2019criticallyreevaluatingcarbohydrate pages 15-21
21. chavarria2016ametabolicwidget pages 9-10
22. chavarria2016ametabolicwidget pages 5-6
23. chavarria2016ametabolicwidget pages 3-5
24. https://doi.org/10.1016/j.cbpa.2016.05.011,
25. https://doi.org/10.1128/msystems.00014-21,
26. https://doi.org/10.1038/s41467-024-46812-9,
27. https://doi.org/10.1101/2020.06.13.149542,
28. https://doi.org/10.1111/1751-7915.70059,
29. https://doi.org/10.1007/s00253-020-10811-9,
30. https://doi.org/10.1101/2023.05.19.541448,
31. https://doi.org/10.1038/s41396-020-00884-9,
32. https://doi.org/10.1128/msystems.00154-16,
33. https://doi.org/10.11575/prism/37096,
34. https://doi.org/10.1111/1751-7915.13862,
35. https://doi.org/10.1128/spectrum.03818-22,
36. https://doi.org/10.1128/aem.02084-18,