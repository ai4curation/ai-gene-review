# PFDN4 notes

## 2026-11-03 ORGANELLES batch 4 (mitochondrion rows)

Rows: GO:0005739 IEA (GO_REF:0000044, SL-0173) and GO:0005739 IDA (PMID:17936702), both
located_in. No sub-compartment rows.

Checks:
- UniProt Q9NQP4 curates the location to the same paper:
  [file:human/PFDN4/PFDN4-uniprot.txt "Mitochondrion {ECO:0000269|PubMed:17936702}"]; the
  reference scope is "INTERACTION WITH URI1, AND SUBCELLULAR LOCATION".
- PMID:17936702 (Djouder et al. 2007, Mol Cell) is cached abstract-only and has no PMC copy
  (PubMed ID converter, 2026-11-03). The abstract is about URI and PP1gamma
  [PMID:17936702 "URI forms stable complexes with protein phosphatase (PP)1gamma at mitochondria"]
  and does not name PFDN4, so the assay behind the curated location cannot be seen.
- No transit peptide or TM in UniProt; MitoCarta3.0 (Human.MitoCarta3.0.xls, Broad, file in the
  shared scratchpad from 2026-10-25) does not list PFDN4 (MitoCarta2.0 score -3.3).

Outcome: both rows stay KEEP_AS_NON_CORE (curator not overruled; organelle claim stands on
one experiment). The IDA row now also quotes the UniProt curated location, because the old
quote is about URI, not PFDN4. Stay at the root: no sub-compartment line.
