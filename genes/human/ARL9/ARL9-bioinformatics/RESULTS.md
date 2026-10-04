# ARL9 G-domain motif check

`uv run python g_motifs.py` aligns ARL9 (Q6T311) and its paralog ARL10 (Q8N8L6) to ARF1 (P84077), using a global BLOSUM62 alignment. It then reports the residues at ARF1's nucleotide-binding and catalytic positions.

## Output

```
## ARL9 (Q6T311) vs ARF1 (P84077)
G1 K30         -> K31
G1 T31         -> T32
switch I T48   -> T50
G3 Q71         -> S73  (differs)
G4 N126        -> N126
G4 K127        -> K127
G4 D129        -> D129

## ARL10 (Q8N8L6) vs ARF1 (P84077)
G1 K30         -> K90
G1 T31         -> S91  (differs)
switch I T48   -> T109
G3 Q71         -> S132  (differs)
G4 N126        -> N185
G4 K127        -> K186
G4 D129        -> D188
```

## Interpretation

- **Retained:** ARL9 keeps the P-loop lysine and threonine, the switch I threonine and the G4 NKxD guanine-specificity motif. Its nucleotide-binding residues are intact.
- **Catalytic glutamine:** At ARF1's catalytic Gln71, ARL9 has a serine (S73), as ARL10 does. Intrinsic GTP hydrolysis by such G proteins is expected to be impaired, but nobody has measured ARL9 hydrolysis.
- **Switch I threonine:** ARL9 retains it (T50). PMID:15033445 says an Asn replaces Thr35 in "all orthologues newly identified here". Its abstract does not make clear whether that applies to the Arl9/Arl10 subfamily or only to Rasl11, and for human ARL9 the alignment does not support it.
