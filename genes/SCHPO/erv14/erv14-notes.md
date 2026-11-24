# erv14 review notes

## Setup

- `just fetch-gene SCHPO erv14` created the review stub, GOA seed, and UniProt cache.
- `just fetch-gene-pmids SCHPO erv14` found PMID:16823372 already cached.
- `just mod-description-deep-research SCHPO erv14 cor1` skipped because `SCHPO` has no configured model-organism-description provider.
- `just deep-research-falcon SCHPO erv14 --fallback perplexity-lite` could not run: the local wrapper reported that `falcon` was unavailable, and the fallback reported that `perplexity` was unavailable.
- PAINT lineage-loss check: no IRD or IKR loss on the `erv14` lineage.

## Literature and database evidence

- The S. pombe Erv14 UniProt record classifies Q9P6K6 as a small cornichon-family multipass membrane protein with a homology-backed role in regulating export of secretory proteins from the ER in COPII-coated vesicles [file:genes/SCHPO/erv14/erv14-uniprot.txt, "Regulates export of the secretory proteins from the endoplasmic reticulum in COPII-coated vesicles"].
- UniProt places Erv14 at both the ER and Golgi compartments, with direct S. pombe large-scale evidence for ER localization and budding-yeast transfer for Golgi membrane residence and ER-derived vesicle packaging [file:genes/SCHPO/erv14/erv14-uniprot.txt, "Resides in the endoplasmic and Golgi compartments, and then packaged into endoplasmic reticulum derived vesicles"].
- The shared PTHR12290 family review separates cornichon cargo receptors from unrelated PPCS enzymes in the same PANTHER family and leaves the cornichon PAINT terms for gene-level review [file:interpro/panther/PTHR12290/PTHR12290-review.yaml, "No cornichon gene review exists in this repo, so the cornichon PAINT terms (cargo receptor activity, ER-to-Golgi transport, COPII vesicle, synapse/dendrite) are left unassessed"].
- Kacovska et al. summarize the conserved S. cerevisiae/human cornichon mechanism: cornichons bind cargoes and COPII-coat proteins so their partners can be incorporated into COPII-coated vesicles for ER export [PMID:41676957, "Due to their ability to bind both cargoes and COPII-complex proteins"]
- The same paper models conserved S. cerevisiae Erv14 residues against Sec24 and finds that the predicted Sec24 contacts lie next to or in the Sec24 D-site, matching experimental work on the budding-yeast cargo receptor [PMID:41676957, "the model corresponds well to experimentally obtained data"].
- The cached literature supports Erv14 as a conserved cornichon COPII cargo receptor, but did not identify an assayed S. pombe Erv14-specific transmembrane cargo or test how Erv14 cargo choice differs from Cor1 cargo choice.

## GO-CAM context

Model `693b3c0900004859` enables S. pombe Erv14 with COPII receptor activity in the COPII-coated ER-to-Golgi transport vesicle and gives it a direct input edge to Sec24. The activity is consistent with Erv14-family cargo receptors cycling from the ER into COPII carriers to hand transmembrane cargo to Sec24.
