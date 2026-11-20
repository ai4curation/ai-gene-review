# uppP (BacA, P60932) curation notes

- Deep research: no provider deep-research file was generated for this gene in this
  session (no provider API keys in the container); the review uses the Swiss-Prot record
  and the cached publications. No provider-named file was written manually.
- Literature checked: PMID:8389741 (bacA amplification gives bacitracin resistance;
  kinase hypothesis), PMID:15138271 (purified BacA is a C55-PP phosphatase, ~75% of
  membrane activity), PMID:15778224 (redundancy with PgpB/YbjG/YeiU(LpxT)),
  PMID:24855653 (catalytic motifs, Mg/Ca), PMID:26560897 (full text; experimental
  7-TM topology, periplasmic active site, Glu21/Ser27/Arg174), PMID:15919996
  (inner-membrane topology proteome).
- Core: GO:0050380 in plasma membrane; process GO:0016094 added as NEW to match the
  UppS step [PMID:15778224 "The enzyme function is to synthesize the carrier lipid"].
- PAINT: PTN001255889 in PTHR30622 (GO:0050380, GO:0005886, GO:0000270), seeded only by
  P60932. P60932 is the reference protein of the PTHR30622 family review.
- Open question: periplasm-facing active site vs. cytoplasmic de novo C55-PP; possible
  flippase role (not asserted).

## 2026-11-02 review round (PR #5923)

- GO:0016311 dephosphorylation changed to KEEP_AS_NON_CORE: BacA demonstrably performs the reaction; the core process is carrier formation.
- Proposed new term "undecaprenyl phosphate biosynthetic process" (parent GO:0008654, modelled on GO:0043048); the GO:0016094 NEW row now rests on primary data (PMID:15138271, PMID:15778224 triple-mutant depletion).
