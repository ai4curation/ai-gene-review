---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:22:27.886756'
end_time: '2026-09-01T02:37:37.760497'
duration_seconds: 909.87
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial Lol-dependent outer-membrane lipoprotein trafficking
  module_summary: A species-neutral diderm-bacterial module for ATP-dependent release
    of outer-membrane-destined mature lipoproteins from the inner membrane by LolCDE,
    periplasmic carriage by LolA, and delivery into the outer membrane by LolB. Lipoprotein
    maturation and inner-membrane retention decisions are upstream of this module.
  module_outline: "- Bacterial Lol-dependent outer-membrane lipoprotein trafficking\n\
    \  - 1. ATP-dependent inner-membrane extraction and release\n  - LolCDE lipoprotein\
    \ release\n    - LolCDE lipoprotein-release complex (molecular player: LolCDE\
    \ ABC lipoprotein-release complex; activity or role: ATP-dependent lipoprotein\
    \ extraction and release activity)\n  - 2. Periplasmic lipoprotein carriage\n\
    \  - LolA periplasmic carriage\n    - LolA periplasmic lipoprotein carrier (molecular\
    \ player: LolA family; activity or role: periplasmic lipoprotein carrier activity)\n\
    \  - 3. Outer-membrane delivery and incorporation\n  - LolB outer-membrane delivery\n\
    \    - LolB outer-membrane lipoprotein receptor (molecular player: LolB family;\
    \ activity or role: outer-membrane lipoprotein delivery activity)"
  module_connections: '- LolCDE lipoprotein release feeds into LolA periplasmic carriage:
    LolCDE loads released lipoprotein onto LolA.

    - LolA periplasmic carriage feeds into LolB outer-membrane delivery: LolA presents
    its lipoprotein cargo to LolB.'
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
  path: PSEPK__bacterial_lol_lipoprotein_trafficking__ppu02010-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_lol_lipoprotein_trafficking__ppu02010-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial Lol-dependent outer-membrane lipoprotein trafficking in Pseudomonas putida KT2440

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

A species-neutral diderm-bacterial module for ATP-dependent release of outer-membrane-destined mature lipoproteins from the inner membrane by LolCDE, periplasmic carriage by LolA, and delivery into the outer membrane by LolB. Lipoprotein maturation and inner-membrane retention decisions are upstream of this module.

### Provisional Biological Outline

- Bacterial Lol-dependent outer-membrane lipoprotein trafficking
  - 1. ATP-dependent inner-membrane extraction and release
  - LolCDE lipoprotein release
    - LolCDE lipoprotein-release complex (molecular player: LolCDE ABC lipoprotein-release complex; activity or role: ATP-dependent lipoprotein extraction and release activity)
  - 2. Periplasmic lipoprotein carriage
  - LolA periplasmic carriage
    - LolA periplasmic lipoprotein carrier (molecular player: LolA family; activity or role: periplasmic lipoprotein carrier activity)
  - 3. Outer-membrane delivery and incorporation
  - LolB outer-membrane delivery
    - LolB outer-membrane lipoprotein receptor (molecular player: LolB family; activity or role: outer-membrane lipoprotein delivery activity)

### Known Relationships Among Steps

- LolCDE lipoprotein release feeds into LolA periplasmic carriage: LolCDE loads released lipoprotein onto LolA.
- LolA periplasmic carriage feeds into LolB outer-membrane delivery: LolA presents its lipoprotein cargo to LolB.

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

# Species-Aware Review: Lol-Dependent Outer-Membrane Lipoprotein Trafficking in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Bacterial Lol-dependent OM lipoprotein trafficking (LolCDE → LolA → LolB)
**Commissioned bucket:** KEGG `ppu02010` "ABC transporters" (207 candidate genes)
**Date:** 2026-09-01

---

## 1. Executive Summary

The Lol module is **fully satisfiable** in *P. putida* KT2440. Every expected step maps one-to-one to a high-confidence, single-copy ortholog (LolD, LolA, LolB are Swiss-Prot/HAMAP-reviewed; LolC, LolE are TrEMBL but confirmed by synteny and 40–46 % identity to *E. coli* — see §4):

| Module step | Gene | Locus | UniProt | KO |
|---|---|---|---|---|
| LolCDE IM extraction/release (permease) | *lolC* | PP_2154 | Q88KY5 | K09808 |
| LolCDE IM extraction/release (ATPase) | *lolD* | PP_2155 | Q88KY4 (LOLD_PSEPK) | K09810 |
| LolCDE IM extraction/release (permease) | *lolE* | PP_2156 | Q88KY3 | K09808 |
| LolA periplasmic carriage | *lolA* | PP_4003 | Q88FS9 (LOLA_PSEPK) | K03634 |
| LolB OM delivery/incorporation | *lolB* | PP_0724 | Q88PX4 (LOLB_PSEPK) | K02494 |

**Two curation-critical points:**

1. **The provided candidate list does not represent this module.** None of the five Lol genes appear in the `kegg:ppu02010` candidate set. `lolA`/`lolB` are not ABC transporters, and `lolCDE`, although mechanistically an ABC transporter, is **not assigned to any KEGG pathway map** (its KEGG `PATHWAY` field is empty for all three genes). The Lol system is a KEGG **BRITE/orthology** entity, not a `map02010` member. Curators must source this module by KO or GO:0044874, **not** by the ABC-transporter bucket.

2. **All steps should be marked `covered`.** There is no gap, and no lineage-specific replacement is needed — unlike some diderms that lack *lolB* and rely on a bifunctional LolA, KT2440 retains a genuine *lolB*.

---

## 2. Target-Organism Pathway Definition

**Included biochemistry (this module):** ATP-dependent release of *mature, OM-destined* triacylated lipoproteins from the outer leaflet of the inner membrane by the LolCDE ABC complex; hand-off to the periplasmic carrier LolA; transfer across the periplasm; and receptor-mediated insertion into the inner leaflet of the OM by LolB.

**Explicitly upstream / separate (keep out of this module):**
- Lipoprotein maturation and IM-retention decisions: Lgt (diacylglyceryl transferase), LspA/signal peptidase II, Lnt (N-acyl transferase), and the "+2 rule" Lol-avoidance signal (Zückert 2014, PMID 24780125). These are *prerequisites*, not Lol steps.
- Sec/general secretory export of prolipoproteins.
- Downstream OM assembly machines that *consume* Lol cargo: Bam (β-barrel assembly), Lpt (LPS export — note LptB PP_0953, LptF PP_0982, LptG PP_0983 are in the candidate list but belong to a **different** module), Lpo–PBP.

**Neighboring overview maps to keep separate:** KEGG `map02010` (ABC transporters) and `map03070` (secretion). The Lol system overlaps mechanistically with ABC transporters but should be curated as its own transport/localization module.

**Alternate names / definitions:** "Lipoprotein-releasing system" (KEGG/GenBank naming for LolCDE), "Lol pathway/machinery," "outer-membrane lipoprotein localization (Lol)."

---

## 3. Expected Step Model vs. Target Taxon

| Generic step | Player | Status in KT2440 | Evidence |
|---|---|---|---|
| 1. ATP-dependent IM extraction/release | LolCDE | **covered** | *lolC-lolD-lolE* syntenic operon PP_2154–2156; HAMAP-reviewed LolD; KO K09808/K09810 |
| 2. Periplasmic carriage | LolA | **covered** | *lolA* PP_4003, HAMAP MF_00240, single-copy, periplasmic |
| 3. OM delivery/incorporation | LolB | **covered** | *lolB* PP_0724, HAMAP MF_00233, OM lipid-anchor, single-copy |

Step-relationships (LolCDE→LolA→LolB) are conserved and structurally characterized in the paradigm organisms (Kaplan et al. 2018/2022, PMID 30012603, 36037338).

---

## 4. Candidate Genes and Evidence

Because the `ppu02010` candidate list omits all Lol genes, the relevant "candidates" are the KO/UniProt-derived orthologs:

- **PP_2154 *lolC* (Q88KY5, K09808):** IM permease, MacB/FtsX-like. Evidence: orthology + HAMAP-family GO annotation (GO:0044874). Caveat: MacB/FtsX permease family is large; BLAST alone can confuse LolC with MacB efflux permeases or TagS-like T6SS proteins. Synteny with *lolD/lolE* is the discriminating feature.
- **PP_2155 *lolD* (Q88KY4, LOLD_PSEPK, K09810):** ABC ATPase, EC 7.6.2.-, HAMAP MF_01708 (reviewed). **Highest confidence** of the operon. Caveat: EC 7.6.2.- and generic "ABC ATP-binding" annotations are broad; do not transfer LolD identity to other ABC ATPases on EC alone.
- **PP_2156 *lolE* (Q88KY3, K09808):** second IM permease; paralogous fold to LolC. Same MacB/FtsX-family caveat.
- **PP_4003 *lolA* (Q88FS9, LOLA_PSEPK, K03634):** periplasmic carrier, HAMAP MF_00240 (reviewed). Single-copy — no paralog ambiguity (confirmed by family and text searches returning exactly one hit).
- **PP_0724 *lolB* (Q88PX4, LOLB_PSEPK, K02494):** OM lipoprotein receptor, HAMAP MF_00233 (reviewed). Single-copy. DUF1329 hits (PP_0766, PP_2043, PP_2810, PP_5590) are **not** LolB — different fold, spurious text matches.

**Genomic context:** *lolCDE* sits between PP_2153 (PilZ-domain protein) and PP_2157 (sensor histidine kinase); a clean three-gene operon. *lolA* and *lolB* are unlinked (as in most gamma-proteobacteria).

**Quantitative orthology check (Needleman–Wunsch % identity, KT2440 vs *E. coli* K-12):**

| Protein | KT2440 | *E. coli* | % identity |
|---|---|---|---|
| LolC | PP_2154 (Q88KY5) | P0ADC3 | 45.9 |
| LolD | PP_2155 (Q88KY4) | P75957 | 61.2 |
| LolE | PP_2156 (Q88KY3) | P75958 | 40.5 |
| LolA | PP_4003 (Q88FS9) | P61316 | 39.7 |
| LolB | PP_0724 (Q88PX4) | P61320 | 30.3 |

All identities are well above the ~20–25 % twilight zone; the gradient (LolD ATPase most conserved → LolB OM receptor least conserved) matches known Lol evolutionary rates. This confirms the two TrEMBL entries (PP_2154 LolC, PP_2156 LolE) are true Lol permeases, **not** MacB efflux paralogs (which score far lower vs *E. coli* LolC/E). Sequence features corroborate function: **LolB** N-terminus `MFLRHCITFTLIALLAGC…` carries a lipobox (+1 Cys after `LAGC`) — LolB is itself a lipoprotein and thus an *autologous* Lol client; **LolA** N-terminus `…VTAYA↓G…` is a cleavable Sec signal peptide with an AXA signal-peptidase-I site and no lipobox — a soluble periplasmic carrier.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

- **No true biological gap.** All three module steps covered by reviewed orthologs.
- **Paralog / over-propagation risk (LolCDE only) — concrete KT2440 loci:** LolC/LolE share the MacB/FtsX permease fold and LolD shares EC 7.6.2.- with several unrelated KT2440 ABC systems. Verified MacB/FtsX-family paralogs that must **not** be labeled Lol: PP_3734/PP_3735 and PP_0506/PP_0507 (MacB-type efflux), PP_2316/PP_2317 (*ybbA*; note PP_2317's annotation even text-matches "lipoprotein releasing"), *pvdT* PP_4210 (pyoverdine export, EC 7.6.2.-), and cell-division **FtsEX** (*ftsX* PP_5109 / *ftsE* PP_5110). *P. aeruginosa* additionally has a LolCDE-homologous **TagTS** ABC dedicated to type VI secretion (Casabona et al. 2013, PMID 22765374); KT2440 carries **three** T6SS clusters (HSI-I ~PP_2614–2627, HSI-II ~PP_3088–3106, HSI-III PP_4049/PP_4071–4081) but no clearly annotated dedicated TagTS. Anchor Lol identity to the syntenic **PP_2154–2156** operon + KO K09808/K09810, never to fold or EC.
- **Cargo vs. machinery:** the three T6SS OM lipoproteins **TssJ** (PP_2618, PP_3094, PP_4079) are Lol-dependent *clients*, not Lol components — curate them downstream of, not within, this module.
- **Broad-mapping caveats:** LolD's EC 7.6.2.- and the generic "ABC transporter, ATP-binding protein" descriptors in the candidate list (e.g., PP_0141, PP_1078) are not Lol-specific.
- **Candidate-bucket mismatch (metadata defect, not biology):** the `ppu02010` extraction is the wrong source for this module (Section 1, point 1).

---

## 6. Module and GO-Curation Recommendations

- **Step 1 (LolCDE):** `covered` — PP_2154/2155/2156.
- **Step 2 (LolA):** `covered` — PP_4003.
- **Step 3 (LolB):** `covered` — PP_0724.
- **Module status:** satisfiable/covered; **not** `gap` or `not_expected_in_target_taxon`.
- **`module_needs_revision` (metadata, not biology):** the candidate-gene provisioning rule should pull Lol genes by KO (K09808, K09810, K03634, K02494) or GO:0044874, replacing the `kegg:ppu02010` bucket, which returns 207 ABC-transporter genes and zero Lol genes. **Verified:** genome-wide KEGG KO→gene links return *exactly* the five Lol genes and nothing else — K09808→PP_2154+PP_2156, K09810→PP_2155, K03634→PP_4003, K02494→PP_0724 — with the MacB/FtsX efflux paralogs excluded (they carry different KOs). KO-keyed sourcing is therefore clean and single-copy; no manual paralog filtering is needed.
- **GO:** existing GO:0044874 (lipoprotein localization to OM), GO:0042953 (lipoprotein transport), GO:0030288 (OM-bounded periplasm) are already applied and adequate; **no new GO term requests needed**.
- **Boundary correction:** ensure Lpt genes present in the candidate list (PP_0953 *lptB*, PP_0982, PP_0983) are curated to the LPS-export module, not conflated with Lol.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority order:
1. **PP_2154 *lolC*** and **PP_2156 *lolE*** — confirm they are the housekeeping Lol permeases (not MacB/TagS paralogs) via synteny and reciprocal-best-hit; these are the least "reviewed" of the set (TrEMBL, not Swiss-Prot).
2. **PP_2155 *lolD*** — verify operon co-transcription; already Swiss-Prot, lower risk.
3. **PP_0724 *lolB*** and **PP_4003 *lolA*** — Swiss-Prot reviewed and single-copy; promote mainly to attach direct citations and confirm essentiality expectation.

---

## 8. Key References

- Zückert WR. Secretion of bacterial lipoproteins… *BBA* 2014. **PMID 24780125** — defines Lol scope and upstream maturation boundary.
- Grabowicz M. Lipoproteins and their trafficking to the OM. 2019. **PMID 30900542** — LolCDE/LolA/LolB paradigm.
- Kaplan E, et al. LolA–LolC structure. *PNAS* 2018. **PMID 30012603**; Structural basis of recognition by LolA. 2022. **PMID 36037338** — mechanism of hand-off.
- Smith AN, et al. Evolution of lipoprotein trafficking; bifunctional LolA. 2023. **PMID 36716372** — lineage variation, *lolB* loss in some diderms (KT2440 retains *lolB*).
- Hoang HH, et al. OM targeting in *P. aeruginosa* depends on Bam/Lol. 2011. **PMID 22147293** — genus-level functional evidence; LolB depletion affects all lipoproteins.
- Casabona MG, et al. LolCDE-homologous TagTS activates T6SS in *P. aeruginosa*. 2013. **PMID 22765374** — paralog/over-annotation caveat.
- Molina-Henares MA, et al. Conditionally essential genes of *P. putida* KT2440. 2010. **PMID 20158506** — KT2440 functional-genomics context.

---

### Evidence-confidence summary
- **Direct for target strain:** genome/proteome annotation (UniProt UP000000556, KEGG ppu) — high confidence, but computational/homology-based; no published KT2440-specific Lol knockout phenotype located.
- **Strong genus transfer:** *P. aeruginosa* functional data (PMID 22147293, 22765374) — same genus, syntenic single-copy orthologs.
- **Paradigm mechanism:** *E. coli* structural/biochemical work — mechanism, not strain-specific claims.

**Open questions:** (i) experimental confirmation that *lolCDE* is one operon in KT2440; (ii) direct essentiality of *lolA/lolB* in KT2440 (expected essential, not in the minimal-medium conditional screen of PMID 20158506); (iii) whether any KT2440 MacB/FtsX paralog carries a mis-propagated Lol label.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_lol_lipoprotein_trafficking__ppu02010-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_lol_lipoprotein_trafficking__ppu02010-deep-research-openscientist_artifacts/final_report.pdf)