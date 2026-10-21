"""Compare the A0A494B8X4 Sdhaf2 product with canonical mouse Q8C6I2 and human Q9NX18.

Reads the A0A494B8X4 sequence from the local UniProt flat file, fetches the reviewed
Swiss-Prot sequences and Pfam PF03937 (Sdh5) coordinates from UniProt / InterPro REST,
and reports the shared prefix, the divergent tail and which domain segment is retained.
Standard library only. Run: python3 compare_products.py
"""

import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
FLAT = HERE.parent / "Sdhaf2-uniprot.txt"


def flatfile_sequence(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ   "))
    seq_lines = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq_lines.append(line.replace(" ", ""))
    return "".join(seq_lines)


def fetch_fasta(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
        text = r.read().decode()
    return "".join(text.splitlines()[1:])


def pfam_spans(acc: str) -> list[tuple[str, int, int]]:
    url = f"https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/{acc}"
    with urllib.request.urlopen(url) as r:
        data = json.load(r)
    spans = []
    for res in data["results"]:
        for prot in res["proteins"]:
            for loc in prot["entry_protein_locations"]:
                for frag in loc["fragments"]:
                    spans.append((res["metadata"]["accession"], frag["start"], frag["end"]))
    return spans


def shared_prefix(a: str, b: str) -> int:
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return n


def main() -> None:
    target = flatfile_sequence(FLAT)
    mouse = fetch_fasta("Q8C6I2")
    human = fetch_fasta("Q9NX18")
    prefix = shared_prefix(target, mouse)
    tail = target[prefix:]
    lost = mouse[prefix:]
    print(f"Selected A0A494B8X4 has {len(target)} residues; reference Q8C6I2 has {len(mouse)} residues.")
    print(f"Identical prefix: residues 1-{prefix} of both sequences.")
    print(f"A0A494B8X4 divergent tail ({len(tail)} aa, residues {prefix + 1}-{len(target)}): {tail}")
    print(f"Q8C6I2 residues absent from A0A494B8X4 ({len(lost)} aa, {prefix + 1}-{len(mouse)}): {lost}")
    print(f"Tail occurs in Q8C6I2: {tail in mouse}; in Q9NX18: {tail in human}")
    for acc in ("Q8C6I2", "A0A494B8X4", "Q9NX18"):
        for name, s, e in pfam_spans(acc):
            print(f"{acc} {name} {s}-{e}")
    motif = "RGMLE"
    print(f"RGxxE motif ({motif}) at Q8C6I2 {mouse.find(motif) + 1}, "
          f"A0A494B8X4 {target.find(motif) + 1}, Q9NX18 {human.find(motif) + 1} (1-based start)")
    hprefix = human.find(mouse[30:60])
    print(f"Q8C6I2 31-60 aligns to Q9NX18 starting at {hprefix + 1} (human offset {hprefix - 30:+d})")


if __name__ == "__main__":
    main()
