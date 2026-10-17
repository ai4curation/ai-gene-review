# ggg1 (SPBC31F10.03, UniProt P87305) – notes

ChaC-family glutathione-specific gamma-glutamylcyclotransferase. Module: CHAC1 step. S. cerevisiae ortholog GCG1 (review genes/yeast/GCG1).

Naming trap: UniProt has no gene name for P87305 (ORF name only), so `just fetch-gene SCHPO ggg1` failed; fetched by accession.

## Evidence
- No S. pombe experimental data. Function by similarity to Gcg1 [UniProt:P87305]: "Gamma-glutamylcyclotransferase acting specifically on glutathione, but not on other gamma-glutamyl peptides."
- Family: [PMID:23070364 "We show using in vivo studies and novel in vitro assays that the ChaC family of proteins function as γ-glutamyl cyclotransferases acting specifically to degrade glutathione but not other γ-glutamyl peptides."]
- Location cytoplasm + nucleus, ORFeome HDA [PMID:16823372].
- PANTHER subfamily PTHR12192:SF2 is named "GLUTATHIONE-SPECIFIC GAMMA-GLUTAMYLCYCLOTRANSFERASE 2" (CHAC2-like) [UniProt:P87305].

## Decisions
- Core MF GO:0061928, BP GO:0006751, cytosol — matches GCG1 review and GO-CAM (cytosol). GCG1 review ACCEPTed the parent GO:0006749; here kept as non-core (parent term).
- Cellular detoxification NAS marked over-annotated.
