# Cacnb3 (P54285) ortholog/paralog grounding

Script: `compare_orthologs.py` (run with `uv run --no-project --with biopython --with requests python compare_orthologs.py`).
Raw output: `results_table.md`.

## Method

- PANTHER subfamily membership read from the release-pinned PANTHER 19.0 classification files (`.cache/panther/PTHR19.0_*`).
- Global pairwise alignment (Needleman-Wunsch, BLOSUM62, gap open -10, extend -0.5) of mouse P54285 against each protein, sequences fetched from UniProt REST at run time; identity is reported as identical aligned positions / length of the shorter sequence.

## Results

| accession | species | gene | length | PANTHER 19.0 subfamily | identity to P54285 (% of shorter) |
|---|---|---|---|---|---|
| P54285 | mouse | Cacnb3 | 484 | PTHR11824:SF8 (VOLTAGE-DEPENDENT L-TYPE CALCIUM CHANNEL SUBUNIT BETA-3) | 100.0 |
| P54284 | human | CACNB3 | 484 | PTHR11824:SF8 (VOLTAGE-DEPENDENT L-TYPE CALCIUM CHANNEL SUBUNIT BETA-3) | 99.2 |
| P54287 | rat | Cacnb3 | 484 | PTHR11824:SF8 (VOLTAGE-DEPENDENT L-TYPE CALCIUM CHANNEL SUBUNIT BETA-3) | 99.2 |
| Q8R3Z5 | mouse | Cacnb1 | 597 | PTHR11824:SF17 (VOLTAGE-DEPENDENT L-TYPE CALCIUM CHANNEL SUBUNIT BETA-1) | 64.7 |
| Q8CC27 | mouse | Cacnb2 | 655 | PTHR11824:SF9 (VOLTAGE-DEPENDENT L-TYPE CALCIUM CHANNEL SUBUNIT BETA-2) | 67.4 |
| Q8R0S4 | mouse | Cacnb4 | 519 | PTHR11824:SF7 (VOLTAGE-DEPENDENT L-TYPE CALCIUM CHANNEL SUBUNIT BETA-4) | 69.0 |

## Interpretation

Mouse Cacnb3 (P54285), human CACNB3 (P54284) and rat Cacnb3 (P54287, the donor for the ISS rows and the RGD source for the ISO rows) all fall in PANTHER subfamily PTHR11824:SF8 (beta-3) and are 99.2% identical over their full 484-residue length. This is the subfamily-level relationship needed to transfer beta3-specific experimental findings between these three species.
The mouse beta1, beta2 and beta4 paralogs sit in separate subfamilies (SF17, SF9, SF7) at about 65-69% identity. Paralog-specific properties, such as CaMKII binding to beta1b/beta2a, should not be transferred to beta3.
