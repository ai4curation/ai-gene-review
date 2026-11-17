# rpoB notes

## 2026-09-01 annotation-reviewer pass

Reviewed every existing GOA-derived row and the proposed complex membership
row against Q88QP2 UniProt/HAMAP evidence. DNA binding and ribonucleoside
binding are retained as non-core substrate-contact context; DNA-templated
transcription and complex membership are retained. GO:0003899 and GO:0034062
are accepted for this large catalytic-cleft subunit, with the synthesis using
`contributes_to_molecular_function` to avoid implying activity by isolated
RpoB. The unsupported inferred cytosol proposal was removed. The prior gene-level
OpenScientist run timed out without an artifact, so this pass uses the reviewed
UniProt record, GOA snapshot, and completed module research rather than
inventing provider output.

## 2026-11-13 cross-subunit alignment with E. coli K-12

Re-reviewed alongside the new E. coli K-12 rpoA/rpoB/rpoC/rpoZ reviews so that
both species follow one policy (projects/PROTEIN_COMPLEX_FUNCTIONS.md). The
earlier "accept polymerase activity on every subunit" convention is retired:
GO:0003899/GO:0034062 are MARK_AS_OVER_ANNOTATED on alpha and omega; on beta and
beta-prime GO:0003899 is accepted and GO:0034062 is MODIFY to GO:0003899. The
proposed complex row now uses GO:0000345 (the eubacterial RNAP) instead of the
pan-domain parent GO:0000428. Omega's core function is GO:0001000 core enzyme
binding (NEW, from HAMAP MF_00366 and the E. coli experimental evidence);
beta-prime's core functions are contribution to GO:0003899 plus Mg(2+) binding,
with structural Zn(2+) binding kept as non-core.
