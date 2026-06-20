#!/usr/bin/env python3
"""Extract and flag PANTHER IBA propagations for reviewed S. pombe genes.

For every IBA annotation (GO_REF:0000033 / ECO:0000318) on a reviewed gene this
script reconstructs the phylogenetic propagation from the GOA ``with/from`` field:

* the ancestral PANTHER node (PTN...) the annotation was propagated from,
* the seed genes (the experimentally-annotated relatives that justified it),
* the PANTHER subfamily of our gene and of each UniProt seed (from the cached
  ``interpro/panther/<FAM>/<FAM>-entries.csv`` member tables).

It then flags propagations that crossed subfamily boundaries (the characteristic
IBA over-propagation failure mode) and cross-references the curation action we
assigned to that annotation, so the family review can focus on real risks.

Nothing is hardcoded: all results derive from the cached GOA/UniProt/PANTHER
files in the repo. Run from the repo root:

    python3 projects/PANTHER_IBA_REVIEW/extract_iba_propagation.py
"""
from __future__ import annotations
import csv
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
PANTHER = REPO / "interpro" / "panther"

# Reuse the PAINT node-level ingest engine.
sys.path.insert(0, str(REPO / "src"))
from ai_gene_review.etl.panther_paint import (  # noqa: E402
    IBD_GAF_URL,
    IBDRecord,
    download_cached,
    parse_ibd_gaf,
)

GENES = [
    # batch 1
    "wee1", "cdc25", "cdc2", "cdc13", "chk1", "cds1", "rad3", "sty1", "wis1",
    "atf1", "pap1", "mei2", "ste11", "clr4", "ago1", "dcr1", "cnp1", "cdc42",
    "pom1", "swi6",
    # batch 2
    "plo1", "ark1", "cut7", "ase1", "mid1", "cdc12", "sid2", "cdc7", "rad21",
    "sgo1", "bub1", "mad2", "mph1", "slp1", "cut1", "cut2", "cdc18", "rhp51",
    "mus81", "rqh1",
]

IBA_REF = "GO_REF:0000033"
CC = "cellular_component"


def gene_panther(uniprot_txt: Path) -> tuple[str | None, str | None]:
    """Return (family PTHRxxxxx, subfamily PTHRxxxxx:SFn) from a UniProt record."""
    fam = sub = None
    for line in uniprot_txt.read_text().splitlines():
        m = re.search(r"PANTHER;\s*(PTHR\d+:SF\d+);", line)
        if m:
            sub = m.group(1)
        else:
            m = re.search(r"PANTHER;\s*(PTHR\d+);", line)
            if m:
                fam = m.group(1)
    return fam, sub


def gene_accession(review_yaml: Path) -> str | None:
    d = yaml.safe_load(review_yaml.read_text())
    return d.get("id")


def iba_actions(review_yaml: Path) -> dict[str, str]:
    """Map GO id -> review action for IBA annotations in a review file."""
    d = yaml.safe_load(review_yaml.read_text())
    out: dict[str, str] = {}
    for a in d.get("existing_annotations", []) or []:
        if a.get("evidence_type") != "IBA":
            continue
        term = (a.get("term") or {}).get("id")
        action = (a.get("review") or {}).get("action")
        if term and action and term not in out:
            out[term] = action
    return out


def family_subfamilies(family: str) -> dict[str, str]:
    """Map UniProt id -> subfamily accession for all members of a cached family."""
    path = PANTHER / family / f"{family}-entries.csv"
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    with path.open() as fh:
        for r in csv.DictReader(fh):
            sf = (r.get("subfamily") or "").strip()
            if r.get("id"):
                out[r["id"]] = sf
    return out


def parse_withfrom(value: str) -> tuple[list[str], list[str]]:
    """Return (PTN nodes, UniProt seed ids) from a GOA with/from field."""
    nodes, seeds = [], []
    for tok in value.split("|"):
        tok = tok.strip()
        if tok.startswith("PANTHER:PTN"):
            nodes.append(tok.split(":", 1)[1])
        elif tok.startswith("UniProtKB:"):
            seeds.append(tok.split(":", 1)[1])
    return nodes, seeds


def node_info(
    ibd_index: dict[str, list[IBDRecord]], nodes: list[str], go_id: str
) -> tuple[bool, int, str, bool]:
    """Look up the node-level (PAINT) record(s) for a propagated (node, GO).

    Returns ``(found, node_seed_count, node_evidence, node_loss)`` where:

    * ``found`` is True if any node carries this GO at the node level,
    * ``node_seed_count`` is the largest canonical seed set across matches (the
      authoritative count curated at the node, vs. the few echoed into a leaf),
    * ``node_evidence`` is the ``;``-joined evidence codes (IBD/IRD/IKR),
    * ``node_loss`` is True if any matching record is a loss (IRD/IKR ``NOT``).
    """
    found = False
    best_seeds = 0
    evidences: list[str] = []
    loss = False
    for node in nodes:
        for rec in ibd_index.get(node, []):
            if rec.go_id != go_id:
                continue
            found = True
            best_seeds = max(best_seeds, len(rec.seeds))
            if rec.evidence not in evidences:
                evidences.append(rec.evidence)
            loss = loss or rec.negated
    return found, best_seeds, ";".join(evidences), loss


def main() -> None:
    ibd_path = download_cached(IBD_GAF_URL, REPO / ".cache" / "panther")
    with ibd_path.open() as fh:
        ibd_index = parse_ibd_gaf(fh)

    rows = []
    for gene in GENES:
        gdir = REPO / "genes" / "SCHPO" / gene
        review = gdir / f"{gene}-ai-review.yaml"
        goa = gdir / f"{gene}-goa.tsv"
        uniprot = gdir / f"{gene}-uniprot.txt"
        if not goa.exists():
            print(f"WARN missing {goa}", file=sys.stderr)
            continue
        fam, sub = gene_panther(uniprot)
        acc = gene_accession(review)
        actions = iba_actions(review)
        sf_map = family_subfamilies(fam) if fam else {}
        for line in goa.read_text().splitlines():
            f = line.split("\t")
            if len(f) < 11 or IBA_REF not in line:
                continue
            go_id, go_label, aspect, withfrom = f[4], f[5], f[6], f[10]
            nodes, seeds = parse_withfrom(withfrom)
            # subfamilies of UniProt seeds that are members of our gene's family
            seed_sfs = [sf_map[s] for s in seeds if s in sf_map]
            same = sum(1 for x in seed_sfs if sub and x == sub)
            other = sum(1 for x in seed_sfs if x and x != sub)
            other_sfs = sorted({x for x in seed_sfs if x and x != sub})
            # node-level (PAINT) lookup for the authoritative seed count + loss
            node_found, node_seeds, node_evidence, node_loss = node_info(
                ibd_index, nodes, go_id
            )
            # flagging
            flags = []
            if seed_sfs and same == 0 and other > 0:
                flags.append("CROSS_SUBFAMILY")
            if aspect == CC:
                flags.append("LOCALIZATION")
            if not sub:
                flags.append("GENE_NO_SUBFAMILY")
            if not seeds:
                flags.append("NO_UNIPROT_SEEDS")
            # Node-level seed count is the authoritative confidence signal.
            if node_found and node_seeds <= 1:
                flags.append("SINGLE_NODE_SEED")
            if not node_found:
                flags.append("NODE_NOT_IN_IBD")
            if node_loss:
                flags.append("NODE_LOSS")
            rows.append({
                "gene": gene,
                "acc": acc or "",
                "family": fam or "",
                "subfamily": sub or "",
                "go_id": go_id,
                "go_label": go_label,
                "aspect": aspect,
                "node": ";".join(nodes),
                "n_seeds": len(seeds),
                "n_seed_in_fam": len(seed_sfs),
                "same_sf": same,
                "other_sf": other,
                "other_subfamilies": ";".join(other_sfs),
                "node_seed_count": node_seeds,
                "node_evidence": node_evidence,
                "node_loss": "true" if node_loss else "false",
                "our_action": actions.get(go_id, "?"),
                "flags": ";".join(flags),
            })

    out = REPO / "projects" / "PANTHER_IBA_REVIEW" / "iba_propagation.tsv"
    cols = list(rows[0].keys())
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # console summary
    n = len(rows)
    cross = [r for r in rows if "CROSS_SUBFAMILY" in r["flags"]]
    single = [r for r in rows if "SINGLE_NODE_SEED" in r["flags"]]
    losses = [r for r in rows if r["node_loss"] == "true"]
    not_in_ibd = [r for r in rows if "NODE_NOT_IN_IBD" in r["flags"]]
    print(f"IBA annotations analyzed: {n}")
    print(f"  with UniProt seeds mappable to family subfamilies: "
          f"{sum(1 for r in rows if r['n_seed_in_fam'])}")
    print(f"  CROSS_SUBFAMILY (seeds only from other subfamilies): {len(cross)}")
    print(f"  SINGLE_NODE_SEED (<=1 canonical seed at the source node): {len(single)}")
    print(f"  NODE_LOSS (IRD/IKR at the source node): {len(losses)}")
    print(f"  NODE_NOT_IN_IBD (node/GO not found in IBD.gaf): {len(not_in_ibd)}")
    print("\nCROSS_SUBFAMILY propagations (the review targets):")
    for r in sorted(cross, key=lambda r: (r["gene"], r["go_id"])):
        print(f"  {r['gene']:7s} {r['go_id']} {r['go_label'][:42]:42s} "
              f"[{r['aspect'][:4]}] our={r['our_action']:22s} "
              f"-> {r['other_subfamilies']}")
    print(f"\nWrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
