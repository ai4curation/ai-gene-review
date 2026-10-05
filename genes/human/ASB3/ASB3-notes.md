# ASB3 notes

- Substrates: TNF-R2 (PMID:15899873), MAVS K297 K48 (PMID:39266719), TRAF6 K48 (PMID:39162488), DR5 (PMID:38334450).
- NEW GO:0039536. Comparator check: RNF125, an E3 degrading RIG-I pathway components, carries it (QuickGO 2026-10-04). ASB3 performs the inhibitory step by degrading MAVS.
- The cancer phenotypes (PMID:28088228, PMID:31016535) and the testis knockout with no defect (PMID:40755808) are not annotated.

## 2026-10-04 review round (PR #4252)

- **No GO:0031466 row.** PMID:15899873 shows SOCS-box recruitment of Elongin B/C [PMID:15899873 "the SOCS box of ASB3 is responsible for recruiting the E3 ubiquitin ligase adaptors Elongins-B/C"]. UniProt records ELOB binding. Neither cached source shows Cullin 5 itself; Elongin BC also partners Cullin 2, and the family survey PMID:16325183 does not name ASB3 in its abstract. This matches ASB13. ASB10's ISS row was a paralog transfer that I would not repeat.
- **No NF-kB process term for the TRAF6 arm.** The MAVS arm has a direct pathway readout (TBK1/IRF3 phosphorylation, IFN-beta) and comparators that carry GO:0039536 (RNF125, UFD1, NPLOC4). The TRAF6 arm rests on IkBa phosphorylation in colitic tissue of knockout mice. TRAF6 also feeds MAPK and other pathways. A comparator check found that TRIM38, a TRAF6-degrading E3, lacks GO:0043124 (QuickGO 2026-10-04). Recorded as a candidate rather than asserted.
