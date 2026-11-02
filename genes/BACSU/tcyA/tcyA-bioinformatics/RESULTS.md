# TcyA (P42199) family placement and comparator identity

Analyses run 2026-10-21 against the live UniProt REST API.

## Scripts

- `panther_placement.py` (stdlib only): prints PANTHER and CDD cross-references for TcyA
  and comparators. Output: `placement.tsv`.
- `pairwise_identity.py` (Biopython; run with `uv run python` from the repo root): global
  BLOSUM62 alignment of TcyA against each comparator (gap open -10, extend -0.5), identity
  over aligned columns, and the TcyA residues aligned to the two Ngo0372 binding-pocket
  residues mutated in PMID:22138345. Output: `pairwise_identity.tsv`.

## PANTHER / CDD placement (placement.tsv)

| accession | protein | PANTHER subfamily | CDD |
|---|---|---|---|
| P42199 | B. subtilis TcyA (target) | PTHR35936:SF34 | cd13711 |
| P42400 | B. subtilis YckB (uncharacterized paralog) | PTHR35936:SF34 | cd01003 |
| O34406 | B. subtilis TcyJ (TcyJKLMN SBP) | PTHR35936:SF18 | cd13710 |
| D3VIU4 | X. nematophila D3VIU4 | PTHR35936:SF34 | cd13711 |
| P0AEM9 | E. coli TcyJ (FliY) | PTHR35936:SF35 | cd13712 |
| Q5F9M1 | N. gonorrhoeae Ngo0372 (L-cystine SBP, crystal structure) | PTHR35936:SF35 | cd13711 |

## Pairwise identity to TcyA (pairwise_identity.tsv)

| comparator | identity | aligned columns |
|---|---|---|
| D3VIU4 | 0.502 | 255 |
| P42400 YckB | 0.432 | 257 |
| O34406 B. subtilis TcyJ | 0.352 | 244 |
| P0AEM9 E. coli TcyJ | 0.421 | 259 |
| Q5F9M1 Ngo0372 | 0.538 | 262 |

## Binding-pocket residues

The Ngo0372 residues reported as Tyr59 and Trp97 in PMID:22138345 correspond to the only
Tyr/Trp pair with that spacing in the UniProt Q5F9M1 sequence, Y58 and W96 (an off-by-one
numbering difference). Both are conserved in TcyA, at Y55 and W94.

## Interpretation

- PANTHER puts TcyA in subfamily SF34 with D3VIU4 and with the uncharacterized B. subtilis
  paralog YckB. No member of SF34 has a direct ligand-binding measurement that we found.
  The two cystine SBPs with biochemical data, E. coli TcyJ and Ngo0372, are in SF35.
- The CDD model cd13711 (PBP2_Ngo0372_TcyA) does group TcyA with Ngo0372, and Ngo0372 is
  the comparator most identical to TcyA (54%). Ngo0372 Tyr59, which PMID:22138345 found to
  be crucial for L-cystine binding, is conserved in TcyA (Y55).
- So the conserved pocket and the CDD placement are consistent with TcyA binding L-cystine.
  This does not establish ligand binding by TcyA. Its experimental evidence in B. subtilis
  is genetic (PMID:15262924). Its SF34 paralog YckB has no known substrate, so membership
  of SF34 alone does not predict L-cystine specificity.
