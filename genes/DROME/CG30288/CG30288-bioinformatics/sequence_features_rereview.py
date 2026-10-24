"""Re-review sequence checks for CG30288 (Q8IRK6), using only the cached UniProt record.

Reports: sequence length, residues at the PROSITE-ProRule active-site positions,
the S1-pocket residue at chymotrypsinogen position 189 (located 6 residues
N-terminal of the catalytic Ser195 in the conserved C191-x-G193-D194-S195 segment),
the predicted zymogen activation site (the residue preceding the start of the
Peptidase S1 domain's conserved I/V-x-G-G N-terminus), cysteine positions, and
length of the propeptide between the signal peptide and the protease domain
(too short to contain a ~40-residue clip domain if well under 40).

Run: python3 sequence_features_rereview.py ../CG30288-uniprot.txt
"""

import re
import sys
from pathlib import Path


def parse(path: Path) -> tuple[str, dict[str, list[tuple[int, int]]]]:
    text = path.read_text()
    seq = "".join(text.split("\nSQ   ")[1].split("\n", 1)[1].replace("//", "").split())
    feats: dict[str, list[tuple[int, int]]] = {}
    for m in re.finditer(r"^FT   (\w+)\s+(\d+)(?:\.\.(\d+))?", text, re.M):
        start = int(m.group(2))
        end = int(m.group(3) or m.group(2))
        feats.setdefault(m.group(1), []).append((start, end))
    return seq, feats


def main(path: str) -> None:
    seq, feats = parse(Path(path))
    print(f"length\t{len(seq)}")
    for start, _ in feats.get("ACT_SITE", []):
        print(f"act_site\t{start}\t{seq[start - 1]}\tcontext={seq[start - 6:start + 5]}")
    ser = [s for s, _ in feats.get("ACT_SITE", []) if seq[s - 1] == "S"]
    if ser:
        s195 = ser[0]
        seg = seq[s195 - 7 : s195 + 3]
        print(f"ser195_segment\t{s195 - 6}-{s195 + 3}\t{seg}")
        p189 = s195 - 6
        print(f"S1_pocket_pos189\t{p189}\t{seq[p189 - 1]}")
    sig_end = feats["SIGNAL"][0][1]
    dom_start = feats["DOMAIN"][0][0]
    m = re.search(r"[IV].GG", seq[dom_start - 4 : dom_start + 6])
    if m:
        new_n = dom_start - 4 + m.start() + 1
        print(f"activation_site\t{new_n - 1}-{new_n}\t{seq[new_n - 2]}-|-{seq[new_n - 1:new_n + 3]}")
    print(f"propeptide\t{sig_end + 1}-{dom_start - 1}\tlength={dom_start - 1 - sig_end}\t{seq[sig_end:dom_start - 1]}")
    cys = [i + 1 for i, c in enumerate(seq) if c == "C"]
    print(f"cysteines\t{','.join(map(str, cys))}")


if __name__ == "__main__":
    main(sys.argv[1])
