#!/usr/bin/env python3
"""Orthology / phylogeny validation for poplar (POPTR) vs Arabidopsis (ARATH) CASP-like proteins.

Goal: test the assumption used in the gene reviews that a poplar CASPL with a given
Roppolo subfamily code (e.g. PtCASPL1B1) is genuinely most similar to the Arabidopsis
protein carrying the same code (AtCASPL1B1), and therefore that functional information
characterized in Arabidopsis can be cautiously transferred by orthology.

Method (reproducible, no external aligners required):
  * read sequences from data/caspl.fasta (fetched from UniProt; see RESULTS.md)
  * all-vs-all global pairwise alignment with Biopython PairwiseAligner (BLOSUM62)
  * percent identity = identical columns / aligned length (excluding gap-gap)
  * distance = 1 - fractional identity
  * cross-species reciprocal best hit (RBH): for each POPTR protein, its top ARATH hit,
    and vice versa; an RBH pair is a putative ortholog pair
  * report whether each RBH pair shares the same subfamily *group* (the leading digit of
    the code, e.g. 1B1 -> group 1) and the same full subfamily code
  * neighbour-joining tree (Biopython) written to results/caspl_nj_tree.nwk

Nothing is hardcoded; if sequences are missing the script reports it rather than inventing
results.
"""
from __future__ import annotations

import csv
import json
import re
from itertools import combinations
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor
from Bio import Phylo

HERE = Path(__file__).parent
DATA = HERE / "data"
RESULTS = HERE / "results"
RESULTS.mkdir(exist_ok=True)


def load_sequences() -> dict[str, str]:
    fasta = DATA / "caspl.fasta"
    if not fasta.exists():
        raise SystemExit(f"Missing {fasta}; run the fetch step in RESULTS.md first.")
    seqs = {rec.id: str(rec.seq) for rec in SeqIO.parse(fasta, "fasta")}
    if not seqs:
        raise SystemExit("No sequences parsed.")
    return seqs


def make_aligner() -> PairwiseAligner:
    aln = PairwiseAligner()
    aln.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aln.open_gap_score = -11
    aln.extend_gap_score = -1
    aln.mode = "global"
    return aln


def pct_identity(aligner: PairwiseAligner, a: str, b: str) -> float:
    """Percent identity over aligned (non gap-gap) columns of the top alignment."""
    aln = aligner.align(a, b)[0]
    # aln.aligned gives matched blocks; iterate the aligned strings instead for identity
    sa, sb = aln[0], aln[1]
    ident = 0
    cols = 0
    for ca, cb in zip(sa, sb):
        if ca == "-" and cb == "-":
            continue
        cols += 1
        if ca == cb and ca != "-":
            ident += 1
    return ident / cols if cols else 0.0


def parse_label(label: str) -> tuple[str, str, str]:
    """'POPTR_CASPL1B1_B9I0U9' -> (species, code, accession)."""
    org, rest = label.split("_", 1)
    code, acc = rest.rsplit("_", 1)
    code = code.replace("CASPL", "")
    return org, code, acc


def group_of(code: str) -> str:
    m = re.match(r"(\d+)", code)
    return m.group(1) if m else "?"


def main() -> None:
    seqs = load_sequences()
    labels = list(seqs)
    aligner = make_aligner()

    n = len(labels)
    idx = {l: i for i, l in enumerate(labels)}
    dist = [[0.0] * n for _ in range(n)]
    ident = {}

    for a, b in combinations(labels, 2):
        pid = pct_identity(aligner, seqs[a], seqs[b])
        ident[(a, b)] = pid
        ident[(b, a)] = pid
        d = 1.0 - pid
        dist[idx[a]][idx[b]] = d
        dist[idx[b]][idx[a]] = d

    poptr = [l for l in labels if l.startswith("POPTR_")]
    arath = [l for l in labels if l.startswith("ARATH_")]

    def best_hit(query: str, pool: list[str]) -> tuple[str, float]:
        best, bid = None, -1.0
        for t in pool:
            if t == query:
                continue
            pid = ident[(query, t)]
            if pid > bid:
                best, bid = t, pid
        return best, bid

    # Reciprocal best hits between POPTR and ARATH
    rbh_rows = []
    for p in poptr:
        a_hit, a_id = best_hit(p, arath)
        p_back, _ = best_hit(a_hit, poptr)
        is_rbh = (p_back == p)
        _, p_code, p_acc = parse_label(p)
        _, a_code, a_acc = parse_label(a_hit)
        rbh_rows.append({
            "poptr": p, "poptr_code": p_code, "poptr_acc": p_acc,
            "best_arath": a_hit, "arath_code": a_code, "arath_acc": a_acc,
            "pct_identity": round(a_id * 100, 1),
            "reciprocal": is_rbh,
            "same_group": group_of(p_code) == group_of(a_code),
            "same_code": p_code == a_code,
        })

    # Write RBH table
    with open(RESULTS / "rbh_orthology.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rbh_rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rbh_rows)

    # NJ tree
    names = labels
    lower = [[dist[i][j] for j in range(i + 1)] for i in range(n)]
    dm = DistanceMatrix(names=names, matrix=lower)
    tree = DistanceTreeConstructor().nj(dm)
    Phylo.write(tree, RESULTS / "caspl_nj_tree.nwk", "newick")

    # Summary
    n_rbh = sum(r["reciprocal"] for r in rbh_rows)
    n_same_group = sum(r["reciprocal"] and r["same_group"] for r in rbh_rows)
    n_same_code = sum(r["reciprocal"] and r["same_code"] for r in rbh_rows)
    summary = {
        "n_sequences": n,
        "n_poptr": len(poptr),
        "n_arath": len(arath),
        "n_poptr_with_rbh": n_rbh,
        "n_rbh_same_group": n_same_group,
        "n_rbh_same_code": n_same_code,
        "characterized_focus": {},
    }
    focus = {"1B1", "1B2", "1D1", "4C1", "4C2"}
    for r in rbh_rows:
        if r["poptr_code"] in focus:
            summary["characterized_focus"][r["poptr_code"]] = {
                "best_arath_code": r["arath_code"],
                "pct_identity": r["pct_identity"],
                "reciprocal": r["reciprocal"],
                "same_group": r["same_group"],
                "same_code": r["same_code"],
            }
    with open(RESULTS / "summary.json", "w") as fh:
        json.dump(summary, fh, indent=2)

    print(json.dumps(summary, indent=2))
    print("\nReciprocal-best-hit orthology (POPTR -> ARATH):")
    print(f"{'POPTR':<10} {'->ARATH':<10} {'%id':>6} {'RBH':>5} {'grp':>4} {'code':>5}")
    for r in sorted(rbh_rows, key=lambda x: (group_of(x['poptr_code']), x['poptr_code'])):
        print(f"{r['poptr_code']:<10} {r['arath_code']:<10} {r['pct_identity']:>6} "
              f"{str(r['reciprocal']):>5} {str(r['same_group']):>4} {str(r['same_code']):>5}")


if __name__ == "__main__":
    main()
