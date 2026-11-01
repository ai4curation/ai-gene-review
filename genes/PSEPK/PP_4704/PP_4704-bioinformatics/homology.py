"""PP_4704 (Q88DW4) vs the AsmA-like proteins of P. aeruginosa PAO1 (Sposato et al. 2024 Table 1),
E. coli K-12 and the other KT2440 AsmA-like proteins. Local Smith-Waterman (BLOSUM62, gap 11/1),
identity over aligned columns, plus a reciprocal-best check between KT2440 and PAO1 sets, and the
dashboard query vs Q88DW4. Sequences fetched from UniProt REST.
Usage: python3 -I homology.py DASHBOARD_FASTA OUTDIR"""
import json, os, sys, urllib.request
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

SETS = {
    "KT2440": {"PP_4704": "Q88DW4", "PP_4572": "Q88E94", "PP_2893_TamB": "Q88IV6", "PP_0938_YhdP": "Q88PB2",
               "PP_4857_YhjG": "Q88DG8", "PP_0287_AsmA": "Q88R47"},
    "PAO1": {"PA4735_EpaF": "Q9HV64", "PA2708": "Q9I0D4", "PA2542_TamB": None, "PA4476_YhdP": None,
             "PA4879_YhjG": None, "PA5146_AsmA": None, "PA5307_YdbH": None},
    "Ecoli": {"AsmA": "P28249", "YicH": "P31433", "YhjG": "P37645", "TamB": "P39321", "YhdP": "P46474", "YdbH": "P52645"},
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.5.0"})
    return urllib.request.urlopen(req, timeout=60).read().decode()


def acc_for_locus(locus):
    t = get(f"https://rest.uniprot.org/uniprotkb/search?query=gene:{locus}+AND+organism_id:208964&fields=accession&format=tsv")
    return t.split("\n")[1].strip()


def seq(acc):
    return "".join(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").split("\n")[1:])


al = Align.PairwiseAligner(mode="local", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                           open_gap_score=-11, extend_gap_score=-1)


def cmp(a, b):
    aln = al.align(a, b)[0]
    ident = cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += a[i] == b[j]
    (qs, qe), (ss, se) = (aln.aligned[0][0][0], aln.aligned[0][-1][1]), (aln.aligned[1][0][0], aln.aligned[1][-1][1])
    return {"score": aln.score, "aligned_pairs": cols, "identical": ident, "pct_id": round(100 * ident / cols, 1) if cols else 0,
            "query_range": [int(qs) + 1, int(qe)], "subject_range": [int(ss) + 1, int(se)],
            "query_cov_pct": round(100 * (qe - qs) / len(a), 1), "subject_cov_pct": round(100 * (se - ss) / len(b), 1)}


fasta, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
seqs, meta = {}, {}
for org, d in SETS.items():
    for name, acc in d.items():
        if acc is None:
            acc = acc_for_locus(name.split("_")[0])
        seqs[f"{org}:{name}"] = seq(acc)
        meta[f"{org}:{name}"] = {"accession": acc, "length": len(seqs[f"{org}:{name}"])}
dash = str(next(SeqIO.parse(fasta, "fasta")).seq)
res = {"proteins": meta, "dashboard_vs_Q88DW4": cmp(dash, seqs["KT2440:PP_4704"]), "dashboard_length": len(dash)}
res["PP_4704_vs_all"] = {k: cmp(seqs["KT2440:PP_4704"], v) for k, v in seqs.items() if k != "KT2440:PP_4704"}
# reciprocal best: for each KT2440 DUF748 protein the best PAO1 hit, and vice versa
kt = [k for k in seqs if k.startswith("KT2440")]
pa = [k for k in seqs if k.startswith("PAO1")]
ec = [k for k in seqs if k.startswith("Ecoli")]
res["best_PAO1_for_KT2440"], res["best_KT2440_for_PAO1"], res["best_Ecoli_for_KT2440_DUF748"] = {}, {}, {}
for k in kt:
    sc = {p: cmp(seqs[k], seqs[p])["score"] for p in pa}
    res["best_PAO1_for_KT2440"][k] = sorted(sc.items(), key=lambda x: -x[1])[:3]
for p in pa:
    sc = {k: cmp(seqs[p], seqs[k])["score"] for k in kt}
    res["best_KT2440_for_PAO1"][p] = sorted(sc.items(), key=lambda x: -x[1])[:3]
for k in ["KT2440:PP_4704", "KT2440:PP_4572"]:
    res["best_Ecoli_for_KT2440_DUF748"][k] = sorted(((e, cmp(seqs[k], seqs[e])) for e in ec), key=lambda x: -x[1]["score"])
res["PA4735_vs_PP_4572"] = cmp(seqs["PAO1:PA4735_EpaF"], seqs["KT2440:PP_4572"])
res["PA2708_vs_PP_4572"] = cmp(seqs["PAO1:PA2708"], seqs["KT2440:PP_4572"])
json.dump(res, open(os.path.join(out, "homology_results.json"), "w"), indent=1)
print(json.dumps(res, indent=1)[:12000])
