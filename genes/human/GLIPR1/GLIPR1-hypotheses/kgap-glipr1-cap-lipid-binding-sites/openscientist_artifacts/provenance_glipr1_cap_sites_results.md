# GLIPR1 CAP lipid-binding site analysis: computed results

All numbers below were produced by code executed in this job (see `glipr1_cap_sites_analysis.py`).
Inputs: PDB 3Q2U, 3Q2R (human GLIPR1), 3U3N, 3U3U (tablysin-15 + palmitate / leukotriene E4),
5ETE (Pry1 CAP domain), 1SMB (human GAPR-1); UniProt P48060, P47032, Q9H4G4;
141 vertebrate GLIPR1 orthologs from UniProt (`gene:GLIPR1 AND taxonomy_id:7742`).

PDB author numbering in 3Q2U is identical to UniProt P48060 numbering (residues 22-214 modelled).

## Table 1. Structural superposition of GLIPR1 (3Q2U chain A, 193 residues) onto CAP homologs

Method: TM-align-style algorithm implemented here (gapless fragment seeding, iterative
DP refinement on 1/(1+(d/d0)^2), Kabsch superposition). TM-score normalised by 193.

| Target | TM-score | aligned pairs | core pairs (<5 A) | core RMSD (A) |
|---|---|---|---|---|
| tablysin-15 3U3N (palmitate complex) | 0.768 | 183 | 158 | 1.99 |
| tablysin-15 3U3U (LTE4 complex) | 0.773 | 183 | 163 | 2.16 |
| Pry1 CAP 5ETE | 0.555 | 142 | 118 | 2.01 |
| GAPR-1 1SMB | 0.606 | 145 | 124 | 1.70 |

## Table 2. CAP tetrad mapping

| GAPR-1 | GLIPR1 equivalent | CA deviation (A) | Pry1 (PMID 27344972) | GLIPR1 equivalent | CA deviation (A) | ortholog identity |
|---|---|---|---|---|---|---|
| His54 | His79 | 0.62 | His208 | Leu83 (loop insertion, unreliable) | 7.15 | 99.3 % |
| Glu65 | Glu98 | 0.66 | Glu215 | Glu98 | 1.32 | 100 % |
| Glu86 | Glu120 | 1.48 | Glu233 | Glu120 | 1.11 | 100 % |
| His103 | His137 | 1.00 | His250 | His137 | 1.27 | 100 % |

Experimental confirmation: in 3Q2R the single Zn2+ is coordinated by His79 NE2 (2.66 A) and
His137 NE2 (2.78 A) and by nothing else within 3.0 A.

## Table 3. Caveolin-binding-motif (CBM) loop mapping

Motif scan (Phi = W/F/Y): Pry1 `YDFSNPGF` 237-244; GAPR-1 `YNFQQPGF` 90-97;
GLIPR1 SCP domain (38-175): **no match**. Only GLIPR1 match is `YYSVVYPGW` 217-225,
outside the CAP domain, in the juxtamembrane segment before the TM helix (233-255).

| Pry1 | GAPR-1 | GLIPR1 equivalent | CA dev. vs Pry1 (A) | ortholog identity | RSA in 3Q2U |
|---|---|---|---|---|---|
| Tyr237 | Tyr90 | Tyr124 | 2.01 | 100 % Y | 12.1 % |
| Asp238 | Asn91 | Asp125 | 1.55 | 71.6 % | 35.1 % |
| Phe239 | Phe92 | Phe126 | 2.37 | 98.6 % aromatic | 9.8 % |
| Ser240 | Gln93 | Lys127 | 2.02 | 26.2 % | - |
| Asn241 | Gln94 | Thr128 | 1.68 | 85.8 % | - |
| Pro242 | Pro95 | Arg129 | 3.48 | 41.8 % | 31.3 % |
| Gly243 | Gly96 | Ile130 | 6.52 | 6.4 % (K in 70/141) | - |
| Phe244 | Phe97 | **Cys131** | 6.88 | 99.3 % C | 29.7 % |

GLIPR1 Cys131 is disulfide-bonded to Cys135 (SG-SG 2.06 A). Full disulfide set in 3Q2U:
C75-C156, C131-C135, C151-C173, C192-C201, C195-C206.

## Table 4. Tablysin-15 fatty-acid channel mapped onto GLIPR1

| tablysin-15 | GLIPR1 | CA dev. (A) | GLIPR1 RSA | ortholog identity |
|---|---|---|---|---|
| Ile43 | Cys37 | 1.54 | - | 96.5 % |
| Lys46 | Ile40 | 1.44 | - | 35.5 % |
| Ile47 | His41 | 1.07 | 0.0 % | 98.6 % |
| Asp49 | Lys43 | 1.24 | - | 60.3 % |
| Val50 | **Phe44** | 1.46 | 12.1 % | 73.0 % (75.9 % aromatic) |
| His53 | Glu47 | 1.33 | - | 49.6 % |
| Trp59 | no structural equivalent | - | - | - |
| Leu106 | Asn99 | 0.47 | - | 100 % |
| Phe108 | Trp101 | 0.70 | 8.4 % | 100 % |
| Ile122 | Val110 | 1.32 | - | 79.4 % |
| Ala125 | Ala113 | 0.90 | 0.0 % | 97.2 % |
| Val126 | Ile114 | 2.76 | 0.0 % | 75.2 % |
| Gly129 | **Trp117** | 2.64 | 0.4 % | 98.6 % |
| His130 | Tyr118 | 3.63 | 12.7 % | 73.8 % |
| Ala159 | Val141 | 1.24 | 0.0 % | 85.1 % |
| Leu184 | Phe171 | 0.78 | 0.0 % | 96.5 % |
| Cys186 | Cys173 | 0.46 | - | 97.9 % |
| Phe188 | Tyr175 | 0.57 | 0.0 % | 97.9 % |

## Table 5. Buried cavity detection (LIGSITE-style, 1.0 A grid, 1.4 A probe, PSP >= 6/13)

Run on protein atoms only (all heteroatoms stripped).

| Protein | cavity 1 (A^3) | hydrophobic frac. | cavity 2 (A^3) | hydrophobic frac. | cavity 3 (A^3) | hydrophobic frac. |
|---|---|---|---|---|---|---|
| GLIPR1 3Q2U | 422 | 0.39 | 112 | 0.38 | 95 | 0.40 |
| tablysin-15 3U3N | 437 | 0.27 | **166** | **0.70** | 141 | 0.50 |
| Pry1 CAP 5ETE | 369 | 0.37 | 75 | 0.54 | 40 | 0.50 |
| GAPR-1 1SMB | 224 | 0.29 | 104 | 0.24 | 55 | 0.50 |

Positive control: 18 of 18 palmitate atoms in 3U3N fall within 2 A of the tablysin-15
cavity-2 grid; 0 of 18 fall near cavity 1 or cavity 3. The method therefore recovers a
known lipid channel. GLIPR1 has no cavity with comparable hydrophobicity.

## Table 6. Palmitate and LTE4 transplanted into the GLIPR1 frame

| Ligand | min dist to GLIPR1 (A) | median (A) | max (A) | atoms >4 A from protein | contacts <2.8 A |
|---|---|---|---|---|---|
| palmitate (from 3U3N) | 0.41 | 1.90 | 3.36 | 0 / 18 | 23 |
| leukotriene E4 (from 3U3U) | 0.52 | 1.89 | 4.52 | 1 / 23 | 24 |

Worst palmitate clashes: Phe44 CD2 0.41 A, Phe44 CD1 1.24 A, Glu47 OE1 1.50 A,
Ile114 CA 2.15 A (backbone), His41 CE1 2.67 A, Ile114 O 2.74 A (backbone),
Ile114 N 2.76 A (backbone). Backbone clashes cannot be relieved by rotamer changes.

## Table 7. Ortholog conservation summary

141 vertebrate GLIPR1 orthologs (lamprey, bony fish, reptiles, birds, marsupials,
placental mammals), 37-100 % identity to human P48060, median 70 %.
Banded Needleman-Wunsch alignment of each ortholog to P48060.

- CAP tetrad: 99.3-100 % identical (invariant).
- CBM-equivalent aromatics Tyr124 / Phe126: 100 % Y and 98.6 % aromatic (invariant).
- CBM-equivalent loop interior Lys127 / Arg129 / Ile130: 26.2 % / 41.8 % / 6.4 % (hypervariable).
- Channel-occluding residues Trp117 / Ala113 / Phe171 / Tyr175: 98.6 % / 97.2 % / 96.5 % / 97.9 %.

## Glycerol sites in 3Q2U

- GOL666: His79, Glu98, Asn99, Val134, Gly136, His137 (central CAP cavity, tetrad site).
- GOL898: Phe77, Ile100, Trp101, Thr102, Asn116, Phe162.
- GOL999: Lys84, Ser95, Leu96, Gly97, Gly178, Gly179, Asn180, Tyr181.
- GOL777: Arg82, His87.
