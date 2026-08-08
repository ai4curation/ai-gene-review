"""Reference-projection test, plus the mouse orthologue's full annotation set.

For each reference AGFG1's GOA rows cite, ask how many *entities* the reference
annotates across all of GOA and whether any functional/phenotype term spreads
across the set. A reference that annotates a complex plus every subunit, or N
entities with one identical triple, is an import or a projection - not N
independent findings.

Two ways to get the entity count wrong, both guarded here:
  * an annotation count is NOT an entity count (one entity can hold several);
  * a large result is paginated, so a page total must never be read as the whole.
    When the result exceeds what can be honestly enumerated the test is reported
    as UNINFORMATIVE rather than answered from one page.

Usage: uv run python reference_projection.py
"""

from __future__ import annotations

import csv
import json
import pathlib

import quickgo

HERE = pathlib.Path(__file__).parent
GOA = HERE.parent / "AGFG1-goa.tsv"
OUT = HERE / "reference_projection.json"
MOUSE = "Q8K2K6"
MAX_ENUMERABLE = 2000


def main() -> None:
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    refs = sorted({r["REFERENCE"] for r in rows if r["REFERENCE"].startswith("PMID:")})
    print(f"{len(refs)} PMID references cited by AGFG1's GOA rows: {refs}\n")

    out = {}
    for ref in refs:
        n = quickgo.count(reference=ref)
        if n > MAX_ENUMERABLE:
            out[ref] = {"n_annotations": n, "entities": None,
                        "verdict": "UNINFORMATIVE (too large to enumerate honestly)"}
            print(f"{ref}: {n} annotations - entity count UNAVAILABLE, "
                  "projection test uninformative")
            continue
        anns = quickgo.annotations(reference=ref)
        entities = sorted({a["geneProductId"] for a in anns})
        terms = sorted({a["goId"] for a in anns})
        per_term_entities = {
            t: len({a["geneProductId"] for a in anns if a["goId"] == t}) for t in terms
        }
        out[ref] = {
            "n_annotations": n,
            "n_entities": len(entities),
            "entities": entities if len(entities) <= 40 else entities[:40] + ["..."],
            "terms": terms,
            "entities_per_term": per_term_entities,
        }
        print(f"{ref}: {n} annotations over {len(entities)} entities, {len(terms)} terms")
        for t, k in sorted(per_term_entities.items()):
            print(f"    {t}: {k} entities")
        if len(entities) <= 12:
            print(f"    entities: {entities}")

    print(f"\n=== full annotation set of the mouse orthologue {MOUSE} (Agfg1) ===")
    m = quickgo.annotations(geneProductId=f"UniProtKB:{MOUSE}")
    out["_mouse_" + MOUSE] = [
        {
            "go_id": a["goId"],
            "name": a["goName"],
            "aspect": a["goAspect"],
            "evidence": a["goEvidence"],
            "qualifier": a["qualifier"],
            "reference": a["reference"],
            "assigned_by": a["assignedBy"],
        }
        for a in m
    ]
    names = {}
    for a in m:
        # QuickGO's annotation search omits goName on some rows; fetch it rather
        # than printing None, which would make the table unreadable.
        if a["goId"] not in names:
            names[a["goId"]] = a.get("goName") or quickgo.term(a["goId"])["name"]
    for a in sorted(m, key=lambda x: (x["goAspect"] or "", x["goId"], x["goEvidence"])):
        print(
            f"  {a['goAspect'] or '?'} {a['goId']} {names[a['goId']]:45s} "
            f"{a['goEvidence']:4s} {(a['qualifier'] or ''):14s} "
            f"{a['reference']:26s} {a['assignedBy']}"
        )
    rna = [a for a in m if a["goId"] == "GO:0003723"]
    print(f"\nmouse Agfg1 rows for GO:0003723 RNA binding: {len(rna)}")

    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
