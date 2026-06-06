#!/usr/bin/env python3
"""Mine curated gene reviews for experimental-readout mentions and correlate
them with the reviewer's action.

For each annotation in every ``*-ai-review.yaml`` file, we build an "evidence
text" from the review summary, reason, and supporting_text snippets, then test
it against the regex patterns in ``readout_catalog.yaml``. Each match is emitted
as a row; we then cross-tabulate readout class against reviewer action to get a
first, data-driven view of which readouts tend to license accepted annotations
vs. those that get downgraded (REMOVE / MARK_AS_OVER_ANNOTATED / NON_CORE).

Usage:
    uv run python projects/ASSAY_TO_FUNCTION/mine_readouts.py \
        --genes-dir genes \
        --catalog projects/ASSAY_TO_FUNCTION/readout_catalog.yaml \
        --out-dir projects/ASSAY_TO_FUNCTION/reports

Nothing is hard-coded about the results; if no readouts are found the report
will say so.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

# Reviewer actions. The "hard" signal is an annotation the curator judged
# wrong or an over-annotation; "soft" downgrades keep the annotation but demote
# or refine it. Reliability percentages are computed over *reviewed*
# annotations only (UNREVIEWED / UNDECIDED excluded from the denominator).
HARD_DOWNGRADE = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
SOFT_DOWNGRADE = {"KEEP_AS_NON_CORE", "MODIFY"}
NOT_REVIEWED = {"UNREVIEWED", "UNDECIDED", "PENDING"}


def load_catalog(path: Path) -> dict[str, dict[str, Any]]:
    data = yaml.safe_load(path.read_text())
    catalog = data["readouts"]
    # Pre-compile patterns.
    for name, spec in catalog.items():
        spec["_compiled"] = [
            re.compile(p, re.IGNORECASE) for p in spec.get("patterns", [])
        ]
    return catalog


def evidence_text(review: dict[str, Any]) -> str:
    """Concatenate the free-text fields a curator wrote/cited for an annotation."""
    parts: list[str] = []
    for key in ("summary", "reason"):
        val = review.get(key)
        if isinstance(val, str):
            parts.append(val)
    for sb in review.get("supported_by", []) or []:
        if isinstance(sb, dict):
            for key in ("supporting_text", "supporting_text_fulltext"):
                val = sb.get(key)
                if isinstance(val, str):
                    parts.append(val)
    return "\n".join(parts)


def snippet_around(text: str, match: re.Match, width: int = 80) -> str:
    start = max(0, match.start() - width)
    end = min(len(text), match.end() + width)
    s = text[start:end].replace("\n", " ").strip()
    return re.sub(r"\s+", " ", s)


def iter_annotations(genes_dir: Path):
    """Yield (path, organism, gene, uniprot_id, annotation_dict)."""
    for path in sorted(genes_dir.rglob("*-ai-review.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        # genes/<organism>/<gene>/<gene>-ai-review.yaml
        rel = path.relative_to(genes_dir)
        organism = rel.parts[0] if len(rel.parts) >= 1 else ""
        gene = doc.get("gene_symbol") or (rel.parts[1] if len(rel.parts) >= 2 else "")
        uniprot = doc.get("id", "")
        for ann in doc.get("existing_annotations", []) or []:
            if isinstance(ann, dict):
                yield path, organism, gene, uniprot, ann


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument(
        "--catalog",
        type=Path,
        default=Path("projects/ASSAY_TO_FUNCTION/readout_catalog.yaml"),
    )
    ap.add_argument(
        "--out-dir", type=Path, default=Path("projects/ASSAY_TO_FUNCTION/reports")
    )
    args = ap.parse_args()

    catalog = load_catalog(args.catalog)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    n_files = 0
    n_annotations = 0
    files_seen: set[Path] = set()

    for path, organism, gene, uniprot, ann in iter_annotations(args.genes_dir):
        if path not in files_seen:
            files_seen.add(path)
            n_files += 1
        n_annotations += 1
        review = ann.get("review") or {}
        text = evidence_text(review)
        if not text:
            continue
        action = (review.get("action") or "").strip() or "UNREVIEWED"
        term = ann.get("term") or {}
        for readout_name, spec in catalog.items():
            for pat in spec["_compiled"]:
                m = pat.search(text)
                if m:
                    rows.append(
                        {
                            "organism": organism,
                            "gene": gene,
                            "uniprot": uniprot,
                            "go_id": term.get("id", ""),
                            "go_label": term.get("label", ""),
                            "evidence_type": ann.get("evidence_type", ""),
                            "negated": str(bool(ann.get("negated", False))),
                            "action": action,
                            "readout_class": readout_name,
                            "proximity": spec.get("proximity", ""),
                            "convergence": spec.get("convergence", ""),
                            "matched": m.group(0),
                            "snippet": snippet_around(text, m),
                            "file": str(path),
                        }
                    )
                    break  # one row per (annotation, readout_class)

    # --- Write per-match TSV ---
    matches_tsv = args.out_dir / "readout_matches.tsv"
    fieldnames = [
        "organism", "gene", "uniprot", "go_id", "go_label", "evidence_type",
        "negated", "action", "readout_class", "proximity", "convergence",
        "matched", "snippet", "file",
    ]
    with matches_tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # --- Cross-tab: readout_class x action ---
    actions_order = ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY",
                     "MARK_AS_OVER_ANNOTATED", "REMOVE", "UNDECIDED",
                     "UNREVIEWED"]
    seen_actions = sorted({r["action"] for r in rows})
    for a in seen_actions:
        if a not in actions_order:
            actions_order.append(a)
    actions_order = [a for a in actions_order if a in seen_actions]

    crosstab: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        crosstab[r["readout_class"]][r["action"]] += 1

    def metrics(counts: Counter) -> tuple[int, int, int, int, str, str]:
        """Return (total, reviewed, hard, soft, pct_hard, pct_soft_or_hard)."""
        total = sum(counts.values())
        reviewed = sum(c for a, c in counts.items() if a not in NOT_REVIEWED)
        hard = sum(counts.get(a, 0) for a in HARD_DOWNGRADE)
        soft = sum(counts.get(a, 0) for a in SOFT_DOWNGRADE)
        pct_hard = f"{100 * hard / reviewed:.0f}%" if reviewed else "-"
        pct_any = f"{100 * (hard + soft) / reviewed:.0f}%" if reviewed else "-"
        return total, reviewed, hard, soft, pct_hard, pct_any

    crosstab_tsv = args.out_dir / "readout_action_crosstab.tsv"
    with crosstab_tsv.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        header = ["readout_class", "proximity", "convergence", "total", "reviewed"]
        header += actions_order + ["pct_removed_or_overann", "pct_any_downgrade"]
        w.writerow(header)
        for name, spec in catalog.items():
            counts = crosstab.get(name)
            if not counts:
                continue
            total, reviewed, hard, soft, pct_hard, pct_any = metrics(counts)
            row = [name, spec.get("proximity", ""), spec.get("convergence", ""),
                   total, reviewed]
            row += [counts.get(a, 0) for a in actions_order]
            row += [pct_hard, pct_any]
            w.writerow(row)

    # --- QC: matched-string distribution per class (surfaces substring bugs) ---
    matched_counts: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        matched_counts[r["readout_class"]][r["matched"].lower()] += 1
    qc_tsv = args.out_dir / "matched_string_counts.tsv"
    with qc_tsv.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["readout_class", "matched_string", "count"])
        for name in catalog:
            for s, c in matched_counts.get(name, Counter()).most_common():
                w.writerow([name, s, c])

    # --- Console summary ---
    print(f"Scanned {n_files} review files, {n_annotations} annotations.")
    print(f"Found {len(rows)} readout matches across "
          f"{len({r['readout_class'] for r in rows})} readout classes.\n")
    if not rows:
        print("No readout mentions detected. Either patterns need broadening "
              "or the evidence text does not name assays.")
        return

    print(f"{'readout_class':<26}{'prox':<11}{'conv':<6}"
          f"{'rev':>5}{'rm/OA%':>8}{'anyDn%':>8}")
    print("-" * 64)
    for name, spec in catalog.items():
        counts = crosstab.get(name)
        if not counts:
            continue
        _, reviewed, _, _, pct_hard, pct_any = metrics(counts)
        print(f"{name:<26}{spec.get('proximity',''):<11}"
              f"{spec.get('convergence',''):<6}{reviewed:>5}{pct_hard:>8}{pct_any:>8}")

    print(f"\nWrote:\n  {matches_tsv}\n  {crosstab_tsv}")


if __name__ == "__main__":
    main()
