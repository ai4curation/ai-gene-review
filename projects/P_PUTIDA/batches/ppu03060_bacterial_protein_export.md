---
title: "PSEPK ppu03060 Protein export batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03060: Protein export

- Module seed: `bacterial_protein_export`
- Candidate genes from membership table: 19
- Primary bucket genes: 19
- Existing review files: 19
- Curated review files: 19
- Existing Asta research files: 19

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
| [x] | `yidC` | PP_0006 | P0A140 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Membrane protein insertase YidC (Foldase YidC) (Membrane integrase YidC) (Membrane protein YidC) |
| [x] | `secE` | PP_0441 | Q88QP7 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Protein translocase subunit SecE |
| [x] | `secY` | PP_0474 | Q88QL5 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Protein translocase subunit SecY |
| [x] | `lspA` | PP_0604 | Q88Q91 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II) |
| [x] | `yajC` | PP_0834 | Q88PL6 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Sec translocon accessory complex subunit YajC |
| [x] | `secD` | PP_0835 | Q88PL5 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Protein translocase subunit SecD |
| [x] | `secF` | PP_0836 | Q88PL4 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Protein-export membrane protein SecF |
| [x] | `tatC-I` | PP_1039 | Q88P14 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Sec-independent protein translocase protein TatC |
| [x] | `tatB-I` | PP_1040 | Q88P13 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Sec-independent protein translocase TatB |
| [x] | `tatA-I` | PP_1041 | Q88P12 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Sec-independent protein translocase protein TatA |
| [x] | `secA` | PP_1345 | Q88N69 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Protein translocase subunit SecA (EC 7.4.2.8) |
| [x] | `lepB` | PP_1432 | Q88MY6 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Signal peptidase I (EC 3.4.21.89) |
| [x] | `ffh` | PP_1461 | Q88MV7 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four homolog) |
| [x] | `tatA-II` | PP_5016 | Q88D13 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Sec-independent protein translocase protein TatA |
| [x] | `tatB` | PP_5017 | Q88D12 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Sec-independent protein translocase protein TatB |
| [x] | `tatC-II` | PP_5018 | Q88D11 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Sec-independent protein translocase protein TatC |
| [x] | `secB` | PP_5053 | Q88CX7 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Protein-export protein SecB |
| [x] | `ftsY` | PP_5111 | Q88CR9 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Signal recognition particle receptor FtsY (SRP receptor) (EC 3.6.5.4) |
| [x] | `secG` | PP_5706 | A0A140FWQ9 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Protein-export membrane protein SecG |

## Notes

Generated UTC: 2026-07-09T11:08:56.686526+00:00

2026-07-09 PDT checkpoint: 19/19 review folders, 19/19 curated review YAMLs,
and 19/19 Asta gene-level reports are present. The module was created and
validated as `modules/bacterial_protein_export.yaml`.

2026-07-11 PDT status sync: re-ran both module validators for
`modules/bacterial_protein_export.yaml`; `linkml-validate -C ModuleReview`
and the module term-label validator both pass. The Falcon boxes remain
unchecked because the real Edison requests below failed with HTTP 402 and no
Falcon report files were written.

Falcon retrieval was attempted with the real commands:

```bash
just module-deep-research-falcon bacterial_protein_export
just module-pathway-deep-research-falcon bacterial_protein_export ppu03060 PSEPK
```

Both failed immediately at Edison task creation with HTTP 402, so no Falcon
output artifacts were written.
