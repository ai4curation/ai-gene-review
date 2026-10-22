# PSCA (human, O43653) curation notes

Deep research providers were unavailable in this environment (`just deep-research-falcon human PSCA
--fallback perplexity-lite` failed: provider not configured). Findings below come from the cached
publications and the UniProt record.

## Localization
- GPI-anchored cell-surface protein: [PMID:9465086 "Flow cytometric analysis demonstrates that PSCA
  is expressed predominantly on the cell surface and is anchored by a GPI linkage."]; UniProt
  `SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:9465086}; Lipid-anchor, GPI-anchor`.
  Signal peptide 1-11, chain 12-83, GPI propeptide 84-114, five disulfides (LU/three-finger fold).
- Soluble pools: GPLD1 can cleave GPI anchors [Reactome:R-HSA-8940388]; PSCA is found in prostatic
  exosomes [PMID:23533145].
- Benchmark conclusion: cell surface, fully extracellular, GPI-anchored.

## Function
- Lynx/Ly-6 family nAChR modulator: [PMID:25680266 "PSCA forms stable complexes with the α4 nAChR
  subunit and decreases nicotine-induced extracellular-signal regulated kinase phosphorylation in
  PC12 cells"]; present in human cortex and increased ~70% in Alzheimer medial frontal gyrus.
- UniProt also notes a cell-proliferation inhibition activity in vitro (PubMed:18488030), not
  currently annotated in GOA; not proposed as NEW because the mechanism and the entity performing
  the step are undefined.

## Review decisions
- All four localization rows (IBA, IDA, IEA SubCell, TAS) accepted as plasma membrane; the Reactome
  extracellular-region row kept as non-core (shed form), likewise exosome and the inter-ontology
  synapse inference.
- Both nAChR activity/binding rows and the three signalling-process rows accepted; these form the
  single core function.
