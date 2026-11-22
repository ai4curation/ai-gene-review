"""Score reviewed IBA REMOVE rows against successive PAINT snapshots.

For every row of inventory.tsv this replays the term's propagation to the gene in each
dated PAINT snapshot of the pinned PANTHER release (the small ``IBD.gaf`` node file is
enough: a term reaches a leaf when an ancestor carries an IBD for it and no IRD/IKR
loss sits between that ancestor and the leaf). For rows the pinned snapshot no longer
propagates, it also finds from git history when the review first said REMOVE.

Writes ``upstream_outcomes.tsv``. ``outcome`` is computed, never judged:

  STILL_PROPAGATED    the newest snapshot still carries the term to the gene
  PREDICTED           the review said REMOVE while PAINT still carried the term: on or before the last
                      snapshot that propagated it, or before a loss record dated inside the window
  ORDER_UNDETERMINED  the review said REMOVE between the last snapshot that carried the term and the
                      first that did not, so which came first cannot be told from the snapshots
  AGREED_AFTER        PAINT had already dropped the term when the review first said REMOVE; the review
                      worked from a GOA file that still listed the row, so this is independent agreement
  UNDATED             PAINT dropped the term and git history holds no REMOVE to date (a shallow clone
                      does this); the order is unknown, not assumed
  NEVER_PROPAGATED    the gene is on the tree but no snapshot of this release carries the term to it
  NOT_A_LEAF          the gene is not a leaf of a tree we can read, so nothing can be replayed

A loss blocks a term when it sits on the lineage at or below the IBD. Depth is read from clade
size, so a loss on a single-child node directly above the IBD, which has the same clade, would
be read as blocking; the cached tree does not record the order of such nodes.

``upstream_change`` says what PAINT did: LOSS_ADDED (an IRD or IKR on the lineage),
IBD_WITHDRAWN (no IBD for the term left in the family), or IBD_MOVED (an IBD for the
term remains in the family, off the gene's lineage).

    uv run python projects/IBA_REVIEW/rereview-2026-11-21/upstream_outcomes.py
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

import requests

from ai_gene_review.etl.panther_families import PAINT_ROOT, PANTHER_RELEASE
from ai_gene_review.etl.panther_paint import parse_ibd_gaf
from ai_gene_review.etl.panther_trees import ancestors_of, leaf_nodes_for, leaves_below, load_family
from ai_gene_review.validation.gene_paint_losses import is_loss, panther_families
from ai_gene_review.yaml_utils import safe_load

HERE = Path(__file__).parent
CACHE = Path(".cache") / "paint_history"
FIELDS = [
    "gene_file", "accession", "go_id", "go_label", "family", "outcome", "upstream_change",
    "first_snapshot_propagated", "last_snapshot_propagated", "first_snapshot_dropped", "loss_node",
    "loss_evidence", "loss_date", "loss_date_after_drop", "review_first_remove_date", "review_first_remove_commit",
]


def snapshots() -> list[str]:
    """Dated snapshot directories of the pinned PANTHER release, oldest first."""
    html = requests.get(f"{PAINT_ROOT}/{PANTHER_RELEASE}/", timeout=60).text
    return sorted(set(re.findall(r'href="(\d{4}-\d{2}-\d{2})/"', html)))


def ibd_for(snapshot: str) -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"IBD-{snapshot}.gaf"
    if not path.exists() or path.stat().st_size == 0:
        r = requests.get(f"{PAINT_ROOT}/{PANTHER_RELEASE}/{snapshot}/IBD.gaf", timeout=300)
        r.raise_for_status()
        path.write_bytes(r.content)
    with open(path) as fh:
        return parse_ibd_gaf(fh)


def state(tree: dict, leaf: str, ibd: dict, go: str) -> tuple[bool, tuple[str, str, str] | None, bool]:
    """(propagated, blocking loss, an IBD for the term exists anywhere in the family)."""
    lineage = sorted(ancestors_of(tree, leaf), key=lambda n: len(leaves_below(tree, n)))
    recs = [(n, r) for n in lineage for r in ibd.get(n, []) if r.go_id == go]
    pos = [(n, r) for n, r in recs if not is_loss(r)]
    loss = [(n, r) for n, r in recs if is_loss(r)]
    anywhere = any(
        r.go_id == go and not is_loss(r) for n in list(tree["under"]) + list(tree["leaves"]) for r in ibd.get(n, [])
    )
    if not pos:
        return False, None, anywhere
    top = len(leaves_below(tree, pos[0][0]))
    block = next(((n, r.evidence, r.date) for n, r in loss if len(leaves_below(tree, n)) <= top), None)
    return block is None, block, anywhere


def first_remove(gene_file: str, go: str) -> tuple[str, str]:
    """Date and commit of the first version of the review whose IBA row on ``go`` is REMOVE."""
    log = subprocess.run(
        ["git", "log", "--follow", "--reverse", "--format=%H %cs", "--", gene_file],
        capture_output=True, text=True, check=False,
    ).stdout.split("\n")
    for line in filter(None, log):
        commit, date = line.split()
        blob = subprocess.run(["git", "show", f"{commit}:{gene_file}"], capture_output=True, text=True, check=False)
        if blob.returncode != 0 or "REMOVE" not in blob.stdout:
            continue
        try:
            doc = safe_load(blob.stdout) or {}
        except Exception:  # an unparseable historical version is skipped, not guessed at
            continue
        for a in doc.get("existing_annotations") or []:
            if (
                a.get("evidence_type") == "IBA"
                and (a.get("term") or {}).get("id") == go
                and (a.get("review") or {}).get("action") == "REMOVE"
            ):
                return date, commit[:10]
    return "", ""


def main() -> None:
    snaps = snapshots()
    ibds = {s: ibd_for(s) for s in snaps}
    out = []
    for r in csv.DictReader(open(HERE / "inventory.tsv"), delimiter="\t"):
        row = dict.fromkeys(FIELDS, "")
        row.update({k: r[k] for k in ("gene_file", "accession", "go_id", "go_label")})
        up = Path(r["gene_file"].replace("-ai-review.yaml", "-uniprot.txt"))
        fams = [r["family"]] if r["family"] else (panther_families(up.read_text()) if up.exists() else [])
        tree = leaf = None
        for fam in fams:
            t = load_family(fam, Path(".cache/panther_trees"))
            lv = leaf_nodes_for(t, r["accession"]) if t else []
            if lv:
                tree, leaf, row["family"] = t, lv[0], fam
                break
        if tree is None:
            row["outcome"] = "NOT_A_LEAF"
            out.append(row)
            continue
        hist = {s: state(tree, leaf, ibds[s], r["go_id"]) for s in snaps}
        on = [s for s in snaps if hist[s][0]]
        row["first_snapshot_propagated"] = on[0] if on else ""
        row["last_snapshot_propagated"] = on[-1] if on else ""
        if hist[snaps[-1]][0]:
            row["outcome"] = "STILL_PROPAGATED"
            out.append(row)
            continue
        dropped = next((s for s in snaps if (not on or s > on[-1]) and not hist[s][0]), snaps[-1])
        _, block, anywhere = hist[snaps[-1]]
        row["first_snapshot_dropped"] = dropped if on else ""
        if block:
            row["upstream_change"] = "LOSS_ADDED"
            row["loss_node"], row["loss_evidence"], row["loss_date"] = block
        else:
            row["upstream_change"] = "IBD_MOVED" if anywhere else "IBD_WITHDRAWN"
        date, commit = first_remove(r["gene_file"], r["go_id"])
        row["review_first_remove_date"], row["review_first_remove_commit"] = date, commit
        if not on:
            row["outcome"] = "NEVER_PROPAGATED"  # the GOA row predates every snapshot of this release
        else:
            # The change happened after the last snapshot that carried the term and by the first that
            # did not. A loss record carries its own date, which can narrow that window, but a loss dated
            # after the first snapshot that dropped the term cannot be what dropped it, so the earlier of
            # the two is used and the disagreement is recorded.
            changed_by = dropped
            if block and block[2]:
                loss_day = f"{block[2][:4]}-{block[2][4:6]}-{block[2][6:]}"
                row["loss_date_after_drop"] = loss_day > dropped
                changed_by = min(dropped, loss_day)
            if not date:
                row["outcome"] = "UNDATED"  # no REMOVE found in git history (for example a shallow clone)
            elif date >= changed_by:
                row["outcome"] = "AGREED_AFTER"
            elif (block and changed_by < dropped) or date <= on[-1]:
                row["outcome"] = "PREDICTED"
            else:
                row["outcome"] = "ORDER_UNDETERMINED"
        out.append(row)
    with open(HERE / "upstream_outcomes.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    counts: dict[str, int] = {}
    for x in out:
        key = x["outcome"] + (":" + x["upstream_change"] if x["upstream_change"] else "")
        counts[key] = counts.get(key, 0) + 1
    print(f"snapshots {snaps[0]} .. {snaps[-1]} ({len(snaps)})", counts, file=sys.stderr)


if __name__ == "__main__":
    main()
