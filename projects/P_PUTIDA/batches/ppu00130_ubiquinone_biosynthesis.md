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
- Gene-level deep-research jobs running: 4

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch selected high-priority genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes selected for full review.
- [ ] Curate selected gene reviews.
- [ ] Validate module and touched gene reviews.
- [x] Open one PR for this module/pathway: [#2137](https://github.com/ai4curation/ai-gene-review/pull/2137).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Gene research | Protein |
|---|---|---|---|---|---|---|---|---|
| [ ] | `coq7` | PP_0427 | Q88QR1 | kegg:ppu00130 | PRESENT | CURATED | RUNNING | 3-demethoxyubiquinol 3-hydroxylase (DMQ hydroxylase) (EC 1.14.99.60) (2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hy |
| [ ] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | PRESENT | CURATED | RUNNING | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [ ] | `PP_1218` | PP_1218 | Q88NI9 | kegg:ppu00130 | MISSING | MISSING | MISSING | Acyl-CoA thioesterase (EC 3.1.2.-) |
| [ ] | `PP_1644` | PP_1644 | Q88MC9 | kegg:ppu00130 | MISSING | MISSING | MISSING | NAD(P)H dehydrogenase (Quinone) (EC 1.6.5.2) |
| [ ] | `ubiG` | PP_1765 | Q88M10 | kegg:ppu00130 | PRESENT | CURATED | RUNNING | Ubiquinone biosynthesis O-methyltransferase (2-polyprenyl-6-hydroxyphenol methylase) (EC 2.1.1.222) (3-demethylubiquinon |
| [ ] | `PP_2789` | PP_2789 | Q88J60 | kegg:ppu00130 | MISSING | MISSING | MISSING | Oxidoreductase |
| [ ] | `hpd` | PP_3433 | Q88HC7 | kegg:ppu00130 | PRESENT | CURATED | MISSING | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) |
| [ ] | `PP_3720` | PP_3720 | Q88GK1 | kegg:ppu00130 | MISSING | MISSING | MISSING | NAD(P)H quinone oxidoreductase |
| [ ] | `ubiE` | PP_5011 | Q88D17 | kegg:ppu00130 | PRESENT | CURATED | RUNNING | Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-b |
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

- Attempted generic module research and module + ppu00130 + PSEPK research on 2026-07-15. Both jobs failed at the provider/API layer (`521` while polling submitted jobs, then `522` at the OpenScientist health check on retry). No provider output files were created.
- Fresh generic, species-aware, and nine gene-level OpenScientist jobs were
  started on 2026-07-18 with 7200-second client timeouts.
- Generic and species-aware reports completed successfully. The species audit
  recovered `ubiJ`, `ubiK`, and `ubiB`; three additional gene reports were
  started with the same 7200-second timeout. `ubiA`, `ubiC`, and `ubiK` are
  complete; `ubiJ` and `ubiB` have now also completed, leaving seven gene jobs
  in progress. UbiB curation replaces the transferred canonical protein-kinase
  call with family-supported ATP hydrolysis and keeps the exact bacterial
  molecular output as a knowledge gap. UbiD has also completed; its report
  confirms the prFMN-dependent reaction. Curation retains peripheral
  inner-membrane localization and rejects the report's unsupported placement of
  UbiD inside the defined seven-protein soluble Ubi metabolon. VisC has also
  completed; the E. coli UbiI evidence corrects the legacy "anaerobic" product
  name, while exact PP_5197 regioselectivity and KT2440 complex membership stay
  explicitly inferential. UbiH has also completed; its report supports the
  family-level hydroxylase assignment, but three incorrect locus-to-gene claims
  in its genomic-context section are explicitly excluded from curation.

Generated UTC: 2026-07-15T11:36:12.085521+00:00
