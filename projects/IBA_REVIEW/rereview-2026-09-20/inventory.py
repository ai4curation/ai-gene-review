"""Freeze source coverage once; derive progress only from explicit manual records."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import subprocess

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TG = ROOT / "projects/TREEGRAFTER/rereview-2026-09-20"
RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE"}


def write_tsv(path, rows, fields):
    with path.open("w") as stream:
        writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def create():
    if (HERE / "baseline.json").exists():
        raise SystemExit("Baseline already exists; refusing to replace it.")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    project = subprocess.check_output(["git", "show", f"{commit}:projects/IBA_REVIEW.md"], cwd=ROOT, text=True)
    names = set(yaml.load(project.split("---", 2)[1], Loader=yaml.CSafeLoader)["genes"])
    paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", commit, "genes"], cwd=ROOT, text=True).splitlines()
    paths = [p for p in paths if p.endswith("-ai-review.yaml")]
    cat = subprocess.Popen(["git", "cat-file", "--batch"], cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    genes, annotations = [], []
    try:
        for path in paths:
            cat.stdin.write(f"{commit}:{path}\n".encode())
            cat.stdin.flush()
            header = cat.stdout.readline().decode().split()
            raw = cat.stdout.read(int(header[2]))
            assert cat.stdout.read(1) == b"\n"
            doc = yaml.load(raw, Loader=yaml.CSafeLoader)
            if not isinstance(doc, dict):
                raise ValueError(f"Not a review mapping: {path}")
            rows = doc.get("existing_annotations") or []
            own = []
            for index, ann in enumerate(rows, 1):
                method = "IBA" if ann.get("evidence_type") == "IBA" else "TreeGrafter" if ann.get("evidence_type") == "IEA" and ann.get("original_reference_id") == "GO_REF:0000118" else None
                if not method:
                    continue
                row = dict(gene_file=path, annotation_index=index, method=method,
                           term_id=ann["term"]["id"], term_label=ann["term"]["label"],
                           evidence_type=ann["evidence_type"], original_reference_id=ann.get("original_reference_id", ""),
                           action=(ann.get("review") or {}).get("action", "UNREVIEWED"),
                           negated=bool(ann.get("negated")), qualifier=ann.get("qualifier", ""), isoform=ann.get("isoform", ""))
                own.append(row)
            named = doc.get("gene_symbol") in names or Path(path).parent.name in names
            if not own and not named:
                continue
            counts = Counter(a["method"] for a in own)
            disputed = sum(a["action"] not in RETAINED for a in own)
            genes.append(dict(gene_file=path, gene_symbol=doc.get("gene_symbol", ""),
                              uniprot_id=doc.get("id", ""), named_iba_gene=named,
                              all_annotations=len(rows), iba_annotations=counts["IBA"],
                              treegrafter_annotations=counts["TreeGrafter"], disputed_annotations=disputed,
                              priority=1 if disputed else 2))
            annotations.extend(own)
    finally:
        cat.stdin.close()
        cat.wait()
    genes.sort(key=lambda g: (g["priority"], -g["disputed_annotations"], g["gene_file"]))
    write_tsv(HERE / "inventory.tsv", genes, list(genes[0]))
    write_tsv(HERE / "annotations.tsv", annotations, list(annotations[0]))
    (HERE / "baseline.json").write_text(json.dumps(dict(commit=commit, gene_count=len(genes),
        propagated_annotations=len(annotations), methods=dict(Counter(a["method"] for a in annotations)),
        disputed_genes=sum(g["priority"] == 1 for g in genes)), indent=2) + "\n")


def progress():
    baseline = json.loads((HERE / "baseline.json").read_text())
    inventory = list(csv.DictReader((HERE / "inventory.tsv").open(), delimiter="\t"))
    records = {}
    for directory in (HERE, TG):
        for path in sorted(directory.glob("*.yaml")):
            data = yaml.load(path.read_text(), Loader=yaml.CSafeLoader) or {}
            for record in data.get("genes", []):
                gene = record["gene_file"]
                if gene in records:
                    raise ValueError(f"Duplicate manual assessment for {gene}; reconcile the batch records")
                records[gene] = (record, str(path.relative_to(ROOT)))
    rows = []
    for gene in inventory:
        record, source = records.get(gene["gene_file"], ({}, ""))
        status = record.get("status", "unreviewed")
        if status == "reviewed" and record.get("scope") != "full_gene":
            status = "focused_only"
        rows.append(dict(gene_file=gene["gene_file"], priority=gene["priority"], status=status,
                         scope=record.get("scope", ""), audit_record=source))
    extra = set(records) - {g["gene_file"] for g in inventory}
    if extra:
        raise ValueError(f"Reviewed genes absent from baseline: {sorted(extra)}")
    write_tsv(HERE / "progress.tsv", rows, list(rows[0]))
    report = dict(baseline=baseline, progress=dict(Counter(r["status"] for r in rows)))
    (HERE / "progress.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--create", action="store_true")
    args = parser.parse_args()
    if args.create:
        create()
    progress()
