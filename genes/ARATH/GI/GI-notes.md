# GI (GIGANTEA; At1g22770; UniProtKB:Q9SQI2) notes

## 2026-10-06: finishing UNDECIDED rows (photoperiodic_flowering_co_ft module)

- GO:0009908 flower development (TAS, PMID:10202817): the cached abstract is about auxin polar transport
  in pin mutants and does not mention GI; full text unavailable. Changed UNDECIDED -> MARK_AS_OVER_ANNOTATED
  (not REMOVE): GI controls flowering time through CO/FT induction
  [PMID:17872410 "The FLAVIN-BINDING, KELCH REPEAT, F-BOX 1 (FKF1), and GIGANTEA (GI) proteins regulate CO
  transcription in Arabidopsis."], not floral organ development.
- GO:0005515 GI-SPY (PMID:15155885): MARK_AS_OVER_ANNOTATED -> REMOVE (term only), per the
  protein-binding policy enforced by the validator; the interaction itself is not disputed.
- Left UNDECIDED (genuinely unverifiable from cached abstracts/supplements): DNA binding IDA
  (PMID:40157149; abstract only, may reflect chromatin association via HOS15/HD2C), and two
  high-throughput protein-binding rows (PMID:19452453 14-3-3 TAP-MS; PMID:32612234 hormone interactome).
- Fixed a folded-scalar hyphen split ("blue-light-dependent").

## 2026-10-06 follow-up (all UNDECIDED resolved)

- DNA binding IDA (PMID:40157149): no open-access full text (Europe PMC lists no PMC record). GI has no
  DNA-binding domain and the abstract describes it as a co-repressor with HOS15/HD2C -> MARK_AS_OVER_ANNOTATED.
- Protein binding, 14-3-3 TAP-MS (PMID:19452453) and hormone interactome Y2H (PMID:32612234) -> REMOVE
  (term only), following the protein-binding policy.
