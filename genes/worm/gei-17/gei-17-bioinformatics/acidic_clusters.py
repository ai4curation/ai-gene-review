"""Map acidic clusters relative to the SP-RING in PIAS1 and GEI-17.

PMID:24036127 maps PIAS1's ligase- and SAP-independent inhibition of IRF3 to
"the C-terminal region of PIAS1 around a cluster of acidic amino acids". This
script asks where acidic clusters sit in each protein relative to the
SP-RING zinc finger and the protein end, using only the cached UniProt
records (sequence plus FT ZN_FING / SUMO1-binding REGION features).

A cluster is a maximal run of overlapping windows of WINDOW residues holding
at least MIN_ACIDIC D/E. Output is a positional description, not an
alignment, and says nothing about function.

Run from the repo root: python genes/worm/gei-17/gei-17-bioinformatics/acidic_clusters.py
"""

from __future__ import annotations

import re
from pathlib import Path

WINDOW = 8
MIN_ACIDIC = 6

RECORDS = {
    "PIAS1 (human, O75925)": Path("genes/human/PIAS1/PIAS1-uniprot.txt"),
    "GEI-17 (C. elegans, Q94361)": Path("genes/worm/gei-17/gei-17-uniprot.txt"),
}


def parse(path: Path) -> tuple[str, list[tuple[str, int, int, str]]]:
    text = path.read_text()
    seq = "".join(re.search(r"^SQ .*?\n(.*?)^//", text, re.S | re.M).group(1).split())
    feats = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (\S+)\s+(\d+)\.\.(\d+)", line)
        if m:
            note = ""
            if i + 1 < len(lines):
                n = re.search(r'/note="([^"]*)', lines[i + 1])
                note = n.group(1) if n else ""
            feats.append((m.group(1), int(m.group(2)), int(m.group(3)), note))
    return seq, feats


def acidic_clusters(seq: str) -> list[tuple[int, int]]:
    hits = [
        i for i in range(len(seq) - WINDOW + 1)
        if sum(c in "DE" for c in seq[i:i + WINDOW]) >= MIN_ACIDIC
    ]
    clusters: list[tuple[int, int]] = []
    for i in hits:
        start, end = i + 1, i + WINDOW
        if clusters and start <= clusters[-1][1] + 1:
            clusters[-1] = (clusters[-1][0], end)
        else:
            clusters.append((start, end))
    return clusters


def main() -> None:
    print(f"cluster definition: >= {MIN_ACIDIC} D/E in any {WINDOW}-residue window\n")
    for name, path in RECORDS.items():
        seq, feats = parse(path)
        ring = next(f for f in feats if f[0] == "ZN_FING" and "SP-RING" in f[3])
        sims = [f for f in feats if f[0] == "REGION" and "SUMO" in f[3]]
        print(f"{name}: length {len(seq)}, SP-RING {ring[1]}-{ring[2]}")
        for f in sims:
            print(f"  annotated {f[3]} region {f[1]}-{f[2]}")
        for s, e in acidic_clusters(seq):
            after_ring = s - ring[2]
            to_end = len(seq) - e
            print(
                f"  acidic cluster {s}-{e} {seq[s - 1:e]}: "
                f"{after_ring:+d} aa from SP-RING end, {to_end} aa before C-terminus"
            )
        print()


if __name__ == "__main__":
    main()
