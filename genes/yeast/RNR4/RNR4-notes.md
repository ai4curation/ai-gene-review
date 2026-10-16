# RNR4 (P49723) notes

Module: `dntp_de_novo_synthesis`, role = inactive small-subunit partner (fungal Rnr4 type).

## Evidence journal
- Catalytically inactive, lacks iron ligands, tyrosine dispensable [PMID:9315671 "Rnr4p lacks a number of sequence elements thought to be essential for iron binding, and mutation of the critical tyrosine residue does not affect Rnr4p function."]
- Folds/stabilises Rnr2 [PMID:10716984 "we demonstrate that the crucial role of Rnr4p (beta') is to fold correctly and stabilize the radical-storing Rnr2p by forming a stable 1:1 Rnr2p/Rnr4p complex."]; no iron [PMID:10716984 "No iron was detected in Rnr4p."]
- In vivo requirement for cofactor [PMID:16285741 "The Y* content of rnr4delta is 15-fold less than that of wt"]
- RNR2 and RNR4 not interchangeable [PMID:9315670 "RNR4 and RNR2 appear to have nonoverlapping functions and cannot substitute for each other even when overproduced."]
- Nuclear anchoring by Wtm1 [PMID:18851834 "We previously reported that Wtm1 anchors Rnr2-Rnr4 in the nucleus."]

## Annotation decisions
- GO:0004748 rows with 'enables' (IEA, IGI, IMP) ACCEPTed, noting that 'contributes_to' is more accurate for this non-catalytic subunit.
- Oxidoreductase activity IEA (IPR012348): REMOVE (pseudoenzyme over-annotation).
- 17 protein binding rows: MODIFY to GO:0046982 for small-scale Rnr2 data; REMOVE others (Rnr1, Wtm1/Wtm2, high-throughput).
- GO:0106387 RCA: REMOVE.
