"""Compare A0A6I8TLE4 (AAEL019982-PE) with the other UniProt entries of gene AAEL019982.

Aligns all five TrEMBL products with MAFFT and reports, for each, the length,
the number of target residues aligned, identity over aligned columns, and the
target segments (1-based) that are absent (gapped) in each other product.

Run: uv run --no-project --with requests python compare_isoforms_rereview.py
"""
import subprocess
from pathlib import Path

import requests

HERE = Path(__file__).parent
TARGET = "A0A6I8TLE4"
OTHERS = ["A0A6I8TXX4", "A0A6I8TX88", "A0A6I8TX83", "A0A6I8TXT3"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def read_fasta(text: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    name = None
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = ""
        elif name:
            seqs[name] += line.strip()
    return seqs


def segments(flags: list[bool]) -> list[tuple[int, int]]:
    out, start = [], None
    for i, f in enumerate(flags, 1):
        if f and start is None:
            start = i
        if not f and start is not None:
            out.append((start, i - 1))
            start = None
    if start is not None:
        out.append((start, len(flags)))
    return out


def main() -> None:
    raw = {a: fetch(a) for a in [TARGET, *OTHERS]}
    fa = HERE / "isoforms_rereview_input.fasta"
    fa.write_text("".join(f">{a}\n{s}\n" for a, s in raw.items()))
    out = subprocess.run(["mafft", "--auto", "--quiet", str(fa)],
                         capture_output=True, text=True, check=True).stdout
    aln = read_fasta(out)
    t = aln[TARGET]
    for a in OTHERS:
        s = aln[a]
        missing = [x != "-" and y == "-" for x, y in zip(t, s) if x != "-"]
        cols = [(x, y) for x, y in zip(t, s) if x != "-" and y != "-"]
        ident = sum(x == y for x, y in cols)
        extra = sum(1 for x, y in zip(t, s) if x == "-" and y != "-")
        print(f"{a} len={len(raw[a])} aligned={len(cols)} id={100*ident/len(cols):.1f}% "
              f"target_segments_absent={segments(missing)} other_extra_residues={extra}")


if __name__ == "__main__":
    main()
