"""PP_2042 / PP_2043 (DUF1302 / DUF1329 pair) analysis.

1. Pairwise local identities (BLOSUM62, Smith-Waterman) between the dashboard query
   sequences, the KT2440 reference entries, the KT2440 paralog pair PP_0765/PP_0766 and
   the P. aeruginosa PAO1 pairs PA3923/PA3922 and PA3422/PA3421, to decide which KT2440
   pair is orthologous to the laminin-binding PA3923.
2. N-terminal signal peptide / lipobox motif scan.
3. Fitness Browser (BERDL kescience.fitnessbrowser) fitness, specific phenotypes and
   cofitness for PP_2042, PP_2043, PP_0765, PP_0766.

Run with a Python that has berdl_notebook_utils (on-cluster), e.g.
  /opt/conda/bin/python -I analyze_pair.py <outdir>
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE
OUT.mkdir(parents=True, exist_ok=True)
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)

DASH = Path("/home/cmungall/.beril/projects/hackathon/user_data/dashboard_calls")

ACC = {
    "PP_2042": "Q88L93", "PP_2043": "Q88L92",
    "PP_0765": "Q88PT3", "PP_0766": "Q88PT2",
    "PA3923": "Q9HX90", "PA3922": "Q9HX91",
    "PA3422": "Q9HYI3", "PA3421": "Q9HYI4",
}
DUF1302 = ["query_NC_017530.1_3648", "PP_2042", "PP_0765", "PA3923", "PA3422"]
DUF1329 = ["query_NZ_PJCG01000017.1_25", "PP_2043", "PP_0766", "PA3922", "PA3421"]


def fetch(acc):
    f = DATA / f"{acc}.fasta"
    if not f.exists():
        url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
        f.write_bytes(urllib.request.urlopen(url, timeout=60).read())
    return str(next(SeqIO.parse(f, "fasta")).seq)


def fetch_features(acc):
    f = DATA / f"{acc}.json"
    if not f.exists():
        url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        f.write_bytes(urllib.request.urlopen(url, timeout=60).read())
    d = json.loads(f.read_text())
    sig = [
        (x["location"]["start"]["value"], x["location"]["end"]["value"])
        for x in d.get("features", []) if x["type"] == "Signal"
    ]
    return sig


seqs = {k: fetch(v) for k, v in ACC.items()}
for did in ["NC_017530.1_3648", "NZ_PJCG01000017.1_25"]:
    seqs["query_" + did] = str(next(SeqIO.parse(DASH / f"{did}.fasta", "fasta")).seq)

aligner = PairwiseAligner()
aligner.mode = "local"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1


def ident(a, b):
    aln = aligner.align(seqs[a], seqs[b])[0]
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2)]
    pairs = [(x, y) for x, y in cols if x != "-" and y != "-"]
    same = sum(1 for x, y in pairs if x == y)
    qs, qe = aln.aligned[0][0][0], aln.aligned[0][-1][1]
    ss, se = aln.aligned[1][0][0], aln.aligned[1][-1][1]
    return {
        "a": a, "b": b, "len_a": len(seqs[a]), "len_b": len(seqs[b]),
        "aligned_pairs": len(pairs), "identical": same,
        "pct_identity": round(100 * same / len(pairs), 1),
        "a_range": [int(qs) + 1, int(qe)], "b_range": [int(ss) + 1, int(se)],
        "score": aln.score,
    }


results = {"sequences": {k: len(v) for k, v in seqs.items()}, "identity": {}}
for fam, members in [("DUF1302", DUF1302), ("DUF1329", DUF1329)]:
    rows = []
    for i, a in enumerate(members):
        for b in members[i + 1:]:
            rows.append(ident(a, b))
    results["identity"][fam] = rows

# Orthology call: which KT2440 member is the best hit of each PAO1 member, and vice versa
orth = {}
for fam, kt, pa in [("DUF1302", ["PP_2042", "PP_0765"], ["PA3923", "PA3422"]),
                    ("DUF1329", ["PP_2043", "PP_0766"], ["PA3922", "PA3421"])]:
    tab = {f"{k}|{p}": next(r for r in results["identity"][fam]
                            if {r["a"], r["b"]} == {k, p})["pct_identity"]
           for k in kt for p in pa}
    best_pa = {k: max(pa, key=lambda p: tab[f"{k}|{p}"]) for k in kt}
    best_kt = {p: max(kt, key=lambda k: tab[f"{k}|{p}"]) for p in pa}
    rbh = [f"{k}<->{best_pa[k]}" for k in kt if best_kt[best_pa[k]] == k]
    orth[fam] = {"pct_identity": tab, "best_PAO1_hit": best_pa,
                 "best_KT2440_hit": best_kt, "reciprocal_best": rbh}
results["orthology"] = orth

# N-terminal motifs
LIPOBOX = re.compile(r"[LVI][ASTVI][GAS]C")
nterm = {}
for k, v in seqs.items():
    head = v[:40]
    m = [(x.start() + 1, x.group()) for x in LIPOBOX.finditer(head)]
    nterm[k] = {
        "first40": head,
        "lipobox_matches_1_40": m,
        "uniprot_signal": fetch_features(ACC[k]) if k in ACC else None,
        "n_cys_total": v.count("C"),
    }
results["nterm"] = nterm

# Fitness Browser via BERDL
try:
    from berdl_notebook_utils.setup_spark_session import get_spark_session
    spark = get_spark_session()
    genes = "('PP_2042','PP_2043','PP_0765','PP_0766')"
    q_gene = (f"SELECT locusId, sysName, scaffoldId, begin, end, strand, desc FROM "
              f"kescience.fitnessbrowser.gene WHERE orgId='Putida' AND locusId IN {genes} "
              f"ORDER BY locusId")
    gdf = spark.sql(q_gene).toPandas()
    results["fb_genes"] = gdf.to_dict(orient="records")
    q_fit = (f"SELECT f.locusId, f.expName, CAST(f.fit AS DOUBLE) AS fit, "
             f"CAST(f.t AS DOUBLE) AS t, e.expDesc, e.expGroup FROM "
             f"kescience.fitnessbrowser.genefitness f JOIN kescience.fitnessbrowser.experiment e "
             f"ON f.orgId=e.orgId AND f.expName=e.expName WHERE f.orgId='Putida' "
             f"AND f.locusId IN {genes} ORDER BY f.locusId, f.expName")
    fdf = spark.sql(q_fit).toPandas()
    fdf.to_csv(OUT / "fitness_putida_pairs.tsv", sep="\t", index=False)
    summ = {}
    for loc, g in fdf.groupby("locusId"):
        strong = g[(g.fit.abs() >= 1) & (g.t.abs() >= 4)].sort_values("fit")
        summ[loc] = {
            "n_experiments": int(len(g)),
            "min_fit": float(g.fit.min()), "max_fit": float(g.fit.max()),
            "n_strong_abs_fit_ge1_abs_t_ge4": int(len(strong)),
            "n_fit_le_minus2": int((g.fit <= -2).sum()),
            "strong": strong[["expName", "expDesc", "fit", "t"]].head(25).to_dict(orient="records"),
            "lowest10": g.sort_values("fit")[["expName", "expDesc", "fit", "t"]].head(10).to_dict(orient="records"),
        }
    results["fitness"] = summ
    q_sp = (f"SELECT s.locusId, s.expName, e.expDesc FROM kescience.fitnessbrowser.specificphenotype s "
            f"JOIN kescience.fitnessbrowser.experiment e ON s.orgId=e.orgId AND s.expName=e.expName "
            f"WHERE s.orgId='Putida' AND s.locusId IN {genes} ORDER BY s.locusId, s.expName")
    results["specific_phenotypes"] = spark.sql(q_sp).toPandas().to_dict(orient="records")
    q_cof = (f"SELECT c.locusId, CAST(c.rank AS INT) AS rank, c.hitId, CAST(c.cofit AS DOUBLE) AS cofit, "
             f"g.sysName AS hitSysName, g.desc AS hitDesc FROM kescience.fitnessbrowser.cofit c "
             f"LEFT JOIN kescience.fitnessbrowser.gene g ON c.orgId=g.orgId AND c.hitId=g.locusId "
             f"WHERE c.orgId='Putida' AND c.locusId IN {genes} AND CAST(c.rank AS INT) <= 10 "
             f"ORDER BY c.locusId, rank")
    results["cofit_top10"] = spark.sql(q_cof).toPandas().to_dict(orient="records")
    q_re = (f"SELECT locusId, new_annotation, comment FROM kescience.fitnessbrowser.reannotation "
            f"WHERE orgId='Putida' AND locusId IN {genes} ORDER BY locusId")
    try:
        results["reannotation"] = spark.sql(q_re).toPandas().to_dict(orient="records")
    except Exception as e:  # column names may differ
        results["reannotation"] = spark.sql(
            f"SELECT * FROM kescience.fitnessbrowser.reannotation WHERE orgId='Putida' "
            f"AND locusId IN {genes}").toPandas().to_dict(orient="records")
except Exception as e:
    results["fitness_error"] = repr(e)[:2000]

(OUT / "results.json").write_text(json.dumps(results, indent=1, default=str))
print(json.dumps({k: results[k] for k in ["orthology"]}, indent=1))
print(json.dumps(results.get("fitness", results.get("fitness_error")), indent=1, default=str)[:6000])
