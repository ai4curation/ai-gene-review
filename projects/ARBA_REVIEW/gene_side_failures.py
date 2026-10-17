#!/usr/bin/env python
"""Break down how gene reviews judged ARBA (GO_REF:0000117) annotations, and why.

Every reviewed gene's ARBA rows are joined to the rule that produced them (the
WITH/FROM column of the gene's GOA file). Rows the review did not keep
(REMOVE, MARK_AS_OVER_ANNOTATED, MODIFY) are assigned one failure category:

* MODIFY rows with a proposed replacement are classified by how the
  replacement relates to the ARBA term in GO (is_a, part_of, has_part,
  regulates): ``NEEDS_MORE_SPECIFIC`` (replacement lies below the term),
  ``TOO_SPECIFIC`` (above it) or ``OTHER_TERM`` (not linked).
* Other rows are classified from the review's reason text by keyword cues
  (``CUES``), tried in an order that depends on the review action (``ORDER``);
  rows matching no cue are ``UNCLASSIFIED``.

The keyword step is a heuristic: categories are a reading aid, and each row's
category, cue and reason are written to ``gene_side_rows.tsv`` for checking.
REMOVE rows, the ones a review judged wrong, are classified by hand in
``gene_side_remove_modes.yaml``; that classification is reported separately and
any REMOVE row missing from it is listed.
Term generality is the number of is_a/part_of descendants in GO, read from the
oaklib GO SQLite build (``sqlite:obo:go``).

Usage::

    uv run python projects/ARBA_REVIEW/gene_side_failures.py
"""

from __future__ import annotations

import collections
import csv
import glob
import re
import sqlite3
from pathlib import Path

import yaml
from oaklib import get_adapter

HERE = Path(__file__).parent
ARBA = "GO_REF:0000117"
KEPT = {"ACCEPT", "KEEP_AS_NON_CORE"}
NOT_KEPT = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}
PREDS = ("rdfs:subClassOf", "BFO:0000050")
#: Relations followed when relating a MODIFY replacement to the original term:
#: is_a, part_of, has_part, regulates (and its positive/negative forms).
LINK_PREDS = PREDS + ("BFO:0000051", "RO:0002211", "RO:0002212", "RO:0002213")

#: Keyword cues: category -> regex over the review's reason text.
CUES = {
    "WRONG_TAXON": r"fungal|fungus|fungi\b|not applicable to|no counterpart|nematode-specific|"
                   r"taxonomically|over-propagation of|plant-specific|animal-specific|in a filamentous",
    "NONCATALYTIC": r"pseudo|catalytically inactive|lacks? the catalytic|non-?catalytic|"
                    r"lacks [^.]{0,40}catalytic",
    "SUBSTRATE_OR_CARGO": r"substrate of|is a substrate|is the substrate|is cargo|as cargo|is degraded",
    "WRONG_PARALOG": r"paralog|isoform|fgf8a|does not phosphorylate|not a component|"
                     r"function of [A-Z0-9]+\b|this is the function of",
    "WRONG_FUNCTION": r"incorrect|demonstrably wrong|no biochemical basis|does not (have|participate|make|bind|"
                      r"catalyze|possess)|not a [a-z-]*-containing|no [a-z-]* activity|conflates",
    "WRONG_LOCATION": r"mislocali|soluble and|soluble cytosolic|not a (generic )?membrane|integral membrane|"
                      r"does not localize|not located",
    "NO_EVIDENCE": r"no (published |experimental |direct )?evidence|unsupported|not supported|no support|"
                   r"not demonstrated|speculative|without (experimental )?support",
    "INDIRECT_EFFECT": r"indirect|downstream|consequence|secondary|phenotype|required for all|housekeeping|"
                       r"pleiotrop|expression change|raised [a-z]+ expression",
    "TOO_GENERAL": r"general|uninformative|generic|broad|parent|high-level|grouping|umbrella|superseded|"
                   r"subsumed|redundant|adds (little|no|nothing)|vague|root|captures the|more (specific|precise|"
                   r"informative)|already (annotated|holds|captured|covered)|restates",
}
#: Cue order by review action: a REMOVE asserts the row is wrong, so error cues
#: are tried first; an over-annotation asserts it is not entirely wrong, so
#: generality and indirectness are tried first.
ERRORS = ["WRONG_TAXON", "NONCATALYTIC", "SUBSTRATE_OR_CARGO", "WRONG_PARALOG", "WRONG_FUNCTION",
          "WRONG_LOCATION", "NO_EVIDENCE"]
ORDER = {
    "REMOVE": ERRORS + ["INDIRECT_EFFECT", "TOO_GENERAL"],
    "MARK_AS_OVER_ANNOTATED": ["INDIRECT_EFFECT", "TOO_GENERAL"] + ERRORS,
    "MODIFY": ["TOO_GENERAL", "INDIRECT_EFFECT"] + ERRORS,
}
#: Broad grouping of categories for headline reporting.
FAMILY = {
    "NEEDS_MORE_SPECIFIC": "true but uninformative", "TOO_GENERAL": "true but uninformative",
    "INDIRECT_EFFECT": "overreach", "NO_EVIDENCE": "overreach", "TOO_SPECIFIC": "overreach",
    "OTHER_TERM": "different term needed",
    "WRONG_TAXON": "wrong", "NONCATALYTIC": "wrong", "SUBSTRATE_OR_CARGO": "wrong",
    "WRONG_PARALOG": "wrong", "WRONG_FUNCTION": "wrong", "WRONG_LOCATION": "wrong",
    "UNCLASSIFIED": "unclassified",
    # hand-classified REMOVE modes (gene_side_remove_modes.yaml)
    "WRONG_ACTIVITY": "wrong", "NONCATALYTIC_HOMOLOG": "wrong", "ROLE_CONFUSION": "wrong",
    "WRONG_PROCESS": "wrong", "WRONG_DIRECTION": "wrong", "TERM_MISREAD": "wrong",
    "SPURIOUS_SIGNATURE": "wrong", "OBSOLETE_OR_PSEUDOGENE": "wrong",
    "INDIRECT": "overreach", "UNSUPPORTED": "overreach",
}


def descendant_counts() -> dict[str, int]:
    """is_a/part_of descendant count of every GO term, from the oaklib SQLite build."""
    get_adapter("sqlite:obo:go")  # ensures the database is downloaded
    db = Path.home() / ".data/oaklib/go.db"
    con = sqlite3.connect(db)
    q = (f"SELECT object, COUNT(DISTINCT subject) FROM entailed_edge "
         f"WHERE predicate IN {PREDS!r} AND subject != object GROUP BY object")
    return dict(con.execute(q).fetchall())


def ancestors_fn():
    con = sqlite3.connect(Path.home() / ".data/oaklib/go.db")

    def anc(term: str) -> set[str]:
        q = f"SELECT object FROM entailed_edge WHERE subject = ? AND predicate IN {LINK_PREDS!r}"
        return {r[0] for r in con.execute(q, (term,))} | {term}
    return anc


def generality(n: int) -> str:
    if n > 200:
        return "very general (>200 descendants)"
    if n > 20:
        return "general (21-200)"
    if n > 0:
        return "specific (1-20)"
    return "leaf (0)"


def classify(row: dict, anc) -> tuple[str, str]:
    if row["action"] == "MODIFY" and row["replacements"]:
        rel = []
        for rep in row["replacements"]:
            if not rep.startswith("GO:"):
                continue
            if row["term"] in anc(rep):
                rel.append("NEEDS_MORE_SPECIFIC")
            elif rep in anc(row["term"]):
                rel.append("TOO_SPECIFIC")
            else:
                rel.append("OTHER_TERM")
        if rel:
            best = min(rel, key=["NEEDS_MORE_SPECIFIC", "TOO_SPECIFIC", "OTHER_TERM"].index)
            return best, "replacement term"
    text = row["reason"]
    for cat in ORDER[row["action"]]:
        m = re.search(CUES[cat], text, flags=re.I)
        if m:
            return cat, m.group(0)
    return "UNCLASSIFIED", ""


def load_rows() -> list[dict]:
    rows = []
    for goa in sorted(glob.glob("genes/*/*/*-goa.tsv")):
        rules = collections.defaultdict(set)
        for r in csv.DictReader(open(goa), delimiter="\t"):
            if r["REFERENCE"] == ARBA:
                rules[r["GO TERM"]].update(x for x in r["WITH/FROM"].split("|") if x.startswith("ARBA:"))
        if not rules:
            continue
        review = Path(goa.replace("-goa.tsv", "-ai-review.yaml"))
        if not review.exists():
            continue
        doc = yaml.load(open(review), Loader=yaml.CSafeLoader) or {}
        for a in doc.get("existing_annotations") or []:
            if a.get("original_reference_id") != ARBA:
                continue
            rv = a.get("review") or {}
            rows.append({
                "gene": "/".join(goa.split("/")[1:3]),
                "term": a["term"]["id"], "label": a["term"].get("label") or "",
                "rules": "|".join(sorted(rules.get(a["term"]["id"], []))),
                "action": rv.get("action") or "",
                "reason": " ".join((rv.get("reason") or rv.get("summary") or "").split()),
                "replacements": [x.get("id", "") for x in rv.get("proposed_replacement_terms") or []
                                 if isinstance(x, dict)],
            })
    return rows


def main() -> None:
    rows = load_rows()
    manual = yaml.safe_load((HERE / "gene_side_remove_modes.yaml").read_text())
    for r in rows:
        r["manual_mode"] = manual["rows"].get(f"{r['gene']}|{r['term']}", "") if r["action"] == "REMOVE" else ""
    ndesc = descendant_counts()
    anc = ancestors_fn()
    for r in rows:
        r["descendants"] = ndesc.get(r["term"], 0)
        r["generality"] = generality(r["descendants"])
        r["category"], r["cue"] = classify(r, anc) if r["action"] in NOT_KEPT else ("", "")
        if r["manual_mode"]:
            r["category"], r["cue"] = r["manual_mode"], "manual"
        r["family"] = FAMILY.get(r["category"], "")

    with open(HERE / "gene_side_rows.tsv", "w", newline="") as fh:
        cols = ["gene", "term", "label", "rules", "action", "generality", "descendants", "category", "family",
                "cue", "manual_mode", "reason"]
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        # reason text is kept only where it explains a failure, to keep the file small
        w.writerows({**r, "reason": r["reason"] if r["action"] in NOT_KEPT else ""} for r in rows)

    # per-rule scorecard from the gene side
    per_rule: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for r in rows:
        for rid in r["rules"].split("|"):
            if rid:
                per_rule[rid][r["action"]] += 1
    with open(HERE / "gene_side_rules.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rule", "rows", "kept", "modify", "rejected", "undecided"])
        for rid, c in sorted(per_rule.items(), key=lambda kv: -sum(kv[1].values())):
            w.writerow([rid.split(":")[-1], sum(c.values()), c["ACCEPT"] + c["KEEP_AS_NON_CORE"], c["MODIFY"],
                        c["REMOVE"] + c["MARK_AS_OVER_ANNOTATED"], c["UNDECIDED"]])
    write_summary(rows, per_rule, manual)


def pct(a: int, b: int) -> str:
    return f"{100 * a / b:.0f}%" if b else "-"


def write_summary(rows: list[dict], per_rule: dict, manual: dict) -> None:
    n = len(rows)
    acts = collections.Counter(r["action"] for r in rows)
    lines = [
        "---",
        'title: "ARBA annotations in gene reviews: failure breakdown"',
        "autolink_gene_symbols: false",
        "---",
        "",
        "# ARBA annotations in gene reviews: failure breakdown",
        "",
        "Generated by `gene_side_failures.py`; do not edit by hand. Per-row detail is in",
        "[gene_side_rows.tsv](gene_side_rows.tsv); per-rule counts in [gene_side_rules.tsv](gene_side_rules.tsv).",
        "",
        f"- ARBA annotations in reviewed genes: **{n}** from **{len(per_rule)}** rules",
        "- review actions: " + ", ".join(f"{k or '(none)'} {v}" for k, v in acts.most_common()),
        "",
        "## Outcome by how general the ARBA term is",
        "",
        "| term generality | rows | kept | modify | over-annotated | remove |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for g in ["very general (>200 descendants)", "general (21-200)", "specific (1-20)", "leaf (0)"]:
        sub = [r for r in rows if r["generality"] == g]
        c = collections.Counter(r["action"] for r in sub)
        m = len(sub)
        lines.append(f"| {g} | {m} | {pct(c['ACCEPT'] + c['KEEP_AS_NON_CORE'], m)} | {pct(c['MODIFY'], m)} "
                     f"| {pct(c['MARK_AS_OVER_ANNOTATED'], m)} | {pct(c['REMOVE'], m)} |")
    bad = [r for r in rows if r["action"] in NOT_KEPT]
    cats = collections.Counter(r["category"] for r in bad)
    fam = collections.Counter(FAMILY[r["category"]] for r in bad)
    lines += ["", f"## What went wrong ({len(bad)} rows not kept)", "",
              "| kind of failure | rows | share |", "|---|---:|---:|"]
    for f, k in fam.most_common():
        lines.append(f"| {f} | {k} | {pct(k, len(bad))} |")
    removed = [r for r in rows if r["action"] == "REMOVE"]
    modes = collections.Counter(r["manual_mode"] or "(not classified)" for r in removed)
    lines += ["", f"## Annotations judged wrong ({len(removed)} REMOVE rows, classified by hand)", "",
              "| failure mode | rows | meaning |", "|---|---:|---|"]
    for m, k in modes.most_common():
        lines.append(f"| {m} | {k} | {manual['modes'].get(m, '')} |")
    missing = [f"{r['gene']}|{r['term']}" for r in removed if not r["manual_mode"]]
    if missing:
        lines += ["", "REMOVE rows not yet in gene_side_remove_modes.yaml: " + ", ".join(missing)]
    lines += ["", "## Failure categories, all rows not kept", "",
              "REMOVE rows use the hand classification; other rows use the keyword heuristic.", "",
              "| category | rows | REMOVE | over-annotated | MODIFY |", "|---|---:|---:|---:|---:|"]
    for cat, k in cats.most_common():
        c = collections.Counter(r["action"] for r in bad if r["category"] == cat)
        lines.append(f"| {cat} ({FAMILY[cat]}) | {k} | {c['REMOVE']} | {c['MARK_AS_OVER_ANNOTATED']} "
                     f"| {c['MODIFY']} |")
    lines += ["", "## Examples per category", ""]
    for cat, _ in cats.most_common():
        lines.append(f"### {cat}")
        lines.append("")
        for r in [r for r in bad if r["category"] == cat][:4]:
            lines.append(f"- {r['gene']} · {r['label']} ({r['action']}): {r['reason'][:220]}")
        lines.append("")
    lines += ["## Rules with the most rows not kept", "",
              "| rule | rows | kept | modify | rejected |", "|---|---:|---:|---:|---:|"]
    worst = sorted(per_rule.items(), key=lambda kv: -(kv[1]["REMOVE"] + kv[1]["MARK_AS_OVER_ANNOTATED"] + kv[1]["MODIFY"]))
    for rid, c in worst[:25]:
        lines.append(f"| {rid.split(':')[-1]} | {sum(c.values())} | {c['ACCEPT'] + c['KEEP_AS_NON_CORE']} "
                     f"| {c['MODIFY']} | {c['REMOVE'] + c['MARK_AS_OVER_ANNOTATED']} |")
    (HERE / "GENE_SIDE_RESULTS.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[5:45]))


if __name__ == "__main__":
    main()
