# Iteration 2 provenance: 3D verification and expression check

## 1. AlphaFold superposition onto the GTP-bound pig G-SCS beta subunit

Models: AF-Q55AI5-F1 v6 (scsC, global pLDDT 89.5), AF-Q869S7-F1 v6 (scsB, global pLDDT 90.9),
retrieved from the AlphaFold DB API (versions v2-v4 return HTTP 404; v6 is current).
Superposition: Needleman-Wunsch residue pairing against the observed chain B of PDB 2FP4,
Kabsch fit on paired CA atoms, six rounds of 90th-percentile outlier trimming.

| Model | CA pairs used | core RMSD |
|---|---|---|
| scsC (Q55AI5) | 353 / 393 | 1.30 A |
| scsB (Q869S7) | 370 / 392 | 0.98 A |

Distance from each mapped residue to the guanine base of GTP after superposition, against the
values measured directly in the pig structure:

| pig site | pig measured (2FP4) | scsB model | pLDDT | scsC model | pLDDT |
|---|---|---|---|---|---|
| Gln20β | 2.58 A | Gln46 **2.59 A** | 95.0 | Pro54 **5.68 A** | 95.0 |
| Val44β | 3.49 A | Val69 4.03 A | 96.8 | Val78 3.96 A | 97.2 |
| Leu69β | 3.58 A | Leu95 4.86 A | 96.7 | Leu103 4.35 A | 95.7 |
| Ala108β | 3.28 A | Ser134 3.93 A | 93.9 | Arg142 3.82 A | 94.1 |
| Leu109β | 2.72 A | Val135 2.76 A | 91.8 | His143 3.32 A | 93.4 |
| Ile111β | 3.72 A | Pro137 3.50 A | 92.4 | Leu145 4.70 A | 93.5 |
| Phe219β | 3.69 A | Met245 2.78 A | 93.8 | Met253 2.81 A | 94.8 |

scsB Gln46 side chain to the polar guanine edge atoms O6/N1/N2/N7: 2.59 A, hydrogen-bonding range.

## 2. Residue 20β to purine base, across all available nucleotide complexes

| Enzyme | PDB / model | Residue 20β | Distance to base | Measured nucleotide use |
|---|---|---|---|---|
| pig G-SCS | 2FP4 (GTP-Mg) | Gln | 2.58 A | GTP-specific |
| T. aquaticus SCS | 3UFX (GDP-Mn, 4 copies) | Pro | 5.77 +/- 0.23 A | dual, prefers GDP/GTP |
| E. coli SCS | 1CQI (ADP-Mg, 2 copies) | Pro | 4.22 +/- 0.15 A | dual, prefers ADP/ATP |
| Dicty scsB | AF model on 2FP4 | Gln46 | 2.59 A | unknown |
| Dicty scsC | AF model on 2FP4 | Pro54 | 5.68 A | unknown |

The two experimentally characterised Pro20β enzymes have opposite nucleotide preferences,
which is the direct basis for calling Pro20β permissive rather than ATP-determining.

## 3. Expression of the three Dictyostelium SCS subunit genes

Source: EBI Expression Atlas baseline experiment E-MTAB-7215, RNA-seq, 13,731 genes,
four cell types, 3 replicates per group. Values are the published median TPM per group.

| Gene | DDB id | cup cell | spore cell | stalk cell | vegetative cell |
|---|---|---|---|---|---|
| scsA alpha | DDB_G0289325 | 8 | 17 | 7 | 590 |
| scsB (Gln20β) | DDB_G0274449 | 16 | 31 | 9 | 313 |
| scsC (Pro20β) | DDB_G0271842 | 6 | 4 | 14 | 236 |

Percentile rank within each sample (cup, spore, stalk, vegetative):
scsA 73.4 / 80.1 / 72.7 / 98.2; scsB 80.1 / 85.4 / 75.4 / 97.1; scsC 70.8 / 66.2 / 79.7 / 96.1.

scsB/scsC TPM ratio: cup 2.67, spore 7.75, stalk 0.64, vegetative 1.33.

Both beta paralogues are abundant in vegetative (growing) cells at close to 1:1, so differential
expression does not explain why the enzyme purified from growing cells used GTP.

## 4. Resources that could not be accessed

- dictyexpress.research.bcm.edu: DNS resolution failure from the execution environment.
- dictybase.org REST path returns the JavaScript single-page application, not queryable data.
- No crystal or cryo-EM structure of any ATP-specific succinyl-CoA synthetase with a bound
  adenine nucleotide exists in the PDB (human SUCLA2 maps only to 6G4Q, apo, and 9SWJ, CoA only).
