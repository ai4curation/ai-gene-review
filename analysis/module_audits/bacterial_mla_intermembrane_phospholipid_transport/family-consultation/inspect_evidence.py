"""Derive exact reference-tree/sequence scope and target classification records."""

import gzip
import hashlib
import json
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def main():
    trees = json.loads((HERE / "trees-compact.json").read_text())
    evidence = {}
    for family, tree in trees.items():
        msa = json.loads(gzip.decompress((HERE / f"{family}-msa.json.gz").read_bytes()))
        seqs = {
            s["persistent_id"]: s["sequence"]
            for s in msa["search"]["MSA_list"]["sequence_info"]
        }
        d = yaml.safe_load(
            (ROOT / f"interpro/panther/{family}/{family}-review.yaml").read_text()
        )
        leaves = []
        for node, member in sorted(tree["leaves"].items()):
            seq = "".join(c for c in seqs[node] if c.isalpha()).upper()
            leaves.append(
                {
                    "ptn": node,
                    **member,
                    "sequence_length": len(seq),
                    "sequence_sha256": hashlib.sha256(seq.encode()).hexdigest(),
                    "walker_a_candidates": [
                        m.group() for m in re.finditer(r"G....GK[ST]", seq)
                    ],
                    "abc_signature_candidates": [
                        m.group() for m in re.finditer(r"LS.G[QE]", seq)
                    ],
                }
            )
        nodes = []
        for n in d["node_assessments"]:
            ptn = n["node_id"].split(":")[-1]
            below = tree["under"].get(ptn, [ptn] if ptn in tree["leaves"] else [])
            nodes.append(
                {
                    "ptn": ptn,
                    "go_id": n["asserted_term"]["id"],
                    "evidence": n["evidence"],
                    "leaves": below,
                    "subfamilies": sorted(
                        {tree["leaves"][x]["subfamily"] for x in below}
                    ),
                }
            )
        evidence[family] = {
            "reference_leaves": leaves,
            "assessed_nodes": nodes,
            "limit": "Reference-tree coverage is incomplete; absence is not absence of family membership or biological function. Motif matches support architecture, not substrate specificity.",
        }
    (HERE / "phylogeny-evidence.json").write_text(
        json.dumps(evidence, indent=2, sort_keys=True) + "\n"
    )
    targets = []
    for org, genes in {
        "ECOLI": ["mlaA", "mlaB", "mlaC", "mlaD", "mlaE", "mlaF"],
        "PSEPK": ["vacJ", "ttg2E", "ttg2D", "mlaD", "mlaE", "mlaF"],
        "BORPE": ["BP3757", "BP3758", "BP3759", "BP3760", "BP3761"],
        "PSEAE": ["ttg2D"],
    }.items():
        for gene in genes:
            path = ROOT / f"genes/{org}/{gene}/{gene}-uniprot.txt"
            if not path.exists():
                continue
            text = path.read_text()
            acc = re.search(r"^AC   (\w+)", text, re.M)[1]
            ids = re.findall(r"^DR   PANTHER; ([^;]+);", text, re.M)
            targets.append(
                {
                    "accession": acc,
                    "gene": f"{org}/{gene}",
                    "source": str(path.relative_to(ROOT)),
                    "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "panther_ids": ids,
                    "reference_tree_leaves": [
                        {"family": f, "ptn": p, **x}
                        for f, t in trees.items()
                        for p, x in t["leaves"].items()
                        if x["uniprot"] == acc
                    ],
                }
            )
    (HERE / "target-membership.json").write_text(json.dumps(targets, indent=2) + "\n")
    print("families", len(evidence), "targets", len(targets))


if __name__ == "__main__":
    main()
