"""Domain, homology, topology and genomic-context analysis of dashboard gene NZ_CP015876.1_2730.

1. Pfam PF02308 (MgtC N-terminal) and PF13194 (DUF4010) hmmsearch on the dashboard query
   and on reference proteins (pyhmmer).
2. Global/local identity of the query to A0ABY3D9I3 (review accession), Salmonella MgtC
   (D0ZLQ7), E. coli YhiD (P0AFV2), M. tuberculosis MgtC (I6YBN6) and Aquifex aq_1828 (O67688).
3. phmmer of the query against the P. aeruginosa PAO1 reference proteome (UP000002438) to
   identify the PAO1 homolog cited by the dashboard (34.3% identity, colistin phenotype).
4. Genomic context in P. putida SJTE-1 (NZ_CP015876.1): locate the CDS whose translation
   matches the query, list +/-10 neighbours, compare gene GC with chromosome GC, and look
   for mobile-element markers (integrase, transposase, phage, tRNA) within 25 kb.
"""
import argparse
import json
import re

import pyhmmer
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.SeqUtils import gc_fraction


def aligner(mode):
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = mode
    return a


def ident(q, s, mode):
    aln = aligner(mode).align(q, s)[0]
    i = n = 0
    qs_min = qe_max = ss_min = se_max = None
    for (qs, qe), (ss, se) in zip(*aln.aligned):
        qs, qe, ss, se = int(qs), int(qe), int(ss), int(se)
        qs_min = qs if qs_min is None else qs_min
        ss_min = ss if ss_min is None else ss_min
        qe_max, se_max = qe, se
        for a, b in zip(range(qs, qe), range(ss, se)):
            n += 1
            i += q[a] == s[b]
    return {"identical": i, "aligned": n, "pct_identity_aligned": round(100 * i / n, 1),
            "pct_identity_query": round(100 * i / len(q), 1),
            "query_range": [qs_min + 1, qe_max], "subject_range": [ss_min + 1, se_max],
            "subject_len": len(s)}


def hmm_hits(hmm_paths, seqs):
    alpha = pyhmmer.easel.Alphabet.amino()
    dig = [pyhmmer.easel.TextSequence(name=k.encode(), sequence=v).digitize(alpha) for k, v in seqs.items()]
    out = []
    for p in hmm_paths:
        with pyhmmer.plan7.HMMFile(p) as hf:
            hmm = hf.read()
        for top in pyhmmer.hmmsearch([hmm], dig, E=10):
            for h in top:
                for d in h.domains:
                    if d.i_evalue > 1e-3:
                        continue
                    out.append({"hmm": hmm.accession.decode() if isinstance(hmm.accession, bytes) else hmm.accession,
                                "seq": h.name.decode() if isinstance(h.name, bytes) else h.name,
                                "env_from": d.env_from, "env_to": d.env_to,
                                "hmm_from": d.alignment.hmm_from, "hmm_to": d.alignment.hmm_to,
                                "hmm_len": hmm.M, "i_evalue": float(f"{d.i_evalue:.2g}"),
                                "score": round(d.score, 1)})
    return out


def phmmer_top(q, proteome, n=5):
    alpha = pyhmmer.easel.Alphabet.amino()
    qd = pyhmmer.easel.TextSequence(name=b"query", sequence=q).digitize(alpha)
    db = [pyhmmer.easel.TextSequence(name=r.id.encode(), description=r.description.encode(),
                                     sequence=str(r.seq)).digitize(alpha) for r in SeqIO.parse(proteome, "fasta")]
    seqmap = {r.id: str(r.seq) for r in SeqIO.parse(proteome, "fasta")}
    res = []
    for top in pyhmmer.phmmer([qd], db, E=1e-5):
        for h in list(top)[:n]:
            nm = h.name.decode() if isinstance(h.name, bytes) else h.name
            desc = h.description.decode() if isinstance(h.description, bytes) else h.description
            r = {"id": nm, "description": desc, "evalue": float(f"{h.evalue:.2g}"), "score": round(h.score, 1)}
            r.update({"local_alignment": ident(q, seqmap[nm], "local")})
            res.append(r)
    return res


MOBILE = re.compile(r"integrase|transposase|phage|IS\d|recombinase|insertion|conjug|mobile|relaxase|tRNA", re.I)


def context(gbk, q, flank=10, window=25000):
    rec = SeqIO.read(gbk, "genbank")
    genome_gc = gc_fraction(rec.seq)
    feats = [f for f in rec.features if f.type in ("CDS", "tRNA", "tmRNA", "rRNA")]
    cds = [f for f in rec.features if f.type == "CDS"]
    hit = None
    for idx, f in enumerate(cds):
        tr = f.qualifiers.get("translation", [""])[0]
        if tr and (tr == q or tr.rstrip("*") == q):
            hit = idx
            break
    if hit is None:
        # best approximate match by local identity among CDS of similar length
        best = None
        for idx, f in enumerate(cds):
            tr = f.qualifiers.get("translation", [""])[0]
            if tr and abs(len(tr) - len(q)) < 30 and tr[:15] == q[:15]:
                best = idx
        hit = best
    f0 = cds[hit]
    gene_seq = f0.extract(rec.seq)
    tr0 = f0.qualifiers.get("translation", [""])[0]
    out = {"genome": rec.id, "description": rec.description, "genome_len": len(rec.seq),
           "genome_gc": round(genome_gc, 4), "cds_index_1based": hit + 1,
           "locus_tag": f0.qualifiers.get("locus_tag", [""])[0],
           "old_locus_tag": f0.qualifiers.get("old_locus_tag", [""])[0],
           "protein_id": f0.qualifiers.get("protein_id", [""])[0],
           "product": f0.qualifiers.get("product", [""])[0],
           "location": [int(f0.location.start) + 1, int(f0.location.end), int(f0.location.strand)],
           "translation_identical_to_query": tr0 == q,
           "gene_gc": round(gc_fraction(gene_seq), 4)}
    neigh = []
    for f in cds[max(0, hit - flank): hit + flank + 1]:
        s = f.extract(rec.seq)
        neigh.append({"locus_tag": f.qualifiers.get("locus_tag", [""])[0],
                      "start": int(f.location.start) + 1, "end": int(f.location.end),
                      "strand": int(f.location.strand),
                      "product": f.qualifiers.get("product", ["?"])[0],
                      "gc": round(gc_fraction(s), 4),
                      "len_aa": len(f.qualifiers.get("translation", [""])[0])})
    out["neighbours"] = neigh
    lo, hi = int(f0.location.start) - window, int(f0.location.end) + window
    region = rec.seq[max(0, lo):hi]
    out["window_bp"] = window
    out["window_gc"] = round(gc_fraction(region), 4)
    mob = []
    for f in feats:
        if f.location.end < lo or f.location.start > hi:
            continue
        txt = " ".join(f.qualifiers.get("product", []) + f.qualifiers.get("note", []))
        if f.type != "CDS" or MOBILE.search(txt):
            mob.append({"type": f.type, "locus_tag": f.qualifiers.get("locus_tag", [""])[0],
                        "start": int(f.location.start) + 1, "product": f.qualifiers.get("product", [""])[0]})
    out["mobile_or_rna_features_in_window"] = mob
    # genome-wide GC distribution of CDS for a z-score
    gcs = [gc_fraction(f.extract(rec.seq)) for f in cds]
    m = sum(gcs) / len(gcs)
    sd = (sum((g - m) ** 2 for g in gcs) / len(gcs)) ** 0.5
    out["cds_gc_mean"] = round(m, 4)
    out["cds_gc_sd"] = round(sd, 4)
    out["gene_gc_z"] = round((gc_fraction(gene_seq) - m) / sd, 2)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", required=True)
    ap.add_argument("--refs", required=True)
    ap.add_argument("--hmms", nargs="+", required=True)
    ap.add_argument("--pao1", required=True)
    ap.add_argument("--gbk", required=True)
    ap.add_argument("--dashboard", required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    q = str(next(SeqIO.parse(a.query, "fasta")).seq).rstrip("*")
    refs = {r.id.split("|")[2] if "|" in r.id else r.id: str(r.seq) for r in SeqIO.parse(a.refs, "fasta")}
    res = {"query_len": len(q)}
    res["identity"] = {k: {"global": ident(q, v, "global"), "local": ident(q, v, "local")} for k, v in refs.items()}
    allseqs = {"query": q, **refs}
    res["pfam_hits"] = hmm_hits(a.hmms, allseqs)
    res["pao1_phmmer_top"] = phmmer_top(q, a.pao1)
    d = json.load(open(a.dashboard))
    tm = re.search(r"positions: ([0-9, -]+)", d["rows"][0]["topology_evidence"]).group(1)
    segs = [tuple(map(int, x.split("-"))) for x in tm.split(", ")]
    res["deeptmhmm_segments"] = segs
    doms = [h for h in res["pfam_hits"] if h["seq"] == "query"]
    res["tm_per_domain"] = {h["hmm"]: sum(1 for s, e in segs if s >= h["env_from"] - 5 and e <= h["env_to"] + 5) for h in doms}
    res["context_SJTE1"] = context(a.gbk, q)
    json.dump(res, open(a.output, "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "context_SJTE1"}, indent=1)[:6000])
    c = res["context_SJTE1"]
    print(json.dumps({k: v for k, v in c.items() if k != "neighbours"}, indent=1))
    for n in c["neighbours"]:
        print(n)


if __name__ == "__main__":
    main()
