# Tbc1d4 (rat, D3Z881) TBC-domain catalytic motif check

Script: `tbc_motifs.py` (run as `python3 -I tbc_motifs.py ../Tbc1d4-uniprot.txt`).

Output (not hand-edited):

```
sequence length: 1245
TBC domain (FT DOMAIN, PS50086): (865, 1059)
arginine finger IxxDxxR: motif ILVDLGR at 913-919; catalytic residue R919
glutamine finger YxQ: motif YCQ at 954-956; catalytic residue Q956
```

Interpretation: both catalytic fingers of the TBC Rab-GAP domain (the dual-finger
mechanism; arginine finger in the IxxDxxR motif and glutamine finger in the YxQ motif)
are present in rat Tbc1d4. Mutation of the corresponding catalytic arginine to lysine
abolishes the GAP activity of human AS160 (PMID:15971998), so rat Tbc1d4 is predicted
to be a catalytically competent Rab GAP, not a pseudo-GAP.
