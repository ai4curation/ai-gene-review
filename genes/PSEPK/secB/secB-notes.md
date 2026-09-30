# secB research notes

## Functional assignment

SecB is a soluble export chaperone that maintains selected precursors in a
translocation-competent state and delivers them to SecA
[file:PSEPK/secB/secB-uniprot.txt "binds to a subset of precursor proteins,
maintaining them in a translocation-competent state."]. This is carrier activity,
not protein-folding catalysis.

Direct work on E. coli SecB established the complete capture-and-handoff
mechanism [PMID:16962134 "SecB delivers its ligand to export sites through its
specific binding to SecA, a peripheral component of the membrane translocon."].
GO:0140309 unfolded protein holdase activity captures both substrate binding and
escort, so adding a second generic unfolded-protein-binding annotation would be
redundant.

## Annotation-reviewer pass (2026-09-01)

Reviewed all 4 GOA-derived rows and the proposed holdase annotation against the
local UniProt record, SecB literature, and the module-aware OpenScientist report.
Outcome: 1 ACCEPT, 1 KEEP_AS_NON_CORE, 1 MODIFY, 1 REMOVE, and 1 NEW; no row
remains PENDING or UNDECIDED. The broad protein-transport row is refined to
Sec-complex transport, and protein folding remains removed because SecB keeps
precursors unfolded rather than catalyzing their folding.
