"""Compare the two UniProt records for Acinetobacter baylyi ADP1 vanA.

Fetches Q6FDI6 (genome-project entry, reference proteome UP000000430) and
O24841 (the 1999 submission, EMBL AAC27107.1) from the UniProt REST API, aligns
them position by position (both are 358 aa, so no gaps are introduced; a
length difference is reported rather than aligned), and writes results.json and
RESULTS.md next to this script. Standard library only.
"""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

ACCESSIONS = ("Q6FDI6", "O24841")
HERE = Path(__file__).resolve().parent


def fetch(accession: str) -> dict:
    """Return the UniProt JSON record for an accession."""
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    with urllib.request.urlopen(url, timeout=60) as handle:
        return json.load(handle)


def main() -> None:
    """Fetch both records, compare sequences and write the result files."""
    records = {acc: fetch(acc) for acc in ACCESSIONS}
    seqs = {acc: rec["sequence"]["value"] for acc, rec in records.items()}
    a, b = (seqs[acc] for acc in ACCESSIONS)
    result: dict = {
        acc: {
            "length": len(seqs[acc]),
            "uniparc": rec.get("extraAttributes", {}).get("uniParcId"),
            "proteomes": [
                x["id"]
                for x in rec.get("uniProtKBCrossReferences", [])
                if x.get("database") == "Proteomes"
            ],
        }
        for acc, rec in records.items()
    }
    if len(a) == len(b):
        diffs = [
            {"position": i + 1, ACCESSIONS[0]: x, ACCESSIONS[1]: y}
            for i, (x, y) in enumerate(zip(a, b))
            if x != y
        ]
        identity = 100.0 * (len(a) - len(diffs)) / len(a)
        result["ungapped_comparison"] = {
            "differences": diffs,
            "n_differences": len(diffs),
            "percent_identity": round(identity, 1),
        }
    else:
        result["ungapped_comparison"] = None
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n")

    lines = ["# ADP1 vanA record comparison (Q6FDI6 vs O24841)", ""]
    for acc in ACCESSIONS:
        r = result[acc]
        lines.append(
            f"- {acc}: {r['length']} aa, UniParc {r['uniparc']}, "
            f"reference proteomes: {', '.join(r['proteomes']) or 'none'}"
        )
    cmp_ = result["ungapped_comparison"]
    lines.append("")
    if cmp_ is None:
        lines.append("The records differ in length; no ungapped comparison was made.")
    else:
        lines.append(
            f"Ungapped comparison: {cmp_['n_differences']} differing positions, "
            f"{cmp_['percent_identity']}% identity."
        )
        lines.append("")
        lines.append("| position | Q6FDI6 | O24841 |")
        lines.append("|---|---|---|")
        for d in cmp_["differences"]:
            lines.append(f"| {d['position']} | {d['Q6FDI6']} | {d['O24841']} |")
    (HERE / "RESULTS.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
