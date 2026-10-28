# Nedd4 (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Nedd4` resolved Q62940 (NEDD4_RAT; RGD:3157; GeneID 25489), 119 GOA
  rows seeded (SynGO rows with several ECO codes collapse to IDA/IMP/IEP rows). UniProt REST
  was rate-limited and needed retries.
- No deep-research API; literature synthesized by hand in `Nedd4-deep-research-manual.md`.
- Additional PMIDs cached for evidence: 8665844, 11323714, 9351815, 21338354, 20026598,
  18931680, 17996703, 19345204, 22673903.

### Key decisions

- MF: HECT E3 `ubiquitin protein ligase activity` (GO:0061630) is core; the IDA/IEA rows on
  the parent `ubiquitin-protein transferase activity` are MODIFY to GO:0061630.
  [PMID:20159449 "The ubiquitination of Rap2A was abolished when catalytically inactive
  instead of WT Nedd4-1 was used"]
- `proline-rich region binding` accepted as the WW-domain/PY-motif substrate recognition
  mechanism, with rat experimental support [PMID:8665844 "the rNedd4-WW domains mediate this
  association by binding to the P2 regions, which include the PY motifs (XPPXY)"].
- Channel inhibitor terms: Nedd4 lowers ENaC/K channel activity by ubiquitination-dependent
  removal, not by direct gating block; kept as non-core (IBA respected) with that caveat.
  The parent `channel inhibitor activity` is TOO_GENERAL relative to the sodium term.
- PMID:19125695 (key paper): rat data are an expression change in denervated gastrocnemius
  [PMID:19125695 "MTMR4 decreases approx. 90% with a 2-fold increase in Nedd4 expression"];
  the IEP `response to denervation involved in regulation of muscle adaptation` is kept as
  non-core. The MTMR4 ubiquitination assays used human proteins.
- PMID:11248052 `immune response` IEP: raft partitioning of Nedd4 in RBL cells is a
  relocalization, not an expression response and not evidence of a role in an immune
  response. Since the mouse T-cell work [PMID:18931680] supports `adaptive immune response`,
  `immune response` is kept non-core rather than removed.
- Very general ARBA terms (regulation of signaling, regulation of cell communication,
  regulation of transport, regulation of protein catabolic process) are TOO_GENERAL: each is
  entailed by a more specific term kept in this review (checked with runoak ancestors).
- `regulation of membrane potential` and `negative regulation of transcription by RNA
  polymerase II` are indirect consequences: MARK_AS_OVER_ANNOTATED.
- GO:0099576 and GO:0140252 are not is_a related in the ontology version used (runoak).
- No NEW terms proposed.

### Open points

- phosphoserine/phosphothreonine residue binding (mouse ISO): source not traced; UNDECIDED.
