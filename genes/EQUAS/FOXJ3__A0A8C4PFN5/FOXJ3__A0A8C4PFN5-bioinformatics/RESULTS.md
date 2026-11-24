# Donkey FOXJ3 (A0A8C4PFN5) versus reviewed mouse and human FOXJ3

Reproduce from this folder with:

    uv run --script compare_orthologs.py ../FOXJ3__A0A8C4PFN5-uniprot.txt mouse-Q8BUR3-uniprot.txt human-Q9UPW0-uniprot.txt > orthologs.json

`mouse-Q8BUR3-uniprot.txt` and `human-Q9UPW0-uniprot.txt` were downloaded from the UniProt REST API on 2026-10-21. Output is in `orthologs.json`. Alignment: Biopython global PairwiseAligner, BLOSUM62, gap open -10, extend -0.5.

## Evolutionary placement

All three proteins carry the same PANTHER subfamily cross-reference, PTHR46078:SF3 (FORKHEAD BOX PROTEIN J3), within family PTHR46078 (FORKHEAD BOX PROTEIN J2 FAMILY MEMBER). FOXJ2 (human Q9P0K8) is a separate subfamily, PTHR46078:SF1. The donkey record is also cross-referenced to CDD cd20052 (FH_FOXJ3) and to InterPro IPR045912 (FOXJ2/3-like).

## Result

| Reference | Length | Aligned positions | Identity (aligned) | Fork-head span (reference) | Fork-head identity |
|---|---|---|---|---|---|
| mouse Q8BUR3 | 623 | 621 | 95.33% | 78-173 | 95/96 |
| human Q9UPW0 | 622 | 622 | 98.23% | 77-168 | 91/92 |

The donkey model is full-length relative to both reviewed orthologs and its fork-head (winged-helix) DNA-binding domain differs from mouse and human at a single position each.

## Interpretation and limits

Same-subfamily membership plus near-identity over the full length, including the DNA-binding domain, supports treating A0A8C4PFN5 as the one-to-one donkey ortholog of mouse and human FOXJ3 and supports transfer of the conserved, domain-intrinsic molecular function (sequence-specific DNA-binding transcription factor). It does not test DNA binding, and sequence conservation alone does not establish that the tissue-level roles found in mouse knockouts (spermatogenesis, muscle fibre type) operate the same way in donkey. No donkey FOXJ3 protein has been studied experimentally.
