"""Identity of the dashboard query (NZ_CP015876.1_1546) to KT2440 PP_4294 (Q88F06) and E. coli YedI (P46125),
and comparison of predicted TM helices (DeepTMHMM on the query; UniProt FT TRANSMEM for Q88F06 and P46125).
Usage: python seq_topology.py DASHBOARD_JSON OUTDIR   (fetches UniProt entries over REST)"""
import json, os, re, sys, urllib.request
from Bio import Align
from Bio.Align import substitution_matrices


def uniprot(acc):
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60) as r:
        d = json.load(r)
    tms = [(f["location"]["start"]["value"], f["location"]["end"]["value"])
           for f in d.get("features", []) if f["type"] == "Transmembrane"]
    return d["sequence"]["value"], tms


def align(a, b):
    al = Align.PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                               open_gap_score=-10, extend_gap_score=-0.5, end_gap_score=0)
    aln = al.align(a, b)[0]
    ident = aligned = 0
    mapping = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += a[i] == b[j]
            mapping[i + 1] = j + 1
    return {"len_a": len(a), "len_b": len(b), "aligned": aligned, "identical": ident,
            "pct_id_aligned": round(100 * ident / aligned, 1), "pct_id_query": round(100 * ident / len(a), 1)}, mapping


def segs(path, ch="M"):
    return [(m.start() + 1, m.end()) for m in re.finditer(ch + "+", path)]


dj, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
row = json.load(open(dj))["rows"][0] if "rows" in json.load(open(dj)) else json.load(open(dj))
d = json.load(open(dj))
q, path = d["sequence"], d["topology_path"]
res = {"query": d["dashboard_id"], "query_len": len(q)}
res["query_deeptmhmm_tm"] = segs(path)
res["query_deeptmhmm_outside_loops"] = segs(path, "O")
res["query_n_terminus"] = {"I": "inside(cytoplasm)", "O": "outside"}.get(path[0], path[0])
res["query_c_terminus"] = {"I": "inside(cytoplasm)", "O": "outside"}.get(path[-1], path[-1])
res["query_n_terminal_soluble_len"] = res["query_deeptmhmm_tm"][0][0] - 1
for acc in ("Q88F06", "P46125"):
    s, tms = uniprot(acc)
    stats, m = align(q, s)
    stats["uniprot_tm"] = tms
    stats["query_tm_mapped_to_subject"] = [(m.get(a), m.get(b)) for a, b in res["query_deeptmhmm_tm"]]
    res[acc] = stats
json.dump(res, open(os.path.join(out, "seq_topology.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
