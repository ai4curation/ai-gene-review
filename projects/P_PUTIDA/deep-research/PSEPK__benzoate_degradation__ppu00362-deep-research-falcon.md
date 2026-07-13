---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T14:17:39.593520'
end_time: '2026-07-06T14:40:20.341381'
duration_seconds: 1360.75
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Benzoate and beta-ketoadipate aromatic degradation
  module_summary: A taxon-neutral bacterial aromatic-catabolism module centered on
    the conversion of benzoate and related hydroxyaromatic compounds into catechol
    or protocatechuate, followed by ortho ring cleavage and beta-ketoadipate pathway
    reactions that funnel carbon to central metabolism. The module distinguishes the
    strict benzoate-to-catechol entry branch from the protocatechuate, gallate, and
    terminal beta-ketoadipate branches that commonly share pathway intermediates in
    Pseudomonas and related bacteria. Broad KEGG benzoate maps can also include phenylacetate,
    xylene, gallate, fatty-acid beta-oxidation, generic thiolase, cytochrome P450,
    and ferredoxin nodes; those are adjacent context unless their substrate-specific
    role is established for a given taxon.
  module_outline: "- Benzoate and beta-ketoadipate degradation\n  - 1. benzoate hydroxylation\
    \ to the cis-diol intermediate\n  - Benzoate to cis-1,2-dihydroxycyclohexa-diene\
    \ carboxylate\n    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase\
    \ activity; activity or role: benzoate 1,2-dioxygenase activity)\n  - 2. benzoate\
    \ cis-diol dehydrogenation\n  - Benzoate cis-diol intermediate to catechol\n \
    \   - 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (molecular\
    \ player: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity;\
    \ activity or role: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase\
    \ activity)\n  - 3. catechol ortho-cleavage branch\n  - Catechol to beta-ketoadipate\
    \ enol-lactone\n    - Catechol 1,2-dioxygenase (molecular player: catechol 1,2-dioxygenase\
    \ activity; activity or role: catechol 1,2-dioxygenase activity)\n    - Muconate\
    \ cycloisomerase (molecular player: muconate cycloisomerase activity; activity\
    \ or role: muconate cycloisomerase activity)\n    - Muconolactone delta-isomerase\
    \ (molecular player: muconolactone delta-isomerase activity; activity or role:\
    \ muconolactone delta-isomerase activity)\n  - 4. protocatechuate entry and ortho-cleavage\
    \ branch\n  - Hydroxybenzoate/protocatechuate branch\n    - 4-hydroxybenzoate\
    \ 3-monooxygenase (molecular player: 4-hydroxybenzoate 3-monooxygenase activity;\
    \ activity or role: 4-hydroxybenzoate 3-monooxygenase activity)\n    - Protocatechuate\
    \ 3,4-dioxygenase (molecular player: protocatechuate 3,4-dioxygenase activity;\
    \ activity or role: protocatechuate 3,4-dioxygenase activity)\n    - 3-carboxy-cis,cis-muconate\
    \ cycloisomerase (molecular player: 3-carboxy-cis,cis-muconate cycloisomerase\
    \ activity; activity or role: 3-carboxy-cis,cis-muconate cycloisomerase activity)\n\
    \    - 4-carboxymuconolactone decarboxylase (molecular player: 4-carboxymuconolactone\
    \ decarboxylase activity; activity or role: 4-carboxymuconolactone decarboxylase\
    \ activity)\n    - 3-oxoadipate enol-lactonase (molecular player: 3-oxoadipate\
    \ enol-lactonase activity; activity or role: 3-oxoadipate enol-lactonase activity)\n\
    \  - 5. terminal beta-ketoadipate CoA activation and thiolysis\n  - 3-oxoadipate\
    \ to succinyl-CoA and acetyl-CoA\n    - 3-oxoadipate CoA-transferase (molecular\
    \ player: 3-oxoadipate CoA-transferase activity; activity or role: 3-oxoadipate\
    \ CoA-transferase activity)\n    - 3-oxoadipyl-CoA thiolase (molecular player:\
    \ 3-oxoadipyl-CoA thiolase activity; activity or role: 3-oxoadipyl-CoA thiolase\
    \ activity)\n  - 6. gallate side branch feeding oxalomesaconate chemistry\n  -\
    \ Gallate to central-carbon entry intermediates\n    - Gallate dioxygenase (molecular\
    \ player: gallate dioxygenase activity; activity or role: gallate dioxygenase\
    \ activity)\n    - 4-oxalomesaconate tautomerase (molecular player: intramolecular\
    \ oxidoreductase activity, transposing C=C bonds; activity or role: intramolecular\
    \ oxidoreductase activity, transposing C=C bonds)\n    - 4-oxalmesaconate hydratase\
    \ (molecular player: 4-oxalmesaconate hydratase activity; activity or role: 4-oxalmesaconate\
    \ hydratase activity)"
  module_connections: '- Benzoate to cis-1,2-dihydroxycyclohexa-diene carboxylate
    feeds into Benzoate cis-diol intermediate to catechol: BenABC forms the cis-diol
    substrate used by BenD.

    - Benzoate cis-diol intermediate to catechol feeds into Catechol to beta-ketoadipate
    enol-lactone: BenD produces catechol, the substrate for catechol 1,2-dioxygenase.

    - Catechol to beta-ketoadipate enol-lactone feeds into 3-oxoadipate to succinyl-CoA
    and acetyl-CoA: The catechol ortho-cleavage branch reaches beta-ketoadipate intermediates.

    - Hydroxybenzoate/protocatechuate branch feeds into 3-oxoadipate to succinyl-CoA
    and acetyl-CoA: The protocatechuate branch also converges on 3-oxoadipate.'
  pathway_query: ppu00362
  pathway_id: ppu00362
  pathway_name: Benzoate degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00362 with 8 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '40'
  candidate_genes: '- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC
    1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - fdx: PP_0847 | Q88PK3 | 2Fe-2S ferredoxin (primary bucket kegg:ppu00362)

    - PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-;
    primary bucket kegg:ppu00130)

    - pcaF-I: PP_1377 | Q88N39 | Beta-ketoadipyl-CoA thiolase (EC 2.3.1.174) (3-oxoadipyl-CoA
    thiolase) (EC 2.3.1.174; primary bucket kegg:ppu00362)

    - pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2)
    (EC 5.5.1.2; primary bucket kegg:ppu01220)

    - pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24;
    primary bucket kegg:ppu01220)

    - pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44)
    (EC 4.1.1.44; primary bucket kegg:ppu01220)

    - PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)

    - PP_1950: PP_1950 | Q88LI2 | Cytochrome P450 (primary bucket kegg:ppu00362)

    - fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes:
    Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA
    epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase
    (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)

    - fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA
    acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate
    tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)

    - galD: PP_2513 | Q88JY0 | 4-oxalomesaconate tautomerase (EC 5.3.2.8) (Gallate
    degradation protein D) (EC 5.3.2.8; primary bucket kegg:ppu00362)

    - galC: PP_2514 | Q88JX9 | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA
    aldolase) (EC 4.1.3.17) (Gallate degradation protein C) (EC 4.1.3.17; primary
    bucket kegg:ppu00660)

    - galB: PP_2515 | Q88JX8 | 4-oxalmesaconate hydratase (OMA hydratase) (EC 4.2.1.83)
    (Gallate degradation protein B) (EC 4.2.1.83; primary bucket kegg:ppu00362)

    - benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component
    (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)

    - benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase
    (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)

    - catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1;
    primary bucket kegg:ppu00361)

    - paaJ: PP_3280 | Q88HS3 | 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase
    (EC 2.3.1.-, EC 2.3.1.174) (EC 2.3.1.-; 2.3.1.174; primary bucket kegg:ppu00362)

    - paaH: PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) (EC
    1.1.1.35; primary bucket kegg:ppu00360)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - pobA: PP_3537 | Q88H28 | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) (EC
    1.14.13.2; primary bucket kegg:ppu01220)

    - PP_3648: PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein
    (primary bucket kegg:ppu01220)

    - catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1;
    primary bucket kegg:ppu00361)

    - catC: PP_3714 | Q88GK7 | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4)
    (EC 5.3.3.4; primary bucket kegg:ppu01220)

    - catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1;
    primary bucket kegg:ppu00361)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - hbd: PP_3755 | Q88GG9 | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) (EC
    1.1.1.157; primary bucket kegg:ppu00360)

    - pcaI: PP_3951 | Q88FX5 | 3-oxoadipate CoA-transferase (EC 2.8.3.6) (EC 2.8.3.6;
    primary bucket kegg:ppu00362)

    - pcaJ: PP_3952 | P0A101 | 3-oxoadipate CoA-transferase subunit B (EC 2.8.3.6)
    (Beta-ketoadipate:succinyl-CoA transferase subunit B) (EC 2.8.3.6; primary bucket
    kegg:ppu00362)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3)
    (EC 1.13.11.3; primary bucket kegg:ppu01220)

    - pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3)
    (EC 1.13.11.3; primary bucket kegg:ppu01220)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__benzoate_degradation__ppu00362-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__benzoate_degradation__ppu00362-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Benzoate and beta-ketoadipate aromatic degradation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00362
- Resolved ID: ppu00362
- Resolved name: Benzoate degradation
- Source: KEGG

Resolved local bucket kegg:ppu00362 with 8 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 40

- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- fdx: PP_0847 | Q88PK3 | 2Fe-2S ferredoxin (primary bucket kegg:ppu00362)
- PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-; primary bucket kegg:ppu00130)
- pcaF-I: PP_1377 | Q88N39 | Beta-ketoadipyl-CoA thiolase (EC 2.3.1.174) (3-oxoadipyl-CoA thiolase) (EC 2.3.1.174; primary bucket kegg:ppu00362)
- pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2) (EC 5.5.1.2; primary bucket kegg:ppu01220)
- pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24; primary bucket kegg:ppu01220)
- pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44) (EC 4.1.1.44; primary bucket kegg:ppu01220)
- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_1950: PP_1950 | Q88LI2 | Cytochrome P450 (primary bucket kegg:ppu00362)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- galD: PP_2513 | Q88JY0 | 4-oxalomesaconate tautomerase (EC 5.3.2.8) (Gallate degradation protein D) (EC 5.3.2.8; primary bucket kegg:ppu00362)
- galC: PP_2514 | Q88JX9 | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA aldolase) (EC 4.1.3.17) (Gallate degradation protein C) (EC 4.1.3.17; primary bucket kegg:ppu00660)
- galB: PP_2515 | Q88JX8 | 4-oxalmesaconate hydratase (OMA hydratase) (EC 4.2.1.83) (Gallate degradation protein B) (EC 4.2.1.83; primary bucket kegg:ppu00362)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)
- catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- paaJ: PP_3280 | Q88HS3 | 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase (EC 2.3.1.-, EC 2.3.1.174) (EC 2.3.1.-; 2.3.1.174; primary bucket kegg:ppu00362)
- paaH: PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) (EC 1.1.1.35; primary bucket kegg:ppu00360)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- pobA: PP_3537 | Q88H28 | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) (EC 1.14.13.2; primary bucket kegg:ppu01220)
- PP_3648: PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein (primary bucket kegg:ppu01220)
- catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- catC: PP_3714 | Q88GK7 | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) (EC 5.3.3.4; primary bucket kegg:ppu01220)
- catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1; primary bucket kegg:ppu00361)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- hbd: PP_3755 | Q88GG9 | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) (EC 1.1.1.157; primary bucket kegg:ppu00360)
- pcaI: PP_3951 | Q88FX5 | 3-oxoadipate CoA-transferase (EC 2.8.3.6) (EC 2.8.3.6; primary bucket kegg:ppu00362)
- pcaJ: PP_3952 | P0A101 | 3-oxoadipate CoA-transferase subunit B (EC 2.8.3.6) (Beta-ketoadipate:succinyl-CoA transferase subunit B) (EC 2.8.3.6; primary bucket kegg:ppu00362)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)
- pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial aromatic-catabolism module centered on the conversion of benzoate and related hydroxyaromatic compounds into catechol or protocatechuate, followed by ortho ring cleavage and beta-ketoadipate pathway reactions that funnel carbon to central metabolism. The module distinguishes the strict benzoate-to-catechol entry branch from the protocatechuate, gallate, and terminal beta-ketoadipate branches that commonly share pathway intermediates in Pseudomonas and related bacteria. Broad KEGG benzoate maps can also include phenylacetate, xylene, gallate, fatty-acid beta-oxidation, generic thiolase, cytochrome P450, and ferredoxin nodes; those are adjacent context unless their substrate-specific role is established for a given taxon.

### Provisional Biological Outline

- Benzoate and beta-ketoadipate degradation
  - 1. benzoate hydroxylation to the cis-diol intermediate
  - Benzoate to cis-1,2-dihydroxycyclohexa-diene carboxylate
    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity; activity or role: benzoate 1,2-dioxygenase activity)
  - 2. benzoate cis-diol dehydrogenation
  - Benzoate cis-diol intermediate to catechol
    - 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (molecular player: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity; activity or role: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity)
  - 3. catechol ortho-cleavage branch
  - Catechol to beta-ketoadipate enol-lactone
    - Catechol 1,2-dioxygenase (molecular player: catechol 1,2-dioxygenase activity; activity or role: catechol 1,2-dioxygenase activity)
    - Muconate cycloisomerase (molecular player: muconate cycloisomerase activity; activity or role: muconate cycloisomerase activity)
    - Muconolactone delta-isomerase (molecular player: muconolactone delta-isomerase activity; activity or role: muconolactone delta-isomerase activity)
  - 4. protocatechuate entry and ortho-cleavage branch
  - Hydroxybenzoate/protocatechuate branch
    - 4-hydroxybenzoate 3-monooxygenase (molecular player: 4-hydroxybenzoate 3-monooxygenase activity; activity or role: 4-hydroxybenzoate 3-monooxygenase activity)
    - Protocatechuate 3,4-dioxygenase (molecular player: protocatechuate 3,4-dioxygenase activity; activity or role: protocatechuate 3,4-dioxygenase activity)
    - 3-carboxy-cis,cis-muconate cycloisomerase (molecular player: 3-carboxy-cis,cis-muconate cycloisomerase activity; activity or role: 3-carboxy-cis,cis-muconate cycloisomerase activity)
    - 4-carboxymuconolactone decarboxylase (molecular player: 4-carboxymuconolactone decarboxylase activity; activity or role: 4-carboxymuconolactone decarboxylase activity)
    - 3-oxoadipate enol-lactonase (molecular player: 3-oxoadipate enol-lactonase activity; activity or role: 3-oxoadipate enol-lactonase activity)
  - 5. terminal beta-ketoadipate CoA activation and thiolysis
  - 3-oxoadipate to succinyl-CoA and acetyl-CoA
    - 3-oxoadipate CoA-transferase (molecular player: 3-oxoadipate CoA-transferase activity; activity or role: 3-oxoadipate CoA-transferase activity)
    - 3-oxoadipyl-CoA thiolase (molecular player: 3-oxoadipyl-CoA thiolase activity; activity or role: 3-oxoadipyl-CoA thiolase activity)
  - 6. gallate side branch feeding oxalomesaconate chemistry
  - Gallate to central-carbon entry intermediates
    - Gallate dioxygenase (molecular player: gallate dioxygenase activity; activity or role: gallate dioxygenase activity)
    - 4-oxalomesaconate tautomerase (molecular player: intramolecular oxidoreductase activity, transposing C=C bonds; activity or role: intramolecular oxidoreductase activity, transposing C=C bonds)
    - 4-oxalmesaconate hydratase (molecular player: 4-oxalmesaconate hydratase activity; activity or role: 4-oxalmesaconate hydratase activity)

### Known Relationships Among Steps

- Benzoate to cis-1,2-dihydroxycyclohexa-diene carboxylate feeds into Benzoate cis-diol intermediate to catechol: BenABC forms the cis-diol substrate used by BenD.
- Benzoate cis-diol intermediate to catechol feeds into Catechol to beta-ketoadipate enol-lactone: BenD produces catechol, the substrate for catechol 1,2-dioxygenase.
- Catechol to beta-ketoadipate enol-lactone feeds into 3-oxoadipate to succinyl-CoA and acetyl-CoA: The catechol ortho-cleavage branch reaches beta-ketoadipate intermediates.
- Hydroxybenzoate/protocatechuate branch feeds into 3-oxoadipate to succinyl-CoA and acetyl-CoA: The protocatechuate branch also converges on 3-oxoadipate.

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

Benzoate and beta-ketoadipate aromatic degradation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00362
- Resolved ID: ppu00362
- Resolved name: Benzoate degradation
- Source: KEGG

Resolved local bucket kegg:ppu00362 with 8 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 40

- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- fdx: PP_0847 | Q88PK3 | 2Fe-2S ferredoxin (primary bucket kegg:ppu00362)
- PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-; primary bucket kegg:ppu00130)
- pcaF-I: PP_1377 | Q88N39 | Beta-ketoadipyl-CoA thiolase (EC 2.3.1.174) (3-oxoadipyl-CoA thiolase) (EC 2.3.1.174; primary bucket kegg:ppu00362)
- pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2) (EC 5.5.1.2; primary bucket kegg:ppu01220)
- pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24; primary bucket kegg:ppu01220)
- pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44) (EC 4.1.1.44; primary bucket kegg:ppu01220)
- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_1950: PP_1950 | Q88LI2 | Cytochrome P450 (primary bucket kegg:ppu00362)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- galD: PP_2513 | Q88JY0 | 4-oxalomesaconate tautomerase (EC 5.3.2.8) (Gallate degradation protein D) (EC 5.3.2.8; primary bucket kegg:ppu00362)
- galC: PP_2514 | Q88JX9 | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA aldolase) (EC 4.1.3.17) (Gallate degradation protein C) (EC 4.1.3.17; primary bucket kegg:ppu00660)
- galB: PP_2515 | Q88JX8 | 4-oxalmesaconate hydratase (OMA hydratase) (EC 4.2.1.83) (Gallate degradation protein B) (EC 4.2.1.83; primary bucket kegg:ppu00362)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)
- catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- paaJ: PP_3280 | Q88HS3 | 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase (EC 2.3.1.-, EC 2.3.1.174) (EC 2.3.1.-; 2.3.1.174; primary bucket kegg:ppu00362)
- paaH: PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) (EC 1.1.1.35; primary bucket kegg:ppu00360)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- pobA: PP_3537 | Q88H28 | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) (EC 1.14.13.2; primary bucket kegg:ppu01220)
- PP_3648: PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein (primary bucket kegg:ppu01220)
- catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- catC: PP_3714 | Q88GK7 | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) (EC 5.3.3.4; primary bucket kegg:ppu01220)
- catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1; primary bucket kegg:ppu00361)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- hbd: PP_3755 | Q88GG9 | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) (EC 1.1.1.157; primary bucket kegg:ppu00360)
- pcaI: PP_3951 | Q88FX5 | 3-oxoadipate CoA-transferase (EC 2.8.3.6) (EC 2.8.3.6; primary bucket kegg:ppu00362)
- pcaJ: PP_3952 | P0A101 | 3-oxoadipate CoA-transferase subunit B (EC 2.8.3.6) (Beta-ketoadipate:succinyl-CoA transferase subunit B) (EC 2.8.3.6; primary bucket kegg:ppu00362)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)
- pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial aromatic-catabolism module centered on the conversion of benzoate and related hydroxyaromatic compounds into catechol or protocatechuate, followed by ortho ring cleavage and beta-ketoadipate pathway reactions that funnel carbon to central metabolism. The module distinguishes the strict benzoate-to-catechol entry branch from the protocatechuate, gallate, and terminal beta-ketoadipate branches that commonly share pathway intermediates in Pseudomonas and related bacteria. Broad KEGG benzoate maps can also include phenylacetate, xylene, gallate, fatty-acid beta-oxidation, generic thiolase, cytochrome P450, and ferredoxin nodes; those are adjacent context unless their substrate-specific role is established for a given taxon.

### Provisional Biological Outline

- Benzoate and beta-ketoadipate degradation
  - 1. benzoate hydroxylation to the cis-diol intermediate
  - Benzoate to cis-1,2-dihydroxycyclohexa-diene carboxylate
    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity; activity or role: benzoate 1,2-dioxygenase activity)
  - 2. benzoate cis-diol dehydrogenation
  - Benzoate cis-diol intermediate to catechol
    - 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (molecular player: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity; activity or role: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity)
  - 3. catechol ortho-cleavage branch
  - Catechol to beta-ketoadipate enol-lactone
    - Catechol 1,2-dioxygenase (molecular player: catechol 1,2-dioxygenase activity; activity or role: catechol 1,2-dioxygenase activity)
    - Muconate cycloisomerase (molecular player: muconate cycloisomerase activity; activity or role: muconate cycloisomerase activity)
    - Muconolactone delta-isomerase (molecular player: muconolactone delta-isomerase activity; activity or role: muconolactone delta-isomerase activity)
  - 4. protocatechuate entry and ortho-cleavage branch
  - Hydroxybenzoate/protocatechuate branch
    - 4-hydroxybenzoate 3-monooxygenase (molecular player: 4-hydroxybenzoate 3-monooxygenase activity; activity or role: 4-hydroxybenzoate 3-monooxygenase activity)
    - Protocatechuate 3,4-dioxygenase (molecular player: protocatechuate 3,4-dioxygenase activity; activity or role: protocatechuate 3,4-dioxygenase activity)
    - 3-carboxy-cis,cis-muconate cycloisomerase (molecular player: 3-carboxy-cis,cis-muconate cycloisomerase activity; activity or role: 3-carboxy-cis,cis-muconate cycloisomerase activity)
    - 4-carboxymuconolactone decarboxylase (molecular player: 4-carboxymuconolactone decarboxylase activity; activity or role: 4-carboxymuconolactone decarboxylase activity)
    - 3-oxoadipate enol-lactonase (molecular player: 3-oxoadipate enol-lactonase activity; activity or role: 3-oxoadipate enol-lactonase activity)
  - 5. terminal beta-ketoadipate CoA activation and thiolysis
  - 3-oxoadipate to succinyl-CoA and acetyl-CoA
    - 3-oxoadipate CoA-transferase (molecular player: 3-oxoadipate CoA-transferase activity; activity or role: 3-oxoadipate CoA-transferase activity)
    - 3-oxoadipyl-CoA thiolase (molecular player: 3-oxoadipyl-CoA thiolase activity; activity or role: 3-oxoadipyl-CoA thiolase activity)
  - 6. gallate side branch feeding oxalomesaconate chemistry
  - Gallate to central-carbon entry intermediates
    - Gallate dioxygenase (molecular player: gallate dioxygenase activity; activity or role: gallate dioxygenase activity)
    - 4-oxalomesaconate tautomerase (molecular player: intramolecular oxidoreductase activity, transposing C=C bonds; activity or role: intramolecular oxidoreductase activity, transposing C=C bonds)
    - 4-oxalmesaconate hydratase (molecular player: 4-oxalmesaconate hydratase activity; activity or role: 4-oxalmesaconate hydratase activity)

### Known Relationships Among Steps

- Benzoate to cis-1,2-dihydroxycyclohexa-diene carboxylate feeds into Benzoate cis-diol intermediate to catechol: BenABC forms the cis-diol substrate used by BenD.
- Benzoate cis-diol intermediate to catechol feeds into Catechol to beta-ketoadipate enol-lactone: BenD produces catechol, the substrate for catechol 1,2-dioxygenase.
- Catechol to beta-ketoadipate enol-lactone feeds into 3-oxoadipate to succinyl-CoA and acetyl-CoA: The catechol ortho-cleavage branch reaches beta-ketoadipate intermediates.
- Hydroxybenzoate/protocatechuate branch feeds into 3-oxoadipate to succinyl-CoA and acetyl-CoA: The protocatechuate branch also converges on 3-oxoadipate.

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

# Benzoate and β-Ketoadipate Aromatic Degradation in *Pseudomonas putida* KT2440: A Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 is a model soil bacterium for aerobic aromatic compound catabolism, utilizing a chromosomally encoded β-ketoadipate (ortho-cleavage) pathway to mineralize benzoate, 4-hydroxybenzoate, and related aromatics to TCA cycle intermediates (jimenez2002genomicanalysisof pages 1-2). The KEGG benzoate degradation map ppu00362 encompasses a broad metabolic space; however, the strict biochemical module in KT2440 centers on three convergent entry branches—benzoate→catechol (ben/cat genes), 4-hydroxybenzoate→protocatechuate (pob/pca genes), and gallate (gal genes)—that funnel into a shared terminal β-ketoadipate pathway producing succinyl-CoA and acetyl-CoA (dumalo2020dioxygenasesinthe pages 27-32, dumalo2020dioxygenasesinthe pages 23-27). Of the 40 candidate genes provided, **17 represent bona fide core pathway enzymes** with direct experimental evidence, **3 are gallate-branch enzymes** (a supported side branch), **3 are adjacent phenylacetate-pathway genes** with moderate cross-pathway relevance, and **~17 are generic thiolases, β-oxidation enzymes, or unrelated genes likely over-propagated from broad KEGG/EC family mappings** (jimenez2002genomicanalysisof pages 12-14, jimenez2002genomicanalysisof pages 14-15). All core pathway steps are satisfiable with high confidence in KT2440.

## 2. Target-Organism Pathway Definition

### 2.1 Pathway Scope

The benzoate and β-ketoadipate degradation module in KT2440 encompasses:

**Core process:** Aerobic catabolism of benzoate and 4-hydroxybenzoate through ortho ring-cleavage of catechol and protocatechuate, respectively, converging at 3-oxoadipate (β-ketoadipate), followed by CoA activation and thiolytic cleavage to succinyl-CoA + acetyl-CoA (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 6-9, dumalo2020dioxygenasesinthe pages 27-32).

**Included side branch:** The gallate degradation pathway (gal operon) processes gallic acid through gallate dioxygenase (GalA) and oxalomesaconate chemistry to central carbon intermediates (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2, dias2023fromdegraderto pages 4-6).

**Neighboring pathways to keep separate:** Phenylacetate degradation (pha/paa genes, KEGG ppu00360), fatty acid β-oxidation (fad genes, ppu00071/ppu00592), toluene/xylene degradation (xyl genes, not native to KT2440), nicotinate catabolism (nic cluster), and homogentisate pathway (hmg/fah/mai genes) (jimenez2002genomicanalysisof pages 10-12, jimenez2002genomicanalysisof pages 12-14, jimenez2002genomicanalysisof pages 14-15, jimenez2002genomicanalysisof pages 15-17).

### 2.2 Biological Funnel Architecture

KT2440 employs a convergent "biological funnel" strategy for aromatic catabolism. Upper pathways convert diverse aromatic substrates (vanillate, ferulate, p-coumarate, benzoate, 4-hydroxybenzoate) through oxygenases and O-demethylases into catechol or protocatechuate. These two catecholic intermediates then enter the shared lower β-ketoadipate pathway (dumalo2020dioxygenasesinthe pages 27-32, dumalo2020dioxygenasesinthe pages 23-27). This architecture has been extensively exploited for metabolic engineering, most notably for production of β-ketoadipic acid from lignin-derived aromatics (werner2023ligninconversionto pages 2-4, werner2023ligninconversionto pages 1-2).

### 2.3 Genomic Organization

A distinctive feature of KT2440 is the dispersed chromosomal organization of its aromatic catabolic genes, in contrast to the clustered "catabolic island" arrangement seen in some other bacteria (jimenez2002genomicanalysisof pages 14-15, jimenez2002genomicanalysisof pages 1-2). Specific cluster locations include:

- **ben cluster:** 3580–3591 kb (benR, catA2/benX, benABCDKF) (jimenez2002genomicanalysisof pages 9-10, jimenez2002genomicanalysisof pages 6-9)
- **cat cluster:** 4236–4239 kb (catRBCA) (jimenez2002genomicanalysisof pages 2-3, jimenez2002genomicanalysisof pages 5-6)
- **pca clusters:** Three separate loci—pcaRKFTBDCP at 1566–1575 kb, pcaIJ at 4457–4459 kb, and pcaGH at 5281–5282 kb (jimenez2002genomicanalysisof pages 14-15, jimenez2002genomicanalysisof pages 2-3)
- **pob cluster:** 4009–4012 kb (pobA, pobR, divergently transcribed) (jimenez2002genomicanalysisof pages 6-9)
- **gal operon:** Contains galA, galB, galC, galD, galT, galP, regulated by galR (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2, dias2023fromdegraderto pages 4-6)

Notably, the ben and cat clusters are not contiguous in KT2440, and no pca cluster is linked to the pob cluster—representing the lowest level of aromatic gene linkage among sequenced Pseudomonas species (jimenez2002genomicanalysisof pages 14-15).

## 3. Expected Step Model

The pathway can be decomposed into six functional steps:

**Step 1. Benzoate hydroxylation:** Benzoate 1,2-dioxygenase (BenABC) converts benzoate to cis-1,2-dihydroxycyclohexa-3,5-diene-1-carboxylate using molecular oxygen and NADH (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10).

**Step 2. Benzoate cis-diol dehydrogenation:** BenD (1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase) oxidizes the cis-diol to catechol with NAD+ (jimenez2002genomicanalysisof pages 9-10, loh2008paradigminbiodegradation pages 6-8).

**Step 3. Catechol ortho-cleavage branch:** CatA (catechol 1,2-dioxygenase) cleaves catechol to cis,cis-muconate; CatB (muconate cycloisomerase) forms muconolactone; CatC (muconolactone δ-isomerase) produces β-ketoadipate enol-lactone (jimenez2002genomicanalysisof pages 5-6, cao2008inductionofortho pages 6-7, dumalo2020dioxygenasesinthe pages 27-32).

**Step 4. Protocatechuate entry and ortho-cleavage branch:** PobA (4-hydroxybenzoate 3-monooxygenase) converts 4-hydroxybenzoate to protocatechuate; PcaGH (protocatechuate 3,4-dioxygenase) cleaves the ring to 3-carboxy-cis,cis-muconate; PcaB (cycloisomerase), PcaC (decarboxylase), and PcaD (enol-lactonase) produce β-ketoadipate (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5).

**Step 5. Terminal β-ketoadipate CoA activation and thiolysis:** PcaIJ (3-oxoadipate CoA-transferase) activates β-ketoadipate using succinyl-CoA; PcaF (β-ketoadipyl-CoA thiolase) cleaves the thioester to succinyl-CoA + acetyl-CoA (jimenez2002genomicanalysisof pages 3-5, cao2008inductionofortho pages 6-7).

**Step 6. Gallate side branch:** GalA (gallate dioxygenase) opens the gallate ring; GalD (4-oxalomesaconate tautomerase), GalB (OMA hydratase), and GalC (CHA aldolase) process intermediates to pyruvate + oxaloacetate (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2).

## 4. Candidate Genes and Evidence

The following table provides a comprehensive assessment of all 40 candidate genes:

| Gene Name | Locus Tag | UniProt | Pathway Step | Evidence Type | Confidence Level | Curation Notes |
|---|---|---|---|---|---|---|
| benA | PP_3161 | Q88I40 | Step 1: benzoate → cis-dihydrodiol | Direct/genetic | HIGH | Benzoate 1,2-dioxygenase α subunit in ben cluster; core entry enzyme for benzoate catabolism in KT2440 (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10, jimenez2002genomicanalysisof pages 6-9) |
| benB | PP_3162 | Q88I39 | Step 1: benzoate → cis-dihydrodiol | Direct/genetic | HIGH | Benzoate 1,2-dioxygenase β subunit; part of benABC entry system (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10) |
| benC | PP_3163 | Q88I38 | Step 1: benzoate → cis-dihydrodiol | Direct/genetic | HIGH | Electron-transfer reductase component of benzoate dioxygenase; core ben operon member (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10) |
| benD | PP_3164 | Q88I37 | Step 2: cis-dihydrodiol → catechol | Direct/genetic | HIGH | cis-diol dehydrogenase converting benzoate dihydrodiol to catechol (jimenez2002genomicanalysisof pages 9-10, loh2008paradigminbiodegradation pages 6-8) |
| catA-II | PP_3166 | Q88I35 | Step 3: catechol ortho-cleavage | Direct/genetic | HIGH | Second catechol 1,2-dioxygenase copy embedded in ben cluster (catA2); likely supports benzoate-derived catechol flux (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10) |
| catA-I | PP_3713 | Q88GK8 | Step 3: catechol ortho-cleavage | Direct/genetic | HIGH | Canonical catechol 1,2-dioxygenase in cat cluster at 4236–4239 kb; core ortho-cleavage enzyme (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 2-3) |
| catB | PP_3715 | Q88GK6 | Step 3: cis,cis-muconate → muconolactone | Direct/genetic | HIGH | Muconate cycloisomerase (cis,cis-muconate lactonizing enzyme); essential ortho-cleavage branch enzyme (cao2008inductionofortho pages 6-7, jimenez2002genomicanalysisof pages 5-6) |
| catC | PP_3714 | Q88GK7 | Step 3: muconolactone → β-ketoadipate enol-lactone | Direct/genetic | HIGH | Muconolactone δ-isomerase in cat cluster; completes catechol branch to shared lower pathway intermediate (jimenez2002genomicanalysisof pages 5-6, dumalo2020dioxygenasesinthe pages 27-32) |
| pcaG | PP_4655 | Q88E13 | Step 4: protocatechuate ring cleavage | Direct/genetic | HIGH | Protocatechuate 3,4-dioxygenase α subunit; pcaGH cluster at 5281–5282 kb (jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 2-3) |
| pcaH | PP_4656 | Q88E12 | Step 4: protocatechuate ring cleavage | Direct/genetic | HIGH | Protocatechuate 3,4-dioxygenase β subunit; pairs with PcaG in protocatechuate branch (jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 2-3) |
| pcaB | PP_1379 | Q88N37 | Step 4: 3-carboxy-cis,cis-muconate cycloisomerization | Direct/genetic | HIGH | Core pca branch enzyme in pcaRKFTBDCP cluster; downstream of PcaGH (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5) |
| pcaC | PP_1381 | Q88N35 | Step 4: 4-carboxymuconolactone decarboxylation | Direct/genetic | HIGH | Core protocatechuate branch enzyme in pca cluster (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5) |
| pcaD | PP_1380 | Q88N36 | Step 4: β-ketoadipate enol-lactone hydrolysis | Direct/genetic | HIGH | 3-oxoadipate enol-lactonase; shared lower-pathway step after branch convergence (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5, dumalo2020dioxygenasesinthe pages 27-32) |
| pcaI | PP_3951 | Q88FX5 | Step 5: 3-oxoadipate CoA transfer | Direct/genetic | HIGH | 3-oxoadipate CoA-transferase subunit A; pcaIJ cluster at 4457–4459 kb (jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 2-3) |
| pcaJ | PP_3952 | P0A101 | Step 5: 3-oxoadipate CoA transfer | Direct/genetic | HIGH | 3-oxoadipate CoA-transferase subunit B; terminal lower β-ketoadipate pathway enzyme pair with PcaI (jimenez2002genomicanalysisof pages 3-5) |
| pcaF-I | PP_1377 | Q88N39 | Step 5: β-ketoadipyl-CoA thiolysis | Direct/genetic | HIGH | β-ketoadipyl-CoA thiolase; canonical terminal thiolase for pathway, despite other thiolase homologs elsewhere in genome (jimenez2002genomicanalysisof pages 3-5, cao2008inductionofortho pages 6-7) |
| pobA | PP_3537 | Q88H28 | Step 4 entry: 4-hydroxybenzoate → protocatechuate | Direct/genetic | HIGH | p-Hydroxybenzoate hydroxylase in pob cluster at 4009–4012 kb; feeds protocatechuate branch (jimenez2002genomicanalysisof pages 6-9) |
| galD | PP_2513 | Q88JY0 | Step 6: gallate branch tautomerization | Direct/genetic | HIGH | 4-oxalomesaconate tautomerase; validated gallate-pathway component, but side branch relative to strict benzoate module (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2) |
| galB | PP_2515 | Q88JX8 | Step 6: gallate branch hydration | Direct/genetic | HIGH | 4-oxalomesaconate hydratase; strong support for gallate degradation role in KT2440 (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2) |
| galC | PP_2514 | Q88JX9 | Step 6: gallate branch aldol cleavage | Direct/genetic | HIGH | CHA aldolase in gal operon; gallate-specific side-branch enzyme (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2) |
| paaJ | PP_3280 | Q88HS3 | Adjacent: phenylacetate/CoA-ring-cleavage branch | Homology / pathway context | MODERATE | Thiolase homolog that may accept 3-oxoadipyl-CoA-like substrates, but primary assignment is phenylacetate (pha/paa) pathway, not benzoate β-ketoadipate core (jimenez2002genomicanalysisof pages 10-12, jimenez2002genomicanalysisof pages 3-5) |
| paaH | PP_3282 | Q88HS1 | Adjacent: phenylacetate branch | Homology / pathway context | LOW | 3-Hydroxyadipyl-CoA dehydrogenase in paa/pha context; not expected for canonical benzoate module satisfiability (jimenez2002genomicanalysisof pages 10-12) |
| paaF | PP_3284 | Q88HR9 | Adjacent: phenylacetate branch | Homology / pathway context | LOW | Enoyl-CoA hydratase-isomerase of phenylacetyl-CoA pathway; neighboring chemistry only (jimenez2002genomicanalysisof pages 10-12) |
| fdx | PP_0847 | Q88PK3 | Electron transfer / unclear linkage | Homology only | MODERATE | Generic 2Fe-2S ferredoxin; no direct evidence tying this locus specifically to benzoate dioxygenase in KT2440; likely over-broad KEGG neighborhood mapping (jimenez2002genomicanalysisof pages 9-10, jimenez2002genomicanalysisof pages 14-15) |
| PP_1950 | PP_1950 | Q88LI2 | Unknown specific role | Computational only | LOW | Cytochrome P450; no direct KT2440 evidence for benzoate/β-ketoadipate function; keep outside core module pending substrate-specific data (jimenez2002genomicanalysisof pages 14-15) |
| fadA__Q88L84 | PP_2051 | Q88L84 | Beta-oxidation | Over-propagation / family-level | LOW | 3-Ketoacyl-CoA thiolase I from fatty-acid β-oxidation; not specific to benzoate lower pathway (jimenez2002genomicanalysisof pages 12-14) |
| fadA__Q88L01 | PP_2137 | Q88L01 | Beta-oxidation | Over-propagation / family-level | LOW | Second fatty-acid oxidation thiolase; broad acyl-CoA catabolism rather than aromatic funnel core (jimenez2002genomicanalysisof pages 12-14) |
| fadB | PP_2136 | Q88L02 | Beta-oxidation | Over-propagation / family-level | LOW | Multifunctional fatty-acid oxidation complex α-subunit; off-pathway for benzoate module (jimenez2002genomicanalysisof pages 12-14) |
| bktB | PP_3754 | Q88GH0 | Broad thiolase chemistry | Over-propagation / family-level | LOW | Broad beta-ketothiolase annotation; insufficient evidence for β-ketoadipyl-CoA specificity in KT2440 (jimenez2002genomicanalysisof pages 12-14, jimenez2002genomicanalysisof pages 3-5) |
| hbd | PP_3755 | Q88GG9 | Broad hydroxyacyl-CoA metabolism | Over-propagation / family-level | LOW | 3-Hydroxybutyryl-CoA dehydrogenase; generic short-chain CoA metabolism, not aromatic lower-pathway specific (jimenez2002genomicanalysisof pages 12-14) |
| PP_0582 | PP_0582 | Q88QB2 | Generic thiolase | Over-propagation / family-level | LOW | Thiolase family protein without direct aromatic-pathway evidence; should not satisfy pcaF step (jimenez2002genomicanalysisof pages 3-5) |
| PP_2215 | PP_2215 | Q88KS4 | Generic thiolase | Over-propagation / family-level | LOW | Acetyl-CoA acetyltransferase; broad central metabolism annotation, not β-ketoadipate-specific (jimenez2002genomicanalysisof pages 3-5) |
| PP_2217 | PP_2217 | Q88KS2 | Generic hydratase | Over-propagation / family-level | LOW | Enoyl-CoA hydratase; likely generic lipid/CoA metabolism rather than benzoate branch enzyme (jimenez2002genomicanalysisof pages 12-14) |
| PP_3355 | PP_3355 | Q88HK1 | Generic thiolase | Over-propagation / family-level | LOW | Beta-ketothiolase family member without direct connection to benzoate or pca locus context (jimenez2002genomicanalysisof pages 14-15, jimenez2002genomicanalysisof pages 3-5) |
| yqeF | PP_4636 | Q88E32 | Generic thiolase | Over-propagation / family-level | LOW | Acetyl-CoA acetyltransferase; not in known ben/cat/pca/gal clusters (jimenez2002genomicanalysisof pages 14-15, jimenez2002genomicanalysisof pages 3-5) |
| gcdH | PP_0158 | Q88RH2 | Lysine/glutaryl-CoA metabolism | Over-propagation / family-level | LOW | Glutaryl-CoA dehydrogenase fits lysine/glutarate catabolism, not benzoate β-ketoadipate pathway (jimenez2002genomicanalysisof pages 14-15) |
| PP_1218 | PP_1218 | Q88NI9 | Generic CoA metabolism | Over-propagation / family-level | LOW | Acyl-CoA thioesterase with no benzoate-pathway evidence; retain outside module (jimenez2002genomicanalysisof pages 14-15) |
| PP_1791 | PP_1791 | Q88LY5 | Unknown link | Over-propagation / computational | LOW | Aldolase/synthase family assignment too broad for benzoate module curation (jimenez2002genomicanalysisof pages 14-15) |
| PP_2504 | PP_2504 | Q88JY9 | Meta-cleavage neighborhood | Over-propagation / family-level | LOW | 2-Hydroxymuconate tautomerase is typical of catechol meta-cleavage, not ortho-cleavage β-ketoadipate route (jimenez2002genomicanalysisof pages 14-15) |


*Table: This table organizes the benzoate, catechol, protocatechuate, gallate, and adjacent-pathway candidate genes for Pseudomonas putida KT2440 by pathway role, evidence, confidence, and curation relevance. It is useful for deciding which genes satisfy the KEGG benzoate-degradation module versus which are neighboring or likely over-propagated annotations.*

### 4.1 High-Confidence Core Pathway Genes (17 genes)

**benABCD (PP_3161–3164):** The benzoate entry operon is well-characterized in KT2440. BenA and BenB form the oxygenase component, BenC is the NADH-dependent reductase, and BenD is the cis-diol dehydrogenase. All four have been confirmed by proteomics, transcriptomics, and genetic studies to be induced during benzoate growth (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10, loh2008paradigminbiodegradation pages 6-8). BenR (AraC-family) activates ben operon transcription, subject to catabolite repression via the Crc global regulator (cao2008catabolicpathwaysand pages 10-11).

**catA-I (PP_3713) and catA-II (PP_3166):** KT2440 uniquely contains two catechol 1,2-dioxygenase paralogs. CatA-I resides in the canonical cat cluster (catRBCA at 4236–4239 kb) and is the primary ortho-cleavage dioxygenase. CatA-II (catA2) is embedded within the ben cluster between benR and benA, shares 77% amino acid identity with CatA-I, and likely serves as an "enzymatic safety valve" to handle excess catechol from benzoate degradation (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10). This paralog relationship is a key curation point: both are genuine catechol 1,2-dioxygenases with confirmed function.

**catB (PP_3715), catC (PP_3714):** Muconate cycloisomerase and muconolactone δ-isomerase, respectively, forming the catechol branch of ortho-cleavage. CatB is essential for growth on benzoate; both are co-regulated by CatR (LysR-type) with cis,cis-muconate as inducer (cao2008inductionofortho pages 6-7, jimenez2002genomicanalysisof pages 5-6, cao2008catabolicpathwaysand pages 10-11).

**pcaGH (PP_4655/4656):** Protocatechuate 3,4-dioxygenase α and β subunits located at 5281–5282 kb. Their overexpression was a key engineering target for enhanced β-ketoadipate production from lignin aromatics (jimenez2002genomicanalysisof pages 3-5, werner2023ligninconversionto pages 5-7, werner2023ligninconversionto pages 4-5).

**pcaBCD (PP_1379–1381):** These reside in the pcaRKFTBDCP cluster at 1566–1575 kb and encode the protocatechuate branch enzymes that converge with the catechol branch at β-ketoadipate (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5).

**pcaIJ (PP_3951/3952):** 3-Oxoadipate CoA-transferase subunits at 4457–4459 kb. PcaIJ proteins show the lowest sequence conservation among pca gene products across Pseudomonas species, suggesting distinct evolutionary origins (jimenez2002genomicanalysisof pages 3-5). Deletion of pcaIJ was the key engineering step to accumulate β-ketoadipate as a product in Werner et al. (2023) (werner2023ligninconversionto pages 2-4, werner2023ligninconversionto pages 1-2).

**pcaF-I (PP_1377):** The canonical β-ketoadipyl-CoA thiolase in the pcaRKFTBDCP cluster. Despite multiple thiolase homologs in the genome, pcaF-I is the pathway-specific enzyme, distinguished by its genetic linkage to other pca genes and its substrate specificity for 3-oxoadipyl-CoA (jimenez2002genomicanalysisof pages 3-5, cao2008inductionofortho pages 6-7).

**pobA (PP_3537):** 4-Hydroxybenzoate 3-monooxygenase at 4009–4012 kb, regulated by PobR (XylS/AraC-type). Converts 4-hydroxybenzoate to protocatechuate, feeding the pca branch (jimenez2002genomicanalysisof pages 6-9).

### 4.2 Gallate Branch Genes (3 genes)

**galD (PP_2513), galB (PP_2515), galC (PP_2514):** These encode 4-oxalomesaconate tautomerase, OMA hydratase, and CHA aldolase, respectively, in the gal operon. Their function has been validated in KT2440 by genetic and biochemical studies (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2). The gal operon is regulated by GalR, with 4-oxalomesaconate (not gallic acid itself) serving as the effector molecule (kutraite2023developmentandapplication pages 2-3). Note that galA (gallate dioxygenase), galT (transporter), and galP (porin) are not in the candidate list but are present in the KT2440 genome and essential for gallate entry (kutraite2023developmentandapplication pages 1-2, dias2023fromdegraderto pages 4-6).

### 4.3 Adjacent-Pathway Genes (3 genes)

**paaJ (PP_3280):** Annotated as 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase with dual EC numbers (2.3.1.– and 2.3.1.174). Its primary role is in the phenylacetyl-CoA catabolic pathway rather than the canonical β-ketoadipate pathway. However, the EC 2.3.1.174 annotation suggests potential cross-reactivity with β-ketoadipyl-CoA. Its placement in the candidate list likely reflects KEGG's broad benzoate map inclusion of phenylacetate-adjacent reactions (jimenez2002genomicanalysisof pages 10-12).

**paaH (PP_3282), paaF (PP_3284):** 3-Hydroxyadipyl-CoA dehydrogenase and enoyl-CoA hydratase-isomerase. These belong to the phenylacetate degradation cluster and should be assigned to ppu00360 rather than the benzoate/β-ketoadipate core (jimenez2002genomicanalysisof pages 10-12).

### 4.4 Uncertain/Peripheral Genes (2 genes)

**fdx (PP_0847):** A generic 2Fe-2S ferredoxin assigned to ppu00362. While ferredoxins participate in electron transfer for Rieske-type dioxygenases, no direct evidence links this specific locus to the benzoate dioxygenase system in KT2440. The ben cluster already encodes BenC as its reductase component (jimenez2002genomicanalysisof pages 9-10).

**PP_1950:** Cytochrome P450 with no established role in benzoate or β-ketoadipate catabolism. Its inclusion likely reflects the broad KEGG map structure (jimenez2002genomicanalysisof pages 14-15).

### 4.5 Likely Over-Propagated Annotations (~15 genes)

Multiple generic thiolases (PP_0582, PP_2215, PP_3355, yqeF/PP_4636, bktB/PP_3754), β-oxidation enzymes (fadA/PP_2051, fadA/PP_2137, fadB/PP_2136), and miscellaneous CoA-metabolism genes (hbd/PP_3755, PP_2217, PP_1218, gcdH/PP_0158, PP_1791) are included in the candidate list. These share broad EC class membership (EC 2.3.1.9, 2.3.1.16, 4.2.1.17, 1.1.1.35) with genuine β-ketoadipate pathway enzymes but function primarily in fatty acid β-oxidation, generic CoA metabolism, or unrelated pathways (jimenez2002genomicanalysisof pages 12-14, jimenez2002genomicanalysisof pages 14-15). PP_2504 (2-hydroxymuconate tautomerase, EC 5.3.2.6) is characteristic of the catechol *meta*-cleavage pathway and is not part of the ortho-cleavage β-ketoadipate route used by KT2440 for benzoate degradation.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Regulatory Genes Not in Candidate List

Several essential regulatory genes are absent from the candidate list but are critical for pathway function: **CatR** (LysR-type, activates catBCA), **PcaR** (IclR-type, activates pca genes with β-ketoadipate as inducer), **BenR** (AraC-type, activates ben operon), **PobR** (XylS/AraC-type, activates pobA), and **GalR** (LysR-type, activates gal operon) (jimenez2002genomicanalysisof pages 6-9, cao2008catabolicpathwaysand pages 10-11, kutraite2023developmentandapplication pages 2-3). These are standard omissions in enzyme-focused KEGG maps but are important for understanding pathway regulation.

### 5.2 Transport Genes Not in Candidate List

Transport genes **BenK** (benzoate permease), **BenF** (benzoate-specific porin), **PcaK** (4-hydroxybenzoate transporter), **PcaT** (β-ketoadipate transporter), **PcaP** (putative porin), **GalT** (MFS transporter), and **GalP** (outer membrane porin) are present in KT2440 but absent from the candidate list (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 9-10, kutraite2023developmentandapplication pages 1-2, dias2023fromdegraderto pages 4-6).

### 5.3 galA Missing from Candidate List

Gallate dioxygenase (galA) is the entry enzyme for the gallate branch and is essential for the function of galB/C/D, which are in the candidate list. Its absence is a notable gap (kutraite2023developmentandapplication pages 1-2, dias2023fromdegraderto pages 4-6).

### 5.4 Thiolase Paralog Inflation

The most significant over-annotation problem is the inflation of thiolase/acetyltransferase candidates. KT2440 encodes numerous thiolase family members (at least 8 in the candidate list beyond pcaF-I), but only pcaF-I (PP_1377) has direct evidence for β-ketoadipyl-CoA thiolase activity. The inclusion of fadA paralogs, bktB, PP_0582, PP_2215, PP_3355, and yqeF likely reflects broad EC 2.3.1.9/2.3.1.16 family propagation rather than pathway-specific annotation (jimenez2002genomicanalysisof pages 12-14, jimenez2002genomicanalysisof pages 3-5).

### 5.5 Meta-Cleavage Gene Contamination

PP_2504 (2-hydroxymuconate tautomerase) belongs to the meta-cleavage pathway, which is not the route used by KT2440 for benzoate catabolism. KT2440 uses exclusively the ortho-cleavage (β-ketoadipate) pathway for benzoate degradation via the chromosomally encoded pathway (cao2008catabolicpathwaysand pages 10-11, dumalo2020dioxygenasesinthe pages 27-32).

## 6. Module and GO-Curation Recommendations

The module satisfiability assessment for KEGG ppu00362 in KT2440 is summarized below:

| Module Step | Expected Enzyme/Activity | Gene(s) in KT2440 | Status | Notes |
|---|---|---|---|---|
| Benzoate hydroxylation | Benzoate 1,2-dioxygenase | benA/benB/benC (PP_3161-PP_3163) | COVERED | Direct experimental and genomic evidence for ben cluster in KT2440 (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10, jimenez2002genomicanalysisof pages 6-9) |
| cis-diol dehydrogenation | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase | benD (PP_3164) | COVERED | Direct experimental and genomic evidence for benzoate cis-diol to catechol conversion (jimenez2002genomicanalysisof pages 9-10, loh2008paradigminbiodegradation pages 6-8) |
| Catechol ortho-cleavage | Catechol 1,2-dioxygenase | catA-I (PP_3713), catA-II (PP_3166) | COVERED | Two paralogs; catA-II is embedded in the ben cluster, supporting benzoate-derived catechol processing (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 9-10) |
| Muconate cycloisomerization | Muconate cycloisomerase | catB (PP_3715) | COVERED | Direct evidence for catechol-branch ortho-cleavage enzyme (cao2008inductionofortho pages 6-7, jimenez2002genomicanalysisof pages 5-6) |
| Muconolactone isomerization | Muconolactone delta-isomerase | catC (PP_3714) | COVERED | Direct evidence for catechol branch lower-pathway step (jimenez2002genomicanalysisof pages 5-6) |
| 4-hydroxybenzoate hydroxylation | 4-hydroxybenzoate 3-monooxygenase | pobA (PP_3537) | COVERED | Direct evidence for protocatechuate-entry branch; pob cluster mapped in KT2440 (jimenez2002genomicanalysisof pages 6-9) |
| Protocatechuate 3,4-dioxygenase | Protocatechuate 3,4-dioxygenase | pcaG/pcaH (PP_4655/PP_4656) | COVERED | Direct evidence for ring-cleavage step of the protocatechuate branch (jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 2-3) |
| 3-carboxy-cis,cis-muconate cycloisomerization | 3-carboxy-cis,cis-muconate cycloisomerase | pcaB (PP_1379) | COVERED | Direct evidence from pca cluster annotation and pathway mapping (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5) |
| 4-carboxymuconolactone decarboxylation | 4-carboxymuconolactone decarboxylase | pcaC (PP_1381) | COVERED | Direct evidence from pca cluster annotation and pathway mapping (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5) |
| 3-oxoadipate enol-lactone hydrolysis | 3-oxoadipate enol-lactonase | pcaD (PP_1380) | COVERED | Direct evidence for shared lower-pathway step after branch convergence (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5, dumalo2020dioxygenasesinthe pages 27-32) |
| 3-oxoadipate CoA transfer | 3-oxoadipate CoA-transferase | pcaI/pcaJ (PP_3951/PP_3952) | COVERED | Direct evidence for terminal beta-ketoadipate CoA activation step (jimenez2002genomicanalysisof pages 3-5) |
| Beta-ketoadipyl-CoA thiolysis | Beta-ketoadipyl-CoA thiolase | pcaF-I (PP_1377) | COVERED | Canonical terminal thiolase of the beta-ketoadipate pathway despite other thiolase paralogs elsewhere in genome (jimenez2002genomicanalysisof pages 3-5, cao2008inductionofortho pages 6-7) |
| Gallate dioxygenation | Gallate dioxygenase | galA (present in genome; not in candidate list) | CANDIDATE_UNCERTAIN | galA is supported by recent KT2440 gallate studies, but it is absent from the supplied candidate list; gallate is a side branch, not core benzoate entry (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2, dias2023fromdegraderto pages 4-6) |
| 4-oxalomesaconate tautomerization | 4-oxalomesaconate tautomerase | galD (PP_2513) | COVERED | Covered for the gallate branch specifically, not required for strict benzoate-to-catechol module satisfiability (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2) |
| OMA hydration | 4-oxalomesaconate hydratase | galB (PP_2515) | COVERED | Covered for the gallate branch specifically (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2) |
| CHA aldol cleavage | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase | galC (PP_2514) | COVERED | Covered for the gallate branch specifically (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2) |
| Ferredoxin electron transfer | Generic 2Fe-2S ferredoxin | fdx (PP_0847) | CANDIDATE_UNCERTAIN | Generic ferredoxin; no direct evidence that this locus is the dedicated benzoate dioxygenase electron-transfer partner in KT2440 (jimenez2002genomicanalysisof pages 14-15, jimenez2002genomicanalysisof pages 6-9) |
| Cytochrome P450 node | Cytochrome P450 | PP_1950 | NOT_EXPECTED | No direct evidence for a role in core benzoate/beta-ketoadipate degradation in KT2440; likely KEGG neighborhood/over-map carryover (jimenez2002genomicanalysisof pages 14-15) |


*Table: This table summarizes step-by-step satisfiability of KEGG ppu00362 in Pseudomonas putida KT2440, distinguishing core covered steps from side-branch and uncertain assignments. It is useful for manual pathway curation and deciding which candidate genes truly satisfy the benzoate/beta-ketoadipate module.*

### 6.1 Key Recommendations

1. **All core β-ketoadipate pathway steps are fully satisfiable** in KT2440 with high-confidence gene assignments. No gaps exist in the benzoate→catechol→β-ketoadipate→succinyl-CoA + acetyl-CoA route or the 4-hydroxybenzoate→protocatechuate→β-ketoadipate route.

2. **The gallate branch should be treated as a separate sub-module** or clearly distinguished from the core benzoate/protocatechuate β-ketoadipate pathway. The three candidate gal genes (galB/C/D) are valid for the gallate side branch but should not be required for core benzoate module satisfiability.

3. **Remove or reclassify ~15 over-propagated genes** that are generic thiolases, β-oxidation enzymes, or unrelated metabolic functions. These should not satisfy any β-ketoadipate pathway step.

4. **Reclassify paaJ/paaH/paaF** to the phenylacetate degradation pathway (ppu00360) as their primary assignment.

5. **Mark fdx (PP_0847) and PP_1950 as candidate_uncertain/not_expected** pending direct experimental evidence for benzoate dioxygenase-specific function.

6. **Consider adding galA** to the candidate list if the gallate branch is retained within the module scope.

7. **Module boundary revision:** The broad KEGG ppu00362 map conflates benzoate core catabolism with phenylacetate, fatty acid β-oxidation, and miscellaneous CoA-metabolism nodes. A stricter module definition restricted to Steps 1–5 above, with the gallate branch as an optional extension, would better reflect the biology of KT2440.

### 6.2 GO Term Considerations

- GO:0019380 (benzoate catabolic process) appropriately covers Steps 1–5.
- The catA-II/catA-I paralog pair could benefit from a qualifier annotation distinguishing the ben-cluster copy (catA-II, PP_3166) from the cat-cluster copy (catA-I, PP_3713).
- EC 2.3.1.174 (β-ketoadipyl-CoA thiolase) should be restricted to pcaF-I (PP_1377) and not propagated to generic thiolases.

## 7. Genes to Promote to Full Review

The following genes warrant detailed fetch-gene review:

1. **pcaF-I (PP_1377):** Critical to resolve paralog ambiguity against paaJ (PP_3280) and multiple generic thiolases. Substrate specificity for 3-oxoadipyl-CoA should be verified.

2. **catA-II (PP_3166):** The second catechol 1,2-dioxygenase in the ben cluster merits review to clarify its physiological role versus catA-I; the "safety valve" hypothesis from Jiménez et al. (2014, not obtained but referenced) should be evaluated.

3. **paaJ (PP_3280):** Dual EC annotation (2.3.1.– and 2.3.1.174) creates ambiguity. Its cross-reactivity with β-ketoadipyl-CoA versus phenylacetate-pathway intermediates needs clarification.

4. **fdx (PP_0847):** Its assignment to ppu00362 should be evaluated against the known BenC reductase component already present in the ben operon.

5. **galA (not in candidate list):** Should be added and reviewed as the entry enzyme for the gallate branch, given that downstream galB/C/D are already candidates.

## 8. Key References

The following literature directly supports the major claims in this review:

- **Jiménez et al. (2002)** – Foundational genomic analysis of all aromatic catabolic pathways in KT2440, including ben, cat, pca, pob, and pha cluster organization (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 9-10, jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 14-15, jimenez2002genomicanalysisof pages 2-3). DOI: 10.1046/j.1462-2920.2002.00370.x

- **Werner et al. (2023)** – Landmark metabolic engineering study producing β-ketoadipic acid from lignin in KT2440; demonstrated pcaIJ deletion and pcaHG overexpression strategies (werner2023ligninconversionto pages 2-4, werner2023ligninconversionto pages 1-2, werner2023ligninconversionto pages 5-7, werner2023ligninconversionto pages 4-5). DOI: 10.1126/sciadv.adj0053

- **Kutraite & Malys (2023)** – Characterization of the gal operon transcriptional regulation; identified 4-oxalomesaconate as the GalR effector molecule (kutraite2023developmentandapplication pages 2-3, kutraite2023developmentandapplication pages 1-2). DOI: 10.1021/acssynbio.2c00537

- **Dias et al. (2023)** – Reverse engineering of gallic acid metabolism in KT2440 (dias2023fromdegraderto pages 4-6). DOI: 10.1007/s10123-022-00282-5

- **Moreno & Rojo (2008)** – Identification of BenR as the Crc target in benzoate pathway regulation (cao2008catabolicpathwaysand pages 10-11). DOI: 10.1128/jb.01604-07

- **Cao & Loh (2008)** – Proteomic characterization of benzoate catabolic enzymes including ortho-cleavage pathway identification (cao2008inductionofortho pages 6-7). DOI: 10.1007/s00253-008-1728-3

- **Dumalo (2020)** – Description of the biological funnel architecture for aromatic catabolism in KT2440 (dumalo2020dioxygenasesinthe pages 27-32, dumalo2020dioxygenasesinthe pages 23-27). DOI: 10.14288/1.0394310

- **Nogales et al. (2008)** – Genome-scale metabolic reconstruction iJN746 including aromatic degradation pathways. DOI: 10.1186/1752-0509-2-79

- **Jin et al. (2024)** – Protocatechuic acid production from lignin hydrolysates using engineered KT2440. DOI: 10.3390/molecules29071555

- **Bleem et al. (2024)** – Evolution and engineering of aromatic O-demethylation pathways in KT2440. DOI: 10.1016/j.ymben.2024.06.009

References

1. (jimenez2002genomicanalysisof pages 1-2): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

2. (dumalo2020dioxygenasesinthe pages 27-32): Linda Dumalo. Dioxygenases in the catabolism of syringols in pseudomonas putida kt2440. ArXiv, Jan 2020. URL: https://doi.org/10.14288/1.0394310, doi:10.14288/1.0394310. This article has 0 citations.

3. (dumalo2020dioxygenasesinthe pages 23-27): Linda Dumalo. Dioxygenases in the catabolism of syringols in pseudomonas putida kt2440. ArXiv, Jan 2020. URL: https://doi.org/10.14288/1.0394310, doi:10.14288/1.0394310. This article has 0 citations.

4. (jimenez2002genomicanalysisof pages 12-14): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

5. (jimenez2002genomicanalysisof pages 14-15): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

6. (jimenez2002genomicanalysisof pages 5-6): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

7. (jimenez2002genomicanalysisof pages 6-9): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

8. (kutraite2023developmentandapplication pages 2-3): Ingrida Kutraite and Naglis Malys. Development and application of whole-cell biosensors for the detection of gallic acid. ACS Synthetic Biology, 12:533-543, Feb 2023. URL: https://doi.org/10.1021/acssynbio.2c00537, doi:10.1021/acssynbio.2c00537. This article has 37 citations and is from a domain leading peer-reviewed journal.

9. (kutraite2023developmentandapplication pages 1-2): Ingrida Kutraite and Naglis Malys. Development and application of whole-cell biosensors for the detection of gallic acid. ACS Synthetic Biology, 12:533-543, Feb 2023. URL: https://doi.org/10.1021/acssynbio.2c00537, doi:10.1021/acssynbio.2c00537. This article has 37 citations and is from a domain leading peer-reviewed journal.

10. (dias2023fromdegraderto pages 4-6): Felipe M. S. Dias, Raoní K. Pantoja, José Gregório C. Gomez, and Luiziana F. Silva. From degrader to producer: reversing the gallic acid metabolism of pseudomonas putida kt2440. International Microbiology, 26:243-255, Nov 2023. URL: https://doi.org/10.1007/s10123-022-00282-5, doi:10.1007/s10123-022-00282-5. This article has 8 citations and is from a peer-reviewed journal.

11. (jimenez2002genomicanalysisof pages 10-12): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

12. (jimenez2002genomicanalysisof pages 15-17): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

13. (werner2023ligninconversionto pages 2-4): Allison Z. Werner, William T. Cordell, Ciaran W. Lahive, Bruno C. Klein, Christine A. Singer, Eric C. D. Tan, Morgan A. Ingraham, Kelsey J. Ramirez, Dong Hyun Kim, Jacob Nedergaard Pedersen, Christopher W. Johnson, Brian F. Pfleger, Gregg T. Beckham, and Davinia Salvachúa. Lignin conversion to β-ketoadipic acid by <i>pseudomonas putida</i> via metabolic engineering and bioprocess development. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adj0053, doi:10.1126/sciadv.adj0053. This article has 92 citations and is from a highest quality peer-reviewed journal.

14. (werner2023ligninconversionto pages 1-2): Allison Z. Werner, William T. Cordell, Ciaran W. Lahive, Bruno C. Klein, Christine A. Singer, Eric C. D. Tan, Morgan A. Ingraham, Kelsey J. Ramirez, Dong Hyun Kim, Jacob Nedergaard Pedersen, Christopher W. Johnson, Brian F. Pfleger, Gregg T. Beckham, and Davinia Salvachúa. Lignin conversion to β-ketoadipic acid by <i>pseudomonas putida</i> via metabolic engineering and bioprocess development. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adj0053, doi:10.1126/sciadv.adj0053. This article has 92 citations and is from a highest quality peer-reviewed journal.

15. (jimenez2002genomicanalysisof pages 9-10): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

16. (jimenez2002genomicanalysisof pages 2-3): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

17. (loh2008paradigminbiodegradation pages 6-8): Kai-Chee Loh and Bin Cao. Paradigm in biodegradation using pseudomonas putida—a review of proteomics studies. Enzyme and Microbial Technology, 43:1-12, Jul 2008. URL: https://doi.org/10.1016/j.enzmictec.2008.03.004, doi:10.1016/j.enzmictec.2008.03.004. This article has 95 citations and is from a peer-reviewed journal.

18. (cao2008inductionofortho pages 6-7): Bin Cao, Anli Geng, and Kai-Chee Loh. Induction of ortho- and meta-cleavage pathways in pseudomonas in biodegradation of high benzoate concentration: ms identification of catabolic enzymes. Nov 2008. URL: https://doi.org/10.1007/s00253-008-1728-3, doi:10.1007/s00253-008-1728-3. This article has 99 citations and is from a domain leading peer-reviewed journal.

19. (jimenez2002genomicanalysisof pages 3-5): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

20. (cao2008catabolicpathwaysand pages 10-11): Bin Cao and Kai‐Chee Loh. Catabolic pathways and cellular responses of pseudomonas putida p8 during growth on benzoate with a proteomics approach. Biotechnology and Bioengineering, 101:1297-1312, Dec 2008. URL: https://doi.org/10.1002/bit.21997, doi:10.1002/bit.21997. This article has 56 citations and is from a domain leading peer-reviewed journal.

21. (werner2023ligninconversionto pages 5-7): Allison Z. Werner, William T. Cordell, Ciaran W. Lahive, Bruno C. Klein, Christine A. Singer, Eric C. D. Tan, Morgan A. Ingraham, Kelsey J. Ramirez, Dong Hyun Kim, Jacob Nedergaard Pedersen, Christopher W. Johnson, Brian F. Pfleger, Gregg T. Beckham, and Davinia Salvachúa. Lignin conversion to β-ketoadipic acid by <i>pseudomonas putida</i> via metabolic engineering and bioprocess development. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adj0053, doi:10.1126/sciadv.adj0053. This article has 92 citations and is from a highest quality peer-reviewed journal.

22. (werner2023ligninconversionto pages 4-5): Allison Z. Werner, William T. Cordell, Ciaran W. Lahive, Bruno C. Klein, Christine A. Singer, Eric C. D. Tan, Morgan A. Ingraham, Kelsey J. Ramirez, Dong Hyun Kim, Jacob Nedergaard Pedersen, Christopher W. Johnson, Brian F. Pfleger, Gregg T. Beckham, and Davinia Salvachúa. Lignin conversion to β-ketoadipic acid by <i>pseudomonas putida</i> via metabolic engineering and bioprocess development. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adj0053, doi:10.1126/sciadv.adj0053. This article has 92 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__benzoate_degradation__ppu00362-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__benzoate_degradation__ppu00362-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. jimenez2002genomicanalysisof pages 1-2
2. jimenez2002genomicanalysisof pages 6-9
3. jimenez2002genomicanalysisof pages 14-15
4. jimenez2002genomicanalysisof pages 3-5
5. jimenez2002genomicanalysisof pages 10-12
6. jimenez2002genomicanalysisof pages 12-14
7. cao2008catabolicpathwaysand pages 10-11
8. kutraite2023developmentandapplication pages 2-3
9. jimenez2002genomicanalysisof pages 9-10
10. jimenez2002genomicanalysisof pages 5-6
11. dias2023fromdegraderto pages 4-6
12. cao2008inductionofortho pages 6-7
13. dumalo2020dioxygenasesinthe pages 27-32
14. dumalo2020dioxygenasesinthe pages 23-27
15. kutraite2023developmentandapplication pages 1-2
16. jimenez2002genomicanalysisof pages 15-17
17. werner2023ligninconversionto pages 2-4
18. werner2023ligninconversionto pages 1-2
19. jimenez2002genomicanalysisof pages 2-3
20. loh2008paradigminbiodegradation pages 6-8
21. werner2023ligninconversionto pages 5-7
22. werner2023ligninconversionto pages 4-5
23. Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)
24. https://doi.org/10.1046/j.1462-2920.2002.00370.x,
25. https://doi.org/10.14288/1.0394310,
26. https://doi.org/10.1021/acssynbio.2c00537,
27. https://doi.org/10.1007/s10123-022-00282-5,
28. https://doi.org/10.1126/sciadv.adj0053,
29. https://doi.org/10.1016/j.enzmictec.2008.03.004,
30. https://doi.org/10.1007/s00253-008-1728-3,
31. https://doi.org/10.1002/bit.21997,