---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T08:16:33.395629'
end_time: '2026-08-13T08:33:20.459603'
duration_seconds: 1007.06
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: bacterial_purine_salvage
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

bacterial_purine_salvage in Pseudomonas putida KT2440

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

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

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

# Module/Pathway/Taxon Review: Bacterial Purine Salvage in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00230` — Purine metabolism (module area: nucleotide_metabolism)
**Commissioned review topic:** `bacterial_purine_salvage`
**Candidate genes supplied:** 65 (36 primary to ppu00230)

---

## 1. Executive Summary

In *Pseudomonas putida* KT2440 the purine-metabolism bucket `ppu00230` is **largely satisfiable**, but the three biological sub-processes that the bucket lumps together resolve very differently under species-aware scrutiny, and the commissioned *salvage* scope is the strongest of the three.

**De novo biosynthesis and ribonucleotide interconversion are complete.** All twelve committed steps from PRPP + glutamine to IMP (KEGG module M00048), and both branch modules IMP→ADP/ATP (M00049) and IMP→GDP/GTP (M00050), are present with unambiguous candidate genes and matching KEGG Orthology (KO) assignments. This part of the bucket needs no curation intervention beyond fixing "primary bucket" cross-map artifacts.

**Purine salvage — the commissioned focus — is fully encoded.** KT2440 carries a complete set of salvage phosphoribosyltransferases (adenine → AMP via *apt*; hypoxanthine/guanine → IMP/GMP via *hpt*/PP_0747; xanthine → XMP via *xpt*), nucleoside phosphorylases (*ppnP*, *yfiH*), an AMP nucleosidase (*amn*), adenine and guanine deaminases (*ade*/PP_0591, *guaD*), and multiple 5′-nucleotidases that feed nucleosides back into salvage. The salvage module should be marked **covered**.

**Oxidative catabolism (xanthine ⇒ urea, KEGG M00546) scores "absent," but this is best interpreted as an annotation gap, not a metabolic gap.** KT2440 possesses a dedicated purine-catabolism gene cluster (PP_4278–PP_4290) with a uric-acid permease and every downstream allantoin-degrading enzyme, yet no gene is currently assigned to two required steps: urate → 5-hydroxyisourate (uricase) and allantoate → S-ureidoglycine (allantoate amidohydrolase). Direct genus-level *Pseudomonas* evidence shows the purine-to-allantoin route is functional and proceeds through a non-canonical, "unstable, membrane-bound" uricase with an unusual low-pH optimum — precisely the kind of divergent enzyme that escapes standard KO/sequence models. These two steps should therefore be marked **candidate_uncertain** and flagged for targeted gene discovery rather than declared true gaps.

Finally, several candidate annotations are **over-propagated or mislabeled** and should be corrected during curation: PP_3662 (actually *ppnN*, not AMP nucleosidase), *paoABC*/PP_3308–3310 (aldehyde oxidoreductase, not a xanthine dehydrogenase relevant to purine oxidation), and PP_4310 (allantoin racemase *hpxA*, not hydantoin racemase).

---

## 2. Target-Organism Pathway Definition

**What the bucket includes.** KEGG `ppu00230` "Purine metabolism" is a broad reference map that in practice aggregates three biologically distinct processes:

1. **De novo purine nucleotide biosynthesis** — PRPP + glutamine → IMP, then IMP → AMP and IMP → GMP, and the kinase cascades to (d)NTPs.
2. **Purine salvage** — recovery of free purine bases (adenine, hypoxanthine, guanine, xanthine) and nucleosides into mononucleotides via phosphoribosyltransferases, nucleoside phosphorylases, nucleosidases and deaminases. *This is the commissioned review scope.*
3. **Oxidative purine catabolism** — degradation of xanthine/urate through allantoin/allantoate to glyoxylate + ammonia/urea, allowing purines to be used as nitrogen (and in some pseudomonads, carbon) sources.

**Neighboring pathways to keep separate.** The 65-gene candidate list is inflated by KEGG's "primary bucket" cross-assignments, which pull in genes whose principal role lies in adjacent maps. These should not be counted as purine-metabolism evidence:

- **PRPP supply** — *prs*/PP_0722 and PP_2744 (ppu00030, pentose phosphate) supply the PRPP substrate but are not purine-specific.
- **Sulfur assimilation** — *cysD*/PP_1303, *cysNC*/PP_1304 (ATP sulfurylase; ppu00261) use ATP but belong to sulfate assimilation.
- **Urea/arginine metabolism** — *ureABC*/PP_2843–2845 (urease; ppu00220) and *arcC*/PP_0999 (carbamate kinase; ppu00910) sit at the catabolic exit but are shared with nitrogen metabolism.
- **Sugar-phosphate mutases** — *cpsG*, *pgm*, *algC* (ppu00052) are phosphomannomutase/phosphoglucomutase enzymes with no purine role; their presence is a pure map-overlap artifact.
- **Signaling / housekeeping NTP handling** — *relA*/*spoT* ((p)ppGpp), *cyaA* (adenylate cyclase), *pde* (cyclic-nucleotide phosphodiesterase), *apaH* (Ap4A hydrolase), *mazG*, *nudE*, *nudF*, *ppx*, *dgt*, *PP_5100* (ITPase) are nucleotide-handling housekeeping enzymes, not core purine biosynthesis/salvage/catabolism steps.

**Alternate names / database definitions.** The relevant KEGG modules are M00048 (de novo IMP), M00049 (IMP⇒ADP/ATP), M00050 (IMP⇒GDP/GTP), M00958/M00959 (AMP/GMP⇒urate), and M00546 (purine degradation, xanthine⇒urea). MetaCyc terms the catabolic portion "purine ribonucleosides degradation" and "urate degradation to allantoin."

---

## 3. Expected Step Model

The table below lists the expected steps, grouped by sub-process, with satisfiability status in KT2440.

| Sub-process | Expected step (enzyme) | KT2440 gene | Status |
|---|---|---|---|
| De novo | PRPP + Gln → PRA (*purF*) | PP_2000 | covered |
| De novo | PRA → GAR (*purD*) | PP_4823 | covered |
| De novo | GAR → FGAR (*purN*/*purT*) | PP_1664 / PP_1457 | covered (redundant) |
| De novo | FGAR → FGAM (*purL*) | PP_1037 | covered |
| De novo | FGAM → AIR (*purM*) | PP_1665 | covered |
| De novo | AIR → CAIR (*purK*/*purE*) | PP_5335 / PP_5336 | covered |
| De novo | CAIR → SAICAR (*purC*) | PP_1240 | covered |
| De novo | SAICAR → AICAR (*purB*) | PP_4016 | covered |
| De novo | AICAR → IMP (*purH*) | PP_4822 | covered |
| Branch | IMP → adenylosuccinate → AMP (*purA*/*purB*) | PP_4889 / PP_4016 | covered |
| Branch | IMP → XMP → GMP (*guaB*/*guaA*) | PP_1031 / PP_1032 | covered |
| Kinases | AMP/GMP → (d)NDP → (d)NTP (*adk*, *gmk*, *ndk*, *nrdAB*) | PP_1506, PP_5296, PP_0849, PP_1179/PP_1177 | covered |
| **Salvage** | adenine → AMP (*apt*, EC 2.4.2.7) | PP_4266 | **covered** |
| **Salvage** | hypoxanthine/guanine → IMP/GMP (*hpt*, EC 2.4.2.8) | PP_0747 | **covered** |
| **Salvage** | xanthine → XMP (*xpt*, EC 2.4.2.22) | PP_5265 | **covered** |
| **Salvage** | purine nucleoside phosphorolysis (*ppnP*, *yfiH*) | PP_4248, PP_0624 | **covered** |
| **Salvage** | AMP → adenine + R5P (*amn*, EC 3.2.2.4) | PP_4779 | **covered** |
| **Salvage** | adenine → hypoxanthine (*ade*, EC 3.5.4.2) | PP_0591 | **covered** |
| **Salvage** | guanine → xanthine (*guaD*, EC 3.5.4.3) | PP_4281 | **covered** |
| **Salvage** | nucleotide → nucleoside (5′-nucleotidases) | PP_0259, PP_1620, PP_2531, PP_1414 | **covered** |
| Catabolism | xanthine → urate (xanthine dehydrogenase, EC 1.17.1.4) | *xdhAB*/PP_4278–4279 | covered |
| Catabolism | **urate → 5-HIU (uricase / HpxO-type)** | **none assigned** | **gap → candidate_uncertain** |
| Catabolism | 5-HIU → OHCU (*pucM*, EC 3.5.2.17) | PP_4285 | covered |
| Catabolism | OHCU → allantoin (*pucL*, EC 4.1.1.97) | PP_4287 | covered |
| Catabolism | allantoin racemization (*hpxA*, EC 5.1.99.3) | PP_4310 | covered (relabel) |
| Catabolism | allantoin → allantoate (*puuE* allantoinase, EC 3.5.2.5) | PP_4286 | covered |
| Catabolism | **allantoate → S-ureidoglycine (amidohydrolase, EC 3.5.3.9)** | **none assigned** | **gap → candidate_uncertain** |
| Catabolism | S-ureidoglycine → ureidoglycolate (*allE*, EC 3.5.3.-) | PP_3530 | covered |
| Catabolism | ureidoglycolate → glyoxylate + urea (*allA*, EC 4.3.2.3) | PP_4288 | covered |
| Catabolism | urea → NH3 + CO2 (*ureABC*) | PP_2843–2845 | covered |

---

## 4. Candidate Genes and Evidence

### 4.1 De novo biosynthesis and interconversion (Finding F001)

De novo purine biosynthesis is unambiguously complete. KEGG module reconstruction for organism `ppu` returns **M00048 PRESENT, M00049 PRESENT, and M00050 PRESENT**. Every committed step maps to a candidate gene with a matching KO: *purF*/PP_2000 (K00764), *purD*/PP_4823 (K01945), the redundant GAR transformylases *purN*/PP_1664 (K11175) and *purT*/PP_1457 (K08289), *purL*/PP_1037, *purM*/PP_1665 (K01933), the split N5-CAIR route *purK*/PP_5335 (K01589) + *purE*/PP_5336 (K01588), *purC*/PP_1240 (K01923), *purB*/PP_4016 (K01756), and the bifunctional *purH*/PP_4822 (K00602). The IMP→AMP and IMP→GMP branches are covered by *purA*/PP_4889 (K01939), *guaB*/PP_1031 (K00088) and *guaA*/PP_1032 (K01951). Kinase and reductase steps are covered by *adk*/PP_1506, *gmk*/PP_5296 (K00942), *ndk*/PP_0849 (K00940), and ribonucleotide reductase *nrdAB*/PP_1179 + PP_1177. **Curation note:** *purF*, *purN*, *purH*, *purB*, *purA*, *prs*, *ndk* and *adk* carry KEGG "primary bucket" assignments in neighboring maps (ppu00250, ppu00670, ppu00240, ppu00030, ppu00730) — an overlap artifact, not evidence of a non-purine role.

### 4.2 Purine salvage — commissioned scope (Finding F002)

Salvage is fully encoded and represents the highest-confidence portion of this review. The three salvage **phosphoribosyltransferases** cover the full base-specificity range: *apt*/PP_4266 (K00759, adenine → AMP, EC 2.4.2.7); *hpt*/PP_0747 (K00760, hypoxanthine/guanine → IMP/GMP, EC 2.4.2.8); and *xpt*/PP_5265 (K03816, xanthine → XMP, EC 2.4.2.22). **Nucleoside phosphorylases** *ppnP*/PP_4248 (K09913, broad pyrimidine/purine nucleoside phosphorylase) and *yfiH*/PP_0624 (K05810, purine-nucleoside/MTA phosphorylase) release free bases from nucleosides. **Deaminases** feed the interconversion network: adenine deaminase *ade*/PP_0591 (K21053, EC 3.5.4.2) and guanine deaminase *guaD*/PP_4281 (K01487, EC 3.5.4.3). **AMP nucleosidase** *amn*/PP_4779 (K01241, EC 3.2.2.4) hydrolyzes AMP to adenine + ribose-5-phosphate. Finally, several **5′-nucleotidases** dephosphorylate mononucleotides to nucleosides, keeping salvage substrate available: *yrfG*/PP_0259 (K20881, GMP/IMP 5′-NT), *surE*/PP_1620 (K03787), PP_2531 (K01081), and *ushA*/PP_1414.

**Curation caveat.** *apt* base specificity is well understood mechanistically — a conserved N–H···N hydrogen bond between the base-binding loop and adenine N1 discriminates adenine (a 6-aminopurine) from 6-oxopurines ([PMID: 29694705](https://pubmed.ncbi.nlm.nih.gov/29694705/), *Francisella* APRT structure). This supports the clean functional separation of *apt* (adenine) from *hpt*/*xpt* (oxopurines) in KT2440, but the structural evidence is from *Francisella*, so transfer to KT2440 is homology-based, not direct.

### 4.3 Oxidative catabolism (Findings F003, F005, F006)

KT2440 has a **dedicated purine-catabolism gene cluster** spanning PP_4278–PP_4290: PP_4278 *xdhA*, PP_4279 *xdhB*, PP_4280 *xdhC* (accessory), PP_4281 *guaD*, PP_4282 *aqpZ*, PP_4283 a GntR regulator, PP_4284 a transporter, PP_4285 *pucM* (HIU hydrolase), PP_4286 *puuE* (allantoinase), PP_4287 *pucL* (OHCU decarboxylase, K13485), PP_4288 *allA* (ureidoglycolate lyase), and PP_4290 *uacT* (uric-acid permease). The presence of a uric-acid permease and every downstream allantoin-processing enzyme strongly implies the organism does oxidize urate — otherwise the cluster's transport and downstream machinery would be functionless.

KEGG reconstruction confirms **M00958 (AMP⇒urate) PRESENT and M00959 (GMP⇒urate) PRESENT**, but **M00546 (purine degradation, xanthine⇒urea) is ABSENT**. Genome-wide KO search found **no** gene for urate oxidase/hydroxylase (K00365, K16838, K16839, K16840, K22879, K13484 all absent) and **no** allantoate amidohydrolase/allantoicase (K01477, K02083 absent). These are exactly the two KEGG-required steps that break M00546. The catabolic sub-map also lacks AMP deaminase (K01490) and adenosine deaminase *add* (K01488) genome-wide; KT2440 therefore routes adenine-derived flux through adenine deaminase (*ade*) rather than an AMP/adenosine deaminase.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 The two catabolic gaps are annotation gaps, not metabolic gaps (Finding F006)

The strongest species-aware conclusion of this review is that the uricase and allantoate-amidohydrolase "gaps" reflect **divergent enzymes that escape standard KO models**, not true metabolic absence.

Direct genus-level evidence: in *P. aeruginosa* and *P. testosteroni*, "*adenine, hypoxanthine, xanthine and guanine are broken down … to allantoin by the concerted action of the enzymes adenine deaminase, guanine deaminase, NAD+-dependent xanthine dehydrogenase and uricase*" and "*uric acid is broken down by an unstable, membrane-bound uricase with an unusually low pH optimum*" ([PMID: 407941](https://pubmed.ncbi.nlm.nih.gov/407941/)). The unusual biochemistry — membrane-bound, unstable, low-pH-optimum — explains why a standard soluble-uricase KO/HMM would miss it. A *P. putida* strain (strain 40) channels xanthine through xanthine dehydrogenase and uricase, both inducible ([PMID: 1158847](https://pubmed.ncbi.nlm.nih.gov/1158847/)). In *Klebsiella oxytoca* the urate→allantoin step is a **flavoprotein monooxygenase HpxO**, with allantoin racemase HpxA and PuuE allantoinase downstream ([PMID: 19060149](https://pubmed.ncbi.nlm.nih.gov/19060149/)) — and the KT2440 cluster already contains the same HpxA (PP_4310) and PuuE (PP_4286) genes, indicating that an HpxO-type flavoprotein monooxygenase is the most likely candidate to search for to close the uricase step. These are **species/genus-level, not KT2440-strain-specific** data, so the transfer is moderately strong for the genus and should be verified directly in KT2440.

### 5.2 Over-propagated / mislabeled annotations (Finding F004)

| Gene | Current label | Problem | Correct interpretation |
|---|---|---|---|
| PP_3662 | "AMP nucleosidase (EC 3.2.2.4)" | KO is **K06966** (*ppnN*, pyrimidine/purine-5′-nucleotide nucleosidase, EC 3.2.2.10); duplicates EC 3.2.2.4 held by the real *amn*/PP_4779 (K01241) | Relabel as *ppnN*; remove EC 3.2.2.4 |
| *paoABC* / PP_3308–3310 | "promiscuous aromatic aldehyde dehydrogenase (EC 1.2.99.7)" | KEGG maps to xanthine-dehydrogenase KOs K13483/K11178/K11177 (yagRST family) — a KO-family collision. The true xanthine dehydrogenase is *xdhAB* | Aldehyde oxidoreductase; **not** the purine-oxidizing xanthine dehydrogenase. Do not count toward xanthine catabolism |
| PP_4310 | "hydantoin racemase (EC 5.1.99.5)" | KO **K16841** = *hpxA* allantoin racemase (EC 5.1.99.3) | Relabel as allantoin racemase *hpxA* |
| *yfiH* / PP_0624 | "purine nucleoside phosphorylase" | Carries broad multi-activity EC (2.4.2.1 / 2.4.2.28 / 3.5.4.4) | Keep salvage role but flag broad EC as over-scoped |
| Core biosynthesis genes | KEGG "primary bucket" in neighbor maps | *purF, purN, purH, purB, purA, prs, ndk, adk* placed in ppu00250/00670/00240/00030/00730 | Map-overlap artifact; retain in purine module |

---

## 6. Module and GO-Curation Recommendations

**Module step statuses:**

- **Covered** — the entire de novo IMP module (M00048), both interconversion branches (M00049/M00050), and the full **salvage** set (*apt*, *hpt*, *xpt*, *ppnP*, *yfiH*, *amn*, *ade*, *guaD*, plus 5′-nucleotidases *yrfG/surE/PP_2531/ushA*). The commissioned `bacterial_purine_salvage` module should be marked **covered** in KT2440.
- **Candidate_uncertain** — urate → 5-HIU (uricase / HpxO-type) and allantoate → S-ureidoglycine (allantoate amidohydrolase). Present metabolically (per genus evidence and the intact flanking cluster) but with no confidently assignable gene. Do **not** mark as hard gaps.
- **Not_expected_in_target_taxon** — AMP deaminase and adenosine deaminase steps: genuinely absent genome-wide; the organism uses adenine deaminase instead.
- **Module_needs_revision** — the generic `ppu00230` bucket conflates biosynthesis, salvage, and catabolism and drags in sulfur, sugar-phosphate, and signaling genes. For KT2440 the boundaries should be split into three modules (biosynthesis / salvage / oxidative catabolism), and the cross-map "primary bucket" genes excluded.

**GO / new-document requests:**

- Consider a GO term / module document for the **non-canonical bacterial uricase (HpxO-type flavoprotein monooxygenase)** so that divergent urate-oxidizing enzymes are captured rather than scored as gaps.
- The *puuE* allantoinase is worth a curation note: it is an **allantoinase analog recruited from polysaccharide deacetylases**, annotated in sequence databases as a polysaccharide deacetylase despite metal-independent allantoinase activity and S-allantoin stereospecificity ([PMID: 18550550](https://pubmed.ncbi.nlm.nih.gov/18550550/)). This is a documented case of the correct function being hidden behind a homology-based misannotation — a template for how the uricase gap may resolve.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority candidates for deeper, individual review:

1. **The uricase gap** — search PP_4278–PP_4290 cluster neighbors and genome-wide for an HpxO-type flavoprotein monooxygenase or a membrane-associated urate oxidase. Highest curation value; resolves the M00546 break.
2. **Allantoate amidohydrolase gap** — search for a divergent EC 3.5.3.9 enzyme upstream of *allE*/PP_3530; the presence of *allE* (S-ureidoglycine aminohydrolase) implies an allantoate→ureidoglycine activity must exist.
3. **PP_3662** — confirm reassignment to *ppnN* (K06966) and strip the erroneous EC 3.2.2.4.
4. **paoABC / PP_3308–3310** — confirm aldehyde-oxidoreductase function and remove from the purine-oxidation step count.
5. **PP_4310** — confirm allantoin-racemase (*hpxA*) identity and correct the "hydantoin racemase" label.
6. **yfiH / PP_0624** — resolve which of its broad EC activities is physiologically relevant in KT2440.

---

## 8. Mechanistic Model

```
   De novo (COMPLETE, M00048)                Salvage (COMPLETE — commissioned scope)
   PRPP+Gln --purF--> ... --purH--> IMP <====== hypoxanthine/guanine --hpt(PP_0747)-->
        |                                        adenine --apt(PP_4266)--> AMP
        +-- purA/purB --> AMP                    xanthine --xpt(PP_5265)--> XMP
        +-- guaB/guaA --> GMP                    nucleosides --ppnP/yfiH--> free bases
                                                 AMP --amn(PP_4779)--> adenine + R5P
                                                 adenine --ade(PP_0591)--> hypoxanthine
                                                 guanine --guaD(PP_4281)--> xanthine

   Oxidative catabolism (cluster PP_4278-4290; M00546 scored ABSENT)
   xanthine --xdhAB--> URATE --[?? uricase GAP]--> 5-HIU --pucM--> OHCU --pucL-->
     allantoin --hpxA(PP_4310)--> --puuE(PP_4286)--> allantoate
     --[?? allantoate amidohydrolase GAP]--> S-ureidoglycine --allE--> ureidoglycolate
     --allA--> glyoxylate + urea --ureABC--> NH3 + CO2
                     ^^ two GAPS = divergent enzymes (annotation gaps, not metabolic)
```

Interpretation: biosynthesis and salvage form a closed, fully-encoded network; the catabolic arm is metabolically intact (genus evidence + complete flanking cluster with uric-acid permease) but has two enzymes that current KO/HMM models cannot place, producing a spurious "not satisfiable" verdict for M00546.

---

## 9. Evidence Base

| PMID | Relevance to this review |
|---|---|
| [407941](https://pubmed.ncbi.nlm.nih.gov/407941/) | *Purine degradation in Pseudomonas aeruginosa and P. testosteroni.* Direct genus evidence that adenine/hypoxanthine/xanthine/guanine → allantoin proceeds via adenine deaminase, guanine deaminase, NAD+-dependent xanthine dehydrogenase and an "unstable, membrane-bound uricase with an unusually low pH optimum." Core support for the annotation-gap interpretation. |
| [1158847](https://pubmed.ncbi.nlm.nih.gov/1158847/) | *Metabolism of N-methylpurines by a P. putida strain.* Species-level evidence that xanthine is channeled through xanthine dehydrogenase and uricase, both inducible. |
| [19060149](https://pubmed.ncbi.nlm.nih.gov/19060149/) | *Purine utilization by Klebsiella oxytoca M5al.* Identifies HpxO flavoprotein monooxygenase (urate→allantoin) with HpxA racemase and PuuE allantoinase downstream — the same HpxA/PuuE present in the KT2440 cluster; tells curators what to search for. |
| [18550550](https://pubmed.ncbi.nlm.nih.gov/18550550/) | *Logical identification of an allantoinase analog (puuE) recruited from polysaccharide deacetylases.* Documents PuuE misannotation as polysaccharide deacetylase — a precedent for hidden purine-catabolic functions. |
| [29694705](https://pubmed.ncbi.nlm.nih.gov/29694705/) | *Crystal structures of APRT from Francisella tularensis.* Mechanistic basis for adenine specificity (N–H···N to N1), supporting the *apt* vs *hpt*/*xpt* functional split. |
| [863854](https://pubmed.ncbi.nlm.nih.gov/863854/) | *Distribution of xanthine oxidase/dehydrogenase specificity types among bacteria.* Confirms P. putida soluble xanthine-dehydrogenase activity, competitively inhibited by uric acid. |
| [17981969](https://pubmed.ncbi.nlm.nih.gov/17981969/) | *Novel caffeine dehydrogenase in Pseudomonas sp. CBB1.* Illustrates lineage-specific purine-oxidizing enzymes in the genus that escape canonical annotation. |

**Evidence-type summary.** Biosynthesis and salvage conclusions rest on direct genome/KO reconstruction of KT2440 (strong, computational-genomic). The catabolic annotation-gap conclusion rests on genus-level biochemistry (moderate transfer) combined with KT2440 genome context (the intact PP_4278–4290 cluster and uric-acid permease). No direct KT2440 enzyme assays exist for the two gap steps.

---

## 10. Limitations and Knowledge Gaps

- **Species transfer:** the strongest catabolic evidence (uricase functionality) is from *P. aeruginosa*, *P. testosteroni*, and other *P. putida* strains — **not** KT2440 directly. The intact flanking cluster and uric-acid permease make transfer plausible but not proven for KT2440.
- **No direct enzymatic assays** for the two gap steps in KT2440; conclusions rest on genome context and homology reasoning.
- **KO-based reconstruction** inherently misses divergent enzymes (the whole point of the uricase gap), so "ABSENT" module calls must be read cautiously.
- **RB-TnSeq / fitness data** for KT2440 exist ([PMID: 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)) but were not mined here; they could functionally implicate the unassigned cluster genes.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Sequence search** the PP_4278–4290 neighborhood and genome for an HpxO-family flavoprotein monooxygenase (PF-level HMM) to nominate the uricase gene.
2. **Growth phenotyping** of KT2440 on urate/allantoin/allantoate as sole N source, ± the cluster regulator (PP_4283) and permease (PP_4290) knockouts.
3. **RB-TnSeq fitness mining** on nitrogen-source conditions to identify genes required for urate/allantoate utilization.
4. **Enzyme assay** of the candidate uricase for the reported membrane-bound, low-pH-optimum, unstable phenotype.
5. **Curation actions:** relabel PP_3662→*ppnN*, PP_4310→*hpxA*; downgrade *paoABC* out of purine oxidation; mark M00546 steps candidate_uncertain; split `ppu00230` into three modules and drop cross-map genes.


## Artifacts

- [OpenScientist final report](final_report.html)
- [OpenScientist final report](final_report.pdf)

## Citations

1. PMID:29694705
2. PMID:1158847
3. PMID:19060149
4. PMID:18550550
5. PMID:38323821