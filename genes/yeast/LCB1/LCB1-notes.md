# LCB1 notes (P25045, YMR296C)

- SPT subunit; LCB1 and LCB2 both required [PMID:1556076 "Membrane preparations from both lcb1 and lcb2 mutant strains exhibited negligible SPT activity when tested in vitro."]; [PMID:8058731 "overproduction in Saccharomyces cerevisiae requires expression of LCB1, a previously isolated yeast gene, and LCB2"].
- Heterodimer, mutual stability [PMID:10713067 "Lcb2p is unstable in cells lacking Lcb1p and vice versa."].
- PLP Schiff-base lysine annotated only on Lcb2 (K366) [UniProt:P40970]; Lcb1 is the non-catalytic partner (as SPTLC1) -> core MF recorded as contributes_to; PLP-binding IEA on Lcb1 marked over-annotated.
- SPOTS complex [PMID:20182505 "we term the SPOTS complex (Serine Palmitoyltransferase, Orm1/2, Tsc3, and Sac1)"].
- IBA 'sphingosine biosynthetic process' -> MODIFY to sphingoid biosynthetic process (yeast makes DHS/PHS, no sphingosine).
- YeastPathways RCA cytosol -> REMOVE (integral ER membrane).
- Decisions: 8 PB REMOVE, cytosol RCA REMOVE, 2 MARK_AS_OVER_ANNOTATED (cytoplasm, PLP binding), 1 MODIFY, 1 KEEP_AS_NON_CORE (sphingolipid homeostasis NAS; Lcb1 is the regulated target of Orm1/2), 16 ACCEPT.
