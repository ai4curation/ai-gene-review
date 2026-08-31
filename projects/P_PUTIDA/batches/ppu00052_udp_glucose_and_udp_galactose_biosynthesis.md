---
title: "PSEPK UDP-glucose and UDP-galactose biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00052: UDP-glucose and UDP-galactose biosynthesis

- Module seed: `udp_glucose_and_udp_galactose_biosynthesis`
- Candidate genes from membership table: 8
- Primary bucket genes: 7
- Existing review files: 8
- Curated or explicitly annotation-free review files: 8
- Selected/boundary gene OpenScientist research files: 6

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected and boundary genes.
- [x] Curate each selected and boundary gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_0501` | PP_0501 | Q88QJ1 | kegg:ppu00052 | PRESENT | NO_ANNOTATIONS | PRESENT | NAD-dependent epimerase/dehydratase family protein |
| [x] | `glk` | PP_1011 | Q88P42 | kegg:ppu00052 | PRESENT | CURATED | N/A (excluded) | Glucokinase (EC 2.7.1.2) (Glucose kinase) |
| [x] | `PP_1165` | PP_1165 | Q88NP2 | kegg:ppu00052 | PRESENT | CURATED | N/A (excluded) | Aldose 1-epimerase |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | phosphomannomutase (EC 5.4.2.8) |
| [x] | `galE` | PP_3129 | Q88I72 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | UDP-glucose 4-epimerase (EC 5.1.3.2) |
| [x] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |
| [x] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |

## Curated Boundary

The KEGG `ppu00052` bucket is broader than a coherent PSEPK galactose pathway.
This batch models the reusable three-operation route from glucose 6-phosphate
to UDP-glucose and UDP-galactose. Downstream polysaccharide synthesis is a
consumer of these activated sugars, not part of this module.

| Gene | Decision | Rationale |
|---|---|---|
| `pgm` | selected | Specific phosphoglucomutase candidate for glucose 1-phosphate formation. |
| `algC` | selected alternative | Reviewed bifunctional phosphomannomutase/phosphoglucomutase; in-vivo division of flux with Pgm remains unresolved. |
| `galU` | selected | Forms UDP-glucose from glucose 1-phosphate and UTP. |
| `galE` | selected | Reversibly interconverts UDP-glucose and UDP-galactose. |
| `cpsG` | boundary review | Current evidence supports phosphomannomutase, not the glucose-phosphate reaction. |
| `glk` | excluded | Produces glucose 6-phosphate upstream and belongs to glucose uptake/central carbon metabolism. |
| `PP_0501` | boundary/conflict review | Divergent nucleotide-sugar epimerase/dehydratase with unresolved substrate; do not double-count as GalE. |
| `PP_1165` | excluded | Aldose 1-epimerase acts on free sugars, outside this nucleotide-sugar module. |

## Curation Questions

- Does direct KT2440 evidence distinguish Pgm from AlgC as the dominant source
  of glucose 1-phosphate for UDP-glucose production?
- Does PSEPK GalE support UDP-glucose/UDP-galactose interconversion only, or is
  the TreeGrafter Leloir-catabolism annotation justified in an organism lacking
  a clearly defined complete Leloir uptake/catabolic module here?
- The GalE UniProt entry maps to a PANTHER subfamily whose official label is
  UDP-arabinose 4-epimerase 1. Until that evolutionary placement is resolved,
  the module uses the exact UniProt exemplar and intentionally asserts no
  PANTHER identifier for GalE.

## Main Conclusions

- The three module operations are covered: Pgm is the dedicated primary
  glucose-1-phosphate candidate, AlgC is a bifunctional alternative, GalU forms
  UDP-glucose, and GalE supplies UDP-galactose reversibly.
- GalE's TreeGrafter annotation to beta-D-galactose catabolism through the
  Leloir pathway is marked over-annotated. KT2440 lacks an established native
  GalK/GalT route; their absence is not a gap in this anabolic module.
- Pgm's TreeGrafter phosphopentomutase and purine-ribonucleoside-salvage rows
  are marked over-annotated because they cross divergent phosphomutase family
  functions.
- CpsG is a mannose-specialized boundary enzyme and is proposed for
  GDP-mannose biosynthesis, not counted as a glucose-phosphate supplier.
- PP_0501 is retained as an unresolved nucleotide-sugar enzyme. Its exact
  substrate requires enzymology; no GalE or deoxy-sugar reaction is asserted.

## Notes

Generated UTC: 2026-08-31T16:15:17.144458+00:00
