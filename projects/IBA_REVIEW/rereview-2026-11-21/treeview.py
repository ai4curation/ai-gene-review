"""Print the PAINT tree context for one gene and one GO term.

For the gene's leaf in each of its PANTHER families this prints every ancestral node
from the leaf to the root (clade size, species, taxon spread), every PAINT record on
those nodes (IBD, IRD, IKR), and, for the node that carries the IBD for the term, the
child clades with their members and which members are experimental seeds.

Trees come from the PANTHER API cache (.cache/panther_trees/<release>/) and node
annotations from the pinned IBD.gaf, both fetched on demand.

    uv run python projects/IBA_REVIEW/rereview-2026-11-21/treeview.py human LALBA GO:0003796
    uv run python projects/IBA_REVIEW/rereview-2026-11-21/treeview.py human LALBA GO:0003796 --members 60
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

import requests
import yaml

from ai_gene_review.etl.panther_paint import IBD_GAF_URL, download_cached, open_text, parse_ibd_gaf
from ai_gene_review.etl.panther_trees import ancestors_of, leaf_nodes_for, leaves_below, load_family
from ai_gene_review.validation.gene_paint_losses import is_loss, paint_cache_dir, panther_families

LABEL_CACHE = Path(".cache") / "go_labels.json"


def go_labels(ids: set[str]) -> dict[str, str]:
    """GO labels from QuickGO, cached in .cache/go_labels.json."""
    known = json.loads(LABEL_CACHE.read_text()) if LABEL_CACHE.exists() else {}
    todo = sorted(i for i in ids if i not in known)
    for k in range(0, len(todo), 50):
        try:
            r = requests.get(
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/" + ",".join(todo[k : k + 50]),
                headers={"Accept": "application/json"},
                timeout=60,
            )
            for t in r.json().get("results", []):
                known[t["id"]] = t["name"] + (" [OBSOLETE]" if t.get("isObsolete") else "")
        except (requests.RequestException, ValueError) as e:
            print(f"(label lookup failed: {e})")
    LABEL_CACHE.parent.mkdir(exist_ok=True)
    LABEL_CACHE.write_text(json.dumps(known))
    return known


def children(tree: dict, node: str) -> list[str]:
    """Direct children of an internal node, derived from clade containment."""
    clade = set(leaves_below(tree, node))
    inner = [n for n, below in tree["under"].items() if n != node and set(below) < clade]
    maximal = [n for n in inner if not any(m != n and set(tree["under"][n]) < set(tree["under"][m]) for m in inner)]
    covered = set().union(*(set(tree["under"][n]) for n in maximal)) if maximal else set()
    return maximal + sorted(clade - covered)


def describe(tree: dict, node: str, limit: int) -> str:
    """Species spread and (up to ``limit``) members of a clade."""
    lv = leaves_below(tree, node)
    orgs = collections.Counter(tree["leaves"][x].get("organism", "?") for x in lv)
    spread = ", ".join(f"{o}:{n}" for o, n in orgs.most_common(8)) + (" ..." if len(orgs) > 8 else "")
    mem = [f"{tree['leaves'][x].get('symbol') or '?'}|{tree['leaves'][x].get('uniprot')}|{tree['leaves'][x].get('organism','?')}" for x in lv]
    shown = "; ".join(mem[:limit]) + (f"; ... (+{len(mem) - limit})" if len(mem) > limit else "")
    return f"{len(lv)} leaves, {len(orgs)} species [{spread}]\n        members: {shown}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("organism")
    ap.add_argument("gene")
    ap.add_argument("go_id", nargs="?", help="term to focus on; omit to list every PAINT record on the lineage")
    ap.add_argument("--members", type=int, default=25, help="members to list per clade")
    a = ap.parse_args()

    folder = Path("genes") / a.organism / a.gene
    review = yaml.safe_load((folder / f"{a.gene}-ai-review.yaml").read_text())
    acc = str(review["id"])
    fams = panther_families((folder / f"{a.gene}-uniprot.txt").read_text())
    inv = Path(__file__).parent / "inventory.tsv"
    if inv.exists():  # the family PAINT actually propagates from can differ from the UniProt cross-reference
        for line in inv.read_text().splitlines()[1:]:
            c = line.split("\t")
            if c[0] == str(folder / f"{a.gene}-ai-review.yaml") and c[7] and c[7] not in fams:
                fams.append(c[7])
    with open_text(download_cached(IBD_GAF_URL, paint_cache_dir(Path(".cache/paint")))) as fh:
        ibd = parse_ibd_gaf(fh)
    print(f"# {a.organism}/{a.gene} {acc}  families: {', '.join(fams) or 'none'}")
    for fam in fams:
        tree = load_family(fam, Path(".cache/panther_trees"))
        if tree is None:
            print(f"\n## {fam}: tree not available")
            continue
        leaves = leaf_nodes_for(tree, acc)
        print(f"\n## {fam}: {len(tree['leaves'])} leaves; {acc} is leaf {leaves or 'NOT A LEAF'}")
        for leaf in leaves:
            lineage = sorted(ancestors_of(tree, leaf), key=lambda n: len(leaves_below(tree, n)))
            ids = {r.go_id for n in lineage for r in ibd.get(n, [])}
            lab = go_labels(ids | ({a.go_id} if a.go_id else set()))
            seeds_all: set[str] = set()
            print(f"subfamily of leaf: {tree['leaves'][leaf].get('subfamily')}")
            print("\n### Lineage, leaf to root (PAINT records at each node)")
            focus = []
            for n in lineage:
                lv = leaves_below(tree, n)
                orgs = {tree["leaves"][x].get("organism", "?") for x in lv}
                print(f"- {n}: {len(lv)} leaves, {len(orgs)} species")
                for r in ibd.get(n, []):
                    mark = " <== FOCUS TERM" if r.go_id == a.go_id else ""
                    kind = ("NOT " if r.negated else "") + r.evidence + (" (loss)" if is_loss(r) else "")
                    print(f"    {kind} {r.go_id} {lab.get(r.go_id, '?')} [{r.aspect}] {r.date} seeds={len(r.seeds)}{mark}")
                    if r.go_id == a.go_id:
                        focus.append((n, r))
            for n, r in focus:
                print(f"\n### Focus record at {n}: {'NOT ' if r.negated else ''}{r.evidence} {r.go_id} {lab.get(r.go_id, '?')}")
                print(f"seeds / with: {' | '.join(r.seeds)}")
                seed_accs = {s.split(':', 1)[1] for s in r.seeds if s.startswith('UniProtKB:')}
                seeds_all |= seed_accs
                if is_loss(r):
                    continue
                print(f"target {acc} is itself a seed: {acc in seed_accs}")
                print("child clades of this node (the one holding the target is marked):")
                for c in children(tree, n):
                    here = leaf in leaves_below(tree, c)
                    below = [x for x in tree["under"] if x != c and set(tree["under"][x]) <= set(leaves_below(tree, c))]
                    sub = [
                        f"{('NOT ' if q.negated else '')}{q.evidence} {q.go_id} {lab.get(q.go_id) or go_labels({q.go_id}).get(q.go_id, '?')} @{x}"
                        for x in [c] + below
                        for q in ibd.get(x, [])
                        if q.aspect == r.aspect
                    ]
                    print(f"  * {c}{'  <== TARGET IS HERE' if here else ''}: {describe(tree, c, a.members)}")
                    if sub:
                        print(f"        same-aspect PAINT records inside this clade: {'; '.join(sorted(set(sub))[:12])}")
            if a.go_id and not focus:
                print(f"\nNo PAINT record for {a.go_id} on any ancestor of {acc} in the pinned snapshot.")


if __name__ == "__main__":
    main()
