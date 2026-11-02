# Horse DUSP5 (F7ALT2) vs human DUSP5 (Q16690)

Script: `compare_horse_human.py` (PEP 723; run with `uv run --script compare_horse_human.py`).
Both sequences are fetched live from UniProt REST and aligned globally (Biopython
PairwiseAligner, BLOSUM62, gap open -10, extend -0.5). Raw output: `compare_horse_human.out`.

## Results (as printed by the script)

human Q16690 length 384; horse F7ALT2 length 384
identity 363/384 paired residues = 94.53%
NLS (human 53-74): human RRARGGAVSARYVLPDEAARAR horse RRARGGAVSARYVLPDEAARAR (22/22 identical)
P-loop HCxxGxxRS (human 262-270): human HCEAGISRS horse HCEAGISRS (9/9 identical)
catalytic Cys: human [263] C -> horse [263] C

## Interpretation

F7ALT2 is a full-length DUSP5 product (same length as the human canonical protein, no
gaps), not a fragment or alternative gene model. The catalytic cysteine and the full
HCxxGxxRS P-loop are conserved, as is the 22-residue nuclear localization signal mapped
in human DUSP5. Both proteins are classified by UniProt in PANTHER subfamily
PTHR10159:SF40 (DUAL SPECIFICITY PROTEIN PHOSPHATASE 5), so this is an orthologous
relationship within one subfamily, not a best-hit transfer.
