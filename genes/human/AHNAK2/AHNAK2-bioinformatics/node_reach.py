"""The reciprocal half of the PAINT question.

The usual question is "which node carries the term my gene received?". The
question that finds misplacements is the other one: **which node's reach is
exactly my gene set, and what did it give them?**

Here the three human PTHR23348 members are AHNAK2, AHNAK and PRX, in three
different subfamilies. Ask, for each of them, which IBA terms they hold and
which WITH/FROM sets those came from. A term that reached only one of the three,
or that reached all three from a donor set belonging to just one, is the
signature of a placement problem.

Run: uv run python node_reach.py
"""

from __future__ import annotations

import json
from collections import defaultdict

from uniprot import _cached_get

HUMAN_FAMILY = {
    "AHNAK2": "Q8IVF2",
    "AHNAK": "Q09666",
    "PRX": "Q9BXM0",
}
BASE = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def iba_rows(acc: str) -> list[dict]:
    url = (f"{BASE}?geneProductId=UniProtKB:{acc}&evidenceCode=ECO:0000318"
           "&evidenceCodeUsage=exact&limit=100")
    d = json.loads(_cached_get(url, f"iba_{acc}"))
    if d["numberOfHits"] > len(d["results"]):
        raise SystemExit(f"truncated IBA result for {acc}: {d['numberOfHits']} hits, "
                         f"{len(d['results'])} read")
    return d["results"]


def main() -> None:
    per_gene: dict[str, dict[str, dict]] = {}
    for name, acc in HUMAN_FAMILY.items():
        rows = iba_rows(acc)
        per_gene[name] = {}
        for r in rows:
            wf = sorted({x["id"] for c in (r.get("withFrom") or [])
                         for x in c.get("connectedXrefs", [])})
            per_gene[name][r["goId"]] = {
                "name": r.get("goName") or "",
                "qualifier": r.get("qualifier"),
                "withfrom": wf,
            }
        print(f"{name} ({acc}): {len(rows)} IBA row(s)")
        for go_id, v in sorted(per_gene[name].items()):
            print(f"    {go_id} {v['name'] or '':38s} {v['qualifier']:14s} "
                  f"nodes/donors: {','.join(v['withfrom'])}")
        print()

    # Which terms reach which subset of the three human family members?
    reach: dict[str, set[str]] = defaultdict(set)
    for name, terms in per_gene.items():
        for go_id in terms:
            reach[go_id].add(name)
    print("=== IBA term reach across the three human PTHR23348 members ===")
    for go_id, genes in sorted(reach.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        label = next(per_gene[g][go_id]["name"] for g in genes)
        print(f"{go_id} {label or '(unnamed)':38s} -> {sorted(genes)}")
    print()
    print("A term reaching exactly one member, or reaching all three from a donor "
          "set belonging to one, is where to look for a placement problem.")
    print()

    # Byte-identical WITH/FROM across the three members means the node treats
    # them as interchangeable. Say so explicitly rather than leaving it implied.
    print("=== is the WITH/FROM set byte-identical across the three members? ===")
    for go_id, genes in sorted(reach.items()):
        if len(genes) < 2:
            continue
        sets = {tuple(per_gene[g][go_id]["withfrom"]) for g in genes}
        print(f"{go_id}: {'IDENTICAL' if len(sets) == 1 else 'DIFFERS'} across "
              f"{sorted(genes)}")
    print()

    # Does any of the three hold these terms by its OWN experimental evidence?
    # If not, the whole family's holding of the term rests on donors outside it.
    print("=== experimental (non-IBA/non-IEA) holdings of the same terms ===")
    exp_codes = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                 "HTP", "HDA", "HMP", "HGI", "HEP"}
    for go_id in sorted(reach):
        for name, acc in HUMAN_FAMILY.items():
            url = (f"{BASE}?geneProductId=UniProtKB:{acc}&goId={go_id}"
                   "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100")
            d = json.loads(_cached_get(url, f"own_{acc}_{go_id.replace(':', '_')}"))
            if d["numberOfHits"] > len(d["results"]):
                raise SystemExit(f"truncated result for {acc}/{go_id}")
            own = [(r["goId"], r["goEvidence"], r.get("reference"))
                   for r in d["results"] if r["goEvidence"] in exp_codes]
            if own:
                print(f"{go_id} {name}: {own}")
            else:
                print(f"{go_id} {name}: none")
        print()


if __name__ == "__main__":
    main()
