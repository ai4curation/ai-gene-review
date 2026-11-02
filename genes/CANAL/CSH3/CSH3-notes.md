# CSH3 (Candida albicans) notes

## 2026-10-01 re-review after GOA refresh

GOA was refreshed from remote. The following previously reviewed rows are no longer present in the
current GOA snapshot and were marked `retired: true` (reviews kept; not a biological REMOVE):

- GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport | IBA | GO_REF:0000033
- GO:0051082 unfolded protein binding | IBA | GO_REF:0000033 -- GO:0051082 is obsolete in GO
- GO:0051082 unfolded protein binding | ISS | PMID:14756779 -- obsolete term
- GO:0051082 unfolded protein binding | IGI | PMID:14756779 -- obsolete term

No new GOA rows. Judgment changed: GO:0005886 plasma membrane (IDA, PMID:19824013) REMOVE -> UNDECIDED,
because the cached paper is abstract-only and an experimental annotation should not be removed without
seeing the full text (biologically, CSH3/Shr3 acts in the ER; a plasma-membrane proteome hit may be
ER co-purification). Core function (GO:0044183 protein folding chaperone, ER membrane) unchanged; the
ER-to-Golgi transport process is retained in core_functions since Shr3-family proteins act at ER exit
of permeases.
