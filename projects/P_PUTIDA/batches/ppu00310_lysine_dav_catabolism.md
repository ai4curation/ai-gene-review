---
title: "PSEPK ppu00310 L-lysine Dav catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [davB, davA, davT, davD]
autolink_gene_symbols: false
---

# PSEPK ppu00310: L-lysine catabolism through 5-aminovalerate

- Module: `lysine_dav_catabolism`
- Pathway context: KEGG `ppu00310` (lysine degradation)
- Pull request: [#2252](https://github.com/ai4curation/ai-gene-review/pull/2252)
- Focused genes: 4
- Broad membership-table candidates: 32

## Boundary

This batch covers the four-reaction Dav route from L-lysine to glutarate:

1. `davB`: L-lysine to 5-aminopentanamide
2. `davA`: 5-aminopentanamide to 5-aminovalerate
3. `davT`: 5-aminovalerate to 5-oxopentanoate
4. `davD`: 5-oxopentanoate to glutarate

The D-lysine/2-aminoadipate route, lysine transport and regulation, and both
downstream glutarate-degradation routes are outside this module. They remain in
the broad TSV for later pathway batches.

## Status

- [x] Fetch focused genes from UniProt and GOA.
- [x] Curate all four gene reviews.
- [x] Create a species-neutral four-part module.
- [x] Attempt OpenScientist gene-level research; DavT and DavD reports
  completed, while the corrected DavA and DavB requests each exhausted the
  7,200-second provider timeout without a report.
- [x] Attempt generic module OpenScientist research; the corrected request
  exhausted its 7,200-second provider timeout without returning a report.
- [x] Complete module + `ppu00310` + PSEPK OpenScientist research.
- [x] Integrate useful research findings without treating provider output as authority.
- [x] Validate and render the module, gene reviews, and batch page.
- [x] Open one PR for this module; automated review and CI are in progress.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `davB` | PP_0383 | Q88QV1 | lysine 2-monooxygenase | Retain GO:0050067; flag conflicting automated tryptophan/auxin assignment |
| `davA` | PP_0382 | Q88QV2 | 5-aminopentanamidase | Retain GO:0047588; remove N-carbamoylputrescine amidase transfer |
| `davT` | PP_0214 | Q88RB9 | 5-aminovalerate aminotransferase | Retain GO:0047589; leave GABA transaminase activity undecided |
| `davD` | PP_0213 | Q88RC0 | glutarate-semialdehyde dehydrogenase | Retain GO:0102810; remove succinate-semialdehyde transfers; leave GABA catabolism undecided |

## Evidence Notes

PMID:16237033 establishes the simultaneous aminovalerate and aminoadipate
routes in KT2440. PMID:31064836 supplies full-text fitness and proteomics
evidence for the four-gene Dav context. PMID:25012259 directly assays purified
KT2440 DavB and DavA, while PMID:11679348 supplies direct genetic evidence for
DavT and a phenotype that places its reaction before glutarate. The
species-aware OpenScientist review independently recovered the same four-step
boundary and identified the UniProt DavB name as the principal annotation
discrepancy. The broad candidate inventory is retained in
[`ppu00310_lysine_dav_catabolism.tsv`](ppu00310_lysine_dav_catabolism.tsv).

The completed DavT report corroborated the 5-aminovalerate aminotransferase
role. The DavD report generalized an NAD-dependent ortholog, whereas the exact
Q88RC0 record assigns the NADP-dependent RHEA:57832 reaction represented by
GO:0102810; that overgeneralization was not imported. DavA and DavB were each
allowed the full configured provider timeout, so their missing reports are
recorded as retrieval failures rather than unfinished curation.

The generic module request was also allowed the full configured timeout with
three iterations but returned no report. No generic report is cited or
represented as evidence; the completed species-aware module/pathway/taxon
report was retained as retrieval context and checked against the primary
evidence above.

The available PANTHER subfamily calls are not tighter reaction selectors:
DavB maps to a histone-demethylase-labeled subfamily, DavA to
beta-ureidopropionase, DavT to leucine/methionine racemase, and DavD to a
mixed succinate-semialdehyde-dehydrogenase family. The module therefore uses
honest fold-level families constrained by exact exemplars and leaf molecular
functions.
