# Provenance tables: GCM consensus scan of the S. purpuratus gcm, pks and gataE loci

Assemblies: Spur_5.0 (S. purpuratus), Lvar_3.0 (L. variegatus). Sequences retrieved by NCBI
E-utilities efetch from nuccore. Motif: ATGCGGRY (GCM consensus used by Ransick & Davidson,
PMID 22509525). PWM: JASPAR MA0767.2 (GCM2), log-odds against the S. purpuratus mononucleotide
background measured on 1,499,503 non-N genomic bases.

## Table 1. Regions scanned and exact ATGCGGRY counts

| region | NCBI accession | span scanned | length (bp) | GC | ATGCGGRY hits |
|---|---|---|---|---|---|
| gcm locus | NW_022145598.1 | TSS-17,600 to TSS+33,400 | 51,001 | 0.364 | 1 |
| gataE locus | NW_022145613.1 | 324,575-381,799 (strand 2), TSS-20,000 to TSS+37,225 | 57,225 | 0.365 | 1 |
| pks1 locus (LOC588806) | NW_022145610.1 | 2,698,754-2,733,214, TSS-10,000 to TSS+24,461 | 34,461 | 0.373 | 3 |
| pks1 -1.5 kb CRM (Calestani & Rogers) | within the above | TSS-1,500 to TSS | 1,500 | 0.371 | 1 |
| gataE proximal 20 kb | within the above | TSS-20,000 to TSS | 20,000 | 0.360 | 1 |
| genomic background | 3 scaffolds | 1,499,503 non-N bp | 1,499,503 | 0.363 | 39 |

Background rates: ATGCGGRY 1 per 38,449 bp (2.60e-05 per bp, obs/exp 0.43);
ATGCGGGY 1 per 115,346 bp; ATGCGGGT 1 per 299,901 bp.
Poisson expectation for the 57,225 bp gataE domain: 1.49 hits. Observed 1. P(X>=1) = 0.77.

## Table 2. Every ATGCGGRY match, with position, strand and PWM score

| locus | position rel. TSS | 8-mer | strand | MA0767.2 score (bits) | above p=1e-4 (10.48)? | above p=1e-5 (13.24)? |
|---|---|---|---|---|---|---|
| gcm | -4,220 (NCBI frame) = -4,062 (Ransick & Davidson frame) | ATGCGGGC | + | 14.63 | yes | yes |
| pks1 | -1,437 | ATGCGGGT | - | 15.20 | yes | yes |
| pks1 | +5,020 | ATGCGGGT | - | 15.20 | yes | yes |
| pks1 | +7,111 | ATGCGGAC | + | 4.52 | no | no |
| gataE | -12,448 | ATGCGGAT | - | 5.09 | no | no |

Thresholds are empirical quantiles of 3,000,000 background scores on both strands.
pks1 +7,111 lies inside a coding exon: frame-1 translation of that segment matches XP_793564.3.

## Table 2b. Full PWM hit density, three matrices, two calibrated thresholds

Not restricted to exact ATGCGGRY. Thresholds are empirical quantiles of 3.0 million background
scores on both strands. Expected counts are 2 x (L - w + 1) x alpha.

| matrix | TF | locus | bp | hits p=1e-4 | expected | obs/exp | hits p=1e-5 | expected | obs/exp | hits per 10 kb at p=1e-5 |
|---|---|---|---|---|---|---|---|---|---|---|
| MA0767.2 | GCM2 | gcm | 51,001 | 16 | 10.20 | 1.57 | 1 | 1.02 | 0.98 | 0.20 |
| MA0767.2 | GCM2 | pks1 | 34,461 | 7 | 6.89 | 1.02 | 2 | 0.69 | 2.90 | 0.58 |
| MA0767.2 | GCM2 | gataE | 57,225 | 13 | 11.44 | 1.14 | **0** | 1.14 | 0.00 | 0.00 |
| MA0646.2 | GCM1 | gcm | 51,001 | 10 | 10.20 | 0.98 | 1 | 1.02 | 0.98 | 0.20 |
| MA0646.2 | GCM1 | pks1 | 34,461 | 13 | 6.89 | 1.89 | 3 | 0.69 | 4.35 | 0.87 |
| MA0646.2 | GCM1 | gataE | 57,225 | 18 | 11.44 | 1.57 | 1 | 1.14 | 0.87 | 0.17 |
| MA1840.2 | gcm (Dm) | gcm | 51,001 | 19 | 10.20 | 1.86 | 2 | 1.02 | 1.96 | 0.39 |
| MA1840.2 | gcm (Dm) | pks1 | 34,461 | 11 | 6.89 | 1.60 | 3 | 0.69 | 4.35 | 0.87 |
| MA1840.2 | gcm (Dm) | gataE | 57,225 | 20 | 11.44 | 1.75 | **0** | 1.14 | 0.00 | 0.00 |

Thresholds: MA0767.2 10.48 / 13.24 bits; MA0646.2 9.79 / 13.20; MA1840.2 9.83 / 12.60.

At p = 1e-4 every locus, including both positive controls, sits at genomic background
(obs/exp 0.98 to 1.89). Discrimination appears only at p = 1e-5.

## Table 2c. Every hit above p = 1e-5, all three matrices

| matrix | locus | position rel. TSS | strand | word | bits |
|---|---|---|---|---|---|
| MA0646.2 | gcm | -4,220 | + | ATGCGGGCAT | 13.83 |
| MA0767.2 | gcm | -4,220 | + | ATGCGGGC | 14.63 |
| MA1840.2 | gcm | -4,220 | - | CCCGCAT | 14.38 |
| MA1840.2 | gcm | +93 | + | CCCGCAC | 12.60 |
| MA0646.2 | pks1 | -1,439 | - | ATGCGGGTAT | 15.19 |
| MA0767.2 | pks1 | -1,437 | - | ATGCGGGT | 15.20 |
| MA1840.2 | pks1 | -1,436 | + | CCCGCAT | 14.38 |
| MA0646.2 | pks1 | +5,018 | - | ATGCGGGTAG | 16.92 |
| MA0767.2 | pks1 | +5,020 | - | ATGCGGGT | 15.20 |
| MA1840.2 | pks1 | +5,021 | + | CCCGCAT | 14.38 |
| MA1840.2 | pks1 | +13,035 | - | CCCGCAT | 14.38 |
| MA0646.2 | pks1 | +14,224 | - | ATGCTGGTAG | 13.70 |
| MA0646.2 | gataE | +36,541 | - | ATACGGGTAG | 13.88 |

The single gataE entry is detected by one matrix only, carries adenine at position 3 of the
ATGCGG core (a base read by the conserved asparagine and histidine side chains), is not an
ATGCGGRY match, lies 684 bp from the window edge, and has zero occurrences in 238,569 bp of the
orthologous L. variegatus region. Its local context is
`GTGGGGCAATATTAATTTCATTTCGTAAATATACGGGTAGGAAACATTTCAAACGGGATAATAAATACAA`.

## Table 2d. Power of the scan: observed best score against the random-window maximum

P(random >= obs) is 1 - F(observed max)^(2N), with F the empirical background CDF of 3.0 million
scores and N the number of scorable positions in the locus.

| matrix | TF | locus | bp | observed best (bits) | median best of a random window of the same length | P(random >= obs) |
|---|---|---|---|---|---|---|
| MA0767.2 | GCM2 | gcm | 51,001 | 14.63 | 13.80 | 0.357 |
| MA0767.2 | GCM2 | pks1 | 34,461 | 15.20 | 13.24 | 0.109 |
| MA0767.2 | GCM2 | gataE | 57,225 | 12.13 | 13.80 | 0.852 |
| MA0646.2 | GCM1 | gcm | 51,001 | 13.83 | 13.83 | 0.510 |
| MA0646.2 | GCM1 | pks1 | 34,461 | 16.92 | 13.23 | 0.067 |
| MA0646.2 | GCM1 | gataE | 57,225 | 13.88 | 14.11 | 0.516 |
| MA1840.2 | gcm (Dm) | gcm | 51,001 | 14.38 | 14.38 | 0.614 |
| MA1840.2 | gcm (Dm) | pks1 | 34,461 | 14.38 | 12.60 | 0.474 |
| MA1840.2 | gcm (Dm) | gataE | 57,225 | 9.90 | 14.38 | 1.000 |

Count-level power at 57,225 bp, from the measured genomic rates:
ATGCGGRY expected 1.49, P(0 observed) = 0.226; ATGCGGGY expected 0.50, P(0 observed) = 0.609.
P(a random 57.2 kb window has at least one hit at p = 1e-5) = 0.682; at p = 1e-4 = 1.000.

The validated gcm site is not significant by the best-score statistic (p = 0.357 to 0.614), so this
statistic has too little power to refute direct binding at a locus of this size. The discriminating
observation is the identity of the matches, not their density.

## Table 3. GCM1 HT-SELEX base counts at the R position (JASPAR MA0646.2)

| base at position R of ATGCGGRY | count |
|---|---|
| G | 21,439 |
| C | 18 |
| T | 10 |
| A | 0 |

## Table 4. DNA-contacting residues of the mouse GCMa GCM domain (PDB 1ODH) and their S. purpuratus equivalents

18 residues within 4.0 A of DNA in 1ODH (Cohen et al. 2003, PMID 12682016). Q8MMJ4 / NP_999826.1
numbering in the sp_pos column.

| mouse res | PDB aa | Sp aa | Sp pos | identical | contact | moiety | min dist (A) |
|---|---|---|---|---|---|---|---|
| R54 | R | K | 90 | no | backbone | mainchain | 3.42 |
| H55 | H | H | 91 | yes | backbone | sidechain | 2.83 |
| R62 | R | R | 98 | yes | backbone | sidechain | 3.10 |
| N63 | N | N | 99 | yes | backbone, base | sidechain | 3.36 |
| N65 | N | N | 101 | yes | base | sidechain | 2.68 |
| H67 | H | H | 103 | yes | base | sidechain | 2.54 |
| S69 | S | K | 105 | no | backbone | sidechain | 2.38 |
| L72 | L | L | 108 | yes | backbone | sidechain | 3.55 |
| K73 | K | K | 109 | yes | backbone | sidechain | 2.80 |
| K74 | K | K | 110 | yes | backbone | sidechain | 2.95 |
| A99 | A | A | 135 | yes | backbone | sidechain | 3.39 |
| I100 | I | T | 136 | no | backbone, base | sidechain | 3.03 |
| C101 | C | S | 137 | no | backbone | sidechain | 2.64 |
| A104 | A | A | 140 | yes | backbone | sidechain | 3.82 |
| K107 | K | K | 143 | yes | backbone | sidechain | 3.35 |
| F131 | F | Y | 169 | no | backbone | sidechain | 3.25 |
| K160 | K | K | 199 | yes | backbone | sidechain | 2.81 |
| R167 | R | L | 206 | no | backbone | sidechain | 3.16 |

12 of 18 identical. 3 of the 4 base-reading residues identical (N99, N101, H103). I100 to T136
is the only base-contact substitution.

## Table 5. Site-centred Sp/Lv conservation test (the only test that passes its positive control)

For each 8-mer, every occurrence in the wide L. variegatus window was located, and shared 10-mers
between the 308 bp S. purpuratus flank and each L. variegatus flank were counted. Null: 400 random
windows in the same L. variegatus locus.

| site | 8-mer | Lv occurrences | best shared 10-mers | null median | null max | empirical p | verdict |
|---|---|---|---|---|---|---|---|
| gcm -4,062 (functional control) | ATGCGGGC | 3 | 12 | 0 | 12 | 0.0050 | conserved |
| pks -1,437 (functional control) | ATGCGGGT | 0 in 323,246 bp | n/a | 0 | 8 | n/a | not conserved |
| pks +5,020 | ATGCGGGT | 0 | n/a | 0 | 3 | n/a | not conserved |
| pks +7,111 (coding exon) | ATGCGGAC | 2 | 77 | 0 | 7 | 0.0025 | conserved (coding constraint) |
| gataE -12,448 (candidate) | ATGCGGAT | 3 | 3 | 0 | 6 | 0.0349 | not conserved |

Aligned positive control:
```
Sp  AAATTCTATTTCGGCGCCCAACAAAATGCGGGCATGTTGCGGGCGAAAAGTGCTTCTT
Lv  AATAGTTTCATTGGCGCCGAATAACATGCGGGCATGTCGTTCTTAAATTTCATACGGG
```
Shared block AACATGCGGGCATGT, 15 bp.

## Table 6. Locus-wide conservation statistics, both of which FAIL the positive control

| site | local 16-mer conservation (300 bp window) | percentile in locus | longest exact Sp/Lv match in 308 bp (bp) | null median (bp) | null 95th (bp) | empirical p |
|---|---|---|---|---|---|---|
| gcm -4,062 (functional control) | 0.000 | 0.0 | 15 | 17.0 | 25.2 | 0.884 |
| pks -1,437 (functional control) | 0.003 | 29.0 | 16 | 17.5 | 41.0 | 0.711 |
| pks +5,020 | 0.000 | 0.0 | 13 | 17.0 | 35.0 | 1.000 |
| pks +7,111 (coding exon) | 0.077 | 78.1 | 27 | 17.0 | 35.0 | 0.182 |
| gataE -12,448 (candidate) | 0.000 | 0.0 | 13 | 17.0 | 30.2 | 1.000 |

## Table 7. Sp/Lv conserved patches in the gataE domain (16-mer sharing >= 0.10 over 300 bp)

16 patches, 9,050 bp of 57,225 bp. None contains an ATGCGGRY. Three contain a bare ATGCGG core.
This table is reported for completeness only: the method fails its positive control (Table 6),
so it locates modules and not individual 8 bp sites.

| start rel. TSS | end rel. TSS | bp | max 16-mer fraction | ATGCGGRY | ATGCGG core |
|---|---|---|---|---|---|
| 12,300 | 12,925 | 625 | 0.280 | 0 | 0 |
| -2,825 | -2,225 | 600 | 0.213 | 0 | 0 |
| 13,100 | 13,675 | 575 | 0.197 | 0 | 0 |
| -15,950 | -15,375 | 575 | 0.193 | 0 | 0 |
| 20,200 | 21,025 | 825 | 0.190 | 0 | 1 |
| 22,250 | 22,725 | 475 | 0.163 | 0 | 0 |
| -350 | 600 | 950 | 0.163 | 0 | 0 |
| -9,775 | -9,200 | 575 | 0.157 | 0 | 1 |
| 18,925 | 19,475 | 550 | 0.153 | 0 | 0 |
| 3,525 | 4,050 | 525 | 0.147 | 0 | 0 |
| 21,675 | 22,125 | 450 | 0.127 | 0 | 0 |
| -4,225 | -3,675 | 550 | 0.127 | 0 | 1 |
| 27,075 | 27,500 | 425 | 0.123 | 0 | 0 |
| 625 | 1,150 | 525 | 0.120 | 0 | 0 |
| 26,575 | 27,025 | 450 | 0.113 | 0 | 0 |
| 34,750 | 35,125 | 375 | 0.103 | 0 | 0 |

## Resources that could not be retrieved programmatically

- Lee, Nam & Davidson 2007 (PMID 17570356) full text, which holds the coordinates of gataE
  Module 10 and Module 24, is publisher-restricted in Europe PMC (HTTP 500) and in NCBI efetch
  db=pmc (PMC2031225). The module boundaries were therefore not obtained, and the analysis
  bounds the whole 57 kb gataE regulatory domain instead of the published modules.
- NCBI Datasets ortholog API returned an empty object for gcm, gatae and pks1. L. variegatus
  orthologs were identified by tblastn of the S. purpuratus proteins, then by GeneID lookup.
- bl2seq through the NCBI BLAST URL API returned no RID for 34 kb to 429 kb subject payloads.
  Pairwise comparison was implemented locally (seed and extend, and shared k-mer counting).
