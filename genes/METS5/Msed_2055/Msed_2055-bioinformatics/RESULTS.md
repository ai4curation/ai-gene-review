# Msed_2055 (A4YIE3) B12-binding motif scan

Script: `motif_scan.py` (stdlib Python), run as
`python3 -I motif_scan.py ../Msed_2055-uniprot.txt > motif_scan.out`.
It reads the sequence from the UniProt flat file and reports 1-based regex matches.

Output (`motif_scan.out`):

```
length	155
DXHXXG	31:DGHDRG
SXL	78:SIL, 142:SKL
GG	108:GG
candidate_axial_His	H33
```

Interpretation: the single DXHXXG match (D31-G36, DGHDRG) lies in the PROSITE
B12-binding domain (residues 20-148), with SIL at 78 and GG at 108 downstream in the
spacing of the class I B12-binding Rossmann fold (SXL ~ 40-45 and GG ~ 70-80 residues
after the His). This matches the DXHXXG-SXL-GG motif reported for M. sedula MCM-beta by
Han et al. 2012. His33 is the candidate lower axial ligand to cobalt (base-off/His-on
binding). SKL at 142 is a second, C-terminal SXL match and is not considered part of
the motif. Motif assignment is by pattern and spacing only; no structure was modelled.
