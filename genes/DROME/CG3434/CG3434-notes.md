# CG3434 (Q9VSZ6) review notes

## Identity
- Ortholog of human QTRT2 (QTRTD1), the non-catalytic accessory subunit of eukaryotic TGT.
  [file:DROME/CG3434/CG3434-uniprot.txt "Non-catalytic subunit of the queuine tRNA-ribosyltransferase"];
  [file:DROME/CG3434/CG3434-uniprot.txt "Heterodimer of a catalytic subunit and an accessory subunit."]
- PANTHER PTHR46064 "QUEUINE TRNA-RIBOSYLTRANSFERASE ACCESSORY SUBUNIT 2"; partner is Tgt (QTRT1).
- QTRT2 retains the TGT fold and zinc site but lacks the catalytic residues; it contributes to
  the heterodimeric enzyme (tRNA binding/positioning) rather than catalysing the exchange.

## Literature
- No Drosophila study of CG3434 in GOA; annotations are IEA/ISS.

## Decisions
- IEA "enables tRNA-guanosine(34) queuine transglycosylase activity" (UniRule): REMOVE, as the
  accessory subunit does not catalyse the reaction (enables qualifier wrong for a non-catalytic
  subunit; activity belongs to Tgt; core function uses contributes_to).
- Accept wobble guanine modification, TGT complex, cytoplasm. Mito outer membrane ISS: non-core.

## Deep research (falcon)
- Supports non-catalytic role of QTRT2 orthologs: [file:DROME/CG3434/CG3434-deep-research-falcon.md "QTRT2 has a degenerate catalytic/substrate-binding site"].
