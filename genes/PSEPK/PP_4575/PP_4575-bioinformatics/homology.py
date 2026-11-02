"""PP_4575 (Q88E91) vs the experimentally characterized PxpC proteins (B. subtilis Q7WY77, E. coli YbgK P75745;
Niehaus et al. 2017, PMID:28830929), the KT2440 paralog PP_2922, and the dashboard query; plus the
neighbouring PP_4576 vs PxpB (B. subtilis P60495, E. coli YbgJ P0AAV4) and PP_4577 vs PxpA (B. subtilis
P42963, E. coli YbgL P75746) and the KT2440 PxpB-like paralog PP_2921. Local Smith-Waterman (BLOSUM62,
gap 11/1); identity over aligned columns. Also lists the KT2440 proteins carrying PxpA (PF03746), PxpB (PF02682)
or PxpC (PF02626) Pfam domains and any urea carboxylase / urea amidolyase entries. Sequences from UniProt REST.
Usage: python3 -I homology.py DASHBOARD_FASTA OUTDIR"""
import json, os, sys, urllib.request
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

PROT = {"PP_4575": "Q88E91", "PP_4576": "Q88E90", "PP_2921": "Q88IS8", "PP_2922": "Q88IS7",
        "Bsu_PxpC_KipA": "Q7WY77", "Eco_PxpC_YbgK": "P75745",
        "Bsu_PxpB_KipI": "P60495", "Eco_PxpB_YbgJ": "P0AAV4",
        "Bsu_PxpA_YcsF": "P42963", "Eco_PxpA_YbgL": "P75746"}
PAIRS = [("dashboard", "PP_4575"), ("PP_4575", "Bsu_PxpC_KipA"), ("PP_4575", "Eco_PxpC_YbgK"), ("PP_4575", "PP_2922"),
         ("PP_2922", "Eco_PxpC_YbgK"), ("PP_4576", "Bsu_PxpB_KipI"), ("PP_4576", "Eco_PxpB_YbgJ"), ("PP_4576", "PP_2921"),
         ("PP_4577", "Bsu_PxpA_YcsF"), ("PP_4577", "Eco_PxpA_YbgL")]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.5.0"})
    return urllib.request.urlopen(req, timeout=120).read().decode()


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
    qs, qe = aln.aligned[0][0][0], aln.aligned[0][-1][1]
    ss, se = aln.aligned[1][0][0], aln.aligned[1][-1][1]
    return {"score": aln.score, "aligned_pairs": cols, "identical": ident, "pct_id": round(100 * ident / cols, 1) if cols else 0,
            "query_range": [int(qs) + 1, int(qe)], "subject_range": [int(ss) + 1, int(se)],
            "query_cov_pct": round(100 * (qe - qs) / len(a), 1), "subject_cov_pct": round(100 * (se - ss) / len(b), 1)}


fasta, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
t = get("https://rest.uniprot.org/uniprotkb/search?query=gene:PP_4577+AND+organism_id:160488&fields=accession&format=tsv")
PROT["PP_4577"] = t.split("\n")[1].strip()
seqs = {k: seq(v) for k, v in PROT.items()}
seqs["dashboard"] = str(next(SeqIO.parse(fasta, "fasta")).seq)
res = {"proteins": {k: {"accession": PROT.get(k, "dashboard query"), "length": len(v)} for k, v in seqs.items()},
       "pairs": {f"{a}_vs_{b}": cmp(seqs[a], seqs[b]) for a, b in PAIRS}}
fam = {}
for label, qry in [("PxpA_PF03746", "xref:pfam-PF03746"), ("PxpB_PF02682", "xref:pfam-PF02682"),
                   ("PxpC_PF02626", "xref:pfam-PF02626"), ("urea_carboxylase_or_amidolyase_name", "protein_name:%22urea%20carboxylase%22")]:
    t = get(f"https://rest.uniprot.org/uniprotkb/search?query={qry}+AND+organism_id:160488&fields=accession,gene_oln,protein_name,length,xref_pfam&format=tsv")
    fam[label] = [dict(zip(["accession", "locus", "name", "length", "pfam"], l.split("\t"))) for l in t.strip().split("\n")[1:] if l]
res["KT2440_family_members"] = fam
json.dump(res, open(os.path.join(out, "homology_results.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
