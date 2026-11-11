# Fosl2 (rat) review notes

## Session 1
- `just fetch-gene rat Fosl2` resolved P51145 (Swiss-Prot, RGD:2628, GeneID 25446); 102 GOA rows.
- No deep-research keys; wrote `Fosl2-deep-research-manual.md` by hand.
- Read full text of PMID:21367864 (Rgs4 repression, ChIP/EMSA, CBP dismissal) and PMID:11340164 (DNF2 transgenic rat).
  Most other rat GOA papers are abstract-only expression studies.

## Decisions
- Core: GO:0000981 (pol II-specific DNA-binding TF activity), GO:0000978, AP-1 complex, nucleus,
  GO:0006357 / GO:0045944. Generic DNA-binding/TF/regulation terms MODIFIED to these.
- NEW: GO:0001227 repressor activity and GO:0000122 negative regulation of pol II transcription, from the Rgs4
  data in PMID:21367864 ["transcriptional repression was blocked by mutation of the AP-1R sequence"]. Fra-2 is the
  DNA-bound factor performing the regulation, so the participation test is met.
- IEP "response to X" rows: Fra-2 is an immediate-early gene; induction alone is not participation, so most are
  MARK_AS_OVER_ANNOTATED. Kept: circadian rhythm (Fra-2-dependent rhythmic target expression in pineal),
  response to cAMP (Fra-2 mediates PKA-induced C/EBPbeta), response to hypoxia (DN screen in PC12).
- PMID:12021174 row is coded IMP but the perturbation is an antiestrogen; treated as expression evidence.
- Mouse ISO rows (MGI:102858): cell-autonomous, target-gene-backed differentiation roles (chondrocyte, osteoblast,
  osteoclast, adipocyte, B cell, T cell) kept as non-core; systemic, gain-of-function or phenotype-only terms (lung
  fibrosis-related development, inflammation, glucose homeostasis, growth, responses to bleomycin/LPS/etc.)
  marked over-annotated. Keratinocyte development UNDECIDED (source paper not retrieved).
