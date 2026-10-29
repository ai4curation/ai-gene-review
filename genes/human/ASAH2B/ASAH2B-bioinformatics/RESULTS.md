# ASAH2B coverage of the neutral ceramidase ASAH2

`uv run python asah2_coverage.py` does a local BLOSUM62 alignment of ASAH2B (P0C7U1, 165 aa) to the full-length neutral ceramidase ASAH2 (Q9NR71, 780 aa). It then checks each ASAH2 active-site and binding-site residue annotated in the live UniProt entry.

## Output

```
ASAH2 length 780; ASAH2B length 165
Aligned ASAH2 region: 636-780 (145 aligned positions, 137 identical)
Active site  ASAH2 S354 (Nucleophile): outside aligned region
Binding site ASAH2 L134 (Ca(2+)): outside aligned region
Binding site ASAH2 H194 (Zn(2+)): outside aligned region
Binding site ASAH2 H303 (Zn(2+)): outside aligned region
Binding site ASAH2 E540 (Zn(2+)): outside aligned region
Binding site ASAH2 Y579 (Zn(2+)): outside aligned region
Binding site ASAH2 D712 (Ca(2+)): aligned to ASAH2B D97
Binding site ASAH2 S714 (Ca(2+)): aligned to ASAH2B S99
Binding site ASAH2 T717 (Ca(2+)): aligned to ASAH2B T102
```

## Interpretation

ASAH2B corresponds only to the C-terminal ~145 residues of ASAH2 (positions 636-780). It lacks the catalytic nucleophile (S354) and all four zinc-binding residues of the amidase active site. It keeps one C-terminal calcium-binding site. A protein made only of this segment cannot form the neutral ceramidase catalytic site, so ceramidase activity and the downstream ceramide/sphingosine process terms are not supported.
