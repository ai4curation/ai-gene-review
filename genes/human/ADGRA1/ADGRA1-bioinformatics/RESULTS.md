# ADGRA1 (Q86SQ6) — computed evidence for the GO review

Regenerate with `uv run python analyze_adgra1.py`. Every number below is
read from UniProt, IntAct or QuickGO at run time; none is hardcoded.

## Q1. A cytoplasmic C-terminal class I PDZ-binding motif

- `AGRA1_HUMAN` (Swiss-Prot), 560 aa, 7 TM helices.
- N-terminal extracellular domain: residues 1–19 (**19 residues**) — there is no ectodomain to hold a GAIN/GPS module.
- C-terminal cytoplasmic tail: residues 306–560 (255 residues).
- Last four residues: `ETTV`; matches the class I PDZ-binding consensus `X-[ST]-X-[VIL]`: **True**.
- UniProt has an annotated `MOTIF` feature for it: **False**.

## Q2. Every GOA `GO:0005515` partner is a PDZ-domain protein

21/21 partners carry at least one annotated PDZ domain; 21 reviewed (Swiss-Prot), 0 unreviewed (TrEMBL).

| partner | accession | entry | status | length | PDZ domains |
|---|---|---|---|---|---|
| APBA1 | Q02410 | APBA1_HUMAN | Swiss-Prot | 837 | 2 |
| APBA2 | Q99767 | APBA2_HUMAN | Swiss-Prot | 749 | 2 |
| DLG1 | Q12959 | DLG1_HUMAN | Swiss-Prot | 904 | 3 |
| DLG2 | Q15700 | DLG2_HUMAN | Swiss-Prot | 870 | 3 |
| DLG3 | Q92796 | DLG3_HUMAN | Swiss-Prot | 817 | 3 |
| DLG4 | P78352 | DLG4_HUMAN | Swiss-Prot | 724 | 3 |
| FRMPD2 | Q68DX3 | FRPD2_HUMAN | Swiss-Prot | 1309 | 3 |
| GRID2IP | A4D2P6 | GRD2I_HUMAN | Swiss-Prot | 1211 | 2 |
| GRIP1 | Q9Y3R0 | GRIP1_HUMAN | Swiss-Prot | 1128 | 7 |
| GRIP2 | Q9C0E4 | GRIP2_HUMAN | Swiss-Prot | 1043 | 7 |
| IL16 | Q14005 | IL16_HUMAN | Swiss-Prot | 1332 | 4 |
| LNX1 | Q8TBB1 | LNX1_HUMAN | Swiss-Prot | 728 | 4 |
| LNX2 | Q8N448 | LNX2_HUMAN | Swiss-Prot | 690 | 4 |
| MAGI1 | Q96QZ7 | MAGI1_HUMAN | Swiss-Prot | 1491 | 6 |
| MAGI2 | Q86UL8 | MAGI2_HUMAN | Swiss-Prot | 1455 | 6 |
| MPDZ | O75970 | MPDZ_HUMAN | Swiss-Prot | 2070 | 13 |
| PATJ | Q8NI35 | INADL_HUMAN | Swiss-Prot | 1801 | 10 |
| PDZK1 | Q5T2W1 | NHRF3_HUMAN | Swiss-Prot | 519 | 4 |
| SCRIB | Q14160 | SCRIB_HUMAN | Swiss-Prot | 1655 | 4 |
| TJP1 | Q07157 | ZO1_HUMAN | Swiss-Prot | 1748 | 3 |
| WHRN | Q9P202 | WHRN_HUMAN | Swiss-Prot | 907 | 3 |

## Q3. IntAct: one quantitative affinity dataset, not a Y2H screen

- 124 interaction records over 80 distinct partners.
- detection methods: `holdup assay` ×122, `bead aggregation` ×1, `phage display` ×1.
- curated-negative flag: False=124.
- Of the GOA partner set, **8 have a quantified Kd** and **13 do not** (IntAct carries `kd:1(molar)`, a placeholder, for the latter).

| GOA partner | best quantified Kd (µM) |
|---|---|
| DLG1 | 4.6 |
| DLG2 | 7.9 |
| DLG3 | 9.8 |
| DLG4 | 8.3 |
| LNX2 | 11.7 |
| MAGI1 | 21.2 |
| MAGI2 | 6.7 |
| SCRIB | 20.6 |
| APBA1 | not quantified |
| APBA2 | not quantified |
| FRMPD2 | not quantified |
| GRID2IP | not quantified |
| GRIP1 | not quantified |
| GRIP2 | not quantified |
| IL16 | not quantified |
| LNX1 | not quantified |
| MPDZ | not quantified |
| PATJ | not quantified |
| PDZK1 | not quantified |
| TJP1 | not quantified |
| WHRN | not quantified |

## Q4. The GOA partner set is selected by domain count, not by affinity

- UniProt's `NbExp` equals the IntAct record count for **21/21** partners.
- IntAct partners with ≥2 records: 22; with exactly 1: 58.
- Multi-record partners absent from the UniProt/GOA set: ['NHERF4'].
- UniProt/GOA partners that are single-record: none.

So `NbExp` here counts **how many PDZ domains of the same partner protein were assayed**
within one holdup dataset, not independent experiments, and the GOA cut is `NbExp ≥ 2`.
The cost: **23 partners with a genuinely measured Kd**
are excluded, including the tightest binders measured:

| excluded partner | Kd (µM) |
|---|---|
| SNX27 | 3.7 |
| MAST2 | 4.9 |
| MAGI3 | 5.1 |
| SYNJ2BP | 7.4 |
| PDZD7 | 12.5 |
| PTPN3 | 17.3 |
| MAST1 | 19.7 |
| SNTB1 | 21.2 |
| SNTA1 | 25.6 |
| RHPN1 | 28.3 |
| TAX1BP3 | 33.8 |
| PDZRN4 | 49.3 |
| LIN7C | 53.7 |
| SNTG2 | 54.7 |
| HTRA1 | 55.0 |
| GIPC2 | 56.9 |
| SNTG1 | 64.7 |
| ARHGEF11 | 80.4 |
| PDZRN3 | 84.9 |
| ARHGEF12 | 90.0 |
| RADIL | 91.7 |
| PDZD2 | 94.9 |
| HTRA4 | 120.7 |

## Q5. PAINT node reach across the human ADGRA family

| node | human reach | terms given |
|---|---|---|
| `PANTHER:PTN001738137` | ADGRA1, ADGRA2, ADGRA3 | GO:0005886, GO:0007166 |
| `PANTHER:PTN002914494` | ADGRA3 | GO:0009897 |
| `PANTHER:PTN002914505` | ADGRA1 | GO:0014069, GO:0098978 |
| `PANTHER:PTN002914520` | ADGRA2 | GO:0002040, GO:0007417, GO:0090263, GO:1990909 |

| IBA donor token | resolves to | organism | status | ADGRA1 ortholog? | own experimental annotations |
|---|---|---|---|---|---|
| `MGI:MGI:1277167` | Adgra1 (Q8C4G9, AGRA1_MOUSE) | Mus musculus | Swiss-Prot | yes | GO:0014069 EXP (PMID:28935861); GO:0014069 IDA (PMID:28935861); GO:0098978 EXP (PMID:28935861); GO:0098978 IDA (PMID:28935861) |
| `MGI:MGI:1917943` | Adgra3 (Q7TT36, AGRA3_MOUSE) | Mus musculus | Swiss-Prot | no — paralog | GO:0009897 IDA (PMID:17882221) |
| `MGI:MGI:1925810` | Adgra2 (Q91ZV8, AGRA2_MOUSE) | Mus musculus | Swiss-Prot | no — paralog | GO:0001525 IMP (PMID:21421844); GO:0002040 IMP (PMID:21071672); GO:0002040 IMP (PMID:23918385); GO:0005886 EXP (PMID:25558062); GO:0005886 IDA (PMID:28803732); GO:0007417 IMP (PMID:21071672); GO:0009986 IDA (PMID:21421844); GO:0010595 IDA (PMID:21421844); GO:0043542 IMP (PMID:21071672); GO:0045765 IMP (PMID:21071672); GO:0050920 IMP (PMID:21071672); GO:0090210 IMP (PMID:21421844); GO:0090210 IMP (PMID:28288111); GO:0090263 IDA (PMID:28803732); GO:1900747 IMP (PMID:21421844) |
| `UniProtKB:Q96PE1` | ADGRA2 (Q96PE1, AGRA2_HUMAN) | Homo sapiens | Swiss-Prot | no — paralog | GO:0005515 IPI (PMID:15021905); GO:0005515 IPI (PMID:24550280); GO:0005515 IPI (PMID:36115835); GO:0005886 EXP (PMID:16982628); GO:0005886 EXP (PMID:21421844); GO:0005886 EXP (PMID:22013897); GO:0005886 IDA (GO_REF:0000052); GO:0060070 IDA (PMID:30026314); GO:1990909 IDA (PMID:30026314) |
| `ZFIN:ZDB-GENE-081104-363` *(1 of 2 candidates — ambiguous xref)* | adgra2 (A0A0U2ULT4, A0A0U2ULT4_DANRE) | Danio rerio | TrEMBL | no — paralog | GO:0001944 IMP (PMID:26051822); GO:0001944 IMP (PMID:27979884); GO:0002040 IMP (PMID:26051822); GO:0005515 IPI (PMID:30026314); GO:0016055 IMP (PMID:26051822); GO:0022009 IMP (PMID:28365243); GO:1904701 IMP (PMID:35649360); GO:1990791 IMP (PMID:24004948); GO:1990791 IMP (PMID:26051822); GO:1990791 IMP (PMID:27979884) |
| `ZFIN:ZDB-GENE-081104-363` *(1 of 2 candidates — ambiguous xref)* | adgra2 (A0A8M1P7B9, A0A8M1P7B9_DANRE) | Danio rerio | TrEMBL | no — paralog | none |
| `ZFIN:ZDB-GENE-131003-2` | adgra3 (S4X0Q8, AGRA3_DANRE) | Danio rerio | Swiss-Prot | no — paralog | GO:0005886 IDA (PMID:23821037); GO:0060027 IGI (PMID:23821037); GO:0060071 IDA (PMID:23821037); GO:0097475 IGI (PMID:23821037); GO:2000095 IMP (PMID:23821037); GO:2000095 IPI (PMID:23821037) |

**1 of 6** IBA donor tokens are ADGRA1 orthologs; the rest are ADGRA2/ADGRA3 paralogs.

## Q6. What each legacy reference annotates

| reference | annotations | distinct entities | terms (entities each) |
|---|---|---|---|
| PMID:12565841 | 2 | 1 | GO:0004930 NAS (1), GO:0016020 NAS (1) |
| PMID:15203201 | 78 | 27 | GO:0004930 TAS (25), GO:0007186 TAS (26), GO:0016020 TAS (27) |
| PMID:17212699 | 3 | 1 | GO:0004930 NAS (1), GO:0007165 NAS (1), GO:0016020 NAS (1) |

`PMID:15203201` annotates **27 distinct entities** with identical evidence:
`ADGRA1`, `ADGRA2`, `ADGRA3`, `ADGRB1`, `ADGRB2`, `ADGRB3`, `ADGRD1`, `ADGRD2`, `ADGRE2`, `ADGRE3`, `ADGRE4P`, `ADGRF1`, `ADGRF2P`, `ADGRF3`, `ADGRF4`, `ADGRF5`, `ADGRG3`, `ADGRG4`, `ADGRG5`, `ADGRG6`, `ADGRG7`, `ADGRL1`, `ADGRL2`, `ADGRL3`, `ADGRL4`, `ADGRV1`, `CELSR3`.
