---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T12:53:04.617875'
end_time: '2026-08-08T13:15:00.275583'
duration_seconds: 1315.66
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: methylglyoxal_detoxification
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00620
  pathway_id: ppu00620
  pathway_name: Pyruvate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00620 with 9 primary genes; module
    area: central_carbon.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '54'
  candidate_genes: '- scpC: PP_0154 | Q88RH5 | Propionyl-CoA:succinate CoA transferase
    (EC 2.8.3.-) (EC 2.8.3.-; primary bucket kegg:ppu00020)

    - aceF: PP_0338 | Q88QZ6 | Acetyltransferase component of pyruvate dehydrogenase
    complex (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)

    - aceE: PP_0339 | Q88QZ5 | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) (EC
    1.2.4.1; primary bucket kegg:ppu00785)

    - glcB: PP_0356 | Q88QX8 | Malate synthase G (EC 2.3.3.9) (EC 2.3.3.9; primary
    bucket kegg:ppu00620)

    - aldB-I: PP_0545 | Q88QE9 | Aldehyde dehydrogenase (EC 1.2.1.3) (EC 1.2.1.3;
    primary bucket kegg:ppu00010)

    - acoC: PP_0553 | Q88QE1 | Dihydrolipoyllysine-residue acetyltransferase component
    of acetoin cleaving system (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)

    - accC: PP_0558 | Q88QD6 | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A
    carboxylase biotin carboxylase subunit A) (EC 6.3.4.14; primary bucket kegg:ppu00061)

    - accB: PP_0559 | Q88QD5 | Biotin carboxyl carrier protein of acetyl-CoA carboxylase
    (primary bucket kegg:ppu00061)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37;
    primary bucket kegg:ppu00566)

    - mqo1: PP_0751 | Q88PU7 | Probable malate:quinone oxidoreductase 1 (EC 1.1.5.4)
    (MQO 1) (Malate dehydrogenase [quinone] 1) (EC 1.1.5.4; primary bucket kegg:ppu00020)

    - PP_0772: PP_0772 | Q88PS6 | Metallo-beta-lactamase family protein (primary bucket
    kegg:ppu00620)

    - pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase)
    (EC 2.3.1.8; primary bucket kegg:ppu00430)

    - PP_0897: PP_0897 | Q88PF3 | Fumarate hydratase class I (EC 4.2.1.2) (EC 4.2.1.2;
    primary bucket kegg:ppu00020)

    - fumC-I: PP_0944 | Q88PA6 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2)
    (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)

    - leuA: PP_1025 | Q88P28 | 2-isopropylmalate synthase (EC 2.3.3.13) (Alpha-IPM
    synthase) (Alpha-isopropylmalate synthase) (EC 2.3.3.13; primary bucket kegg:ppu00290)

    - mqo2: PP_1251 | Q88NF9 | Probable malate:quinone oxidoreductase 2 (EC 1.1.5.4)
    (MQO 2) (Malate dehydrogenase [quinone] 2) (EC 1.1.5.4; primary bucket kegg:ppu00020)

    - ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate
    reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81;
    primary bucket kegg:ppu00030)

    - pykA: PP_1362 | Q88N54 | Pyruvate kinase (EC 2.7.1.40) (EC 2.7.1.40; primary
    bucket kegg:ppu00010)

    - PP_1389: PP_1389 | Q88N27 | Oxaloacetate decarboxylase (EC 4.1.1.112) (EC 4.1.1.112;
    primary bucket kegg:ppu00620)

    - ppc: PP_1505 | Q88MR4 | Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC
    4.1.1.31) (EC 4.1.1.31; primary bucket kegg:ppu00710)

    - accA: PP_1607 | Q88MG4 | Acetyl-coenzyme A carboxylase carboxyl transferase
    subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyltransferase
    subunit alpha) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)

    - frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1)
    (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III)
    (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary
    bucket kegg:ppu00626)

    - ldhA: PP_1649 | Q88MC4 | D-lactate dehydrogenase (EC 1.1.1.28) (EC 1.1.1.28;
    primary bucket kegg:ppu00620)

    - fumC: PP_1755 | Q88M20 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2)
    (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)

    - accD: PP_1996 | Q88LD9 | Acetyl-coenzyme A carboxylase carboxyl transferase
    subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltransferase
    subunit beta) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)

    - ppsA: PP_2082 | Q88L53 | Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2)
    (Pyruvate, water dikinase) (EC 2.7.9.2; primary bucket kegg:ppu00680)

    - PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary
    bucket kegg:ppu00680)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - calA: PP_2426 | Q88K65 | Coniferyl alcohol dehydrogenase (EC 1.1.1.194) (EC
    1.1.1.194; primary bucket kegg:ppu00561)

    - pedE: PP_2674 | Q88JH5 | Quinoprotein alcohol dehydrogenase PedE (EC 1.1.2.8)
    (Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Ca(2+)-dependent
    PQQ-ADH) (EC 1.1.2.8; primary bucket kegg:ppu00625)

    - pedH: PP_2679 | Q88JH0 | Quinoprotein alcohol dehydrogenase PedH (EC 1.1.2.-)
    (Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase)
    (Lanthanide-dependent PQQ-ADH) (EC 1.1.2.-; primary bucket kegg:ppu00625)

    - aldB-II: PP_2680 | Q88JG9 | Aldehyde dehydrogenase (EC 1.2.1.3) (EC 1.2.1.3;
    primary bucket kegg:ppu00010)

    - mqo3: PP_2925 | Q88IS4 | Probable malate:quinone oxidoreductase 3 (EC 1.1.5.4)
    (MQO 3) (Malate dehydrogenase [quinone] 3) (EC 1.1.5.4; primary bucket kegg:ppu00020)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - PP_3382: PP_3382 | Q88HH6 | Gluconate 2-dehydrogenase cytochrome c subunit (EC
    1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)

    - adhB: PP_3623 | Q88GU4 | Alcohol dehydrogenase cytochrome c subunit (primary
    bucket kegg:ppu00030)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - gloA: PP_3766 | Q88GF8 | Lactoylglutathione lyase (EC 4.4.1.5) (Glyoxalase I)
    (EC 4.4.1.5; primary bucket kegg:ppu00620)

    - adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1)
    (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)

    - gloB: PP_4144 | Q88FF3 | Hydroxyacylglutathione hydrolase (EC 3.1.2.6) (Glyoxalase
    II) (Glx II) (EC 3.1.2.6; primary bucket kegg:ppu00620)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - pyk: PP_4301 | Q88EZ9 | Pyruvate kinase (EC 2.7.1.40) (EC 2.7.1.40; primary
    bucket kegg:ppu00010)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1)
    (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2)
    (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - lldD: PP_4736 | Q88DT3 | L-lactate dehydrogenase (EC 1.1.-.-) (EC 1.1.-.-; primary
    bucket kegg:ppu00620)

    - dld2: PP_4737 | Q88DT2 | D-lactate dehydrogenase (EC 1.1.-.-) (EC 1.1.-.-; primary
    bucket kegg:ppu00620)

    - maeB: PP_5085 | Q88CU5 | NADP-dependent malic enzyme (EC 1.1.1.40) (EC 1.1.1.40;
    primary bucket kegg:ppu00710)

    - ycgM: PP_5153 | Q88CM7 | Isomerase/hydrolase (EC 3.-.-.-) (EC 3.-.-.-; primary
    bucket kegg:ppu00620)

    - pycB: PP_5346 | Q88C37 | Pyruvate carboxylase subunit B (EC 6.4.1.1) (EC 6.4.1.1;
    primary bucket kegg:ppu00020)

    - pycA: PP_5347 | Q88C36 | Biotin carboxylase (Acetyl-coenzyme A carboxylase biotin
    carboxylase subunit A) (primary bucket kegg:ppu00020)

    - lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)'
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__methylglyoxal-detoxification__ppu00620-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__methylglyoxal-detoxification__ppu00620-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

methylglyoxal_detoxification in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00620
- Resolved ID: ppu00620
- Resolved name: Pyruvate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00620 with 9 primary genes; module area: central_carbon.

## Candidate Genes From Local Metadata

Candidate gene count: 54

- scpC: PP_0154 | Q88RH5 | Propionyl-CoA:succinate CoA transferase (EC 2.8.3.-) (EC 2.8.3.-; primary bucket kegg:ppu00020)
- aceF: PP_0338 | Q88QZ6 | Acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)
- aceE: PP_0339 | Q88QZ5 | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) (EC 1.2.4.1; primary bucket kegg:ppu00785)
- glcB: PP_0356 | Q88QX8 | Malate synthase G (EC 2.3.3.9) (EC 2.3.3.9; primary bucket kegg:ppu00620)
- aldB-I: PP_0545 | Q88QE9 | Aldehyde dehydrogenase (EC 1.2.1.3) (EC 1.2.1.3; primary bucket kegg:ppu00010)
- acoC: PP_0553 | Q88QE1 | Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)
- accC: PP_0558 | Q88QD6 | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) (EC 6.3.4.14; primary bucket kegg:ppu00061)
- accB: PP_0559 | Q88QD5 | Biotin carboxyl carrier protein of acetyl-CoA carboxylase (primary bucket kegg:ppu00061)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37; primary bucket kegg:ppu00566)
- mqo1: PP_0751 | Q88PU7 | Probable malate:quinone oxidoreductase 1 (EC 1.1.5.4) (MQO 1) (Malate dehydrogenase [quinone] 1) (EC 1.1.5.4; primary bucket kegg:ppu00020)
- PP_0772: PP_0772 | Q88PS6 | Metallo-beta-lactamase family protein (primary bucket kegg:ppu00620)
- pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) (EC 2.3.1.8; primary bucket kegg:ppu00430)
- PP_0897: PP_0897 | Q88PF3 | Fumarate hydratase class I (EC 4.2.1.2) (EC 4.2.1.2; primary bucket kegg:ppu00020)
- fumC-I: PP_0944 | Q88PA6 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)
- leuA: PP_1025 | Q88P28 | 2-isopropylmalate synthase (EC 2.3.3.13) (Alpha-IPM synthase) (Alpha-isopropylmalate synthase) (EC 2.3.3.13; primary bucket kegg:ppu00290)
- mqo2: PP_1251 | Q88NF9 | Probable malate:quinone oxidoreductase 2 (EC 1.1.5.4) (MQO 2) (Malate dehydrogenase [quinone] 2) (EC 1.1.5.4; primary bucket kegg:ppu00020)
- ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81; primary bucket kegg:ppu00030)
- pykA: PP_1362 | Q88N54 | Pyruvate kinase (EC 2.7.1.40) (EC 2.7.1.40; primary bucket kegg:ppu00010)
- PP_1389: PP_1389 | Q88N27 | Oxaloacetate decarboxylase (EC 4.1.1.112) (EC 4.1.1.112; primary bucket kegg:ppu00620)
- ppc: PP_1505 | Q88MR4 | Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC 4.1.1.31) (EC 4.1.1.31; primary bucket kegg:ppu00710)
- accA: PP_1607 | Q88MG4 | Acetyl-coenzyme A carboxylase carboxyl transferase subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyltransferase subunit alpha) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- ldhA: PP_1649 | Q88MC4 | D-lactate dehydrogenase (EC 1.1.1.28) (EC 1.1.1.28; primary bucket kegg:ppu00620)
- fumC: PP_1755 | Q88M20 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)
- accD: PP_1996 | Q88LD9 | Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltransferase subunit beta) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)
- ppsA: PP_2082 | Q88L53 | Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2) (Pyruvate, water dikinase) (EC 2.7.9.2; primary bucket kegg:ppu00680)
- PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary bucket kegg:ppu00680)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- calA: PP_2426 | Q88K65 | Coniferyl alcohol dehydrogenase (EC 1.1.1.194) (EC 1.1.1.194; primary bucket kegg:ppu00561)
- pedE: PP_2674 | Q88JH5 | Quinoprotein alcohol dehydrogenase PedE (EC 1.1.2.8) (Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Ca(2+)-dependent PQQ-ADH) (EC 1.1.2.8; primary bucket kegg:ppu00625)
- pedH: PP_2679 | Q88JH0 | Quinoprotein alcohol dehydrogenase PedH (EC 1.1.2.-) (Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase) (Lanthanide-dependent PQQ-ADH) (EC 1.1.2.-; primary bucket kegg:ppu00625)
- aldB-II: PP_2680 | Q88JG9 | Aldehyde dehydrogenase (EC 1.2.1.3) (EC 1.2.1.3; primary bucket kegg:ppu00010)
- mqo3: PP_2925 | Q88IS4 | Probable malate:quinone oxidoreductase 3 (EC 1.1.5.4) (MQO 3) (Malate dehydrogenase [quinone] 3) (EC 1.1.5.4; primary bucket kegg:ppu00020)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- PP_3382: PP_3382 | Q88HH6 | Gluconate 2-dehydrogenase cytochrome c subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- adhB: PP_3623 | Q88GU4 | Alcohol dehydrogenase cytochrome c subunit (primary bucket kegg:ppu00030)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- gloA: PP_3766 | Q88GF8 | Lactoylglutathione lyase (EC 4.4.1.5) (Glyoxalase I) (EC 4.4.1.5; primary bucket kegg:ppu00620)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)
- gloB: PP_4144 | Q88FF3 | Hydroxyacylglutathione hydrolase (EC 3.1.2.6) (Glyoxalase II) (Glx II) (EC 3.1.2.6; primary bucket kegg:ppu00620)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- pyk: PP_4301 | Q88EZ9 | Pyruvate kinase (EC 2.7.1.40) (EC 2.7.1.40; primary bucket kegg:ppu00010)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- lldD: PP_4736 | Q88DT3 | L-lactate dehydrogenase (EC 1.1.-.-) (EC 1.1.-.-; primary bucket kegg:ppu00620)
- dld2: PP_4737 | Q88DT2 | D-lactate dehydrogenase (EC 1.1.-.-) (EC 1.1.-.-; primary bucket kegg:ppu00620)
- maeB: PP_5085 | Q88CU5 | NADP-dependent malic enzyme (EC 1.1.1.40) (EC 1.1.1.40; primary bucket kegg:ppu00710)
- ycgM: PP_5153 | Q88CM7 | Isomerase/hydrolase (EC 3.-.-.-) (EC 3.-.-.-; primary bucket kegg:ppu00620)
- pycB: PP_5346 | Q88C37 | Pyruvate carboxylase subunit B (EC 6.4.1.1) (EC 6.4.1.1; primary bucket kegg:ppu00020)
- pycA: PP_5347 | Q88C36 | Biotin carboxylase (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) (primary bucket kegg:ppu00020)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

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

# Module/Pathway/Taxon Review — Methylglyoxal Detoxification in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Nominal bucket:** KEGG `ppu00620` "Pyruvate metabolism" (module area: central carbon)
**Review focus:** methylglyoxal (MG) detoxification module satisfiability and gene-annotation curation

---

## 1. Executive Summary

The methylglyoxal (MG) detoxification module is **fully satisfiable** in *Pseudomonas putida* KT2440 through a complete, canonical, glutathione (GSH)-dependent glyoxalase system. Both enzymatic steps are encoded: **glyoxalase I** (`gloA` = PP_3766, lactoylglutathione lyase, EC 4.4.1.5) and **glyoxalase II** (`gloB` = PP_4144, hydroxyacylglutathione hydrolase, EC 3.1.2.6). These two enzymes sequentially convert the spontaneously-formed GSH–MG hemithioacetal into D-lactate and regenerate GSH. Crucially, the *P. putida* glyoxalase I gene has **direct experimental validation**: heterologous expression detoxified MG in *E. coli* and in mammalian (CHO) cells, giving PP_3766 an unusually strong evidence footing for a KT2440 metabolic gene. The GSH cofactor required by this route is itself synthesizable, since both de novo biosynthesis steps — `gshA` (PP_0243) and `gshB` (PP_4993) — are encoded, so the module is cofactor-satisfiable and does not depend on GSH import.

The one "step" that is **not expected** in this organism is the *generation* of MG by a dedicated methylglyoxal synthase. Exhaustive UniProt searches of the KT2440 proteome (and of all *P. putida*) for methylglyoxal synthase / `mgsA` / EC 4.2.3.3 returned **zero hits**. In KT2440, MG arises non-enzymatically (and as a metabolic side-product) rather than through the *E. coli*-style MgsA bypass. This is a meaningful curation distinction: a generic MG module that expects an MG synthase should mark that step `not_expected_in_target_taxon` for KT2440 rather than as a gap.

Finally, this review flags a mismatch between the delivered "pyruvate metabolism" candidate list (54 genes, dominated by central-carbon enzymes) and the biology of the MG-detox module. The genuinely MG-relevant genes are a small subset (`gloA`, `gloB`, plus downstream lactate dehydrogenases feeding D-lactate to pyruvate), while several real alternative-route detox candidates are **absent from the candidate metadata** and should be curated separately: a second glyoxalase-II-family paralog (**PP_0772**), reductive aldo-keto reductases (**`yeaE`/PP_3120**, **`dkgB`/PP_2368**), and DJ-1/ThiJ/PfpI-superfamily glyoxalase-III candidates (**PP_0893, PP_2491, PP_2992, PP_3431**). Conversely, `ycgM` (PP_5153), despite sitting in the `ppu00620` bucket, is a fumarylacetoacetase-family enzyme unrelated to MG and should be excluded from the module.

---

## 2. Target-Organism Pathway Definition

**Process included.** "Methylglyoxal detoxification" is the conversion of the reactive dicarbonyl 2-oxopropanal (methylglyoxal, MG) — a cytotoxic electrophile that glycates DNA, RNA, and protein — into a non-toxic hydroxy acid. In the canonical glutathione-dependent route the module comprises exactly two catalytic steps operating on the non-enzymatically formed GSH–MG adduct:

1. **Glyoxalase I (GlxI, EC 4.4.1.5):** isomerizes the hemithioacetal of GSH + MG to (R)-S-lactoylglutathione.
2. **Glyoxalase II (GlxII, EC 3.1.2.6):** hydrolyzes S-lactoylglutathione to **D-lactate**, regenerating GSH.

The D-lactate product then enters central carbon metabolism (oxidation to pyruvate), which is why the module is administratively bucketed under KEGG **ppu00620 "Pyruvate metabolism."**

**Boundaries — neighboring processes to keep separate.**
- **MG *generation*** (methylglyoxal synthase, `mgsA`, EC 4.2.3.3, from dihydroxyacetone phosphate) is a distinct, catabolic-overflow process. It is a separate pathway node and, as shown below, is not encoded in KT2440.
- **Glutathione metabolism (ppu00480):** GSH biosynthesis (`gshA`/`gshB`) and recycling is an upstream cofactor-supply module, not part of the two-step detox module itself, but it gates satisfiability.
- **Downstream lactate oxidation** (D-/L-lactate dehydrogenases; pyruvate metabolism proper) is a separate, well-populated central-carbon module.
- **Glycolysis / triose-phosphate handling (ppu00010):** the non-enzymatic *source* of MG, not its detox.
- **GSH-independent MG detox** (aldo-keto reductase reductive route to acetol/lactaldehyde; DJ-1/glyoxalase-III direct hydrolysis to lactate) are alternative modules/routes that should be documented separately, not merged into the glyoxalase module.

**Alternate names / database definitions.** Glyoxalase system; GlxI / GloA / lactoylglutathione lyase / aldoketomutase (EC 4.4.1.5); GlxII / GloB / hydroxyacylglutathione hydrolase / S-2-hydroxyacylglutathione hydrolase (EC 3.1.2.6); "methylglyoxal degradation" (MetaCyc/BioCyc). The broad KEGG "Pyruvate metabolism" map (ppu00620) is an overview bucket and is *not* an MG-specific module — hence the candidate list is dominated by unrelated central-carbon enzymes.

**Cofactor requirement (verified).** The glyoxalase route depends on a regenerated glutathione pool; KT2440 encodes complete de novo GSH biosynthesis — `gshA` (PP_0243, EC 6.3.2.2) and `gshB` (PP_4993, EC 6.3.2.3), plus a second putative γ-glutamylcysteine ligase (PP_3253) — so the primary route is satisfiable at both the enzyme and cofactor level.

---

## 3. Expected Step Model

| Step | Reaction | Enzyme / EC | Expected in KT2440? | Encoded by |
|------|----------|-------------|---------------------|------------|
| (0) MG generation | DHAP → methylglyoxal + Pi | Methylglyoxal synthase, EC 4.2.3.3 (`mgsA`) | **No** (not_expected_in_target_taxon) | *none found* |
| (pre) Adduct formation | MG + GSH → hemithioacetal | non-enzymatic | Yes (spontaneous) | — |
| 1 | hemithioacetal → (R)-S-lactoylglutathione | **Glyoxalase I, EC 4.4.1.5** | **Yes (covered)** | `gloA` / PP_3766 |
| 2 | S-lactoylglutathione + H₂O → D-lactate + GSH | **Glyoxalase II, EC 3.1.2.6** | **Yes (covered)** | `gloB` / PP_4144 (+ paralog PP_0772) |
| cofactor | Glu+Cys→γ-EC→GSH | GshA EC 6.3.2.2 / GshB EC 6.3.2.3 | **Yes (covered)** | PP_0243 / PP_4993 |
| downstream | D-lactate → pyruvate | D-/L-lactate DH | Yes (covered) | `ldhA`/PP_1649, `dld2`/PP_4737, `lldD`/PP_4736 |
| alt route A | MG → acetol / lactaldehyde (reductive, GSH-independent) | Aldo-keto reductase, EC 1.1.1.- | Likely (candidate_uncertain) | `yeaE`/PP_3120, `dkgB`/PP_2368 |
| alt route B | MG → D-lactate directly (GSH-independent) | Glyoxalase III / DJ-1, EC 4.2.1.130 | Possible (candidate_uncertain) | PP_0893, PP_2491, PP_2992, PP_3431 |

```
        (no MgsA in KT2440)
             DHAP ─────X──────►  [methylglyoxal synthase absent]
                                        │
   spontaneous side-product ────────────┤
                                        ▼
                              METHYLGLYOXAL (MG)
        ┌──────────────────────────────┼───────────────────────────────┐
        │ GSH-DEPENDENT (canonical)     │ GSH-INDEPENDENT (alternatives) │
        │                               │                                │
   MG + GSH (spontaneous)          reductive AKR route            glyoxalase III / DJ-1
        │                          (yeaE PP_3120,                 (PP_0893/2491/2992/3431)
        ▼                           dkgB PP_2368)                        │
  hemithioacetal                        │                                │
        │  gloA (GlxI, PP_3766) ✔       ▼                                ▼
        ▼      EC 4.4.1.5          acetol / lactaldehyde            D-lactate (direct)
 (R)-S-lactoylglutathione               │                                │
        │  gloB (GlxII, PP_4144) ✔      ▼                                │
        │  + PP_0772 paralog        further reduction/oxidation          │
        ▼      EC 3.1.2.6                │                                │
   D-LACTATE + GSH(regen) ──────────────┴────────────────────────────────┘
        │
        ▼  ldhA/dld2/lldD  →  PYRUVATE  →  central carbon (ppu00620)
```

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence, module-defining genes

**`gloA` — PP_3766 (Q88GF8) — Glyoxalase I (EC 4.4.1.5).** This is the core, rate-relevant enzyme of the module. UniProt annotates it as lactoylglutathione lyase with the catalytic activity (R)-S-lactoylglutathione = methylglyoxal + glutathione, and it carries Ni/Zn metal-binding keywords consistent with a metalloisomerase glyoxalase I. It maps to KEGG ppu00620. Its UniProt existence level is 3 (inferred from homology), but the *P. putida* glyoxalase I gene itself has **direct functional evidence** independent of that annotation: heterologous expression in *E. coli* and in Chinese hamster ovary cells produced substantial MG reductions (35–43% intracellular MG in *E. coli*; 80–90% in CHO cells) ([PMID: 11461144](https://pubmed.ncbi.nlm.nih.gov/11461144/); [PMID: 22358913](https://pubmed.ncbi.nlm.nih.gov/22358913/)). *P. putida* GlxI is a classically studied enzyme, and its metal-activation class (Ni²⁺ vs Zn²⁺) and distinctive loop/helix features have been characterized ([PMID: 10824093](https://pubmed.ncbi.nlm.nih.gov/10824093/); [PMID: 25557363](https://pubmed.ncbi.nlm.nih.gov/25557363/)). **Curation call: covered (high confidence). Promote to full `fetch-gene` review** to attach the experimental citations, lock metal class, and confirm the KT2440 locus corresponds to the historically studied *P. putida* GlxI.

**`gloB` — PP_4144 (Q88FF3) — Glyoxalase II (EC 3.1.2.6).** Annotated as hydroxyacylglutathione hydrolase (S-(2-hydroxyacyl)glutathione + H₂O = 2-hydroxy carboxylate + glutathione), mapping to ppu00620, existence level 3. InterPro signatures are specific to the GlxII subfamily: IPR017782 (hydroxyacylglutathione hydrolase), IPR035680 (Glx_II metallo-β-lactamase), and an HAGH_C domain — i.e., a bona fide glyoxalase II, not merely a generic metallo-β-lactamase. **Curation call: covered.** One important caveat for module *weighting*: in *E. coli*, a ΔgloB mutant remains as MG-tolerant as wild type despite showing the same block in MG detoxification as ΔgloA ([PMID: 21143325](https://pubmed.ncbi.nlm.nih.gov/21143325/)). This indicates GlxII is not the tolerance-limiting step — the accumulation and disposal of S-lactoylglutathione at the GlxI step is what governs tolerance. For satisfiability the module still needs a GlxII activity, but curators should not treat `gloB` as the essential determinant.

**`gshA` — PP_0243 (Q88R90) — glutamate–cysteine ligase (EC 6.3.2.2)** and **`gshB` — PP_4993 (Q88D35) — glutathione synthetase (EC 6.3.2.3).** Both de novo GSH-biosynthesis steps are encoded (a second putative γ-glutamylcysteine ligase, PP_3253, also exists), so the GSH cofactor consumed transiently and regenerated by the glyoxalase cycle is supplied endogenously. **Curation call: cofactor supply covered.** These belong to glutathione metabolism, not the detox module proper, but they gate its satisfiability and should be cross-linked.

### 4.2 Downstream disposal (genuinely in ppu00620)

The D-lactate produced by GlxII is returned to pyruvate metabolism by lactate dehydrogenases already in the candidate list: **`ldhA`/PP_1649** (D-lactate DH, EC 1.1.1.28), **`dld2`/PP_4737** (D-lactate DH, EC 1.1.-.-), and **`lldD`/PP_4736** (L-lactate DH). These are correctly bucketed and give the module a plausible sink into central carbon. **Curation call: covered (downstream), low ambiguity** — though these are multifunctional central-carbon enzymes and should not be labeled MG-specific.

### 4.3 Second glyoxalase-II candidate (present in bucket, missing from list logic)

**PP_0772 (Q88PS6) — "Metallo-β-lactamase family protein," ppu00620.** InterPro classifies PP_0772 with IPR051453 "MBL_Glyoxalase_II" together with IPR001279 (metallo-β-lactamase fold) and IPR036866 (RNase Z / hydroxyglutathione hydrolase). It therefore falls in the **glyoxalase-II subfamily** and is a credible second GlxII-family activity, distinct from the primary `gloB` (which carries the more specific IPR017782/IPR035680/HAGH_C signatures). Note that the IPR051453 subfamily also contains non-glyoxalase metallo-hydrolases (persulfide dioxygenase/ETHE1, tRNase Z), so specificity is not guaranteed. **Curation call: candidate_uncertain; promote to full review** to resolve whether PP_0772 is a true GlxII, an ETHE1-type sulfur dioxygenase, or a tRNase Z.

### 4.4 Genes in the bucket that are NOT MG-related

**`ycgM` — PP_5153 (Q88CM7) — "Isomerase/hydrolase (EC 3.-.-.-)," ppu00620.** Despite the vague EC and its placement in the pyruvate bucket, InterPro assigns it to the **fumarylacetoacetase-like (FAH) family** (IPR011234 / PF01557), a hydratase/decarboxylase fold with no glyoxalase activity. **Curation call: exclude from the MG module** (over-broad EC placeholder driving spurious inclusion).

The remaining ~48 candidate genes (PDH complex `aceE`/`aceF`/`lpd`, ACC `accABCD`, malate/fumarate enzymes, pyruvate kinases, PEP carboxylase/synthase, acetyl-CoA synthetases, thiolases, quinoprotein/alcohol dehydrogenases, etc.) are legitimate pyruvate/central-carbon enzymes but have **no role in MG detoxification** and should not be scored against this module.

### 4.5 Alternative-route detox genes MISSING from the candidate metadata

These are real KT2440 proteome members not present in the delivered ppu00620 candidate list, and they should be added as separate MG-related candidates:

| Gene / locus | UniProt | Annotation | Proposed MG role | Confidence |
|---|---|---|---|---|
| `yeaE` / PP_3120 | Q88I81 | Methylglyoxal reductase (EC 1.1.1.-), AKR (PF00248) | Reductive, GSH-independent MG→acetol/lactaldehyde | Moderate (name + fold) |
| `dkgB` / PP_2368 | Q88KC2 | Aldo-keto reductase; hydroxyacetone + NADP⁺ = MG + NADPH | Reductive MG↔acetol | Moderate |
| PP_0893, PP_2491, PP_2992, PP_3431 | — | DJ-1/ThiJ/PfpI-superfamily | Candidate glyoxalase III (GSH-independent MG→D-lactate) | Low–moderate (homology only) |

The DJ-1/ThiJ flag is justified by demonstrated glutathione-independent glyoxalase activity in DJ-1-superfamily proteins in other organisms (e.g., *Candida albicans* GLX3) ([PMID: 24302734](https://pubmed.ncbi.nlm.nih.gov/24302734/)). Transfer to KT2440 is by homology only and is **uncertain** — the same fold also yields proteases (e.g., PfpI-type), a classic mis-annotation trap — so these are worth flagging so the module is not scored as a single point of failure on `gloA`.

---

## 5. Mechanistic Interpretation

The satisfiability logic of this module is best understood as a **core route plus optional parallel branches**:

- **Core (covered):** MG spontaneously forms a hemithioacetal with GSH; **GlxI (`gloA`/PP_3766)** isomerizes it and **GlxII (`gloB`/PP_4144)** hydrolyzes the product to D-lactate, recycling GSH. Because GSH is regenerated stoichiometrically and is itself synthesizable (`gshA`/`gshB`), the route is self-sustaining and requires no external cofactor input. Direct heterologous functional data for *P. putida* GlxI make this the best-evidenced branch.
- **Rate/tolerance logic:** GlxI is the committed, tolerance-governing step; GlxII is required to complete turnover and recycle GSH but is not, by itself, the determinant of MG resistance (the *E. coli* ΔgloB phenotype). Curators should therefore weight `gloA` presence more heavily than `gloB` when scoring "detox capability," while still requiring both for a complete pathway.
- **Parallel branches (candidate_uncertain):** KT2440 additionally carries reductive (AKR: `yeaE`, `dkgB`) and potentially GSH-independent (DJ-1/ThiJ glyoxalase III) routes. These provide functional redundancy — biologically plausible for a soil bacterium that experiences oxidative and carbonyl stress — but are not needed to declare the module satisfiable, and their activity in KT2440 is unproven.
- **Boundary correction:** The absence of an MG synthase means the module in KT2440 is purely *defensive* (detoxifying incidentally-formed MG), not a deliberate glycolytic-bypass sink as in some enterobacteria. This reframes the upstream step from "gap" to "not expected."

---

## 6. Evidence Base

| PMID | Finding it supports | Organism / transfer strength |
|------|---------------------|------------------------------|
| [11461144](https://pubmed.ncbi.nlm.nih.gov/11461144/) | *P. putida* glyoxalase I detoxifies MG (35–43% intracellular MG reduction) when expressed in *E. coli* — direct functional support for `gloA`/PP_3766 | *P. putida* gene, heterologous host — **strong** transfer to KT2440 |
| [22358913](https://pubmed.ncbi.nlm.nih.gov/22358913/) | *P. putida* GlxI expressed in CHO cells lowers free MG 80–90% — corroborates gloA function | *P. putida* gene — **strong** |
| [28939611](https://pubmed.ncbi.nlm.nih.gov/28939611/) | Defines the GloA/GloB GSH-dependent MG→D-lactate two-enzyme system | Generic bacterial framework — **strong** conceptual |
| [21143325](https://pubmed.ncbi.nlm.nih.gov/21143325/) | ΔgloB is as MG-tolerant as parent; S-lactoylglutathione formation is critical — GlxII non-essentiality caveat | *E. coli* — **moderate** (mechanism likely conserved) |
| [24302734](https://pubmed.ncbi.nlm.nih.gov/24302734/) | DJ-1 superfamily member has GSH-independent glyoxalase (glyoxalase III) activity — justifies flagging KT2440 DJ-1/ThiJ paralogs | *C. albicans* — **weak/uncertain** transfer |
| [10824093](https://pubmed.ncbi.nlm.nih.gov/10824093/) | Bacterial GlxI sequence identification; *P. putida* GlxI is distinctive among bacterial GlxI | Cross-genus — context only |
| [25557363](https://pubmed.ncbi.nlm.nih.gov/25557363/) | Structural determinants of GlxI Ni²⁺ vs Zn²⁺ metal selectivity | *P. aeruginosa* — genus-level context |

Verbatim supporting quotes recorded during the investigation: *"the transgenic cells with the P. putida glyoxalase I displayed a reduction of 35-43% in intracellular MG"* (PMID 11461144); *"Glyoxalase I and II (GloA and GloB) sequentially convert MG into d-lactic acid using glutathione (GSH) as a cofactor"* (PMID 28939611); *"a ΔgloB mutant is as tolerant of MG as the parent, despite having the same degree of inhibition of MG detoxification as a ΔgloA strain"* (PMID 21143325); *"the DJ-1 superfamily member ORF 19.251/GLX3 from Candida albicans is shown to possess glyoxalase activity"* (PMID 24302734).

---

## 7. Gaps, Ambiguities, and Likely Over-Annotations

- **Gap / boundary correction — MG synthase.** UniProt searches over UP000000556 for protein name "methylglyoxal synthase," gene `mgsA`, and EC 4.2.3.3 all returned zero hits; a broader search across all *P. putida* (taxonomy 303) for EC 4.2.3.3 was also empty. Free-text "methylglyoxal" in the KT2440 proteome returns only detox/reductase enzymes (`gloA`, `gloB`, `yeaE` PP_3120, `dkgB` PP_2368), never a synthase. Mark the synthesis step **not_expected_in_target_taxon** and document that MG arises non-enzymatically (triose-phosphate decomposition) and from aminoacetone/threonine and lipid-peroxidation routes. This is a negative database result and should be confirmed by manual synteny/HMM search.
- **Bucket/module mismatch (module_needs_revision at the bucket level).** The ppu00620 "pyruvate metabolism" bucket is an overview map, not an MG module. It (a) sweeps in ~48 unrelated central-carbon enzymes, (b) includes a non-glyoxalase (`ycgM`/PP_5153) apparently on the strength of a placeholder EC, and (c) omits the true alternative-route MG genes (PP_3120, PP_2368, DJ-1 paralogs). A dedicated **methylglyoxal-detoxification module document** would be far more curatable than scoring against ppu00620.
- **Over-propagation risk:** broad EC "1.1.1.-" and AKR annotations (`yeaE`, `dkgB`) may be over-mapped to MG; treat MG reductase activity as candidate, not established, for KT2440. `ycgM` EC 3.-.-.- is a meaningless placeholder driving mis-inclusion; correct family is fumarylacetoacetase.
- **Paralog ambiguity:** four DJ-1/ThiJ paralogs — cannot assign glyoxalase III to a specific locus by homology alone. PP_0772 vs `gloB` — two GlxII-family proteins; which carries the physiological S-lactoylglutathione hydrolase load in KT2440 is untested.
- **Evidence level:** all focal genes are UniProt existence level 3 (inferred from homology) *within KT2440*; the strongest experimental transfer is for `gloA` (the *P. putida* gene is functionally validated).

---

## 8. Module and GO-Curation Recommendations

| Module element | Recommended status | Rationale |
|---|---|---|
| GlxI step (EC 4.4.1.5) | **covered** — `gloA`/PP_3766 | Homology annotation + direct heterologous functional data for *P. putida* GlxI |
| GlxII step (EC 3.1.2.6) | **covered** — `gloB`/PP_4144 (paralog PP_0772) | Specific GlxII InterPro signatures; caveat: not tolerance-limiting |
| GSH cofactor supply | **covered** (cross-link) — `gshA`/PP_0243, `gshB`/PP_4993 | Both biosynthesis steps encoded |
| D-lactate disposal | **covered** (downstream) — `ldhA`/`dld2`/`lldD` | Multifunctional central-carbon LDHs |
| MG synthase (EC 4.2.3.3) | **not_expected_in_target_taxon** | Zero hits across KT2440 and all *P. putida* |
| Second GlxII paralog PP_0772 | **candidate_uncertain** | GlxII subfamily fold; substrate untested |
| Reductive route (`yeaE`, `dkgB`) | **candidate_uncertain** (separate branch) | AKR fold + MG reductase naming; not in bucket |
| Glyoxalase III (DJ-1 paralogs) | **candidate_uncertain** (separate branch) | Homology only; activity unproven in KT2440 |
| `ycgM`/PP_5153 | **exclude / module_needs_revision** | Fumarylacetoacetase family, not glyoxalase |
| ppu00620 bucket as MG module | **module_needs_revision** | Overview map; create dedicated MG-detox module |

**GO-curation notes.** Appropriate GO terms for the covered steps: GlxI → GO:0004462 (lactoylglutathione lyase activity) and GlxII → GO:0004416 (hydroxyacylglutathione hydrolase activity), both under GO:0051596 (methylglyoxal catabolic process) / GO:0019243 (methylglyoxal catabolic process to D-lactate via S-lactoylglutathione). A GO-term request is likely warranted only for the **glutathione-independent glyoxalase (glyoxalase III / DJ-1)** branch (activity ~GO:0019172) if those paralogs are experimentally validated. No new module document is strictly required to mark satisfiability, but a dedicated MG-detox module would materially improve curation over the ppu00620 overview bucket.

---

## 9. Genes to Promote to Full `fetch-gene` Review

1. **`gloA` / PP_3766 (Q88GF8)** — module-defining GlxI; attach direct experimental citations (PMID 11461144, 22358913), confirm metal class (Ni vs Zn), and verify locus identity to historically characterized *P. putida* GlxI. **Highest priority.**
2. **`gloB` / PP_4144 (Q88FF3)** — module-defining GlxII; record the "not tolerance-limiting" caveat (PMID 21143325).
3. **PP_0772 (Q88PS6)** — second GlxII-family candidate; resolve whether it is a redundant S-lactoylglutathione hydrolase, an ETHE1-type persulfide dioxygenase, or a tRNase Z.
4. **`yeaE` / PP_3120 (Q88I81)** and **`dkgB` / PP_2368 (Q88KC2)** — reductive GSH-independent MG detox; confirm MG as physiological substrate and product (acetol vs lactaldehyde).
5. **DJ-1/ThiJ paralogs PP_0893, PP_2491, PP_2992, PP_3431** — glyoxalase III candidates; low prior but high value if positive.
6. (Cross-link only) **`gshA` / PP_0243** and **`gshB` / PP_4993** — cofactor supply.

---

## 10. Limitations and Knowledge Gaps

- **Evidence type is mixed.** The GlxI/GlxII annotations in KT2440 are UniProt existence level 3 (homology-inferred). The strongest experimental support (PMID 11461144, 22358913) is for "the *P. putida* glyoxalase I gene" used as a heterologous tool; it is very likely the PP_3766 ortholog but the exact KT2440 locus identity should be confirmed during full review. No KT2440-specific knockout/phenotype study of `gloA`/`gloB` was located in this investigation.
- **Alternative routes are homology-only.** The reductive AKR route and the DJ-1 glyoxalase-III branch are inferred from fold/family and from cross-species precedent (*C. albicans*, PMID 24302734). Transfer to KT2440 is **uncertain** and untested biochemically.
- **Flux partitioning unknown.** How much MG is handled by the GSH-dependent vs GSH-independent routes under physiological/stress conditions in KT2440 has not been measured.
- **PP_0772 substrate scope unresolved** — metallo-β-lactamase-superfamily proteins are notoriously promiscuous, so InterPro placement in the GlxII subfamily is suggestive, not definitive.
- **Negative results are robust but bounded.** The absence of `mgsA`/EC 4.2.3.3 is well-supported across KT2440 and all *P. putida*, but "absent from UniProt-annotated proteome" cannot fully exclude an unannotated or divergent synthase; this is a low-probability caveat.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Confirm PP_3766 ↔ historical *P. putida* GlxI** by sequence alignment to the clones used in PMID 11461144 / 22358913; this converts homology-level annotation to direct functional evidence for the KT2440 locus.
2. **Targeted deletion / complementation of `gloA` (PP_3766) and `gloB` (PP_4144)** in KT2440, scoring MG sensitivity and D-lactate accumulation; test the *E. coli*-derived prediction that ΔgloB is MG-tolerant while ΔgloA is sensitive.
3. **Biochemical assay of PP_0772** against S-lactoylglutathione to determine whether it is a redundant GlxII.
4. **Substrate assays for PP_3120 (`yeaE`) and PP_2368 (`dkgB`)** with MG ± NADPH to validate the reductive branch and its product.
5. **Express and assay the four DJ-1/ThiJ paralogs** for glutathione-independent MG→D-lactate (glyoxalase III) activity.
6. **Curatorial action:** create a dedicated MG-detox module (GlxI + GlxII, GSH-supply cross-link, optional GSH-independent branches); remove `ycgM`/PP_5153; add PP_3120, PP_2368, and DJ-1 paralogs as candidate genes; mark the MG-synthase step not_expected_in_target_taxon.

---

## 12. Key References

- *Accumulation of methylglyoxal in anaerobically grown Escherichia coli and its detoxification by expression of the Pseudomonas putida glyoxalase I gene.* [PMID: 11461144](https://pubmed.ncbi.nlm.nih.gov/11461144/) — direct functional support for PP_3766 (gloA).
- *Effect of endogenous methylglyoxal on Chinese hamster ovary cells grown in culture.* [PMID: 22358913](https://pubmed.ncbi.nlm.nih.gov/22358913/) — *P. putida* GlxI lowers free MG 80–90% in CHO cells.
- *Concomitant Loss of the Glyoxalase System and Glycolysis Makes "Candidatus Liberibacter asiaticus" an Energy Scavenger.* [PMID: 28939611](https://pubmed.ncbi.nlm.nih.gov/28939611/) — defines the GloA/GloB GSH-dependent system.
- *The critical role of S-lactoylglutathione formation during methylglyoxal detoxification in Escherichia coli.* [PMID: 21143325](https://pubmed.ncbi.nlm.nih.gov/21143325/) — GlxII non-essentiality caveat.
- *A glutathione-independent glyoxalase of the DJ-1 superfamily plays an important role in managing metabolically generated methylglyoxal in Candida albicans.* [PMID: 24302734](https://pubmed.ncbi.nlm.nih.gov/24302734/) — glyoxalase III precedent for DJ-1/ThiJ paralogs.
- *Identification of sequences encoding the detoxification metalloisomerase glyoxalase I in microbial genomes.* [PMID: 10824093](https://pubmed.ncbi.nlm.nih.gov/10824093/) — *P. putida* GlxI is distinctive among bacterial GlxI.
- *Modulating glyoxalase I metal selectivity by deletional mutagenesis.* [PMID: 25557363](https://pubmed.ncbi.nlm.nih.gov/25557363/) — Ni²⁺/Zn²⁺ GlxI activation classes (genus-level context).
- UniProt proteome UP000000556: gloA Q88GF8, gloB Q88FF3, PP_0772 Q88PS6, yeaE Q88I81, dkgB Q88KC2, gshA Q88R90, gshB Q88D35, DJ-1/ThiJ PP_0893/PP_2491/PP_2992/PP_3431; no EC 4.2.3.3 / `mgsA` hit.

**Uncertainty statement.** `gloA` carries direct *P. putida* functional evidence (strong transfer to KT2440). `gloB`, `yeaE`, `dkgB`, PP_0772 and the DJ-1 candidates are homology-based within KT2440; glyoxalase III and reductive-route assignments are inferred from related organisms and remain to be verified experimentally in KT2440. The absence of `mgsA` is a negative database result and should be confirmed by manual synteny/HMM search.


## Artifacts

- [OpenScientist final report](PSEPK__methylglyoxal-detoxification__ppu00620-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__methylglyoxal-detoxification__ppu00620-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11461144
2. PMID:22358913
3. PMID:10824093
4. PMID:25557363
5. PMID:21143325
6. PMID:24302734
7. PMID:28939611