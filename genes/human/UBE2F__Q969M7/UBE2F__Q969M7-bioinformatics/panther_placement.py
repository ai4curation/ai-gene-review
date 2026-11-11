"""Evolutionary grounding for UBE2F (Q969M7).

1. Query the PANTHER geneinfo API for the PANTHER family/subfamily of human
   UBE2F and of the experimentally characterised NEDD8 E2s (UBE2M, yeast UBC12).
2. Read the PAINT IBD rows for node PTN000630367 from the local PANTHER cache.
3. Confirm the catalytic Cys (position 116) and N-terminal Met in the UniProt
   sequence.

Run: uv run python panther_placement.py   (from this folder)
"""

import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

QUERIES = [
    ("Q969M7", "9606", "human UBE2F"),
    ("P61081", "9606", "human UBE2M"),
    ("Q9CY34", "10090", "mouse Ube2f"),
    ("P61082", "10090", "mouse Ube2m"),
    ("P52491", "559292", "yeast UBC12"),
]


def panther_geneinfo(acc: str, taxon: str) -> dict:
    url = (
        "https://www.pantherdb.org/services/oai/pantherdb/geneinfo"
        f"?geneInputList={acc}&organism={taxon}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=60) as fh:
        data = json.load(fh)
    gene = data["search"]["mapped_genes"]["gene"]
    return {
        "family_id": gene.get("family_id"),
        "family_name": gene.get("family_name"),
        "sf_id": gene.get("sf_id"),
        "sf_name": gene.get("sf_name"),
    }


def paint_rows(node: str) -> list[list[str]]:
    paint = REPO / "interpro/panther/PTHR24067/PTHR24067-paint.tsv"
    return [
        line.split("\t")
        for line in paint.read_text().splitlines()
        if f"\t{node}\t" in line
    ]


def uniprot_sequence(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ "))
    seq = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    print("## PANTHER placement (live PANTHER geneinfo API)")
    for acc, taxon, label in QUERIES:
        info = panther_geneinfo(acc, taxon)
        print(f"{label}\t{acc}\t{info['family_id']}\t{info['sf_id']}\t{info['sf_name']}")

    print("\n## PAINT rows for PANTHER:PTN000630367 (local PTHR24067 cache)")
    for row in paint_rows("PTN000630367"):
        print("\t".join(row[1:8]))

    seq = uniprot_sequence(HERE.parent / "UBE2F__Q969M7-uniprot.txt")
    print("\n## Sequence checks")
    print(f"length={len(seq)}")
    print(f"residue_1={seq[0]}")
    print(f"residue_116={seq[115]} context={seq[110:121]}")


if __name__ == "__main__":
    main()
