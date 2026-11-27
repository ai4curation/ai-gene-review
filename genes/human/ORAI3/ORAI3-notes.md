# ORAI3 curation notes

## 2026-11-25

- `just fetch-gene human ORAI3` seeded 22 GOA annotations from a non-empty GOA
  fetch, and `just paint-losses human ORAI3` reported no IRD or IKR loss on the
  Q9BRQ5 lineage.
- Agent-backed deep research was attempted on ORAI1 and failed because only
  `claude_code` was registered in this checkout; for this paralog the review
  used the UniProt record, cached ORAI-family publications, PAINT `PTHR31501`,
  and the store-operated-calcium-entry module.
- Core function: ORAI3 is a four-pass plasma-membrane ORAI channel subunit that
  forms STIM-gated store-operated CRAC channels. It is also the ORAI paralog
  that heteromerizes with ORAI1 in store-independent arachidonate-regulated
  channels, which is real biology but outside the SOCE module curated here.
- The cached 2007, 2009 and 2020 ORAI-family papers support store-operated
  calcium channel activity for ORAI3; PMID:32415068 is the key native-cell paper
  for ORAI2/3 heteromerization with ORAI1.
