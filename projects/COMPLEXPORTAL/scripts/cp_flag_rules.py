"""Heuristic rules that flag possibly-bad ComplexPortal (CP) subunit annotations, scored
against the actions in existing gene reviews.

Inputs (run from repo root):
  1. joined.json from cp_review_join.py (CP GOA rows + review action)
  2. projects/COMPLEXPORTAL/data/cp_pmid_usage.yaml from cp_pmid_usage.py (optional)

Usage:
  uv run python projects/COMPLEXPORTAL/scripts/cp_flag_rules.py joined.json \
      projects/COMPLEXPORTAL/data/cp_pmid_usage.yaml projects/COMPLEXPORTAL/data/cp_rule_eval.yaml

A row counts as "rejected" when the review action is MARK_AS_OVER_ANNOTATED, MODIFY or REMOVE.
For each rule the output gives the number of rows flagged, the rejected fraction among them
(precision), the share of all rejected rows it catches (recall) and the lift over the base rate.
"""
import collections
import csv
import json
import os
import re
import sys

import yaml

BAD = {"MARK_AS_OVER_ANNOTATED", "MODIFY", "REMOVE"}
# Developmental-process terms only; "maturation"/"formation" also match molecular processes
# (protein maturation, heterochromatin formation) and are deliberately excluded.
DEV = re.compile(r"development|morphogenesis|differentiation")
# A cached paper counts as full text only if flagged so AND long enough: some HTML extractions
# are flagged full_text_available but hold little more than the abstract (e.g. PMID:20616062).
MIN_FULL_TEXT_CHARS = 20000


def gene_names(org, gene):
    """Gene symbol plus UniProt GN-line names/synonyms/ORF names."""
    names = {gene}
    path = f"genes/{org}/{gene}/{gene}-uniprot.txt"
    if os.path.exists(path):
        for line in open(path):
            if line.startswith("GN   "):
                for part in line[5:].split(";"):
                    if "=" in part:
                        k, v = part.split("=", 1)
                        names.update(x.split("{")[0].strip() for x in v.split(","))
    return {n for n in names if len(n) >= 3}


_pub_cache = {}


def paper(ref):
    if ref not in _pub_cache:
        path = f"publications/PMID_{ref.split(':')[1]}.md" if ref.startswith("PMID:") else ""
        text = open(path).read() if path and os.path.exists(path) else None
        full = bool(text and "full_text_available: true" in text[:3000] and len(text) >= MIN_FULL_TEXT_CHARS)
        _pub_cache[ref] = (text, full)
    return _pub_cache[ref]


def mentions(text, names):
    for n in names:
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(n) + r"(?![A-Za-z0-9])", text, re.I):
            return True
    return False


def other_rows(org, gene):
    rows = list(csv.DictReader(open(f"genes/{org}/{gene}/{gene}-goa.tsv"), delimiter="\t"))
    return rows


def main(joined, usage_path, out_path):
    R = json.load(open(joined))
    usage = {}
    if usage_path and os.path.exists(usage_path):
        usage = yaml.safe_load(open(usage_path))["pmids"]

    # per-gene context
    ctx = {}
    for org, gene in {(r["org"], r["gene"]) for r in R}:
        rows = other_rows(org, gene)
        noncp = [x for x in rows if x["ASSIGNED BY"] != "ComplexPortal"]
        cp_refs = {x["REFERENCE"] for x in rows if x["ASSIGNED BY"] == "ComplexPortal"}
        ctx[(org, gene)] = dict(
            names=gene_names(org, gene),
            by_ref=collections.defaultdict(set,
                {ref: {x["GO TERM"] for x in noncp if x["REFERENCE"] == ref} for ref in {x["REFERENCE"] for x in noncp}}),
            negated={x["GO TERM"] for x in rows if x["QUALIFIER"].startswith("NOT")},
            n_cp_refs=len(cp_refs),
        )

    flags = collections.defaultdict(list)
    for i, r in enumerate(R):
        c = ctx[(r["org"], r["gene"])]
        name = r["name"].lower()
        bp = r["aspect"] == "biological_process"
        if "regulation of" in name:
            flags["regulation_term"].append(i)
        if name.startswith("negative regulation"):
            flags["negative_regulation_term"].append(i)
        if name.startswith("positive regulation"):
            flags["positive_regulation_term"].append(i)
        if "response to" in name:
            flags["response_to_term"].append(i)
        if bp and DEV.search(name):
            flags["developmental_term"].append(i)
        if c["n_cp_refs"] >= 5:
            flags["promiscuous_subunit_ge5_cp_refs"].append(i)
        text, full = paper(r["ref"])
        if text is not None and not mentions(text, c["names"]):
            flags["gene_not_named_in_cached_text"].append(i)
            flags["gene_not_named_in_full_text" if full else "gene_not_named_in_abstract_or_short_text"].append(i)
        if r["term"] in c["negated"]:
            flags["conflicts_with_NOT_annotation"].append(i)
        same_paper = c["by_ref"].get(r["ref"])
        if same_paper:
            if r["term"] in same_paper:
                flags["same_paper_same_term_by_other_group"].append(i)
            else:
                flags["same_paper_other_terms_only_by_other_group"].append(i)
        else:
            flags["paper_not_used_by_other_group_for_gene"].append(i)
        u = usage.get(r["ref"])
        if u and u["total_annotations"] is not None:
            if u["total_annotations"] == u["complexportal_annotations"]:
                flags["paper_cited_only_by_cp_in_all_goa"].append(i)
            else:
                flags["paper_also_cited_by_other_groups_in_goa"].append(i)
        if u and "Review" in (u.get("pubtype") or []):
            flags["paper_is_review"].append(i)
            if u["total_annotations"] == u["complexportal_annotations"]:
                flags["paper_is_review_and_cited_only_by_cp"].append(i)

    # combined rules
    S = {k: set(v) for k, v in flags.items()}
    bp = {i for i, r in enumerate(R) if r["aspect"] == "biological_process"}
    uncorr = set(range(len(R))) - S.get("same_paper_same_term_by_other_group", set())
    outcome = S.get("regulation_term", set()) | S.get("response_to_term", set()) | S.get("developmental_term", set())
    flags["bp_any"] = sorted(bp)
    flags["combo_regulation_and_uncorroborated"] = sorted(S.get("regulation_term", set()) & uncorr)
    flags["combo_outcome_term_and_uncorroborated"] = sorted(outcome & uncorr)
    flags["combo_bp_and_promiscuous_subunit"] = sorted(bp & S.get("promiscuous_subunit_ge5_cp_refs", set()))
    flags["combo_bp_and_gene_not_named_in_full_text"] = sorted(bp & S.get("gene_not_named_in_full_text", set()))
    flags["combo_outcome_term_and_promiscuous_subunit"] = sorted(outcome & S.get("promiscuous_subunit_ge5_cp_refs", set()))
    if "paper_cited_only_by_cp_in_all_goa" in S:
        flags["combo_bp_and_paper_cited_only_by_cp"] = sorted(bp & S["paper_cited_only_by_cp_in_all_goa"])
        flags["combo_outcome_term_and_paper_cited_only_by_cp"] = sorted(outcome & S["paper_cited_only_by_cp_in_all_goa"])
    if "paper_is_review" in S:
        flags["combo_bp_and_review_paper"] = sorted(bp & S["paper_is_review"])
        flags["combo_outcome_term_and_review_paper"] = sorted(outcome & S["paper_is_review"])

    n = len(R)
    nbad = sum(r["action"] in BAD for r in R)
    base = nbad / n
    result = {"rows": n, "rejected": nbad, "base_rejection_rate": round(base, 4), "rules": {}}
    for rule, idx in sorted(flags.items()):
        b = sum(R[i]["action"] in BAD for i in idx)
        prec = b / len(idx) if idx else 0
        result["rules"][rule] = {
            "flagged": len(idx),
            "rejected": b,
            "precision": round(prec, 4),
            "recall": round(b / nbad, 4) if nbad else 0,
            "lift": round(prec / base, 2) if base else None,
            "examples_rejected": [
                f"{R[i]['org']}/{R[i]['gene']} {R[i]['term']} {R[i]['name']} [{R[i]['ev']} {R[i]['ref']}] {R[i]['action']}"
                for i in idx if R[i]["action"] in BAD][:5],
        }
    yaml.safe_dump(result, open(out_path, "w"), sort_keys=False, width=200)
    print(f"base rejection rate {base:.3f} ({nbad}/{n})")
    print(f"{'rule':48} {'flag':>5} {'rej':>4} {'prec':>6} {'recall':>6} {'lift':>5}")
    for rule, v in sorted(result["rules"].items(), key=lambda x: -x[1]["lift"]):
        print(f"{rule:48} {v['flagged']:5} {v['rejected']:4} {v['precision']:6.3f} {v['recall']:6.3f} {v['lift']:5}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None, sys.argv[3] if len(sys.argv) > 3 else "cp_rule_eval.yaml")
