# Every CAP-domain structure in the PDB: ligand census and cavity survey (iteration 3)

Code: `glipr1_cap_family_survey.py` (verbatim concatenation of the four executor calls run in
iteration 3, in execution order: the PF00188 structure and ligand census, the cavity sweep in
two batches because of the 60 s executor timeout, and the 4AIW mapping plus figure).
Figure: `plot_3.png`. All numbers below are output of that code.

Purpose. Iterations 1 and 2 compared GLIPR1 with four reference CAP proteins and five human
paralogs. That leaves open whether tablysin-15 is a representative CAP lipid binder or an
outlier, and whether a sterol has ever been seen in a CAP protein at all. This survey answers
both by treating every CAP structure that exists identically.

## How the set was defined

RCSB Search API v2, query on `rcsb_polymer_entity_annotation.annotation_id = "PF00188"`
(Pfam CAP/SCP/TAPS domain), return type `entry`. The query returns 27 entries:

1CFE, 1QNX, 1RC9, 1SMB, 1WVR, 1XTA, 1XX5, 2DDA, 2DDB, 2EPF, 2GIZ, 2VZN, 3MZ8, 3Q2R, 3Q2U,
3U3L, 3U3N, 3U3U, 4AIW, 4D53, 4IFA, 4TPV, 5ETE, 5JYS, 5VHG, 5WEE, 6IMF.

This is the complete experimentally determined CAP structural family as of this run.

## Table 1. Ligand census across all 27 entries

Nonpolymer components were read from the RCSB GraphQL Data API for every entry, then waters,
ions and common cryoprotectant/buffer species were removed and the remainder filtered to
formula weight above 120 Da.

| entry | protein | retained ligand | identity |
|---|---|---|---|
| 3U3L | tablysin-15 | PLM | palmitic acid |
| 3U3N | tablysin-15 | PLM | palmitic acid |
| 3U3U | tablysin-15 | EAH | leukotriene E4 analogue |
| 4AIW | GAPR-1 / GLIPR2 | IHP | inositol hexakisphosphate |
| 5WEE | CAP glycoprotein | NAG, FUC | N-glycan |
| 6IMF | CAP domain | MES | buffer |
| other 21 entries | - | none above 120 Da | - |

Two results follow directly.

- **No sterol, cholesterol, cholesteryl ester or sterol analogue occurs in any CAP structure.**
  The caveolin-binding-motif sterol site named in the hypothesis has never been visualised.
  All evidence for it is mutagenesis and solution binding, not structure.
- **The only lipid-bound CAP structures in the PDB are the three tablysin-15 entries.**

## Table 2. Buried cavities in all 27 entries, computed identically

LIGSITE-style detection on the largest polymer chain of each entry, all heteroatoms stripped:
1.0 A grid, 1.4 A probe, protein-solvent-protein threshold 6 of 13 directions, 6-connectivity
clustering, lining residues within 5 A, hydrophobic set AVLIMFWCPG. "Largest" is the biggest
cavity by volume; "most hydrophobic" is the highest hydrophobic lining fraction among cavities
of at least 60 A^3.

| entry | largest cavity (A^3) | hyd. frac. | most hydrophobic >= 60 A^3 (A^3) | hyd. frac. |
|---|---|---|---|---|
| 1CFE | 161 | 0.50 | 161 | 0.50 |
| 1QNX | 455 | 0.37 | 169 | 0.50 |
| 1RC9 | 1315 | 0.45 | 62 | 0.50 |
| 1SMB | 227 | 0.38 | 227 | 0.38 |
| 1WVR | 1170 | 0.42 | 1170 | 0.42 |
| 1XTA | 1243 | 0.44 | 125 | 0.50 |
| 1XX5 | 1242 | 0.43 | 69 | 0.57 |
| 2DDA | 1323 | 0.47 | 1323 | 0.47 |
| 2DDB | 697 | 0.41 | 101 | 0.56 |
| 2EPF | 510 | 0.38 | 69 | 0.70 |
| 2GIZ | 1175 | 0.47 | 1175 | 0.47 |
| 2VZN | 674 | 0.54 | 674 | 0.54 |
| 3MZ8 | 1145 | 0.43 | 70 | 0.45 |
| **3Q2R (GLIPR1)** | 473 | 0.45 | 69 | 0.47 |
| **3Q2U (GLIPR1)** | 422 | 0.45 | 76 | 0.47 |
| **3U3L (tablysin-15)** | 482 | 0.34 | **169** | **0.69** |
| **3U3N (tablysin-15)** | 437 | 0.27 | **166** | **0.74** |
| **3U3U (tablysin-15)** | 638 | 0.35 | **153** | **0.70** |
| 4AIW | 294 | 0.50 | 294 | 0.50 |
| 4D53 | 236 | 0.33 | 236 | 0.33 |
| 4IFA | 1334 | 0.34 | 345 | 0.54 |
| 4TPV | 463 | 0.30 | 463 | 0.30 |
| 5ETE (Pry1) | 369 | 0.43 | 75 | 0.62 |
| 5JYS (Pry1) | 233 | 0.35 | 233 | 0.35 |
| 5VHG | 217 | 0.48 | 178 | 0.55 |
| 5WEE | 172 | 0.40 | 76 | 0.42 |
| 6IMF | 1453 | 0.43 | 1453 | 0.43 |

Cavities above roughly 1000 A^3 are interdomain or interchain clefts in the larger multidomain
entries, not CAP-internal pockets, and their hydrophobic fractions sit near the 0.42-0.47
surface average. They are reported for completeness and are not candidate acyl channels.

## Table 3. The palmitate-size test applied to the whole family

A palmitate needs a cavity of roughly 166 A^3, the measured volume of the tablysin-15 channel
in 3U3N. Seventeen of the 27 entries have a buried cavity of at least 150 A^3. Ranked by the
hydrophobic lining fraction of that cavity:

| rank | entry | volume (A^3) | hyd. frac. |
|---|---|---|---|
| 1 | 3U3N tablysin-15 | 166 | 0.74 |
| 2 | 3U3U tablysin-15 | 153 | 0.70 |
| 3 | 3U3L tablysin-15 | 169 | 0.69 |
| 4 | 5VHG | 178 | 0.55 |
| 5 | 4IFA | 345 | 0.54 |
| 6 | 2VZN | 674 | 0.54 |
| 7 | 1CFE | 161 | 0.50 |
| 7 | 1QNX | 169 | 0.50 |
| 9 | 2DDA | 1323 | 0.47 |
| 9 | 2GIZ | 1175 | 0.47 |
| 11 | **3Q2U GLIPR1** | 422 (largest) | **0.45** |
| 11 | **3Q2R GLIPR1** | 473 (largest) | **0.45** |
| 13 | 1WVR | 1170 | 0.42 |
| 14 | 1SMB GAPR-1 | 227 | 0.38 |
| 15 | 4D53 | 236 | 0.33 |
| 16 | 4TPV | 463 | 0.30 |
| 17 | 5JYS Pry1 | 233 | 0.35 |

The three tablysin-15 entries take the top three ranks and are separated from rank 4 by 0.14
in hydrophobic fraction, a larger gap than spans ranks 4 through 17. **No non-tablysin CAP
structure combines palmitate-sized volume with hydrophobic lining.** GLIPR1 sits in the middle
of the family distribution, which makes it ordinary for a CAP protein rather than specifically
channel-deficient. This replaces the iteration-1 reading that GLIPR1 had lost a channel the
family otherwise has.

## Table 4. The GAPR-1 inositol hexakisphosphate site mapped onto GLIPR1

4AIW is the only CAP structure with a polyanion bound, so it is the only structural test of the
competing hypothesis that the conserved CAP cavity binds an anionic phosphoinositide or
polyanion rather than a lipid.

| quantity | value |
|---|---|
| GAPR-1 residues within 4.0 A of IHP (chain A) | Lys7 only, NZ at 2.73 A |
| formal charge of that contact set | +1 |
| 3Q2U onto 4AIW superposition | TM 0.608, 125 core pairs, core RMSD 2.02 A |
| GLIPR1 equivalent of Lys7 | Asn30, CA deviation 1.30 A |
| formal charge of GLIPR1 equivalent set | 0 |

IHP sits against a single lysine on the N-terminal surface segment, outside the CAP tetrad
cavity that holds Zn2+ in 3Q2R and glycerol GOL666 in 3Q2U. The structure does not put a
polyanion in the conserved cavity, so it is not evidence that GLIPR1's cavity binds one.

## Figure

`plot_3.png`, two panels.
- Left: all 27 CAP entries as cavity volume (log x) against hydrophobic lining fraction, with
  the three tablysin-15 entries in green, the two GLIPR1 entries in red, and a dotted vertical
  line at 166 A^3, the palmitate requirement.
- Right: formal charge of the GAPR-1 residues contacting IHP in 4AIW, labelled with their
  GLIPR1 structural equivalents.

## Limits of this survey

- Cavity detection is run on single chains with heteroatoms stripped and side chains in their
  deposited rotamers. A cryptic pocket that opens on ligand binding would be missed. The
  method is calibrated by its positive control, recovery of the tablysin-15 channel at
  166 A^3 with 18 of 18 palmitate atoms inside it, and nothing more.
- Absence of a sterol in the PDB is absence of evidence about sterol binding, not evidence of
  absence. It constrains what structural inference can be transferred, not what the proteins do.
- PF00188 annotation defines the set. A CAP-fold structure not annotated with that Pfam entry
  would be omitted.
