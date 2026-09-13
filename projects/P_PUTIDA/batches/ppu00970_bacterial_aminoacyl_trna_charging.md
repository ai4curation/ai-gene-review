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
- Existing review files: 26
- Curated review files: 26
- Selected module proteins: 24
- Selected gene reviews audited in this batch: 24

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
- Asparaginyl-tRNA formation is a route variant: direct AsnRS where present, or
  the two-part indirect route in which a non-discriminating AspRS supplies
  Asp-tRNA(Asn) and GatABC transamidates it. KT2440 has no canonical `asnS`;
  Q88NJ4 AspS and Q88PB9/Q88PC0/Q88PB8 GatABC satisfy the indirect route.
- Glutaminyl-tRNA formation is a route variant: direct GlnRS (`glnS`) or the
  two-part indirect route in which a non-discriminating GluRS supplies
  Glu-tRNA(Gln) and GatABC (`gatA`, `gatB`, `gatC`) transamidates it.
- KT2440 encodes both GlnS and GatABC. Its direct GlnS route is supported;
  use of Q88LF6 GltX on tRNA(Gln) is not established and remains a knowledge
  gap. The experimentally resolved homologous system in Pseudomonas aeruginosa
  uses direct GlnRS charging and discriminating GluRS alongside the required
  indirect AspRS-GatABC Asn route (PMID:14729703).
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
| Direct Asn-tRNA(Asn) route | `asnS` | Not present in KT2440; retained as a reusable bacterial alternative with exact ECOLI P0A8M0 exemplar |
| Indirect Asn-tRNA(Asn) route | `aspS` then `gatA`-`gatB`-`gatC` | Required in KT2440 and covered by exact PSEPK exemplars plus comparative experimental support (PMID:14729703) |
| Direct Gln-tRNA(Gln) route | `glnS` / PP_2904 / Q88IU5 | Covered by the exact reviewed UniProt identity |
| Indirect Gln-tRNA(Gln) route | non-discriminating GluRS then `gatA`-`gatB`-`gatC` | Retained as a reusable bacterial alternative; not assigned to KT2440 because Q88LF6 recognition of tRNA(Gln) is unestablished |

The module is species-neutral and route-complete as a reusable model. The
required PSEPK indirect Asn route and direct Gln route are covered. KT2440
GatABC has predicted dual-substrate transamidation capacity, but no complete
indirect Gln route is asserted because Glu-tRNA(Gln) precursor production by
Q88LF6 has not been established.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all 24 selected PSEPK charging genes.
- [x] Use exact UniProt records plus module-level and taxon-aware primary evidence.
- [x] Apply the annotation-reviewer workflow to every GOA row for all 24 selected genes; retain DRAFT status because most local assignments are rule-based rather than direct KT2440 assays.
- [x] Validate the module and all selected gene reviews.
- [ ] Open and shepherd one wave121 PR through formal review.

2026-09-01: A fresh generic OpenScientist run completed after 1,328 seconds and
is included as `modules/bacterial_aminoacyl_trna_charging-deep-research-openscientist.md`.
No completed module+pathway+taxon OpenScientist report is present in the current
repository or the prior PR history; the KT2440 route decision therefore relies
on exact local records and cached primary evidence, especially PMID:14729703,
rather than claiming a missing report as support.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `glyS` | PP_0060 | Q88RR9 | kegg:ppu00970 | PRESENT | CURATED | module research | Glycine--tRNA ligase beta subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase beta subunit) (GlyRS) |
| [x] | `glyQ` | PP_0061 | Q88RR8 | kegg:ppu00970 | PRESENT | CURATED | module research | Glycine--tRNA ligase alpha subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase alpha subunit) (GlyRS) |
| [ ] | `fmt` | PP_0067 | Q88RR2 | kegg:ppu00970 | PRESENT | CURATED | MISSING | Methionyl-tRNA formyltransferase (EC 2.1.2.9) |
| [x] | `tyrS` | PP_0436 | Q88QQ2 | kegg:ppu00970 | PRESENT | CURATED | module research | Tyrosine--tRNA ligase (EC 6.1.1.1) (Tyrosyl-tRNA synthetase) (TyrRS) |
| [ ] | `selA` | PP_0493 | Q88QJ8 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | L-seryl-tRNA(Sec) selenium transferase (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec)  |
| [x] | `ileS` | PP_0603 | Q88Q92 | kegg:ppu00970 | PRESENT | CURATED | module research | Isoleucine--tRNA ligase (EC 6.1.1.5) (Isoleucyl-tRNA synthetase) (IleRS) |
| [ ] | `PP_0613` | PP_0613 | Q88Q82 | kegg:ppu00970 | MISSING | MISSING | MISSING | Amidase family protein |
| [x] | `hisS` | PP_0854 | Q88PJ6 | kegg:ppu00970 | PRESENT | CURATED | module research | Histidine--tRNA ligase (EC 6.1.1.21) (Histidyl-tRNA synthetase) (HisRS) |
| [x] | `gatB` | PP_0930 | Q88PC0 | kegg:ppu00970 | PRESENT | CURATED | module research | Aspartyl/glutamyl-tRNA(Asn/Gln) amidotransferase subunit B (Asp/Glu-ADT subunit B) (EC 6.3.5.-) |
| [x] | `gatA` | PP_0931 | Q88PB9 | kegg:ppu00970 | PRESENT | CURATED | module research | Glutamyl-tRNA(Gln) amidotransferase subunit A (Glu-ADT subunit A) (EC 6.3.5.7) |
| [x] | `gatC` | PP_0932 | Q88PB8 | kegg:ppu00970 | PRESENT | CURATED | module research | Aspartyl/glutamyl-tRNA(Asn/Gln) amidotransferase subunit C (Asp/Glu-ADT subunit C) (EC 6.3.5.-) |
| [x] | `valS` | PP_0977 | Q88P76 | kegg:ppu00970 | PRESENT | CURATED | module research | Valine--tRNA ligase (EC 6.1.1.9) (Valyl-tRNA synthetase) (ValRS) |
| [x] | `metG` | PP_1097 | Q88NV7 | kegg:ppu00450 | PRESENT | CURATED | module research | Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl-tRNA synthetase) (MetRS) |
| [x] | `proS` | PP_1205 | Q88NK2 | kegg:ppu00970 | PRESENT | CURATED | module research | Proline--tRNA ligase (EC 6.1.1.15) (Prolyl-tRNA synthetase) (ProRS) |
| [x] | `aspS` | PP_1213 | Q88NJ4 | kegg:ppu00970 | PRESENT | CURATED | module research | Aspartate--tRNA(Asp/Asn) ligase (EC 6.1.1.23) (Aspartyl-tRNA synthetase) (AspRS) (Non-discriminating aspartyl-tRNA synth |
| [x] | `trpS` | PP_1311 | Q88NA1 | kegg:ppu00970 | PRESENT | CURATED | module research | Tryptophan--tRNA ligase (EC 6.1.1.2) (Tryptophanyl-tRNA synthetase) (TrpRS) |
| [x] | `lysS` | PP_1496 | Q88MS3 | kegg:ppu00970 | PRESENT | CURATED | module research | Lysine--tRNA ligase (EC 6.1.1.6) (Lysyl-tRNA synthetase) (LysRS) |
| [x] | `gltX` | PP_1977 | Q88LF6 | kegg:ppu00860 | PRESENT | CURATED | module research | Glutamate--tRNA ligase (EC 6.1.1.17) (Glutamyl-tRNA synthetase) (GluRS) |
| [x] | `thrS` | PP_2465 | Q88K27 | kegg:ppu00970 | PRESENT | CURATED | module research | Threonine--tRNA ligase (EC 6.1.1.3) (Threonyl-tRNA synthetase) (ThrRS) |
| [x] | `pheS` | PP_2469 | Q88K23 | kegg:ppu00970 | PRESENT | CURATED | module research | Phenylalanine--tRNA ligase alpha subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase alpha subunit) (PheRS) |
| [x] | `pheT` | PP_2470 | Q88K22 | kegg:ppu00970 | PRESENT | CURATED | module research | Phenylalanine--tRNA ligase beta subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase beta subunit) (PheRS) |
| [x] | `glnS` | PP_2904 | Q88IU5 | kegg:ppu00970 | PRESENT | CURATED | module research | Glutamine--tRNA ligase (EC 6.1.1.18) (Glutaminyl-tRNA synthetase) (GlnRS) |
| [x] | `cysS` | PP_2905 | Q88IU4 | kegg:ppu00970 | PRESENT | CURATED | module research | Cysteine--tRNA ligase (EC 6.1.1.16) (Cysteinyl-tRNA synthetase) (CysRS) |
| [x] | `serS` | PP_4000 | Q88FT2 | kegg:ppu00970 | PRESENT | CURATED | module research | Serine--tRNA ligase (EC 6.1.1.11) (Seryl-tRNA synthetase) (SerRS) (Seryl-tRNA(Ser/Sec) synthetase) |
| [x] | `alaS` | PP_4474 | Q88EI8 | kegg:ppu00970 | PRESENT | CURATED | module research | Alanine--tRNA ligase (EC 6.1.1.7) (Alanyl-tRNA synthetase) (AlaRS) |
| [x] | `leuS` | PP_4794 | Q88DN1 | kegg:ppu00970 | PRESENT | CURATED | module research | Leucine--tRNA ligase (EC 6.1.1.4) (Leucyl-tRNA synthetase) (LeuRS) |
| [x] | `argS` | PP_5089 | Q88CU1 | kegg:ppu00970 | PRESENT | CURATED | module research | Arginine--tRNA ligase (EC 6.1.1.19) (Arginyl-tRNA synthetase) (ArgRS) |

## Notes

The TSV is the machine-readable 27-protein KEGG candidate snapshot. The 24
checked charging genes have row-complete annotation-reviewer audits. `fmt`,
`selA`, and `PP_0613` are retained only to document boundary exclusions and are
not counted as selected module proteins.
