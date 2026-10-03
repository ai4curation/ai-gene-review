#!/usr/bin/env python3
"""Join Human Protein Atlas (HPA) subcellular data with HPA-sourced GO annotations
in our human gene reviews.

HPA exports GO cellular-component annotations to GOA as IDA with reference
GO_REF:0000052 (pre-2013: PMID:18029348). The HPA download records, per gene and
per location, a reliability grade (Enhanced / Supported / Approved / Uncertain).
This script joins each HPA-sourced annotation in genes/human/*/*-ai-review.yaml
with the HPA per-location reliability and our review action, so the two
evidence frameworks can be compared.

Usage (from repo root):
    uv run python projects/HUMAN_PROTEIN_ATLAS/scripts/hpa_join.py \
        [--hpa projects/HUMAN_PROTEIN_ATLAS/data/subcellular_location.tsv]

Outputs (projects/HUMAN_PROTEIN_ATLAS/data/):
    hpa_review_join.tsv   one row per HPA-sourced annotation in a review
    hpa_summary.md        cross-tabulations (printed to stdout as well)
    hpa_worklist.tsv      annotations where the two frameworks disagree:
                          tier 1 = our review rejects/doubts an HPA call
                          tier 2 = HPA now grades the location Approved/Uncertain
                                   or no longer reports it (stale in GOA)
"""

import argparse
import csv
import io
import re
import urllib.request
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HPA_URL = "https://www.proteinatlas.org/download/tsv/subcellular_location.tsv.zip"
HPA_REFS = {"GO_REF:0000052", "PMID:18029348"}
GRADES = ["Enhanced", "Supported", "Approved", "Uncertain"]
PROJECT = Path("projects/HUMAN_PROTEIN_ATLAS")
GO_RE = re.compile(r"^(.*) \((GO:\d{7})\)$")


def fetch_hpa(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(HPA_URL) as resp:
        data = resp.read()
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        name = [n for n in zf.namelist() if n.endswith(".tsv")][0]
        path.write_bytes(zf.read(name))


def load_hpa(path: Path) -> dict:
    """symbol -> {reliability, main, additional, go: {GO id: (location, grade)}}"""
    out = {}
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            loc_grade = {}
            for g in GRADES:
                for loc in filter(None, (row.get(g) or "").split(";")):
                    loc_grade[loc] = g
            go = {}
            for item in filter(None, (row.get("GO id") or "").split(";")):
                m = GO_RE.match(item.strip())
                if m:
                    loc, gid = m.groups()
                    go[gid] = (loc, loc_grade.get(loc, ""))
            out[row["Gene name"]] = {
                "ensembl": row["Gene"],
                "reliability": row["Reliability"],
                "main": row["Main location"],
                "additional": row["Additional location"],
                "go": go,
            }
    return out


def iter_hpa_annotations(review_dir: Path):
    for f in sorted(review_dir.glob("*/*-ai-review.yaml")):
        try:
            doc = yaml.safe_load(f.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        for ann in doc.get("existing_annotations") or []:
            if ann.get("original_reference_id") not in HPA_REFS:
                continue
            term = ann.get("term") or {}
            review = ann.get("review") or {}
            yield {
                "gene": doc.get("gene_symbol") or f.parent.name,
                "uniprot": doc.get("id", ""),
                "go_id": term.get("id", ""),
                "go_label": term.get("label", ""),
                "reference": ann.get("original_reference_id"),
                "negated": bool(ann.get("negated")),
                "action": review.get("action", "") or "",
                "file": str(f),
            }


def crosstab(rows, rkey, ckey, cols):
    tab = defaultdict(Counter)
    for r in rows:
        tab[r[rkey]][r[ckey]] += 1
    lines = ["| " + rkey + " | " + " | ".join(cols) + " | total |",
             "|" + "---|" * (len(cols) + 2)]
    for k in sorted(tab, key=lambda k: -sum(tab[k].values())):
        c = tab[k]
        lines.append(f"| {k or '(none)'} | " + " | ".join(str(c[x]) for x in cols)
                     + f" | {sum(c.values())} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hpa", type=Path, default=PROJECT / "data/subcellular_location.tsv")
    ap.add_argument("--reviews", type=Path, default=Path("genes/human"))
    ap.add_argument("--refresh", action="store_true", help="re-download HPA file")
    args = ap.parse_args()

    if args.refresh or not args.hpa.exists():
        fetch_hpa(args.hpa)
    hpa = load_hpa(args.hpa)

    rows = []
    for a in iter_hpa_annotations(args.reviews):
        h = hpa.get(a["gene"])
        if h is None:
            a.update(hpa_gene_reliability="NOT_IN_HPA", hpa_location="",
                     hpa_location_grade="", hpa_main="", hpa_status="gene not in HPA file")
        else:
            loc, grade = h["go"].get(a["go_id"], ("", ""))
            if loc:
                status = "main" if loc in h["main"].split(";") else "additional"
            else:
                status = "term not in current HPA GO mapping"
            a.update(hpa_gene_reliability=h["reliability"], hpa_location=loc,
                     hpa_location_grade=grade or ("(absent)" if not loc else ""),
                     hpa_main=h["main"], hpa_status=status)
        rows.append(a)

    out_dir = PROJECT / "data"
    out_dir.mkdir(parents=True, exist_ok=True)
    fields = ["gene", "uniprot", "go_id", "go_label", "reference", "negated", "action",
              "hpa_gene_reliability", "hpa_location", "hpa_location_grade",
              "hpa_status", "hpa_main", "file"]
    with (out_dir / "hpa_review_join.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    reject = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "UNDECIDED", "MODIFY"}
    stale = {"Approved", "Uncertain", "(absent)", ""}
    work = []
    for r in rows:
        tiers = []
        if r["action"] in reject:
            tiers.append("1")
        if r["hpa_location_grade"] in stale:
            tiers.append("2")
        if tiers:
            work.append({**r, "tier": ",".join(tiers)})
    work.sort(key=lambda r: (r["tier"], r["gene"], r["go_id"]))
    with (out_dir / "hpa_worklist.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["tier"] + fields, delimiter="\t",
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(work)

    actions = ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "MARK_AS_OVER_ANNOTATED",
               "REMOVE", "UNDECIDED", "PENDING"]
    genes = {r["gene"] for r in rows}
    hpa_rel = Counter(h["reliability"] for h in hpa.values())
    parts = [
        "# HPA vs. review actions (generated by scripts/hpa_join.py)\n",
        f"- HPA subcellular file: {len(hpa)} genes; gene-level reliability "
        + ", ".join(f"{g}={hpa_rel[g]}" for g in GRADES),
        f"- HPA-sourced annotations in human reviews: {len(rows)} across {len(genes)} genes",
        f"- Worklist (disagreements + stale calls): {len(work)} annotations across "
        f"{len({r['gene'] for r in work})} genes\n",
        "## Action by HPA per-location reliability\n",
        crosstab(rows, "hpa_location_grade", "action", actions),
        "\n## Action by whether HPA still reports the location\n",
        crosstab(rows, "hpa_status", "action", actions),
        "\n## Action by GO term (top terms)\n",
        crosstab(rows, "go_label", "action", actions),
    ]
    summary = "\n".join(parts) + "\n"
    (out_dir / "hpa_summary.md").write_text(summary)
    print(summary)


if __name__ == "__main__":
    main()
