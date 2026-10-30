# Tgt (Q9VPY8; CG4947) review notes

## Identity
- Ortholog of human QTRT1, catalytic subunit of eukaryotic tRNA-guanine transglycosylase (TGT).
  [file:DROME/Tgt/Tgt-uniprot.txt "Catalytic subunit of the queuine tRNA-ribosyltransferase"];
  reaction [file:DROME/Tgt/Tgt-uniprot.txt "Reaction=guanosine(34) in tRNA + queuine = queuosine(34) in tRNA +"].
- PANTHER PTHR43530:SF1 "QUEUINE TRNA-RIBOSYLTRANSFERASE CATALYTIC SUBUNIT 1"; partner is the
  accessory subunit CG3434 (QTRT2 ortholog, PTHR46064).
- Animals cannot make queuine; it is salvaged from diet/microbiota and inserted by QTRT1-QTRT2
  into G34 of tRNA-Asp, -Asn, -His, -Tyr (GUN anticodons). Background from orthologs.

## Literature
- No Drosophila TGT paper is cited in GOA; all annotations are IEA/IBA/ISS (mouse/human QTRT1).
- Mammalian QTRT1 has been reported at the cytoplasmic side of the mitochondrial outer membrane
  (source of the ISS location row); kept as non-core.

## Decisions
- Accept transglycosylase activity, wobble guanine modification, cytoplasm, TGT complex.
- tRNA modification (InterPro): non-core parent.

## Deep research (falcon)
- Fly studies (Zaborske et al. 2014; Guo et al. 2025) show Q-tRNA exists and is nutrient/developmentally regulated in Drosophila, but do not test Tgt itself: [file:DROME/Tgt/Tgt-deep-research-falcon.md "human and mouse studies establish the detailed chemistry of the corresponding catalytic enzyme"].
