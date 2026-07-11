---
title: "PSEPK ppu00470 D-Amino acid metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00470: D-Amino acid metabolism

- Module seed: `d_amino_acid_metabolism_boundary`
- Candidate genes from membership table: 21
- Primary bucket genes: 11
- Existing review files: 21
- Curated review files: 21
- Existing Asta research files: 21

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
| [x] | `murI` | PP_0736 | Q88PW2 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Glutamate racemase (EC 5.1.1.3) |
| [x] | `PP_1255` | PP_1255 | Q88NF6 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Cis-4-hydroxy-D-proline oxidase (EC 1.5.1.-) |
| [x] | `PP_1256` | PP_1256 | Q88NF5 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `PP_1257` | PP_1257 | Q88NF4 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | 1-pyrroline-4-hydroxy-2-carboxylate deaminase (EC 3.5.4.22) |
| [x] | `proR` | PP_1258 | Q88NF3 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | 4-hydroxyproline 2-epimerase (4-hydroxyproline epimerase) (4Hyp 2-epimerase) (4HypE) (EC 5.1.1.8) |
| [x] | `murD` | PP_1335 | Q88N78 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC 6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-ala |
| [x] | `ddlB` | PP_1339 | Q88N74 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala ligase B) (D-alanylalanine synthetase B) |
| [x] | `lysA-I` | PP_2077 | Q88L58 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) |
| [x] | `dauA` | PP_2246 | Q88KP4 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Catabolic D-arginine dehydrogenase, FAD-dependent (EC 1.4.99.-) |
| [x] | `ansB` | PP_2453 | Q88K39 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase) (L-asparagine/L-glutamine amidohydrolase) |
| [x] | `PP_2585` | PP_2585 | Q88JR4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `PP_3602` | PP_3602 | Q88GW5 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `alr` | PP_3722 | Q88GJ9 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Broad specificity amino-acid racemase (EC 5.1.1.10) (Broad spectrum racemase) |
| [x] | `dapF__Q88GD4` | PP_3790 | Q88GD4 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) |
| [x] | `PP_4311` | PP_4311 | Q88EY9 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | D-amino acid dehydrogenase 2 small subunit (EC 1.4.99.6) |
| [x] | `ddlA` | PP_4346 | Q88EV6 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A) |
| [x] | `dadA1` | PP_4434 | Q88EM0 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | D-amino acid dehydrogenase 1 (EC 1.4.99.-) |
| [x] | `lysA-II` | PP_5227 | Q88CF4 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) |
| [x] | `dapF__Q88CF3` | PP_5228 | Q88CF3 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) |
| [x] | `dadX` | PP_5269 | Q88CB2 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | Alanine racemase, catabolic (EC 5.1.1.1) |
| [x] | `dadA2` | PP_5270 | Q88CB1 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | D-amino acid dehydrogenase 2 (EC 1.4.99.-) |

## Notes

Generated UTC: 2026-07-07T23:02:26.619050+00:00

Completed first-pass curation on 2026-07-07. Created and validated
`modules/d_amino_acid_metabolism_boundary.yaml`; all 21 KEGG membership genes
have review folders, Asta gene-level retrieval, curated YAML, validation, and
rendered HTML.

Main conclusions:

- `murI`, `murD`, `ddlA`, `ddlB`, `dadX`, and `alr` cover the peptidoglycan
  D-Glu/D-Ala and alanine-racemase chemistry.
- `dadA1`, `dadA2`, `PP_4311`, and `dauA` are D-amino-acid or D-arginine
  dehydrogenase/oxidoreductase context.
- `proR`, `PP_1255`, `PP_1257`, `PP_1256`, `PP_2585`, and `PP_3602` are
  hydroxyproline/dioxovalerate side-route nodes.
- `dapF__Q88GD4`, `dapF__Q88CF3`, `lysA-I`, `lysA-II`, and `ansB` belong to
  diaminopimelate/lysine biosynthesis or asparaginase side context, not a single committed
  D-amino-acid catabolic route.
- First-pass fixes include narrowing broad racemase/ligase/catalytic terms for
  `murI`, `murD`, `PP_1257`, `lysA-II`, and `dadX`; retaining cofactor and
  location terms as non-core for Ddl/Mur/Dad/Lys proteins; and adding
  conservative oxidoreductase annotations for `PP_1255` and `dauA`.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon d_amino_acid_metabolism_boundary` and
  `just module-pathway-deep-research-falcon d_amino_acid_metabolism_boundary ppu00470 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/d_amino_acid_metabolism_boundary-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__d_amino_acid_metabolism_boundary__ppu00470-deep-research-falcon.md`.
