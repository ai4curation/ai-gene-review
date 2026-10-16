---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T08:48:07.276122'
end_time: '2026-08-19T09:21:39.298845'
duration_seconds: 2012.02
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial purine base oxidation to urate
  module_summary: A reusable bacterial pathway realization in which xanthine is supplied
    by either zinc-dependent guanine deamination or NAD+-dependent hypoxanthine oxidation
    and is then oxidized to urate. In the two-subunit realization, the same XdhAB
    molybdo-flavo-iron-sulfur complex performs both NAD+-dependent oxidation reactions.
  module_outline: "- Bacterial purine base oxidation to urate\n  - 1. alternative\
    \ xanthine supply\n  - Alternative purine-base routes to xanthine\n    - Alternative\
    \ versions by purine base substrate: Xanthine supply variants\n      - Guanine\
    \ deamination to xanthine\n        - Guanine deaminase activity (molecular player:\
    \ guanine deaminase family; activity or role: guanine deaminase activity)\n  \
    \    - Hypoxanthine oxidation to xanthine\n        - XdhAB hypoxanthine dehydrogenase\
    \ activity (molecular player: two-subunit bacterial XdhAB complex; activity or\
    \ role: hypoxanthine dehydrogenase activity)\n  - 2. terminal xanthine oxidation\
    \ to urate\n  - XdhAB-dependent xanthine oxidation to urate\n    - XdhAB xanthine\
    \ dehydrogenase activity (molecular player: two-subunit bacterial XdhAB complex;\
    \ activity or role: xanthine dehydrogenase activity)"
  module_connections: '- Guanine deamination to xanthine precedes XdhAB-dependent
    xanthine oxidation to urate: The guanine branch converges on the terminal xanthine
    oxidation step.

    - Hypoxanthine oxidation to xanthine precedes XdhAB-dependent xanthine oxidation
    to urate: The hypoxanthine branch proceeds through xanthine to urate.'
  pathway_query: ppu00230
  pathway_id: ppu00230
  pathway_name: Purine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00230 with 36 primary genes; module
    area: nucleotide_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '65'
  candidate_genes: '- yrfG: PP_0259 | Q88R75 | Purine nucleotidase (EC 3.1.3.5) (EC
    3.1.3.5; primary bucket kegg:ppu00230)

    - nudE: PP_0260 | Q88R74 | ADP-sugar pyrophosphorylase (EC 3.6.1.21) (EC 3.6.1.21;
    primary bucket kegg:ppu00230)

    - apaH: PP_0399 | Q88QT8 | Bis(5''-nucleosyl)-tetraphosphatase, symmetrical (EC
    3.6.1.41) (Ap4A hydrolase) (Diadenosine 5'',5''''''-P1,P4-tetraphosphate pyrophosphohydrolase)
    (Diadenosine tetraphosphatase) (EC 3.6.1.41; primary bucket kegg:ppu00230)

    - PP_0591: PP_0591 | Q88QA3 | Adenine deaminase (ADE) (EC 3.5.4.2) (Adenine aminohydrolase)
    (AAH) (EC 3.5.4.2; primary bucket kegg:ppu00230)

    - yfiH: PP_0624 | Q88Q72 | Purine nucleoside phosphorylase (primary bucket kegg:ppu00270)

    - prs: PP_0722 | Q88PX6 | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1)
    (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate
    synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase)
    (PRPPase) (EC 2.7.6.1; primary bucket kegg:ppu00030)

    - PP_0747: PP_0747 | Q88PV1 | Hypoxanthine-guanine phosphoribosyltransferase (primary
    bucket kegg:ppu00230)

    - ndk: PP_0849 | Q88PK1 | Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC
    2.7.4.6) (Nucleoside-2-P kinase) (EC 2.7.4.6; primary bucket kegg:ppu00240)

    - arcC: PP_0999 | Q88P54 | Carbamate kinase (primary bucket kegg:ppu00910)

    - guaB: PP_1031 | Q88P22 | Inosine-5''-monophosphate dehydrogenase (IMP dehydrogenase)
    (IMPD) (IMPDH) (EC 1.1.1.205) (EC 1.1.1.205; primary bucket kegg:ppu00230)

    - guaA: PP_1032 | Q88P21 | GMP synthase [glutamine-hydrolyzing] (EC 6.3.5.2) (GMP
    synthetase) (Glutamine amidotransferase) (EC 6.3.5.2; primary bucket kegg:ppu00230)

    - purL: PP_1037 | Q88P16 | Phosphoribosylformylglycinamidine synthase (FGAM synthase)
    (FGAMS) (EC 6.3.5.3) (Formylglycinamide ribonucleotide amidotransferase) (FGAR
    amidotransferase) (FGAR-AT) (EC 6.3.5.3; primary bucket kegg:ppu00230)

    - nrdB: PP_1177 | Q88NN0 | Ribonucleoside-diphosphate reductase subunit beta (EC
    1.17.4.1) (EC 1.17.4.1; primary bucket kegg:ppu00240)

    - nrdA: PP_1179 | Q88NM8 | Ribonucleoside-diphosphate reductase (EC 1.17.4.1)
    (EC 1.17.4.1; primary bucket kegg:ppu00240)

    - purC: PP_1240 | Q88NG9 | Phosphoribosylaminoimidazole-succinocarboxamide synthase
    (EC 6.3.2.6) (SAICAR synthetase) (EC 6.3.2.6; primary bucket kegg:ppu00230)

    - cysD: PP_1303 | Q88NA9 | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4)
    (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4;
    primary bucket kegg:ppu00261)

    - cysNC: PP_1304 | Q88NA8 | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4)
    (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4;
    primary bucket kegg:ppu00261)

    - ushA: PP_1414 | Q88N04 | 5''-nucleotidase-2'',3''-cyclic phosphodiesterase (EC
    3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) (EC 3.1.3.5; 3.1.4.16; 3.6.1.45; primary bucket
    kegg:ppu00760)

    - purT: PP_1457 | Q88MW1 | Formate-dependent phosphoribosylglycinamide formyltransferase
    (EC 6.3.1.21) (5''-phosphoribosylglycinamide transformylase 2) (Formate-dependent
    GAR transformylase) (GAR transformylase 2) (GART 2) (Non-folate glycinamide ribonucleotide
    transformylase) (Phosphoribosylglycinamide formyltransferase 2) (EC 6.3.1.21;
    primary bucket kegg:ppu00230)

    - adk: PP_1506 | P0A136 | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase)
    (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase) (EC 2.7.4.3; primary
    bucket kegg:ppu00730)

    - surE: PP_1620 | Q88MF1 | 5''-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5''-monophosphate
    phosphohydrolase) (EC 3.1.3.5; primary bucket kegg:ppu00760)

    - relA: PP_1656 | Q88MB8 | GTP pyrophosphokinase ((p)ppGpp synthase) (ATP:GTP
    3''-pyrophosphotransferase) (ppGpp synthase I) (primary bucket kegg:ppu00230)

    - mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8)
    (EC 3.6.1.8; primary bucket kegg:ppu00770)

    - purN: PP_1664 | Q88MB0 | Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2)
    (5''-phosphoribosylglycinamide transformylase) (GAR transformylase) (GART) (EC
    2.1.2.2; primary bucket kegg:ppu00670)

    - purM: PP_1665 | Q88MA9 | Phosphoribosylformylglycinamidine cyclo-ligase (EC
    6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthetase) (EC
    6.3.3.1; primary bucket kegg:ppu00230)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - purF: PP_2000 | Q88LD5 | Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14)
    (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase) (EC 2.4.2.14;
    primary bucket kegg:ppu00250)

    - dgt: PP_2102 | Q88L33 | Deoxyguanosinetriphosphate triphosphohydrolase-like
    protein (primary bucket kegg:ppu00230)

    - PP_2531: PP_2531 | Q88JW6 | 5-nucleotidase (primary bucket kegg:ppu00760)

    - PP_2744: PP_2744 | Q88JA5 | ribose-phosphate diphosphokinase (EC 2.7.6.1) (EC
    2.7.6.1; primary bucket kegg:ppu00030)

    - ureA: PP_2843 | Q88J06 | Urease subunit gamma (EC 3.5.1.5) (Urea amidohydrolase
    subunit gamma) (EC 3.5.1.5; primary bucket kegg:ppu00220)

    - ureB: PP_2844 | Q88J05 | Urease subunit beta (EC 3.5.1.5) (Urea amidohydrolase
    subunit beta) (EC 3.5.1.5; primary bucket kegg:ppu00220)

    - ureC: PP_2845 | Q88J04 | Urease subunit alpha (EC 3.5.1.5) (Urea amidohydrolase
    subunit alpha) (EC 3.5.1.5; primary bucket kegg:ppu00220)

    - paoA: PP_3308 | Q88HP5 | Promiscuous aromatic aldehyde dehydrogenase, 2Fe-2S
    subunit (EC 1.2.99.7) (EC 1.2.99.7; primary bucket kegg:ppu00230)

    - paoB: PP_3309 | Q88HP4 | Promiscuous aromatic aldehyde dehydrogenase, FAD-binding
    subunit (EC 1.2.99.7) (EC 1.2.99.7; primary bucket kegg:ppu00230)

    - paoC: PP_3310 | Q88HP3 | Promiscuous aromatic aldehyde dehydrogenase, molybdopterin-binding
    subunit (EC 1.2.99.7) (EC 1.2.99.7; primary bucket kegg:ppu00230)

    - allE: PP_3530 | Q88H35 | S-ureidoglycine aminohydrolase (EC 3.5.3.-) (EC 3.5.3.-;
    primary bucket kegg:ppu00230)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - PP_3662: PP_3662 | Q88GQ6 | AMP nucleosidase (EC 3.2.2.4) (AMP nucleosidase)
    (EC 3.2.2.4; primary bucket kegg:ppu00240)

    - purB: PP_4016 | Q88FR7 | Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase)
    (EC 4.3.2.2; primary bucket kegg:ppu00250)

    - ppnP: PP_4248 | Q88F51 | Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1)
    (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase) (Guanosine phosphorylase)
    (Inosine phosphorylase) (Thymidine phosphorylase) (Uridine phosphorylase) (Xanthosine
    phosphorylase) (EC 2.4.2.1; 2.4.2.2; primary bucket kegg:ppu00240)

    - apt: PP_4266 | Q88F33 | Adenine phosphoribosyltransferase (APRT) (EC 2.4.2.7)
    (EC 2.4.2.7; primary bucket kegg:ppu00230)

    - xdhA: PP_4278 | Q88F21 | Xanthine dehydrogenase subunit XdhA (EC 1.17.1.4) (EC
    1.17.1.4; primary bucket kegg:ppu00230)

    - xdhB: PP_4279 | Q88F20 | Xanthine dehydrogenase subunit XdhB (EC 1.17.1.4) (EC
    1.17.1.4; primary bucket kegg:ppu00230)

    - guaD: PP_4281 | Q88F18 | Guanine deaminase (Guanase) (EC 3.5.4.3) (Guanine aminohydrolase)
    (EC 3.5.4.3; primary bucket kegg:ppu00230)

    - pucM: PP_4285 | Q88F14 | 5-hydroxyisourate hydrolase (HIU hydrolase) (HIUHase)
    (EC 3.5.2.17) (EC 3.5.2.17; primary bucket kegg:ppu00230)

    - puuE: PP_4286 | Q88F13 | Allantoinase (EC 3.5.2.5) (EC 3.5.2.5; primary bucket
    kegg:ppu00230)

    - pucL: PP_4287 | Q88F12 | 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline decarboxylase
    (EC 4.1.1.97) (EC 4.1.1.97; primary bucket kegg:ppu00230)

    - allA: PP_4288 | P59285 | Ureidoglycolate lyase (EC 4.3.2.3) (Ureidoglycolatase)
    (EC 4.3.2.3; primary bucket kegg:ppu00230)

    - PP_4310: PP_4310 | Q88EZ0 | Hydantoin racemase (EC 5.1.99.5) (EC 5.1.99.5; primary
    bucket kegg:ppu00230)

    - amn: PP_4779 | Q88DP5 | AMP nucleosidase (EC 3.2.2.4) (EC 3.2.2.4; primary bucket
    kegg:ppu00230)

    - purH: PP_4822 | Q88DK3 | Bifunctional purine biosynthesis protein PurH [Includes:
    Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR
    transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)]
    (EC 2.1.2.3; 3.5.4.10; primary bucket kegg:ppu00670)

    - purD: PP_4823 | Q88DK2 | Phosphoribosylamine--glycine ligase (EC 6.3.4.13) (GARS)
    (Glycinamide ribonucleotide synthetase) (Phosphoribosylglycinamide synthetase)
    (EC 6.3.4.13; primary bucket kegg:ppu00230)

    - purA: PP_4889 | Q88DD8 | Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4)
    (IMP--aspartate ligase) (EC 6.3.4.4; primary bucket kegg:ppu00250)

    - pde: PP_4917 | Q88DB0 | 3'',5''-cyclic-nucleotide phosphodiesterase (EC 3.1.4.17)
    (EC 3.1.4.17; primary bucket kegg:ppu02025)

    - nudF: PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose
    diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphoribose pyrophosphatase)
    (EC 3.6.1.13; primary bucket kegg:ppu00740)

    - PP_5100: PP_5100 | Q88CT0 | dITP/XTP pyrophosphatase (EC 3.6.1.66) (Non-canonical
    purine NTP pyrophosphatase) (Non-standard purine NTP pyrophosphatase) (Nucleoside-triphosphate
    diphosphatase) (Nucleoside-triphosphate pyrophosphatase) (NTPase) (EC 3.6.1.66;
    primary bucket kegg:ppu00230)

    - ppx: PP_5216 | Q88CG5 | Exopolyphosphatase (EC 3.6.1.11) (EC 3.6.1.11; primary
    bucket kegg:ppu00230)

    - cyaA: PP_5222 | Q88CF9 | Adenylate cyclase (EC 4.6.1.1, EC 4.6.1.6) (EC 4.6.1.1;
    4.6.1.6; primary bucket kegg:ppu00230)

    - xpt: PP_5265 | Q88CB6 | Xanthine phosphoribosyltransferase (XPRTase) (EC 2.4.2.22)
    (EC 2.4.2.22; primary bucket kegg:ppu00230)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

    - gmk: PP_5296 | Q88C87 | Guanylate kinase (EC 2.7.4.8) (GMP kinase) (EC 2.7.4.8;
    primary bucket kegg:ppu00230)

    - spoT: PP_5302 | Q88C81 | guanosine-3'',5''-bis(diphosphate) 3''-diphosphatase
    (EC 3.1.7.2) (EC 3.1.7.2; primary bucket kegg:ppu00230)

    - purK: PP_5335 | Q88C48 | N5-carboxyaminoimidazole ribonucleotide synthase (N5-CAIR
    synthase) (EC 6.3.4.18) (5-(carboxyamino)imidazole ribonucleotide synthetase)
    (EC 6.3.4.18; primary bucket kegg:ppu00230)

    - purE: PP_5336 | Q88C47 | N5-carboxyaminoimidazole ribonucleotide mutase (N5-CAIR
    mutase) (EC 5.4.99.18) (5-(carboxyamino)imidazole ribonucleotide mutase) (EC 5.4.99.18;
    primary bucket kegg:ppu00230)'
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
  path: PSEPK__bacterial_purine_base_oxidation_to_urate__ppu00230-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_purine_base_oxidation_to_urate__ppu00230-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial purine base oxidation to urate in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00230
- Resolved ID: ppu00230
- Resolved name: Purine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00230 with 36 primary genes; module area: nucleotide_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 65

- yrfG: PP_0259 | Q88R75 | Purine nucleotidase (EC 3.1.3.5) (EC 3.1.3.5; primary bucket kegg:ppu00230)
- nudE: PP_0260 | Q88R74 | ADP-sugar pyrophosphorylase (EC 3.6.1.21) (EC 3.6.1.21; primary bucket kegg:ppu00230)
- apaH: PP_0399 | Q88QT8 | Bis(5'-nucleosyl)-tetraphosphatase, symmetrical (EC 3.6.1.41) (Ap4A hydrolase) (Diadenosine 5',5'''-P1,P4-tetraphosphate pyrophosphohydrolase) (Diadenosine tetraphosphatase) (EC 3.6.1.41; primary bucket kegg:ppu00230)
- PP_0591: PP_0591 | Q88QA3 | Adenine deaminase (ADE) (EC 3.5.4.2) (Adenine aminohydrolase) (AAH) (EC 3.5.4.2; primary bucket kegg:ppu00230)
- yfiH: PP_0624 | Q88Q72 | Purine nucleoside phosphorylase (primary bucket kegg:ppu00270)
- prs: PP_0722 | Q88PX6 | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase) (PRPPase) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- PP_0747: PP_0747 | Q88PV1 | Hypoxanthine-guanine phosphoribosyltransferase (primary bucket kegg:ppu00230)
- ndk: PP_0849 | Q88PK1 | Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC 2.7.4.6) (Nucleoside-2-P kinase) (EC 2.7.4.6; primary bucket kegg:ppu00240)
- arcC: PP_0999 | Q88P54 | Carbamate kinase (primary bucket kegg:ppu00910)
- guaB: PP_1031 | Q88P22 | Inosine-5'-monophosphate dehydrogenase (IMP dehydrogenase) (IMPD) (IMPDH) (EC 1.1.1.205) (EC 1.1.1.205; primary bucket kegg:ppu00230)
- guaA: PP_1032 | Q88P21 | GMP synthase [glutamine-hydrolyzing] (EC 6.3.5.2) (GMP synthetase) (Glutamine amidotransferase) (EC 6.3.5.2; primary bucket kegg:ppu00230)
- purL: PP_1037 | Q88P16 | Phosphoribosylformylglycinamidine synthase (FGAM synthase) (FGAMS) (EC 6.3.5.3) (Formylglycinamide ribonucleotide amidotransferase) (FGAR amidotransferase) (FGAR-AT) (EC 6.3.5.3; primary bucket kegg:ppu00230)
- nrdB: PP_1177 | Q88NN0 | Ribonucleoside-diphosphate reductase subunit beta (EC 1.17.4.1) (EC 1.17.4.1; primary bucket kegg:ppu00240)
- nrdA: PP_1179 | Q88NM8 | Ribonucleoside-diphosphate reductase (EC 1.17.4.1) (EC 1.17.4.1; primary bucket kegg:ppu00240)
- purC: PP_1240 | Q88NG9 | Phosphoribosylaminoimidazole-succinocarboxamide synthase (EC 6.3.2.6) (SAICAR synthetase) (EC 6.3.2.6; primary bucket kegg:ppu00230)
- cysD: PP_1303 | Q88NA9 | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4; primary bucket kegg:ppu00261)
- cysNC: PP_1304 | Q88NA8 | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4; primary bucket kegg:ppu00261)
- ushA: PP_1414 | Q88N04 | 5'-nucleotidase-2',3'-cyclic phosphodiesterase (EC 3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) (EC 3.1.3.5; 3.1.4.16; 3.6.1.45; primary bucket kegg:ppu00760)
- purT: PP_1457 | Q88MW1 | Formate-dependent phosphoribosylglycinamide formyltransferase (EC 6.3.1.21) (5'-phosphoribosylglycinamide transformylase 2) (Formate-dependent GAR transformylase) (GAR transformylase 2) (GART 2) (Non-folate glycinamide ribonucleotide transformylase) (Phosphoribosylglycinamide formyltransferase 2) (EC 6.3.1.21; primary bucket kegg:ppu00230)
- adk: PP_1506 | P0A136 | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase) (EC 2.7.4.3; primary bucket kegg:ppu00730)
- surE: PP_1620 | Q88MF1 | 5'-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5'-monophosphate phosphohydrolase) (EC 3.1.3.5; primary bucket kegg:ppu00760)
- relA: PP_1656 | Q88MB8 | GTP pyrophosphokinase ((p)ppGpp synthase) (ATP:GTP 3'-pyrophosphotransferase) (ppGpp synthase I) (primary bucket kegg:ppu00230)
- mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) (EC 3.6.1.8; primary bucket kegg:ppu00770)
- purN: PP_1664 | Q88MB0 | Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2) (5'-phosphoribosylglycinamide transformylase) (GAR transformylase) (GART) (EC 2.1.2.2; primary bucket kegg:ppu00670)
- purM: PP_1665 | Q88MA9 | Phosphoribosylformylglycinamidine cyclo-ligase (EC 6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthetase) (EC 6.3.3.1; primary bucket kegg:ppu00230)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- purF: PP_2000 | Q88LD5 | Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14) (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase) (EC 2.4.2.14; primary bucket kegg:ppu00250)
- dgt: PP_2102 | Q88L33 | Deoxyguanosinetriphosphate triphosphohydrolase-like protein (primary bucket kegg:ppu00230)
- PP_2531: PP_2531 | Q88JW6 | 5-nucleotidase (primary bucket kegg:ppu00760)
- PP_2744: PP_2744 | Q88JA5 | ribose-phosphate diphosphokinase (EC 2.7.6.1) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- ureA: PP_2843 | Q88J06 | Urease subunit gamma (EC 3.5.1.5) (Urea amidohydrolase subunit gamma) (EC 3.5.1.5; primary bucket kegg:ppu00220)
- ureB: PP_2844 | Q88J05 | Urease subunit beta (EC 3.5.1.5) (Urea amidohydrolase subunit beta) (EC 3.5.1.5; primary bucket kegg:ppu00220)
- ureC: PP_2845 | Q88J04 | Urease subunit alpha (EC 3.5.1.5) (Urea amidohydrolase subunit alpha) (EC 3.5.1.5; primary bucket kegg:ppu00220)
- paoA: PP_3308 | Q88HP5 | Promiscuous aromatic aldehyde dehydrogenase, 2Fe-2S subunit (EC 1.2.99.7) (EC 1.2.99.7; primary bucket kegg:ppu00230)
- paoB: PP_3309 | Q88HP4 | Promiscuous aromatic aldehyde dehydrogenase, FAD-binding subunit (EC 1.2.99.7) (EC 1.2.99.7; primary bucket kegg:ppu00230)
- paoC: PP_3310 | Q88HP3 | Promiscuous aromatic aldehyde dehydrogenase, molybdopterin-binding subunit (EC 1.2.99.7) (EC 1.2.99.7; primary bucket kegg:ppu00230)
- allE: PP_3530 | Q88H35 | S-ureidoglycine aminohydrolase (EC 3.5.3.-) (EC 3.5.3.-; primary bucket kegg:ppu00230)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- PP_3662: PP_3662 | Q88GQ6 | AMP nucleosidase (EC 3.2.2.4) (AMP nucleosidase) (EC 3.2.2.4; primary bucket kegg:ppu00240)
- purB: PP_4016 | Q88FR7 | Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase) (EC 4.3.2.2; primary bucket kegg:ppu00250)
- ppnP: PP_4248 | Q88F51 | Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1) (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase) (Guanosine phosphorylase) (Inosine phosphorylase) (Thymidine phosphorylase) (Uridine phosphorylase) (Xanthosine phosphorylase) (EC 2.4.2.1; 2.4.2.2; primary bucket kegg:ppu00240)
- apt: PP_4266 | Q88F33 | Adenine phosphoribosyltransferase (APRT) (EC 2.4.2.7) (EC 2.4.2.7; primary bucket kegg:ppu00230)
- xdhA: PP_4278 | Q88F21 | Xanthine dehydrogenase subunit XdhA (EC 1.17.1.4) (EC 1.17.1.4; primary bucket kegg:ppu00230)
- xdhB: PP_4279 | Q88F20 | Xanthine dehydrogenase subunit XdhB (EC 1.17.1.4) (EC 1.17.1.4; primary bucket kegg:ppu00230)
- guaD: PP_4281 | Q88F18 | Guanine deaminase (Guanase) (EC 3.5.4.3) (Guanine aminohydrolase) (EC 3.5.4.3; primary bucket kegg:ppu00230)
- pucM: PP_4285 | Q88F14 | 5-hydroxyisourate hydrolase (HIU hydrolase) (HIUHase) (EC 3.5.2.17) (EC 3.5.2.17; primary bucket kegg:ppu00230)
- puuE: PP_4286 | Q88F13 | Allantoinase (EC 3.5.2.5) (EC 3.5.2.5; primary bucket kegg:ppu00230)
- pucL: PP_4287 | Q88F12 | 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline decarboxylase (EC 4.1.1.97) (EC 4.1.1.97; primary bucket kegg:ppu00230)
- allA: PP_4288 | P59285 | Ureidoglycolate lyase (EC 4.3.2.3) (Ureidoglycolatase) (EC 4.3.2.3; primary bucket kegg:ppu00230)
- PP_4310: PP_4310 | Q88EZ0 | Hydantoin racemase (EC 5.1.99.5) (EC 5.1.99.5; primary bucket kegg:ppu00230)
- amn: PP_4779 | Q88DP5 | AMP nucleosidase (EC 3.2.2.4) (EC 3.2.2.4; primary bucket kegg:ppu00230)
- purH: PP_4822 | Q88DK3 | Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)] (EC 2.1.2.3; 3.5.4.10; primary bucket kegg:ppu00670)
- purD: PP_4823 | Q88DK2 | Phosphoribosylamine--glycine ligase (EC 6.3.4.13) (GARS) (Glycinamide ribonucleotide synthetase) (Phosphoribosylglycinamide synthetase) (EC 6.3.4.13; primary bucket kegg:ppu00230)
- purA: PP_4889 | Q88DD8 | Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4) (IMP--aspartate ligase) (EC 6.3.4.4; primary bucket kegg:ppu00250)
- pde: PP_4917 | Q88DB0 | 3',5'-cyclic-nucleotide phosphodiesterase (EC 3.1.4.17) (EC 3.1.4.17; primary bucket kegg:ppu02025)
- nudF: PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphoribose pyrophosphatase) (EC 3.6.1.13; primary bucket kegg:ppu00740)
- PP_5100: PP_5100 | Q88CT0 | dITP/XTP pyrophosphatase (EC 3.6.1.66) (Non-canonical purine NTP pyrophosphatase) (Non-standard purine NTP pyrophosphatase) (Nucleoside-triphosphate diphosphatase) (Nucleoside-triphosphate pyrophosphatase) (NTPase) (EC 3.6.1.66; primary bucket kegg:ppu00230)
- ppx: PP_5216 | Q88CG5 | Exopolyphosphatase (EC 3.6.1.11) (EC 3.6.1.11; primary bucket kegg:ppu00230)
- cyaA: PP_5222 | Q88CF9 | Adenylate cyclase (EC 4.6.1.1, EC 4.6.1.6) (EC 4.6.1.1; 4.6.1.6; primary bucket kegg:ppu00230)
- xpt: PP_5265 | Q88CB6 | Xanthine phosphoribosyltransferase (XPRTase) (EC 2.4.2.22) (EC 2.4.2.22; primary bucket kegg:ppu00230)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)
- gmk: PP_5296 | Q88C87 | Guanylate kinase (EC 2.7.4.8) (GMP kinase) (EC 2.7.4.8; primary bucket kegg:ppu00230)
- spoT: PP_5302 | Q88C81 | guanosine-3',5'-bis(diphosphate) 3'-diphosphatase (EC 3.1.7.2) (EC 3.1.7.2; primary bucket kegg:ppu00230)
- purK: PP_5335 | Q88C48 | N5-carboxyaminoimidazole ribonucleotide synthase (N5-CAIR synthase) (EC 6.3.4.18) (5-(carboxyamino)imidazole ribonucleotide synthetase) (EC 6.3.4.18; primary bucket kegg:ppu00230)
- purE: PP_5336 | Q88C47 | N5-carboxyaminoimidazole ribonucleotide mutase (N5-CAIR mutase) (EC 5.4.99.18) (5-(carboxyamino)imidazole ribonucleotide mutase) (EC 5.4.99.18; primary bucket kegg:ppu00230)

## Generic Module Context

### Working Scope

A reusable bacterial pathway realization in which xanthine is supplied by either zinc-dependent guanine deamination or NAD+-dependent hypoxanthine oxidation and is then oxidized to urate. In the two-subunit realization, the same XdhAB molybdo-flavo-iron-sulfur complex performs both NAD+-dependent oxidation reactions.

### Provisional Biological Outline

- Bacterial purine base oxidation to urate
  - 1. alternative xanthine supply
  - Alternative purine-base routes to xanthine
    - Alternative versions by purine base substrate: Xanthine supply variants
      - Guanine deamination to xanthine
        - Guanine deaminase activity (molecular player: guanine deaminase family; activity or role: guanine deaminase activity)
      - Hypoxanthine oxidation to xanthine
        - XdhAB hypoxanthine dehydrogenase activity (molecular player: two-subunit bacterial XdhAB complex; activity or role: hypoxanthine dehydrogenase activity)
  - 2. terminal xanthine oxidation to urate
  - XdhAB-dependent xanthine oxidation to urate
    - XdhAB xanthine dehydrogenase activity (molecular player: two-subunit bacterial XdhAB complex; activity or role: xanthine dehydrogenase activity)

### Known Relationships Among Steps

- Guanine deamination to xanthine precedes XdhAB-dependent xanthine oxidation to urate: The guanine branch converges on the terminal xanthine oxidation step.
- Hypoxanthine oxidation to xanthine precedes XdhAB-dependent xanthine oxidation to urate: The hypoxanthine branch proceeds through xanthine to urate.

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

# Module Review: Bacterial Purine Base Oxidation to Urate in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00230 "Purine metabolism" (module area: nucleotide_metabolism)
**Module under review:** *Bacterial purine base oxidation to urate* — guanine and hypoxanthine converge on xanthine, which is oxidized to urate.
**Date:** 2026-08-19

---

## 1. Executive summary

The purine-base oxidation-to-urate module is **present and functional** in *P. putida* KT2440. The organism uses adenine, guanine, hypoxanthine, xanthine and uric acid as **sole nitrogen sources**, direct strain-level evidence from the McpH chemoreceptor study (PMID 26355499). All catalytic steps of the module are encoded within a single contiguous purine-catabolic gene island (**PP_4278–PP_4290**):

- **Terminal step (xanthine → urate)** and **hypoxanthine → xanthine**: the two-subunit NAD⁺-dependent xanthine dehydrogenase **XdhAB** (PP_4278 / PP_4279, EC 1.17.1.4), matured by the accessory factor **XdhC** (PP_4280, *absent from candidate metadata*).
- **Guanine → xanthine**: guanine deaminase **guaD** (PP_4281, EC 3.5.4.3).

Two curation-critical issues: (1) **PaoABC (PP_3308–PP_3310)** is bucketed in ppu00230 but is a **periplasmic aldehyde oxidoreductase**, not a xanthine oxidase — a likely over-propagated annotation that must **not** be counted toward the terminal step. (2) **xdhC (PP_4280)** is a required accessory factor missing from the candidate list. The module boundary should stop at urate; the co-localized HIU/allantoin genes (PP_4285–PP_4288) and uric-acid permease (uacT, PP_4290) belong to the **downstream urate-degradation module**.

Overall satisfiability: **COVERED** for all three module steps, with high confidence.

---

## 2. Target-organism pathway definition

**Included biochemistry (module scope):**
- Guanine + H₂O → xanthine + NH₃ (guanine deaminase, Zn-dependent amidohydrolase; EC 3.5.4.3)
- Hypoxanthine + NAD⁺ + H₂O → xanthine + NADH (xanthine dehydrogenase; EC 1.17.1.4)
- Xanthine + NAD⁺ + H₂O → urate + NADH (xanthine dehydrogenase; EC 1.17.1.4)

**Neighboring processes to keep separate:**
- **De novo purine biosynthesis / IMP–AMP–GMP interconversion and salvage** (purF, purL, purM, purN, purH, purD, purC, purK, purE, purB, purA, guaA, guaB, apt, xpt, hpt/PP_0747, prs, gmk, adk, ndk, nrdAB, etc.). These dominate the 65-gene candidate list but are **anabolic/salvage** functions, **not** catabolic oxidation to urate. Exclude from this module.
- **Urate degradation to allantoin / glyoxylate + urea** (urate oxidase → HIU → OHCU → allantoin → allantoate → ureidoglycolate; pucM PP_4285, pucL PP_4287, puuE PP_4286, allA PP_4288, allE PP_3530, PP_4310, ureABC PP_2843-5). This is the **next** module downstream of urate.
- **Adenine deamination to hypoxanthine** (adenine deaminase PP_0591, EC 3.5.4.2) feeds the hypoxanthine branch but sits one step **upstream** of the module boundary (module begins at guanine/hypoxanthine).
- **Nucleotide/nucleoside catabolism upstream of free bases** (5′-nucleotidases, purine nucleoside phosphorylases ppnP/yfiH/deoD) — feeder reactions, separate.

**Alternate names / database definitions:** KEGG lumps all of the above into a single overview map ppu00230 "Purine metabolism"; the oxidation-to-urate segment corresponds to the classic **purine catabolism / purine dissimilation** pathway (MetaCyc "purine nucleobases degradation", "guanine and adenine ring degradation"). EC 1.17.1.4 (NAD⁺-dependent xanthine **dehydrogenase**) should be distinguished from EC 1.17.3.2 (O₂-dependent xanthine **oxidase**) — KT2440 is annotated as the dehydrogenase.

---

## 3. Expected step model and satisfiability calls

| Module step | Reaction | KT2440 gene(s) | Call |
|---|---|---|---|
| Guanine supply | guanine → xanthine | **guaD** PP_4281 (EC 3.5.4.3) | **covered** |
| Hypoxanthine supply | hypoxanthine → xanthine | **xdhA/xdhB** PP_4278/PP_4279 (EC 1.17.1.4), + xdhC PP_4280 | **covered** |
| Terminal oxidation | xanthine → urate | **xdhA/xdhB** PP_4278/PP_4279 (EC 1.17.1.4), + xdhC PP_4280 | **covered** |
| (accessory) | MoCo maturation/sulfuration for Xdh | **xdhC** PP_4280 | covered (add to module) |

**Not part of this module (keep separate / boundary):** urate → HIU (urate oxidase; no co-clustered classical uricase identified — see §5), HIU/OHCU/allantoin genes, uacT permease, adenine deaminase.

---

## 4. Candidate genes and evidence

### High-confidence, in-module

- **xdhA — PP_4278 (Q88F21), EC 1.17.1.4.** Small subunit of the two-component bacterial xanthine dehydrogenase (2Fe-2S/FAD module). Evidence: sequence/annotation + genomic context (head of the catabolic island). A single XdhAB (EC 1.17.1.4) canonically performs **both** hypoxanthine→xanthine and xanthine→urate, satisfying two module steps. Caveat: no direct KT2440 enzymology published; assignment rests on strong orthology + operon context.
- **xdhB — PP_4279 (Q88F20), EC 1.17.1.4.** Large molybdopterin (MoCo)-binding catalytic subunit (799 aa). Same evidence and caveats as xdhA. Together XdhAB is the "two-subunit XdhAB complex" of the generic module realization.
- **xdhC — PP_4280 (Q88F19), EC 1.17.1.4 (accessory).** XdhC-family maturation factor (MoCo sulfuration / cofactor insertion), immediately downstream of xdhB. **Not in the candidate metadata** — should be added to the module as a required accessory (non-catalytic) component. Promote to full review.
- **guaD — PP_4281 (Q88F18), EC 3.5.4.3.** Guanine deaminase (guanine aminohydrolase), the guanine-supply branch to xanthine. Adjacent to xdhABC in the island. UniProt confirms it **binds 1 Zn²⁺ per subunit** (metallo-dependent hydrolase superfamily), **exactly matching the generic module's "zinc-dependent guanine deamination"** realization. Evidence: orthology + operon context + cofactor annotation; no direct KT2440 assay found but assignment strong.

### Direct physiological support (strain-level)

- **McpH — PP_2643 (not in candidate list; chemoreceptor).** Binds adenine, guanine, xanthine, hypoxanthine, uric acid; enables their use as sole N sources (PMID 26355499). Confirms flux through the module in vivo. Not an enzyme of the module but the strongest **direct KT2440 evidence** that the pathway operates.

### In bucket but OUTSIDE this module (boundary/feeder)

- **PP_0591 adenine deaminase (EC 3.5.4.2)** — adenine → hypoxanthine; upstream feeder.
- **pucM PP_4285, pucL PP_4287, puuE PP_4286, allA PP_4288, allE PP_3530, PP_4310** — downstream urate/allantoin degradation.
- **uacT PP_4290 (uric acid permease)** — urate uptake; module-boundary transporter (missing from candidate list).
- **De novo/salvage purine genes** (purF/L/M/N/H/D/C/K/E, purA/B, guaA/B, apt, xpt, PP_0747 hpt, prs, gmk, adk, ndk, nrdAB, ppnP, amn, PP_3662, dgt, PP_5100, cyaA, relA/spoT, ushA, surE, yrfG, nudE/F, apaH, mazG, ppx, etc.) — anabolic, salvage, signalling, or generic nucleotide housekeeping; **not** oxidation-to-urate.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **PaoABC (PP_3308/09/10) — likely over-propagated into ppu00230.** Annotated "promiscuous aromatic aldehyde dehydrogenase (EC 1.2.99.7)." The *E. coli* ortholog is the **periplasmic aldehyde oxidoreductase** — a molybdopterin-cytosine-dinucleotide heterotrimer of the xanthine-oxidase **structural** family whose physiological role is **aldehyde detoxification**, with a surface-exposed active site lacking aromatic residues (PMID 27622978; PMID 24492481; Tat-exported heterotrimer, PMID 25531212). Reinforced by **genomic context**: in KT2440 the paoABC operon (subunit sizes PaoA 175 aa / PaoB 333 aa / PaoC 738 aa, matching *E. coli*) is flanked by Rho termination factor (PP_3307), a K⁺/H⁺ antiporter (PP_3311) and a heat-shock protein (PP_3312) — **no purine-catabolic genes nearby**. **Do not count toward xanthine→urate.** Recommend mark as **not-in-module / mis-bucketed** and flag EC 1.2.99.7 (not 1.17.1.4).
2. **xdhC (PP_4280) missing from candidate metadata** — required accessory factor; add to module.
3. **uacT (PP_4290) missing** — uric acid permease at the module boundary.
4. **Downstream uricase identified (gap closed).** No classical uricase is *co-clustered* with xdhABC, but a proteome search identifies **puuD (PP_3099), "Uricase/urate oxidase" (EC 1.7.3.3), 500 aa**, which performs urate → 5-hydroxyisourate — the **first step of the NEXT (urate-degradation) module**, feeding pucM/pucL. No enterobacterial-type HpxO FAD-monooxygenase or HpxDE Rieske system is present, consistent with the conventional molybdoflavo route. This confirms the terminal boundary of the oxidation-to-urate module sits cleanly at urate, with PuuD initiating downstream catabolism.
5. **Lineage-specific alternative realization exists.** In enterobacteria (e.g., *Klebsiella oxytoca/pneumoniae*) (hypo)xanthine→urate is done by a **Rieske two-component oxygenase HpxDE**, not by molybdoflavo XdhAB (PMID 19060149). KT2440 uses the **conventional molybdoflavo XdhAB** route; the generic "two-subunit XdhAB" realization fits. Transfer of any Hpx-based annotation to KT2440 would be **incorrect**.
6. **No direct KT2440 enzymology** for XdhAB or GuaD substrate range; assignments are homology + genomic-context + physiology (growth on purines). Confidence high but not biochemically proven in-strain.

---

## 6. Module and GO-curation recommendations

- **Mark COVERED:** guanine→xanthine (guaD PP_4281); hypoxanthine→xanthine (XdhAB PP_4278/79); xanthine→urate (XdhAB PP_4278/79). Confidence: high (orthology + operon + physiology).
- **Add to module:** **xdhC PP_4280** as accessory/maturation factor (GO:0043545 molybdopterin cofactor metabolic/insertion context; associate with XdhAB assembly). Consider adding **uacT PP_4290** as the associated urate transporter (module boundary).
- **Exclude / re-bucket:** **PaoABC PP_3308-3310** — remove from the purine-oxidation module; annotate as periplasmic aldehyde oxidoreductase (EC 1.2.99.7). Recommend flag as **over-propagated** in ppu00230.
- **Boundary correction:** the generic module correctly ends at urate. Keep the HIU/OHCU/allantoin genes and ureases in the separate **urate/allantoin degradation** module; do not let ppu00230's overview scope merge them.
- **GO term adequacy:** existing GO terms suffice — GO:0004855 (xanthine dehydrogenase activity)/GO:0004854 (xanthine oxidase) for XdhAB, GO:0008892 (guanine deaminase activity) for guaD. No new GO requests appear necessary. A **new module document is not needed**; only metadata edits (add xdhC, drop PaoABC).
- **module_needs_revision:** minor — add xdhC, remove/flag PaoABC.

---

## 7. Genes to promote to full `fetch-gene` review

1. **xdhC — PP_4280** (missing accessory factor; confirm role and module membership).
2. **PaoABC — PP_3308/PP_3309/PP_3310** (resolve mis-bucketing; confirm EC 1.2.99.7 aldehyde-oxidoreductase function, exclude from module).
3. **guaD — PP_4281** and **xdhA/xdhB — PP_4278/PP_4279** (confirm substrate range; ideally direct evidence that a single XdhAB does both hypoxanthine and xanthine oxidation in KT2440).
4. **Cryptic urate oxidase** search (downstream): identify the uricase feeding pucM/pucL, since none is co-clustered.

---

## 8. Key references

- Fernández M, Morel B, Corral-Lugo A, Krell T. *Identification of a chemoreceptor that specifically mediates chemotaxis toward metabolizable purine derivatives.* Mol Microbiol. 2016. **PMID 26355499.** — Direct KT2440 evidence: adenine, guanine, xanthine, hypoxanthine, uric acid used as sole N sources.
- Correia MAS, et al. *The Escherichia coli Periplasmic Aldehyde Oxidoreductase Is an Exceptional Member of the Xanthine Oxidase Family of Molybdoenzymes.* J Biol Chem/Biochemistry 2016. **PMID 27622978.** — PaoABC is an aldehyde oxidoreductase, not a xanthine oxidase.
- Otrelo-Cardoso AR, et al. *Structural data on the periplasmic aldehyde oxidoreductase PaoABC…* 2014. **PMID 24492481.** — PaoABC role = aldehyde detoxification.
- Lee PA, et al. *…natural three-component hitchhiker mechanism (PaoABC Tat export).* 2014. **PMID 25531212.** — PaoABC is a periplasmic (Tat-exported) heterotrimer.
- Pope SD, Chen L-L, Stewart V. *Purine utilization by Klebsiella oxytoca M5al: genes for ring-oxidizing and -opening enzymes.* J Bacteriol. 2009. **PMID 19060149.** — Enterobacterial Rieske HpxDE alternative vs. conventional molybdoflavo xanthine dehydrogenase.
- UniProt (proteome UP000000556) locus annotations PP_4277–PP_4291 — purine-catabolic gene island (xdhABC, guaD, pucM/puuE/pucL/allA, uacT).

---

### Confidence & species-transfer notes
- **Direct KT2440 experimental:** growth on purines / N-source use and chemotaxis (PMID 26355499).
- **Homology + genomic context (strong transfer):** XdhAB, XdhC, GuaD identities and operon structure (UniProt/KEGG for PSEPK itself — not cross-species).
- **Comparative (function-defining, from related taxa):** PaoABC function (*E. coli*); Rieske HpxDE alternative (*Klebsiella*) — used to *exclude* mis-annotations, transfer of the negative/alternative is appropriate.
- **Not established in-strain:** purified-enzyme kinetics of KT2440 XdhAB/GuaD; identity of the downstream uricase.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_purine_base_oxidation_to_urate__ppu00230-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_purine_base_oxidation_to_urate__ppu00230-deep-research-openscientist_artifacts/final_report.pdf)