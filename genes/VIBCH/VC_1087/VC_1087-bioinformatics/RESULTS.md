# VC_1087 bioinformatics: is the dashboard protein the VC1087 (HnoD) ortholog, and is its HD-GYP domain degenerate?

Run: `beril run` id `20261030T213524Z-vc1087-ortholog-hdgyp` (hackathon project); script `analyze.py`,
outputs `results.json` and `alignment_vs_VC_1087.txt` (copied here).

Inputs: dashboard protein `NZ_QKKU01000066.1_29` (447 aa, `data/NZ_QKKU01000066.1_29.fasta`) and the
V. cholerae N16961 reference proteome (UP000000584) used by the batch mapping run.

## 1. Ortholog assignment

Smith-Waterman (BLOSUM62, gap open -11, extend -1) of the dashboard protein against every N16961 protein:

| N16961 hit | local score | % identity (aligned) | query coverage |
|---|---|---|---|
| VC_1087 (Q9KT18) | 2093 | 91.3 | 100% |
| VC_1086 (HnoB, EAL RR) | 193 | 38.4 | 25% (REC only) |
| VC_1348 (REC-HD-GYP PDE) | 164 | 25.3 | 75% |
| VC_A0210 (REC-HD-GYP, CGAP2) | 143 | 25.9 | 48% |
| VC_1295 (HD-GYP PDE) | 140 | 27.3 | 51% |

The dashboard protein is the VC_1087 ortholog, not a paralog: the top hit scores 1900 points above the next one,
it aligns over its full length with no gaps (447/447 residues), and the other N16961 REC/HD-GYP proteins
(VC_1348, VC_A0210) are only about 25% identical.

The 39 differences from VC_1087 are concentrated in the N-terminal receiver (REC) domain (17 in residues 1-126)
and the coiled-coil linker (residues 127-194). Only 4 fall in the HD-GYP domain (195-391). The phosphoacceptor
Asp60 is conserved. A 91% identity is low for two V. cholerae strains, so the source genome (QKKU01) is probably a
divergent non-O1 or environmental lineage. The PaperBLAST figure on the dashboard page (88.6%) was computed by a
different method and does not change the assignment.

## 2. HD-GYP motif status

Pairwise global alignments to the N16961 HD-GYP phosphodiesterases (VC_1348, VC_A0210, VC_A0681, VC_1295,
VC_A0931) place the canonical motifs as follows:

| motif | dashboard protein (= VC_1087) | active N16961 HD-GYP PDEs |
|---|---|---|
| HD dyad (metal ligands) | `GLMHQIG` (res. 249-255): **H-Q**, Asp replaced by Gln | `PLHDIG`/`PLHDVG`/`LVHDIG` |
| GYP motif | `YDGTGKPD` (res. 310-317): **GKP**, Tyr replaced by Lys | `WDGSGYP`/`LDGSGYP`/`WDGTGYP`/`LDGTGYP` |

The HD-GYP domain is degenerate. The Asp of the HD dyad, which coordinates the catalytic metals, and the Tyr of
the GYP motif are both lost. The motif residues are identical in the dashboard protein and in VC_1087, so the
dashboard protein lacks the HD dyad just as VC_1087 does. McKee et al. 2014 (PMID:25343965) showed directly that
VC_1087 has no c-di-GMP hydrolytic activity.
