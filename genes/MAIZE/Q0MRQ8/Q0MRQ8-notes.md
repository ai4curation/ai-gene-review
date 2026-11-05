# Q0MRQ8 (ZmrbohA) review notes

- Fetched 2026-10-28; UniProt id confirmed Q0MRQ8, GeneID 778438, 6 IEA GOA rows.
- Identity: ZmrbohA, EMBL DQ855284 [PMID:20693409 "ZmrbohA (GenBank accession no. DQ855284)"];
  852 aa [PMID:19592501 "encoding a protein of 852 amino acids"].
- Clade IV with AtrbohH/J and OsrbohE [PMID:19592501 "The fourth major cluster consists of the
  newly identified ZmrbohA and the four proteins of unknown function AtrbohH, AtrbohJ, OsrbohD,
  and OsrbohE"]. AtRbohH/J are Ca2+-activated plasma membrane ROS producers in pollen tubes
  [PMID:24610725].
- Maize evidence is expression only (ABA, H2O2, BR induction in leaves); no NEW process
  terms proposed (expression is not participation).
- Decisions: peroxidase -> REMOVE (wrong InterPro2GO mapping, source defect); cellular oxidant
  detoxification -> REMOVE (derived from it, source defect); calcium ion binding ->
  KEEP_AS_NON_CORE; membrane -> MODIFY plasma membrane; oxidoreductase rows -> MODIFY to
  GO:0106292 (ancestry checked with OAK). Consistent with sibling maize review rbohC.
