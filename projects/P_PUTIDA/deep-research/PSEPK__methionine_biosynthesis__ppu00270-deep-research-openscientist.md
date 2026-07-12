---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:15:27.393763'
end_time: '2026-07-11T16:27:09.613257'
duration_seconds: 702.22
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-methionine biosynthesis (from homoserine)
  module_summary: 'De novo biosynthesis of L-methionine from L-homoserine, modelled
    as a species-agnostic pathway template with alternative routes at three steps,
    so the same logic can be evaluated across genomes (a eukaryote-to-prokaryote test
    of the module satisfiability engine). Homoserine is first activated by acylation,
    for which bacteria use either an O-succinyltransferase (metA) or an O-acetyltransferase
    (metX). Sulfur is then incorporated to give homocysteine by one of two routes:
    trans-sulfuration (cystathionine gamma-synthase metB plus cystathionine beta-lyase
    metC, drawing sulfur from cysteine) or direct sulfhydrylation (an O-acyl-homoserine
    sulfhydrylase, metY/metZ, using free sulfide in a single step). Finally homocysteine
    is methylated to methionine by either the cobalamin-independent synthase (metE)
    or the cobalamin-dependent synthase (metH). Because every step has alternatives,
    no single enzyme is universally required; an organism makes methionine if it encodes
    at least one option at each of the three steps. This mirrors GapMind-style pathway
    reconstruction: the template defines steps and route alternatives, and a per-genome
    oracle decides which candidates are present.'
  module_outline: "- L-methionine biosynthesis\n  - 1. acylation of homoserine (succinyl\
    \ or acetyl)\n  - Homoserine activation by acylation\n    - Alternative versions\
    \ by acyl donor: Homoserine acyltransferase\n      - O-succinyltransferase (metA)\n\
    \        - metA: homoserine O-succinyltransferase (molecular player: metA (homoserine\
    \ O-succinyltransferase); activity or role: homoserine O-succinyltransferase activity)\n\
    \      - O-acetyltransferase (metX)\n        - metX: homoserine O-acetyltransferase\
    \ (molecular player: metX (homoserine O-acetyltransferase); activity or role:\
    \ homoserine O-acetyltransferase activity)\n  - 2. sulfur incorporation to homocysteine\
    \ (trans-sulfuration or direct)\n  - Sulfur incorporation to homocysteine\n  \
    \  - Alternative versions by sulfur source: Sulfur-incorporation route\n     \
    \ - Trans-sulfuration (metB + metC)\n        - 1. cystathionine formation\n  \
    \      - Cystathionine gamma-synthase\n          - metB: cystathionine gamma-synthase\
    \ (molecular player: metB (cystathionine gamma-synthase); activity or role: cystathionine\
    \ gamma-synthase activity)\n        - 2. cystathionine cleavage to homocysteine\n\
    \        - Cystathionine beta-lyase\n          - metC: cystathionine beta-lyase\
    \ (molecular player: metC (cystathionine beta-lyase); activity or role: cysteine-S-conjugate\
    \ beta-lyase activity)\n      - Direct sulfhydrylation (metY)\n        - metY:\
    \ O-acylhomoserine sulfhydrylase (molecular player: metY (O-acetylhomoserine sulfhydrylase);\
    \ activity or role: O-acetylhomoserine aminocarboxypropyltransferase activity)\n\
    \  - 3. methylation of homocysteine to methionine (cobalamin-independent or -dependent)\n\
    \  - Homocysteine methylation to methionine\n    - Alternative versions by cobalamin\
    \ dependence: Methionine synthase\n      - Cobalamin-independent synthase (metE)\n\
    \        - metE: cobalamin-independent methionine synthase (molecular player:\
    \ metE (cobalamin-independent methionine synthase); activity or role: 5-methyltetrahydropteroyltriglutamate-homocysteine\
    \ S-methyltransferase activity)\n      - Cobalamin-dependent synthase (metH)\n\
    \        - metH: cobalamin-dependent methionine synthase (molecular player: metH\
    \ (cobalamin-dependent methionine synthase); activity or role: methionine synthase\
    \ activity)"
  module_connections: '- Homoserine activation by acylation precedes Sulfur incorporation
    to homocysteine

    - Sulfur incorporation to homocysteine precedes Homocysteine methylation to methionine'
  pathway_query: ppu00270
  pathway_id: ppu00270
  pathway_name: Cysteine and methionine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00270 with 16 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '46'
  candidate_genes: '- PP_0228: PP_0228 | Q88RA5 | serine O-acetyltransferase (EC 2.3.1.30)
    (EC 2.3.1.30; primary bucket kegg:ppu00543)

    - gshA: PP_0243 | Q88R90 | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS)
    (GCS) (Gamma-glutamylcysteine synthetase) (EC 6.3.2.2; primary bucket kegg:ppu00340)

    - tdcG-I: PP_0297 | Q88R37 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00270)

    - yfiH: PP_0624 | Q88Q72 | Purine nucleoside phosphorylase (primary bucket kegg:ppu00270)

    - mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37;
    primary bucket kegg:ppu00566)

    - metB: PP_0659 | Q88Q39 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)

    - PP_0664: PP_0664 | Q88Q34 | homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3;
    primary bucket kegg:ppu00300)

    - cysE: PP_0840 | Q88PL0 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - tdcG-II: PP_0987 | Q88P66 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00270)

    - PP_1110: PP_1110 | Q88NU4 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - mdeA: PP_1308 | Q88NA4 | L-methionine gamma-lyase (EC 4.4.1.11) (EC 4.4.1.11;
    primary bucket kegg:ppu00450)

    - hom: PP_1470 | Q88MU8 | Homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary
    bucket kegg:ppu00300)

    - PP_1541: PP_1541 | Q88MN0 | Methyltransferase (primary bucket kegg:ppu00270)

    - cysM: PP_1654 | Q88MC0 | Cysteine synthase (EC 2.5.1.47) (EC 2.5.1.47; primary
    bucket kegg:ppu00270)

    - mtnA: PP_1766 | Q88M09 | Methylthioribose-1-phosphate isomerase (M1Pi) (MTR-1-P
    isomerase) (EC 5.3.1.23) (S-methyl-5-thioribose-1-phosphate isomerase) (EC 5.3.1.23;
    primary bucket kegg:ppu00270)

    - serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine
    aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)

    - PP_1832: PP_1832 | Q88LU5 | Oxidase (primary bucket kegg:ppu00270)

    - msrC: PP_1877 | Q88LQ2 | Free methionine-(R)-sulfoxide reductase (EC 1.8.4.14)
    (EC 1.8.4.14; primary bucket kegg:ppu00270)

    - tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - asd__Q88LE4: PP_1989 | Q88LE4 | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase)
    (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenase) (EC 1.2.1.11;
    primary bucket kegg:ppu00261)

    - metZ: PP_2001 | Q88LD4 | O-succinylhomoserine sulfhydrylase (OSH sulfhydrylase)
    (OSHS sulfhydrylase) (EC 2.5.1.-) (EC 2.5.1.-; primary bucket kegg:ppu00270)

    - metH: PP_2375 | Q88KB5 | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine
    methyltransferase) (EC 2.1.1.13; primary bucket kegg:ppu04980)

    - PP_2528: PP_2528 | Q88JW9 | O-acetylhomoserine (Thiol)-lyase (EC 2.5.1.49) (EC
    2.5.1.49; primary bucket kegg:ppu00270)

    - PP_2533: PP_2533 | Q88JW4 | D-isomer specific 2-hydroxyacid dehydrogenase family
    protein (primary bucket kegg:ppu00680)

    - metE: PP_2698 | Q88JF1 | 5-methyltetrahydropteroyltriglutamate-homocysteine
    methyltransferase (primary bucket kegg:ppu00450)

    - PP_2930: PP_2930 | Q88IR9 | L-serine ammonia-lyase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00290)

    - PP_3029: PP_3029 | Q88IH0 | DNA (cytosine-5-)-methyltransferase (EC 2.1.1.37)
    (EC 2.1.1.37; primary bucket kegg:ppu00270)

    - PP_3136: PP_3136 | Q88I65 | Serine acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - tdcG-III: PP_3144 | Q88I57 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17;
    primary bucket kegg:ppu00270)

    - PP_3254: PP_3254 | Q88HU9 | Nucleosidase (primary bucket kegg:ppu00270)

    - ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42)
    (EC 2.6.1.42; primary bucket kegg:ppu00290)

    - amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10)
    (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)

    - PP_3912: PP_3912 | Q88G14 | DNA (cytosine-5-)-methyltransferase (EC 2.1.1.37)
    (EC 2.1.1.37; primary bucket kegg:ppu00270)

    - PP_3989: PP_3989 | Q88FU3 | DNA (cytosine-5-)-methyltransferase (EC 2.1.1.37)
    (EC 2.1.1.37; primary bucket kegg:ppu00270)

    - PP_4348: PP_4348 | Q88EV4 | Cystathionine beta-lyase (primary bucket kegg:ppu00450)

    - PP_4473: PP_4473 | Q88EI9 | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) (EC
    2.7.2.4; primary bucket kegg:ppu00261)

    - cysK: PP_4571 | Q88E95 | Cysteine synthase (EC 2.5.1.47) (EC 2.5.1.47; primary
    bucket kegg:ppu01320)

    - PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)

    - PP_4637: PP_4637 | Q88E31 | 5-methyltetrahydropteroyltriglutamate-homocysteine
    S-methyltransferase family protein (primary bucket kegg:ppu00450)

    - rhdA: PP_4907 | Q88DC0 | Sulfurtransferase (primary bucket kegg:ppu04122)

    - metK: PP_4967 | Q88D60 | S-adenosylmethionine synthase (AdoMet synthase) (EC
    2.5.1.6) (MAT) (Methionine adenosyltransferase) (EC 2.5.1.6; primary bucket kegg:ppu00999)

    - ahcY: PP_4976 | A0A140FWS3 | Adenosylhomocysteinase (EC 3.13.2.1) (S-adenosyl-L-homocysteine
    hydrolase) (AdoHcyase) (EC 3.13.2.1; primary bucket kegg:ppu00670)

    - metXS: PP_5097 | Q88CT3 | Homoserine O-succinyltransferase (HST) (EC 2.3.1.46)
    (Homoserine transsuccinylase) (HTS) (EC 2.3.1.46; primary bucket kegg:ppu00270)

    - sseA: PP_5118 | Q88CR2 | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) (EC
    2.8.1.2; primary bucket kegg:ppu04122)

    - serA: PP_5155 | Q88CM5 | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC
    1.1.1.95) (2-oxoglutarate reductase) (EC 1.1.1.399; 1.1.1.95; primary bucket kegg:ppu00680)'
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
  path: PSEPK__methionine_biosynthesis__ppu00270-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__methionine_biosynthesis__ppu00270-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-methionine biosynthesis (from homoserine) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00270
- Resolved ID: ppu00270
- Resolved name: Cysteine and methionine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00270 with 16 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 46

- PP_0228: PP_0228 | Q88RA5 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- gshA: PP_0243 | Q88R90 | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) (EC 6.3.2.2; primary bucket kegg:ppu00340)
- tdcG-I: PP_0297 | Q88R37 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00270)
- yfiH: PP_0624 | Q88Q72 | Purine nucleoside phosphorylase (primary bucket kegg:ppu00270)
- mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37; primary bucket kegg:ppu00566)
- metB: PP_0659 | Q88Q39 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)
- PP_0664: PP_0664 | Q88Q34 | homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary bucket kegg:ppu00300)
- cysE: PP_0840 | Q88PL0 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- tdcG-II: PP_0987 | Q88P66 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00270)
- PP_1110: PP_1110 | Q88NU4 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- mdeA: PP_1308 | Q88NA4 | L-methionine gamma-lyase (EC 4.4.1.11) (EC 4.4.1.11; primary bucket kegg:ppu00450)
- hom: PP_1470 | Q88MU8 | Homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary bucket kegg:ppu00300)
- PP_1541: PP_1541 | Q88MN0 | Methyltransferase (primary bucket kegg:ppu00270)
- cysM: PP_1654 | Q88MC0 | Cysteine synthase (EC 2.5.1.47) (EC 2.5.1.47; primary bucket kegg:ppu00270)
- mtnA: PP_1766 | Q88M09 | Methylthioribose-1-phosphate isomerase (M1Pi) (MTR-1-P isomerase) (EC 5.3.1.23) (S-methyl-5-thioribose-1-phosphate isomerase) (EC 5.3.1.23; primary bucket kegg:ppu00270)
- serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)
- PP_1832: PP_1832 | Q88LU5 | Oxidase (primary bucket kegg:ppu00270)
- msrC: PP_1877 | Q88LQ2 | Free methionine-(R)-sulfoxide reductase (EC 1.8.4.14) (EC 1.8.4.14; primary bucket kegg:ppu00270)
- tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- asd__Q88LE4: PP_1989 | Q88LE4 | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase) (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenase) (EC 1.2.1.11; primary bucket kegg:ppu00261)
- metZ: PP_2001 | Q88LD4 | O-succinylhomoserine sulfhydrylase (OSH sulfhydrylase) (OSHS sulfhydrylase) (EC 2.5.1.-) (EC 2.5.1.-; primary bucket kegg:ppu00270)
- metH: PP_2375 | Q88KB5 | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) (EC 2.1.1.13; primary bucket kegg:ppu04980)
- PP_2528: PP_2528 | Q88JW9 | O-acetylhomoserine (Thiol)-lyase (EC 2.5.1.49) (EC 2.5.1.49; primary bucket kegg:ppu00270)
- PP_2533: PP_2533 | Q88JW4 | D-isomer specific 2-hydroxyacid dehydrogenase family protein (primary bucket kegg:ppu00680)
- metE: PP_2698 | Q88JF1 | 5-methyltetrahydropteroyltriglutamate-homocysteine methyltransferase (primary bucket kegg:ppu00450)
- PP_2930: PP_2930 | Q88IR9 | L-serine ammonia-lyase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00290)
- PP_3029: PP_3029 | Q88IH0 | DNA (cytosine-5-)-methyltransferase (EC 2.1.1.37) (EC 2.1.1.37; primary bucket kegg:ppu00270)
- PP_3136: PP_3136 | Q88I65 | Serine acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- tdcG-III: PP_3144 | Q88I57 | L-serine dehydratase (EC 4.3.1.17) (EC 4.3.1.17; primary bucket kegg:ppu00270)
- PP_3254: PP_3254 | Q88HU9 | Nucleosidase (primary bucket kegg:ppu00270)
- ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) (EC 2.6.1.42; primary bucket kegg:ppu00290)
- amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10) (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)
- PP_3912: PP_3912 | Q88G14 | DNA (cytosine-5-)-methyltransferase (EC 2.1.1.37) (EC 2.1.1.37; primary bucket kegg:ppu00270)
- PP_3989: PP_3989 | Q88FU3 | DNA (cytosine-5-)-methyltransferase (EC 2.1.1.37) (EC 2.1.1.37; primary bucket kegg:ppu00270)
- PP_4348: PP_4348 | Q88EV4 | Cystathionine beta-lyase (primary bucket kegg:ppu00450)
- PP_4473: PP_4473 | Q88EI9 | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) (EC 2.7.2.4; primary bucket kegg:ppu00261)
- cysK: PP_4571 | Q88E95 | Cysteine synthase (EC 2.5.1.47) (EC 2.5.1.47; primary bucket kegg:ppu01320)
- PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)
- PP_4637: PP_4637 | Q88E31 | 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase family protein (primary bucket kegg:ppu00450)
- rhdA: PP_4907 | Q88DC0 | Sulfurtransferase (primary bucket kegg:ppu04122)
- metK: PP_4967 | Q88D60 | S-adenosylmethionine synthase (AdoMet synthase) (EC 2.5.1.6) (MAT) (Methionine adenosyltransferase) (EC 2.5.1.6; primary bucket kegg:ppu00999)
- ahcY: PP_4976 | A0A140FWS3 | Adenosylhomocysteinase (EC 3.13.2.1) (S-adenosyl-L-homocysteine hydrolase) (AdoHcyase) (EC 3.13.2.1; primary bucket kegg:ppu00670)
- metXS: PP_5097 | Q88CT3 | Homoserine O-succinyltransferase (HST) (EC 2.3.1.46) (Homoserine transsuccinylase) (HTS) (EC 2.3.1.46; primary bucket kegg:ppu00270)
- sseA: PP_5118 | Q88CR2 | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) (EC 2.8.1.2; primary bucket kegg:ppu04122)
- serA: PP_5155 | Q88CM5 | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC 1.1.1.95) (2-oxoglutarate reductase) (EC 1.1.1.399; 1.1.1.95; primary bucket kegg:ppu00680)

## Generic Module Context

### Working Scope

De novo biosynthesis of L-methionine from L-homoserine, modelled as a species-agnostic pathway template with alternative routes at three steps, so the same logic can be evaluated across genomes (a eukaryote-to-prokaryote test of the module satisfiability engine). Homoserine is first activated by acylation, for which bacteria use either an O-succinyltransferase (metA) or an O-acetyltransferase (metX). Sulfur is then incorporated to give homocysteine by one of two routes: trans-sulfuration (cystathionine gamma-synthase metB plus cystathionine beta-lyase metC, drawing sulfur from cysteine) or direct sulfhydrylation (an O-acyl-homoserine sulfhydrylase, metY/metZ, using free sulfide in a single step). Finally homocysteine is methylated to methionine by either the cobalamin-independent synthase (metE) or the cobalamin-dependent synthase (metH). Because every step has alternatives, no single enzyme is universally required; an organism makes methionine if it encodes at least one option at each of the three steps. This mirrors GapMind-style pathway reconstruction: the template defines steps and route alternatives, and a per-genome oracle decides which candidates are present.

### Provisional Biological Outline

- L-methionine biosynthesis
  - 1. acylation of homoserine (succinyl or acetyl)
  - Homoserine activation by acylation
    - Alternative versions by acyl donor: Homoserine acyltransferase
      - O-succinyltransferase (metA)
        - metA: homoserine O-succinyltransferase (molecular player: metA (homoserine O-succinyltransferase); activity or role: homoserine O-succinyltransferase activity)
      - O-acetyltransferase (metX)
        - metX: homoserine O-acetyltransferase (molecular player: metX (homoserine O-acetyltransferase); activity or role: homoserine O-acetyltransferase activity)
  - 2. sulfur incorporation to homocysteine (trans-sulfuration or direct)
  - Sulfur incorporation to homocysteine
    - Alternative versions by sulfur source: Sulfur-incorporation route
      - Trans-sulfuration (metB + metC)
        - 1. cystathionine formation
        - Cystathionine gamma-synthase
          - metB: cystathionine gamma-synthase (molecular player: metB (cystathionine gamma-synthase); activity or role: cystathionine gamma-synthase activity)
        - 2. cystathionine cleavage to homocysteine
        - Cystathionine beta-lyase
          - metC: cystathionine beta-lyase (molecular player: metC (cystathionine beta-lyase); activity or role: cysteine-S-conjugate beta-lyase activity)
      - Direct sulfhydrylation (metY)
        - metY: O-acylhomoserine sulfhydrylase (molecular player: metY (O-acetylhomoserine sulfhydrylase); activity or role: O-acetylhomoserine aminocarboxypropyltransferase activity)
  - 3. methylation of homocysteine to methionine (cobalamin-independent or -dependent)
  - Homocysteine methylation to methionine
    - Alternative versions by cobalamin dependence: Methionine synthase
      - Cobalamin-independent synthase (metE)
        - metE: cobalamin-independent methionine synthase (molecular player: metE (cobalamin-independent methionine synthase); activity or role: 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase activity)
      - Cobalamin-dependent synthase (metH)
        - metH: cobalamin-dependent methionine synthase (molecular player: metH (cobalamin-dependent methionine synthase); activity or role: methionine synthase activity)

### Known Relationships Among Steps

- Homoserine activation by acylation precedes Sulfur incorporation to homocysteine
- Sulfur incorporation to homocysteine precedes Homocysteine methylation to methionine

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

# Module Review: L-Methionine Biosynthesis (from L-homoserine) in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway bucket:** kegg:ppu00270 "Cysteine and methionine metabolism"
**Module template:** de novo L-methionine from L-homoserine (3 steps, each with route alternatives)
**Prepared for:** manual module-satisfiability and gene-annotation curation

---

## 1. Executive summary

The three-step L-methionine-from-homoserine module is **SATISFIABLE** in *P. putida* KT2440: every step is covered by at least one credible candidate gene. The organism uses the characteristic *Pseudomonas* route — **O-succinyl activation** of homoserine followed by **single-step direct sulfhydrylation** — rather than the acetyl/trans-sulfuration-only logic assumed by many templates.

Three curation-critical conclusions:

1. **Activation (step 1) is covered with strong, target-specific evidence.** PP_5097 (`metXS`, Q88CT3) is a homoserine **O-succinyl**transferase (EC 2.3.1.46), UniProt **PE=1 "evidence at protein level."** Despite the *metX* family name it transfers **succinyl**, not acetyl — a well-documented misannotation hazard (Bastard et al. 2017, PMID 28581482).
2. **Sulfur incorporation (step 2) is covered by direct sulfhydrylation** via PP_2001 (`metZ`), which is substrate-matched to the O-succinyl intermediate. A parallel forward **trans-sulfuration** route (PP_0659 `metB` + PP_4348 `metC`) is also present. Two other PF01053 paralogs (PP_4594, PP_2528/`metY`) are **paralog-ambiguous** and should not be counted as primary evidence.
3. **Methylation (step 3): only the cobalamin-DEPENDENT alternative is genuinely present.** MetH (PP_2375) is a complete 1235-aa multidomain enzyme. The lone `metE` annotation (PP_2698, 344 aa, PE=4) is a **truncated single-domain protein and a likely over-annotation** — a functional cobalamin-independent MetE (~750 aa, two domains) is absent from the proteome. De novo methionine synthesis in KT2440 is effectively **B12-dependent**.

The module boundary framing "metA=succinyl vs metX=acetyl" and "metE OR metH both realized" is **incorrect for this lineage** and warrants `module_needs_revision` notes (see §6).

---

## 2. Target-organism pathway definition

**Included process:** conversion of L-homoserine → O-succinyl-L-homoserine → L-homocysteine → L-methionine (3 enzymatic steps). This is the terminal, methionine-specific segment of the aspartate/homoserine branch.

**Neighboring processes to keep separate (do NOT fold into this module):**
- Upstream aspartate→homoserine (`thrA`/`hom` PP_1470/PP_0664, `asd` PP_1989, `lysC`/aspartokinase PP_4473, `thrB` PP_0RK8) — threonine/lysine/homoserine supply, KEGG ppu00260/00261/00300.
- Cysteine biosynthesis / sulfur assimilation (`cysK` PP_4571, `cysM` PP_1654, `cysE`/serine acetyltransferases) — supplies the cysteine sulfur donor for trans-sulfuration but is a distinct module (ppu00920/00272).
- Downstream S-adenosylmethionine cycle: `metK` (PP_4967, SAM synthase), `ahcY` (PP_4976), `metH`-linked methyl-cycle — SAM/SAH metabolism, not de novo Met.
- Methionine **catabolism/salvage**: `mdeA` (PP_1308, methionine γ-lyase), the MTA/methylthioribose salvage genes (`mtnA` PP_1766, `PP_3254` nucleosidase), and methionine-sulfoxide reductase (`msrC` PP_1877). These are in the same KEGG map but are not biosynthetic.
- The many DNA cytosine-methyltransferases (PP_3029/PP_3912/PP_3989), serine dehydratases (`tdcG`), and aminotransferases in the candidate list are **map co-occurrence artifacts** of ppu00270, not methionine-biosynthesis genes.

**Alternate names / database definitions:** KEGG module **M00017** (methionine biosynthesis, aspartate → homocysteine → methionine); MetaCyc "L-methionine biosynthesis I/II/III" (I = trans-sulfuration + acetyl; II = direct sulfhydrylation; III = succinyl trans-sulfuration); UniPathway "L-methionine biosynthesis via de novo pathway." GapMind for amino-acid biosynthesis models the same step/route structure used here.

---

## 3. Expected step model (as realized in KT2440)

| Step | Template alternatives | Realized in KT2440 | Status |
|------|----------------------|--------------------|--------|
| 1. Homoserine activation | O-succinyl (metA) **or** O-acetyl (metX) | **O-succinyl** by MetX-family enzyme **PP_5097** (EC 2.3.1.46) | **covered** (direct, PE=1) |
| 2. Sulfur → homocysteine | direct sulfhydrylation (metY/metZ) **or** trans-sulfuration (metB+metC) | **metZ direct sulfhydrylation (PP_2001)** on O-succinyl-homoserine; **parallel** trans-sulfuration (PP_0659 metB + PP_4348 metC) | **covered** (homology, strong) |
| 3. Homocysteine methylation | cobalamin-independent (metE) **or** -dependent (metH) | **metH only (PP_2375)**; metE alternative absent/degenerate | **covered by metH**; metE = **candidate_uncertain/gap** |

Ordering constraints (activation → sulfur → methylation) are satisfied.

---

## 4. Candidate genes and evidence

### High-confidence, module-defining

**PP_5097 `metXS` (Q88CT3) — Step 1, activation.** Homoserine O-succinyltransferase, EC 2.3.1.46; catalytic reaction L-homoserine + succinyl-CoA → O-succinyl-L-homoserine + CoA; UniPathway step 1/1; **UniProt PE=1 (protein-level evidence)**. Highest-confidence gene in the set. Caveat: `metX`/`metA` gene names do **not** indicate acyl donor (PMID 28581482); the succinyl activity here is substrate-consistent with downstream MetZ. → **covered**.

**PP_2001 `metZ` (Q88LD4) — Step 2, direct sulfhydrylation.** O-succinylhomoserine sulfhydrylase, EC 2.5.1.-; O-succinyl-L-homoserine + H₂S → L-homocysteine + succinate; UniPathway L-homocysteine step 1/1; PE=3 (homology). Substrate-matched to PP_5097. Directly supported by the *P. aeruginosa* precedent (PMID 7704274). → **covered** (transfer from *P. aeruginosa* is strong: same genus, same intermediate).

**PP_2375 `metH` (Q88KB5) — Step 3, methylation.** Cobalamin-dependent methionine synthase, EC 2.1.1.13; complete 1235-aa multidomain protein (PF02310 B12-binding, PF02607, PF00809 pterin, PF02965, PF02574); PE=3. → **covered**; makes de novo Met **B12-dependent**.

**PP_0659 `metB` (Q88Q39) — Step 2, trans-sulfuration (cystathionine formation).** Cystathionine γ-synthase, PF01053, IPR054542; GO transsulfuration. Forward metB of the parallel route. → **covered (secondary route)**.

**PP_4348 `metC` (Q88EV4) — Step 2, trans-sulfuration (cystathionine cleavage).** Cystathionine β-lyase, PF01053 + IPR006233 (MetC-specific); L,L-cystathionine + H₂O → L-homocysteine + pyruvate + NH₄⁺. → **covered (secondary route)**.

### Paralog-ambiguous / context-specific (flag, do not use as primary evidence)

**PP_4594 (Q88E72) — "cystathionine γ-synthase".** PF01053 but GO = **cystathionine γ-LYASE** + **L-cysteine biosynthesis via cystathionine**; best interpreted as a reverse-transsulfuration enzyme (cysteine formation), not the forward metB. → **candidate_uncertain**.

**PP_2528 `metY` (Q88JW9) — "O-acetylhomoserine (thiol)-lyase".** PF01053 + IPR006235; GO O-acetylhomoserine aminocarboxypropyltransferase + cysteine synthase. Its substrate (O-**acetyl**-homoserine) is **not** the intermediate produced by the O-succinyl activation route, so its de novo methionine role in KT2440 is uncertain (may act in cysteine/sulfide chemistry or on alternative substrates). → **candidate_uncertain**.

**PP_2698 `metE` (Q88JF1) — "5-methyl-THF-triglutamate–homocysteine methyltransferase".** Only 344 aa, PE=4 (predicted), carries **only** the C-terminal PF01717 (Meth_synt_2) domain. Functional MetE needs both N-terminal PF08267 and C-terminal PF01717 (~750 aa). → **likely over-annotation / gap** (see §5).

**PP_4637 (Q88E31) — MetE-family (274 aa, PF08267 only).** Partial N-terminal domain; not a stand-alone methionine synthase. → not a functional metE.

### Related but out-of-module (context only)
`metK` (PP_4967, SAM synthase), `ahcY` (PP_4976, SAH hydrolase), `mdeA` (PP_1308, Met γ-lyase = catabolism), `mtnA`/`PP_3254` (Met salvage), Q88Q40/Q88J73 (homocysteine S-methyltransferase/MmuM-type salvage, not de novo metE).

---

## 5. Gaps, ambiguities, and likely over-annotations

- **metE step (cobalamin-independent methionine synthase) — likely GAP / over-annotation.** No full-length two-domain MetE in UP000000556. The single `metE` (PP_2698) is a truncated PF01717-only protein (PE=4). This is the most consequential deviation: KT2440's de novo methylation is realized **only** via cobalamin-dependent MetH, making the pathway **B12-dependent**. This is physiologically viable because KT2440 encodes a **complete de novo cobalamin biosynthesis operon set** (cobI/G/J/M/H/K/L, cbiD, cobaltochelatase cobN, adenosyltransferases cobO/pduO, cobQ/D/S/T, plus a cobalamin ABC transporter — 22 corrin/B12 genes in UP000000556), so MetH has its cofactor and no functional MetE is required. The "metE" template alternative is therefore **not genuinely satisfied** (not merely unannotated). → mark **candidate_uncertain**, lean **gap**.
- **Acyl-donor mis-framing.** The template's "metA=succinyl vs metX=acetyl" dichotomy is wrong here: a MetX-family enzyme performs the **succinyl** activation (PMID 28581482 predicts >60% of MetA/MetX sequences are misannotated). Curators must derive acyl donor from biochemistry/InterPro sub-signature, not gene name.
- **PF01053 paralog family (metZ/metB/metC/metY/PP_4594).** Six+ proteins share this PLP fold with broad EC (2.5.1.-, 2.5.1.49) and overlapping GO; specificity must be assigned from InterPro sub-signatures (IPR006233 metC; IPR006235 metY; IPR054542 metB-like) rather than family-level annotation. PP_4594 and PP_2528 are the main over-propagation risks.
- **Bucket contamination.** The 46-gene candidate list mixes in DNA methyltransferases, serine dehydratases, sulfurtransferases, and generic aminotransferases that co-occur on KEGG map ppu00270 but are unrelated to methionine biosynthesis.

---

## 6. Module and GO-curation recommendations

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| Homoserine activation (acylation) | **covered** — O-succinyl branch (PP_5097) | Direct PE=1 evidence; acetyl branch not_expected_in_target_taxon |
| — O-acetyltransferase (metX-acetyl) sub-branch | **not_expected_in_target_taxon** | KT2440 activation is succinyl |
| Sulfur incorporation — direct sulfhydrylation (metZ) | **covered** (primary) | PP_2001 substrate-matched; genus precedent |
| Sulfur incorporation — trans-sulfuration (metB+metC) | **covered** (parallel/secondary) | PP_0659 + PP_4348 |
| — metY (O-acetylhomoserine) direct sulfhydrylation | **candidate_uncertain** | PP_2528 substrate mismatch |
| Methylation — cobalamin-dependent (metH) | **covered** | Complete PP_2375; KT2440 makes B12 de novo (viable) |
| Methylation — cobalamin-independent (metE) | **candidate_uncertain → gap** | PP_2698 truncated single-domain, PE=4 |

**Module-boundary revisions (`module_needs_revision`):**
1. Reframe step 1 as "homoserine acyl-transfer (acetyl **or** succinyl), donor determined biochemically" rather than binding donor to the metA/metX gene name.
2. Note lineage rule for *Pseudomonas*: **O-succinyl + direct sulfhydrylation (metZ)** is diagnostic and unusual (only genus using O-succinyl-homoserine for direct sulfhydrylation, PMID 7704274).
3. Add a satisfiability caveat that the metE alternative can be a truncated over-annotation; require a length/two-domain (PF08267+PF01717) check before scoring metE "present."

**GO-curation:** PP_2698 GO `5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase activity` should be reviewed/qualified given the truncation (candidate for NOT/with-caveat). PP_4594 GO conflicts (γ-synthase name vs γ-lyase GO) should be reconciled. No new GO terms appear necessary; existing terms suffice if applied at correct specificity.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_2698 `metE` (Q88JF1)** — resolve whether truncated protein is a functional methionine synthase, a salvage-type homocysteine methyltransferase, or a pseudo/fragment. Highest priority (decides metE gap call).
2. **PP_5097 `metXS` (Q88CT3)** — confirm the experimental basis of PE=1 and the succinyl-CoA specificity (anchor gene; verify it is the KT2440 activation enzyme).
3. **PP_2001 `metZ` (Q88LD4)** — confirm O-succinylhomoserine (vs O-acetyl) specificity in KT2440; central to the direct-sulfhydrylation call.
4. **PP_4594 (Q88E72)** and **PP_2528 `metY` (Q88JW9)** — assign forward-metB vs reverse-γ-lyase (PP_4594) and de-novo relevance vs cysteine/O-acetyl chemistry (metY).

---

## 8. Key references

- Foglino M, et al. (1995) *A direct sulfhydrylation pathway is used for methionine biosynthesis in Pseudomonas aeruginosa.* **PMID 7704274.** Establishes O-succinylhomoserine synthase + metZ direct sulfhydrylation; Pseudomonas uniquely uses O-succinyl-homoserine for direct sulfhydrylation; trans-sulfuration present in parallel.
- Bastard K, et al. (2017) *Parallel evolution of non-homologous isofunctional enzymes in methionine biosynthesis.* Nat Chem Biol. **PMID 28581482.** MetA/MetX acyl-donor cannot be inferred from family; >60% of ~10,000 sequences likely misannotated; recent bacteria evolved succinyl-using MetX.
- Bourhy P, et al. (1997) *Homoserine O-acetyltransferase … Leptospira meyeri … MetX.* **PMID 9209059.** Illustrates a MetX with acetyl activity (contrasting lineage), reinforcing donor ambiguity.
- UniProt (2024) entries Q88CT3, Q88LD4, Q88Q39, Q88EV4, Q88E72, Q88JW9, Q88JF1, Q88E31, Q88KB5 (proteome UP000000556) — annotations, EC, Pfam/InterPro, protein-existence evidence used throughout.

---

*Evidence transfer notes:* Step-1 activation is **direct** (PE=1, KT2440). Steps 2–3 gene assignments are **homology-based** within KT2440 but strongly corroborated by **same-genus** experimental work (*P. aeruginosa*, PMID 7704274); genus transfer is strong for the succinyl/direct-sulfhydrylation logic. The metE gap call rests on **sequence/domain-architecture** analysis of the KT2440 proteome (strong), general MetE biochemistry (strong), and the presence of a **complete de novo cobalamin biosynthetic gene set** (strong) that makes a MetH-only route viable. Remaining open experimental questions: a direct growth demonstration of B12-conditional methionine auxotrophy in a KT2440 ΔmetH background, and substrate-specificity assays for PP_2528 (metY) and PP_4594 to settle their de novo relevance.


## Artifacts

- [OpenScientist final report](PSEPK__methionine_biosynthesis__ppu00270-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__methionine_biosynthesis__ppu00270-deep-research-openscientist_artifacts/final_report.pdf)