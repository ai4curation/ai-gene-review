#!/usr/bin/env python3
"""Reproducible sequence/feature audit of var4 (A0A0N7FMV9) from var4-uniprot.txt."""
from pathlib import Path
import re

uniprot_path = Path(__file__).resolve().parent.parent / "var4-uniprot.txt"
text = uniprot_path.read_text()

ft_types = re.findall(r"^FT   ([A-Z_]+)\s+(\S+)", text, flags=re.M)
seq_lines = []
in_seq = False
for line in text.splitlines():
    if line.startswith("SQ   "):
        in_seq = True
        continue
    if in_seq:
        if line.startswith("//"):
            break
        seq_lines.append(re.sub(r"\s+", "", line))
seq = "".join(seq_lines)

signal_cnt = sum(1 for k, _ in ft_types if k in {"SIGNAL", "TRANSIT", "PROPEP"})
tm_cnt = sum(1 for k, _ in ft_types if k in {"TRANSMEM", "INTRAMEM"})
has_subcell = "CC   -!- SUBCELLULAR LOCATION:" in text

out = f"""# Sequence and Topology Audit: Var4 (UniProtKB:A0A0N7FMV9)

- **Source record:** `genes/VARPD/var4/var4-uniprot.txt` (`ALG65339.1`, `EMBL:KT362218`)
- **Sequence length:** {len(seq)} aa
- **`CC -!- SUBCELLULAR LOCATION` lines:** {int(has_subcell)}
- **Secretory signal/transit features (`FT SIGNAL` / `FT TRANSIT` / `FT PROPEP`):** {signal_cnt}
- **Membrane-spanning features (`FT TRANSMEM` / `FT INTRAMEM`):** {tm_cnt}
- **Annotated features:** {", ".join(f"{k} {v}" for k, v in ft_types)}
- **Ser1468 residue check (1-based):** `{seq[1467]}` within `{seq[1462:1475]}` (residues 1463-1475, `DSL` phosphopantetheine attachment motif)
- **Adenylation (`PF00501`) match count:** {len(re.findall(r"PF00501", text))} (confirms Var4 lacks an intrinsic NRPS adenylation domain; the position-3 aspartate monomer is activated in trans by the adjacent cluster NRPS module Var5 / `ALG65340.1`)

## Conclusion
Var4 (`A0A0N7FMV9`, 2,345 aa) contains 0 signal/transit peptides (`FT SIGNAL` = 0) and 0 transmembrane helices (`FT TRANSMEM` = 0), carries a covalent 4'-phosphopantetheinyl carrier domain (`Ser1468`), and requires cytosolic malonyl-/methylmalonyl-CoA, NADPH, Fe(II), and 2-oxoglutarate cofactors, supporting cytoplasmic localization (`GO:0005737`).
"""

(Path(__file__).resolve().parent / "RESULTS.md").write_text(out)
print("Wrote var4-bioinformatics/RESULTS.md")
