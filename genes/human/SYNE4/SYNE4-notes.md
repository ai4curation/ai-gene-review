# SYNE4 (nesprin-4) curation notes

## 2026-09-27 — initial review (claude-code)

Sources: UniProt Q8N205, cached GOA-cited papers, PMID:19164528 (abstract only), PMID:23348741, and papers
fetched after reading `SYNE4-deep-research-falcon.md`: PMID:36211453 (Taiber 2022), PMID:33350593 (Taiber 2021).

### Biology
- 404-aa ONM KASH protein; kinesin-1 binding, SUN-dependent ONM localization [PMID:19164528 "Nesp4 is a
  kinesin-1-binding protein that displays Sun-dependent localization to the ONM."].
- LEWD motif (aa 243-246) mediates Kif5b binding; LEWD->LEAA mutant fails to rescue OHC nuclear position and
  hearing in vivo [PMID:36211453 "Thus, the LEWD interaction domain in Nesprin-4 is required for proper nuclear
  positioning, hearing function, and survival of OHC."].
- SUN1-KASH4 / SUN2-KASH4 6:6 complexes with zinc coordination by CCSH motif [PMID:33393904]; SUN2-KASH4 crystal
  structure [PMID:33058875].
- Hair cells: Nesp4 and Sun1 KO mice lose basal OHC nuclear position, then OHCs degenerate [PMID:23348741 "These
  results demonstrate that nesprin-4 and Sun1 play an essential role in the basal positioning of OHC nuclei and at
  the same time are essential for the maintenance of OHC viability."]; human c.228delAT causes DFNB76.
- Expressed mainly in secretory epithelia (e.g. salivary gland) and cochlear hair cells (OHC and IHC).

### Decisions
- 54 protein-binding rows: SUN1/SUN2 (structural papers) MODIFY -> GO:0140444; KLC4 rows (Y2H and BioPlex AP-MS)
  MODIFY -> GO:0019894 kinesin binding; remaining 49 HT hits REMOVE (sticky TM protein; uninformative).
- GO:0034993 -> MODIFY GO:0106094 (all three rows).
- GO:0045198 apical/basal polarity (IBA/IEA/ISS from mouse IMP, Roux 2009) KEEP_AS_NON_CORE: KO OHCs form and
  polarize normally; the specific defect is nuclear position.
- NEW GO:0140444 (ISS; comparator: SYNE1/2/3 and SUN1/2 carry it) and NEW GO:0051647 nucleus localization (ISS;
  participation: nesprin-4 is the kinesin attachment site on the nucleus; LEWD-mutant rescue failure).
- Did not add sensory perception of sound (downstream of OHC survival); raised as a question.

### For the LINC module
- MF GO:0140444 (+ GO:0019894 kinesin binding); location GO:0005640; complex GO:0106094 with SUN1 (hair cells);
  cytoskeletal partner kinesin-1 (KIF5B/KLC via LEWD) -> microtubules; restricted expression (secretory epithelia,
  cochlear hair cells); disease DFNB76.
