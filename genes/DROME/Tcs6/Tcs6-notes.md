# Tcs6 (E1JIY8) review notes

## Identity
- Pcc1/LAGE3 ortholog, CTAG/Pcc1 family (PANTHER PTHR31283:SF5), 111 aa; KEOPS dimerization subunit.

## Literature
- No fly-specific experimental papers. KEOPS reviews:
  [PMID:25629598 "Archaea and Eukarya use the KEOPS complex composed of Tcs3 (Kae1), Tcs5 (Bud32), Tcs6 (Pcc1) and Tcs7 (Cgi121) proteins"]
  [PMID:34614169 "Pcc1 has homo-dimerization capabilities"]
  [PMID:34614169 "As a result, t6A is essential for the fidelity of translation and for the functionality of ANN-decoding tRNAs"]

## Decisions
- Core: contributes_to GO:0061711, in KEOPS, cytoplasm (same as Tcs5).
- ND root MF MODIFY to GO:0061711 (contributes_to); ND CC/BP REMOVE as superseded.
- PR #4482 review: UniProt lists obsolete GO:0070525 IBA (replaced_by GO:0002949), absent from GOA. Yeast PCC1 carries GO:0002949; human LAGE3 does not. Added NEW GO:0002949 (ISS) and put it in core_functions.

## Deep research (falcon) additions
- [file:DROME/Tcs6/Tcs6-deep-research-falcon.md "Expressing fly **Pcc1 together with fly Kae1** in *yeast kae1* mutants improved growth and recovery of t⁶A-modified tRNAs compared with fly Kae1 alone"]
- Reports Tcs6 RNAi (Rojas-Benitez et al. 2017, Biomolecules) gives small, developmentally delayed larvae; not in GOA, not added (no fly t6A measurement for Tcs6). No change to decisions.
