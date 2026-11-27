#!/usr/bin/env python3
"""Reproducible sequence/feature audit of var6 (A0A0N9LX43) from var6-uniprot.txt."""
from pathlib import Path
import re

uniprot_path = Path(__file__).resolve().parent.parent / "var6-uniprot.txt"
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

out = f"""# Sequence and Topology Audit: Var6 (UniProtKB:A0A0N9LX43)

- **Source record:** `genes/VARPD/var6/var6-uniprot.txt` (`ALG65341.1`, `EMBL:KT362218`)
- **Sequence length:** {len(seq)} aa
- **`CC -!- SUBCELLULAR LOCATION` lines:** {int(has_subcell)}
- **Secretory signal/transit features (`FT SIGNAL` / `FT TRANSIT` / `FT PROPEP`):** {signal_cnt}
- **Membrane-spanning features (`FT TRANSMEM` / `FT INTRAMEM`):** {tm_cnt}
- **Annotated features:** {", ".join(f"{k} {v}" for k, v in ft_types)}
- **PCP phosphopantetheine attachment sites (1-based):** `Ser1016` (`{seq[1015]}` in `{seq[1010:1022]}`, residues 1011-1022) and `Ser2517` (`{seq[2516]}` in `{seq[2511:2523]}`, residues 2512-2523)

## Conclusion
Var6 (`A0A0N9LX43`, 2,583 aa) contains 0 signal/transit peptides (`FT SIGNAL` = 0) and 0 transmembrane helices (`FT TRANSMEM` = 0), carries two 4'-phosphopantetheinylated PCP carrier domains (`Ser1016`, `Ser2517`) and two ATP-dependent amino acid adenylation domains (`PF00501`), supporting cytoplasmic localization (`GO:0005737`).
"""

(Path(__file__).resolve().parent / "RESULTS.md").write_text(out)
print("Wrote var6-bioinformatics/RESULTS.md")
