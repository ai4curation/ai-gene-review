"""Verify (rather than assume) that AGFG1 and AGFG2 are paralogues.

The shared name is not evidence. Three independent lines are checked and each is
reported with its own number:
  1. shared PANTHER family / distinct subfamily (from the UniProt DR lines);
  2. identical InterPro domain-signature set (from the InterPro API);
  3. pairwise sequence identity, computed - full length and ArfGAP domain only,
     because a 562/481-aa pair with a conserved 125-aa domain and long
     low-complexity tails will give very different numbers for the two, and
     quoting only the full-length figure understates the relationship.

A control pair is included so that a low number cannot be read as "unrelated"
without a scale: ARFGAP1 vs ARFGAP3 are an accepted paralogue pair in a
different ArfGAP subfamily, and ARFGAP1 vs ACTB is a negative control.

Usage: uv run python paralogy.py
"""

from __future__ import annotations

import json
import pathlib
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

OUT = pathlib.Path(__file__).parent / "paralogy.json"

# (accession, label, ArfGAP domain start, end) - domain bounds from the InterPro
# IPR001164 match positions, printed by the InterPro query in the notes.
ENTRIES = {
    "P52594": ("AGFG1 human", 11, 135),
    "O95081": ("AGFG2 human", 27, 153),
    "Q8N6T3": ("ARFGAP1 human", 7, 124),
    "Q9NP61": ("ARFGAP3 human", 10, 126),
    "P60709": ("ACTB human (negative control)", None, None),
}

PAIRS = [
    ("P52594", "O95081", "subject vs paralogue"),
    ("Q8N6T3", "Q9NP61", "control: accepted ArfGAP paralogue pair"),
    ("P52594", "Q8N6T3", "cross-subfamily ArfGAP"),
    ("P52594", "P60709", "negative control (unrelated protein)"),
]


def fetch(acc: str) -> tuple[str, list[str], list[str]]:
    url = (
        f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        "?fields=accession,sequence,xref_panther,xref_interpro"
    )
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        d = json.load(fh)
    assert d["primaryAccession"] == acc, f"{acc} -> {d['primaryAccession']}"
    panther, interpro = [], []
    for x in d.get("uniProtKBCrossReferences", []):
        if x["database"] == "PANTHER":
            panther.append(x["id"])
        elif x["database"] == "InterPro":
            interpro.append(x["id"])
    return d["sequence"]["value"], sorted(panther), sorted(interpro)


def identity(a: str, b: str) -> dict:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aln = aligner.align(a, b)[0]
    s1, s2 = aln[0], aln[1]
    assert len(s1) == len(s2)
    aligned_cols = sum(1 for x, y in zip(s1, s2) if x != "-" and y != "-")
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    return {
        "aligned_columns": aligned_cols,
        "identities": ident,
        "pct_identity_over_aligned": round(100 * ident / aligned_cols, 1),
        "pct_identity_over_shorter": round(100 * ident / min(len(a), len(b)), 1),
        "len_a": len(a),
        "len_b": len(b),
    }


def main() -> None:
    data = {}
    for acc, (label, s, e) in ENTRIES.items():
        seq, panther, interpro = fetch(acc)
        data[acc] = {
            "label": label,
            "length": len(seq),
            "panther": panther,
            "interpro": interpro,
            "seq": seq,
            "domain": (s, e),
        }
        print(f"{acc} {label:34s} len={len(seq):5d} PANTHER={panther} InterPro={interpro}")

    a, b = data["P52594"], data["O95081"]
    fam_a = {p for p in a["panther"] if ":" not in p}
    fam_b = {p for p in b["panther"] if ":" not in p}
    shared_family = sorted(fam_a & fam_b)
    sub_a = sorted(p for p in a["panther"] if ":" in p)
    sub_b = sorted(p for p in b["panther"] if ":" in p)
    print("\n1) PANTHER")
    print(f"   shared family: {shared_family}")
    print(f"   subfamilies:   AGFG1 {sub_a} vs AGFG2 {sub_b}")
    assert shared_family, "no shared PANTHER family - paralogy NOT supported"
    assert sub_a != sub_b, "same subfamily - would make them closer than paralogues"

    print("\n2) InterPro signature sets")
    print(f"   AGFG1: {a['interpro']}")
    print(f"   AGFG2: {b['interpro']}")
    print(f"   identical: {a['interpro'] == b['interpro']}")

    print("\n3) pairwise identity")
    results = {}
    for x, y, label in PAIRS:
        full = identity(data[x]["seq"], data[y]["seq"])
        row = {"label": label, "full_length": full}
        dx, dy = data[x]["domain"], data[y]["domain"]
        if all(v is not None for v in (*dx, *dy)):
            dom = identity(
                data[x]["seq"][dx[0] - 1 : dx[1]], data[y]["seq"][dy[0] - 1 : dy[1]]
            )
            row["arfgap_domain"] = dom
        results[f"{x}|{y}"] = row
        dom_txt = (
            f"  ArfGAP domain {row['arfgap_domain']['pct_identity_over_aligned']}%"
            if "arfgap_domain" in row
            else "  (no domain bounds)"
        )
        print(
            f"   {data[x]['label']} vs {data[y]['label']:34s} "
            f"full-length {full['pct_identity_over_aligned']}%{dom_txt}   [{label}]"
        )

    subj = results["P52594|O95081"]
    ctrl = results["Q8N6T3|Q9NP61"]
    neg = results["P52594|P60709"]
    assert (
        subj["arfgap_domain"]["pct_identity_over_aligned"]
        > neg["full_length"]["pct_identity_over_aligned"]
    ), "subject pair scores no better than the negative control"
    print(
        "\nscale check: the AGFG1/AGFG2 ArfGAP-domain identity "
        f"({subj['arfgap_domain']['pct_identity_over_aligned']}%) sits against an "
        f"accepted paralogue pair at "
        f"{ctrl['arfgap_domain']['pct_identity_over_aligned']}% and an unrelated "
        f"protein at {neg['full_length']['pct_identity_over_aligned']}%"
    )

    for v in data.values():
        v.pop("seq")
    OUT.write_text(
        json.dumps({"entries": data, "pairs": results}, indent=2, sort_keys=True) + "\n"
    )
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
