"""Acquire compact, provenance-recorded official evidence without altering caches."""

import gzip
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from ai_gene_review.etl.panther_trees import compact_tree

HERE = Path(__file__).resolve().parent
FAMILIES = [
    "PTHR30035",
    "PTHR36573",
    "PTHR43023",
    "PTHR30188",
    "PTHR33371",
    "PTHR35849",
]


def get(job):
    name, url = job
    path = HERE / name
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite {path}")
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    data = response.content
    if path.suffix == ".gz":
        path.write_bytes(gzip.compress(data, mtime=0))
    else:
        path.write_bytes(data)
    return {
        "path": name,
        "url": response.url,
        "status": response.status_code,
        "retrieved": "2026-11-07",
        "response_sha256": hashlib.sha256(data).hexdigest(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main():
    jobs = [
        (
            f"{f}-{kind}.json.gz",
            f"https://pantherdb.org/services/oai/pantherdb/{endpoint}?family={f}",
        )
        for f in FAMILIES
        for kind, endpoint in [("tree", "treeinfo"), ("msa", "familymsa")]
    ]
    terms = [
        "GO:0120010",
        "GO:0120014",
        "GO:1990531",
        "GO:0043190",
        "GO:0005319",
        "GO:0005543",
        "GO:0009274",
        "GO:0006974",
    ]
    jobs.append(
        (
            "ontology.json",
            "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
            + ",".join(terms),
        )
    )
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(get, jobs))
    (HERE / "acquisition.json").write_text(json.dumps(results, indent=2) + "\n")
    trees = {
        f: compact_tree(
            json.loads(gzip.decompress((HERE / f"{f}-tree.json.gz").read_bytes()))
        )
        for f in FAMILIES
    }
    (HERE / "trees-compact.json").write_text(
        json.dumps(trees, sort_keys=True, separators=(",", ":")) + "\n"
    )
    print({f: len(t["leaves"]) for f, t in trees.items()})


if __name__ == "__main__":
    main()
