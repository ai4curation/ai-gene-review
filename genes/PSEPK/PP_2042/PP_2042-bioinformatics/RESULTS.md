# PP_2042 / PP_2043 (DUF1302 / DUF1329 pair) bioinformatics results

Scripts: `analyze_pair.py` (identities, N-terminal motifs, Fitness Browser data from BERDL
`kescience.fitnessbrowser`), `pair_cofit.py` (fitness-profile correlations),
`neighbourhood.py` (KT2440 gene neighbourhoods). Outputs: `results.json`,
`fitness_putida_pairs.tsv`, `pair_cofit.json`, `neighbourhood.json`.

BERIL runs (projects/hackathon/runs/): `20261030T211615Z-pp2042-pp2043-pair-analysis`,
`20261030T211659Z-pp2042-pp2043-pair-cofit`, `20261030T211829Z-pp2042-neighbourhood`.

## 1. Mapping of the dashboard sequences

- NC_017530.1_3648 vs PP_2042 (Q88L93): 98.9% identity over 617 aligned pairs (1-617 / 1-617).
- NZ_PJCG01000017.1_25 vs PP_2043 (Q88L92): 98.0% identity over 440 aligned pairs (query 1-440 / subject 3-442).

## 2. Orthology: which KT2440 pair corresponds to P. aeruginosa PA3923/PA3922?

Smith-Waterman, BLOSUM62, gap open 11 / extend 1; identity over aligned pairs.

| DUF1302 pair | % identity | aligned pairs |
|---|---|---|
| PP_0765 vs PA3923 | 76.9 | 624 |
| PP_0765 vs PA3422 | 62.8 | 573 |
| PP_2042 vs PA3923 | 52.2 | 590 |
| PP_2042 vs PA3422 | 51.9 | 555 |
| PP_2042 vs PP_0765 | 53.1 | 584 |

| DUF1329 pair | % identity | aligned pairs |
|---|---|---|
| PP_0766 vs PA3922 | 78.0 | 454 |
| PP_0766 vs PA3421 | 69.7 | 452 |
| PP_2043 vs PA3922 | 52.9 | 420 |
| PP_2043 vs PA3421 | 49.9 | 431 |
| PP_2043 vs PP_0766 | 48.9 | 419 |

The laminin-binding PA3923 is the reciprocal best hit of PP_0765, not of PP_2042, and PA3922 is the reciprocal best hit of PP_0766, not of PP_2043.
PP_2042 and PP_2043 are equidistant (about 50-53%) from both P. aeruginosa pairs and from their KT2440 paralogs, so they form a separate subfamily with no characterized member.

## 3. N-terminal features

- PP_2042: SignalP signal peptide 1-27 (UniProt). No lipobox ([LVI][ASTVI][GAS]C) in residues 1-40 of the KT2440 sequence, which has Gly at position 26 where the dashboard sequence has Cys. The dashboard sequence context at 23-26 is A-S-A-C, which does not fit the lipobox consensus; the PS51257 lipoprotein profile hit shown on the dashboard page has E = 5.0 and is not significant.
- PP_2042: DeepTMHMM on the dashboard sequence predicts an 18-strand outer-membrane beta-barrel with signal peptide 1-27; the protein ends in a C-terminal aromatic residue (...SLGVTF).
- PP_2043: SignalP signal peptide 1-20 (UniProt), no lipobox, no transmembrane segment; DeepTMHMM on the dashboard sequence predicts signal peptide 1-18 and "outside" 19-440 (class SP, secreted/periplasmic).
- PP_0766, PA3922 and PA3421 (DUF1329) likewise have signal peptides and no lipobox.

## 4. Fitness Browser (KT2440, orgId Putida; 300 experiments per gene)

| gene | min fit | max fit | experiments with abs(fit) >= 1 and abs(t) >= 4 | specific phenotypes |
|---|---|---|---|---|
| PP_2042 | -0.42 | 0.46 | 0 | none |
| PP_2043 | -0.31 | 0.30 | 0 | none |
| PP_0765 | -4.06 | 0.68 | 5 | Tween 20 (C) x2, butyl stearate (C) x2, alpha-ketoglutarate (C) |
| PP_0766 | -3.65 | 0.58 | 5 | Tween 20 (C) x2, butyl stearate (C) x2, alpha-ketoglutarate (C) |

PP_2042 and PP_2043 have no fitness phenotype in any of 300 KT2440 experiments, including the Tween 20 and butyl stearate experiments in which PP_0765 and PP_0766 are strongly required.

The KT2440 Tween 20 fitness value (-4.064) shown to the dashboard annotator for the 48.4%-identity homolog belongs to PP_0765, and the -3.649 value shown for the 48.2% homolog belongs to PP_0766.

Pearson correlation of fitness profiles across the 300 experiments: PP_0765 vs PP_0766 r = 0.951; PP_2042 vs PP_2043 r = 0.098; PP_2042 vs PP_0765 r = -0.108; PP_2043 vs PP_0766 r = -0.080.

Top cofitness hits of PP_2042 and PP_2043 are all below 0.31 and are unrelated genes (for example PP_5433, PP_1231). PP_0765 and PP_0766 are each other's top hit (0.951), followed by PP_2019 (RND efflux transporter, 0.93-0.94) and PP_2018 (BNR domain protein, 0.86-0.87).

Fitness Browser reannotations exist only for PP_0765 ("putative adhesin (DUF1302)") and PP_0766 ("adhesin-associated sorting protein (DUF1329)"); there is none for PP_2042 or PP_2043.

## 5. KT2440 gene neighbourhoods

- PP_2041 (LysR regulator, minus strand) | PP_2042 (+, 2321455-2323308) | PP_2043 (+, 2323313-2324641) | PP_2044 (+, 2324641-2325027, DUF202 inner membrane protein). PP_2042-PP_2043 are separated by 4 bp and PP_2043 ends where PP_2044 starts, consistent with one operon. No RND/MMPL exporter or BNR protein is encoded at this locus. Upstream genes PP_2038-PP_2040 encode a long-chain-fatty-acid-CoA ligase, an acyl-CoA dehydrogenase and an MFS transporter.
- PP_0765/PP_0766 are adjacent to the LuxR regulator PP_0767; their RND/BNR partners PP_2018/PP_2019 are encoded elsewhere.
- PP_2810-PP_2813 is a complete cassette of two exported unknown proteins, a putative transporter and a BNR protein (an AmeABCD-like arrangement); none of PP_2810-PP_2813 has a phenotype (all abs(fit) < 1).
