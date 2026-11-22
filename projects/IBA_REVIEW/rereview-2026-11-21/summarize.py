"""Check the batch records against inventory.tsv and the gene reviews, print tallies, write results.tsv and paint_requests.tsv.

Reports rows of inventory.tsv with no verdict, verdicts for rows not in the inventory,
verdicts whose recorded action disagrees with the gene review as it now stands, and
nodes whose rows were given different PAINT fixes in different records.

    uv run python projects/IBA_REVIEW/rereview-2026-11-21/summarize.py
"""

from __future__ import annotations

import collections
import csv
import glob
from pathlib import Path

import yaml

from ai_gene_review.yaml_utils import safe_load

HERE = Path(__file__).parent


def main() -> None:
    inv = {(r["gene_file"], r["go_id"]): r for r in csv.DictReader(open(HERE / "inventory.tsv"), delimiter="\t")}
    seen: dict[tuple[str, str], dict] = {}
    for path in sorted(glob.glob(str(HERE / "batches" / "*.yaml"))):
        for gene in yaml.safe_load(open(path))["genes"]:
            for row in gene["rows"]:
                row["_batch"] = Path(path).stem
                seen[(gene["gene_file"], row["go_id"])] = row
    print("inventory rows:", len(inv), " verdicts:", len(seen))
    print("missing verdicts:", sorted(set(inv) - set(seen)))
    print("verdicts not in inventory:", sorted(set(seen) - set(inv)))
    print("verdicts:", dict(collections.Counter(r["verdict"] for r in seen.values())))
    print("grounds:", dict(collections.Counter(str(r.get("ground")) for r in seen.values())))
    print("new actions:", dict(collections.Counter(r.get("new_action") for r in seen.values() if r["verdict"] == "ACTION_CHANGED")))
    print("paint fixes:", dict(collections.Counter((r.get("paint_fix") or {}).get("paint_action") for r in seen.values())))

    fields = ["gene_file", "go_id", "go_label", "status", "family", "ibd_node", "batch", "verdict", "ground",
              "new_action", "paint_action", "target_node_id", "review_edited"]
    with open(HERE / "results.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for (gene_file, go), row in sorted(seen.items()):
            i = inv.get((gene_file, go), {})
            fix = row.get("paint_fix") or {}
            w.writerow({
                "gene_file": gene_file, "go_id": go, "go_label": i.get("go_label"), "status": i.get("status"),
                "family": i.get("family"), "ibd_node": i.get("ibd_node"), "batch": row["_batch"],
                "verdict": row["verdict"], "ground": row.get("ground"), "new_action": row.get("new_action") or "",
                "paint_action": fix.get("paint_action"), "target_node_id": fix.get("target_node_id") or "",
                "review_edited": row.get("review_edited"),
            })

    # One line per PAINT change asked for: the unit a PAINT curator acts on.
    asks: dict[tuple, list[str]] = collections.defaultdict(list)
    for (gene_file, go), row in sorted(seen.items()):
        i = inv.get((gene_file, go), {})
        fix = row.get("paint_fix") or {}
        if row["verdict"] != "REMOVE_UPHELD" or fix.get("paint_action") in (None, "NONE"):
            continue
        key = (i.get("family"), i.get("ibd_node"), go, i.get("go_label"), row.get("ground"),
               fix["paint_action"], fix.get("target_node_id") or "")
        asks[key].append("/".join(gene_file.split("/")[1:3]))
    with open(HERE / "paint_requests.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family", "ibd_node", "go_id", "go_label", "ground", "paint_action", "target_node_id",
                    "reviewed_genes", "genes"])
        for key, genes in sorted(asks.items(), key=lambda kv: (kv[0][0] or "", kv[0][1] or "", kv[0][2])):
            w.writerow([*key, len(genes), "; ".join(sorted(genes))])
    print("PAINT change requests:", len(asks), "over", len({k[:3] for k in asks}), "node-term pairs")

    docs: dict[str, dict] = {}
    for (gene_file, go), row in sorted(seen.items()):
        doc = docs.setdefault(gene_file, safe_load(Path(gene_file).read_text()))
        actions = {
            (a.get("review") or {}).get("action")
            for a in doc["existing_annotations"]
            if a.get("evidence_type") == "IBA" and a["term"]["id"] == go
        }
        want = "REMOVE" if row["verdict"] == "REMOVE_UPHELD" else row.get("new_action")
        if want not in actions:
            print(f"MISMATCH {gene_file} {go}: record says {want}, review has {sorted(map(str, actions))} ({row['_batch']})")

    by_node = collections.defaultdict(set)
    for (gene_file, go), row in seen.items():
        node = inv.get((gene_file, go), {}).get("ibd_node")
        fix = row.get("paint_fix") or {}
        if node:
            by_node[(node, go)].add((fix.get("paint_action"), fix.get("target_node_id"), row["verdict"], row.get("new_action")))
    for (node, go), fixes in sorted(by_node.items()):
        if len(fixes) > 1:
            print(f"DIFFERS {node} {go}: {sorted(map(str, fixes))}")


if __name__ == "__main__":
    main()
