---
title: "PDB GAP_OPPORTUNITY review worklist"
species: [human, yeast]
---
# PDB GAP_OPPORTUNITY review worklist

Genes whose deposited structure papers predate their last experimental GO curation yet are never cited by GOA -- i.e. structural evidence that curation had the opportunity to use but did not. Ranked by gene priority (dark-MF / eukaryote / contested-catalytic) plus the cofactor / ligand / complex richness and number of the uncited structures. Collapsed to one row per gene (the review unit); per-paper detail is in `data/gap_worklist.tsv`.

- Unreviewed genes with >=1 uncited GAP_OPPORTUNITY structure paper: **316**.
- Showing top **30**.

**Caveat:** bound ligands/cofactors are taken from the whole PDB entry, so for a subunit solved inside a megacomplex (ribosome, spliceosome, chaperonin) the ligands may belong to the assembly, not this protein. Treat the ligand column as a hint, and confirm per-chain contacts during review.

| # | gene | org | score | reason | exp_MF | uncited papers | total str | best paper | ligands |
| - | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FANCB | human | 18.5 | euk | 1 | 1 | 6 | PMID:33686268 (2021) | ZN |
| 2 | PNO1 | yeast | 18.5 | euk | 2 | 8 | 15 | PMID:32943521 (2020) | GTP,MG,ZN |
| 3 | RCO1 | yeast | 18.0 | dark_mf,euk | 0 | 5 | 15 | PMID:37468628 (2023) | ZN |
| 4 | RPS3 | human | 17.5 | contested | 78 | 9 | 12 | PMID:29875412 (2018) | ZN |
| 5 | ACLY | human | 17.0 | contested | 7 | 4 | 15 | PMID:28777081 (2017) | 2HP,7A2,7A3,ADE,ADN,ADP,MG |
| 6 | AEBP2 | human | 17.0 | dark_mf,euk | 0 | 6 | 11 | PMID:39303719 (2024) | SAH |
| 7 | AP1S3 | human | 17.0 | euk | 2 | 4 | 15 | PMID:36269825 (2022) | GTP,MG |
| 8 | APEX1 | human | 17.0 | contested | 62 | 7 | 11 | PMID:10667800 (2000) | MN |
| 9 | ATP5F1E | human | 17.0 | contested | 5 | 2 | 10 | PMID:37244256 (2023) | 3PH,ADP,ATP,CDL,MG |
| 10 | ATP5PO | human | 17.0 | contested | 24 | 2 | 9 | PMID:37244256 (2023) | 3PH,ADP,ATP,CDL,MG |
| 11 | BIRC5 | human | 17.0 | contested | 59 | 6 | 14 | PMID:22357620 (2012) | ZN |
| 12 | CPS1 | human | 17.0 | contested | 13 | 4 | 11 | PMID:25111069 (2014) | 0L1,3NP,F9V,FSL,GUA,JO3,NX6,SU8,... |
| 13 | GCH1 | human | 17.0 | contested | 19 | 2 | 10 | PMID:33229582 (2020) | 5RW,8GT,HBI,PHE,QBK,QBQ,ZN |
| 14 | HSD17B10 | human | 17.0 | contested | 33 | 4 | 6 | PMID:39747487 (2025) | SAH,ZN |
| 15 | MCCC1 | human | 17.0 | contested | 9 | 1 | 9 | PMID:39223421 (2025) | ACO,BTI,TW3 |
| 16 | NAA10 | human | 17.0 | contested | 93 | 4 | 8 | PMID:39169182 (2024) | GTP,IHP,MG,SPD,SPM,ZN |
| 17 | NAA15 | human | 17.0 | contested | 26 | 5 | 10 | PMID:39169182 (2024) | GTP,IHP,MG,SPD,SPM,ZN |
| 18 | RAD51C | human | 17.0 | contested | 33 | 2 | 5 | PMID:41196948 (2026) | ADP,ATP,CA,MG |
| 19 | CCT2 | yeast | 16.5 | euk | 1 | 5 | 14 | PMID:31492816 (2019) | ADP,AF3,MG |
| 20 | CCT5 | yeast | 16.5 | dark_mf,euk | 0 | 5 | 14 | PMID:31492816 (2019) | ADP,AF3,MG |
| 21 | CCT7 | yeast | 16.5 | euk | 1 | 6 | 15 | PMID:31492816 (2019) | ADP,AF3,MG |
| 22 | CWC27 | human | 16.5 | euk | 1 | 3 | 4 | PMID:29361316 (2018) | ADP,GTP,IHP,MG,ZN |
| 23 | EIF2D | human | 16.5 | euk | 1 | 2 | 3 | PMID:28732596 (2017) | ZN |
| 24 | PHKA1 | human | 16.5 | contested,dark_mf,euk | 0 | 1 | 5 | PMID:40148320 (2025) | ATP |
| 25 | ATM | human | 16.0 | contested | 77 | 5 | 12 | PMID:37756394 (2023) | ANP,MG,ZN |
| 26 | BCL11A | human | 16.0 | euk | 2 | 7 | 11 | PMID:40246927 (2025) | MG,ZN |
| 27 | COLGALT1 | human | 16.0 | euk | 1 | 2 | 7 | PMID:40069201 (2025) | 660,AKG,FE2,GDU,MN,NAG,UDP |
| 28 | GPI | human | 16.0 | contested | 4 | 8 | 13 | PMID:37347872 (2023) | AAC,GTP,MG,N,SPD,SPM,ZN |
| 29 | IDH3B | human | 16.0 | contested,dark_mf,euk | 0 | 3 | 9 | PMID:31515270 (2019) | CA,NAD,NAI,PE7 |
| 30 | Ndufb1 | mouse | 16.0 | dark_mf,euk | 0 | 7 | 15 | PMID:39395414 (2024) | 3PE,3PH,ADP,CDL,EHZ,FES,FMN,HEC,... |
