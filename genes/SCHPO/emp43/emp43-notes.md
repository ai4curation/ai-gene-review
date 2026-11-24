# emp43 review notes

## Setup

- `just fetch-gene SCHPO emp43` could not resolve the current PomBase symbol through UniProt; `just fetch-gene SCHPO SPBC4F6.05c` created the review stub, GOA seed, and UniProt cache, and the generated folder was renamed to `emp43`.
- `just fetch-gene-pmids SCHPO emp43` found PMID:16823372 and PMID:41203586 already cached.
- `just mod-description-deep-research SCHPO emp43 ssp120` skipped because `SCHPO` has no configured model-organism-description provider.
- `just deep-research-falcon SCHPO emp43 --fallback perplexity-lite` could not run: the local wrapper reported that `falcon` was unavailable, and the fallback reported that `perplexity` was unavailable.
- PAINT lineage-loss check: no IRD or IKR loss on the `emp43` lineage.

## Literature and database evidence

- The S. pombe Emp43 UniProt record identifies O42707/SPBC4F6.05c as an L-type lectin-like, type I single-pass membrane precursor with a large non-cytoplasmic domain and a short cytoplasmic tail [file:genes/SCHPO/emp43/emp43-uniprot.txt, "Single-pass type I membrane protein"].
- The PTHR12223 PAINT table places ERGIC, ER membrane, Golgi membrane, COPII vesicle, D-mannose binding and ER-to-Golgi transport on `PTN000259611`, the node inherited by S. pombe Emp43 [file:interpro/panther/PTHR12223/PTHR12223-paint.tsv, "PTHR12223\tPTN000259611"].
- Yamamoto et al. identify Emp43 as the S. pombe orthologue of human ERGIC-53 and report that it localizes to an ERGIC-like compartment [PMID:41203586, "identified Emp43 (SPBC4F6.05c) of Schizosaccharomyces pombe, an orthologue of human (Homo sapiens) ERGIC-53"].
- The same abstract reports that Emp43 localization depends on its C-terminal KYL motif and Ypt1, identifies Ssp120 as a functional partner, shows that the proteins interact and co-localize, and identifies Ght2 as a potential ligand [PMID:41203586, "Our findings indicate that Emp43 forms a complex with Ssp120"].
- The cached PMID:41203586 entry is abstract-only, so the direct PomBase IMP/IPI annotations from that paper are treated as full-text curation calls rather than reinterpreted from the abstract alone.

## GO-CAM context

Model `693b3c0900004859` enables S. pombe Emp43 with COPII receptor activity in the COPII-coated ER-to-Golgi transport vesicle and gives it a direct input edge to Sec24. The activity is consistent with a membrane cargo receptor whose luminal lectin domain works with Ssp120 and whose cytosolic tail can contact COPII machinery.
