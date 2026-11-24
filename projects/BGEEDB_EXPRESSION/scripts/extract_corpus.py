"""Collect reviewed human GO annotations and the matching Bgee calls.

Reads every ``genes/human/*/*-ai-review.yaml``, keeps each existing annotation
with its evidence code and the reviewer's action, attaches the Ensembl gene id
from the UniProt ``DR   Bgee;`` line, and streams the Bgee human "simple" call
file once to pull present/absent calls for those genes.

Outputs (git-ignored cache; regenerate with this script):
    .cache/bgee_expression/corpus_annotations.tsv
    .cache/bgee_expression/corpus_calls.pkl

Usage (from repo root):
    uv run python projects/BGEEDB_EXPRESSION/scripts/extract_corpus.py
"""

from __future__ import annotations

import csv
import pickle
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import bgee_common as bc  # noqa: E402

try:
    Loader = yaml.CSafeLoader
except AttributeError:  # pragma: no cover
    Loader = yaml.SafeLoader

OUT_ANN = bc.CACHE / "corpus_annotations.tsv"
OUT_CALLS = bc.CACHE / "corpus_calls.pkl"
FIELDS = [
    "gene",
    "uniprot",
    "ensembl",
    "go_id",
    "go_label",
    "aspect",
    "evidence",
    "action",
    "negated",
    "reference",
    "in_core_process",
]


def core_process_ids(doc: dict) -> set[str]:
    ids = set()
    for cf in doc.get("core_functions") or []:
        for t in cf.get("directly_involved_in") or []:
            if isinstance(t, dict) and t.get("id"):
                ids.add(t["id"])
    return ids


def main() -> None:
    go = bc.load_go_anatomy()
    rows = []
    genes: dict[str, str] = {}
    paths = sorted(bc.REPO.glob("genes/human/*/*-ai-review.yaml"))
    for i, path in enumerate(paths):
        gene = path.parent.name
        if path.name != f"{gene}-ai-review.yaml":
            continue
        try:
            doc = yaml.load(path.read_text(), Loader=Loader) or {}
        except yaml.YAMLError as exc:
            print(f"skip {path}: {exc}", file=sys.stderr)
            continue
        ens = bc.bgee_gene_id(path.parent / f"{gene}-uniprot.txt")
        if not ens:
            continue
        genes[ens] = gene
        core = core_process_ids(doc)
        for ann in doc.get("existing_annotations") or []:
            term = ann.get("term") or {}
            gid = term.get("id")
            if not gid or not str(gid).startswith("GO:"):
                continue
            review = ann.get("review") or {}
            rows.append(
                {
                    "gene": gene,
                    "uniprot": doc.get("id", ""),
                    "ensembl": ens,
                    "go_id": gid,
                    "go_label": term.get("label", ""),
                    "aspect": go.namespaces.get(gid, ""),
                    "evidence": ann.get("evidence_type", ""),
                    "action": review.get("action", ""),
                    "negated": "true" if ann.get("negated") else "",
                    "reference": ann.get("original_reference_id", ""),
                    "in_core_process": "true" if gid in core else "",
                }
            )
        if i % 500 == 0:
            print(f"  {i}/{len(paths)} reviews", file=sys.stderr)
    OUT_ANN.parent.mkdir(parents=True, exist_ok=True)
    with OUT_ANN.open("w", newline="") as fh:
        w = csv.DictWriter(fh, FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} annotations on {len(genes)} genes -> {OUT_ANN}", file=sys.stderr)
    calls = bc.read_simple_calls("human", genes)
    with OUT_CALLS.open("wb") as fh:
        pickle.dump({"calls": calls, "symbols": genes}, fh)
    print(f"Bgee calls for {len(calls)}/{len(genes)} genes -> {OUT_CALLS}", file=sys.stderr)


if __name__ == "__main__":
    main()
