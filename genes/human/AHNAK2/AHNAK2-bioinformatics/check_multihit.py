"""Print EVERY candidate behind each multi-hit MOD cross-reference.

`resolve_withfrom.py` keeps one entry per token so its tables stay one-row-per
(GOA row, token). That is the `size=1` trap in disguise: a token with 3 or 5
hits has been silently collapsed. This script prints all of them so the
ambiguity is visible as data, and so a truncated TrEMBL entry cannot be mistaken
for a short protein.

Run: uv run python check_multihit.py
"""

from __future__ import annotations

import csv
from pathlib import Path

from uniprot import resolve_mod_id, summarise, uniprot_entry

HERE = Path(__file__).parent
TSV = HERE / "withfrom_resolved.tsv"


def main() -> None:
    if not TSV.exists():
        raise SystemExit(f"missing {TSV}; run `uv run python resolve_withfrom.py` first")
    with TSV.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    tokens = sorted({r["token"] for r in rows if r["kind"] == "mod-id"})
    for token in tokens:
        hits = resolve_mod_id(token)
        print(f"{token}: {len(hits)} UniProt hit(s)")
        for h in hits:
            s = summarise(uniprot_entry(h["primaryAccession"]))
            status = "Swiss-Prot" if s["reviewed"] else "TrEMBL"
            print(f"    {s['accession']:12s} {s['id']:20s} {status:10s} "
                  f"{str(s['length']):>6s} aa  {s['gene']:8s} {s['protein']}")
        print()


if __name__ == "__main__":
    main()
