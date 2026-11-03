# lolC (Escherichia coli K-12) review notes

## 2026-10-23

- Review created as an experimental exemplar for the reusable module
  `modules/bacterial_lol_lipoprotein_trafficking.yaml`; E. coli K-12 is the
  organism in which the LolCDE-LolA-LolB pathway was defined biochemically and
  genetically (Tokuda laboratory).
- Provider deep research was not generated: no deep-research provider API key
  is configured in this session. The review is based on the UniProt record,
  the GOA rows and the cached publications in `publications/`, most of which
  are abstract-only (`full_text_available: false`).
- GO has specific molecular-function terms for two Lol stages:
  GO:0140306 lipoprotein releasing activity (LolCDE; already annotated to
  E. coli LolC, LolD and LolE by IDA/IMP) and GO:0140598 lipoprotein carrier
  activity (LolA). No MF term exists for the LolB acceptance/insertion step.
