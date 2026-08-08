"""Compare the GOA records of AGFG1 (P52594) and its paralogue AGFG2 (O95081).

Answers the two questions the paralogue cross-check exists for:
  1. which GO terms reach BOTH genes from the same PANTHER node (a term
     propagated to both from a donor that may only support one of them), and
  2. which of AGFG1's rows name AGFG2 (or vice versa) in WITH/FROM, i.e. rows
     whose only support is the sibling.

Usage: uv run python paralog_goa.py
"""

from __future__ import annotations

import json
import pathlib

import quickgo

PAIR = {"P52594": "AGFG1", "O95081": "AGFG2"}
OUT = pathlib.Path(__file__).parent / "paralog_goa.json"


def collect(acc: str) -> list[dict]:
    rows = quickgo.annotations(geneProductId=f"UniProtKB:{acc}", limit=100)
    out = []
    for r in rows:
        out.append(
            {
                "go_id": r["goId"],
                "go_name": r["goName"],
                "aspect": r["goAspect"],
                "evidence": r["goEvidence"],
                "qualifier": r["qualifier"],
                "reference": r["reference"],
                "assigned_by": r["assignedBy"],
                "withfrom": quickgo.withfrom_tokens(r),
            }
        )
    return out


def main() -> None:
    data = {acc: collect(acc) for acc in PAIR}
    for acc, sym in PAIR.items():
        print(f"{sym} ({acc}): {len(data[acc])} annotations")

    terms = {acc: {r["go_id"] for r in rows} for acc, rows in data.items()}
    a, b = "P52594", "O95081"
    shared = sorted(terms[a] & terms[b])
    print(f"\nterms on both: {len(shared)}")
    names = {r["go_id"]: r["go_name"] for rows in data.values() for r in rows}
    for t in shared:
        ea = sorted({r["evidence"] for r in data[a] if r["go_id"] == t})
        eb = sorted({r["evidence"] for r in data[b] if r["go_id"] == t})
        wa = sorted({w for r in data[a] if r["go_id"] == t for w in r["withfrom"]})
        wb = sorted({w for r in data[b] if r["go_id"] == t for w in r["withfrom"]})
        same_node = sorted(
            {w for w in wa if w.startswith("PANTHER:")}
            & {w for w in wb if w.startswith("PANTHER:")}
        )
        print(f"  {t} {names[t]}")
        print(f"      AGFG1 {ea} withfrom={wa}")
        print(f"      AGFG2 {eb} withfrom={wb}")
        if same_node:
            print(f"      SAME PANTHER NODE: {same_node}")

    print(f"\nAGFG1-only terms: {len(terms[a] - terms[b])}")
    for t in sorted(terms[a] - terms[b]):
        print(f"  {t} {names[t]}")
    print(f"\nAGFG2-only terms: {len(terms[b] - terms[a])}")
    for t in sorted(terms[b] - terms[a]):
        ev = sorted({r["evidence"] for r in data[b] if r["go_id"] == t})
        wf = sorted({w for r in data[b] if r["go_id"] == t for w in r["withfrom"]})
        print(f"  {t} {names[t]} {ev} withfrom={wf}")

    # Sibling-derived rows: does either gene's WITH/FROM name the other?
    print("\nrows whose WITH/FROM names the sibling accession:")
    found = False
    for acc, other in ((a, b), (b, a)):
        for r in data[acc]:
            if any(other in w for w in r["withfrom"]):
                found = True
                print(f"  {PAIR[acc]} {r['go_id']} {r['evidence']} -> {r['withfrom']}")
    if not found:
        print("  NONE - neither gene's annotations cite the other as support")

    # Self-referential rows (WITH/FROM naming the recipient itself).
    print("\nself-referential rows (WITH/FROM names the recipient):")
    for acc in PAIR:
        for r in data[acc]:
            if any(acc in w for w in r["withfrom"]):
                print(f"  {PAIR[acc]} {r['go_id']} {r['evidence']} -> {r['withfrom']}")

    OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
