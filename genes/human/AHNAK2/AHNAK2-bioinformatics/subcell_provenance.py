"""Where does AHNAK2's only UniProt SUBCELLULAR LOCATION come from?

GOA row `GO:0005634 nucleus / IEA / GO_REF:0000044 / UniProtKB-SubCell:SL-0191`
is a mechanical mapping of whatever UniProt's SUBCELLULAR LOCATION comment says.
So the question "is the nucleus annotation evidence about AHNAK2?" reduces to
"what evidence does that comment carry?".

Prints, for AHNAK2 and for each donor on the nucleus IBA, the SUBCELLULAR
LOCATION and SUBUNIT comments with their ECO evidence codes and source
references, so a `ECO:0000250` (by similarity) cannot be read as a measurement.

Run: uv run python subcell_provenance.py
"""

from __future__ import annotations

import json
from pathlib import Path

from uniprot import _cached_get

ACCS = {
    "AHNAK2 (subject)": "Q8IVF2",
    "AHNAK (paralogue donor)": "Q09666",
    "Ahnak mouse (donor on all three IBAs)": "E9Q616",
    "PRX (donor)": "Q9BXM0",
    "Prx mouse (donor)": "O55103",
    "Prx rat (donor)": "Q63425",
    "Ahnak2 mouse (ortholog, cytoplasm IBA only)": "A0A7N9VR94",
}
WANT = {"SUBCELLULAR LOCATION", "SUBUNIT"}


def entry(acc: str) -> dict:
    return json.loads(_cached_get(f"https://rest.uniprot.org/uniprotkb/{acc}.json",
                                  f"arch_{acc}"))


def ev(items: list[dict]) -> str:
    if not items:
        return "no evidence tag"
    return "; ".join(
        f"{e['evidenceCode']}" + (f"|{e['source']}:{e['id']}" if e.get("source") else "")
        for e in items
    )


def main() -> None:
    for label, acc in ACCS.items():
        e = entry(acc)
        status = ("Swiss-Prot" if e["entryType"].startswith("UniProtKB reviewed")
                  else "TrEMBL")
        print(f"=== {label}  {acc}  [{status}] ===")
        found = False
        for c in e.get("comments", []):
            if c["commentType"] not in WANT:
                continue
            found = True
            if c["commentType"] == "SUBCELLULAR LOCATION":
                for loc in c.get("subcellularLocations", []):
                    v = loc["location"]
                    print(f"  LOCATION: {v['value']:45s} {ev(v.get('evidences', []))}")
            else:
                for t in c.get("texts", []):
                    print(f"  SUBUNIT : {t['value']}")
                    print(f"            evidence: {ev(t.get('evidences', []))}")
        if not found:
            print("  (no SUBCELLULAR LOCATION or SUBUNIT comment)")
        print()


if __name__ == "__main__":
    main()
