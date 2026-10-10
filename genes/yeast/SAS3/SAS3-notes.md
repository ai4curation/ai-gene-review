# SAS3 re-review notes

## 2026-09-29 IBA re-review

- Re-read the SAS3 review together with the relevant cached NuA3 literature,
  including PMID:10817755, PMID:12077334, PMID:17157260, PMID:25104842,
  PMID:25473596, and PMID:37968396.
- Checked the PTHR10615 PAINT cache. The broad SAS3 IBA rows for chromatin,
  nucleus, chromatin binding, histone acetyltransferase activity, transcription
  coregulator activity, and regulation of transcription by RNA polymerase II all
  come from `PANTHER:PTN004172926`, a eukaryotic MYST-family node. The NuA3a
  IBA comes from `PANTHER:PTN008308138`, which is seeded by `SGD:S000000148`
  (SAS3) itself; this is expected PAINT behavior, not circular support.
- Searched PubMed and the web for 2023-2026 yeast SAS3/NuA3 papers. Two direct
  S. cerevisiae primary papers were newly cached and added to the review:
  PMID:38914563 for Taf14/Yng1/Sas3 assembly contacts in NuA3 and PMID:41318527
  for cryo-EM structures explaining NuA3 H3K14 substrate recognition.
- Other 2023-2026 PubMed hits were not direct SAS3 evidence: PMID:39299382 is a
  review of H3K36 methylation, PMID:39082211 studies a NuA3 ortholog subunit in
  Beauveria bassiana, and PMID:36864781 focuses on Gcn5 and NuA4 HAT activities.

## 2026-10-10 refresh

- Re-fetched `yeast/SAS3`, bringing the review to the current 36 GOA rows and
  adding six current rows for IntAct protein interactions, experimentally
  supported UniProt protein-lysine-acetyltransferase activity, and ComplexPortal
  NuA3a membership.
- Dropped eight stale rows from the older GOA snapshot: obsolete keyword-derived
  GO_REF:0000043 parent rows and two interaction rows no longer present in GOA.
- Removed the three newly seeded generic `GO:0005515 protein binding` rows and
  accepted the new experimental `GO:0061733 protein-lysine-acetyltransferase
  activity` and `GO:1990467 NuA3a histone acetyltransferase complex` rows.
- Added a conservative `NEW` row for `GO:0036408 histone H3K14
  acetyltransferase activity`, which already exists as a GO molecular-function
  term and is directly supported by NuA3 H3-tail substrate positioning in
  PMID:41318527.
- Kept the standing PAINT decisions: the broad `PANTHER:PTN004172926`
  MYST-family rows are safe for Sas3/NuA3, and fungal `PANTHER:PTN008308138`
  correctly places NuA3a complex membership on the Sas3 branch.
