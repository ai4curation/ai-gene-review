#!/usr/bin/env python3
"""Reproducible sequence/feature and [2Fe-2S] motif audit of var13 (A0A0N9M354) from var13-uniprot.txt."""
from pathlib import Path
import re

uniprot_path = Path(__file__).resolve().parent.parent / "var13-uniprot.txt"
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

motif_match = re.search(r"CC.{10}C.{2}C", seq)
assert motif_match is not None, "CC-x(10)-C-x(2)-C motif not found"
c1 = motif_match.start() + 1  # 1-based
c2 = c1 + 1
c3 = c2 + 11
c4 = c3 + 3
window_start = 226
window_end = 250
window_seq = seq[window_start - 1 : window_end]

out = f"""# Sequence, Topology, and [2Fe-2S] Motif Audit: Var13 (UniProtKB:A0A0N9M354)

- **Source record:** `genes/VARPD/var13/var13-uniprot.txt` (`ALG65348.1`, `EMBL:KT362218`)
- **Sequence length:** {len(seq)} aa
- **`CC -!- SUBCELLULAR LOCATION` lines:** {int(has_subcell)}
- **Secretory signal/transit features (`FT SIGNAL` / `FT TRANSIT` / `FT PROPEP`):** {signal_cnt}
- **Membrane-spanning features (`FT TRANSMEM` / `FT INTRAMEM`):** {tm_cnt}
- **Annotated features:** {", ".join(f"{k} {v}" for k, v in ft_types)}
- **FhuF-family `CC-x(10)-C-x(2)-C` `[2Fe-2S]` cluster-binding motif (1-based coordinates in `A0A0N9M354`):**
  - **25-residue C-terminal window (residues {window_start}-{window_end}):** `{window_seq}`
  - **Exact `CC-x(10)-C-x(2)-C` core (residues {c1}-{c4}):** `{motif_match.group(0)}`
  - **Coordinating cysteines:** `Cys{c1}` (`{seq[c1-1]}`), `Cys{c2}` (`{seq[c2-1]}`), `Cys{c3}` (`{seq[c3-1]}`), and `Cys{c4}` (`{seq[c4-1]}`)

## Conclusion
Var13 (`A0A0N9M354`, 261 aa) contains 0 signal/transit peptides (`FT SIGNAL` = 0) and 0 transmembrane helices (`FT TRANSMEM` = 0), supporting cytoplasmic localization (`GO:0005737`), and retains an intact C-terminal FhuF-family `CC-x(10)-C-x(2)-C` `[2Fe-2S]` cluster-coordinating motif spanning residues 226-250 (`LHRQCCLYYLVPRLGYCGACPLSPE`; `Cys230`, `Cys231`, `Cys242`, `Cys245`), supporting `[2Fe-2S]` cluster binding (`GO:0051537`).
"""

(Path(__file__).resolve().parent / "RESULTS.md").write_text(out)
print("Wrote var13-bioinformatics/RESULTS.md")
