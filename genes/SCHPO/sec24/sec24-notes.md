# sec24 review notes

## Setup

- `just fetch-gene SCHPO sec24` created the review stub, GOA seed, and UniProt cache, and fetched the PTHR13803 Sec24 PANTHER family.
- `just fetch-gene-pmids SCHPO sec24` found all cited PMIDs already present.
- `just mod-description-deep-research SCHPO sec24` skipped because `SCHPO` has no configured model-organism-description provider.
- `just deep-research-falcon SCHPO sec24 --fallback perplexity-lite` could not run: the local wrapper reported that `falcon` was unavailable, and the fallback reported that `perplexity` was unavailable.
- PAINT lineage-loss check: no IRD or IKR loss on the `sec24` lineage.

## Literature and database evidence

- S. pombe Sec24 is the single full-length fission-yeast member of the fungal Sec24 clade in the PTHR13803 family table, grouping with budding-yeast SEC24 in PTHR13803:SF39.
- The S. pombe UniProt record assigns Sec24 to the SEC23/SEC24 family and SEC24 subfamily and carries the conserved Sec23/24 trunk, helical, beta-sandwich, gelsolin-like, vWA-like, and zinc-finger-like regions.
- Conserved COPII literature supports Sec24 as the inner-coat cargo receptor/adaptor: activated Sar1 recruits Sec23/Sec24, and Sec24 captures transmembrane cargo during pre-budding complex formation [PMID:27432890, "Sar1-GTP on the ER membrane recruits Sec23 and Sec24 forming an inner layer on COPII-coated vesicles through the interaction with Sec23, and the transmembrane cargo is captured by the contact with Sec24 to form a pre-budding complex"].
- Davis et al. describe budding-yeast Sec24 as the major COPII cargo adaptor that recruits biosynthetic cargo and SNAREs into Golgi-directed COPII vesicles [PMID:27855785, "Sec24, the major cargo adaptor of the COPII coat, recruits biosynthetic cargo and SNAREs"].
- Vjestica et al. are the source for direct PomBase Sec24 localization rows. The cached record is abstract-only, but the abstract confirms a fission-yeast survey of markers for the ER, COPII sites, and early and late Golgi during division-site polarization [PMID:18184749, "These included markers for the endoplasmic reticulum, the COPII sites, and the early and late Golgi"].

## GO-CAM context

Model `693b3c0900004859` enables Sec24 cargo-adaptor activity as the hub that receives input from COPII cargo receptors during cargo loading. The gene annotations already capture the expected cargo adaptor activity, SNARE binding, COPII coat membership, ER-to-Golgi vesicle traffic, and ER-exit-site localization.
