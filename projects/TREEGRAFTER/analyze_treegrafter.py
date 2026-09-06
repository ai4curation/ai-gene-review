#!/usr/bin/env python3
"""Evaluate TreeGrafter inferences against AIGR reviews.

TreeGrafter (Tang et al. 2019, doi:10.1093/bioinformatics/bty625) is the
algorithm bundled into InterProScan that **grafts** a query protein onto the
most appropriate PANTHER reference phylogenetic tree and propagates the GO
annotations of the grafting node. Crucially, this is distinct from PAINT/IBA:

  * PAINT (GO_Central) annotations are made by curators directly on genes that
    are already *in* the PANTHER reference tree; they surface in GOA as
    ``IBA`` / ``GO_REF:0000033`` / assigned-by ``GO_Central``.
  * TreeGrafter inferences are for sequences *not* in the reference tree — they
    are grafted on and propagated automatically, surfacing in GOA as
    ``IEA`` / ``GO_REF:0000118`` / assigned-by ``TreeGrafter`` / with-from
    ``PANTHER:...``.

This script evaluates the TreeGrafter set (GO_REF:0000118). For contrast it
also reports the PAINT/IBA set (GO_REF:0000033), but that is a *different*
pipeline and is labelled as such. ``GO_REF:0000120`` is UniProt's "combined
multiple IEA methods" reference (InterPro/ARBA/RHEA/...) and is NOT TreeGrafter,
so it is excluded.

Outputs (written next to this script):
  - treegrafter_review.tsv     one row per reviewed TreeGrafter (GO_REF:0000118) annotation
  - treegrafter_summary.tsv    action counts + most-downgraded terms, with the PAINT/IBA contrast

Run:
  uv run --with pyyaml projects/TREEGRAFTER/analyze_treegrafter.py
or:
  python3 projects/TREEGRAFTER/analyze_treegrafter.py
"""
from __future__ import annotations

import csv
import glob
import os
from collections import Counter

import yaml

# The C loader is ~10x faster over the ~3k-file corpus; fall back to the pure-Python one.
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

TREEGRAFTER_REF = "GO_REF:0000118"  # IEA / assigned-by TreeGrafter / with-from PANTHER
PAINT_REF = "GO_REF:0000033"        # IBA / GO_Central — contrast only, NOT TreeGrafter


def annotations(doc: dict):
    for ann in doc.get("existing_annotations") or []:
        if isinstance(ann, dict):
            yield ann


def collect(files, ref: str, evidence: str):
    """Return per-annotation rows for annotations matching ref + evidence code."""
    rows = []
    for path in files:
        try:
            with open(path) as fh:
                doc = yaml.load(fh, Loader=LOADER)
        except Exception as exc:  # noqa: BLE001
            print(f"WARN: failed to parse {path}: {exc}")
            continue
        if not isinstance(doc, dict):
            continue
        gene = doc.get("gene_symbol", "")
        taxon = (doc.get("taxon") or {}).get("label", "")
        rel = os.path.relpath(path, ROOT)
        for ann in annotations(doc):
            if (ann.get("original_reference_id") or "") != ref:
                continue
            if ann.get("evidence_type") != evidence:
                continue
            review = ann.get("review") or {}
            term = ann.get("term") or {}
            rows.append({
                "gene": gene,
                "taxon": taxon,
                "term_id": term.get("id", ""),
                "term_label": term.get("label", ""),
                "action": (review.get("action") or "UNREVIEWED").strip(),
                "negated": bool(ann.get("negated", False)),
                "has_replacement": bool(review.get("proposed_replacement_terms")),
                "aspect": goa_aspect(rel, term.get("id", "")),
                "file": rel,
            })
    return rows


def action_counter(rows):
    return Counter(r["action"] for r in rows)


_ASPECT_CACHE: dict = {}
_ASPECT_NAMES = {"F": "molecular_function", "P": "biological_process",
                 "C": "cellular_component"}


def goa_aspect(review_rel_path: str, term_id: str) -> str:
    """GO aspect (molecular_function / biological_process / cellular_component)
    of ``term_id`` as recorded in the gene's cached GOA download (column
    ``GO ASPECT``). Cached per gene directory; '' when not found."""
    gene_dir = os.path.dirname(os.path.join(ROOT, review_rel_path))
    if gene_dir not in _ASPECT_CACHE:
        table = {}
        try:
            for name in os.listdir(gene_dir):
                if name.endswith("-goa.tsv"):
                    with open(os.path.join(gene_dir, name)) as fh:
                        header = next(fh, "").rstrip("\n").split("\t")
                        try:
                            i_term, i_asp = header.index("GO TERM"), header.index("GO ASPECT")
                        except ValueError:
                            continue
                        for line in fh:
                            cols = line.rstrip("\n").split("\t")
                            if len(cols) > max(i_term, i_asp):
                                # Older downloads use the one-letter aspect codes.
                                table.setdefault(cols[i_term],
                                                 _ASPECT_NAMES.get(cols[i_asp], cols[i_asp]))
        except FileNotFoundError:
            pass
        _ASPECT_CACHE[gene_dir] = table
    return _ASPECT_CACHE[gene_dir].get(term_id, "")


def main() -> None:
    files = sorted(glob.glob(os.path.join(ROOT, "genes", "**", "*-ai-review.yaml"),
                             recursive=True))

    tg_rows = collect(files, TREEGRAFTER_REF, "IEA")
    paint_rows = collect(files, PAINT_REF, "IBA")

    # Per-annotation TSV for the TreeGrafter set.
    out_rows = os.path.join(HERE, "treegrafter_review.tsv")
    fields = ["gene", "taxon", "term_id", "term_label", "action", "negated",
              "has_replacement", "aspect", "file"]
    with open(out_rows, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(tg_rows)

    tg_actions = action_counter(tg_rows)
    paint_actions = action_counter(paint_rows)
    problem_actions = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}
    problem_terms = Counter(
        (r["term_id"], r["term_label"]) for r in tg_rows
        if r["action"] in problem_actions
    )

    out_sum = os.path.join(HERE, "treegrafter_summary.tsv")
    with open(out_sum, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["metric", "value"])
        w.writerow(["total_review_files", len(files)])
        w.writerow(["genes_with_treegrafter", len({r["file"] for r in tg_rows})])
        w.writerow(["treegrafter_annotations (GO_REF:0000118, IEA)", len(tg_rows)])
        w.writerow(["paint_iba_annotations (GO_REF:0000033, IBA; contrast only)",
                    len(paint_rows)])
        w.writerow([])
        w.writerow(["TreeGrafter action", "count"])
        for action, n in tg_actions.most_common():
            w.writerow([action, n])
        w.writerow([])
        w.writerow(["PAINT/IBA action (contrast, NOT TreeGrafter)", "count"])
        for action, n in paint_actions.most_common():
            w.writerow([action, n])
        w.writerow([])
        w.writerow(["TreeGrafter action by GO aspect", "aspect", "count", "pct_of_aspect"])
        by_aspect = Counter(r["aspect"] or "unknown" for r in tg_rows)
        for aspect, total in by_aspect.most_common():
            for action, n in Counter(r["action"] for r in tg_rows
                                     if (r["aspect"] or "unknown") == aspect).most_common():
                w.writerow([action, aspect, n, f"{100 * n / total:.1f}"])
        w.writerow([])
        w.writerow(["TreeGrafter annotations by taxon", "count", "accept_pct",
                    "downgraded_pct (REMOVE/MODIFY/OVER)"])
        for taxon, total in Counter(r["taxon"] for r in tg_rows).most_common(15):
            sub = [r for r in tg_rows if r["taxon"] == taxon]
            acc = sum(1 for r in sub if r["action"] == "ACCEPT")
            bad = sum(1 for r in sub if r["action"] in problem_actions)
            w.writerow([taxon, total, f"{100 * acc / total:.1f}", f"{100 * bad / total:.1f}"])
        w.writerow([])
        w.writerow(["top_problematic_treegrafter_terms (REMOVE/MODIFY/OVER)", "count"])
        for (tid, label), n in problem_terms.most_common(25):
            w.writerow([f"{tid} {label}", n])

    def report(title, rows, counts):
        total = len(rows)
        print(f"\n{title}: {total} annotations across "
              f"{len({r['file'] for r in rows})} genes")
        for action, n in counts.most_common():
            pct = 100 * n / total if total else 0
            print(f"  {action:24s} {n:5d}  ({pct:5.1f}%)")

    print(f"Scanned {len(files)} review files")
    report("TreeGrafter (GO_REF:0000118, IEA)", tg_rows, tg_actions)
    report("PAINT/IBA (GO_REF:0000033, IBA) — contrast, NOT TreeGrafter",
           paint_rows, paint_actions)
    print("\nTreeGrafter down-grade rate (REMOVE/MODIFY/OVER) by GO aspect:")
    for aspect, total in Counter(r["aspect"] or "unknown" for r in tg_rows).most_common():
        bad = sum(1 for r in tg_rows if (r["aspect"] or "unknown") == aspect
                  and r["action"] in problem_actions)
        print(f"  {aspect:22s} {bad:4d}/{total:<4d} ({100 * bad / total:5.1f}%)")
    print(f"\nWrote {os.path.relpath(out_rows, ROOT)}")
    print(f"Wrote {os.path.relpath(out_sum, ROOT)}")


if __name__ == "__main__":
    main()
