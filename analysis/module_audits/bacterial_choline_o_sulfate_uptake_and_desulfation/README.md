# Choline-O-sulfate uptake and desulfation audit

The two required roles are intact COS import and BetC hydrolysis. Bacillus OpuC
supplies a resolved import implementation, with four distinct subunit types and
complex-level cargo evidence. Its native strains accumulate COS intact and are
not full-pathway exemplars. KT2440 intact-accumulation physiology establishes
uptake without identifying its transporter. BetD/BetE candidates remain optional
context. Ruegeria BetT is a transporter candidate with a choline-depletion phenotype and a COS growth phenotype. Downstream betA polarity remains unresolved, so neither phenotype establishes its cargo. Native compartments remain unresolved for all three BetC exemplars.

Ten COMPLETE member reviews span Pseudomonas, Sinorhizobium, Bacillus and Ruegeria.
The BetC-specific NCBIfam signature is preferred to a heterogeneous PANTHER
sulfatase family. OpuC family names do not specify cargo or distinguish every
related transporter; independent subunit identity and cargo evidence are required.
OpuCD has conflicting official PANTHER and UniProt placements, documented as an
advisory rather than silently changed. No family ID is invented for Ruegeria BetT.

Three comparative reviews and nine primary papers provide curated findings and
step/connection evidence. Original source strains, recombinant constructs and
reference strains are distinguished. In particular, Sinorhizobium 102F34R, 1021
and CECT 4857 evidence are not interchangeable; OpuCC structure-to-sequence and
Ruegeria locus/primer mappings are recorded in the gene source analyses.

Run `uv run python modules/bacterial_choline_o_sulfate_uptake_and_desulfation-source-analysis/check_audit.py`.
The 34 cases use the production compiler with explicit cargo, complex-member,
curated-role and strain-specific physiology predicates. Missing units, a generic
same-family ATPase, generic transporter activity and growth-only evidence do not
close the import step. False means unresolved panel coverage, not pathway absence.
The checker is not a genome-wide predictor or a cross-species assembly model.

All 38 historical rows (37 machine rows and one inherited proposal), 20 raw
UniProt/GOA files and 12 inherited provider artifacts are preserved. Eleven new
annotations give 49 current rows. One earlier authored choline-transport proposal is withdrawn from active assertions and archived verbatim. New process terms were not manufactured from
necessity evidence. Falcon attempts failed with HTTP 403; manual literature notes
and primary-source identity checks record the work actually performed.

Focused gene/module/history checks and rendering pass.

Before round1 follow-up, full-corpus validation finished across 10,542 reviews. Schema, ontology and best-practices have zero blocking errors, and all 54 pathway files with PMIDs pass. Exit status 1 is solely due to 19 reference errors in 17 unrelated yeast reviews. The committed failure inventory proves all 23 review/source/configuration inputs are unchanged from the audit base. There are 115 ontology label advisories, 52 reference advisories and 27,996 best-practice warnings repository-wide.

Round1 focused checks pass. The fresh full-corpus validation on cb46f285c4 completed with exactly the same 19 reference errors in 17 unrelated yeast reviews; all 23 underlying input blobs are unchanged. Schema, ontology, best-practices and 54 pathway checks pass. The capacity predicates distinguish enabled activities from explicit contributes_to corrections and reject the unresolved SPO1087 cargo candidate. KT2440 intact-COS uptake physiology supports the import role without assigning a native BetC compartment or claiming compartment-resolved flux.

PR #6105 science commit cb46f285c4 is approved. The completion ledger and an AST-identical checker formatting fix are recorded; current-head review/CI and actual merge remain pending.
