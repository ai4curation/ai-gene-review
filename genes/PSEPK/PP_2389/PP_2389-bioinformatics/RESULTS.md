# PP_2389 (Q88KA1) bioinformatics results

Two analyses, each run through `beril run` in the BERIL hackathon project
(`/home/cmungall/.beril/projects/hackathon/runs/`). Outputs are copied here unchanged.

## 1. Fitness Browser data for PP_2389 and its neighbours (`fb_fitness.py`, `fitness/`)

Run `20261030T211248Z-pp2389-fitness`. The Fitness Browser web site returned HTTP 403, so the
KT2440 (orgId Putida) RB-TnSeq data were read from the BERDL lakehouse copy
(`kescience.fitnessbrowser`: tables gene, genefitness, experiment, cofit, specificphenotype).

- PP_2389 was measured in 300 experiments. Only 10 experiments pass |fit| >= 1 and |t| >= 4, and all 10 are positive (mutants grow better). Its most negative score is -1.03.
- The strongest positive scores are on DL-2-aminobutyrate as nitrogen source (fit 4.01, t 23.8; fit 3.88, t 19.0), then L-methionine (N) (fit 2.06 and 1.94), L-phenylalanine (N) (1.41, 1.40), L-leucine (N) (1.39), levulinic acid (C) (1.05), 4-hydroxyvalerate (C) (1.03) and 6-aminocaproate (N) (1.02).
- PP_2389 has no entry in the specificphenotype table.
- The DL-2-aminobutyrate effect is not unique to PP_2389. In experiment set27IT028, 113 of 4778 genes have fit >= 1 and t >= 4; PP_2389 ranks 4th. The list includes many NADH:quinone oxidoreductase (complex I, nuo) subunits.
- The positive phenotypes are shared with the neighbouring genes. The divergent LysR-family regulator PP_2390 scores 4.14 and 4.03 on DL-2-aminobutyrate, and the LysE-family transporter PP_2388 scores 3.80 and 3.50. PP_2387 (unknown function) scores 3.87 and 3.12.
- PP_2389's top cofitness partners are PP_2390 (cofit 0.77) and PP_2388 (cofit 0.69). PP_2388's top partner is PP_2390 (cofit 0.93).
- PP_2388 and PP_2390 also have strong negative phenotypes on aromatic carbon sources (protocatechuate, p-coumarate, ferulate) and in bioreactor runs; PP_2389 has none. Insertions in PP_2389 are therefore not simply polar on PP_2388.
- Gene order (minus strand): PP_2389 (2727324-2728112) is 3 bp upstream of PP_2388 (2726695-2727321); PP_2390 (plus strand, 2728273-2729193) is divergent.

Interpretation: the phenotype is real and reproducible, with both replicates on two nitrogen
sources. It is a gain of fitness on loss, shared with the LysR regulator and the LysE exporter of
the same locus. That points to a costly, co-regulated module, not to a role for PP_2389 in using
these nitrogen sources. The data do not identify a molecular activity.

## 2. Alignment to characterized YqcI/YcgG (PF08892) members (`family_align.py`, `family_align/`)

Run `20261030T211546Z-pp2389-family-align`. Local Smith-Waterman alignments (BLOSUM62, gap -11/-1)
of Q88KA1 against AglA (PDB 9UB3 sequence), DcsA (D2Z024), GntA (A0ABX8WWF6) and *B. subtilis*
YqcI (P45944) and YcgG (P94382).

- The dashboard query is 99.6% identical to Q88KA1 (261/262).
- Identity of Q88KA1 to the characterized members: DcsA 38.4% over 224 aligned positions; AglA 33.6% over 214; GntA 27.6% over only 87 (a weak local hit). To the uncharacterized *B. subtilis* proteins: YqcI 31.2% over 218; YcgG 35.7% over 196.
- The AglA functional residues (PMID:41221789) map onto PP_2389 as follows: heme thiolate ligand Cys44 to Cys46 (in the FPC motif at 44-46); heme-propionate salt bridges Arg166, Lys196 and Arg200 to Arg167, Arg198 and Arg202; and the substrate-gate residues Phe152, Arg179 and Phe182 to Phe153, Arg180 and Phe183.
- The C-terminal CPF motif is at residue 244.

Interpretation: PP_2389 keeps the heme-ligand cysteine and the heme- and substrate-binding
residues of the structurally characterized heme-dependent guanidine N-hydroxylase AglA. It is
therefore predicted to be a heme-thiolate N-hydroxylase of the YqcI/YcgG family. Its substrate is
unknown. These are pairwise alignments, not a structure superposition.
