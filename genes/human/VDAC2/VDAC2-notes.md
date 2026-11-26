# VDAC2 notes

Deep research providers were unavailable for this manual pass; evidence came from cached GOA PMIDs, the
UniProt record, and the already-reviewed human VDAC1 file.

## Curation decisions

- Core functions: mitochondrial outer-membrane voltage-gated anion channel activity [PMID:8420959;
  file:human/VDAC2/VDAC2-uniprot.txt], phospholipid scramblase activity [PMID:38065946], and
  ceramide binding that promotes ceramide-triggered MOMP [PMID:31015432].
- `GO:0005244` is correct but less specific than the anion-channel term and is modified to
  `GO:0008308`.
- Root `mitochondrion`, `membrane`, and `mitochondrial membrane` rows are kept as real claims but
  modified to `mitochondrial outer membrane` except for the erythrocyte `membrane` row, whose own evidence
  supports a non-mitochondrial, likely plasma-membrane, pool.
- `GO:0017121 plasma membrane phospholipid scrambling` is marked over-annotated. The direct scramblase
  paper assays VDAC2 as a mitochondrial outer-membrane lipid importer, not as a plasma-membrane
  scramblase.
- Acrosomal/zona-pellucida and sperm-midpiece rows are retained as sperm-specific, non-core roles.
- The mitochondrial-nucleoid row is retained as peripheral, mirroring VDAC1: nucleoid purifications can
  retain outer-membrane proteins, but the row does not establish a nucleoid-localized core function.
- Nuclear proteome and bare protein-binding rows are marked over-annotated or removed following the VDAC1
  review and the protein-binding policy.
