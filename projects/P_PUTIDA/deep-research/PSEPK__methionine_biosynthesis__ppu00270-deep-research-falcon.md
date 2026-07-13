---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T16:02:12.812849'
end_time: '2026-07-06T16:24:57.602434'
duration_seconds: 1364.79
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
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PSEPK__methionine_biosynthesis__ppu00270-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__methionine_biosynthesis__ppu00270-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PSEPK__methionine_biosynthesis__ppu00270-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
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

# L-Methionine Biosynthesis from Homoserine in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

The L-methionine biosynthesis module from homoserine is **fully satisfiable** in *Pseudomonas putida* KT2440 (NCBI taxon 160488; proteome UP000000556). All three required pathway steps—homoserine acylation, sulfur incorporation to homocysteine, and homocysteine methylation to methionine—are covered by at least one high-confidence gene assignment. The biologically preferred route in this organism proceeds via: (1) O-succinylation of homoserine by the two-component MetXW system (PP_5097/PP_5098), (2) direct sulfhydrylation of O-succinylhomoserine to homocysteine by MetZ (PP_2001), and (3) methylation of homocysteine by either the cobalamin-independent MetE (PP_2698) or cobalamin-dependent MetH (PP_2375) (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11). This pathway configuration is characteristic of pseudomonads and differs importantly from the enteric bacterial model (e.g., *E. coli*), which uses a single-polypeptide MetA for acylation and relies primarily on trans-sulfuration (MetB + MetC) for sulfur incorporation (vermeij1999pathwaysofassimilative pages 1-2, vermeij1999pathwaysofassimilative pages 2-3). Of the 46 candidate genes provided, only 5 are high-confidence core pathway members, 4 are medium-confidence paralogs or candidates, and the majority belong to neighboring pathways (upstream precursor supply, downstream SAM cycle, cysteine biosynthesis) or are annotation over-propagations from the broad KEGG ppu00270 "cysteine and methionine metabolism" map.

## 2. Target-Organism Pathway Definition

### Biochemical process included

The scoped module covers de novo biosynthesis of L-methionine starting from L-homoserine. It encompasses three enzymatic steps: (i) acylation of homoserine to O-acyl-L-homoserine, (ii) sulfur incorporation to form L-homocysteine (via either direct sulfhydrylation or trans-sulfuration through cystathionine), and (iii) methylation of homocysteine to methionine (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11).

### Neighboring pathways to keep separate

The following should be excluded from this module:
- **Upstream precursor supply**: aspartate kinase (PP_4473), aspartate-semialdehyde dehydrogenase (PP_1989/asd), and homoserine dehydrogenase (PP_1470/hom, PP_0664) supply homoserine but belong to the aspartate-family amino acid biosynthesis branch (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 9-11).
- **Downstream SAM cycle**: S-adenosylmethionine synthase (metK, PP_4967) and adenosylhomocysteinase (ahcY, PP_4976) operate after methionine formation.
- **Cysteine biosynthesis**: serine O-acetyltransferases (cysE), cysteine synthases (cysK, cysM), and sulfate assimilation genes are part of the parallel cysteine pathway (molina‐henares2010identificationofconditionally pages 9-11).
- **Methionine salvage/catabolism**: methylthioribose-1-phosphate isomerase (mtnA, PP_1766), methionine γ-lyase (mdeA, PP_1308), and methionine sulfoxide reductase (msrC, PP_1877) handle recycling and repair (vermeij1999pathwaysofassimilative pages 3-5).

### Database definitions

KEGG map ppu00270 ("Cysteine and methionine metabolism") is far broader than this module, encompassing cysteine biosynthesis, SAM cycling, methionine salvage, and catabolism. MetaCyc pathway "L-methionine biosynthesis I" and GapMind-style module templates more closely match the scoped three-step process.

## 3. Expected Step Model

The pathway step model with all route alternatives, evidence types, and KT2440 status assessments is summarized below:

| Step | Alternative Route | Gene(s) | Locus Tag(s) | EC Number | Evidence Type | Status in KT2440 | Notes |
|---|---|---|---|---|---|---|---|
| 1. Acylation of homoserine | O-succinyltransferase / homoserine acylation by two-component MetXW system | metXW | PP_5097-PP_5098 | 2.3.1.46 for MetX/HST; MetW accessory/non-catalytic partner, no separate EC clearly assigned | Direct target-organism evidence: genomic assignment, operon structure, and metX mutant methionine auxotrophy; pathway described specifically for KT2440 | **Covered; preferred/established route** | KT2440 uses metXW rather than the classical single-polypeptide metA route. metX mutant is methionine auxotroph; cysteine does not rescue, supporting placement at pathway entry (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 9-11) |
| 1. Acylation of homoserine | O-acetyltransferase alternative | metA / metX (single-polypeptide O-acetyltransferase type) | Not identified in KT2440 candidate set | Typically 2.3.1.31 or 2.3.1.- depending on enzyme family | Comparative pathway knowledge only; no KT2440-specific gene support found | **Not covered / not expected as primary route** | Generic module should allow this route, but current KT2440 evidence supports metXW-mediated O-succinylation instead; no convincing KT2440 metA-like alternative was found (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11) |
| 2. Sulfur incorporation to homocysteine | Direct sulfhydrylation via O-succinylhomoserine sulfhydrylase | metZ | PP_2001 | 2.5.1.- | Direct/strong evidence from KT2440 pathway descriptions; strong species-transfer support from P. putida sulfur-metabolism physiology | **Covered; primary/preferred route** | Literature on pseudomonads indicates direct sulfhydrylation is strongly preferred over trans-sulfuration. In KT2440, metZ is the named second-step enzyme; in related P. putida physiology, this route is dominant (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 2-3, molina‐henares2010identificationofconditionally pages 9-11) |
| 2. Sulfur incorporation to homocysteine | Trans-sulfuration via cystathionine | metB + metC | PP_0659 + PP_0658 | MetB: 2.5.1.48; MetC: 4.4.1.8 | KT2440 genomic evidence plus related-species biochemical physiology | **Covered but secondary / low-activity route** | KT2440 has metBC homologs, but P. putida physiology indicates this route is poorly active under most conditions and may become more relevant when cysteine is sole sulfur source. Important for curation, but not the preferred route for de novo methionine synthesis (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 1-2, vermeij1999pathwaysofassimilative pages 2-3, molina‐henares2010identificationofconditionally pages 9-11) |
| 2. Sulfur incorporation to homocysteine | Direct sulfhydrylation via metY-like O-acylhomoserine sulfhydrylase | metY-like candidate | PP_2528 | 2.5.1.49 or 2.5.1.- | Homology-based inference only | **Candidate_uncertain** | Santos et al. noted a KT2440 ortholog of Corynebacterium glutamicum metY, but direct functional validation in KT2440 was not found. Could represent a backup or misannotated paralog; merits deeper review (santos2004insightsintothe pages 5-7) |
| 2. Sulfur incorporation to homocysteine | Additional cystathionine beta-lyase annotation | putative metC paralog | PP_4348 | 4.4.1.8 (annotated) | Annotation only; no direct pathway evidence found | **Candidate_uncertain / likely over-annotation until reviewed** | Because PP_0658 sits adjacent to metB and matches the expected metBC organization, PP_4348 is less compelling as the main pathway metC. Needs sequence/neighborhood review before accepting as a functional duplicate (molina‐henares2010identificationofconditionally pages 9-11, vermeij1999pathwaysofassimilative pages 2-3) |
| 3. Methylation of homocysteine to methionine | Cobalamin-independent methionine synthase | metE | PP_2698 | 2.1.1.14 | Direct KT2440 pathway descriptions; comparative regulon support | **Covered** | One of two alternative terminal methylation enzymes in KT2440. Useful under B12 limitation; MetR-regulated methionine regulons across Proteobacteria commonly include metE (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11, leyn2014comparativegenomicsof pages 9-10) |
| 3. Methylation of homocysteine to methionine | Cobalamin-dependent methionine synthase | metH | PP_2375 | 2.1.1.13 | Direct KT2440 pathway descriptions; comparative regulon support | **Covered** | Second terminal methylation option in KT2440. Presence of both metE and metH provides flexibility with respect to cobalamin availability; PP_2375 is specifically identified in KT2440 pathway descriptions (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11, leyn2014comparativegenomicsof pages 9-10) |


*Table: This table summarizes the stepwise pathway model for L-methionine biosynthesis from homoserine in Pseudomonas putida KT2440, including route alternatives, candidate genes, evidence types, and curation status. It is useful for deciding which module steps are covered, secondary, uncertain, or not expected in this organism.*

## 4. Candidate Genes and Evidence

### 4.1 High-confidence core pathway genes

**metXS / metXW (PP_5097 / PP_5098) — Step 1: Homoserine O-succinyltransferase.** Unlike the single-polypeptide MetA of *E. coli*, *P. putida* KT2440 uses a two-component system in which MetX (PP_5097, EC 2.3.1.46) catalyzes homoserine O-succinylation and MetW (PP_5098) acts as an accessory subunit (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 7-9). The metXW genes form an operon (molina‐henares2010identificationofconditionally pages 9-11). A metX transposon mutant was isolated four independent times in a genome-wide screen and is a strict methionine auxotroph; growth was not restored by external cysteine, confirming that the route from cysteine to homocysteine does not operate under standard conditions in *P. putida* (molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 9-11). This is the strongest direct evidence in the target organism. The candidate gene list labels PP_5097 as "metXS" (homoserine O-succinyltransferase), which is consistent with this assignment.

**metZ (PP_2001) — Step 2: O-succinylhomoserine sulfhydrylase.** MetZ catalyzes direct sulfhydrylation of O-succinylhomoserine to yield homocysteine, using free sulfide as the sulfur donor (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 2-3). Biochemical studies in the related *P. putida* S-313 demonstrated that O-succinyl-L-homoserine sulfhydrylase activity is present at substantial levels, and direct sulfhydrylation is strongly preferred over trans-sulfuration under most growth conditions (vermeij1999pathwaysofassimilative pages 1-2, vermeij1999pathwaysofassimilative pages 2-3, vermeij1999pathwaysofassimilative pages 5-5). PP_2001 (metZ) is located in an operon with purF (PP_2000) (molina‐henares2010identificationofconditionally pages 9-11). This gene is annotated with EC 2.5.1.- consistent with the sulfhydrylase activity.

**metH (PP_2375) — Step 3: Cobalamin-dependent methionine synthase.** PP_2375 is transcribed divergently from the cti gene (encoding cis-to-trans isomerase of unsaturated fatty acids) (molina‐henares2010identificationofconditionally pages 9-11). MetH (EC 2.1.1.13) catalyzes the final methylation of homocysteine to methionine using methylcobalamin as cofactor. Both MetH and MetE provide pathway redundancy at the terminal step (santos2004insightsintothe pages 5-7).

**metE (PP_2698) — Step 3: Cobalamin-independent methionine synthase.** PP_2698 encodes the 5-methyltetrahydropteroyltriglutamate–homocysteine S-methyltransferase (EC 2.1.1.14), providing a B12-independent route to methionine (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11). MetE is part of the core MetR regulon across Proteobacteria, where the MetR-metE divergon is a widely conserved regulatory unit (leyn2014comparativegenomicsof pages 9-10).

**metB (PP_0659) — Step 2 (trans-sulfuration route): Cystathionine γ-synthase.** PP_0659 is the primary cystathionine γ-synthase candidate, adjacent to the metC-like gene PP_0658 (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11, vermeij1999pathwaysofassimilative pages 2-3). However, the trans-sulfuration route is secondary in pseudomonads; under most conditions, cystathionine γ-synthase and β-lyase activities are expressed at low levels, and direct sulfhydrylation predominates (vermeij1999pathwaysofassimilative pages 1-2, vermeij1999pathwaysofassimilative pages 2-3). Trans-sulfuration may become more active when cysteine is the sole sulfur source (vermeij1999pathwaysofassimilative pages 3-5).

### 4.2 Medium-confidence candidates and paralogs

**PP_0658 (metC-like, adjacent to metB) — Cystathionine β-lyase.** PP_0658 is the strongest metC candidate based on genomic context (adjacent to metB/PP_0659), consistent with the metBC operon organization seen in other bacteria. Homologues to metC (PP_0658) and metB (PP_0659) were explicitly identified in the *P. putida* genome and noted to provide the capacity for homocysteine-to-cysteine conversion (molina‐henares2010identificationofconditionally pages 9-11). Importantly, PP_0658 is not present in the candidate list as a standalone entry; the candidate list instead includes PP_4348 as the cystathionine β-lyase.

**PP_4348 — Cystathionine β-lyase (annotated).** This gene is annotated as cystathionine β-lyase in the candidate list. However, given that PP_0658 is the genomic-context-supported metC (adjacent to metB), PP_4348 likely represents either a paralog with partially overlapping specificity or an over-propagated annotation. No direct experimental evidence was found supporting PP_4348 as the primary trans-sulfuration β-lyase in KT2440. Status: **candidate_uncertain** pending deeper sequence analysis.

**PP_2528 — O-acetylhomoserine (thiol)-lyase (metY-like).** Santos et al. (2004) noted that KT2440 contains an ortholog of metY from *Corynebacterium glutamicum* at PP_2528, which catalyzes direct sulfhydrylation of O-acetylhomoserine (santos2004insightsintothe pages 5-7). Since KT2440 primarily uses O-succinylhomoserine (via MetZ) rather than O-acetylhomoserine, the biological significance of PP_2528 in *P. putida* is unclear. It may represent a latent or backup activity. Status: **candidate_uncertain**.

**PP_4594 — Cystathionine γ-synthase (paralog).** A second annotated cystathionine γ-synthase. Since PP_0659 is the primary metB assignment, PP_4594 is likely a paralog or broad-EC propagation. No literature specifically validates this gene in the methionine pathway. Status: **candidate_uncertain**.

**PP_4637 — Methyltransferase family protein.** Annotated as "5-methyltetrahydropteroyltriglutamate–homocysteine S-methyltransferase family protein." Since MetE (PP_2698) and MetH (PP_2375) are both well-supported, PP_4637 may be a divergent family member with a different substrate. Status: **candidate_uncertain**.

### 4.3 Full candidate gene triage

The complete assessment of all 46 candidate genes against the scoped module is provided below:

| Gene Name | Locus Tag | UniProt | Annotated Function | Relevance to Met-from-Hse Module | Confidence Level | Curation Notes |
|---|---|---|---|---|---|---|
| PP_0228 | PP_0228 | Q88RA5 | serine O-acetyltransferase | Not relevant | None | Cysteine/serine metabolism, not homoserine activation for methionine (local metadata). |
| gshA | PP_0243 | Q88R90 | glutamate--cysteine ligase | Not relevant | None | Glutathione biosynthesis, outside methionine-from-homoserine module (local metadata). |
| tdcG-I | PP_0297 | Q88R37 | L-serine dehydratase | Not relevant | None | Serine catabolism; no direct role in methionine biosynthesis from homoserine (local metadata). |
| yfiH | PP_0624 | Q88Q72 | purine nucleoside phosphorylase | Not relevant | None | Annotation appears broad/KEGG-bucket driven; no evidence for module role. |
| mdh | PP_0654 | Q88Q44 | probable malate dehydrogenase | Not relevant | None | TCA/central metabolism gene; not part of methionine pathway. |
| metB | PP_0659 | Q88Q39 | cystathionine gamma-synthase | Trans-sulfuration sulfur-incorporation route | High | Expected step-2 trans-sulfuration enzyme; pathway present in KT2440 but likely secondary to direct sulfhydrylation (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 2-3, molina‐henares2010identificationofconditionally pages 9-11). |
| PP_0664 | PP_0664 | Q88Q34 | homoserine dehydrogenase | Neighboring upstream pathway | Low | Upstream supply of homoserine from aspartate semialdehyde; not part of the scoped module itself (molina‐henares2010identificationofconditionally pages 7-9). |
| cysE | PP_0840 | Q88PL0 | serine O-acetyltransferase | Not relevant | None | Cysteine biosynthesis, not methionine-from-homoserine module. |
| tdcG-II | PP_0987 | Q88P66 | L-serine dehydratase | Not relevant | None | Serine catabolism; no direct pathway role. |
| PP_1110 | PP_1110 | Q88NU4 | serine O-acetyltransferase | Not relevant | None | Serine/cysteine pathway paralog, outside scoped module. |
| mdeA | PP_1308 | Q88NA4 | L-methionine gamma-lyase | Neighboring/catabolic | Low | Methionine degradation/utilization, not de novo methionine synthesis; relevant to sulfur salvage/catabolism (vermeij1999pathwaysofassimilative pages 3-5). |
| hom | PP_1470 | Q88MU8 | homoserine dehydrogenase | Neighboring upstream pathway | Low | Produces homoserine precursor; belongs upstream of module boundary (molina‐henares2010identificationofconditionally pages 7-9). |
| PP_1541 | PP_1541 | Q88MN0 | methyltransferase | Not relevant | None | Generic methyltransferase annotation; no evidence for homocysteine methylation role. |
| cysM | PP_1654 | Q88MC0 | cysteine synthase | Not relevant | None | Cysteine synthase for sulfur assimilation, outside methionine-from-homoserine module (molina‐henares2010identificationofconditionally pages 9-11). |
| mtnA | PP_1766 | Q88M09 | methylthioribose-1-phosphate isomerase | Neighboring/catabolic | Low | Methionine salvage pathway, not de novo biosynthesis from homoserine (local metadata). |
| serC | PP_1768 | Q88M07 | phosphoserine aminotransferase | Not relevant | None | Serine biosynthesis; no direct role in module. |
| PP_1832 | PP_1832 | Q88LU5 | oxidase | Not relevant | None | Uninformative oxidase annotation; no evidence for module role. |
| msrC | PP_1877 | Q88LQ2 | methionine-(R)-sulfoxide reductase | Neighboring/catabolic | Low | Methionine repair/redox maintenance, not biosynthesis from homoserine. |
| tyrB | PP_1972 | Q88LG1 | aminotransferase | Not relevant | None | Broad aminotransferase annotation; no specific module evidence. |
| asd__Q88LE4 | PP_1989 | Q88LE4 | aspartate-semialdehyde dehydrogenase | Neighboring upstream pathway | Low | Supplies aspartate semialdehyde for homoserine branch; upstream, not inside scoped module (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 9-11). |
| metZ | PP_2001 | Q88LD4 | O-succinylhomoserine sulfhydrylase | Direct sulfhydrylation sulfur-incorporation route | High | Strongly supported primary sulfur-incorporation route in P. putida KT2440/pseudomonads; step 2 direct sulfhydrylation (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 2-3, molina‐henares2010identificationofconditionally pages 9-11). |
| metH | PP_2375 | Q88KB5 | methionine synthase (B12-dependent) | Homocysteine methylation | High | One of two confirmed terminal methylation enzymes in KT2440; provides B12-dependent route (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11). |
| PP_2528 | PP_2528 | Q88JW9 | O-acetylhomoserine (thiol)-lyase | Alternative sulfur-incorporation candidate | Medium | Reported as metY-like ortholog in KT2440; plausible alternative direct sulfhydrylation enzyme but lacking direct functional validation in strain (santos2004insightsintothe pages 5-7). |
| PP_2533 | PP_2533 | Q88JW4 | D-isomer specific 2-hydroxyacid dehydrogenase family protein | Not relevant | None | No clear connection to methionine module. |
| metE | PP_2698 | Q88JF1 | 5-methyltetrahydropteroyltriglutamate--homocysteine methyltransferase | Homocysteine methylation | High | Confirmed B12-independent methionine synthase; terminal step alternative to MetH (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11, leyn2014comparativegenomicsof pages 9-10). |
| PP_2930 | PP_2930 | Q88IR9 | L-serine ammonia-lyase | Not relevant | None | Serine catabolism; no direct role in module. |
| PP_3029 | PP_3029 | Q88IH0 | DNA (cytosine-5)-methyltransferase | Not relevant | None | DNA methylation enzyme; unrelated to methionine synthase step. |
| PP_3136 | PP_3136 | Q88I65 | serine acetyltransferase | Not relevant | None | Serine/cysteine metabolism, not methionine biosynthesis. |
| tdcG-III | PP_3144 | Q88I57 | L-serine dehydratase | Not relevant | None | Serine catabolism; no module role. |
| PP_3254 | PP_3254 | Q88HU9 | nucleosidase | Not relevant | None | No direct role in methionine-from-homoserine pathway. |
| ilvE | PP_3511 | Q88H54 | branched-chain amino-acid aminotransferase | Not relevant | None | Branched-chain amino acid synthesis; outside module. |
| amaC | PP_3590 | Q88GX7 | aminotransferase | Not relevant | None | Broad aminotransferase annotation without methionine-pathway evidence. |
| alr | PP_3722 | Q88GJ9 | broad-specificity amino-acid racemase | Not relevant | None | Racemase; no direct role in module. |
| PP_3912 | PP_3912 | Q88G14 | DNA (cytosine-5)-methyltransferase | Not relevant | None | DNA methylation, not homocysteine methylation. |
| PP_3989 | PP_3989 | Q88FU3 | DNA (cytosine-5)-methyltransferase | Not relevant | None | DNA methylation, not module-related. |
| PP_4348 | PP_4348 | Q88EV4 | cystathionine beta-lyase | Trans-sulfuration sulfur-incorporation candidate | Medium | Plausible metC-like activity, but PP_0658 is the stronger canonical metBC-cluster candidate; PP_4348 may be paralog/over-annotation until reviewed (vermeij1999pathwaysofassimilative pages 2-3). |
| PP_4473 | PP_4473 | Q88EI9 | aspartate kinase | Neighboring upstream pathway | Low | Upstream aspartate-family biosynthesis, outside module boundary. |
| cysK | PP_4571 | Q88E95 | cysteine synthase | Not relevant | None | Cysteine synthase paralog; sulfur assimilation/cysteine pathway, not methionine module (molina‐henares2010identificationofconditionally pages 9-11). |
| PP_4594 | PP_4594 | Q88E72 | cystathionine gamma-synthase | Trans-sulfuration candidate/paralog | Medium | Could represent paralogous MetB-like activity, but PP_0659 is the strongest expected metB assignment; needs deeper sequence/neighborhood review. |
| PP_4637 | PP_4637 | Q88E31 | 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase family protein | Homocysteine methylation candidate/paralog | Medium | Family-level annotation suggests methionine synthase-like role, but metE and metH already cover step 3; likely paralog/divergent family member needing manual review. |
| rhdA | PP_4907 | Q88DC0 | sulfurtransferase | Not relevant | None | General sulfur metabolism; not specific to methionine-from-homoserine module. |
| metK | PP_4967 | Q88D60 | S-adenosylmethionine synthase | Neighboring downstream pathway | Low | Downstream SAM cycle after methionine formation; should be kept outside this module boundary. |
| ahcY | PP_4976 | A0A140FWS3 | adenosylhomocysteinase | Neighboring downstream pathway | Low | SAM/SAH cycle metabolism downstream of methionine, not de novo formation from homoserine. |
| metXS | PP_5097 | Q88CT3 | homoserine O-succinyltransferase | Homoserine activation/acylation | High | Strongly supported step-1 enzyme; metX mutant is methionine auxotroph in KT2440. Literature often describes metXW operon with PP_5098 as accessory subunit (molina‐henares2010identificationofconditionally pages 7-9, santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 9-11). |
| sseA | PP_5118 | Q88CR2 | 3-mercaptopyruvate sulfurtransferase | Not relevant | None | Sulfur transfer enzyme, not part of methionine biosynthesis from homoserine. |
| serA | PP_5155 | Q88CM5 | D-3-phosphoglycerate dehydrogenase | Not relevant | None | Serine biosynthesis; outside module. |


*Table: This table triages all 46 local candidate genes against the scoped L-methionine-from-homoserine module in Pseudomonas putida KT2440. It separates high-confidence pathway genes from upstream precursors, downstream SAM-cycle genes, catabolic/salvage genes, and likely KEGG over-propagations to support manual curation.*

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### No genuine gaps

The module is fully satisfiable: every step has at least one high-confidence gene assignment. The biologically preferred route (metXW → metZ → metE/metH) is well-supported by direct KT2440 evidence.

### Key ambiguities

1. **PP_0658 (metC) is missing from the candidate list.** The candidate list includes PP_4348 as a cystathionine β-lyase but omits PP_0658, which is the genomically adjacent metC partner of metB (PP_0659). This is a curation gap: PP_0658 should be added to the candidate set for the trans-sulfuration route (molina‐henares2010identificationofconditionally pages 9-11).

2. **PP_4348 vs. PP_0658 as metC.** Without detailed sequence comparison, it remains uncertain whether PP_4348 has equivalent β-lyase activity. It could be a paralog with different substrate preference or a genuine metC duplicate. Status: needs manual review.

3. **PP_2528 (metY-like) biological role.** The substrate specificity of PP_2528 (O-acetylhomoserine thiol-lyase) is mismatched with the primary pathway substrate (O-succinylhomoserine) in KT2440. Its function may be peripheral or conditional (santos2004insightsintothe pages 5-7).

### Likely over-annotations in the candidate list

The KEGG ppu00270 bucket is too broad for this module. The following categories of genes in the candidate list are clearly outside the module scope:
- **DNA (cytosine-5)-methyltransferases** (PP_3029, PP_3912, PP_3989): These are DNA modification enzymes, not methionine pathway methyltransferases. Their inclusion is an artifact of sharing the same KEGG map.
- **Serine O-acetyltransferases** (PP_0228, PP_0840/cysE, PP_1110, PP_3136): These belong to cysteine biosynthesis (O-acetylserine formation), not homoserine acylation.
- **L-serine dehydratases** (PP_0297, PP_0987, PP_3144): Serine catabolism, not methionine biosynthesis.
- **Purine nucleoside phosphorylase** (PP_0624/yfiH), **nucleosidase** (PP_3254): Likely part of the methionine salvage pathway or generic nucleotide metabolism, not de novo methionine from homoserine.

## 6. Module and GO-Curation Recommendations

### Module satisfiability summary

| Module Step | Route | Status | Assigned Gene(s) | Justification |
|---|---|---|---|---|
| 1. Acylation of homoserine | O-succinyltransferase (metXW-type activation) | covered | metXW / PP_5097-PP_5098 | KT2440 uses the metXW system for the first activation step; a metX mutant is methionine auxotrophic, supporting this assignment directly in the target strain (molina‐henares2010identificationofconditionally pages 7-9, santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 9-11) |
| 1. Acylation of homoserine | O-acetyltransferase (metA-type alternative) | not_expected_in_target_taxon | none assigned | The generic alternative should remain in the module, but current KT2440 evidence supports metXW-mediated acylation rather than a canonical metA route (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11) |
| 2. Sulfur incorporation to homocysteine | Direct sulfhydrylation (metY/metZ-type) | covered | metZ / PP_2001 | Direct sulfhydrylation is the preferred methionine-biosynthetic route in Pseudomonas; KT2440 specifically encodes metZ for this step, and related P. putida physiology strongly supports this as the primary route (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 2-3, molina‐henares2010identificationofconditionally pages 9-11) |
| 2. Sulfur incorporation to homocysteine | Trans-sulfuration (metB + metC) | covered | metB / PP_0659 + metC-like / PP_0658 | KT2440 contains the expected metBC-like pair, but evidence indicates this route is secondary/weakly used under most conditions compared with direct sulfhydrylation (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 1-2, vermeij1999pathwaysofassimilative pages 2-3, molina‐henares2010identificationofconditionally pages 9-11) |
| 3. Homocysteine methylation | Cobalamin-independent methionine synthase | covered | metE / PP_2698 | KT2440 encodes a validated MetE-type terminal methylation enzyme, providing a B12-independent route to methionine (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11, leyn2014comparativegenomicsof pages 9-10) |
| 3. Homocysteine methylation | Cobalamin-dependent methionine synthase | covered | metH / PP_2375 | KT2440 also encodes MetH, giving a B12-dependent alternative for the final methylation step (santos2004insightsintothe pages 5-7, molina‐henares2010identificationofconditionally pages 9-11, leyn2014comparativegenomicsof pages 9-10) |
| Overall module outcome | L-methionine biosynthesis from homoserine | covered | metXW; metZ and/or metBC; metE and/or metH | Fully satisfiable in KT2440 because each of the three required steps has at least one covered route; the biologically preferred path is metXW → metZ → metE/metH (santos2004insightsintothe pages 5-7, vermeij1999pathwaysofassimilative pages 2-3, molina‐henares2010identificationofconditionally pages 9-11) |


*Table: This table summarizes stepwise satisfiability of the homoserine-to-methionine module in Pseudomonas putida KT2440. It highlights which route alternatives are covered in the target organism and which generic alternatives are not expected.*

### Specific recommendations

1. **Module step 1 (acylation)**: The generic module correctly provides metA and metX as alternatives. For *P. putida* KT2440, the module should note that metXW is a two-component system (not a single polypeptide), and metA is not expected. The metXW operon at PP_5097–PP_5098 satisfies this step.

2. **Module step 2 (sulfur incorporation)**: The module correctly offers trans-sulfuration (metB + metC) and direct sulfhydrylation (metY/metZ) as alternatives. For KT2440, the direct sulfhydrylation route via MetZ (PP_2001) is the primary satisfying assignment. The trans-sulfuration route via MetB (PP_0659) + MetC (PP_0658) is present but secondary. The module template's use of "metY" as the direct sulfhydrylation gene name is potentially confusing because in *P. putida* the direct sulfhydrylase is called metZ (acting on O-succinylhomoserine) rather than metY (which acts on O-acetylhomoserine) (vermeij1999pathwaysofassimilative pages 2-3). **Recommendation**: The module should distinguish metZ (O-succinylhomoserine sulfhydrylase) from metY (O-acetylhomoserine sulfhydrylase), as these represent different substrate specificities correlated with step 1 (succinylation vs. acetylation).

3. **Module step 3 (methylation)**: Both alternatives (metE/metH) are covered. No revision needed.

4. **GO term considerations**: The GO annotation for PP_5097 should explicitly capture EC 2.3.1.46 (homoserine O-succinyltransferase) and include a note about the two-component MetXW system. PP_2001 should carry the O-succinylhomoserine sulfhydrylase activity term (currently annotated with EC 2.5.1.-; a more specific EC assignment would improve curation).

5. **Boundary recommendation**: The module boundary should exclude upstream homoserine supply (hom, asd, aspartate kinase) and downstream SAM cycling (metK, ahcY), consistent with the "from homoserine" scope designation.

## 7. Genes to Promote to Full Review

The following genes merit full `fetch-gene` review based on this analysis:

1. **PP_0658 (metC)**: Not in the current candidate list but is the genomically supported cystathionine β-lyase adjacent to metB (PP_0659). Should be added and reviewed for the trans-sulfuration route.

2. **PP_5098 (metW)**: The accessory subunit of the MetXW system. Not in the candidate list but directly relevant—MetW regulates MetX enzymatic activity. Hasebe (2021, doi:10.1093/bbb/zbaa044) demonstrated that MetW regulates MetX activity in *Pseudomonas*, warranting detailed review.

3. **PP_4348**: Currently annotated as cystathionine β-lyase. Needs sequence and neighborhood analysis to determine whether this is a genuine metC paralog or annotation over-propagation.

4. **PP_2528**: Annotated as O-acetylhomoserine (thiol)-lyase (metY-like). Needs assessment of substrate specificity and biological role given that KT2440 primarily uses O-succinylhomoserine.

5. **PP_4594**: Second cystathionine γ-synthase annotation. Needs comparison with PP_0659 to determine paralog status.

6. **PP_4637**: Methyltransferase family protein with metE-like annotation. Needs comparison with PP_2698 to determine if this is a functional methionine synthase or a divergent family member.

## 8. Key References

The following references provide the primary evidence base for this review:

- **Alaminos & Ramos (2001)**, Arch. Microbiol. 176:151–154 (doi:10.1007/s002030100293): The foundational study demonstrating that methionine biosynthesis from homoserine in *P. putida* involves the metW, metX, metZ, metH, and metE gene products. Referenced extensively throughout the literature but not directly obtainable for this review (leyn2014comparativegenomicsof pages 11-11).

- **dos Santos et al. (2004)**, Environ. Microbiol. 6:1264–1286 (doi:10.1111/j.1462-2920.2004.00734.x): Genomic analysis identifying metXW (PP_5097–PP_5098), metBC (PP_0659/PP_0658), metZ (PP_2001), metY-like (PP_2528), metH (PP_2375), and metE (PP_2698) in KT2440, and describing the combined pathway configuration (santos2004insightsintothe pages 5-7).

- **Molina-Henares et al. (2010)**, Environ. Microbiol. 12:1468–1485 (doi:10.1111/j.1462-2920.2010.02166.x): Genome-wide transposon mutant screen confirming metX as conditionally essential for growth on minimal medium (methionine auxotroph), with detailed description of the three-step pathway (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 9-11).

- **Vermeij & Kertesz (1999)**, J. Bacteriol. 181:5833–5837 (doi:10.1128/jb.181.18.5833-5837.1999): Biochemical characterization of sulfur metabolism in *P. putida* S-313 demonstrating that direct sulfhydrylation is strongly preferred over trans-sulfuration, with low cystathionine β-lyase and γ-synthase activities under most conditions (vermeij1999pathwaysofassimilative pages 1-2, vermeij1999pathwaysofassimilative pages 2-3, vermeij1999pathwaysofassimilative pages 5-5, vermeij1999pathwaysofassimilative pages 3-5).

- **Leyn et al. (2014)**, PLoS ONE 9:e113714 (doi:10.1371/journal.pone.0113714): Comparative genomics of methionine metabolism regulation in Proteobacteria, identifying MetR-regulated genes including metE and metH, and regulatory patterns across γ-proteobacteria including Pseudomonadaceae (leyn2014comparativegenomicsof pages 11-11, leyn2014comparativegenomicsof pages 5-8, leyn2014comparativegenomicsof pages 1-2, leyn2014comparativegenomicsof pages 8-9, leyn2014comparativegenomicsof pages 9-10).

- **Domínguez-Cuevas et al. (2006)**, J. Biol. Chem. 281:11981–11991 (doi:10.1074/jbc.m509848200): Transcriptomic study showing strong induction of every methionine biosynthesis gene in KT2440 upon toluene exposure, linking methionine metabolism to stress response (dominguezcuevas2006transcriptionaltradeoffbetween pages 8-9, dominguezcuevas2006transcriptionaltradeoffbetween pages 3-4).

- **Schmidt et al. (2022)**, Appl. Environ. Microbiol. 88:e02430-21 (doi:10.1128/aem.02430-21): RB-TnSeq functional genomics including amino acid dropout conditions for methionine in KT2440, supporting gene essentiality assignments (schmidt2022nitrogenmetabolismin pages 2-4).

- **Hasebe (2021)**, Biosci. Biotechnol. Biochem. 85:351–358 (doi:10.1093/bbb/zbaa044): Demonstration that MetW regulates MetX enzymatic activity in *Pseudomonas* (unobtainable but cited in search results).

- **Nogales et al. (2020)**, Environ. Microbiol. 22:255–269 (doi:10.1111/1462-2920.14843): The iJN1462 genome-scale metabolic model of KT2440 with gene essentiality predictions validated against knock-out libraries.

- **Belda et al. (2016)**, Environ. Microbiol. 18:3403–3424 (doi:10.1111/1462-2920.13230): Revisited genome annotation of KT2440 with 1548 re-annotated gene functions.

### Evidence strength summary

Direct *P. putida* KT2440 evidence exists for: metXW essentiality (transposon mutant auxotrophy), pathway gene identity (genomic analysis), and stress-responsive expression (transcriptomics). The preference for direct sulfhydrylation over trans-sulfuration is demonstrated biochemically in the closely related *P. putida* S-313 strain; transfer to KT2440 is considered **strong** given species identity and consistent genomic architecture. Transcriptional regulation via MetR is inferred from comparative genomics across γ-proteobacteria (evidence transfer: **moderate**). The role of PP_2528 (metY-like) is inferred from homology to *C. glutamicum* metY only (evidence transfer: **weak/uncertain**).

References

1. (santos2004insightsintothe pages 5-7): V. A. P. Martins Dos Santos, S. Heim, E. R. B. Moore, M. Strätz, and K. N. Timmis. Insights into the genomic basis of niche specificity of pseudomonas putida kt2440. Environmental microbiology, 6 12:1264-86, Dec 2004. URL: https://doi.org/10.1111/j.1462-2920.2004.00734.x, doi:10.1111/j.1462-2920.2004.00734.x. This article has 343 citations and is from a domain leading peer-reviewed journal.

2. (molina‐henares2010identificationofconditionally pages 9-11): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

3. (vermeij1999pathwaysofassimilative pages 1-2): Paul Vermeij and Michael A. Kertesz. Pathways of assimilative sulfur metabolism inpseudomonas putida. Journal of Bacteriology, 181:5833-5837, Sep 1999. URL: https://doi.org/10.1128/jb.181.18.5833-5837.1999, doi:10.1128/jb.181.18.5833-5837.1999. This article has 122 citations and is from a peer-reviewed journal.

4. (vermeij1999pathwaysofassimilative pages 2-3): Paul Vermeij and Michael A. Kertesz. Pathways of assimilative sulfur metabolism inpseudomonas putida. Journal of Bacteriology, 181:5833-5837, Sep 1999. URL: https://doi.org/10.1128/jb.181.18.5833-5837.1999, doi:10.1128/jb.181.18.5833-5837.1999. This article has 122 citations and is from a peer-reviewed journal.

5. (molina‐henares2010identificationofconditionally pages 7-9): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

6. (vermeij1999pathwaysofassimilative pages 3-5): Paul Vermeij and Michael A. Kertesz. Pathways of assimilative sulfur metabolism inpseudomonas putida. Journal of Bacteriology, 181:5833-5837, Sep 1999. URL: https://doi.org/10.1128/jb.181.18.5833-5837.1999, doi:10.1128/jb.181.18.5833-5837.1999. This article has 122 citations and is from a peer-reviewed journal.

7. (molina‐henares2010identificationofconditionally pages 6-7): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

8. (leyn2014comparativegenomicsof pages 9-10): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

9. (vermeij1999pathwaysofassimilative pages 5-5): Paul Vermeij and Michael A. Kertesz. Pathways of assimilative sulfur metabolism inpseudomonas putida. Journal of Bacteriology, 181:5833-5837, Sep 1999. URL: https://doi.org/10.1128/jb.181.18.5833-5837.1999, doi:10.1128/jb.181.18.5833-5837.1999. This article has 122 citations and is from a peer-reviewed journal.

10. (leyn2014comparativegenomicsof pages 11-11): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

11. (leyn2014comparativegenomicsof pages 5-8): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

12. (leyn2014comparativegenomicsof pages 1-2): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

13. (leyn2014comparativegenomicsof pages 8-9): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

14. (dominguezcuevas2006transcriptionaltradeoffbetween pages 8-9): Patricia Domínguez-Cuevas, José-Eduardo González-Pastor, Silvia Marqués, Juan-Luis Ramos, and Víctor de Lorenzo. Transcriptional tradeoff between metabolic and stress-response programs in pseudomonas putida kt2440 cells exposed to toluene*. Journal of Biological Chemistry, 281:11981-11991, Apr 2006. URL: https://doi.org/10.1074/jbc.m509848200, doi:10.1074/jbc.m509848200. This article has 269 citations and is from a domain leading peer-reviewed journal.

15. (dominguezcuevas2006transcriptionaltradeoffbetween pages 3-4): Patricia Domínguez-Cuevas, José-Eduardo González-Pastor, Silvia Marqués, Juan-Luis Ramos, and Víctor de Lorenzo. Transcriptional tradeoff between metabolic and stress-response programs in pseudomonas putida kt2440 cells exposed to toluene*. Journal of Biological Chemistry, 281:11981-11991, Apr 2006. URL: https://doi.org/10.1074/jbc.m509848200, doi:10.1074/jbc.m509848200. This article has 269 citations and is from a domain leading peer-reviewed journal.

16. (schmidt2022nitrogenmetabolismin pages 2-4): Matthias Schmidt, Allison N. Pearson, Matthew R. Incha, Mitchell G. Thompson, Edward E. K. Baidoo, Ramu Kakumanu, Aindrila Mukhopadhyay, Patrick M. Shih, Adam M. Deutschbauer, Lars M. Blank, and Jay D. Keasling. Nitrogen metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Applied and Environmental Microbiology, Apr 2022. URL: https://doi.org/10.1128/aem.02430-21, doi:10.1128/aem.02430-21. This article has 36 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__methionine_biosynthesis__ppu00270-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__methionine_biosynthesis__ppu00270-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PSEPK__methionine_biosynthesis__ppu00270-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. vermeij1999pathwaysofassimilative pages 3-5
2. santos2004insightsintothe pages 5-7
3. leyn2014comparativegenomicsof pages 9-10
4. vermeij1999pathwaysofassimilative pages 2-3
5. leyn2014comparativegenomicsof pages 11-11
6. schmidt2022nitrogenmetabolismin pages 2-4
7. vermeij1999pathwaysofassimilative pages 1-2
8. vermeij1999pathwaysofassimilative pages 5-5
9. leyn2014comparativegenomicsof pages 5-8
10. leyn2014comparativegenomicsof pages 1-2
11. leyn2014comparativegenomicsof pages 8-9
12. dominguezcuevas2006transcriptionaltradeoffbetween pages 8-9
13. dominguezcuevas2006transcriptionaltradeoffbetween pages 3-4
14. https://doi.org/10.1111/j.1462-2920.2004.00734.x,
15. https://doi.org/10.1111/j.1462-2920.2010.02166.x,
16. https://doi.org/10.1128/jb.181.18.5833-5837.1999,
17. https://doi.org/10.1371/journal.pone.0113714,
18. https://doi.org/10.1074/jbc.m509848200,
19. https://doi.org/10.1128/aem.02430-21,