# ssp120 review notes

## Setup

- `just fetch-gene SCHPO ssp120` could not resolve the current PomBase symbol through UniProt; `just fetch-gene SCHPO O74903` created the review stub, and its 12-row YAML seed was moved under the existing `ssp120` folder that already held identical GOA and UniProt cache files.
- `just fetch-gene-pmids SCHPO ssp120` found PMID:16823372 and PMID:41203586 already cached.
- `just fetch-panther-paint PTHR19237 --extra-uniprot O74903` created the local PAINT node table for the Ssp120/nucleobindin family.
- `just mod-description-deep-research SCHPO emp43 ssp120` skipped because `SCHPO` has no configured model-organism-description provider.
- `just deep-research-falcon SCHPO ssp120 --fallback perplexity-lite` could not run: the local wrapper reported that `falcon` was unavailable, and the fallback reported that `perplexity` was unavailable.
- PAINT lineage-loss check: no IRD or IKR loss on the `ssp120` lineage.

## Literature and database evidence

- The S. pombe Ssp120 UniProt record identifies O74903/SPCC613.03 as an uncharacterized calcium-binding protein precursor with a signal peptide, EF-hand domains, and no annotated transmembrane segment [file:genes/SCHPO/ssp120/ssp120-uniprot.txt, "SIGNAL          1..20"].
- UniProt places Ssp120 in the ER lumen and Golgi lumen, matching a soluble luminal partner rather than a transmembrane COPII-tail receptor [file:genes/SCHPO/ssp120/ssp120-uniprot.txt, "Endoplasmic reticulum lumen"].
- The PTHR19237 PAINT table places ERGIC localization and calcium ion binding on `PTN001059206`, the Ssp120/nucleobindin 1 node inherited by S. pombe Ssp120 [file:interpro/panther/PTHR19237/PTHR19237-paint.tsv, "PTHR19237\tPTN001059206"].
- Imamura et al. identify Ssp120 as the S. pombe orthologue of human MCFD2 and as a functional partner of Emp43 in an ERGIC-like compartment [PMID:41203586, "identified Ssp120 of S. pombe, an orthologue of human MCFD2, as a functional partner of Emp43"].
- The cached PMID:41203586 entry is abstract-only, so the direct PomBase IMP/IPI annotations from that paper are treated as full-text curation calls rather than reinterpreted from the abstract alone.

## GO-CAM context

Model `693b3c0900004859` enables Ssp120 with COPII receptor activity in the COPII-coated ER-to-Golgi transport vesicle and gives Ssp120 a direct input edge to Sec24. The molecular function is reasonable as the luminal component of the Emp43-Ssp120 cargo receptor complex, but the gene review should preserve the topology caveat already recorded in the GO-CAM review: soluble Ssp120 should work through transmembrane Emp43 rather than directly contacting cytosolic Sec24.
