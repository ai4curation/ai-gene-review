# SDF-9 catalytic-residue check

Script: `catalytic_residues.py` (run with `uv run python genes/worm/sdf-9/sdf-9-bioinformatics/catalytic_residues.py`
from the repo root). It reads the SDF-9 (G5EGA9) sequence from `sdf-9-uniprot.txt`, fetches human
PTP1B/PTPN1 (P18031) from UniProt, does a BLOSUM62 local alignment (gap open -10, extend -0.5) of the
PTP1B catalytic region (residues 1-300) against SDF-9, and reports the SDF-9 residue aligned to each PTP1B
landmark. Raw output: `catalytic_residues_output.tsv`.

## Result

| PTP1B residue | Role | SDF-9 residue |
|---|---|---|
| Y46 | pTyr-recognition loop (KNRY) | V37 |
| D48 | pTyr-recognition loop | K39 |
| D181 | WPD-loop general acid | E171 (WPD loop region poorly aligned; low confidence) |
| H214 | P-loop, lowers Cys pKa | Q222 |
| **C215** | **catalytic nucleophile** | **S223** |
| S216 | P-loop | A224 |
| G220 | P-loop | S228 |
| R221 | P-loop phosphate binding | R229 (retained) |
| S222 | P-loop | A230 |
| Q262 | Q-loop | P269 (gapped region; low confidence) |

The signature motif aligns without gaps: PTP1B `HCSAGIGRSG` (214-223) vs SDF-9 `QSARGSSRAG` (222-231).

## Interpretation

- The catalytic cysteine position is **Ser223** in the current SDF-9 sequence. UniProt's CAUTION text
  says "lysine at position 223"; the sequence in `sdf-9-uniprot.txt` has S at 223, so the CAUTION text is
  inaccurate about the identity of the substituting residue (the conclusion, loss of the nucleophile, holds).
- Besides Cys->Ser, SDF-9 also lost the P-loop His (->Gln) and the P-loop Ser/Thr (->Ala) and the
  pTyr-recognition Tyr46 (->Val). Loss of multiple catalytic and substrate-recognition residues supports a
  catalytically dead pseudophosphatase.
- The P-loop arginine (R229) is retained, so a residual phosphate/anion-binding pocket is possible, but the
  pTyr-recognition loop is degenerate; there is no sequence-level basis to assert phosphotyrosine binding.
- Limitation: pairwise alignment to a single PTP; WPD- and Q-loop assignments fall in gapped regions and are
  low confidence. The P-loop assignment is unambiguous.
