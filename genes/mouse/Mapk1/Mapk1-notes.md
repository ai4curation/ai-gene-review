# Mapk1 review notes

## 2026-09-30 refresh

Refreshed the mouse Mapk1 GOA and UniProt snapshots and resolved 18 newly
seeded source rows. ERK2/MAPK1 remains a canonical RAS-RAF-MEK-ERK terminal
kinase whose core function is proline-directed serine/threonine MAP kinase
activity.

Four new `GO:0005515 protein binding` rows were removed. Three came from the
AfCS signaling-database review [PMID:15102471 "databases such as the Alliance
for Cellular Signaling (AfCS) Molecule Pages"] and one from the pseudorabies
virus Us2/ERK membrane-recruitment study [PMID:20554783 "Us2 regulates ERK
activity by spatially restricting ERK localization"]. The PMID:16148006 ERK2
docking-groove row was instead narrowed from generic binding to
`GO:0019902 phosphatase binding` because the abstract directly supports
selective ERK2 binding to MKP-3/DUSP6 phosphatase.

Accepted refreshed nucleoplasm, cytoplasm, and cytosol rows because they match
the established ERK2 nuclear-cytosolic shuttling model already used in the
review. Kept `regulation of ossification` and `myelination` as non-core
developmental ERK outputs; the new myelination row is from the neuregulin/ErbB
study [PMID:18760695 "myelination is markedly different between Schwann cells
and oligodendrocytes"], consistent with the existing non-core myelination rows.

Handled the transferred pathway rows consistently with the existing review:
`GO:0045542 positive regulation of cholesterol biosynthetic process` and
`GO:0045880 positive regulation of smoothened signaling pathway` remain
over-annotations of narrow human crosstalk contexts, `GO:0070371 ERK1 and ERK2
cascade` is an accepted core cascade term, and three new `GO:0106310 protein
serine kinase activity` rows were narrowed to the more informative
`GO:0004707 MAP kinase activity`.
