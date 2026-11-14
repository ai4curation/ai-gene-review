# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare HATPase ATP-binding motifs and the HisKA H-box of KT2440 RetS with
P. aeruginosa RetS (reported kinase-dead, degenerate HATPase) and the GacS
kinases of both strains (active kinases).

Sequences and the UniProt 'Histidine kinase' DOMAIN span are fetched live from
UniProt REST; nothing is hard-coded except the accessions. Output: a TSV-like
report on stdout (redirected to results.txt by the caller).

Motif definitions (Dutta & Inouye 2000-style HATPase boxes, loose regexes):
  N-box  : N within the first ~40 aa of the HATPase half, pattern 'N..[NHT]A'
  G1-box : 'D.G.G'   (DxGxG)
  G2-box : 'G.G.G'   (GxGxG / GxGL)
  H-box  : 'H[ED]..[TN]' around the phospho-acceptor His in HisKA (HExxT/N)
"""
import re
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "RetS_PSEPK": "Q88DK1",
    "RetS_PSEAE": "Q9HUV7",
    "GacS_PSEPK": "Q88MC3",
    "GacS_PSEAE": "G3XD98",
}


def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    j = r.json()
    seq = j["sequence"]["value"]
    hk = [
        (f["location"]["start"]["value"], f["location"]["end"]["value"])
        for f in j.get("features", [])
        if f["type"] == "Domain" and f.get("description", "").lower().startswith("histidine kinase")
    ]
    return seq, hk


def motifs(seq, start, end):
    dom = seq[start - 1 : end]
    half = len(dom) // 2
    hat = dom[half:]  # HATPase_c occupies the C-terminal part of the HK domain
    hat_off = start + half
    out = {}
    for name, pat, region, off in [
        ("H-box", r"H[ED]..[TN]", dom[: half], start),
        ("N-box", r"N..[NHT]A", hat[:60], hat_off),
        ("G1-box", r"D.G.G", hat, hat_off),
        ("G2-box", r"G.G.G", hat, hat_off),
    ]:
        hits = [(m.start() + off, m.group()) for m in re.finditer(f"(?=({pat}))", region)]
        hits = [(p, re.match(pat, region[p - off :]).group()) for p, _ in hits]
        out[name] = hits
    return out


def main():
    data = {k: fetch(a) for k, a in ACCS.items()}
    print("protein\taccession\tlength\tHK_domain\tH-box\tN-box\tG1-box(DxGxG)\tG2-box(GxGxG)")
    for k, (seq, hk) in data.items():
        if not hk:
            print(f"{k}\t{ACCS[k]}\t{len(seq)}\tNO_HK_DOMAIN_FEATURE")
            continue
        s, e = hk[0]
        m = motifs(seq, s, e)
        fmt = lambda h: ",".join(f"{p}:{g}" for p, g in h) or "none"
        print(f"{k}\t{ACCS[k]}\t{len(seq)}\t{s}-{e}\t{fmt(m['H-box'])}\t{fmt(m['N-box'])}\t{fmt(m['G1-box'])}\t{fmt(m['G2-box'])}")

    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    print()
    print("pair\tidentity_over_aligned_columns\taligned_columns")
    for a, b in [("RetS_PSEPK", "RetS_PSEAE"), ("GacS_PSEPK", "GacS_PSEAE"), ("RetS_PSEPK", "GacS_PSEPK")]:
        aln = aligner.align(data[a][0], data[b][0])[0]
        ident = cols = 0
        for (s1, e1), (s2, e2) in zip(*aln.aligned):
            for i, j in zip(range(s1, e1), range(s2, e2)):
                cols += 1
                ident += data[a][0][i] == data[b][0][j]
        print(f"{a} vs {b}\t{ident / cols:.3f}\t{cols}")


if __name__ == "__main__":
    sys.exit(main())
