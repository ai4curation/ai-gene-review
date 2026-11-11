# D3VIU4 re-review: placement among family-3 cystine-binding proteins

Script: `compare_sequences_rereview.py` (MAFFT L-INS-i; sequences from UniProt REST).
Raw output: `rereview_output.txt`; alignment: `rereview_aln.fa`.

## Subfamily placement (UniProt PANTHER cross-references, PANTHER 19 entries file)

- D3VIU4 (XNC1_0570) is PTHR35936:SF34 (ABC TRANSPORTER EXTRACELLULAR-BINDING PROTEIN YCKB-RELATED), CDD cd13711 (PBP2_Ngo0372_TcyA).
- The same subfamily holds Bacillus subtilis TcyA (P42199, L-cystine uptake system TcyABC) and YckB (P42400), and the Xenorhabdus paralog XNC1_0574 (D3VIU8).
- E. coli TcyJ/FliY (P0AEM9, the experimentally characterised high-affinity cystine binding protein) is in a different subfamily, PTHR35936:SF35, with CDD cd13712. Neisseria gonorrhoeae Ngo0372 (Q5F9M1, L-cystine-bound crystal structure, Kd 21 nM) is also SF35 in UniProt.
- Xenorhabdus nematophila ATCC 19061 has no SF35 member; its PTHR35936 proteins are D3VIU4 and D3VIU8 (SF34), ArtI D3VBG0 (SF20) and MltF D3VLL0 (SF32).

## Gene neighbourhood

XNC1_0570 (D3VIU4, SBP) is followed by XNC1_0571 (D3VIU5, yecC, ABC ATPase, PTHR43166) and XNC1_0572 (D3VIU6, yecS, "L-cystine transport system permease protein TcyL", PTHR30614), the same SBP-ATPase-permease arrangement as the E. coli fliY(tcyJ)-yecC(tcyN)-yecS(tcyL) cluster. XNC1_0574 (D3VIU8, second SF34 SBP) lies just downstream of yecS, separated by XNC1_0573 (D3VIU7, uncharacterized).

## Pairwise identity (% over mutually ungapped columns)

| | D3VIU4 |
|---|---|
| D3VIU8 (Xenorhabdus paralog, SF34) | 57 |
| P42199 B. subtilis TcyA (SF34) | 48 |
| Q5F9M1 N. gonorrhoeae Ngo0372 (SF35) | 48 |
| P45024 H. influenzae HI_1080 (SF35) | 44 |
| P0AEM9 E. coli TcyJ/FliY (SF35) | 39 |
| P42400 B. subtilis YckB (SF34) | 34 |
| O34406 B. subtilis TcyJ (SF18) | 25 |
| P39906 D. nodosus AabA (SF35) | 27 |

D3VIU4 is not closer to E. coli TcyJ than to the other cystine binders; its nearest characterised relatives are TcyA (same subfamily) and Ngo0372.

## Binding-pocket residues

Ngo0372 Tyr58 and Trp96 (UniProt SV2 numbering; Tyr59/Trp97 in PMID:22138345, where Tyr59 is crucial for L-cystine binding) align to D3VIU4 Tyr49 and Trp87. Both are conserved in TcyA, E. coli TcyJ and D3VIU8, but not in YckB (Leu/Ile) or B. subtilis TcyJ (Phe/Phe).

## Interpretation

L-cystine binding is shared by cystine-binding proteins in both SF34 (TcyA) and SF35 (TcyJ, Ngo0372), and D3VIU4 keeps the two pocket residues tested in Ngo0372 and sits in a conserved tcyJ-tcyN-tcyL-type operon. L-cystine-binding SBP function is therefore a reasonable inference, but it rests on subfamily membership with TcyA, conserved pocket residues and synteny, not on orthology to E. coli FliY. Exact ligand specificity (cystine vs other sulfur amino acids such as cystathionine or djenkolate), and which of D3VIU4/D3VIU8 serves the YecSC-type permease, have not been tested.
