# ROS1 (human, P08922) curation notes

Deep research providers were unavailable in this environment; evidence from cached publications and
UniProt.

## Localization
- UniProt `SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Single-pass type I membrane protein`.
  Large extracellular fibronectin-type-III region is surface-exposed; the kinase domain is
  cytoplasmic.
- Generic `GO:0016020 membrane` modified to plasma membrane.
- Caveat recorded in the review: oncogenic ROS1 fusions (FIG/GOPC, CD74, SLC34A2) lose the
  transmembrane anchoring and are not plasma-membrane receptors.

## Function
- NELL2 is the endogenous ligand; ROS1 "triggers epididymal epithelial differentiation and
  subsequent sperm maturation" (UniProt, by similarity to mouse).
- Substrates: PTPN11 ("Mediates the phosphorylation of PTPN11, an activator of this pathway"),
  VAV3 [PMID:11094073], STAT3; downstream PI3K-mTOR, ERK.
- Phosphatase recruitment: "Phosphorylation at Tyr-2274 is required for the interaction with PTPN6".

## Review decisions
- Three generic `GO:0005515` rows removed per policy (the SHP-1/PTP1B peptide study is represented
  by protein phosphatase binding).
- `GO:0004672` modified to the tyrosine-specific kinase terms; `GO:1902531 regulation of
  intracellular signal transduction` marked TOO_GENERAL.
- Spermatogenesis and epithelial-development ISS rows kept as non-core tissue outputs.
