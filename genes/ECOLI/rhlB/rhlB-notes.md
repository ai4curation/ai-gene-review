# rhlB (E. coli K-12) curation notes

## 2026-11-10

Reviewed as an exemplar for the RNase E-centred RNA degradation module
(`modules/bacterial_rna_degradation.yaml`). No provider deep-research run was
made for this gene in this session (no provider API keys available); the review
rests on the UniProt record and the cached publications under `publications/`,
most of which are abstract-only. Rows whose evidence could only be checked at
abstract level defer to the GOA curator unless the abstract contradicts them.

Conventions applied (shared with the other degradosome members): bare
GO:0005515 protein-binding rows are removed per the protein-binding policy;
parent terms entailed by an accepted, more specific term in the same review are
TOO_GENERAL; generic `membrane` rows on degradosome partners are refined to
cytoplasmic side of plasma membrane, reflecting recruitment to the
membrane-bound RNase E scaffold.
