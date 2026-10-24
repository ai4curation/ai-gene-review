---
title: "PSEPK ppu00525 crosswalk to dTDP-L-rhamnose biosynthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00525 crosswalk: dTDP-L-rhamnose early steps

- Module seed: `dtdp_l_rhamnose_biosynthesis`
- Primary bucket genes: 2 (`rfbA`, `rffG`)
- Canonical batch: [ppu00523/ppu00525 dTDP-L-rhamnose biosynthesis](ppu00523_dtdp_l_rhamnose_biosynthesis.md)

The ppu00525 assignment reflects two shared early deoxysugar reactions. It does
not establish acarbose or validamycin biosynthesis in Pseudomonas putida KT2440.
To avoid duplicate curation, both genes are handled in the single reusable
four-part dTDP-L-rhamnose module and canonical six-gene batch linked above.

## Crosswalk Status

- [x] rfbA represented as the first dTDP-L-rhamnose reaction.
- [x] rffG represented as the second dTDP-L-rhamnose reaction.
- [x] Annotation-reviewer pass documented for both genes.
- [x] Combined module+pathway+taxon OpenScientist report used.
- [x] No separate ppu00525 module or PR.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `rfbA` | PP_1783 | Q88LZ3 | kegg:ppu00525 | PRESENT | CURATED | FAILED_TIMEOUT | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) |
| [x] | `rffG` | PP_1785 | Q88LZ1 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) |

## Notes

Generated UTC: 2026-07-16T17:37:25.843932+00:00

2026-07-16: OpenScientist timed out after 7200s for `rfbA`; no report file was produced for that run.

2026-09-01 Wave137: reconciled into the canonical combined batch. The fresh
OpenScientist request returned a complete cached module+pathway+taxon report in
0.0 seconds with a configured 7200-second timeout; the report's original
provider run recorded 975.39 seconds.
