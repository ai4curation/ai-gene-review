# CC2D2A (horse, A0A5F5PUW7): orthology and conservation check

Script: `compare_orthologs.py` (run with `uv run compare_orthologs.py`); raw output in `compare_orthologs.out`.

## Question

Is horse A0A5F5PUW7 the full-length 1:1 ortholog of the experimentally characterised human and mouse
CC2D2A proteins, and not the CC2D2B paralog, so that the PAINT (PTN000464650) and Ensembl Compara
transfers apply to it?

## Phylogenetic placement

- UniProt A0A5F5PUW7 carries the PANTHER cross-references PTHR20837 (CENTROSOMAL PROTEIN-RELATED) and
  PTHR20837:SF7 (COILED-COIL AND C2 DOMAIN-CONTAINING PROTEIN 2A), the same subfamily as human CC2D2A
  (Q9P2K1) and mouse Cc2d2a (Q8CFW7). Human CC2D2B (Q6DHV5) is in a separate subfamily, SF2
  (`interpro/panther/PTHR20837/PTHR20837-entries.csv`).
- The PAINT IBDs for this family (`interpro/panther/PTHR20837/PTHR20837-paint.tsv`) sit at one node,
  PTN000464650 (taxon Eukaryota): ciliary transition zone (GO:0035869), protein localization to ciliary
  transition zone (GO:1904491) and non-motile cilium assembly (GO:1905515). The horse protein receives all
  three as IBA rows, so it lies below that node.

## Pairwise alignments (global, BLOSUM62, gap open -10, extend -0.5)

| Comparison | Length | Identical / aligned pairs |
|---|---|---|
| human CC2D2A Q9P2K1 (SF7) | 1620 | 1440/1619 (88.9%) |
| mouse Cc2d2a Q8CFW7 (SF7) | 1633 | 1376/1618 (85.0%) |
| human CC2D2B Q6DHV5 (SF2) | 1437 | 592/1400 (42.3%) |
| horse A0A5F5PJ44 (second model of the same gene) | 1480 | 1480/1480 (100.0%) |

Horse A0A5F5PUW7 (1643 aa) aligns end to end with human CC2D2A, with ~89% identity, and is much less
similar to CC2D2B (42%), consistent with the SF7 assignment. The other horse model, A0A5F5PJ44, is an
identical 1480-residue sub-sequence of A0A5F5PUW7. A0A5F5PUW7 is therefore the full-length,
gene-centric product of horse CC2D2A (Ensembl ENSECAG00000025115).

## Domain conservation (human UniProt features mapped to horse)

- C2 domain, human 1025-1203 -> horse 1048-1226; 160/179 identical (89.4%). The horse record's own
  SMART C2 prediction is at 1065-1225.
- Coiled coil, human 439-493 -> horse 462-516; 78.2% identical.
- Coiled coil, human 532-582 -> horse 555-605; 82.4% identical.

The horse record also carries the InterPro/Pfam CC2D2AN-C2, CEP76_C and CEPT76/DRC7 peptidase-like (TGL)
signatures and the tectonic-like complex component family (IPR052434), the same architecture as human
CC2D2A.

## Disease-variant positions

Of 26 human missense variants that UniProt associates with MKS6, JBTS9, COACH2 or RP93, 25 are at
residues conserved in horse. The exception, human E1447A, is at a conservative Asp in horse (D1470).
The positions that are functionally sensitive in human are thus preserved in horse.

## Conclusion

Horse A0A5F5PUW7 is the full-length 1:1 ortholog of human and mouse CC2D2A, in the same PANTHER subfamily
(SF7) and below the PAINT node that carries the transition-zone terms. Nothing in the sequence suggests a
loss or divergence of function. This supports transferring the mammalian experimental findings to it.
The analysis is sequence-only: it establishes the evolutionary basis for transfer, not any experimental
result in horse.
