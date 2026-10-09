#!/usr/bin/env python3
"""Group strong R. toruloides fitness defects into nutrient modules.

Joins ``data/rhoto_specific_defects.tsv`` and
``data/rhoto_accession_resolution.tsv`` (written by
``projects/PROTEOME_REMOVAL/scripts/resolve_deleted_accessions.py``), keeps genes whose strongest specific
defect is <= --strong (default -3) in at most --max-conditions carbon
conditions (default 6), assigns each to a module by the conditions it is
defective in, and annotates the current UniProtKB entry (protein name,
annotation score, number of GO terms, and whether
``projects/GENE_MODEL_ERRORS`` found the entry to be a fused gene model). Output:
``data/rhoto_candidates.tsv``.

    uv run python projects/FUNGAL_PHENOTYPES/scripts/rhoto_candidates.py

Module assignment is by condition only; it says which growth conditions need
the gene, not what the gene does.
"""

from __future__ import annotations

import argparse
import collections
import csv
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

DATA = Path("projects/FUNGAL_PHENOTYPES/data")
# Optional: fused current entries found by projects/GENE_MODEL_ERRORS.
FUSIONS = Path("projects/GENE_MODEL_ERRORS/data/rhoto_fusion_genetics.tsv")
MODULES = {
    "aromatic": ["Benzoate", "p-Coumarate", "Ferulate", "Phenylalanine"],
    "branched_chain_amino_acid": ["Leucine", "Valine"],
    "pentose_polyol": [
        "Xylose", "Arabinose", "L-lyxose", "D-arabitol", "L-arabitol",
        "xylitol", "D-ribulose", "D-xylulose",
    ],
    "galactose": ["Galactose"],
    "fatty_acid_acetate": ["Oleic Acid", "Acetate"],
    "lactate": ["Lactate"],
    "cellobiose_mannose": ["Cellobiose", "Mannose"],
}


def parse(conds: str) -> dict[str, float]:
    out = {}
    for part in conds.split("; "):
        name, val = part.rsplit("=", 1)
        out[name] = float(val)
    return out


def module_of(defects: dict[str, float]) -> str:
    """Module holding the gene's strongest defect."""
    worst = min(defects, key=defects.get)
    for mod, keys in MODULES.items():
        if any(worst.endswith(k) for k in keys):
            return mod
    return "other"


def uniprot_info(accs: list[str]) -> dict[str, tuple[str, str, int]]:
    info = {}
    for i in range(0, len(accs), 100):
        batch = accs[i : i + 100]
        params = {
            "query": " OR ".join(f"accession:{a}" for a in batch),
            "fields": "accession,protein_name,annotation_score,go_id",
            "format": "tsv",
            "size": 500,
        }
        url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=120) as r:
            for line in r.read().decode().splitlines()[1:]:
                f = line.split("\t") + ["", "", ""]
                go = [g for g in f[3].split(";") if g.strip()]
                info[f[0]] = (f[1], f[2], len(go))
        time.sleep(0.2)
    return info


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--strong", type=float, default=-3.0)
    ap.add_argument("--max-conditions", type=int, default=6)
    args = ap.parse_args()

    res = {r["accession"]: r for r in csv.DictReader((DATA / "rhoto_accession_resolution.tsv").open(), delimiter="\t")}
    unresolved = {"replacement": "", "call": "no_accession"}
    keep = []
    for r in csv.DictReader((DATA / "rhoto_specific_defects.tsv").open(), delimiter="\t"):
        d = parse(r["defective_conditions"])
        if min(d.values()) <= args.strong and len(d) <= args.max_conditions:
            keep.append((r, d))

    fused = {}
    if FUSIONS.exists():
        for f in csv.DictReader(FUSIONS.open(), delimiter="\t"):
            fused[f["target"]] = f["evidence"]
    accs = sorted({res.get(r["uniprot_2023"], unresolved)["replacement"] for r, _ in keep} - {""})
    info = uniprot_info(accs)

    out = DATA / "rhoto_candidates.tsv"
    counts = collections.Counter()
    with out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(
            ["module", "rto4_id", "strongest_fitness", "defective_conditions",
             "current_accession", "resolution", "current_protein_name",
             "annotation_score", "n_go_terms", "current_entry_fused",
             "kog_annotation", "sc_orthologs"]
        )
        rows = []
        for r, d in keep:
            rr = res.get(r["uniprot_2023"], unresolved)
            acc = rr["replacement"] if rr["call"] != "weak" else ""
            name, score, ngo = info.get(acc, ("", "", 0))
            mod = module_of(d)
            counts[mod] += 1
            rows.append(
                [mod, r["rto4_id"], f"{min(d.values()):.1f}", r["defective_conditions"],
                 acc, rr["call"], name, score, ngo, fused.get(acc, ""),
                 r["kog_annotation"], r["sc_orthologs"]]
            )
        for row in sorted(rows, key=lambda x: (x[0], float(x[2]))):
            w.writerow(row)
    print(f"{len(keep)} strong specific genes by module: {dict(counts)}", file=sys.stderr)
    print(f"wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
