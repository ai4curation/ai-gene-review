---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:42:25.321648'
end_time: '2026-08-31T19:51:28.810282'
duration_seconds: 543.49
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: De novo UMP biosynthesis
  module_summary: 'The conserved six-reaction pathway that builds UMP from glutamine,
    hydrogencarbonate, ATP, aspartate, and PRPP. Carbamoyl phosphate is formed first,
    followed by assembly and oxidation of the pyrimidine ring, attachment to phosphoribose,
    and decarboxylation to UMP. Enzyme architecture varies: bacteria commonly use
    separate CarA, CarB, PyrB, PyrC, PyrE, and PyrF proteins, whereas animals fuse
    the first three activities in CAD and the final two activities in UMPS. These
    fusions do not change the six chemical leaves represented by the module.'
  module_outline: "- De novo UMP biosynthesis\n  - 1. glutamine-dependent carbamoyl-phosphate\
    \ synthesis\n  - Glutamine and hydrogencarbonate to carbamoyl phosphate\n    -\
    \ Carbamoyl-phosphate synthase glutaminase component (molecular player: carbamoyl-phosphate\
    \ synthase small-chain domain family; activity or role: glutaminase activity)\n\
    \    - Carbamoyl-phosphate synthase ATP-dependent component (molecular player:\
    \ carbamoyl-phosphate synthase large-chain domain family; activity or role: carbamoyl-phosphate\
    \ synthase (glutamine-hydrolyzing) activity)\n  - 2. aspartate carbamoylation\n\
    \  - Carbamoyl phosphate and aspartate to carbamoyl aspartate\n    - Aspartate\
    \ carbamoyltransferase activity (molecular player: aspartate carbamoyltransferase\
    \ domain family; activity or role: aspartate carbamoyltransferase activity)\n\
    \  - 3. dihydroorotate ring closure\n  - Carbamoyl aspartate to dihydroorotate\n\
    \    - Dihydroorotase activity (molecular player: dihydroorotase catalytic domain\
    \ family; activity or role: dihydroorotase activity)\n  - 4. dihydroorotate oxidation\n\
    \  - Dihydroorotate to orotate\n    - Quinone-dependent dihydroorotate dehydrogenase\
    \ activity (molecular player: class 2 dihydroorotate dehydrogenase family; activity\
    \ or role: dihydroorotate dehydrogenase (quinone) activity)\n  - 5. phosphoribosylation\
    \ of orotate\n  - Orotate and PRPP to OMP\n    - Orotate phosphoribosyltransferase\
    \ activity (molecular player: orotate phosphoribosyltransferase domain family;\
    \ activity or role: orotate phosphoribosyltransferase activity)\n  - 6. UMP formation\
    \ by OMP decarboxylation\n  - OMP to UMP\n    - Orotidine-5'-phosphate decarboxylase\
    \ activity (molecular player: OMP decarboxylase domain family; activity or role:\
    \ orotidine-5'-phosphate decarboxylase activity)"
  module_connections: '- Glutamine and hydrogencarbonate to carbamoyl phosphate feeds
    into Carbamoyl phosphate and aspartate to carbamoyl aspartate: Carbamoyl phosphate
    is consumed by aspartate carbamoyltransferase.

    - Carbamoyl phosphate and aspartate to carbamoyl aspartate feeds into Carbamoyl
    aspartate to dihydroorotate: N-carbamoyl-L-aspartate undergoes ring closure.

    - Carbamoyl aspartate to dihydroorotate feeds into Dihydroorotate to orotate:
    Dihydroorotate is oxidized to orotate.

    - Dihydroorotate to orotate feeds into Orotate and PRPP to OMP: Orotate receives
    a phosphoribosyl group from PRPP.

    - Orotate and PRPP to OMP feeds into OMP to UMP: OMP is decarboxylated to UMP.'
  pathway_query: ppu00240
  pathway_id: ppu00240
  pathway_name: Pyrimidine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00240 with 24 primary genes; module
    area: nucleotide_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '36'
  candidate_genes: '- PP_0488: PP_0488 | Q88QK2 | NADP-dependent dehydrogenase HI_1430
    (EC 1.1.1.-) (EC 1.1.1.-; primary bucket kegg:ppu00240)

    - PP_0614: PP_0614 | Q88Q81 | N-carbamoyl-beta-alanine amidohydrolase/allantoine
    amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket
    kegg:ppu00410)

    - upp: PP_0746 | Q88PV2 | Uracil phosphoribosyltransferase (EC 2.4.2.9) (UMP pyrophosphorylase)
    (UPRTase) (EC 2.4.2.9; primary bucket kegg:ppu00240)

    - ndk: PP_0849 | Q88PK1 | Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC
    2.7.4.6) (Nucleoside-2-P kinase) (EC 2.7.4.6; primary bucket kegg:ppu00240)

    - maf-1: PP_0936 | Q88PB4 | dTTP/UTP pyrophosphatase (dTTPase/UTPase) (EC 3.6.1.9)
    (Nucleoside triphosphate pyrophosphatase) (Nucleotide pyrophosphatase) (Nucleotide
    PPase) (EC 3.6.1.9; primary bucket kegg:ppu00240)

    - pyrC: PP_1086 | Q88NW7 | Dihydroorotase (DHOase) (EC 3.5.2.3) (EC 3.5.2.3; primary
    bucket kegg:ppu00240)

    - dcd: PP_1100 | Q88NV4 | dCTP deaminase (EC 3.5.4.13) (Deoxycytidine triphosphate
    deaminase) (EC 3.5.4.13; primary bucket kegg:ppu00240)

    - nrdB: PP_1177 | Q88NN0 | Ribonucleoside-diphosphate reductase subunit beta (EC
    1.17.4.1) (EC 1.17.4.1; primary bucket kegg:ppu00240)

    - nrdA: PP_1179 | Q88NM8 | Ribonucleoside-diphosphate reductase (EC 1.17.4.1)
    (EC 1.17.4.1; primary bucket kegg:ppu00240)

    - ushA: PP_1414 | Q88N04 | 5''-nucleotidase-2'',3''-cyclic phosphodiesterase (EC
    3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) (EC 3.1.3.5; 3.1.4.16; 3.6.1.45; primary bucket
    kegg:ppu00760)

    - pyrH: PP_1593 | Q88MH8 | Uridylate kinase (UK) (EC 2.7.4.22) (Uridine monophosphate
    kinase) (UMP kinase) (UMPK) (EC 2.7.4.22; primary bucket kegg:ppu00240)

    - pyrG: PP_1610 | Q88MG1 | CTP synthase (EC 6.3.4.2) (Cytidine 5''-triphosphate
    synthase) (Cytidine triphosphate synthetase) (CTP synthetase) (CTPS) (UTP--ammonia
    ligase) (EC 6.3.4.2; primary bucket kegg:ppu00240)

    - surE: PP_1620 | Q88MF1 | 5''-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5''-monophosphate
    phosphohydrolase) (EC 3.1.3.5; primary bucket kegg:ppu00760)

    - mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8)
    (EC 3.6.1.8; primary bucket kegg:ppu00770)

    - cmk: PP_1771 | Q88M04 | Cytidylate kinase (CK) (EC 2.7.4.25) (Cytidine monophosphate
    kinase) (CMP kinase) (EC 2.7.4.25; primary bucket kegg:ppu00240)

    - pyrF: PP_1815 | Q88LW2 | Orotidine 5''-phosphate decarboxylase (EC 4.1.1.23)
    (OMP decarboxylase) (OMPDCase) (OMPdecase) (EC 4.1.1.23; primary bucket kegg:ppu00240)

    - pyrD: PP_2095 | Q88L40 | Dihydroorotate dehydrogenase (quinone) (EC 1.3.5.2)
    (DHOdehase) (DHOD) (DHODase) (Dihydroorotate oxidase) (EC 1.3.5.2; primary bucket
    kegg:ppu00240)

    - PP_2531: PP_2531 | Q88JW6 | 5-nucleotidase (primary bucket kegg:ppu00760)

    - codA: PP_3189 | Q88I13 | Cytosine deaminase / isoguanine deaminase (EC 3.5.4.-,
    EC 3.5.4.1) (EC 3.5.4.-; 3.5.4.1; primary bucket kegg:ppu00240)

    - PP_3238: PP_3238 | Q88HW5 | Transcriptional regulator PyrR (primary bucket kegg:ppu00240)

    - PP_3662: PP_3662 | Q88GQ6 | AMP nucleosidase (EC 3.2.2.4) (AMP nucleosidase)
    (EC 3.2.2.4; primary bucket kegg:ppu00240)

    - hyuC: PP_4034 | Q88FQ3 | N-carbamoyl-beta-alanine amidohydrolase/allantoine
    amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket
    kegg:ppu00410)

    - pydB: PP_4036 | A0A140FWK2 | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2)
    (EC 3.5.2.2; primary bucket kegg:ppu00410)

    - pydX: PP_4037 | Q88FQ1 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine
    dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)

    - pydA: PP_4038 | Q88FQ0 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine
    dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)

    - ppnP: PP_4248 | Q88F51 | Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1)
    (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase) (Guanosine phosphorylase)
    (Inosine phosphorylase) (Thymidine phosphorylase) (Uridine phosphorylase) (Xanthosine
    phosphorylase) (EC 2.4.2.1; 2.4.2.2; primary bucket kegg:ppu00240)

    - carB: PP_4723 | Q88DU6 | Carbamoyl phosphate synthase large chain (EC 6.3.4.16)
    (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) (EC 6.3.4.16; 6.3.5.5;
    primary bucket kegg:ppu00220)

    - carA: PP_4724 | Q88DU5 | Carbamoyl phosphate synthase small chain (EC 6.3.5.5)
    (Carbamoyl phosphate synthetase glutamine chain) (EC 6.3.5.5; primary bucket kegg:ppu00220)

    - ydfG: PP_4862 | Q88DG3 | 3-hydroxy acid dehydrogenase, NADP-dependent / malonic
    semialdehyde reductase (EC 1.1.1.276, EC 1.1.1.298) (EC 1.1.1.276; 1.1.1.298;
    primary bucket kegg:ppu00240)

    - ygjP: PP_4958 | Q88D69 | Metal-dependent hydrolase (primary bucket kegg:ppu00240)

    - pyrR: PP_4997 | Q88D31 | Pyrimidine operon regulatory protein/uracil phosphoribosyltransferase
    (EC 2.4.2.9) (EC 2.4.2.9; primary bucket kegg:ppu00240)

    - pyrB: PP_4998 | Q88D30 | Aspartate carbamoyltransferase catalytic subunit (EC
    2.1.3.2) (Aspartate transcarbamylase) (ATCase) (EC 2.1.3.2; primary bucket kegg:ppu00240)

    - pyrC'': PP_4999 | Q88D29 | Dihydroorotase-like protein (EC 3.5.2.3) (EC 3.5.2.3;
    primary bucket kegg:ppu00240)

    - thyA: PP_5141 | Q88CN9 | Thymidylate synthase (TS) (TSase) (EC 2.1.1.45) (EC
    2.1.1.45; primary bucket kegg:ppu04981)

    - dut: PP_5286 | Q88C95 | Deoxyuridine 5''-triphosphate nucleotidohydrolase (dUTPase)
    (EC 3.6.1.23) (dUTP pyrophosphatase) (EC 3.6.1.23; primary bucket kegg:ppu00240)

    - pyrE: PP_5291 | Q88C92 | Orotate phosphoribosyltransferase (OPRT) (OPRTase)
    (EC 2.4.2.10) (EC 2.4.2.10; primary bucket kegg:ppu00240)'
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
  path: PSEPK__de_novo_pyrimidine_synthesis__ppu00240-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__de_novo_pyrimidine_synthesis__ppu00240-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

De novo UMP biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00240
- Resolved ID: ppu00240
- Resolved name: Pyrimidine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00240 with 24 primary genes; module area: nucleotide_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 36

- PP_0488: PP_0488 | Q88QK2 | NADP-dependent dehydrogenase HI_1430 (EC 1.1.1.-) (EC 1.1.1.-; primary bucket kegg:ppu00240)
- PP_0614: PP_0614 | Q88Q81 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- upp: PP_0746 | Q88PV2 | Uracil phosphoribosyltransferase (EC 2.4.2.9) (UMP pyrophosphorylase) (UPRTase) (EC 2.4.2.9; primary bucket kegg:ppu00240)
- ndk: PP_0849 | Q88PK1 | Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC 2.7.4.6) (Nucleoside-2-P kinase) (EC 2.7.4.6; primary bucket kegg:ppu00240)
- maf-1: PP_0936 | Q88PB4 | dTTP/UTP pyrophosphatase (dTTPase/UTPase) (EC 3.6.1.9) (Nucleoside triphosphate pyrophosphatase) (Nucleotide pyrophosphatase) (Nucleotide PPase) (EC 3.6.1.9; primary bucket kegg:ppu00240)
- pyrC: PP_1086 | Q88NW7 | Dihydroorotase (DHOase) (EC 3.5.2.3) (EC 3.5.2.3; primary bucket kegg:ppu00240)
- dcd: PP_1100 | Q88NV4 | dCTP deaminase (EC 3.5.4.13) (Deoxycytidine triphosphate deaminase) (EC 3.5.4.13; primary bucket kegg:ppu00240)
- nrdB: PP_1177 | Q88NN0 | Ribonucleoside-diphosphate reductase subunit beta (EC 1.17.4.1) (EC 1.17.4.1; primary bucket kegg:ppu00240)
- nrdA: PP_1179 | Q88NM8 | Ribonucleoside-diphosphate reductase (EC 1.17.4.1) (EC 1.17.4.1; primary bucket kegg:ppu00240)
- ushA: PP_1414 | Q88N04 | 5'-nucleotidase-2',3'-cyclic phosphodiesterase (EC 3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) (EC 3.1.3.5; 3.1.4.16; 3.6.1.45; primary bucket kegg:ppu00760)
- pyrH: PP_1593 | Q88MH8 | Uridylate kinase (UK) (EC 2.7.4.22) (Uridine monophosphate kinase) (UMP kinase) (UMPK) (EC 2.7.4.22; primary bucket kegg:ppu00240)
- pyrG: PP_1610 | Q88MG1 | CTP synthase (EC 6.3.4.2) (Cytidine 5'-triphosphate synthase) (Cytidine triphosphate synthetase) (CTP synthetase) (CTPS) (UTP--ammonia ligase) (EC 6.3.4.2; primary bucket kegg:ppu00240)
- surE: PP_1620 | Q88MF1 | 5'-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5'-monophosphate phosphohydrolase) (EC 3.1.3.5; primary bucket kegg:ppu00760)
- mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) (EC 3.6.1.8; primary bucket kegg:ppu00770)
- cmk: PP_1771 | Q88M04 | Cytidylate kinase (CK) (EC 2.7.4.25) (Cytidine monophosphate kinase) (CMP kinase) (EC 2.7.4.25; primary bucket kegg:ppu00240)
- pyrF: PP_1815 | Q88LW2 | Orotidine 5'-phosphate decarboxylase (EC 4.1.1.23) (OMP decarboxylase) (OMPDCase) (OMPdecase) (EC 4.1.1.23; primary bucket kegg:ppu00240)
- pyrD: PP_2095 | Q88L40 | Dihydroorotate dehydrogenase (quinone) (EC 1.3.5.2) (DHOdehase) (DHOD) (DHODase) (Dihydroorotate oxidase) (EC 1.3.5.2; primary bucket kegg:ppu00240)
- PP_2531: PP_2531 | Q88JW6 | 5-nucleotidase (primary bucket kegg:ppu00760)
- codA: PP_3189 | Q88I13 | Cytosine deaminase / isoguanine deaminase (EC 3.5.4.-, EC 3.5.4.1) (EC 3.5.4.-; 3.5.4.1; primary bucket kegg:ppu00240)
- PP_3238: PP_3238 | Q88HW5 | Transcriptional regulator PyrR (primary bucket kegg:ppu00240)
- PP_3662: PP_3662 | Q88GQ6 | AMP nucleosidase (EC 3.2.2.4) (AMP nucleosidase) (EC 3.2.2.4; primary bucket kegg:ppu00240)
- hyuC: PP_4034 | Q88FQ3 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- pydB: PP_4036 | A0A140FWK2 | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) (EC 3.5.2.2; primary bucket kegg:ppu00410)
- pydX: PP_4037 | Q88FQ1 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- pydA: PP_4038 | Q88FQ0 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- ppnP: PP_4248 | Q88F51 | Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1) (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase) (Guanosine phosphorylase) (Inosine phosphorylase) (Thymidine phosphorylase) (Uridine phosphorylase) (Xanthosine phosphorylase) (EC 2.4.2.1; 2.4.2.2; primary bucket kegg:ppu00240)
- carB: PP_4723 | Q88DU6 | Carbamoyl phosphate synthase large chain (EC 6.3.4.16) (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) (EC 6.3.4.16; 6.3.5.5; primary bucket kegg:ppu00220)
- carA: PP_4724 | Q88DU5 | Carbamoyl phosphate synthase small chain (EC 6.3.5.5) (Carbamoyl phosphate synthetase glutamine chain) (EC 6.3.5.5; primary bucket kegg:ppu00220)
- ydfG: PP_4862 | Q88DG3 | 3-hydroxy acid dehydrogenase, NADP-dependent / malonic semialdehyde reductase (EC 1.1.1.276, EC 1.1.1.298) (EC 1.1.1.276; 1.1.1.298; primary bucket kegg:ppu00240)
- ygjP: PP_4958 | Q88D69 | Metal-dependent hydrolase (primary bucket kegg:ppu00240)
- pyrR: PP_4997 | Q88D31 | Pyrimidine operon regulatory protein/uracil phosphoribosyltransferase (EC 2.4.2.9) (EC 2.4.2.9; primary bucket kegg:ppu00240)
- pyrB: PP_4998 | Q88D30 | Aspartate carbamoyltransferase catalytic subunit (EC 2.1.3.2) (Aspartate transcarbamylase) (ATCase) (EC 2.1.3.2; primary bucket kegg:ppu00240)
- pyrC': PP_4999 | Q88D29 | Dihydroorotase-like protein (EC 3.5.2.3) (EC 3.5.2.3; primary bucket kegg:ppu00240)
- thyA: PP_5141 | Q88CN9 | Thymidylate synthase (TS) (TSase) (EC 2.1.1.45) (EC 2.1.1.45; primary bucket kegg:ppu04981)
- dut: PP_5286 | Q88C95 | Deoxyuridine 5'-triphosphate nucleotidohydrolase (dUTPase) (EC 3.6.1.23) (dUTP pyrophosphatase) (EC 3.6.1.23; primary bucket kegg:ppu00240)
- pyrE: PP_5291 | Q88C92 | Orotate phosphoribosyltransferase (OPRT) (OPRTase) (EC 2.4.2.10) (EC 2.4.2.10; primary bucket kegg:ppu00240)

## Generic Module Context

### Working Scope

The conserved six-reaction pathway that builds UMP from glutamine, hydrogencarbonate, ATP, aspartate, and PRPP. Carbamoyl phosphate is formed first, followed by assembly and oxidation of the pyrimidine ring, attachment to phosphoribose, and decarboxylation to UMP. Enzyme architecture varies: bacteria commonly use separate CarA, CarB, PyrB, PyrC, PyrE, and PyrF proteins, whereas animals fuse the first three activities in CAD and the final two activities in UMPS. These fusions do not change the six chemical leaves represented by the module.

### Provisional Biological Outline

- De novo UMP biosynthesis
  - 1. glutamine-dependent carbamoyl-phosphate synthesis
  - Glutamine and hydrogencarbonate to carbamoyl phosphate
    - Carbamoyl-phosphate synthase glutaminase component (molecular player: carbamoyl-phosphate synthase small-chain domain family; activity or role: glutaminase activity)
    - Carbamoyl-phosphate synthase ATP-dependent component (molecular player: carbamoyl-phosphate synthase large-chain domain family; activity or role: carbamoyl-phosphate synthase (glutamine-hydrolyzing) activity)
  - 2. aspartate carbamoylation
  - Carbamoyl phosphate and aspartate to carbamoyl aspartate
    - Aspartate carbamoyltransferase activity (molecular player: aspartate carbamoyltransferase domain family; activity or role: aspartate carbamoyltransferase activity)
  - 3. dihydroorotate ring closure
  - Carbamoyl aspartate to dihydroorotate
    - Dihydroorotase activity (molecular player: dihydroorotase catalytic domain family; activity or role: dihydroorotase activity)
  - 4. dihydroorotate oxidation
  - Dihydroorotate to orotate
    - Quinone-dependent dihydroorotate dehydrogenase activity (molecular player: class 2 dihydroorotate dehydrogenase family; activity or role: dihydroorotate dehydrogenase (quinone) activity)
  - 5. phosphoribosylation of orotate
  - Orotate and PRPP to OMP
    - Orotate phosphoribosyltransferase activity (molecular player: orotate phosphoribosyltransferase domain family; activity or role: orotate phosphoribosyltransferase activity)
  - 6. UMP formation by OMP decarboxylation
  - OMP to UMP
    - Orotidine-5'-phosphate decarboxylase activity (molecular player: OMP decarboxylase domain family; activity or role: orotidine-5'-phosphate decarboxylase activity)

### Known Relationships Among Steps

- Glutamine and hydrogencarbonate to carbamoyl phosphate feeds into Carbamoyl phosphate and aspartate to carbamoyl aspartate: Carbamoyl phosphate is consumed by aspartate carbamoyltransferase.
- Carbamoyl phosphate and aspartate to carbamoyl aspartate feeds into Carbamoyl aspartate to dihydroorotate: N-carbamoyl-L-aspartate undergoes ring closure.
- Carbamoyl aspartate to dihydroorotate feeds into Dihydroorotate to orotate: Dihydroorotate is oxidized to orotate.
- Dihydroorotate to orotate feeds into Orotate and PRPP to OMP: Orotate receives a phosphoribosyl group from PRPP.
- Orotate and PRPP to OMP feeds into OMP to UMP: OMP is decarboxylated to UMP.

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

# Species-Aware Module Review: De novo UMP Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** De novo UMP biosynthesis (six conserved chemical leaves)
**Local bucket reviewed:** KEGG `ppu00240` (Pyrimidine metabolism), 36 candidate genes
**Curation purpose:** support manual module satisfiability and gene-annotation curation.

---

## 1. Executive summary

- **The de novo UMP module is fully satisfiable in *P. putida* KT2440.** All six chemical leaves map to a credible candidate gene: `carA/carB` (step 1), `pyrB` (step 2), `pyrC` (step 3), `pyrD` (step 4), `pyrE` (step 5), `pyrF` (step 6). **Recommendation: mark all six steps `covered`.**
- **One high-value species-specific caveat.** *P. putida* carries **two dihydroorotase-homologous genes**: the catalytically active **`pyrC` (PP_1086)** and a **vestigial, catalytically inactive `pyrC'` (PP_4999)**. The `pyrC'` product is a pseudo-enzyme that exists only to hold the dodecameric aspartate transcarbamoylase (ATCase) holoenzyme together; its **EC 3.5.2.3 annotation is over-propagated**. This is **direct experimental evidence in the target species** (Schurr et al. 1995, PMID 7896697).
- **The KEGG `ppu00240` bucket is much broader than this module.** Only ~8 of 36 candidates are de novo UMP leaves. The rest are UMP→UTP/CTP interconversion, dNTP metabolism, salvage, or reductive pyrimidine *catabolism* (KEGG `ppu00410`). These must be kept **out** of the module to avoid false "satisfied-by-salvage" calls.
- **Step 1 genes sit in a different bucket.** `carA/carB` carry primary bucket `ppu00220` because carbamoyl phosphate is shared between arginine and pyrimidine biosynthesis. The module is still satisfied, but the module document should explicitly point to these out-of-bucket genes.
- **Genes to promote to full `fetch-gene` review:** `pyrC'` (PP_4999), `pyrC` (PP_1086), `pyrD` (PP_2095), and the regulatory `pyrR`/`PyrR` pair (PP_4997, PP_3238).

---

## 2. Target-organism pathway definition

**Included process.** The conserved six-reaction route converting glutamine + hydrogencarbonate + ATP + L-aspartate + PRPP into **UMP**:
carbamoyl-phosphate synthesis → aspartate carbamoylation → dihydroorotate ring closure → dihydroorotate oxidation → orotate phosphoribosylation → OMP decarboxylation. **The module ends at UMP.**

**Neighboring processes to keep separate.**
- **UMP → UDP → UTP → CTP** and **UMP → dUMP → dTMP** conversions (`pyrH`, `ndk`, `cmk`, `pyrG`, `nrdAB`, `dcd`, `dut`, `thyA`) — downstream nucleotide metabolism, **not** de novo UMP synthesis.
- **Pyrimidine salvage / degradation:** `upp` (uracil salvage), `ppnP`, `codA`, 5′-nucleotidases (`ushA`, `surE`, PP_2531), `mazG`, `maf-1`, AMP nucleosidase (PP_3662).
- **Reductive pyrimidine catabolism** (KEGG `ppu00410`): `pydA/pydB/pydX`, `hyuC`, PP_0614 — these degrade uracil/thymine to β-alanine; opposite direction to biosynthesis.
- **Broad overview maps to keep distinct:** KEGG `ppu00240` "Pyrimidine metabolism" (this is a metabolism *map*, not the module), `ppu00220` (arginine biosynthesis, shares carbamoyl-P), `ppu01100`/`ppu01110` global maps.

**Alternate names / database definitions.** MetaCyc **PWY-5686 (UMP biosynthesis I)**; BioCyc "de novo biosynthesis of pyrimidine ribonucleotides"; KEGG module **M00051** ("Uridine monophosphate biosynthesis, glutamine (+ PRPP) → UMP"). EC set: 6.3.5.5, 2.1.3.2, 3.5.2.3, 1.3.5.2, 2.4.2.10, 4.1.1.23.

---

## 3. Expected step model (six leaves)

| # | Reaction | Expected activity (EC) | Enzyme family |
|---|----------|------------------------|---------------|
| 1 | Gln + HCO₃⁻ + 2ATP → carbamoyl-P | CPS glutaminase + synthetase (6.3.5.5) | CarA (small/Gln) + CarB (large/ATP) |
| 2 | carbamoyl-P + Asp → N-carbamoyl-L-Asp | aspartate carbamoyltransferase (2.1.3.2) | PyrB (ATCase catalytic) |
| 3 | N-carbamoyl-Asp → (S)-dihydroorotate | dihydroorotase (3.5.2.3) | PyrC (amidohydrolase / metallo) |
| 4 | dihydroorotate → orotate | DHOdehase, quinone (1.3.5.2) | Class 2 membrane DHODH (PyrD) |
| 5 | orotate + PRPP → OMP | orotate PRTase (2.4.2.10) | PyrE (type I PRTase) |
| 6 | OMP → UMP + CO₂ | OMP decarboxylase (4.1.1.23) | PyrF |

Architecture note: *P. putida* uses the bacterial **separate-protein** organization (not the animal CAD/UMPS fusions). This does not change the six leaves.

---

## 4. Candidate genes and evidence

### High-confidence de novo UMP leaves (mark `covered`)

| Step | Gene / locus | UniProt | Role | Evidence basis | Curation caveat |
|------|--------------|---------|------|----------------|-----------------|
| 1 | **carB** / PP_4723 | Q88DU6 | CPS large chain (ATP, EC 6.3.4.16/6.3.5.5) | Homology + operon `carAB`; strong across γ-proteobacteria | **Primary bucket `ppu00220`**; carbamoyl-P shared with arginine biosynthesis. Usually single CPS in *Pseudomonas* → also required for arginine. |
| 1 | **carA** / PP_4724 | Q88DU5 | CPS small chain (glutaminase, EC 6.3.5.5) | Homology + operon | Same shared-node caveat. |
| 2 | **pyrB** / PP_4998 | Q88D30 | ATCase catalytic subunit (EC 2.1.3.2) | **Direct in *P. putida*** — cloned, complements *E. coli* pyrB (PMID 7896697) | Regulatory nucleotide site is in an N-terminal extension of PyrB itself; no separate PyrI regulatory chain. Part of `pyrR-pyrB-pyrC'` cluster. |
| 3 | **pyrC** / PP_1086 | Q88NW7 | Dihydroorotase (EC 3.5.2.3) | Homology; **the catalytic DHOase** distinct from ATCase complex (inference supported by PMID 7896697, which shows the *pyrC'* copy is inactive) | This is the functional step-3 gene, NOT PP_4999. Promote to full review to confirm catalytic His residues. |
| 4 | **pyrD** / PP_2095 | Q88L40 | Dihydroorotate dehydrogenase, quinone-dependent (EC 1.3.5.2) | Homology; **class 2** membrane-associated DHODH is expected for an obligate aerobe using ubiquinone | Correct enzyme class for *Pseudomonas*; not the cytosolic class 1. |
| 5 | **pyrE** / PP_5291 | Q88C92 | Orotate phosphoribosyltransferase (EC 2.4.2.10) | Homology; conserved bacterial PyrE | High confidence; standalone (no PyrE-PyrF fusion). |
| 6 | **pyrF** / PP_1815 | Q88LW2 | OMP decarboxylase (EC 4.1.1.23) | Homology; conserved bacterial PyrF | High confidence; genetic marker (5-FOA sensitivity) in many taxa. |

### The pseudo-enzyme (over-annotation flag)

| Gene | UniProt | Current annotation | Corrected interpretation |
|------|---------|--------------------|--------------------------|
| **pyrC'** / PP_4999 | Q88D29 | "Dihydroorotase-like protein (EC 3.5.2.3)" | **Catalytically inactive vestigial DHOase.** In *P. putida* the 44.2-kDa PyrC′ lacks catalytic histidyl residues, has no DHOase activity, and does **not** complement *E. coli pyrC*; its role is **structural** — required to assemble the dodecameric ATCase holoenzyme (PMID 7896697). **EC 3.5.2.3 is over-propagated.** |

### Regulatory genes (not catalytic leaves)

- **pyrR / PP_4997** (Q88D31): "Pyrimidine operon regulatory protein/UPRTase (EC 2.4.2.9)", clustered with `pyrB-pyrC'`. Regulatory + possible moonlighting UPRTase.
- **PP_3238** (Q88HW5): "Transcriptional regulator PyrR."
- Caveat: PyrR-protein-mediated attenuation is characteristic of **Gram-positives**; enteric Gram-negatives regulate `pyr` operons by **PyrR-independent** UTP-sensitive reiterative transcription / coupled attenuation (PMID 18535147). Whether *P. putida* uses a genuine PyrR mechanism is **not established for the target strain** (open question). The EC 2.4.2.9 (UPRTase) label on PyrR is paralogy-based; the bona fide salvage UPRTase is **upp/PP_0746**.

### Out-of-module candidates (keep separate)

Downstream/interconversion: `pyrH` (PP_1593, UMP kinase), `ndk` (PP_0849), `cmk` (PP_1771), `pyrG` (PP_1610, CTP synthase), `nrdA/nrdB`, `dcd`, `dut`, `thyA`, `maf-1`, `mazG`.
Salvage/degradation: `upp`, `ppnP`, `codA`, `ushA`, `surE`, PP_2531, PP_3662.
Reductive catabolism (`ppu00410`): `pydA/pydB/pydX`, `hyuC`, PP_0614.
Uncertain/mis-bucketed: PP_0488 (NADP dehydrogenase, EC 1.1.1.-), `ydfG`/PP_4862, `ygjP`/PP_4958 ("metal-dependent hydrolase" — generic; could be spuriously linked to DHOase family but no evidence it is a UMP-pathway enzyme).

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **Dihydroorotase paralog ambiguity (highest priority).** Two EC 3.5.2.3 genes (`pyrC`/PP_1086 active; `pyrC'`/PP_4999 inactive). **Over-annotation on PP_4999.** Direct target-species evidence (PMID 7896697). Curation must route step 3 to PP_1086 and re-label PP_4999 as a pseudo-dihydroorotase / ATCase assembly subunit.
2. **Step-1 bucket mismatch.** `carA/carB` in `ppu00220`, not `ppu00240`. Not a gap — a cross-bucket module dependency. Shared with arginine biosynthesis; typically a **single CPS** in *Pseudomonas*, so it is essential to both pathways.
3. **`ygjP`/PP_4958 "metal-dependent hydrolase."** Broad, non-specific annotation in the `ppu00240` bucket. No evidence it participates in de novo UMP synthesis; likely unrelated amidohydrolase-superfamily member. Do not count toward any leaf.
4. **Regulatory over-mapping.** `PyrR`/`pyrR` UPRTase EC labels can be mistaken for salvage/biosynthetic function. They are regulatory; mechanism in *P. putida* uncertain.
5. **No leaf is missing.** No step requires a lineage-specific alternative enzyme in this organism; the standard bacterial enzyme set is present.

---

## 6. Module and GO-curation recommendations

| Module step | Status | Basis |
|-------------|--------|-------|
| 1. carbamoyl-P synthesis | **covered** (cross-bucket) | `carA/carB` (PP_4724/PP_4723); note `ppu00220` bucket + arginine sharing |
| 2. aspartate carbamoylation | **covered** | `pyrB`/PP_4998; direct *P. putida* evidence (PMID 7896697) |
| 3. dihydroorotate ring closure | **covered** — assign to PP_1086; **do NOT** use PP_4999 | PP_1086 active DHOase; PP_4999 inactive pseudo-enzyme (PMID 7896697) |
| 4. dihydroorotate oxidation | **covered** | `pyrD`/PP_2095, class 2 quinone DHODH (EC 1.3.5.2) |
| 5. orotate phosphoribosylation | **covered** | `pyrE`/PP_5291 (EC 2.4.2.10) |
| 6. OMP decarboxylation | **covered** | `pyrF`/PP_1815 (EC 4.1.1.23) |

**Module-document actions:**
- Add an explicit note that step-1 genes live in `ppu00220`; the module should reference them despite the bucket boundary. Generic module boundaries are **not wrong**, but need the shared-carbamoyl-P annotation.
- Add a curation flag on PP_4999: pseudo-dihydroorotase (ATCase assembly subunit), **suppress EC 3.5.2.3 as functional**. Consider requesting/using a GO term for "protein-containing complex scaffold / ATCase assembly" and demoting `GO:0004151 dihydroorotase activity` to NOT for PP_4999.
- No new module document is required. No new GO **term** request is strictly needed, but a **GO annotation correction** (remove dihydroorotase MF from PP_4999; keep on PP_1086) is warranted.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_4999 (`pyrC'`)** — confirm pseudo-enzyme status; remove functional DHOase EC/GO; annotate structural ATCase role. *(Direct evidence exists — highest priority.)*
2. **PP_1086 (`pyrC`)** — confirm it is the sole catalytic dihydroorotase; verify conserved metal-binding His residues.
3. **PP_2095 (`pyrD`)** — confirm class 2 (membrane, quinone) assignment vs. class 1.
4. **PP_4997 (`pyrR`) and PP_3238 (`PyrR`)** — clarify regulatory role and whether UPRTase EC 2.4.2.9 should be retained; resolve redundancy of two PyrR-like loci.
5. **PP_4958 (`ygjP`)** — decide whether it belongs in the `ppu00240` bucket at all.

---

## 8. Evidence quality and open questions

- **Direct target-species (KT2440 / *P. putida*) experimental evidence:** ATCase organization, PyrB catalytic subunit, and the inactive PyrC′ pseudo-enzyme (PMID 7896697). **Strong, do not need transfer.**
- **Homology/pathway-database inference:** `carAB`, `pyrC` (PP_1086), `pyrD`, `pyrE`, `pyrF` gene identities. Well supported by conserved bacterial `pyr` biology (PMIDs 7516791, 8787418, 10517335) but **not individually enzymatically verified in KT2440** — standard confidence for a housekeeping pathway.
- **Uncertain / species-transfer caveats:** the regulatory mechanism (PyrR-mediated vs. enteric-style attenuation; PMID 18535147) is not established for *P. putida*; DHODH class assignment inferred, not shown in KT2440.
- **Experiments/expert questions that would resolve gaps:** (i) enzymatic assay or complementation of PP_1086 vs. PP_4999 to confirm which is the active DHOase in KT2440; (ii) knockout of `carAB` to confirm dual arginine/pyrimidine auxotrophy; (iii) determine `pyr` operon regulation mode in *P. putida* (does PyrR/PP_4997 bind pyr mRNA?).

---

## 9. Key references

- Schurr MJ, Vickrey JF, Kumar AP, et al. *Aspartate transcarbamoylase genes of Pseudomonas putida: requirement for an inactive dihydroorotase for assembly into the dodecameric holoenzyme.* J Bacteriol. 1995. **PMID 7896697.** *(Direct target-species evidence for PyrB/PyrC′.)*
- Turnbough CL Jr, Switzer RL. *Regulation of pyrimidine biosynthetic gene expression in bacteria: repression without repressors.* Microbiol Mol Biol Rev. 2008. **PMID 18535147.** *(Gram-positive PyrR vs. enteric attenuation.)*
- Ghim SY, Nielsen P, Neuhard J. *Molecular characterization of pyrimidine biosynthesis genes from the thermophile Bacillus caldolyticus.* 1994. **PMID 7516791.** *(Canonical six-gene pyr set / operon organization.)*
- Grabner GK, Switzer RL. *Kinetic studies of the UPRTase reaction catalyzed by the B. subtilis PyrR.* J Biol Chem. 2003. **PMID 12482852.** *(PyrR is a bifunctional UPRTase-homolog regulator.)*
- Yamagishi A, et al. *pyrE and pyrF of Thermus thermophilus.* 1996. **PMID 8787418**; Watrin L, et al. *pyrE of Pyrococcus abyssi.* 1999. **PMID 10517335.** *(pyrE/pyrF as the terminal de novo UMP genes.)*

*Prepared for manual module-satisfiability and gene-annotation curation. Confidence levels and species-transfer strength are stated per claim above.*


## Artifacts

- [OpenScientist final report](PSEPK__de_novo_pyrimidine_synthesis__ppu00240-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__de_novo_pyrimidine_synthesis__ppu00240-deep-research-openscientist_artifacts/final_report.pdf)