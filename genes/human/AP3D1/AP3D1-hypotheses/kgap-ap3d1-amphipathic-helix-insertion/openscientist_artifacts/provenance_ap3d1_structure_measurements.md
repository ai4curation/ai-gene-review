# AP3D1 (O14617) N-terminus in experimental AP-3 structures

All values computed in this job by parsing mmCIF files downloaded from RCSB
(`https://files.rcsb.org/download/<ID>.cif`) and measuring coordinates directly.
SASA was computed with a Shrake-Rupley implementation (probe 1.4 A, 96 sphere points)
and normalised with the Tien et al. theoretical Gly-X-Gly maxima.

## Table 1. Modelled delta (AP3D1) residue ranges

| PDB | Description | Method / resolution | Delta chain | Modelled delta residues | Residues 1-17 modelled? |
|---|---|---|---|---|---|
| 9C5C | Human AP-3, apo | cryo-EM 3.6 A | D | 18-650 | no |
| 9C58 | AP-3 + myristoylated Arf1 (Q71L) | cryo-EM 4.7 A | D | 18-601 | no |
| 9RTW | Mammalian AP-3 on tubular membranes | cryo-EM 7.4 A | D | 18-632 | no |
| 9C59 | AP-3 dimer + myr-Arf1 + LAMP1 cargo on lipid nanodisc | cryo-EM 4.3 A | D, d | 1-605 | yes |
| 9C5B | Same, combined map | cryo-EM 4.5 A | D | 1-605 | yes |
| 4AFI | VAMP7 longin domain + delta fragment | X-ray 2.8 A | A, B | 19-173 (delta-ear region) | not applicable |
| 7P3X | Yeast AP-3 homology model into EM map | EM 9.1 A | A | 63-638 | no |

## Table 2. Helicity of delta residues 1-40 in 9C59 (CA i to i+4 distance; alpha helix approx. 6.2 A)

| i - i+4 | d (A) | i - i+4 | d (A) | i - i+4 | d (A) |
|---|---|---|---|---|---|
| 1-5 | 6.63 | 13-17 | 9.83 | 25-29 | 5.49 |
| 2-6 | 6.30 | 14-18 | 13.31 | 26-30 | 9.09 |
| 3-7 | 6.11 | 15-19 | 11.35 | 27-31 | 8.82 |
| 4-8 | 6.23 | 16-20 | 5.07 | 28-32 | 5.51 |
| 5-9 | 6.17 | 17-21 | 5.92 | 29-33 | 8.32 |
| 6-10 | 6.15 | 18-22 | 6.23 | 30-34 | 8.91 |
| 7-11 | 6.16 | 19-23 | 6.10 | 31-35 | 5.86 |
| 8-12 | 6.16 | 20-24 | 6.05 | 32-36 | 6.00 |
| 9-13 | 6.18 | 21-25 | 6.20 | 33-37 | 6.08 |
| 10-14 | 6.30 | 22-26 | 6.10 | 34-38 | 6.27 |
| 11-15 | 5.96 | 23-27 | 6.16 | 35-39 | 6.11 |
| 12-16 | 7.91 | 24-28 | 5.88 | 36-40 | 5.91 |

Interpretation: residues 1-15 are a continuous alpha helix; residues 12-17 break the
helix; residues 16/17 onward restart as the first helix of the alpha-solenoid trunk.
The two helices are therefore distinct structural elements.

## Table 3. Local model confidence and position relative to the bilayer (9C59)

| Measurement | Value |
|---|---|
| Mean atomic B factor, delta residues 1-17 | 266.8 |
| Mean atomic B factor, delta residues 18-60 | 183.2 |
| Mean atomic B factor, whole delta chain | 206.2 |
| Min heavy-atom distance, delta 1-14 to Arf1 myristoyl helix (chains C/c res 2-17) | 31.9 A (mean 55.0 A) |
| Min heavy-atom distance, delta 1-14 to LAMP1 cargo res 410-411 | 31.4 A (mean 60.0 A) |
| Min heavy-atom distance, mu3 res 160-180 to Arf1 myristoyl helix (scale reference) | 12.0 A |
| Min heavy-atom distance, delta res 300-320 (solenoid core) to Arf1 myristoyl helix | 37.9 A |

The Arf1 N-terminal myristoylated amphipathic helix is the only unambiguously
bilayer-embedded element in the deposited model (no lipids are present; HETATM records
contain only GTP and Mg). A membrane-inserting helix would have to be essentially
coplanar with it. Note that a direct bilayer-plane fit was attempted and rejected: the
two Arf1 helices in the dimer are nearly collinear (axis-axis angle 38.7 deg, centroid
separation 32.2 A, angle between axis C and the centroid-linking vector 80 deg), so a
plane fitted to them is degenerate and places the two AP-3 copies on opposite sides.
Direct interatomic distances are reported instead, which require no plane fit.

## Table 4. Relative solvent accessibility of delta residues 1-30 in 9C59 (whole complex)

Residues 1-17 RSA: M1 0.84, A2 0.52, L3 0.69, K4 0.68, M5 0.63, V6 0.42, K7 0.51,
G8 0.40, S9 0.24, I10 0.40, D11 0.35, R12 0.39, M13 0.68, F14 0.69, D15 0.24, K16 0.25,
N17 0.30. Isolated-chain and whole-complex values are identical over 1-17, so the helix
makes no contact with the rest of the complex in this model. From L18 onward the
whole-complex values drop below the isolated-chain values (L18 0.20 vs 0.37, Q19 0.29 vs
0.55, V22 0.01 vs 0.21), marking the start of trunk packing.
