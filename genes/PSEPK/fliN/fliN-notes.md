# fliN notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK fliN --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK fliN` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

TrEMBL entry Q88EU6 (PP_4357), FliN/MopA/SpaO family (TIGR02480). No KT2440 fliN experiments cached.
- [PMID:31452860 "CheY-P binds to FliNC in a FliM-dependent manner"]
- [PMID:31452860 "A continuous spiral density at the bottom edge of the C ring is made of the C-terminal domains of FliM (FliMC) and FliN."]
- [PMID:31452860 "FliN also provides binding sites for FliH"]

Decisions: GO:0003774 MODIFY -> GO:0005198 (same reasoning as FliM); plasma membrane KEEP_AS_NON_CORE; membrane MODIFY -> GO:0005886; chemotaxis ACCEPT; flagellum and basal body MODIFY -> GO:0009433; cell motility ACCEPT. Core MF GO:0005198 (module C-ring complex-level MF).


## 2026-11-06 comparative flagellar audit

Reviewed every existing annotation and the biological summary/core functions. Original annotation payloads, including historical NEW proposals, are preserved. Family/domain evidence supports conserved structural assignments; comparative Salmonella or other bacterial assays are not presented as KT2440 experiments. Exact subunit counts and interaction geometries are not transferred as target measurements.

The normal Falcon research attempt failed (HTTP 403; provider output was not fabricated). This entry records manual review of the cached primary/comparative literature.

GO:0003774 explicitly includes electrochemical-gradient-driven flagellar rotation. Rotor/switch structural roles are distinguished from autonomous torque generation. The C-ring/MS-ring CC terms were verified against ontology ancestry and remain valid substructure locations.
