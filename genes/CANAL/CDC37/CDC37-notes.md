# CDC37 (Candida albicans) notes

## 2026-10-01 re-review after GOA refresh

GOA was refreshed from remote. The following previously reviewed rows are no longer present in the
current GOA snapshot and were marked `retired: true` (their reviews are kept for provenance; this is
not a biological REMOVE judgment):

- GO:0005737 cytoplasm | IBA | GO_REF:0000033 (cytoplasm is still supported by the current IEA GO_REF:0000120 row)
- GO:0051082 unfolded protein binding | IBA | GO_REF:0000033 -- GO:0051082 is now obsolete in GO
- GO:0051087 protein-folding chaperone binding | IBA | GO_REF:0000033
- GO:0051082 unfolded protein binding | IEA | GO_REF:0000107 -- obsolete term
- GO:0051301 cell division | IEA | GO_REF:0000043 (UniProt keyword mapping no longer emitted)
- GO:0005515 protein binding | IPI | PMID:15013782 (Crk1 interaction)
- GO:0051082 unfolded protein binding | IGI | PMID:15013782 -- obsolete term

New GOA rows reviewed: GO:0140597 protein carrier activity (IEA, from S. cerevisiae Cdc37; ACCEPT --
fits the kinase-to-Hsp90 client delivery role) and GO:1990565 HSP90-CDC37 chaperone complex (IBA; ACCEPT).
Core function MF remains GO:0044183 protein folding chaperone (current, non-obsolete term).
