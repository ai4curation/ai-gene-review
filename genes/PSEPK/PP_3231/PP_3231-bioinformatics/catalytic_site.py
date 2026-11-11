"""Map Ere-family catalytic residues onto PP_3231 (Q88HX2) by pairwise global alignment.

Catalytic residues (EreC numbering, Zielinski et al. 2021, PMID:33741980): E47, H50 (general
base), E78, R261 (K in EreB/EreD), H289. EreB H46 = EreC H50 (Morar et al. 2012, PMID:22303981).
References: EreA P07684, EreB P05789, EreC C7C425, EreD A0A0H4JQQ7 (UniProt REST), Bcr136
(PDB 2QGM chain A, B. cereus ATCC 14579; an esterase that does not inactivate macrolides).
Query: the dashboard FASTA (identical to Q88HX2).

Usage: python -I catalytic_site.py QUERY_FASTA OUTDIR
"""
import json
import os
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = {"EreA": "P07684", "EreB": "P05789", "EreC": "C7C425", "EreD": "A0A0H4JQQ7"}
PDB = {"Bcr136": "2QGM"}
CATALYTIC_EREC = {47: "E", 50: "H", 78: "E", 261: "R", 289: "H"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        txt = r.read().decode()
    lines = txt.strip().splitlines()
    first = lines[0]
    seq = "".join(lines[1:]) if first.startswith(">") else None
    if first.startswith(">") and txt.count(">") > 1:  # PDB multi-chain: take the first chain
        seq = "".join(txt.split(">")[1].splitlines()[1:])
    return first, seq


def read_fasta(p):
    return "".join(l.strip() for l in open(p) if not l.startswith(">"))


def aligner():
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score, a.extend_gap_score = -10, -0.5
    a.mode = "global"
    a.end_gap_score = 0  # free end gaps (semi-global)
    return a


def mapping(aln):
    """Return dict target_pos(1-based) -> query_pos(1-based) for aligned columns."""
    m = {}
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            m[int(ts) + i + 1] = int(qs) + i + 1
    return m


def identity(aln, t, q):
    pairs = ident = 0
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            pairs += 1
            ident += t[ts + i] == q[qs + i]
    return pairs, ident


def main():
    query = read_fasta(sys.argv[1])
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    refs = {}
    for k, acc in UNIPROT.items():
        h, s = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
        refs[k] = {"source": f"UniProt:{acc}", "header": h, "seq": s}
    for k, pid in PDB.items():
        h, s = fetch(f"https://www.rcsb.org/fasta/entry/{pid}")
        refs[k] = {"source": f"PDB:{pid}", "header": h, "seq": s}
    erec = refs["EreC"]["seq"]
    check = {p: erec[p - 1] for p in CATALYTIC_EREC}
    a = aligner()
    res = {"query_length": len(query), "erec_numbering_check": check, "refs": {}}
    # map EreC positions onto every reference and onto the query
    erec_to_query = mapping(a.align(erec, query)[0])
    for k, r in refs.items():
        aln = a.align(r["seq"], query)[0]
        pairs, ident = identity(aln, r["seq"], query)
        entry = {"source": r["source"], "length": len(r["seq"]), "aligned_pairs": pairs,
                 "identity_pct_over_aligned": round(100 * ident / pairs, 1), "score": float(aln.score)}
        if k != "EreC":
            aln_e = a.align(erec, r["seq"])[0]
            e2r = mapping(aln_e)
        else:
            e2r = {p: p for p in CATALYTIC_EREC}
        entry["catalytic_residues_in_ref"] = {
            f"EreC_{CATALYTIC_EREC[p]}{p}": (r["seq"][e2r[p] - 1] + str(e2r[p])) if p in e2r else "gap"
            for p in CATALYTIC_EREC}
        res["refs"][k] = entry
        with open(os.path.join(out, f"aln_{k}_vs_PP_3231.txt"), "w") as fh:
            fh.write(str(aln))
    q = {}
    for p, aa in CATALYTIC_EREC.items():
        qp = erec_to_query.get(p)
        q[f"EreC_{aa}{p}"] = {"query_pos": qp, "query_aa": query[qp - 1] if qp else None,
                             "window_query": query[max(0, qp - 6):qp + 5] if qp else None,
                             "window_erec": erec[p - 6:p + 5]}
    res["PP_3231_at_EreC_catalytic_positions"] = q
    json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
