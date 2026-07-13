---
title: "PSEPK ppu00290 Valine, leucine and isoleucine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00290: Valine, leucine and isoleucine biosynthesis

- Module seed: `branched_chain_amino_acid_biosynthesis`
- Candidate genes from membership table: 18
- Primary bucket genes: 11
- Existing review files: 18
- Curated review files: 18
- Existing Asta research files: 18

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `leuA` | PP_1025 | Q88P28 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | 2-isopropylmalate synthase (EC 2.3.3.13) (Alpha-IPM synthase) (Alpha-isopropylmalate synthase) |
| [x] | `PP_1157` | PP_1157 | Q877U6 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase |
| [x] | `PP_1394` | PP_1394 | Q88N22 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase, large subunit |
| [x] | `alaA` | PP_1872 | Q88LQ7 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2) |
| [x] | `leuC` | PP_1985 | Q88LE8 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 3-isopropylmalate dehydratase large subunit (EC 4.2.1.33) (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) |
| [x] | `leuD` | PP_1986 | Q88LE7 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 3-isopropylmalate dehydratase small subunit (EC 4.2.1.33) (Alpha-IPM isomerase) (IPMI) (Isopropylmalate isomerase) |
| [x] | `leuB` | PP_1988 | Q88LE5 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 3-isopropylmalate dehydrogenase (EC 1.1.1.85) (3-IPM-DH) (Beta-IPM dehydrogenase) (IMDH) |
| [x] | `PP_2930` | PP_2930 | Q88IR9 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | L-serine ammonia-lyase (EC 4.3.1.17) |
| [x] | `PP_3191` | PP_3191 | Q88I11 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Threonine ammonia-lyase / dehydratase (EC 4.3.1.19) |
| [x] | `ilvA-I` | PP_3446 | Q88HB4 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) |
| [x] | `ilvE` | PP_3511 | Q88H54 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) |
| [x] | `PP_4430` | PP_4430 | Q88EM4 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Threonine dehydratase (EC 4.3.1.19) |
| [x] | `ldh` | PP_4617 | Q88E51 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Leucine dehydrogenase (EC 1.4.1.9) |
| [x] | `ilvC` | PP_4678 | Q88DZ0 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86) (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta- |
| [x] | `ilvH` | PP_4679 | Q88DY9 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) |
| [x] | `ilvI` | PP_4680 | Q88DY8 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | Acetolactate synthase (EC 2.2.1.6) |
| [x] | `ilvD` | PP_5128 | Q88CQ2 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) |
| [x] | `ilvA-II` | PP_5149 | Q88CN1 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | L-threonine dehydratase (EC 4.3.1.19) (Threonine deaminase) |

## Workflow Notes

- Species-neutral module created and validated:
  `modules/branched_chain_amino_acid_biosynthesis.yaml`.
- All 18 KEGG `ppu00290` membership genes have review folders, Asta reports,
  curated YAML reviews, and rendered gene pages.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon branched_chain_amino_acid_biosynthesis` and
  `just module-pathway-deep-research-falcon branched_chain_amino_acid_biosynthesis ppu00290 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/branched_chain_amino_acid_biosynthesis-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__branched_chain_amino_acid_biosynthesis__ppu00290-deep-research-falcon.md`.
- Validation passed for the module and all 18 candidate gene reviews. Remaining
  full-batch warnings are pre-existing Asta-citation warnings on older
  cross-bucket reviews; the new leucine-branch reviews validate cleanly.

## Curation Notes

- Strict branched-chain amino-acid biosynthesis centers on AHAS
  (`ilvI`/`ilvH`, with PP_1157/PP_1394 as side AHAS-like candidates), `ilvC`,
  `ilvD`, `ilvE`, and the leucine branch `leuA`/`leuC`/`leuD`/`leuB`.
- Threonine dehydratase paralogs (`ilvA-I`, `ilvA-II`, PP_3191, PP_4430) are
  best treated as isoleucine-precursor and threonine-catabolism boundary
  context until direct paralog-specific evidence resolves their main flux role.
- `PP_2930` is serine ammonia-lyase side context; `alaA` and `ldh` are
  broader aminotransferase/dehydrogenase boundary nodes in the KEGG map rather
  than strict committed BCAA biosynthesis steps.
- `GO:0009097` is obsolete. Authored first-pass L-isoleucine biosynthesis terms
  should use `GO:1901705`; machine-sourced GOA IDs and provenance text were
  preserved where appropriate.

## Notes

Generated UTC: 2026-07-07T19:09:13.074728+00:00
