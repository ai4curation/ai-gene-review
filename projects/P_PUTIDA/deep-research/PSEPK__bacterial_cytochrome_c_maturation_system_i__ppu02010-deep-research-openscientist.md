---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T12:40:27.557408'
end_time: '2026-09-01T12:54:33.264315'
duration_seconds: 845.71
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial cytochrome c maturation system I
  module_summary: A reusable bacterial module for covalent attachment of heme to exported
    c-type cytochrome apoproteins by cytochrome c maturation system I. The canonical
    CcmABCDEFGH machinery combines CcmAB-dependent energy coupling, CcmCDE-dependent
    heme trafficking and holo-CcmE formation, CcmG/CcmH thiol reduction, and CcmF/CcmH-dependent
    heme ligation. Lineage-dependent CcmI/CycH-family factors can support the ligation
    stage. Sec-dependent apocytochrome export, upstream DsbD electron delivery, and
    heme biosynthesis are external dependencies.
  module_outline: "- Bacterial cytochrome c maturation system I\n  - 1. heme trafficking\
    \ and holo-CcmE formation\n  - CcmABCDE heme trafficking and holo-CcmE formation\n\
    \    - 1. ATP-dependent holo-CcmE processing\n    - CcmAB energy-coupling subcomplex\n\
    \      - CcmA ATPase (molecular player: CcmA cytochrome-c-maturation ATPase family;\
    \ activity or role: ATP hydrolysis activity)\n      - CcmB membrane subunit (molecular\
    \ player: CcmB cytochrome-c-maturation family)\n    - 2. heme transfer and covalent\
    \ loading of CcmE\n    - CcmCDE holo-CcmE-forming assembly\n      - CcmC heme-handling\
    \ subunit (molecular player: CcmC cytochrome-c-biogenesis family; activity or\
    \ role: heme binding)\n      - CcmD accessory subunit (molecular player: CcmD\
    \ cytochrome-c-maturation family)\n      - CcmE heme chaperone (molecular player:\
    \ CcmE heme-chaperone family; activity or role: heme binding)\n  - 2. reductive\
    \ preparation of apocytochrome CXXCH motifs\n  - CcmG/CcmH apocytochrome thiol-redox\
    \ preparation\n    - CcmG thiol-disulfide oxidoreductase (molecular player: CcmG/DsbE\
    \ thioredoxin family; activity or role: disulfide oxidoreductase activity)\n \
    \   - CcmH redox component (molecular player: CcmH cytochrome-c-maturation family)\n\
    \  - 3. covalent heme ligation to reduced apocytochrome\n  - CcmF/CcmH heme-ligation\
    \ machinery\n    - 1. holocytochrome-c synthase complex\n    - CcmF/CcmH holocytochrome-c\
    \ synthase complex\n      - CcmF/CcmH holocytochrome-c synthase activity (molecular\
    \ player: bacterial CcmF/CcmH heme-ligation complex; activity or role: holocytochrome-c\
    \ synthase activity)\n    - 2. lineage-dependent maturation accessory\n    - CcmI/CycH-family\
    \ accessory factor\n      - CycH-family maturation accessory (molecular player:\
    \ CycH cytochrome-c-maturation family)"
  module_connections: '- CcmABCDE heme trafficking and holo-CcmE formation feeds into
    CcmF/CcmH heme-ligation machinery

    - CcmG/CcmH apocytochrome thiol-redox preparation feeds into CcmF/CcmH heme-ligation
    machinery

    - CcmAB energy-coupling subcomplex feeds into CcmCDE holo-CcmE-forming assembly

    - CcmC heme-handling subunit feeds into CcmE heme chaperone

    - CcmD accessory subunit feeds into CcmE heme chaperone

    - CcmG thiol-disulfide oxidoreductase feeds into CcmH redox component

    - CcmI/CycH-family accessory factor part of CcmF/CcmH holocytochrome-c synthase
    complex'
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
  path: PSEPK__bacterial_cytochrome_c_maturation_system_i__ppu02010-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_cytochrome_c_maturation_system_i__ppu02010-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial cytochrome c maturation system I in Pseudomonas putida KT2440

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

A reusable bacterial module for covalent attachment of heme to exported c-type cytochrome apoproteins by cytochrome c maturation system I. The canonical CcmABCDEFGH machinery combines CcmAB-dependent energy coupling, CcmCDE-dependent heme trafficking and holo-CcmE formation, CcmG/CcmH thiol reduction, and CcmF/CcmH-dependent heme ligation. Lineage-dependent CcmI/CycH-family factors can support the ligation stage. Sec-dependent apocytochrome export, upstream DsbD electron delivery, and heme biosynthesis are external dependencies.

### Provisional Biological Outline

- Bacterial cytochrome c maturation system I
  - 1. heme trafficking and holo-CcmE formation
  - CcmABCDE heme trafficking and holo-CcmE formation
    - 1. ATP-dependent holo-CcmE processing
    - CcmAB energy-coupling subcomplex
      - CcmA ATPase (molecular player: CcmA cytochrome-c-maturation ATPase family; activity or role: ATP hydrolysis activity)
      - CcmB membrane subunit (molecular player: CcmB cytochrome-c-maturation family)
    - 2. heme transfer and covalent loading of CcmE
    - CcmCDE holo-CcmE-forming assembly
      - CcmC heme-handling subunit (molecular player: CcmC cytochrome-c-biogenesis family; activity or role: heme binding)
      - CcmD accessory subunit (molecular player: CcmD cytochrome-c-maturation family)
      - CcmE heme chaperone (molecular player: CcmE heme-chaperone family; activity or role: heme binding)
  - 2. reductive preparation of apocytochrome CXXCH motifs
  - CcmG/CcmH apocytochrome thiol-redox preparation
    - CcmG thiol-disulfide oxidoreductase (molecular player: CcmG/DsbE thioredoxin family; activity or role: disulfide oxidoreductase activity)
    - CcmH redox component (molecular player: CcmH cytochrome-c-maturation family)
  - 3. covalent heme ligation to reduced apocytochrome
  - CcmF/CcmH heme-ligation machinery
    - 1. holocytochrome-c synthase complex
    - CcmF/CcmH holocytochrome-c synthase complex
      - CcmF/CcmH holocytochrome-c synthase activity (molecular player: bacterial CcmF/CcmH heme-ligation complex; activity or role: holocytochrome-c synthase activity)
    - 2. lineage-dependent maturation accessory
    - CcmI/CycH-family accessory factor
      - CycH-family maturation accessory (molecular player: CycH cytochrome-c-maturation family)

### Known Relationships Among Steps

- CcmABCDE heme trafficking and holo-CcmE formation feeds into CcmF/CcmH heme-ligation machinery
- CcmG/CcmH apocytochrome thiol-redox preparation feeds into CcmF/CcmH heme-ligation machinery
- CcmAB energy-coupling subcomplex feeds into CcmCDE holo-CcmE-forming assembly
- CcmC heme-handling subunit feeds into CcmE heme chaperone
- CcmD accessory subunit feeds into CcmE heme chaperone
- CcmG thiol-disulfide oxidoreductase feeds into CcmH redox component
- CcmI/CycH-family accessory factor part of CcmF/CcmH holocytochrome-c synthase complex

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

# Species-Aware Review: Cytochrome *c* Maturation System I in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Bacterial cytochrome *c* maturation (Ccm) System I — covalent heme attachment to exported apo-*c*-cytochromes
**Commissioned bucket:** kegg:ppu02010 "ABC transporters" (207 candidate genes)
**Iteration:** 3 of 3 (final)

---

## 1. Executive summary

*P. putida* KT2440 encodes a **complete, canonical, single-operon cytochrome *c* maturation System I** (`ccmABCDEFGH` + `ccmI/cycH`) at a contiguous chromosomal locus, **PP_4327 → PP_5748 → PP_4320**. **Every step of the generic module is COVERED** by a dedicated gene with matching domain architecture, membrane topology, and intact catalytic residues.

The most important curation message is a **framing error, not a biology gap**: the commissioned candidate list (KEGG map ppu02010, "ABC transporters") **does not contain the Ccm machinery at all**. The bucket resolved to ABC transporters only because CcmA/CcmB constitute an ABC-family energy module; the 207 listed genes are unrelated importers/exporters (Met, Zn, taurine, dipeptide, LPS, etc.). The module must be **re-anchored to the PP_4320–PP_4327 operon**.

Two annotation problems require action: (i) KEGG maps **both** PP_4320 and PP_5748 to `ccmH` (K02200), but domains show they are functionally distinct — **PP_5748 = redox CcmH**, **PP_4320 = CcmI/CycH chaperone** — so the apparent `ccmI` (K02201) "gap" is a **false negative**; (ii) several ppu display names are imprecise (e.g., PP_4321 CcmG labelled "holocytochrome c synthetase subunit"). All evidence for KT2440 is **homology/prediction-tier** (no strain-specific *ccm* mutant published), but functional need is strong: KT2440's respiratory chain uses a *cbb₃*-type cytochrome *c* oxidase and other *c*-type cytochromes.

---

## 2. Target-organism pathway definition

**Process included:** Post-translational, periplasmic **covalent attachment of heme *b* to the CXXCH motif of Sec-exported apo-*c*-cytochromes**, via System I: (a) ATP-energized heme handling and holo-CcmE formation (CcmABCDE), (b) thiol-reductive preparation of the apocytochrome CXXCH cysteines (CcmG + CcmH, fed by DsbD), and (c) covalent heme ligation by the CcmF/CcmH synthase, assisted by the CcmI/CycH apocytochrome chaperone.

**Kept separate (neighboring processes / boundary):**
- **KEGG ppu02010 "ABC transporters"** and **ppu00860 "Porphyrin/heme biosynthesis"** — external dependencies, not part of the module.
- **Sec translocon (SecYEG)** and **DsbD** — upstream boundary dependencies (heme substrate is made by the porphyrin pathway; apoprotein export by Sec; reducing equivalents by DsbD → CcmG).
- **Cytochrome *c* oxidase / oxidative-phosphorylation maps (ppu00190)** — these are *clients* of Ccm, not part of it.
- **System II (Ccs/Res, `ccsBA`)** — an *alternative* maturation system; **absent** in KT2440 (see §5), so it must not be conflated.

**Alternate names/definitions:** "Cytochrome *c* biogenesis pathway I"; genes historically named *helABCDX* (Rhodobacter), *cycHJKL*/*ccl* (Ccl1=CcmF, Ccl2=CcmH), *dsbE*=*ccmG*, *cycH*=*ccmI*. KEGG module M00259; GO:0017004 (cytochrome complex assembly) / GO:0018063 (cytochrome *c*-heme linkage).

---

## 3. Expected step model → gene mapping

| Module step (generic) | Expected player | KT2440 gene | KO | Call |
|---|---|---|---|---|
| CcmA ATPase (energy) | CcmA ATPase | **PP_4327** | K02193 | covered |
| CcmB membrane subunit | CcmB | **PP_4326** | K02194 | covered |
| CcmC heme-handling | CcmC | **PP_4325** | K02195 | covered |
| CcmD accessory | CcmD | **PP_4324** | K02196 | covered |
| CcmE heme chaperone | CcmE | **PP_4323** | K02197 | covered |
| CcmG thiol-disulfide oxidoreductase | CcmG/DsbE | **PP_4321** | K02199 | covered |
| CcmH redox component | CcmH | **PP_5748** | K02200 | covered |
| CcmF/CcmH holocytochrome-*c* synthase | CcmF | **PP_4322** | K02198 | covered |
| CcmI/CycH accessory | CcmI/CycH | **PP_4320** | (K02201, mis-mapped to K02200) | covered |
| *External:* DsbD electron delivery | DsbD | **PP_4235 / PP_0561** | K04084 | candidate_uncertain (paralog ambiguity) |
| *External:* Sec export; heme biosynthesis | — | assumed present | — | out of scope |

**All nine internal module slots are covered.** The operon is fully contiguous (complement strand, ~4.91 Mb): PP_4327→PP_4326→PP_4325→PP_4324→PP_4323→PP_4322→PP_4321→**PP_5748**→PP_4320, i.e. `ccmA-B-C-D-E-F-G-H-I`. PP_5748's out-of-sequence tag is a re-annotation artifact (small ORF inserted in its canonical *ccmH* slot between *ccmG* and *ccmI*), **not** genomic separation.

---

## 4. Candidate genes and evidence

Evidence tier for all target-organism assignments: **homology/prediction** (UniProt "Inferred from homology" or "Predicted"; no published KT2440 *ccm* knockout). Domain and motif calls are from InterPro/Pfam + sequence inspection; mechanistic roles transferred from *E. coli* and *Rhodobacter capsulatus* (transfer **strong** given operon synteny and conserved catalytic residues).

- **PP_4327 CcmA** (Q88EX5, 210 aa) — Cytochrome *c* biogenesis ATP-binding export protein, **EC 7.6.2.5**, inner membrane. ABC ATPase energizing heme handling. *Caveat:* EC/ABC annotation is why the gene family enters the ppu02010 bucket — do not treat as a solute transporter.
- **PP_4326 CcmB** (Q88EX6, 222 aa, 6 TM) — Heme exporter B membrane subunit. Covered.
- **PP_4325 CcmC** (Q88EX7, 255 aa, 6 TM) — Heme-handling subunit (WWD/heme-binding, Cyt_c biogenesis family). Covered.
- **PP_4324 CcmD** (Q88EX8, 58 aa, 1 TM) — Small accessory subunit; short length is normal for CcmD (not a fragment). Covered.
- **PP_4323 CcmE** (Q88EX9, 151 aa) — OB-fold heme chaperone (Pfam PF03100); **conserved heme-binding His in HxxxY (HDEKY@124)**, equivalent to *E. coli* His130. Covered; functional.
- **PP_4322 CcmF** (Q88EY0, 662 aa, 15 TM) — Holocytochrome-*c* synthetase (Pfam PF01578 + PF16327); periplasmic **WWD-region tryptophans (WWA@233, WWF@244)** and multiple heme-coordinating His. Covered; functional.
- **PP_4321 CcmG/DsbE** (Q88EY1, 178 aa) — Periplasmic thioredoxin-fold disulfide oxidoreductase (Pfam PF08534 Redoxin, DsbE family IPR004799); **redox CXXC = CPSC@73**. Covered. *Caveat:* ppu/UniProt display name "holocytochrome c synthetase subunit" is imprecise — it is CcmG/DsbE.
- **PP_5748 CcmH (redox)** (A0A140FWM4, 158 aa, 1 TM) — CcmH/CycL/Ccl2/NrfF N-terminal redox domain (Pfam PF03918, IPR005616); **redox CXXC = CPKC@45**. Covered. *Caveat:* co-mapped with PP_4320 to K02200; this is the genuine redox CcmH.
- **PP_4320 CcmI/CycH** (A0A140FWM3, 398 aa, 2 TM) — CcmI (IPR017560) + Ig_CycH (PF23892) + TPR_CcmH_CycH (PF23914) + TPR repeats; **no CXXC** → apocytochrome-binding chaperone, **not** a redox subunit. Covered as the CcmI/CycH accessory. *Caveat:* mis-mapped to K02200; should be K02201.
- **PP_4235 / PP_0561 DsbD** (Q88F64 / Q88QD3, 571/590 aa, 8 TM, **EC 1.8.1.8**) — Two paralogous thiol:disulfide interchange proteins delivering electrons to CcmG. **External** to the module. *Caveat:* which paralog services Ccm is unresolved by homology.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **Bucket/candidate-list mismatch (module_needs_revision at the metadata level).** None of the 207 ppu02010 candidates are Ccm genes; the *ccm* operon is absent from the supplied list. The module was mis-seeded from an ABC-transporter overview map. **Re-anchor to PP_4320–PP_4327.**
2. **K02200 double-mapping (annotation over-propagation).** KEGG assigns *ccmH* to both PP_4320 and PP_5748. Domain evidence splits them cleanly: PP_5748 = redox CcmH (CXXC), PP_4320 = CcmI/CycH (TPR, no CXXC). **Reassign PP_4320 → ccmI/CycH (K02201).**
3. **False `ccmI` (K02201) gap.** `link/ppu K02201` returns nothing, implying a gap; in reality CcmI/CycH is present as PP_4320. **Mark covered, not gap.**
4. **System II is genuinely absent (clean boundary).** No `ccsA/resC` (K07399) or fused `ccsBA` (K12265) in ppu. The single K07400 ("ccsB/resB") hit, **PP_2378, is NfuA** (Fe/S biogenesis; Pfam PF01521/PF01106) — a spurious cross-map. So the CcmF/CcmH ligation step is **not** replaced by a lineage alternative → covered, not candidate_uncertain.
5. **Imprecise ppu/UniProt display names** (PP_4321 "holocytochrome c synthetase subunit"; PP_4325 "protoheme IX reservoir complex subunit"). Cosmetic; the KO/domain assignments are correct.
6. **DsbD paralog ambiguity** (external): PP_4235 vs PP_0561 — flag candidate_uncertain but out-of-module.

---

## 6. Module and GO-curation recommendations

**Step status calls:**
- **covered:** CcmA (PP_4327), CcmB (PP_4326), CcmC (PP_4325), CcmD (PP_4324), CcmE (PP_4323), CcmF (PP_4322), CcmG (PP_4321), CcmH-redox (PP_5748), CcmI/CycH (PP_4320) — the entire internal module.
- **candidate_uncertain:** DsbD electron delivery (PP_4235 / PP_0561) — external boundary, paralog choice unresolved.
- **not_expected_in_target_taxon:** System-II (Ccs) alternative — correctly absent; do not open a Ccs module for KT2440.
- **module_needs_revision (metadata seeding):** replace the ppu02010 ABC-transporter candidate set with the PP_4320–PP_4327 operon.

**GO/annotation actions:**
- Assign **GO:0017004** (cytochrome complex assembly) and **GO:0018063** (cytochrome-*c*-heme linkage) to the operon members; **GO:0020037** heme binding to CcmC/CcmE/CcmF; **GO:0015232** heme transmembrane transport to CcmABC.
- Correct KO mapping: PP_4320 → K02201 (ccmI/cycH); retain PP_5748 → K02200 (ccmH).
- No new GO term requests appear necessary; existing terms cover all steps. The **generic module boundary is correct** for this organism (single-operon System I); only the *candidate-gene seeding* was wrong.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_4320** — resolve KO/name conflict (CcmI/CycH vs CcmH); confirm reassignment to K02201.
2. **PP_5748** — confirm redox CcmH identity and in-operon position; reconcile the non-sequential locus tag.
3. **PP_4235 and PP_0561** — determine which DsbD paralog feeds the Ccm/CcmG branch vs general periplasmic disulfide/DsbC recycling.
4. *(Optional)* **PP_4321** — update display name from "holocytochrome c synthetase subunit" to CcmG/DsbE.

---

## 8. Key references & evidence provenance

- **Databases (direct for KT2440):** KEGG GENES/REST (`link/ppu`, gene coordinates) — KO→locus mapping and operon synteny; UniProt UP000000556 (Q88EX5–Q88EY1, A0A140FWM3, A0A140FWM4, Q88F64, Q88QD3) — protein names, TM topology, EC; InterPro/Pfam domains and sequence motifs (CXXC, HxxxY, WWD).
- **Sanders C, Deshmukh M, Astor H, Kranz RG, Daldal F (2005)** *J Bacteriol* 187:4245–56. **PMID 15937187.** CcmI/CycH is an apo-Cyt *c* chaperone distinct from the CcmF–CcmH(Ccl2) redox/ligation components — supports the PP_4320 (CcmI) vs PP_5748 (CcmH) split. *Transfer from R. capsulatus: strong (domain-conserved).* 
- **Fernández-Piñar R, et al. (2008)** *J Bacteriol* 190:7666–74. **PMID 18820016.** KT2440 respiratory chain includes a *cbb₃* cytochrome *c* oxidase and cytochrome-*c*-related proteins under RoxS/RoxR — establishes functional need for *c*-type cytochrome maturation. *Direct for KT2440.*
- **Grether J, et al. (2025)** *Microb Cell Fact.* **PMID 39827133.** Oxygen-sensitive *cbb₃*-type cytochrome *c* oxidase promoter in KT2440 — corroborates *c*-type oxidase expression. *Direct for KT2440.*

**Uncertainty statement:** No published *P. putida* KT2440 *ccm* deletion/biochemical study was found; all gene-level assignments are homology/prediction-tier. Confidence is nonetheless high because (i) the operon is syntenic and complete, (ii) catalytic residues (CcmE HxxxY, CcmF WWD/His, CcmG/CcmH CXXC) are intact, and (iii) the strain demonstrably makes *c*-type cytochromes. The one true biological ambiguity is external (which DsbD paralog services Ccm), resolvable by a targeted PP_4235/PP_0561 knockout + cytochrome *c* heme-staining assay.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_cytochrome_c_maturation_system_i__ppu02010-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_cytochrome_c_maturation_system_i__ppu02010-deep-research-openscientist_artifacts/final_report.pdf)