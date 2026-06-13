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


def main() -> None:
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
    print(f"IBA annotations analyzed: {n}")
    print(f"  with UniProt seeds mappable to family subfamilies: "
          f"{sum(1 for r in rows if r['n_seed_in_fam'])}")
    print(f"  CROSS_SUBFAMILY (seeds only from other subfamilies): {len(cross)}")
    print("\nCROSS_SUBFAMILY propagations (the review targets):")
    for r in sorted(cross, key=lambda r: (r["gene"], r["go_id"])):
        print(f"  {r['gene']:7s} {r['go_id']} {r['go_label'][:42]:42s} "
              f"[{r['aspect'][:4]}] our={r['our_action']:22s} "
              f"-> {r['other_subfamilies']}")
    print(f"\nWrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
