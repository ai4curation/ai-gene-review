"""Flag IBA REMOVE rows whose written reason may not be a ground for removal.

Two independent signals per LIVE_IBD row of inventory.tsv, written to reason_scan.tsv:

1. Where the seeds sit (computed from the tree). The IBD node's seeds are mapped to
   leaves, and the smallest clade holding the target and any seed is found.
   ``seed_in_target_child_clade`` is true when a seed sits in the same child clade of
   the IBD node as the target; ``nearest_seed_clade_leaves`` is the size of the
   smallest clade shared with a seed. A REMOVE whose target shares a small clade with
   a seed cannot rest on "the seeds are elsewhere in the family".
2. What the reason says (phrase matching on review.reason and review.summary):
   absence of evidence on the target, term obsolescence, redundancy, donor counting,
   and whether any divergence, loss, lineage or bad-seed argument is made at all.

The flags are leads for the manual re-review, never verdicts.

    uv run python projects/IBA_REVIEW/rereview-2026-11-21/reason_scan.py
"""

from __future__ import annotations

import csv
import gzip
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from ai_gene_review.etl.panther_paint import IBD_GAF_URL, download_cached, open_text, parse_ibd_gaf
from ai_gene_review.etl.panther_trees import TREE_URL, _children, leaves_below, load_family
from ai_gene_review.validation.gene_paint_losses import is_loss, paint_cache_dir
from ai_gene_review.yaml_utils import safe_load

HERE = Path(__file__).parent
NAMES = Path(".cache") / "panther_leaf_names"

PHRASES = {
    "absence_of_evidence": r"no (direct |experimental |published |reviewed |known )*(experimental )?(evidence|data|support|report)|not (been )?(experimentally )?(demonstrated|shown|tested|established|reported)|lacks? (direct|experimental) (evidence|support)|unsupported|no .{0,30} evidence supports",
    "obsolete_term": r"obsolete",
    "redundancy": r"redundan|duplicat|already (covered|captured|annotated)|subsumed",
    "donor_count": r"single[- ](donor|seed|source)|only (one|a single) (donor|seed|source)|sole (donor|seed)|short with/?from|circular",
    "seeds_elsewhere": r"seeded elsewhere|outside the clade|other (branch|clade|subfamily)|different (branch|clade|subfamily)|distinct (clade|branch|subfamily)",
}
GROUND = r"pseudo|catalytic(ally)? (dead|inactive|residue)|lost|loss of|lacks? the|diverg|neofunction|paralog|subfamil|lineage|absent (in|from)|does not (exist|occur)|not present in|contradict|refut|exclud|instead|mis-?annot|wrong (seed|gene|paper)|seed (is|paper|error)|duplication"


def leaf_names(family: str) -> dict[str, str]:
    """``leaf PTN -> node_name`` (ORG|DB=id|UniProtKB=ACC) for a family, cached."""
    NAMES.mkdir(parents=True, exist_ok=True)
    path = NAMES / f"{family}.json.gz"
    if path.exists():
        with gzip.open(path, "rt") as fh:
            return json.load(fh)
    out: dict[str, str] = {}
    try:
        payload = requests.get(TREE_URL, params={"family": family}, timeout=300).json()
        stack = [payload["search"]["tree_topology"]["annotation_node"]]
        while stack:
            n = stack.pop()
            kids = _children(n)
            if kids:
                stack.extend(kids)
            else:
                out[n.get("persistent_id", "")] = n.get("node_name", "")
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"{family}: {e}", file=sys.stderr)
        return {}
    with gzip.open(path, "wt") as fh:
        json.dump(out, fh)
    return out


def seed_keys(seed: str) -> set[str]:
    """Strings a seed id may appear as in a node_name (``MGI:MGI:96897`` -> ``MGI=96897``, ...)."""
    db, _, rest = seed.partition(":")
    keys = {rest, rest.split(":")[-1]}
    return {k for k in keys if k}


def main() -> None:
    with open_text(download_cached(IBD_GAF_URL, paint_cache_dir(Path(".cache/paint")))) as fh:
        ibd = parse_ibd_gaf(fh)
    rows = [r for r in csv.DictReader(open(HERE / "inventory.tsv"), delimiter="\t") if r["status"] == "LIVE_IBD"]
    with ThreadPoolExecutor(8) as ex:
        names = dict(zip(sorted({r["family"] for r in rows}), ex.map(leaf_names, sorted({r["family"] for r in rows}))))
    reviews: dict[str, dict] = {}
    out = []
    for r in rows:
        tree = load_family(r["family"], Path(".cache/panther_trees"))
        doc = reviews.setdefault(r["gene_file"], safe_load(Path(r["gene_file"]).read_text()))
        ann = next(
            (a for a in doc["existing_annotations"]
             if a.get("evidence_type") == "IBA" and a["term"]["id"] == r["go_id"] and bool(a.get("negated")) == (r["negated"] == "True")),
            None,
        )
        rev = (ann or {}).get("review") or {}
        text = f"{rev.get('summary', '')} {rev.get('reason', '')}".lower()
        node = r["ibd_node"]
        rec = next((x for x in ibd.get(node, []) if x.go_id == r["go_id"] and not is_loss(x)), None)
        clade = leaves_below(tree, node)
        nm = names.get(r["family"], {})
        seed_leaves, unmapped = set(), 0
        for s in (rec.seeds if rec else []):
            if s.startswith("PANTHER:"):
                continue
            keys = seed_keys(s)
            hit = [lf for lf in clade if any(f"={k}" in nm.get(lf, "") + "|" and re.search(rf"[=:]{re.escape(k)}(\||$)", nm.get(lf, "")) for k in keys)]
            if hit:
                seed_leaves.update(hit)
            else:
                unmapped += 1
        target = next((lf for lf in clade if tree["leaves"][lf].get("uniprot") == r["accession"]), None)
        inner = sorted((n for n, below in tree["under"].items() if target in below and set(below) <= set(clade)), key=lambda n: len(tree["under"][n]))
        nearest = next((n for n in inner if seed_leaves & set(tree["under"][n]) - {target}), "")
        child = inner[-2] if len(inner) >= 2 else ""
        flags = [k for k, p in PHRASES.items() if re.search(p, text)]
        row = {
            "gene_file": r["gene_file"], "go_id": r["go_id"], "go_label": r["go_label"],
            "action_now": rev.get("action", "(row gone)"), "family": r["family"], "ibd_node": node,
            "clade_leaves": len(clade), "seeds": len(rec.seeds) if rec else 0, "seeds_mapped": len(seed_leaves),
            "seeds_unmapped": unmapped, "target_is_seed": target in seed_leaves,
            "seed_in_target_child_clade": bool(child and (seed_leaves - {target}) & set(tree["under"][child])),
            "nearest_seed_clade": nearest,
            "nearest_seed_clade_leaves": len(tree["under"][nearest]) if nearest else "",
            "reason_flags": ";".join(flags),
            "states_a_ground": bool(re.search(GROUND, text)),
            "cites_node": "ptn0" in text,
        }
        out.append(row)
    with open(HERE / "reason_scan.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, list(out[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print(len(out), "rows written", file=sys.stderr)


if __name__ == "__main__":
    main()
