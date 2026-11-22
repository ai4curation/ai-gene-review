# NCU08595 Rpf2 motif check (re-review, 2026-10-21)

Script: `rpf2_motif_rereview.py` (run with `uv run --script rpf2_motif_rereview.py`).
Sequences fetched live from UniProt REST. Global pairwise alignment, BLOSUM62, gap open -10, extend -0.5.

## Raw output

```
Q7SCN3 length 341
Q7SCN3 (N. crassa NCU08595) length 341; KKR motif starts at [94]
G0SF80 (C. thermophilum Rpf2) length 350; KKR motif starts at [94]
P36160 (S. cerevisiae Rpf2) length 344; KKR motif starts at [94]
Q9H7B2 (H. sapiens RPF2) length 306; KKR motif starts at [97, 285]
Q7SCN3 vs G0SF80: identical aligned residues 252; identity over shorter seq 0.74
Q7SCN3 vs P36160: identical aligned residues 157; identity over shorter seq 0.46
  S. cerevisiae R236 (R) aligns to Q7SCN3 position 242: R
Q7SCN3 vs Q9H7B2: identical aligned residues 135; identity over shorter seq 0.44
```

## Interpretation

Q7SCN3 is full length (341 aa) relative to the PANTHER PTHR12728:SF0 members fetched here
(C. thermophilum 350 aa, S. cerevisiae 344 aa, human 306 aa), so it is not a fragment.
It is 74% identical to the C. thermophilum Rpf2 used for the direct 5S rRNA EMSA in PMID:26117542.
The conserved KKR loop that inserts into 5S rRNA loop E in the A. nidulans structure is present
at the same position (K94-K95-R96) in Q7SCN3, C. thermophilum and S. cerevisiae Rpf2, and the
residue aligned to S. cerevisiae R236 (implicated in 5S rRNA binding, PMID:25855814) is an arginine (R242)
in Q7SCN3. The 5S rRNA-binding residues are therefore retained.
