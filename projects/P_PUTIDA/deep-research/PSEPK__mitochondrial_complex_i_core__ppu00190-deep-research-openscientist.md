---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-10T22:59:41.655632'
end_time: '2026-08-10T23:11:22.995778'
duration_seconds: 701.34
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: "Mitochondrial respiratory Complex I core (NADH:ubiquinone oxidoreductase)\
    \ \u2014 catalytic N and Q modules; NDUFV1/NDUFV2/NDUFS1-3/NDUFS6-8/NDUFA9"
  module_summary: "Respiratory Complex I (NADH:ubiquinone oxidoreductase) is the largest\
    \ enzyme of the electron transport chain and its main entry point: it oxidises\
    \ NADH, passes the electrons through a chain of flavin and iron-sulfur cofactors\
    \ to reduce ubiquinone, and uses the energy released to pump four protons across\
    \ the inner membrane. This module covers the catalytic core of the L-shaped peripheral\
    \ (matrix) arm \u2014 the seven conserved \"core\" nuclear subunits plus the closely\
    \ associated flavoprotein subunits \u2014 organised into two functional modules.\
    \ The N-module (NADH-oxidising) holds the flavin site: NDUFV1 (51 kDa) binds FMN\
    \ and the NADH substrate, NDUFV2 (24 kDa) carries the first [2Fe-2S] cluster (N1a),\
    \ and NDUFS1 (75 kDa) provides further Fe-S clusters, forming the flavoprotein\
    \ (FP) subcomplex with the accessory NDUFS6. The Q-module (ubiquinone-reducing)\
    \ forms the wire to the quinone site: NDUFS2 (49 kDa) and NDUFS3 (30 kDa) are\
    \ cofactor-less core subunits shaping the ubiquinone cavity, NDUFS7 (PSST) coordinates\
    \ the terminal [4Fe-4S] cluster N2 that donates electrons to ubiquinone, NDUFS8\
    \ (TYKY) carries the N6a/N6b [4Fe-4S] clusters of the electron-transfer wire,\
    \ and the accessory NDUFA9 (SDR-fold, structural NADPH) stabilises the Q-module/membrane-arm\
    \ junction; NDUFS4 is an accessory subunit required for assembly and stability\
    \ of the whole peripheral arm. Inherited defects in these core subunits are among\
    \ the commonest causes of mitochondrial complex I deficiency \u2014 typically\
    \ Leigh syndrome, leukoencephalopathy, fatal infantile lactic acidosis or encephalocardiomyopathy."
  module_outline: "- Mitochondrial respiratory Complex I core (N and Q modules)\n\
    \  - 1. N-module (NADH oxidation, FMN + entry Fe-S clusters)\n  - N-module (flavoprotein\
    \ / NADH-oxidising)\n    - NDUFV1: FMN/NADH catalytic subunit (51 kDa) (molecular\
    \ player: NADH dehydrogenase flavoprotein 1 family (NDUFV1); activity or role:\
    \ NADH dehydrogenase activity)\n    - NDUFV2: N1a [2Fe-2S] subunit (24 kDa) (molecular\
    \ player: NADH dehydrogenase flavoprotein 2 family (NDUFV2); activity or role:\
    \ electron transfer activity)\n    - NDUFS1: 75 kDa Fe-S subunit (molecular player:\
    \ NADH-quinone oxidoreductase G/NDUFS1 family; activity or role: electron transfer\
    \ activity)\n    - NDUFS6: zinc-binding N-module accessory (13 kDa) (molecular\
    \ player: NDUFS6 accessory-subunit family; activity or role: structural molecule\
    \ activity)\n  - 2. Q-module (ubiquinone reduction, terminal Fe-S wire)\n  - Q-module\
    \ (ubiquinone-reducing)\n    - NDUFS2: 49 kDa Q-module core subunit (molecular\
    \ player: NADH-quinone oxidoreductase D/NDUFS2 family; activity or role: ubiquinone\
    \ binding)\n    - NDUFS3: 30 kDa Q-module core subunit (molecular player: NADH-quinone\
    \ oxidoreductase C/NDUFS3 family; activity or role: structural molecule activity)\n\
    \    - NDUFS7 (PSST): N2 [4Fe-4S] subunit (molecular player: NADH-quinone oxidoreductase\
    \ B/NDUFS7 (PSST) family; activity or role: NADH dehydrogenase (ubiquinone) activity)\n\
    \    - NDUFS8 (TYKY): N6a/N6b [4Fe-4S] subunit (molecular player: NADH-quinone\
    \ oxidoreductase I/NDUFS8 (TYKY) family; activity or role: 4 iron, 4 sulfur cluster\
    \ binding)\n    - NDUFA9: SDR-fold junction accessory (39 kDa) (molecular player:\
    \ NDUFA9 / SDR-fold accessory family; activity or role: structural molecule activity)\n\
    \  - 3. peripheral-arm assembly/stability accessory\n  - NDUFS4 accessory subunit\
    \ (peripheral-arm assembly)\n    - NDUFS4: accessory/assembly subunit (18 kDa)\
    \ (molecular player: NDUFS4 accessory-subunit family)"
  module_connections: '- N-module (flavoprotein / NADH-oxidising) feeds into Q-module
    (ubiquinone-reducing): Electrons from NADH oxidation at the FMN/N-module are relayed
    through the Fe-S wire to the Q-module N2 cluster, which reduces ubiquinone.

    - NDUFS4 accessory subunit (peripheral-arm assembly) promotes N-module (flavoprotein
    / NADH-oxidising): NDUFS4 is required for assembly and stability of the catalytic
    peripheral arm.'
  pathway_query: ppu00190
  pathway_id: ppu00190
  pathway_name: Oxidative phosphorylation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00190 with 44 primary genes; module
    area: energy_respiration_inorganic_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '54'
  candidate_genes: '- PP_0103: PP_0103 | Q88RM6 | Cytochrome c oxidase subunit 2 (EC
    7.1.1.9) (EC 7.1.1.9; primary bucket kegg:ppu00190)

    - ctaD: PP_0104 | Q88RM5 | Cytochrome c oxidase subunit 1 (EC 7.1.1.9) (EC 7.1.1.9;
    primary bucket kegg:ppu00190)

    - PP_0105: PP_0105 | Q88RM4 | Cytochrome c oxidase assembly protein CtaG (primary
    bucket kegg:ppu00190)

    - PP_0106: PP_0106 | Q88RM3 | Probable cytochrome c oxidase subunit 3 (EC 7.1.1.9)
    (Cytochrome aa3 subunit 3) (Cytochrome c oxidase polypeptide III) (EC 7.1.1.9;
    primary bucket kegg:ppu00190)

    - PP_0109: PP_0109 | Q88RM0 | Cytochrome B (primary bucket kegg:ppu00860)

    - cyoE1: PP_0110 | Q88RL9 | Protoheme IX farnesyltransferase 1 (EC 2.5.1.141)
    (Heme B farnesyltransferase 1) (Heme O synthase 1) (EC 2.5.1.141; primary bucket
    kegg:ppu00860)

    - ppa: PP_0538 | Q88QF6 | Inorganic pyrophosphatase (EC 3.6.1.1) (Pyrophosphate
    phospho-hydrolase) (PPase) (EC 3.6.1.1; primary bucket kegg:ppu00190)

    - ndh: PP_0626 | Q88Q70 | NADH dehydrogenase (EC 1.6.99.3) (EC 1.6.99.3; primary
    bucket kegg:ppu00190)

    - ppkB: PP_0712 | Q88PY6 | ADP/GDP-polyphosphate phosphotransferase (EC 2.7.4.-)
    (Polyphosphate kinase PPK2) (EC 2.7.4.-; primary bucket kegg:ppu03018)

    - cyoA: PP_0812 | Q88PN7 | Ubiquinol oxidase subunit 2 (primary bucket kegg:ppu00190)

    - cyoB: PP_0813 | Q88PN6 | Cytochrome bo(3) ubiquinol oxidase subunit 1 (EC 7.1.1.3)
    (Cytochrome o ubiquinol oxidase subunit 1) (Oxidase bo(3) subunit 1) (Ubiquinol
    oxidase polypeptide I) (Ubiquinol oxidase subunit 1) (EC 7.1.1.3; primary bucket
    kegg:ppu00190)

    - cyoC: PP_0814 | Q88PN5 | Cytochrome bo(3) ubiquinol oxidase subunit 3 (Cytochrome
    o ubiquinol oxidase subunit 3) (Oxidase bo(3) subunit 3) (Ubiquinol oxidase polypeptide
    III) (Ubiquinol oxidase subunit 3) (primary bucket kegg:ppu00190)

    - cyoD: PP_0815 | Q88PN4 | Cytochrome bo(3) ubiquinol oxidase subunit 4 (Cytochrome
    o ubiquinol oxidase subunit 4) (Oxidase bo(3) subunit 4) (Ubiquinol oxidase polypeptide
    IV) (Ubiquinol oxidase subunit 4) (primary bucket kegg:ppu00190)

    - cyoE2: PP_0816 | Q88PN3 | Protoheme IX farnesyltransferase 2 (EC 2.5.1.141)
    (Heme B farnesyltransferase 2) (Heme O synthase 2) (EC 2.5.1.141; primary bucket
    kegg:ppu00860)

    - petA: PP_1317 | Q88N95 | Ubiquinol-cytochrome c reductase iron-sulfur subunit
    (EC 7.1.1.8) (EC 7.1.1.8; primary bucket kegg:ppu04148)

    - petB: PP_1318 | Q88N94 | Cytochrome b (primary bucket kegg:ppu00190)

    - petC: PP_1319 | Q88N93 | Ubiquinol--cytochrome c reductase, cytochrome c1 (primary
    bucket kegg:ppu00190)

    - PP_2867: PP_2867 | Q88IY2 | Pyridine nucleotide-disulphide oxidoreductase family
    protein (primary bucket kegg:ppu00190)

    - nuoA: PP_4119 | Q88FH7 | NADH-quinone oxidoreductase subunit A (EC 7.1.1.-)
    (NADH dehydrogenase I subunit A) (NDH-1 subunit A) (NUO1) (EC 7.1.1.-; primary
    bucket kegg:ppu00190)

    - nuoB: PP_4120 | Q88FH6 | NADH-quinone oxidoreductase subunit B (EC 7.1.1.-)
    (NADH dehydrogenase I subunit B) (NDH-1 subunit B) (EC 7.1.1.-; primary bucket
    kegg:ppu00190)

    - nuoC: PP_4121 | Q88FH5 | NADH-quinone oxidoreductase subunit C/D (EC 7.1.1.-)
    (NADH dehydrogenase I subunit C/D) (NDH-1 subunit C/D) (EC 7.1.1.-; primary bucket
    kegg:ppu00190)

    - nuoE: PP_4122 | Q88FH4 | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase
    I subunit E) (NDH-1 subunit E) (primary bucket kegg:ppu00190)

    - nuoF: PP_4123 | Q88FH3 | NADH-quinone oxidoreductase subunit F (EC 7.1.1.-)
    (EC 7.1.1.-; primary bucket kegg:ppu00190)

    - nuoG: PP_4124 | Q88FH2 | NADH-quinone oxidoreductase subunit G (EC 7.1.1.-)
    (NADH dehydrogenase I subunit G) (NDH-1 subunit G) (EC 7.1.1.-; primary bucket
    kegg:ppu00190)

    - nuoH: PP_4125 | Q88FH1 | NADH-quinone oxidoreductase subunit H (EC 7.1.1.-)
    (NADH dehydrogenase I subunit H) (NDH-1 subunit H) (EC 7.1.1.-; primary bucket
    kegg:ppu00190)

    - nuoI: PP_4126 | Q88FH0 | NADH-quinone oxidoreductase subunit I (EC 7.1.1.-)
    (NADH dehydrogenase I subunit I) (NDH-1 subunit I) (EC 7.1.1.-; primary bucket
    kegg:ppu00190)

    - nuoJ: PP_4127 | Q88FG9 | NADH-quinone oxidoreductase subunit J (EC 7.1.1.-)
    (EC 7.1.1.-; primary bucket kegg:ppu00190)

    - nuoK: PP_4128 | Q88FG8 | NADH-quinone oxidoreductase subunit K (EC 7.1.1.-)
    (NADH dehydrogenase I subunit K) (NDH-1 subunit K) (EC 7.1.1.-; primary bucket
    kegg:ppu00190)

    - nuoL: PP_4129 | Q88FG7 | NADH-quinone oxidoreductase subunit L (NADH dehydrogenase
    I subunit L) (NDH-1 subunit L) (primary bucket kegg:ppu00190)

    - nuoM: PP_4130 | Q88FG6 | NADH-quinone oxidoreductase subunit M (NADH dehydrogenase
    I subunit M) (NDH-1 subunit M) (primary bucket kegg:ppu00190)

    - nuoN: PP_4131 | Q88FG5 | NADH-quinone oxidoreductase subunit N (EC 7.1.1.-)
    (NADH dehydrogenase I subunit N) (NDH-1 subunit N) (EC 7.1.1.-; primary bucket
    kegg:ppu00190)

    - sdhB: PP_4190 | Q88FA8 | Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1)
    (EC 1.3.5.1; primary bucket kegg:ppu00020)

    - sdhA: PP_4191 | Q88FA7 | Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1)
    (EC 1.3.5.1; primary bucket kegg:ppu00020)

    - sdhD: PP_4192 | Q88FA6 | Succinate dehydrogenase hydrophobic membrane anchor
    subunit (primary bucket kegg:ppu00020)

    - sdhC: PP_4193 | Q88FA5 | Succinate dehydrogenase cytochrome b556 subunit (primary
    bucket kegg:ppu00020)

    - ccoN-I: PP_4250 | Q88F49 | cytochrome-c oxidase (EC 7.1.1.9) (EC 7.1.1.9; primary
    bucket kegg:ppu00190)

    - ccoO-I: PP_4251 | Q88F48 | Cytochrome c oxidase subunit, cbb3-type (primary
    bucket kegg:ppu00190)

    - ccoQ-I: PP_4252 | Q88F47 | Cytochrome c oxidase subunit, cbb3-type (primary
    bucket kegg:ppu00190)

    - ccoP-I: PP_4253 | Q88F46 | Cbb3-type cytochrome c oxidase subunit (primary bucket
    kegg:ppu00190)

    - ccoN-II: PP_4255 | Q88F44 | cytochrome-c oxidase (EC 7.1.1.9) (EC 7.1.1.9; primary
    bucket kegg:ppu00190)

    - ccoO-II: PP_4256 | Q88F43 | Cytochrome c oxidase subunit, cbb3-type (primary
    bucket kegg:ppu00190)

    - ccoQ-II: PP_4257 | Q88F42 | Cytochrome c oxidase subunit, cbb3-type (primary
    bucket kegg:ppu00190)

    - ccoP-II: PP_4258 | Q88F41 | Cbb3-type cytochrome c oxidase subunit (primary
    bucket kegg:ppu00190)

    - cioB: PP_4650 | Q88E18 | Ubiquinol oxidase subunit II, cyanide insensitive (primary
    bucket kegg:ppu00190)

    - cioA: PP_4651 | Q88E17 | Ubiquinol oxidase subunit I, cyanide insensitive (primary
    bucket kegg:ppu00190)

    - ppk: PP_5217 | Q88CG4 | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate
    phosphotransferase) (Polyphosphoric acid kinase) (EC 2.7.4.1; primary bucket kegg:ppu03018)

    - atpC: PP_5412 | Q88BX5 | ATP synthase epsilon chain (ATP synthase F1 sector
    epsilon subunit) (F-ATPase epsilon subunit) (primary bucket kegg:ppu00190)

    - atpD: PP_5413 | Q88BX4 | ATP synthase subunit beta (EC 7.1.2.2) (ATP synthase
    F1 sector subunit beta) (F-ATPase subunit beta) (EC 7.1.2.2; primary bucket kegg:ppu00190)

    - atpG: PP_5414 | Q88BX3 | ATP synthase gamma chain (ATP synthase F1 sector gamma
    subunit) (F-ATPase gamma subunit) (primary bucket kegg:ppu00190)

    - atpA: PP_5415 | Q88BX2 | ATP synthase subunit alpha (EC 7.1.2.2) (ATP synthase
    F1 sector subunit alpha) (F-ATPase subunit alpha) (EC 7.1.2.2; primary bucket
    kegg:ppu00190)

    - atpH: PP_5416 | Q88BX1 | ATP synthase subunit delta (ATP synthase F(1) sector
    subunit delta) (F-type ATPase subunit delta) (F-ATPase subunit delta) (primary
    bucket kegg:ppu00190)

    - atpF: PP_5417 | Q88BX0 | ATP synthase subunit b (ATP synthase F(0) sector subunit
    b) (ATPase subunit I) (F-type ATPase subunit b) (F-ATPase subunit b) (primary
    bucket kegg:ppu00190)

    - atpE: PP_5418 | Q88BW9 | ATP synthase subunit c (ATP synthase F(0) sector subunit
    c) (F-type ATPase subunit c) (F-ATPase subunit c) (Lipid-binding protein) (primary
    bucket kegg:ppu00190)

    - atpB: PP_5419 | Q88BW8 | ATP synthase subunit a (ATP synthase F0 sector subunit
    a) (F-ATPase subunit 6) (primary bucket kegg:ppu00190)'
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__mitochondrial_complex_i_core__ppu00190-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__mitochondrial_complex_i_core__ppu00190-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Mitochondrial respiratory Complex I core (NADH:ubiquinone oxidoreductase) — catalytic N and Q modules; NDUFV1/NDUFV2/NDUFS1-3/NDUFS6-8/NDUFA9 in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00190
- Resolved ID: ppu00190
- Resolved name: Oxidative phosphorylation
- Source: KEGG

Resolved local bucket kegg:ppu00190 with 44 primary genes; module area: energy_respiration_inorganic_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 54

- PP_0103: PP_0103 | Q88RM6 | Cytochrome c oxidase subunit 2 (EC 7.1.1.9) (EC 7.1.1.9; primary bucket kegg:ppu00190)
- ctaD: PP_0104 | Q88RM5 | Cytochrome c oxidase subunit 1 (EC 7.1.1.9) (EC 7.1.1.9; primary bucket kegg:ppu00190)
- PP_0105: PP_0105 | Q88RM4 | Cytochrome c oxidase assembly protein CtaG (primary bucket kegg:ppu00190)
- PP_0106: PP_0106 | Q88RM3 | Probable cytochrome c oxidase subunit 3 (EC 7.1.1.9) (Cytochrome aa3 subunit 3) (Cytochrome c oxidase polypeptide III) (EC 7.1.1.9; primary bucket kegg:ppu00190)
- PP_0109: PP_0109 | Q88RM0 | Cytochrome B (primary bucket kegg:ppu00860)
- cyoE1: PP_0110 | Q88RL9 | Protoheme IX farnesyltransferase 1 (EC 2.5.1.141) (Heme B farnesyltransferase 1) (Heme O synthase 1) (EC 2.5.1.141; primary bucket kegg:ppu00860)
- ppa: PP_0538 | Q88QF6 | Inorganic pyrophosphatase (EC 3.6.1.1) (Pyrophosphate phospho-hydrolase) (PPase) (EC 3.6.1.1; primary bucket kegg:ppu00190)
- ndh: PP_0626 | Q88Q70 | NADH dehydrogenase (EC 1.6.99.3) (EC 1.6.99.3; primary bucket kegg:ppu00190)
- ppkB: PP_0712 | Q88PY6 | ADP/GDP-polyphosphate phosphotransferase (EC 2.7.4.-) (Polyphosphate kinase PPK2) (EC 2.7.4.-; primary bucket kegg:ppu03018)
- cyoA: PP_0812 | Q88PN7 | Ubiquinol oxidase subunit 2 (primary bucket kegg:ppu00190)
- cyoB: PP_0813 | Q88PN6 | Cytochrome bo(3) ubiquinol oxidase subunit 1 (EC 7.1.1.3) (Cytochrome o ubiquinol oxidase subunit 1) (Oxidase bo(3) subunit 1) (Ubiquinol oxidase polypeptide I) (Ubiquinol oxidase subunit 1) (EC 7.1.1.3; primary bucket kegg:ppu00190)
- cyoC: PP_0814 | Q88PN5 | Cytochrome bo(3) ubiquinol oxidase subunit 3 (Cytochrome o ubiquinol oxidase subunit 3) (Oxidase bo(3) subunit 3) (Ubiquinol oxidase polypeptide III) (Ubiquinol oxidase subunit 3) (primary bucket kegg:ppu00190)
- cyoD: PP_0815 | Q88PN4 | Cytochrome bo(3) ubiquinol oxidase subunit 4 (Cytochrome o ubiquinol oxidase subunit 4) (Oxidase bo(3) subunit 4) (Ubiquinol oxidase polypeptide IV) (Ubiquinol oxidase subunit 4) (primary bucket kegg:ppu00190)
- cyoE2: PP_0816 | Q88PN3 | Protoheme IX farnesyltransferase 2 (EC 2.5.1.141) (Heme B farnesyltransferase 2) (Heme O synthase 2) (EC 2.5.1.141; primary bucket kegg:ppu00860)
- petA: PP_1317 | Q88N95 | Ubiquinol-cytochrome c reductase iron-sulfur subunit (EC 7.1.1.8) (EC 7.1.1.8; primary bucket kegg:ppu04148)
- petB: PP_1318 | Q88N94 | Cytochrome b (primary bucket kegg:ppu00190)
- petC: PP_1319 | Q88N93 | Ubiquinol--cytochrome c reductase, cytochrome c1 (primary bucket kegg:ppu00190)
- PP_2867: PP_2867 | Q88IY2 | Pyridine nucleotide-disulphide oxidoreductase family protein (primary bucket kegg:ppu00190)
- nuoA: PP_4119 | Q88FH7 | NADH-quinone oxidoreductase subunit A (EC 7.1.1.-) (NADH dehydrogenase I subunit A) (NDH-1 subunit A) (NUO1) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoB: PP_4120 | Q88FH6 | NADH-quinone oxidoreductase subunit B (EC 7.1.1.-) (NADH dehydrogenase I subunit B) (NDH-1 subunit B) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoC: PP_4121 | Q88FH5 | NADH-quinone oxidoreductase subunit C/D (EC 7.1.1.-) (NADH dehydrogenase I subunit C/D) (NDH-1 subunit C/D) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoE: PP_4122 | Q88FH4 | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase I subunit E) (NDH-1 subunit E) (primary bucket kegg:ppu00190)
- nuoF: PP_4123 | Q88FH3 | NADH-quinone oxidoreductase subunit F (EC 7.1.1.-) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoG: PP_4124 | Q88FH2 | NADH-quinone oxidoreductase subunit G (EC 7.1.1.-) (NADH dehydrogenase I subunit G) (NDH-1 subunit G) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoH: PP_4125 | Q88FH1 | NADH-quinone oxidoreductase subunit H (EC 7.1.1.-) (NADH dehydrogenase I subunit H) (NDH-1 subunit H) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoI: PP_4126 | Q88FH0 | NADH-quinone oxidoreductase subunit I (EC 7.1.1.-) (NADH dehydrogenase I subunit I) (NDH-1 subunit I) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoJ: PP_4127 | Q88FG9 | NADH-quinone oxidoreductase subunit J (EC 7.1.1.-) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoK: PP_4128 | Q88FG8 | NADH-quinone oxidoreductase subunit K (EC 7.1.1.-) (NADH dehydrogenase I subunit K) (NDH-1 subunit K) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- nuoL: PP_4129 | Q88FG7 | NADH-quinone oxidoreductase subunit L (NADH dehydrogenase I subunit L) (NDH-1 subunit L) (primary bucket kegg:ppu00190)
- nuoM: PP_4130 | Q88FG6 | NADH-quinone oxidoreductase subunit M (NADH dehydrogenase I subunit M) (NDH-1 subunit M) (primary bucket kegg:ppu00190)
- nuoN: PP_4131 | Q88FG5 | NADH-quinone oxidoreductase subunit N (EC 7.1.1.-) (NADH dehydrogenase I subunit N) (NDH-1 subunit N) (EC 7.1.1.-; primary bucket kegg:ppu00190)
- sdhB: PP_4190 | Q88FA8 | Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1) (EC 1.3.5.1; primary bucket kegg:ppu00020)
- sdhA: PP_4191 | Q88FA7 | Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1) (EC 1.3.5.1; primary bucket kegg:ppu00020)
- sdhD: PP_4192 | Q88FA6 | Succinate dehydrogenase hydrophobic membrane anchor subunit (primary bucket kegg:ppu00020)
- sdhC: PP_4193 | Q88FA5 | Succinate dehydrogenase cytochrome b556 subunit (primary bucket kegg:ppu00020)
- ccoN-I: PP_4250 | Q88F49 | cytochrome-c oxidase (EC 7.1.1.9) (EC 7.1.1.9; primary bucket kegg:ppu00190)
- ccoO-I: PP_4251 | Q88F48 | Cytochrome c oxidase subunit, cbb3-type (primary bucket kegg:ppu00190)
- ccoQ-I: PP_4252 | Q88F47 | Cytochrome c oxidase subunit, cbb3-type (primary bucket kegg:ppu00190)
- ccoP-I: PP_4253 | Q88F46 | Cbb3-type cytochrome c oxidase subunit (primary bucket kegg:ppu00190)
- ccoN-II: PP_4255 | Q88F44 | cytochrome-c oxidase (EC 7.1.1.9) (EC 7.1.1.9; primary bucket kegg:ppu00190)
- ccoO-II: PP_4256 | Q88F43 | Cytochrome c oxidase subunit, cbb3-type (primary bucket kegg:ppu00190)
- ccoQ-II: PP_4257 | Q88F42 | Cytochrome c oxidase subunit, cbb3-type (primary bucket kegg:ppu00190)
- ccoP-II: PP_4258 | Q88F41 | Cbb3-type cytochrome c oxidase subunit (primary bucket kegg:ppu00190)
- cioB: PP_4650 | Q88E18 | Ubiquinol oxidase subunit II, cyanide insensitive (primary bucket kegg:ppu00190)
- cioA: PP_4651 | Q88E17 | Ubiquinol oxidase subunit I, cyanide insensitive (primary bucket kegg:ppu00190)
- ppk: PP_5217 | Q88CG4 | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate phosphotransferase) (Polyphosphoric acid kinase) (EC 2.7.4.1; primary bucket kegg:ppu03018)
- atpC: PP_5412 | Q88BX5 | ATP synthase epsilon chain (ATP synthase F1 sector epsilon subunit) (F-ATPase epsilon subunit) (primary bucket kegg:ppu00190)
- atpD: PP_5413 | Q88BX4 | ATP synthase subunit beta (EC 7.1.2.2) (ATP synthase F1 sector subunit beta) (F-ATPase subunit beta) (EC 7.1.2.2; primary bucket kegg:ppu00190)
- atpG: PP_5414 | Q88BX3 | ATP synthase gamma chain (ATP synthase F1 sector gamma subunit) (F-ATPase gamma subunit) (primary bucket kegg:ppu00190)
- atpA: PP_5415 | Q88BX2 | ATP synthase subunit alpha (EC 7.1.2.2) (ATP synthase F1 sector subunit alpha) (F-ATPase subunit alpha) (EC 7.1.2.2; primary bucket kegg:ppu00190)
- atpH: PP_5416 | Q88BX1 | ATP synthase subunit delta (ATP synthase F(1) sector subunit delta) (F-type ATPase subunit delta) (F-ATPase subunit delta) (primary bucket kegg:ppu00190)
- atpF: PP_5417 | Q88BX0 | ATP synthase subunit b (ATP synthase F(0) sector subunit b) (ATPase subunit I) (F-type ATPase subunit b) (F-ATPase subunit b) (primary bucket kegg:ppu00190)
- atpE: PP_5418 | Q88BW9 | ATP synthase subunit c (ATP synthase F(0) sector subunit c) (F-type ATPase subunit c) (F-ATPase subunit c) (Lipid-binding protein) (primary bucket kegg:ppu00190)
- atpB: PP_5419 | Q88BW8 | ATP synthase subunit a (ATP synthase F0 sector subunit a) (F-ATPase subunit 6) (primary bucket kegg:ppu00190)

## Generic Module Context

### Working Scope

Respiratory Complex I (NADH:ubiquinone oxidoreductase) is the largest enzyme of the electron transport chain and its main entry point: it oxidises NADH, passes the electrons through a chain of flavin and iron-sulfur cofactors to reduce ubiquinone, and uses the energy released to pump four protons across the inner membrane. This module covers the catalytic core of the L-shaped peripheral (matrix) arm — the seven conserved "core" nuclear subunits plus the closely associated flavoprotein subunits — organised into two functional modules. The N-module (NADH-oxidising) holds the flavin site: NDUFV1 (51 kDa) binds FMN and the NADH substrate, NDUFV2 (24 kDa) carries the first [2Fe-2S] cluster (N1a), and NDUFS1 (75 kDa) provides further Fe-S clusters, forming the flavoprotein (FP) subcomplex with the accessory NDUFS6. The Q-module (ubiquinone-reducing) forms the wire to the quinone site: NDUFS2 (49 kDa) and NDUFS3 (30 kDa) are cofactor-less core subunits shaping the ubiquinone cavity, NDUFS7 (PSST) coordinates the terminal [4Fe-4S] cluster N2 that donates electrons to ubiquinone, NDUFS8 (TYKY) carries the N6a/N6b [4Fe-4S] clusters of the electron-transfer wire, and the accessory NDUFA9 (SDR-fold, structural NADPH) stabilises the Q-module/membrane-arm junction; NDUFS4 is an accessory subunit required for assembly and stability of the whole peripheral arm. Inherited defects in these core subunits are among the commonest causes of mitochondrial complex I deficiency — typically Leigh syndrome, leukoencephalopathy, fatal infantile lactic acidosis or encephalocardiomyopathy.

### Provisional Biological Outline

- Mitochondrial respiratory Complex I core (N and Q modules)
  - 1. N-module (NADH oxidation, FMN + entry Fe-S clusters)
  - N-module (flavoprotein / NADH-oxidising)
    - NDUFV1: FMN/NADH catalytic subunit (51 kDa) (molecular player: NADH dehydrogenase flavoprotein 1 family (NDUFV1); activity or role: NADH dehydrogenase activity)
    - NDUFV2: N1a [2Fe-2S] subunit (24 kDa) (molecular player: NADH dehydrogenase flavoprotein 2 family (NDUFV2); activity or role: electron transfer activity)
    - NDUFS1: 75 kDa Fe-S subunit (molecular player: NADH-quinone oxidoreductase G/NDUFS1 family; activity or role: electron transfer activity)
    - NDUFS6: zinc-binding N-module accessory (13 kDa) (molecular player: NDUFS6 accessory-subunit family; activity or role: structural molecule activity)
  - 2. Q-module (ubiquinone reduction, terminal Fe-S wire)
  - Q-module (ubiquinone-reducing)
    - NDUFS2: 49 kDa Q-module core subunit (molecular player: NADH-quinone oxidoreductase D/NDUFS2 family; activity or role: ubiquinone binding)
    - NDUFS3: 30 kDa Q-module core subunit (molecular player: NADH-quinone oxidoreductase C/NDUFS3 family; activity or role: structural molecule activity)
    - NDUFS7 (PSST): N2 [4Fe-4S] subunit (molecular player: NADH-quinone oxidoreductase B/NDUFS7 (PSST) family; activity or role: NADH dehydrogenase (ubiquinone) activity)
    - NDUFS8 (TYKY): N6a/N6b [4Fe-4S] subunit (molecular player: NADH-quinone oxidoreductase I/NDUFS8 (TYKY) family; activity or role: 4 iron, 4 sulfur cluster binding)
    - NDUFA9: SDR-fold junction accessory (39 kDa) (molecular player: NDUFA9 / SDR-fold accessory family; activity or role: structural molecule activity)
  - 3. peripheral-arm assembly/stability accessory
  - NDUFS4 accessory subunit (peripheral-arm assembly)
    - NDUFS4: accessory/assembly subunit (18 kDa) (molecular player: NDUFS4 accessory-subunit family)

### Known Relationships Among Steps

- N-module (flavoprotein / NADH-oxidising) feeds into Q-module (ubiquinone-reducing): Electrons from NADH oxidation at the FMN/N-module are relayed through the Fe-S wire to the Q-module N2 cluster, which reduces ubiquinone.
- NDUFS4 accessory subunit (peripheral-arm assembly) promotes N-module (flavoprotein / NADH-oxidising): NDUFS4 is required for assembly and stability of the catalytic peripheral arm.

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

# Module/Pathway/Taxon Review: Mitochondrial Complex I Core (N & Q Modules) in *Pseudomonas putida* KT2440

**Review topic:** Mitochondrial respiratory Complex I core (NADH:ubiquinone oxidoreductase) — catalytic N and Q modules (NDUFV1/NDUFV2/NDUFS1-3/NDUFS6-8/NDUFA9)
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00190` "Oxidative phosphorylation" (44 primary genes; 54 candidates)
**Module area:** energy_respiration_inorganic_metabolism

---

## 1. Executive Summary

The catalytic core of mitochondrial respiratory Complex I — the seven conserved core subunits distributed across the NADH-oxidising **N-module** and the ubiquinone-reducing **Q-module** — is **fully present and satisfiable** in *Pseudomonas putida* KT2440, but it is encoded by the **bacterial `nuo` operon (NDH-1)** rather than by any eukaryote-style `NDUF*` genes. Every one of the seven conserved catalytic core subunits has a clean 1:1 bacterial ortholog in the KT2440 candidate list: the N-module subunits NDUFV1, NDUFV2 and NDUFS1 map to **nuoF (PP_4123)**, **nuoE (PP_4122)** and **nuoG (PP_4124)**; the Q-module subunits NDUFS7 (PSST) and NDUFS8 (TYKY) map to **nuoB (PP_4120)** and **nuoI (PP_4126)**; and the two cofactor-less Q-module core subunits NDUFS2 (49 kDa) and NDUFS3 (30 kDa) are both encoded by the **single fused `nuoCD` gene (PP_4121)**, exactly as in *Escherichia coli* and other gamma-proteobacteria.

The three **accessory/supernumerary** subunits in the review scope — **NDUFS4**, **NDUFS6** and **NDUFA9** — are **eukaryote-specific additions** to Complex I and have no bacterial orthologs. Their absence from the KT2440 candidate list is expected and correct; they should be marked `not_expected_in_target_taxon`, not flagged as gaps. Bacterial NDH-1 is the "minimal" ~14-subunit enzyme, roughly half the size of the 44-subunit mammalian complex, and lacks the ~30 supernumerary subunits that arose in the eukaryotic lineage.

For curation, the central conclusions are: (i) the module is **covered** at the catalytic core level but **needs revision** because its generic boundary is eukaryote-centric and expects `NDUF*` gene names that do not exist in bacteria; (ii) the KEGG `ppu00190` bucket is a **whole-OXPHOS conflation** and must not be treated as a Complex I gene set — only PP_4119–PP_4131 (nuoA–N) belong to Complex I, while the other ~40 candidates are Complexes II–V and terminal oxidases; and (iii) the `ndh` gene (**PP_0626**) is a **type-II NADH dehydrogenase (NDH-2)**, a non-homologous, non-proton-pumping single-subunit alternative that must not be mapped onto any Complex I core step. KT2440 carries a **single-copy, complete, syntenic** `nuo` locus with no paralogous second cluster, so satisfiability is unambiguous. All conclusions rest on strong homology/orthology evidence with robust biochemical transfer from *E. coli* and *Thermus thermophilus*; no KT2440-specific subunit-mutant data were located.

---

## 2. Target-Organism Pathway Definition

### 2.1 What process is in scope

The reviewed module is the **catalytic peripheral (hydrophilic) arm core of Complex I / NDH-1** — specifically the electron-input **N-module** (FMN + entry Fe-S clusters, NADH oxidation) and the electron-output **Q-module** (terminal Fe-S wire + quinone reduction). In *P. putida* KT2440 the physiological enzyme is the bacterial **proton-translocating NADH:quinone oxidoreductase (NDH-1)**, encoded by the `nuo` operon. It oxidises NADH, passes electrons through FMN and a chain of iron-sulfur clusters to reduce the native quinone pool, and couples this to proton translocation across the inner membrane.

The core fold, cofactor set and electron-transfer logic of the peripheral arm are **highly conserved from bacteria to mammals** ([PMID: 41977177](https://pubmed.ncbi.nlm.nih.gov/41977177/)), which is exactly what makes the bacterial enzyme the accepted "minimal model" for the mitochondrial complex ([PMID: 26807915](https://pubmed.ncbi.nlm.nih.gov/26807915/)).

### 2.2 Neighboring pathways to keep separate

The KEGG map `ppu00190` "Oxidative phosphorylation" is an **overview bucket for all five OXPHOS complexes plus accessory energetics**, not a Complex I module. For this review it must be decomposed:

| Complex / system | KT2440 genes in the bucket | In scope for this module? |
|---|---|---|
| **Complex I (NDH-1)** | `nuoA–N` = PP_4119–PP_4131 | **YES (core only)** |
| Type-II NADH dehydrogenase (NDH-2) | `ndh` = PP_0626 | No — non-homologous alternative |
| Complex II (SDH) | `sdhABCD` = PP_4190–4193 | No (TCA/`ppu00020`) |
| Complex III (cytochrome *bc₁*) | `petABC` = PP_1317–1319 | No |
| Complex IV / terminal oxidases | `cox`/`ctaD` (PP_0103–0106), `cyoABCD` (PP_0812–0815), `ccoNOQP-I/II` (PP_4250–4258), `cioAB` (PP_4650–4651) | No |
| Complex V (F₁F₀ ATP synthase) | `atpA–H` = PP_5412–5419 | No |
| Broad flavoprotein | PP_2867 (pyridine nucleotide-disulphide oxidoreductase) | No — not a Nuo subunit |

Neighboring maps to keep distinct: TCA cycle (`ppu00020`), polyphosphate metabolism (`ppu03018`), porphyrin/heme biosynthesis (`ppu00860`), and photosynthesis-family electron transport (`ppu04148`).

### 2.3 Alternate names and database definitions

- **NDH-1 / Complex I / NADH:ubiquinone oxidoreductase / NADH-quinone oxidoreductase** all refer to the same `nuo`-encoded enzyme.
- Bacterial subunit names use the **Nuo** nomenclature (NuoA–N); *T. thermophilus* uses **Nqo1–14**; mammals use **NDUF\*** and **ND1–6**. The mapping across nomenclatures is standard (see §3).
- **EC** for the complex: 7.1.1.2 (formerly 1.6.5.3); individual KT2440 subunits are annotated EC 7.1.1.- .

---

## 3. Expected Step Model (Bacterial Re-mapping)

The generic (eukaryote-centric) module lists nine core/accessory subunits. Below is the species-aware re-mapping to bacterial `nuo` genes, which is the correct expectation model for KT2440.

```
   NADH ──► [ N-MODULE ]  ──►  Fe-S wire  ──►  [ Q-MODULE ]  ──► Quinone (Q → QH2)
             FMN + N1a,N3            (N4,N5,N6a/b)      N2 cluster
             NADH oxidation                            quinone reduction

   Mito subunit      Function                         KT2440 gene   Locus tag    Call
   ------------------------------------------------------------------------------------
   N-MODULE
   NDUFV1 (51 kDa)   FMN/NADH catalytic               nuoF          PP_4123      COVERED
   NDUFV2 (24 kDa)   N1a [2Fe-2S]                      nuoE          PP_4122      COVERED
   NDUFS1 (75 kDa)   Fe-S relay                        nuoG          PP_4124      COVERED
   NDUFS6 (13 kDa)   Zn accessory (N-module)           —            —            NOT EXPECTED
   Q-MODULE
   NDUFS2 (49 kDa)   quinone-cavity core          ┐   nuoCD (D seg) PP_4121      COVERED (fused)
   NDUFS3 (30 kDa)   quinone-cavity core          ┘   nuoCD (C seg) PP_4121      COVERED (fused)
   NDUFS7 (PSST)     N2 [4Fe-4S] terminal cluster      nuoB          PP_4120      COVERED
   NDUFS8 (TYKY)     N6a/N6b [4Fe-4S] wire             nuoI          PP_4126      COVERED
   NDUFA9 (39 kDa)   SDR-fold Q/membrane junction      —            —            NOT EXPECTED
   ASSEMBLY ACCESSORY
   NDUFS4 (18 kDa)   peripheral-arm assembly/stability —            —            NOT EXPECTED
```

**Result: 7 of 7 conserved catalytic core subunits COVERED; 3 accessory subunits NOT_EXPECTED_IN_TARGET_TAXON.**

The key species-aware subtlety is the **nuoC/nuoD fusion**: in *P. putida* (and other gamma-proteobacteria) subunits C and D are a single polypeptide, annotated explicitly as "subunit C/D" (PP_4121). The two mitochondrial core subunits it corresponds to — NDUFS3 (30 kDa, ~NuoC) and NDUFS2 (49 kDa, ~NuoD) — therefore both map to one KT2440 gene. Curation logic must treat a **single satisfied `nuoCD` gene as covering two module steps**.

---

## 4. Candidate Genes and Evidence

### 4.1 Complex I core subunits (in scope, high confidence)

| Gene | Locus | UniProt | Mito ortholog / module role | Module | Evidence type | Call |
|---|---|---|---|---|---|---|
| `nuoF` | PP_4123 | Q88FH3 | NDUFV1 — FMN/NADH catalytic | N | Homology + biochem transfer | Covered |
| `nuoE` | PP_4122 | Q88FH4 | NDUFV2 — N1a [2Fe-2S] | N | Homology | Covered |
| `nuoG` | PP_4124 | Q88FH2 | NDUFS1 — 75 kDa Fe-S | N | Homology | Covered |
| `nuoB` | PP_4120 | Q88FH6 | NDUFS7 (PSST) — N2 [4Fe-4S] | Q | Homology + structural | Covered |
| `nuoCD` | PP_4121 | Q88FH5 | NDUFS3 + NDUFS2 (fused C/D) | Q | Homology + explicit fusion annotation | Covered (2 steps) |
| `nuoI` | PP_4126 | Q88FH0 | NDUFS8 (TYKY) — N6a/N6b [4Fe-4S] | Q | Homology | Covered |

Supporting membrane-arm and connector subunits also present (not part of the N/Q catalytic-core scope but confirming a complete enzyme): `nuoA` (PP_4119), `nuoH` (PP_4125, ND1), `nuoJ` (PP_4127), `nuoK` (PP_4128), `nuoL` (PP_4129, ND5), `nuoM` (PP_4130, ND4), `nuoN` (PP_4131, ND2). All lie in a contiguous, canonically ordered operon PP_4119→PP_4131.

**Curation-relevant caveats.** All KT2440 `nuo` subunits carry broad **EC 7.1.1.-** and generic "NADH-quinone oxidoreductase subunit X" annotations; these are family-level, not KT2440-experimental. The transfer of specific cofactor/site assignments (FMN on NuoF, N2 on NuoB, quinone Asp on NuoCD) comes from *E. coli* and *T. thermophilus*, not from KT2440 experiments — a **strong** but homology-based transfer, given the deep conservation of the core.

### 4.2 The `nuoCD` fusion — direct supporting evidence

The C/D fusion is not an annotation artifact. Structure/function work on the *E. coli* NuoD segment established it as the homolog of the mitochondrial 49 kDa subunit (NDUFS2) and localised the conserved quinone-site aspartate to NuoCD ([PMID: 25545070](https://pubmed.ncbi.nlm.nih.gov/25545070/); [PMID: 39262040](https://pubmed.ncbi.nlm.nih.gov/39262040/)). The KT2440 "subunit C/D" annotation for PP_4121 is therefore biochemically well-founded.

### 4.3 Genes that must NOT be mapped to Complex I core

| Gene | Locus | Why excluded |
|---|---|---|
| `ndh` | PP_0626 | **Type-II NADH dehydrogenase (NDH-2)** — single-subunit, non-homologous to Nuo, does **not** pump protons, no Fe-S/FMN wire. A parallel/alternative NADH entry point, not a Complex I subunit. |
| PP_2867 | Q88IY2 | Broad "pyridine nucleotide-disulphide oxidoreductase" flavoprotein family; not a Nuo subunit. Likely bucket noise. |
| `sdhA-D`, `petA-C`, `cox`/`cta`, `cyo`, `cco`, `cio`, `atp*` | various | Complexes II–V and terminal oxidases; separate modules. |

### 4.4 Accessory subunits (out-of-taxon)

NDUFS4, NDUFS6, NDUFA9 have **no candidate gene** and **no expected bacterial ortholog**. Bacterial NDH-1 is the ~14-subunit minimal enzyme ([PMID: 26807915](https://pubmed.ncbi.nlm.nih.gov/26807915/)) versus the 44-subunit mammalian complex ([PMID: 23836892](https://pubmed.ncbi.nlm.nih.gov/23836892/)); the ~30 supernumerary subunits (including these three) are eukaryotic-lineage additions. Their absence is the correct null result, not a gap.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Not true gaps — expected absences
- **NDUFS4, NDUFS6, NDUFA9:** `not_expected_in_target_taxon`. Marking these as gaps would be a false negative driven by an eukaryote-centric module boundary.

### 5.2 Genuine curation issues
1. **Module boundary is eukaryote-centric.** The generic module expects `NDUF*` gene names and separate N-/Q-module accessory subunits that do not exist in bacteria. The module needs a **bacterial variant** keyed on `nuo` genes → `module_needs_revision`.
2. **nuoCD fusion.** Two module steps (NDUFS2, NDUFS3) satisfied by one gene (PP_4121). The satisfiability logic must accept a single fused gene covering two steps, or the step count will look artificially short by one.
3. **KEGG bucket over-inclusion.** `ppu00190` conflates all five complexes; ~40 of 54 candidates are irrelevant to Complex I. Do not use the bucket as a Complex I gene set.
4. **NDH-2 mis-mapping risk.** `ndh` (PP_0626) is annotated "NADH dehydrogenase (EC 1.6.99.3)" and sits in the same bucket. Automated tools may over-propagate it to a Complex I step; it must be explicitly excluded.
5. **Broad EC/GO on `nuo` subunits.** EC 7.1.1.- and generic GO ("NADH dehydrogenase activity", "electron transfer activity") are family-level; specific cofactor-binding GO (FMN binding, [4Fe-4S] binding, ubiquinone binding) is transferred by homology, not KT2440 experiment.

### 5.3 Over-annotation summary
- No over-propagation *within* the true `nuo` set — those annotations are appropriate.
- The over-annotation risk is at the **bucket level** (whole OXPHOS grouped as one map) and the **NDH-2 confounder**.

---

## 6. Module and GO-Curation Recommendations

**Per-step calls**

| Step (mito subunit) | KT2440 mapping | Call |
|---|---|---|
| NDUFV1 | nuoF / PP_4123 | `covered` |
| NDUFV2 | nuoE / PP_4122 | `covered` |
| NDUFS1 | nuoG / PP_4124 | `covered` |
| NDUFS7 (PSST) | nuoB / PP_4120 | `covered` |
| NDUFS8 (TYKY) | nuoI / PP_4126 | `covered` |
| NDUFS2 (49 kDa) | nuoCD / PP_4121 | `covered` (fused) |
| NDUFS3 (30 kDa) | nuoCD / PP_4121 | `covered` (fused) |
| NDUFS6 | — | `not_expected_in_target_taxon` |
| NDUFA9 | — | `not_expected_in_target_taxon` |
| NDUFS4 | — | `not_expected_in_target_taxon` |

**Overall module status: `module_needs_revision`** — the catalytic core is genuinely covered, but the module document must be re-expressed for bacteria.

**Recommended actions**
1. Create/attach a **bacterial NDH-1 (`nuo`) variant** of the module that maps the seven catalytic core steps onto NuoF/E/G/B/I and fused NuoCD, and explicitly declares NDUFS4/S6/A9 as eukaryote-specific (not_expected).
2. Add a **fusion rule** so PP_4121 (nuoCD) satisfies both the NDUFS2 and NDUFS3 steps.
3. Add an **exclusion note** that `ndh`/PP_0626 (NDH-2) and PP_2867 are *not* Complex I core and must not satisfy any step.
4. Add a **bucket caveat** that KEGG `ppu00190` spans all OXPHOS complexes.
5. GO curation: retain family-level GO on `nuo` subunits; where specific cofactor GO is asserted (e.g., GO:0051539 4Fe-4S binding on nuoB/nuoI; FMN binding on nuoF), annotate with an **ISS/IEA homology evidence code**, not experimental, since no KT2440-specific biochemistry was found. No new GO term request appears necessary — existing bacterial NDH-1 GO terms are adequate.

---

## 7. Genes to Promote to Full `fetch-gene` Review

| Priority | Gene | Locus | Reason |
|---|---|---|---|
| High | `nuoCD` | PP_4121 | Fused two-in-one subunit; verify fusion boundary and that it truly covers both NDUFS2 and NDUFS3; confirm quinone-site Asp. |
| High | `nuoF` | PP_4123 | N-module catalytic entry (FMN/NADH, ~NDUFV1); anchor of the N-module call. |
| High | `nuoB` | PP_4120 | Terminal N2 [4Fe-4S] cluster (~NDUFS7/PSST); electron donor to quinone. |
| Medium | `nuoI` | PP_4126 | TYKY/NDUFS8 [4Fe-4S] wire; confirm both cluster-binding motifs. |
| Medium | `nuoE`, `nuoG` | PP_4122, PP_4124 | N1a and 75 kDa Fe-S relay; confirm cluster complement. |
| Medium | `ndh` | PP_0626 | Confirm NDH-2 identity and **explicitly exclude** from Complex I to prevent auto over-propagation. |

---

## 8. Mechanistic Model / Interpretation

*P. putida* KT2440 runs an aerobic, branched respiratory chain in which NADH oxidation is served by **two independent, non-homologous enzymes**: the proton-pumping **Complex I / NDH-1** (`nuo`, PP_4119–4131) and the non-pumping **NDH-2** (`ndh`, PP_0626). Only the former corresponds to the reviewed mitochondrial Complex I core. Its peripheral arm is a linear electron conduit that is structurally and mechanistically conserved across all domains of life:

```
NADH → FMN(NuoF/NDUFV1) → N3 → N1b → N4 → N5(NuoG/NDUFS1)
        → N6a/N6b(NuoI/NDUFS8) → N2(NuoB/NDUFS7) → Quinone
                                        │
                       quinone cavity shaped by fused NuoCD (NDUFS2+NDUFS3)
```

The quinone chemistry at the deep end of the cavity — protonation of a conserved aspartate near cluster N2 — has been pinned to the NuoCD/49-kDa subunit and is central to redox-coupled proton pumping ([PMID: 39262040](https://pubmed.ncbi.nlm.nih.gov/39262040/); [PMID: 26330610](https://pubmed.ncbi.nlm.nih.gov/26330610/); [PMID: 23417064](https://pubmed.ncbi.nlm.nih.gov/23417064/)). Because this machinery is conserved and KT2440 carries a **single, complete, syntenic** operon, the module is satisfiable with high confidence, even without strain-specific mutant data. The eukaryotic accessory subunits (NDUFS4/S6/A9) are structural/assembly add-ons of the larger mitochondrial complex; the bacterial enzyme achieves the same catalysis without them, which is why they are legitimately absent here.

---

## 9. Evidence Base

| PMID | How it supports the review |
|---|---|
| [25545070](https://pubmed.ncbi.nlm.nih.gov/25545070/) | *"The NuoD segment (homologue of mitochondrial 49 kDa subunit)"* — establishes NuoD = NDUFS2, underpinning the Q-module core mapping and the nuoCD fusion. |
| [39262040](https://pubmed.ncbi.nlm.nih.gov/39262040/) | *"a specific, conserved aspartic acid residue in the quinone binding site (D325 on subunit NuoCD in Escherichia coli)"* — confirms the fused NuoCD polypeptide and the quinone-cavity core (NDUFS2/NDUFS3). |
| [26807915](https://pubmed.ncbi.nlm.nih.gov/26807915/) | *"Bacterial enzyme is about half the size of mitochondrial and thus provides its important 'minimal' model."* — supports that NDUFS4/S6/A9 accessory subunits are not expected in bacteria. |
| [23836892](https://pubmed.ncbi.nlm.nih.gov/23836892/) | *"Complex I ... in mammalian mitochondria is an L-shaped assembly of 44 protein subunits"* — contrasts 44-subunit mammalian vs ~14-subunit bacterial core. |
| [23417064](https://pubmed.ncbi.nlm.nih.gov/23417064/) | Crystal structure of intact *T. thermophilus* Complex I — defines the conserved 16-subunit core, quinone chamber and N2 cluster used for the mapping. |
| [41977177](https://pubmed.ncbi.nlm.nih.gov/41977177/) | *"This basic core subunit architecture is highly conserved from bacterial to mammalian CI"* — justifies homology transfer to KT2440. |
| [26330610](https://pubmed.ncbi.nlm.nih.gov/26330610/), [30697773](https://pubmed.ncbi.nlm.nih.gov/30697773/), [32347721](https://pubmed.ncbi.nlm.nih.gov/32347721/), [24973951](https://pubmed.ncbi.nlm.nih.gov/24973951/) | Mechanistic/structural detail on Fe-S wire, cluster potentials, quinone site and membrane-arm proton pumping — supports the conserved electron-transfer logic. |

**Evidence class:** Homology/orthology (UniProt/KEGG assignments) with **strong biochemical transfer** from *E. coli* and *T. thermophilus* Complex I. No *P. putida* KT2440-specific Complex I subunit-mutant or structural study was found in the literature searched; the target-organism evidence is genomic (single complete syntenic `nuo` operon) plus annotation, not direct enzymology.

---

## 10. Limitations and Knowledge Gaps

1. **No KT2440-specific functional data.** All catalytic/cofactor assignments are transferred by homology from *E. coli*/*Thermus*. Transfer is strong (deep conservation) but not experimentally verified in KT2440.
2. **Native quinone identity.** The physiological quinone (ubiquinone-9 vs menaquinone) and its exact affinity in KT2440 were not established here; this affects downstream OXPHOS reasoning but not the core mapping.
3. **NDH-2 vs NDH-1 flux partitioning.** KT2440 uses both NADH dehydrogenases; the relative in vivo contribution is condition-dependent and out of scope but relevant to any energetic module.
4. **Cofactor stoichiometry per subunit** (exact Fe-S cluster complement of nuoG/nuoI in KT2440) is inferred, not measured.
5. **Assembly factors.** Bacterial NDH-1 assembly factors were not surveyed; the module scope was the structural core only.

---

## 11. Proposed Follow-up Actions

1. **Promote PP_4121 (nuoCD), PP_4123 (nuoF) and PP_4120 (nuoB) to full `fetch-gene` review** to confirm the fusion boundary, FMN/NADH site and N2 cluster respectively.
2. **Author a bacterial NDH-1 module variant** mapping the seven core steps onto `nuo` genes, encoding the nuoCD-covers-two-steps rule, and declaring NDUFS4/S6/A9 as `not_expected_in_target_taxon`.
3. **Add exclusion flags** for `ndh`/PP_0626 (NDH-2) and PP_2867 so they cannot satisfy Complex I steps.
4. **Add a KEGG bucket caveat** documenting that `ppu00190` spans all five OXPHOS complexes.
5. **Optional experimental resolution:** targeted deletion or complementation of the KT2440 `nuo` operon, or purified-enzyme assays, would convert the current homology-based calls to direct evidence — but is likely unnecessary for satisfiability given the completeness and synteny of the locus.

---

## 12. Key References

- Efremov & Sazanov. *Structure of bacterial respiratory complex I.* [PMID: 26807915](https://pubmed.ncbi.nlm.nih.gov/26807915/)
- Baradaran et al. *Crystal structure of the entire respiratory complex I.* [PMID: 23417064](https://pubmed.ncbi.nlm.nih.gov/23417064/)
- *Conserved amino acid residues of the NuoD segment important for structure and function of E. coli NDH-1 (complex I).* [PMID: 25545070](https://pubmed.ncbi.nlm.nih.gov/25545070/)
- *Quinone chemistry in respiratory complex I involves protonation of a conserved aspartic acid residue.* [PMID: 39262040](https://pubmed.ncbi.nlm.nih.gov/39262040/)
- *Post-translational modifications near the quinone binding site of mammalian complex I.* [PMID: 23836892](https://pubmed.ncbi.nlm.nih.gov/23836892/)
- *Roles of Subunit ND2/NuoN in the Proton Pumping Coupling Mechanism of Complex I.* [PMID: 41977177](https://pubmed.ncbi.nlm.nih.gov/41977177/)
- *Redox-induced activation of the proton pump in the respiratory complex I.* [PMID: 26330610](https://pubmed.ncbi.nlm.nih.gov/26330610/)
- *Reduction potential calculations of the Fe-S clusters in T. thermophilus respiratory complex I.* [PMID: 30697773](https://pubmed.ncbi.nlm.nih.gov/30697773/)
- *Charge Transfer and Chemo-Mechanical Coupling in Respiratory Complex I.* [PMID: 32347721](https://pubmed.ncbi.nlm.nih.gov/32347721/)
- *Essential regions in the membrane domain of bacterial complex I (NDH-1).* [PMID: 24973951](https://pubmed.ncbi.nlm.nih.gov/24973951/)

---

*Prepared for manual module satisfiability and gene-annotation curation. Target organism: Pseudomonas putida KT2440 (taxon 160488). Evidence base: 21 papers reviewed, 5 findings confirmed across 3 iterations.*


## Artifacts

- [OpenScientist final report](PSEPK__mitochondrial_complex_i_core__ppu00190-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__mitochondrial_complex_i_core__ppu00190-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:41977177
2. PMID:26807915
3. PMID:25545070
4. PMID:39262040
5. PMID:23836892
6. PMID:26330610
7. PMID:23417064
8. PMID:30697773
9. PMID:32347721
10. PMID:24973951