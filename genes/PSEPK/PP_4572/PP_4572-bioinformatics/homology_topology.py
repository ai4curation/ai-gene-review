"""PP_4572 (Q88E94): identity of the dashboard query to Q88E94; local Smith-Waterman (BLOSUM62, gap 11/1)
identity to P. aeruginosa PA2708 (Q9I0D4; Sposato et al. 2024, PMID:38305166) and to the E. coli AsmA-like
proteins (AsmA, TamB, YhdP, YdbH, YicH, YhjG); Kyte-Doolittle hydropathy (19-residue window); and the AlphaFold
DB model: mean pLDDT, length of the periplasmic region's longest CA-CA extent, and a crude CA-geometry
secondary-structure count. Sequences from UniProt REST, model from the AlphaFold DB API.
Usage: python3 -I homology_topology.py DASHBOARD_FASTA OUTDIR ALPHAFOLD_PDB
(the AlphaFold DB returns 403 inside `beril run`, so the v6 model is downloaded beforehand with curl)"""
import io, json, os, sys, urllib.request
import numpy as np
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices
from Bio.PDB import PDBParser

PROT = {"PP_4572": "Q88E94", "PA2708": "Q9I0D4", "Eco_AsmA": "P28249", "Eco_TamB": "P39321", "Eco_YhdP": "P46474",
        "Eco_YdbH": "P52645", "Eco_YicH": "P31433", "Eco_YhjG": "P37645"}


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


KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5, L=3.8, K=-3.9, M=1.9, F=2.8,
          P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)

fasta, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
seqs = {k: seq(v) for k, v in PROT.items()}
seqs["dashboard"] = str(next(SeqIO.parse(fasta, "fasta")).seq)
res = {"proteins": {k: {"accession": PROT.get(k, "dashboard query"), "length": len(v)} for k, v in seqs.items()}}
res["pairs"] = {f"PP_4572_vs_{k}": cmp(seqs["PP_4572"], seqs[k]) for k in PROT if k != "PP_4572"}
res["pairs"]["dashboard_vs_PP_4572"] = cmp(seqs["dashboard"], seqs["PP_4572"])
s = seqs["PP_4572"]
w = 19
kd = [sum(KD[c] for c in s[i:i + w]) / w for i in range(len(s) - w + 1)]
res["hydropathy"] = {"window": w, "windows_above_1.6": [i + 1 for i, v in enumerate(kd) if v > 1.6],
                     "max": round(max(kd), 2), "max_window_start": 1 + int(np.argmax(kd)),
                     "n_term_40": s[:40], "positively_charged_in_first_6": sum(c in "KR" for c in s[:6])}
# AlphaFold model
meta = {"pdbUrl": "https://alphafold.ebi.ac.uk/files/AF-Q88E94-F1-model_v6.pdb (local copy: " + sys.argv[3] + ")"}
pdb = open(sys.argv[3]).read()
st = PDBParser(QUIET=True).get_structure("m", io.StringIO(pdb))
ca = [(r.id[1], r["CA"].coord, r["CA"].bfactor) for r in st.get_residues() if "CA" in r]
idx = np.array([c[0] for c in ca]); xyz = np.array([c[1] for c in ca]); pl = np.array([c[2] for c in ca])
peri = xyz[idx >= 31]
d = np.linalg.norm(peri[:, None, :] - peri[None, :, :], axis=-1)
# crude SS from CA(i)-CA(i+3) distance: helix ~5-5.5 A, strand ~9-10.5 A
d3 = np.linalg.norm(xyz[3:] - xyz[:-3], axis=1)
res["alphafold"] = {"model": meta["pdbUrl"], "mean_plddt": round(float(pl.mean()), 1),
                    "frac_plddt_ge70": round(float((pl >= 70).mean()), 3),
                    "mean_plddt_res31_end": round(float(pl[idx >= 31].mean()), 1),
                    "max_CA_extent_res31_end_A": round(float(d.max()), 1),
                    "frac_CA_i_i3_helixlike_lt6A": round(float((d3 < 6).mean()), 3),
                    "frac_CA_i_i3_strandlike_gt9A": round(float((d3 > 9).mean()), 3)}
json.dump(res, open(os.path.join(out, "homology_topology_results.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
