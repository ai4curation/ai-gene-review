## FBXO10

- **UniProt:** Q9UK96 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|CASH` (aux domain IPR006633) ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent and well-aligned. Review explicitly executes the canonical F-box pattern: two NAS GO:0004842 ubiquitin-protein transferase annotations MODIFY → GO:1990756 (verified real), exactly matching the PN projection. DR ↔ YAML agree on BCL2/HGAL/PGAM5/RAGE substrates and SCF(FBXO10) membership.
- **PN story / NEW pressure:** PN asserts the adaptor MF; review supplies it via MODIFY of the wrong catalytic-transferase terms — already captured/improved, not over-reach. Beyond the PN family story, the review carries substantial extra biology (apoptosis via BCL2 IMP PMID:23431138; mitochondrial OMM PGAM5 degradation; species caveat from Fbxo10 KO mice) that PN does not assert. No additional NEW GO pressure beyond GO:1990756. Validated substrates present (not a substrate-less F-box).
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 is at correct altitude (matches the review's MODIFY replacement target). Class GO:0061630 correctly too_broad.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:23431138 (BCL2), 31570756 (HGAL), 34445249 (SCF), 10531035/10531037 (family cloning, source of the transferase NAS terms), plus Falcon PGAM5/RAGE leads. Expansion, no conflict.
- **Verdict:** Consistent; review already implements the PN adaptor-MF mapping via MODIFY GO:0004842→GO:1990756.
- **Recommended edits:** none to FBXO10-ai-review.yaml. [MAP] none — node mapping and review concur.
