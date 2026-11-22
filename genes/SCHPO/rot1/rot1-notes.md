# rot1 curation notes

## 2026-11 PTHR28090 fungal PAINT review

Fetched the S. pombe `rot1` GOA, UniProt, and cached supporting publications for a PTHR28090 fungal PAINT pass. The current PAINT cache places both `GO:0005789 endoplasmic reticulum membrane` and `GO:0006458 'de novo' protein folding` at `PANTHER:PTN001999053`, a Dikarya Rot1 node seeded by SGD `ROT1`. S. pombe `rot1` inherits those two rows, but not the Saccharomycetales `PTN001999057` `GO:0007118 budding cell apical bud growth` row.

The PomBase ORFeome HDA row places `rot1` in the endoplasmic reticulum. The exact molecular function is inferred by orthology: S. cerevisiae Rot1 is an ER-localized membrane protein and recombinant Rot1 has antiaggregation activity [PMID:16567426; PMID:18508919]. I accepted the ER and de novo folding transfers, accepted PomBase's ER protein-folding IC row, and removed only the old ND molecular-function placeholder.

Newer-paper search: PMID:40846641 was already cached in the yeast ROT1 review and reinforces Rot1 as a UPR-independent ER chaperone in budding yeast. A 2026 C. albicans paper, PMID:42042339, directly characterizes CaROT1; it corroborates conservation of the Rot1 family but does not add target-specific S. pombe evidence.
