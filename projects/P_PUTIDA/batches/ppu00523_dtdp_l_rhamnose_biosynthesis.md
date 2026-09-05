---
title: "PSEPK dTDP-L-rhamnose biosynthesis: ppu00523/ppu00525 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK dTDP-L-rhamnose biosynthesis: ppu00523/ppu00525

- Module seed: `dtdp_l_rhamnose_biosynthesis`
- Combined candidate genes: 6
- Primary ppu00523 genes: 4
- Primary ppu00525 genes: 2
- Curated review files: 6

This is the canonical batch page for the focused six-gene curation. KEGG splits
the candidates between broad maps ppu00523 and ppu00525, but they form one
biologically coherent four-reaction dTDP-L-rhamnose route. The two ppu00525
assignments are shared early nucleotide-sugar reactions, not evidence that
KT2440 synthesizes acarbose or validamycin.

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Consult available gene-level research and perform an annotation-reviewer
  pass for every selected gene.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Prepare one Wave137 PR scope for this module/pathway.
- [ ] Shepherd the Wave137 PR through review and CI; do not merge in this wave.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `rmlC` | PP_0265 | Q88R69 | kegg:ppu00523 | PRESENT | CURATED | FAILED_TIMEOUT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `PP_0500` | PP_0500 | Q88QJ2 | kegg:ppu00523 | PRESENT | CURATED (activity and pathway UNDECIDED) | PRESENT | RmlD-family reductase; physiological substrate unresolved |
| [x] | `rfbC` | PP_1782 | Q88LZ4 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `rfbA` | PP_1783 | Q88LZ3 | kegg:ppu00525 | PRESENT | CURATED | FAILED_TIMEOUT | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) |
| [x] | `rfbD` | PP_1784 | Q88LZ2 | kegg:ppu00523 | PRESENT | CURATED | FAILED_TIMEOUT | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) |
| [x] | `rffG` | PP_1785 | Q88LZ1 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) |

## Notes

Generated UTC: 2026-07-16T17:37:22.097822+00:00

2026-07-16: OpenScientist timed out after 7200s for `rfbA`, `rmlC`, and `rfbD`; no report files were produced for those runs.

2026-09-01 Wave137: the module+pathway+taxon OpenScientist request used the
configured 7200-second allowance and returned the existing complete report as a
cache hit (`duration_seconds: 0.0`; the cached report's original provider run
recorded 975.39 seconds). All six reviews received a documented
annotation-reviewer pass. The reusable module has four required reaction parts;
late PSEPK paralogs are exemplars of one family role, not co-required steps.
