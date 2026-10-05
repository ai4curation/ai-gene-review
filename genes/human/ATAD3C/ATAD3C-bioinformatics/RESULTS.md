# ATAD3C AAA+ catalytic-residue check

`atad3c_sites.py` aligns human ATAD3C (Q5T2N8) locally to ATAD3A isoform 2 (Q9NVI7-2), the numbering used in PMID:32004445. It reports the ATAD3C residues at the ATAD3A Walker A lysine, the Walker B Asp/Glu and the arginine finger (Arg466), each with a +/-6 window. ATAD3B (Q5T9A4) is run as a positive control. Raw output is in `results.txt`.

## Findings

- ATAD3C aligns to ATAD3A residues 71-584 (365/407 identical), so it lacks the first ~70 residues of ATAD3A.
- **Walker A and Walker B are intact:** ATAD3A K358 aligns to ATAD3C K183, and ATAD3A D411/E412 align to ATAD3C D236/E237, with identical windows (GPPGTGKTLFAKK; GLLLFVDEADAFL).
- **ATAD3A arginine finger R466 aligns to ATAD3C C291.** The window shows no arginine nearby (ATAD3A DWAINDRINEMVH / ATAD3C DWAINACIDVMVH), so the arginine finger is lost, not offset.
- The positive control ATAD3B keeps all four residues, including R466.

## Conclusion

ATAD3C keeps the nucleotide-binding Walker A and B motifs but has lost the trans-acting arginine finger of the AAA+ module, so an ATAD3C subunit cannot complete the ATP site of its neighbour.
