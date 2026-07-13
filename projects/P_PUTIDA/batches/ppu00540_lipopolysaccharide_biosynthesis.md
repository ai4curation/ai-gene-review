---
title: "PSEPK ppu00540 Lipopolysaccharide biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00540: Lipopolysaccharide biosynthesis

- Module seed: `lipopolysaccharide_biosynthesis`
- Candidate genes from membership table: 20
- Primary bucket genes: 20
- Existing review files: 20
- Curated review files: 20
- Existing Asta research files: 20

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
| [x] | `PP_0024` | PP_0024 | Q88RV5 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Membrane-associated metal-dependent hydrolase |
| [x] | `PP_0063` | PP_0063 | Q88RR6 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipid A biosynthesis lauroyl acyltransferase |
| [x] | `waaF` | PP_0341 | Q88QZ3 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | lipopolysaccharide heptosyltransferase II (EC 2.4.99.24) |
| [x] | `waaC` | PP_0342 | Q88QZ2 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipopolysaccharide heptosyltransferase 1 (EC 2.4.99.23) (ADP-heptose:lipopolysaccharide heptosyltransferase I) |
| [x] | `waaG` | PP_0343 | Q88QZ1 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipopolysaccharide glucosyltransferase I (EC 2.4.1.58) |
| [x] | `waaP` | PP_0344 | Q88QZ0 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipopolysaccharide core heptose(I) kinase (EC 2.7.1.-) |
| [x] | `pagL-I` | PP_0737 | Q88PW1 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipid A deacylase (EC 3.1.1.77) (LPS 3-O-deacylase) (Outer membrane enzyme) |
| [x] | `lpxC` | PP_1343 | Q88N71 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | UDP-3-O-acyl-N-acetylglucosamine deacetylase (UDP-3-O-acyl-GlcNAc deacetylase) (EC 3.5.1.108) (UDP-3-O-[R-3-hydroxymyris |
| [x] | `lpxD` | PP_1601 | Q88MH0 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | UDP-3-O-acylglucosamine N-acyltransferase (EC 2.3.1.191) |
| [x] | `lpxA` | PP_1603 | Q88MG8 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine O-acyltransferase (UDP-N-acetylglucosamine acyltransferase) (EC 2.3 |
| [x] | `lpxB` | PP_1604 | Q88MG7 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipid-A-disaccharide synthase (EC 2.4.1.182) |
| [x] | `htrB` | PP_1735 | Q88M40 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipid A biosynthesis acyltransferase (EC 2.3.1.241) (Kdo(2)-lipid IV(A) acyltransferase) |
| [x] | `lpxK` | PP_1900 | Q88LM9 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Tetraacyldisaccharide 4'-kinase (EC 2.7.1.130) (Lipid A 4'-kinase) |
| [x] | `lpxOA` | PP_2423 | Q88K68 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Fe(2+)/alpha-ketoglutarate-dependent dioxygenase (EC 1.14.11.-) |
| [x] | `yijP` | PP_2579 | Q88JS0 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Phosphoethanolamine transferase CptA |
| [x] | `lpxH` | PP_2902 | Q88IU7 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | UDP-2,3-diacylglucosamine hydrolase (EC 3.6.1.54) (UDP-2,3-diacylglucosamine diphosphatase) |
| [x] | `pagL-II` | PP_3154 | Q88I47 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Lipid A deacylase (EC 3.1.1.77) (LPS 3-O-deacylase) (Outer membrane enzyme) |
| [x] | `PP_4570` | PP_4570 | Q88E96 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Aspartyl/asparaginy/proline hydroxylase domain-containing protein |
| [x] | `PP_4592` | PP_4592 | Q88E74 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | Metal dependent hydrolase |
| [x] | `waaA` | PP_4928 | Q88D99 | kegg:ppu00540 | PRESENT | CURATED | PRESENT | 3-deoxy-D-manno-octulosonic acid transferase (Kdo transferase) (EC 2.4.99.12) (Lipid IV(A) 3-deoxy-D-manno-octulosonic a |

## Notes

Generated UTC: 2026-07-08T00:44:39.442481+00:00

Completed first-pass curation on 2026-07-07 PDT / 2026-07-08 UTC.

Validation and rendering completed:

- `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/lipopolysaccharide_biosynthesis.yaml`
- `uv run python -m ai_gene_review.validation.module_validator modules/lipopolysaccharide_biosynthesis.yaml`
- `just validate PSEPK <gene>` for all 20 genes in this batch.
- `just render PSEPK <gene>` for all 20 genes in this batch.

Main curation conclusions:

- Treat KEGG `ppu00540` as a combined LPS/lipid A module rather than one
  linear pathway. The batch separates lipid IVA/lipid A biosynthesis,
  Kdo2-lipid A formation, LPS core oligosaccharide assembly, and lipid A/LPS
  remodeling side nodes.
- Core lipid A precursor enzymes: `lpxA`, `lpxC`, `lpxD`, `lpxH`, `lpxB`, and
  `lpxK`.
- Kdo2-lipid A/core bridge and late acylation: `waaA`, `htrB`/`lpxL`, and
  candidate lipid A acyltransferase `PP_0063`.
- LPS core assembly: `waaC`, `waaF`, `waaG`, and `waaP`.
- Remodeling or unresolved side nodes: `pagL-I`, `pagL-II`, `yijP`, `PP_0024`,
  `PP_4592`, `lpxOA`, and `PP_4570`.
- Broad membrane, cofactor, hydrolase, glycosyltransferase, transferase, and
  acyltransferase parent terms were retained as non-core or marked
  over-annotated when a more specific enzyme term was available. `lpxK`'s LPS
  core-region process annotation was marked over-annotated in favor of lipid A
  biosynthesis. New first-pass UniProt-backed annotations were added for
  `PP_0063`, `lpxOA`, and `PP_4570` because the fetched GOA block did not carry
  the relevant acyltransferase/dioxygenase terms.

- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon lipopolysaccharide_biosynthesis` and
  `just module-pathway-deep-research-falcon lipopolysaccharide_biosynthesis ppu00540 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/lipopolysaccharide_biosynthesis-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__lipopolysaccharide_biosynthesis__ppu00540-deep-research-falcon.md`.
