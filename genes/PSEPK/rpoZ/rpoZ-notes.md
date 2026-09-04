# rpoZ notes

## 2026-09-01 annotation-reviewer pass

Reviewed every existing GOA-derived row and the proposed additions against
Q88C82 UniProt/HAMAP evidence. Generic DNA binding remains over-annotated. The
two polymerase-activity assertions are accepted under the repository's current
RNA-polymerase-subunit convention, while core-function synthesis records omega
as contributing to the assembled complex activity. DNA-templated transcription
and complex membership are retained, and GO:0065003 is proposed for the
explicitly documented RNA polymerase assembly role. Unsupported inferred
cytosol and generic structural-molecule proposals were removed. The prior gene-level
OpenScientist run timed out without an artifact, so this pass uses the reviewed
UniProt record, GOA snapshot, and completed module research.
