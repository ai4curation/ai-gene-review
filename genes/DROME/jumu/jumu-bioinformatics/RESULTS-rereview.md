# jumu (Q9XTP7) PANTHER placement check, 2026-10-20 re-review

Script: `panther_placement_rereview.py` (reads the release-pinned PANTHER 19.0
HMM classification files under `.cache/panther/`, built by `just validate-families`).

## Output (run 2026-10-20)

| accession | protein | PANTHER 19.0 subfamily |
|---|---|---|
| Q9XTP7 | fly jumu | PTHR13962:SF17 |
| Q96NZ1 | human FOXN4 | PTHR13962:SF17 |
| Q8K3Q3 | mouse Foxn4 | PTHR13962:SF17 |
| A2BGM5 | zebrafish foxn4 | PTHR13962:SF17 |
| Q3BJS1 | Xenopus foxn4 | PTHR46721:SF2 |
| O15353 | human FOXN1 | PTHR46721:SF1 |
| Q61575 | mouse Foxn1 | PTHR46721:SF1 |
| O00409 | human FOXN3 | PTHR13962:SF20 |
| P32314 | human FOXN2 | PTHR13962:SF19 |

## Interpretation

- In the official PANTHER 19.0 classification, jumu Q9XTP7 sits in PTHR13962:SF17
  (PANTHER name "FORKHEAD BOX PROTEIN N4"), the same subfamily as human FOXN4,
  mouse Foxn4 and zebrafish foxn4. The UniProt cross-reference on the frozen Q9XTP7
  record instead gives PTHR46721:SF3 (FORKHEAD BOX N1). The two sources disagree;
  the official HMM classification groups jumu with the FOXN4 orthologs.
- The IBA donors for jumu (PTN000216159; MGI:2151057 = mouse Foxn4, ZFIN
  ZDB-GENE-990415-277 = zebrafish foxn4, UniProtKB:Q96NZ1 = human FOXN4,
  O00409 = FOXN3, P32314 = FOXN2) all fall in PTHR13962, consistent with the
  PANTHER 19.0 placement and with jumu descending from a FOXN2/3/4-containing node.
- Placement in the FOXN4 subfamily supports transfer of the generic forkhead
  DNA-binding transcription factor mechanism, but not FOXN4-specific developmental
  programs (retinal amacrine/horizontal fate, atrioventricular canal, multiciliogenesis).
- Q9XTP7 is the full-length 719-residue product (forkhead DNA-binding domain at
  residues 411-508 per the UniProt record); it is not a fragment or isoform.
