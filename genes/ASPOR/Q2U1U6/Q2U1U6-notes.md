# Q2U1U6 notes

## Re-review 2026-10-01 (GOA refresh)

- Current GOA snapshot has no rows for Q2U1U6; nothing to review or retire.
- Audit of core_functions: removed the `locations: GO:0005576 extracellular region`
  assertion, which had no supporting evidence (the review's own knowledge gap states
  secretion is unknown and no signal peptide is annotated). Added a knowledge gap and a
  description caveat that the 134-aa protein may be a truncated gene model / non-catalytic
  fragment (OpenScientist hypothesis report in `Q2U1U6-hypotheses/`: only fold-level
  SSF48230 match over residues 6-97; paralogs Q2TXR4, Q2USR3, Q2UB60 are 395-453 aa).
  The predicted polysaccharide lyase MF is retained as a hedged, domain-based prediction.
