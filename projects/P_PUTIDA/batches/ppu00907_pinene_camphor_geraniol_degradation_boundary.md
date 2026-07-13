---
title: "PSEPK ppu00907 Pinene, camphor and geraniol degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00907: Pinene, camphor and geraniol degradation

- Module seed: `pinene_camphor_geraniol_degradation_boundary`
- Candidate genes from membership table: 7
- Primary bucket genes: 2
- Existing review files: 7
- Curated review files: 7
- Existing Asta research files: 7

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `fadA__Q88L84` | PP_2051 | Q88L84 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `fadA__Q88L01` | PP_2137 | Q88L01 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex sub |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `PP_3394` | PP_3394 | Q88HG4 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | 3-hydroxy-3-methylglutaryl-CoA lyase |
| [x] | `mvaB` | PP_3540 | Q88H25 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | hydroxymethylglutaryl-CoA lyase (EC 4.1.3.4) |

## Notes

Generated UTC: 2026-07-08T16:24:12.148961+00:00

2026-07-11 PDT status sync: `modules/pinene_camphor_geraniol_degradation_boundary.yaml`
is curated and validates with both module validators. The two primary
ppu00907 genes (`PP_3394`, `mvaB`) validate, and the module records this KEGG
bucket as HMG-CoA lyase and CoA-thioester spillover context rather than a
complete pinene, camphor, or geraniol degradation pathway.

Real Falcon commands were run:

```bash
just module-deep-research-falcon pinene_camphor_geraniol_degradation_boundary
just module-pathway-deep-research-falcon pinene_camphor_geraniol_degradation_boundary ppu00907 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no
Falcon reports were written. Expected output paths remain:

- `modules/pinene_camphor_geraniol_degradation_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__pinene_camphor_geraniol_degradation_boundary__ppu00907-deep-research-falcon.md`
