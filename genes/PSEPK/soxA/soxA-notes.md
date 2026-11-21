# soxA curation notes

- Q88R09 is the alpha subunit of tetrameric sarcosine oxidase [file:PSEPK/soxA/soxA-uniprot.txt, "DR   InterPro; IPR006277; Sarcosine_oxidase_asu."].
- The `2Fe-2S-bd_N` InterPro name denotes a structural fold here; the characterized complex contains NAD, FAD, FMN, and zinc but no Fe-S cluster [PMID:15946648, "The alpha subunit is composed of two domains, contains NAD(+), and binds folinic acid."].
- KT2440 literature identifies SoxBDAG as the tetrameric enzyme converting sarcosine to glycine. [PMID:35266867, "sarcosine is then converted to glycine and formaldehyde by the tetrameric sarcosine oxidase (SoxBDAG)"]
- SoxA contributes to the complex-level activity rather than enabling it independently; complex membership is proposed separately.

## 2026-11-04 review completion

- Provider deep research was not generated in this session (no API keys); cached literature only.
- Aligned with the CORS9 Sox reviews and the module (orchestrator decision): GO:0008115 (defined by the
  formaldehyde-forming reaction, EC 1.5.3.1/RHEA:13313) is KEEP_AS_NON_CORE, a real conditional folate-free
  activity [PMID:16934831, "In the absence of H 4 folate, turnover occurs at a somewhat slower rate and the sarcosine imine is hydrolyzed to glycine and formaldehyde."].
  WRONG_QUALIFIER source defect (enables -> contributes_to) recorded on the UniProt row.
- Core function uses proposed_molecular_function "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) activity"
  (EC 1.5.3.24, RHEA:70455; proposed parent GO:0016647), in_complex GO:0032921, location cytoplasm.
- Earlier draft NEW contributes_to GO:0008115 rows were dropped (the qualifier issue is a source defect).
- GO:0016491 (InterPro2GO, IPR023753) MODIFY -> the proposed term. GO:0051536 (IPR001041) REMOVE:
  characterised TSOX contains only NAD+, FAD, FMN and a SoxD zinc [PMID:11902668, "The enzyme was found to contain 1 mol of non-covalently-bound NAD+, 1 mol of non-covalently-bound FAD, and 1 mol of covalent FMN."].
- SoxA is in PANTHER PTHR43757 (aminomethyltransferase/GcvT), the same family as yeast GCV1.


## Independent module audit — 2026-11-06

All six rows reviewed. Retain folate-process participation, cytoplasm/complex membership, rejection of the unsupported Fe-S mapping, and the NTR refinement of broad redox activity. SoxA handles folate/NAD in the assembled enzyme, not full independent oxidation. The proposed folate-forming activity is now explicitly a collective reaction; core uses contribution to the oxygen-dependent parent.

Chemistry/assembly sources: [PMID:9185627] heterotetramer-specific folate coupling; [PMID:16934831] full-text flavin mechanism and folate-free imine hydrolysis; [PMID:15914915] publisher full PDF, p955, scoped excerpt in `genes/PSEPK/soxB/soxB-source-analysis/assembly-evidence.md`. [PMID:35266867] is KT2440 pathway background, not purification of KT2440 SoxABDG. The schema lacks a proposed-contribution slot; this is an ontology representation question, not an unresolved biological activity.

All original annotation payloads and inherited NEW rows retained unchanged. No NEW rows added. Raw UniProt/GOA and existing provider artifacts preserved. Existing OpenScientist report preserved and reviewed alongside primary evidence; no provider refresh.


## PR #6122 round-1 gene follow-up (2026-11-06)

- Retain the supported alpha subunit role and existing cofactor core, if any; use the same subunit-specific versus complex-contribution convention without filling unsupported cofactor slots.
- Record provenance-specific WRONG_QUALIFIER correction queries (enables to contributes_to) on original sarcosine-oxidase rows; keep all original qualifiers and actions unchanged.

Schema compatibility does not establish an isolated-subunit reaction. The common convention preserves supported catalytic, structural, and cofactor distinctions and marks ortholog transfers explicitly. All historical non-review payloads, inherited NEW actions, and raw/provider bytes remain unchanged; no annotation rows were added or deleted and no publication cache was refreshed.

Existing qualifier defects were consolidated with the refined provenance-specific assessment (one correction per source row). Legacy OTHER resource labels on direct InterPro2GO defects were corrected to INTERPRO after checking ASSIGNED BY; original assertions and biological judgments were preserved.
