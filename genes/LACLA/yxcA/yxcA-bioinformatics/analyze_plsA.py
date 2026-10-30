"""Compare Q9CDI2 (L. lactis IL1403 yxcA) with experimentally characterized
plasmalogen synthases (PlsA / PlsAR) and test the uncharacterised C-terminal
region for the HGD-D (Red2) domain that Pfam does not call on the full sequence.

Run:  uv run python analyze_plsA.py
Writes: sequences.fasta, results.json (all numbers are computed here).
"""

import io
import json
import time
from pathlib import Path

import pyhmmer
import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent

# label -> (source, identifier, note)
SEQUENCES = {
    "Q9CDI2": ("uniprot", "Q9CDI2", "L. lactis subsp. lactis IL1403 yxcA (this review)"),
    "UPI00072AC48C": ("uniparc", "UPI00072AC48C",
                      "KBase NZ_VXKC01000008.1_19 / WP_081041604 (L. lactis)"),
    "ABJ73971.1": ("ncbi", "ABJ73971.1",
                   "L. cremoris SK11/ATCC BAA-493 LACR_2543 = PlsA cloned in PMID:41427725"),
    "A2RP33": ("uniprot", "A2RP33", "L. cremoris MG1363 llmg_2516"),
    "AAO81118.1": ("ncbi", "AAO81118.1",
                   "E. faecalis V583 EF1327 PlsA (PMID:33350306)"),
    "BAB80901.1": ("ncbi", "BAB80901.1",
                   "C. perfringens str. 13 CPE1195 PlsA (Act1-Act2-Red1)"),
    "BAB80900.1": ("ncbi", "BAB80900.1",
                   "C. perfringens str. 13 CPE1194 PlsR (Red2)"),
}

PFAM_MODELS = ["PF01869", "PF09989", "PF06050"]


def fetch(source, ident):
    if source == "uniprot":
        url = f"https://rest.uniprot.org/uniprotkb/{ident}.fasta"
    elif source == "uniparc":
        url = f"https://rest.uniprot.org/uniparc/{ident}.fasta"
    else:
        url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
               f"?db=protein&id={ident}&rettype=fasta&retmode=text")
    for attempt in range(4):
        r = requests.get(url, timeout=60)
        if r.ok:
            break
        time.sleep(2 ** attempt)
    r.raise_for_status()
    time.sleep(0.4)
    return str(next(SeqIO.parse(io.StringIO(r.text), "fasta")).seq)


def aligner(mode):
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score, a.extend_gap_score, a.mode = -11, -1, mode
    return a


def identity(a, b, mode="global"):
    aln = aligner(mode).align(a, b)[0]
    c = aln.counts()
    cols = c.identities + c.mismatches + c.gaps
    (qs, qe) = aln.coordinates[0][0], aln.coordinates[0][-1]
    return {
        "identity_pct": round(100 * c.identities / cols, 1),
        "aligned_columns": int(cols),
        "query_span": f"{qs + 1}-{qe}",
    }, aln


def residue_map(aln):
    """Map 0-based query positions to 0-based target positions."""
    m = {}
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        for i in range(qe - qs):
            m[qs + i] = ts + i
    return m


def fetch_hmm(acc):
    url = f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{acc}?annotation=hmm"
    for attempt in range(5):
        r = requests.get(url, timeout=120)
        if r.ok:
            break
        time.sleep(2 ** attempt)
    r.raise_for_status()
    import gzip
    data = gzip.decompress(r.content) if r.content[:2] == b"\x1f\x8b" else r.content
    with pyhmmer.plan7.HMMFile(io.BytesIO(data)) as f:
        return next(iter(f))


def hmm_hits(hmms, name, seq):
    alpha = pyhmmer.easel.Alphabet.amino()
    ds = pyhmmer.easel.TextSequence(name=name.encode(), sequence=seq).digitize(alpha)
    out = []
    for hits in pyhmmer.hmmsearch(hmms, [ds], E=10, domE=10):
        model = hits.query.name if isinstance(hits.query.name, str) else hits.query.name.decode()
        for h in hits:
            for d in h.domains:
                out.append({
                    "model": model,
                    "env": f"{d.env_from}-{d.env_to}",
                    "hmm": f"{d.alignment.hmm_from}-{d.alignment.hmm_to}",
                    "i_evalue": float(f"{d.i_evalue:.2e}"),
                    "score": round(d.score, 1),
                    "reported": bool(d.reported),
                })
    return out


def main():
    seqs = {k: fetch(s, i) for k, (s, i, _) in SEQUENCES.items()}
    with open(HERE / "sequences.fasta", "w") as fh:
        for k, s in seqs.items():
            fh.write(f">{k} {SEQUENCES[k][2]}\n{s}\n")

    q = seqs["Q9CDI2"]
    res = {"lengths": {k: len(s) for k, s in seqs.items()}, "pairwise": {}}

    # Global identity of Q9CDI2 to each full-length single-chain homolog
    alns = {}
    for k in ["UPI00072AC48C", "ABJ73971.1", "A2RP33", "AAO81118.1"]:
        res["pairwise"][k], alns[k] = identity(q, seqs[k], "global")
    # C. perfringens split operon: local alignments of PlsA and PlsR
    for k in ["BAB80901.1", "BAB80900.1"]:
        res["pairwise"][k], alns[k] = identity(q, seqs[k], "local")

    # Conservation of Act-domain cysteines (Q9CDI2 numbering) in the homologs
    cys = [i for i, aa in enumerate(q) if aa == "C" and i < 620]
    cons = {}
    for i in cys:
        row = {}
        for k in ["AAO81118.1", "BAB80901.1"]:
            j = residue_map(alns[k]).get(i)
            row[k] = seqs[k][j] if j is not None else "-"
        cons[f"C{i + 1}"] = row
    res["act_region_cysteines"] = cons

    # Pfam HMMs on the full chain and on the C-terminal segment (Red2 candidate)
    hmms = [fetch_hmm(a) for a in PFAM_MODELS]
    res["pfam_full"] = hmm_hits(hmms, "Q9CDI2", q)
    cterm_start = 900
    res["pfam_cterm"] = {
        "segment": f"{cterm_start + 1}-{len(q)}",
        "hits": hmm_hits(hmms, "Q9CDI2_Cterm", q[cterm_start:]),
    }
    res["pfam_plsR_control"] = hmm_hits(hmms, "BAB80900.1", seqs["BAB80900.1"])
    res["pfam_EF1327"] = hmm_hits(hmms, "AAO81118.1", seqs["AAO81118.1"])

    (HERE / "results.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
