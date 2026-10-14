"""Check the protein-kinase catalytic residues of ANKK1 (Q8NFD2) against an active control.

For each protein, reads the UniProt flat file and uses its own feature table:
the ATP-binding glycine-rich loop (first BINDING range for ATP), the beta-3 lysine
(single-residue ATP BINDING inside the N-lobe), and the catalytic Asp (ACT_SITE,
"Proton acceptor"). It then reports the catalytic-loop context around the Asp
(the HRD...N motif) and the first DFG within 40 residues downstream.
ANKK1 is read from the cached record; RIPK2 (O43353), an active RIP-family
kinase, is fetched from UniProt as a positive control. It reports what it finds.

Run: uv run python kinase_motif_check.py
"""

import re
import urllib.request
from pathlib import Path

UNIPROT = Path(__file__).resolve().parent.parent / "ANKK1-uniprot.txt"


def read_sequence(text: str) -> str:
    """Sequence from a UniProt flat file.

    >>> read_sequence("ID   X\\nSQ   SEQUENCE\\n     MKV LL\\n//\\n")
    'MKVLL'
    """
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ   "))
    body = []
    for line in lines[start + 1:]:
        if line.startswith("//"):
            break
        body.append(line.replace(" ", ""))
    return "".join(body)


def features(text: str) -> tuple[list[tuple[int, int]], list[int]]:
    """ATP BINDING spans and ACT_SITE positions from a UniProt flat file."""
    lines = text.splitlines()
    atp, act = [], []
    for i, line in enumerate(lines):
        if line.startswith("FT   BINDING") and any('ligand="ATP"' in nxt for nxt in lines[i + 1:i + 3]):
            loc = line.split()[-1]
            a, _, b = loc.partition("..")
            atp.append((int(a), int(b or a)))
        if line.startswith("FT   ACT_SITE"):
            act.append(int(line.split()[-1]))
    return atp, act


def report(name: str, text: str) -> str:
    seq = read_sequence(text)
    atp, act = features(text)
    loop = next((s for s in atp if s[1] > s[0]), None)
    lys = [p for s, e in atp if s == e for p in [s] if seq[p - 1] == "K"]
    asp = act[0]
    cat = seq[asp - 3:asp + 6]
    window = seq[asp:asp + 40]
    m = re.search("DFG", window)
    dfg = f"DFG@{asp + 1 + m.start()}" if m else "no DFG within 40"
    gly = seq[loop[0] - 1:loop[1]] if loop else "n/a"
    return (f"{name}\tgly_loop={gly}\tbeta3_K={','.join(str(p) for p in lys) or 'none'}\t"
            f"catalytic_Asp={seq[asp - 1]}{asp}\tcatalytic_loop={cat}\t{dfg}")


def main() -> None:
    print(report("ANKK1", UNIPROT.read_text()))
    with urllib.request.urlopen("https://rest.uniprot.org/uniprotkb/O43353.txt") as handle:
        print(report("RIPK2_control", handle.read().decode()))


if __name__ == "__main__":
    main()
