#!/usr/bin/env python3
"""Emit `propagation_review.source_entities` YAML built FROM the GOA WITH/FROM field.

Hand-maintained source lists have drifted on every gene in this campaign that
tried it, so the blocks pasted into the review are generated here and then
re-asserted against the GOA TSV by `audit_claims.py`.  The two together mean the
lists cannot silently diverge from GOA.

Labels and per-entity `source_status` come from `withfrom.json` (resolve_withfrom.py),
so they are also derived rather than typed.
"""

from __future__ import annotations

import csv
import json
import pathlib

HERE = pathlib.Path(__file__).parent
GOA = HERE.parent / "AGFG2-goa.tsv"
WF = json.loads((HERE / "withfrom.json").read_text())
SITE = json.loads((HERE / "arfgap_domain.json").read_text())


def label_for(token: str) -> str:
    rec = WF["tokens"].get(token, {})
    kind = rec.get("kind")
    if kind == "panther_node":
        return "PANTHER tree node (not a protein)"
    if kind == "interpro_signature":
        return "InterPro signature (not a protein)"
    cands = rec.get("candidates")
    if cands:
        rev = [c for c in cands if c["reviewed"]]
        pick = rev[0] if rev else cands[0]
        status = "Swiss-Prot" if pick["reviewed"] else "TrEMBL"
        gene = "/".join(g for g in pick["gene"] if g) or "?"
        return (f"{pick['organism']} {gene} ({pick['accession']}, {status}"
                + (f"; {len(cands)} UniProt entries, {len(rev)} reviewed)"
                   if len(cands) > 1 else ")"))
    if rec.get("entry_name"):
        gene = "/".join(g for g in rec.get("gene", []) if g) or "?"
        status = "Swiss-Prot" if rec.get("reviewed") else "TrEMBL"
        return f"{rec.get('organism')} {gene} ({rec['id']}, {status})"
    return "unresolved"


def main() -> None:
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    for r in rows:
        toks = [t for t in r["WITH/FROM"].split("|") if t]
        if not toks:
            continue
        print(f"# {r['GO TERM']} {r['GO NAME']} [{r['GO EVIDENCE CODE']}] "
              f"-- {len(toks)} WITH/FROM tokens")
        print("      source_entities:")
        for t in toks:
            print(f"      - source_id: {t}")
            print(f"        source_label: {label_for(t)}")
        print()


if __name__ == "__main__":
    main()
