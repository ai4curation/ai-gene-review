## FBXO15

- **UniProt:** Q8NCQ5 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent. Review adds GO:1990756 as an explicit `action: NEW` MF annotation (GOA had no MF for FBXO15), which directly realizes the PN projection — tighter alignment than most siblings. DR ↔ YAML agree on the SCF adaptor role and reported substrates (CLS1, ABCB1/P-gp, SOX2, STAT3).
- **PN story / NEW pressure:** PN asserts the adaptor MF; review ADDs it as NEW (GO:1990756, verified real). This is a defensible ADD, not over-reach: UniProt states FBXO15 is a substrate-recognition component directly interacting with SKP1 and CUL1, and ComplexPortal has an FBXO15-variant SCF complex. Substrate links rest on single studies (Falcon UNVERIFIED), but family/complex membership is solid; not a substrate-less F-box at the family level.
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 is at the right altitude (= the NEW MF the review added). Class GO:0061630 correctly too_broad.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:34445249 (SCF/ComplexPortal CPX-7925), 32814053 (JPH3 Y2H, bare protein binding, LOW), plus Falcon substrate leads. The one experimental annotation (protein binding/JPH3) is non-core. Expansion, no conflict.
- **Verdict:** Consistent; review's NEW GO:1990756 exactly implements the PN adaptor mapping.
- **Recommended edits:** none to FBXO15-ai-review.yaml. [MAP] none — node mapping and review concur.
