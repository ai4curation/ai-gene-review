# aruG (PSEAE) curation notes

- Reviewed as a representative member of the bacterial succinylarginine (AST)
  catabolism module (modules/bacterial_succinylarginine_catabolism.yaml).
- No provider deep-research file was generated for this gene: provider API keys
  were not available in this session. The review is based on the UniProt record,
  the GOA rows, and the cached publications cited in the review (abstracts for
  most; full text for PMID:23484010).
- PANTHER/PAINT context is taken from interpro/panther/*/ (PTHR30420, PTHR11986,
  PTHR11699, PTHR15162) and the corresponding family reviews.
- The IBA GO:0009015 (N-succinylarginine dihydrolase) row is a PAINT
  over-propagation from PTN000764516, which spans both PTHR30420 subfamilies
  (SF1 transferases, SF2 dihydrolases); removed and recorded as a source defect.
- UniProt's SIMILARITY comment ("succinylarginine dihydrolase family") conflicts
  with the entry's AstA Pfam/InterPro domains; recorded as a source defect.

## Tier-2 PseudoCAP IBA-seed session, 2026-11-05

Added by the PseudoCAP tier-2 seed audit, which reviewed this gene independently of the
AST-module pass above. Both passes reached the same verdict on all five rows. Retained for its
seed-level detail; where the two differ, the module pass above governs.


## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P80358 --alias aruG`; accession matches the worklist. No
deep-research provider used. PMID:16593724, PMID:7523119 and PMID:9393691 are abstract-only.

### Literature

- AruG is the beta subunit (AruAII) of the heterotetrameric arginine/ornithine
  N2-succinyltransferase [PMID:9393691 "the aruF and aruG genes encode the subunits (AruAI and AruAII) of arginine and ornithine N2-succinyltransferases"];
  purified enzyme [PMID:7523119 "After SDS/PAGE two subunits of 35 kDa and 37 kDa were evident, indicating that the enzyme is a heterotetramer."]
- Family: Pfam AstA (PF04958) and AstA_C, GNAT-like acyl-CoA N-acyltransferase (IPR016181),
  NCBIfam TIGR03244. Same PANTHER placement as astA (PTHR30420:SF1); see astA notes for the
  family-lumping issue and the UniProt similarity-note concern.

### Annotation decisions

- ACCEPT: GO:0006527 (IDA, IBA, IEA), GO:0008791 (IEA).
- REMOVE: GO:0009015 N-succinylarginine dihydrolase activity (IBA). The node-level GO_CENTRAL
  defect is recorded once, on astA (PA0896); not duplicated here.
- Action counts: ACCEPT 4, REMOVE 1. No source defects on this gene (node defect on astA).

## PseudoCAP IBA-seed assessment

PTN000764516 is shared with astA and astB; verdicts consistent across the three.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000764516 | GO:0006527 L-arginine catabolic process | 4 | 12 (6 taxa) | GO:0006527, IDA, PMID:16593724 (PseudoCAP) | SOUND | AruG is the beta subunit of the step-1 enzyme of the AST pathway. The 1986 paper establishes the pathway; gene identity came from PMID:7523119 and PMID:9393691. Abstract only. | E. coli AstB P76216 (IMP PMID:9696779), astB O50175, astA P80357 | Yes |
| PTN000764516 | GO:0009015 N-succinylarginine dihydrolase activity | 1 | 12 | not seeded by aruG | n/a (not a PseudoCAP seed) | Wrongly inherited by the succinyltransferase subfamily; defect recorded on astA. | — | Stands for AstB (SF2) only |
