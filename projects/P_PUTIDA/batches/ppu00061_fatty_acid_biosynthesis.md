---
title: "PSEPK ppu00061 Fatty acid biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00061: Fatty acid biosynthesis

- Module seed: `fatty_acid_biosynthesis`
- Candidate genes from membership table: 19
- Primary bucket genes: 7
- Existing review files: 19
- Curated review files: 19
- Existing Asta research files: 19

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `accC` | PP_0558 | Q88QD6 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) |
| [x] | `accB` | PP_0559 | Q88QD5 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Biotin carboxyl carrier protein of acetyl-CoA carboxylase |
| [x] | `PP_0581` | PP_0581 | Q88QB3 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-(Acyl-carrier-protein) reductase |
| [x] | `fabZ` | PP_1602 | Q88MG9 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ (EC 4.2.1.59) ((3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydr |
| [x] | `accA` | PP_1607 | Q88MG4 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A carboxylase carboxyl transferase subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyl |
| [x] | `PP_1852` | PP_1852 | Q88LS6 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific) (EC 1.3.1.10) |
| [x] | `fabD` | PP_1913 | Q88LL7 | kegg:ppu00074 | PRESENT | CURATED | PRESENT | Malonyl CoA-acyl carrier protein transacylase (EC 2.3.1.39) |
| [x] | `fabG` | PP_1914 | Q88LL6 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] reductase (EC 1.1.1.100) |
| [x] | `fabF` | PP_1916 | Q88LL4 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) |
| [x] | `accD` | PP_1996 | Q88LD9 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltr |
| [x] | `PP_2540` | PP_2540 | Q88JV7 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | Oxidoreductase, short-chain dehydrogenase/reductase family |
| [x] | `PP_2783` | PP_2783 | Q88J66 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase (EC 1.3.1.58) (Biphenyl-2,3-dihydro-2,3-diol dehydrogenase) |
| [x] | `PP_3303` | PP_3303 | Q88HQ0 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) |
| [x] | `fabA` | PP_4174 | Q88FC4 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | 3-hydroxydecanoyl-[acyl-carrier-protein] dehydratase (EC 4.2.1.59) (3-hydroxyacyl-[acyl-carrier-protein] dehydratase Fab |
| [x] | `fabB` | PP_4175 | Q88FC3 | kegg:ppu00780 | PRESENT | CURATED | PRESENT | 3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41) (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-A |
| [x] | `PP_4379` | PP_4379 | Q88ES4 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Beta-ketoacyl-acyl-carrier-protein synthase I (EC 2.3.1.180) |
| [x] | `fadD-I` | PP_4549 | Q88EB7 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) |
| [x] | `fadD-II` | PP_4550 | Q88EB6 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) |
| [x] | `fabV` | PP_4635 | Q88E33 | kegg:ppu00061 | PRESENT | CURATED | PRESENT | Enoyl-[acyl-carrier-protein] reductase [NADH] (ENR) (EC 1.3.1.9) |

## Notes

Generated UTC: 2026-07-07T05:11:20.427707+00:00

Falcon-backed curation summary:

- Core ACC/FAS-II route: `accA`, `accB`, `accC`, `accD`, `fabD`, `fabG`,
  `fabZ`, `fabA`, `fabB`, `fabF`, `PP_4379`, and `fabV`.
- Module lesson: pseudomonad initiation should allow `fabB` as a possible
  FabH-independent initiator; `PP_4379` remains a KAS III candidate but is not
  assumed to be the sole required initiator.
- Boundary or uncertain candidates: `PP_0581`, `PP_1852`, and `PP_2540`.
  `PP_1852` was downgraded after Falcon because `fabV` is the best core ENR.
- Excluded from core FAS-II: `fadD-I` and `fadD-II` belong with
  beta-oxidation/acyl-CoA activation, and `PP_2783` belongs with aromatic
  catabolism.
