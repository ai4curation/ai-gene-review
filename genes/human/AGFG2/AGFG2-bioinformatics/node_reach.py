#!/usr/bin/env python3
"""Ask both halves of the PAINT node question for AGFG2.

1. Which terms does each node AGFG2 cites actually donate, and to whom?
2. Reciprocally: which node's *reach* is exactly the human AGFG clade, and what
   did that node give them?

Also records what the *other* human member of PTHR46134 (AGFG1) receives, so a
claim that AGFG2 inherits its paralogue's record is measured rather than asserted.
"""

from __future__ import annotations

import json
import pathlib
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import quickgo_annotations  # noqa: E402

HERE = pathlib.Path(__file__).parent
NODES = ["PTN002353603", "PTN002919572"]
SUBJECT = "O95081"
PARALOG = "P52594"


def node_recipients(node: str) -> dict:
    rows = quickgo_annotations(withFrom=f"PANTHER:{node}", limit=100)
    if not rows:
        raise AssertionError(
            f"{node}: zero annotations — a rejected query and an empty result look "
            f"identical, so this is treated as a failure rather than a finding"
        )
    by_term: dict[str, set] = defaultdict(set)
    by_entity: dict[str, set] = defaultdict(set)
    taxa: dict[str, str] = {}
    for r in rows:
        gp = r["geneProductId"]
        by_term[f"{r['goId']}"].add(gp)
        by_entity[gp].add(r["goId"])
        taxa[gp] = str(r.get("taxonId"))
    human = sorted(gp for gp, tx in taxa.items() if tx == "9606")
    return {
        "node": node,
        "n_annotations": len(rows),
        "n_entities": len(by_entity),
        "n_human_entities": len(human),
        "human_entities": human,
        "terms": {t: sorted(v) for t, v in sorted(by_term.items())},
        "terms_to_human": {
            t: sorted(v & set(human)) for t, v in sorted(by_term.items()) if v & set(human)
        },
        "entities": {e: sorted(v) for e, v in sorted(by_entity.items())},
    }


def gene_record(acc: str) -> dict:
    rows = quickgo_annotations(geneProductId=f"UniProtKB:{acc}", limit=100)
    if not rows:
        raise AssertionError(f"{acc}: zero annotations returned")
    out = defaultdict(list)
    for r in rows:
        out[r["goEvidence"]].append((r["goId"], r["reference"], r.get("qualifier")))
    return {
        "accession": acc,
        "n_annotations": len(rows),
        "by_evidence": {k: sorted(set(v)) for k, v in sorted(out.items())},
        "n_experimental": sum(
            1 for r in rows
            if r["goEvidence"] in {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                                    "HTP", "HDA", "HMP", "HGI", "HEP"}
        ),
    }


def main() -> None:
    out = {"nodes": {}, "genes": {}}
    for n in NODES:
        out["nodes"][n] = node_recipients(n)
    for acc in (SUBJECT, PARALOG):
        out["genes"][acc] = gene_record(acc)

    (HERE / "node_reach.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    for n, d in out["nodes"].items():
        print(f"\n=== PANTHER:{n} ===")
        print(f"annotations={d['n_annotations']} entities={d['n_entities']} "
              f"human={d['n_human_entities']} {d['human_entities']}")
        for t, ents in d["terms"].items():
            hs = d["terms_to_human"].get(t, [])
            print(f"  {t}: {len(ents)} entities; human -> {hs}")

    for acc, d in out["genes"].items():
        print(f"\n=== {acc} ===  n={d['n_annotations']} experimental={d['n_experimental']}")
        for ev, rows in d["by_evidence"].items():
            print(f"  {ev}: {len(rows)}")


if __name__ == "__main__":
    main()
