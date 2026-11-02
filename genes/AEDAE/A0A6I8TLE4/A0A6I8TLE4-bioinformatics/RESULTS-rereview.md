# A0A6I8TLE4 re-review bioinformatics (2026-10-21)

Independent of any ProtNLM2 output. Two reproducible scripts in this folder:

- `compare_rasgap_rereview.py` (output: `rasgap_rereview_output.txt`, alignment
  `rasgap_rereview_aln.fasta`): MAFFT L-INS-i alignment of A0A6I8TLE4 with nine
  PTHR10194 members from five subfamilies.
- `compare_isoforms_rereview.py` (output: `isoforms_rereview_output.txt`):
  MAFFT alignment of A0A6I8TLE4 with the other four UniProt entries of gene
  AAEL019982.

## 1. Placement and nearest relatives

UniProt assigns A0A6I8TLE4 to PANTHER PTHR10194:SF60 (RAS GTPASE-ACTIVATING
PROTEIN RASKOL). The subfamily members in the local PANTHER entry list are
Drosophila raskol (Q8T498), C. elegans gap-2 (Q8MLZ5), S. cerevisiae BUD2
(P33314), C. albicans BUD2 (Q5A506) and Dictyostelium ngap (Q54Y08). Human
DAB2IP (SF26), RASAL2/nGAP (SF52) and SYNGAP1 (SF25) are separate subfamilies.

Identity over aligned columns:

| comparator | subfamily | % identity |
|---|---|---|
| raskol (Q8T498, Drosophila) | SF60 | 61.2 |
| gap-2 (Q8MLZ5, C. elegans) | SF60 | 34.2 |
| RASAL2 (Q9UJF2, human) | SF52 | 33.6 |
| DAB2IP (Q5VWQ8, human) | SF26 | 33.1 |
| SYNGAP1 (Q96PV0, human) | SF25 | 30.8 |
| RASA1 (P20936, human) | SF146 | 24.0 |
| ngap (Q54Y08, Dictyostelium) | SF60 | 22.7 |
| BUD2 (P33314, yeast) | SF60 | 19.6 |
| NF1 (P21359, human) | SF142 | 18.1 |

Interpretation: Drosophila raskol is by far the closest relative and shares the
PANTHER subfamily, so it is the dipteran ortholog. Within SF60 the fungal and
amoebal members are no closer to the mosquito protein than the human
DAB2IP/RASAL2/SYNGAP1 paralog subfamilies are, so SF60 is a heterogeneous
subfamily and substrate preferences of BUD2 (a GAP for the Rap-like Bud1/Rsr1)
should not be transferred specifically.

## 2. Catalytic arginine finger

The column of the p120GAP (RASA1) arginine finger R789 aligns to an arginine in
every sequence. In A0A6I8TLE4 it is R483, in the motif TFRGNS, identical to
raskol (R515, TFRGNS) and matching NF1 R1276 (LFRGNS). The catalytic arginine
finger of the RasGAP domain is conserved in A0A6I8TLE4.

## 3. Isoform status

Gene AAEL019982 (NCBI Gene 5579847) has five unreviewed UniProt entries; none is
Swiss-Prot reviewed:

| entry | transcripts | length | relation to A0A6I8TLE4 |
|---|---|---|---|
| A0A6I8TLE4 | RE | 1442 | benchmark |
| A0A6I8TXX4 | RH, RI | 1609 | 94.2% id; differs in N-terminal residues 43-130; 187 extra residues |
| A0A6I8TX88 | RG | 1431 | 100% id; lacks target residues 64-74 |
| A0A6I8TX83 | RA, RB, RC, RF | 1381 | 96.3% id; lacks target N-terminal segments within 1-106 |
| A0A6I8TXT3 | RD | 1376 | 96.2% id; lacks target N-terminal segments within 1-106 |

InterPro locations on A0A6I8TLE4 (InterPro API, 2026-10-21): SynGAP-like PH
domain IPR057606 157-267 (SMART PH match IPR001849 17-270), C2 IPR000008
259-378, RasGAP domain IPR001936 391-735 (conserved site IPR023152 588-602),
DAB2P_C IPR021887 1357-1421.

All isoform differences lie within the first ~130 residues: inside the
N-terminal extension of the broad SMART PH match but upstream of the Pfam
SynGAP-like PH core (157-267), the C2 domain, the RasGAP domain (with the R483
arginine finger) and the DAB2P_C region. A0A6I8TLE4 is therefore one
alternative splice product of AAEL019982 that carries the complete domain
architecture; it is not a fragment and lacks no catalytic residues.
