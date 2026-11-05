# didum review notes

## Session 1

- fetch-gene by symbol timed out (UniProt stream endpoint); fetched by accession:
  `just fetch-gene DROME A1Z6Z8 --alias didum`. UniProt id confirmed A1Z6Z8 (FlyBase FBgn0261397, GeneID 35680). 43 GOA rows.
- Literature synthesis in didum-deep-research-manual.md (no deep-research API).
- Full text read: PMID:22105348 (Crb stabilizes MyoV; MyoV at rhabdomere base; Rh1 transport), PMID:17517962 (Rab11/dRip11/MyoV), PMID:18585038 (pigment granules). Others abstract-only.

### Key decisions
- Core MF: microfilament motor activity (ensemble, non-processive) [PMID:15980429 "it is a nonprocessive, ensemble motor"].
- myosin complex rows -> MODIFY to myosin V complex (already carried by IPI).
- cytoskeletal motor activity (IEA) -> MODIFY to microfilament motor activity.
- mitochondrion transport along microtubule (IDA, PMID:20592219): RNAi depletion INCREASES MT-based transport; MyoV opposes it [PMID:20592219 "they oppose, rather than complement, protracted MT-based movements"]. MODIFY to regulation of organelle transport along microtubule (no negative-organelle term exists; GO:0061882 is anterograde-only, while effect was bidirectional).
- IBA endocytosis: node PTN008546178 seeds checked against UniProt: MYO6 (human/pig/chicken), mouse Myo6, Myo7a, and yeast MYO2 (only class V seed). Endocytosis is a myosin VI hallmark; no fly evidence for MyoV in endocytosis -> MARK_AS_OVER_ANNOTATED with propagation_review.
- ARBA developmental terms: imaginal disc morphogenesis, tissue development -> over-annotated; regionalization -> MODIFY to A/P axis specification, embryo (posterior group gene).
- Calmodulin binding / myosin V complex IPI from PMID:15178316: abstract is about murine myosin-V IQ peptides; calmodulin is nonetheless a genuine Drosophila MyoV light chain (IPI from PMID:15980429 for light chain binding with Cam). ACCEPT, defer to curator; flagged for expert.
- NEW: vesicle transport along actin filament (PMID:17517962), pigment granule transport (PMID:18585038), small GTPase binding (Rab11; PMID:17517962, PMID:25940004). In each, MyoV is the motor that does the work (passes the NEW bar: it performs the transport step / binds the GTPase directly).

## 2026-10-28 review fixes

Reworded the NEW GO:0030050 reason: it is the more specific is_a descendant of the ACCEPTed GO:0030048 row, not its parent.
