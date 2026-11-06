"""Census of review rows whose reason argues the annotated sign/direction is wrong.

Complements sign_flip_census.py: catches sign problems handled by REMOVE,
UNDECIDED, MARK_AS_OVER_ANNOTATED or a MODIFY to a non-sibling term.
Prefilters files with a regex, then parses only those.  Output: YAML to stdout.

Usage: uv run python projects/REGULATION_SIGN/sign_reason_census.py [genes_dir]
"""
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
PATTERN = re.compile(
    r"opposite (sign|direction)|wrong sign|sign (error|flip|inver|correct|conflict)"
    r"|direction of (regulation|effect)|inverted sign|reverse(d)? (sign|direction)",
    re.I,
)


def main(genes_dir: Path):
    rows = []
    for path in sorted(genes_dir.glob("*/*/*-ai-review.yaml")):
        text = path.read_text()
        if not PATTERN.search(text):
            continue
        doc = yaml.load(text, Loader=Loader)
        for ann in (doc or {}).get("existing_annotations") or []:
            rev = ann.get("review") or {}
            reason = " ".join(str(rev.get(k) or "") for k in ("summary", "reason"))
            m = PATTERN.search(reason)
            if not m:
                continue
            term = ann.get("term") or {}
            rows.append({
                "file": str(path.relative_to(genes_dir.parent)),
                "gene": doc.get("gene_symbol"),
                "evidence_type": ann.get("evidence_type"),
                "action": rev.get("action"),
                "term": f"{term.get('id')} {term.get('label')}",
                "replacement": [f"{r.get('id')} {r.get('label')}" for r in rev.get("proposed_replacement_terms") or []],
                "match": m.group(0),
            })
    summary = {"count": len(rows),
               "by_action": dict(Counter(r["action"] for r in rows)),
               "by_evidence": dict(Counter(r["evidence_type"] for r in rows))}
    yaml.safe_dump({"summary": summary, "rows": rows}, sys.stdout, sort_keys=False, width=200)


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "genes"))
