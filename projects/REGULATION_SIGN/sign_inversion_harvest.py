"""Harvest existing_annotations rows tagged REGULATORY_SIGN_INVERSION.

Reviewers record this failure mode in review.propagation_review.failure_modes
("Family contains activators and inhibitors, and a positive/negative regulatory
term leaks across members"). This collects every tagged row with its action,
replacement, root cause and propagation sources, and classifies the correction:

  FLIP     replacement is the same term with the opposite sign word
  NEUTRAL  replacement drops the sign (e.g. regulation of X)
  OTHER    replacement is a different kind of term
  NONE     no replacement (REMOVE, UNDECIDED, ...)

and records whether the original term itself carries a direction
(`original_signed`). Unsigned tagged rows are mostly the "participant for
an inhibitor" shape: a gene that opposes process X annotated to X itself.

Prefilters files with a plain substring test, then parses only those.

Usage: uv run python projects/REGULATION_SIGN/sign_inversion_harvest.py [genes_dir]
"""
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
TAG = "REGULATORY_SIGN_INVERSION"
PAIRS = [
    ("positive regulation", "negative regulation"),
    ("activating", "inhibiting"),
    ("activator", "inhibitor"),
    ("agonist", "antagonist"),
    ("up-regulation", "down-regulation"),
    ("stimulat", "inhibit"),
]


def strip_sign(label: str):
    """Return (label with the first sign word removed, sign) or (label, None)."""
    low = label.lower()
    for a, b in PAIRS:
        for word, sign in ((a, "+"), (b, "-")):
            if re.search(r"\b" + re.escape(word), low):
                return re.sub(r"\b" + re.escape(word), "<SIGN>", low, count=1), sign
    return low, None


SIGN_WORDS = re.compile(
    r"\b(positive|negative) regulation|\b(activating|activator|inhibit|stimulat|suppress|repress|"
    r"coactivator|corepressor|elevation|acidification|agonist|antagonist)",
    re.I,
)


def classify(term_label: str, replacements: list) -> str:
    if not replacements:
        return "NONE"
    base, sign = strip_sign(term_label)
    kinds = set()
    for rep in replacements:
        rbase, rsign = strip_sign(rep.get("label") or "")
        if sign and rsign and rsign != sign and rbase == base:
            kinds.add("FLIP")
        elif sign and not rsign and base.replace("<SIGN>", "regulation").replace(
            "regulation regulation", "regulation"
        ) == rbase:
            kinds.add("NEUTRAL")
        elif sign and not rsign and "regulation of" in rbase and base.split(" of ", 1)[-1] == rbase.split(" of ", 1)[-1]:
            kinds.add("NEUTRAL")
        else:
            kinds.add("OTHER")
    for k in ("FLIP", "NEUTRAL", "OTHER"):
        if k in kinds:
            return k
    return "OTHER"


def main(genes_dir: Path):
    rows = []
    for path in sorted(genes_dir.glob("*/*/*-ai-review.yaml")):
        text = path.read_text()
        if TAG not in text:
            continue
        doc = yaml.load(text, Loader=Loader) or {}
        for ann in doc.get("existing_annotations") or []:
            rev = ann.get("review") or {}
            pr = rev.get("propagation_review") or {}
            if TAG not in (pr.get("failure_modes") or []):
                continue
            term = ann.get("term") or {}
            reps = rev.get("proposed_replacement_terms") or []
            rows.append({
                "file": str(path.relative_to(genes_dir.parent)),
                "organism": path.parts[-3],
                "gene": doc.get("gene_symbol"),
                "term": f"{term.get('id')} {term.get('label')}",
                "evidence_type": ann.get("evidence_type"),
                "reference": ann.get("original_reference_id"),
                "negated": bool(ann.get("negated")),
                "action": rev.get("action"),
                "replacement": [f"{r.get('id')} {r.get('label')}" for r in reps],
                "correction": classify(term.get("label") or "", reps),
                "original_signed": bool(SIGN_WORDS.search(term.get("label") or "")),
                "root_cause": pr.get("root_cause"),
                "failure_modes": pr.get("failure_modes"),
                "sources": [
                    {"id": s.get("source_id"), "status": s.get("source_status")}
                    for s in pr.get("source_entities") or []
                ],
                "has_source_defect": bool(rev.get("source_defects")),
            })
    count = lambda key: dict(Counter(r[key] for r in rows).most_common())
    co_modes = Counter(m for r in rows for m in r["failure_modes"] if m != TAG)
    summary = {
        "rows": len(rows),
        "files": len({r["file"] for r in rows}),
        "by_organism": count("organism"),
        "by_evidence_type": count("evidence_type"),
        "by_action": count("action"),
        "by_correction": count("correction"),
        "by_root_cause": count("root_cause"),
        "original_signed": count("original_signed"),
        "by_evidence_and_organism": dict(Counter(f"{r['evidence_type']} {r['organism']}" for r in rows).most_common()),
        "co_occurring_failure_modes": dict(co_modes.most_common()),
        "with_source_defect": sum(r["has_source_defect"] for r in rows),
    }
    yaml.safe_dump({"summary": summary, "rows": rows}, sys.stdout, sort_keys=False,
                   width=200, allow_unicode=True)


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "genes"))
