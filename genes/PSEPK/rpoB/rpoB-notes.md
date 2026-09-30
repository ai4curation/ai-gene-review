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
