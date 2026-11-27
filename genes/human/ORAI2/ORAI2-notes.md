# ORAI2 curation notes

## 2026-11-25

- `just fetch-gene human ORAI2` seeded 23 GOA annotations from a non-empty GOA
  fetch, and `just paint-losses human ORAI2` reported no IRD or IKR loss on the
  Q96SN7 lineage.
- Agent-backed deep research was attempted on ORAI1 and failed because only
  `claude_code` was registered in this checkout; for this paralog the review
  used the UniProt record, cached ORAI-family publications, PAINT `PTHR31501`,
  and the store-operated-calcium-entry module.
- Core function: ORAI2 is a four-pass plasma-membrane ORAI channel subunit.
  PMID:17442569 shows CRACM2/ORAI2 potentiating CRAC current in STIM1-expressing
  cells; PMID:19182790 shows STIM1 SOAR activating all ORAI isoforms; and
  PMID:32415068 supports endogenous ORAI2/ORAI1 heteromers that help generate
  oscillatory receptor-evoked calcium signals.
- The HPA nucleoplasm, cytosol and mitochondrion rows are not supported by the
  curated record or by ORAI2 topology and were marked as over-annotations rather
  than as hard removals.
