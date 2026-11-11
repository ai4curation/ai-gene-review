# NADK2 (donkey): comparison of all donkey NADK2 gene models with human NADK2 (re-review, 2026-10-21)

This supplements RESULTS.md (unchanged) and was written for the full re-review.

Reproduce:
`uv run --script genes/EQUAS/NADK2/NADK2-bioinformatics/compare_gene_models_rereview.py genes/EQUAS/NADK2/NADK2-bioinformatics/rereview_sequences A0A9L0K2P4 A0A8C4M4D0 A0A8C4M5G3 F7DCV0`

Raw output: `compare_gene_models_rereview.out`; sequences in `rereview_sequences/`.

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5, each model
against human Q4G0N4 (442 aa). The three donkey entries are all the UniProt entries with gene
NADK2 for taxon 9793 (UniProt REST query, 2026-10-21); all three are transcripts of the same
Ensembl gene ENSEASG00005014681.2. F7DCV0 is a horse NADK2 model, included for comparison only.

## Results

| Accession | Length | Human coverage | Identity | Donkey residue aligned to human Met1 | Human 288-319 aligned | Human S306/K317/W319 |
|---|---|---|---|---|---|---|
| A0A9L0K2P4 (benchmark) | 506 | 92.76% | 96.59% | 97 | 0 of 32 | ABSENT |
| A0A8C4M4D0 | 538 | 100.00% | 96.83% | 97 | 32 of 32 | S402/K413/W415 |
| A0A8C4M5G3 | 560 | 100.00% | 96.83% | 97 | 32 of 32 (after a 22-aa insertion) | S424/K435/W437 |
| F7DCV0 (horse) | 538 | 100.00% | 96.83% | 97 | 32 of 32 | S402/K413/W415 |

All models keep the GGDG motif (human 159-162; donkey 255-258).

## Interpretation

- A0A9L0K2P4 is an alternative-splice gene model of donkey NADK2, equivalent to human isoform 2
  (Q4G0N4-2, VSP_027193, human 288-319 missing). The missing segment (human
  ASYYEISVDDGPWEKQKSSGLNLCTGTGSKAW) contains human Ser306, Lys317 and Trp319, the positions that
  PMID:23212377 maps to the NAD+-binding-site Asp/Thr/Tyr residues of M. tuberculosis Ppnk.
  The benchmark product therefore lacks part of the predicted NAD+-binding region; whether it is
  catalytically active is untested (no isoform 2 activity data exist for human either).
- A0A8C4M4D0 (538 aa) aligns gap-free to the whole human canonical sequence and is the donkey
  product that corresponds to the human canonical isoform. It is the canonical-equivalent product
  of the same gene.
- All three donkey models and the horse model start 96 residues upstream of the Met that aligns to
  human Met1 (donkey Met97). The extension is shared by every equid model, so it reflects a common
  Ensembl start-site choice; whether translation begins there or at Met96/Met97 is not resolved by
  sequence comparison. Either way, the region corresponding to the human transit peptide
  (human 1-62) is internal (donkey 97-158) in these models.
