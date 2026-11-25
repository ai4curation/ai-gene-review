# RAB7B notes

## 2026-11-22 ORGANELLES lysosome batch 2

- Three lysosome (GO:0005764) rows (IBA is_active_in, combined IEA GO_REF:0000120, IDA PMID:20375062)
  moved ACCEPT -> KEEP_AS_NON_CORE; lysosome removed from the myosin II core function's locations.
- Lines: two abstract-only human papers state a lysosome association positively
  [PMID:15144907 "By immunofluorescence confocal microscopy, we demonstrate that Rab7b is associated with lysosomal organelles."]
  [PMID:20375062 "wild-type Rab7b is lysosome associated whereas an activated, GTP-bound form of Rab7b localizes to the Golgi apparatus"].
  Neither abstract names the marker or says whether the protein was endogenous. PMID:15144907 fetched
  (abstract only).
- The activity is retrograde transport from late endosomes to the TGN; "required for normal lysosome
  function" rests on cathepsin D maturation, a read-out of that retrieval. So root kept, non-core.
- IEA GO_REF:0000120 = ARBA00028565 + Ensembl projection from mouse Rab7b Q8VEA8 (UniProt lysosome
  item curated from PMID:17395780 and PMID:19587007, checked on the UniProt record, papers not read)
  + human SL-0158 keyword (curated from the two papers above).
- PAINT IBD PTN000635769 (PTHR47981) seeds: Rab7 lineage (human RAB7A, mouse Rab7 MGI:105068, rat,
  fly, worm, Dictyostelium), mouse Rab7b (MGI:2442295), RAB9A and RAB7B. MGI symbols checked via the
  Alliance API. WRONG_QUALIFIER CHECK defect added on the is_active_in IBA.
- Cycling recruitment of a prenylated RAB is not tethering: no GO:0098574 row.
- Fixed a pre-existing non-verbatim deep-research quote (TBC1D5 finding) so the file validates
  without its local quote baseline entry.
