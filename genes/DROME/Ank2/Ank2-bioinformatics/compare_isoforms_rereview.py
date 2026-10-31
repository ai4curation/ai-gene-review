"""Map the Ank2-PE product (Q3KN55) onto giant Ank2 isoforms.

Fetches sequences from the UniProt REST API and reports exact shared blocks
(difflib longest matching blocks, >20 residues) between Q3KN55 and other
Ank2 gene products, plus the PROSITE ANK repeat coordinates of Q3KN55.

Run: python3 compare_isoforms_rereview.py
"""

import json
import urllib.request
from difflib import SequenceMatcher

TARGET = "Q3KN55"  # Ank2-PE, 697 aa
OTHERS = {
    "M9MRX4": "Ank2 isoform U (UniProt gene-centric canonical)",
    "Q7KU92": "Ank2 isoform L (Ank2-L)",
    "M9PBV0": "Ank2 isoform X (short)",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def main() -> None:
    target = fetch(TARGET)
    print(f"{TARGET} length {len(target)}")
    giant_blocks = []
    for acc, label in OTHERS.items():
        seq = fetch(acc)
        sm = SequenceMatcher(None, target, seq, autojunk=False)
        blocks = [b for b in sm.get_matching_blocks() if b.size > 20]
        print(f"{acc} ({label}) length {len(seq)}")
        for b in blocks:
            print(
                f"  identical block: {TARGET} {b.a + 1}-{b.a + b.size} == "
                f"{acc} {b.b + 1}-{b.b + b.size} ({b.size} aa)"
            )
        covered = sum(b.size for b in blocks)
        print(f"  fraction of {acc} covered by {TARGET}: {covered / len(seq):.3f}")
        if acc == "Q7KU92":
            giant_blocks = blocks
        repeats = ank_repeats(acc)
        shared = [r for r in repeats if blocks and blocks[0].b < r[0] and r[1] <= blocks[0].b + blocks[0].size]
        print(f"  {acc} ANK repeats (UniProt features): {len(repeats)}; "
              f"fully inside the block shared with {TARGET}: {len(shared)}")
    first, last = giant_blocks[0], giant_blocks[-1]
    end = last.a + last.size
    print(f"{TARGET} sequence not shared with Ank2-L: 1-{first.a} and {end + 1}-{len(target)}")
    print(f"{TARGET} C-terminal tail not shared with Ank2-L: {target[end:]}")


def ank_repeats(acc: str) -> list[tuple[int, int]]:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=ft_repeat"
    with urllib.request.urlopen(url) as fh:
        data = json.load(fh)
    out = []
    for ft in data.get("features", []):
        if ft["type"] == "Repeat" and ft.get("description", "").startswith("ANK"):
            out.append((ft["location"]["start"]["value"], ft["location"]["end"]["value"]))
    return sorted(out)


if __name__ == "__main__":
    main()
