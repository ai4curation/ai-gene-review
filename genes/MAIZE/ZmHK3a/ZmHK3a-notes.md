# ZmHK3a notes

- 2026-10-28: Review created. fetch-gene resolved Q76GZ9 (GeneID 541642, EMBL AB102957), 16 GOA
  rows. Deep-research API unavailable; literature compiled by hand in
  ZmHK3a-deep-research-manual.md.
- Key papers (both full text): PMID:15064375 (cloning, E. coli rcsC complementation, ligand
  preference, expression) and PMID:21778179 (direct [3H]tZ binding; ER localization shown only
  for ZmHK1) [PMID:21778179 "ZmHK3a preferred iP."].
- Decisions mirror the sibling ZmHK1 review: core MF GO:0009885; generic MF rows MODIFY to it;
  hormone binding MODIFY to GO:0044373 cytokinin binding plus NEW IDA row from PMID:21778179;
  cytokine binding (ARBA) REMOVE with source defect (cytokine vs cytokinin).
- Location kept at membrane / endomembrane system: no ZmHK3a-specific localization assay; ER
  membrane rests only on the paralog ZmHK1 data, so no NEW ER membrane row
  [PMID:21778179 "Taken together, our results suggest that ZmHKs are localized predominantly in the ER membrane."].
- ZmHK3b splice form (AB121445) lacks part of the CHASE input domain and is not
  cytokinin-responsive [PMID:15064375 "ZmHK3b did not respond to any cytokinin tested"]; not an
  isoform of this TrEMBL entry.
- ARBA FUNCTION comment mentions "stress signal to a downstream MAPK cascade" (AHK1-type wording);
  flagged as a CHECK source defect.
