"""Measure how gene reviews treat annotations to root organelle CC terms.

For each existing annotation whose term is one of ROOTS (e.g. GO:0005739
mitochondrion), record the reviewer's action and evidence type, and whether
the same gene also carries a more specific sub-compartment of that organelle
(an is_a/part_of descendant) anywhere in its review: another existing
annotation not REMOVEd, a proposed replacement, or a core_functions location.
Descendants are classed as membrane (under GO:0016020 membrane), lumen
(under GO:0031974 membrane-enclosed lumen) or other.

Each row's evidence code is also classed as direct (an experiment on this
gene, e.g. IDA/HDA) or synthesis (a propagation or curator inference, e.g.
IBA/IEA/ISS/IC). Under the project policy a root term from synthesis is a red
flag to examine; root_organelle_red_flags.md lists those rows for the
first-pass organelles.

Writes projects/ORGANELLES/root_organelle_usage.yaml and .md, and
projects/ORGANELLES/root_organelle_red_flags.md.

Run from the repository root:
    uv run python projects/ORGANELLES/scripts/root_organelle_usage.py
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A, PART_OF

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "projects" / "ORGANELLES"

ROOTS = {
    "GO:0005739": "mitochondrion",
    "GO:0005634": "nucleus",
    "GO:0005783": "endoplasmic reticulum",
    "GO:0005794": "Golgi apparatus",
    "GO:0005764": "lysosome",
    "GO:0005777": "peroxisome",
    "GO:0005768": "endosome",
    "GO:0009507": "chloroplast",
    "GO:0005773": "vacuole",
    "GO:0005776": "autophagosome",
}
#: Organelles in the first pass (nucleus, series organelles and plastids are deferred).
FIRST_PASS = ["GO:0005739", "GO:0005783", "GO:0005794", "GO:0005777", "GO:0005764"]

#: Evidence codes that come from an experiment on the annotated gene itself.
DIRECT = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
#: Evidence codes that synthesise or propagate rather than observe.
SYNTHESIS = {"IBA", "IBD", "IKR", "IRD", "IEA", "ISS", "ISO", "ISA", "ISM", "IGC", "RCA", "IC"}


def evidence_class(code: str | None) -> str:
    if code in DIRECT:
        return "direct"
    if code in SYNTHESIS:
        return "synthesis"
    return "author"  # TAS, NAS, ND and anything unrecognised


MEMBRANE = "GO:0016020"
LUMEN = "GO:0031974"

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def terms_in_review(doc: dict) -> set[str]:
    """CC-candidate term ids the review asserts or keeps, besides the row itself."""
    ids: set[str] = set()
    for ann in doc.get("existing_annotations") or []:
        rev = ann.get("review") or {}
        tid = (ann.get("term") or {}).get("id")
        if rev.get("action") == "REMOVE" or ann.get("negated"):
            continue
        if tid:
            ids.add(tid)
        for rep in rev.get("proposed_replacement_terms") or []:
            if rep.get("id"):
                ids.add(rep["id"])
    for cf in doc.get("core_functions") or []:
        for loc in cf.get("locations") or []:
            if loc.get("id"):
                ids.add(loc["id"])
    return ids


def main() -> None:
    go = get_adapter("sqlite:obo:go")
    anc_cache: dict[str, set[str]] = {}

    def ancestors(t: str) -> set[str]:
        if t not in anc_cache:
            try:
                anc_cache[t] = set(go.ancestors(t, predicates=[IS_A, PART_OF], reflexive=False))
            except Exception:
                anc_cache[t] = set()
        return anc_cache[t]

    rows = []
    for path in sorted(ROOT.glob("genes/*/*/*-ai-review.yaml")):
        try:
            doc = yaml.load(path.read_text(), Loader=Loader) or {}
        except Exception:
            continue
        anns = doc.get("existing_annotations") or []
        if not any((a.get("term") or {}).get("id") in ROOTS for a in anns):
            continue
        others = terms_in_review(doc)
        for ann in anns:
            tid = (ann.get("term") or {}).get("id")
            if tid not in ROOTS or ann.get("negated"):
                continue
            rev = ann.get("review") or {}
            desc = sorted(o for o in others if o != tid and tid in ancestors(o))
            kinds = set()
            for d in desc:
                a = ancestors(d) | {d}
                kinds.add("membrane" if MEMBRANE in a else "lumen" if LUMEN in a else "other")
            rows.append(
                {
                    "gene": f"{path.parts[-3]}/{path.parts[-2]}",
                    "term": tid,
                    "evidence": ann.get("evidence_type"),
                    "evidence_class": evidence_class(ann.get("evidence_type")),
                    "action": rev.get("action") or "NONE",
                    "replacements": [r.get("id") for r in rev.get("proposed_replacement_terms") or []],
                    "descendants": desc,
                    "kinds": sorted(kinds),
                }
            )

    summary = {}
    for tid, label in ROOTS.items():
        rs = [r for r in rows if r["term"] == tid]
        if not rs:
            continue
        genes = {r["gene"] for r in rs}
        genes_with_desc = {r["gene"] for r in rs if r["descendants"]}
        kind_genes: Counter = Counter()
        for g in genes_with_desc:
            ks = set().union(*(set(r["kinds"]) for r in rs if r["gene"] == g))
            kind_genes["+".join(sorted(ks))] += 1
        bare = [r for r in rs if not r["descendants"]]
        summary[tid] = {
            "label": label,
            "rows": len(rs),
            "genes": len(genes),
            "genes_with_specific_subcompartment": len(genes_with_desc),
            "subcompartment_kinds_by_gene": dict(kind_genes.most_common()),
            "actions": dict(Counter(r["action"] for r in rs).most_common()),
            "evidence": dict(Counter(r["evidence"] for r in rs).most_common()),
            "bare_rows_actions": dict(Counter(r["action"] for r in bare).most_common()),
            "bare_rows_evidence": dict(Counter(r["evidence"] for r in bare).most_common()),
            "bare_gene_examples": sorted({r["gene"] for r in bare})[:25],
            "evidence_class_by_subcompartment": {
                "with_subcompartment": dict(
                    Counter(r["evidence_class"] for r in rs if r["descendants"]).most_common()
                ),
                "root_only": dict(Counter(r["evidence_class"] for r in bare).most_common()),
            },
        }

    (OUT / "root_organelle_usage.yaml").write_text(
        yaml.safe_dump({"summary": summary, "rows": rows}, sort_keys=False, width=100)
    )

    lines = [
        "# Root organelle term usage in gene reviews",
        "",
        "Generated by `scripts/root_organelle_usage.py`; do not edit by hand.",
        "",
        "A gene is counted as having a *specific sub-compartment* when its review",
        "also carries (not REMOVEd), proposes, or lists as a core location an",
        "is_a/part_of descendant of the same organelle.",
        "",
        "| organelle | rows | genes | genes w/ sub-compartment | % | rows w/o sub-compartment |",
        "|---|---|---|---|---|---|",
    ]
    for tid, s in summary.items():
        bare_n = sum(s["bare_rows_actions"].values())
        pct = 100 * s["genes_with_specific_subcompartment"] / s["genes"]
        lines.append(
            f"| {s['label']} ({tid}) | {s['rows']} | {s['genes']} | "
            f"{s['genes_with_specific_subcompartment']} | {pct:.0f} | {bare_n} |"
        )
    for tid, s in summary.items():
        lines += ["", f"## {s['label']} ({tid})", ""]
        lines.append(f"- Actions (all rows): {s['actions']}")
        lines.append(f"- Evidence (all rows): {s['evidence']}")
        lines.append(f"- Sub-compartment kinds, by gene: {s['subcompartment_kinds_by_gene']}")
        lines.append(f"- Rows with no sub-compartment, actions: {s['bare_rows_actions']}")
        lines.append(f"- Rows with no sub-compartment, evidence: {s['bare_rows_evidence']}")
        lines.append(f"- Example genes with only the root term: {', '.join(s['bare_gene_examples'])}")
    (OUT / "root_organelle_usage.md").write_text("\n".join(lines) + "\n")

    flags = [
        "# Root organelle red flags",
        "",
        "Generated by `scripts/root_organelle_usage.py`; do not edit by hand.",
        "",
        "Rows annotating a root organelle term from synthesis evidence",
        f"({', '.join(sorted(SYNTHESIS))}), for the first-pass organelles. Rows that",
        "were already REMOVEd are left out. *Root only* means the review gives the",
        "gene no sub-compartment of that organelle: these are the strongest",
        "candidates for a bold MODIFY to a membrane, lumen or matrix term.",
        "",
        "| organelle | synthesis rows | root only | with sub-compartment |",
        "|---|---|---|---|",
    ]
    flagged = {
        t: [r for r in rows if r["term"] == t and r["evidence_class"] == "synthesis"
            and r["action"] != "REMOVE"]
        for t in FIRST_PASS
    }
    for t, rs in flagged.items():
        n_bare = sum(1 for r in rs if not r["descendants"])
        flags.append(f"| {ROOTS[t]} ({t}) | {len(rs)} | {n_bare} | {len(rs) - n_bare} |")
    for t, rs in flagged.items():
        for title, sub in (("root only", [r for r in rs if not r["descendants"]]),
                           ("with sub-compartment", [r for r in rs if r["descendants"]])):
            flags += ["", f"## {ROOTS[t]} ({t}): {title}", "",
                      "| gene | evidence | action | sub-compartments in review |", "|---|---|---|---|"]
            for r in sorted(sub, key=lambda r: (r["gene"], r["evidence"] or "")):
                flags.append(f"| {r['gene']} | {r['evidence']} | {r['action']} | "
                             f"{', '.join(r['descendants'])} |")
    (OUT / "root_organelle_red_flags.md").write_text("\n".join(flags) + "\n")


if __name__ == "__main__":
    main()
