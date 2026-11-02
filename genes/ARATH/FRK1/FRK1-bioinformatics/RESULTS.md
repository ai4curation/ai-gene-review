# FRK1 (O64483) kinase-domain catalytic motif check

Script: `kinase_motifs.py` (reads `../FRK1-uniprot.txt`; no dependencies).

Output:

```
sequence length 876; kinase domain 574-847
Gly-rich loop GxGxxG: GKGGFG at 581-586
beta3 lysine (VAIK-like): VAVK at 598-601
alphaC glutamate region (E within helix): FRAEV at 614-618
catalytic loop HRD: HRDVKPTN at 695-702
activation loop DFG: DFG at 715-717
```

Interpretation: all canonical catalytic motifs of a eukaryotic protein kinase are intact
(glycine-rich loop, VAIK lysine K601, alphaC glutamate E617, HRD catalytic loop with
catalytic Asp697, and DFG Asp715). FRK1 is therefore an RD-type kinase predicted to be
catalytically competent, i.e. not a pseudokinase. This is a sequence-level prediction only;
no in vitro kinase activity of FRK1 has been published.
