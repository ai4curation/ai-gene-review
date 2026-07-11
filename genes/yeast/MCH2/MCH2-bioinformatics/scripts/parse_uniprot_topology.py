#!/usr/bin/env python3
"""Parse TRANSMEM / TOPO_DOM features from a UniProt flat (.txt) file.

Reports the number and boundaries of annotated transmembrane helices and their
evidence codes. Runs on any UniProt .txt file (path passed as argument).

Usage:
    python parse_uniprot_topology.py --uniprot ../MCH2-uniprot.txt \
        --out results/uniprot_topology.tsv
"""
import argparse
import re
from pathlib import Path


def parse_features(path: Path) -> dict:
    text = path.read_text().splitlines()
    transmem = []
    topo = []
    current = None  # ('TRANSMEM'|'TOPO_DOM', start, end, note, evidence)
    for line in text:
        m = re.match(r"^FT\s+(TRANSMEM|TOPO_DOM)\s+(\d+)\.\.(\d+)", line)
        if m:
            if current:
                (transmem if current[0] == "TRANSMEM" else topo).append(current)
            current = [m.group(1), int(m.group(2)), int(m.group(3)), "", ""]
            continue
        if current:
            note = re.match(r'^FT\s+/note="([^"]*)"', line)
            if note:
                current[3] = note.group(1)
            ev = re.match(r'^FT\s+/evidence="([^"]*)"', line)
            if ev:
                current[4] = ev.group(1)
            # a new FT of a different type or CHAIN etc ends current only when a new feature starts (handled above)
            if re.match(r"^FT\s+[A-Z_]+\s+\d", line) and not re.match(
                r"^FT\s+(TRANSMEM|TOPO_DOM)", line
            ):
                (transmem if current[0] == "TRANSMEM" else topo).append(current)
                current = None
    if current:
        (transmem if current[0] == "TRANSMEM" else topo).append(current)
    return {"transmem": transmem, "topo": topo}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--uniprot", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    feats = parse_features(args.uniprot)
    tm = feats["transmem"]
    topo = feats["topo"]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w") as fh:
        fh.write("feature\tstart\tend\tlength\tnote\tevidence\n")
        for f in tm + topo:
            fh.write(f"{f[0]}\t{f[1]}\t{f[2]}\t{f[2] - f[1] + 1}\t{f[3]}\t{f[4]}\n")

    n_term = topo[0][3] if topo else "?"
    c_term = topo[-1][3] if topo else "?"
    print(f"Annotated TRANSMEM helices: {len(tm)}")
    print(f"N-terminus topology: {n_term}")
    print(f"C-terminus topology: {c_term}")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
