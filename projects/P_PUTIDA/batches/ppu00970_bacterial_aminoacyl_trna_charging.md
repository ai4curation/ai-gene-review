---
title: "PSEPK ppu00970 Aminoacyl-tRNA biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00970: Aminoacyl-tRNA biosynthesis

- Module seed: `bacterial_aminoacyl_trna_charging`
- Candidate genes from membership table: 27
- Primary bucket genes: 24
- Existing review files: 8
- Curated review files: 8
- Selected module proteins: 24
- Focused gene reviews curated in this batch: 5

## Curated Boundary

- The reusable module ends when a correctly charged canonical aminoacyl-tRNA
  has been formed. Aminoacyl-tRNA use in initiation, elongation, protein
  formylation, selenocysteine synthesis, and quality-control hydrolysis is
  downstream or adjacent biology.
- Direct charging is organized into class I and class II aaRS groups. Each
  substrate-specific molecular function is attached to a leaf annoton, with
  the exact PSEPK UniProt protein as its representative member.
- Bacterial alpha2-beta2 GlyRS (`glyQ`, `glyS`) and PheRS (`pheS`, `pheT`) are
  represented as complexes with explicit active subunits rather than as four
  independent complete synthetases.
- Glutaminyl-tRNA formation is a route variant: direct GlnRS (`glnS`) or the
  two-part indirect route in which a non-discriminating GluRS supplies
  Glu-tRNA(Gln) and GatABC (`gatA`, `gatB`, `gatC`) transamidates it.
- KT2440 encodes both GlnS and GatABC. Its GlnS route is directly supported;
  use of Q88LF6 GltX on tRNA(Gln) is not established in the exact UniProt
  record and remains a knowledge gap. GatABC also has a strongly supported
  Asp-tRNA(Asn) to Asn-tRNA(Asn) activity, but that additional output is not
  used to erase the requested Gln-route alternative.
- `fmt` is excluded because it formylates already charged initiator
  Met-tRNA(fMet). `selA` is excluded because it converts already charged
  Ser-tRNA(Sec) after SerS aminoacylation.
- `PP_0613` / Q88Q82 is an amidase-family KEGG-map candidate without an aaRS or
  GatABC assignment and is excluded from the module pending contrary evidence.

## Pathway Satisfiability

| Route or group | KT2440 implementation | Decision |
|---|---|---|
| Direct class I aaRS charging | `argS`, `cysS`, `gltX`, `ileS`, `leuS`, `metG`, `trpS`, `tyrS`, `valS` | Covered by exact reviewed UniProt identities |
| Direct class II aaRS charging | `alaS`, `aspS`, `glyQ`-`glyS`, `hisS`, `lysS`, `pheS`-`pheT`, `proS`, `serS`, `thrS` | Covered by exact reviewed UniProt identities |
| Direct Gln-tRNA(Gln) route | `glnS` / PP_2904 / Q88IU5 | Covered; focused review complete |
| Indirect Gln-tRNA(Gln) route | `gltX` then `gatA`-`gatB`-`gatC` | GatABC reaction capacity covered; PSEPK GltX recognition of tRNA(Gln) unresolved |

The module is species-neutral and route-complete as a reusable model. The
PSEPK direct route is covered. The PSEPK indirect Gln route is represented as
documented GatABC biochemical capacity with an explicit strain-specific GltX
substrate-discrimination gap, not asserted as the dominant physiological route.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch focused genes `glnS`, `gltX`, `gatA`, `gatB`, and `gatC`.
- [x] Use exact UniProt records plus module-level and pathway/taxon research for focused genes.
- [x] Curate each focused gene review using the annotation-reviewer workflow.
- [x] Validate module and focused gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

2026-08-11: The first full-timeout generic and module+pathway+taxon
OpenScientist jobs both returned provider HTTP 522 errors during normal status
polling. Full `--timeout 7200` retries were still active at publication time;
no incomplete provider output is included in this batch.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `glyS` | PP_0060 | Q88RR9 | kegg:ppu00970 | MISSING | MISSING | MISSING | Glycine--tRNA ligase beta subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase beta subunit) (GlyRS) |
| [ ] | `glyQ` | PP_0061 | Q88RR8 | kegg:ppu00970 | MISSING | MISSING | MISSING | Glycine--tRNA ligase alpha subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase alpha subunit) (GlyRS) |
| [ ] | `fmt` | PP_0067 | Q88RR2 | kegg:ppu00970 | PRESENT | CURATED | MISSING | Methionyl-tRNA formyltransferase (EC 2.1.2.9) |
| [ ] | `tyrS` | PP_0436 | Q88QQ2 | kegg:ppu00970 | MISSING | MISSING | MISSING | Tyrosine--tRNA ligase (EC 6.1.1.1) (Tyrosyl-tRNA synthetase) (TyrRS) |
| [x] | `selA` | PP_0493 | Q88QJ8 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | L-seryl-tRNA(Sec) selenium transferase (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec)  |
| [ ] | `ileS` | PP_0603 | Q88Q92 | kegg:ppu00970 | MISSING | MISSING | MISSING | Isoleucine--tRNA ligase (EC 6.1.1.5) (Isoleucyl-tRNA synthetase) (IleRS) |
| [ ] | `PP_0613` | PP_0613 | Q88Q82 | kegg:ppu00970 | MISSING | MISSING | MISSING | Amidase family protein |
| [ ] | `hisS` | PP_0854 | Q88PJ6 | kegg:ppu00970 | MISSING | MISSING | MISSING | Histidine--tRNA ligase (EC 6.1.1.21) (Histidyl-tRNA synthetase) (HisRS) |
| [x] | `gatB` | PP_0930 | Q88PC0 | kegg:ppu00970 | PRESENT | CURATED | module research | Aspartyl/glutamyl-tRNA(Asn/Gln) amidotransferase subunit B (Asp/Glu-ADT subunit B) (EC 6.3.5.-) |
| [x] | `gatA` | PP_0931 | Q88PB9 | kegg:ppu00970 | PRESENT | CURATED | module research | Glutamyl-tRNA(Gln) amidotransferase subunit A (Glu-ADT subunit A) (EC 6.3.5.7) |
| [x] | `gatC` | PP_0932 | Q88PB8 | kegg:ppu00970 | PRESENT | CURATED | module research | Aspartyl/glutamyl-tRNA(Asn/Gln) amidotransferase subunit C (Asp/Glu-ADT subunit C) (EC 6.3.5.-) |
| [ ] | `valS` | PP_0977 | Q88P76 | kegg:ppu00970 | MISSING | MISSING | MISSING | Valine--tRNA ligase (EC 6.1.1.9) (Valyl-tRNA synthetase) (ValRS) |
| [ ] | `metG` | PP_1097 | Q88NV7 | kegg:ppu00450 | MISSING | MISSING | MISSING | Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl-tRNA synthetase) (MetRS) |
| [ ] | `proS` | PP_1205 | Q88NK2 | kegg:ppu00970 | MISSING | MISSING | MISSING | Proline--tRNA ligase (EC 6.1.1.15) (Prolyl-tRNA synthetase) (ProRS) |
| [ ] | `aspS` | PP_1213 | Q88NJ4 | kegg:ppu00970 | MISSING | MISSING | MISSING | Aspartate--tRNA(Asp/Asn) ligase (EC 6.1.1.23) (Aspartyl-tRNA synthetase) (AspRS) (Non-discriminating aspartyl-tRNA synth |
| [ ] | `trpS` | PP_1311 | Q88NA1 | kegg:ppu00970 | MISSING | MISSING | MISSING | Tryptophan--tRNA ligase (EC 6.1.1.2) (Tryptophanyl-tRNA synthetase) (TrpRS) |
| [ ] | `lysS` | PP_1496 | Q88MS3 | kegg:ppu00970 | MISSING | MISSING | MISSING | Lysine--tRNA ligase (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS) |
| [x] | `gltX` | PP_1977 | Q88LF6 | kegg:ppu00860 | PRESENT | CURATED | module research | Glutamate--tRNA ligase (EC 6.1.1.17) (Glutamyl-tRNA synthetase) (GluRS) |
| [ ] | `thrS` | PP_2465 | Q88K27 | kegg:ppu00970 | MISSING | MISSING | MISSING | Threonine--tRNA ligase (EC 6.1.1.3) (Threonyl-tRNA synthetase) (ThrRS) |
| [ ] | `pheS` | PP_2469 | Q88K23 | kegg:ppu00970 | MISSING | MISSING | MISSING | Phenylalanine--tRNA ligase alpha subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase alpha subunit) (PheRS) |
| [ ] | `pheT` | PP_2470 | Q88K22 | kegg:ppu00970 | MISSING | MISSING | MISSING | Phenylalanine--tRNA ligase beta subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase beta subunit) (PheRS) |
| [x] | `glnS` | PP_2904 | Q88IU5 | kegg:ppu00970 | PRESENT | CURATED | module research | Glutamine--tRNA ligase (EC 6.1.1.18) (Glutaminyl-tRNA synthetase) (GlnRS) |
| [ ] | `cysS` | PP_2905 | Q88IU4 | kegg:ppu00970 | MISSING | MISSING | MISSING | Cysteine--tRNA ligase (EC 6.1.1.16) (Cysteinyl-tRNA synthetase) (CysRS) |
| [ ] | `serS` | PP_4000 | Q88FT2 | kegg:ppu00970 | PRESENT | CURATED | MISSING | Serine--tRNA ligase (EC 6.1.1.11) (Seryl-tRNA synthetase) (SerRS) (Seryl-tRNA(Ser/Sec) synthetase) |
| [ ] | `alaS` | PP_4474 | Q88EI8 | kegg:ppu00970 | MISSING | MISSING | MISSING | Alanine--tRNA ligase (EC 6.1.1.7) (Alanyl-tRNA synthetase) (AlaRS) |
| [ ] | `leuS` | PP_4794 | Q88DN1 | kegg:ppu00970 | MISSING | MISSING | MISSING | Leucine--tRNA ligase (EC 6.1.1.4) (Leucyl-tRNA synthetase) (LeuRS) |
| [ ] | `argS` | PP_5089 | Q88CU1 | kegg:ppu00970 | MISSING | MISSING | MISSING | Arginine--tRNA ligase (EC 6.1.1.19) (Arginyl-tRNA synthetase) (ArgRS) |

## Notes

The TSV is the machine-readable 27-protein KEGG candidate snapshot. The checked
rows above are the five focused reviews created or completed in this batch;
unchecked aaRS rows remain exact module exemplars grounded by reviewed UniProt
records, while `fmt`, `selA`, and `PP_0613` are retained only to document the
boundary exclusions.
