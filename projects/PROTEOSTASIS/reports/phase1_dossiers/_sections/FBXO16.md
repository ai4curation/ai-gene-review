## FBXO16

- **UniProt:** Q8IX29 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent. DR ↔ YAML agree FBXO16 is a nuclear-acting CRL1/SCF substrate receptor driving K48-linked degradation of beta-catenin, hnRNPL, ULK1, RELA/p65. Review ACCEPTs SCF complex (GO:0019005) and SCF-dependent catabolism (GO:0031146); GO:1990756 is the core MF, matching PN.
- **PN story / NEW pressure:** PN asserts the adaptor MF. GO:1990756 (verified real) is NOT in GOA for FBXO16 — but, as with FBXO8, it appears only in `core_functions`, not as a NEW `existing_annotation`; FBXO16 has NO MF annotation in its existing_annotations at all (only protein binding IPI + two NAS CC/BP). So the adaptor MF is a defensible ADD that the review states but does not formally annotate. Validated substrates present (not substrate-less).
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 at right altitude. Class GO:0061630 too_broad. A nuclear-localization theme (DR) is not yet annotated but PN does not assert it either.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:32296183 (binary interactome, LOW), 34445249 (SCF/ComplexPortal CPX-7926), plus Falcon substrate leads (Khan 2019, Ji 2021, Zhang 2024, Sugimoto-Ishige 2025). Expansion, no conflict.
- **Verdict:** Consistent; PN adaptor mapping appropriate and matches review core function.
- **Recommended edits:** [YAML] consider adding GO:1990756 as a NEW MF `existing_annotation` (currently FBXO16 carries no MF annotation; the adaptor activity lives only in core_functions) — mirrors the explicit NEW done for FBXO15. [MAP] none.
