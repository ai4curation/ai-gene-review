---
title: "PSEPK ppu00440 Phosphonate and phosphinate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00440: Phosphonate and phosphinate metabolism

- Module seed: `phosphonate_phosphinate_metabolism`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

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
| [x] | `phnX` | PP_2208 | Q88KT1 | kegg:ppu00440 | PRESENT | CURATED | PRESENT | Phosphonoacetaldehyde hydrolase (Phosphonatase) (EC 3.11.1.1) (Phosphonoacetaldehyde phosphonohydrolase) |
| [x] | `phnW` | PP_2209 | Q88KT0 | kegg:ppu00440 | PRESENT | CURATED | PRESENT | 2-aminoethylphosphonate--pyruvate transaminase (EC 2.6.1.37) (2-aminoethylphosphonate aminotransferase) (AEP transaminas |

## Notes

Generated UTC: 2026-07-07T22:23:06.415096+00:00

Completed first-pass curation of `ppu00440` as the compact PhnW/PhnX
2-aminoethylphosphonate catabolic route. `phnW` is the upstream PLP-dependent
AEP:pyruvate transaminase producing phosphonoacetaldehyde; `phnX` is the
downstream Mg(2+)-dependent phosphonoacetaldehyde hydrolase releasing
acetaldehyde and phosphate. The `phnX` review accepts the specific
phosphonoacetaldehyde hydrolase and organic phosphonate catabolism annotations,
keeps Mg(2+) binding and cytosol as non-core context, modifies the
phosphoglycolate phosphatase transfer to the specific PhnX activity, and removes
the unsupported TreeGrafter DNA repair process annotation.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon phosphonate_phosphinate_metabolism`
  and `just module-pathway-deep-research-falcon phosphonate_phosphinate_metabolism ppu00440 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/phosphonate_phosphinate_metabolism-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__phosphonate_phosphinate_metabolism__ppu00440-deep-research-falcon.md`.
