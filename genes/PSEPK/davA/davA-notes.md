# davA curation notes

- Q88QV2 is the `davA` locus and is submitted as 5-aminopentanamidase
  [file:PSEPK/davA/davA-uniprot.txt, "SubName: Full=5-aminopentanamidase"].
- The KT2440 pathway study assigns DavA to the second initial L-lysine-catabolic
  reaction [PMID:31064836, "the oxidation of lysine to 5-aminopentanamide by
  DavB and its subsequent deamination to 5AVA by DavA"].
- Purified KT2440 DavA directly converts 5-aminovaleramide to
  5-aminovalerate [PMID:25012259, "DavA is a hydrolase that catalyzes the
  production of 5-aminovalerate from 5-aminovaleramide."].
  This supports a curator evidence upgrade from the current IEA annotation for
  GO:0047588.
- KT2440 genetics identify davB and davA in the aminovalerate route required
  for L-lysine utilization [PMID:16237033, "New genes were identified in both
  pathways, including the davB and davA genes"].
- GO:0050126 is a nitrilase-family propagation error. It conflicts with the Dav
  pathway substrate and is removed rather than retained as a second amidase
  function.
- The same TreeGrafter transfer also places GO:0033388 putrescine biosynthetic
  process from arginine on the UniProt record. It is absent from the GOA
  snapshot reviewed here but should be rejected for the same substrate and
  pathway mismatch [file:PSEPK/davA/davA-uniprot.txt, "GO; GO:0033388;
  P:putrescine biosynthetic process from arginine"].
- Comparative kinetics with N-carbamoylputrescine remain absent and would
  resolve the nitrilase-family specificity boundary more directly.
