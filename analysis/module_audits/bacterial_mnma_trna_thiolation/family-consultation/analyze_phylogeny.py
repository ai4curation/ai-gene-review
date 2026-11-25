"""Reproduce exact node/member and MSA observations without inferring function."""

import csv
import gzip
import json
from collections import Counter
from pathlib import Path

from ai_gene_review.etl.panther_trees import (
    compact_tree,
    leaf_nodes_for,
    ancestors_of,
    leaves_below,
)

P = Path(__file__).resolve().parent
families = [
    "PTHR" + n
    for n in ["11601", "11933", "33279", "34874", "37010", "37526", "38780", "43586"]
]
accessions = [
    "P0A6B7",
    "Q88PK8",
    "O34599",
    "Q72LH2",
    "Q72HV9",
    "P25745",
    "Q88FR9",
    "O35020",
    "Q72GX1",
    "O75648",
    "P0A890",
    "Q88L21",
    "P45532",
    "Q88FT9",
    "P0AB18",
    "Q88FT6",
    "P45530",
    "Q88FT7",
    "P45531",
    "Q88FT8",
]
output = {}
for fam in families:
    tree = compact_tree(
        json.loads(gzip.decompress((P / f"{fam}-treeinfo.json.gz").read_bytes()))
    )
    msa = json.loads(gzip.decompress((P / f"{fam}-familymsa.json.gz").read_bytes()))[
        "search"
    ]["MSA_list"]["sequence_info"]
    seqs = {x["persistent_id"]: x["sequence"].replace(".", "-") for x in msa}
    entries = list(
        csv.DictReader(Path(f"interpro/panther/{fam}/{fam}-entries.csv").open())
    )
    paintpath = Path(f"interpro/panther/{fam}/{fam}-paint.tsv")
    paint = (
        list(csv.DictReader(paintpath.open(), delimiter="\t"))
        if paintpath.exists()
        else []
    )
    nodes = {r["node"] for r in paint}
    target = {
        a: {
            "leaves": leaf_nodes_for(tree, a),
            "ancestral_paint_nodes": sorted(
                set().union(
                    *(
                        ancestors_of(tree, leaf_id)
                        for leaf_id in leaf_nodes_for(tree, a)
                    )
                )
                & nodes
            ),
            "entries": [x for x in entries if x["id"] == a],
        }
        for a in accessions
        if leaf_nodes_for(tree, a) or any(x["id"] == a for x in entries)
    }
    scope = {
        n: {
            "leaf_count": len(leaves_below(tree, n)),
            "subfamilies": dict(
                Counter(
                    tree["leaves"][leaf_id]["subfamily"]
                    for leaf_id in leaves_below(tree, n)
                )
            ),
            "leaves": {
                leaf_id: tree["leaves"][leaf_id] for leaf_id in leaves_below(tree, n)
            },
        }
        for n in sorted(nodes)
    }
    out = {
        "tree_leaf_count": len(tree["leaves"]),
        "msa_sequences": len(seqs),
        "msa_lengths": dict(Counter(map(len, seqs.values()))),
        "inventory_subfamilies": dict(Counter(x["subfamily"] for x in entries)),
        "targets": target,
        "nodes": scope,
    }
    if fam == "PTHR11933":
        profiles = {}
        for a, positions in [
            ("P25745", [99, 102, 199]),
            ("O35020", [101, 104, 200]),
            ("Q72GX1", [105, 108, 200]),
        ]:
            for leaf in leaf_nodes_for(tree, a):
                seq = seqs[leaf]
                mapping = {}
                n = 0
                for i, c in enumerate(seq):
                    if c != "-":
                        n += 1
                        if n in positions:
                            mapping[n] = {"residue": c, "alignment_column": i + 1}
                profiles[a] = {"leaf": leaf, "positions": mapping}
        out["anchor_msa_observations"] = profiles
    output[fam] = out
(P / "tree-scope.json").write_text(json.dumps(output, indent=2) + "\n")
for fam, v in output.items():
    print(fam, "leaves", v["tree_leaf_count"], "SF", v["inventory_subfamilies"])
    print(
        "targets",
        [(a, x["leaves"], x["ancestral_paint_nodes"]) for a, x in v["targets"].items()],
    )
    print(
        "nodes", [(n, x["leaf_count"], x["subfamilies"]) for n, x in v["nodes"].items()]
    )
    if "anchor_msa_observations" in v:
        print(v["anchor_msa_observations"])
