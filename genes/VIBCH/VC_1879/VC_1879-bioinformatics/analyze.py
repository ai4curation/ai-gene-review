"""VC_1879 (Q9KQW8) ComEC/Rec2 sequence checks.

1. Identity of the dashboard sequence (NZ_CWQE01000001.1_287) to Q9KQW8.
2. Pairwise alignment of Q9KQW8 to B. subtilis ComEC (P39695) and
   H. influenzae Rec2 (P44408): global identity and identity within the
   C-terminal MBL-like domain region (Q9KQW8 506-689, SMART SM00849 in UniProt).
3. MBL metal-binding motifs in Q9KQW8 and the aligned residues of the
   references: motif II (H-x-[HD]-x-D-H; in ComEC the canonical HxHxDH has
   D at the second position, Silale et al. 2021, PMID:33772889).

Usage: python analyze.py <data_dir> <out_dir>
"""

import json
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices


def read_fasta(p):
    seq, name = [], None
    for line in Path(p).read_text().splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
        else:
            seq.append(line.strip())
    return name, "".join(seq)


def aligner(mode):
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = mode
    return a


def pair_stats(aln, q_range=None):
    """identity over aligned (non-gap) columns; optionally restricted to query range (1-based incl)."""
    ident = cols = 0
    qmap = {}
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        for i in range(qe - qs):
            qi, ti = qs + i, ts + i
            qmap[qi + 1] = ti + 1
            if q_range and not (q_range[0] <= qi + 1 <= q_range[1]):
                continue
            cols += 1
            if aln.target[qi] == aln.query[ti]:
                ident += 1
    return ident, cols, qmap


def main(data_dir, out_dir):
    data_dir, out_dir = Path(data_dir), Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _, vc = read_fasta(data_dir / "Q9KQW8_VC_1879.fasta")
    _, dash = read_fasta(data_dir / "query_NZ_CWQE01000001.1_287.fasta")
    refs = {
        "P39695_BACSU_comEC": read_fasta(data_dir / "P39695_BACSU_comEC.fasta")[1],
        "P44408_HAEIN_rec2": read_fasta(data_dir / "P44408_HAEIN_rec2.fasta")[1],
    }
    res = {"Q9KQW8_length": len(vc), "dashboard_length": len(dash),
           "dashboard_X_count": dash.count("X")}

    # 1. dashboard vs Q9KQW8 (target = Q9KQW8)
    aln = aligner("global").align(vc, dash)[0]
    i, c, _ = pair_stats(aln)
    mism = sum(1 for (qs, qe), (ts, te) in zip(*aln.aligned)
               for k in range(qe - qs)
               if vc[qs + k] != dash[ts + k] and dash[ts + k] != "X")
    res["dashboard_vs_Q9KQW8"] = {
        "aligned_columns": c, "identical": i,
        "identity_pct_over_aligned": round(100 * i / c, 2),
        "mismatches_excluding_X": mism,
    }

    # 3. motifs in Q9KQW8
    motifs = []
    for m in re.finditer(r"H.[HD].[DH]H", vc):
        motifs.append({"motif": "II-like H-x-[HD]-x-[DH]-H", "start": m.start() + 1,
                       "seq": m.group(), "context": vc[m.start() - 6:m.end() + 6]})
    res["Q9KQW8_motifII_matches"] = motifs
    res["Q9KQW8_HH_pairs_in_CTD"] = [
        {"pos": m.start() + 1, "context": vc[m.start() - 4:m.end() + 4]}
        for m in re.finditer(r"HH", vc) if m.start() + 1 >= 500]

    # 2. references
    mbl = (506, 689)
    for name, rs in refs.items():
        g = aligner("global").align(vc, rs)[0]
        gi, gc, qmap = pair_stats(g)
        di, dc, _ = pair_stats(g, mbl)
        entry = {
            "ref_length": len(rs),
            "global_identity_pct_over_aligned": round(100 * gi / gc, 1),
            "aligned_columns": gc,
            "MBL_region_506_689_identity_pct": round(100 * di / dc, 1) if dc else None,
            "MBL_region_aligned_columns": dc,
        }
        # aligned residues for motif II positions in Q9KQW8
        for m in motifs:
            s = m["start"]
            entry[f"aligned_to_Q9KQW8_{s}-{s + 5}"] = "".join(
                rs[qmap[p] - 1] if p in qmap else "-" for p in range(s, s + 6))
        res[name] = entry
        (out_dir / f"aln_Q9KQW8_vs_{name}.txt").write_text(str(g))
    (out_dir / "results.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
