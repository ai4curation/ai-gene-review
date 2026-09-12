"""Ask the two node questions the campaign brief says are the productive ones:

  1. WHICH nodes carry each term AGFG1 receives by IBA?
  2. Reciprocally, WHICH gene products does each of those nodes reach, and what
     did the node give them?

Implemented by querying QuickGO for every IBA annotation to the term
(reference=GO_REF:0000033) and grouping the recipients by the PANTHER node named
in their own WITH/FROM. Fully paginated with the numberOfHits == len(results)
assertion, so a clamped page cannot masquerade as a complete answer.

Usage: uv run python node_reach.py
"""

from __future__ import annotations

import json
import pathlib
from collections import defaultdict

import quickgo

OUT = pathlib.Path(__file__).parent / "node_reach.json"

# The five terms AGFG1 receives by IBA (from AGFG1-goa.tsv). Each is queried only
# if its IBA population is small enough to enumerate honestly; a term whose
# population exceeds MAX_HITS is reported as NOT ATTEMPTED rather than sampled,
# because a first-page count read as a whole is the pagination trap.
TERMS = {
    "GO:0005737": "cytoplasm",
    "GO:0031410": "cytoplasmic vesicle",
    "GO:0001675": "acrosome assembly",
    "GO:0007289": "spermatid nucleus differentiation",
    "GO:0045109": "intermediate filament organization",
}
MAX_HITS = 3000
NODES_OF_INTEREST = {"PANTHER:PTN002919572", "PANTHER:PTN002353603"}


def main() -> None:
    result = {}
    skipped = {}
    for go_id, label in TERMS.items():
        n = quickgo.count(goId=go_id, reference="GO_REF:0000033")
        if n > MAX_HITS:
            skipped[go_id] = n
            print(
                f"\n=== {go_id} {label}: {n} IBA annotations - NOT ATTEMPTED "
                f"(> MAX_HITS={MAX_HITS}); no partial count is reported for it"
            )
            continue
        anns = quickgo.annotations(
            goId=go_id,
            reference="GO_REF:0000033",
            limit=100,
        )
        by_node: dict[str, set[str]] = defaultdict(set)
        for a in anns:
            toks = quickgo.withfrom_tokens(a)
            nodes = [t for t in toks if t.startswith("PANTHER:")]
            gp = f"{a['geneProductId']} ({a['symbol']}, taxon {a['taxonId']})"
            for n in nodes:
                by_node[n].add(gp)
        print(f"\n=== {go_id} {label}: {len(anns)} IBA annotations, {len(by_node)} nodes")
        for n in sorted(by_node, key=lambda k: (-len(by_node[k]), k)):
            mark = " <== AGFG1's node" if n in NODES_OF_INTEREST else ""
            print(f"  {n}: {len(by_node[n])} recipients{mark}")
            if n in NODES_OF_INTEREST or len(by_node[n]) <= 12:
                for gp in sorted(by_node[n]):
                    print(f"        {gp}")
        result[go_id] = {n: sorted(v) for n, v in by_node.items()}

    # Reciprocal question: what is the FULL term set each node of interest gives,
    # and is its human reach exactly the AGFG1/AGFG2 pair?
    print("\n=== reciprocal view of AGFG1's own nodes")
    for node in sorted(NODES_OF_INTEREST):
        print(f"\n{node}")
        for go_id, label in TERMS.items():
            if go_id in skipped:
                print(f"  {go_id} {label}: not attempted ({skipped[go_id]} annotations)")
                continue
            recips = result[go_id].get(node, [])
            if recips:
                human = [r for r in recips if "taxon 9606" in r]
                print(
                    f"  {go_id} {label}: {len(recips)} recipients, "
                    f"{len(human)} human -> {sorted(human)}"
                )

    # Classify PTN002919572's recipients by symbol. Hand-counted panels have
    # drifted on several genes in this campaign, so this is computed and the
    # three classes are asserted to sum to the total.
    node = "PANTHER:PTN002919572"
    recips = set()
    for go_id in result:
        recips |= set(result[go_id].get(node, []))
    if recips:
        import re

        def sym(entry: str) -> str:
            m = re.search(r"\((?P<sym>[^,]+),", entry)
            assert m, entry
            return m.group("sym")

        by_class = {"AGFG1-type": [], "AGFG2-type": [], "unnamed": []}
        for r in sorted(recips):
            s = sym(r).lower()
            if s.startswith("agfg1"):
                by_class["AGFG1-type"].append(r)
            elif s.startswith("agfg2"):
                by_class["AGFG2-type"].append(r)
            else:
                by_class["unnamed"].append(r)
        total = sum(len(v) for v in by_class.values())
        assert total == len(recips), f"{total} classified vs {len(recips)} recipients"
        print(f"\n=== {node} recipient composition ({len(recips)} distinct)")
        for k, v in by_class.items():
            print(f"  {k}: {len(v)}")
            if k == "unnamed":
                for e in v:
                    print(f"      {e}")
        result["_recipient_composition"] = {k: len(v) for k, v in by_class.items()}
        result["_recipient_composition"]["total"] = len(recips)

    OUT.write_text(
        json.dumps({"by_term": result, "not_attempted": skipped}, indent=2, sort_keys=True)
        + "\n"
    )
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
