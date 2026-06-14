# PDB GAP_OPPORTUNITY review worklist

Genes whose deposited structure papers predate their last experimental GO curation yet are never cited by GOA -- i.e. structural evidence that curation had the opportunity to use but did not. Ranked by gene priority (dark-MF / eukaryote / contested-catalytic) plus the cofactor / ligand / complex richness and number of the uncited structures. Collapsed to one row per gene (the review unit); per-paper detail is in `data/gap_worklist.tsv`.

- Genes with >=1 uncited GAP_OPPORTUNITY structure paper: **138**.
- Showing top **25**.

**Caveat:** bound ligands/cofactors are taken from the whole PDB entry, so for a subunit solved inside a megacomplex (ribosome, spliceosome, chaperonin) the ligands may belong to the assembly, not this protein. Treat the ligand column as a hint, and confirm per-chain contacts during review.

| # | gene | org | score | reason | exp_MF | uncited papers | total str | best paper | ligands |
| - | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PNO1 | yeast | 18.5 | euk | 2 | 8 | 15 | PMID:32943521 (2020) | GTP,MG,ZN |
| 2 | RPS3 | human | 17.5 | contested | 75 | 9 | 12 | PMID:29875412 (2018) | ZN |
| 3 | BIRC5 | human | 17.0 | contested | 59 | 6 | 14 | PMID:22357620 (2012) | ZN |
| 4 | GCH1 | human | 17.0 | contested | 19 | 2 | 10 | PMID:33229582 (2020) | 5RW,8GT,HBI,PHE,QBK,QBQ,ZN |
| 5 | HAP1 | human | 17.0 | contested | 61 | 6 | 9 | PMID:10667800 (2000) | MN |
| 6 | NAA15 | human | 17.0 | contested | 25 | 5 | 10 | PMID:39169182 (2024) | GTP,IHP,MG,SPD,SPM,ZN |
| 7 | CCT7 | yeast | 16.5 | euk | 1 | 6 | 15 | PMID:31492816 (2019) | ADP,AF3,MG |
| 8 | CWC27 | human | 16.5 | euk | 1 | 3 | 4 | PMID:29361316 (2018) | ADP,GTP,IHP,MG,ZN |
| 9 | BRCA2 | human | 16.0 | contested | 69 | 9 | 12 | PMID:38075664 (2023) | ADP,MG,RF6,TKI |
| 10 | COLGALT1 | human | 16.0 | euk | 1 | 2 | 7 | PMID:40069201 (2025) | 660,AKG,FE2,GDU,MN,NAG,UDP |
| 11 | HEN1 | ARATH | 16.0 | contested,euk | 2 | 1 | 1 | PMID:19812675 (2009) | MG,SAH |
| 12 | IDH3B | human | 16.0 | contested,dark_mf,euk | 0 | 3 | 9 | PMID:31515270 (2019) | CA,NAD,NAI,PE7 |
| 13 | Ndufb1 | mouse | 16.0 | dark_mf,euk | 0 | 7 | 15 | PMID:39395414 (2024) | 3PE,3PH,ADP,CDL,EHZ,FES,FMN,HEC,HEM, |
| 14 | SIRT2 | human | 16.0 | contested | 50 | 6 | 13 | PMID:25672491 (2015) | 3TE,3TK,AR6,NAD,NCA,ZN |
| 15 | TOMM20 | human | 16.0 | contested | 10 | 3 | 6 | PMID:40263465 (2026) | ZN |
| 16 | ATG14 | human | 15.5 | contested | 41 | 2 | 4 | PMID:39913640 (2025) | GTP,MG |
| 17 | ATP6V1C1 | human | 15.5 | euk | 1 | 3 | 5 | PMID:33065002 (2020) | ADP,CLR,NAG,PSF,PTY,WJP,WJS,WSS |
| 18 | DOT1 | yeast | 15.5 | contested | 8 | 2 | 3 | PMID:33479126 (2021) | SAM |
| 19 | HTT | human | 15.5 | contested | 1061 | 5 | 15 | PMID:19748341 (2009) | CA,ZN |
| 20 | MAPK1 | human | 15.5 | contested | 111 | 9 | 15 | PMID:23047924 (2012) | ANP |
| 21 | AKT1 | human | 15.0 | contested | 213 | 10 | 15 | PMID:18456494 (2008) | CQU,CQW,MN |
| 22 | CRY2 | ARATH | 15.0 | contested | 33 | 4 | 6 | PMID:32398826 (2020) | AMP,FAD,MG |
| 23 | EDS1 | ARATH | 15.0 | contested | 15 | 3 | 5 | PMID:39939760 (2025) | APR,ATP |
| 24 | HSPA1A | human | 15.0 | contested | 73 | 9 | 13 | PMID:18555782 (2008) | ATP,MG |
| 25 | PAD4 | ARATH | 15.0 | contested | 6 | 2 | 4 | PMID:35857645 (2022) | ADP,RP5 |
