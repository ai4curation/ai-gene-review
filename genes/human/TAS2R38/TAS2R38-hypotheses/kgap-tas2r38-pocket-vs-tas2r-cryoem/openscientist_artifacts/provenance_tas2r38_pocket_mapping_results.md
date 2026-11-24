# TAS2R38 (P59533) pocket mapping onto TAS2R cryo-EM structures: computed results

All values below are direct outputs of code run in this job. Structures were
fetched live from RCSB and the AlphaFold DB, sequences from UniProt. No values
are transcribed from publications.

## Inputs

| Resource | Identifier | Notes |
|---|---|---|
| TAS2R38 sequence | UniProt P59533, 333 aa | canonical is A49 / A262 / I296, i.e. the AAI haplotype, not PAV and not AVI |
| TAS2R38 model | AF-P59533-F1-model_v6.pdb | AlphaFold DB |
| TAS2R46 + strychnine | PDB 7XP6, chain R, ligand SY9 501, 3.01 A | Xu et al. 2022, PMID 36108005 |
| TAS2R14 + cholesterol / aristolochic acid A | PDB 8XQO, chain R, CLR 502 and GOQ 501, 2.77 A | |
| TAS2R14 + flufenamic acid x2 | PDB 8RQL, chain R, FLF 401 and FLF 402, 3.03 A | |
| human TAS2R paralogs | UniProt reviewed, 28 sequences | TAS2R38 plus 27 others |

A search of the RCSB Search API v2 for PDB entries mapped to UniProt P59533
returned HTTP 204 with an empty body: there is no experimental structure of
TAS2R38.

## 1. Which ligand copy is orthosteric

Minimum heavy-atom distance from each modelled ligand to the Galpha chain.

| Entry | Ligand | dist to Galpha (A) | receptor contacts <=4.5 A | site |
|---|---|---|---|---|
| 7XP6 | SY9 (strychnine) | 27.3 | 8 | extracellular / orthosteric |
| 8XQO | CLR (cholesterol) | 23.7 | 20 | extracellular / orthosteric |
| 8XQO | GOQ (aristolochic acid A) | 3.4 | 17 | intracellular |
| 8RQL | FLF 401 (flufenamic acid) | 30.7 | 12 | extracellular / orthosteric |
| 8RQL | FLF 402 (flufenamic acid) | 3.1 | 13 | intracellular |

Structural superposition of 7XP6 chain R on 8XQO chain R (TM-score 0.839,
268 aligned pairs, core RMSD 1.90 A) places the strychnine centroid 25.2 A
from the aristolochic acid centroid, closest heavy-atom approach 18.9 A, and
the two contact residue sets have zero overlap. The strychnine site instead
coincides with the cholesterol site (TAS2R46 L62/N65/Y85/W88/T180/S248/F252/E265
map to TAS2R14 I62/S65/T86/W89/S183/F247/V251/Q266).

## 2. Superposition of the TAS2R38 AlphaFold model

| Template | TM-score | aligned pairs | core Calpha RMSD (A) |
|---|---|---|---|
| TAS2R46 / 7XP6 | 0.763 | 283 | 2.65 |
| TAS2R14 / 8XQO | 0.707 | 281 | 2.35 |
| TAS2R14 / 8RQL | 0.737 | 278 | 2.40 |

Sequence identity (global Needleman-Wunsch, BLOSUM62): TAS2R38 vs TAS2R46
32.2% over 304 aligned positions; TAS2R38 vs TAS2R14 32.0% over 306.

Agreement between the sequence-derived and structure-derived residue mapping:
74% (7XP6), 74% (8XQO), 79% (8RQL). Commonest disagreement offsets +1, +3,
+5 and +8 residues.

## 3. TAS2R38 equivalents of the template orthosteric pockets

Union over the three templates of residues within 4.5 A of the extracellular
ligand, transferred by structural equivalence:

L71, S74, E86, Y92, I95, I96, **W99**, **N103**, Q185, L189, S194, **F197**,
C198, **W201**, F256, S260, A263, S266, L270, V279, C282, V283, I285, M286

Bold = residue named in the Marchiori/Behrens MM/CG mutagenesis set or the
Biarnes toggle residue. F264 is not in the union but A263 is.

## 4. Per-residue measurements in the superposed model

Minimum heavy-atom distance (A) from the TAS2R38 AlphaFold residue to the
indicated superposed feature. `d_cav` is distance to the largest buried
cavity detected in the model; `d_a5` is distance to the six C-terminal
residues of the Galpha alpha5 helix.

| residue | class | pLDDT | d_strychnine | d_cholesterol | d_flufenamic | d_cav | d_intracellular | d_a5 | in orthosteric map | lines largest cavity |
|---|---|---|---|---|---|---|---|---|---|---|
| A49 | HAPLOTYPE | 87.5 | 34.07 | 32.54 | 34.84 | 8.86 | 19.10 | 8.27 | no | no |
| W99 | Biarnes 2010 | 93.6 | 2.44 | 2.64 | 3.55 | 19.28 | 16.76 | 23.57 | yes | no |
| M100 | Biarnes 2010 | 91.2 | 3.75 | 5.53 | 6.38 | 20.05 | 16.78 | 24.51 | no | no |
| N103 | Marchiori 2013 | 91.6 | 7.41 | 4.83 | 8.60 | 15.15 | 11.85 | 19.62 | yes | no |
| F197 | Marchiori 2013 | 84.4 | 10.38 | 12.94 | 14.53 | 25.50 | 21.52 | 29.34 | yes | no |
| W201 | Marchiori 2013 | 86.3 | 13.41 | 13.24 | 16.50 | 20.46 | 16.45 | 23.88 | yes | no |
| F255 | Biarnes 2010 | 89.8 | 13.98 | 7.37 | 15.01 | 9.11 | 7.10 | 12.51 | no | no |
| S259 | Biarnes 2010 | 92.8 | 8.80 | 1.70 | 9.93 | 13.69 | 10.41 | 18.01 | no | no |
| A262 | HAPLOTYPE | 94.9 | 5.88 | 2.12 | 7.91 | 19.16 | 15.42 | 23.41 | no | no |
| F264 | Marchiori 2013 | 90.6 | 6.68 | 3.84 | 9.22 | 21.15 | 17.28 | 25.51 | no | no |
| I296 | HAPLOTYPE | 86.0 | 21.92 | 15.89 | 22.59 | 5.12 | 5.44 | 6.35 | no | yes |

## 5. Contiguity of the mutagenesis set

Pairwise minimum heavy-atom distances (A) in the AlphaFold model:

|  | W99 | M100 | N103 | F197 | W201 | F264 |
|---|---|---|---|---|---|---|
| W99 | 0.0 | 1.3 | 2.8 | 11.2 | 11.6 | 5.6 |
| M100 | 1.3 | 0.0 | 3.4 | 7.5 | 8.3 | 8.6 |
| N103 | 2.8 | 3.4 | 0.0 | 11.1 | 8.9 | 6.9 |
| F197 | 11.2 | 7.5 | 11.1 | 0.0 | 3.0 | 9.1 |
| W201 | 11.6 | 8.3 | 8.9 | 3.0 | 0.0 | 10.0 |
| F264 | 5.6 | 8.6 | 6.9 | 9.1 | 10.0 | 0.0 |

Connected components at an 8 A cutoff: one component containing all of
99, 100, 103, 197, 201, 264. The set is contiguous, but spans ~12 A, more
than a single phenylthiocarbamide molecule can bridge.

## 6. Cavity detection in the TAS2R38 AlphaFold model, unrestricted scan

1 A grid, residues with pLDDT >= 70, probe-accessible points >3.3 A from any
heavy atom, buriedness >= 24 of 26 ray directions, single-linkage clustering
at 1.5 A. 22856 interior candidates, 361 buried points, 28 clusters, three
largest 176 / 54 / 27 points.

Largest cavity (~176 A^3) lining residues: S51, S53, D54, L113, Y117, C118,
K120, L216, S219, L220, E240, A241, H242, K244, A245, S248, L249, F252, H293,
L297, G300, N301, A302, K303, R305.

Closest approach from this cavity to the superposed orthosteric ligands:
17.9 A (cholesterol), 23.0 A (strychnine), 23.9 A (flufenamic acid). The
cavity overlaps the TAS2R38 equivalents of the TAS2R14 intracellular site.
No discrete buried cavity was detected at the orthosteric site in this
unrestricted scan.

## 7. Focused cavity probe at the transferred orthosteric position

Same algorithm, search box centred on the agonist position transferred from
the superposed cryo-EM templates.

| buriedness cutoff | volume of the cluster nearest the agonist | centroid offset from transferred agonist |
|---|---|---|
| >= 20 of 26 | 34 A^3 | 0.9 A |
| >= 22 of 26 | 34 A^3 | 0.9 A |
| >= 24 of 26 | 34 A^3 | 0.9 A |

Lining residues: L70, L71, S74, Y92, I95, I96, W99, S266, V267, L270, V279,
V283, M286. Nine of these 13 are in the section 3 orthosteric union, which is
an independent derivation.

Distance from this cavity to the residues of interest (A):

| W99 | M100 | A262 | N103 | F264 | F197 | W201 | I296 | A49 |
|---|---|---|---|---|---|---|---|---|
| 3.03 (lines) | 5.50 | 6.02 | 7.65 | 7.67 | 12.73 | 15.55 | 20.67 | 33.73 |

At 34 A^3 this cavity is about one fifth the volume of the intracellular
cavity in the same model and too small to hold phenylthiocarbamide, which is
the expected signature of a ligand-free, non-activated model.

## 8. Paralog conservation by site (28 reviewed human TAS2Rs)

Each of the 27 paralogs aligned to TAS2R38 by global Needleman-Wunsch,
BLOSUM62, affine gaps (open -11, extend -1). Global identity to TAS2R38
ranges 0.201 (TAS2R16) to 0.315 (TAS2R7).

| position set | n | mean identity | median | IQR |
|---|---|---|---|---|
| orthosteric-site equivalents (section 3) | 24 | 0.261 | 0.185 | 0.111-0.389 |
| intracellular cavity lining (section 6) | 25 | 0.673 | 0.815 | 0.333-0.926 |
| rest of residues 45-310 | 217 | 0.254 | 0.148 | 0.037-0.407 |

| comparison | Mann-Whitney U | p | Cliff delta |
|---|---|---|---|
| intracellular vs rest | 4550 | 2.7e-08 | +0.677 |
| intracellular vs orthosteric | 502 | 5.3e-05 | +0.673 |
| orthosteric vs rest | 2880 | 0.39 | +0.106 |

## 9. Residue spectrum at the positions of interest

| pos | P59533 | paralog consensus | consensus frequency | spectrum |
|---|---|---|---|---|
| 49 | A | K | 16/26 (0.62) | K:16, R:4, E:1, A:1, T:1 |
| 99 | W | W | 22/27 (0.81) | W:22, F:3, S:1, T:1 |
| 100 | M | A | 9/27 (0.33) | A:9, T:5, V:4, I:3, M:2 |
| 103 | N | N | 22/27 (0.81) | N:22, S:2, G:2, D:1 |
| 197 | F | V | 9/25 (0.36) | V:9, F:6, L:5, T:2, K:2 |
| 201 | W | A | 11/27 (0.41) | A:11, G:6, F:4, W:4, S:1 |
| 255 | F | L | 22/27 (0.81) | L:22, F:4, V:1 |
| 259 | S | Y | 16/26 (0.62) | Y:16, S:3, F:2, N:2, L:1 |
| 262 | A | S / A | 9/26 each (0.35) | S:9, A:9, C:3, V:2, M:1 |
| 264 | F | F | 8/27 (0.30) | F:8, I:7, L:6, M:2, K:1 |
| 296 | I | I | 21/27 (0.78) | I:21, L:3, V:1, S:1, Q:1 |

Haplotype alleles against the family: P49 0/26 paralogs, A49 1/26;
A262 9/26, V262 2/26; V296 1/27, I296 21/27.

## 10. Conformational state and regional accuracy of the model

Mean per-residue Calpha deviation after optimal superposition on the two
active, G-protein-bound templates.

| region | n | dev vs 7XP6 (A) | dev vs 8XQO (A) | mean pLDDT |
|---|---|---|---|---|
| intracellular cavity lining (section 6) | 23-25 | 1.64 | 1.94 | 82.9 |
| TM3 cytoplasmic end 118-134 | 17 | 3.00 | 2.93 | |
| ICL3 / TM6 cytoplasmic end 232-252 | 12-21 | 2.73 | 3.41 | 74.3 |
| orthosteric-site equivalents (section 3) | 23-24 | 4.01 | 6.16 | 88.8 |
| ECL2 region 145-174 | 30 | 8.86 | 14.32 | 68.6 |
| all aligned residues | 281-283 | 3.57 | 4.51 | 82.2 |

Ten largest deviations against 7XP6: E86 15.1, P87 13.0, K83 12.7, F168 11.8,
F162 11.8, T155 11.6, V159 11.6, I148 11.3, A323 11.2, C152 10.6.
Against 8XQO: P166 21.0, F168 20.3, F163 20.2, V159 17.9, S164 17.6, W160 17.0,
V156 16.8, C152 16.3, T155 15.5, F162 15.5. Both lists are dominated by ECL2.

## 11. Per-residue model reliability at the residues of interest

| residue | class | pLDDT | dev vs 7XP6 (A) | dev vs 8XQO (A) | region |
|---|---|---|---|---|---|
| A49 | haplotype | 87.5 | 2.26 | 4.15 | TM1 cytoplasmic |
| W99 | literature pocket | 93.6 | 3.60 | 1.40 | TM3 |
| M100 | literature pocket | 91.2 | 3.70 | 1.07 | TM3 |
| N103 | literature pocket | 91.6 | 2.62 | 1.15 | TM3 |
| F197 | literature pocket | 84.4 | 3.78 | 9.70 | TM5 extracellular end |
| W201 | literature pocket | 86.2 | 5.96 | 10.11 | TM5 extracellular end |
| F255 | literature pocket | 89.8 | 1.68 | 5.88 | TM6 |
| S259 | literature pocket | 92.8 | 1.87 | 7.66 | TM6 |
| A262 | haplotype | 94.9 | 2.62 | 8.07 | TM6 |
| F264 | literature pocket | 90.6 | 4.09 | 6.87 | TM6 |
| I296 | haplotype | 86.0 | 1.90 | 1.76 | TM7 cytoplasmic |

## Figures

- `plot_1.png`, `plot_2.png`: paralog conservation by site, and conservation
  along the TAS2R38 sequence with the site memberships marked.
- `plot_3.png`: residue spectrum across the 27 paralogs at the three
  haplotype positions.
- `plot_4.png`: per-residue Calpha deviation of the apo model from both
  active cryo-EM templates along the sequence.
- `plot_5.png`: per-residue deviation and pLDDT at the 11 residues of interest.

## Tools and resources that could not be used

- No experimental structure of TAS2R38 exists (RCSB Search API v2 on UniProt
  P59533 returned HTTP 204, empty result).
- Biopython is not available in the execution environment, so the PDB parser,
  the Needleman-Wunsch implementation and the TM-align-style structural
  superposition were written from scratch for this job. They are approximations
  of the standard tools, not the standard tools themselves.
- No experimental TAS2R38 ligand-bound structure, no TAS2R38 PTC co-structure
  and no TAS2R38 molecular dynamics trajectory were available to validate the
  cavity results.
