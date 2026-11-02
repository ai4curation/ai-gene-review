# Scarface (Q7K5M0) catalytic-triad check

Script: `catalytic_triad_check.py` (run with `uv run catalytic_triad_check.py`;
raw output in `catalytic_triad_check.out`). Sequences fetched live from UniProt.

Method: local BLOSUM62 alignment of the Scaf peptidase S1 domain (residues
421-655) and of the active Drosophila CLIP protease Persephone (psh, Q9VWU1,
positive control) to bovine chymotrypsinogen A (P00766), whose positions define
chymotrypsin numbering.

## Result

| Chymotrypsin position | Scaf Q7K5M0 | psh Q9VWU1 (control) |
|---|---|---|
| His57 | S465 (substituted) | H187 (retained) |
| Asp102 | D515 (retained) | D234 (retained) |
| Gly193 (oxyanion hole) | F597 (substituted) | G337 (retained) |
| Ser195 | V599 (substituted) | S339 (retained) |

The His57 motif reads LSSASC in Scaf where active S1 proteases have the
TAAHC motif, so the catalytic histidine is replaced by serine. The GDSGGP motif
around Ser195 is replaced by FDVGSA. The exact Ser195 equivalent depends on the
alignment (Ser601 lies two residues downstream), but the motif is disrupted and
Gly193 is lost; the His57 substitution alone is sufficient to rule out the
canonical charge-relay mechanism. Asp102 is retained.

Conclusion: Scarface retains the S1 fold but lacks the catalytic His and an
intact Ser195/oxyanion-hole motif, consistent with the published description of
Scaf as a serine protease homolog with an inactive catalytic site. This is a
sequence argument; no biochemical assay of Scaf proteolysis has been reported.
