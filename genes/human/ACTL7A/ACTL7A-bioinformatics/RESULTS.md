# ACTL7A actin-fold audit: does the fold still carry actin's working parts?

Reproduce with `uv run --script actin_fold_audit.py` (regenerates `results.json`
and this file byte-for-byte; inputs are cached under `data/`, which is not committed).

## Why

ACTL7A is annotated with actin-derived terms (`GO:0005200 structural constituent of
cytoskeleton`, `GO:0007010 cytoskeleton organization`, `GO:0005198 structural molecule
activity`). Those hold only if ACTL7A retains the machinery the terms imply. This audit
derives two residue sets from experimental actin structures and reports what ACTL7A has
at those positions, against a panel that spans the family from conventional actin to the
most divergent SWI/SNF Arps.

## Findings

* Whole-chain identity of ACTL7A to the deposited actin: **43.7%**.
* **Nucleotide cleft largely retained.** ACTL7A is 63.2% identical to actin across the 19 G-actin cleft positions (66.7% at the phosphate contacts), against 96.5% for conventional actins, 79.0% for Arp2/Arp3 and 36.9% for the divergent SWI/SNF Arps.
* **The ATP-hydrolysis trigger is not retained.** Of the 5 literature-defined catalytic positions ACTL7A keeps 3 (DQEVY); changed: D154->E, H161->Y. Every conventional actin and Arp1/Arp2/Arp3 in the panel keeps all of them.
* **The filament interface is not retained.** ACTL7A matches actin at 42.3% of the 79 inter-protomer contact positions, versus 93.2% for conventional actins and 55.7% for Arp1, which does form a filament (in dynactin).
* **The cleft is under disease-relevant constraint.** 2/5 ACTL7A variants reported in SPGF86 patients map into the nucleotide cleft, which covers only 4.6% of the protein (binomial p = 0.0193); 0/4 population polymorphisms do.

## Method

* Nucleotide-cleft residues: every residue within 4.0 A of
  ATP or the divalent cation in **PDB 2BTF** (profilin-beta-actin), and of ADP/Pi/Mg in
  **PDB 8A2S** (cryo-EM F-actin, Mg-ADP-Pi, 5 protomers).
* Inter-protomer interface: every residue within 4.5 A of a
  *different* protomer in 8A2S, required in >=50% of the protomers that have any such contact
  (so the terminal protomers do not dilute the set).
* Alignment: `mafft --localpair --maxiterate 1000 --anysymbol` (v7.526 (2024/Apr/26)), with the deposited SEQRES sequences
  included as alignment entries so that structural positions map without hard-coded numbering.
* Contact sets are computed by neighbour search, never listed by hand.

## Site sizes

| site | n positions | description |
|---|---|---|
| `g_pocket_all` | 19 | any residue within 4.0 A of ATP or the divalent cation (PDB 2BTF (profilin-beta-actin, ATP)) |
| `g_pocket_adenine` | 4 | within 4.0 A of the ATP adenine ring (PDB 2BTF) |
| `g_pocket_phosphate` | 12 | within 4.0 A of the ATP alpha/beta/gamma phosphates (PDB 2BTF) |
| `g_pocket_metal` | 1 | within 4.0 A of the divalent cation (PDB 2BTF) |
| `f_pocket_all` | 20 | within 4.0 A of ADP/Pi/Mg in >=50% of protomers (PDB 8A2S (cryo-EM F-actin, Mg-ADP-Pi)) |
| `f_protomer_interface` | 79 | within 4.5 A of a neighbouring protomer in >=50% of protomers that have any inter-protomer contact (PDB 8A2S) |

## Conservation at the derived sites

`% id` = identity to the deposited actin sequence at that site's positions.

| protein | group | len | % id vs actin (whole chain) | nucleotide cleft, G-actin | phosphates | metal | adenine | nucleotide cleft, F-actin | protomer interface |
|---|---|---|---|---|---|---|---|---|---|
| ACTL7A_HUMAN | query | 435 | 43.7 | 63.2 | 66.7 | 100.0 | 50.0 | 60.0 | 42.3 |
| ACTL7A_MOUSE | query_ortholog | 440 | 43.7 | 63.2 | 66.7 | 100.0 | 50.0 | 60.0 | 41.0 |
| ACTL7A_RAT | query_ortholog | 440 | 44.2 | 63.2 | 66.7 | 100.0 | 50.0 | 60.0 | 41.0 |
| ACTL7B_HUMAN | query_paralog | 415 | 44.6 | 68.4 | 75.0 | 100.0 | 50.0 | 65.0 | 36.4 |
| ACTL9_HUMAN | testis_arp | 416 | 41.2 | 57.9 | 66.7 | 100.0 | 25.0 | 55.0 | 29.5 |
| ACTL10_HUMAN | testis_arp | 245 | 33.3 | 50.0 | 71.4 | 0.0 | 25.0 | 46.7 | 18.2 |
| ACTRT1_HUMAN | testis_arp | 376 | 48.7 | 73.7 | 83.3 | 0.0 | 50.0 | 75.0 | 39.7 |
| ACTRT2_HUMAN | testis_arp | 377 | 48.5 | 68.4 | 75.0 | 100.0 | 25.0 | 65.0 | 41.8 |
| ACTRT3_HUMAN | testis_arp | 372 | 49.2 | 78.9 | 91.7 | 100.0 | 50.0 | 70.0 | 43.6 |
| ACTB_HUMAN | conventional_actin | 375 | 99.7 | 100.0 | 100.0 | 100.0 | 100.0 | 95.0 | 96.2 |
| ACTA1_HUMAN | conventional_actin | 377 | 93.3 | 94.7 | 91.7 | 100.0 | 100.0 | 100.0 | 100.0 |
| ACT1_YEAST | conventional_actin | 375 | 88.5 | 94.7 | 100.0 | 100.0 | 75.0 | 90.0 | 83.5 |
| ARP1_HUMAN | filament_forming_arp | 376 | 52.8 | 73.7 | 83.3 | 100.0 | 50.0 | 70.0 | 55.7 |
| ARP2_HUMAN | nucleotide_binding_arp | 394 | 47.5 | 84.2 | 83.3 | 100.0 | 100.0 | 85.0 | 41.8 |
| ARP3_HUMAN | nucleotide_binding_arp | 418 | 38.7 | 73.7 | 75.0 | 100.0 | 75.0 | 70.0 | 24.4 |
| ARP4_BAF53A_HUMAN | nuclear_arp | 429 | 37.1 | 31.6 | 41.7 | 0.0 | 25.0 | 30.0 | 38.0 |
| ARP5_HUMAN | nuclear_arp | 607 | 29.2 | 42.1 | 41.7 | 0.0 | 75.0 | 40.0 | 22.4 |
| ARP6_HUMAN | nuclear_arp | 396 | 28.6 | 42.1 | 41.7 | 0.0 | 50.0 | 40.0 | 21.4 |
| ARP8_HUMAN | nuclear_arp | 624 | 22.1 | 52.6 | 50.0 | 0.0 | 75.0 | 50.0 | 17.7 |
| ARP4_YEAST | nuclear_arp | 489 | 32.9 | 47.4 | 41.7 | 0.0 | 50.0 | 45.0 | 29.2 |
| ARP7_YEAST | divergent_swisnf_arp | 477 | 22.9 | 42.1 | 41.7 | 0.0 | 0.0 | 40.0 | 16.7 |
| ARP9_YEAST | divergent_swisnf_arp | 467 | 18.7 | 31.6 | 33.3 | 0.0 | 25.0 | 30.0 | 20.3 |

## Residue-by-residue at the G-actin nucleotide cleft

Positions (2BTF numbering): 13, 14, 15, 16, 18, 137, 156, 157, 158, 159, 182, 213, 214, 301, 302, 303, 305, 306, 336

| protein | residues at those positions |
|---|---|
| **2BTF actin (reference)** | `GSGMKQGDGVGKEGGTMYK` |
| ACTL7A_HUMAN | `GTGYKQGHGVGKKGGSMLD` |
| ACTL7A_MOUSE | `GTGFKQGHGVGKTGGSMLD` |
| ACTL7A_RAT | `GTGFKQGHGVGKTGGSMLD` |
| ACTL7B_HUMAN | `GSQYKQGHGVGKKGGCMLK` |
| ACTL9_HUMAN | `GTGTKQGHGVGKHGGSLFN` |
| ACTL10_HUMAN | `-----TGAGVGKKGGSLFG` |
| ACTRT1_HUMAN | `GSGLKHGDGVGKEGGTLLC` |
| ACTRT2_HUMAN | `GSGFKQGDAVGKKGGTLFW` |
| ACTRT3_HUMAN | `GSGMKQGAGVGKEGGSSFK` |
| ACTB_HUMAN | `GSGMKQGDGVGKEGGTMYK` |
| ACTA1_HUMAN | `GSGLKQGDGVGKEGGTMYK` |
| ACT1_YEAST | `GSGMKQGDGVGKEGGTMFK` |
| ARP1_HUMAN | `GSGVKQGDGVGKEGGSLFL` |
| ARP2_HUMAN | `GTGFKQGDGVGKEGGSMYK` |
| ARP3_HUMAN | `GTGYKQGDGVGKEGGSMFR` |
| ARP4_BAF53A_HUMAN | `GSYTRTGATHGQAGGNLIR` |
| ARP5_HUMAN | `GSFQRDGYQCGLHGGNMYV` |
| ARP6_HUMAN | `GAYNKAGYSFGKEGGNLFI` |
| ARP8_HUMAN | `GSTTREGDQKGKEGGGMFR` |
| ARP4_YEAST | `GSYTNTGHDTGKEGGTSIQ` |
| ARP7_YEAST | `GSHRVEGASGGKSGSTLIK` |
| ARP9_YEAST | `RSQTLAGTHHGAKGGTSIS` |

## The ATP-hydrolysis catalytic set

Actin residues D11, Q137, D154, V159, H161 (standard actin numbering, verified against the 2BTF SEQRES).
Gln137 and His161 are the hydrolysis pair; Asp154 and the Val159 main chain stabilise the
attacking water; Asp11 is part of the divalent-cation site. Sources: PMID:37009486,
PMID:30622175.

| protein | group | residues at D11, Q137, D154, V159, H161 | conserved / 5 |
|---|---|---|---|
| ACTL7A_HUMAN | query | `DQEVY` | 3 |
| ACTL7A_MOUSE | query_ortholog | `DQEVY` | 3 |
| ACTL7A_RAT | query_ortholog | `DQEVY` | 3 |
| ACTL7B_HUMAN | query_paralog | `DQEVH` | 4 |
| ACTL9_HUMAN | testis_arp | `DQDVY` | 4 |
| ACTL10_HUMAN | testis_arp | `-TEVH` | 2 |
| ACTRT1_HUMAN | testis_arp | `DHDVC` | 3 |
| ACTRT2_HUMAN | testis_arp | `DQDVC` | 4 |
| ACTRT3_HUMAN | testis_arp | `DQNVQ` | 3 |
| ACTB_HUMAN | conventional_actin | `DQDVH` | 5 |
| ACTA1_HUMAN | conventional_actin | `DQDVH` | 5 |
| ACT1_YEAST | conventional_actin | `DQDVH` | 5 |
| ARP1_HUMAN | filament_forming_arp | `DQDVH` | 5 |
| ARP2_HUMAN | nucleotide_binding_arp | `DQDVH` | 5 |
| ARP3_HUMAN | nucleotide_binding_arp | `DQDVH` | 5 |
| ARP4_BAF53A_HUMAN | nuclear_arp | `DTDHT` | 2 |
| ARP5_HUMAN | nuclear_arp | `DDSCH` | 2 |
| ARP6_HUMAN | nuclear_arp | `DADFH` | 3 |
| ARP8_HUMAN | nuclear_arp | `HEDKS` | 1 |
| ARP4_YEAST | nuclear_arp | `DTDTS` | 2 |
| ARP7_YEAST | divergent_swisnf_arp | `HEDGN` | 1 |
| ARP9_YEAST | divergent_swisnf_arp | `YADHD` | 1 |

## ACTL7A variants against the derived sites

ACTL7A numbering includes its 64-residue N-terminal extension, so ACTL7A position *n*
aligns to roughly actin position *n* - 64; the mapped actin position is given explicitly.

| variant | reported in SPGF86 | aligned actin position | actin residue there | falls in |
|---|---|---|---|---|
| R45C | no | - | - | - |
| D75A | yes | 11 | D | - |
| A161P | no | 97 | A | - |
| A245T | yes | 181 | A | - |
| G246A | yes | 182 | G | `f_pocket_all`, `g_pocket_all` |
| V340M | no | 279 | F | - |
| L343V | no | 282 | I | - |
| G362R | yes | 301 | G | `f_pocket_all`, `g_pocket_all`, `g_pocket_phosphate` |
| G402S | yes | 342 | G | - |

20 of ACTL7A's 435 residues align to a nucleotide-cleft column (4.6% of the protein). 2/5 variants reported in SPGF86 patients fall there (exact binomial upper tail p = 0.0193), versus 0/4 population polymorphisms.

*Caveat:* n is small and the variant set is not an unbiased sample, so this is suggestive only; UniProt annotates A245T, G246A and G362R as 'uncertain significance'.

## Alignment windows around every mapped position

Included so the mapping can be checked rather than trusted: if these windows were
gap-ridden the residue calls above would be alignment artefacts.

actin 3-19:

```
ACTB_2BTF_chainA     DDIAALVVDNGSGMCKA
ACTB_HUMAN           DDIAALVVDNGSGMCKA
ACTA1_HUMAN          DETTALVCDNGSGLVKA
ACTL7A_HUMAN         EVTKAVVVDLGTGYCKC
ACTL7B_HUMAN         HKIKAVIIDLGSQYCKC
ACTL9_HUMAN          PKTGAVVIDMGTGTCKV
ARP1_HUMAN           IANQPVVIDNGSGVIKA
ARP2_HUMAN           QGRKVVVCDNGTGFVKC
ARP9_YEAST           RQDSILIIYPRSQTTLV
```

actin 89-105:

```
ACTB_2BTF_chainA     TFY-NEL-RVAPE-----------EH-PVLL
ACTB_HUMAN           TFY-NEL-RVAPE-----------EH-PVLL
ACTA1_HUMAN          TFY-NEL-RVAPE-----------EH-PTLL
ACTL7A_HUMAN         LFR-QEM-KIAPE-----------EH-AVLV
ACTL7B_HUMAN         IFR-TAM-KILPE-----------EH-AVLV
ACTL9_HUMAN          LLE-HDL-RVATH-----------DH-PLLF
ARP1_HUMAN           VYSKDQL-QTFSE-----------EH-PVLL
ARP2_HUMAN           TFGPEKL-NIDTR-----------NC-KILL
ARP9_YEAST           IFV-SIL-SDRANKNQDAFEAELSNI-PLLL
```

actin 129-169:

```
ACTB_2BTF_chainA     TPAMYVAIQAVLSLYASGRT--------TGIVMDSGDGVTHTVPIYEGY
ACTB_HUMAN           TPAMYVAIQAVLSLYASGRT--------TGIVMDSGDGVTHTVPIYEGY
ACTA1_HUMAN          VPAMYVAIQAVLSLYASGRT--------TGIVLDSGDGVTHNVPIYEGY
ACTL7A_HUMAN         TPAMHIAYQSRLSMYSYGRT--------SGLVVEVGHGVSYVVPIYEGY
ACTL7B_HUMAN         IPAMHVTSQSLLSIYSYGKT--------SGLVVESGHGVSHVVPISEGD
ACTL9_HUMAN          SPAMYVASQSVLSVYAHGRV--------SGLVVDTGHGVTYTVPVFQGY
ARP1_HUMAN           VPALFISMQAVLSLYATGRT--------TGVVLDSGDGVTHAVPIYEGF
ARP2_HUMAN           FSGVYVAIQAVLTLYAQGLL--------TGVVVDSGDGVTHICPVYEGF
ARP9_YEAST           INNLIQLPASLAATYSMISL-------QNCCIIDVGTHHTDIIPIVDYA
```

actin 173-190:

```
ACTB_2BTF_chainA     HAILRLDLAGRDLTDYLM
ACTB_HUMAN           HAILRLDLAGRDLTDYLM
ACTA1_HUMAN          HAIMRLDLAGRDLTDYLM
ACTL7A_HUMAN         SITGRLDYAGSDLTAYLL
ACTL7B_HUMAN         GLTSRADYAGGDLTNYLM
ACTL9_HUMAN          HATERLDLAGNNLTAFLA
ARP1_HUMAN           HSIMRIDIAGRDVSRFLR
ARP2_HUMAN           HLTRRLDIAGRDITRYLI
ARP9_YEAST           HLVSSIPMGGQSINDSLK
```

actin 271-290:

```
ACTB_2BTF_chainA     SCGIHETTFNSIMKC-DVDIR
ACTB_HUMAN           SCGIHETTFNSIMKC-DVDIR
ACTA1_HUMAN          SAGIHETTYNSIMKC-DIDIR
ACTL7A_HUMAN         QLGLHTQTVSCLNKC-DIALK
ACTL7B_HUMAN         QPGLPELTAACLGRCQDTGFK
ACTL9_HUMAN          PVGLSTMAKQSLRKL-SLEMR
ARP1_HUMAN           SEGIHEVLVFAIQKS-DMDLR
ARP2_HUMAN           GVGVAELLFNTIQAA-DIDTR
ARP9_YEAST           -KNISNRVGLTLDNIDDINKA
```

actin 293-309:

```
ACTB_2BTF_chainA     LYANTVLSGGTTMYPGI
ACTB_HUMAN           LYANTVLSGGTTMYPGI
ACTA1_HUMAN          LYANNVMSGGTTMYPGI
ACTL7A_HUMAN         LMGNILLCGGSTMLSGF
ACTL7B_HUMAN         MAANVLLCGGCTMLDGF
ACTL9_HUMAN          LAQNVLLCGGSSLFTGF
ARP1_HUMAN           LFSNIVLSGGSTLFKGF
ARP2_HUMAN           FYKHIVLSGGSTMYPGL
ARP9_YEAST           VWENIIIVGGTTSISGF
```

actin 334-350:

```
ACTB_2BTF_chainA     ERKYSVWIGGSILA-SLS
ACTB_HUMAN           ERKYSVWIGGSILA-SLS
ACTA1_HUMAN          ERKYSVWIGGSILA-SLS
ACTL7A_HUMAN         ERDSAVWTGGSILA-SLQ
ACTL7B_HUMAN         ERKTSVWTGGSILA-SLQ
ACTL9_HUMAN          TRNFSVWIGGSILA-SLR
ARP1_HUMAN           ERLYSTWIGGSILA-SLD
ARP2_HUMAN           RRKHMVFLGGAVLA-DIM
ARP9_YEAST           GYSEIIFLGAQIVSKQIF
```

## Notes on interpretation

* This is a sequence-and-structure audit, not an assay. Retained residues mean the
  activity is *not excluded*; they do not demonstrate it. Lost residues are the stronger
  signal, because they exclude the activity on structural grounds.
* The comparator groups are the yardstick: read ACTL7A's numbers against the conventional
  actins (which bind nucleotide and polymerise) and against ARP7/ARP9 (the family's most
  divergent members).
* Percentages at a site are identity to *this particular* actin, so a conservative
  substitution counts as a mismatch. The residue-level table above is the thing to read
  when a percentage looks low.
