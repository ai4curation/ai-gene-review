#!/usr/bin/env python3
"""Query QuickGO for the full reach of the PANTHER nodes cited in ADGRA2's IBA
WITH/FROM column, with hard anti-truncation assertions.

Anti-truncation rule (GENE_BRIEF): compare numberOfHits against the accumulated
len(results), never against a page-size constant the server may clamp.
"""
import json
import sys
import urllib.request
import collections

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
PAGE = 100  # QuickGO's documented cap for this endpoint


def fetch_all(params: dict) -> list:
    """Page through a QuickGO annotation search, asserting nothing is dropped."""
    results = []
    page = 1
    total = None
    while True:
        q = dict(params, limit=PAGE, page=page)
        url = QUICKGO + "?" + urllib.parse.urlencode(q)
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req) as fh:
            assert fh.status == 200, f"HTTP {fh.status} for {url}"
            d = json.load(fh)
        if total is None:
            total = d["numberOfHits"]
        got = d["results"]
        results.extend(got)
        if len(results) >= total or not got:
            break
        page += 1
    # The load-bearing assertion: what the server said it had vs what we read.
    assert len(results) == total, (
        f"TRUNCATED: numberOfHits={total} but read {len(results)} rows for {params}"
    )
    return results


def reach(node: str) -> dict:
    rows = fetch_all({"withFrom": f"PANTHER:{node}"})
    by_term = collections.defaultdict(set)
    for r in rows:
        by_term[r["goId"]].add((r["taxonId"], r["symbol"], r["geneProductId"]))
    return {"n_annotations": len(rows), "by_term": by_term}


def main() -> None:
    out = {}
    for node in sys.argv[1:] or ["PTN002914520", "PTN001738137"]:
        info = reach(node)
        human = {
            t: sorted({(s, g) for (tx, s, g) in v if tx == 9606})
            for t, v in info["by_term"].items()
        }
        all_syms = {s for v in info["by_term"].values() for (_, s, _) in v}
        out[node] = {
            "n_annotations": info["n_annotations"],
            "terms": sorted(info["by_term"]),
            "n_entities_total": len({g for v in info["by_term"].values() for (_, _, g) in v}),
            "human_reach_per_term": human,
            "human_symbols": sorted({s for v in human.values() for (s, _) in v}),
            "distinct_symbols_sample": sorted(all_syms)[:0],  # not used
        }
        print(f"=== {node} ===")
        print(f"  annotations: {info['n_annotations']}  entities: {out[node]['n_entities_total']}")
        for t in sorted(info["by_term"]):
            hs = human.get(t, [])
            print(f"  {t}: {len(info['by_term'][t])} entities; human = {[s for s, _ in hs] or 'NONE'}")
        print(f"  ALL human genes reached by this node: {out[node]['human_symbols'] or 'NONE'}")
    json.dump(
        {k: {kk: (vv if kk != "human_reach_per_term" else {t: [list(x) for x in y] for t, y in vv.items()})
             for kk, vv in v.items() if kk != "distinct_symbols_sample"}
         for k, v in out.items()},
        open("node_reach.json", "w"), indent=2, sort_keys=True,
    )


if __name__ == "__main__":
    import urllib.parse
    main()
