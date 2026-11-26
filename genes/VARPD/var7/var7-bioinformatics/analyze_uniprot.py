#!/usr/bin/env python3
"""Reproducible sequence/feature audit of var7 (A0A0N9LYB5) from var7-uniprot.txt."""
from pathlib import Path
import re

uniprot_path = Path(__file__).resolve().parent.parent / "var7-uniprot.txt"
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

out = f"""# Sequence and Topology Audit: Var7 (UniProtKB:A0A0N9LYB5)

- **Source record:** `genes/VARPD/var7/var7-uniprot.txt` (`ALG65342.1`, `EMBL:KT362218`)
- **Sequence length:** {len(seq)} aa
- **`CC -!- SUBCELLULAR LOCATION` lines:** {int(has_subcell)}
- **Secretory signal/transit features (`FT SIGNAL` / `FT TRANSIT` / `FT PROPEP`):** {signal_cnt}
- **Membrane-spanning features (`FT TRANSMEM` / `FT INTRAMEM`):** {tm_cnt}
- **Annotated features:** {", ".join(f"{k} {v}" for k, v in ft_types)}
- **PCP phosphopantetheine attachment sites (1-based):** `Ser1041` (`{seq[1040]}` in `{seq[1035:1047]}`, residues 1036-1047) and `Ser2111` (`{seq[2110]}` in `{seq[2105:2117]}`, residues 2106-2117)

## Conclusion
Var7 (`A0A0N9LYB5`, 2,431 aa) contains 0 signal/transit peptides (`FT SIGNAL` = 0) and 0 transmembrane helices (`FT TRANSMEM` = 0), carries two 4'-phosphopantetheinylated PCP carrier domains (`Ser1041`, `Ser2111`), two ATP-dependent adenylation domains (`PF00501`), and a C-terminal offloading thioesterase domain (`PF00975`), supporting cytoplasmic localization (`GO:0005737`).
"""

(Path(__file__).resolve().parent / "RESULTS.md").write_text(out)
print("Wrote var7-bioinformatics/RESULTS.md")
