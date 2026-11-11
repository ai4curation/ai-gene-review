#!/usr/bin/env python3
"""Analyse an NCBI-vs-GOA comparison at three levels: genome, source, and curated review.

Reads the outputs of ``compare_refseq_goa.py`` (``term_comparison.tsv``,
``loci.tsv``, ``ncbi_proteins.tsv``, ``summary.yaml``) and the curated gene reviews under
``genes/<SPECIES>/*/*-ai-review.yaml``.

Review-based judgments
----------------------
Reviewers judged GOA rows, not NCBI rows, so each term on a reviewed gene is
classified against the review as follows (first match wins):

* ``over_annotated_general`` -- marked over-annotated by the reviewer, but a
  proper ancestor of a term the reviewer accepted: true, just too general.
  This is kept apart from ``removed`` (wrong) because reviewers often use
  MARK_AS_OVER_ANNOTATED for terms that are only less specific.
* ``removed`` / ``over_annotated`` / ``modified`` -- the term itself carries that
  reviewer action (strongest action across the term's rows).
* ``accepted`` -- the term is accepted/kept/NEW, a MODIFY replacement, or a
  ``core_functions`` term.
* ``general_of_accepted`` -- a proper ancestor of an accepted term (true but less
  specific).
* ``specific_of_accepted`` -- a proper descendant of an accepted term (a
  refinement the reviewer did not assert; needs checking).
* ``near_removed`` -- an ancestor or descendant of a removed term.
* ``unassessed`` -- none of the above; the review neither supports nor rejects it.

Experimental ground truth
-------------------------
GOA's experimental annotations (EXP/IDA/IMP/IGI/IEP/IPI and high-throughput
equivalents, excluding generic protein binding) are a second, independent
ground truth, most useful for well-studied genomes such as *E. coli* K-12. On
loci with experimental terms in an aspect, each NCBI term and each GOA
electronic (IEA) term is classed as ``exact``, ``general_of_experimental``
(true but less specific), ``specific_of_experimental`` (an unverified
refinement) or ``not_supported``. Experimental annotation is incomplete, so
``not_supported`` means unconfirmed, not wrong. Recall is the share of
experimental terms each side covers with the same or a more specific term.
GOA's electronic pipelines are partly built from these same experimental
annotations (IBA is excluded from "electronic" for that reason, but UniRule and
InterPro2GO curation also draw on them), so this comparison favours GOA.

Outputs (in ``--results-dir``): ``analysis.yaml`` and four case tables,
``ncbi_review_cases.tsv``, ``goa_errors_vs_ncbi.tsv``, ``core_coverage.tsv`` and
``experimental_cases.tsv``.

Usage::

    uv run python projects/REFSEQ_GO/analyze_refseq_goa.py \\
        --results-dir projects/REFSEQ_GO/results/PSEPK --species PSEPK
"""

from __future__ import annotations

import csv
import glob
from collections import Counter, defaultdict
from pathlib import Path

import typer
import yaml

from compare_refseq_goa import GOREF_PIPELINE, Closure

app = typer.Typer(add_completion=False)

POSITIVE = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "TOO_GENERAL"}
# Strongest-first: a term's verdict is the strongest action on any of its rows.
ACTION_RANK = ["REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY", "UNDECIDED"]
VERDICT = {
    "REMOVE": "removed",
    "MARK_AS_OVER_ANNOTATED": "over_annotated",
    "MODIFY": "modified",
    "UNDECIDED": "undecided",
}
ELECTRONIC = set(GOREF_PIPELINE.values()) | {"Combined IEA (other)"}
# Annotation sets compared side by side in ``pipeline_variants``. "IBA" is the
# GO Central phylogenetic annotation (PAINT), which TreeGrafter extends to
# proteins outside the PAINT trees.
GOA_SUBSETS = {
    "GOA InterPro2GO": {"InterPro2GO"},
    "GOA InterPro2GO + TreeGrafter + IBA": {"InterPro2GO", "TreeGrafter", "IBA"},
    "GOA electronic without ARBA": ELECTRONIC - {"ARBA"},
    "GOA electronic": ELECTRONIC,
}
# Experimental evidence used as ground truth. IPI is kept, but generic protein
# binding is excluded because it says nothing about function.
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IEP", "IPI", "HDA", "HMP", "HGI", "HEP"}
PROTEIN_BINDING = "GO:0005515"


def term_verdict(actions: set[str]) -> str:
    """Collapse the reviewer actions on one term's rows into one verdict.

    >>> term_verdict({"ACCEPT", "REMOVE"})
    'removed'
    >>> term_verdict({"KEEP_AS_NON_CORE"})
    'accepted'
    >>> term_verdict({"MODIFY", "ACCEPT"})
    'modified'
    """
    for action in ACTION_RANK:
        if action in actions:
            return VERDICT[action]
    return "accepted" if actions & POSITIVE else "undecided"


class Review:
    def __init__(self, path: Path) -> None:
        d = yaml.safe_load(path.open())
        self.path = path
        self.symbol = d["gene_symbol"]
        self.accession = d["id"]
        actions: dict[str, set[str]] = defaultdict(set)
        self.reasons: dict[str, str] = {}
        self.accepted: set[str] = set()
        for a in d.get("existing_annotations") or []:
            r = a.get("review") or {}
            t = a["term"]["id"]
            if a.get("negated"):
                continue
            action = r.get("action")
            if action:
                actions[t].add(action)
            if action in ("REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"):
                self.reasons.setdefault(t, " ".join((r.get("reason") or "").split()))
            for rep in r.get("proposed_replacement_terms") or []:
                if rep.get("id", "").startswith("GO:"):
                    self.accepted.add(rep["id"])
        self.verdict = {t: term_verdict(a) for t, a in actions.items()}
        self.accepted |= {t for t, v in self.verdict.items() if v == "accepted"}
        self.core_mf: set[str] = set()
        self.core_bp: set[str] = set()
        for cf in d.get("core_functions") or []:
            mf = (cf.get("molecular_function") or {}).get("id")
            if mf:
                self.core_mf.add(mf)
            self.core_bp |= {x["id"] for x in cf.get("directly_involved_in") or []}
            self.accepted |= {x["id"] for x in cf.get("locations") or []}
        self.accepted |= self.core_mf | self.core_bp
        self.removed = {t for t, v in self.verdict.items() if v == "removed"}

    def classify(self, term: str, closure: Closure) -> str:
        v = self.verdict.get(term)
        if v == "over_annotated" and any(
            term in closure.ancestors(a) for a in self.accepted if a != term
        ):
            # Marked over-annotated, but an ancestor of an accepted term: true,
            # just less specific. Reported apart from errors.
            return "over_annotated_general"
        if v and v != "accepted":
            return v
        if term in self.accepted:
            return "accepted"
        if any(term in closure.ancestors(a) for a in self.accepted):
            return "general_of_accepted"
        anc = closure.ancestors(term)
        if anc & self.accepted:
            return "specific_of_accepted"
        if anc & self.removed or any(
            term in closure.ancestors(r) for r in self.removed
        ):
            return "near_removed"
        return "unassessed"


def covered(core: str, terms: set[str], closure: Closure) -> str:
    """How a side covers one core term: exact/more specific, only more general, or not."""
    if core in terms or any(core in closure.ancestors(t) for t in terms):
        return "covered"
    if closure.ancestors(core) & terms:
        return "general_only"
    return "missed"


def pct(n: int, d: int) -> float:
    return round(100 * n / d, 1) if d else 0.0


def load_ncbi_proteins(path: Path) -> dict[str, dict]:
    """WP_ -> {product, naming_evidence}, from compare_refseq_goa.py's ncbi_proteins.tsv."""
    with path.open() as fh:
        return {r["refseq_protein"]: r for r in csv.DictReader(fh, delimiter="\t")}


@app.command()
def main(
    results_dir: Path = typer.Option(..., help="Output dir of compare_refseq_goa.py"),
    species: str = typer.Option(..., help="genes/<SPECIES> folder with reviews"),
) -> None:
    summary = yaml.safe_load((results_dir / "summary.yaml").open())
    proteins = load_ncbi_proteins(results_dir / "ncbi_proteins.tsv")
    closure = Closure()
    labels = closure.adapter.label

    loci = {}
    with (results_dir / "loci.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            loci[row["locus"]] = row
    rows = list(
        csv.DictReader((results_dir / "term_comparison.tsv").open(), delimiter="\t")
    )

    # side -> locus -> aspect -> {term: source}
    terms: dict[str, dict[str, dict[str, dict[str, str]]]] = {
        "ncbi": defaultdict(lambda: defaultdict(dict)),
        "goa": defaultdict(lambda: defaultdict(dict)),
    }
    for r in rows:
        terms[r["side"]][r["locus"]][r["aspect"]][r["go_id"]] = r["source"]
    compared = [
        lc
        for lc, row in loci.items()
        if row["refseq_proteins"] and row["uniprot_accessions"]
    ]

    def goa_iea(locus: str, aspect: str | None = None) -> set[str]:
        out = set()
        for asp, ts in terms["goa"][locus].items():
            if aspect and asp != aspect:
                continue
            out |= {t for t, s in ts.items() if set(s.split("|")) & ELECTRONIC}
        return out

    def side_terms(side: str, locus: str, aspect: str | None = None) -> set[str]:
        return {
            t
            for asp, ts in terms[side][locus].items()
            if not aspect or asp == aspect
            for t in ts
        }

    def name_of(locus: str) -> str:
        wps = loci[locus]["refseq_proteins"].split("|")
        return proteins.get(wps[0], {}).get("product", "") if wps[0] else ""

    def model_of(locus: str) -> str:
        wps = loci[locus]["refseq_proteins"].split("|")
        return proteins.get(wps[0], {}).get("naming_evidence", "") if wps[0] else ""

    # ---------------- Level 1: genome-wide ----------------
    per_aspect = {}
    for asp, name in (
        ("F", "molecular_function"),
        ("P", "biological_process"),
        ("C", "cellular_component"),
    ):
        n = {lc for lc in compared if side_terms("ncbi", lc, asp)}
        g = {lc for lc in compared if side_terms("goa", lc, asp)}
        gi = {lc for lc in compared if goa_iea(lc, asp)}
        per_aspect[name] = {
            "loci_ncbi": len(n),
            "loci_goa": len(g),
            "loci_goa_electronic": len(gi),
            "loci_both": len(n & g),
            "loci_ncbi_only": len(n - g),
            "loci_goa_only": len(g - n),
            "terms_ncbi": sum(len(side_terms("ncbi", lc, asp)) for lc in compared),
            "terms_goa": sum(len(side_terms("goa", lc, asp)) for lc in compared),
        }

    ncbi_only_genes = [
        lc for lc in compared if side_terms("ncbi", lc) and not side_terms("goa", lc)
    ]
    goa_only_genes = [
        lc for lc in compared if side_terms("goa", lc) and not side_terms("ncbi", lc)
    ]
    goa_only_names = Counter(name_of(lc) for lc in goa_only_genes)
    ncbi_only_src = Counter(loci[lc]["ncbi_sources"] for lc in ncbi_only_genes)

    # goslim_prokaryote: loci per slim term on each side
    slim = set(closure.adapter.subset_members("goslim_prokaryote"))
    slim_counts: dict[str, Counter] = defaultdict(Counter)
    for side in ("ncbi", "goa"):
        for lc in compared:
            hit = set()
            for t in side_terms(side, lc):
                hit |= closure.ancestors(t) & slim
            for s in hit:
                slim_counts[s][side] += 1
    slim_rows = sorted(
        (
            {
                "slim": f"{s} {labels(s)}",
                "ncbi": c["ncbi"],
                "goa": c["goa"],
                "goa_minus_ncbi": c["goa"] - c["ncbi"],
            }
            for s, c in slim_counts.items()
        ),
        key=lambda x: -abs(x["goa_minus_ncbi"]),
    )

    # ---------------- Level 2: by source ----------------
    def rel_table(side: str) -> dict:
        out: dict[str, Counter] = defaultdict(Counter)
        for r in rows:
            if r["side"] != side:
                continue
            for s in r["source"].split("|"):
                out[f"{s} [{r['aspect']}]"][r["relation_to_other_side"]] += 1
        table = {}
        for k, c in sorted(out.items()):
            comp = sum(v for rel, v in c.items() if rel != "other_side_no_aspect")
            table[k] = {
                "compared": comp,
                "exact_pct": pct(c["exact"], comp),
                "other_more_specific_pct": pct(c["other_more_specific"], comp),
                "other_more_general_pct": pct(c["other_more_general"], comp),
                "only_pct": pct(c["only"], comp),
                "other_side_lacks_aspect": c["other_side_no_aspect"],
            }
        return table

    # ---------------- Level 3: reviews ----------------
    acc_to_locus = {}
    for lc, row in loci.items():
        for acc in row["uniprot_accessions"].split("|"):
            if acc:
                acc_to_locus[acc] = lc
    reviews = {}
    for f in sorted(glob.glob(f"genes/{species}/*/*-ai-review.yaml")):
        rv = Review(Path(f))
        lc = acc_to_locus.get(rv.accession)
        if lc and lc in compared:
            reviews[lc] = rv

    ncbi_cls: dict[str, Counter] = defaultdict(Counter)
    goa_cls: dict[str, Counter] = defaultdict(Counter)
    ncbi_cases = []
    for lc, rv in reviews.items():
        for asp, ts in terms["ncbi"][lc].items():
            for t, src in ts.items():
                cls = rv.classify(t, closure)
                ncbi_cls[src][cls] += 1
                ncbi_cls["ALL"][cls] += 1
                in_goa = t in side_terms("goa", lc)
                ncbi_cases.append(
                    [
                        lc,
                        rv.symbol,
                        rv.accession,
                        name_of(lc),
                        model_of(lc),
                        src,
                        asp,
                        t,
                        labels(t) or "",
                        cls,
                        "yes" if in_goa else "no",
                        rv.reasons.get(t, ""),
                        str(rv.path),
                    ]
                )
        for asp, ts in terms["goa"][lc].items():
            for t, src in ts.items():
                cls = rv.classify(t, closure)
                for s in src.split("|"):
                    goa_cls[s][cls] += 1
                if set(src.split("|")) & ELECTRONIC:
                    goa_cls["ALL electronic"][cls] += 1

    def cls_table(c: dict[str, Counter]) -> dict:
        out = {}
        for k, v in sorted(c.items(), key=lambda kv: -sum(kv[1].values())):
            tot = sum(v.values())
            out[k] = {"terms": tot, **{cls: pct(n, tot) for cls, n in v.most_common()}}
        return out

    # Errors GOA made (reviewer REMOVE / over-annotation): did NCBI share them?
    err_rows = []
    err_summary: dict[str, Counter] = defaultdict(Counter)
    for lc, rv in reviews.items():
        n_terms = side_terms("ncbi", lc)
        for asp, ts in terms["goa"][lc].items():
            for t, src in ts.items():
                v = rv.verdict.get(t)
                if v not in ("removed", "over_annotated"):
                    continue
                if t in n_terms:
                    shared = "ncbi_same_term"
                elif any(t in closure.ancestors(n) for n in n_terms):
                    shared = "ncbi_more_specific"
                elif closure.ancestors(t) & n_terms:
                    shared = "ncbi_more_general_only"
                elif not side_terms("ncbi", lc, asp):
                    shared = "ncbi_no_terms_in_aspect"
                else:
                    shared = "ncbi_avoided"
                for s in src.split("|"):
                    err_summary[f"{v} via {s}"][shared] += 1
                err_rows.append(
                    [
                        lc,
                        rv.symbol,
                        rv.accession,
                        asp,
                        t,
                        labels(t) or "",
                        src,
                        v,
                        shared,
                        model_of(lc),
                        rv.reasons.get(t, ""),
                    ]
                )

    # Core-function coverage: NCBI vs GOA electronic vs GOA all
    core_rows = []
    core_summary: dict[str, Counter] = defaultdict(Counter)
    for lc, rv in reviews.items():
        for kind, cores, asp in (("MF", rv.core_mf, "F"), ("BP", rv.core_bp, "P")):
            n_t = side_terms("ncbi", lc, asp)
            ge = goa_iea(lc, asp)
            ga = side_terms("goa", lc, asp)
            for c in cores:
                cn, ce, ca = (
                    covered(c, n_t, closure),
                    covered(c, ge, closure),
                    covered(c, ga, closure),
                )
                core_summary[f"{kind} ncbi"][cn] += 1
                core_summary[f"{kind} goa_electronic"][ce] += 1
                core_summary[f"{kind} goa_all"][ca] += 1
                core_summary[f"{kind} ncbi_vs_goa_electronic"][f"{cn}/{ce}"] += 1
                core_rows.append(
                    [
                        lc,
                        rv.symbol,
                        rv.accession,
                        kind,
                        c,
                        labels(c) or "",
                        cn,
                        ce,
                        ca,
                        model_of(lc),
                        name_of(lc),
                    ]
                )

    # ---------------- Level 3b: experimental GO as ground truth ----------------
    def exp_terms(locus: str, aspect: str) -> set[str]:
        return {
            t
            for t, src in terms["goa"][locus].get(aspect, {}).items()
            if set(src.split("|")) & EXPERIMENTAL and t != PROTEIN_BINDING
        }

    exp_prec: dict[str, Counter] = defaultdict(Counter)
    exp_rec: dict[str, Counter] = defaultdict(Counter)
    exp_rows = []
    exp_loci = set()
    for lc in compared:
        for asp in "FPC":
            truth = exp_terms(lc, asp)
            if not truth:
                continue
            exp_loci.add(lc)
            for name, ts in (
                ("NCBI", side_terms("ncbi", lc, asp)),
                ("GOA electronic", goa_iea(lc, asp)),
            ):
                for t in ts:
                    if t in truth:
                        cls = "exact"
                    elif any(t in closure.ancestors(x) for x in truth):
                        cls = "general_of_experimental"
                    elif closure.ancestors(t) & truth:
                        cls = "specific_of_experimental"
                    else:
                        cls = "not_supported"
                    exp_prec[name][cls] += 1
                    exp_prec[f"{name} [{asp}]"][cls] += 1
                    if cls == "not_supported":
                        exp_rows.append(
                            [
                                lc,
                                name,
                                asp,
                                t,
                                labels(t) or "",
                                model_of(lc),
                                name_of(lc),
                            ]
                        )
                for x in truth:
                    exp_rec[name][covered(x, ts, closure)] += 1
                    exp_rec[f"{name} [{asp}]"][covered(x, ts, closure)] += 1

    # ---------------- Pipeline variants, scored the same way ----------------
    def variant_terms(name: str, locus: str, aspect: str) -> set[str]:
        out: set[str] = set()
        parts = name.split(" ∪ ")
        for part in parts:
            if part == "NCBI":
                out |= side_terms("ncbi", locus, aspect)
            else:
                allowed = GOA_SUBSETS[part]
                out |= {
                    t
                    for t, src in terms["goa"][locus].get(aspect, {}).items()
                    if set(src.split("|")) & allowed
                }
        return out

    variant_names = [
        "NCBI",
        *GOA_SUBSETS,
        "NCBI ∪ GOA InterPro2GO + TreeGrafter + IBA",
    ]
    review_groups = {
        "accepted": "correct",
        "general_of_accepted": "correct",
        "specific_of_accepted": "correct",
        "over_annotated_general": "too_general",
        "over_annotated": "over_annotated_other",
        "modified": "modified",
        "removed": "wrong",
        "near_removed": "wrong",
        "unassessed": "unassessed",
        "undecided": "unassessed",
    }
    variants = {}
    for vn in variant_names:
        genes_with = sum(
            1 for lc in compared if any(variant_terms(vn, lc, a) for a in "FPC")
        )
        rv_c: Counter = Counter()
        for lc, rv in reviews.items():
            for a in "FPC":
                for t in variant_terms(vn, lc, a):
                    rv_c[review_groups[rv.classify(t, closure)]] += 1
        core_c: dict[str, Counter] = defaultdict(Counter)
        for lc, rv in reviews.items():
            for kind, cores, a in (("MF", rv.core_mf, "F"), ("BP", rv.core_bp, "P")):
                ts = variant_terms(vn, lc, a)
                for c in cores:
                    core_c[kind][covered(c, ts, closure)] += 1
        ex_p: Counter = Counter()
        ex_r: Counter = Counter()
        for lc in compared:
            for a in "FPC":
                truth = exp_terms(lc, a)
                if not truth:
                    continue
                ts = variant_terms(vn, lc, a)
                for t in ts:
                    supported = t in truth or any(
                        t in closure.ancestors(x) for x in truth
                    )
                    ex_p["supported" if supported else "other"] += 1
                for x in truth:
                    ex_r[covered(x, ts, closure)] += 1
        tot = sum(rv_c.values())
        variants[vn] = {
            "genes_with_go": genes_with,
            "reviewed_terms": tot,
            **{f"review_{k}_pct": pct(v, tot) for k, v in sorted(rv_c.items())},
            "core_mf_covered_pct": pct(
                core_c["MF"]["covered"], sum(core_c["MF"].values())
            ),
            "core_bp_covered_pct": pct(
                core_c["BP"]["covered"], sum(core_c["BP"].values())
            ),
            "experimental_supported_pct": pct(ex_p["supported"], sum(ex_p.values())),
            "experimental_recall_pct": pct(ex_r["covered"], sum(ex_r.values())),
        }

    analysis = {
        "species": species,
        "annotation_release": summary["annotation_release"],
        "level1_genome": {
            "loci_compared": len(compared),
            "per_aspect": per_aspect,
            "genes_ncbi_only": {
                "count": len(ncbi_only_genes),
                "by_ncbi_source": dict(ncbi_only_src.most_common()),
            },
            "genes_goa_only": {
                "count": len(goa_only_genes),
                "top_refseq_names": dict(goa_only_names.most_common(25)),
            },
            "goslim_prokaryote_largest_differences": slim_rows[:30],
        },
        "level2_by_source": {
            "ncbi_terms_vs_goa": rel_table("ncbi"),
            "goa_terms_vs_ncbi": rel_table("goa"),
        },
        "level3_reviews": {
            "reviewed_loci": len(reviews),
            "ncbi_terms_by_review_class_pct": cls_table(ncbi_cls),
            "goa_terms_by_review_class_pct": cls_table(goa_cls),
            "goa_errors_shared_by_ncbi": {
                k: dict(v) for k, v in sorted(err_summary.items())
            },
            "core_function_coverage": {
                k: dict(v) for k, v in sorted(core_summary.items())
            },
        },
        "pipeline_variants": variants,
        "level3_experimental": {
            "loci_with_experimental_go": len(exp_loci),
            "terms_vs_experimental_pct": cls_table(exp_prec),
            "experimental_terms_recalled": {
                k: {**dict(v), "covered_pct": pct(v["covered"], sum(v.values()))}
                for k, v in sorted(exp_rec.items())
            },
        },
    }

    def write(name: str, header: list[str], data: list[list[str]]) -> None:
        with (results_dir / name).open("w") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(header)
            w.writerows(sorted(data))

    write(
        "ncbi_review_cases.tsv",
        [
            "locus",
            "symbol",
            "accession",
            "refseq_name",
            "ncbi_model",
            "ncbi_source",
            "aspect",
            "go_id",
            "go_label",
            "review_class",
            "also_in_goa",
            "reviewer_reason",
            "review_file",
        ],
        ncbi_cases,
    )
    write(
        "goa_errors_vs_ncbi.tsv",
        [
            "locus",
            "symbol",
            "accession",
            "aspect",
            "go_id",
            "go_label",
            "goa_source",
            "reviewer_verdict",
            "ncbi_status",
            "ncbi_model",
            "reviewer_reason",
        ],
        err_rows,
    )
    write(
        "core_coverage.tsv",
        [
            "locus",
            "symbol",
            "accession",
            "kind",
            "core_go_id",
            "core_label",
            "ncbi",
            "goa_electronic",
            "goa_all",
            "ncbi_model",
            "refseq_name",
        ],
        core_rows,
    )
    write(
        "experimental_cases.tsv",
        ["locus", "side", "aspect", "go_id", "go_label", "ncbi_model", "refseq_name"],
        exp_rows,
    )
    with (results_dir / "analysis.yaml").open("w") as fh:
        yaml.safe_dump(analysis, fh, sort_keys=False, width=120)
    typer.echo(
        yaml.safe_dump(
            {k: analysis[k] for k in ("pipeline_variants",)},
            sort_keys=False,
            width=120,
        )
    )


if __name__ == "__main__":
    app()
