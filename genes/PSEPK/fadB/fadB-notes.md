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

## 2026-11-04 PR #5935 review round

- GO:0008692 3-hydroxybutyryl-CoA epimerase changed from KEEP_AS_NON_CORE to
  MARK_AS_OVER_ANNOTATED: the row is rule-assigned, there is no KT2440 assay,
  and the deep-research summary of the KT2440 literature says the epimerase
  role may not be physiologically relevant in Pseudomonas.
- The GO:0004300 IEA row now quotes its own Rhea 20724 (3E) reaction; the
  GO:0018812 reason now states that it is an is_a child of GO:0004300.
- UniProt FUNCTION quotes now start at "Catalyzes the formation of".
