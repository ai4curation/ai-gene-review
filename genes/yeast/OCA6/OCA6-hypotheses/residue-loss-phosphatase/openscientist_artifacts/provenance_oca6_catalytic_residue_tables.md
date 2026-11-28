# OCA6 (Q12454) catalytic residue analysis: computed provenance tables

All values below were computed in this job with `execute_code` against live UniProt,
InterPro, AlphaFold DB, RCSB and QuickGO web services. Code is in the job transcript.

## Table 1. CX5R P-loop mapping (Needleman-Wunsch, BLOSUM62, gap open -11, extend -1)

Reference: S. cerevisiae Siw14/Oca3 (P53965), catalytic Cys214, invariant Arg220,
P-loop `C214-N-R-G-K-H-R220`.

| Protein | UniProt | NW score vs Siw14 | % id (aligned cols) | Siw14 P-loop cols | Query P-loop cols | Residue at cat-Cys | Residue at inv-Arg | Cys OK | Arg OK |
|---|---|---|---|---|---|---|---|---|---|
| ScOca6 | Q12454 | -7.0 | 31.3 | IHCNRGKHRTGC | MHCTNGELIISL | C114 | **I120** | yes | **NO** |
| ScOca1 | P50946 | 205.0 | 33.8 | IHCNRGKHRTGC | VCCGMGRHRTGT | C168 | R174 | yes | yes |
| ScOca2 | P53949 | 86.0 | 38.0 | IHCNRGKHRTGC | VHSNKGKHRVGV | S102 | R108 | **NO** | yes |
| SpSiw14 | Q9UUF3 | 227.0 | 34.6 | IHCNRGKHRTGC | LHCSRGKHRTGI | C189 | R195 | yes | yes |
| AtDSP1 | Q9ZVN4 | 405.0 | 49.5 | IHCNRGKHRTGC | IHCKRGKHRTGC | C150 | R156 | yes | yes |
| AtDSP2 | Q84MD6 | 332.0 | 44.8 | IHCNRGKHRTGC | IHCKRGKHRTGC | C192 | R198 | yes | yes |
| AtDSP4 | Q940L5 | 353.0 | 46.1 | IHCNRGKHRTGC | IHCKSGKHRTGC | C126 | R132 | yes | yes |
| HsDUSP3 (VHR) | P51452 | -26.0 | 31.8 | IHCNRGKHRTGC | VHCREGYSRSPT | C124 | R130 | yes | yes |
| HsLaforin | O95278 | -27.0 | 23.6 | IHCNRGKHRTGC | VHCNAGVGRTAA | C266 | R272 | yes | yes |

Oca6 is the only protein in this panel without an arginine at the +6 position.

## Table 2. Exhaustive CX5R scan of Oca6 (Q12454, 224 aa)

| Cysteine | Local context | Residue at +6 | CX5R? |
|---|---|---|---|
| C56 | VKF**C**EENNIKTIH | K | no |
| C68 | HIK**C**QSERKADKT | A | no |
| C98 | VVR**C**VKFLIDKGH | D | no |
| C110 | HYP**C**YMHCTNGEL | N | no |
| C114 | YMH**C**TNGELIISL | I | no |
| C127 | VVA**C**MRKFSYWST | Y | no |

- `C[A-Z]{5}R` present anywhere in Q12454: **False**
- `C[A-Z]{5}R[ST]` (PTP signature) present: **False**
- `HC[A-Z]{5}R` present: **False**

## Table 3. InterPro / PANTHER assignment for Q12454

| Source | Accession | Type | Name | Span |
|---|---|---|---|---|
| CDD | cd17663 | domain | atypical DSPs similar to oxidant-induced cell-cycle arrest proteins | 4-181 |
| Gene3D | G3DSA:3.90.190.10 | superfamily | Protein tyrosine phosphatase superfamily | 2-164 |
| InterPro | IPR004861 | family | Atypical dual-specificity phosphatase Siw14-like | 3-179 |
| InterPro | IPR020422 | domain | Dual specificity protein phosphatase domain | 8-170 |
| InterPro | IPR029021 | superfamily | Protein-tyrosine phosphatase-like | 2-164 |
| Pfam | PF03162 | domain | Tyrosine phosphatase family | 3-179 |
| PROSITE | PS50054 | domain | DSP domain profile | 8-170 |
| PANTHER | PTHR31126 | family | TYROSINE-PROTEIN PHOSPHATASE | 3-172 |
| SUPFAM | SSF52799 | superfamily | (Phosphotyrosine protein) phosphatases II | 3-154 |

The fold assignment is unambiguous; the catalytic motif is not present.

## Table 4. Clade-wide motif census, 341 PTHR31126 proteins from Saccharomycetes (taxid 4891)

Method: ungapped BLOSUM62 window scan with the Siw14 probe `IHCNRGKHRTGCLIGCIRKLQNW`
(Siw14 213-235), with the catalytic-Cys and +6 columns masked so the scan cannot be
biased toward finding an arginine. Validation: the masked scan reproduced the
independent full Needleman-Wunsch catalytic-Cys positions for Siw14 (214), Oca1 (168),
Oca2 (102) and Oca6 (114) exactly. 329/341 proteins gave confident assignments
(window score >= 20).

Residue at the invariant-Arg (+6) position, all 329: R 215, K 46, I 32, V 31, N 4, S 1.
Residue at the catalytic-Cys position, all 329: C 195, S 66, N 55, D 5, K 4, F 2, A 1, V 1.

By P-loop subfamily (nearest archetype among Siw14 / Oca1 / Oca2 / Oca6 windows,
catalytic columns masked):

| Subfamily | n | Arg at +6 | no Arg at +6 | Cys present | Cys absent | mean net charge of 7-res CX5R loop (SD) |
|---|---|---|---|---|---|---|
| Siw14-like | 124 | 76 | 48 | 65 | 59 | +1.63 (1.47) |
| Oca1-like | 66 | 65 | 1 | 64 | 2 | +1.97 (0.25) |
| Oca2-like | 75 | 74 | 1 | 12 | 63 | +2.64 (0.80) |
| **Oca6-like** | **64** | **0** | **64** | **54** | **10** | **-0.98 (0.58)** |

Fisher exact, Arg(+6) retention Siw14-like vs Oca6-like: table [[76, 48], [0, 64]],
p = 1.0e-19.

Oca6-like clade: 64 proteins from 59 species. Arg at +6 in 0/64 (0%). Catalytic Cys
retained in 54/64 (84%). Residues observed at +6: Ile 32, Val 31, Lys 1.
Species span Saccharomyces (cerevisiae, uvarum, eubayanus, kudriavzevii, mikatae,
arboricola, pastorianus), Kazachstania africana, Naumovozyma dairenensis and castellii,
Lachancea (thermotolerans, fermentati, nothofagi, dasiensis, meyersii, mirantina,
lanzarotensis, quebecensis), Torulaspora delbrueckii and globosa, Zygosaccharomyces
bailii and mellis, Zygotorulaspora mrakii, Nakaseomyces bracarensis, Candida glabrata,
Eremothecium gossypii and sinecaudum, Henningerozyma blattae, Hanseniaspora osmophila,
Saccharomycodes ludwigii, Wickerhamomyces anomalus and ciferrii, Ascoidea rubescens,
Monosporozyma unispora and servazzii, Maudiozyma spp., Waltiozyma spp.

## Table 5. Active-site geometry: catalytic Cys SG to nearest cationic group

AlphaFold DB models (v6) unless marked experimental.

| Protein | Source | Catalytic Cys | P-loop (C-1 .. C+7) | Residue at +6 | Nearest cation | Distance SG to CZ/NZ (A) | Cations within 8 A |
|---|---|---|---|---|---|---|---|
| **ScOca6** | AF-Q12454-F1 | C114 | HCTNGELII | **I120** | Arg18 (not P-loop) | **7.54** | 1 |
| ScOca1 | AF-P50946-F1 | C168 | CCGMGRHRT | R174 | Arg174 | 4.89 | 2 |
| ScSiw14 | AF-P53965-F1 | C214 | HCNRGKHRT | R220 | Arg220 | 5.05 | 1 |
| SpSiw14 | AF-Q9UUF3-F1 | C189 | HCSRGKHRT | R195 | Arg195 | 5.17 | 1 |
| AtDSP1 | AF-Q9ZVN4-F1 | C150 | HCKRGKHRT | R156 | Arg156 | 4.88 | 1 |
| HsDUSP3 | AF-P51452-F1 | C124 | HCREGYSRS | R130 | Arg130 | 4.70 | 1 |
| ScSiw14 | **PDB 6BYF chain A (experimental, 2.35 A)** | C214 | HCNRGKHRT | R220 | Arg220 | **5.70** | - |

Oca6 model confidence: mean pLDDT 80.2 (whole chain), 88.9 (catalytic domain 3-179),
91-98 across the P-loop residues 112-124. The loop conformation is therefore not a
low-confidence artifact.

## Table 6. Current GO annotation set for UniProtKB:Q12454 (QuickGO)

| GO ID | Name | Aspect | Evidence | Reference | With/From | Assigned by |
|---|---|---|---|---|---|---|
| GO:0003674 | molecular_function | MF | ND | GO_REF:0000015 | - | SGD |
| GO:0004725 | protein tyrosine phosphatase activity | MF | IEA | GO_REF:0000120 | 10684; EC 3.1.3.48 | UniProt |
| GO:0016791 | phosphatase activity | MF | **IBA** | GO_REF:0000033 | AT1G05000, AT2G32960, AT3G02800, AT5G16480, PTN001258896, S000005043 (SIW14), I6WXK4, Q4QBX1, Q6K461, Q9HXC7 | GO_Central |
| GO:0008150 | biological_process | BP | ND | GO_REF:0000015 | - | SGD |
| GO:0005737 | cytoplasm | CC | IEA | GO_REF:0000044 | SL-0086 | UniProt |
| GO:0005737 | cytoplasm | CC | HDA | PMID:14562095 | - | SGD |

Both phosphatase-activity annotations are inferred (IBA from the PANTHER family tree,
IEA from a UniProt family rule). SGD records ND for molecular function.

## Table 7. Sequence-independent structural superposition, Oca6 onto Siw14

Method: TM-align-style superposition implemented in this job. Kabsch superposition with
iterative dynamic-programming refinement on s_ij = 1/(1+(d_ij/d0)^2),
d0 = 1.24*(L-15)^(1/3) - 1.8, seeded by gapless threading. The DP is vectorized with a
prefix-max scan over a constant gap penalty. Runtime 5.69 s.

Mobile: AF-Q12454-F1 (Oca6, AlphaFold v6). Target: PDB 6BYF chain A (Siw14 catalytic
core, experimental, 2.35 A).

| Metric | Value |
|---|---|
| TM-score (normalised by Siw14, n = 162) | 0.477 |
| Aligned pairs | 120 |
| Core pairs (CA-CA < 5 A) | 88 |
| Core RMSD | 2.80 A |
| Sequence identity across the structural alignment | 15.0% |

Structural equivalents of the Siw14 P-loop, driven by geometry alone:

| Siw14 (6BYF) | Oca6 (AF-Q12454-F1) | CA deviation | Note |
|---|---|---|---|
| His213 | His113 | 1.28 A | |
| **Cys214** | **Cys114** | **1.67 A** | catalytic cysteine, retained |
| Gly217 | Gly117 | 1.38 A | |
| Lys218 | Glu118 | 1.60 A | charge reversal |
| His219 | Leu119 | 1.62 A | |
| **Arg220** | **Ile120** | **1.82 A** | invariant arginine, lost |

This reproduces the independent Needleman-Wunsch mapping in Table 1 exactly, at 15%
sequence identity, so the arginine loss is a property of the fold and not an alignment
artifact.

Two routes to this comparison could not be used and are reported as failures rather
than worked around silently:

- The RCSB pairwise structure alignment service (alignment.rcsb.org) returned HTTP 400
  ("Required parameter 'query' is not present") and then HTTP 415 ("Unsupported Media
  Type"). No result was obtained from it.
- `phenix.superpose_pdbs` returned a final RMSD of 9.955 A over 121 atoms with 60
  matched residues. It drives the superposition from a sequence alignment, and at 15%
  identity that alignment is not informative. Its output was discarded.

## Table 8. Pocket electrostatics around the catalytic cysteine

Charged side chains with CB within 12 A of the catalytic-cysteine CB. The CB proxy is
crude and ignores side-chain rotamers, so this is a weak supporting observation.

| Protein | Source | Arg/Lys | Asp/Glu | Net |
|---|---|---|---|---|
| ScOca6 | AF-Q12454-F1 | 2 | 2 | **0** |
| ScSiw14 | AF-P53965-F1 | 4 | 3 | +1 |
| ScSiw14 | PDB 6BYF (experimental) | 6 | 3 | +3 |
| ScOca1 | AF-P50946-F1 | 4 | 3 | +1 |
| ScOca2 | AF-P53949-F1 | 6 | 3 | +3 |
| AtDSP1 | AF-Q9ZVN4-F1 | 7 | 3 | +4 |

Oca6 is the only protein in the panel with a neutral pocket. Inositol pyrophosphate
substrates such as 5-InsP7 carry a large negative charge, so a neutral pocket is
consistent with loss of substrate binding, but the margin against ScSiw14 (AlphaFold)
is one unit and the method cannot carry the claim on its own.

## Table 9. Physical interaction partners of Q12454

IntAct `findInteractions` for Q12454: 34 records.

| Partner | Max MI score | Detection methods | Source publications |
|---|---|---|---|
| **OCA4 / YCR095C** | **0.70** | validated two hybrid, mappit, two hybrid array, two hybrid prey pooling, anti-tag coIP | multiple |
| OCA5 | - | tandem affinity purification | PMID:16429126 |
| OCA1, OCA2, SIW14 | - | anti-tag coimmunoprecipitation | PMID:37968396 |
| TEM1, GSP2, MUK1, GCD7, SRP1 | - | two hybrid | PMID:41935050 |
| SSB1 | - | affinity chromatography | PMID:19536198 |
| UBC7 | - | two hybrid | PMID:14690591 |
| CRM1 | - | affinity capture | PMID:26673895 |

STRING at combined score >= 400 gives OCA1, OCA2, OCA4, OCA5 and SIW14 near 0.99 with
experimental subscores near 0.99, plus RTR2, ENV9, YPT1, DOS2 and VIP1.
