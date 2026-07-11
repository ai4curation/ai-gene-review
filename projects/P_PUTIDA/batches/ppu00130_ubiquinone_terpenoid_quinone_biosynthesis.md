---
title: "PSEPK ppu00130 Ubiquinone and other terpenoid-quinone biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00130: Ubiquinone and other terpenoid-quinone biosynthesis

- Module seed: `ubiquinone_biosynthesis`
- Candidate genes from membership table: 14
- Promoted accessory genes outside KEGG membership: 3
- Primary bucket genes: 13
- Existing review files: 14
- Curated review files: 17
- Existing Asta research files: 17

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
| [x] | `coq7` | PP_0427 | Q88QR1 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 3-demethoxyubiquinol 3-hydroxylase (DMQ hydroxylase) (EC 1.14.99.60) (2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hy |
| [x] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [x] | `PP_1218` | PP_1218 | Q88NI9 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Acyl-CoA thioesterase (EC 3.1.2.-) |
| [x] | `PP_1644` | PP_1644 | Q88MC9 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | NAD(P)H dehydrogenase (Quinone) (EC 1.6.5.2) |
| [x] | `ubiG` | PP_1765 | Q88M10 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Ubiquinone biosynthesis O-methyltransferase (2-polyprenyl-6-hydroxyphenol methylase) (EC 2.1.1.222) (3-demethylubiquinon |
| [x] | `PP_2789` | PP_2789 | Q88J60 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Oxidoreductase |
| [x] | `hpd` | PP_3433 | Q88HC7 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) |
| [x] | `PP_3720` | PP_3720 | Q88GK1 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | NAD(P)H quinone oxidoreductase |
| [x] | `ubiE` | PP_5011 | Q88D17 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-b |
| [x] | `visC` | PP_5197 | Q88CI4 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Oxidoreductase involved in anerobic synthesis of ubiquinone, FAD/NAD(P)-binding domain |
| [x] | `ubiH` | PP_5199 | Q88CI2 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 2-octaprenyl-6-methoxyphenyl hydroxylase |
| [x] | `ubiD` | PP_5213 | Q88CG8 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98) (Polyprenyl p-hydroxybenzoate decarboxylase) |
| [x] | `ubiC` | PP_5317 | Q88C66 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Probable chorismate pyruvate-lyase (CL) (CPL) (EC 4.1.3.40) |
| [x] | `ubiA` | PP_5318 | Q88C65 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 4-hydroxybenzoate octaprenyltransferase (EC 2.5.1.39) (4-HB polyprenyltransferase) |

## Promoted Accessory Genes

These genes are absent from the 14-gene KEGG ppu00130 membership batch but were
promoted after the Falcon reports and local UniPathway metadata showed that
UbiB/UbiJ/UbiK are expected accessory factors for efficient bacterial
ubiquinone biosynthesis.

| Done | Gene | Locus | UniProt | Source | Curation | Asta research | Protein / outcome |
|---|---|---|---|---|---|---|---|
| [x] | `ubiJ` | PP_5012 | Q88D16 | Falcon/UniPathway accessory | CURATED | PRESENT | SCP2-domain lipid-binding accessory factor for Ubi-complex intermediate handling |
| [x] | `ubiB` | PP_5013 | A0A140FWS4 | Falcon/UniPathway accessory | CURATED | PRESENT | Kinase-like UbiB accessory/regulatory factor; broad protein kinase annotation marked over-specific |
| [x] | `ubiK` | PP_5235 | Q88CE6 | Generic Falcon/UniPathway accessory | CURATED | PRESENT | Small UbiK assembly/targeting accessory factor for efficient ubiquinone biosynthesis |

## Pathway Decision

KT2440 satisfies the strict aerobic ubiquinone biosynthesis module after adding
the UniPathway-promoted accessory factors `ubiJ`, `ubiB`, and `ubiK`. The
apparent Falcon UbiI gap resolves to a nomenclature issue: `visC`/PP_5197 is a
UbiH/Coq6-family, PTHR43876:SF7, GO:0019168 2-polyprenylphenol hydroxylase
candidate and is treated as the UbiI-like C5 hydroxylation step pending deeper
experimental confirmation.

KEGG ppu00130 remains broader than strict ubiquinone biosynthesis. `hpd` belongs
to homogentisate/aromatic amino-acid catabolism; `PP_1644` and `PP_3720` are
quinone redox enzymes; `PP_1218` is an acyl-CoA thioesterase; and `PP_2789` is a
generic oxidoreductase. These side nodes were curated but should not count
toward module satisfiability.

## Notes

Generated UTC: 2026-07-07T07:31:52.339437+00:00

Completed first-pass state:

- Gene-level first pass is complete: all 14 KEGG candidate genes plus 3
  promoted accessory genes have review folders, Asta first-pass research,
  curated YAML reviews, rendered HTML, and validation complete.
- Both Falcon reports are complete:
  `modules/ubiquinone_biosynthesis-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon.md`.
- Module validation complete with both LinkML schema validation and the module
  term-label validator.
- Gene validation warnings are limited to expected "Asta not cited" notices for
  genes where Asta was used as identity/context retrieval rather than
  decision-grade evidence.
