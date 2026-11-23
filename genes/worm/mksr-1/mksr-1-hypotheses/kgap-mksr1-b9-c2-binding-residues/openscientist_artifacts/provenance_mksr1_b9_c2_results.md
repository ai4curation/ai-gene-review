# MKSR-1 (Q21191) B9/C2 domain: computed results, iteration 1

All numbers below were produced by code run in this job (see `mksr1_b9_c2_analysis.py`).
Inputs: UniProt REST, AlphaFold DB API (model_v6), RCSB PDB, InterPro API, Foldseek web API.

## 1. Fold assignment (Foldseek 3Di+AA, AF-Q21191-F1-model_v6 vs PDB100, 171 hits)

| rank | target | description | E-value | seq id |
|---|---|---|---|---|
| 1 | 2nq3_A | C2 domain of human ITCH E3 ubiquitin ligase | 1.0e-4 | 9.7% |
| 2 | 2nsq_A | C2 domain of human NEDD4-like E3 ligase | 2.1e-4 | - |
| 3 | 1djh_B | PLC-delta1 (C2 domain), Ba2+ complex | 2.8e-4 | - |
| 4 | 6nyc_A | Munc13-1 C2B, calcium free | 4.4e-4 | - |
| 5 | 7as6_A | plant Extended Synaptotagmin 1 C2A | 4.9e-4 | - |
| ... | 3gpe_A | PKC-alpha C2 + Ca2+ + PtdIns(4,5)P2 | 8.8e-3 | 16.9% |
| ... | 3f05_A | Synaptotagmin-1 C2A + Mn2+ | 1.2e-2 | 12.1% |

Every top hit is a C2 domain. InterPro gives IPR010796 "B9-type C2 domain" (7-203) and
PROSITE PS51381; no CATH 2.60.40.150 / SCOP SSF49562 assignment exists for B9 proteins.

## 2. Calcium-site geometry: tightest 5-carboxylate cluster radius

| structure | class | cluster radius (A) | residues found |
|---|---|---|---|
| Syt1 C2A 1BYN (Ca-bound) | Ca2+-dependent C2 | 5.26 | D172, D178, D230, D232, D238 |
| Syt1 C2A 1RSY (apo) | Ca2+-dependent C2 | 6.18 | D172, D178, D230, D232, D238 |
| PKC-alpha C2 1DSY (Ca-bound) | Ca2+-dependent C2 | 5.17 | D187, D193, D246, D248, D254 |
| PTEN C2 1D5R | Ca2+-independent C2 | 11.88 | E256, D268, D324, D326, D331 |
| MKSR-1 B9 (AF Q21191, 7-203) | B9 | 9.36 | E19, D57, D63, D164, E166 |
| B9D1 human (AF Q9UPM9) | B9 | 10.58 | E24, D26, D27, D93, D98 |
| MKSR-2 B9 (AF Q9N423) | B9 | 11.95 | D18, D84, E90, E121, E122 |
| B9D2 human (AF Q9BPU9) | B9 | 16.09 | E3, D62, E160, D169, E174 |
| MKS1 human B9 (AF Q9NXB0, 311-493) | B9 | 10.21 | E326, D328, D405, E413, E481 |

The search is unsupervised: it rediscovered the published calcium ligands in both positive
controls. AlphaFold models were filtered to pLDDT >= 70.

## 3. Ground-truth calcium coordination (<= 3.3 A) used for calibration

- 1BYN (Syt1 C2A, NMR, model 1): Ca272 - D172, D178, D230, F231(O), D232;
  Ca273 - L171(O), D172, D230, D232, D238; Ca274 - S235(OG), K236(O), D232, D238.
- 1DSY (PKC-alpha C2): Ca501 - M186(O), D187, D246, D248, D254;
  Ca502 - W247(O), D187, D193, D246, D248.

## 4. Structural equivalence at the calcium-ligand positions

Core superposition after iterative outlier trimming:
MKSR-1 vs 3gpe, 1.64 A over 51 Calpha; MKSR-1 vs 3f05, 1.57 A over 56 Calpha.

| canonical ligand | MKSR-1 equivalent | pLDDT |
|---|---|---|
| PKC-alpha D187 | Glu23 | 92 |
| Syt1 D178 / PKC-alpha D193 | Asn25 | 94 |
| Syt1 D230 / PKC-alpha D246 | Ser87 | 94 |
| Syt1 D232 / PKC-alpha D248 | Asp89 | 87 |
| Syt1 D238 / PKC-alpha D254 | Cys95 | 88 |
| Syt1 D172 | gap (no aligned residue) | - |

Mapping the metal positions into the MKSR-1 frame: PKC-alpha Ca501/502/503 and Syt1 Mn267
all land in a pocket lined by Ser87, Lys88, Asp89, Lys93, Asp94, Cys95, Asn25, Glu23,
with at most two carboxylates within 8 A (five are required for a C2 site).

## 5. Cross-species conservation of the five positions (pairwise NW, BLOSUM62)

| protein | % id to MKSR-1 | D187-eq | D193-eq | D246-eq | D248-eq | D254-eq |
|---|---|---|---|---|---|---|
| MKSR-1 (C. elegans) | 100 | E | N | S | D | C |
| B9D1 human | 28.0 | Y | D | G | D | V |
| B9D1 mouse | 29.0 | Y | D | G | D | V |
| B9D1 zebrafish | 30.8 | Y | D | G | D | V |
| B9D1 X. tropicalis | 30.8 | F | D | G | D | V |
| B9D1 Drosophila | 25.7 | K | F | G | S | T |
| B9D1 Chlamydomonas | 26.7 | C | N | G | D | V |
| MKSR-2/B9D2 C. elegans | 22.9 | D | R | H | D | E |
| B9D2 human | 29.4 | S | L | S | D | Q |
| MKS1 human (B9 region) | 26.9 | Y | N | S | D | R |

Only the D232/D248-equivalent position is acidic in most orthologs. Three of five positions
are never acidic in any B9 protein examined.

## 6. Lipid-binding surface at the PKC-alpha PtdIns(4,5)P2 site (3GPE, ligand PT5)

| protein | Lys+Arg within 10 A | Asp+Glu within 10 A | net |
|---|---|---|---|
| PKC-alpha C2 (actual site) | 5 | 3 | +2 |
| MKSR-1 (structurally equivalent position) | 1 (Lys29) | 2 (Asp94, Glu139) | -1 |

Around the calcium cluster (12 A): PKC-alpha 3 K/R vs 5 D/E (net -2); MKSR-1 2 K/R vs 5 D/E
(Glu22, Glu23, Lys88, Asp89, Lys93, Asp94, Glu139; net -3).


## 7. Conservation of the calcium-loop-equivalent apex (iteration 2)

Per-residue identity to MKSR-1 from six pairwise NW alignments (BLOSUM62, go -11, ge -1)
against B9D1 orthologs: human Q9UPM9, mouse Q9R1S0, zebrafish Q503B7, X. tropicalis Q5BJ61,
Drosophila Q9VF59, Chlamydomonas A8J3B5.

| region (B9 domain 7-203) | n residues | mean identity |
|---|---|---|
| CBR-equivalent apex (<= 12 A from mapped Ca site) | 30 | 0.233 |
| rest of the domain | 167 | 0.266 |
| whole domain | 197 | 0.261 |

Mann-Whitney U = 2314, p = 0.47, rank-biserial r = -0.08. No elevated constraint at the apex.
Identical in 6/6: Gly92, Gly98, Glu139. Identical in >= 5/6: Glu22, Asp89, Gly92, Asp94, Gly98, Glu139.

Apex residue set (from the 1.64 A MKSR-1/3gpe core fit, 12 A sphere, 30 residues):
Glu22, Glu23, Ser24, Asn25, Val26, Cys27, Phe51, Phe53, Cys85, Phe86, Ser87, Lys88, Asp89,
His90, Ser91, Gly92, Lys93, Asp94, Cys95, Val96, Thr97, Gly98, Leu119, Ala131, Arg134,
Arg135, Val136, Asn137, Ala138, Glu139.

## 8. Annotation and structure availability (iteration 2)

QuickGO for Q21191: GO:0005515 protein binding (IPI; PMIDs 14704431, 18337471, 19123269),
GO:0035869 ciliary transition zone (IDA, PMID 21422230), GO:0036038 MKS complex (IBA).
No GO:0005509, GO:0046872, GO:0008289 or GO:0005544. Same for Q9UPM9 and Q9N423.

RCSB search by UniProt accession returns zero entries for Q21191, Q9UPM9, Q9BPU9, Q9NXB0
and Q9N423. No experimental structure exists for any B9-family protein.

## 9. Position of the one functionally mapped B9 residue (iteration 2)

AF-Q9BPU9 (human B9D2) vs 3gpe_A: core fit 1.67 A over 44 of 86 Calpha.
Mapped Ca site in the B9D2 frame is lined by Ser82, Asp84 (3.4 A), Gly87, Arg88, Cys89, Gln90.
B9D2 residue 101 is Ser; its Calpha is 35.5 A from the mapped Ca site.
Burial: 14 Calpha within 10 A vs domain median 16 (37th percentile, exposed).
B9D2 p.Ser101Arg abrogates the B9D2-MKS1 interaction (PMID 21763481).


## 10. Unbiased basic-patch scan over the whole domain (iteration 3)

For every residue centre (CB, or CA for Gly), count Lys/Arg and Asp/Glu side-chain tips
(NZ, CZ, CG, CD) within 12 A. AlphaFold models filtered to pLDDT >= 70.

| structure | strongest patch centre | Lys+Arg | Asp+Glu | net | domain mean net per patch | n centres |
|---|---|---|---|---|---|---|
| Syt1 C2A 3f05_A | Lys190 | 6 | 1 | +5 | -1.27 | 134 |
| PKC-alpha C2 3gpe_A | Ser208 | 7 | 3 | +4 | -0.42 | 137 |
| PTEN C2 1d5r_A (186-351) | Val216 | 5 | 1 | +4 | +0.90 | 135 |
| B9D1 human AF Q9UPM9 | Gly113 | 3 | 0 | +3 | -0.25 | 146 |
| MKSR-1 AF Q21191 (7-203) | Val8 | 2 | 0 | +2 | -0.57 | 144 |

MKSR-1 patch members: Lys71 and Lys172 only. PTEN C2, the standard calcium-independent
membrane-binding C2, is the only domain here with a positive mean surface charge.

## 11. The Lys71/Lys172 pair (iteration 3)

Invariant in all six B9D1 orthologs. Lys or Arg at both equivalent positions in 15 of 18
tests across nine B9 proteins (MKSR-2 has Arg at the 71-equivalent, B9D2 has Gln; MKS1 has
a gap at the 172-equivalent).

Geometry in AF-Q21191: NZ-NZ 10.2 A; pLDDT 95 (Lys71) and 90 (Lys172); Lys71 has 21 Calpha
within 10 A vs domain median 16 (partly buried), Lys172 has 15. Calpha distance to the
calcium-loop-equivalent apex centroid: 35.2 A and 39.9 A. Charged tips within 12 A of the
NZ-NZ midpoint: Lys71 (5.1), Lys172 (5.1), Lys3 (7.5), Asp175 (11.1), Asp5 (11.2).

Conservation baseline: 19 of 197 domain positions (9.6%) are identical in all six orthologs
(Gly13, Pro21, Val33, Asp37, Trp38, Gly43, Pro65, Lys71, Trp78, Pro79, Gly92, Gly98, Tyr99,
Pro105, Pro120, Glu139, Asp142, Pro143, Lys172). Lys/Arg are not enriched among invariant
positions: 2/19 vs 17/178, Fisher odds ratio 1.11, p = 1.00.
