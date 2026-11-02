# dpm-1 (Q9TYJ7) sequence and family checks

Script: `analyze_dpm1.py` (run with `uv run --script analyze_dpm1.py`; stdlib only, fetches live from UniProt REST).
Raw output: `results_run.txt` (run 2026-10-21).

## Results

| Accession | Protein | Length | PANTHER | [VI]DDxS motif | MDAD motif | Max 19-res Kyte-Doolittle window |
|---|---|---|---|---|---|---|
| Q9TYJ7 | worm dpm-1 (Y66H1A.2a) | 239 | PTHR43398:SF1 | 41 | 95 | 0.89 at 22 |
| U4PF58 | worm dpm-1 fragment (Y66H1A.2b) | 51 | PTHR43398:SF1 | absent | absent | 0.78 at 32 |
| O60762 | human DPM1 | 260 | PTHR43398:SF1 | 63 | 117 | 1.09 at 241 |
| P14020 | yeast Dpm1 | 267 | PTHR43398:SF1 | 42 | 94 | 2.01 at 244 |

- U4PF58 is an exact substring of Q9TYJ7: True (it is the C-terminal 51 residues of the full-length product).
- Q9TYJ7, human DPM1 and yeast Dpm1 all fall in the same PANTHER subfamily, PTHR43398:SF1.
- Q9TYJ7 retains both acidic motifs (VDDAS at 41, MDAD at 95) that correspond to the conserved aspartates of
  the GT2 glycosyltransferase family described for DPM synthases (Colussi et al. 1997, PMID:9223280).
- Q9TYJ7 has no hydrophobic window above the conventional ~1.6 threshold for a transmembrane helix; yeast Dpm1
  does (2.01 at its C terminus). The worm protein therefore has the human-class architecture (no C-terminal
  membrane anchor), not the S. cerevisiae class.
- worm proteins with DPM2 Pfam PF07297: none found.
- worm proteins with DPM3 Pfam PF08285: Q9XVV5 (dpm-3, F28D1.11, 95 aa).

## Interpretation

The full-length worm DPM-1 is a canonical, intact member of the DPM1 subfamily, with the catalytic acidic
motifs present and a human-like soluble architecture. A DPM3 orthologue exists in C. elegans and could
supply ER-membrane tethering, as DPM3 does for human DPM1. No DPM2 orthologue was detected by Pfam domain
search; this is a negative result from one method, not proof of absence. None of these observations is a
biochemical measurement on the worm protein.
