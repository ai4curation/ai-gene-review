# clec-67 (Q8ITX4) CTLD motif inspection

Script: `ctld_motifs.py` (run as `python3 -I ctld_motifs.py ../clec-67-uniprot.txt`).
Input: the cached UniProt flat file; the CTLD boundaries are the PROSITE PS50041 DOMAIN feature (27..144).

## Output

```
length=467 CTLD=27..144
CTLD cysteines (3): [31, 48, 143]
motif EPN in CTLD: False
motif QPD in CTLD: False
motif WND in CTLD: False
total cysteines in protein: 6
```

## Interpretation

The CTLD carries three cysteines rather than the four that form the two canonical CTLD disulfide bonds, consistent with the UniProt PROSITE-ProRule CAUTION that the domain lacks conserved residues required for feature propagation. None of the canonical calcium-dependent sugar-binding motifs (EPN for mannose-type, QPD for galactose-type, WND calcium ligand) is present. The domain therefore cannot be assumed to bind carbohydrate in the classical calcium-dependent manner; carbohydrate binding by clec-67 is untested.

Besides the CTLD, the UniProt record lists only Pfam PF23673 (DUF7154), a domain of unknown function; no catalytic or chaperone-like domain signature (e.g. HSP70, HSP90, small HSP, PDI thioredoxin, calnexin/calreticulin) is listed among its InterPro/Pfam/SMART cross-references.
