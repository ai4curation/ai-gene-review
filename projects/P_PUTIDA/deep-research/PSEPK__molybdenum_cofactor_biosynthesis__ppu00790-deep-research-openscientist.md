---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T21:22:13.819886'
end_time: '2026-07-20T21:57:43.798518'
duration_seconds: 2129.98
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Prokaryotic molybdenum cofactor biosynthesis from GTP to Mo-molybdopterin
    and optional dinucleotide variants
  module_summary: 'A reusable prokaryotic module for molybdenum cofactor biosynthesis
    constructs the pyranopterin dithiolene ligand from GTP, loads it with molybdenum,
    and may append a nucleotide to produce a client-class-specific cofactor variant.
    MoaA first performs radical-SAM cyclization of GTP and MoaC rearranges the cyclic
    intermediate to cyclic pyranopterin monophosphate (cPMP). Molybdopterin synthase
    then inserts two sulfurs: MoeB activates the small MoaD sulfur carrier, and the
    MoaD-MoaE synthase converts cPMP to molybdopterin (MPT). Across prokaryotic realizations,
    MPT is adenylylated by a separate bacterial MogA or by a catalytically competent
    prokaryotic MoaB lineage, and MoeA then inserts molybdate to form Mo-MPT. Some
    realizations stop at Mo-MPT, whereas others use MobA to make MGD or MocA to make
    MCD. The module excludes upstream sulfur supply, molybdate transport, terminal
    cofactor sulfuration, cofactor insertion into client apoenzymes, mature molybdoenzyme
    reactions, pathway regulation, eukaryotic MOCS/CNX/GPHN fusion organization, and
    human disease.'
  module_outline: "- Prokaryotic molybdenum cofactor biosynthesis\n  - 1. cyclic pyranopterin\
    \ monophosphate formation\n  - Cyclic pyranopterin monophosphate formation\n \
    \   - 1. radical-SAM GTP cyclization\n    - MoaA GTP cyclization\n      - MoaA\
    \ GTP 3',8'-cyclase (molecular player: PSEPK canonical MoaA; activity or role:\
    \ GTP 3',8'-cyclase activity)\n    - 2. cyclic intermediate rearrangement to cPMP\n\
    \    - MoaC cPMP synthesis\n      - MoaC cyclic pyranopterin monophosphate synthase\
    \ (molecular player: bacterial MoaC cPMP synthase family; activity or role: cyclic\
    \ pyranopterin monophosphate synthase activity)\n  - 2. sulfur-carrier activation\
    \ and molybdopterin synthesis\n  - Sulfur-carrier activation and MPT formation\n\
    \    - 1. MoaD sulfur-carrier activation\n    - MoeB-dependent MoaD activation\n\
    \      - MoeB molybdopterin-synthase sulfur-carrier adenylyltransferase (molecular\
    \ player: bacterial MoeB molybdopterin-synthase sulfur-carrier adenylyltransferase\
    \ family; activity or role: molybdopterin-synthase adenylyltransferase activity)\n\
    \      - MoaD molybdopterin-synthase sulfur carrier (molecular player: bacterial\
    \ MoaD molybdopterin-synthase sulfur-carrier family)\n    - 2. sulfur insertion\
    \ into cPMP\n    - MoaD-MoaE molybdopterin synthesis\n      - MoaD2-MoaE2 molybdopterin\
    \ synthase complex (molecular player: prokaryotic MoaD2-MoaE2 molybdopterin synthase\
    \ complex; activity or role: molybdopterin synthase activity)\n  - 3. MPT adenylylation\
    \ and molybdate insertion\n  - Mo-molybdopterin formation\n    - 1. MPT adenylylation\n\
    \    - Molybdopterin adenylylation\n      - Alternative versions by prokaryotic\
    \ enzyme lineage: MPT adenylyltransferase implementations\n        - Separate\
    \ MogA adenylyltransferase\n          - MogA molybdopterin adenylyltransferase\
    \ (molecular player: bacterial MogA molybdopterin adenylyltransferase family;\
    \ activity or role: molybdopterin adenylyltransferase activity)\n        - Catalytically\
    \ competent prokaryotic MoaB adenylyltransferase\n          - Catalytically competent\
    \ prokaryotic MoaB molybdopterin adenylyltransferase (molecular player: Pyrococcus\
    \ furiosus MoaB; activity or role: molybdopterin adenylyltransferase activity)\n\
    \    - 2. molybdate insertion into adenylyl-MPT\n    - Molybdopterin molybdotransfer\n\
    \      - MoeA molybdopterin molybdotransferase (molecular player: PSEPK MoeA;\
    \ activity or role: molybdopterin molybdotransferase activity)\n  - 4. optional\
    \ nucleotide maturation of Mo-MPT\n  - Optional Mo-MPT nucleotide maturation\n\
    \    - Alternative versions by appended nucleotide: Mo-MPT dinucleotide variants\n\
    \      - MGD formation by MobA\n        - MobA molybdenum cofactor guanylyltransferase\
    \ (molecular player: bacterial MobA molybdenum cofactor guanylyltransferase family;\
    \ activity or role: molybdenum cofactor guanylyltransferase activity)\n      -\
    \ MCD formation by MocA\n        - MocA molybdenum cofactor cytidylyltransferase\
    \ (molecular player: bacterial MocA molybdenum cofactor cytidylyltransferase family;\
    \ activity or role: molybdenum cofactor cytidylyltransferase activity)"
  module_connections: '- Cyclic pyranopterin monophosphate formation feeds into Sulfur-carrier
    activation and MPT formation: cPMP is the pterin substrate for sulfur insertion
    by molybdopterin synthase.

    - Sulfur-carrier activation and MPT formation feeds into Mo-molybdopterin formation:
    MPT is activated and loaded with molybdate to form Mo-MPT.

    - Mo-molybdopterin formation feeds into Optional Mo-MPT nucleotide maturation:
    Mo-MPT may be retained directly or converted to MGD and/or MCD.

    - MoaA GTP cyclization feeds into MoaC cPMP synthesis: The cyclic GTP product
    of MoaA is the substrate for MoaC.

    - MoeB-dependent MoaD activation precedes MoaD-MoaE molybdopterin synthesis: Activated
    MoaD is sulfur-loaded by an external sulfur-donor system before supplying the
    MoaE reaction.

    - Molybdopterin adenylylation feeds into Molybdopterin molybdotransfer: Adenylyl-MPT
    produced by the selected activation variant is the substrate for molybdate insertion.'
  pathway_query: ppu00790
  pathway_id: ppu00790
  pathway_name: Folate biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00790 with 19 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '32'
  candidate_genes: '- folB: PP_0392 | Q88QU4 | 7,8-dihydroneopterin aldolase (EC 4.1.2.25)
    (EC 4.1.2.25; primary bucket kegg:ppu00790)

    - PP_0393: PP_0393 | Q88QU3 | 2-amino-4-hydroxy-6-hydroxymethyldihydropteridine
    diphosphokinase (EC 2.7.6.3) (EC 2.7.6.3; primary bucket kegg:ppu00790)

    - ribAB-I: PP_0516 | Q88QH7 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - ribA: PP_0522 | Q88QH1 | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase
    II) (EC 3.5.4.25; primary bucket kegg:ppu00740)

    - queE: PP_1225 | Q88NI4 | 7-carboxy-7-deazaguanine synthase (CDG synthase) (EC
    4.3.99.3) (Queuosine biosynthesis protein QueE) (EC 4.3.99.3; primary bucket kegg:ppu00790)

    - queC: PP_1226 | Q88NI3 | 7-cyano-7-deazaguanine synthase (EC 6.3.4.20) (7-cyano-7-carbaguanine
    synthase) (PreQ(0) synthase) (Queuosine biosynthesis protein QueC) (EC 6.3.4.20;
    primary bucket kegg:ppu00790)

    - moaC: PP_1292 | Q88NC0 | Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17)
    (Molybdenum cofactor biosynthesis protein C) (EC 4.6.1.17; primary bucket kegg:ppu04122)

    - moaE: PP_1294 | Q88NB8 | Molybdopterin synthase catalytic subunit (EC 2.8.1.12)
    (MPT synthase subunit 2) (Molybdenum cofactor biosynthesis protein E) (Molybdopterin-converting
    factor large subunit) (Molybdopterin-converting factor subunit 2) (EC 2.8.1.12;
    primary bucket kegg:ppu04122)

    - folE1: PP_1823 | Q88LV4 | GTP cyclohydrolase 1 1 (EC 3.5.4.16) (GTP cyclohydrolase
    I 1) (GTP-CH-I 1) (EC 3.5.4.16; primary bucket kegg:ppu00790)

    - pabC: PP_1917 | Q88LL3 | Aminodeoxychorismate lyase (EC 4.1.3.38) (EC 4.1.3.38;
    primary bucket kegg:ppu00790)

    - PP_1969: PP_1969 | Q88LG4 | Molybdenum cofactor biosynthesis protein A (primary
    bucket kegg:ppu04122)

    - folC: PP_1997 | Q88LD8 | Dihydrofolate synthase/folylpolyglutamate synthase
    (EC 6.3.2.12) (EC 6.3.2.17) (Folylpoly-gamma-glutamate synthetase-dihydrofolate
    synthetase) (Folylpolyglutamate synthetase) (Tetrahydrofolylpolyglutamate synthase)
    (EC 6.3.2.12; 6.3.2.17; primary bucket kegg:ppu00790)

    - moaB-I: PP_2122 | Q88L15 | Molybdenum cofactor biosynthesis protein B (primary
    bucket kegg:ppu04122)

    - moeA: PP_2123 | Q88L14 | Molybdopterin molybdenumtransferase (EC 2.10.1.1) (EC
    2.10.1.1; primary bucket kegg:ppu00790)

    - queF: PP_2160 | Q88KX9 | NADPH-dependent 7-cyano-7-deazaguanine reductase (EC
    1.7.1.13) (7-cyano-7-carbaguanine reductase) (NADPH-dependent nitrile oxidoreductase)
    (PreQ(0) reductase) (EC 1.7.1.13; primary bucket kegg:ppu00790)

    - pabB: PP_2329 | Q88KG1 | aminodeoxychorismate synthase (EC 2.6.1.85) (EC 2.6.1.85;
    primary bucket kegg:ppu00790)

    - queD: PP_2341 | Q88KE9 | 6-carboxy-5,6,7,8-tetrahydropterin synthase (EC 4.-.-.-)
    (EC 4.-.-.-; primary bucket kegg:ppu00790)

    - PP_2482: PP_2482 | Q88K11 | Molybdenum cofactor biosynthesis protein A (primary
    bucket kegg:ppu04122)

    - PP_2483: PP_2483 | Q88K10 | MobA-like NTP transferase domain-containing protein
    (primary bucket kegg:ppu00790)

    - folE2__Q88JY1: PP_2512 | Q88JY1 | GTP cyclohydrolase 1 2 (EC 3.5.4.16) (GTP
    cyclohydrolase I 2) (GTP-CH-I 2) (EC 3.5.4.16; primary bucket kegg:ppu00790)

    - folE2__Q88HM9: PP_3324 | Q88HM9 | GTP cyclohydrolase FolE2 (EC 3.5.4.16) (EC
    3.5.4.16; primary bucket kegg:ppu00790)

    - mobA: PP_3457 | Q88HA3 | Molybdenum cofactor guanylyltransferase (MoCo guanylyltransferase)
    (EC 2.7.7.77) (GTP:molybdopterin guanylyltransferase) (Mo-MPT guanylyltransferase)
    (Molybdopterin guanylyltransferase) (Molybdopterin-guanine dinucleotide synthase)
    (MGD synthase) (EC 2.7.7.77; primary bucket kegg:ppu00790)

    - ribAB-II: PP_3813 | Q88GB1 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - PP_4230: PP_4230 | Q88F68 | MobA-like NTP transferase domain-containing protein
    (primary bucket kegg:ppu00790)

    - phhA: PP_4490 | Q88EH3 | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase)
    (EC 1.14.16.1; primary bucket kegg:ppu00360)

    - phhB: PP_4491 | Q88EH2 | Pterin-4-alpha-carbinolamine dehydratase (PHS) (EC
    4.2.1.96) (4-alpha-hydroxy-tetrahydropterin dehydratase) (Pterin carbinolamine
    dehydratase) (PCD) (EC 4.2.1.96; primary bucket kegg:ppu00790)

    - moaA: PP_4597 | Q88E69 | GTP 3'',8-cyclase (EC 4.1.99.22) (Molybdenum cofactor
    biosynthesis protein A) (EC 4.1.99.22; primary bucket kegg:ppu04122)

    - moaB-II: PP_4600 | Q88E67 | Molybdenum cofactor biosynthesis protein B (primary
    bucket kegg:ppu04122)

    - folM: PP_4632 | Q88E36 | Dihydromonapterin reductase (EC 1.5.1.3) (EC 1.5.1.50)
    (Dihydrofolate reductase) (EC 1.5.1.3; 1.5.1.50; primary bucket kegg:ppu00670)

    - folK: PP_4698 | Q88DX0 | 2-amino-4-hydroxy-6-hydroxymethyldihydropteridine pyrophosphokinase
    (EC 2.7.6.3) (6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase) (7,8-dihydro-6-hydroxymethylpterin-pyrophosphokinase)
    (EC 2.7.6.3; primary bucket kegg:ppu00790)

    - folP: PP_4717 | Q88DV2 | Dihydropteroate synthase (DHPS) (EC 2.5.1.15) (Dihydropteroate
    pyrophosphorylase) (EC 2.5.1.15; primary bucket kegg:ppu00790)

    - folA: PP_5132 | Q88CP8 | Dihydrofolate reductase (EC 1.5.1.3) (EC 1.5.1.3; primary
    bucket kegg:ppu04981)'
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
  path: PSEPK__molybdenum_cofactor_biosynthesis__ppu00790-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__molybdenum_cofactor_biosynthesis__ppu00790-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Prokaryotic molybdenum cofactor biosynthesis from GTP to Mo-molybdopterin and optional dinucleotide variants in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00790
- Resolved ID: ppu00790
- Resolved name: Folate biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00790 with 19 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 32

- folB: PP_0392 | Q88QU4 | 7,8-dihydroneopterin aldolase (EC 4.1.2.25) (EC 4.1.2.25; primary bucket kegg:ppu00790)
- PP_0393: PP_0393 | Q88QU3 | 2-amino-4-hydroxy-6-hydroxymethyldihydropteridine diphosphokinase (EC 2.7.6.3) (EC 2.7.6.3; primary bucket kegg:ppu00790)
- ribAB-I: PP_0516 | Q88QH7 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- ribA: PP_0522 | Q88QH1 | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II) (EC 3.5.4.25; primary bucket kegg:ppu00740)
- queE: PP_1225 | Q88NI4 | 7-carboxy-7-deazaguanine synthase (CDG synthase) (EC 4.3.99.3) (Queuosine biosynthesis protein QueE) (EC 4.3.99.3; primary bucket kegg:ppu00790)
- queC: PP_1226 | Q88NI3 | 7-cyano-7-deazaguanine synthase (EC 6.3.4.20) (7-cyano-7-carbaguanine synthase) (PreQ(0) synthase) (Queuosine biosynthesis protein QueC) (EC 6.3.4.20; primary bucket kegg:ppu00790)
- moaC: PP_1292 | Q88NC0 | Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17) (Molybdenum cofactor biosynthesis protein C) (EC 4.6.1.17; primary bucket kegg:ppu04122)
- moaE: PP_1294 | Q88NB8 | Molybdopterin synthase catalytic subunit (EC 2.8.1.12) (MPT synthase subunit 2) (Molybdenum cofactor biosynthesis protein E) (Molybdopterin-converting factor large subunit) (Molybdopterin-converting factor subunit 2) (EC 2.8.1.12; primary bucket kegg:ppu04122)
- folE1: PP_1823 | Q88LV4 | GTP cyclohydrolase 1 1 (EC 3.5.4.16) (GTP cyclohydrolase I 1) (GTP-CH-I 1) (EC 3.5.4.16; primary bucket kegg:ppu00790)
- pabC: PP_1917 | Q88LL3 | Aminodeoxychorismate lyase (EC 4.1.3.38) (EC 4.1.3.38; primary bucket kegg:ppu00790)
- PP_1969: PP_1969 | Q88LG4 | Molybdenum cofactor biosynthesis protein A (primary bucket kegg:ppu04122)
- folC: PP_1997 | Q88LD8 | Dihydrofolate synthase/folylpolyglutamate synthase (EC 6.3.2.12) (EC 6.3.2.17) (Folylpoly-gamma-glutamate synthetase-dihydrofolate synthetase) (Folylpolyglutamate synthetase) (Tetrahydrofolylpolyglutamate synthase) (EC 6.3.2.12; 6.3.2.17; primary bucket kegg:ppu00790)
- moaB-I: PP_2122 | Q88L15 | Molybdenum cofactor biosynthesis protein B (primary bucket kegg:ppu04122)
- moeA: PP_2123 | Q88L14 | Molybdopterin molybdenumtransferase (EC 2.10.1.1) (EC 2.10.1.1; primary bucket kegg:ppu00790)
- queF: PP_2160 | Q88KX9 | NADPH-dependent 7-cyano-7-deazaguanine reductase (EC 1.7.1.13) (7-cyano-7-carbaguanine reductase) (NADPH-dependent nitrile oxidoreductase) (PreQ(0) reductase) (EC 1.7.1.13; primary bucket kegg:ppu00790)
- pabB: PP_2329 | Q88KG1 | aminodeoxychorismate synthase (EC 2.6.1.85) (EC 2.6.1.85; primary bucket kegg:ppu00790)
- queD: PP_2341 | Q88KE9 | 6-carboxy-5,6,7,8-tetrahydropterin synthase (EC 4.-.-.-) (EC 4.-.-.-; primary bucket kegg:ppu00790)
- PP_2482: PP_2482 | Q88K11 | Molybdenum cofactor biosynthesis protein A (primary bucket kegg:ppu04122)
- PP_2483: PP_2483 | Q88K10 | MobA-like NTP transferase domain-containing protein (primary bucket kegg:ppu00790)
- folE2__Q88JY1: PP_2512 | Q88JY1 | GTP cyclohydrolase 1 2 (EC 3.5.4.16) (GTP cyclohydrolase I 2) (GTP-CH-I 2) (EC 3.5.4.16; primary bucket kegg:ppu00790)
- folE2__Q88HM9: PP_3324 | Q88HM9 | GTP cyclohydrolase FolE2 (EC 3.5.4.16) (EC 3.5.4.16; primary bucket kegg:ppu00790)
- mobA: PP_3457 | Q88HA3 | Molybdenum cofactor guanylyltransferase (MoCo guanylyltransferase) (EC 2.7.7.77) (GTP:molybdopterin guanylyltransferase) (Mo-MPT guanylyltransferase) (Molybdopterin guanylyltransferase) (Molybdopterin-guanine dinucleotide synthase) (MGD synthase) (EC 2.7.7.77; primary bucket kegg:ppu00790)
- ribAB-II: PP_3813 | Q88GB1 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- PP_4230: PP_4230 | Q88F68 | MobA-like NTP transferase domain-containing protein (primary bucket kegg:ppu00790)
- phhA: PP_4490 | Q88EH3 | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase) (EC 1.14.16.1; primary bucket kegg:ppu00360)
- phhB: PP_4491 | Q88EH2 | Pterin-4-alpha-carbinolamine dehydratase (PHS) (EC 4.2.1.96) (4-alpha-hydroxy-tetrahydropterin dehydratase) (Pterin carbinolamine dehydratase) (PCD) (EC 4.2.1.96; primary bucket kegg:ppu00790)
- moaA: PP_4597 | Q88E69 | GTP 3',8-cyclase (EC 4.1.99.22) (Molybdenum cofactor biosynthesis protein A) (EC 4.1.99.22; primary bucket kegg:ppu04122)
- moaB-II: PP_4600 | Q88E67 | Molybdenum cofactor biosynthesis protein B (primary bucket kegg:ppu04122)
- folM: PP_4632 | Q88E36 | Dihydromonapterin reductase (EC 1.5.1.3) (EC 1.5.1.50) (Dihydrofolate reductase) (EC 1.5.1.3; 1.5.1.50; primary bucket kegg:ppu00670)
- folK: PP_4698 | Q88DX0 | 2-amino-4-hydroxy-6-hydroxymethyldihydropteridine pyrophosphokinase (EC 2.7.6.3) (6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase) (7,8-dihydro-6-hydroxymethylpterin-pyrophosphokinase) (EC 2.7.6.3; primary bucket kegg:ppu00790)
- folP: PP_4717 | Q88DV2 | Dihydropteroate synthase (DHPS) (EC 2.5.1.15) (Dihydropteroate pyrophosphorylase) (EC 2.5.1.15; primary bucket kegg:ppu00790)
- folA: PP_5132 | Q88CP8 | Dihydrofolate reductase (EC 1.5.1.3) (EC 1.5.1.3; primary bucket kegg:ppu04981)

## Generic Module Context

### Working Scope

A reusable prokaryotic module for molybdenum cofactor biosynthesis constructs the pyranopterin dithiolene ligand from GTP, loads it with molybdenum, and may append a nucleotide to produce a client-class-specific cofactor variant. MoaA first performs radical-SAM cyclization of GTP and MoaC rearranges the cyclic intermediate to cyclic pyranopterin monophosphate (cPMP). Molybdopterin synthase then inserts two sulfurs: MoeB activates the small MoaD sulfur carrier, and the MoaD-MoaE synthase converts cPMP to molybdopterin (MPT). Across prokaryotic realizations, MPT is adenylylated by a separate bacterial MogA or by a catalytically competent prokaryotic MoaB lineage, and MoeA then inserts molybdate to form Mo-MPT. Some realizations stop at Mo-MPT, whereas others use MobA to make MGD or MocA to make MCD. The module excludes upstream sulfur supply, molybdate transport, terminal cofactor sulfuration, cofactor insertion into client apoenzymes, mature molybdoenzyme reactions, pathway regulation, eukaryotic MOCS/CNX/GPHN fusion organization, and human disease.

### Provisional Biological Outline

- Prokaryotic molybdenum cofactor biosynthesis
  - 1. cyclic pyranopterin monophosphate formation
  - Cyclic pyranopterin monophosphate formation
    - 1. radical-SAM GTP cyclization
    - MoaA GTP cyclization
      - MoaA GTP 3',8'-cyclase (molecular player: PSEPK canonical MoaA; activity or role: GTP 3',8'-cyclase activity)
    - 2. cyclic intermediate rearrangement to cPMP
    - MoaC cPMP synthesis
      - MoaC cyclic pyranopterin monophosphate synthase (molecular player: bacterial MoaC cPMP synthase family; activity or role: cyclic pyranopterin monophosphate synthase activity)
  - 2. sulfur-carrier activation and molybdopterin synthesis
  - Sulfur-carrier activation and MPT formation
    - 1. MoaD sulfur-carrier activation
    - MoeB-dependent MoaD activation
      - MoeB molybdopterin-synthase sulfur-carrier adenylyltransferase (molecular player: bacterial MoeB molybdopterin-synthase sulfur-carrier adenylyltransferase family; activity or role: molybdopterin-synthase adenylyltransferase activity)
      - MoaD molybdopterin-synthase sulfur carrier (molecular player: bacterial MoaD molybdopterin-synthase sulfur-carrier family)
    - 2. sulfur insertion into cPMP
    - MoaD-MoaE molybdopterin synthesis
      - MoaD2-MoaE2 molybdopterin synthase complex (molecular player: prokaryotic MoaD2-MoaE2 molybdopterin synthase complex; activity or role: molybdopterin synthase activity)
  - 3. MPT adenylylation and molybdate insertion
  - Mo-molybdopterin formation
    - 1. MPT adenylylation
    - Molybdopterin adenylylation
      - Alternative versions by prokaryotic enzyme lineage: MPT adenylyltransferase implementations
        - Separate MogA adenylyltransferase
          - MogA molybdopterin adenylyltransferase (molecular player: bacterial MogA molybdopterin adenylyltransferase family; activity or role: molybdopterin adenylyltransferase activity)
        - Catalytically competent prokaryotic MoaB adenylyltransferase
          - Catalytically competent prokaryotic MoaB molybdopterin adenylyltransferase (molecular player: Pyrococcus furiosus MoaB; activity or role: molybdopterin adenylyltransferase activity)
    - 2. molybdate insertion into adenylyl-MPT
    - Molybdopterin molybdotransfer
      - MoeA molybdopterin molybdotransferase (molecular player: PSEPK MoeA; activity or role: molybdopterin molybdotransferase activity)
  - 4. optional nucleotide maturation of Mo-MPT
  - Optional Mo-MPT nucleotide maturation
    - Alternative versions by appended nucleotide: Mo-MPT dinucleotide variants
      - MGD formation by MobA
        - MobA molybdenum cofactor guanylyltransferase (molecular player: bacterial MobA molybdenum cofactor guanylyltransferase family; activity or role: molybdenum cofactor guanylyltransferase activity)
      - MCD formation by MocA
        - MocA molybdenum cofactor cytidylyltransferase (molecular player: bacterial MocA molybdenum cofactor cytidylyltransferase family; activity or role: molybdenum cofactor cytidylyltransferase activity)

### Known Relationships Among Steps

- Cyclic pyranopterin monophosphate formation feeds into Sulfur-carrier activation and MPT formation: cPMP is the pterin substrate for sulfur insertion by molybdopterin synthase.
- Sulfur-carrier activation and MPT formation feeds into Mo-molybdopterin formation: MPT is activated and loaded with molybdate to form Mo-MPT.
- Mo-molybdopterin formation feeds into Optional Mo-MPT nucleotide maturation: Mo-MPT may be retained directly or converted to MGD and/or MCD.
- MoaA GTP cyclization feeds into MoaC cPMP synthesis: The cyclic GTP product of MoaA is the substrate for MoaC.
- MoeB-dependent MoaD activation precedes MoaD-MoaE molybdopterin synthesis: Activated MoaD is sulfur-loaded by an external sulfur-donor system before supplying the MoaE reaction.
- Molybdopterin adenylylation feeds into Molybdopterin molybdotransfer: Adenylyl-MPT produced by the selected activation variant is the substrate for molybdate insertion.

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

# Species-Aware Review: Prokaryotic Molybdenum Cofactor (Moco) Biosynthesis in *Pseudomonas putida* KT2440

**Module:** GTP → cyclic pyranopterin monophosphate (cPMP) → molybdopterin (MPT) → Mo‑MPT, with optional MGD/MCD dinucleotide variants
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI 160488; proteome UP000000556)
**Assigned local bucket:** kegg:ppu00790 ("Folate biosynthesis") — *see boundary caveat below*
**Scope of this review:** module satisfiability + gene-annotation curation, not a generic pathway essay.

---

## 1. Executive summary

*P. putida* KT2440 **encodes a complete, satisfiable molybdenum cofactor biosynthesis module** from GTP to Mo‑MPT, and it supports **both** optional dinucleotide branches (Mo‑MGD and Mo‑MCD). Every mechanistic step of the generic module maps to at least one credible KT2440 locus with UniProt/InterPro support, and the MCD branch is backed by **direct functional evidence** in the target strain (heterologous Mo‑MCD molybdoenzymes mature to catalytically competent form in KT2440; PMID 12730200).

The main issues are **curation/metadata artifacts, not biological gaps**:

1. **Two essential enzymes are missing from the candidate list** — `moaD` (PP_1293) and `moeB` (PP_0735) — because they partition to the KEGG sulfur‑relay map (ppu04122) instead of the folate bucket used to build the list. They are present in the genome and must be added.
2. **No dedicated `mogA`.** MPT adenylylation is supplied by the **MoaB paralog lineage** (`moaB‑I` PP_2122 / `moaB‑II` PP_4600), the lineage‑specific alternative that the generic module explicitly permits.
3. **Paralog ambiguity / likely over‑propagation.** Three "MoaA" and three "MobA‑like/MoaB" paralogs exist; InterPro signatures cleanly separate the canonical enzyme from accessory paralogs.
4. **The assigned bucket ppu00790 is the wrong boundary** for this module; the true Moco genes live in ppu04122 + `moeA`/`mobA`.

**Bottom line for curation:** mark the core module **covered**; add MoaD/MoeB; mark MPT‑adenylylation **covered‑by‑alternative (MoaB)**; mark MCD **candidate_uncertain→covered** pending a `mocA` naming decision; exclude the folate/riboflavin/queuosine genes from this module.

---

## 2. Target‑organism pathway definition

**Included process (this module):** construction of the pyranopterin dithiolene ligand from GTP, its dithiolene sulfuration to molybdopterin, molybdate insertion to Mo‑MPT, and optional appending of GMP (→ MGD) or CMP (→ MCD).

**Explicitly excluded (kept as neighboring processes):**
- **Molybdate uptake** — `modABC` (PP_2489‑type; UniProt `modA` Q88G97, `modB` Q88G96, `modC` Q88G95) and regulator `modR` (Q88QX4). Transport, not synthesis.
- **Terminal cofactor sulfuration / apoenzyme insertion chaperones** — e.g. XdhC‑family accessory factors (PP_2480 Q88K13, PP_4231 Q88F67, `xdhC` PP_4280 Q88F19), `fdhD` sulfur carrier (PP_0257 Q88R77). These load/insert the finished cofactor into client enzymes.
- **Mature molybdoenzyme reactions** — xanthine dehydrogenase (`xdhAB` PP_4279/…), `paoC` (Q88HP3), nicotinate dehydrogenase (`nicB` Q88FX8), assimilatory nitrate/sulfite reductase (Q88M71), formate dehydrogenases, MsrP (Q88DZ2), isoquinoline oxidoreductase β‑subunits.

**Database naming / boundary caveats:**
- The genuine Moco genes carry **KEGG map ppu04122 ("Sulfur relay system")** as primary bucket (`moaA, moaB‑I/II, moaC, moaE, moaD, moeB` + `moaA` paralogs), *not* the assigned **ppu00790 ("Folate biosynthesis")**. Only the maturation enzymes `moeA` and `mobA` and the MobA‑like paralogs sit in ppu00790.
- KEGG also groups Moco under **map00790 (Folate)** and **module M00880 (Molybdenum cofactor biosynthesis)**; MetaCyc PWY‑5963/PWY‑6823 are the corresponding reference pathways. The four GTP‑consuming pterin/deazaguanine pathways (folate, riboflavin, queuosine, Moco) co‑occur in the candidate list **only because they share GTP as precursor** — they are separate modules and should stay separate.

---

## 3. Expected step model (generic module → KT2440 realization)

| Step | Generic player | KT2440 gene(s) | Status |
|---|---|---|---|
| 1a. Radical‑SAM GTP 3′,8‑cyclization | MoaA | **`moaA` PP_4597** (Q88E69, EC 4.1.99.22) | covered |
| 1b. cPMP synthesis | MoaC | **`moaC` PP_1292** (Q88NC0, EC 4.6.1.17) | covered |
| 2a. MoaD adenylylation (activation) | MoeB | **`moeB` PP_0735** (Q88PW3, EC 2.7.7.80) | covered *(missing from candidate list)* |
| 2b. Sulfur carrier | MoaD | **`moaD` PP_1293** (Q88NB9) | covered *(missing from candidate list)* |
| 2c. MPT synthesis | MoaD₂‑MoaE₂ synthase | **`moaE` PP_1294** (Q88NB8, EC 2.8.1.12) + MoaD | covered |
| 3a. MPT adenylylation | MogA **or** MoaB | **`moaB‑I` PP_2122 / `moaB‑II` PP_4600** (no MogA present) | covered‑by‑alternative (MoaB) |
| 3b. Molybdate insertion → Mo‑MPT | MoeA | **`moeA` PP_2123** (Q88L14, EC 2.10.1.1) | covered |
| 4a. Mo‑MGD (optional) | MobA | **`mobA` PP_3457** (Q88HA3, EC 2.7.7.77) | covered |
| 4b. Mo‑MCD (optional) | MocA | **PP_2483** (Q88K10) / **PP_4230** (Q88F68), MobA‑like | candidate_uncertain (functional evidence supports presence) |

Gene order confirms functional clustering: `moaC‑moaD‑moaE` form a mini‑operon (PP_1292‑1294); `moaB‑I`–`moeA` are adjacent (PP_2122‑2123); `moaA`–`moaB‑II` are near‑adjacent (PP_4597/PP_4600). `moeB` is standalone (PP_0735).

---

## 4. Candidate genes and evidence

**High‑confidence core enzymes (EC‑level UniProt annotation; treat as covered):**
- **`moaA` PP_4597 (Q88E69)** — GTP 3′,8‑cyclase, EC 4.1.99.22. Radical‑SAM (PF04055) + MoaA C‑term (PF06463) + **MoaA‑specific IPR013483**. The canonical, housekeeping MoaA.
- **`moaC` PP_1292 (Q88NC0)** — cPMP synthase, EC 4.6.1.17. Unambiguous.
- **`moaD` PP_1293 (Q88NB9)** — MPT‑synthase sulfur carrier; ThiS/MoaD fold (PF02597, MoaD‑specific IPR010038). *Absent from candidate list.*
- **`moaE` PP_1294 (Q88NB8)** — MPT synthase catalytic subunit, EC 2.8.1.12.
- **`moeB` PP_0735 (Q88PW3)** — MPT‑synthase adenylyltransferase, EC 2.7.7.80; UniProt function: "adenylation by ATP of the C‑terminal glycine of MoaD." ThiF/MoeB (PF00899). *Absent from candidate list.*
- **`moeA` PP_2123 (Q88L14)** — MPT molybdotransferase, EC 2.10.1.1.
- **`mobA` PP_3457 (Q88HA3)** — Mo cofactor guanylyltransferase, EC 2.7.7.77; **MGD‑specific IPR013482**. Canonical MGD synthase.

**MoaB paralogs (MPT‑adenylylation / MogA surrogate):**
- **`moaB‑I` PP_2122 (Q88L15)** and **`moaB‑II` PP_4600 (Q88E67)** — MogA/MoaB MoCF_biosynth domain (PF00994, IPR001453). In many bacteria and archaea a catalytically competent MoaB performs the MogA (MPT‑adenylyltransferase) reaction; genomic adjacency to `moeA` and `moaA` respectively supports functional partnership. Evidence type: **homology + operon context** (no direct KT2440 assay).

**MobA‑like paralogs (MCD/MocA candidates):**
- **PP_2483 (Q88K10)** and **PP_4230 (Q88F68)** — generic MobA‑like NTP‑transferase (PF12804/IPR025877) **lacking** the MobA/MGD signature IPR013482, the architecture expected for **MocA** cytidylyltransferases. PP_2483 sits in a Mo‑hydroxylase maturation island (Ior β PP_2478, XdhC PP_2480, MoaA‑paralog PP_2482); PP_4230 is near an XdhC/`xdhBC` cluster. Evidence type: **domain architecture + genomic context**, plus strain‑level functional support (§ below).
- **Quantitative caveat (this study):** global % identity to *E. coli* references cannot discriminate MGD from MCD here. `mobA` PP_3457 is clearly MobA/MGD (39.8% to *E. coli* MobA P32173 vs 32.5% to MocA Q46810), but PP_2483 (35.6% MobA / 33.9% MocA) and PP_4230 (34.0% MobA / 35.6% MocA) are essentially equidistant — consistent with the fact that *E. coli* MobA and MocA share only **36.5%** identity with each other. **Conclusion: sequence identity alone does not assign MGD vs MCD** for the two paralogs; genomic context is the better discriminator and a CTP‑vs‑GTP substrate assay is the decisive experiment. Both remain MocA candidates (PP_2483 favored on context, but not by sequence).

**MoaA paralogs (likely over‑propagation):**
- **PP_1969 (Q88LG4)** and **PP_2482 (Q88K11)** — radical‑SAM (PF04055/PF06463) but **lacking MoaA‑specific IPR013483** and any EC number. Likely non‑canonical radical‑SAM enzymes over‑labeled "MoaA."

**Direct target‑strain functional evidence (MCD branch):**
- Quinaldine 4‑oxidase Qox (Mo‑MCD enzyme) was *"synthesized in a catalytically fully competent form by a heterologous host, P. putida KT2440 pKP1"* (**PMID 12730200**) → KT2440 has a working Mo‑MCD maturation apparatus.
- Caveats/nuance: heterologous Qor (**PMID 12654012**) was Mo‑deficient and Ior (**PMID 12023088**) inactive in KT2440, indicating **client‑specific insertion/chaperone requirements** downstream of Moco synthesis — an *apoenzyme‑loading* limitation, outside this module's scope. A 2026 study again uses KT2440 to produce a molybdenum‑containing xanthine oxidase where the accessory **XodC** aids maturation (**PMID 41933999**).

**Not part of this module but present (neighbors):** `modABC`/`modR` (molybdate transport), XdhC‑family and `fdhD` (cofactor insertion/sulfur handling), and numerous molybdoenzymes — all correctly excluded.

---

## 5. Gaps, ambiguities, and likely over‑annotations

- **Metadata gap (not biological):** `moaD` (PP_1293) and `moeB` (PP_0735) are genuine, essential module members omitted from the candidate list due to KEGG bucket partitioning (ppu04122 vs ppu00790). **Action: add both.**
- **No `mogA` gene** in UP000000556 (searched by gene name and protein name). The MPT‑adenylylation step is **covered by the MoaB alternative**, not a gap. Do **not** mark this step a gap for lack of MogA.
- **`mocA` naming gap:** MCD is made by MobA‑like paralogs (PP_2483 best candidate) that are not literally named `mocA`. Functionally supported but formally **candidate_uncertain**.
- **MoaA over‑propagation:** PP_1969 and PP_2482 are non‑canonical radical‑SAM paralogs labeled "MoaA"; only PP_4597 is the canonical cyclase. Risk of double‑counting step 1.
- **Broad/loose EC & domain mappings:** the MobA‑like PF12804 domain is shared by MobA (MGD), MocA (MCD), and other NTP transferases — protein‑name "MobA‑like NTP transferase domain‑containing protein" is intentionally noncommittal and should not be read as MGD.
- **Boundary error in the assigned bucket:** ppu00790 (Folate) is not the Moco pathway; the module should be curated against ppu04122 + `moeA`/`mobA`.

---

## 6. Module and GO‑curation recommendations

**Per‑step calls:**
- cPMP formation (MoaA, MoaC): **covered** — PP_4597, PP_1292.
- Sulfur‑carrier activation + MPT synthesis (MoeB, MoaD, MoaE): **covered** — PP_0735, PP_1293, PP_1294 (**add PP_0735 & PP_1293 to the module gene set**).
- MPT adenylylation: **covered‑by‑alternative (MoaB lineage)**, PP_2122/PP_4600; annotate as "MogA function fulfilled by MoaB paralog." Not a gap.
- Molybdate insertion (MoeA): **covered** — PP_2123.
- MGD (MobA): **covered** — PP_3457.
- MCD (MocA): **candidate_uncertain** — PP_2483 (primary) / PP_4230; promote for `mocA` assignment. Strain functional evidence argues for eventual **covered**.
- Overall module: **satisfiable / covered** in PSEPK.

**Module‑document / boundary:**
- **module_needs_revision (metadata):** update the candidate‑gene provenance so Moco members are gathered from ppu04122 + `moeA`/`mobA`, not the folate bucket. Exclude folate (`folB/E/C/K/P/A/M`, `pab`, `phh`), riboflavin (`rib`), and queuosine (`que`) genes from the Moco module.
- The generic module boundaries are **appropriate** for this organism; only the *local bucket mapping* is wrong.

**GO‑curation:**
- Assign/confirm: PP_4597 GO:0061799 (cyclic pyranopterin monophosphate synthase / GTP 3′,8‑cyclase GO:0061798), PP_1292 GO:0061799, PP_0735 GO:0008641, PP_1293/PP_1294 GO:0030366 (molybdopterin synthase), PP_2123 GO:0061604 (molybdopterin molybdotransferase), PP_3457 GO:0061603 (Mo cofactor guanylyltransferase).
- **Likely GO/term request:** a **MocA / Mo cofactor cytidylyltransferase (GO:0061602)** assignment for PP_2483 (and possibly PP_4230). Consider a MoaB "molybdopterin adenylyltransferase" functional annotation (GO:0061598) for PP_2122/PP_4600 to document the MogA‑surrogate role.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0735 `moeB`** — essential, missing from candidate list; confirm and add.
2. **PP_1293 `moaD`** — essential sulfur carrier, missing from candidate list; confirm and add.
3. **PP_2483 (Q88K10)** — primary MocA/MCD candidate; resolve MGD vs MCD assignment and gene naming.
4. **PP_4230 (Q88F68)** — secondary MobA‑like/MocA candidate; disambiguate from PP_2483.
5. **PP_2122 / PP_4600 `moaB‑I/II`** — confirm MPT‑adenylyltransferase (MogA‑surrogate) capability; decide the covered‑by‑alternative call.
6. **PP_1969 & PP_2482 ("MoaA")** — adjudicate over‑propagation; likely re‑annotate as non‑canonical radical‑SAM paralogs.

---

## 8. Key references

- **PMID 12730200** — Parschat et al. 2003. Qox (Mo‑MCD quinaldine 4‑oxidase) *"synthesized in a catalytically fully competent form by a heterologous host, P. putida KT2440 pKP1."* Direct KT2440 evidence for functional Mo‑MCD maturation.
- **PMID 12654012** — Frerichs‑Deeken et al. 2003. Qor (Mo‑MCD) in KT2440 pUF1 is Mo‑deficient — client‑specific insertion limitation (outside module scope).
- **PMID 12023088** — Israel et al. 2002. Ior (Mo‑MCD) inactive in KT2440 pIL1; accessory maturation genes required — apoenzyme loading, not Moco synthesis.
- **PMID 41933999** — Guo et al. 2026. Molybdenum‑containing xanthine oxidase produced in KT2440; XodC accessory role in maturation.
- **PMID 8798497** — Bläse et al. 1996. Molybdopterin‑cytosine‑dinucleotide (MCD) cofactor in quinoline 2‑oxidoreductase, functional in recombinant KT2440.
- UniProt proteome **UP000000556** (all locus/EC/InterPro annotations cited above); KEGG maps **ppu04122** (sulfur relay), **ppu00790** (folate), module **M00880**; InterPro **IPR013483** (MoaA), **IPR013482** (MobA/MGD).

---

### Uncertainty & species‑transfer notes
- Core enzyme presence/EC assignments: **strong** (UniProt/InterPro, target proteome; homology‑based but high‑confidence).
- MCD‑branch functionality: **direct KT2440 experimental** evidence (heterologous‑host maturation).
- MPT‑adenylylation via MoaB and MocA identity of PP_2483/PP_4230: **inferred** from domain architecture, genomic context, and functional maturation data — no direct KT2440 enzymatic assay of these specific genes. These are the key open questions for expert review.


## Artifacts

- [OpenScientist final report](PSEPK__molybdenum_cofactor_biosynthesis__ppu00790-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__molybdenum_cofactor_biosynthesis__ppu00790-deep-research-openscientist_artifacts/final_report.pdf)