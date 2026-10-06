# erg25 (SPAC630.08c, UniProt Q9UUH4) notes

Module: `ergosterol_biosynthesis` (C-4 methylsterol oxidase); S. cerevisiae ortholog ERG25 (P53045). Fetch verified: Q9UUH4.

## Evidence
- Sterol desaturase-family di-iron oxidase; three His boxes [UniProt:Q9UUH4 "demethylation complex that catalyzes the three-step monooxygenation"].
- Strongly Sre1/Scp1-induced under low O2/sterol [UniProt:Q9UUH4 "INDUCTION: Expression is highly up-regulated under low oxygen and low"]; [PMID:15797383 "Microarray analysis revealed that Sre1 activates sterol biosynthetic"].
- ER IDA from PMID:31217286 (abstract only; ergosterol and F-actin cables).

## Curation decisions
- All MF/CC/BP rows accepted; iron binding and lipid biosynthesis non-core.
- UniProt EC is 1.14.18.- (by similarity); module lists no EC for this step in its evidence.
- in_complex not asserted: the C-4 demethylation complex is only by similarity in S. pombe (yeast ERG25 review uses GO:1902494).
