# soxD curation notes

- Q88R10 is the small delta subunit of tetrameric sarcosine oxidase. [file:PSEPK/soxD/soxD-uniprot.txt, "DR   InterPro; IPR006279; SoxD."]
- KT2440 literature identifies SoxBDAG as the tetrameric enzyme converting sarcosine to glycine. [PMID:35266867, "sarcosine is then converted to glycine and formaldehyde by the tetrameric sarcosine oxidase (SoxBDAG)"]
- SoxD contributes to complex activity rather than independently enabling it.
- The characterized delta subunit coordinates structural zinc through a Cys3His motif [PMID:15946648, "The delta subunit contains a single atom of zinc and has a Cys(3)His zinc finger structure."].

## 2026-11-04 review completion

- Provider deep research was not generated in this session (no API keys); cached literature only.
- Aligned with the CORS9 Sox reviews and the module (orchestrator decision): GO:0008115 (defined by the
  formaldehyde-forming reaction, EC 1.5.3.1/RHEA:13313) is KEEP_AS_NON_CORE, a real conditional folate-free
  activity [PMID:16934831, "In the absence of H 4 folate, turnover occurs at a somewhat slower rate and the sarcosine imine is hydrolyzed to glycine and formaldehyde."].
  WRONG_QUALIFIER source defect (enables -> contributes_to) recorded on the UniProt row.
- Core function uses proposed_molecular_function "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) activity"
  (EC 1.5.3.24, RHEA:70455; proposed parent GO:0016647), in_complex GO:0032921, location cytoplasm.
- Earlier draft NEW contributes_to GO:0008115 rows were dropped (the qualifier issue is a source defect).


## Independent module audit — 2026-11-06

All five rows reviewed. Zinc binding and structural membership support contribution to assembled enzyme chemistry, not autonomous catalysis. Preserve inherited complex/location/zinc proposals and folate-process participation. The latter rests on structural work in the catalytic assembly, not merely a knockout phenotype. Product partition in native KT2440 is unknown.

Chemistry/assembly sources: [PMID:9185627] heterotetramer-specific folate coupling; [PMID:16934831] full-text flavin mechanism and folate-free imine hydrolysis; [PMID:15914915] publisher full PDF, p955, scoped excerpt in `genes/PSEPK/soxB/soxB-source-analysis/assembly-evidence.md`. [PMID:35266867] is KT2440 pathway background, not purification of KT2440 SoxABDG. The schema lacks a proposed-contribution slot; this is an ontology representation question, not an unresolved biological activity.

All original annotation payloads and inherited NEW rows retained unchanged. No NEW rows added. Raw UniProt/GOA and existing provider artifacts preserved. Default Falcon research genuinely attempted; failed with HTTP 403 authentication/access error. Manual source assessment is recorded here; no provider report was fabricated.


## PR #6122 round-1 gene follow-up (2026-11-06)

- Retain the supported delta subunit role and existing cofactor core, if any; use the same subunit-specific versus complex-contribution convention without filling unsupported cofactor slots.
- Record provenance-specific WRONG_QUALIFIER correction queries (enables to contributes_to) on original sarcosine-oxidase rows; keep all original qualifiers and actions unchanged.

Schema compatibility does not establish an isolated-subunit reaction. The common convention preserves supported catalytic, structural, and cofactor distinctions and marks ortholog transfers explicitly. All historical non-review payloads, inherited NEW actions, and raw/provider bytes remain unchanged; no annotation rows were added or deleted and no publication cache was refreshed.
