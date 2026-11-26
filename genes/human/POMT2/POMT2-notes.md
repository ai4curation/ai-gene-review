# POMT2 notes

## 2026-11-22 review

Deep research via `just deep-research-falcon human POMT2 --fallback perplexity-lite` failed locally:
the first sparse run lacked `templates/gene_research_go_focused.md`, and after adding `templates/`
the configured deep-research client exposed only the `claude_code` provider. I therefore reviewed the
POMT2 GOA rows manually from the cached UniProt record, GOA fetch, PANTHER `PTHR10050` PAINT slice,
the existing POMT1 review, the mouse production GO-CAM for protein O-linked glycosylation, and three
locally cached POMT primary papers.

PMID:14699049 is the direct biochemical paper for the mammalian POMT assay. It shows that human
POMT1 and POMT2 must be coexpressed in HEK293T cells to raise microsomal transfer of radiolabeled
mannose from Dol-P-Man to GST-alpha-dystroglycan above background, and alpha-mannosidase sensitivity
confirms an alpha-O-glycosidic Man-Ser/Thr product. This supports the specific EC 2.4.1.109 /
GO:0004169 activity and the POMT1:POMT2 complex model.

PMID:16698797 is abstract-only in the local cache, but its abstract states that POMT1 forms a
physical and functional complex with POMT2 that has protein O-mannosyltransferase activity. This is
enough for the ComplexPortal `part_of GO:0031502` and `involved_in GO:0035269` rows, and I did not
try to re-fetch or refresh the existing PMID cache.

PMID:28512129 used POMT1/POMT2 knockouts in CHO and HEK293 cells and found that either single
knockout eliminated alpha-dystroglycan O-Man glycopeptides but did not remove cadherin/protocadherin
O-mannosylation. This supports the UniProt IMP rows while narrowing the biological reading: POMT2 is
not the universal enzyme for every mammalian O-Man site, but it is essential for the classical
POMT-dependent alpha-dystroglycan/KIAA1549 route.

`just paint-losses human POMT2` reported no IRD or IKR loss on the human POMT2 lineage. The PAINT
IBD row at `PTN008936969` carries both GO:0004169 and GO:0035269 across the whole `PTHR10050` tree,
including bacterial Pmt leaves, and the ER row at `PTN001295889` starts below the bacterial branch.
The `PANTHER:PTN001295889` row includes human POMT1 and POMT2 as seeds, which is the expected
self-seeded IBA pattern for an experimentally grounded target.

Module fit: the family contributes the obligate POMT1:POMT2 complex, a real two-subunit ER enzymatic
module. The existing Drosophila protein O-glycosylation module has a Rotated abdomen/Twisted POMT
complex variant with the same `GO:0031502` complex term. The cached mouse production GO-CAM
`6690711d00001433` covers the alpha-dystroglycan pathway and pins the mouse Pomt1/Pomt2 complex to
`GO:0004169` in the ER membrane, so the human module references that GO-CAM rather than creating a
new GO-CAM review for a mouse model.
