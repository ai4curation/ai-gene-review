"""Census of sign-flip corrections in gene reviews.

Finds existing_annotations rows whose review action is MODIFY and whose
proposed replacement differs from the original term only by the sign of
regulation (positive<->negative, activating<->inhibiting, activator<->inhibitor,
agonist<->antagonist, up<->down).  Writes a YAML table to stdout.

Usage: uv run python projects/REGULATION_SIGN/sign_flip_census.py [genes_dir]
"""
import re
import sys
from pathlib import Path

import yaml

PAIRS = [
    ("positive regulation", "negative regulation"),
    ("activating", "inhibiting"),
    ("activator", "inhibitor"),
    ("agonist", "antagonist"),
    ("up-regulation", "down-regulation"),
    ("upregulation", "downregulation"),
    ("stimulat", "inhibit"),
]


def sign_key(label: str):
    """Return (label with sign words replaced by a placeholder, sign) or None."""
    low = label.lower()
    for a, b in PAIRS:
        for word, sign in ((a, "+"), (b, "-")):
            if re.search(r"\b" + re.escape(word), low):
                return re.sub(r"\b" + re.escape(word), "<SIGN>", low, count=1), sign
    return None


def main(genes_dir: Path):
    rows = []
    for path in sorted(genes_dir.glob("*/*/*-ai-review.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        for ann in doc.get("existing_annotations") or []:
            rev = ann.get("review") or {}
            if rev.get("action") != "MODIFY":
                continue
            term = ann.get("term") or {}
            orig = sign_key(term.get("label") or "")
            if not orig:
                continue
            for rep in rev.get("proposed_replacement_terms") or []:
                new = sign_key(rep.get("label") or "")
                if new and new[0] == orig[0] and new[1] != orig[1]:
                    rows.append({
                        "file": str(path.relative_to(genes_dir.parent)),
                        "gene": doc.get("gene_symbol"),
                        "evidence_type": ann.get("evidence_type"),
                        "reference": ann.get("original_reference_id"),
                        "original": f"{term.get('id')} {term.get('label')}",
                        "replacement": f"{rep.get('id')} {rep.get('label')}",
                        "flip": f"{orig[1]} -> {new[1]}",
                    })
    yaml.safe_dump({"count": len(rows), "rows": rows}, sys.stdout, sort_keys=False, width=200)


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "genes"))
