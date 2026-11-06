# Bacterial cellulose comparative audit

The module distinguishes common polymerization from five support/envelope architectures. The reviewed panel covers 21 genes across Pseudomonas, Rhodobacter, Agrobacterium, E. coli, Komagataeibacter, cyanobacteria and Streptomyces. Seventeen curated references include three comparative reviews.

Run `uv run python modules/bacterial_cellulose_biosynthesis-source-analysis/check_audit.py` from the repository root to verify original annotation payloads and raw hashes and replay 27 scenarios through the production module compiler. These are checks of the reviewed panel, not exhaustive genome capacity predictions. Family names alone do not establish chemistry. The synthetic GT2 negative case tests the functional restriction; it is not a claim about an actual inactive CslA.

`seed-baseline.yaml` retains 88 original payloads, including one inherited NEW row. Thirteen newly proposed annotations are separate. `provider-source-preservation.yaml` records 12 unchanged existing research artifacts. `selector-scope-findings.yaml` records corrections to family constraints and database prose.

TypeIII and cyanobacterial envelope roles are deliberately unresolved required obligations, reported as abduction targets. They must not become empty compiler branches that silently evaluate true. Native cellulose production in these organisms is not contradicted by incomplete machinery coverage. The Streptomyces route establishes binary-complex cellulose synthesis in vitro; native glycan composition remains unresolved. E. coli intact/repaired BcsQ and the native K12 pseudogene fragment are distinct scenarios.

`validation-results.yaml` records focused checks and the separately tracked repository-wide run. No pending run is represented as a pass. Existing PR2143 is adopted rather than replaced by a new cellulose PR.

The full 10,553-review validation run finished with 19 blocking reference failures in 17 unrelated yeast reviews. Their review/source/validation-input blobs are unchanged from the audit base; the exact errors and hashes are recorded in `preexisting-reference-failures.yaml`. Schema, ontology, best-practices and pathway checks pass. This is a scoped clean audit with documented repository-wide failures, not an unconditional full-corpus pass.

The generic BcsB/BcsC branch now carries positive sampled-lineage contexts. Two explicit oracle cases show that family predicates alone permit an E. coli bypass and that external context enforcement rejects it. Neither genus membership nor a positive machinery result proves native expression, extracellular cellulose production or genus-wide BcsQ dispensability. The production compiler delegates context to its caller.

Round15 follow-up adds two explicit frozen-GOA controls: RKN E5RST0 and TK24 A0ABM5R5V5 are admitted by reviewed biochemical refinements, while unchanged GOA alone remains insufficient. The 27 cases make this dependency visible. Catalytic BcsA UDP-glucose metabolism is retained consistently, and AcsD has an explicit noncatalytic core summary. All original payloads and sources remain unchanged.

Round16 follow-up checks all five catalytic BcsA donor-metabolism claims across the panel. Each retains GO:0006011 and includes it in the catalytic core. PSEPK and CERS4 also retain product-pathway coverage through separately supported NEW cellulose-process rows; the E. coli specific process row and existing AGRFC/KOMXY rows remain. All 88 original payloads are preserved, yielding 101 current rows. Fresh full-corpus validation is pending after these focused checks.

## Round17 specificity and provenance

The bacterial subtype GO:0090540 is now used consistently for all already-supported process claims and module concepts. It adds bacterial context to GO:0030244, without adding a native-output or fibril criterion; purified CERS4 IDA and PSEPK homology inference remain distinct. The frozen target RuleBase statement and explicit ISS donor are restored. Official IPR044846 metadata supports the existing label.

The immutable historical ledger contains 87 machine payloads and one historical authored PP_2634 proposal. The machine payloads remain unchanged. The latter proposal is archived as exact original YAML and refined under a checker exception pinned to its accession, path, index and both exact payloads. Thirteen additional authored proposals remain separately counted; three existing terms are refined, and no rows are added or deleted. Current total: 101 rows. All 42 raw files, 12 provider artifacts and 178 scoped source files remain unchanged.

Thirteen gene validations, 14 new history validations, module/schema checks, 27 capacity cases, five catalytic donor/product checks, six checker controls, rendering and diff checks pass. The five catalytic checks require GO:0090540 in both reviewed functions and their cores. Detailed results and hashes are in `round17-followup.yaml`.

The pre-round17 full run terminated with exit 1 at science commit 04a28f01332c3ffc6900650249d5fe7c6bf2db8c, reproducing the same 19 reference errors in 17 unrelated unchanged yeast reviews. All 23 source/validation-input blobs in the preexisting proof were rechecked. This run does not validate the subsequent round17 edits; a fresh full run is pending and owned by the parent agent. See `round16-fullrun-terminal.json`.
