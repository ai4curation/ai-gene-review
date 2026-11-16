"""Tally how this repository's gene reviews treat annotations to given GO terms.

For each GO id, count the ``existing_annotations`` rows that carry it across
``genes/*/*/*-ai-review.yaml``, broken down by ``review.action`` (NOT rows are
counted separately), and the reviews that name it in ``core_functions``.
Prints a markdown table; ``--json`` also writes per-action gene lists.

    python projects/GO_TRACKER_BACKLOG/term_actions.py GO:0042803 GO:0046982
    python projects/GO_TRACKER_BACKLOG/term_actions.py --obo ../go-ontology/src/ontology/go-edit.obo \\
        --descendants GO:0051606 --json /tmp/detection.json

``--descendants`` adds every non-obsolete is_a/part_of descendant of the
given roots (needs ``--obo``), including part_of edges in logical definitions. It does not follow ``regulates`` links, so
pass regulation terms explicitly. Rows are counted as they stand in the review
files, so NEW rows proposed by a review are included.
"""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
MAIN_ACTIONS = ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "MARK_AS_OVER_ANNOTATED", "REMOVE", "UNDECIDED"]
CORE_SLOTS = (
    "molecular_function",
    "contributes_to_molecular_function",
    "directly_involved_in",
    "locations",
    "in_complex",
)


def obo_index(path: Path) -> tuple[dict[str, str], dict[str, set[str]], set[str]]:
    names: dict[str, str] = {}
    kids: dict[str, set[str]] = collections.defaultdict(set)
    obsolete: set[str] = set()
    cur: str | None = None
    in_term = False
    with path.open() as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.startswith("["):
                in_term, cur = line == "[Term]", None
                continue
            if not in_term or ": " not in line:
                continue
            key, val = line.split(": ", 1)
            if key == "id":
                cur = val
            elif cur is None:
                continue
            elif key == "name":
                names[cur] = val
            elif key == "is_obsolete" and val.startswith("true"):
                obsolete.add(cur)
            elif key == "is_a" or (key == "intersection_of" and val.startswith("GO:")):
                kids[val.split()[0]].add(cur)
            elif (key == "relationship" or key == "intersection_of") and val.startswith("part_of GO:"):
                kids[val.split()[1]].add(cur)
    return names, kids, obsolete


def expand(roots: list[str], kids: dict[str, set[str]], obsolete: set[str]) -> list[str]:
    seen: list[str] = []
    stack = list(roots)
    while stack:
        term = stack.pop()
        if term in seen:
            continue
        seen.append(term)
        stack.extend(sorted(kids.get(term, ()), reverse=True))
    return [t for t in seen if t not in obsolete]


def tally(genes_root: Path, ids: set[str]) -> dict[str, dict]:
    res = {
        i: {"label": None, "actions": collections.Counter(), "genes": collections.defaultdict(set), "core": set()}
        for i in ids
    }
    for review in sorted(genes_root.glob("*/*/*-ai-review.yaml")):
        text = review.read_text(errors="replace")
        if not any(i in text for i in ids):
            continue
        gene = f"{review.parent.parent.name}/{review.parent.name}"
        doc = yaml.load(text, Loader=LOADER) or {}
        for row in doc.get("existing_annotations") or []:
            term = row.get("term") or {}
            tid = term.get("id")
            if tid not in res:
                continue
            res[tid]["label"] = res[tid]["label"] or term.get("label")
            action = (row.get("review") or {}).get("action") or "NONE"
            if row.get("negated"):
                action = f"NOT {action}"
            res[tid]["actions"][action] += 1
            res[tid]["genes"][action].add(gene)
        for core in doc.get("core_functions") or []:
            for slot in CORE_SLOTS:
                vals = core.get(slot)
                for val in vals if isinstance(vals, list) else [vals]:
                    if isinstance(val, dict) and val.get("id") in res:
                        res[val["id"]]["core"].add(gene)
    return res


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", help="GO ids to tally")
    ap.add_argument("--descendants", nargs="*", default=[], help="roots whose descendants are added (needs --obo)")
    ap.add_argument("--obo", type=Path, help="go-edit.obo, for labels and --descendants")
    ap.add_argument("--genes", type=Path, default=REPO / "genes")
    ap.add_argument("--json", type=Path, help="write per-action gene lists here")
    ap.add_argument("--min-rows", type=int, default=0, help="omit terms with fewer rows from the table")
    args = ap.parse_args()

    names: dict[str, str] = {}
    ids = list(args.ids)
    if args.obo:
        names, kids, obsolete = obo_index(args.obo)
        ids += expand(args.descendants, kids, obsolete)
    elif args.descendants:
        ap.error("--descendants needs --obo")
    ids = list(dict.fromkeys(ids))
    res = tally(args.genes, set(ids))

    print("| Term | Rows | Genes | " + " | ".join(MAIN_ACTIONS) + " | Other | Core in |")
    print("|---|---:|---:|" + "---:|" * len(MAIN_ACTIONS) + "---|---:|")
    all_genes: set[str] = set()
    totals: collections.Counter = collections.Counter()
    for tid in ids:
        r = res[tid]
        rows = sum(r["actions"].values())
        genes = set().union(*r["genes"].values()) if r["genes"] else set()
        all_genes |= genes
        totals.update(r["actions"])
        if rows < args.min_rows:
            continue
        other = {k: v for k, v in r["actions"].items() if k not in MAIN_ACTIONS}
        other_txt = ", ".join(f"{k} {v}" for k, v in sorted(other.items())) or ""
        label = names.get(tid) or r["label"] or ""
        cells = " | ".join(str(r["actions"].get(a, 0)) for a in MAIN_ACTIONS)
        print(f"| {tid} {label} | {rows} | {len(genes)} | {cells} | {other_txt} | {len(r['core'])} |")
    print(f"\nTotal: {sum(totals.values())} rows on {len(all_genes)} reviewed genes; " + ", ".join(
        f"{k} {v}" for k, v in totals.most_common()))
    if args.json:
        args.json.write_text(json.dumps({
            tid: {
                "label": names.get(tid) or res[tid]["label"],
                "actions": dict(res[tid]["actions"]),
                "genes": {k: sorted(v) for k, v in res[tid]["genes"].items()},
                "core_function_genes": sorted(res[tid]["core"]),
            }
            for tid in ids
        }, indent=1))


if __name__ == "__main__":
    main()
