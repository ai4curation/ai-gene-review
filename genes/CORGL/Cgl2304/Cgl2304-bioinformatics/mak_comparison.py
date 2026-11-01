"""Compare Cgl2304 (Q8NNA0; dashboard NZ_CP025533.1_2296) with characterised maltokinases.

Questions tested:
  1. How similar is the query to characterised maltokinases (Mak, EC 2.7.1.175)?
  2. Which part of the Mak chain does the query cover (is the N-terminal cap
     subdomain or the C-terminal maltose-binding region missing)?
  3. Are the catalytic / nucleotide / Mg / maltose-binding residues identified in
     the M. vanbaalenii Mak structure (Fraga et al. 2015, PMID:25619172) and the
     M. tuberculosis Mak mutants conserved in the query?
  4. Do Pfam HMMs for the Mak N-terminal cap (PF18085) and the APH
     phosphotransferase fold (PF01636) hit the query?

All sequences are downloaded from UniProt REST at run time; nothing is hardcoded
except the accession list and the published residue numbers being mapped.
Writes results to $BERIL_RUN_DIR (or ./data if unset).
"""
import argparse
import gzip
import io
import json
import os
import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

REFS = {
    # accession: label (all reviewed Swiss-Prot maltokinases or literature-named Pep2)
    "A1TH50": "Mak M. vanbaalenii Mvan_5735 (structure 4U94; PMID:25619172)",
    "O07177": "Mak M. tuberculosis Rv0127 (structure 4O7O)",
    "Q7U2S7": "Mak M. bovis AF2122/97 (BCG Mak identical; PMID:20507595)",
    "A0R6D9": "Mak/Pep2 M. smegmatis MSMEG_6514",
    "Q7WUM3": "Mak1 Actinoplanes missouriensis (PMID:12879214, 15378530)",
    "Q7AKG7": "Pep2A S. coelicolor SCO5441 (PMID:15378530)",
}
CGL_TRES = "Q8NNA1"  # Cgl2303 / cg2529 TreS of C. glutamicum

# Residues named in Fraga et al. 2015 (M. vanbaalenii Mak, A1TH50 numbering)
MVAN_SITES = {
    13: "Arg13 invariant, cap subdomain (contacts P-loop region)",
    14: "Trp14 conserved, cap subdomain (stacks with Arg152)",
    88: "Asp88 strictly conserved (salt bridge to Arg152)",
    92: "Asp92 strictly conserved (salt bridge to cap Arg59)",
    134: "Glu134 P-loop (AEQSNTSV)",
    135: "Gln135 P-loop (water-mediated gamma-phosphate contact)",
    136: "Ser136 P-loop gamma-phosphate (S144A in Mtb: activity drastically reduced)",
    137: "Asn137 P-loop (N145A in Mtb: inactive)",
    149: "Lys149 invariant ATP alpha-phosphate lysine (AMLKV motif)",
    152: "Arg152 strictly conserved cap/intermediate interface",
    267: "Arg267 conserved basic residue, maltose pocket",
    303: "His303 catalytic loop HGD",
    304: "Gly304 catalytic loop HGD",
    305: "Asp305 catalytic base (HGD)",
    307: "His307 catalytic loop, maltose pocket",
    310: "Gln310 Mg1 ligand (Brenner-motif N position)",
    322: "Asp322 DFE Mg-binding Asp (D339N in Mtb: inactive)",
    323: "Phe323 DFE",
    324: "Glu324 DFE",
    334: "Arg334 stabilises DFE Glu (R351A in Mtb: decreased)",
    342: "Arg342 conserved basic residue, maltose pocket",
    413: "Lys413 maltose binding (K413A: activity practically abolished)",
    416: "Tyr416 maltose binding (Y416A/F: activity practically abolished)",
    420: "Tyr420 maltose binding (Y420A/F: activity practically abolished)",
}

PFAM = {"PF18085": "Mak_N_cap", "PF01636": "APH"}


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def uniprot_seq(acc):
    txt = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").decode()
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def aligner():
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    # free end gaps so a shorter protein is not penalised for missing termini
    al.target_end_gap_score = 0
    al.query_end_gap_score = 0
    return al


def pair_stats(aln, qlen, tlen):
    """aln: target=query (Cgl2304), query=reference."""
    qmap = {}  # ref pos (1-based) -> query pos (1-based)
    ident = cols = 0
    qcov = set()
    rcov = set()
    for (qs, qe), (rs, re_) in zip(*aln.aligned):
        for i, j in zip(range(qs, qe), range(rs, re_)):
            cols += 1
            qcov.add(i)
            rcov.add(j)
            qmap[j + 1] = i + 1
            if aln.target[i] == aln.query[j]:
                ident += 1
    return {
        "aligned_pairs": cols,
        "identical": ident,
        "pct_identity_over_aligned": round(100 * ident / cols, 1) if cols else 0,
        "pct_identity_over_query_len": round(100 * ident / qlen, 1),
        "query_coverage_pct": round(100 * len(qcov) / qlen, 1),
        "ref_coverage_pct": round(100 * len(rcov) / tlen, 1),
        "ref_first_aligned": min(rcov) + 1 if rcov else None,
        "ref_last_aligned": max(rcov) + 1 if rcov else None,
        "query_first_aligned": min(qcov) + 1 if qcov else None,
        "query_last_aligned": max(qcov) + 1 if qcov else None,
    }, qmap


def run_pfam(seqs, outdir):
    import pyhmmer

    alpha = pyhmmer.easel.Alphabet.amino()
    hmms = []
    for acc in PFAM:
        raw = fetch(f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{acc}?annotation=hmm")
        try:
            raw = gzip.decompress(raw)
        except OSError:
            pass
        (outdir / f"{acc}.hmm").write_bytes(raw)
        with pyhmmer.plan7.HMMFile(io.BytesIO(raw)) as fh:
            hmms.append(fh.read())
    digital = [
        pyhmmer.easel.TextSequence(name=name.encode(), sequence=s).digitize(alpha)
        for name, s in seqs.items()
    ]
    res = []
    for hits in pyhmmer.hmmsearch(hmms, digital, E=10.0, domE=10.0):
        model = hits.query.name if hasattr(hits, "query") else None
        model = model.decode() if isinstance(model, bytes) else str(model)
        for h in hits:
            for d in h.domains:
                res.append({
                    "hmm": model,
                    "sequence": h.name.decode() if isinstance(h.name, bytes) else h.name,
                    "seq_evalue": h.evalue,
                    "dom_i_evalue": d.i_evalue,
                    "dom_score": round(d.score, 1),
                    "env_from": d.env_from,
                    "env_to": d.env_to,
                    "hmm_from": d.alignment.hmm_from,
                    "hmm_to": d.alignment.hmm_to,
                })
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fasta", type=Path, required=True, help="dashboard query FASTA")
    a = ap.parse_args()
    out = Path(os.environ.get("BERIL_RUN_DIR", "data"))
    out.mkdir(parents=True, exist_ok=True)

    q = "".join(l.strip() for l in a.fasta.read_text().splitlines() if not l.startswith(">"))
    q_up = uniprot_seq("Q8NNA0")
    seqs = {"Q8NNA0": q_up}
    for acc in REFS:
        seqs[acc] = uniprot_seq(acc)
    seqs[CGL_TRES] = uniprot_seq(CGL_TRES)
    (out / "sequences.fasta").write_text("".join(f">{k}\n{v}\n" for k, v in seqs.items()))

    result = {
        "query_len": len(q),
        "query_identical_to_Q8NNA0": q == q_up,
        "ref_lengths": {k: len(v) for k, v in seqs.items()},
        "pairwise": {},
        "mvan_site_mapping": [],
        "mtb_site_mapping": [],
        "motif_scan": {},
    }
    al = aligner()
    qmaps = {}
    for acc, label in list(REFS.items()) + [(CGL_TRES, "TreS C. glutamicum Cgl2303/cg2529")]:
        aln = al.align(q, seqs[acc])[0]
        stats, qmap = pair_stats(aln, len(q), len(seqs[acc]))
        stats["label"] = label
        result["pairwise"][acc] = stats
        qmaps[acc] = qmap
        (out / f"aln_Q8NNA0_vs_{acc}.txt").write_text(str(aln))

    mv = seqs["A1TH50"]
    for pos, desc in MVAN_SITES.items():
        qp = qmaps["A1TH50"].get(pos)
        result["mvan_site_mapping"].append({
            "mvan_pos": pos,
            "mvan_aa": mv[pos - 1],
            "description": desc,
            "query_pos": qp,
            "query_aa": q[qp - 1] if qp else None,
            "conserved": bool(qp) and q[qp - 1] == mv[pos - 1],
        })
    mtb = seqs["O07177"]
    for pos, desc in {144: "Ser144 (S144A drastically reduced)", 145: "Asn145 (N145A inactive)",
                      339: "Asp339 Mg-binding (D339N inactive)", 351: "Arg351 (R351A decreased)"}.items():
        qp = qmaps["O07177"].get(pos)
        result["mtb_site_mapping"].append({
            "mtb_pos": pos, "mtb_aa": mtb[pos - 1], "description": desc,
            "query_pos": qp, "query_aa": q[qp - 1] if qp else None,
            "conserved": bool(qp) and q[qp - 1] == mtb[pos - 1],
        })

    patterns = {
        "catalytic_loop_HGDxHxxQ_or_N (Mak HGD..H..Q; APH HxDxxxxN)": r"H[GA]D.H..[NQ]",
        "Brenner_HxDxxxxN_strict": r"H.D....N",
        "DFE/DFG Mg-binding": r"DF[EG]",
        "P-loop E-Q-S-N (Mak AEQSNTSV)": r"EQSN",
    }
    for name, pat in patterns.items():
        hits = {}
        for acc, s in seqs.items():
            hits[acc] = [(m.start() + 1, m.group(0)) for m in re.finditer(pat, s)]
        result["motif_scan"][name] = hits

    try:
        result["pfam_hmmsearch"] = run_pfam(seqs, out)
    except Exception as e:  # report, do not invent
        result["pfam_hmmsearch_error"] = repr(e)

    (out / "mak_comparison.json").write_text(json.dumps(result, indent=2, default=float))
    print(json.dumps({k: v for k, v in result.items() if k != "motif_scan"}, indent=1, default=float)[:8000])
    print(json.dumps(result["motif_scan"], indent=1))


if __name__ == "__main__":
    main()
