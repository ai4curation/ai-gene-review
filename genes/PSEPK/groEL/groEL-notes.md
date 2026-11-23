# groEL review notes


## 2026-11-07 UTC — comparative GroEL-system evidence audit

Completed the previously DRAFT review after assessing all five rows. Replaced GO_REF-as-evidence and invented/paraphrased quotations with frozen HAMAP-curated target function, ATP-dependent reaction and location statements. PMID39169181 is full cached E. coli BL21(DE3) cryo-ET, not a KT2440 experiment. Conserved GroEL activity supports folding/refolding inference; stress-expression observations alone do not establish enzyme kinetics, exact client range or an interchangeable cross-species partner. Target cytoplasm is kept at curated granularity; no extra annotation was manufactured.

All original ordered annotation payloads, historical NEW actions and protected source/provider bytes were retained. No NEW rows were added. Existing provider research was used as a lead, with primary/curated evidence checked independently. PAINT-loss check completed: target was not a leaf in the cached family tree, so loss absence could not be established; no loss was invented.

Current actions: 5 ACCEPT. Status COMPLETE reflects completed adjudication, including explicit uncertainty, not proof of every tested proposition. Focused validation/render/history results and source preservation are recorded in the existing-member consultation proof.


## PR 6164 reference consultation (2026-11-07)

Restored the documented PMID:38987603 → PMID:39169181 citation correction as structured `reference_review.replacement` metadata on the original wrong reference. The earlier review at `6332a1d51e^` records the intended DOI `10.1038/s41586-024-07843-w`; cached publication identities and fresh NCBI EFetch metadata agree. The unrelated original paper is retained for provenance, with its real title, and is not marked invalid or used as biological support. See `analysis/module_audits/bacterial_groel_groes_chaperonin_folding/round1-reference-consultation/reference-identities.json`.

The description now presents the conserved group I double-ring, apical-client-binding and equatorial ATPase mechanism explicitly. Target evidence is the curated HAMAP MF_00600 assignment and UniProt function/subunit/catalytic statements. Detailed structural mechanism in PMID:39169181 is comparative E. coli evidence, not a KT2440 assay; neither target-specific client range nor a new RpoH regulatory claim is asserted. All five annotation actions and payloads remain unchanged.
