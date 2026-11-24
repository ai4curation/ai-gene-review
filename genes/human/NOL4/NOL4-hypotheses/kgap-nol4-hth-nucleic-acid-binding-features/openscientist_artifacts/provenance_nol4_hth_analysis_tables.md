# NOL4 HTH_NOL4 region: computed provenance tables (iteration 1)

All values below were computed in this run. Sources: UniProt REST (O94818, Q96MY1),
InterPro API, AlphaFold DB (AF-O94818-F1-model_v6, released 2025-08-01),
Foldseek web API (3Di-AA mode), RCSB PDB files, QuickGO annotation API,
NCBI efetch (BAA34576.1).

## Table 1. InterPro / Pfam domain architecture of NOL4 (O94818, 638 aa)

| Source | Accession | Name | Short name | Residues | Score |
|---|---|---|---|---|---|
| Pfam | PF47726 | NOL4 nucleolar protein 4 N-terminal domain | - | 4-129 | 6.5e-40 |
| InterPro | IPR056549 | **Nucleolar protein 4, helical domain** | HTH_NOL4 | 406-500 | - |
| Pfam | PF23079 | Nucleolar protein 4, helical | HTH_NOL4_2nd | 406-500 | 1e-60 |
| Pfam | PF38089 | NOL4 C-terminal helical region | - | 602-638 | 1.1e-18 |
| InterPro | IPR039788 | Nucleolar protein 4 family | NOL4/NOL4L | 6-590 | - |
| PANTHER | PTHR12449 | DEATH DOMAIN-CONTAINING PROTEIN | - | 6-590 | 3.9e-77 |

IPR056549 description, verbatim from the InterPro API:
> "This domain is found in human Nucleolar protein 4 (NOL4), Nucleolar protein 4-like (NOL4L)
> and similar animal sequences. This domain is predicted to form an alpha-helical bundle."

IPR056549 has **no associated GO terms**. The string "HTH" appears only in the short names.

## Table 2. AlphaFold confidence by region (AF-O94818-F1-model_v6)

| Region | Assignment | Mean pLDDT | frac >70 | frac >90 |
|---|---|---|---|---|
| 1-638 | whole protein | 63.4 | 0.42 | - |
| 4-129 | PF47726 | 79.0 | 0.70 | - |
| 406-500 | IPR056549 "HTH_NOL4" | 87.2 | 0.83 | 0.77 |
| 602-638 | PF38089 | 92.8 | - | - |

45% of residues have pLDDT < 50; 58% have pLDDT < 70. UniProt annotates disordered
regions at 210-312, 343-403, 503-535, 573-603.

## Table 3. Foldseek 3Di-AA search, query = NOL4 406-500 (95 aa)

| Database | n hits returned | Best non-family E-value | Interpretation |
|---|---|---|---|
| pdb100 | 17 | **2.96** (4x0g chain D, Bsg25A) | No hit below E=1. No HTH, no DNA-bound, no RNA-bound structure. |
| afdb-swissprot | 15 | 4.9 (bacterial GPAT, prob 0.098) | All 8 significant hits are NOL4/NOL4L orthologs (E 1e-10 to 1e-14, prob 1). |
| afdb50 | 1000 | - | All top hits are NOL4/NOL4L orthologs across vertebrates. |

Top 10 PDB100 hits (all non-significant): 4x0g_D Bsg25A (E=9.1), 5jy3_C (E=7.6),
2khv_A (E=4.7), 5z12_C FXR/RXR (E=5.3), 4rak_A (E=6.4), 1dkf_A (E=5.3), 5jg7_B (E=7.6),
6a5z_H (E=8.5), 4cbj_F ATP synthase c-ring (E=5.3), 4wri_A (E=3.0).

## Table 4. Calibrated HTH geometry test

Helices assigned by own Kabsch-Sander (DSSP) H-bond implementation on each structure.
An HTH-like pair requires: inter-helix turn 2-5 residues, first helix 6-12 aa,
second helix 6-14 aa, inter-helical angle 70-145 deg.

| Structure | Description | Class | HTH-like pairs | Closest unit (h1 / turn / h2) | Angle |
|---|---|---|---|---|---|
| 1R69_A | 434 repressor N-terminal HTH | DNA-binding HTH | 3 | 2-12 / LGLN / 17-24 | 97.9 |
| 1HDD_C | Engrailed homeodomain + DNA | DNA-binding HTH | 1 | 28-38 / GLNEA / 44-57 | 106.4 |
| 6CRO_A | Cro repressor | DNA-binding HTH | 1 | 16-23 / GVY / 27-36 | 101.1 |
| 1LMB_3 | Lambda repressor DBD + DNA | DNA-binding HTH | 1 | 33-40 / GMG / 44-51 | 91.9 |
| 256B_A | Cytochrome b562 4-helix bundle | no nucleic acid | 0 | none | - |
| 1BBH_A | Cytochrome c' 4-helix bundle | no nucleic acid | 0 | none | - |
| 1NKL_A | NK-lysin saposin fold | no nucleic acid | 0 | none | - |
| **NOL4 406-500** | IPR056549 "HTH_NOL4" | QUERY | **0** | 434-447 / FPEY / 452-470 | 123.1 |
| **NOL4 4-129** | PF47726 N-terminal domain | QUERY | **0** | none | - |

4/4 true HTH domains score at least one HTH-like pair; 0/3 non-nucleic-acid helical
bundles and 0/2 NOL4 domains score any.

NOL4 406-500 DSSP helices: 407-422 (16 aa, RLKAFNMFVRLFVDEN), 434-447 (14 aa, KEKIQAIIDSCRRQ),
452-470 (19 aa, QERARKRIRTYLKSCRRMK), 487-499 (13 aa, AVAESILASACES). No beta strands.

Two specific failures of the closest candidate unit:
1. Helix 452-470 is 19 residues. Every benchmark recognition helix is 6-14 residues.
2. The turn FPEY has no glycine. All 6 benchmark HTH turns contain one
   (GLNEA, LGLN, GTT, LGVS, GVY, GMG).

A naive single-pass CA-geometry assignment merges 434-470 into one 47-residue helix.
This is an artifact: the segment has an end-to-end CA distance of 19.7 A against 69 A for
an ideal straight 47-residue helix, a maximum radial deviation of 11.7 A from a single
axis, and local axis bends of 64, 69, 88 and 46 degrees. The region is a compact bundle.

## Table 5. Electrostatic positive-patch analysis

Own Shrake-Rupley SASA (72-point sphere, 1.4 A probe); exposed = relative SASA > 0.20;
patch = largest connected component of exposed Lys/Arg side-chain charge centres under
12 A linkage; patch net charge = patch size minus exposed Asp/Glu within 10 A.

| Structure | Class | n res | net charge | NCPR | largest patch | per 100 res | patch net |
|---|---|---|---|---|---|---|---|
| 1HDD_C | DNA-binding HTH | 57 | +9 | 0.158 | 11 | 19.3 | +9 |
| 1R69_A | DNA-binding HTH | 63 | +4 | 0.063 | 3 | 4.8 | +2 |
| 1CMA_A | DNA-binding HTH | 104 | -4 | -0.038 | 8 | 7.7 | +2 |
| 6CRO_A | DNA-binding HTH | 60 | +3 | 0.050 | 3 | 5.0 | +1 |
| 1LMB_3 | DNA-binding HTH | 87 | -2 | -0.023 | 5 | 5.7 | 0 |
| **NOL4 406-500** | QUERY | 95 | +8 | 0.084 | 17 | 17.9 | **+8** |
| **NOL4 4-129** | QUERY | 126 | +4 | 0.032 | 10 | 7.9 | +5 |
| 1NKL_A | no nucleic acid | 78 | +6 | 0.077 | 13 | 16.7 | **+7** |
| 1BBH_A | no nucleic acid | 131 | -4 | -0.031 | 9 | 6.9 | +3 |
| 256B_A | no nucleic acid | 106 | -3 | -0.028 | 8 | 7.5 | +2 |
| 1ROP_A | no nucleic acid | 56 | -4 | -0.071 | 3 | 5.4 | +1 |

Group means: DNA-binding HTH 8.5 patch per 100 res; non-nucleic-acid bundles 9.1.
**The metric does not discriminate the two classes.** NOL4 406-500 is matched by
NK-lysin, a saposin-fold helical bundle with no nucleic-acid-binding function.

## Table 6. Mapping Ueki 1998 (PMID 9813152) onto canonical O94818

NOLP = GenBank BAA34576.1, 524 aa, verified to be an exact contiguous C-terminal
fragment of canonical O94818 (638 aa). Offset = +114.

| Ueki region (NOLP numbering) | Reported property | Canonical O94818 | Sequence |
|---|---|---|---|
| 342-371 | sufficient for **nucleolar** localisation (COS-7, fluorescent fusion) | **456-485** | RKRIRTYLKSCRRMKRSGFEMSRPIPSHLT |
| 372-401 | sufficient for **nuclear** localisation | **486-515** | SAVAESILASACESESRNAAKRMRLERQQD |

The nucleolar targeting region 456-485 lies inside IPR056549 (406-500) and coincides
with the most basic 20-mer in the whole protein, 454-473 RARKRIRTYLKSCRRMKRSG (net +10,
peak NCPR 0.533 over window 15, against a whole-protein mean NCPR of -0.028).

Independent motif scanning flags 456-471 (RKRIRTYLKSCRRMKR) and 445-458 (RRQFPEYQERARKR)
as bipartite-NLS-like.

## Table 7. Conservation across vertebrate NOL4 and NOL4L

Alignment columns taken from the Foldseek AFDB50 search. 349 sequences at E < 1e-5
(244 NOL4, 105 NOL4L), 265 distinct taxa.

Mean per-position identity to human NOL4 over 406-500: **0.839**
(NOL4 orthologs 0.841, NOL4L orthologs 0.842). NOL4L is 87.2% identical over this
domain by structural alignment.

| Position | aa | identity (all, n=349) | identity (NOL4L) |
|---|---|---|---|
| 416 | R | 1.000 | 1.000 |
| 434 | K | 1.000 | 1.000 |
| 445 | R | **0.115** | **0.010** |
| 446 | R | 1.000 | 1.000 |
| 454 | R | 0.997 | 1.000 |
| 456 | R | 0.997 | 1.000 |
| 457 | K | 0.997 | 0.990 |
| 458 | R | 1.000 | 1.000 |
| 460 | R | 0.980 | 1.000 |
| 464 | K | 0.994 | 0.981 |
| 467 | R | 0.994 | 0.981 |
| 468 | R | 0.997 | 0.990 |
| 470 | K | 0.917 | 0.924 |
| 471 | R | **0.473** | **0.276** |

Basic patch 454-473 mean identity 0.886 vs 0.826 for the rest of the domain.
Mann-Whitney U = 833, **p = 0.45**: the patch is NOT more conserved than the
rest of the domain. R445 and R471 are poorly conserved, which is inconsistent
with a fixed set of DNA-phosphate contacts.

## Table 8. Current GO annotations (QuickGO)

### NOL4 (UniProtKB:O94818) - 4 annotations total

| GO ID | Term | Aspect | Evidence | Reference | Assigned by |
|---|---|---|---|---|---|
| GO:0005654 | nucleoplasm | CC | IDA (ECO:0000314) | GO_REF:0000052 | HPA |
| GO:0005730 | nucleolus | CC | IEA (ECO:0007322) | GO_REF:0000044 | UniProt |
| GO:0005730 | nucleolus | CC | TAS (ECO:0000304) | PMID:9813152 | PINC |
| **GO:0003723** | **RNA binding** | **MF** | **TAS (ECO:0000304)** | **PMID:9813152** | **PINC** |

No DNA-binding term. No BP term of any kind.

### NOL4L (UniProtKB:Q96MY1) - 5 annotations total

| GO ID | Term | Aspect | Evidence | Reference | Assigned by |
|---|---|---|---|---|---|
| GO:0005654 | nucleoplasm | CC | IDA | GO_REF:0000052 | HPA |
| GO:0005515 | protein binding | MF | IPI | PMID:25416956 | IntAct |
| GO:0005515 | protein binding | MF | IPI | PMID:35271311 | IntAct |

No nucleic-acid-binding term on the paralog either.

## Provenance of PMID 9813152 content

Verbatim from the abstract, the entire scope of the paper:
> "This study reports cDNA isolation and partial characterization of a novel human
> nucleolar protein isolated by 'nuclear transportation trap' described previously.
> The cDNA encodes a putative polypeptide of 524 amino acids with a short Escherichia
> coli DNA helicase homologous region, an acid-rich domain, three potential base-rich
> nuclear localization signals (NLSs), a serine-rich domain, and a deduced coiled-coil
> domain. The protein has no known prominent similarities with any other protein in the
> protein databases."

No RNA-binding, crosslinking, EMSA, filter-binding, SELEX or interactome-capture
experiment is described.
