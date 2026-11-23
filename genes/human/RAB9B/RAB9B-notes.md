# RAB9B notes

## 2026-11-22 ORGANELLES lysosome batch 2

- Lysosome (GO:0005764) IBA is_active_in row moved ACCEPT -> KEEP_AS_NON_CORE; the old supporting
  quotes (a phagosome abstract sentence and a deep-research header line) replaced.
- RAB9B has no lysosome data of its own (UniProt: cell membrane by inference, phagosome by
  PMID:21255211). The row is the PAINT IBD at PTN000635769 (PTHR47981), shared with RAB9A and RAB7B.
  Its RAB9A seed (MGI IDA, PMID:15078902) shows no lysosome in its full text, but RAB9A has a
  readable human LAMP1 line in PMID:20937701 (EGFP-Rab9A in HeLa). RAB9B stands or falls with that
  RAB9A evidence: same source, same call as the RAB9A IBA.
- WRONG_QUALIFIER CHECK on the IBA. Description reworded so it no longer asserts RAB9B localization
  data that do not exist (late endosome and lysosome by analogy with RAB9A).
- Cycling recruitment of a prenylated RAB is not tethering: no GO:0098574 row.
