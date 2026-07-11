---
title: "PSEPK ppu00053 Ascorbate and aldarate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00053: Ascorbate and aldarate metabolism

- Module seed: `hexuronate_aldarate_catabolism`
- Candidate genes from membership table: 8
- Primary bucket genes: 4
- Existing review files: 8
- Curated review files: 8
- Existing Asta research files: 8

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
| [x] | `udh` | PP_1171 | Q88NN6 | kegg:ppu00053 | PRESENT | CURATED | PRESENT | Uronate dehydrogenase (EC 1.1.1.203) (D-galacturonate dehydrogenase) (D-glucuronate dehydrogenase) (Hexuronate dehydroge |
| [x] | `PP_1256` | PP_1256 | Q88NF5 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `PP_2585` | PP_2585 | Q88JR4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `udg` | PP_2926 | Q88IS3 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) |
| [x] | `PP_3599` | PP_3599 | Q88GW8 | kegg:ppu00053 | PRESENT | CURATED | PRESENT | 5-dehydro-4-deoxyglucarate dehydratase (EC 4.2.1.41) (5-keto-4-deoxy-glucarate dehydratase) (KDGDH) |
| [x] | `garD` | PP_3601 | Q88GW6 | kegg:ppu00053 | PRESENT | CURATED | PRESENT | Galactarate dehydratase (EC 4.2.1.42) |
| [x] | `PP_3602` | PP_3602 | Q88GW5 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `gudD` | PP_4757 | Q88DR6 | kegg:ppu00053 | PRESENT | CURATED | PRESENT | Glucarate dehydratase (EC 4.2.1.40) |

## Notes

- Falcon promoted `gnl`/PP_1170 as the missing UxuL-family lactonase for the
  free-hexuronate arm. It is not in the KEGG ppu00053 membership table, but it
  was already fetched, Asta-backed, curated, and validated from the ppu00040
  boundary pass.
- Treat `PP_3602` as the strongest local aldarate-pathway KGSADH candidate;
  `PP_1256` and `PP_2585` remain KGSADH-like paralogs without equivalent
  aldarate-cluster context.
- Treat `udg` as a KEGG side-node from UDP-glucuronate/nucleotide-sugar
  biosynthesis, not as a free-hexuronate or aldarate catabolic step.

Generated UTC: 2026-07-07T03:21:57.041750+00:00
