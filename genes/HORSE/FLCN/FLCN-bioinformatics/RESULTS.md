# FLCN (horse, A0A3Q2LPC0): horse-human sequence comparison

Script: `compare_horse_human.py` (run with `uv run --script compare_horse_human.py`). Global alignment
(Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5) of horse A0A3Q2LPC0 (from
`../FLCN-uniprot.txt`) to human Swiss-Prot Q8NFG4 (`human_Q8NFG4-uniprot.txt`, fetched from UniProt REST
on 2026-10-21). Alignment written to `alignment_rereview.txt`.

## Output (verbatim)

```
Horse A0A3Q2LPC0 length: 578; human Q8NFG4 length: 579
Aligned pairs: 578; identical: 548; identity: 94.81%
Coverage of human: 99.83%; coverage of horse: 100.00%
SITE human R164 -> horse R164 (Essential for GTPase activation (GAP) activity)
MUTAGEN human F10 -> horse F10 (F->D: Abolished GTPase activation (GAP) activity.)
MUTAGEN human F118 -> horse F118 (F->D: Does not assemble into a stable folliculin)
MUTAGEN human R164 -> horse R164 (R->A: Abolished GTPase activation (GAP) activity.)
MUTAGEN human S406 -> horse S405 (S->A: Impaired ability to regulate autophagy; when)
MUTAGEN human S537 -> horse S536 (S->A: Impaired ability to regulate autophagy; when)
MUTAGEN human S542 -> horse S541 (S->A: Impaired ability to regulate autophagy; when)
```

## Interpretation

- The horse protein is a full-length FLCN product (578 vs 579 aa, one-residue indel, 100% of horse
  aligned), not a fragment or truncated gene model.
- All experimentally defined human functional residues are conserved: the catalytic GAP arginine (human
  Arg164 = horse Arg164), Phe10 (needed for GAP activity), Phe118 (needed for LFC assembly), and the three
  serines whose combined mutation impairs autophagy regulation (offset by one after the indel).
- Phylogenetic placement: UniProt places the horse protein in PANTHER PTHR31441:SF2 (FOLLICULIN), the same
  subfamily as human FLCN.
  Human Q8NFG4 carries the same assignment ("PTHR31441:SF2; FOLLICULIN" in its UniProt record).
