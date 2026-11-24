# GLIPR1 against its human CAP paralogs: computed results (iteration 2)

Code: `glipr1_paralog_comparison.py`. Figure: `plot_2.png`.
All numbers below are output of code executed in this job.

Inputs
- Crystal structures from RCSB: 3Q2U (GLIPR1, chain A), 5ETE (Pry1 CAP, chain A),
  1SMB (GAPR-1, chain A), 3U3N (tablysin-15 + palmitate, chain C).
- AlphaFold v6 models fetched from the EBI API inside the code executor (the same files
  returned HTTP 403 to the host shell in iteration 1): P48060 GLIPR1, P16562 CRISP2,
  P54107 CRISP1, P54108 CRISP3, Q6UXB8 PI16, Q6UWM5 GLIPR1L1.
- Each model trimmed to the UniProt SCP domain plus 6 residues on each side, then residues
  with pLDDT below 70 discarded.

RCSB Search API v2 query by UniProt accession returned experimental structures only for
P48060 (3Q2R, 3Q2U), P16562 (2CQ7), Q9H4G4 (1SMB, 4AIW, 5VHG) and P47032 (5ETE, 5JYS).
CRISP1, CRISP3, PI16 and GLIPR1L1 have **no** PDB entry (HTTP 204, empty result set), which
is why AlphaFold models were used for the paralog comparison.

## Table 1. AlphaFold models used

| accession | protein | SCP domain | residues kept (pLDDT >= 70) | mean pLDDT |
|---|---|---|---|---|
| P48060 | GLIPR1 | 38-175 | 150 | 97.4 |
| P16562 | CRISP2 | 41-169 | 141 | 97.6 |
| P54107 | CRISP1 | 45-175 | 140 | 96.2 |
| P54108 | CRISP3 | 43-171 | 141 | 97.7 |
| Q6UXB8 | PI16 | 37-165 | 141 | 96.6 |
| Q6UWM5 | GLIPR1L1 | 39-171 | 145 | 98.0 |

## Table 2. Palmitate transplantation and buried cavities, all structures treated identically

Each domain was superposed onto tablysin-15 3U3N (TM-align-style algorithm implemented here),
the tablysin palmitate was moved into the target frame by the inverse transform, and contacts
were counted over all protein heavy atoms. Cavity detection: LIGSITE-style, 1.0 A grid,
1.4 A probe, PSP threshold 6 of 13 directions, lining residues within 5 A, hydrophobic set
AVLIMFWCPG.

| protein | source | TM vs tablysin | palmitate contacts < 2.8 A | ligand atoms with >= 3.2 A clearance | largest cavity | hyd. frac. | most hydrophobic cavity >= 60 A^3 | hyd. frac. | residue at tablysin Gly129 |
|---|---|---|---|---|---|---|---|---|---|
| tablysin-15 | xtal 3U3N | 1.000 | 0 | 18/18 | 437 A^3 | 0.27 | 166 A^3 | 0.74 | G129 |
| Pry1 | xtal 5ETE | 0.727 | 52 | 0/18 | 369 A^3 | 0.37 | 75 A^3 | 0.62 | W230 |
| GAPR-1 | xtal 1SMB | 0.677 | 67 | 0/18 | 224 A^3 | 0.42 | 224 A^3 | 0.42 | W83 |
| GLIPR1 | xtal 3Q2U | 0.768 | 58 | 1/18 | 422 A^3 | 0.45 | 76 A^3 | 0.47 | W117 |
| GLIPR1 | AF P48060 | 0.810 | 55 | 1/18 | 244 A^3 | 0.50 | 244 A^3 | 0.50 | W117 |
| CRISP1 | AF P54107 | 0.858 | 58 | 0/18 | 670 A^3 | 0.45 | 64 A^3 | 0.73 | W119 |
| CRISP2 | AF P16562 | 0.832 | 45 | 4/18 | 227 A^3 | 0.62 | 227 A^3 | 0.62 | W114 |
| CRISP3 | AF P54108 | 0.829 | 44 | 5/18 | 253 A^3 | 0.67 | 253 A^3 | 0.67 | W116 |
| PI16 | AF Q6UXB8 | 0.831 | 49 | 1/18 | 388 A^3 | 0.53 | 85 A^3 | 0.62 | W106 |
| GLIPR1L1 | AF Q6UWM5 | 0.822 | 72 | 1/18 | 217 A^3 | 0.68 | 217 A^3 | 0.68 | W117 |

Controls. The self-superposition of tablysin-15 gives 0 contacts and 18 of 18 free ligand
atoms, so the transplantation code is correct. Pry1, which binds fatty acids at micromolar
affinity (PMID 28365570), gives 52 contacts and 0 of 18 free, i.e. it fails the test as badly
as GLIPR1. **The rigid transplantation metric therefore does not discriminate fatty-acid
binders from non-binders and must not be used to claim that GLIPR1 lost a fatty-acid site.**
The tablysin-15 Gly129 is the outlier: every other CAP domain examined, including Pry1 and
GAPR-1, has a tryptophan at that position.

## Table 3. Caveolin-binding-motif scan inside each SCP domain

Patterns, Phi = W/F/Y: `PhiXPhiXXXXPhi`, `PhiXXXXPhiXXPhi`, `PhiXPhiXXXXPhiXXPhi`.

| protein | accession | domain scanned | match |
|---|---|---|---|
| Pry1 | P47032 | 167-281 | YDFSNPGF at 237 |
| GAPR-1 | Q9H4G4 | 14-132 | YNFQQPGF at 90 |
| GLIPR1 | P48060 | 38-175 | none |
| CRISP1 | P54107 | 45-175 | none |
| CRISP2 | P16562 | 41-169 | none |
| CRISP3 | P54108 | 43-171 | none |
| PI16 | Q6UXB8 | 37-165 | none |
| GLIPR1L1 | Q6UWM5 | 39-171 | YNETQFYDF at 118 (different position) |

## Table 4. Structural equivalents of the Pry1 CBM loop Y237-DFSNPG-F244

Each AlphaFold CAP domain superposed onto Pry1 5ETE, residues read off the alignment.

| protein | TM vs Pry1 CAP | segment | sequence | residues at Pry1 Y237 / F239 / F244 | aromatics retained |
|---|---|---|---|---|---|
| Pry1 | 1.000 | 237-244 | YDFSNPGF | Y237 / F239 / F244 | 3/3 |
| GLIPR1 | 0.689 | 124-131 | YDFKTRIC | Y124 / F126 / C131 | 2/3 |
| CRISP2 | 0.736 | 121-128 | FVYGVGPK | F121 / Y123 / K128 | 2/3 |
| CRISP3 | 0.730 | 123-130 | FDFGVGPK | F123 / F125 / K130 | 2/3 |
| GLIPR1L1 | 0.706 | 124-131 | YDFDSLSC | Y124 / F126 / C131 | 2/3 |
| CRISP1 | 0.714 | 126-133 | FKHGEWTT | F126 / H128 / T133 | 1/3 |
| PI16 | 0.760 | 113-120 | YNLSAATC | Y113 / L115 / C120 | 1/3 |

CRISP2 binds cholesterol in vitro and complements yeast *pry1 pry2* (PMID 23027975), and its
CBM loop is degenerate to exactly the same degree as GLIPR1's (2 of 3 aromatics, third
position replaced by a non-aromatic). **CBM status therefore has no discriminating power for
sterol binding in human CAP proteins.**

## Reconciliation with iteration 1

- Cavity volumes are identical after the PSP scan was rewritten in vectorised form
  (GLIPR1 3Q2U 422 / 112 / 95 A^3; tablysin-15 3U3N 437 / 166 / 141 A^3).
- Hydrophobic lining fractions differ slightly between the two runs (3Q2U cavity 1: 0.39 then
  0.45; 3U3N cavity 2: 0.70 then 0.74) because the set of residues counted as hydrophobic was
  not identical. Iteration 2 uses AVLIMFWCPG throughout. The contrast between GLIPR1 and
  tablysin-15 is the same in both runs.
- The palmitate contact count reported in iteration 1 (23 contacts below 2.8 A for GLIPR1) was
  computed on a reduced atom set. The superposition is identical (min 0.41 A, median 1.90 A in
  both runs). The current definition, all protein heavy atoms, gives 58 contacts. The metric
  is reported here only alongside its controls, which it fails.
- Iteration 1 attributed the missing channel to GLIPR1-specific substitutions (Gly129 to
  Trp117, Val50 to Phe44). Table 2 shows the Trp is family-wide. That part of the iteration-1
  interpretation is withdrawn.
