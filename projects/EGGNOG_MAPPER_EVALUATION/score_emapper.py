#!/usr/bin/env python3
"""Score eggNOG-mapper GO predictions against AIGR gene reviews.

eggNOG-mapper reports, per query, the GO terms of its orthologs already
propagated up the ontology -- with the GO release current when the eggNOG 5.0.2
database was built, not today's. Each prediction set is first reduced to its
**leaf terms**: a predicted term is dropped when it is an ancestor of another
predicted term under the 2019-07-01, 2020-12-08 *or* current release. Using the
older releases matters: grouping classes such as "heterocyclic compound binding"
have since lost their links to specific terms and would otherwise surface as
spurious leaves. Leaf ids are then mapped to the current release (alt_id and
replaced_by followed; obsolete terms without a replacement are counted and
dropped), and each leaf is compared, through the GO is_a/part_of closure, with the review's adjudicated
terms:

  SUPPORTED_SET  ACCEPT / KEEP_AS_NON_CORE / NEW rows, MODIFY replacement
                 terms, and every core_functions term (MF, BP, location, complex)
  DOWNGRADED     MARK_AS_OVER_ANNOTATED / TOO_GENERAL rows, and the original
                 term of MODIFY rows
  UNDECIDED_SET  UNDECIDED rows: the reviewer reached no judgment, so these are
                 kept apart from DOWNGRADED rather than read as a negative signal
  REJECTED       REMOVE rows, and curated NOT annotations not overturned by review

Leaf categories, assigned in this order:
  EXACT        the leaf is in SUPPORTED_SET
  REJECTED     the leaf equals, or descends from, a REJECTED term
  BROADER      the leaf is an ancestor of a SUPPORTED_SET term (correct, less precise)
  NARROWER     the leaf descends from a SUPPORTED_SET term (more specific than curated;
               unverified)
  DOWNGRADED   the leaf equals, descends from, or is an ancestor of a DOWNGRADED term
  UNDECIDED    likewise related to an UNDECIDED_SET term (and to nothing above)
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

GOA baseline: each protein's cached ``*-goa.tsv`` (non-NOT rows, any evidence)
is also closed over the ontology, so per protein and per stratum the summary
reports how many core_functions terms GOA already covered and how many emapper
adds that GOA did not.

Reviews and GOA files are read as of a pinned commit (``--reviews-at``, default
REVIEW_SNAPSHOT), so the scores do not drift as the corpus keeps changing.

Run: uv run python projects/EGGNOG_MAPPER_EVALUATION/score_emapper.py [--base DIR] [--runs a,b] [--reviews-at REV]
``--base`` is a directory holding cohort.yaml and runs/ (default: this
project directory; e.g. ``deep_dive``); results go to ``<base>/results``.
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import subprocess
import sys
from collections import Counter, defaultdict

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
from ai_gene_review.bioreason_ontology import GO_RELEASE, ensure_frozen_go  # noqa: E402

# GO releases bracketing the eggNOG 5.0.2 annotation build, used only for leaf reduction.
LEGACY_GO = {
    "2019-07-01": "f96adc6c08a1030fee2fcb143271d4d671fb48ac45d2a20b3b23f7d61bcf17c1",
    "2020-12-08": "bd6474bd048a67021b2cf482b056b1074ea8f96ddd60e6ae13e24af68cbe5c46",
}


def legacy_go_paths() -> list[str]:
    import hashlib
    import urllib.request
    paths = []
    for rel, sha in LEGACY_GO.items():
        path = os.path.join(ROOT, "cache", "ontologies", f"go-basic-{rel}.obo")
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            urllib.request.urlretrieve(
                f"https://release.geneontology.org/{rel}/ontology/go-basic.obo", path)
        digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
        if digest != sha:
            raise RuntimeError(f"checksum mismatch for {path}")
        paths.append(path)
    return paths

LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
# The corpus commit whose reviews this evaluation was scored against (the main
# commit the evaluation branch started from). "WORKTREE" reads the working tree.
REVIEW_SNAPSHOT = "b9da9839c"


def read_repo_file(rel: str, rev: str) -> str | None:
    """Text of a repository file at ``rev`` (or the working tree), None if absent."""
    if rev == "WORKTREE":
        path = os.path.join(ROOT, rel)
        return open(path).read() if os.path.exists(path) else None
    r = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{rel}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None
RUNS = {
    "default": "all orthologs (emapper defaults)",
    "species_excluded": "orthologs from the query's own species excluded (--excluded_taxa)",
    "narrow_scope": "default, with --tax_scope all_narrow (narrowest pre-configured clade)",
    "species_excluded_narrow": "own species excluded, with --tax_scope all_narrow",
    "species_excluded_experimental": ("own species excluded, experimental GO evidence only "
                                      "(--go_evidence experimental)"),
}
CATEGORIES = ["EXACT", "BROADER", "NARROWER", "DOWNGRADED", "REJECTED", "UNDECIDED", "UNRELATED"]
SUPPORT_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW"}
DOWNGRADE_ACTIONS = {"MARK_AS_OVER_ANNOTATED", "TOO_GENERAL"}
NS = {"biological_process": "BP", "molecular_function": "MF", "cellular_component": "CC"}
ROOTS = {"GO:0008150", "GO:0003674", "GO:0005575"}
PLACEHOLDER_REMOVALS = ROOTS | {"GO:0005488", "GO:0005515"}  # binding, protein binding


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



def leaf_terms(raw: set[str], go: GO, legacy: list[GO]):
    """Reduce emapper's propagated raw ids to current-release leaf terms.

    Returns (leaves, closure, n_obsolete_leaves): ``closure`` is the current-release
    ancestor closure of every mappable predicted term."""
    covered: set[str] = set()
    for u in raw:
        for g in legacy:
            covered |= g.ancestors(u) - {u}
        n = go.norm(u)
        if n:
            covered |= go.ancestors(n) - {n}
    leaves, obsolete = set(), 0
    for t in raw - covered:
        n = go.norm(t)
        if n is None:
            obsolete += 1
        elif n not in ROOTS:
            leaves.add(n)
    # a raw leaf may map onto an ancestor of another leaf after replaced_by/alt_id
    cov_now = set()
    for t in leaves:
        cov_now |= go.ancestors(t) - {t}
    leaves -= cov_now
    closure = set()
    for u in raw:
        n = go.norm(u)
        if n:
            closure |= go.ancestors(n)
    return leaves, closure, obsolete


def review_sets(doc: dict, go: GO):
    support, down, undecided, reject, core = set(), set(), set(), set(), set()

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
        elif action == "UNDECIDED":
            add(undecided, term)
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
    reject -= support | PLACEHOLDER_REMOVALS
    down -= support
    undecided -= support | down | reject
    return support, down, undecided, reject, core


def categorize(leaf: str, support, down, undecided, reject, go: GO) -> str:
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
    if anc & undecided or any(leaf in go.ancestors(u) for u in undecided):
        return "UNDECIDED"
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
            if header is None:
                raise ValueError(f"{path}: data line before the #query header")
            row = dict(zip(header, line.rstrip("\n").split("\t")))
            out[row["query"]] = row
    return out


def goa_closure(rec: dict, go: GO, rev: str) -> set[str]:
    """Ontology closure of the gene's cached GOA terms (NOT rows excluded)."""
    text = read_repo_file(f"{os.path.dirname(rec['review'])}/{rec['gene']}-goa.tsv", rev)
    out: set[str] = set()
    if text is None:
        return out
    for row in csv.DictReader(io.StringIO(text), delimiter="\t"):
        if "NOT" in (row.get("QUALIFIER") or "").split("|"):
            continue
        t = go.norm(row.get("GO TERM", ""))
        if t:
            out |= go.ancestors(t)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=HERE)
    ap.add_argument("--runs", default=",".join(RUNS))
    ap.add_argument("--reviews-at", default=REVIEW_SNAPSHOT)
    args = ap.parse_args()
    base = os.path.abspath(args.base)
    run_names = [r for r in args.runs.split(",") if r]
    go = GO(str(ensure_frozen_go()))
    legacy = [GO(p) for p in legacy_go_paths()]
    with open(os.path.join(base, "cohort.yaml")) as fh:
        cohort = yaml.safe_load(fh)["proteins"]
    seen_acc = set()
    for rec in cohort:
        if rec["accession"] in seen_acc:
            raise ValueError(f"duplicate accession {rec['accession']} in cohort.yaml; "
                             "each accession must be scored against one review")
        seen_acc.add(rec["accession"])
    reviews, goa = {}, {}
    for rec in cohort:
        text = read_repo_file(rec["review"], args.reviews_at)
        if text is None:
            raise FileNotFoundError(f"{rec['review']} not found at {args.reviews_at}")
        reviews[rec["accession"]] = review_sets(yaml.load(text, Loader=LOADER), go)
        goa[rec["accession"]] = goa_closure(rec, go, args.reviews_at)

    os.makedirs(os.path.join(base, "results"), exist_ok=True)
    summary = {"review_snapshot": args.reviews_at, "go_release": GO_RELEASE, "leaf_reduction_releases": sorted(LEGACY_GO) + [GO_RELEASE], "cohort_size": len(cohort), "runs": {}}
    for run in run_names:
        desc = RUNS.get(run, run)
        ann_path = os.path.join(base, "runs", run, f"{run}.emapper.annotations")
        if not os.path.exists(ann_path):
            print(f"skip {run}: {ann_path} missing")
            continue
        ann = read_annotations(ann_path)
        leaf_rows, prot_rows = [], []
        cat_ns = Counter()
        obsolete_leaves = 0
        for rec in cohort:
            acc = rec["accession"]
            support, down, undecided, reject, core = reviews[acc]
            row = ann.get(acc)
            raw = [] if row is None or row.get("GOs", "-") in ("-", "") else row["GOs"].split(",")
            leaves, closure, n_obs = leaf_terms(set(raw), go, legacy)
            obsolete_leaves += n_obs
            cats = Counter()
            for leaf in sorted(leaves):
                c = categorize(leaf, support, down, undecided, reject, go)
                cats[c] += 1
                cat_ns[(go.ns.get(leaf, "?"), c)] += 1
                leaf_rows.append({
                    "accession": acc, "gene": rec["gene"], "organism_dir": rec["organism_dir"],
                    "stratum": rec["stratum"], "aspect": go.ns.get(leaf, "?"),
                    "term_id": leaf, "term_label": go.name.get(leaf, ""), "category": c})
            core_hit = {c for c in core if c in closure}
            core_goa = {c for c in core if c in goa[acc]}
            prot_rows.append({
                "accession": acc, "gene": rec["gene"], "organism_dir": rec["organism_dir"],
                "stratum": rec["stratum"], "annotated": int(row is not None),
                "seed_ortholog": (row or {}).get("seed_ortholog", ""),
                "max_annot_lvl": (row or {}).get("max_annot_lvl", ""),
                "preferred_name": (row or {}).get("Preferred_name", ""),
                "n_go_propagated": len(set(raw)), "n_leaves": len(leaves),
                **{c.lower(): cats[c] for c in CATEGORIES},
                "n_core_terms": len(core), "n_core_recovered": len(core_hit),
                "n_core_in_goa": len(core_goa), "n_core_emapper_only": len(core_hit - core_goa),
                "core_missed": ";".join(sorted(core - core_hit))})
        if not leaf_rows:
            print(f"warning: {run} produced no GO leaf terms")
        for name, rows in (("leaf_scores", leaf_rows), ("protein", prot_rows)):
            if not rows:
                continue
            with open(os.path.join(base, "results", f"{run}_{name}.tsv"), "w", newline="") as fh:
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
                "core_recall": round(sum(p["n_core_recovered"] for p in ps) / ct, 3) if ct else None,
                "core_terms": ct,
                "core_in_goa": sum(p["n_core_in_goa"] for p in ps),
                "core_emapper_only": sum(p["n_core_emapper_only"] for p in ps)}
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
            "core_in_goa": sum(p["n_core_in_goa"] for p in prot_rows),
            "core_emapper_only": sum(p["n_core_emapper_only"] for p in prot_rows),
            "obsolete_leaves_dropped": obsolete_leaves,
            "by_stratum": by_stratum,
        }
        print(run, yaml.safe_dump(summary["runs"][run]["leaf_categories"]), core_hit, core_total)
    with open(os.path.join(base, "results", "summary.yaml"), "w") as fh:
        fh.write("# Generated by score_emapper.py; do not edit by hand.\n")
        yaml.safe_dump(summary, fh, sort_keys=False)


if __name__ == "__main__":
    main()
