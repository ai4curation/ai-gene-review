# ORAI1 curation notes

## 2026-11-25

- `just fetch-gene human ORAI1` seeded 100 GOA annotations from a non-empty GOA
  fetch, and `just paint-losses human ORAI1` reported no IRD or IKR loss on the
  Q96D31 lineage.
- Agent-backed deep research was attempted with `just deep-research-falcon human
  ORAI1 --fallback perplexity-lite`, but only `claude_code` was registered in
  this checkout; no provider report was created. This review therefore rests on
  the UniProt record, the cached GOA rows, PAINT `PTHR31501` rows, the existing
  store-operated-calcium-entry module, and the cached primary publications.
- Core function: ORAI1 is a four-pass plasma-membrane pore subunit of STIM-gated
  calcium release-activated calcium channels. PMID:16921383 supports ORAI1 as
  the CRAC pore by ion-selectivity mutants; PMID:19182790 defines SOAR and shows
  activation of ORAI channels by the STIM1 activation region; PMID:32415068
  supports native ORAI1/2/3 heteromers that tune receptor-evoked calcium signals.
- Kept process/location context only when it names a direct ORAI1 channel
  consequence. AC8/ADCY8 coupling and endothelial calcium signaling are non-core
  contexts; Weibel-Palade exocytosis is over-annotated because the paper places
  ORAI1 upstream as the calcium-entry route rather than as exocytic machinery.
- Removed all bare `GO:0005515` protein-binding rows by policy. The interactions
  are often real and include STIM1, STIM2, ORAI paralogs, CRACR2A and TSPAN18,
  but the unqualified molecular-function term does not describe a reusable role.
