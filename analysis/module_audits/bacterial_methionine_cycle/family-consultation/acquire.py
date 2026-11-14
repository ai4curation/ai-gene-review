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
        for f in [
            "PTHR11964",
            "PTHR23420",
            "PTHR46832",
            "PTHR35799",
            "PTHR45833",
            "PTHR30519",
        ]
    ]
    jobs += [
        (f"{a}-uniprot.json", f"https://rest.uniprot.org/uniprotkb/{a}.json")
        for a in [
            "Q88D60",
            "A0A140FWS3",
            "Q88KB5",
            "Q88JF1",
            "Q88JF0",
            "P0AF12",
            "P45578",
            "Q6F6Z8",
            "P05694",
            "P39954",
            "B5DFN2",
            "P23526",
            "P0A817",
            "P13009",
        ]
    ]
    jobs += [
        (
            "go-terms.json",
            "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
            + ",".join(
                [
                    "GO:0003871",
                    "GO:0008705",
                    "GO:0043768",
                    "GO:0004013",
                    "GO:0033353",
                    "GO:0004478",
                    "GO:0006556",
                    "GO:0008782",
                    "GO:0008930",
                    "GO:0009372",
                    "GO:0009507",
                    "GO:0048269",
                    "GO:0005829",
                    "GO:0046653",
                    "GO:0071265",
                ]
            ),
        )
    ]
    with ThreadPoolExecutor(max_workers=4) as pool:
        output = list(pool.map(get, jobs))
    (HERE / "acquisition.json").write_text(json.dumps(output, indent=2) + "\n")
    trees = {}
    for family in [
        "PTHR11964",
        "PTHR23420",
        "PTHR46832",
        "PTHR35799",
        "PTHR45833",
        "PTHR30519",
    ]:
        trees[family] = compact_tree(
            json.loads((HERE / f"{family}-tree.json").read_text())
        )
    (HERE / "trees-compact.json").write_text(json.dumps(trees, indent=2) + "\n")
    print([(k, len(v["leaves"])) for k, v in trees.items()])


if __name__ == "__main__":
    main()
