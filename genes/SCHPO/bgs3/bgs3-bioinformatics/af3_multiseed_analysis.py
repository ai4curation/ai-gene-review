"""Aggregate AlphaFold3 (AlphaFold Server) runs of Ghs2 with a partner synthase.

Usage:
    uv run python af3_multiseed_analysis.py DIR [DIR ...]

Each DIR is searched recursively for AF Server output (unzipped):
fold_<job>_model_<k>.cif, fold_<job>_full_data_<k>.json and
fold_<job>_summary_confidences_<k>.json. Only jobs whose chain A is Ghs2
(O13789; sequence taken from af_server_jobs/ghs2_bgs3_multiseed.json, produced
by make_af_server_jobs.py) are analysed. Chain B is the partner.

Per model it reports:
  * iptm and ranking_score
  * for each Ghs2 region: number of inter-chain contacts (heavy atoms < 5 A)
    and mean inter-chain PAE over them (both directions averaged)
  * GH16 block PAE: median inter-chain PAE between confident (pLDDT > 70)
    GH16 residues and confident partner residues, irrespective of contact
  * for partner == Bgs3 only: placement of the GH16 domain and of the Ghs2 TM
    helix after superposing the model's Bgs3 (confident CA atoms) onto a
    reference model (the authors' deposited model_0 by default): RMSD of the
    GH16 / TM CA atoms without refitting, and GH16 centroid displacement.

Per job and overall it summarises these values. No numbers are hardcoded.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics as st
from collections import defaultdict
from pathlib import Path

import gemmi
import numpy as np

HERE = Path(__file__).parent
CONTACT_A = 5.0
GHS2_REGIONS = {  # UniProt O13789 features
    "Nterm 1-170": (1, 170),
    "TM 171-191": (171, 191),
    "linker 192-217": (192, 217),
    "GH16 218-587": (218, 587),
    "Cterm 588-636": (588, 636),
}
GH16 = GHS2_REGIONS["GH16 218-587"]
TM = GHS2_REGIONS["TM 171-191"]


def ref_seqs() -> dict[str, str]:
    jobs = json.loads((HERE / "af_server_jobs" / "ghs2_bgs3_multiseed.json").read_text())
    s = [x["proteinChain"]["sequence"] for x in jobs[0]["sequences"]]
    return {"Ghs2": s[0], "Bgs3": s[1]}


def load_model(cif: Path):
    stc = gemmi.read_structure(str(cif))
    chains = {}
    for ch in stc[0]:
        res = {}
        for r in ch:
            heavy = np.array([[a.pos.x, a.pos.y, a.pos.z] for a in r if a.element.name != "H"])
            ca = r.find_atom("CA", "*")
            res[r.seqid.num] = {
                "name": r.name,
                "xyz": heavy,
                "ca": np.array([ca.pos.x, ca.pos.y, ca.pos.z]) if ca else heavy.mean(0),
                "plddt": float(np.mean([a.b_iso for a in r])),
            }
        seq = gemmi.one_letter_code([r.name for r in ch])
        chains[ch.name] = (seq, res)
    return chains


def kabsch(P: np.ndarray, Q: np.ndarray):
    """Rotation R and translation t minimising |(P @ R.T + t) - Q|."""
    pc, qc = P.mean(0), Q.mean(0)
    H = (P - pc).T @ (Q - qc)
    U, _, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1, 1, d])
    R = Vt.T @ D @ U.T
    return R, qc - pc @ R.T


def contacts(A: dict, B: dict) -> set[tuple[int, int]]:
    a_ids, b_ids = sorted(A), sorted(B)
    ac = np.array([A[i]["xyz"].mean(0) for i in a_ids])
    bc = np.array([B[j]["xyz"].mean(0) for j in b_ids])
    d = np.linalg.norm(ac[:, None] - bc[None], axis=2)
    out = set()
    for ia, jb in zip(*np.where(d < 20.0)):
        i, j = a_ids[ia], b_ids[jb]
        if np.min(np.linalg.norm(A[i]["xyz"][:, None] - B[j]["xyz"][None], axis=2)) < CONTACT_A:
            out.add((i, j))
    return out


def region(n: int) -> str:
    for k, (s, e) in GHS2_REGIONS.items():
        if s <= n <= e:
            return k
    return "other"


def find_models(dirs: list[Path]):
    pat = re.compile(r"(.*)_summary_confidences_(\d+)\.json$")
    for d in dirs:
        for sc in sorted(d.rglob("*_summary_confidences_*.json")):
            m = pat.match(sc.name)
            if not m:
                continue
            stem, k = m.group(1), m.group(2)
            cif = sc.with_name(f"{stem}_model_{k}.cif")
            fd = sc.with_name(f"{stem}_full_data_{k}.json")
            if cif.exists() and fd.exists():
                yield stem, int(k), sc, cif, fd


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+", type=Path)
    ap.add_argument("--reference", type=Path, default=HERE / "data" / "fold_ghs2_bgs3_model_0.cif",
                    help="model whose Bgs3 frame defines GH16/TM placement (default: deposited model_0)")
    args = ap.parse_args()
    seqs = ref_seqs()

    ref = load_model(args.reference)
    ref_A, ref_B = ref["A"][1], ref["B"][1]

    rows = []
    for stem, k, sc, cif, fd in find_models(args.dirs):
        ch = load_model(cif)
        if ch["A"][0] != seqs["Ghs2"]:
            continue
        partner = "Bgs3" if ch["B"][0] == seqs["Bgs3"] else f"other(len {len(ch['B'][0])})"
        A, B = ch["A"][1], ch["B"][1]
        conf = json.loads(sc.read_text())
        full = json.loads(fd.read_text())
        pae = np.array(full["pae"])
        tok = {(c, r): i for i, (c, r) in enumerate(zip(full["token_chain_ids"], full["token_res_ids"]))}

        def ppae(i, j):
            return (pae[tok[("A", i)], tok[("B", j)]] + pae[tok[("B", j)], tok[("A", i)]]) / 2

        cs = contacts(A, B)
        reg = defaultdict(list)
        for i, j in cs:
            reg[region(i)].append(ppae(i, j))
        gh_conf = [i for i in range(GH16[0], GH16[1] + 1) if A[i]["plddt"] > 70]
        b_conf = [j for j in B if B[j]["plddt"] > 70]
        ia = np.array([tok[("A", i)] for i in gh_conf]); jb = np.array([tok[("B", j)] for j in b_conf])
        gh_block = float(np.median((pae[np.ix_(ia, jb)] + pae[np.ix_(jb, ia)].T) / 2))

        row = {"job": stem, "model": k, "partner": partner, "iptm": conf["iptm"],
               "ranking": conf["ranking_score"], "gh16_block_pae": gh_block,
               "contacts": {r: (len(v), float(np.mean(v))) for r, v in reg.items()}}
        if partner == "Bgs3":
            common = [j for j in B if j in ref_B and B[j]["plddt"] > 70 and ref_B[j]["plddt"] > 70]
            R, t = kabsch(np.array([B[j]["ca"] for j in common]), np.array([ref_B[j]["ca"] for j in common]))

            def placed(rng):
                ids = [i for i in range(rng[0], rng[1] + 1) if i in A and i in ref_A]
                P = np.array([A[i]["ca"] for i in ids]) @ R.T + t
                Q = np.array([ref_A[i]["ca"] for i in ids])
                return float(np.sqrt(((P - Q) ** 2).sum(1).mean())), float(np.linalg.norm(P.mean(0) - Q.mean(0)))

            row["gh16_rmsd"], row["gh16_centroid_shift"] = placed(GH16)
            row["tm_rmsd"], _ = placed(TM)
            row["bgs3_fit_atoms"] = len(common)
        rows.append(row)

    if not rows:
        print("no Ghs2-containing AF3 models found")
        return
    print(f"reference frame: {args.reference}\n")
    hdr = "job model partner iptm ranking GH16blockPAE | contacts(n, meanPAE) by Ghs2 region | GH16 RMSD / centroid shift / TM RMSD vs ref"
    print(hdr)
    for r in rows:
        c = "; ".join(f"{k}: {n}, {p:.1f}" for k, (n, p) in sorted(r["contacts"].items()))
        place = (f"{r['gh16_rmsd']:.1f} / {r['gh16_centroid_shift']:.1f} / {r['tm_rmsd']:.1f} A"
                 if "gh16_rmsd" in r else "-")
        print(f"{r['job']} {r['model']} {r['partner']} {r['iptm']:.2f} {r['ranking']:.2f} "
              f"{r['gh16_block_pae']:.1f} | {c} | {place}")

    print("\n# summary by job (median over models)")
    by = defaultdict(list)
    for r in rows:
        by[r["job"]].append(r)
    for job, rs in by.items():
        def med(key):
            v = [x[key] for x in rs if key in x]
            return f"{st.median(v):.2f}" if v else "-"
        tm = [x["contacts"].get("TM 171-191", (0, float("nan"))) for x in rs]
        print(f"{job} partner={rs[0]['partner']} n={len(rs)} iptm={med('iptm')} "
              f"GH16blockPAE={med('gh16_block_pae')} TMcontacts={st.median(n for n, _ in tm)} "
              f"TMcontactPAE={st.median(p for _, p in tm):.2f} GH16rmsd={med('gh16_rmsd')} "
              f"GH16shift={med('gh16_centroid_shift')} TMrmsd={med('tm_rmsd')}")
    b3 = [r for r in rows if "gh16_rmsd" in r]
    if b3:
        print(f"\n# Ghs2-Bgs3 placement over all {len(b3)} models: GH16 centroid shift "
              f"median {st.median(r['gh16_centroid_shift'] for r in b3):.1f} A, "
              f"max {max(r['gh16_centroid_shift'] for r in b3):.1f} A; TM RMSD median "
              f"{st.median(r['tm_rmsd'] for r in b3):.1f} A")


if __name__ == "__main__":
    main()
