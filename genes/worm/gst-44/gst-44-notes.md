# gst-44 review notes

## 2026-10-28 session

- Fetched O45352 (gst-44, F13A7.10, WBGene00001792, GeneID 184405); 11 GOA rows (4 IBA, 6 IEA, 1 IMP).
- Key primary paper: PMID:40186509 (Kaiser et al. 2025), full text cached. Recombinant GST-44 has
  DHAR, MMA(V) reductase, thioltransferase (HEDS) and cumene-hydroperoxide peroxidase activity, but
  no CDNB/ethacrynic acid conjugation [PMID:40186509 "For the typical GST substrates 1‐chloro‐2,4‐dinitrobenzene (CDNB) and ethacrynic acid, no GSH‐conjugating activity could be shown (data not shown)."].
- PMID:23593298 (IMP source for GO:0000302): gst-44 RNAi affected arsenite survival only; juglone
  survival 90.0 +/- 3.3% (control 90.8). The WormBase term "response to reactive oxygen species"
  does not match the reported phenotype -> MODIFY to GO:0046685 response to arsenic-containing
  substance, plus source_defects (WRONG_TERM, WB).
- GO:0004364 glutathione transferase activity (IBA + IEA): marked over-annotated; omega-class
  enzymes are thiol/redox enzymes and GST-44 itself showed no conjugation.
- New rows proposed: GO:0004601 peroxidase activity (IDA; cumene hydroperoxide is an organic
  hydroperoxide, so GO:0004602, defined on H2O2, is not used) and GO:0071722 detoxification of
  arsenic-containing substance (IMP; the enzyme catalyses an arsenical reduction step and the
  deletion is specifically arsenic-sensitive among the GSTO paralogs).
- Thioltransferase (HEDS) activity is not added as GO:0015038 glutathione disulfide oxidoreductase
  activity because GO:0045174 (already accepted) is_a GO:0015038 (checked in OLS).
- Nuclear GFP signal is weak and from an extrachromosomal translational reporter; not annotated.
- Curation follow-up (not a knowledge gap): the paper's "arsenate reductase" wording refers to an
  MMA(V) assay; inorganic arsenate reduction was not measured.
