# Choline-O-sulfate uptake and desulfation audit

The two required roles are intact COS import and BetC hydrolysis. Bacillus OpuC
supplies a resolved import implementation, with four distinct subunit types and
complex-level cargo evidence. Its native strains accumulate COS intact and are
not full-pathway exemplars. KT2440 intact-accumulation physiology establishes
uptake without identifying its transporter. BetD/BetE candidates remain optional
context. Ruegeria BetT has choline uptake evidence and a COS growth phenotype;
neither proves intact COS import, and its BetC compartment remains unresolved.

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
The 33 cases use the production compiler with explicit cargo, complex-member,
curated-role and strain-specific physiology predicates. Missing units, a generic
same-family ATPase, generic transporter activity and growth-only evidence do not
close the import step. False means unresolved panel coverage, not pathway absence.
The checker is not a genome-wide predictor or a cross-species assembly model.

All 38 historical rows (37 machine rows and one inherited proposal), 20 raw
UniProt/GOA files and 12 inherited provider artifacts are preserved. Twelve new
annotations give 50 current rows. New process terms were not manufactured from
necessity evidence. Falcon attempts failed with HTTP 403; manual literature notes
and primary-source identity checks record the work actually performed.

Focused gene/module/history checks and rendering are completed; full-corpus
validation, publication, remote review/CI and actual merge remain pending.
