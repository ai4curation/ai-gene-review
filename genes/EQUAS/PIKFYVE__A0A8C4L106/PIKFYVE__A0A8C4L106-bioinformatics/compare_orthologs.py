# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85", "httpx"]
# ///
"""Align donkey PIKFYVE canonical product (A0A8C4L106) to human (Q9Y2I7) and mouse (Q9Z1T6) PIKFYVE.

Usage: uv run --script compare_orthologs.py OUTDIR (adapted from genes/HORSE/PIKFYVE/PIKFYVE-bioinformatics/compare_orthologs.py; horse A0A3Q2HE51 also compared)
Downloads the three UniProt flat files into OUTDIR, runs global alignments
(BLOSUM62, open -10, extend -0.5) and reports identity among paired residues,
coverage, and the donkey residue aligned to selected reference positions:
the eight FYVE Zn-ligand cysteines of human (UniProt BINDING features), and
human Lys-1877 and Ser-2053 (UniProt MUTAGEN features from PMID:33098764;
K1877E abolishes lipid kinase activity and autophosphorylation).
Pairwise similarity alone does not establish orthology; the orthology claim
rests on PANTHER subfamily membership, reported separately.
"""
import json, sys
from pathlib import Path
import httpx
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

ACC = {"donkey": "A0A8C4L106", "horse": "A0A3Q2HE51", "human": "Q9Y2I7", "mouse": "Q9Z1T6"}


def fetch(acc, outdir):
    p = outdir / f"{acc}.txt"
    if not p.exists():
        r = httpx.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60)
        r.raise_for_status()
        p.write_text(r.text)
    return SeqIO.read(p, "swiss")


def align(ref, qry):
    al = Align.PairwiseAligner(mode="global")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    a = al.align(ref.seq, qry.seq)[0]
    x, y = str(a[0]), str(a[1])
    ri = qi = 0
    rmap, pairs, ident = {}, 0, 0
    for c1, c2 in zip(x, y):
        if c1 != "-":
            ri += 1
        if c2 != "-":
            qi += 1
        if c1 != "-" and c2 != "-":
            pairs += 1
            ident += c1 == c2
        if c1 != "-":
            rmap[ri] = (c1, c2, qi if c2 != "-" else None)
    return {
        "ref_len": len(ref.seq), "query_len": len(qry.seq), "paired": pairs,
        "identity_pct_of_paired": round(100 * ident / pairs, 2),
        "ref_coverage_pct": round(100 * pairs / len(ref.seq), 2),
        "query_coverage_pct": round(100 * pairs / len(qry.seq), 2),
    }, rmap


def main():
    outdir = Path(sys.argv[1])
    recs = {k: fetch(v, outdir) for k, v in ACC.items()}
    res = {}
    for ref, positions in (("human", [164, 167, 180, 183, 188, 191, 210, 213, 1877, 2053]),
                           ("mouse", []), ("horse", [])):
        stats, rmap = align(recs[ref], recs["donkey"])
        stats["positions"] = {str(p): {"ref_residue": rmap[p][0], "donkey_residue": rmap[p][1],
                                       "donkey_position": rmap[p][2]} for p in positions}
        res[f"{ref}_{ACC[ref]}_vs_donkey"] = stats
    (outdir / "results.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
