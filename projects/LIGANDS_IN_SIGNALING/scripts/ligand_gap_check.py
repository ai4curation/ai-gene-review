"""Ligand gap check over GO Consortium GAFs.

Rule: for each organism, every receptor-initiated signaling pathway term P that the
organism's GAF uses directly must contain at least one gene that is involved_in P
(or a subterm, via is_a/part_of) and enables receptor ligand activity (GO:0048018
or an is_a subterm).

Pathway scope: non-obsolete is_a descendants of GO:0007166 cell surface receptor
signaling pathway OR GO:0007186 G protein-coupled receptor signaling pathway (GPCR
signaling is not under GO:0007166, because it can start at internal membranes).

Counted annotations: positive (no NOT) rows, any evidence code; BP rows with
qualifier involved_in; MF rows with qualifier enables.

Also reports the reverse check: ligand-activity genes not involved_in any signal
transduction term (GO:0007165 or a subterm).

--or-receptor-binding is an experimental mode that also counts genes with an MF
under GO:0005102 signaling receptor binding plus an extracellular-region CC
annotation. It produces mostly false passes (see the project page); kept only so
the result can be reproduced.

Usage:
  uv run python projects/LIGANDS_IN_SIGNALING/scripts/ligand_gap_check.py \
      --data .cache/ligands_in_signaling --out projects/LIGANDS_IN_SIGNALING/results
"""
from __future__ import annotations

import argparse
import collections
import gzip
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from go_ontology import GO  # noqa: E402

ORGANISMS = {
    "human": "goa_human",
    "mouse": "mgi",
    "rat": "rgd",
    "zebrafish": "zfin",
    "fly": "fb",
    "yeast": "sgd",
    "pombe": "pombase",
}
CELL_SURFACE = "GO:0007166"
GPCR = "GO:0007186"
SIGNAL_TRANSDUCTION = "GO:0007165"
LIGAND_ACTIVITY = "GO:0048018"
RECEPTOR_BINDING = "GO:0005102"
EXTRACELLULAR_REGION = "GO:0005576"


def read_gaf(path: Path):
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 15 or "NOT" in cols[3]:
                continue
            yield cols


def check_organism(go: GO, gaf: Path, pathways: set[str], or_receptor_binding: bool) -> dict:
    symbol: dict[str, str] = {}
    ligand, binding, extracellular, in_signal = set(), set(), set(), set()
    genes_in = collections.defaultdict(set)
    direct = collections.defaultdict(set)
    for c in read_gaf(gaf):
        gene, sym, qual, term, aspect = c[1], c[2], c[3], c[4], c[8]
        symbol[gene] = sym
        if aspect == "F" and qual == "enables":
            anc = go.ancestors(term)
            if LIGAND_ACTIVITY in anc:
                ligand.add(gene)
            if RECEPTOR_BINDING in anc:
                binding.add(gene)
        elif aspect == "C" and EXTRACELLULAR_REGION in go.ancestors(term, True):
            extracellular.add(gene)
        elif aspect == "P" and qual == "involved_in":
            direct[term].add((gene, c[6]))
            anc = go.ancestors(term, True)
            if SIGNAL_TRANSDUCTION in anc:
                in_signal.add(gene)
            for a in anc & pathways:
                genes_in[a].add(gene)
    counted = ligand | (binding & extracellular) if or_receptor_binding else ligand
    rows = []
    for p in pathways:
        if not direct.get(p):
            continue
        genes = genes_in[p]
        lig = genes & counted
        rows.append(
            dict(
                term=p,
                name=go.name[p],
                n_genes=len(genes),
                n_ligand_genes=len(lig),
                ligand_genes=sorted(symbol[g] for g in lig)[:8],
                binding_only_genes=sorted(symbol[g] for g in (genes & binding) - ligand)[:6],
                genes=sorted(symbol[g] for g in genes)[:12],
                evidence=sorted({e for _, e in direct[p]}),
            )
        )
    rows.sort(key=lambda r: (r["n_ligand_genes"] > 0, -r["n_genes"]))
    return dict(
        n_ligand_activity_genes=len(ligand),
        ligand_genes_not_in_any_signaling=sorted(symbol[g] for g in ligand - in_signal),
        rows=rows,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=Path(".cache/ligands_in_signaling"))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--orgs", nargs="*", default=list(ORGANISMS))
    ap.add_argument("--or-receptor-binding", action="store_true")
    args = ap.parse_args()
    go = GO(args.data / "go-basic.obo")
    pathways = go.descendants_of_any({CELL_SURFACE, GPCR})
    args.out.mkdir(parents=True, exist_ok=True)
    suffix = "-or-binding" if args.or_receptor_binding else ""
    for org in args.orgs:
        res = check_organism(go, args.data / f"{ORGANISMS[org]}.gaf.gz", pathways, args.or_receptor_binding)
        res["go_version"] = go.data_version
        (args.out / f"gapcheck-{org}{suffix}.json").write_text(json.dumps(res, indent=1))
        fail = sum(1 for r in res["rows"] if r["n_ligand_genes"] == 0)
        print(
            f"{org:10} pathway terms={len(res['rows']):4} no ligand gene={fail:4} "
            f"ligand-activity genes={res['n_ligand_activity_genes']:4} "
            f"ligand genes in no signaling term={len(res['ligand_genes_not_in_any_signaling'])}"
        )


if __name__ == "__main__":
    main()
