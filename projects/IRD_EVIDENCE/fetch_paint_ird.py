"""Extract every IRD (Inferred from Rapid Divergence) annotation from PANTHER PAINT.

IRD (ECO:0000321) exists only in PAINT's node-level file, ``IBD.gaf``: GOA carries
no IRD rows at all. This script therefore works from the PAINT release files:

* ``IBD.gaf``: node-level annotations (IBD, IRD, IKR). Each IRD row is a
  ``NOT`` on a ``PTN`` node, and its with/from names the ancestral node whose
  IBD it overrides.
* ``PAINT_TreeGrafter_Annotations_TOTAL.txt.gz``: maps every ``PTN`` node to its
  PANTHER family.
* ``gene_association.paint_uniprot.gaf.gz``: the leaf IBA file. It is scanned to
  count which leaf rows (positive and ``NOT``) descend from an ancestor+term that
  carries an IRD and/or IKR loss.

All three are cached under ``.cache/paint/`` (git-ignored).

Outputs:
  ird_nodes.tsv              one row per IRD node annotation
  leaf_iba_loss_sources.tsv  leaf IBA rows tallied by the losses on their source

Usage:
    uv run python projects/IRD_EVIDENCE/fetch_paint_ird.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

from oaklib import get_adapter

from ai_gene_review.etl.panther_paint import (
    IBD_GAF_URL,
    LEAF_GAF_URL,
    PAINT_BASE,
    download_cached,
    open_text,
    parse_ptn_nodes,
)

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
CACHE = ROOT / ".cache" / "paint"
TREEGRAFTER_URL = f"{PAINT_BASE}/PAINT_TreeGrafter_Annotations_TOTAL.txt.gz"
OUT_NODES = HERE / "ird_nodes.tsv"
OUT_LEAF = HERE / "leaf_iba_loss_sources.tsv"


def node_families(path: Path) -> dict[str, str]:
    """Map PTN node id -> PANTHER family from the TreeGrafter annotation table.

    The first column is ``PTHRnnnnn:ANn`` and the last is the node's PTN id.
    """
    fam: dict[str, str] = {}
    with open_text(path) as fh:
        for line in fh:
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 2 or not cols[-1].startswith("PTN"):
                continue
            fam[cols[-1]] = cols[0].split(":", 1)[0]
    return fam


def main() -> int:
    ibd = download_cached(IBD_GAF_URL, CACHE)
    leaf = download_cached(LEAF_GAF_URL, CACHE)
    tg = download_cached(TREEGRAFTER_URL, CACHE)
    fam = node_families(tg)
    go = get_adapter("sqlite:obo:go")

    rows = [line.rstrip("\n").split("\t") for line in open_text(ibd) if not line.startswith("!")]
    rows = [r for r in rows if len(r) > 13 and r[1].startswith("PTN")]
    evidence = Counter(r[6] for r in rows)
    print(f"IBD.gaf node rows by evidence: {dict(evidence)}", file=sys.stderr)

    # positive IBD terms per node, and losses per (ancestral node, term)
    ibd_terms: dict[str, set[str]] = defaultdict(set)
    losses: dict[tuple[str, str], set[str]] = defaultdict(set)
    for r in rows:
        node, qual, go_id, ev = r[1], r[3], r[4], r[6]
        if "NOT" in qual:
            for anc in parse_ptn_nodes(r[7]):
                losses[(anc, go_id)].add(ev)
        elif ev == "IBD":
            ibd_terms[node].add(go_id)

    labels: dict[str, str] = {}
    out = []
    for r in rows:
        if r[6] != "IRD":
            continue
        node, qual, go_id, aspect = r[1], r[3], r[4], r[8]
        ancs = parse_ptn_nodes(r[7])
        if go_id not in labels:
            labels[go_id] = go.label(go_id) or ""
        anc = ancs[0] if ancs else ""
        out.append(
            {
                "family": fam.get(node, ""),
                "ird_node": node,
                "qualifier": qual,
                "go_id": go_id,
                "go_label": labels[go_id],
                "aspect": aspect,
                "ancestral_node": anc,
                "ancestral_node_family": fam.get(anc, ""),
                "ancestral_has_ibd_for_term": str(go_id in ibd_terms.get(anc, set())).lower(),
                "ikr_on_same_ancestor_term": str("IKR" in losses.get((anc, go_id), set())).lower(),
                "taxon": r[12],
                "date": r[13],
                "assigned_by": r[14],
            }
        )
    out.sort(key=lambda d: (d["family"], d["ird_node"], d["go_id"]))
    with OUT_NODES.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print(f"wrote {len(out)} IRD rows to {OUT_NODES}", file=sys.stderr)

    # Leaf IBA rows: which losses sit on the ancestor+term the row was projected from?
    tally: Counter[tuple[str, str]] = Counter()
    with open_text(leaf) as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 9:
                continue
            go_id = cols[4]
            evs: set[str] = set()
            for n in parse_ptn_nodes(cols[7]):
                evs |= losses.get((n, go_id), set())
            polarity = "NOT" if "NOT" in cols[3] else "positive"
            tally[(polarity, "+".join(sorted(evs)) or "none")] += 1
    with OUT_LEAF.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["leaf_polarity", "losses_on_source_ancestor_term", "leaf_rows"])
        for (pol, evs), n in sorted(tally.items()):
            w.writerow([pol, evs, n])
    print(f"wrote leaf tallies to {OUT_LEAF}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
