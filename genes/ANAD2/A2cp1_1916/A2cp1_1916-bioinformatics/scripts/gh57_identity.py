"""Pairwise global identity (BLOSUM62, gap -11/-1; identity over aligned columns without
end gaps, and over the shorter sequence) among the GH57_6 / DUF3536 proteins: GSU2359 (Q74AJ5),
A2cp1_1916 (B8J768), DVU_2472 (Q728Y0), characterized PoGH57 (QCR22797.1) and Amo45 (D3SMQ0).
Writes $BERIL_RUN_DIR/results.json."""
import json, os, urllib.request, itertools
from Bio import Align
from Bio.Align import substitution_matrices
def get(u):
    with urllib.request.urlopen(u, timeout=120) as r: return r.read().decode()
S = {a: "".join(get(f"https://rest.uniprot.org/uniprotkb/{a}.fasta").splitlines()[1:]) for a in ["Q74AJ5", "B8J768", "Q728Y0", "D3SMQ0"]}
S["QCR22797.1"] = "".join(get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=QCR22797.1&rettype=fasta").splitlines()[1:])
al = Align.PairwiseAligner(); al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score, al.mode = -11, -1, "global"
al.end_gap_score = 0
res = {}
for a, b in itertools.combinations(S, 2):
    aln = al.align(S[a], S[b])[0]
    ident = aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1; ident += S[a][i] == S[b][j]
    res[f"{a}|{b}"] = {"pct_id_aligned": round(100 * ident / aligned, 1), "aligned": aligned,
                        "pct_id_shorter": round(100 * ident / min(len(S[a]), len(S[b])), 1)}
    print(a, b, res[f"{a}|{b}"])
json.dump({"lengths": {k: len(v) for k, v in S.items()}, "pairs": res}, open(os.path.join(os.environ.get("BERIL_RUN_DIR", "/tmp"), "results.json"), "w"), indent=1)
