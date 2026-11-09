# fliM notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK fliM --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK fliM` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

TrEMBL entry Q88EU5 (PP_4358), FliM family (PIRSF002888, TIGR01397). No KT2440 fliM experiments cached; family evidence from PMID:31452860 (full text review).
- [PMID:31452860 "FliM and FliN together form the FliM1/FliN3 complex consisting of one copy of FliM and three copies of FliN"]
- [PMID:31452860 "FliMN contains a well conserved LSQXEIDALL sequence, which is responsible for the interaction with CheY-P"]
- [PMID:31452860 "Each stator unit is composed of two transmembrane proteins, MotA and MotB, and acts as a transmembrane proton channel to couple the proton flow through the channel with torque generation"]
- [PMID:36409076 "However, P. putida does not swarm in a flagella-dependent manner (16)"] (introduction statement citing earlier work).

Decisions: GO:0003774 cytoskeletal motor activity MODIFY -> GO:0005198 structural molecule activity (lateral: torque made by stator/FliG, FliM is structural/switch); plasma membrane KEEP_AS_NON_CORE (peripheral); flagellum and basal body MODIFY -> GO:0009433 C ring; positive chemotaxis MODIFY -> GO:0006935 (switch serves both directions); cell motility ACCEPT; swarming MARK_AS_OVER_ANNOTATED (consistent with PSEPK motA).
Module: complex-level GO:0005198 for C ring; recorded GO:0005198 as FliM's own best-supported MF. Considered GO:0140031 phosphorylation-dependent protein binding for CheY-P docking but did not add (binding term, family-level only).
