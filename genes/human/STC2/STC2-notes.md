# STC2 notes

## 2026-11-19 ORGANELLES Golgi batch 4 (Golgi apparatus rows)

- One GO:0005794 row: IEA, Ensembl projection (GO_REF:0000107) from mouse O88452. A QuickGO query
  (geneProductId=O88452) shows the donor is an MGI IDA citing PMID:15485913 (Ito et al. 2004 Mol
  Cell Biol, PMC522226, DOI 10.1128/MCB.24.21.9456-9469.2004). The same paper is behind the mouse ER
  IDA.
- PMID:15485913 was fetched: abstract only. The PMC full text could not be retrieved through the
  PubMed MCP. The abstract has no localization data.
- The earlier ACCEPT rested on secretory transit and a deep-research sentence ("predominantly in the
  ER and Golgi") that summarizes the same unread paper. Changed ACCEPT to UNDECIDED (CD247/NTN3
  pattern). The possible outcomes are KEEP_AS_NON_CORE (marker-confirmed endogenous biosynthetic
  pool) or MARK_AS_OVER_ANNOTATED (transit or perinuclear only). ACCEPT is not open.
- The description no longer says STC2 "localizes to the ER and Golgi apparatus". The ER rows were
  not part of this check and still cite the same deep-research sentence. They are worth an ER-policy
  pass.
