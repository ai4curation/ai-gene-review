---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:47:17.807726'
end_time: '2026-09-01T03:01:32.664117'
duration_seconds: 854.86
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial Mla intermembrane phospholipid transport
  module_summary: A species-neutral diderm-bacterial module for phospholipid exchange
    across the cell envelope through an outer-membrane MlaA/VacJ interface, a soluble
    periplasmic MlaC carrier, and an ATP-coupled inner-membrane MlaFEDB complex. The
    module represents the conserved transport architecture without forcing a universal
    retrograde or anterograde net direction.
  module_outline: "- Bacterial Mla intermembrane phospholipid transport\n  - 1. Outer-membrane\
    \ phospholipid handling\n  - MlaA/VacJ outer-membrane interface\n    - MlaA/VacJ\
    \ outer-membrane phospholipid interface (molecular player: MlaA/VacJ family; activity\
    \ or role: outer-membrane phospholipid handling activity)\n  - 2. Periplasmic\
    \ phospholipid shuttling\n  - MlaC periplasmic phospholipid shuttle\n    - MlaC-family\
    \ periplasmic phospholipid carrier (molecular player: MlaC phospholipid-carrier\
    \ family; activity or role: phospholipid binding)\n  - 3. ATP-coupled inner-membrane\
    \ phospholipid handling\n  - MlaFEDB inner-membrane complex\n    - MlaFEDB phospholipid\
    \ transport complex (molecular player: MlaFEDB ABC phospholipid transport complex;\
    \ activity or role: phospholipid transfer activity)"
  module_connections: No explicit connections.
  pathway_query: ppu02010
  pathway_id: ppu02010
  pathway_name: ABC transporters
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu02010 with 151 primary genes; module
    area: transport_motility_signaling.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '207'
  candidate_genes: '- PP_0076: PP_0076 | Q88RQ3 | Choline betaine-binding protein
    (primary bucket kegg:ppu02010)

    - metQ: PP_0112 | Q88RL7 | Methionine ABC transporter, periplasmic binding protein
    (primary bucket kegg:ppu02010)

    - metI: PP_0113 | Q88RL6 | Methionine ABC transporter, permease protein (primary
    bucket kegg:ppu02010)

    - metN1: PP_0114 | Q88RL5 | Methionine import ATP-binding protein MetN 1 (EC 7.4.2.11)
    (EC 7.4.2.11; primary bucket kegg:ppu02010)

    - znuB: PP_0117 | Q88RL2 | High-affinity zinc uptake system membrane protein ZnuB
    (primary bucket kegg:ppu02010)

    - znuC: PP_0118 | Q88RL1 | Zinc import ATP-binding protein ZnuC (EC 7.2.2.20)
    (EC 7.2.2.20; primary bucket kegg:ppu02010)

    - PP_0120: PP_0120 | Q88RK9 | High-affinity zinc uptake system protein ZnuA (primary
    bucket kegg:ppu02010)

    - PP_0140: PP_0140 | Q88RI9 | Mce/MlaD domain-containing protein (primary bucket
    kegg:ppu02010)

    - PP_0141: PP_0141 | Q88RI8 | ABC transporter, ATP-binding protein (primary bucket
    kegg:ppu02010)

    - PP_0142: PP_0142 | Q88RI7 | ABC transporter, permease protein (primary bucket
    kegg:ppu02010)

    - paxB: PP_0167 | Q88RG3 | Toxin secretion ATP-binding protein (primary bucket
    kegg:ppu02010)

    - PP_0170: PP_0170 | Q88RG0 | ABC transporter, periplasmic binding protein (primary
    bucket kegg:ppu00920)

    - PP_0171: PP_0171 | Q88RF9 | ABC transporter, ATP-binding protein (primary bucket
    kegg:ppu00920)

    - PP_0172: PP_0172 | Q88RF8 | ABC transporter, permease protein (primary bucket
    kegg:ppu00920)

    - PP_0207: PP_0207 | Q88RC5 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - PP_0208: PP_0208 | Q88RC4 | Nitrate ABC transporter, permease protein (primary
    bucket kegg:ppu00920)

    - tauB-I: PP_0209 | Q88RC3 | ATP-binding taurine transporter subunit (EC 3.6.3.36)
    (EC 3.6.3.36; primary bucket kegg:ppu00920)

    - metP: PP_0219 | Q88RB4 | L,D-methionine D-methionine ABC transporter-permease
    subunit (primary bucket kegg:ppu02010)

    - metN2: PP_0220 | Q88RB3 | Methionine import ATP-binding protein MetN 2 (EC 7.4.2.11)
    (EC 7.4.2.11; primary bucket kegg:ppu02010)

    - PP_0221: PP_0221 | Q88RB2 | Methionine ABC transporter periplasmic-binding lipoprotein
    (MetQ-like protein) (primary bucket kegg:ppu02010)

    - sctC: PP_0225 | Q88RA8 | Sulfur compound ABC transporter-ATP-binding subunit
    (primary bucket kegg:ppu02010)

    - sctS: PP_0226 | Q88RA7 | Sulfur compound ABC transporter-permease subunit (primary
    bucket kegg:ppu02010)

    - fliY: PP_0227 | Q88RA6 | Periplasmic cystine-binding protein (primary bucket
    kegg:ppu02040)

    - tauC: PP_0231 | Q88RA2 | Taurine ABC transporter permease subunit (EC 3.6.3.36)
    (EC 3.6.3.36; primary bucket kegg:ppu00920)

    - tauB: PP_0232 | Q88RA1 | Taurine import ATP-binding protein TauB (EC 7.6.2.7)
    (EC 7.6.2.7; primary bucket kegg:ppu00920)

    - tauA: PP_0233 | Q88RA0 | Taurine ABC transporter periplasmic binding subunit
    (primary bucket kegg:ppu00920)

    - ssuA: PP_0237 | Q88R96 | Putative aliphatic sulfonates-binding protein (primary
    bucket kegg:ppu00920)

    - ssuC: PP_0239 | Q88R94 | Aliphatic sulfonate ABC transporter-permease subunit
    / transport of isethionate (primary bucket kegg:ppu00920)

    - ssuB: PP_0240 | Q88R93 | Aliphatic sulfonates import ATP-binding protein SsuB
    (EC 7.6.2.14) (EC 7.6.2.14; primary bucket kegg:ppu00920)

    - PP_0280: PP_0280 | Q88R54 | Arginine ABC transporter permease protein ArtM (primary
    bucket kegg:ppu02010)

    - PP_0281: PP_0281 | Q88R53 | Amino acid ABC transporter, permease protein (primary
    bucket kegg:ppu02010)

    - artJ: PP_0282 | Q88R52 | L-arginine ABC transporter-periplasmic binding subunit
    (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)

    - aotP: PP_0283 | Q88R51 | Arginine/ornithine transport ATP-binding protein AotP
    (primary bucket kegg:ppu02010)

    - cbcV: PP_0294 | Q88R40 | Choline / betaine / carnitine ABC transporter-ATP binding
    subunit (EC 3.6.3.32) (EC 3.6.3.32; primary bucket kegg:ppu02010)

    - cbcW: PP_0295 | Q88R39 | Choline / betaine / carnitine ABC transporter-membrane
    subunit (EC 3.6.3.32) (EC 3.6.3.32; primary bucket kegg:ppu02010)

    - cbcX: PP_0296 | Q88R38 | Choline / betaine / carnitine ABC transporter-substrate
    binding protein (EC 3.6.3.32) (EC 3.6.3.32; primary bucket kegg:ppu02010)

    - caiX: PP_0304 | Q88R30 | Carnitine uptake ABC transporter, periplasmic component
    (primary bucket kegg:ppu02010)

    - PP_0524: PP_0524 | Q88QG9 | Periplasmic cobalamin-binding protein HutB (primary
    bucket kegg:ppu02010)

    - PP_0615: PP_0615 | Q88Q80 | Branched-chain amino acid ABC transporter, ATP-binding
    protein (primary bucket kegg:ppu02024)

    - PP_0616: PP_0616 | Q88Q79 | Branched-chain amino acid ABC transporter, ATP binding
    protein (primary bucket kegg:ppu02024)

    - PP_0617: PP_0617 | Q88Q78 | Branched-chain amino acid ABC transporter, permease
    protein (primary bucket kegg:ppu02024)

    - PP_0618: PP_0618 | Q88Q77 | Branched-chain amino acid ABC transporter, permease
    protein (primary bucket kegg:ppu02024)

    - PP_0619: PP_0619 | Q88Q76 | Branched-chain amino acid ABC transporter, periplasmic
    amino acid-binding protein (primary bucket kegg:ppu02024)

    - PP_0804: PP_0804 | Q88PP4 | Protein secretion ABC efflux system, permease and
    ATP-binding protein (primary bucket kegg:ppu02010)

    - ptxB: PP_0824 | Q88PM6 | Phosphonate transport system-binding protein (primary
    bucket kegg:ppu02010)

    - phnC: PP_0825 | Q88PM5 | Phosphonates import ATP-binding protein PhnC (EC 7.3.2.2)
    (EC 7.3.2.2; primary bucket kegg:ppu02010)

    - phnE: PP_0826 | Q88PM4 | Phosphonate ABC transporter, permease protein (primary
    bucket kegg:ppu02010)

    - ptxC: PP_0827 | Q88PM3 | Phosphonate transport system permease protein PtxC
    (primary bucket kegg:ppu02010)

    - yehX: PP_0868 | Q88PI2 | Quaternary amine transport ATP-binding protein (EC
    7.6.2.9) (EC 7.6.2.9; primary bucket kegg:ppu02010)

    - yehW: PP_0869 | Q88PI1 | Osmoprotectant ABC transporter permease subunit (primary
    bucket kegg:ppu02010)

    - PP_0870: PP_0870 | Q88PI0 | Glycine betaine/carnitine/choline ABC transporter,
    periplasmic binding protein (primary bucket kegg:ppu02010)

    - PP_0871: PP_0871 | Q88PH9 | Glycine betaine/carnitine/choline ABC transporter,
    permease protein (primary bucket kegg:ppu02010)

    - potF-I: PP_0873 | Q88PH7 | Putrescine-binding periplasmic protein (primary bucket
    kegg:ppu02010)

    - dppF: PP_0878 | Q88PH2 | ABC-type dipeptide transporter (EC 7.4.2.9) (EC 7.4.2.9;
    primary bucket kegg:ppu02010)

    - dppD: PP_0879 | Q88PH1 | ABC-type dipeptide transporter (EC 7.4.2.9) (EC 7.4.2.9;
    primary bucket kegg:ppu02010)

    - dppC: PP_0880 | Q88PH0 | Dipeptide ABC transporter-putative membrane subunit
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02010)

    - dppB: PP_0881 | Q88PG9 | Dipeptide ABC transporter-putative membrane subunit
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02010)

    - dppA-I: PP_0882 | Q88PG8 | Dipeptide ABC transporter-periplasmic binding protein
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)

    - dppA-II: PP_0884 | Q88PG6 | Dipeptide ABC transporter-periplasmic binding protein
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)

    - dppA-III: PP_0885 | Q88PG5 | Dipeptide ABC transporter-periplasmic binding protein
    (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)

    - lptB: PP_0953 | Q88P99 | Lipopolysaccharide export system ATP-binding protein
    LptB (primary bucket kegg:ppu02010)

    - mlaF: PP_0958 | Q88P94 | Intermembrane phospholipid transport system ATP-binding
    protein MlaF (primary bucket kegg:ppu02010)

    - mlaE: PP_0959 | Q88P93 | Intermembrane phospholipid transport system permease
    protein MlaE (primary bucket kegg:ppu02010)

    - mlaD: PP_0960 | Q88P92 | Phospholipid ABC transporter binding protein (primary
    bucket kegg:ppu02010)

    - ttg2D: PP_0961 | Q88P91 | Toluene tolerance protein (primary bucket kegg:ppu02010)

    - ttg2E: PP_0962 | Q88P90 | Toluene-tolerance protein (primary bucket kegg:ppu02010)

    - PP_0982: PP_0982 | Q88P71 | Lipopolysaccharide export system permease protein
    LptF (primary bucket kegg:ppu02010)

    - PP_0983: PP_0983 | Q88P70 | LPS export ABC transporter permease LptG (primary
    bucket kegg:ppu02010)

    - gtsA: PP_1015 | Q88P38 | Mannose/glucose ABC transporter, glucose-binding periplasmic
    protein (primary bucket kegg:ppu02010)

    - gtsB: PP_1016 | Q88P37 | Mannose/glucose ABC transporter, permease protein (primary
    bucket kegg:ppu02010)

    - gtsC: PP_1017 | Q88P36 | Mannose/glucose ABC transporter, permease protein (primary
    bucket kegg:ppu02010)

    - gtsD: PP_1018 | Q88P35 | Maltose import ATP-binding protein YcjV (EC 7.5.2.1)
    (EC 7.5.2.1; primary bucket kegg:ppu02010)

    - gltL: PP_1068 | Q88NY5 | Glutamate / aspartate ABC transporter-ATP binding subunit
    (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)

    - gltK: PP_1069 | Q88NY4 | Glutamate/aspartate import permease protein GltK (primary
    bucket kegg:ppu02010)

    - gltJ: PP_1070 | Q88NY3 | Glutamate / aspartate ABC transporter-permease subunit
    (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)

    - gltI: PP_1071 | Q88NY2 | Glutamate / aspartate ABC transporter-periplasmic binding
    protein (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)

    - PP_1078: PP_1078 | Q88NX5 | ABC transporter, ATP-binding protein (primary bucket
    kegg:ppu02010)

    - livF-I: PP_1137 | Q88NR8 | High-affinity branched-chain amino acid transport
    ATP-binding protein (primary bucket kegg:ppu02024)

    - livG: PP_1138 | Q88NR7 | Branched chain amino acid transporter-ATP binding subunit
    (primary bucket kegg:ppu02024)

    - livM: PP_1139 | Q88NR6 | Branched chain amino acid transporter-permease subunit
    (primary bucket kegg:ppu02024)

    - ... 127 additional candidate genes omitted from prompt.'
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
  path: PSEPK__bacterial_mla_intermembrane_phospholipid_transport__ppu02010-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_mla_intermembrane_phospholipid_transport__ppu02010-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial Mla intermembrane phospholipid transport in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu02010
- Resolved ID: ppu02010
- Resolved name: ABC transporters
- Source: KEGG

Resolved local bucket kegg:ppu02010 with 151 primary genes; module area: transport_motility_signaling.

## Candidate Genes From Local Metadata

Candidate gene count: 207

- PP_0076: PP_0076 | Q88RQ3 | Choline betaine-binding protein (primary bucket kegg:ppu02010)
- metQ: PP_0112 | Q88RL7 | Methionine ABC transporter, periplasmic binding protein (primary bucket kegg:ppu02010)
- metI: PP_0113 | Q88RL6 | Methionine ABC transporter, permease protein (primary bucket kegg:ppu02010)
- metN1: PP_0114 | Q88RL5 | Methionine import ATP-binding protein MetN 1 (EC 7.4.2.11) (EC 7.4.2.11; primary bucket kegg:ppu02010)
- znuB: PP_0117 | Q88RL2 | High-affinity zinc uptake system membrane protein ZnuB (primary bucket kegg:ppu02010)
- znuC: PP_0118 | Q88RL1 | Zinc import ATP-binding protein ZnuC (EC 7.2.2.20) (EC 7.2.2.20; primary bucket kegg:ppu02010)
- PP_0120: PP_0120 | Q88RK9 | High-affinity zinc uptake system protein ZnuA (primary bucket kegg:ppu02010)
- PP_0140: PP_0140 | Q88RI9 | Mce/MlaD domain-containing protein (primary bucket kegg:ppu02010)
- PP_0141: PP_0141 | Q88RI8 | ABC transporter, ATP-binding protein (primary bucket kegg:ppu02010)
- PP_0142: PP_0142 | Q88RI7 | ABC transporter, permease protein (primary bucket kegg:ppu02010)
- paxB: PP_0167 | Q88RG3 | Toxin secretion ATP-binding protein (primary bucket kegg:ppu02010)
- PP_0170: PP_0170 | Q88RG0 | ABC transporter, periplasmic binding protein (primary bucket kegg:ppu00920)
- PP_0171: PP_0171 | Q88RF9 | ABC transporter, ATP-binding protein (primary bucket kegg:ppu00920)
- PP_0172: PP_0172 | Q88RF8 | ABC transporter, permease protein (primary bucket kegg:ppu00920)
- PP_0207: PP_0207 | Q88RC5 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- PP_0208: PP_0208 | Q88RC4 | Nitrate ABC transporter, permease protein (primary bucket kegg:ppu00920)
- tauB-I: PP_0209 | Q88RC3 | ATP-binding taurine transporter subunit (EC 3.6.3.36) (EC 3.6.3.36; primary bucket kegg:ppu00920)
- metP: PP_0219 | Q88RB4 | L,D-methionine D-methionine ABC transporter-permease subunit (primary bucket kegg:ppu02010)
- metN2: PP_0220 | Q88RB3 | Methionine import ATP-binding protein MetN 2 (EC 7.4.2.11) (EC 7.4.2.11; primary bucket kegg:ppu02010)
- PP_0221: PP_0221 | Q88RB2 | Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein) (primary bucket kegg:ppu02010)
- sctC: PP_0225 | Q88RA8 | Sulfur compound ABC transporter-ATP-binding subunit (primary bucket kegg:ppu02010)
- sctS: PP_0226 | Q88RA7 | Sulfur compound ABC transporter-permease subunit (primary bucket kegg:ppu02010)
- fliY: PP_0227 | Q88RA6 | Periplasmic cystine-binding protein (primary bucket kegg:ppu02040)
- tauC: PP_0231 | Q88RA2 | Taurine ABC transporter permease subunit (EC 3.6.3.36) (EC 3.6.3.36; primary bucket kegg:ppu00920)
- tauB: PP_0232 | Q88RA1 | Taurine import ATP-binding protein TauB (EC 7.6.2.7) (EC 7.6.2.7; primary bucket kegg:ppu00920)
- tauA: PP_0233 | Q88RA0 | Taurine ABC transporter periplasmic binding subunit (primary bucket kegg:ppu00920)
- ssuA: PP_0237 | Q88R96 | Putative aliphatic sulfonates-binding protein (primary bucket kegg:ppu00920)
- ssuC: PP_0239 | Q88R94 | Aliphatic sulfonate ABC transporter-permease subunit / transport of isethionate (primary bucket kegg:ppu00920)
- ssuB: PP_0240 | Q88R93 | Aliphatic sulfonates import ATP-binding protein SsuB (EC 7.6.2.14) (EC 7.6.2.14; primary bucket kegg:ppu00920)
- PP_0280: PP_0280 | Q88R54 | Arginine ABC transporter permease protein ArtM (primary bucket kegg:ppu02010)
- PP_0281: PP_0281 | Q88R53 | Amino acid ABC transporter, permease protein (primary bucket kegg:ppu02010)
- artJ: PP_0282 | Q88R52 | L-arginine ABC transporter-periplasmic binding subunit (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)
- aotP: PP_0283 | Q88R51 | Arginine/ornithine transport ATP-binding protein AotP (primary bucket kegg:ppu02010)
- cbcV: PP_0294 | Q88R40 | Choline / betaine / carnitine ABC transporter-ATP binding subunit (EC 3.6.3.32) (EC 3.6.3.32; primary bucket kegg:ppu02010)
- cbcW: PP_0295 | Q88R39 | Choline / betaine / carnitine ABC transporter-membrane subunit (EC 3.6.3.32) (EC 3.6.3.32; primary bucket kegg:ppu02010)
- cbcX: PP_0296 | Q88R38 | Choline / betaine / carnitine ABC transporter-substrate binding protein (EC 3.6.3.32) (EC 3.6.3.32; primary bucket kegg:ppu02010)
- caiX: PP_0304 | Q88R30 | Carnitine uptake ABC transporter, periplasmic component (primary bucket kegg:ppu02010)
- PP_0524: PP_0524 | Q88QG9 | Periplasmic cobalamin-binding protein HutB (primary bucket kegg:ppu02010)
- PP_0615: PP_0615 | Q88Q80 | Branched-chain amino acid ABC transporter, ATP-binding protein (primary bucket kegg:ppu02024)
- PP_0616: PP_0616 | Q88Q79 | Branched-chain amino acid ABC transporter, ATP binding protein (primary bucket kegg:ppu02024)
- PP_0617: PP_0617 | Q88Q78 | Branched-chain amino acid ABC transporter, permease protein (primary bucket kegg:ppu02024)
- PP_0618: PP_0618 | Q88Q77 | Branched-chain amino acid ABC transporter, permease protein (primary bucket kegg:ppu02024)
- PP_0619: PP_0619 | Q88Q76 | Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein (primary bucket kegg:ppu02024)
- PP_0804: PP_0804 | Q88PP4 | Protein secretion ABC efflux system, permease and ATP-binding protein (primary bucket kegg:ppu02010)
- ptxB: PP_0824 | Q88PM6 | Phosphonate transport system-binding protein (primary bucket kegg:ppu02010)
- phnC: PP_0825 | Q88PM5 | Phosphonates import ATP-binding protein PhnC (EC 7.3.2.2) (EC 7.3.2.2; primary bucket kegg:ppu02010)
- phnE: PP_0826 | Q88PM4 | Phosphonate ABC transporter, permease protein (primary bucket kegg:ppu02010)
- ptxC: PP_0827 | Q88PM3 | Phosphonate transport system permease protein PtxC (primary bucket kegg:ppu02010)
- yehX: PP_0868 | Q88PI2 | Quaternary amine transport ATP-binding protein (EC 7.6.2.9) (EC 7.6.2.9; primary bucket kegg:ppu02010)
- yehW: PP_0869 | Q88PI1 | Osmoprotectant ABC transporter permease subunit (primary bucket kegg:ppu02010)
- PP_0870: PP_0870 | Q88PI0 | Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein (primary bucket kegg:ppu02010)
- PP_0871: PP_0871 | Q88PH9 | Glycine betaine/carnitine/choline ABC transporter, permease protein (primary bucket kegg:ppu02010)
- potF-I: PP_0873 | Q88PH7 | Putrescine-binding periplasmic protein (primary bucket kegg:ppu02010)
- dppF: PP_0878 | Q88PH2 | ABC-type dipeptide transporter (EC 7.4.2.9) (EC 7.4.2.9; primary bucket kegg:ppu02010)
- dppD: PP_0879 | Q88PH1 | ABC-type dipeptide transporter (EC 7.4.2.9) (EC 7.4.2.9; primary bucket kegg:ppu02010)
- dppC: PP_0880 | Q88PH0 | Dipeptide ABC transporter-putative membrane subunit (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02010)
- dppB: PP_0881 | Q88PG9 | Dipeptide ABC transporter-putative membrane subunit (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02010)
- dppA-I: PP_0882 | Q88PG8 | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)
- dppA-II: PP_0884 | Q88PG6 | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)
- dppA-III: PP_0885 | Q88PG5 | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) (EC 3.6.3.23; primary bucket kegg:ppu02030)
- lptB: PP_0953 | Q88P99 | Lipopolysaccharide export system ATP-binding protein LptB (primary bucket kegg:ppu02010)
- mlaF: PP_0958 | Q88P94 | Intermembrane phospholipid transport system ATP-binding protein MlaF (primary bucket kegg:ppu02010)
- mlaE: PP_0959 | Q88P93 | Intermembrane phospholipid transport system permease protein MlaE (primary bucket kegg:ppu02010)
- mlaD: PP_0960 | Q88P92 | Phospholipid ABC transporter binding protein (primary bucket kegg:ppu02010)
- ttg2D: PP_0961 | Q88P91 | Toluene tolerance protein (primary bucket kegg:ppu02010)
- ttg2E: PP_0962 | Q88P90 | Toluene-tolerance protein (primary bucket kegg:ppu02010)
- PP_0982: PP_0982 | Q88P71 | Lipopolysaccharide export system permease protein LptF (primary bucket kegg:ppu02010)
- PP_0983: PP_0983 | Q88P70 | LPS export ABC transporter permease LptG (primary bucket kegg:ppu02010)
- gtsA: PP_1015 | Q88P38 | Mannose/glucose ABC transporter, glucose-binding periplasmic protein (primary bucket kegg:ppu02010)
- gtsB: PP_1016 | Q88P37 | Mannose/glucose ABC transporter, permease protein (primary bucket kegg:ppu02010)
- gtsC: PP_1017 | Q88P36 | Mannose/glucose ABC transporter, permease protein (primary bucket kegg:ppu02010)
- gtsD: PP_1018 | Q88P35 | Maltose import ATP-binding protein YcjV (EC 7.5.2.1) (EC 7.5.2.1; primary bucket kegg:ppu02010)
- gltL: PP_1068 | Q88NY5 | Glutamate / aspartate ABC transporter-ATP binding subunit (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)
- gltK: PP_1069 | Q88NY4 | Glutamate/aspartate import permease protein GltK (primary bucket kegg:ppu02010)
- gltJ: PP_1070 | Q88NY3 | Glutamate / aspartate ABC transporter-permease subunit (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)
- gltI: PP_1071 | Q88NY2 | Glutamate / aspartate ABC transporter-periplasmic binding protein (EC 3.6.3.21) (EC 3.6.3.21; primary bucket kegg:ppu02010)
- PP_1078: PP_1078 | Q88NX5 | ABC transporter, ATP-binding protein (primary bucket kegg:ppu02010)
- livF-I: PP_1137 | Q88NR8 | High-affinity branched-chain amino acid transport ATP-binding protein (primary bucket kegg:ppu02024)
- livG: PP_1138 | Q88NR7 | Branched chain amino acid transporter-ATP binding subunit (primary bucket kegg:ppu02024)
- livM: PP_1139 | Q88NR6 | Branched chain amino acid transporter-permease subunit (primary bucket kegg:ppu02024)
- ... 127 additional candidate genes omitted from prompt.

## Generic Module Context

### Working Scope

A species-neutral diderm-bacterial module for phospholipid exchange across the cell envelope through an outer-membrane MlaA/VacJ interface, a soluble periplasmic MlaC carrier, and an ATP-coupled inner-membrane MlaFEDB complex. The module represents the conserved transport architecture without forcing a universal retrograde or anterograde net direction.

### Provisional Biological Outline

- Bacterial Mla intermembrane phospholipid transport
  - 1. Outer-membrane phospholipid handling
  - MlaA/VacJ outer-membrane interface
    - MlaA/VacJ outer-membrane phospholipid interface (molecular player: MlaA/VacJ family; activity or role: outer-membrane phospholipid handling activity)
  - 2. Periplasmic phospholipid shuttling
  - MlaC periplasmic phospholipid shuttle
    - MlaC-family periplasmic phospholipid carrier (molecular player: MlaC phospholipid-carrier family; activity or role: phospholipid binding)
  - 3. ATP-coupled inner-membrane phospholipid handling
  - MlaFEDB inner-membrane complex
    - MlaFEDB phospholipid transport complex (molecular player: MlaFEDB ABC phospholipid transport complex; activity or role: phospholipid transfer activity)

### Known Relationships Among Steps

No explicit connections.

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

# Module Review: Bacterial Mla Intermembrane Phospholipid Transport in *Pseudomonas putida* KT2440

**Target:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Mla intermembrane phospholipid transport (OM MlaA/VacJ – periplasmic MlaC – IM MlaFEDB)
**Local bucket reviewed:** KEGG ppu02010 "ABC transporters" (151 primary genes; 207 candidates)

---

## 1. Executive summary

The Mla system is **fully present and satisfiable** in *P. putida* KT2440. All conserved
components map cleanly to the genome:

- **Inner-membrane MlaFEDB + periplasmic MlaC** are encoded by a single contiguous operon,
  **PP_0958–PP_0962** (`mlaF–mlaE–mlaD–mlaC–mlaB`), plus a Pseudomonas-specific BolA gene
  (PP_0963).
- **Outer-membrane MlaA/VacJ** is encoded by **PP_2163** (`vacJ`), an MlaA-family lipoprotein
  at an unlinked locus.

The two most curation-relevant problems are **hidden/mis-labeled subunits**, not gaps:

1. **MlaC = PP_0961** and **MlaB = PP_0962** are annotated only as generic *"toluene tolerance
   protein"* (`ttg2D`/`ttg2E`). Domain evidence (PF05494/IPR008869 for MlaC; PF13466 STAS for
   MlaB) **and KEGG Orthology (PP_0961→K07323 mlaC; PP_0962→K07122 mlaB, both single-copy)**
   firmly identify them. Without domain/KO-level review these steps would be **falsely scored as
   gaps**.
2. **MlaA/VacJ (PP_2163)** is a lipoprotein, not an ABC subunit, so it is **not in the
   ppu02010 candidate list**. Its absence from the ABC bucket is expected and must not be read
   as an OM gap.

A separate paralogous **Mce/MlaE-family ABC system (PP_0140–PP_0142)** is present in the
candidate list and should **not** be counted as core Mla (over-annotation risk on PP_0140's
generic "Mce/MlaD" label). Note that this Mce operon shares KEGG KOs **K02065/66/67 (mlaF/E/D)**
with the true Mla operon, so KO-based scoring cannot distinguish them — the module must be
anchored on the **Mla-specific KOs K07323 (mlaC) + K07122 (mlaB)** plus operon context.

**Module step verdicts at a glance:**

| Step | Verdict | Gene(s) | Evidence tier |
|------|---------|---------|---------------|
| 1. OM MlaA/VacJ | **covered** | PP_2163 (vacJ) | UniProt PF04333 + KO K04754; add to module (outside bucket) |
| 2. Periplasmic MlaC | **covered** | PP_0961 (ttg2D) | PF05494 + **single-copy KO K07323**; re-annotate |
| 3. IM MlaFEDB | **covered** | PP_0958/0959/0960 + MlaB PP_0962 | PF00005/02405/02470 + KOs; MlaB via **single-copy KO K07122** |
| OM porin partner | candidate_uncertain | unassigned | low priority; not required for satisfiability |
| Paralogs to exclude | keep separate | PP_0140–0142 (Mce), PP_0599/PP_2577 (PqiB), PP_1737 (2nd MlaA) | distinct systems / uncertain |

Evidence is a mix of **strong homology/domain assignment (curated UniProt + Pfam/InterPro,
direct for KT2440 proteins)** and **functional transfer from other Gram-negatives**
(*E. coli*, *P. aeruginosa*). Direct experimental phenotyping of the Mla/Ttg2 locus exists in
*P. putida* strains (solvent tolerance), giving indirect functional support.

---

## 2. Target-organism pathway definition

**Process included:** Protein-mediated exchange of glycerophospholipids (GPLs) across the
cell envelope of a diderm (Gram-negative) bacterium, via three coupled sub-assemblies:
(i) an OM MlaA/VacJ–porin interface that accesses GPLs at the OM inner/outer leaflet;
(ii) a soluble periplasmic MlaC carrier that ferries a single GPL across the periplasm;
(iii) an ATP-hydrolyzing IM ABC complex MlaFEDB. In *E. coli* the net direction is largely
**retrograde** (OM→IM), restoring OM lipid asymmetry, though anterograde roles have been
debated (PMID 36459067). The module is deliberately direction-neutral.

**Neighboring pathways to keep separate (do not merge):**
- **Lpt LPS export** (KT2440: `lptB` PP_0953, `lptF` PP_0982, `lptG` PP_0983, plus LptA/C/D/E)
  — transports LPS, not GPLs; shares the ABC bucket but is a distinct module.
- **Mce/Pqi-type intermembrane transporters** (KT2440: PP_0140–PP_0142) — architecturally
  related (MlaD/Mce and MlaE domains) but a separate system.
- Generic **ABC import systems** in ppu02010 (amino acid, sugar, phosphonate, metal uptake) —
  unrelated to lipid trafficking.
- Broad overview maps (KEGG "ABC transporters" ppu02010; "Transporters" BRITE) are collection
  buckets, not the Mla module.

**Alternate names / database definitions:**
- Mla = "Maintenance of Lipid Asymmetry."
- **Pseudomonas/lineage synonym: `ttg2`** ("toluene tolerance genes"). KT2440 uses `ttg2D`
  (=MlaC) and `ttg2E` (=MlaB); the DOT-T1E literature labels the operon `ttg2ABCDEF`.
- MlaA is also called **VacJ** (KT2440 uses `vacJ`).
- OM complex is "MlaA–OmpC/OmpF" in *E. coli*; the porin partner in *Pseudomonas* is not
  firmly established.

---

## 3. Expected step model

| # | Module step | Molecular player | Expected in KT2440? |
|---|-------------|------------------|---------------------|
| 1 | OM phospholipid handling | MlaA/VacJ (+porin) | Yes |
| 2 | Periplasmic shuttle | MlaC carrier | Yes |
| 3 | IM ATP-coupled complex | MlaFEDB (F=ATPase, E=permease, D=MCE, B=STAS regulator) | Yes |

MlaB (STAS domain) is a regulatory subunit of the IM complex; the canonical complement is
"six Mla proteins, MlaFEDBCA" (PMID 33199922).

---

## 4. Candidate genes and evidence

### Core Mla — high confidence (all direct KT2440 protein evidence via UniProt/Pfam)

| Gene | Locus | UniProt | Assigned role | Key domain evidence | Status |
|------|-------|---------|---------------|---------------------|--------|
| mlaF | PP_0958 | Q88P94 | IM ABC ATPase | PF00005; "ABC transporter superfamily, **MlaF family**" | Covered |
| mlaE | PP_0959 | Q88P93 | IM permease (5 TM) | PF02405; MlaE permease family; IM multipass | Covered |
| mlaD | PP_0960 | Q88P92 | MCE substrate-binding subunit | PF02470; **IPR030970 (MlaD-specific)** | Covered |
| **mlaC** | **PP_0961** | Q88P91 | **Periplasmic GPL carrier** | **PF05494 / IPR008869 (MlaC/Ttg2D)**; SignalP 1–22 → periplasm | Covered (re-annotate) |
| **mlaB** | **PP_0962** | Q88P90 | **STAS regulatory subunit** | **PF13466 (STAS)**; 100 aa | Covered (re-annotate) |
| vacJ/mlaA | PP_2163 | Q88KX6 | **OM lipoprotein** | PF04333 / IPR007428; **MlaA family**; lipoprotein signal 1–31 | Covered (not in bucket) |

Operon context: `kdsD`(PP_0957) – **mlaFEDCB** (PP_0958–0962) – **ttg2F/BolA** (PP_0963,
PF01722). Contiguous synteny mirrors the *E. coli* `mlaFEDCB` operon and confirms co-assignment.

**Independent KEGG-Orthology (KO) confirmation:** PP_0958→**K02065 (mlaF)**, PP_0959→**K02066
(mlaE)**, PP_0960→**K02067 (mlaD)**, PP_0961→**K07323 (mlaC)**, PP_0962→**K07122 (mlaB)**,
PP_2163→**K04754 (mlaA/vacJ)**. Crucially, KEGG assigns MlaC and MlaB to PP_0961/PP_0962 despite
their generic "toluene tolerance protein" free-text names, and the two Mla-specific KOs — **K07323
(mlaC) and K07122 (mlaB) — are single-copy in *ppu*** and sit inside the operon. This gives
high-confidence coverage of module step 2 (MlaC) and the MlaB regulatory subunit.

> **Curation caveat — shared KOs are NOT Mla-specific.** KEGG KOs K02065/K02066/K02067
> (mlaF/E/D) are also assigned to the paralogous Mce operon (PP_0141→K02065, PP_0142→K02066,
> PP_0140→K02067). KO-based module scoring therefore cannot, on its own, distinguish the true Mla
> operon from the Mce system and could double-count the F/E/D subunits. **Anchor the Mla module on
> the Mla-specific single-copy KOs K07323 (mlaC) + K07122 (mlaB) plus operon context** — not on
> the shared mlaF/E/D KOs. The PqiB proteins PP_0599/PP_2577 (K06192, pqiB/letB) are a further
> distinct system.

### Related but distinct — candidate_uncertain

| Gene | Locus | UniProt | Note |
|------|-------|---------|------|
| PP_0140 | PP_0140 | Q88RI9 | "Mce/MlaD domain" (PF02470, **generic IPR003399**, not MlaD-specific IPR030970). Part of a separate Mce/Pqi-like transporter. |
| PP_0141 | PP_0141 | Q88RI8 | ABC ATPase (PF00005) of that system. |
| PP_0142 | PP_0142 | Q88RI7 | Permease fusing **MlaE (PF02405) + STAS (PF13466)** domains — hallmark of Mce/Pqi-type, not core MlaE. |

### Not part of this module (present in the bucket, keep separate)
`lptB` (PP_0953), `lptF` (PP_0982), `lptG` (PP_0983) — LPS export; and all amino-acid/sugar/
metal/phosphonate ABC importers listed among the 207 candidates.

### Genome-wide paralog census (Pfam over proteome UP000000556)

Copy-number analysis both firms up the assignments and exposes the paralogs that must be
excluded from the core Mla module:

| Pfam | Family | # in proteome | Core Mla member | Other (non-Mla) members |
|------|--------|---------------|-----------------|--------------------------|
| PF05494 | MlaC/Ttg2D | **1** | **PP_0961 (MlaC)** | none — single-copy, unambiguous |
| PF02405 | MlaE permease | 2 | PP_0959 (MlaE) | PP_0142 (Mce-system permease, MlaE+STAS fusion) |
| PF02470 | MlaD/Mce | 4 | PP_0960 (MlaD) | PP_0140 (Mce), PP_0599 & PP_2577 (PqiB-like) |
| PF13466 | STAS | 4 | PP_0962 (MlaB, by operon context) | PP_4364, PP_2166 (anti-σ antagonists), PP_0142 |
| PF04333 | MlaA/VacJ | 2 | **PP_2163 (VacJ)** | **PP_1737 (paralog, uncertain)** |

Take-aways:
- **MlaC is single-copy → PP_0961 is a definitive assignment.**
- KT2440 encodes **three architecturally related but functionally distinct intermembrane
  systems**: Mla (PP_0958–0963), a **Mce/Pqi-type ABC system** (PP_0140–0142), and a **PqiAB/PqiB
  system** (PP_0599, PP_2577). These belong in separate modules.
- **A second MlaA/VacJ paralog, PP_1737** (248 aa, PF04333, mis-labeled "ABC transporter"), has
  **no detected lipoprotein signal** and lies next to a patatin/PNPLA phospholipase (PP_1736) and
  a lipid A acyltransferase (PP_1735) — a lipid-metabolism neighborhood distinct from the Mla
  operon. **PP_2163 (VacJ)**, which carries the canonical lipoprotein signal and the `vacJ`
  name, remains the primary OM Mla component; **PP_1737 should be `candidate_uncertain`**.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true gaps.** Every module step is encoded.
- **Hidden subunits (annotation gap, not sequence gap):** MlaC (PP_0961) and MlaB (PP_0962)
  carry only legacy `ttg2D`/`ttg2E` "toluene tolerance protein" names. This is the single
  biggest curation risk — automated step-scoring keyed on the string "Mla" would mark steps 2
  and the MlaB part of step 3 as missing.
- **Bucket-scope artifact:** MlaA/VacJ (PP_2163) is correctly outside ppu02010 (it is not an
  ABC protein). Module scoring must look beyond the KEGG ABC bucket for step 1.
- **Over-annotation risk:** PP_0140's "Mce/MlaD domain-containing" label should not be promoted
  to core MlaD. The MlaD-specific signature (IPR030970) is on PP_0960, not PP_0140.
- **Porin partner unresolved:** the MlaA-associated OM porin (OmpC/F equivalent) is not
  assigned in KT2440; low priority for module satisfiability but relevant for a complete OM
  sub-complex.
- **PP_0963 (ttg2F, BolA family):** a Pseudomonas operon extension of undefined Mla function —
  ambiguous, likely accessory/regulatory.

---

## 6. Module and GO-curation recommendations

**Step verdicts for the generic module:**

| Module step | Verdict | Genes |
|-------------|---------|-------|
| 1. OM MlaA/VacJ interface | **covered** | PP_2163 (add to module; outside candidate bucket) |
| 2. Periplasmic MlaC shuttle | **covered** | PP_0961 (re-annotate MlaC) |
| 3. IM MlaFEDB complex | **covered** | PP_0958 (F), PP_0959 (E), PP_0960 (D), PP_0962 (B) |

**Module document / boundary actions:**
- The generic module boundaries are **correct** for KT2440; no `module_needs_revision`.
  Recommend adding an explicit **`ttg2` synonym note** and mapping `ttg2D→MlaC`, `ttg2E→MlaB`
  so Pseudomonas loci are captured.
- Add PP_2163 (VacJ) as the step-1 gene despite its exclusion from the KEGG ABC bucket; note
  that MlaA/VacJ is a lipoprotein, not an ABC subunit.
- Mark **PP_0140–PP_0142 as `candidate_uncertain` / assign to a separate Mce–Pqi module**, not
  core Mla.
- **GO curation:** the KT2440 UniProt entries for PP_0960/0961/0962 would benefit from explicit
  GO annotations `GO:0120010 (intermembrane phospholipid transfer activity)` /
  `GO:0032365 (intracellular lipid transport)` / `GO:0015221` context and the process term for
  OM lipid-asymmetry maintenance; PP_0961 should also get `phospholipid binding`. No new GO
  *term* requests appear necessary — existing Mla-related terms suffice.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0961 (ttg2D → MlaC)** — highest priority: periplasmic carrier mis-labeled "toluene
   tolerance protein"; re-annotation directly satisfies module step 2.
2. **PP_0962 (ttg2E → MlaB)** — STAS regulatory subunit mis-labeled; completes the IM complex.
3. **PP_2163 (vacJ/MlaA)** — confirm lipoprotein processing and add to module as step 1.
4. **PP_0140** — resolve Mce/MlaD vs. core-MlaD ambiguity; assign to the correct (separate)
   Mce/Pqi system.
5. **PP_1737** — second MlaA/VacJ (PF04333) paralog; determine whether it is a functional MlaA
   or a distinct phospholipase-associated lipoprotein (currently `candidate_uncertain`).
6. **PP_0963 (ttg2F, BolA)** — determine whether it is a bona fide Mla accessory subunit.

---

## 8. Key references

- Tang et al. 2021, *Nat Commun* — MlaFEDB structure; "comprises six Mla proteins, MlaFEDBCA."
  **PMID 33199922**.
- Wotherspoon et al. 2024 — MlaC–MlaD complex; periplasmic shuttle definition.
  **PMID 39080293**.
- MacRae et al. 2023 — Mla protein–protein interactions / MlaC deep mutational scanning.
  **PMID 37100290**.
- Abellon-Ruiz 2023 — review of Mla transport directionality. **PMID 36459067**.
- Low & Chng 2021 — OmpC-Mla mechanism review. **PMID 34753108**.
- Ekiert et al. 2022 — MlaFEDB mechanism synthesis. **PMID 35981415**.
- Kaur et al. 2023 — *P. aeruginosa* MlaA/VacJ OM lipoprotein phenotypes. **PMID 37660742**.
- Kim et al. 1998 — *P. putida* GM73 `ttg` mutants; Ttg2 = ABC transporter, solvent tolerance.
  **PMID 9658016**.
- Dutta et al. 2026 — computational analysis of MlaA/MlaB/MlaE/MlaF distinctive features.
  **PMID 41047745**.

---

### Evidence-strength notes

- **Direct for KT2440 proteins:** all Pfam/InterPro domain and subcellular-location assignments
  (UniProt UP000000556). This is homology-based annotation of the *actual* target-strain
  sequences — strong for identity, but the transport *function* is inferred.
- **Functional transfer (strong):** Mla mechanism from *E. coli*/*P. aeruginosa* — high sequence
  and architectural conservation; transfer to KT2440 is well justified.
- **Direct-ish phenotype in species (indirect for module):** *P. putida* `ttg2` solvent-tolerance
  mutants (GM73/DOT-T1E lineage) link this locus to envelope stress but do not by themselves
  prove GPL transport in KT2440.
- **Open experiments:** GPL-transport assay / OM-asymmetry phenotype of a KT2440 `mlaC`
  (PP_0961) or `mlaFEDB` deletion; identification of the MlaA porin partner; role of the BolA
  gene PP_0963.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_mla_intermembrane_phospholipid_transport__ppu02010-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_mla_intermembrane_phospholipid_transport__ppu02010-deep-research-openscientist_artifacts/final_report.pdf)