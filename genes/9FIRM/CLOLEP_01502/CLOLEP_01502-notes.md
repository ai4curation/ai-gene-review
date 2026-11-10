# Manual gene evidence notes

## 2026-11-05 comparative module audit

Reviewed the complete gene rather than only a module placement: all seeded GO
rows, original reference fields, exact raw UniProt record and relevant primary
literature were checked. The 2016 polyamine synthesis review (PMID:27268252)
and 2018 function review (PMID:30254075) were read as background; neither
substitutes for a target-specific assay. The broad family names encompass
substrate-divergent proteins and do not determine native substrate preference.

The normal command `just deep-research 9FIRM CLOLEP_01502 --provider falcon` failed
with HTTP 403 authentication. No Falcon-branded text was authored. The raw
UniProt/GOA files were retained without refresh or edits. Manual curation uses
these notes and the genuine primary sources; no source cache was hand-edited.

QuickGO searches for carboxyaminopropylagmatine and the specific carboxypolyamine
decarboxylases found no corresponding specific activity term. GO:0102143 is
active and its definition explicitly covers both PUT/DAP reactions; obsolete
GO:0102144 is not used. NTRs describe missing activities rather than guessing IDs.
Exact PANTHER labels were checked against panther.obo and the record's DR lines.

The raw entry A7VSG1 cross-references EDO61991.1. PMID:37437886 explicitly
tested that sequence, naming it ClCASDH, and measured similar PUT/DAP catalytic
efficiencies (approximately 74 and 71 M−1 s−1). These assays did not test
agmatine. The paper's inference that substrate availability makes putrescine
physiological cannot settle preference against an untested substrate.

PMID:40074085 supplementary Table S1 identifies Clostridium CAPADH as
EDO61991 (399 residues) and CAPADC as EDO61992 (376 residues). The primary
reconstruction produced about 150-fold more aminopropylagmatine with the
Clostridium pair than with the Agrobacterium CASDH/CASDC comparator. The
authors conclude that the Cl pair synthesizes spermidine from agmatine and
aminopropylagmatine [PMID:40074085]. The paired experiment identifies a CAPA
route; it does not supply isolated-enzyme agmatine kcat/Km or native-cell flux.

Decision: REMOVE the wrong saccharopine EC-based IEA. In the direct control
assays, all Cl enzyme measurements were at the detection limit; the lone
weak saccharopine positive was BfCASDH, not ClCASDH [PMID:37437886, "In all
experiments except one, turnover was within error of the limit of detection
of our assay (<0.008 VO/[E] s−1)"]. Use a supported CAPADH proposed activity
in the core, retaining PUT/DAP turnover as measured alternate catalytic
capacity in findings and this notebook. It is not assigned as a separate
native biological function without evidence that it serves one. The CAPADH
NTR excludes PUT/DAP chemistry and its support comes from the exact-pair
reconstruction, not family membership alone.


## PR 6089 review 5812319279 follow-up (2026-11-07)

Clarified the threshold for not adding a PUT/DAP MF proposal solely for coverage. Purified EDO61991.1 activities remain positively recorded; their evolved secondary role is unresolved against the agmatine-route reconstruction. Comparable BfCASDH rates alone do not decide this distinction. No activity is denied and no numerical cutoff is imposed.

Read-only source caches were used; no downloads or source refreshes. Original annotation payloads/order and every historical NEW lifecycle are preserved. Heavy validation and rendering are deferred because disk space is critically low.
