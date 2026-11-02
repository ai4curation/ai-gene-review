# SEC23A (horse, A0A3Q2H5Z6): sequence comparison to human SEC23A and SEC23B

Script: `compare_to_human.py` (run with `uv run --script compare_to_human.py`). It fetches the
sequences from UniProt REST and performs a global BLOSUM62 alignment (gap open -10, extend -0.5).

## Output (2026-10-21)

```
human SEC23A Q15436: horse_len=765 ref_len=765 identical=760 identity_vs_ref=0.993 gap_columns=0
  substitutions (human pos, horse residue): ['S97T', 'L104M', 'L211V', 'D317E', 'S588P']
  human Cys in 56-100: [61, 66, 74, 85, 88]  horse at same: ['C61', 'C66', 'C74', 'C85', 'C88']
human SEC23B Q15437: horse_len=765 ref_len=767 identical=651 identity_vs_ref=0.849 gap_columns=2
```

## Interpretation

- A0A3Q2H5Z6 is a full-length SEC23A product: 765 aa, the same length as human SEC23A (Q15436),
  gap-free alignment, 760/765 identical residues (99.3%) with five conservative or surface
  substitutions. It is not a fragment or an alternative gene model.
- It is far closer to SEC23A than to the paralog SEC23B (85% identity), consistent with UniProt's
  PANTHER assignment PTHR11141:SF7 (PROTEIN TRANSPORT PROTEIN SEC23A), the same subfamily as human,
  mouse, bovine, Xenopus and zebrafish SEC23A in `interpro/panther/PTHR11141/PTHR11141-entries.csv`.
- All cysteines of the Sec23/Sec24-type zinc-finger region (human 56-100) are conserved, and the
  UniProt record carries all five Sec23 Pfam domains (zinc finger, trunk, beta-sandwich, helical,
  gelsolin-like).
- Horse retains F382 (the residue mutated F382L in cranio-lenticulo-sutural dysplasia in human SEC23A); no substitution lies between human positions 317 and 588.
