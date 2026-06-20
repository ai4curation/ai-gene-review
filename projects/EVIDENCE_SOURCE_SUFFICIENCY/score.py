#!/usr/bin/env python
"""Score the EVIDENCE_SOURCE_SUFFICIENCY study once the instruments are filled.

Reads the labeling instrument TSVs produced by ``sample_genes.py`` and computes
the pre-registered estimands (see ``../PROTOCOL.md``) with **gene-clustered**
95% bootstrap confidence intervals, plus the retrospective-vs-blind calibration.

It is safe to run on partially- or un-filled instruments: each estimand is
computed only over rows whose relevant field has been filled, and the report
states the filled denominator. Nothing is fabricated — an empty instrument
yields an explicit "0 labeled" result.

Run:

    uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/sample/../score.py
    # or with explicit dir:
    uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/score.py --dir projects/EVIDENCE_SOURCE_SUFFICIENCY/sample
"""

from __future__ import annotations

import argparse
import csv
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

NARRATIVE_SECTIONS = {"INTRODUCTION", "LITERATURE_REVIEW", "DISCUSSION", "CONCLUSIONS"}
ASPECTS = ("MF", "BP", "CC")


def read_tsv(path: Path) -> List[dict]:
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def to_bool(value: str) -> Optional[float]:
    """Map a Y/N/partial cell to 1.0/0.0; partial->0.5; blank/other->None.

    Examples:
        >>> to_bool("Y"), to_bool("n"), to_bool("partial"), to_bool("")
        (1.0, 0.0, 0.5, None)
        >>> to_bool("  Yes ")
        1.0
    """
    v = (value or "").strip().lower()
    if not v:
        return None
    if v.startswith("y"):
        return 1.0
    if v.startswith("n"):
        return 0.0
    if v.startswith("partial"):
        return 0.5
    return None


def _percentile(sorted_vals: List[float], q: float) -> float:
    """Linear-interpolation percentile of an already-sorted list (q in [0,1])."""
    if not sorted_vals:
        return float("nan")
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    pos = q * (len(sorted_vals) - 1)
    lo = int(pos)
    frac = pos - lo
    hi = min(lo + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + frac * (sorted_vals[hi] - sorted_vals[lo])


def cluster_bootstrap_ci(
    valued_rows: List[Tuple[str, float]],
    n_boot: int = 2000,
    seed: int = 20260614,
) -> Tuple[float, Optional[float], Optional[float], int, int]:
    """Point estimate + gene-clustered bootstrap 95% CI for a proportion.

    Args:
        valued_rows: list of (cluster_id, value) where value is 0/0.5/1.
        n_boot: bootstrap resamples (clusters drawn with replacement).
        seed: RNG seed.

    Returns:
        (point, lo, hi, k_positive_equiv_unused, n). lo/hi are None when there
        are too few clusters to bootstrap.
    """
    n = len(valued_rows)
    if n == 0:
        return (float("nan"), None, None, 0, 0)

    point = sum(v for _, v in valued_rows) / n

    clusters: Dict[str, List[float]] = defaultdict(list)
    for cid, v in valued_rows:
        clusters[cid].append(v)
    cluster_ids = list(clusters)
    if len(cluster_ids) < 3:
        return (point, None, None, 0, n)

    rng = random.Random(seed)
    draws: List[float] = []
    for _ in range(n_boot):
        pooled: List[float] = []
        for _ in cluster_ids:
            pooled.extend(clusters[rng.choice(cluster_ids)])
        if pooled:
            draws.append(sum(pooled) / len(pooled))
    draws.sort()
    return (point, _percentile(draws, 0.025), _percentile(draws, 0.975), 0, n)


def estimate(
    rows: List[dict],
    value_fn: Callable[[dict], Optional[float]],
    cluster_key: str = "gene",
    seed: int = 20260614,
) -> dict:
    """Compute point + clustered CI over rows where value_fn is not None."""
    valued = [
        (r.get(cluster_key, ""), value_fn(r))
        for r in rows
    ]
    valued = [(c, v) for c, v in valued if v is not None]
    point, lo, hi, _, n = cluster_bootstrap_ci(valued, seed=seed)
    return {"point": point, "lo": lo, "hi": hi, "n": n}


def fmt(est: dict) -> str:
    if est["n"] == 0:
        return "n=0 (not yet labeled)"
    ci = (
        f" [{est['lo'] * 100:.0f}–{est['hi'] * 100:.0f}%]"
        if est["lo"] is not None
        else " [CI n/a: <3 genes]"
    )
    return f"{est['point'] * 100:.1f}%{ci}  (n={est['n']})"


def by_aspect(rows: List[dict], value_fn, seed: int) -> str:
    parts = []
    for asp in ASPECTS:
        sub = [r for r in rows if r.get("aspect") == asp]
        parts.append(f"{asp} {fmt(estimate(sub, value_fn, seed=seed))}")
    return "\n    - " + "\n    - ".join(parts)


def is_iba(row: dict) -> bool:
    """Conserved / phylogenetically-inferred annotation (IBA or GO_REF:0000033)."""
    if (row.get("evidence_code") or "").strip().upper() == "IBA":
        return True
    refs = (row.get("original_reference_ids") or "") + (
        row.get("support_reference_ids") or ""
    )
    return "GO_REF:0000033" in refs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--dir",
        default=str(Path(__file__).parent / "sample"),
        help="Directory containing the instrument TSVs",
    )
    ap.add_argument("--seed", type=int, default=20260614)
    ap.add_argument("--out", default=None, help="Optional path to write the markdown report")
    args = ap.parse_args()

    d = Path(args.dir)
    anns = read_tsv(d / "annotation_instrument.tsv")
    blind = read_tsv(d / "blind_ablation_assignments.tsv")
    refs = read_tsv(d / "reference_instrument.tsv")

    lines: List[str] = []
    lines.append("# EVIDENCE_SOURCE_SUFFICIENCY — scoring\n")
    n_labeled = sum(1 for r in anns if (r.get("minimal_sufficient_tier") or "").strip())
    lines.append(
        f"- Annotation rows: **{len(anns)}** (labeled with a tier: **{n_labeled}**)\n"
        f"- Blind-ablation rows: **{len(blind)}**  |  reference rows: **{len(refs)}**\n"
    )
    if n_labeled == 0 and not any(
        (r.get("fact_in_abstract") or "").strip() for r in anns
    ):
        lines.append(
            "\n**No labels filled yet** — fill `annotation_instrument.tsv` "
            "(and the blind/reference instruments), then re-run. Estimand "
            "scaffolding below will populate automatically.\n"
        )

    abstract = lambda r: 1.0 if (r.get("minimal_sufficient_tier") or "").strip().upper() == "ABSTRACT" else (0.0 if (r.get("minimal_sufficient_tier") or "").strip() else None)  # noqa: E731
    review = lambda r: to_bool(r.get("fact_in_review", ""))  # noqa: E731
    deep = lambda r: to_bool(r.get("fact_in_deep_research", ""))  # noqa: E731

    lines.append("\n## E-b (H-b) abstract is the minimal sufficient tier | ACCEPT")
    lines.append(f"- overall: {fmt(estimate(anns, abstract, seed=args.seed))}")
    lines.append(f"- by aspect:{by_aspect(anns, abstract, args.seed)}")

    lines.append("\n## E-a (H-a) a review carries the justifying fact | ACCEPT")
    lines.append(f"- overall: {fmt(estimate(anns, review, seed=args.seed))}")
    lines.append(f"- by aspect:{by_aspect(anns, review, args.seed)}")
    iba_rows = [r for r in anns if is_iba(r)]
    lines.append(
        f"- conserved/IBA subgroup: {fmt(estimate(iba_rows, review, seed=args.seed))}"
    )

    lines.append("\n## E-c (H-c) deep research carries the justifying fact | ACCEPT")
    lines.append(f"- overall: {fmt(estimate(anns, deep, seed=args.seed))}")
    lines.append(f"- by aspect:{by_aspect(anns, deep, args.seed)}")

    lines.append("\n## E-d (H-d) where the justifying fact first appears")
    sec = Counter(
        (r.get("section_of_fact") or "").strip().upper()
        for r in anns
        if (r.get("section_of_fact") or "").strip()
    )
    sec_total = sum(sec.values())
    if sec_total:
        narr = sum(v for k, v in sec.items() if k in NARRATIVE_SECTIONS)
        lines.append(
            f"- narrative (intro/lit-review/discussion/conclusions): "
            f"{100 * narr / sec_total:.1f}%  (n={sec_total})"
        )
        for k, v in sec.most_common():
            lines.append(f"    - {k}: {v} ({100 * v / sec_total:.0f}%)")
    else:
        lines.append("- not yet labeled (n=0)")

    lines.append("\n## Blind-ablation validation (unbiased sufficiency)")
    blind_scored = [r for r in blind if (r.get("blind_verdict") or "").strip()]
    # "Available" = a restricted bundle actually had evidence (not NO_SOURCE).
    blind_avail = [r for r in blind_scored if (r.get("blind_verdict") or "").strip().upper() != "NO_SOURCE"]
    if blind_scored:
        acc = lambda r: 1.0 if (r.get("blind_verdict") or "").strip().upper() == "ACCEPT" else 0.0  # noqa: E731
        for bundle in ("ABSTRACT_ONLY", "REVIEW_ONLY", "DEEP_RESEARCH_ONLY"):
            assigned = [r for r in blind_scored if r.get("bundle") == bundle]
            avail = [r for r in blind_avail if r.get("bundle") == bundle]
            n_assigned = len(assigned)
            n_avail = len(avail)
            lines.append(
                f"- **{bundle}** — source available {n_avail}/{n_assigned}; "
                f"P(ACCEPT | available): {fmt(estimate(avail, acc, seed=args.seed))}; "
                f"P(ACCEPT | assigned): {fmt(estimate(assigned, acc, seed=args.seed))}"
            )
        # calibration vs retrospective E-b (abstract), among available abstracts
        retro = estimate(anns, abstract, seed=args.seed)
        abs_avail = [r for r in blind_avail if r.get("bundle") == "ABSTRACT_ONLY"]
        blind_abs = estimate(abs_avail, acc, seed=args.seed)
        if retro["n"] and blind_abs["n"]:
            lines.append(
                f"- **calibration**: retrospective abstract-sufficient "
                f"{retro['point'] * 100:.1f}% vs blind ACCEPT|ABSTRACT_ONLY (available) "
                f"{blind_abs['point'] * 100:.1f}% "
                f"(gap {100 * (retro['point'] - blind_abs['point']):+.1f} pts = "
                f"retrospective optimism)"
            )
    else:
        lines.append("- not yet labeled (n=0)")

    lines.append("\n## Context: reference-level review rate (H-a denominator)")
    rev_refs = [r for r in refs if (r.get("is_review_final") or "").strip()]
    if rev_refs:
        k = sum(1 for r in rev_refs if to_bool(r.get("is_review_final", "")) == 1.0)
        lines.append(
            f"- references manually confirmed as reviews: {k}/{len(rev_refs)} "
            f"({100 * k / len(rev_refs):.1f}% of confirmed)"
        )
    else:
        lines.append("- `is_review_final` not yet confirmed (n=0)")

    report = "\n".join(lines) + "\n"
    print(report)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"[written to {args.out}]")


if __name__ == "__main__":
    main()
