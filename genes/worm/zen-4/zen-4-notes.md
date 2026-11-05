# zen-4 review notes

- Fetched UniProt G5EG83 (TrEMBL, WormBase M03D4.1a, WBGene00006974, GeneID 177374): matches
  the requested accession. Q8MQ03 is a second TrEMBL entry with the zen-4 gene name (not reviewed here).
- 24 GOA rows: 7 IEA (InterPro/UniRule/SubCell), 2 IPI from PMID:25875822 (IntAct), and
  WormBase experimental rows from 1998-2018 papers.
- Deep research API unavailable; see zen-4-deep-research-manual.md for literature notes with
  provenance.

## Key decisions

- Motor MF: PMID:25875822 shows ZEN-4 alone moves to plus ends and glides microtubules
  ["Both Z601mAG and Z601mAG/C120 move to the plus end."]. So the IEA motor rows are MODIFIED
  to plus-end-directed microtubule motor activity (GO:0008574), which is the core MF.
- Antiparallel bundling needs CYK-4 ["In vitro, neither MKLP1 alone nor CYK4 alone can
  efficiently bundle microtubules."]: bundling is a complex-level activity; represented as
  centralspindlin complex (NEW, GO:0097149) plus microtubule binding, and BP mitotic spindle
  midzone assembly.
- Mitotic cytokinesis (GO:0000281) is absent from GOA; added as NEW IMP from PMID:9693365.
  This passes the NEW bar: ZEN-4 performs a step (midzone microtubule bundling and midbody
  assembly) rather than being a substrate.
- Meiotic spindle midzone assembly IMP (PMID:20729837): the paper states ZEN-4 inhibition did
  not prevent meiotic anaphase bundles; MARK_AS_OVER_ANNOTATED and a SUSPECTED source defect.
- Pronuclear migration IGI (with cyk-1; abstract-only paper PMID:11050384): PMID:9693365 shows
  zen-4 null embryos have normal pronuclear migration; MARK_AS_OVER_ANNOTATED.
- Centrosome IDA: based on "occasional", "unpublished" interphase observation -> over-annotated.
- Mitotic sister chromatid segregation IGI (with mcm-7): indirect via LEM-3 tethering ->
  over-annotated.
- Bare protein binding (CYK-4) removed per policy; complex membership captured by NEW
  centralspindlin complex row.

## 2026-10-28 PR review fixes

Rewrote the summaries of the two IMP GO:0031991 rows (PMID:11050384, PMID:9693365) so that each describes its own RNAi/allele evidence, not the IGI row's CYK-1 interaction.
