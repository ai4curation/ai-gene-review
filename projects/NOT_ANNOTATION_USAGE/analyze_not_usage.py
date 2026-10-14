"""Characterise how the GO NOT qualifier is used, and how it lines up with UniProt
CAUTION notes and with this repo's gene reviews.

Inputs (produced by the fetch scripts in this folder):
  not_annotations.tsv          every NOT annotation in GOA (QuickGO download)
  not_accessions_caution.tsv   UniProt CAUTION text for each NOT-annotated protein
  genes/**/*-ai-review.yaml    existing reviews (rows with ``negated: true``)

Outputs:
  not_annotations_classified.tsv   one row per NOT annotation with term category
                                   and CAUTION flags
  review_negated_actions.tsv       one row per negated annotation in a review
  RESULTS.md                       summary tables (regenerated on every run)

Term categories come from GO is_a/part_of ancestry in the local GO SQLite build
(``sqlite:obo:go``). They are deliberately coarse and ordered: the first matching
category wins.

Usage:
    uv run python projects/NOT_ANNOTATION_USAGE/analyze_not_usage.py
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from oaklib import get_adapter

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
NOTS = HERE / "not_annotations.tsv"
CAUTION = HERE / "not_accessions_caution.tsv"
OUT_ROWS = HERE / "not_annotations_classified.tsv"
OUT_REVIEWS = HERE / "review_negated_actions.tsv"
OUT_MD = HERE / "RESULTS.md"

MF_CATS = [
    ("protein binding (bare)", None),  # exact GO:0005515, handled specially
    ("catalytic activity", "GO:0003824"),
    ("transporter activity", "GO:0005215"),
    ("molecular transducer activity", "GO:0060089"),
    ("transcription regulator activity", "GO:0140110"),
    ("binding (other)", "GO:0005488"),
]
BP_CATS = [
    ("signaling", "GO:0023052"),
    ("defense/immune response", "GO:0006952"),
    ("defense/immune response", "GO:0002376"),
    ("response to stimulus (other)", "GO:0050896"),
    ("regulation of biological process", "GO:0050789"),
    ("developmental process", "GO:0032502"),
    ("metabolic process", "GO:0008152"),
    ("localization", "GO:0051179"),
]
NEGATIVE_ACTIVITY = re.compile(
    r"\b(lack|lacks|lacking|devoid|inactive|pseudo|no detectable|not detect|does not|"
    r"did not|unable|absence of|absent|catalytically|no .{0,40}activity)\b",
    re.IGNORECASE,
)
PREDS = ["rdfs:subClassOf", "BFO:0000050"]


def categorise(go, go_id: str, aspect: str, cache: dict) -> str:
    if go_id in cache:
        return cache[go_id]
    if aspect == "C":
        cat = "cellular component"
    else:
        anc = set(go.ancestors(go_id, predicates=PREDS, reflexive=True))
        cats = MF_CATS if aspect == "F" else BP_CATS
        cat = "other " + ("MF" if aspect == "F" else "BP")
        if aspect == "F" and go_id == "GO:0005515":
            cat = "protein binding (bare)"
        else:
            for name, root in cats:
                if root and root in anc:
                    cat = name
                    break
    cache[go_id] = cat
    return cat


def load_caution() -> dict[str, dict]:
    with CAUTION.open() as fh:
        return {r["accession"]: r for r in csv.DictReader(fh, delimiter="\t")}


def scan_reviews() -> list[dict]:
    rows = []
    for path in sorted(ROOT.glob("genes/*/*/*-ai-review.yaml")):
        text = path.read_text()
        if "negated: true" not in text:
            continue
        try:
            doc = yaml.safe_load(text)
        except yaml.YAMLError:
            continue
        for a in doc.get("existing_annotations") or []:
            if not a.get("negated"):
                continue
            term = a.get("term") or {}
            review = a.get("review") or {}
            rows.append({
                "organism": path.parts[-3],
                "gene": doc.get("gene_symbol", path.parts[-2]),
                "uniprot": doc.get("id", ""),
                "go_id": term.get("id", ""),
                "go_label": term.get("label", ""),
                "evidence": a.get("evidence_type", ""),
                "reference": a.get("original_reference_id", ""),
                "action": review.get("action", ""),
                "file": str(path.relative_to(ROOT)),
            })
    return rows


def table(counter: Counter, total: int, header: tuple[str, str]) -> list[str]:
    lines = [f"| {header[0]} | {header[1]} | % |", "|---|---:|---:|"]
    for k, v in counter.most_common():
        lines.append(f"| {k or '(none)'} | {v} | {100 * v / total:.1f} |")
    return lines


def main() -> int:
    go = get_adapter("sqlite:obo:go")
    caution = load_caution()
    cache: dict[str, str] = {}
    with NOTS.open() as fh:
        nots = list(csv.DictReader(fh, delimiter="\t"))
    for r in nots:
        r["category"] = categorise(go, r["GO TERM"], r["GO ASPECT"], cache)
        acc = r["GENE PRODUCT ID"].split("-")[0]
        c = caution.get(acc, {})
        r["reviewed"] = c.get("reviewed", "")
        r["has_caution"] = "yes" if c.get("caution") else "no"
        r["caution_negative_activity"] = (
            "yes" if c.get("caution") and NEGATIVE_ACTIVITY.search(c["caution"]) else "no"
        )
        r["relation"] = r["QUALIFIER"].split("|", 1)[1]

    fields = list(nots[0].keys())
    with OUT_ROWS.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(nots)

    reviews = scan_reviews()
    roots = {"GO:0003674": "F", "GO:0008150": "P", "GO:0005575": "C"}
    for r in reviews:
        anc = set(go.ancestors(r["go_id"], predicates=PREDS, reflexive=True)) if r["go_id"] else set()
        aspect = next((v for k, v in roots.items() if k in anc), "")
        r["aspect"] = aspect
        r["category"] = categorise(go, r["go_id"], aspect, cache) if aspect else "unknown"
    if reviews:
        with OUT_REVIEWS.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(reviews[0].keys()), delimiter="\t",
                               lineterminator="\n")
            w.writeheader()
            w.writerows(reviews)

    n = len(nots)
    md: list[str] = [
        "---",
        'title: "NOT annotation usage: results"',
        "species: [human, rat, ARATH, SCHPO]",
        "---",
        "# NOT annotation usage: results",
        "",
        "Generated by `analyze_not_usage.py`; do not edit by hand.",
        "",
        f"- NOT annotations in GOA: **{n}** on "
        f"**{len({r['GENE PRODUCT ID'] for r in nots})}** gene products",
        f"- Distinct GO terms negated: **{len({r['GO TERM'] for r in nots})}**",
        "",
        "## By aspect",
        "",
        *table(Counter(r["GO ASPECT"] for r in nots), n, ("Aspect", "NOT rows")),
        "",
        "## By relation",
        "",
        *table(Counter(r["relation"] for r in nots), n, ("Relation", "NOT rows")),
        "",
        "## By evidence code",
        "",
        *table(Counter(r["GO EVIDENCE CODE"] for r in nots), n, ("Evidence", "NOT rows")),
        "",
        "## By assigning group",
        "",
        *table(Counter(r["ASSIGNED BY"] for r in nots), n, ("Assigned by", "NOT rows")),
        "",
        "## By term category",
        "",
        *table(Counter(r["category"] for r in nots), n, ("Category", "NOT rows")),
        "",
        "## Evidence code within each category",
        "",
        "| Category | Rows | Top evidence codes |",
        "|---|---:|---|",
    ]
    by_cat: dict[str, Counter] = defaultdict(Counter)
    for r in nots:
        by_cat[r["category"]][r["GO EVIDENCE CODE"]] += 1
    for cat, cnt in sorted(by_cat.items(), key=lambda kv: -sum(kv[1].values())):
        top = ", ".join(f"{k} {v}" for k, v in cnt.most_common(5))
        md.append(f"| {cat} | {sum(cnt.values())} | {top} |")

    resp = [r for r in nots if r["category"] == "response to stimulus (other)"]
    md += [
        "",
        "## 'Response to' NOTs (excluding signaling and defense/immune)",
        "",
        f"{len(resp)} NOT rows are to descendants of GO:0050896 response to stimulus that are "
        "not signaling pathways or defense/immune responses: mostly responses to chemicals, "
        "abiotic stimuli and endogenous signals.",
        "",
        *table(Counter(r["GO EVIDENCE CODE"] for r in resp), max(len(resp), 1),
               ("Evidence", "rows")),
        "",
        "Most frequent terms:",
        "",
        "| GO term | Label | Rows |",
        "|---|---|---:|",
    ]
    for (gid, lab), v in Counter((r["GO TERM"], r["GO NAME"]) for r in resp).most_common(15):
        md.append(f"| {gid} | {lab} | {v} |")

    iep = [r for r in nots if r["GO EVIDENCE CODE"] == "IEP"]
    md += [
        "",
        "## NOTs supported only by expression pattern (IEP)",
        "",
        f"{len(iep)} NOT rows use IEP. An expression measurement cannot show that a gene "
        "product lacks a function, so these are the clearest misuse of the qualifier.",
        "",
        *table(Counter(r["ASSIGNED BY"] for r in iep), max(len(iep), 1), ("Assigned by", "rows")),
        "",
        *table(Counter(r["category"] for r in iep), max(len(iep), 1), ("Category", "rows")),
    ]

    # CAUTION alignment
    prot = {}
    for r in nots:
        acc = r["GENE PRODUCT ID"].split("-")[0]
        prot.setdefault(acc, {"aspects": set(), "reviewed": r["reviewed"],
                              "caution": r["has_caution"],
                              "negact": r["caution_negative_activity"]})
        prot[acc]["aspects"].add(r["GO ASPECT"])
    rev = {a: p for a, p in prot.items() if p["reviewed"] == "reviewed"}
    mf_rev = {a: p for a, p in rev.items() if "F" in p["aspects"]}
    nonmf_rev = {a: p for a, p in rev.items() if "F" not in p["aspects"]}

    def frac(d: dict, key: str) -> str:
        k = sum(1 for p in d.values() if p[key] == "yes")
        return f"{k}/{len(d)} ({100 * k / max(len(d), 1):.1f}%)"

    md += [
        "",
        "## Alignment with UniProt CAUTION notes",
        "",
        "Counts are per reviewed (Swiss-Prot) protein carrying at least one NOT annotation. "
        "'Negative-activity CAUTION' means the CAUTION text matches a loss-of-activity "
        "pattern (lacks, inactive, pseudo, no ... activity, and similar).",
        "",
        "| Protein set | Any CAUTION | Negative-activity CAUTION |",
        "|---|---|---|",
        f"| Reviewed proteins with any NOT | {frac(rev, 'caution')} | {frac(rev, 'negact')} |",
        f"| ... with a NOT to a molecular function | {frac(mf_rev, 'caution')} | "
        f"{frac(mf_rev, 'negact')} |",
        f"| ... with NOTs only to BP/CC | {frac(nonmf_rev, 'caution')} | "
        f"{frac(nonmf_rev, 'negact')} |",
    ]

    # Our reviews
    md += ["", "## How this repo's reviews treated negated annotations", ""]
    if reviews:
        md += [
            f"{len(reviews)} negated rows across "
            f"{len({(r['organism'], r['gene']) for r in reviews})} reviewed genes.",
            "",
            *table(Counter(r["action"] for r in reviews), len(reviews), ("Action", "rows")),
            "",
            *table(Counter(r["evidence"] for r in reviews), len(reviews), ("Evidence", "rows")),
            "",
            "### Action by term category",
            "",
            "| Category | Rows | Actions |",
            "|---|---:|---|",
        ]
        cat_act: dict[str, Counter] = defaultdict(Counter)
        for r in reviews:
            cat_act[r["category"]][r["action"]] += 1
        for cat, cnt in sorted(cat_act.items(), key=lambda kv: -sum(kv[1].values())):
            md.append(f"| {cat} | {sum(cnt.values())} | "
                      + ", ".join(f"{k} {v}" for k, v in cnt.most_common()) + " |")
        flagged = [r for r in reviews
                   if r["category"] == "response to stimulus (other)" or r["evidence"] == "IEP"]
        md += [
            "",
            "### Worklist: reviewed NOTs to non-defense 'response to' terms or with IEP evidence",
            "",
            "| Organism | Gene | GO term | Label | Evidence | Current action |",
            "|---|---|---|---|---|---|",
        ]
        for r in sorted(flagged, key=lambda r: (r["organism"], r["gene"])):
            md.append(f"| {r['organism']} | {r['gene']} | {r['go_id']} | {r['go_label']} | "
                      f"{r['evidence']} | {r['action']} |")
    else:
        md.append("No negated rows found in reviews.")

    OUT_MD.write_text("\n".join(md) + "\n")
    print(f"wrote {OUT_MD}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
