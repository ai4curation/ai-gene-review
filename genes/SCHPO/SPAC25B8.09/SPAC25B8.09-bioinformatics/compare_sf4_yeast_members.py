# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Pairwise global-alignment comparison of the PTHR44942:SF4 members of fission
and budding yeast (Q9UTA9, Q9UTA8, P32643 TMT1, P38892 CRG1).

Fetches sequences from UniProt REST, aligns every pair with BLOSUM62 global
alignment (gap open -10, extend -0.5), and reports identity over aligned
columns and over the shorter sequence. Output is printed and written to
results_sf4_pairwise.json next to this script.
"""
import json
import pathlib
import itertools
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q9UTA9": "SPAC25B8.09 (S. pombe)",
    "Q9UTA8": "SPAC25B8.10 (S. pombe)",
    "P32643": "TMT1 (S. cerevisiae)",
    "P38892": "CRG1 (S. cerevisiae)",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    rows = []
    for a, b in itertools.combinations(ACCS, 2):
        aln = aligner.align(seqs[a], seqs[b])[0]
        s1, s2 = aln[0], aln[1]
        ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
        cols = sum(1 for x, y in zip(s1, s2) if x != "-" and y != "-")
        short = min(len(seqs[a]), len(seqs[b]))
        rows.append({
            "a": a, "b": b, "score": aln.score,
            "identical": ident, "aligned_columns": cols,
            "pct_id_aligned": round(100 * ident / cols, 1),
            "pct_id_shorter": round(100 * ident / short, 1),
        })
    out = {"lengths": {a: len(s) for a, s in seqs.items()}, "labels": ACCS, "pairs": rows}
    for r in rows:
        print(f"{r['a']} {ACCS[r['a']]:25s} vs {r['b']} {ACCS[r['b']]:25s} "
              f"score={r['score']:.1f} id_aligned={r['pct_id_aligned']}% id_shorter={r['pct_id_shorter']}%")
    print(out["lengths"])
    pathlib.Path(__file__).with_name("results_sf4_pairwise.json").write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
