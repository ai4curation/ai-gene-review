"""Scan S. pombe Cbl1 (O94350) for peroxisomal targeting signals.

PTS1: C-terminal tripeptide matching [SAC][KRH][LM] (canonical consensus).
PTS2: (R/K)(L/V/I/Q)x2(L/V/I/H/Q)(L/S/G/A/K)x(H/Q)(L/A/F) within the first 40 residues
(the extended PTS2 nonapeptide consensus). Reads the cached UniProt flat file.
Run from the repository root:
    python genes/SCHPO/cbl1/cbl1-bioinformatics/targeting_signals.py
"""
import re
from pathlib import Path

text = Path("genes/SCHPO/cbl1/cbl1-uniprot.txt").read_text()
seq = "".join(c for c in text.split("\nSQ")[1].split("\n", 1)[1] if c.isalpha())
print(f"length {len(seq)}; C-terminal 12 residues: {seq[-12:]}")
pts1 = re.fullmatch(r"[SAC][KRH][LM]", seq[-3:])
print(f"PTS1 consensus at C-terminus ({seq[-3:]}): {'yes' if pts1 else 'no'}")
hits = [m.start() + 1 for m in re.finditer(r"(?=[RK][LVIQ]..[LVIHQ][LSGAK].[HQ][LAF])", seq[:40])]
print(f"PTS2-like motifs in residues 1-40: {hits if hits else 'none'}")
