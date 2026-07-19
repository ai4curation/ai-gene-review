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
- Accessory genes recovered outside KEGG map membership: 3
- Primary bucket genes: 13
- Existing review files: 13
- Curated review files: 13
- Gene-level deep-research jobs running: 0

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch selected high-priority genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes selected for full review.
- [x] Curate selected gene reviews.
- [ ] Validate module and touched gene reviews.
- [x] Open one PR for this module/pathway: [#2137](https://github.com/ai4curation/ai-gene-review/pull/2137).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Gene research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `coq7` | PP_0427 | Q88QR1 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | 3-demethoxyubiquinol 3-hydroxylase (DMQ hydroxylase) (EC 1.14.99.60) (2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hy |
| [x] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | PRESENT | CURATED | COMPLETE | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [ ] | `PP_1218` | PP_1218 | Q88NI9 | kegg:ppu00130 | MISSING | MISSING | MISSING | Acyl-CoA thioesterase (EC 3.1.2.-) |
| [ ] | `PP_1644` | PP_1644 | Q88MC9 | kegg:ppu00130 | MISSING | MISSING | MISSING | NAD(P)H dehydrogenase (Quinone) (EC 1.6.5.2) |
| [x] | `ubiG` | PP_1765 | Q88M10 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | Ubiquinone biosynthesis O-methyltransferase (2-polyprenyl-6-hydroxyphenol methylase) (EC 2.1.1.222) (3-demethylubiquinon |
| [ ] | `PP_2789` | PP_2789 | Q88J60 | kegg:ppu00130 | MISSING | MISSING | MISSING | Oxidoreductase |
| [ ] | `hpd` | PP_3433 | Q88HC7 | kegg:ppu00130 | PRESENT | CURATED | MISSING | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) |
| [ ] | `PP_3720` | PP_3720 | Q88GK1 | kegg:ppu00130 | MISSING | MISSING | MISSING | NAD(P)H quinone oxidoreductase |
| [x] | `ubiE` | PP_5011 | Q88D17 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-b |
| [x] | `ubiJ` | PP_5012 | Q88D16 | outside ppu00130 | PRESENT | CURATED | COMPLETE | Ubiquinone biosynthesis accessory factor UbiJ |
| [x] | `ubiB` | PP_5013 | A0A140FWS4 | outside ppu00130 | PRESENT | CURATED | COMPLETE | Probable protein kinase UbiB |
| [x] | `visC` | PP_5197 | Q88CI4 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | Predicted aerobic UbiI/VisC-type ubiquinone hydroxylase |
| [x] | `ubiH` | PP_5199 | Q88CI2 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | 2-octaprenyl-6-methoxyphenyl hydroxylase |
| [x] | `ubiD` | PP_5213 | Q88CG8 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98) (Polyprenyl p-hydroxybenzoate decarboxylase) |
| [x] | `ubiK` | PP_5235 | Q88CE6 | outside ppu00130 | PRESENT | CURATED | COMPLETE | Ubiquinone biosynthesis accessory factor UbiK |
| [x] | `ubiC` | PP_5317 | Q88C66 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | Probable chorismate pyruvate-lyase (CL) (CPL) (EC 4.1.3.40) |
| [x] | `ubiA` | PP_5318 | Q88C65 | kegg:ppu00130 | PRESENT | CURATED | COMPLETE | 4-hydroxybenzoate polyprenyltransferase (EC 2.5.1.39) |

## Notes

First-pass boundary:

- Core aerobic ubiquinone biosynthesis: `ubiC` supplies 4-hydroxybenzoate from chorismate; `ubiA` attaches the polyprenyl side chain; `ubiD` performs the prFMN-dependent decarboxylation; `visC`, `ubiH`, `coq7`, `ubiG`, and `ubiE` carry the complementary ring hydroxylation/methylation steps.
- Cofactor context: `ubiX` makes prenylated FMN for UbiD-family decarboxylases. It is not a direct ubiquinone-substrate conversion, but it is included as UbiD activation context in the reusable module.
- Assembly/accessory context missed by the KEGG membership list: `ubiJ`, `ubiK`, and `ubiB`. The `ubiE-ubiJ-ubiB` gene cluster provides additional species-level support; these factors are optional context in the reusable module, not extra ring reactions. UbiB is modeled conservatively as a kinase-like ATP-dependent accessory factor rather than a demonstrated UbiI regulator.
- KEGG map spillover / neighboring processes to scrutinize: `hpd` is already curated as homogentisate-pathway tyrosine/phenylalanine catabolism, while `PP_1218`, `PP_1644`, `PP_2789`, and `PP_3720` look like acyl-CoA thioesterase or generic quinone reductase entries rather than required ubiquinone-biosynthesis steps.

This PR began as a module-first light pass. The nine selected catalytic/cofactor
genes and three recovered accessory genes are now fetched for full review. The
five neighboring or map-spillover entries remain metadata-only because the
species-level audit found no required ubiquinone-biosynthesis role for them.

OpenScientist status:

- Initial generic and species-aware attempts on 2026-07-15 failed at the
  provider/API layer. Fresh jobs with long client timeouts completed on
  2026-07-18, producing generic, species-aware, and all 12 selected gene-level
  reports plus their provider artifacts.
- The species audit recovered `ubiJ`, `ubiK`, and `ubiB` outside KEGG map
  membership and excluded five map-spillover genes from the de novo pathway.
- Gene-level integration was deliberately adversarial: UbiX carboxy-lyase and
  UbiB protein-kinase transfers were corrected; UbiE menaquinone process was
  removed while family-level demethylmenaquinone activity was retained only as
  over-annotation; unsupported target-strain metabolon, locus, exact side-chain,
  and membrane-orientation claims were not propagated.
- The final Coq7 report is anchored by direct complementation of an E. coli
  `ubiF` mutant by a Pseudomonas aeruginosa Coq7 ortholog. PP_0427 remains an
  explicitly homology- and pathway-supported assignment because the KT2440
  protein itself has not been assayed.

Generated UTC: 2026-07-19T02:51:10Z
