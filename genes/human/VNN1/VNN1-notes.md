# VNN1 notes

## 2026-11-25

- Fetched `human VNN1`; `VNN1-goa.tsv` contained 33 annotations plus the header, so this was not a failed/header-only GOA fetch.
- Ran `just paint-losses human VNN1`; no IRD or IKR loss lies on the VNN1 lineage in PTHR10609.
- Tried the default Falcon deep-research recipe, but the local provider failed with `agentapi not found in PATH`. I continued with manual review from the seeded GOA rows, cached UniProt, cached PTHR10609 entries/PAINT files, Reactome summaries and the fetched PubMed records.
- No production GO-CAM activity in `gocams/index.tsv` used `UniProtKB:O95497`; the Reactome vitamin B5 reaction was enough context for the single VNN1 catalytic step.
- I did not create a ModuleReview. VNN1 and VNN2 are alternative single-step pantetheinases, and BTD is the biotinidase-side salvage enzyme rather than a second part of the same module.
