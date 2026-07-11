---
title: "PSEPK ppu00561 Glycerolipid metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00561: Glycerolipid metabolism

- Module seed: `glycerolipid_metabolism_boundary`
- Candidate genes from membership table: 12
- Primary bucket genes: 12
- Existing review files: 12
- Curated review files: 12
- Existing Asta research files: 12

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
| [x] | `PP_0058` | PP_0058 | Q88RS1 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | 1-acyl-sn-glycerol-3-phosphate acyltransferase |
| [x] | `plsY` | PP_0391 | Q88QU5 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerol-3-phosphate acyltransferase (Acyl-PO4 G3P acyltransferase) (Acyl-phosphate--glycerol-3-phosphate acyltransferas |
| [x] | `glpK` | PP_1075 | Q88NX8 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerol kinase (EC 2.7.1.30) (ATP:glycerol 3-phosphotransferase) (Glycerokinase) (GK) |
| [x] | `plsB` | PP_1520 | Q88MQ0 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerol-3-phosphate acyltransferase (GPAT) (EC 2.3.1.15) |
| [x] | `dgkA-I` | PP_1636 | Q88MD7 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Diacylglycerol kinase (EC 2.7.1.107) |
| [x] | `plsC` | PP_1844 | Q88LT3 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | 1-acyl-sn-glycerol-3-phosphate acyltransferase (EC 2.3.1.51) |
| [x] | `plsX` | PP_1912 | Q88LL8 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Phosphate acyltransferase (EC 2.3.1.274) (Acyl-ACP phosphotransacylase) (Acyl-[acyl-carrier-protein]--phosphate acyltran |
| [x] | `calA` | PP_2426 | Q88K65 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Coniferyl alcohol dehydrogenase (EC 1.1.1.194) |
| [x] | `dgkA-II` | PP_2973 | Q88IM6 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Diacylglycerol kinase (EC 2.7.1.107) |
| [x] | `garK` | PP_3178 | Q88I24 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Glycerate kinase (EC 2.7.1.165) |
| [x] | `ttuD` | PP_4300 | Q88F00 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Hydroxypyruvate reductase (EC 1.1.1.81) |
| [x] | `lip` | PP_4854 | Q88DH1 | kegg:ppu00561 | PRESENT | CURATED | PRESENT | Lipase |

## Notes

Generated UTC: 2026-07-08T10:46:44.545375+00:00

Completed first-pass curation on 2026-07-08 UTC.

Main conclusions:

- PSEPK `ppu00561` is a broad glycerolipid/glycerophospholipid boundary map,
  not a single linear route.
- Core membrane-lipid precursor assembly is represented by `plsX`, `plsY`,
  `plsB`, `plsC`, `PP_0058`, `dgkA-I`, and `dgkA-II`.
- `plsX` supplies acyl-phosphate for the PlsY route; the review adds a `NEW`
  phospholipid biosynthetic process lead from the UniProt record because the
  local GOA table omitted that process row.
- `glpK` supplies glycerol/glycerol-3-phosphate context but remains reviewed as
  glycerol catabolism rather than a dedicated membrane-lipid enzyme.
- `calA`, `garK`, `ttuD`, and `lip` are boundary/side nodes. `lip` remains an
  unreviewed alpha/beta hydrolase candidate with no GOA terms or assigned core
  function pending substrate evidence.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon glycerolipid_metabolism_boundary`
  and `just module-pathway-deep-research-falcon glycerolipid_metabolism_boundary ppu00561 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/glycerolipid_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__glycerolipid_metabolism_boundary__ppu00561-deep-research-falcon.md`.
