# VDAC3 notes

Deep research providers were unavailable for this manual pass; evidence came from cached GOA PMIDs, the
UniProt record, and the already-reviewed human VDAC1 file.

## Curation decisions

- Core function: mitochondrial outer-membrane voltage-gated anion channel activity. The decisive
  VDAC3-specific paper shows weakly anion-selective, voltage-gated pores after reconstitution in planar
  lipid membranes [PMID:31935282].
- `GO:0005244` is modified to the specific supported term `GO:0008308`.
- Mitochondrion and generic membrane rows are modified to mitochondrial outer membrane, the family-specific
  location supported by PAINT, VDAC1 similarity, Reactome, and the UniProt record.
- The 1998 TAS row to `GO:0015853 adenine transport` is removed because the abstract describes adenine
  nucleotide movement as a general VDAC-family property, not transport of the free base adenine by VDAC3.
- Sperm rows are kept as non-core because mouse Vdac3 supports male fertility and sperm mitochondrial
  sheath assembly, but human direct evidence is not present in the GOA seed.
- Nucleus and extracellular-exosome HDA rows are over-annotations of high-throughput proteomics hits.
- Bare VDAC1/VDAC2 protein-binding rows are removed under the protein-binding policy.
