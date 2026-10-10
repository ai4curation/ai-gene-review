"""Report how much of PANTHER PAINT's IBD.gaf is covered by our family reviews.

Three levels of coverage, by evidence code (IBD gains; IRD/IKR losses):

* **assessed**: the (node, term) row has a ``node_assessments`` entry in a family review
  (``interpro/panther/<FAM>/<FAM>-review.yaml``).
* **in a reviewed family**: the row's node belongs to a family that has a review at all.
* **leaf IBAs** (``--leaf``): leaf IBA rows in PAINT's leaf GAF whose source node+term
  has been assessed. This weights coverage by how many gene annotations a node produces.

Uses the cached PAINT release files in ``.cache/paint/`` (downloaded if missing).
Prints a markdown summary; writes no files.

Usage:
    uv run python scripts/paint_review_coverage.py [--leaf]
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from ai_gene_review.etl.panther_paint import (
    IBD_GAF_URL,
    LEAF_GAF_URL,
    PAINT_BASE,
    download_cached,
    open_text,
    parse_ptn_nodes,
)

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "paint"
TREEGRAFTER_URL = f"{PAINT_BASE}/PAINT_TreeGrafter_Annotations_TOTAL.txt.gz"


def node_families(path: Path) -> dict[str, set[str]]:
    """PTN node -> PANTHER families (PTN ids are not always family-unique)."""
    fams: dict[str, set[str]] = defaultdict(set)
    with open_text(path) as fh:
        for line in fh:
            cols = line.rstrip("\n").split("\t")
            if len(cols) >= 2 and cols[-1].startswith("PTN"):
                fams[cols[-1]].add(cols[0].split(":", 1)[0])
    return fams


def reviewed() -> tuple[set[str], set[tuple[str, str]], Counter]:
    """Reviewed families, assessed (node, term) pairs, and verdict counts."""
    families: set[str] = set()
    assessed: set[tuple[str, str]] = set()
    verdicts: Counter = Counter()
    for path in sorted(ROOT.glob("interpro/panther/*/PTHR*-review.yaml")):
        doc = yaml.safe_load(path.read_text()) or {}
        families.add(str(doc.get("family_id", "")).split(":")[-1])
        for a in doc.get("node_assessments") or []:
            node = str(a.get("node_id", "")).split(":")[-1]
            term = (a.get("asserted_term") or {}).get("id", "")
            assessed.add((node, term))
            verdicts[a.get("assessment", "")] += 1
    return families, assessed, verdicts


def pct(a: int, b: int) -> str:
    return f"{100 * a / b:.2f}%" if b else "n/a"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--leaf", action="store_true", help="also weight by leaf IBA rows (scans ~400 MB)")
    args = ap.parse_args()

    ibd = download_cached(IBD_GAF_URL, CACHE)
    fam_of = node_families(download_cached(TREEGRAFTER_URL, CACHE))
    families, assessed, verdicts = reviewed()

    total: Counter = Counter()
    in_fam: Counter = Counter()
    hit: Counter = Counter()
    gaf_families: set[str] = set()
    with open_text(ibd) as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            c = line.rstrip("\n").split("\t")
            if len(c) < 9 or not c[1].startswith("PTN"):
                continue
            ev = c[6]
            total[ev] += 1
            fams = fam_of.get(c[1], set())
            gaf_families |= fams
            if fams & families:
                in_fam[ev] += 1
            if (c[1], c[4]) in assessed:
                hit[ev] += 1

    out = [
        "# PAINT IBD.gaf coverage by family reviews",
        "",
        f"Family reviews: {len(families)} of {len(gaf_families)} families with PAINT node rows "
        f"({pct(len(families & gaf_families), len(gaf_families))}). "
        f"Node assessments: {sum(verdicts.values())}.",
        "",
        "| Evidence | IBD.gaf rows | In a reviewed family | Assessed |",
        "|---|---|---|---|",
    ]
    for ev in sorted(total, key=lambda e: -total[e]) + ["all"]:
        t = sum(total.values()) if ev == "all" else total[ev]
        f = sum(in_fam.values()) if ev == "all" else in_fam[ev]
        h = sum(hit.values()) if ev == "all" else hit[ev]
        out.append(f"| {ev} | {t} | {f} ({pct(f, t)}) | {h} ({pct(h, t)}) |")
    out += ["", "Verdicts: " + ", ".join(f"{k} {v}" for k, v in verdicts.most_common())]

    if args.leaf:
        leaf = download_cached(LEAF_GAF_URL, CACHE)
        n = covered = 0
        with open_text(leaf) as fh:
            for line in fh:
                if line.startswith("!"):
                    continue
                c = line.split("\t")
                if len(c) < 9:
                    continue
                n += 1
                if any((p, c[4]) in assessed for p in parse_ptn_nodes(c[7])):
                    covered += 1
        out += ["", f"Leaf IBA rows whose source node+term is assessed: {covered} of {n} ({pct(covered, n)})."]

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
