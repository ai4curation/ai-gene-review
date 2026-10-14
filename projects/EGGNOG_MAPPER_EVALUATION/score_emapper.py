#!/usr/bin/env python3
"""Score eggNOG-mapper GO predictions against AIGR gene reviews.

eggNOG-mapper reports, per query, the GO terms of its orthologs already
propagated up the ontology. Each prediction set is first reduced to its
**leaf terms** (no predicted term is an ancestor of another), and each leaf is
compared, through the GO is_a/part_of closure, with the review's adjudicated
terms:

  SUPPORTED_SET  ACCEPT / KEEP_AS_NON_CORE / NEW rows, MODIFY replacement
                 terms, and every core_functions term (MF, BP, location, complex)
  DOWNGRADED     MARK_AS_OVER_ANNOTATED / TOO_GENERAL / UNDECIDED rows, and the
                 original term of MODIFY rows
  REJECTED       REMOVE rows, and curated NOT annotations not overturned by review

Leaf categories, assigned in this order:
  EXACT        the leaf is in SUPPORTED_SET
  REJECTED     the leaf equals, or descends from, a REJECTED term
  BROADER      the leaf is an ancestor of a SUPPORTED_SET term (correct, less precise)
  NARROWER     the leaf descends from a SUPPORTED_SET term (more specific than curated;
               unverified)
  DOWNGRADED   the leaf equals, descends from, or is an ancestor of a DOWNGRADED term
  UNRELATED    none of the above: not supported by the review (novel or wrong)

Recall: a core_functions term counts as recovered when it is in the
prediction's propagated closure (the leaf equals it or descends from it).

Inputs: ``cohort.yaml``; ``runs/<run>/<run>.emapper.annotations`` for each run
(see README / project page); the pinned GO release from
``ai_gene_review.bioreason_ontology.ensure_frozen_go``.

Outputs (in ``results/``):
  <run>_leaf_scores.tsv   one row per predicted leaf term
  <run>_protein.tsv       one row per protein (counts, recall)
  summary.yaml            aggregate tables for the project page

Run: uv run python projects/EGGNOG_MAPPER_EVALUATION/score_emapper.py
"""
from __future__ import annotations

import csv
import os
import sys
from collections import Counter, defaultdict

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
from ai_gene_review.bioreason_ontology import GO_RELEASE, ensure_frozen_go  # noqa: E402

LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
RUNS = {
    "default": "all orthologs (emapper defaults)",
    "species_excluded": "orthologs from the query's own species excluded (--excluded_taxa)",
}
CATEGORIES = ["EXACT", "BROADER", "NARROWER", "DOWNGRADED", "REJECTED", "UNRELATED"]
SUPPORT_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW"}
DOWNGRADE_ACTIONS = {"MARK_AS_OVER_ANNOTATED", "TOO_GENERAL", "UNDECIDED"}
NS = {"biological_process": "BP", "molecular_function": "MF", "cellular_component": "CC"}
ROOTS = {"GO:0008150", "GO:0003674", "GO:0005575"}


class GO:
    def __init__(self, path: str):
        self.parents: dict[str, set[str]] = defaultdict(set)
        self.name: dict[str, str] = {}
        self.ns: dict[str, str] = {}
        self.alias: dict[str, str] = {}
        self.obsolete: set[str] = set()
        replaced: dict[str, str] = {}
        cur = None
        with open(path) as fh:
            for line in fh:
                line = line.rstrip("\n")
                if line.startswith("["):
                    cur = None if line != "[Term]" else {}
                    continue
                if cur is None or ": " not in line:
                    continue
                k, v = line.split(": ", 1)
                if k == "id":
                    cur["id"] = v
                elif k == "name":
                    self.name[cur["id"]] = v
                elif k == "namespace":
                    self.ns[cur["id"]] = NS.get(v, v)
                elif k == "alt_id":
                    self.alias[v] = cur["id"]
                elif k == "is_obsolete" and v == "true":
                    self.obsolete.add(cur["id"])
                elif k == "replaced_by":
                    replaced[cur["id"]] = v.split()[0]
                elif k == "is_a":
                    self.parents[cur["id"]].add(v.split()[0])
                elif k == "relationship" and v.startswith("part_of "):
                    self.parents[cur["id"]].add(v.split()[1])
        self.alias.update(replaced)
        self._anc: dict[str, frozenset[str]] = {}

    def norm(self, t: str) -> str | None:
        t = self.alias.get(t, t)
        if t not in self.name or t in self.obsolete:
            return None
        return t

    def ancestors(self, t: str) -> frozenset[str]:
        """Reflexive is_a/part_of ancestors."""
        if t not in self._anc:
            out = {t}
            stack = [t]
            while stack:
                for p in self.parents.get(stack.pop(), ()):
                    if p not in out:
                        out.add(p)
                        stack.append(p)
            self._anc[t] = frozenset(out)
        return self._anc[t]

    def leaves(self, terms: set[str]) -> set[str]:
        covered = set()
        for t in terms:
            covered |= self.ancestors(t) - {t}
        return terms - covered


def review_sets(doc: dict, go: GO):
    support, down, reject, core = set(), set(), set(), set()

    def add(dest, term):
        if isinstance(term, dict) and term.get("id"):
            t = go.norm(term["id"])
            if t:
                dest.add(t)

    for ann in doc.get("existing_annotations") or []:
        if not isinstance(ann, dict) or ann.get("retired"):
            continue
        action = (ann.get("review") or {}).get("action")
        term = ann.get("term")
        if ann.get("negated"):
            if action != "REMOVE":
                add(reject, term)  # curated NOT annotation upheld
            continue
        if action in SUPPORT_ACTIONS:
            add(support, term)
        elif action in DOWNGRADE_ACTIONS:
            add(down, term)
        elif action == "MODIFY":
            add(down, term)
            for rep in (ann.get("review") or {}).get("proposed_replacement_terms") or []:
                add(support, rep)
        elif action == "REMOVE":
            add(reject, term)
    for cf in doc.get("core_functions") or []:
        if not isinstance(cf, dict):
            continue
        for key in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
            add(core, cf.get(key))
        for key in ("directly_involved_in", "locations"):
            for t in cf.get(key) or []:
                add(core, t)
    support |= core
    # A term both supported and rejected (e.g. REMOVE on one evidence row, ACCEPT on
    # another) is a claim the review upholds; it is not counted as rejected.
    reject -= support
    down -= support
    return support, down, reject, core


def categorize(leaf: str, support, down, reject, go: GO) -> str:
    anc = go.ancestors(leaf)
    if leaf in support:
        return "EXACT"
    if anc & reject:
        return "REJECTED"
    if any(leaf in go.ancestors(s) for s in support):
        return "BROADER"
    if anc & support:
        return "NARROWER"
    if anc & down or any(leaf in go.ancestors(d) for d in down):
        return "DOWNGRADED"
    return "UNRELATED"


def read_annotations(path: str) -> dict[str, dict]:
    out = {}
    with open(path) as fh:
        header = None
        for line in fh:
            if line.startswith("##"):
                continue
            if line.startswith("#query"):
                header = line[1:].rstrip("\n").split("\t")
                continue
            row = dict(zip(header, line.rstrip("\n").split("\t")))
            out[row["query"]] = row
    return out


def main() -> None:
    go = GO(str(ensure_frozen_go()))
    with open(os.path.join(HERE, "cohort.yaml")) as fh:
        cohort = yaml.safe_load(fh)["proteins"]
    reviews = {}
    for rec in cohort:
        with open(os.path.join(ROOT, rec["review"])) as fh:
            reviews[rec["accession"]] = review_sets(yaml.load(fh, Loader=LOADER), go)

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    summary = {"go_release": GO_RELEASE, "cohort_size": len(cohort), "runs": {}}
    for run, desc in RUNS.items():
        ann_path = os.path.join(HERE, "runs", run, f"{run}.emapper.annotations")
        if not os.path.exists(ann_path):
            print(f"skip {run}: {ann_path} missing")
            continue
        ann = read_annotations(ann_path)
        leaf_rows, prot_rows = [], []
        cat_ns = Counter()
        unmapped_terms = Counter()
        for rec in cohort:
            acc = rec["accession"]
            support, down, reject, core = reviews[acc]
            row = ann.get(acc)
            raw = [] if row is None or row.get("GOs", "-") in ("-", "") else row["GOs"].split(",")
            pred = set()
            for t in raw:
                n = go.norm(t)
                if n:
                    pred.add(n)
                else:
                    unmapped_terms[t] += 1
            pred -= ROOTS
            leaves = go.leaves(pred)
            closure = set()
            for t in pred:
                closure |= go.ancestors(t)
            cats = Counter()
            for leaf in sorted(leaves):
                c = categorize(leaf, support, down, reject, go)
                cats[c] += 1
                cat_ns[(go.ns.get(leaf, "?"), c)] += 1
                leaf_rows.append({
                    "accession": acc, "gene": rec["gene"], "organism_dir": rec["organism_dir"],
                    "stratum": rec["stratum"], "aspect": go.ns.get(leaf, "?"),
                    "term_id": leaf, "term_label": go.name.get(leaf, ""), "category": c})
            core_hit = {c for c in core if c in closure}
            prot_rows.append({
                "accession": acc, "gene": rec["gene"], "organism_dir": rec["organism_dir"],
                "stratum": rec["stratum"], "annotated": int(row is not None),
                "seed_ortholog": (row or {}).get("seed_ortholog", ""),
                "max_annot_lvl": (row or {}).get("max_annot_lvl", ""),
                "preferred_name": (row or {}).get("Preferred_name", ""),
                "n_go_propagated": len(pred), "n_leaves": len(leaves),
                **{c.lower(): cats[c] for c in CATEGORIES},
                "n_core_terms": len(core), "n_core_recovered": len(core_hit),
                "core_missed": ";".join(sorted(core - core_hit))})
        for name, rows in (("leaf_scores", leaf_rows), ("protein", prot_rows)):
            with open(os.path.join(HERE, "results", f"{run}_{name}.tsv"), "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
                w.writeheader()
                w.writerows(rows)

        n_leaf = len(leaf_rows)
        with_go = [p for p in prot_rows if p["n_leaves"]]
        core_total = sum(p["n_core_terms"] for p in prot_rows)
        core_hit = sum(p["n_core_recovered"] for p in prot_rows)
        by_stratum = {}
        for s in sorted({p["stratum"] for p in prot_rows}):
            ps = [p for p in prot_rows if p["stratum"] == s]
            ls = [r for r in leaf_rows if r["stratum"] == s]
            ct = sum(p["n_core_terms"] for p in ps)
            by_stratum[s] = {
                "proteins": len(ps), "with_go": sum(1 for p in ps if p["n_leaves"]),
                "leaves": len(ls),
                **{c.lower(): sum(1 for r in ls if r["category"] == c) for c in CATEGORIES},
                "core_recall": round(sum(p["n_core_recovered"] for p in ps) / ct, 3) if ct else None}
        summary["runs"][run] = {
            "description": desc,
            "proteins_annotated": sum(p["annotated"] for p in prot_rows),
            "proteins_with_go": len(with_go),
            "leaf_terms": n_leaf,
            "leaf_categories": {c: sum(1 for r in leaf_rows if r["category"] == c) for c in CATEGORIES},
            "leaf_categories_by_aspect": {
                a: {c: cat_ns[(a, c)] for c in CATEGORIES} for a in ("MF", "BP", "CC")},
            "core_terms": core_total, "core_terms_recovered": core_hit,
            "core_recall": round(core_hit / core_total, 3) if core_total else None,
            "unmapped_obsolete_terms": sum(unmapped_terms.values()),
            "by_stratum": by_stratum,
        }
        print(run, yaml.safe_dump(summary["runs"][run]["leaf_categories"]), core_hit, core_total)
    with open(os.path.join(HERE, "results", "summary.yaml"), "w") as fh:
        fh.write("# Generated by score_emapper.py; do not edit by hand.\n")
        yaml.safe_dump(summary, fh, sort_keys=False)


if __name__ == "__main__":
    main()
