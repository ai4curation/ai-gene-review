# VNN2 notes

## 2026-11-25

- Fetched `human VNN2`; `VNN2-goa.tsv` contained 17 annotations plus the header, so this was not a failed/header-only GOA fetch.
- Ran `just paint-losses human VNN2`; no IRD or IKR loss lies on the VNN2 lineage in PTHR10609.
- The VNN1 Falcon deep-research attempt failed with `agentapi not found in PATH`; to avoid another unavailable-provider call, I reviewed VNN2 manually from its seeded GOA rows, cached UniProt record, the local PTHR10609 entries/PAINT files, Reactome summaries and the cached PubMed records.
- The five `GO:0005515` rows from PMID:32814053 all came from a systematic yeast two-hybrid candidate network and were removed under the bare protein-binding policy rather than promoted to specific molecular functions.
