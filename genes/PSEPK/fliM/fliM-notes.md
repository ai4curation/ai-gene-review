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


## Taxon/module audit, 2026-11-06

The primary Salmonella structure uses constitutively active CheY D13K/Y106W; it supports conserved FliM switching structure, not a direct KT2440 FliM experiment. Retain the structural molecule MF and C-ring location refinements. No uninformative bare protein binding term is proposed. Existing swarming caution is retained because semisolid swimming is not a swarming assay.

Source anchor: [PMID:39179739 "The CheY proteins are bound into an open groove between two adjacent protomers on the surface of the middle subring of the C ring and interact with the FliG and FliM subunits."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.



## 2026-11-06 comparative flagellar audit

Reviewed every existing annotation and the biological summary/core functions. Original annotation payloads, including historical NEW proposals, are preserved. Family/domain evidence supports conserved structural assignments; comparative Salmonella or other bacterial assays are not presented as KT2440 experiments. Exact subunit counts and interaction geometries are not transferred as target measurements.

The normal Falcon research attempt failed (HTTP 403; provider output was not fabricated). This entry records manual review of the cached primary/comparative literature.

General flagellar motility does not by itself establish swarming. The electronically transferred swarming term is qualified against the KT2440 physiological context in PMID:36409076, not rejected because an experimental source is unavailable.

GO:0003774 explicitly includes electrochemical-gradient-driven flagellar rotation. Rotor/switch structural roles are distinguished from autonomous torque generation. The C-ring/MS-ring CC terms were verified against ontology ancestry and remain valid substructure locations.


## 2026-11-11 — reconcile chemotaxis and merged flagellar audits

Retain merged flagellar evidence and decisions, including gradient-guided stator mechanics and FliG switching; retain branch primary structural references, target-specific caveats, and broad-family limits. FliN direct CheY-contact uncertainty is preserved.
