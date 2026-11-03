# Curation notes: *Pseudomonas putida* KT2440 fadB (Q88L02, PP_2136)

## Sources

- `fadB-deep-research-falcon.md` (provider report, already present) and the
  OpenScientist function-hypothesis report for GO:0016509 under
  `fadB-hypotheses/`.
- The reviewed UniProt entry is typed by HAMAP rule MF_01621.
- Experimental support is transferred from the E. coli orthologue FadB
  (P21177; `genes/ECOLI/fadB/`): G116F abolishes the hydratase
  (PMID:8454629), His450 is the dehydrogenase catalytic residue
  (PMID:8755745), and the purified complex carries all five activities
  (PMID:368024).

## Decisions (2026-11 completion pass)

- Generic parents (catalytic activity, oxidoreductase, CH-OH oxidoreductase,
  fatty acid metabolic and catabolic process, lipid catabolic process) changed
  from MARK_AS_OVER_ANNOTATED/ACCEPT to TOO_GENERAL, matching the E. coli
  review: they are true but entailed by accepted specific terms.
- The dehydrogenase core function is GO:0003857 rather than its long-chain
  child GO:0016509, matching E. coli FadB, whose dehydrogenase also acts on
  acetoacetyl-CoA; the GO:0016509 TreeGrafter row is still accepted.
- Truncated UniProt quotes in the draft were replaced with complete sentences.
