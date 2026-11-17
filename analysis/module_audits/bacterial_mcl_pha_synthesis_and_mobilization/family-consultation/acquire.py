"""Acquire official reference evidence into this consultation; never refresh raw caches."""

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from ai_gene_review.etl.panther_trees import compact_tree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def get(spec):
    name, url = spec
    path = HERE / name
    if path.exists():
        return {
            "path": str(path.relative_to(ROOT)),
            "url": url,
            "status": "existing_not_refreshed",
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    result = requests.get(url, timeout=60)
    result.raise_for_status()
    path.write_bytes(result.content)
    return {
        "path": str(path.relative_to(ROOT)),
        "url": result.url,
        "status": result.status_code,
        "retrieved": "2026-11-07",
        "sha256": hashlib.sha256(result.content).hexdigest(),
    }


def main():
    jobs = [
        (
            f"{f}-tree.json",
            f"https://pantherdb.org/services/oai/pantherdb/treeinfo?family={f}",
        )
        for f in ["PTHR36837", "PTHR43194", "PTHR43433", "PTHR43798"]
    ]
    jobs += [
        (f"{a}-uniprot.json", f"https://rest.uniprot.org/uniprotkb/{a}.json")
        for a in [
            "P23608",
            "P96935",
            "O07732",
            "Q9BV23",
            "P13001",
            "Q88D25",
            "Q88D23",
            "Q88D24",
            "O85207",
            "P26494",
            "P26496",
            "P26495",
            "Q51553",
        ]
    ]
    jobs += [
        (
            "go-terms.json",
            "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
            + ",".join(
                [
                    "GO:0008415",
                    "GO:0016787",
                    "GO:0004806",
                    "GO:0046503",
                    "GO:0047372",
                    "GO:0046464",
                    "GO:0090499",
                    "GO:0009102",
                    "GO:0004016",
                    "GO:0006171",
                    "GO:0042619",
                    "GO:0042620",
                ]
            ),
        )
    ]
    with ThreadPoolExecutor(max_workers=4) as pool:
        output = list(pool.map(get, jobs))
    (HERE / "acquisition.json").write_text(json.dumps(output, indent=2) + "\n")
    trees = {}
    for family in ["PTHR36837", "PTHR43194", "PTHR43433", "PTHR43798"]:
        trees[family] = compact_tree(
            json.loads((HERE / f"{family}-tree.json").read_text())
        )
    (HERE / "trees-compact.json").write_text(json.dumps(trees, indent=2) + "\n")
    print([(k, len(v["leaves"])) for k, v in trees.items()])


if __name__ == "__main__":
    main()
