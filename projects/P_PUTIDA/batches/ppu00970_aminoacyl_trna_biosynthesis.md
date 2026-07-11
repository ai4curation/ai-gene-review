---
title: "PSEPK ppu00970 Aminoacyl-tRNA biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00970: Aminoacyl-tRNA biosynthesis

- Module seed: `aminoacyl_trna_biosynthesis`
- Candidate genes from membership table: 27
- Primary bucket genes: 24
- Existing review files: 27
- Curated review files: 27
- Existing Asta research files: 27

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
| [x] | `glyS` | PP_0060 | Q88RR9 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Glycine--tRNA ligase beta subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase beta subunit) (GlyRS) |
| [x] | `glyQ` | PP_0061 | Q88RR8 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Glycine--tRNA ligase alpha subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase alpha subunit) (GlyRS) |
| [x] | `fmt` | PP_0067 | Q88RR2 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Methionyl-tRNA formyltransferase (EC 2.1.2.9) |
| [x] | `tyrS` | PP_0436 | Q88QQ2 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Tyrosine--tRNA ligase (EC 6.1.1.1) (Tyrosyl-tRNA synthetase) (TyrRS) |
| [x] | `selA` | PP_0493 | Q88QJ8 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | L-seryl-tRNA(Sec) selenium transferase (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec)  |
| [x] | `ileS` | PP_0603 | Q88Q92 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Isoleucine--tRNA ligase (EC 6.1.1.5) (Isoleucyl-tRNA synthetase) (IleRS) |
| [x] | `PP_0613` | PP_0613 | Q88Q82 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Amidase family protein |
| [x] | `hisS` | PP_0854 | Q88PJ6 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Histidine--tRNA ligase (EC 6.1.1.21) (Histidyl-tRNA synthetase) (HisRS) |
| [x] | `gatB` | PP_0930 | Q88PC0 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Aspartyl/glutamyl-tRNA(Asn/Gln) amidotransferase subunit B (Asp/Glu-ADT subunit B) (EC 6.3.5.-) |
| [x] | `gatA` | PP_0931 | Q88PB9 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Glutamyl-tRNA(Gln) amidotransferase subunit A (Glu-ADT subunit A) (EC 6.3.5.7) |
| [x] | `gatC` | PP_0932 | Q88PB8 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Aspartyl/glutamyl-tRNA(Asn/Gln) amidotransferase subunit C (Asp/Glu-ADT subunit C) (EC 6.3.5.-) |
| [x] | `valS` | PP_0977 | Q88P76 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Valine--tRNA ligase (EC 6.1.1.9) (Valyl-tRNA synthetase) (ValRS) |
| [x] | `metG` | PP_1097 | Q88NV7 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl-tRNA synthetase) (MetRS) |
| [x] | `proS` | PP_1205 | Q88NK2 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Proline--tRNA ligase (EC 6.1.1.15) (Prolyl-tRNA synthetase) (ProRS) |
| [x] | `aspS` | PP_1213 | Q88NJ4 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Aspartate--tRNA(Asp/Asn) ligase (EC 6.1.1.23) (Aspartyl-tRNA synthetase) (AspRS) (Non-discriminating aspartyl-tRNA synth |
| [x] | `trpS` | PP_1311 | Q88NA1 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Tryptophan--tRNA ligase (EC 6.1.1.2) (Tryptophanyl-tRNA synthetase) (TrpRS) |
| [x] | `lysS` | PP_1496 | Q88MS3 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Lysine--tRNA ligase (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS) |
| [x] | `gltX` | PP_1977 | Q88LF6 | kegg:ppu00860 | PRESENT | CURATED | PRESENT | Glutamate--tRNA ligase (EC 6.1.1.17) (Glutamyl-tRNA synthetase) (GluRS) |
| [x] | `thrS` | PP_2465 | Q88K27 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Threonine--tRNA ligase (EC 6.1.1.3) (Threonyl-tRNA synthetase) (ThrRS) |
| [x] | `pheS` | PP_2469 | Q88K23 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Phenylalanine--tRNA ligase alpha subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase alpha subunit) (PheRS) |
| [x] | `pheT` | PP_2470 | Q88K22 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Phenylalanine--tRNA ligase beta subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase beta subunit) (PheRS) |
| [x] | `glnS` | PP_2904 | Q88IU5 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Glutamine--tRNA ligase (EC 6.1.1.18) (Glutaminyl-tRNA synthetase) (GlnRS) |
| [x] | `cysS` | PP_2905 | Q88IU4 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Cysteine--tRNA ligase (EC 6.1.1.16) (Cysteinyl-tRNA synthetase) (CysRS) |
| [x] | `serS` | PP_4000 | Q88FT2 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Serine--tRNA ligase (EC 6.1.1.11) (Seryl-tRNA synthetase) (SerRS) (Seryl-tRNA(Ser/Sec) synthetase) |
| [x] | `alaS` | PP_4474 | Q88EI8 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Alanine--tRNA ligase (EC 6.1.1.7) (Alanyl-tRNA synthetase) (AlaRS) |
| [x] | `leuS` | PP_4794 | Q88DN1 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Leucine--tRNA ligase (EC 6.1.1.4) (Leucyl-tRNA synthetase) (LeuRS) |
| [x] | `argS` | PP_5089 | Q88CU1 | kegg:ppu00970 | PRESENT | CURATED | PRESENT | Arginine--tRNA ligase (EC 6.1.1.19) (Arginyl-tRNA synthetase) (ArgRS) |

## Notes

Generated UTC: 2026-07-08T17:57:57.518941+00:00

2026-07-11 PDT status sync: `modules/aminoacyl_trna_biosynthesis.yaml` is curated and validates with both module validators. The module treats canonical aminoacyl-tRNA synthetases as the core ppu00970 pathway, with GatCAB indirect Asn/Gln-tRNA formation, aminoacyl-tRNA editing/fidelity, initiator methionyl-tRNA formylation, selenocysteine-tRNA chemistry, and unresolved `PP_0613` amidase-family chemistry kept as boundary or side nodes.

The ppu00970 batch TSV has 27/27 review files, 27/27 curated review YAMLs, and 27/27 Asta reports. All 27 PSEPK review YAMLs validate; 24 emit only the expected warning that annotation reviews do not yet reference available `*-deep-research-asta.md` files.

Real Falcon commands were run:

```bash
just module-deep-research-falcon aminoacyl_trna_biosynthesis
just module-pathway-deep-research-falcon aminoacyl_trna_biosynthesis ppu00970 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/aminoacyl_trna_biosynthesis-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__aminoacyl_trna_biosynthesis__ppu00970-deep-research-falcon.md`
