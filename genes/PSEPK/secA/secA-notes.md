# secA research notes

## Functional assignment

KT2440 SecA is the ATP-driven motor of the Sec translocase (EC 7.4.2.8). UniProt
states that it couples ATP hydrolysis to protein transfer into and across the
cell membrane and acts both as the SecB-complex receptor and as the stepwise
translocation motor [file:PSEPK/secA/secA-uniprot.txt "Has a central role in
coupling the hydrolysis of ATP to the transfer of proteins into and across the
cell membrane"].

SecA ATPase cycling and reversible SecYEG binding are supported experimentally
at the family level [PMID:12242434 "The SecA adenosine triphosphatase (ATPase)
mediates extrusion of the amino termini of secreted proteins from the
eubacterial cytosol based on cycles of reversible binding to the SecYEG
translocon"].

## Structure and localization

The local record assigns a C-terminal SEC-C domain, four zinc-coordinating
residues, monomer/homodimer states, and an approximately 50:50 distribution
between cytoplasm and the cytoplasmic face of the inner membrane. Cytosol is the
more specific term for the soluble pool; retaining both cytoplasm and cytosol
would be redundant.

## Annotation-reviewer pass (2026-09-01)

Reviewed all 12 GOA-derived rows against the local UniProt record, GOA evidence,
SecA literature, and the module-aware OpenScientist report. Outcome: 6 ACCEPT,
2 KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED, and 1 REMOVE; no row remains
PENDING or UNDECIDED. The directional `protein import` IEA remains REMOVE,
while the exact Sec ATPase, Sec-process, translocon-membership, cytosol, and
plasma-membrane assertions remain core.
