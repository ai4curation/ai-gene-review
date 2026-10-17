# IPT1 (YDR072C) notes

UniProt P38954, M(IP)2C synthase (inositolphosphotransferase 1; EC 2.7.1.228), AUR1-family multipass Golgi membrane protein [UniProt:P38954].

- [PMID:9368028 "we show that a homolog (open reading frame YDR072c), termed Ipt1 (inositolphosphotransferase 1) is necessary for synthesis of mannose-(inositol-P)2-ceramide (M(IP)2C), the most abundant and complex sphingolipid in S. cerevisiae"]; membranes from ipt1 lack M(IP)2C synthase activity [PMID:9368028 "membranes prepared from it do not incorporate [3H-inositol]phosphatidylinositol into M(IP)2C"].
- Membrane activity transferring PI-inositol phosphate to sphingolipid [PMID:6991492].
- Golgi (EXP, PMID:14583628; abstract only mentions Csg1/Csh1 co-localising with IPC synthase in medial Golgi; deferred to curator).
- With SKN1, required for M(IP)2C and DmAMP1 sensitivity [PMID:15792805 "These results show that SKN1, together with IPT1, is involved in sphingolipid biosynthesis in S. cerevisiae."]; ipt1 skn1 double mutant has increased autophagy [PMID:20030721].

## GO term gap
- No GO MF for MIPC + PI -> M(IP)2C + DAG (EC 2.7.1.228, RHEA:64540). Existing rows use "transferase activity, transferring phosphorus-containing groups". Proposed new term.
- Note: GO:0045140 (IPC synthase, Aur1) is placed is_a GO:0016758 hexosyltransferase activity, which is chemically wrong (it is a phosphoinositol transfer) - ontology issue relevant to AUR1/IPT1.

## Pathway context
- YeastPathways reaction for IPT1 (MIPC + PI -> M(IP)2C) correct. RCA cytosol wrong (Golgi membrane enzyme).
- IBA "inositol phosphoceramide synthase complex" propagated from Aur1 (Aur1-Kei1) to its paralog Ipt1: not supported.
