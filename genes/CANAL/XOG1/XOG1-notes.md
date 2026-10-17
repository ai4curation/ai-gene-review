# CANAL XOG1 notes

## 2026-10-10

Reviewed `PTHR31297` for the fungal glucan exo-1,3-beta-glucosidase branch. XOG1 sits in `PTHR31297:SF1`, and the precise PAINT assertions for extracellular region and fungal-type cell wall beta-glucan metabolism are placed on `PANTHER:PTN001262686`; the catalytic `GO:0004338` assertion is one node lower at `PANTHER:PTN001262687`. Both placements are supported by the Candida seed itself plus budding-yeast and PomBase exoglucanases, so the XOG1 IBAs are retained as node-level inheritance calls rather than treated as simple similarity transfer.

Core activity is well established. XOG1 disruption removes the major C. albicans exoglucanase activity [PMID:9308184, "this gene is responsible for the major exoglucanase activity in C. albicans"], purified Exg prefers beta-1,3-glucosidic substrates and also catalyzes beta-1,3 transglucosylation [PMID:10469155, "Exg catalyses an efficient transglucosylation reaction"], and Glu-330 is the catalytic nucleophile [PMID:9013549, "A crucial role for Glu-330 is confirmed by site-directed mutagenesis"].

The adhesion and biofilm annotations are biologically real but downstream of the glucanase activity. Xog1 binds the LL-37 antimicrobial peptide and LL-37 inhibits Xog1-associated adhesion [PMID:21713010, "One Xog1p-derived peptide, Xog1p(90-115), and recombinant Xog1p associated with LL-37"], so the old `cell adhesion molecule binding` row should be redirected to peptide binding. Taff et al. show that Bgl2/Phr1/Xog1 deliver beta-1,3-glucan to biofilm matrix, but explicitly note that the enzymes are not required for filamentation or biofilm formation [PMID:22876186, "nor are they necessary for filamentation or biofilm formation"], so the broad biofilm formation rows overstate the more precise matrix-glucan delivery role. Newer host-surface work found that Xog1 and Eng1 affect epithelial adhesion and surface glucan exposure, but Eng1 plays the greater role in lactate-induced beta-1,3-glucan masking and Xog1 itself is only a minor contributor to shaving under the assayed conditions [PMID:38938582, "this major exoglucanase does not make a major contribution to lactate-induced β-1,3-glucan shaving"].

The only row left unresolved is the PMID:31412284 extracellular-vesicle localization. The local cache is abstract-only and describes the EV proteomics screen, but the abstract does not name XOG1; leave `GO:1903561` as `UNDECIDED` until the supplemental protein table is checked.

Follow-up cleanup: tightened the PMID:7975893 support for the Candida XOG1
reporter-gene IGI row and added the extracellular-vesicle supplemental-table
check as a suggested question.
