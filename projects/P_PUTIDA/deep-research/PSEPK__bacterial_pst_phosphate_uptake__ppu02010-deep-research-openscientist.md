---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T03:54:59.779349'
end_time: '2026-08-11T04:16:44.371253'
duration_seconds: 1304.59
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial Pst high-affinity phosphate uptake
  module_summary: A reusable bacterial ABC-transport module in which periplasmic PstS
    captures inorganic phosphate, the PstA/PstC membrane pair forms the translocation
    pathway, and PstB supplies ATP-dependent energy coupling. PhoU-mediated phosphate-homeostasis
    regulation and the PhoR/PhoB starvation response are adjacent regulatory systems
    rather than transport steps.
  module_outline: "- Bacterial Pst high-affinity phosphate uptake\n  - 1. periplasmic\
    \ phosphate capture\n  - PstS phosphate capture\n    - PstS phosphate-binding\
    \ activity (molecular player: bacterial PstS family; activity or role: phosphate\
    \ ion binding)\n  - 2. phosphate-selective membrane translocation\n  - PstA/PstC\
    \ membrane translocation\n    - PstA/PstC phosphate permease activity (molecular\
    \ player: bacterial PstA/PstC permease pair; activity or role: phosphate transmembrane\
    \ transporter activity)\n  - 3. ATP-dependent energy coupling\n  - PstB ATP-dependent\
    \ energy coupling\n    - PstB phosphate-transport ATPase activity (molecular player:\
    \ bacterial PstB-like ABC ATPase family; activity or role: ATPase-coupled phosphate\
    \ ion transmembrane transporter activity)"
  module_connections: '- PstS phosphate capture feeds into PstA/PstC membrane translocation:
    Phosphate-loaded PstS presents substrate to the PstA/PstC permease.

    - PstB ATP-dependent energy coupling causes PstA/PstC membrane translocation:
    PstB ATP hydrolysis drives phosphate passage through PstA/PstC.'
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_pst_phosphate_uptake__ppu02010-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_pst_phosphate_uptake__ppu02010-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial Pst high-affinity phosphate uptake in Pseudomonas putida KT2440

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

A reusable bacterial ABC-transport module in which periplasmic PstS captures inorganic phosphate, the PstA/PstC membrane pair forms the translocation pathway, and PstB supplies ATP-dependent energy coupling. PhoU-mediated phosphate-homeostasis regulation and the PhoR/PhoB starvation response are adjacent regulatory systems rather than transport steps.

### Provisional Biological Outline

- Bacterial Pst high-affinity phosphate uptake
  - 1. periplasmic phosphate capture
  - PstS phosphate capture
    - PstS phosphate-binding activity (molecular player: bacterial PstS family; activity or role: phosphate ion binding)
  - 2. phosphate-selective membrane translocation
  - PstA/PstC membrane translocation
    - PstA/PstC phosphate permease activity (molecular player: bacterial PstA/PstC permease pair; activity or role: phosphate transmembrane transporter activity)
  - 3. ATP-dependent energy coupling
  - PstB ATP-dependent energy coupling
    - PstB phosphate-transport ATPase activity (molecular player: bacterial PstB-like ABC ATPase family; activity or role: ATPase-coupled phosphate ion transmembrane transporter activity)

### Known Relationships Among Steps

- PstS phosphate capture feeds into PstA/PstC membrane translocation: Phosphate-loaded PstS presents substrate to the PstA/PstC permease.
- PstB ATP-dependent energy coupling causes PstA/PstC membrane translocation: PstB ATP hydrolysis drives phosphate passage through PstA/PstC.

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

# Module/Pathway/Taxon Review: Bacterial Pst High-Affinity Phosphate Uptake in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu02010 "ABC transporters" (151 primary genes; 207 candidates; module area: transport_motility_signaling)
**Module reviewed:** Bacterial Pst high-affinity phosphate uptake (PstS capture → PstA/PstC translocation → PstB ATP coupling)

---

## 1. Executive Summary

The bacterial Pst high-affinity phosphate-uptake module is **fully satisfiable (COVERED)** in *Pseudomonas putida* KT2440. All three canonical module steps — periplasmic phosphate capture, phosphate-selective membrane translocation, and ATP-dependent energy coupling — are encoded by a single, contiguous Pho-regulon operon on the KT2440 chromosome: **PP_5329 (pstS)**, **PP_5328 (pstC)**, **PP_5327 (pstA)**, and **PP_5326 (pstB)**, immediately followed by **PP_5325 (phoU)** and adjacent to the **PhoB/PhoR** two-component regulatory system (PP_5320/PP_5321). This architecture — *pstSCAB-phoU* beside *phoBR* — is the canonical bacterial Pho regulon layout, and KEGG correctly partitions the transport genes into ppu02010 (ABC transporters) while placing the regulatory genes in ppu02020 (two-component system).

The module assignment is supported by **direct, same-species functional evidence**. Wu et al. (1999; [PMID: 16232467](https://pubmed.ncbi.nlm.nih.gov/16232467/)) cloned the *pstSCAB* genes of *Pseudomonas putida* PRS2000 and showed that chromosomal inactivation of *pstSC* abolished ³²Pi uptake even under phosphate limitation, while causing constitutive alkaline phosphatase synthesis and Pi chemotaxis. This demonstrates that PstSCAB is both the high-affinity Pi transporter and a negative regulator of the *pho* regulon in this species. Because KT2440's Pho-box/PhoBR-adjacent operon is orthologous to the PRS2000 operon (and the encoded proteins share >75% identity even with *P. aeruginosa* PAO1), the functional transfer to KT2440 is **strong**.

For curators, the principal issues are **not gaps but paralog ambiguity and over-annotation** within the broad ppu02010 bucket. KT2440 carries (i) a second, complete but **non-Pho-linked** Pst-type operon (PP_2656–2659) whose physiological role is uncertain; (ii) a standalone **OmpA–phosphate-binding fusion** (PP_3818) that is likely mis-annotated as a classic PstS; and (iii) a distinct **phosphonate (C–P bond) ABC transporter** (PhnCE/PtxABCD, PP_0824–0827) plus **low-affinity non-ABC Pi carriers** (PiT-family PP_4103, Na⁺/Pi symporter PP_1373). These belong to separate modules and should be kept out of the inorganic-Pi Pst module. The recommended curation outcome is: **all three Pst steps = covered** via PP_5326–5329; PP_2656–2659 = **candidate_uncertain**; PP_3818, PP_0824–0827, PP_4103, PP_1373 = **excluded from this module** (belong to adjacent modules).

---

## 2. Target-Organism Pathway Definition

### 2.1 What the module includes

The Pst (phosphate-specific transport) module is the **ATP-binding-cassette (ABC) importer for inorganic orthophosphate (Pi)** operating under phosphate-limiting conditions. It comprises exactly three biochemical steps:

1. **Periplasmic phosphate capture** — the substrate-binding protein PstS scavenges free Pi in the periplasm with high affinity.
2. **Phosphate-selective membrane translocation** — the transmembrane permease pair PstA/PstC forms the channel through which Pi passes across the inner membrane.
3. **ATP-dependent energy coupling** — the cytoplasmic ATPase PstB (EC 7.3.2.1) hydrolyzes ATP to drive Pi import against its concentration gradient.

The two mechanistic relationships defined in the module scope both hold in KT2440: phosphate-loaded PstS presents substrate to the PstA/PstC permease, and PstB ATP hydrolysis drives phosphate passage through PstA/PstC.

### 2.2 What must be kept separate

- **PhoU-mediated homeostasis (PP_5325)** and the **PhoR/PhoB starvation response (PP_5321/PP_5320)** are *adjacent regulatory systems*, not transport steps. They are genomically part of the same locus but are correctly mapped by KEGG to ppu02020 (two-component system), and should remain outside the transport module.
- **Phosphonate uptake (PhnCE / PtxABCD; PP_0824–0827)** is a chemically distinct system that imports organophosphonates (C–P bond compounds), not inorganic orthophosphate. It is a separate Pho-regulon member (KO K02041/K02042/K02044; EC 7.3.2.2).
- **Low-affinity Pi uptake** is provided by non-ABC carriers — the PiT-family symporter **PP_4103** (KO K03306) and a phosphate:Na⁺ symporter **PP_1373** (KO K16322) — which are not ABC transporters and belong to different transport modules.
- Broad **overview maps** (KEGG "ABC transporters" ppu02010 as a whole) mix ~207 candidate genes covering dozens of unrelated substrates (amino acids, metals, sugars, LPS export, etc.). Only the Pst-specific loci belong to this module.

### 2.3 Alternate names and database definitions

- **Pst** = "phosphate-specific transport" system; genes *pstS*, *pstC*, *pstA*, *pstB* (sometimes *pstB1/pstB2* for paralogs).
- KEGG orthologs: **K02040 (pstS), K02037 (pstC), K02038 (pstA), K02036 (pstB)**; PhoU = K02039.
- EC number for the ATPase: **7.3.2.1** (ABC-type phosphate transporter). Note the naming inversion in UniProt: the ATPase of the canonical Pho-linked operon (PP_5326) is annotated **pstB2**, while the paralog ATPase (PP_2659) is **pstB1** — an inversion relative to genomic/regulatory context that curators should flag.

---

## 3. Expected Step Model and Satisfiability

| Module step | Expected player | KT2440 gene(s) | KEGG KO | Status |
|---|---|---|---|---|
| 1. Periplasmic phosphate capture | PstS (phosphate-binding protein) | **PP_5329** (pstS) | K02040 | **Covered** |
| 2. Phosphate-selective translocation | PstA/PstC permease pair | **PP_5327** (pstA) + **PP_5328** (pstC) | K02038 / K02037 | **Covered** |
| 3. ATP-dependent energy coupling | PstB ABC ATPase (EC 7.3.2.1) | **PP_5326** (pstB2) | K02036 | **Covered** |
| (Adjacent) Homeostasis regulator | PhoU | PP_5325 | K02039 | Out of module (ppu02020) |
| (Adjacent) Starvation two-component system | PhoR/PhoB | PP_5321 / PP_5320 | K07636 / K07657 | Out of module (ppu02020) |

**All three module steps are encoded by candidate genes in the queried ppu02010 bucket.** No step is missing. The Pst genes fall in the high-PP-number range (PP_5326–5329) and were therefore among the 127 candidate genes truncated from the prompt excerpt (which cut off at PP_1139), not absent from the metadata — this was explicitly verified against `KEGG link/ppu/path:ppu02010` (13/13 relevant loci present, 0 absent).

No Pst step is "not expected" in this organism; *P. putida* is a soil bacterium that routinely experiences phosphate limitation and possesses the full canonical Pho regulon.

---

## 4. Candidate Genes and Evidence

### 4.1 Finding F001 — The canonical pstSCAB-phoU operon (PP_5325–PP_5329)

KEGG (ppu) and UniProt (proteome UP000000556, taxon 160488) jointly identify a contiguous, single-strand (complement) gene cluster on the KT2440 chromosome that encodes all three module steps:

- **PP_5329 pstS** — phosphate-binding protein, periplasmic capture (UniProt Q88C54, 332 aa)
- **PP_5328 pstC** + **PP_5327 pstA** — permease pair, membrane translocation (Q88C55 / Q88C56)
- **PP_5326 pstB2** — phosphate import ATP-binding protein, EC 7.3.2.1 (Q88C57, 277 aa)

Immediately downstream lies **PP_5325 phoU** (PhoU accessory regulator; Q88C58) and the **PhoB/PhoR two-component system** (PP_5320/PP_5321; Q88C63/Q88C62). Genomic positions (~6.070–6.078 Mb, all complement strand) are consistent with a single *pstSCAB-phoU* operon adjacent to *phoBR* — the canonical bacterial Pho regulon architecture. KEGG maps PP_5326–5329 to ppu02010 (ABC transporters) while *phoU/phoB/phoR* map to ppu02020 (two-component system), correctly excluded from the transporter map. **This is the high-confidence, module-satisfying operon.**

### 4.2 Finding F003 — Direct same-species functional validation

Wu et al. (1999; [PMID: 16232467](https://pubmed.ncbi.nlm.nih.gov/16232467/)) cloned the *pstSCAB* genes of *Pseudomonas putida* PRS2000. Predicted products showed **83 / 75 / 78 / 88 % amino-acid identity** (PstS / PstC / PstA / PstB) to the *P. aeruginosa* PAO1 counterparts. Two Pho box sequences were found upstream of *pstS* (15/18 base identity to consensus) and in the *pstS–pstC* intercistronic region (11/18). Chromosomal inactivation of *pstSC* (mutant PNT1) **abolished ³²Pi uptake even under Pi limitation** and caused constitutive alkaline phosphatase synthesis and Pi chemotaxis, showing PstSCAB is both the high-affinity Pi transporter and a negative regulator of the *pho* regulon.

> *"The resultant mutant, designated PNT1, failed to take up ³²Pi even under conditions of Pi limitation."* — [PMID: 16232467](https://pubmed.ncbi.nlm.nih.gov/16232467/)

> *"Two well-conserved Pho box sequences were found in the region upstream of the pstS gene."* — [PMID: 16232467](https://pubmed.ncbi.nlm.nih.gov/16232467/)

UniProt/KEGG place the orthologous, Pho-box/PhoBR-adjacent operon in KT2440 at PP_5329/PP_5328/PP_5327/PP_5326 (Q88C54/55/56/57). **Species transfer is STRONG** (same species, different strain; >75% identity even to *P. aeruginosa*).

### 4.3 Findings F002 & F004 — Paralog landscape and domain architecture

KEGG KO mapping returns multiple ppu genes per phosphate KO, revealing paralog ambiguity:

| KO | Gene | Canonical (Pho-linked) | Paralog | Third copy |
|---|---|---|---|---|
| K02040 pstS | phosphate-binding | PP_5329 | PP_2656 | PP_3818 |
| K02037 pstC | permease | PP_5328 | PP_2657 | — |
| K02038 pstA | permease | PP_5327 | PP_2658 | — |
| K02036 pstB | ATPase | PP_5326 (pstB2) | PP_2659 (pstB1) | — |

**Cluster 2 (PP_2656–2659)** is a second complete *pst* operon at ~3.043–3.047 Mb (forward strand). Domain/transmembrane analysis clarifies the roles:

- **Phosphate-binding subunits:** PP_5329 (PF12849, 332 aa) and PP_2656 (PF12849, 348 aa) are classic PBP-type PstS. **PP_3818 (435 aa) carries PF00691 (OmpA) fused to PF12849** — an outer-membrane-associated phosphate-binding fusion, *not* a canonical periplasmic PstS.
- **Permeases:** all PF00528 (BPD_transp_1). Canonical **PP_5327 (556 aa, 6 TM)** and **PP_5328 (762 aa, 8 TM)** are genuine ABC permeases but markedly **longer** than the paralogous PP_2658 (297 aa, 6 TM) and PP_2657 (322 aa, 7 TM), which match canonical PstA/PstC sizes (~300–320 aa).
- **ATPases:** PP_5326 and PP_2659 are both PF00005 (ABC_tran, ~277–279 aa).

All these entries are UniProt evidence level "Inferred from homology" or "Predicted."

### 4.4 Finding F006 — Genomic-context distinction of the paralog

The second Pst-type operon PP_2656–2659 is flanked by PP_2653 (Cro/CI-family transcriptional regulator), PP_2654 (glutathione S-transferase), and hypothetical proteins PP_2655/PP_2660/PP_2661 — i.e., **NOT adjacent to phoU/phoB/phoR**, unlike the canonical PP_5325–5329 / PP_5320–5321 locus. This absence of Pho-regulon context is the key argument that PP_2656–2659 is *not* the primary high-affinity Pi transporter and should be treated as candidate_uncertain (possibly serving a specialized or conditionally expressed role).

PP_3818 (OmpA + phosphate-binding fusion) is isolated among a polyamine ABC transporter (PP_3816/PP_3817), glutathione reductase (PP_3819), and a group II intron maturase (PP_3820), **with no cognate permease/ATPase neighbours** — reinforcing that it is not a functional Pst substrate-binding subunit.

### 4.5 Finding F005 — Phosphonate transporters are a distinct system

The ppu02010 candidate list includes **PP_0824 ptxB / PP_0825 phnC (EC 7.3.2.2) / PP_0826 phnE / PP_0827 ptxC** — a phosphonate (C–P bond) uptake ABC transporter (KO K02041/K02042/K02044), biochemically distinct from inorganic-phosphate PstSCAB (KO K02036–K02040, EC 7.3.2.1). Comparative *Pseudomonas* Pho-regulon proteomics (Lidbury et al. 2016, [PMID: 27233093](https://pubmed.ncbi.nlm.nih.gov/27233093/)) found putative phosphonate transporters among Pi-depletion-induced PHO proteins, and *P. putida* can degrade organophosphonates such as 2-aminoethylphosphonate ([PMID: 9841125](https://pubmed.ncbi.nlm.nih.gov/9841125/)). Both PstSCAB and PhnCE are Pho-regulon members but serve **different substrates**.

> *"...several proteins, previously not associated with the response to Pi depletion, were also identified. These included putative nucleases, phosphotriesterases, putative phosphonate transporters and outer membrane proteins."* — [PMID: 27233093](https://pubmed.ncbi.nlm.nih.gov/27233093/)

### 4.6 Finding F007 — Coverage is real, not a metadata gap

`KEGG link/ppu/path:ppu02010` confirms all relevant loci are members of the queried bucket: the PstS/C/A/B primary operon (PP_5326, PP_5327, PP_5328, PP_5329); the paralog operon (PP_2656, PP_2657, PP_2658, PP_2659); the OmpA-fusion PP_3818; and the phosphonate transporter PP_0824–PP_0827 (**13/13 present; 0 absent**). These loci fall in the high-PP-number range and were among the candidate genes omitted from the truncated prompt excerpt, not missing from the metadata.

---

## 5. Mechanistic Model / Interpretation

The KT2440 high-affinity phosphate-uptake landscape can be summarized as a single functional Pst module embedded in the Pho regulon, surrounded by paralogs and alternative carriers that must be kept out of the module:

```
             PERIPLASM                     INNER MEMBRANE            CYTOPLASM
             ---------                     --------------            ---------

  Pi  ──►  PstS (PP_5329) ──presents──►  PstC (PP_5328) │ PstA (PP_5327)  ──► Pi in
           phosphate capture             permease pair (translocation)
           [K02040]                      [K02037 / K02038]
                                                  ▲
                                                  │ ATP hydrolysis drives transport
                                                  │
                                         PstB2 (PP_5326)  [K02036, EC 7.3.2.1]
                                         ATP ──► ADP + Pi

  Regulatory context (NOT part of transport module, KEGG ppu02020):
     PhoU (PP_5325) ── homeostasis ──┐
     PhoR (PP_5321) ─ sensor kinase ─┼─► PhoB (PP_5320) ─► Pho-box activation
                                     │      of pstSCAB & pho regulon
     (Pho boxes upstream of pstS)  ──┘
```

**Parallel / alternative phosphorus systems (separate modules):**

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │ Second Pst operon  PP_2656–2659  (forward strand, ~3.04 Mb)          │
  │   NO phoU/phoBR neighbours → candidate_uncertain                     │
  │   canonical-size permeases (297/322 aa), ATPase = pstB1              │
  ├─────────────────────────────────────────────────────────────────────┤
  │ PP_3818  OmpA(PF00691)+PBP(PF12849) fusion, 435 aa, no permease/ATPase│
  │   → likely mis-annotated PstS; NOT a canonical binding subunit       │
  ├─────────────────────────────────────────────────────────────────────┤
  │ Phosphonate ABC importer  PhnCE/PtxABCD  PP_0824–0827 (EC 7.3.2.2)   │
  │   → C–P bond substrates, separate module                            │
  ├─────────────────────────────────────────────────────────────────────┤
  │ Low-affinity Pi carriers (non-ABC): PiT PP_4103 (K03306),           │
  │   Na+/Pi symporter PP_1373 (K16322)  → separate modules              │
  └─────────────────────────────────────────────────────────────────────┘
```

The interpretive core is that **genomic context is decisive for disambiguating paralogs**. Two features cleanly separate the true module-satisfying operon from its look-alikes: (1) adjacency to *phoU-phoBR* and the presence of upstream Pho boxes (present only for PP_5326–5329), and (2) the concordance of same-species knockout phenotype with this operon's orthology. The paralog operon lacks the regulatory context, and the OmpA fusion lacks both the correct domain architecture and cognate transport partners. This is a textbook case where an unfiltered KEGG ABC-transporter bucket over-reports "phosphate transporter" candidates because homology-based KO assignment cannot by itself distinguish the physiologically dominant transporter from paralogs and chemically distinct systems.

An important curation caveat is the **UniProt pstB1/pstB2 naming inversion**: the ATPase of the canonical Pho-linked operon (PP_5326) is named *pstB2*, while the paralog (PP_2659) is *pstB1*. Curators relying on a "pstB1 = primary" heuristic would pick the wrong locus; the genomic/regulatory evidence should override the name.

---

## 6. Gaps, Ambiguities, and Likely Over-Annotations

| Item | KT2440 loci | Issue | Recommended handling |
|---|---|---|---|
| Paralog Pst operon | PP_2656–2659 | Complete *pst*-type operon but **no Pho-regulon context**; unknown physiological trigger | **candidate_uncertain** — promote to full review |
| OmpA–PBP fusion | PP_3818 | OmpA(PF00691)+PstS(PF12849) fusion, no permease/ATPase partners; likely **over-propagated "PstS" annotation** | Exclude from Pst module; flag annotation |
| Phosphonate transporter | PP_0824–0827 | Distinct substrate (C–P bond, EC 7.3.2.2); Pho-regulon member but **different module** | Exclude; assign to phosphonate module |
| Low-affinity Pi carriers | PP_4103 (PiT), PP_1373 (Na⁺/Pi) | Non-ABC; **not part of Pst ABC module** | Exclude; separate transporter modules |
| pstB naming inversion | PP_5326 (pstB2) vs PP_2659 (pstB1) | UniProt names invert genomic/regulatory context | Curator note; trust genomic context |
| Elongated canonical permeases | PP_5327 (556 aa), PP_5328 (762 aa) | Longer than typical PstA/PstC (~300 aa) but genuine PF00528 permeases | Accept as genuine; note length atypicality |
| Broad ppu02010 bucket | ~207 candidate genes | Overview map mixes dozens of unrelated ABC substrates | Only PP_5326–5329 belong to this module |

**Key uncertainty:** All KT2440 Pst annotations are UniProt evidence level "Inferred from homology" or "Predicted." The functional demonstration is in *P. putida* PRS2000, not KT2440 directly — a same-species but different-strain transfer (strong, but not strain-direct experimental proof for KT2440 itself).

---

## 7. Module and GO-Curation Recommendations

### 7.1 Module step status

- **Step 1 (PstS phosphate capture): COVERED** by PP_5329 (K02040). High confidence.
- **Step 2 (PstA/PstC translocation): COVERED** by PP_5327 + PP_5328 (K02038/K02037). High confidence.
- **Step 3 (PstB ATP coupling): COVERED** by PP_5326 (K02036, EC 7.3.2.1). High confidence.
- **Overall module: COVERED / satisfiable** in *P. putida* KT2440 via the single operon PP_5326–5329.

### 7.2 Module boundary recommendations

- The **generic module boundaries are correct** for this organism. PhoU/PhoR/PhoB should remain *outside* the transport module as adjacent regulatory systems (KEGG already segregates them to ppu02020).
- **No module_needs_revision** flag for the core three steps.
- **No new GO term requests** appear necessary; existing GO terms cover phosphate ion binding (GO:0042301), phosphate ion transmembrane transporter activity (GO:0015415 / GO:0005315), and ATPase-coupled phosphate transport.

### 7.3 Genes to exclude / reassign

- PP_2656–2659 → **candidate_uncertain** (do not count toward primary coverage; investigate role).
- PP_3818 → exclude from Pst module; likely **over-annotation** of the PstS role.
- PP_0824–0827 → belongs to a **phosphonate uptake module**, not inorganic-Pi Pst.
- PP_4103, PP_1373 → **low-affinity / non-ABC Pi transport**, separate modules.

---

## 8. Genes to Promote to Full `fetch-gene` Review

1. **PP_5329 (pstS), PP_5328 (pstC), PP_5327 (pstA), PP_5326 (pstB2)** — the four module-satisfying genes; promote to confirm strain-direct annotation and lock coverage. *Priority: high (module-defining).*
2. **PP_2656–2659 (second Pst operon)** — resolve whether this is a functional Pi transporter, a specialized/conditional paralog, or a pseudo-operon. Its lack of Pho context and canonical-size permeases make its role the single most important open question. *Priority: high (ambiguity resolution).*
3. **PP_3818 (OmpA–PBP fusion)** — confirm and correct the likely over-propagated "PstS" annotation; determine actual function (possibly outer-membrane phosphate scavenging). *Priority: medium.*
4. **PP_0824–0827 (PhnCE/PtxABCD)** — confirm phosphonate-transport assignment and route to the correct module. *Priority: medium (boundary hygiene).*

---

## 9. Evidence Base and Key References

| PMID | Title (abbrev.) | Role in this review | Evidence strength for KT2440 |
|---|---|---|---|
| [16232467](https://pubmed.ncbi.nlm.nih.gov/16232467/) | *Cloning and characterization of P. putida pst system* | **Primary functional evidence**: pstSC knockout abolishes ³²Pi uptake; Pho boxes upstream of pstS | Strong (same species, PRS2000 strain) |
| [27233093](https://pubmed.ncbi.nlm.nih.gov/27233093/) | *Comparative genomic/proteomic analyses of three Pseudomonas strains* | Distinguishes phosphonate transporters as a separate Pi-depletion-induced class | Moderate (genus-level) |
| [9841125](https://pubmed.ncbi.nlm.nih.gov/9841125/) | *2-aminoethylphosphonic acid biodegradation in P. putida NG2* | Confirms *P. putida* organophosphonate metabolism, supporting phosphonate-system separation | Moderate (species, different strain) |

**Supporting context papers** (phosphate-related *P. putida* physiology, not module-defining): [PMID: 41264166](https://pubmed.ncbi.nlm.nih.gov/41264166/) (aluminium exposure perturbs phosphate metabolism in KT2440); [PMID: 39522389](https://pubmed.ncbi.nlm.nih.gov/39522389/), [PMID: 38360401](https://pubmed.ncbi.nlm.nih.gov/38360401/), [PMID: 36966146](https://pubmed.ncbi.nlm.nih.gov/36966146/) (*P. putida* phosphate-solubilization / plant-interaction studies).

**Database evidence:** KEGG (organism ppu; pathways ppu02010, ppu02020; KO K02036–K02040), UniProt (proteome UP000000556; Q88C54–Q88C58, Q88C62/C63; Pfam PF12849, PF00528, PF00005, PF00691), NCBI taxon 160488.

---

## 10. Limitations and Knowledge Gaps

1. **No strain-direct functional data for KT2440.** The decisive knockout evidence is from *P. putida* PRS2000, not KT2440. Orthology and >75% identity make transfer strong, but a KT2440-specific *pstSC* deletion phenotype has not been cited here.
2. **All KT2440 Pst annotations are homology-inferred or predicted** (UniProt evidence levels), not experimentally curated at the protein level.
3. **The role of the second Pst operon (PP_2656–2659) is unknown.** Without expression or knockout data, we cannot say whether it contributes to Pi uptake, transports a different oxyanion, or is silent.
4. **PP_3818's actual function is unverified** — the OmpA fusion suggests outer-membrane phosphate handling, but this is inferred from domain architecture only.
5. **Pi-affinity kinetics (Km) for KT2440's transporters have not been measured** in the data reviewed; "high-affinity" status rests on the Pho-regulon linkage and PRS2000 phenotype.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Strain-direct genetics:** Construct a KT2440 Δ*pstSCAB* (ΔPP_5326–5329) mutant and measure ³²Pi/³³Pi uptake and alkaline phosphatase derepression to confirm strain-specific function.
2. **Paralog dissection:** Single and double deletions of PP_2656–2659 vs PP_5326–5329, with growth on limiting Pi and transcriptomics under Pi starvation, to define the paralog's role and Pho-regulon (in)dependence.
3. **Expression profiling:** RNA-seq / proteomics under Pi-replete vs Pi-depleted conditions to test which operon(s) are Pho-regulated (expect PP_5326–5329 induced, PP_2656–2659 possibly not).
4. **PP_3818 characterization:** Localization and phosphate-binding assays to test the outer-membrane phosphate-scavenging hypothesis and correct the annotation.
5. **Curation actions:** Mark the three Pst steps covered; flag PP_2656–2659 candidate_uncertain and promote to full review; reassign PP_0824–0827 to a phosphonate module; add a curator note on the pstB1/pstB2 naming inversion.
6. **Expert question:** Ask a *Pseudomonas* phosphate-physiology expert whether the second Pst operon is known to be functional or conditionally expressed in any *P. putida* strain.

---

*Review complete. Module: Bacterial Pst high-affinity phosphate uptake — COVERED and satisfiable in P. putida KT2440 via PP_5326–5329, with paralog and boundary curation flags delivered.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_pst_phosphate_uptake__ppu02010-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_pst_phosphate_uptake__ppu02010-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16232467
2. PMID:27233093
3. PMID:9841125
4. PMID:41264166
5. PMID:39522389
6. PMID:38360401
7. PMID:36966146