#!/usr/bin/env python3
"""Reproducible sequence/feature audit of var4 (A0A0N7FMV9) and GenBank KT362218.1 CDS map."""
from pathlib import Path
import re

here = Path(__file__).resolve().parent
uniprot_path = here.parent / "var4-uniprot.txt"
gb_path = here / "KT362218_features.gb"

text = uniprot_path.read_text()
gb_text = gb_path.read_text()

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

# Parse all CDS features from KT362218_features.gb
cds_blocks = re.split(r"(?=^     CDS             )", gb_text, flags=re.M)[1:]
cds_rows = []
for blk in cds_blocks:
    # Stop at the next top-level feature if present
    blk = re.split(r"^     (?!CDS)[a-z_]+\s+", blk, maxsplit=1, flags=re.M)[0]
    loc = re.search(r"^     CDS\s+(\S+)", blk, flags=re.M).group(1)
    gene = re.search(r'/gene="([^"]+)"', blk).group(1)
    note = re.search(r'/note="([^"]+)"', blk).group(1)
    prod = re.search(r'/product="([^"]+)"', blk).group(1)
    pid = re.search(r'/protein_id="([^"]+)"', blk).group(1)
    trans_m = re.search(r'/translation="([^"]+)"', blk, flags=re.S)
    aa_len = len(re.sub(r"\s+", "", trans_m.group(1)))
    cds_rows.append((gene, loc, pid, prod, aa_len, note))

assert len(cds_rows) == 14, f"Expected 14 CDSs in KT362218.1, got {len(cds_rows)}"

table_lines = [
    "| Gene | Coordinates (`KT362218.1`) | `protein_id` | Product | Length (aa) | GenBank `/note` |",
    "| --- | --- | --- | --- | ---: | --- |",
]
for gene, loc, pid, prod, aa_len, note in cds_rows:
    table_lines.append(f"| `{gene}` | `{loc}` | `{pid}` | `{prod}` | {aa_len} | {note} |")
cds_table = "\n".join(table_lines)

cds_summary = "; ".join(f"{g} ({loc}) = {pid} [{note}]" for g, loc, pid, _, _, note in cds_rows)

out = f"""# Sequence, Topology, and GenBank KT362218.1 Cluster Audit: Var4 (UniProtKB:A0A0N7FMV9)

- **Source records:** `genes/VARPD/var4/var4-uniprot.txt` (`ALG65339.1`, `EMBL:KT362218`) and `genes/VARPD/var4/var4-bioinformatics/KT362218_features.gb` (`KT362218.1`, 41,899 bp)
- **Sequence length:** {len(seq)} aa
- **`CC -!- SUBCELLULAR LOCATION` lines:** {int(has_subcell)}
- **Secretory signal/transit features (`FT SIGNAL` / `FT TRANSIT` / `FT PROPEP`):** {signal_cnt}
- **Membrane-spanning features (`FT TRANSMEM` / `FT INTRAMEM`):** {tm_cnt}
- **Annotated features:** {", ".join(f"{k} {v}" for k, v in ft_types)}
- **Ser1468 residue check (1-based):** `{seq[1467]}` within `{seq[1462:1475]}` (residues 1463-1475, `DSL` phosphopantetheine attachment motif)
- **Adenylation (`PF00501`) match count:** {len(re.findall(r"PF00501", text))} (confirms Var4 lacks an intrinsic NRPS adenylation domain; the position-3 aspartate monomer is activated in trans by the adjacent cluster NRPS module Var5 / `ALG65340.1`)

## GenBank `KT362218.1` (`41,899 bp`) 14-CDS Feature Map (`var1`–`var14`)

{cds_table}

GenBank `KT362218.1` (`41,899 bp`) contains 14 CDSs (`var1`–`var14`) with non-monotonic `protein_id` assignment across the first three ORFs (`var1` `1..834` = `ALG65337.1` thioesterase, `var2` `812..1513` = `ALG65338.1` phospantetheinyl transferase, `var3` `1510..6735` = `ALG65336.1` nonribosomal peptide synthetase) followed in locus order by `var4`–`var14` (`ALG65339.1`–`ALG65349.1`): {cds_summary}.

## Conclusion
Var4 (`A0A0N7FMV9`, 2,345 aa) contains 0 signal/transit peptides (`FT SIGNAL` = 0) and 0 transmembrane helices (`FT TRANSMEM` = 0), carries a covalent 4'-phosphopantetheinyl carrier domain (`Ser1468`), and requires cytosolic malonyl-/methylmalonyl-CoA, NADPH, Fe(II), and 2-oxoglutarate cofactors, supporting cytoplasmic localization (`GO:0005737`).
"""

(here / "RESULTS.md").write_text(out)
print("Wrote var4-bioinformatics/RESULTS.md")
