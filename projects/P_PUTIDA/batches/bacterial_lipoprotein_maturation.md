---
title: "PSEPK bacterial lipoprotein maturation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [lgt, lspA, lnt]
autolink_gene_symbols: false
---

# PSEPK bacterial lipoprotein maturation

- Module seed: `bacterial_lipoprotein_maturation`
- Module scope: ordered Lgt diacylglyceryl transfer, LspA signal peptide cleavage, and Lnt terminal N-acylation
- Candidate genes in PSEPK instantiation: 3
- Existing review files: 3
- Curated review files: 3
- OpenScientist gene research files: 3

## Required Workflow

- [x] Retire the previous one-step Lgt and Lnt conceptual modules as standalone modules.
- [x] Fetch and curate the missing middle-step gene review for `lspA`.
- [x] Run OpenScientist gene-level deep research for `lspA`.
- [x] Build a reusable multi-step bacterial lipoprotein maturation module.
- [x] Validate `lgt`, `lspA`, and `lnt` gene reviews.
- [x] Run generic OpenScientist retrieval for the combined module.
- [x] Run module + pathway + PSEPK OpenScientist research for the UPA00665 middle step.
- [x] Validate and render the combined module and project pages.
- [x] Open one PR for this module/pathway: [#2118](https://github.com/ai4curation/ai-gene-review/pull/2118).
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Module role | Review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|---|
| [x] | `lgt` | PP_5142 | Q88CN8 | unipathway:UPA00664 | Lgt diacylglyceryl transfer | PRESENT | CURATED | PRESENT | Phosphatidylglycerol--prolipoprotein diacylglyceryl transferase |
| [x] | `lspA` | PP_0604 | Q88Q91 | kegg:ppu03060; member of UPA00665 | LspA signal peptide cleavage | PRESENT | CURATED | PRESENT | Lipoprotein signal peptidase |
| [x] | `lnt` | PP_4790 | Q88DN4 | unipathway:UPA00666 | Lnt N-acylation | PRESENT | CURATED | PRESENT | Apolipoprotein N-acyltransferase |

## Boundary Notes

This batch supersedes the previous standalone-module interpretation of
UPA00664 and UPA00666. Those UniPathway records remain useful provenance for
the Lgt and Lnt substeps, but each is a single reaction and should not be
represented as a one-part module. The reusable module boundary is the
three-step bacterial lipoprotein maturation chemistry: Lgt installs the
diacylglyceryl group on the lipobox cysteine, LspA removes the signal peptide,
and Lnt performs terminal N-acylation where triacylated lipoproteins are made.

The module intentionally excludes downstream Lol sorting and the biological
functions of mature substrate lipoproteins. Those are adjacent envelope
biogenesis contexts, not part of the maturation chemistry.

## Notes

Curator notes, 2026-07-14:

- Added `modules/bacterial_lipoprotein_maturation.yaml` as the multi-part
  replacement for the old single-step conceptual seeds. The top-level module is
  species-neutral; PSEPK appears through UniProt exemplar members Q88CN8,
  Q88Q91, and Q88DN4.
- Fetched, OpenScientist-backed, curated, and validated the missing PSEPK
  middle-step review: `lspA` / PP_0604 / Q88Q91.
- `lspA` accepts GO:0004190 `aspartic-type endopeptidase activity` as the
  available broad MF term, accepts GO:0005886 `plasma membrane`, modifies broad
  GO:0006508 `proteolysis` to GO:0042158 `lipoprotein biosynthetic process`,
  and proposes a more specific lipoprotein signal peptidase activity term.
- The combined module keeps molecular functions at the step/annoton level and
  uses only GO:0042158 `lipoprotein biosynthetic process` as the module-level
  biological-process concept.
- Generic OpenScientist module research completed:
  `modules/bacterial_lipoprotein_maturation-deep-research-openscientist.md`.
  It supports the reusable Lgt-to-LspA-to-terminal-acylation boundary, keeps
  Lol sorting outside the module, and emphasizes that the terminal
  N-acylation/modification chemistry is lineage-variable.
- OpenScientist PSEPK module+pathway research for UPA00665 completed:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00665-deep-research-openscientist.md`.
  It supports `lspA` / PP_0604 / Q88Q91 as the signal-peptidase-II step and
  flags the lspA-only local candidate list as a KEGG-boundary artifact, not a
  biological gap in KT2440.
- Curation caveat retained from UPA00664: PP_4236/Q88F63 should not be counted
  as an Lgt module member without a separate gene review, because the
  species-aware report flagged it as a likely over-propagated DsbE/CcmG-like
  protein rather than a second prolipoprotein diacylglyceryl transferase.
