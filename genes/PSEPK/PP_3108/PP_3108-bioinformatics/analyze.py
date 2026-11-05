"""Compare dashboard protein NZ_SPUT01000035.1_2 (P. putida KB3, WP_135192713.1)
with KT2440 Tke2 (PP_3108, Q88I91) along its length, and its locus partners.

Questions:
  1. Is identity uniform along the length, or does the C-terminal toxin
     (after the Rhs PxxxxDPxGL motif) differ?
  2. Which toxin-domain HMMs hit each C-terminus?
  3. Are PAAR / prePAAR motifs present?
  4. Do the flanking immunity / chaperone / VgrG genes match KT2440's?
"""
from __future__ import annotations

import argparse
import gzip
import json
import random
import re
import urllib.request
from pathlib import Path

import pyhmmer
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

INTERPRO_HMM = "https://www.ebi.ac.uk/interpro/api/entry/pfam/{acc}?annotation=hmm"
# PAAR, prePAAR (class I), LHH, AHH, colicin DNase, HNH, WHH, Endonuclea_NS_2
PFAMS = ["PF05488", "PF25799", "PF14411", "PF14412", "PF12639", "PF01844", "PF14414", "PF13930"]
# Rhs core C-terminal boundary motif; Bernal et al. 2017 write it PxxxxDPxGL,
# but in both proteins here it reads VTQDPIGL, so only DPxGL is matched.
RHS_END = re.compile(r"DP.GL")
KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
          L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)


def fetch_hmm(acc: str, cache: Path) -> Path:
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / f"{acc}.hmm"
    if not path.exists():
        with urllib.request.urlopen(INTERPRO_HMM.format(acc=acc), timeout=120) as r:
            raw = r.read()
        path.write_bytes(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)
    return path


def read_fasta(path: Path) -> dict[str, str]:
    return {r.id: str(r.seq).upper().rstrip("*") for r in SeqIO.parse(str(path), "fasta")}


def aligner(mode: str) -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = mode
    return a


def stats(q: str, s: str, mode: str = "global") -> dict:
    aln = aligner(mode).align(q, s)[0]
    cols = [(x, y) for x, y in zip(aln[0], aln[1]) if x != "-" and y != "-"]
    ident = sum(1 for x, y in cols if x == y)
    qb, tb = aln.aligned
    return {
        "query_len": len(q), "subject_len": len(s),
        "aligned_pairs": len(cols),
        "identical": ident,
        "identity": round(ident / len(cols), 3) if cols else 0.0,
        "query_span": [int(qb[0][0]) + 1, int(qb[-1][1])] if len(qb) else None,
        "subject_span": [int(tb[0][0]) + 1, int(tb[-1][1])] if len(tb) else None,
        "score": aln.score,
    }


def shuffled_z(q: str, s: str, n: int = 100, seed: int = 1) -> float:
    a = aligner("local")
    real = a.score(q, s)
    rng = random.Random(seed)
    scores = []
    for _ in range(n):
        lst = list(s)
        rng.shuffle(lst)
        scores.append(a.score(q, "".join(lst)))
    mu = sum(scores) / n
    sd = (sum((x - mu) ** 2 for x in scores) / (n - 1)) ** 0.5
    return round((real - mu) / sd, 1) if sd else None


def column_map(q: str, s: str):
    """Per query position: (subject residue or '-', identical?)."""
    aln = aligner("global").align(q, s)[0]
    out = []
    for x, y in zip(aln[0], aln[1]):
        if x == "-":
            continue
        out.append((y, x == y))
    return out


def windows(q: str, colmap, size: int, step: int) -> list[dict]:
    res = []
    for start in range(0, len(q) - size + 1, step):
        seg = colmap[start:start + size]
        aligned = sum(1 for y, _ in seg if y != "-")
        ident = sum(1 for _, i in seg if i)
        res.append({"query_start": start + 1, "query_end": start + size,
                    "aligned": aligned, "identical": ident,
                    "identity_over_window": round(ident / size, 3)})
    last = len(q) - (len(q) % step or step)
    return res


def region(colmap, a: int, b: int) -> dict:
    seg = colmap[a - 1:b]
    aligned = sum(1 for y, _ in seg if y != "-")
    ident = sum(1 for _, i in seg if i)
    return {"query_range": [a, b], "length": b - a + 1, "aligned": aligned,
            "identical": ident, "identity_over_region": round(ident / (b - a + 1), 3),
            "identity_over_aligned": round(ident / aligned, 3) if aligned else 0.0}


def hmm_hits(hmms: list[Path], seqs: dict[str, str]) -> list[dict]:
    alpha = pyhmmer.easel.Alphabet.amino()
    dig = [pyhmmer.easel.TextSequence(name=k.encode(), sequence=v).digitize(alpha)
           for k, v in seqs.items()]
    out = []
    for p in hmms:
        with pyhmmer.plan7.HMMFile(str(p)) as f:
            hmm = f.read()
        for hits in pyhmmer.hmmsearch([hmm], dig, E=10.0):
            for h in hits:
                for d in h.domains:
                    _s = lambda v: v.decode() if isinstance(v, bytes) else v
                    out.append({"hmm": _s(hmm.accession) or _s(hmm.name), "name": _s(hmm.name),
                                "sequence": _s(h.name), "env": [d.env_from, d.env_to],
                                "i_evalue": float(f"{d.i_evalue:.2g}"),
                                "score": round(d.score, 1)})
    return out


def hydrophobic_segments(seq: str, win: int = 19, thr: float = 1.6) -> list[list[int]]:
    segs, cur = [], None
    for i in range(len(seq) - win + 1):
        h = sum(KD[c] for c in seq[i:i + win]) / win
        if h >= thr:
            cur = [i + 1, i + win] if cur is None else [cur[0], i + win]
        elif cur:
            segs.append(cur)
            cur = None
    if cur:
        segs.append(cur)
    return segs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", required=True)
    ap.add_argument("--kt2440", required=True)
    ap.add_argument("--contig", required=True)
    ap.add_argument("--hmm-cache", required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()

    qd = read_fasta(Path(a.query))
    qid, q = next(iter(qd.items()))
    kt = {k.split("|")[1] if "|" in k else k: v for k, v in read_fasta(Path(a.kt2440)).items()}
    contig = read_fasta(Path(a.contig))
    s = kt["Q88I91"]  # PP_3108

    res: dict = {"query": qid, "reference": "Q88I91 (PP_3108, Tke2)"}
    res["full_length_global"] = stats(q, s)
    cm = column_map(q, s)
    res["windows_100_step50"] = windows(q, cm, 100, 50)

    qm = [(m.start() + 1, m.group()) for m in RHS_END.finditer(q)]
    sm = [(m.start() + 1, m.group()) for m in RHS_END.finditer(s)]
    res["DPxGL_query"] = qm
    res["DPxGL_PP_3108"] = sm
    # toxin region = residues after the FIRST DPxGL (the one shared by both proteins)
    q_ct = qm[0][0] + 5
    s_ct = sm[0][0] + 5
    res["regions_on_query"] = {
        "prePAAR_1_58": region(cm, 1, 58),
        "PAAR_59_148": region(cm, 59, 148),
        "Rhs_shell_149_to_DPxGL": region(cm, 149, q_ct - 1),
        "C_terminal_toxin_after_DPxGL": region(cm, q_ct, len(q)),
        "Ctox_proximal_linker_to_1312": region(cm, q_ct, 1312),
        "Ctox_LHH_domain_1313_1409": region(cm, 1313, len(q)),
    }
    lhh = q[1312:]
    res["LHH_segment_vs_PP_3108_Ctox"] = {
        "local": stats(lhh, s[s_ct - 1:], "local"),
        "local_shuffle_z": shuffled_z(lhh, s[s_ct - 1:]),
    }
    qtox, stox = q[q_ct - 1:], s[s_ct - 1:]
    res["C_terminal_toxin"] = {
        "query_start": q_ct, "query_len": len(qtox),
        "PP_3108_start": s_ct, "PP_3108_len": len(stox),
        "query_seq": qtox, "PP_3108_seq": stox,
        "local": stats(qtox, stox, "local"),
        "global": stats(qtox, stox, "global"),
        "local_shuffle_z": shuffled_z(qtox, stox),
    }
    # C-terminal toxin vs the KT2440 Rhs shell excluded: identity of shell alone
    res["Rhs_shell_global"] = stats(q[148:q_ct - 1], s[148:s_ct - 1])

    pairs = {
        "immunity_WP_223271142.1_vs_PP_3109(Tki2)": ("WP_223271142.1", "Q88I90"),
        "DcrB_WP_003248404.1_vs_PP_3107(EagR,DUF1795)": ("WP_003248404.1", "Q88I92"),
        "VgrG_WP_103444332.1_vs_PP_3106(VgrG1)": ("WP_103444332.1", "Q88I93"),
        "DcrB_WP_003248404.1_vs_PP_4084(DUF1795)": ("WP_003248404.1", "Q88FK7"),
    }
    res["locus_partners"] = {}
    for label, (c, k) in pairs.items():
        st = stats(contig[c], kt[k], "global")
        st["local"] = stats(contig[c], kt[k], "local")
        st["local_shuffle_z"] = shuffled_z(contig[c], kt[k])
        res["locus_partners"][label] = st

    hmms = [fetch_hmm(p, Path(a.hmm_cache)) for p in PFAMS]
    res["hmm_hits"] = hmm_hits(hmms, {
        "query_full": q, "PP_3108_full": s,
        "query_Ctox": qtox, "PP_3108_Ctox": stox,
    })
    res["paar_region_query_59_148"] = q[58:148]
    res["paar_region_PP_3108_59_148"] = s[58:148]
    res["hydrophobic_segments_KD19_ge1.6"] = {
        "query_1_160": hydrophobic_segments(q[:160]),
        "PP_3108_1_160": hydrophobic_segments(s[:160]),
    }
    Path(a.output).write_text(json.dumps(res, indent=2))
    print(json.dumps({k: v for k, v in res.items() if k not in ("windows_100_step50",)}, indent=1)[:6000])


if __name__ == "__main__":
    main()
