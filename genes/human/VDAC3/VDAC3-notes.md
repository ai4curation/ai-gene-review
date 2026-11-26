# VDAC3 notes

Deep research providers were unavailable for this manual pass; evidence came from cached GOA PMIDs, the
UniProt record, and the already-reviewed human VDAC1 file.

## Curation decisions

- Core function: mitochondrial outer-membrane voltage-gated anion channel activity. The decisive
  VDAC3-specific paper shows weakly anion-selective, voltage-gated pores after reconstitution in planar
  lipid membranes [PMID:31935282].
- `GO:0005244` is modified to the specific supported term `GO:0008308`.
- Root `mitochondrion` rows are accepted as real organelle-localization claims because sub-compartment
  replacement is handled by separate `mitochondrial outer membrane` rows. The generic `membrane` rows
  are kept as peripheral non-mitochondrial-membrane claims from the human erythrocyte evidence rather
  than narrowed to plasma membrane.
- The 1998 TAS row to `GO:0015853 adenine transport` is modified to `GO:0051503 adenine nucleotide
  transport` because the abstract describes adenine nucleotide movement as a general VDAC-family
  property, not transport of the free base adenine by VDAC3.
- Reports that VDAC3 recruits Mps1 to centrosomes [PMID:22935710] and negatively regulates
  ciliogenesis [PMID:23388454] are left as a suggested question until this non-mitochondrial pool can
  be compared against VDAC3 channel activity and human GO term choices.
- Sperm rows are kept as non-core because mouse Vdac3 supports male fertility and sperm mitochondrial
  sheath assembly, but human direct evidence is not present in the GOA seed.
- Nucleus and extracellular-exosome HDA rows are over-annotations of high-throughput proteomics hits.
- Bare VDAC1/VDAC2 protein-binding rows are removed under the protein-binding policy.
