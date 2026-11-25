# Manual gene evidence notes

## 2026-11-05 comparative module audit

Reviewed the complete gene rather than only a module placement: all seeded GO
rows, original reference fields, exact raw UniProt record and relevant primary
literature were checked. The 2016 polyamine synthesis review (PMID:27268252)
and 2018 function review (PMID:30254075) were read as background; neither
substitutes for a target-specific assay. The broad family names encompass
substrate-divergent proteins and do not determine native substrate preference.

The normal command `just deep-research BACTN BT_4612 --provider falcon` failed
with HTTP 403 authentication. No Falcon-branded text was authored. The raw
UniProt/GOA files were retained without refresh or edits. Manual curation uses
these notes and the genuine primary sources; no source cache was hand-edited.

QuickGO searches for carboxyaminopropylagmatine and the specific carboxypolyamine
decarboxylases found no corresponding specific activity term. GO:0102143 is
active and its definition explicitly covers both PUT/DAP reactions; obsolete
GO:0102144 is not used. NTRs describe missing activities rather than guessing IDs.
Exact PANTHER labels were checked against panther.obo and the record's DR lines.

BT_4612/Q89YW9 belongs to PTHR43796:SF2, CARBOXYNORSPERMIDINE SYNTHASE, with
the expected NAD(P)-binding/C-terminal domains. The public Figure 1 of
PMID:27118128 labels CASDH (BT_4612) on a dotted pathway arrow; the experimentally
assayed decarboxylase in that study is BT_0674, not BT_4612. The downloaded
original figure is under the BT_0674 source-analysis directory with its publisher
URL recorded. This is a primary author prediction, not direct enzyme evidence.

No direct BT_4612 PUT/DAP/agmatine assay was recovered from targeted searches
for the exact locus and carboxyspermidine. The B. fragilis sequence assayed in
PMID:37437886 is WP_005801052.1, not the BT_4612 RefSeq WP_008764762.1. Their
shared family is compatible with the proposed pathway, but the CAPADH
diversification demonstrated in PMID:37878710 and PMID:40074085 makes a specific
native putrescine assignment uncertain. No numerical sequence-identity claim is
used, and no unperformed phylogenetic analysis is implied.

Decision: complete the review as an explicitly uncertain candidate with no
substrate-specific core or NEW row, and an actionable biological knowledge gap.
The absence of a core is deliberate, not an incomplete PENDING review. There
were zero source annotations and none was invented to fill that empty set.
