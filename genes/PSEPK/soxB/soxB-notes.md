# soxB curation notes

- Q88R11 is the FAD-bearing beta subunit and its UniProt reaction is tetrahydrofolate coupled. [file:PSEPK/soxB/soxB-uniprot.txt, "Rhea:RHEA:70455"]
- KT2440 literature identifies SoxBDAG as the tetrameric enzyme converting sarcosine to glycine. [PMID:35266867, "sarcosine is then converted to glycine and formaldehyde by the tetrameric sarcosine oxidase (SoxBDAG)"]
- SoxB contains the sarcosine-binding FAD site and oxygen-reducing FMN site, so its oxidase annotation remains `enables`; accessory subunits use `contributes_to` [PMID:15946648, "The beta subunit contains dimethylglycine, FAD, and FMN, and these flavins are approximately 10A apart."].
- Recombinant heterotetrameric sarcosine oxidase contains a stable FMN-sulfide
  adduct implicated in electron transfer and oxidase function [PMID:16934831,
  "The results provide definitive evidence for sulfide as the endogenous TSOX ligand"].

## 2026-11-04 review completion

- Provider deep research was not generated in this session (no API keys); cached literature only.
- Aligned with the CORS9 Sox reviews and the module (orchestrator decision): GO:0008115 (defined by the
  formaldehyde-forming reaction, EC 1.5.3.1/RHEA:13313) is KEEP_AS_NON_CORE, a real conditional folate-free
  activity [PMID:16934831, "In the absence of H 4 folate, turnover occurs at a somewhat slower rate and the sarcosine imine is hydrolyzed to glycine and formaldehyde."].
  enables kept (SoxB carries the FAD substrate site); no qualifier defect.
- Core function uses proposed_molecular_function "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) activity"
  (EC 1.5.3.24, RHEA:70455; proposed parent GO:0016647), in_complex GO:0032921, location cytoplasm.
- Earlier draft NEW contributes_to GO:0008115 rows were dropped (the qualifier issue is a source defect).


## Independent module audit — 2026-11-06

All six rows reviewed. FAD and FMN binding, cytoplasm, complex membership, folate-process participation and conditional formaldehyde chemistry remain supported. Official full PMID15914915 p955 reports no bound flavin in separately expressed beta/beta-delta samples and instability during purification. Active-site localization therefore does not establish autonomous full activity. Retain individual FAD binding with complex-level redox contribution.

Chemistry/assembly sources: [PMID:9185627] heterotetramer-specific folate coupling; [PMID:16934831] full-text flavin mechanism and folate-free imine hydrolysis; [PMID:15914915] publisher full PDF, p955, scoped excerpt in `genes/PSEPK/soxB/soxB-source-analysis/assembly-evidence.md`. [PMID:35266867] is KT2440 pathway background, not purification of KT2440 SoxABDG. The schema lacks a proposed-contribution slot; this is an ontology representation question, not an unresolved biological activity.

All original annotation payloads and inherited NEW rows retained unchanged. No NEW rows added. Raw UniProt/GOA and existing provider artifacts preserved. Default Falcon research genuinely attempted; failed with HTTP 403 authentication/access error. Manual source assessment is recorded here; no provider report was fabricated.


## PR #6122 round-1 gene follow-up (2026-11-06)

- Replace the FAD-binding-only beta core (where present) with proposed sarcosine oxidase (imine-forming) activity, retaining complex contribution and all inherited cofactor NEW rows. This is beta-localized catalysis within the assembled enzyme, not autonomous full THF-coupled turnover.
- Record provenance-specific WRONG_QUALIFIER correction queries (enables to contributes_to) on original sarcosine-oxidase rows; keep all original qualifiers and actions unchanged.

Schema compatibility does not establish an isolated-subunit reaction. The common convention preserves supported catalytic, structural, and cofactor distinctions and marks ortholog transfers explicitly. All historical non-review payloads, inherited NEW actions, and raw/provider bytes remain unchanged; no annotation rows were added or deleted and no publication cache was refreshed.
