# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Sequence architecture of an intermediate filament protein from its UniProt record.

Outputs (prefix results/01_<tag>_): domains.tsv, heptad_register.tsv, architecture.json

Heptad register method (sequence only, no external predictor):
  For each UniProt 'Coil ...' segment a Viterbi path over the seven heptad positions a-g is
  computed. A residue at a or d scores its Kyte-Doolittle hydropathy / 4.5; residues at other
  positions score 0. Moving to the next heptad position is free; any other step (a register
  discontinuity) costs --break-penalty. The path with the best total is reported, together with
  every discontinuity, expressed as the number of residues that would have to be inserted to
  restore a continuous heptad (shift 4 = 'stutter', 3 = 'stammer', 1 = 'skip').
  Limits: purely hydrophobic-periodicity based; ends of segments and short segments are poorly
  determined; it does not model hendecad/parallel-bundle regions. It is cross-checked against
  crystal structures in 05_structure.py.

Usage: uv run 01_architecture.py [--entry data/uniprot_P35527.json] [--tag KRT9]
       (--keratin-gene KRT14 reads the entry from data/human_keratins.json instead)
"""
from __future__ import annotations

import argparse
import math
import re
from collections import Counter
from pathlib import Path

from common import (DATA, HEPTAD, RESULTS, architecture, domain_of, dump_json, gene_name, load_json,
                    seg, write_tsv)

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2,
      "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9,
      "Y": -1.3, "V": 4.2}
SHIFT_NAMES = {4: "stutter (4-residue insertion / 3-residue deletion equivalent)",
               3: "stammer (3-residue insertion / 4-residue deletion equivalent)",
               1: "skip (1-residue insertion equivalent)"}


def viterbi_register(seq: str, break_penalty: float) -> tuple[list[int], float]:
    n = len(seq)
    emit = [[(KD.get(aa, 0.0) / 4.5) if p in (0, 3) else 0.0 for p in range(7)] for aa in seq]
    score = [emit[0][:]]
    back = [[-1] * 7]
    for i in range(1, n):
        row, brow = [], []
        best_prev = max(range(7), key=lambda q: score[-1][q])
        for p in range(7):
            cont = score[-1][(p - 1) % 7]
            jump = score[-1][best_prev] - break_penalty
            if cont >= jump:
                row.append(cont + emit[i][p]); brow.append((p - 1) % 7)
            else:
                row.append(jump + emit[i][p]); brow.append(best_prev)
        score.append(row); back.append(brow)
    p = max(range(7), key=lambda q: score[-1][q])
    total = score[-1][p]
    path = [p]
    for i in range(n - 1, 0, -1):
        p = back[i][p]
        path.append(p)
    return path[::-1], total


def composition(s: str) -> dict:
    c = Counter(s)
    n = len(s)
    ent = -sum((v / n) * math.log2(v / n) for v in c.values()) if n else 0.0
    top = c.most_common(4)
    return {"length": n, "pct_G": 100 * c["G"] / n, "pct_S": 100 * c["S"] / n,
            "pct_G_plus_S": 100 * (c["G"] + c["S"]) / n,
            "pct_aromatic_FYW": 100 * (c["F"] + c["Y"] + c["W"]) / n,
            "pct_charged_DEKR": 100 * sum(c[x] for x in "DEKR") / n,
            "pct_C": 100 * c["C"] / n,
            "shannon_entropy_bits": ent, "top_residues": ",".join(f"{a}:{v}" for a, v in top)}


def glycine_loops(s: str, offset: int) -> dict:
    """Glycine-loop candidates: a non-Gly/Ser anchor residue, a run of >=3 residues that are only
    G/S with at least 2 G, then the next anchor. Counts and anchor residue types are reported."""
    anchors = [m.start() for m in re.finditer(r"[^GS]", s)]
    loops = []
    for a, b in zip(anchors, anchors[1:]):
        run = s[a + 1:b]
        if len(run) >= 3 and run.count("G") >= 2:
            loops.append({"start": a + offset, "end": b + offset, "anchor_n": s[a], "anchor_c": s[b],
                          "loop": run, "loop_length": len(run)})
    return {"n_loops": len(loops),
            "n_loops_between_aromatic_or_aliphatic_anchors":
                sum(1 for l in loops if l["anchor_n"] in "FYWLIVM" and l["anchor_c"] in "FYWLIVM"),
            "anchor_residue_counts": dict(Counter(l["anchor_n"] for l in loops) + Counter(l["anchor_c"] for l in loops)),
            "loop_length_min": min((l["loop_length"] for l in loops), default=0),
            "loop_length_max": max((l["loop_length"] for l in loops), default=0),
            "residues_in_loops": sum(l["loop_length"] for l in loops), "loops": loops}


def top_kmers(s: str, ks=(3, 4, 5, 6, 7, 8), n=5) -> dict:
    out = {}
    for k in ks:
        c = Counter(s[i:i + k] for i in range(len(s) - k + 1))
        out[str(k)] = [{"kmer": m, "count": v} for m, v in c.most_common(n) if v > 1]
    return out


def longest_tandem(s: str, offset: int, max_period: int = 30) -> dict:
    """Best exact tandem repeat (period, copies) by total residues covered."""
    best = {"period": 0, "copies": 0, "start": None, "unit": "", "covered": 0}
    for period in range(2, max_period + 1):
        for i in range(len(s) - 2 * period + 1):
            unit = s[i:i + period]
            if len(set(unit)) == 1:
                continue
            copies = 1
            while s[i + copies * period:i + (copies + 1) * period] == unit:
                copies += 1
            if copies >= 2 and copies * period > best["covered"]:
                best = {"period": period, "copies": copies, "start": i + offset, "unit": unit,
                        "covered": copies * period}
    return best


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entry", default=str(DATA / "uniprot_P35527.json"))
    ap.add_argument("--keratin-gene", default=None)
    ap.add_argument("--interpro", default=str(DATA / "interpro_P35527.json"))
    ap.add_argument("--tag", default="KRT9")
    ap.add_argument("--break-penalty", type=float, default=3.0)
    ap.add_argument("--boundary-window", type=int, default=20,
                    help="residues at the start of coil 1A / end of coil 2 reported as boundary segments")
    a = ap.parse_args()

    if a.keratin_gene:
        entry = next(e for e in load_json(DATA / "human_keratins.json") if gene_name(e) == a.keratin_gene)
        interpro = []
    else:
        entry = load_json(Path(a.entry))
        interpro = load_json(Path(a.interpro)) if Path(a.interpro).exists() else []
    seq = entry["sequence"]["value"]
    arch = architecture(entry)
    pre = RESULTS / f"01_{a.tag}_"

    # --- domains and composition
    dom_rows = []
    for s in arch:
        sub = seq[s["start"] - 1:s["end"]]
        dom_rows.append({"domain": s["name"], "start": s["start"], "end": s["end"], **composition(sub)})
    dom_rows.append({"domain": "full length", "start": 1, "end": len(seq), **composition(seq)})
    write_tsv(dom_rows, Path(str(pre) + "domains.tsv"))

    # --- heptad register per coil segment
    reg: dict[int, str] = {}
    breaks, seg_scores = [], []
    for s in arch:
        if not s["name"].startswith("Coil"):
            continue
        sub = seq[s["start"] - 1:s["end"]]
        path, total = viterbi_register(sub, a.break_penalty)
        for i, p in enumerate(path):
            reg[s["start"] + i] = HEPTAD[p]
        nb = 0
        for i in range(1, len(path)):
            if path[i] != (path[i - 1] + 1) % 7:
                shift = (path[i - 1] + 1 - path[i]) % 7  # residues missing to keep the heptad continuous
                nb += 1
                breaks.append({"segment": s["name"], "after_residue": s["start"] + i - 1,
                               "before_residue": s["start"] + i,
                               "position_before": HEPTAD[path[i - 1]], "position_after": HEPTAD[path[i]],
                               "residues_to_insert_to_restore_heptad": shift,
                               "class": SHIFT_NAMES.get(shift, f"other (shift {shift})"),
                               "residues_from_segment_end": s["end"] - (s["start"] + i - 1),
                               "context": seq[s["start"] + i - 8:s["start"] + i + 6]})
        core = [sub[i] for i, p in enumerate(path) if p in (0, 3)]
        seg_scores.append({"segment": s["name"], "start": s["start"], "end": s["end"], "length": len(sub),
                           "viterbi_score": total, "n_discontinuities": nb,
                           "n_core_positions": len(core),
                           "core_fraction_apolar_LIVMFAYWC": sum(x in "LIVMFAYWC" for x in core) / len(core),
                           "core_residue_counts": dict(Counter(core).most_common())})
    res_rows = []
    for i, aa in enumerate(seq, start=1):
        res_rows.append({"position": i, "residue": aa, "domain": domain_of(i, arch), "heptad": reg.get(i, "")})
    write_tsv(res_rows, Path(str(pre) + "heptad_register.tsv"))

    # --- boundary motifs
    c1a, c2 = seg(arch, "Coil 1A"), seg(arch, "Coil 2")
    w = a.boundary_window
    motifs = {}
    if c1a:
        motifs["helix_initiation_segment"] = {
            "definition": f"first {w} residues of UniProt Coil 1A", "start": c1a["start"],
            "end": c1a["start"] + w - 1, "sequence": seq[c1a["start"] - 1:c1a["start"] + w - 1],
            "heptad": "".join(reg[p] for p in range(c1a["start"], c1a["start"] + w))}
    if c2:
        motifs["helix_termination_segment"] = {
            "definition": f"last {w} residues of UniProt Coil 2", "start": c2["end"] - w + 1,
            "end": c2["end"], "sequence": seq[c2["end"] - w:c2["end"]],
            "heptad": "".join(reg[p] for p in range(c2["end"] - w + 1, c2["end"] + 1))}
    for m in interpro:
        if m["accession"] == "PS00226":
            motifs["prosite_PS00226_IF_rod_signature"] = {
                "start": m["start"], "end": m["end"], "sequence": seq[m["start"] - 1:m["end"]],
                "name": m["name"]}
    for label, pat in (("regex_[ST]YR.LLEGE", r"[ST]YR.LLEGE"), ("regex_TY..LLEG", r"TY..LLEG"),
                       ("regex_LLEG", r"LLEG")):
        motifs[label + "_matches"] = [{"start": m.start() + 1, "end": m.end(), "match": m.group(),
                                       "domain": domain_of(m.start() + 1, arch)}
                                      for m in re.finditer(pat, seq)]

    head, tail = seg(arch, "Head"), seg(arch, "Tail")
    lowc = {}
    for nm, s in (("Head", head), ("Tail", tail)):
        if s:
            sub = seq[s["start"] - 1:s["end"]]
            lowc[nm] = {"glycine_loops": glycine_loops(sub, s["start"]), "top_kmers": top_kmers(sub),
                        "longest_exact_tandem_repeat": longest_tandem(sub, s["start"])}

    dump_json({"accession": entry["primaryAccession"], "gene": gene_name(entry), "length": len(seq),
               "sequence_crc64": entry["sequence"].get("crc64"),
               "parameters": {"break_penalty": a.break_penalty, "boundary_window": w,
                              "core_score": "Kyte-Doolittle/4.5 at a and d"},
               "architecture": arch, "coil_segments": seg_scores, "register_discontinuities": breaks,
               "boundary_motifs": motifs, "low_complexity": lowc,
               "interpro_matches": interpro}, Path(str(pre) + "architecture.json"))
    print(f"wrote {pre}*  ({len(breaks)} register discontinuities)")


if __name__ == "__main__":
    main()
