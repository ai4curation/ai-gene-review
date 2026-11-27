"""Tests on the annotated variant sets (no conclusions encoded here).

1. Patient missense vs gnomAD missense (patient variants excluded from the gnomAD
   set): permutation test on mean family identity, RSA and ligand distance.
2. Spatial clustering of patient missense positions outside the ligand site:
   mean pairwise CA distance vs random position sets of the same size drawn from
   well-modelled residues (pLDDT >= 70).
3. N-terminal presequence descriptors (net charge, acidic residues, hydrophobic
   moment at 100 degrees) for a given window. This is a descriptor table, not a
   targeting predictor; TargetP/MitoFates are not run here.
"""
import argparse
import json
import math
import random
from itertools import combinations
from pathlib import Path

import numpy as np
from Bio import SeqIO
from Bio.PDB import PDBParser

EISENBERG = dict(A=0.62, R=-2.53, N=-0.78, D=-0.90, C=0.29, Q=-0.85, E=-0.74, G=0.48, H=-0.40, I=1.38,
                 L=1.06, K=-1.50, M=0.64, F=1.19, P=0.12, S=-0.18, T=-0.05, W=0.81, Y=0.26, V=1.08)


def perm(a, b, n=20000, seed=1):
    rng = random.Random(seed)
    obs = np.mean(a) - np.mean(b)
    pool = list(a) + list(b)
    hits = 0
    for _ in range(n):
        rng.shuffle(pool)
        if abs(np.mean(pool[:len(a)]) - np.mean(pool[len(a):])) >= abs(obs):
            hits += 1
    return {"mean_a": float(np.mean(a)), "mean_b": float(np.mean(b)), "n_a": len(a), "n_b": len(b),
            "p_two_sided": (hits + 1) / (n + 1)}


def moment(seq, angle=100.0):
    s = sum(EISENBERG[c] * math.sin(math.radians(angle * i)) for i, c in enumerate(seq))
    c = sum(EISENBERG[c] * math.cos(math.radians(angle * i)) for i, c in enumerate(seq))
    return math.hypot(s, c) / len(seq)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="results")
    ap.add_argument("--model", required=True)
    ap.add_argument("--query-fasta", required=True)
    ap.add_argument("--nterm-window", type=int, default=30)
    ap.add_argument("--site-label", default="ligand_site")
    a = ap.parse_args()
    res = Path(a.results)
    lit = json.load(open(res / "literature_variants_annotated.json"))
    gn = json.load(open(res / "gnomad_annotated.json"))
    seq = str(next(SeqIO.parse(a.query_fasta, "fasta")).seq)

    pat = [r for r in lit if r.get("computed", {}).get("type") == "missense"]
    pat_p = {r["computed"]["hgvs_p"] for r in pat}
    pop = [r for r in gn if "structure" in r and r["hgvsp"] not in pat_p and r["structure"]["plddt"] >= 70]
    pat_s = [r for r in pat if r["structure"]["plddt"] >= 70]
    out = {"patient_vs_gnomad_missense_plddt70": {
        k: perm([r["structure"][k] for r in pat_s], [r["structure"][k] for r in pop])
        for k in ("family_identity", "rsa", "min_ligand_distance")}}
    hom = [r for r in pop if r["hom"] > 0]
    out["gnomad_homozygous_missense_plddt70"] = [
        {"p": r["hgvsp"], "ac": r["ac"], "hom": r["hom"], **{k: r["structure"][k] for k in
         ("family_identity", "rsa", "min_ligand_distance", "structural_label")}} for r in hom]

    ca = {r.id[1]: r["CA"].coord for r in PDBParser(QUIET=True).get_structure("m", a.model)[0].get_residues()}
    plddt = {r.id[1]: r["CA"].get_bfactor() for r in
             PDBParser(QUIET=True).get_structure("m", a.model)[0].get_residues()}
    pos = sorted({r["computed"]["pos"] for r in pat_s if r["structure"]["structural_label"] != a.site_label})

    def mpd(ps):
        return float(np.mean([np.linalg.norm(ca[i] - ca[j]) for i, j in combinations(ps, 2)]))

    rng = random.Random(1)
    eligible = [p for p in ca if plddt[p] >= 70]
    null = [mpd(rng.sample(eligible, len(pos))) for _ in range(20000)]
    out["non_site_patient_positions"] = pos
    out["clustering"] = {"mean_pairwise_ca_distance": mpd(pos), "null_mean": float(np.mean(null)),
                         "p_more_clustered": (sum(x <= mpd(pos) for x in null) + 1) / 20001}
    close = [(f"{seq[i-1]}{i}", f"{seq[j-1]}{j}", round(float(np.linalg.norm(ca[i] - ca[j])), 1))
             for i, j in combinations(pos, 2) if np.linalg.norm(ca[i] - ca[j]) <= 8.0]
    out["patient_position_pairs_within_8A_CA"] = close

    w = seq[:a.nterm_window]
    out["nterm_descriptors"] = {
        "window": w, "net_charge": sum(c in "KR" for c in w) - sum(c in "DE" for c in w),
        "n_acidic": sum(c in "DE" for c in w), "n_basic": sum(c in "KR" for c in w),
        "n_ser_thr": sum(c in "ST" for c in w),
        "max_hydrophobic_moment_18mer_100deg": max(moment(w[i:i + 18]) for i in range(len(w) - 17)),
        "mean_plddt": float(np.mean([plddt[i] for i in range(1, a.nterm_window + 1)]))}
    (res / "spatial_tests.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
