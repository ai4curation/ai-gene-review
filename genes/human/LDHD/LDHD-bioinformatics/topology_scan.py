"""Is there a stop-transfer (membrane-anchor) segment after the presequence?

Kyte-Doolittle hydropathy (19-residue window) over the N-terminal 120 residues of human,
mouse and zebrafish LDHD, yeast Dld1 and Arabidopsis D-LDH, plus net charge of the first
30 residues. A window mean >= 1.6 is the classical Kyte-Doolittle threshold for a
membrane-spanning helix. This is a coarse sequence heuristic, not a topology prediction;
it only asks whether animal LDHD has anything like a hydrophobic anchor near the N-terminus.
"""
import json

import common as c

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}
W = 19


def scan(seq, upto):
    best = (-9, 0)
    for i in range(0, min(upto, len(seq)) - W + 1):
        m = sum(KD[a] for a in seq[i:i + W]) / W
        best = max(best, (m, i + 1))
    return best


def main():
    out = {}
    for name, seq in c.orthologs().items():
        m, start = scan(seq, 120)
        whole, wstart = scan(seq, len(seq))
        n30 = seq[:30]
        out[name] = {"length": len(seq), "max_KD_19mer_in_first_120": round(m, 2), "window": f"{start}-{start + W - 1}", "window_seq": seq[start - 1:start + W - 1],
                     "passes_1.6_threshold": m >= 1.6, "max_KD_19mer_whole_protein": round(whole, 2), "whole_window": f"{wstart}-{wstart + W - 1}",
                     "first30_net_charge": sum(a in "KR" for a in n30) - sum(a in "DE" for a in n30), "first30_acidic": sum(a in "DE" for a in n30)}
    (c.RESULTS / "topology_scan.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
