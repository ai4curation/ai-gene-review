# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare horse ENTR1 (A0A5F5Q1J2) with characterized human (Q96C92) and mouse (A2AIW0) ENTR1.

Fetches sequences and PANTHER cross-references from UniProt REST, performs global
alignments (BLOSUM62, gap open -10, extend -0.5), and reports identity, coverage and
the alignment of the first-sequence N-terminal region 1-100 (basal-body / IFT88-binding region,
PMID:27767179). The two other horse ENTR1
TrEMBL models (F6QT44, A0A3Q2H8N2) are compared to the target as well. Writes results.json and alignments next to this script.
"""
import json
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
ACCS = {
    "horse": "A0A5F5Q1J2",
    "human": "Q96C92",
    "mouse": "A2AIW0",
    "horse_F6QT44": "F6QT44",
    "horse_A0A3Q2H8N2": "A0A3Q2H8N2",
}


def fetch(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    d = r.json()
    panther = [
        x["id"]
        for x in d.get("uniProtKBCrossReferences", [])
        if x["database"] == "PANTHER"
    ]
    return {"acc": acc, "seq": d["sequence"]["value"], "panther": panther}


def align(a: str, b: str):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al.align(a, b)[0]


def stats(aln, a: str, b: str) -> dict:
    ident = 0
    paired = 0
    pairs = []  # (i_a, i_b) 0-based
    for (sa, ea), (sb, eb) in zip(*aln.aligned):
        for k in range(ea - sa):
            paired += 1
            pairs.append((int(sa + k), int(sb + k)))
            if a[sa + k] == b[sb + k]:
                ident += 1
    return {
        "paired": paired,
        "identical": ident,
        "identity_over_paired_pct": round(100 * ident / paired, 2),
        "coverage_of_first_pct": round(100 * paired / len(a), 2),
        "coverage_of_second_pct": round(100 * paired / len(b), 2),
        "pairs": pairs,
    }


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    out = {k: {"acc": v["acc"], "length": len(v["seq"]), "panther": v["panther"]} for k, v in seqs.items()}
    for other in ("human", "mouse", "horse_F6QT44", "horse_A0A3Q2H8N2"):
        a, b = seqs[other]["seq"], seqs["horse"]["seq"]
        aln = align(a, b)
        s = stats(aln, a, b)
        pairs = s.pop("pairs")
        nterm = [(i, j) for i, j in pairs if i < 100]
        nterm_id = sum(1 for i, j in nterm if a[i] == b[j])
        s["nterm_1_100_paired"] = len(nterm)
        s["nterm_1_100_identical"] = nterm_id
        s["nterm_1_100_horse_span"] = (
            [nterm[0][1] + 1, nterm[-1][1] + 1] if nterm else None
        )
        out[f"{other}_vs_horse"] = s
        (HERE / f"alignment_{other}_vs_horse.txt").write_text(str(aln))
    (HERE / "results.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
