---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T11:25:15.233194'
end_time: '2026-09-01T11:44:51.975289'
duration_seconds: 1176.74
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
    max_iterations: 5
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

# Species-Aware Curation Review: Prokaryotic Molybdenum Cofactor (Moco) Biosynthesis in *Pseudomonas putida* KT2440

**Module scope:** GTP → cyclic pyranopterin monophosphate (cPMP) → molybdopterin (MPT) → Mo-MPT, plus the optional dinucleotide variants MGD and MCD.
**Target:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556).
**Seeding bucket:** KEGG `ppu00790` ("Folate biosynthesis"); KEGG module `ppu_M00880` ("Molybdenum cofactor biosynthesis, GTP => molybdenum cofactor").

---

## 1. Executive summary

The generic prokaryotic Moco module is **fully satisfiable** in *P. putida* KT2440. Every catalytic step from GTP to Mo-MPT, and **both** optional dinucleotide branches (MGD via MobA and MCD via MocA), is encoded. Mapping to the authoritative resources (UniProt UP000000556 + KEGG orthology) gives a complete, one-gene-per-step assignment with several curation-relevant refinements:

- **Two steps that look absent in the seeded candidate list are in fact covered:** the sulfur-relay genes **moeB (PP_0735)** and **moaD (PP_1293)** were omitted from the 32-gene candidate set because they are bucketed under KEGG `ppu04122` (sulfur relay), not `ppu00790`.
- **No dedicated MogA exists in KT2440.** The MogA-type MPT-adenylyltransferase step (EC 2.7.7.75) is carried by the **MoaB lineage** (PP_2122, PP_4600) — the "catalytically competent prokaryotic MoaB" alternative already anticipated by the module. This is the only step with residual mechanistic uncertainty (`candidate_uncertain`).
- **Two genes labelled generically as "MobA-like NTP transferase" (PP_2483, PP_4230) are specifically MocA** cytidylyltransferases (K07141, EC 2.7.7.76) — the MCD branch. KT2440 is a well-documented heterologous host that matures **MCD-form** molybdenum hydroxylases, giving direct target-strain support.
- **The seeding bucket is contaminated:** of 32 candidates, only ~11 are Moco genes; the rest are folate, queuosine (7-deazapurine), riboflavin and biopterin genes that share pterin/GTP chemistry but belong to neighbouring pathways.
- KT2440 shows **paralog expansion** (3× MoaA, 2× MoaB, 2× MocA) organized as a housekeeping core plus **molybdoenzyme-adjacent gene islands** that supply client-specific cofactor tailoring.

**Bottom line for curation:** mark all core steps `covered`; mark the MPT-adenylylation step `covered` with a `candidate_uncertain` mechanistic flag (MoaB-for-MogA); no steps are `gap` or `not_expected_in_target_taxon`; the generic module boundaries are correct but the *ppu00790 seeding bucket* is too broad and needs pruning.

---

## 2. Target-organism pathway definition

**Included process (this module):** the biosynthesis of the pyranopterin dithiolene ligand from GTP and its loading with molybdenum, i.e.

1. radical-SAM cyclization of GTP to 3′,8-cyclo-7,8-dihydro-GTP (MoaA);
2. rearrangement to cPMP (MoaC);
3. activation of the MoaD sulfur carrier (MoeB) and double sulfur insertion into cPMP to give MPT (MoaD–MoaE synthase);
4. adenylylation of MPT (MogA-type activity) and molybdate insertion to give Mo-MPT (MoeA);
5. optional attachment of GMP → MGD (MobA) or CMP → MCD (MocA).

**Explicitly excluded** (and must be kept in separate modules): molybdate uptake (**modABC** PP_3828–3830; regulator **modR** PP_0360), upstream sulfur mobilisation, terminal cofactor sulfuration (e.g. **fdhD**-type sulfurtransferase PP_0257 for formate dehydrogenase), cofactor insertion into apo-enzymes (XdhC-family chaperones PP_2480, PP_4231, PP_4280, xdhC PP_4279–4280 region), the mature molybdoenzyme reactions themselves (nitrate reductase PP_1703, formate dehydrogenases fdoG PP_0489/PP_2185, nicotinate dehydrogenase nicB PP_3948, xanthine dehydrogenase PP_4234/PP_4279, isoquinoline/quinoline oxidoreductases PP_2478/PP_3622, MsrP PP_4676), and pathway regulation.

**Neighbouring pathways to keep separate (critical here):** KEGG **map00790 is an umbrella "folate/pterin" map**, not folate-specific. It bundles four biochemically distinct GTP/pterin branches that must not be merged into the Moco module:
- **Folate/tetrahydrofolate:** folE1/E2 (GTP cyclohydrolase I), folB, folK, folP, folC, folA, folM, pabB, pabC, PP_0393 → map00790/map00670/map04981.
- **7-deazapurine / queuosine:** queC, queD, queE, queF → 7-deazaguanine branch of map00790.
- **Riboflavin:** ribA, ribAB-I, ribAB-II (GTP cyclohydrolase II) → map00740.
- **Biopterin / pterin regeneration:** phhA (Phe hydroxylase), phhB (pterin-4α-carbinolamine dehydratase) → map00360/aromatic amino-acid metabolism.

**Database-specific names / IDs:** KEGG module **M00880**; KEGG maps map00790 (Folate biosynthesis), map01240 (Biosynthesis of cofactors), map01100 (Metabolic pathways); MetaCyc "molybdenum cofactor biosynthesis" (PWY-5963/PWY-6823); GO:0006777 (Mo-molybdopterin cofactor biosynthetic process). Common gene-name synonyms: MoaA=MoaA/moco-A; cPMP was historically called "precursor Z"; MPT = molybdopterin/pterin; MGD = MPT-guanine dinucleotide; MCD = MPT-cytosine dinucleotide.

---

## 3. Expected step model and satisfiability

KEGG module **M00880** definition: `((K03639 K03637),K20967) (K03635,K21142) (((K03831,K03638) K03750),K15376)` — i.e. (MoaA+MoaC) → MoaE synthase → (MogA/MoaB adenylyltransferase → MoeA molybdotransferase). MoaD (K03636), MoeB (K21029) and the dinucleotide transferases (K03752 MobA, K07141 MocA) are captured in the sibling sulfur-relay/dinucleotide steps.

| # | Module step | EC / KO | KT2440 gene(s) | Status |
|---|---|---|---|---|
| 1 | MoaA GTP 3′,8-cyclase (radical-SAM) | 4.1.99.22 / K03639 | **PP_4597** (canonical) + PP_1969, PP_2482 (paralogs) | **covered** (3 copies) |
| 2 | MoaC cPMP synthase | 4.6.1.17 / K03637 | **PP_1292** | **covered** |
| 3 | MoeB MoaD-adenylyltransferase (sulfur-carrier activation) | 2.7.7.80 / K21029 | **PP_0735** | **covered** (missing from candidate list) |
| 4 | MoaD sulfur carrier | – / K03636 | **PP_1293** | **covered** (missing from candidate list) |
| 5 | MoaD–MoaE molybdopterin synthase | 2.8.1.12 / K03635 | **PP_1294** (+PP_1293) | **covered** |
| 6 | MPT adenylylation (MogA-type) | 2.7.7.75 / K03638 | **PP_2122 (moaB-I), PP_4600 (moaB-II)** — no dedicated MogA | **covered / candidate_uncertain** |
| 7 | MoeA molybdotransferase | 2.10.1.1 / K03750 | **PP_2123** | **covered** |
| 8 | MobA → MGD (optional) | 2.7.7.77 / K03752 | **PP_3457** | **covered** |
| 9 | MocA → MCD (optional) | 2.7.7.76 / K07141 | **PP_2483, PP_4230** | **covered** (branch active by direct evidence; gene→MocA call orthology/context-based, moderate confidence) |

**Steps missing from metadata but present:** #3 MoeB (PP_0735) and #4 MoaD (PP_1293) — both real, both in the moaCDE operon / sulfur-relay bucket.
**Steps not expected / not applicable:** none are absent. The eukaryotic MOCS/CNX/gephyrin fusion organisation (K15376, K20967, K21142) is correctly **not_expected_in_target_taxon** (bacteria use discrete genes).

---

## 4. Candidate genes and evidence

**Genomic architecture (KEGG positions).** Two organisational tiers:
- **Housekeeping core:** `moaC-moaD-moaE` contiguous operon (PP_1292/1293/1294, overlapping start–stop codons); `moaB-I–moeA` operon (PP_2122/2123, overlapping); standalone `moeB` (PP_0735); canonical `moaA` (PP_4597) beside `moaB-II` (PP_4600) and an oxidoreductase (PP_4596); standalone `mobA` (PP_3457).
- **Molybdoenzyme gene islands:** a MoaA paralog + MocA pair (PP_2482 + PP_2483) embedded beside an isoquinoline-oxidoreductase/XDH island (PP_2478, PP_2480); a second MocA (PP_4230) contiguous with xanthine-dehydrogenase genes (PP_4231, PP_4234). This physical linkage supports **client-specific cofactor tailoring** rather than redundancy.

**High-confidence genes (direct SwissProt-level or KO evidence):**
- **PP_4597 moaA** (Q88E69, SwissProt): 4Fe-4S radical-SAM GTP 3′,8-cyclase; well-annotated. Caveat: KEGG's *GenBank product name* mislabels it "cyclic pyranopterin monophosphate synthase" — rely on KO/UniProt, not GenBank text.
- **PP_1292 moaC** (Q88NC0, SwissProt): cPMP synthase; single copy; unambiguous.
- **PP_3457 mobA** (Q88HA3, SwissProt): MGD synthase EC 2.7.7.77; single copy; unambiguous.
- **PP_0735 moeB** (Q88PW3): MoaD-adenylyltransferase EC 2.7.7.80 (K21029); high confidence.
- **PP_2123 moeA** (Q88L14): molybdotransferase EC 2.10.1.1 (K03750); high confidence.
- **PP_1294 moaE / PP_1293 moaD** (Q88NB8 / Q88NB9): MPT-synthase large/small subunits; operon context reinforces.

**Paralog-ambiguous / broad-mapping genes (curation attention):**
- **MoaA ×3 (PP_4597, PP_1969, PP_2482):** all K03639. PP_4597 is the canonical housekeeping copy; PP_1969 and PP_2482 are paralogs (PP_2482 is island-embedded). Broad GO/EC transfer risk: paralogs may be over-annotated as fully interchangeable; functional specialisation is inferred, not proven.
- **MoaB ×2 (PP_2122, PP_4600):** both K03638 / EC 2.7.7.75. **Domain evidence confirms they are bona fide MoaB, not MogA**: each carries the MoaB-specific InterPro signatures IPR012245 (MoaB) and IPR013484 ("Molybdenum cofactor biosynthesis protein B, proteobacteria") on the shared MoaB/Mog fold (PF00994). They provide the **MogA-equivalent** adenylyltransferase in the absence of a dedicated MogA. The EC 2.7.7.75 *activity* assignment is a family-level inference (precedent: catalytically competent *Pyrococcus furiosus* MoaB); which paralog is physiologically dominant is unknown → `candidate_uncertain`.
- **MocA ×2 (PP_2483, PP_4230):** both K07141 / EC 2.7.7.76 by KEGG orthology, delivered to curation as "MobA-like NTP transferase domain protein." **Important domain caveat:** InterPro shows these carry *only* the generic PF12804/IPR025877 "MobA-like NTP transferase" domain — there is **no MocA-specific InterPro/Pfam signature** in existence, and they lack the MobA-specific IPR013482 that the true MobA (PP_3457) carries. So the MocA (MCD) upgrade rests on **KEGG orthology (K07141) + genomic adjacency to MCD-molybdoenzyme clusters**, not on a domain signature. Recommendation: re-annotate to MocA as a **moderate-confidence** call (they are clearly *not* MobA and are orthologous to characterised MocA; MocA vs MobA differ by only ~22% identity and are nucleotide-specific — Neumann 2009/2011), and confirm by SSDB reciprocal-best-hit or activity assay.

**Direct target-strain evidence.** KT2440 functions as a heterologous host that assembles **catalytically fully competent MCD-containing** molybdenum hydroxylases (quinaldine 4-oxidase; quinoline/isoquinoline 2-oxidoreductases), with CMP release on acid hydrolysis confirming the MCD form (PMID 12730200, 12654012, 8798497, 12023088). This is strong, *direct* evidence that KT2440's endogenous Moco machinery reaches Mo-MPT **and** can make MCD (MocA active). One caveat from the same work: heterologous Qor in KT2440 pUF1 showed partial Mo-centre deficiency (PMID 12654012), i.e. cofactor supply can be limiting for high-level heterologous expression — a physiological, not a genetic, gap.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Not gaps (resolved):** MoeB (PP_0735) and MoaD (PP_1293) — present; only *missing from the candidate list* due to sulfur-relay bucketing.
- **Genuine mechanistic ambiguity:** the MPT-adenylylation step. No MogA; the MoaB paralogs carry EC 2.7.7.75 by family inference. Recommend `candidate_uncertain`.
- **Likely under-annotation (moderate confidence):** PP_2483 and PP_4230 as generic "MobA-like NTP transferase" — should be MocA (EC 2.7.7.76) per KEGG orthology K07141 and MCD-cluster adjacency. Note: no MocA-specific InterPro domain exists (both share only PF12804 with MobA), so this is an orthology/context call, not a domain call.
- **Domain-shared / disambiguation-by-orthology:** MoeB (PP_0735) sits in the PF00899 ThiF/MoeB/HesA superfamily shared with thiamine-biosynthesis ThiF and other E1-like adenylyltransferases; the specific MoaD-adenylyltransferase assignment relies on KO K21029 (over-propagation watch-point). Domain checks otherwise *confirm* the core calls: MoaD (PP_1293) ThiS/MoaD β-grasp sulfur carrier (PF02597/IPR044672); MoeA (PP_2123) full MoeA architecture (PF00994+PF03453+PF03454); MoaB proteins carry MoaB-specific IPR012245/IPR013484 (i.e. genuinely MoaB, hardening the MogA-absence conclusion).
- **Likely over-broad bucketing (not over-propagation of function, but pathway assignment):** the ppu00790 seeding pulled in ~21 non-Moco genes (folate, queuosine, riboflavin, biopterin). These are correctly annotated as their own enzymes but do **not** belong to the Moco module.
- **GenBank name inconsistency:** KEGG GenBank product strings are unreliable for this locus set (e.g. PP_4597 mislabelled as cPMP synthase; PP_1292 called an "accessory protein"). Curation must use KO/UniProt.
- **Paralog over-transfer risk:** treating the three MoaA / two MoaB / two MocA copies as functionally identical could over-state redundancy; the island-embedded copies may be client-specialised.

---

## 6. Module and GO-curation recommendations

| Module step | Recommended mark | Rationale |
|---|---|---|
| MoaA GTP cyclization | `covered` | PP_4597 + paralogs, SwissProt |
| MoaC cPMP synthesis | `covered` | PP_1292, SwissProt |
| MoeB MoaD activation | `covered` | PP_0735; add to module (was outside bucket) |
| MoaD sulfur carrier | `covered` | PP_1293; add to module (was outside bucket) |
| MoaD–MoaE synthase | `covered` | PP_1294 (+PP_1293) |
| MPT adenylylation (MogA/MoaB) | `covered` + `candidate_uncertain` | MoaB lineage substitutes for MogA; competence inferred |
| MoeA molybdotransfer | `covered` | PP_2123 |
| MGD (MobA) | `covered` | PP_3457, SwissProt |
| MCD (MocA) | `covered` (branch); gene call moderate-confidence | PP_2483, PP_4230 re-annotate from "MobA-like" → MocA via K07141 + MCD-cluster context (no MocA-specific domain exists) |
| Eukaryotic fusion variants | `not_expected_in_target_taxon` | bacterium uses discrete genes |

- **Module boundaries:** the *generic module* boundaries are **correct** for KT2440 (both dinucleotide branches apply). No `module_needs_revision` at the biology level. The **seeding query is the problem**: reseed from KEGG module **M00880** (or GO:0006777) rather than the ppu00790 folate map to avoid dragging in folate/queuosine/riboflavin/biopterin genes.
- **Add to module document:** MoeB (PP_0735) and MoaD (PP_1293) as explicit members of the sulfur-carrier activation step.
- **GO requests:** existing terms suffice — GO:0006777 (Mo-molybdopterin biosynthesis), GO:0061599 (molybdopterin adenylyltransferase, for the MogA/MoaB step), GO:0061602 (MoaA GTP 3′,8-cyclase), GO:0035673 (MobA), GO:0061604 (MocA / MCD synthase). No new GO term appears necessary. If a term is needed, a "MoaB-acting-as-MPT-adenylyltransferase" refinement note could help capture the MogA-less lineage.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0735 (moeB)** — sulfur-carrier activation; missing from candidate list; confirm EC 2.7.7.80.
2. **PP_1293 (moaD)** — MPT-synthase small subunit; missing from candidate list.
3. **PP_2483 and PP_4230 (MocA)** — re-annotate from "MobA-like NTP transferase" to MocA (EC 2.7.7.76); island context supports client-specific MCD synthesis.
4. **PP_2122 and PP_4600 (moaB-I/II)** — resolve which MoaB (if either) is the physiological MPT-adenylyltransferase in the absence of MogA; this is the module's only mechanistic uncertainty.
5. **PP_1969 and PP_2482 (MoaA paralogs)** — clarify whether these are housekeeping-redundant or client-specialised, and whether any is a pseudogene/divergent.

---

## 8. Key references

- Parschat et al. 2003, *J Bacteriol* — quinaldine 4-oxidase; KT2440 as host makes catalytically competent **MCD** molybdenum hydroxylase. **PMID 12730200**.
- Frerichs-Deeken et al. 2003, *Biochemistry/Eur J Biochem* — quinoline 2-oxidoreductase in KT2440; Mo-MCD form; partial Mo-centre deficiency in KT2440 host. **PMID 12654012**.
- Israel et al. 2002 — isoquinoline 1-oxidoreductase (Mo-MCD) expression in *P. putida*. **PMID 12023088**.
- Bläse et al. 1996 — quinoline 2-oxidoreductase genes; active enzyme in recombinant KT2440. **PMID 8798497**.
- Guo et al. 2026 — xanthine oxidase (molybdoenzyme) production in a KT2440 cell factory; Mo-content dependence. **PMID 41933999**.
- Neumann et al. 2009, *J Biol Chem* — **MocA** is a specific CTP:molybdopterin cytidylyltransferase for **MCD**; distinct from MobA. **PMID 19542235**.
- Neumann et al. 2011 — MobA vs MocA nucleotide-specificity determinants (MGD vs MCD). **PMID 21081498**.
- Data resources: UniProt proteome **UP000000556**; KEGG organism **ppu**, module **M00880**, orthologies K03639/K03637/K03636/K21029/K03635/K03638/K03750/K03752/K07141; InterPro/Pfam domain signatures (PF00994 MoaB/Mog; IPR012245/IPR013484 MoaB-proteobacterial; IPR013482 MobA guanylyltransferase; PF12804/IPR025877 MobA-like NTP transferase; PF00899 ThiF/MoeB; PF02597 ThiS/MoaD; PF03453/PF03454 MoeA).

---

### Uncertainty / species-transfer notes
- Step-to-gene mapping (§3) is **direct** for KT2440 (its own UniProt/KEGG annotations; several SwissProt-reviewed).
- MCD-branch activity is supported by **direct KT2440 experiments** (heterologous MCD-hydroxylase maturation).
- MGD-branch client presence (nitrate reductase, formate dehydrogenases) is inferred from the KT2440 proteome (annotation-level), not from a dedicated MGD-quantification experiment.
- The MoaB-for-MogA adenylylation assignment is a **family/homology inference** (mechanistic precedent from *P. furiosus* MoaB and *E. coli* MogA/MoaB biochemistry) — the weakest link and the top experimental question (in-vitro MPT-adenylyltransferase assay of PP_2122 vs PP_4600).


## Artifacts

- [OpenScientist final report](PSEPK__molybdenum_cofactor_biosynthesis__ppu00790-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__molybdenum_cofactor_biosynthesis__ppu00790-deep-research-openscientist_artifacts/final_report.pdf)