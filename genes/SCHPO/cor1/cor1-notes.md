# cor1 review notes

## Setup

- `just fetch-gene SCHPO SPAC2C4.05` created the review stub, GOA seed, and UniProt cache; the generated folder and files were renamed to the current PomBase gene symbol `cor1` to avoid the unrelated `nse6` record that UniProt still exposes with `cor1` as an old synonym.
- `just fetch-gene-pmids SCHPO cor1` found PMID:16823372 and PMID:41676957 already cached.
- PMID:10759889 was already cached and was checked because UniProt cites it as direct S. pombe localization support for O14038.
- `just mod-description-deep-research SCHPO erv14 cor1` skipped because `SCHPO` has no configured model-organism-description provider.
- `just deep-research-falcon SCHPO cor1 --fallback perplexity-lite` could not run: the local wrapper reported that `falcon` was unavailable, and the fallback reported that `perplexity` was unavailable.
- PAINT lineage-loss check: no IRD or IKR loss on the `cor1` lineage.

## Literature and database evidence

- The S. pombe Cor1 UniProt record classifies O14038/SPAC2C4.05 as a predicted cornichon-family multipass ER-membrane protein [file:genes/SCHPO/cor1/cor1-uniprot.txt, "Belongs to the cornichon family"].
- Its current reviewed UniProt entry still lacks the `cor1` gene name and has no functional comment, so the current PomBase symbol is carried in this review rather than copied from the `GN` line [file:genes/SCHPO/cor1/cor1-uniprot.txt, "ORFNames=SPAC2C4.05"].
- The same PTHR12290 PAINT node, PTN000265246, supports ER membrane, COPII-coated ER-to-Golgi transport vesicle, and ER-to-Golgi vesicle-mediated transport for both S. pombe Cor1 and Erv14; the more specific PTN000265245 cargo receptor activity node is also inherited by Cor1 and Erv14 [file:interpro/panther/PTHR12290/PTHR12290-paint.tsv, "PTN000265245\tGO:0038024"].
- Kacovska et al. describe the broad cornichon mechanism, in which conserved CNIH/Erv14-family COPII cargo receptors facilitate ER export of transmembrane cargoes into COPII-coated vesicles [PMID:41676957, "Cornichon (CNIH/Erv14) proteins are a family of COPII-coated vesicle cargo receptors that are conserved from yeasts to mammals"].
- That conserved evidence supports a predicted cornichon cargo-receptor role for Cor1, but the cached literature did not identify an assayed Cor1-specific cargo; avoid adding cargo-specific phenotypes or named substrates.

## GO-CAM context

Model `693b3c0900004859` enables S. pombe Cor1 with COPII receptor activity in the COPII-coated ER-to-Golgi transport vesicle and gives it a direct input edge to Sec24. The activity is consistent with the PANTHER placement of Cor1 at the same cornichon cargo-receptor nodes as Erv14.
