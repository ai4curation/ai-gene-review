# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Map human SDHAF2 (Q9NX18) structural features onto mouse Sdhaf2 products.

Fetches live UniProt entries for the mouse canonical product (Q8C6I2), the
benchmark alternative product (A0A494B8X4) and human SDHAF2 (Q9NX18), aligns
each mouse product to human, and reports which human HELIX / VARIANT features
and Pfam PF03937 residues are retained in each mouse product.

Run: uv run --script map_structure_rereview.py > RESULTS-rereview-raw.txt
"""
import json

import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.json"
INTERPRO = "https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/{}"


def entry(acc: str) -> dict:
    r = requests.get(UNIPROT.format(acc), timeout=60)
    r.raise_for_status()
    return r.json()


def pfam_spans(acc: str) -> list[tuple[str, int, int]]:
    r = requests.get(INTERPRO.format(acc), timeout=60)
    r.raise_for_status()
    out = []
    for res in r.json()["results"]:
        for p in res["proteins"]:
            for loc in p["entry_protein_locations"]:
                for f in loc["fragments"]:
                    out.append((res["metadata"]["accession"], f["start"], f["end"]))
    return out


def residue_map(a: str, b: str) -> dict[int, tuple[int, bool]]:
    """Map 1-based positions in a to (position in b, identical) via global alignment."""
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    m: dict[int, tuple[int, bool]] = {}
    for (sa, ea), (sb, eb) in zip(*aln.aligned):
        for i, j in zip(range(sa, ea), range(sb, eb)):
            m[i + 1] = (j + 1, a[i] == b[j])
    return m


def main() -> None:
    human = entry("Q9NX18")
    hseq = human["sequence"]["value"]
    feats = [
        (f["type"], f["location"]["start"]["value"], f["location"]["end"]["value"],
         f.get("description", ""))
        for f in human["features"]
        if f["type"] in ("Helix", "Natural variant", "Transit peptide")
    ]
    print(f"Human Q9NX18 length {len(hseq)}")
    for acc in ("Q8C6I2", "A0A494B8X4"):
        mseq = entry(acc)["sequence"]["value"]
        hm = residue_map(hseq, mseq)
        print(f"\n## {acc} (length {len(mseq)}); Pfam spans: {pfam_spans(acc)}")
        print("| Human feature | Human interval | Mouse mapped interval | Mapped / length | Identical |")
        print("|---|---|---|---|---|")
        for ftype, s, e, desc in feats:
            mapped = [hm[i] for i in range(s, e + 1) if i in hm]
            ident = sum(1 for _, same in mapped if same)
            interval = f"{mapped[0][0]}-{mapped[-1][0]}" if mapped else "none"
            label = ftype if not desc else f"{ftype} ({desc[:40]})"
            print(f"| {label} | {s}-{e} | {interval} | {len(mapped)} / {e - s + 1} | {ident} |")
    print("\n" + json.dumps({"human_features": feats}))


if __name__ == "__main__":
    main()
