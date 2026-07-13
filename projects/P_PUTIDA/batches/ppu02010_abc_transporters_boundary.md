---
title: "PSEPK ppu02010 ABC transporters batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02010: ABC transporters

- Module seed: `abc_transporters_boundary`
- Candidate genes from membership table: 207
- Primary bucket genes: 151
- Existing review files: 207
- Curated review files: 207
- Existing Asta research files: 207

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_0076` | PP_0076 | Q88RQ3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Choline betaine-binding protein |
| [x] | `metQ` | PP_0112 | Q88RL7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Methionine ABC transporter, periplasmic binding protein |
| [x] | `metI` | PP_0113 | Q88RL6 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Methionine ABC transporter, permease protein |
| [x] | `metN1` | PP_0114 | Q88RL5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Methionine import ATP-binding protein MetN 1 (EC 7.4.2.11) |
| [x] | `znuB` | PP_0117 | Q88RL2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | High-affinity zinc uptake system membrane protein ZnuB |
| [x] | `znuC` | PP_0118 | Q88RL1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Zinc import ATP-binding protein ZnuC (EC 7.2.2.20) |
| [x] | `PP_0120` | PP_0120 | Q88RK9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | High-affinity zinc uptake system protein ZnuA |
| [x] | `PP_0140` | PP_0140 | Q88RI9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Mce/MlaD domain-containing protein |
| [x] | `PP_0141` | PP_0141 | Q88RI8 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, ATP-binding protein |
| [x] | `PP_0142` | PP_0142 | Q88RI7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, permease protein |
| [x] | `paxB` | PP_0167 | Q88RG3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Toxin secretion ATP-binding protein |
| [x] | `PP_0170` | PP_0170 | Q88RG0 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ABC transporter, periplasmic binding protein |
| [x] | `PP_0171` | PP_0171 | Q88RF9 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ABC transporter, ATP-binding protein |
| [x] | `PP_0172` | PP_0172 | Q88RF8 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ABC transporter, permease protein |
| [x] | `PP_0207` | PP_0207 | Q88RC5 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_0208` | PP_0208 | Q88RC4 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Nitrate ABC transporter, permease protein |
| [x] | `tauB-I` | PP_0209 | Q88RC3 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | ATP-binding taurine transporter subunit (EC 3.6.3.36) |
| [x] | `metP` | PP_0219 | Q88RB4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | L,D-methionine D-methionine ABC transporter-permease subunit |
| [x] | `metN2` | PP_0220 | Q88RB3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Methionine import ATP-binding protein MetN 2 (EC 7.4.2.11) |
| [x] | `PP_0221` | PP_0221 | Q88RB2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Methionine ABC transporter periplasmic-binding lipoprotein (MetQ-like protein) |
| [x] | `sctC` | PP_0225 | Q88RA8 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Sulfur compound ABC transporter-ATP-binding subunit |
| [x] | `sctS` | PP_0226 | Q88RA7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Sulfur compound ABC transporter-permease subunit |
| [x] | `fliY` | PP_0227 | Q88RA6 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Periplasmic cystine-binding protein |
| [x] | `tauC` | PP_0231 | Q88RA2 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Taurine ABC transporter permease subunit (EC 3.6.3.36) |
| [x] | `tauB` | PP_0232 | Q88RA1 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Taurine import ATP-binding protein TauB (EC 7.6.2.7) |
| [x] | `tauA` | PP_0233 | Q88RA0 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Taurine ABC transporter periplasmic binding subunit |
| [x] | `ssuA` | PP_0237 | Q88R96 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `ssuC` | PP_0239 | Q88R94 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Aliphatic sulfonate ABC transporter-permease subunit / transport of isethionate |
| [x] | `ssuB` | PP_0240 | Q88R93 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Aliphatic sulfonates import ATP-binding protein SsuB (EC 7.6.2.14) |
| [x] | `PP_0280` | PP_0280 | Q88R54 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Arginine ABC transporter permease protein ArtM |
| [x] | `PP_0281` | PP_0281 | Q88R53 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Amino acid ABC transporter, permease protein |
| [x] | `artJ` | PP_0282 | Q88R52 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | L-arginine ABC transporter-periplasmic binding subunit (EC 3.6.3.21) |
| [x] | `aotP` | PP_0283 | Q88R51 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Arginine/ornithine transport ATP-binding protein AotP |
| [x] | `cbcV` | PP_0294 | Q88R40 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Choline / betaine / carnitine ABC transporter-ATP binding subunit (EC 3.6.3.32) |
| [x] | `cbcW` | PP_0295 | Q88R39 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Choline / betaine / carnitine ABC transporter-membrane subunit (EC 3.6.3.32) |
| [x] | `cbcX` | PP_0296 | Q88R38 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Choline / betaine / carnitine ABC transporter-substrate binding protein (EC 3.6.3.32) |
| [x] | `caiX` | PP_0304 | Q88R30 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Carnitine uptake ABC transporter, periplasmic component |
| [x] | `PP_0524` | PP_0524 | Q88QG9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Periplasmic cobalamin-binding protein HutB |
| [x] | `PP_0615` | PP_0615 | Q88Q80 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_0616` | PP_0616 | Q88Q79 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP binding protein |
| [x] | `PP_0617` | PP_0617 | Q88Q78 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_0618` | PP_0618 | Q88Q77 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_0619` | PP_0619 | Q88Q76 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein |
| [x] | `PP_0804` | PP_0804 | Q88PP4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Protein secretion ABC efflux system, permease and ATP-binding protein |
| [x] | `ptxB` | PP_0824 | Q88PM6 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphonate transport system-binding protein |
| [x] | `phnC` | PP_0825 | Q88PM5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphonates import ATP-binding protein PhnC (EC 7.3.2.2) |
| [x] | `phnE` | PP_0826 | Q88PM4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphonate ABC transporter, permease protein |
| [x] | `ptxC` | PP_0827 | Q88PM3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphonate transport system permease protein PtxC |
| [x] | `yehX` | PP_0868 | Q88PI2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Quaternary amine transport ATP-binding protein (EC 7.6.2.9) |
| [x] | `yehW` | PP_0869 | Q88PI1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Osmoprotectant ABC transporter permease subunit |
| [x] | `PP_0870` | PP_0870 | Q88PI0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glycine betaine/carnitine/choline ABC transporter, periplasmic binding protein |
| [x] | `PP_0871` | PP_0871 | Q88PH9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glycine betaine/carnitine/choline ABC transporter, permease protein |
| [x] | `potF-I` | PP_0873 | Q88PH7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Putrescine-binding periplasmic protein |
| [x] | `dppF` | PP_0878 | Q88PH2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC-type dipeptide transporter (EC 7.4.2.9) |
| [x] | `dppD` | PP_0879 | Q88PH1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC-type dipeptide transporter (EC 7.4.2.9) |
| [x] | `dppC` | PP_0880 | Q88PH0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-putative membrane subunit (EC 3.6.3.23) |
| [x] | `dppB` | PP_0881 | Q88PG9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-putative membrane subunit (EC 3.6.3.23) |
| [x] | `dppA-I` | PP_0882 | Q88PG8 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) |
| [x] | `dppA-II` | PP_0884 | Q88PG6 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) |
| [x] | `dppA-III` | PP_0885 | Q88PG5 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Dipeptide ABC transporter-periplasmic binding protein (EC 3.6.3.23) |
| [x] | `lptB` | PP_0953 | Q88P99 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Lipopolysaccharide export system ATP-binding protein LptB |
| [x] | `mlaF` | PP_0958 | Q88P94 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Intermembrane phospholipid transport system ATP-binding protein MlaF |
| [x] | `mlaE` | PP_0959 | Q88P93 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Intermembrane phospholipid transport system permease protein MlaE |
| [x] | `mlaD` | PP_0960 | Q88P92 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phospholipid ABC transporter binding protein |
| [x] | `ttg2D` | PP_0961 | Q88P91 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Toluene tolerance protein |
| [x] | `ttg2E` | PP_0962 | Q88P90 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Toluene-tolerance protein |
| [x] | `PP_0982` | PP_0982 | Q88P71 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Lipopolysaccharide export system permease protein LptF |
| [x] | `PP_0983` | PP_0983 | Q88P70 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | LPS export ABC transporter permease LptG |
| [x] | `gtsA` | PP_1015 | Q88P38 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Mannose/glucose ABC transporter, glucose-binding periplasmic protein |
| [x] | `gtsB` | PP_1016 | Q88P37 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Mannose/glucose ABC transporter, permease protein |
| [x] | `gtsC` | PP_1017 | Q88P36 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Mannose/glucose ABC transporter, permease protein |
| [x] | `gtsD` | PP_1018 | Q88P35 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Maltose import ATP-binding protein YcjV (EC 7.5.2.1) |
| [x] | `gltL` | PP_1068 | Q88NY5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glutamate / aspartate ABC transporter-ATP binding subunit (EC 3.6.3.21) |
| [x] | `gltK` | PP_1069 | Q88NY4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glutamate/aspartate import permease protein GltK |
| [x] | `gltJ` | PP_1070 | Q88NY3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glutamate / aspartate ABC transporter-permease subunit (EC 3.6.3.21) |
| [x] | `gltI` | PP_1071 | Q88NY2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glutamate / aspartate ABC transporter-periplasmic binding protein (EC 3.6.3.21) |
| [x] | `PP_1078` | PP_1078 | Q88NX5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, ATP-binding protein |
| [x] | `livF-I` | PP_1137 | Q88NR8 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport ATP-binding protein |
| [x] | `livG` | PP_1138 | Q88NR7 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched chain amino acid transporter-ATP binding subunit |
| [x] | `livM` | PP_1139 | Q88NR6 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched chain amino acid transporter-permease subunit |
| [x] | `livH` | PP_1140 | Q88NR5 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched chain amino acid transporter-permease subunit |
| [x] | `livK` | PP_1141 | Q88NR4 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acids ABC transporter-periplasmic leucine binding subunit |
| [x] | `yhdW` | PP_1297 | Q88NB5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Amino-acid ABC transporter-binding protein YhdW |
| [x] | `yhdX` | PP_1298 | Q88NB4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Amino acid ABC transporter-permease subunit |
| [x] | `yhdY` | PP_1299 | Q88NB3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Amino acid ABC transporter-membrane subunit |
| [x] | `yhdZ` | PP_1300 | Q88NB2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Amino acid ABC transporter-ATP-binding subunit |
| [x] | `betX` | PP_1741 | Q88M34 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Choline / betaine / carnitine ABC transporter-substrate binding protein BetX (EC 3.6.3.32) |
| [x] | `PP_1778` | PP_1778 | Q88LZ8 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Transport permease protein |
| [x] | `PP_1779` | PP_1779 | Q88LZ7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Lipopolysaccharide ABC export system, ATP-binding protein |
| [x] | `lolC` | PP_2154 | Q88KY5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | LolC |
| [x] | `lolD` | PP_2155 | Q88KY4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Lipoprotein-releasing system ATP-binding protein LolD (EC 7.6.2.-) |
| [x] | `lolE` | PP_2156 | Q88KY3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Lipoprotein releasing system, permease protein |
| [x] | `PP_2195` | PP_2195 | Q88KU4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Putrescine-binding periplasmic protein |
| [x] | `PP_2240` | PP_2240 | Q88KQ0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC efflux transporter, permease/ATP-binding protein |
| [x] | `PP_2260` | PP_2260 | Q88KN0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glycerol-phosphate ABC transporter, ATP-binding protein |
| [x] | `PP_2261` | PP_2261 | Q88KM9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Sugar ABC transporter, ATP-binding protein |
| [x] | `PP_2262` | PP_2262 | Q88KM8 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Sugar ABC transporter, permease protein |
| [x] | `PP_2263` | PP_2263 | Q88KM7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Sugar ABC transporter, permease protein |
| [x] | `PP_2264` | PP_2264 | Q88KM6 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Sugar ABC transporter, periplasmic sugar-binding protein |
| [x] | `rbsB` | PP_2454 | Q88K38 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Ribose ABC transporter, periplasmic ribose-binding subunit |
| [x] | `rbsA-I` | PP_2455 | Q88K37 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Ribose ABC transporter-ATP-binding subunit (EC 3.6.3.17) |
| [x] | `rbsC` | PP_2456 | Q88K36 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | D-ribose ABC transporter-permease subunit (EC 3.6.3.17) |
| [x] | `rbsD` | PP_2459 | Q88K33 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | D-ribose pyranase (EC 5.4.99.62) |
| [x] | `aprDA` | PP_2560 | Q88JT7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Alkaline protease secretion transporter ATP-binding protein |
| [x] | `PP_2595` | PP_2595 | Q88JQ4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, permease/ATP-binding protein |
| [x] | `PP_2596` | PP_2596 | Q88JQ3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, permease/ATP-binding protein |
| [x] | `PP_2628` | PP_2628 | Q88JM1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Uncharacterized ABC transporter ATP-binding protein HI_1051 |
| [x] | `pstS` | PP_2656 | Q88JJ3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate-binding protein PstS |
| [x] | `pstC` | PP_2657 | Q88JJ2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate transport system permease protein |
| [x] | `pstA` | PP_2658 | Q88JJ1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate transport system permease protein PstA |
| [x] | `pstB1` | PP_2659 | Q88JJ0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate import ATP-binding protein PstB 1 (EC 7.3.2.1) (ABC phosphate transporter 1) (Phosphate-transporting ATPase 1) |
| [x] | `PP_2748` | PP_2748 | Q88JA1 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_2749` | PP_2749 | Q88JA0 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2750` | PP_2750 | Q88J99 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2751` | PP_2751 | Q88J98 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Leucine-binding protein domain-containing protein |
| [x] | `PP_2752` | PP_2752 | Q88J97 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Leucine-binding protein domain-containing protein |
| [x] | `PP_2753` | PP_2753 | Q88J96 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_2757` | PP_2757 | Q88J92 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Sugar-binding protein |
| [x] | `PP_2758` | PP_2758 | Q88J91 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Ribose ABC transporter, periplasmic ribose-binding protein |
| [x] | `rbsA` | PP_2759 | Q88J90 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Ribose import ATP-binding protein RbsA (EC 7.5.2.7) |
| [x] | `PP_2760` | PP_2760 | Q88J89 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Ribose transport permease protein |
| [x] | `PP_2761` | PP_2761 | Q88J88 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Ribose ABC transporter, permease protein |
| [x] | `PP_2767` | PP_2767 | Q88J82 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, ATP-binding protein |
| [x] | `PP_2768` | PP_2768 | Q88J81 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2769` | PP_2769 | Q88J80 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, permease protein |
| [x] | `PP_2770` | PP_2770 | Q88J79 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Leucine-binding protein domain-containing protein |
| [x] | `opuA` | PP_2774 | Q88J75 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glycine betaine ABC transporter, ATPase/permease fusion protein |
| [x] | `PP_2775` | PP_2775 | Q88J74 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glycine betaine/L-proline ABC transporter, periplasmic component |
| [x] | `PP_3076` | PP_3076 | Q88IC3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter permease protein |
| [x] | `PP_3077` | PP_3077 | Q88IC2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Oligopeptide transport system permease protein YejB |
| [x] | `PP_3078` | PP_3078 | Q88IC1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, periplasmic binding protein |
| [x] | `potF-II` | PP_3147 | Q88I54 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Putrescine-binding periplasmic protein |
| [x] | `PP_3217` | PP_3217 | Q88HY6 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_3228` | PP_3228 | Q88HX5 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_3229` | PP_3229 | Q88HX4 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `nikA` | PP_3342 | Q88HL4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Nickel ABC transporter periplasmic binding protein (EC 3.6.3.24) |
| [x] | `nikB` | PP_3343 | Q88HL3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Nickel ABC transporter permease subunit (EC 3.6.3.24) |
| [x] | `nikC` | PP_3344 | Q88HL2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Nickel ABC transporter permease subunit (EC 3.6.3.24) |
| [x] | `nikD` | PP_3345 | Q88HL1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Nickel import ATP-binding protein NikD (EC 7.2.2.11) |
| [x] | `nikE` | PP_3346 | Q88HL0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Nickel import ATP-binding protein NikE (EC 7.2.2.11) |
| [x] | `PP_3528` | PP_3528 | Q88H37 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Putative aliphatic sulfonates-binding protein |
| [x] | `PP_3558` | PP_3558 | Q88H07 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Amino acid transporter, periplasmic amino acid-binding protein |
| [x] | `PP_3559` | PP_3559 | Q88H06 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Glycine betaine ABC transporter (Permease) |
| [x] | `PP_3719` | PP_3719 | Q88GK2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Putrescine-binding periplasmic protein |
| [x] | `PP_3801` | PP_3801 | Q88GC3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | High-affinity zinc uptake system protein ZnuA |
| [x] | `PP_3802` | PP_3802 | Q88GC2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Cation ABC transporter, ATP-binding protein |
| [x] | `PP_3803` | PP_3803 | Q88GC1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Cation ABC transporter, permease protein |
| [x] | `PP_3818` | PP_3818 | Q88GA6 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Periplamic phosphate-binding protein |
| [x] | `modA` | PP_3828 | Q88G97 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Molybdate-binding periplasmic protein |
| [x] | `modB` | PP_3829 | Q88G96 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Molybdenum transport system permease |
| [x] | `modC` | PP_3830 | Q88G95 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Molybdenum import ATP-binding protein ModC (EC 7.3.2.5) |
| [x] | `potF-III` | PP_3845 | Q88G80 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Putrescine-binding periplasmic protein |
| [x] | `PP_4146` | PP_4146 | Q88FF1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Peptide ABC transporter, periplamic peptide-binding protein |
| [x] | `yejA` | PP_4147 | Q88FF0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Microcin C transporter-periplasmic binding protein |
| [x] | `PP_4148` | PP_4148 | Q88FE9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Oligopeptide transport system permease protein YejB |
| [x] | `PP_4149` | PP_4149 | Q88FE8 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Inner membrane ABC transporter permease protein |
| [x] | `yejF` | PP_4150 | Q88FE7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC-type dipeptide transporter (EC 7.4.2.9) |
| [x] | `pvdT` | PP_4210 | Q88F88 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Pyoverdine export ATP-binding/permease protein PvdT (EC 7.6.2.-) |
| [x] | `pvdE` | PP_4216 | Q88F82 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Pyoverdine ABC export system, fused ATPase and permease components |
| [x] | `sbp-I` | PP_4305 | Q88EZ5 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate ABC transporter |
| [x] | `ccmD` | PP_4324 | Q88EX8 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Heme exporter protein D |
| [x] | `ccmC` | PP_4325 | Q88EX7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Heme exporter protein C (Cytochrome c-type biogenesis protein) |
| [x] | `ccmB` | PP_4326 | Q88EX6 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Heme exporter protein B |
| [x] | `ccmA` | PP_4327 | Q88EX5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Cytochrome c biogenesis ATP-binding export protein CcmA (EC 7.6.2.5) (Heme exporter protein A) |
| [x] | `hisP` | PP_4483 | Q88EI0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Histidine lysine / arginine / ornithine ABC transporter-ATP binding subunit (EC 3.6.3.21) |
| [x] | `hisM` | PP_4484 | Q88EH9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Histidine/lysine/arginine/ornithine transport system permease protein HisM |
| [x] | `hisQ` | PP_4485 | Q88EH8 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Histidine / lysine / arginine / ornithine ABC transporter-permease subunit (EC 3.6.3.21) |
| [x] | `argT` | PP_4486 | Q88EH7 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Lysine / arginine / ornithine ABC transporter-periplasmic binding protein (EC 3.6.3.21) |
| [x] | `PP_4542` | PP_4542 | Q88EC4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, ATP-binding protein/permease protein |
| [x] | `urtA` | PP_4841 | Q88DI4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Urea ABC transporter, periplasmic protein |
| [x] | `urtB` | PP_4842 | Q88DI3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Urea ABC transporter |
| [x] | `urtC` | PP_4843 | Q88DI2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Urea ABC transporter, permease protein |
| [x] | `urtD` | PP_4844 | Q88DI1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Urea ABC transporter, ATP-binding protein |
| [x] | `urtE` | PP_4845 | Q88DI0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Urea ABC transporter, ATP-binding protein |
| [x] | `livF-II` | PP_4863 | Q88DG2 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport ATP-binding protein |
| [x] | `braF` | PP_4864 | Q88DG1 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport ATP-binding protein BraF |
| [x] | `braE` | PP_4865 | Q88DG0 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport system permease protein BraE |
| [x] | `braD` | PP_4866 | Q88DF9 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | High-affinity branched-chain amino acid transport system permease protein BraD |
| [x] | `PP_4867` | PP_4867 | Q88DF8 | kegg:ppu02024 | PRESENT | CURATED | PRESENT | Branched-chain amino acid ABC transporter, periplasmic amino acid-binding protein (BraC-like) |
| [x] | `PP_4881` | PP_4881 | Q88DE5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Iron ABC transporter, periplasmic iron-binding protein |
| [x] | `PP_4882` | PP_4882 | Q88DE4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Iron ABC transporter, permease protein |
| [x] | `cyaB` | PP_4927 | Q88DA0 | kegg:ppu03070 | PRESENT | CURATED | PRESENT | Cyclolysin secretion/processing ATP-binding protein CyaB (EC 3.4.22.-) |
| [x] | `msbA` | PP_4935 | Q88D92 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ATP-dependent lipid A-core flippase (EC 7.5.2.6) (Lipid A export ATP-binding/permease protein MsbA) |
| [x] | `ftsX` | PP_5109 | Q88CS1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Cell division protein FtsX |
| [x] | `ftsE` | PP_5110 | Q88CS0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Cell division ATP-binding protein FtsE |
| [x] | `PP_5135` | PP_5135 | Q88CP5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, periplasmic binding protein |
| [x] | `PP_5136` | PP_5136 | Q88CP4 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | ABC transporter, permease protein |
| [x] | `fbpC` | PP_5137 | Q88CP3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Ferric iron ABC transporter, ATP-binding protein |
| [x] | `PP_5157` | PP_5157 | Q88CM3 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Solute-binding protein family 3/N-terminal domain-containing protein |
| [x] | `plpB` | PP_5165 | Q88CL5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | NLPA lipoprotein |
| [x] | `cysA` | PP_5168 | Q88CL2 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate/thiosulfate import ATP-binding protein CysA (EC 7.3.2.3) (Sulfate-transporting ATPase) |
| [x] | `cysW` | PP_5169 | Q88CL1 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate transport system permease protein CysW |
| [x] | `cysU` | PP_5170 | Q88CL0 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate transport system permease protein CysT |
| [x] | `sbp-II` | PP_5171 | Q88CK9 | kegg:ppu00920 | PRESENT | CURATED | PRESENT | Sulfate ABC transporter |
| [x] | `spuH` | PP_5177 | Q88CK3 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Putrescine transport system permease protein PotI |
| [x] | `spuG` | PP_5178 | Q88CK2 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Spermidine/putrescine ABC transporter-inner membrane subunit |
| [x] | `spuF` | PP_5179 | Q88CK1 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Spermidine/putrescine import ATP-binding protein PotA (EC 7.6.2.11) |
| [x] | `spuE` | PP_5180 | Q88CK0 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Spermidine/putrescine ABC transporter-periplasmic subunit |
| [x] | `spuD` | PP_5181 | Q88CJ9 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Spermidine/putrescine ABC transporter-periplasmic subunit |
| [x] | `PP_5195` | PP_5195 | Q88CI6 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Iron ABC transporter, permease protein |
| [x] | `fbpA` | PP_5196 | Q88CI5 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Iron(III) iron ABC transporter, periplasmic iron-binding protein |
| [x] | `dppA-IV` | PP_5283 | Q88C98 | kegg:ppu02030 | PRESENT | CURATED | PRESENT | Periplasmic dipeptide transport protein |
| [x] | `pstB2` | PP_5326 | Q88C57 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate import ATP-binding protein PstB 2 (EC 7.3.2.1) (ABC phosphate transporter 2) (Phosphate-transporting ATPase 2) |
| [x] | `PP_5327` | PP_5327 | Q88C56 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate transport system permease protein PstA |
| [x] | `PP_5328` | PP_5328 | Q88C55 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate transport system permease protein |
| [x] | `PP_5329` | PP_5329 | Q88C54 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Phosphate-binding protein |
| [x] | `potF-IV` | PP_5341 | Q88C42 | kegg:ppu02010 | PRESENT | CURATED | PRESENT | Putrescine-binding periplasmic protein |

## Notes

Generated UTC: 2026-07-09T05:51:14.356323+00:00

2026-07-11 PDT status sync: created and validated `modules/abc_transporters_boundary.yaml` as an umbrella boundary/index module for KEGG ppu02010. The module uses the cluster report to keep ppu02010 as 74 locus-neighborhood clusters across unrelated import, export, envelope-biogenesis, and residual ABC-family component contexts rather than one satisfiable pathway.

The ppu02010 batch TSV has 207/207 review files, 207/207 curated review YAMLs, and 207/207 Asta reports. Module validation passed with both module validators. Gene review validation passed for all 207 batch review files with `uv run ai-gene-review validate --verbose --terms --tsv-output reports/validation-psepk-ppu02010.tsv <207 files from the batch TSV>`. The TSV contains 28 non-blocking warnings: 19 `no_deep_research_results` warnings, two `missing_core_functions` warnings, and seven warnings where core-function molecular-function, location, process, or complex terms are not mirrored in `existing_annotations`.

Real Falcon commands were run:

```bash
just module-deep-research-falcon abc_transporters_boundary
just module-pathway-deep-research-falcon abc_transporters_boundary ppu02010 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/abc_transporters_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__abc_transporters_boundary__ppu02010-deep-research-falcon.md`
