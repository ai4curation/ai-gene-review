# mek-2 annotation review notes

## 2026-09-30 seeded GOA review

Provider deep research was unavailable in this environment, so this pass relied on the seeded GOA rows, the local UniProt record, the four cached PMID abstracts, and local GO-CAM/Reactome checks.

- `PMID:7729690` is the key primary source for MEK-2 itself. Its abstract reports that C. elegans MEK-2 can phosphorylate and activate human ERK1, can itself be phosphorylated and activated by Raf, acts between `lin-45`/Raf and `sur-1/mpk-1`, and is required for efficient Ras-mediated vulval induction.
- `PMID:10409742` supports the `GO:0097110` scaffold protein binding row by showing MEK binding to the KSR scaffold. The row was kept as non-core because this interaction localizes/regulates MEK in the Ras/MAPK module rather than naming the catalytic activity.
- `PMID:11861555` supports the LET-60/LIN-45/MEK-2/MPK-1 ordering used for the Ras protein signal transduction and vulval-development IGI rows. Ras signal transduction was treated as direct pathway biology; the four vulval development rows were kept as non-core developmental outputs.
- `PMID:15268855` supports the `GO:0000165` and `GO:0050830` infection-response rows. The MAPK cascade row was accepted as direct ERK-cascade signaling, while defense response to Gram-positive bacterium was kept as a non-core M. nematophilum-specific physiological deployment of the cascade.
- Broad kinase terms from InterPro, ARBA, and Rhea were modified to `GO:0004708` MAP kinase kinase activity when they represented the same dual-specificity MAP2K chemistry at lower specificity. The generic ARBA `GO:0006950` response to stress row was removed after PR follow-up because replacing it with `GO:0050830` defense response to Gram-positive bacterium would duplicate an existing, experimentally supported IMP row.
- Local GO-CAM search found no production model indexed to `WB:WBGene00003186`; a PAINT cached GO-CAM includes `mek-2` only as a with-object for the ancestral MAPK-cascade inference. The cached Reactome files corroborate conserved human MEK1/MEK2 phosphorylation of ERK1/ERK2, but no worm-specific Reactome event was present locally.
