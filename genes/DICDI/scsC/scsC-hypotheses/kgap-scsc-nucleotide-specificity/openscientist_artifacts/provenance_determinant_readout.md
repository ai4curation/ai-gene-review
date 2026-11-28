# scsC / scsB nucleotide-specificity determinant readout

Reference frame: pig GTP-specific succinyl-CoA synthetase beta subunit, observed chain B of
PDB 2FP4 (Fraser et al. 2006, PMID 16481318), residues 1-393, mature-subunit numbering.

## Residues within 4.0 A of the guanine base of GTP in 2FP4 chain B

Computed from deposited coordinates. Base atoms used: N1, C2, N2, N3, C4, C5, C6, O6, N7, C8, N9.

| Residue | Min distance to guanine base |
|---|---|
| Gln20β | 2.58 A |
| Val44β | 3.49 A |
| Leu69β | 3.58 A |
| Ala108β | 3.28 A |
| Leu109β | 2.72 A |
| Ile111β | 3.72 A |
| Phe219β | 3.69 A |

Whole-GTP contacts also include Gly52β, Gly53β, Arg54β, Gly55β, Val67β, Glu114β, Asp220β, Lys222β.
Arg54β is assigned by PMID 16481318 to the gamma-phosphate, not to base discrimination.

## Readout across subunits with measured nucleotide use

| Subunit | Measured nucleotide use | 20β | 44β | 69β | 108β | 109β | 111β | 219β |
|---|---|---|---|---|---|---|---|---|
| pig SUCLG2 (P53590) | GTP-specific | Q | V | L | A | L | I | F |
| human SUCLG2 (Q96I99) | GTP-specific | Q | V | L | A | L | I | F |
| mouse Suclg2 (Q9Z2I8) | GTP-specific (by orthology) | Q | V | L | A | L | I | F |
| pig SUCLA2 (O97580) | ATP-specific | P | V | I | R | R | P | M |
| human SUCLA2 (Q9P2R7) | ATP-specific | P | V | I | R | K | P | M |
| mouse Sucla2 (Q9Z2I9) | ATP-specific (by orthology) | P | V | I | R | K | P | M |
| S. cerevisiae Lsc2 (P53312) | ADP-forming | P | V | M | R | V | T | T |
| E. coli SucC (P0A836) | dual, prefers ADP/ATP | P | V | V | A | T | I | L |
| T. aquaticus SucC (A0ABN4IHZ4) | dual, prefers GDP/GTP | P | V | L | A | V | I | A |
| **Dicty scsC (Q55AI5)** | **unknown** | **P** (Pro54) | V78 | L103 | **R**142 | H143 | L145 | **M**253 |
| **Dicty scsB (Q869S7)** | **unknown** | **Q** (Gln46) | V69 | L95 | S134 | V135 | **P**137 | **M**245 |

Alignment method: pairwise Needleman-Wunsch, BLOSUM62, gap open -11, gap extend -1, each
full-length UniProt sequence against the observed 2FP4 chain B sequence. Identity to 2FP4 B:
pig SUCLG2 99.8%, human SUCLG2 96.4%, scsB 59.5%, pig SUCLA2 54.7%, scsC 54.5%,
human SUCLA2 53.9%, E. coli 44.0%, T. aquaticus 41.7%.

## Cross-checks on nucleotide-bound structures

| PDB | Enzyme | Ligand | Residue 20β | Contact with base |
|---|---|---|---|---|
| 2FP4 | pig G-SCS, GTP-specific | GTP-Mg | Gln20 | 2.58 A, direct H-bonding side chain |
| 3UFX | T. aquaticus SCS, prefers GDP/GTP | GDP-Mn (4 copies) | Pro20 | 5.56-6.15 A, no contact; ordered waters H-bond the base at 2.31-3.18 A |
| 1CQI | E. coli SCS, prefers ADP/ATP | ADP-Mg (2 copies) | Pro20 | not within 4.0 A; adenine read by Val44, Lys46, Glu99, Ala100, Ala101, Thr102, Ile104, Leu212 |

No crystal or cryo-EM structure of an ATP-specific succinyl-CoA synthetase with a bound adenine
nucleotide was found. RCSB entries mapping to human SUCLA2 are 6G4Q (2.59 A, apo SUCLG1-SUCLA2)
and 9SWJ (3.7 A cryo-EM, CoA only). No structures map to pig SUCLA2 (O97580).

## Numbering caveat

Placing scsC Pro54 at mature position 20 implies a cleaved presequence of 34 residues. UniProt
Q55AI5 currently predicts a 17-residue transit peptide (HAMAP rule MF_03220, ECO:0000255), and
Q869S7 has no transit peptide annotated at all. The "mature position 20" numbering is therefore
alignment-derived, not based on an experimentally determined mature N-terminus.
