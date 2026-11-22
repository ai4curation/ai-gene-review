# RAB9A notes

## 2026-11-22 ORGANELLES lysosome batch 2

- Two lysosome (GO:0005764) rows (IBA is_active_in, MGI IDA PMID:15078902) moved ACCEPT -> KEEP_AS_NON_CORE.
- PMID:15078902 (Seaman 2004, full text cached, read): the only Rab9 data are GFP-rab9 stably
  expressed in HeLaM cells, compared with mVPS26 ("very little overlap"), without a lysosome or late
  endosome marker. The lysosome is stated only in background citing a review
  [PMID:15078902 "rabs 7 and 9 are present on late endosomes (and some lysosomes) (Pfeffer, 2003)"].
  Recorded a WRONG_EVIDENCE_CODE CHECK (PROBABLE) source defect against MGI; candidate replacement
  reference PMID:20937701. The late endosome IDA from the same paper rests on the same sentence
  (out of scope; reason annotated, action unchanged).
- Readable human line: PMID:20937701 (Yoshimura 2010, full text cached)
  [PMID:20937701 "As expected, Rab9 was present on LAMP1-positive lysosomes defined by the marker LAMP1"];
  EGFP-Rab9A in HeLa; Rab9 depletion clusters lysosomes perinuclearly. One tagged line plus a
  positioning phenotype: root, not a sub-compartment.
- The activity (MPR retrieval late endosome -> TGN) acts at late endosomes, so non-core;
  WRONG_QUALIFIER CHECK on the IBA. Same IBD (PTN000635769) and same call as RAB9B.
- Cycling recruitment of a prenylated RAB is not tethering: no GO:0098574 row.
