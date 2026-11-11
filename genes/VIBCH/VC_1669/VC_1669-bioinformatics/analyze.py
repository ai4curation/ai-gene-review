"""Paralog comparison of the two V. cholerae N16961 NSS (SLC6/SNF, PF00209) proteins.

VC_2283 (Q9KPS9, named AatX in PMID:36130487) and VC_1669 (Q9KRH3).

1. Global pairwise identity (BLOSUM62, gap open -10, extend -0.5) between the two
   paralogs, the two dashboard sequences, and characterized/annotated bacterial NSS
   proteins (LeuT, MhsT, TnaT, SO_4339 'hypotaurine transporter', B. subtilis YocR).
2. TrpR operator scan: best Hamming match (both strands) to the E. coli trpEDCBA
   operator 20-mer in the 300 bp upstream of each CDS start, compared with the
   distribution over every CDS on both chromosomes (empirical percentile).
3. Neighbouring genes (+/- 3 CDS) of each paralog.
"""

import argparse
import json
import re
import urllib.request
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

REFS = {
    "Q9KPS9": "VC_2283 (AatX) V. cholerae N16961",
    "Q9KRH3": "VC_1669 V. cholerae N16961",
    "O67854": "LeuT (snf, aq_2077) Aquifex aeolicus; Leu/Ala transporter, structure",
    "Q9KDT3": "MhsT (BH1128) Bacillus halodurans; hydrophobic amino acid (incl. Trp) transporter, structure",
    "Q67SB6": "TnaT (STH442) Symbiobacterium thermophilum; Na+-coupled Trp transporter",
    "Q8E9E5": "SO_4339 Shewanella oneidensis; 'hypotaurine transporter' from fitness",
    "O34383": "YocR (BSU19340) Bacillus subtilis; uncharacterized",
}
TRPO = "CGAACTAGTTAACTAGTACG"  # E. coli trpEDCBA operator 20-mer


def fetch_uniprot(acc, cache):
    p = cache / f"{acc}.fasta"
    if not p.exists():
        with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
            p.write_bytes(r.read())
    return str(next(SeqIO.parse(p, "fasta")).seq)


def identity(a, b, aligner):
    aln = aligner.align(a, b)[0]
    pairs = ident = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            pairs += 1
            ident += a[i] == b[j]
    return {"identity_pct": round(100 * ident / pairs, 1), "aligned_pairs": pairs,
            "identity_over_shorter_pct": round(100 * ident / min(len(a), len(b)), 1)}


def parse_ft(path):
    """Return list of CDS dicts (start, end, strand, old_locus_tag, gene, product)."""
    cds, cur, kind = [], None, None
    for line in open(path):
        m = re.match(r"^<?(\d+)\t>?(\d+)\t(\w+)", line)
        if m:
            kind = m.group(3)
            a, b = int(m.group(1)), int(m.group(2))
            if kind == "gene":
                cur = {"start": a, "end": b, "strand": "+" if b > a else "-", "tags": [], "gene": None}
            elif kind == "CDS" and cur is not None:
                cur["cds"] = True
                cds.append(cur)
            continue
        f = line.strip().split("\t")
        if cur is None or len(f) < 2:
            continue
        if kind == "gene" and f[0] == "old_locus_tag":
            cur["tags"].append(f[1])
        elif kind == "gene" and f[0] == "gene":
            cur["gene"] = f[1]
        elif kind == "CDS" and f[0] == "product":
            cur["product"] = f[1]
    return cds


def revcomp(s):
    return s[::-1].translate(str.maketrans("ACGTN", "TGCAN"))


def upstream(genome, g, n=300):
    if g["strand"] == "+":
        s = g["start"] - 1
        return genome[max(0, s - n):s]
    e = g["start"]  # 1-based start on minus strand is the larger coordinate
    return revcomp(genome[e:e + n])


def best_match(seq, motif):
    best = (len(motif) + 1, None)
    L = len(motif)
    rc = revcomp(motif)
    for i in range(len(seq) - L + 1):
        w = seq[i:i + L]
        for m in (motif, rc):
            d = sum(x != y for x, y in zip(w, m))
            if d < best[0]:
                best = (d, w)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--output", default="results.json")
    a = ap.parse_args()
    data = Path(a.data)
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aligner.mode = "global"

    seqs = {acc: fetch_uniprot(acc, data) for acc in REFS}
    for f in sorted(data.glob("dashboard_*.fasta")):
        seqs[f.stem] = str(next(SeqIO.parse(f, "fasta")).seq)
    res = {"lengths": {k: len(v) for k, v in seqs.items()}, "labels": REFS, "pairwise": {}}
    keys = list(seqs)
    for i, k1 in enumerate(keys):
        for k2 in keys[i + 1:]:
            res["pairwise"][f"{k1}|{k2}"] = identity(seqs[k1], seqs[k2], aligner)

    genome = {}
    cds = []
    for chrom in ("NC_002505.1", "NC_002506.1"):
        fa = data / f"{chrom}.fasta"
        if fa.exists():
            genome[chrom] = str(next(SeqIO.parse(fa, "fasta")).seq).upper()
            for g in parse_ft(data / f"{chrom}.ft"):
                g["chrom"] = chrom
                cds.append(g)
    scores = []
    for g in cds:
        d, w = best_match(upstream(genome[g["chrom"]], g), TRPO)
        g["trpo_mismatch"], g["trpo_site"] = d, w
        scores.append(d)
    n = len(scores)

    def tag(g):
        return next((t for t in g["tags"] if "_" not in t), g["tags"][0] if g["tags"] else None)

    focus = {}
    want = {"VC2283", "VC1669", "VC2282", "VC1670"}
    for g in cds:
        t = tag(g)
        if t in want or g.get("gene") in {"trpR", "tyrR"} or "tryptophan operon leader" in g.get("product", "") \
                or (t and t.startswith("VCA") and t in {"VCA0160", "VCA0772"}):
            d = g["trpo_mismatch"]
            focus[t or g.get("product")] = {
                "gene": g.get("gene"), "product": g.get("product"), "strand": g["strand"],
                "start": g["start"], "trpO_best_mismatches": d, "site": g["trpo_site"],
                "fraction_of_all_CDS_with_<=_mismatches": round(sum(s <= d for s in scores) / n, 4)}
    res["trpO_scan"] = {"motif": TRPO, "upstream_bp": 300, "n_cds": n,
                        "mismatch_histogram": {k: scores.count(k) for k in sorted(set(scores))},
                        "genes": focus,
                        "top_hits_<=6_mismatches": [
                            {"tag": tag(g), "gene": g.get("gene"), "product": g.get("product"),
                             "mismatches": g["trpo_mismatch"], "site": g["trpo_site"]}
                            for g in sorted(cds, key=lambda g: g["trpo_mismatch"]) if g["trpo_mismatch"] <= 6]}

    nb = {}
    chrI = [g for g in cds if g["chrom"] == "NC_002505.1"]
    chrI.sort(key=lambda g: min(g["start"], g["end"]))
    for target in ("VC2283", "VC1669"):
        idx = next(i for i, g in enumerate(chrI) if tag(g) == target)
        nb[target] = [{"tag": tag(g), "gene": g.get("gene"), "strand": g["strand"], "product": g.get("product")}
                      for g in chrI[max(0, idx - 3): idx + 4]]
    res["neighbourhood"] = nb
    Path(a.output).write_text(json.dumps(res, indent=2))
    print(json.dumps({k: v for k, v in res["pairwise"].items()}, indent=1))
    print(json.dumps(res["trpO_scan"], indent=1))
    print(json.dumps(nb, indent=1))


if __name__ == "__main__":
    main()
