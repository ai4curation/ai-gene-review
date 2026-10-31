"""Map query Glu residues of CP088958.1_900 (Q31PW6) onto the Pfam DUF4062 HMM (PF13271).

Downloads the PF13271 profile HMM from InterPro, aligns the query with pyhmmer
(hmmscan-equivalent domain alignment), and for each query Glu inside the domain hit
reports the HMM match state and that state's emission probability for Glu (E). A Glu
at a state with high E emission is the family-conserved Glu.

Writes $BERIL_RUN_DIR/results.json.
"""
import argparse
import gzip
import io
import json
import os
import urllib.request
from pathlib import Path

import pyhmmer

URL = "https://www.ebi.ac.uk/interpro/api/entry/pfam/PF13271?annotation=hmm"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fasta", type=Path, required=True)
    a = ap.parse_args()
    out = Path(os.environ["BERIL_RUN_DIR"])
    out.mkdir(parents=True, exist_ok=True)

    raw = urllib.request.urlopen(URL, timeout=120).read()
    try:
        raw = gzip.decompress(raw)
    except OSError:
        pass
    (out / "PF13271.hmm").write_bytes(raw)
    with pyhmmer.plan7.HMMFile(io.BytesIO(raw)) as fh:
        hmm = fh.read()

    alpha = pyhmmer.easel.Alphabet.amino()
    q = "".join(l.strip() for l in a.fasta.read_text().splitlines() if not l.startswith(">"))
    seq = pyhmmer.easel.TextSequence(name=b"query", sequence=q).digitize(alpha)
    hits = next(iter(pyhmmer.hmmsearch([hmm], [seq], E=10, domE=10)))
    e_idx = alpha.symbols.index("E")
    doms = []
    for hit in hits:
        for d in hit.domains:
            ali = d.alignment
            qpos, hpos = ali.target_from, ali.hmm_from
            states = {}
            for hc, tc in zip(ali.hmm_sequence, ali.target_sequence):
                if hc != "." and tc != "-":
                    states[qpos] = hpos
                if hc != ".":
                    hpos += 1
                if tc != "-":
                    qpos += 1
            glu = []
            for p, st in sorted(states.items()):
                if q[p - 1] == "E":
                    glu.append({"query_pos": p, "hmm_state": st,
                                "p_E": round(float(hmm.match_emissions[st][e_idx]), 3),
                                "consensus": hmm.consensus[st - 1] if hmm.consensus else None})
            doms.append({"i_evalue": d.i_evalue, "score": d.score,
                         "query_range": [ali.target_from, ali.target_to],
                         "hmm_range": [ali.hmm_from, ali.hmm_to],
                         "hmm_line": ali.hmm_sequence, "query_line": ali.target_sequence,
                         "glu": glu})
    res = {"hmm": hmm.name.decode() if isinstance(hmm.name, bytes) else hmm.name,
           "hmm_length": hmm.M, "domains": doms}
    (out / "results.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps(res, indent=1, default=str))


if __name__ == "__main__":
    main()
