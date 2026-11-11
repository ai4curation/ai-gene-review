# air-2 review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene worm air-2`; UniProt O01427 (AIR2_CAEEL) confirmed; 64 GOA rows.
- Cached extra PMIDs: 12213836, 10354474, 11914278, 15854913 (12707312 was already cached).
- Literature synthesis is in `air-2-deep-research-manual.md` (no provider deep research).

Key decisions:

- Core: AIR-2 is the Aurora B catalytic subunit of the CPC [PMID:12707312 "AIR-2/ICP-1/CSC-1/BIR-1 form a robust complex"].
  Direct in vitro substrates: REC-8, ICP-1, BMK-1, ZEN-4, TLK-1, KLP-7.
- `protein kinase activity` rows -> MODIFY to protein serine/threonine kinase activity (already carried by IDA).
- Bare `protein binding` rows: REMOVE, except the BMK-1 row (PMID:15548597) -> MODIFY to kinesin binding,
  matching the existing ZEN-4 kinesin-binding IPI.
- Centrosome / spindle pole IBA: AIR-2 is chromosomal/midzone; centrosomal localization is the
  Aurora A (AIR-1) property [PMID:9852156]. MARK_AS_OVER_ANNOTATED, not REMOVE (no experiment
  shows absence directly).
- Kinetochore IBA: worm CPC sits between kinetochore cups [PMID:20729837]; MARK_AS_OVER_ANNOTATED.
- Regulation of actomyosin contractile ring contraction (11050384, abstract only): the abstract
  places AIR-2/ZEN-4 in parallel to the CYK-1 contractile ring pathway; MODIFY to regulation of
  cytokinesis rather than remove.
- ComplexPortal NAS rows for SAC and sister chromatid separation: MARK_AS_OVER_ANNOTATED,
  consistent with the icp-1 review.
- No NEW rows: the meiotic chromosome segregation role is captured as a replacement on the
  chromosome segregation MODIFY rows, which already carry the IMP evidence.

Open: histone H3 kinase IDA/IMP cite PMID:14614817 (TLK-1 transcription paper, abstract only);
deferred to curator.
