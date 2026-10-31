"""Does Q31PW6 Glu83 correspond to human TEP1 E1008, the tested DUF4062 catalytic Glu?

Two independent mappings:
1. Each sequence is aligned to the Pfam PF13271 (DUF4062) profile HMM with pyhmmer;
   the HMM match state of Q31PW6 E83 and of TEP1 E1008 are compared.
2. A direct pairwise local alignment (BLOSUM62, gap open 10 / extend 1) of the Q31PW6
   DUF4062 region (1-160) against the TEP1 DUF4062 region (886-1113); the TEP1 residue
   aligned to Q31PW6 position 83 is reported.

Sequences are the UniProt records, fetched through NCBI efetch. The HMM is read from --hmm when given (a saved copy
of the InterPro download), else fetched. Writes $BERIL_RUN_DIR/results.json.
"""
import argparse
import gzip
import io
import json
import os
import urllib.request
from pathlib import Path

import pyhmmer
from Bio import Align
from Bio.Align import substitution_matrices

HMM_URL = "https://www.ebi.ac.uk/interpro/api/entry/pfam/PF13271?annotation=hmm"
# UniProt REST returned HTTP 500 on 2026-10-31; NCBI serves the same UniProt records.
SEQ_URL = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
           "?db=protein&id={acc}&rettype=fasta&retmode=text")
QUERY, QUERY_GLU = "Q31PW6", 83
TEP1, TEP1_GLU, TEP1_DOM = "Q99973", 1008, (886, 1113)


def fetch(url):
    return urllib.request.urlopen(url, timeout=120).read()


def uniprot_seq(acc):
    txt = fetch(SEQ_URL.format(acc=acc)).decode()
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def hmm_states(hmm, alpha, name, seq):
    """Map sequence positions (1-based) to HMM match states for the best domain."""
    ds = pyhmmer.easel.TextSequence(name=name.encode(), sequence=seq).digitize(alpha)
    hits = next(iter(pyhmmer.hmmsearch([hmm], [ds], E=10, domE=10)))
    best = None
    for hit in hits:
        for d in hit.domains:
            if best is None or d.score > best.score:
                best = d
    ali = best.alignment
    qpos, hpos, states = ali.target_from, ali.hmm_from, {}
    for hc, tc in zip(ali.hmm_sequence, ali.target_sequence):
        if hc != "." and tc != "-":
            states[qpos] = hpos
        if hc != ".":
            hpos += 1
        if tc != "-":
            qpos += 1
    return states, {"i_evalue": best.i_evalue, "score": best.score,
                    "seq_range": [ali.target_from, ali.target_to],
                    "hmm_range": [ali.hmm_from, ali.hmm_to]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hmm", type=Path)
    a = ap.parse_args()
    out = Path(os.environ["BERIL_RUN_DIR"])
    out.mkdir(parents=True, exist_ok=True)
    raw = a.hmm.read_bytes() if a.hmm else fetch(HMM_URL)
    try:
        raw = gzip.decompress(raw)
    except OSError:
        pass
    with pyhmmer.plan7.HMMFile(io.BytesIO(raw)) as fh:
        hmm = fh.read()
    alpha = pyhmmer.easel.Alphabet.amino()
    e_idx = alpha.symbols.index("E")

    q, t = uniprot_seq(QUERY), uniprot_seq(TEP1)
    assert q[QUERY_GLU - 1] == "E" and t[TEP1_GLU - 1] == "E"
    qs, qdom = hmm_states(hmm, alpha, QUERY, q)
    ts, tdom = hmm_states(hmm, alpha, TEP1, t)
    q_state, t_state = qs.get(QUERY_GLU), ts.get(TEP1_GLU)

    # Direct pairwise alignment of the two DUF4062 regions.
    al = Align.PairwiseAligner(mode="local",
                               substitution_matrix=substitution_matrices.load("BLOSUM62"),
                               open_gap_score=-10, extend_gap_score=-1)
    qreg, treg = q[:160], t[TEP1_DOM[0] - 1:TEP1_DOM[1]]
    aln = al.align(qreg, treg)[0]
    paired = {}
    for (qa, qb), (ta, tb) in zip(*aln.aligned):
        for k in range(qb - qa):
            paired[qa + k + 1] = TEP1_DOM[0] + ta + k
    t_at_q83 = paired.get(QUERY_GLU)
    ident = sum(q[i - 1] == t[j - 1] for i, j in paired.items())
    window = {p: (q[p - 1], paired.get(p), t[paired[p] - 1] if p in paired else None)
              for p in range(QUERY_GLU - 5, QUERY_GLU + 4)}

    res = {
        "query": QUERY, "tep1": TEP1, "query_glu": QUERY_GLU, "tep1_glu": TEP1_GLU,
        "hmm": {"name": hmm.name if isinstance(hmm.name, str) else hmm.name.decode(),
                "length": hmm.M, "query_domain": qdom, "tep1_domain": tdom,
                "query_E83_state": q_state, "tep1_E1008_state": t_state,
                "same_state": q_state is not None and q_state == t_state,
                "state_consensus": hmm.consensus[q_state - 1] if q_state else None,
                "state_p_E": round(float(hmm.match_emissions[q_state][e_idx]), 3) if q_state else None},
        "pairwise": {"score": aln.score, "aligned_pairs": len(paired),
                     "identity_over_aligned": round(ident / len(paired), 3) if paired else None,
                     "tep1_residue_aligned_to_q83": t_at_q83,
                     "tep1_aa_at_that_position": t[t_at_q83 - 1] if t_at_q83 else None,
                     "matches_E1008": t_at_q83 == TEP1_GLU,
                     "window_q76_86": {str(k): v for k, v in window.items()},
                     "alignment": str(aln)},
    }
    (out / "results.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps({k: v for k, v in res.items() if k != "pairwise"}, indent=1, default=str))
    print(json.dumps({k: v for k, v in res["pairwise"].items() if k != "alignment"}, indent=1, default=str))
    print(res["pairwise"]["alignment"])


if __name__ == "__main__":
    main()
