---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T08:34:52.696804'
end_time: '2026-08-13T09:01:44.251025'
duration_seconds: 1611.55
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial purine nucleoside and nucleobase salvage
  module_summary: A reusable bacterial salvage module in which purine nucleosides
    are phosphorolyzed to free bases and ribose 1-phosphate, after which adenine,
    hypoxanthine or guanine, and xanthine are returned to the nucleotide pool as AMP,
    IMP or GMP, and XMP. The three phosphoribosyltransferase branches use PRPP and
    release diphosphate.
  module_outline: "- Bacterial purine nucleoside and nucleobase salvage\n  - 1. liberation\
    \ of purine bases from nucleosides\n  - Purine nucleoside phosphorolysis\n   \
    \ - PpnP purine-nucleoside phosphorylase activity (molecular player: PpnP pyrimidine/purine\
    \ nucleoside phosphorylase family; activity or role: purine-nucleoside phosphorylase\
    \ activity)\n  - 2. adenine salvage\n  - Adenine conversion to AMP\n    - Apt\
    \ adenine phosphoribosyltransferase activity (molecular player: Adenine phosphoribosyltransferase\
    \ family; activity or role: adenine phosphoribosyltransferase activity)\n  - 3.\
    \ hypoxanthine and guanine salvage\n  - Hypoxanthine and guanine conversion to\
    \ IMP and GMP\n    - HGPRT hypoxanthine-guanine phosphoribosyltransferase activity\
    \ (molecular player: Hypoxanthine-guanine phosphoribosyltransferase family; activity\
    \ or role: hypoxanthine phosphoribosyltransferase activity)\n  - 4. xanthine salvage\n\
    \  - Xanthine conversion to XMP\n    - Xpt xanthine phosphoribosyltransferase\
    \ activity (molecular player: Xanthine phosphoribosyltransferase subfamily; activity\
    \ or role: xanthine phosphoribosyltransferase activity)"
  module_connections: '- Purine nucleoside phosphorolysis feeds into Adenine conversion
    to AMP: PpnP can release adenine from adenosine for Apt-dependent salvage.

    - Purine nucleoside phosphorolysis feeds into Hypoxanthine and guanine conversion
    to IMP and GMP: PpnP can release hypoxanthine or guanine from inosine or guanosine
    for HGPRT-dependent salvage.

    - Purine nucleoside phosphorolysis feeds into Xanthine conversion to XMP: PpnP
    can release xanthine from xanthosine for Xpt-dependent salvage.'
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
  path: PSEPK__bacterial_purine_salvage__ppu00230-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_purine_salvage__ppu00230-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial purine nucleoside and nucleobase salvage in Pseudomonas putida KT2440

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

A reusable bacterial salvage module in which purine nucleosides are phosphorolyzed to free bases and ribose 1-phosphate, after which adenine, hypoxanthine or guanine, and xanthine are returned to the nucleotide pool as AMP, IMP or GMP, and XMP. The three phosphoribosyltransferase branches use PRPP and release diphosphate.

### Provisional Biological Outline

- Bacterial purine nucleoside and nucleobase salvage
  - 1. liberation of purine bases from nucleosides
  - Purine nucleoside phosphorolysis
    - PpnP purine-nucleoside phosphorylase activity (molecular player: PpnP pyrimidine/purine nucleoside phosphorylase family; activity or role: purine-nucleoside phosphorylase activity)
  - 2. adenine salvage
  - Adenine conversion to AMP
    - Apt adenine phosphoribosyltransferase activity (molecular player: Adenine phosphoribosyltransferase family; activity or role: adenine phosphoribosyltransferase activity)
  - 3. hypoxanthine and guanine salvage
  - Hypoxanthine and guanine conversion to IMP and GMP
    - HGPRT hypoxanthine-guanine phosphoribosyltransferase activity (molecular player: Hypoxanthine-guanine phosphoribosyltransferase family; activity or role: hypoxanthine phosphoribosyltransferase activity)
  - 4. xanthine salvage
  - Xanthine conversion to XMP
    - Xpt xanthine phosphoribosyltransferase activity (molecular player: Xanthine phosphoribosyltransferase subfamily; activity or role: xanthine phosphoribosyltransferase activity)

### Known Relationships Among Steps

- Purine nucleoside phosphorolysis feeds into Adenine conversion to AMP: PpnP can release adenine from adenosine for Apt-dependent salvage.
- Purine nucleoside phosphorolysis feeds into Hypoxanthine and guanine conversion to IMP and GMP: PpnP can release hypoxanthine or guanine from inosine or guanosine for HGPRT-dependent salvage.
- Purine nucleoside phosphorolysis feeds into Xanthine conversion to XMP: PpnP can release xanthine from xanthosine for Xpt-dependent salvage.

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

# Module Review: Bacterial Purine Nucleoside & Nucleobase Salvage in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI:txid160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00230` "Purine metabolism" (broad overview map)
**Module area:** nucleotide_metabolism
**Purpose:** species-aware curation review supporting manual module satisfiability and gene-annotation triage. Curation verdicts use the controlled vocabulary: `covered`, `candidate_uncertain`, `gap`, `not_expected_in_target_taxon`, `module_needs_revision`.

---

## 1. Executive summary

The commissioned module — *phosphorolysis of purine nucleosides followed by re-fixation of the free bases to nucleotides* — is a **narrow 4-step process**, whereas the 65-gene candidate list is a projection of the entire KEGG overview map `ppu00230` plus ~15 neighboring buckets. **Only 4 of the 65 candidates encode true salvage steps:** `ppnP` (PP_4248), `apt` (PP_4266), `hpt` (PP_0747) and `xpt` (PP_5265). The other 61 belong to de novo IMP biosynthesis, nucleotide interconversion/kinases, purine **catabolism**/ureide nitrogen assimilation, housekeeping nucleotidases/Nudix hydrolases, and nucleotide-based signalling, and should be scored as neighboring-pathway context, not salvage evidence.

The module is **nominally satisfiable**. The three phosphoribosyltransferase (PRT) branches are all present:
- **Adenine → AMP** (`apt`/PP_4266) — `covered`, high-quality (SwissProt-reviewed, EC 2.4.2.7).
- **Xanthine → XMP** (`xpt`/PP_5265) — `covered`, reviewed (EC 2.4.2.22).
- **Hypoxanthine/Guanine → IMP/GMP** (`hpt`/PP_0747) — `covered` but **`candidate_uncertain`** (unreviewed, "Predicted", no EC assigned).

The **one substantive weakness is step 1 (nucleoside phosphorolysis).** A proteome-wide UniProt search shows that the **only** enzyme in KT2440 bearing EC 2.4.2.1 is the accessory Cupin-fold **PpnP** (PP_4248); there is **no DeoD (PNP-I) or XapA (PNP-II) ortholog** — the canonical high-flux bacterial purine nucleoside phosphorylases. The best uncharacterised candidate for a classical phosphorylase is **PP_3254** (PF01048 / IPR000845 "nucleoside phosphorylase domain"), which is **absent from the candidate list**. `yfiH`/PP_0624, listed as "purine nucleoside phosphorylase", is an **unreviewed, EC-less, likely over-propagated annotation** (YfiH/DUF152 polyphenol-oxidase-like family) and should not be counted.

---

## 2. Target-organism pathway definition

**Included (this module):** the salvage arm only —
1. Phosphorolytic cleavage of purine ribonucleosides (adenosine, inosine, guanosine, xanthosine) → free base + α-D-ribose-1-phosphate;
2. Adenine + PRPP → AMP + PPi (APRT);
3. Hypoxanthine/Guanine + PRPP → IMP/GMP + PPi (HGPRT);
4. Xanthine + PRPP → XMP + PPi (XPRT).

All three PRT branches consume **PRPP** (supplied by `prs`/PP_0722 and the second PRPP synthase PP_2744) and release **diphosphate**; this is a boundary input, not a salvage step.

**Explicitly kept separate (neighboring maps / must not be scored as salvage):**
- **De novo IMP biosynthesis** (`purF, purD, purN, purT, purL, purM, purK, purE, purC, purB, purH`) and the IMP→AMP/GMP branch (`purA, purB, guaA, guaB`).
- **Nucleotide interconversion / kinases** (`adk, gmk, ndk, nrdAB`, `prs`, `PP_2744`).
- **Purine catabolism → ureide/nitrogen assimilation** (`xdhAB` xanthine dehydrogenase; `pucL, pucM, puuE, allA, allE, PP_4310`; `ureABC`). This is a *distinct* degradative pathway (purine → urate → allantoin → glyoxylate + NH₃/urea) and in *P. putida* underlies purine/allantoin use as N-source. It should be its **own module**, not folded into salvage.
- **Molybdo-hydroxylase mis-mapping:** `paoABC` (PP_3308–3310), annotated "promiscuous aromatic **aldehyde** dehydrogenase" (EC 1.2.99.7), is a PaoABC-type aldehyde oxidoreductase erroneously projected onto the purine map — **not** a purine enzyme.
- **Housekeeping nucleotidases / Nudix / NTP-sanitising** (`yrfG, surE, ushA, PP_2531, nudE, nudF, mazG, apaH, PP_5100, dgt`) and **nucleotide signalling** (`relA, spoT, cyaA, pde, ppx`).
- **Cross-listed non-purine enzymes**: `cysD/cysNC` (ATP sulfurylase), `arcC` (carbamate kinase), `pgm/cpsG/algC` (phospho-mutases).

**Alternate names / DB definitions:** KEGG `ppu00230` = "Purine metabolism" (overview, not a module). MetaCyc/BioCyc split the equivalent biology into "purine ribonucleosides degradation" / "purine nucleobases salvage" / "adenine and adenosine salvage" / "guanine and guanosine salvage". The relevant GO umbrella is **purine-containing compound salvage (GO:0043101)** with base-specific children (see §6).

---

## 3. Expected step model

| # | Step | Reaction (EC) | Expected enzyme family | KT2440 candidate |
|---|------|---------------|------------------------|------------------|
| 1 | Nucleoside phosphorolysis | nucleoside + Pi → base + R1P (2.4.2.1/2.4.2.2) | PNP-I (DeoD)/PNP-II (XapA)/PpnP-Cupin | `ppnP` PP_4248 (+ candidate PP_3254) |
| 2 | Adenine salvage | adenine + PRPP → AMP (2.4.2.7) | APRT (PF00156) | `apt` PP_4266 |
| 3 | Hypoxanthine/guanine salvage | Hx/Gua + PRPP → IMP/GMP (2.4.2.8) | HGPRT (PF00156) | `hpt` PP_0747 |
| 4 | Xanthine salvage | xanthine + PRPP → XMP (2.4.2.22) | XPRT (PF00156-clan) | `xpt` PP_5265 |

Accessory funnels that determine which branch carries flux: **adenine deaminase** (`PP_0591`, EC 3.5.4.2, adenine→hypoxanthine) and **guanine deaminase** (`guaD`/PP_4281, EC 3.5.4.3, guanine→xanthine). Their presence means salvage does not require a distinct enzyme per base — deaminated bases converge on the HGPRT/XPRT branches.

---

## 4. Candidate genes and evidence

**Evidence tiers derived from UniProt UP000000556 (reviewed status, EC assignment, protein-existence).**

| Gene | Locus / Acc | Step | Evidence tier | Verdict | Curation notes |
|------|-------------|------|---------------|---------|----------------|
| `apt` | PP_4266 / Q88F33 | 2 (Ade→AMP) | **Reviewed, EC 2.4.2.7, PF00156** | `covered` | Single-copy APRT; strong. Homology-inferred but unambiguous family. |
| `xpt` | PP_5265 / Q88CB6 | 4 (Xan→XMP) | **Reviewed, EC 2.4.2.22** | `covered` | XPRT. (No Pfam mapped in UniProt — minor annotation quirk, not a concern.) |
| `ppnP` | PP_4248 / Q88F51 | 1 (phosphorolysis) | **Reviewed, EC 2.4.2.1/2.4.2.2, PF06865 (Cupin)** | `covered` (accessory) | Genuine PpnP class, broad pyrimidine+purine specificity (PMID 35094440). In *E. coli* PpnP is accessory to DeoD, so may be low-capacity here. |
| `hpt` | PP_0747 / Q88PV1 | 3 (Hx/Gua→IMP/GMP) | **Unreviewed, "Predicted", NO EC, PF00156** | `covered` / **`candidate_uncertain`** | Name-only HGPRT; broad PRT clan. Promote to full review. |
| `PP_3254` | Q88HU9 | 1 (phosphorolysis) | Unreviewed, "Predicted", **PF01048 / IPR000845** | **new candidate** for step 1 | Not in candidate list. Nucleoside-phosphorylase-domain (DeoD/MTAP/UP superfamily); best hit for a classical high-flux PNP. **Promote.** |
| `yfiH` | PP_0624 / Q88Q72 | (claimed 1) | Unreviewed, **no EC**, PF02578 (DUF152/YfiH) | **likely over-annotation** | "Purine nucleoside phosphorylase" name unsupported; do not score. |
| `PP_3230` | Q88HX3 | (possible 3/4) | Unreviewed, PF00156 "PRT-domain protein" | `candidate_uncertain` | Possible additional/second PRT (e.g. a `gpt`-type). Check substrate. |
| `PP_0591` (Ade deaminase) | Q88QA3 | funnel | Reviewed, EC 3.5.4.2 | context | Routes adenine→hypoxanthine; species-relevant flux nuance. |
| `guaD` | PP_4281 / Q88F18 | funnel | Unreviewed, EC 3.5.4.3 | context | Guanine→xanthine. |
| `amn`, `PP_3662` | PP_4779, PP_3662 | (not salvage) | EC 3.2.2.4 | out-of-scope | AMP nucleosidase = AMP→adenine+R5P (degradation, not salvage). `amn` shares PF01048 but is functionally distinct. |

**Paralog ambiguity:** The type-I PRT clan **PF00156** in KT2440 contains `apt`, `hpt`/PP_0747, `purF`, `pyrE` (OPRT), `upp`/`pyrR`, `comF`, plus uncharacterised **PP_3230** and PP_0361. Pfam membership alone cannot assign a substrate; substrate specificity for `hpt`/PP_0747 and PP_3230 rests on best-hit orthology, not experiment.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **Step-1 phosphorylase identity — the principal gap.** No DeoD/XapA ortholog exists in the proteome (only `ppnP` carries EC 2.4.2.1). Either (a) PpnP is the physiological purine-nucleoside phosphorylase in KT2440, or (b) **PP_3254** (uncharacterised PF01048/IPR000845) is the real workhorse. This is the single most important item to resolve. Verdict: **`candidate_uncertain`** for step 1.
2. **`yfiH`/PP_0624 over-propagation.** YfiH/DUF152 is a polyphenol-oxidase/laccase-like family; the "purine nucleoside phosphorylase" label is EC-less and unreviewed. Recommend **down-weighting / re-annotation review**; do not treat as salvage evidence.
3. **`hpt`/PP_0747 under-characterised.** Unreviewed + "Predicted" + no EC. Functionally likely correct (conserved HGPRT synteny across *Pseudomonas*), but evidence is homology-only.
4. **`ppnP` broad EC.** EC 2.4.2.1 **and** 2.4.2.2 with 8 substrate synonyms (adenosine…xanthosine, plus pyrimidines). This breadth is a family-level over-listing; in vivo purine contribution is uncertain.
5. **Catabolism mislabelled as core purine map.** `paoABC` (aldehyde oxidoreductase) and the ureide genes (`pucL/pucM/puuE/allA/allE`, `ureABC`, `xdhAB`) are catabolic/N-assimilatory, not salvage. Their inclusion inflates apparent module coverage — a `module_needs_revision` boundary issue.
6. **`arcC`, `cysD/cysNC`, `pgm/cpsG/algC`, `cyaA`, `pde`, `relA/spoT`, `ppx`, Nudix set** — clearly out of scope; over-inclusive projection from the overview map.

---

## 6. Module and GO-curation recommendations

**Per-step module verdicts:**
- Step 1 (nucleoside phosphorolysis): **`candidate_uncertain`** — PpnP present (EC-supported) but likely accessory; classical PNP unrepresented; investigate PP_3254.
- Step 2 (adenine→AMP, `apt`): **`covered`**.
- Step 3 (Hx/Gua→IMP/GMP, `hpt`): **`covered`** with a `candidate_uncertain` evidence flag (predicted, no EC).
- Step 4 (xanthine→XMP, `xpt`): **`covered`**.

**Boundary / module-document recommendations:**
- **`module_needs_revision` at the source:** the KEGG-`ppu00230`→module projection is far too broad. The salvage module document should enumerate **only** the 4 steps and explicitly exclude de novo synthesis, interconversion, catabolism, signalling and housekeeping hydrolases.
- **Create a separate "purine catabolism / ureide N-assimilation" module** for `xdhAB`, `pucL/pucM/puuE/allA/allE`, `PP_4310`, `ureABC` (and possibly `paoABC` after re-annotation). This is where the bulk of the mis-attributed genes belong and is biologically important in *P. putida* (purines/allantoin as N sources).
- **GO annotation targets:** `apt` → GO:0006168 (adenine salvage); `hpt` → GO:0032264 (IMP salvage) + GO:0032263 (GMP salvage); `xpt` → GO:0032265 (XMP salvage, if present) under GO:0043101 (purine-containing compound salvage); `ppnP`/PP_3254 → GO:0006152/GO:0006157-type purine ribonucleoside catabolic/phosphorylase activity (GO:0004731 purine-nucleoside phosphorylase activity). No new GO **term** requests appear necessary; existing salvage terms suffice.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_3254 (Q88HU9)** — *highest priority.* Test whether this IPR000845 nucleoside-phosphorylase-domain protein is the classical (DeoD/MTAP-type) purine nucleoside phosphorylase; would close the step-1 gap.
2. **`hpt` / PP_0747 (Q88PV1)** — confirm HGPRT substrate range and assign EC 2.4.2.8; currently predicted/no-EC.
3. **`yfiH` / PP_0624 (Q88Q72)** — adjudicate the "purine nucleoside phosphorylase" name vs. the YfiH/DUF152 polyphenol-oxidase assignment; likely re-annotate.
4. **PP_3230 (Q88HX3)** — resolve whether this extra PF00156 PRT is a second hypoxanthine/xanthine-guanine PRT (`gpt`) or unrelated.
5. **`ppnP` / PP_4248 (Q88F51)** — confirm physiological purine (vs pyrimidine) role and whether it is the sole phosphorylase.

---

## 8. Evidence status and open questions

- **Direct target-organism experimental evidence:** none located for the salvage enzymes themselves (KT2440 salvage biochemistry is largely unstudied). Available KT2440 literature retrieved concerns unrelated topics (biofilm/(p)ppGpp, malonyl-CoA engineering).
- **Homology / database-inferred (this review):** all four PRT/phosphorylase assignments are homology-based; the two SwissProt-reviewed entries (`apt`, `xpt`) carry the strongest inference, `ppnP` is reviewed, `hpt` is predicted-only. Proteome composition (presence of PpnP, absence of DeoD/XapA, existence of PP_3254) is **directly verified** against UniProt UP000000556 (this work).
- **Cross-organism transfer:** DeoD-as-workhorse and PpnP-as-accessory are *E. coli* facts (PMID 17639373; PMID 35094440); transfer to KT2440 is **weak-to-uncertain** precisely because KT2440 lacks DeoD — so the *E. coli* paradigm cannot be assumed.
- **Resolving experiments:** (i) enzymatic assay of purified PP_3254 and PpnP on inosine/guanosine/adenosine; (ii) growth of Δ*ppnP*, ΔPP_3254 and Δ*hpt*/Δ*apt*/Δ*xpt* mutants on the corresponding nucleosides/bases as C/N source; (iii) substrate profiling of PP_0747 and PP_3230 to settle the HGPRT/XPRT/GPT split.

---

### Key references
- Wen et al. 2022, *Int J Biol Macromol* — Crystal structures of PpnP (pyrimidine/purine nucleoside phosphorylase), a distinct Cupin-fold NP class that phosphorolyses diverse nucleosides to ribose-1-phosphate + free base. **PMID 35094440.**
- Modrak-Wójcik et al. 2008, *Eur Biophys J* — *E. coli* purine nucleoside phosphorylase PNP-I is the product of the *deoD* gene (reference for the canonical workhorse absent in KT2440). **PMID 17639373.**
- UniProt Knowledgebase, proteome **UP000000556** (*P. putida* KT2440) — entries Q88F51 (`ppnP`), Q88F33 (`apt`), Q88CB6 (`xpt`), Q88PV1 (`hpt`/PP_0747), Q88Q72 (`yfiH`), Q88HU9 (PP_3254), Q88HX3 (PP_3230); queried this work.
- KEGG map **ppu00230** "Purine metabolism" (overview-map scope caveat).


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_purine_salvage__ppu00230-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_purine_salvage__ppu00230-deep-research-openscientist_artifacts/final_report.pdf)