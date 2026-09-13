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

Two further electronic populations are reported as contrasts on the *same
genes* that carry TreeGrafter rows:

  * ``GO_REF:0000120`` / IEA / UniProt rows whose GOA ``WITH/FROM`` is a
    ``PANTHER:PTN...`` node — PANTHER-tree inferences relayed by UniProt's
    "combined IEA methods" reference (almost certainly TreeGrafter output under
    a different label).
  * ``GO_REF:0000002`` / IEA / InterPro rows — InterPro2GO signature-based
    transfer, the natural non-phylogenetic comparator.

Outputs (written next to this script):
  - treegrafter_review.tsv     one row per reviewed TreeGrafter (GO_REF:0000118) annotation
  - treegrafter_contrast.tsv   one row per reviewed UniProt-relayed-PANTHER / InterPro2GO
                               annotation on the TreeGrafter genes (``set`` column)
  - treegrafter_summary.tsv    action counts + most-downgraded terms, with the PAINT/IBA,
                               UniProt-PANTHER and InterPro2GO contrasts and a same-term
                               TreeGrafter-vs-InterPro2GO head-to-head

Run:
  uv run --with pyyaml projects/TREEGRAFTER/analyze_treegrafter.py
or:
  python3 projects/TREEGRAFTER/analyze_treegrafter.py
"""
from __future__ import annotations

import csv
import glob
import os
import re
from collections import Counter

import yaml

# The C loader is ~10x faster over the ~3k-file corpus; fall back to the pure-Python one.
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

TREEGRAFTER_REF = "GO_REF:0000118"  # IEA / assigned-by TreeGrafter / with-from PANTHER
PAINT_REF = "GO_REF:0000033"        # IBA / GO_Central — contrast only, NOT TreeGrafter
UNIPROT_IEA_REF = "GO_REF:0000120"  # IEA / UniProt combined methods; PANTHER subset only
INTERPRO2GO_REF = "GO_REF:0000002"  # IEA / InterPro signature -> GO transfer
PROBLEM_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}


def annotations(doc: dict):
    for ann in doc.get("existing_annotations") or []:
        if isinstance(ann, dict):
            yield ann


def collect(files, ref: str, evidence: str, with_from_re: "re.Pattern | None" = None):
    """Return per-annotation rows for annotations matching ref + evidence code.

    ``with_from_re``, when given, additionally requires the matching GOA row
    (same term + reference in the gene's cached GOA) to have a ``WITH/FROM``
    matching the pattern — used to pick out the PANTHER-derived subset of
    UniProt's combined-IEA reference."""
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
            if with_from_re is not None:
                wf = goa_with_from(rel, term.get("id", ""), ref)
                if not with_from_re.search(wf):
                    continue
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


_GOA_CACHE: dict = {}
_ASPECT_NAMES = {"F": "molecular_function", "P": "biological_process",
                 "C": "cellular_component"}


def _goa_table(review_rel_path: str) -> dict:
    """Parse the gene's cached GOA once: {term_id: {"aspect": str,
    "with_from": {reference: with/from}}}."""
    gene_dir = os.path.dirname(os.path.join(ROOT, review_rel_path))
    if gene_dir in _GOA_CACHE:
        return _GOA_CACHE[gene_dir]
    table: dict = {}
    try:
        for name in os.listdir(gene_dir):
            if not name.endswith("-goa.tsv"):
                continue
            with open(os.path.join(gene_dir, name)) as fh:
                header = next(fh, "").rstrip("\n").split("\t")
                try:
                    i_term = header.index("GO TERM")
                    i_asp = header.index("GO ASPECT")
                    i_ref = header.index("REFERENCE")
                    i_wf = header.index("WITH/FROM")
                except ValueError:
                    continue
                for line in fh:
                    cols = line.rstrip("\n").split("\t")
                    if len(cols) <= max(i_term, i_asp, i_ref, i_wf):
                        continue
                    entry = table.setdefault(cols[i_term], {"aspect": "", "with_from": {}})
                    # Older downloads use the one-letter aspect codes.
                    entry["aspect"] = entry["aspect"] or _ASPECT_NAMES.get(cols[i_asp], cols[i_asp])
                    entry["with_from"].setdefault(cols[i_ref], cols[i_wf])
    except FileNotFoundError:
        pass
    _GOA_CACHE[gene_dir] = table
    return table


def goa_aspect(review_rel_path: str, term_id: str) -> str:
    """GO aspect of ``term_id`` per the gene's cached GOA; '' when not found."""
    return _goa_table(review_rel_path).get(term_id, {}).get("aspect", "")


def goa_with_from(review_rel_path: str, term_id: str, ref: str) -> str:
    """``WITH/FROM`` of the GOA row for (term, reference); '' when not found."""
    return _goa_table(review_rel_path).get(term_id, {}).get("with_from", {}).get(ref, "")


def main() -> None:
    files = sorted(glob.glob(os.path.join(ROOT, "genes", "**", "*-ai-review.yaml"),
                             recursive=True))

    tg_rows = collect(files, TREEGRAFTER_REF, "IEA")
    paint_rows = collect(files, PAINT_REF, "IBA")
    tg_genes = {r["file"] for r in tg_rows}
    # Contrast populations, restricted to the genes that carry TreeGrafter rows.
    up_panther_rows = [r for r in collect(files, UNIPROT_IEA_REF, "IEA",
                                          with_from_re=re.compile(r"PANTHER:PTN"))
                       if r["file"] in tg_genes]
    ip2go_rows = [r for r in collect(files, INTERPRO2GO_REF, "IEA")
                  if r["file"] in tg_genes]

    # Per-annotation TSV for the TreeGrafter set.
    out_rows = os.path.join(HERE, "treegrafter_review.tsv")
    fields = ["gene", "taxon", "term_id", "term_label", "action", "negated",
              "has_replacement", "aspect", "file"]
    with open(out_rows, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(tg_rows)

    out_contrast = os.path.join(HERE, "treegrafter_contrast.tsv")
    with open(out_contrast, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["set"] + fields, delimiter="\t")
        w.writeheader()
        for r in up_panther_rows:
            w.writerow({"set": "uniprot_panther (GO_REF:0000120, PANTHER with/from)", **r})
        for r in ip2go_rows:
            w.writerow({"set": "interpro2go (GO_REF:0000002)", **r})

    tg_actions = action_counter(tg_rows)
    paint_actions = action_counter(paint_rows)
    up_actions = action_counter(up_panther_rows)
    ip_actions = action_counter(ip2go_rows)
    problem_actions = PROBLEM_ACTIONS

    # Head-to-head: same gene + same term annotated by both TreeGrafter and
    # InterPro2GO — did the reviewer treat the two sources the same way?
    tg_by_key = {(r["file"], r["term_id"]): r for r in tg_rows}
    ip_by_key = {(r["file"], r["term_id"]): r for r in ip2go_rows}
    shared = sorted(set(tg_by_key) & set(ip_by_key))
    h2h = Counter((tg_by_key[k]["action"], ip_by_key[k]["action"]) for k in shared)
    tg_only = [tg_by_key[k] for k in set(tg_by_key) - set(ip_by_key)]
    ip_only = [ip_by_key[k] for k in set(ip_by_key) - set(tg_by_key)]
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
        w.writerow(["uniprot_panther_annotations (GO_REF:0000120 IEA with PANTHER:PTN "
                    "with/from; same genes; contrast)", len(up_panther_rows)])
        w.writerow(["interpro2go_annotations (GO_REF:0000002 IEA; same genes; contrast)",
                    len(ip2go_rows)])
        w.writerow([])
        w.writerow(["TreeGrafter action", "count"])
        for action, n in tg_actions.most_common():
            w.writerow([action, n])
        w.writerow([])
        w.writerow(["PAINT/IBA action (contrast, NOT TreeGrafter)", "count"])
        for action, n in paint_actions.most_common():
            w.writerow([action, n])
        w.writerow([])
        w.writerow(["UniProt-relayed PANTHER action (GO_REF:0000120, PANTHER with/from; "
                    "same genes)", "count"])
        for action, n in up_actions.most_common():
            w.writerow([action, n])
        w.writerow([])
        w.writerow(["InterPro2GO action (GO_REF:0000002; same genes)", "count"])
        for action, n in ip_actions.most_common():
            w.writerow([action, n])
        w.writerow([])
        w.writerow(["TreeGrafter vs InterPro2GO, same gene + same term",
                    "treegrafter_action", "interpro2go_action", "count"])
        w.writerow(["shared (gene, term) pairs", len(shared)])
        for (a_tg, a_ip), n in sorted(h2h.items(), key=lambda kv: -kv[1]):
            w.writerow(["pair", a_tg, a_ip, n])
        w.writerow(["treegrafter-only terms on shared genes", len(tg_only),
                    "downgraded_pct",
                    f"{100 * sum(r['action'] in problem_actions for r in tg_only) / len(tg_only):.1f}"
                    if tg_only else ""])
        w.writerow(["interpro2go-only terms on shared genes", len(ip_only),
                    "downgraded_pct",
                    f"{100 * sum(r['action'] in problem_actions for r in ip_only) / len(ip_only):.1f}"
                    if ip_only else ""])
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
    report("UniProt-relayed PANTHER (GO_REF:0000120, PANTHER with/from) — same genes",
           up_panther_rows, up_actions)
    report("InterPro2GO (GO_REF:0000002) — same genes", ip2go_rows, ip_actions)
    print(f"\nTreeGrafter vs InterPro2GO on the same (gene, term): {len(shared)} pairs")
    for (a_tg, a_ip), n in sorted(h2h.items(), key=lambda kv: -kv[1]):
        print(f"  TG={a_tg:24s} IP2GO={a_ip:24s} {n}")
    print(f"  TreeGrafter-only terms: {len(tg_only)}; InterPro2GO-only terms: {len(ip_only)}")
    print("\nTreeGrafter down-grade rate (REMOVE/MODIFY/OVER) by GO aspect:")
    for aspect, total in Counter(r["aspect"] or "unknown" for r in tg_rows).most_common():
        bad = sum(1 for r in tg_rows if (r["aspect"] or "unknown") == aspect
                  and r["action"] in problem_actions)
        print(f"  {aspect:22s} {bad:4d}/{total:<4d} ({100 * bad / total:5.1f}%)")
    print(f"\nWrote {os.path.relpath(out_rows, ROOT)}")
    print(f"Wrote {os.path.relpath(out_contrast, ROOT)}")
    print(f"Wrote {os.path.relpath(out_sum, ROOT)}")


if __name__ == "__main__":
    main()
