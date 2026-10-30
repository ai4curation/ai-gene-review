# CG3515 (Q9VQD1) SWD2-family paralog comparison (re-review, 2026-10-20)

Script: `compare_swd2_paralogs_rereview.py` (raw output in `compare_swd2_paralogs_rereview.out`).
Sequences fetched live from UniProt REST; global alignment with BLOSUM62, gap open -10, extend -0.5;
identity = identical / aligned (non-gap) positions.

| Pair | Identity |
|------|----------|
| CG3515 vs fly Wdr82 (Q9VLN1) | 0.364 (115/316) |
| CG3515 vs human WDR82 (Q6UXN9) | 0.347 (108/311) |
| CG3515 vs yeast Swd2 (P36104) | 0.295 (90/305) |
| fly Wdr82 vs human WDR82 | 0.693 (217/313) |
| fly Wdr82 vs yeast Swd2 | 0.396 (118/298) |
| human WDR82 vs yeast Swd2 | 0.389 (114/293) |

Lengths: CG3515 395 aa; fly Wdr82 317 aa; human WDR82 313 aa; yeast Swd2 329 aa.

## Interpretation

Fly Wdr82 (CG17293) and human WDR82 are 69% identical, so Wdr82 is the conserved, slowly evolving
WDR82 ortholog in Drosophila. CG3515 is only about 35% identical to either, less similar to the
animal WDR82 proteins than fly Wdr82 is to yeast Swd2. CG3515 is therefore a rapidly diverging
paralog within the Swd2/WDR82 family (PANTHER PTHR19861:SF0, which also contains Wdr82 and human
WDR82), and it carries a C-terminal extension of about 80 residues absent from the other members.
Pairwise identities do not establish when the duplication occurred; a tree with other insect
genomes would be needed for that. Retention of the WD40 fold does not by itself show retention of
the Set1/COMPASS or RNA polymerase II CTD-binding surfaces.
