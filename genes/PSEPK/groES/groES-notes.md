# groES review notes


## 2026-11-07 UTC — comparative GroEL-system evidence audit

Replaced invalid quotation/support and the wrong Q88DS3 accession in the metal rationale. Q88N56 is the frozen 97 aa GroES. Curated HAMAP function supports GroEL binding/capping; the core records contribution to assembled ATP-dependent folding. The true GO0044183 row remains accepted. ATP binding and metal binding are UNDECIDED: E. coli counter-assays and mycobacterial metal-site structures do not by themselves resolve every homolog. No KT2440 purified assay or native ion-regulatory role is asserted. Detailed chamber studies are comparative, and expression induction alone is not functional chemistry.

All original ordered annotation payloads, historical NEW actions and protected source/provider bytes were retained. No NEW rows were added. Existing provider research was used as a lead, with primary/curated evidence checked independently. PAINT-loss check completed: target was not a leaf in the cached family tree, so loss absence could not be established; no loss was invented.

Current actions: 4 ACCEPT, 2 UNDECIDED. Status COMPLETE reflects completed adjudication, including explicit uncertainty, not proof of every tested proposition. Focused validation/render/history results and source preservation are recorded in the existing-member consultation proof.


## PR 6164 reference consultation (2026-11-07)

Restored the documented PMID:38092042 → PMID:38064510 citation correction as structured `reference_review.replacement` metadata on the original wrong reference. The earlier review at `6332a1d51e^` records the intended DOI `10.1073/pnas.2308933120`; cached publication identities and fresh NCBI EFetch metadata agree. The unrelated original paper is retained for provenance, with its real title, and is not marked invalid or used as biological support. See `analysis/module_audits/bacterial_groel_groes_chaperonin_folding/round1-reference-consultation/reference-identities.json`.

Added the GroEL-GroES complex relationship to the core function: target HAMAP-curated UniProt FUNCTION explicitly says GroES binds and caps the GroEL ring, independently of the comparator pattern. Official QuickGO GO:1990220 defines the assembled GroES heptamer and GroEL tetradecamer; GroEL supplies ATPase activity. The existing `contributes_to_molecular_function` remains distinct from independent ATPase activity. All six annotation actions and payloads remain unchanged; no NEW row was added. BACSU and MYCTU already carry the contribution relationship, so that reviewer suggestion requires no change there.
