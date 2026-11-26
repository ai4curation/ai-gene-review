"""Sequence analysis for the PP_0765 (DUF1302) / PP_0766 (DUF1329) pair.

Usage: python analyze_pair.py <uniprot_seqs.fasta> <dashboard_A.json> <dashboard_B.json> <out.json>

Reports:
  * global identity of each dashboard sequence to its UniProt reference entry;
  * global identity to the P. aeruginosa orthologues (PA3923, PA3922), the KT2440
    paralogues (PP_2042, PP_2043) and, for PP_0766, E. coli LolA/LolB;
  * a shuffle z-score for the PP_0766 vs LolA/LolB alignments (are they above noise?);
  * lipobox search ([LVI][ASTVI][GAS]C) in residues 1-40 and Cys positions;
  * intergenic distance between PP_0765 and PP_0766 from the dashboard neighbourhood.
"""
import json
import random
import re
import sys

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def aligner():
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    a.end_gap_score = 0  # do not penalise terminal overhangs
    return a


def identity(a, s1, s2):
    aln = a.align(s1, s2)[0]
    ident = pairs = 0
    for (s1s, s1e), (s2s, s2e) in zip(*aln.aligned):
        for i, j in zip(range(s1s, s1e), range(s2s, s2e)):
            pairs += 1
            ident += s1[i] == s2[j]
    return {
        "score": aln.score,
        "aligned_pairs": pairs,
        "identical": ident,
        "percent_identity_over_aligned": round(100 * ident / pairs, 1) if pairs else 0,
        "percent_identity_over_query": round(100 * ident / len(s1), 1),
        "query_len": len(s1),
        "subject_len": len(s2),
    }


def shuffle_z(a, s1, s2, n=200, seed=1):
    rnd = random.Random(seed)
    real = a.score(s1, s2)
    scores = []
    for _ in range(n):
        lst = list(s2)
        rnd.shuffle(lst)
        scores.append(a.score(s1, "".join(lst)))
    m = sum(scores) / n
    sd = (sum((x - m) ** 2 for x in scores) / (n - 1)) ** 0.5
    return {"real_score": real, "shuffle_mean": round(m, 1), "shuffle_sd": round(sd, 1),
            "z": round((real - m) / sd, 1), "n_shuffles": n}


def features(seq):
    nterm = seq[:40]
    lipobox = [{"motif": m.group(), "cys_pos": m.end()} for m in re.finditer(r"[LVI][ASTVI][GAS]C", nterm)]
    return {
        "length": len(seq),
        "n_terminal_40": nterm,
        "lipobox_hits_1_40": lipobox,
        "cys_positions": [i + 1 for i, c in enumerate(seq) if c == "C"],
    }


def main():
    fasta, dash_a, dash_b, out = sys.argv[1:5]
    seqs = {}
    for r in SeqIO.parse(fasta, "fasta"):
        gn = re.search(r"GN=(\S+)", r.description)
        seqs[gn.group(1) if gn else r.id] = str(r.seq)
    da = json.load(open(dash_a))
    db = json.load(open(dash_b))
    seqs["dashboard_NZ_NBWA01000007.1_52"] = da["sequence"]
    seqs["dashboard_NZ_KZ987399.1_4512"] = db["sequence"]
    a = aligner()
    res = {"features": {}, "identity": {}, "shuffle": {}}
    for k in ["PP_0765", "PP_0766", "dashboard_NZ_NBWA01000007.1_52", "dashboard_NZ_KZ987399.1_4512",
              "PA3923", "PA3922", "PP_2042", "PP_2043", "lolA", "lolB"]:
        res["features"][k] = features(seqs[k])
    pairs = [
        ("dashboard_NZ_NBWA01000007.1_52", "PP_0765"),
        ("dashboard_NZ_KZ987399.1_4512", "PP_0766"),
        ("PP_0765", "PA3923"), ("PP_0765", "PP_2042"), ("PP_2042", "PA3923"),
        ("PP_0766", "PA3922"), ("PP_0766", "PP_2043"), ("PP_2043", "PA3922"),
        ("PP_0766", "lolB"), ("PP_0766", "lolA"),
    ]
    for q, s in pairs:
        res["identity"][f"{q}__vs__{s}"] = identity(a, seqs[q], seqs[s])
    for s in ["lolB", "lolA", "PA3922", "PP_2043"]:
        res["shuffle"][f"PP_0766__vs__{s}"] = shuffle_z(a, seqs["PP_0766"], seqs[s])
    # neighbourhood from the dashboard evidence of gene B (KT2440 block)
    nb = db["rows"][0]["gene_neighborhoods"]
    m = re.search(r"organism=Pseudomonas putida KT2440.*?\[BEGIN UPSTREAM\]\s*GENE start=(\d+) stop=(\d+) strand=(\S)", nb, re.S)
    m2 = re.search(r"organism=Pseudomonas putida KT2440.*?\[BEGIN DOWNSTREAM\]\s*GENE start=(\d+) stop=(\d+) strand=(\S)", da["rows"][0]["gene_neighborhoods"], re.S)
    res["neighbourhood"] = {
        "PP_0765_coords_from_geneB_upstream": [int(m.group(1)), int(m.group(2)), m.group(3)],
        "PP_0766_coords_from_geneA_downstream": [int(m2.group(1)), int(m2.group(2)), m2.group(3)],
        "intergenic_bp": int(m2.group(1)) - int(m.group(2)) - 1,
    }
    json.dump(res, open(out, "w"), indent=2)
    print(json.dumps({k: v for k, v in res.items() if k != "features"}, indent=1))
    for k, v in res["features"].items():
        print(k, v["lipobox_hits_1_40"], v["cys_positions"][:12], v["n_terminal_40"])


if __name__ == "__main__":
    main()
