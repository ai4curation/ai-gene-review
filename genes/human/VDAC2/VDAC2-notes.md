# VDAC2 notes

Deep research providers were unavailable for this manual pass; evidence came from cached GOA PMIDs, the
UniProt record, and the already-reviewed human VDAC1 file.

## Curation decisions

- Core functions: mitochondrial outer-membrane voltage-gated anion channel activity [PMID:8420959;
  file:human/VDAC2/VDAC2-uniprot.txt], phospholipid scramblase activity [PMID:38065946], and
  ceramide binding that promotes ceramide-triggered MOMP [PMID:31015432]. VDAC2 also recruits
  pro-apoptotic BAK/BAX proteins to mitochondrial VDAC complexes [PMID:17110923; PMID:26417093;
  PMID:30478310], but whether that should be represented as a VDAC2 molecular function, a direct
  apoptotic-process contribution, or a more specific ontology term needs expert guidance before
  proposing a new GO row.
- `GO:0005244` is correct but less specific than the anion-channel term and is modified to
  `GO:0008308`.
- Root `mitochondrion` rows are accepted as real organelle-localization claims because sub-compartment
  replacement is handled by separate `mitochondrial outer membrane` rows. Root `mitochondrial membrane`
  rows are modified to `mitochondrial outer membrane`. The erythrocyte `membrane` rows are kept as
  generic, peripheral non-mitochondrial-membrane claims because PMID:27641616 supports a mature
  erythrocyte pool but does not force the isoform-specific row to `plasma membrane`.
- `GO:0017121 plasma membrane phospholipid scrambling` is marked over-annotated. The direct scramblase
  paper assays VDAC2 as a mitochondrial outer-membrane lipid importer, not as a plasma-membrane
  scramblase. A new `mitochondrial outer membrane phospholipid scrambling` process term would remove
  the need for GO_REF:0000108 to choose the plasma-membrane-specific process when it sees
  `phospholipid scramblase activity`.
- Acrosomal/zona-pellucida and sperm-midpiece rows are retained as sperm-specific, non-core roles.
- The mitochondrial-nucleoid row is marked over-annotated: nucleoid purifications can retain
  outer-membrane proteins, but the row does not establish a real nucleoid-localized VDAC2 pool.
- The zebrafish efsevin work [PMID:25588501] supports a candidate role for VDAC2-dependent
  mitochondrial Ca2+ uptake in cardiac rhythmicity, but human GOA has no matching row and the
  mammalian basal function needs direct review.
- Nuclear proteome and bare protein-binding rows are marked over-annotated or removed following the VDAC1
  review and the protein-binding policy.
