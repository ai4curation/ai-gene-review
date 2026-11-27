"""Re-analyse the deposited AlphaFold3 Ghs2-Bgs3 and Sbg1-Bgs1 predictions.

Source: Mendeley Data doi:10.17632/8j46dhsyxr.1 (Willet, Jacob et al. 2026,
PMID:42786154), folders "Figure 3/AF3_Ghs2_Bgs3" and "Figure S3/AF3_Sbg1_Bgs1".

Downloads the AF3 server output (job request, 5 models, summary confidences,
full_data with PAE matrices) into ./data, then reports:
  * job metadata (seed, sequence lengths) and summary confidences per model
  * mean pLDDT per region
  * inter-chain contacts per region pair (heavy atoms < 5 A) with the mean
    inter-chain PAE over contacting residue pairs (both directions)
  * contacts of the specific residues the paper mutated
  * reproducibility of each contact set over the 5 models

Nothing is hardcoded except region boundaries (from UniProt features) and the
residue numbers named in the paper. Run:  uv run python af3_interface_analysis.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from itertools import product
from pathlib import Path

import gemmi
import numpy as np

HERE = Path(__file__).parent
DATA = HERE / "data"
API = "https://data.mendeley.com/public-api/datasets/8j46dhsyxr"
FOLDERS = {
    "ghs2_bgs3": "c033c0f0-0cec-467d-adb1-c8b23e100c90",
    "sbg1_bgs1": "75eb2ba6-4d6a-4372-8af1-41b4fdc14df8",
}
CONTACT_A = 5.0

# Region boundaries (1-based, inclusive). Ghs2 (O13789) and Bgs3 (Q9P377) from
# UniProt TOPO_DOM/TRANSMEM/DOMAIN features. Bgs3 TM helices are ECO:0000255
# predictions; we group them into the two TM clusters flanking the cytosolic
# catalytic (GT48) region.
REGIONS = {
    "ghs2_bgs3": {
        "A": {  # Ghs2
            "Ghs2 N-term cytosolic 1-170": (1, 170),
            "Ghs2 TM 171-191": (171, 191),
            "Ghs2 linker 192-217": (192, 217),
            "Ghs2 GH16 218-587": (218, 587),
            "Ghs2 C-term 588-636": (588, 636),
        },
        "B": {  # Bgs3
            "Bgs3 N-term 1-426": (1, 426),
            "Bgs3 TM1-7 cluster 427-680": (427, 680),
            "Bgs3 central cytosolic (GT48) 681-1271": (681, 1271),
            "Bgs3 TM8-18 cluster 1272-1790": (1272, 1790),
            "Bgs3 C-term 1791-1826": (1791, 1826),
        },
    },
}
NAMED = {
    "ghs2_bgs3": {
        "A": [177, 184, 185, 414, 419, 449, 478],  # Ghs2 TM residues, E414/E419, F449, Y478
        "B": [670, 673, 1224, 1334, 1338, 1341],  # Bgs3 residues named in the paper
    }
}


def curl(url: str, out: Path) -> None:
    if out.exists() and out.stat().st_size > 0:
        return
    subprocess.run(["curl", "-sS", "-L", "--fail", "-o", str(out), url], check=True)


def fetch(job: str) -> list[str]:
    DATA.mkdir(exist_ok=True)
    listing = DATA / f"listing_{job}.json"
    curl(f"{API}/files?folder_id={FOLDERS[job]}&version=1", listing)
    names = []
    for f in json.loads(listing.read_text()):
        n = f["filename"]
        if n.startswith("fold_"):
            curl(f["content_details"]["download_url"], DATA / n)
            names.append(n)
    return sorted(names)


def residue_atoms(structure: gemmi.Structure):
    """Return {chain: {resnum: (resname, coords ndarray, plddt)}}."""
    out = {}
    for ch in structure[0]:
        d = {}
        for r in ch:
            xyz = np.array([[a.pos.x, a.pos.y, a.pos.z] for a in r if a.element.name != "H"])
            d[r.seqid.num] = (r.name, xyz, float(np.mean([a.b_iso for a in r])))
        out[ch.name] = d
    return out


def contacts(res, ca="A", cb="B"):
    a_ids = sorted(res[ca]); b_ids = sorted(res[cb])
    a_cent = np.array([res[ca][i][1].mean(0) for i in a_ids])
    b_cent = np.array([res[cb][i][1].mean(0) for i in b_ids])
    pairs = set()
    dmat = np.linalg.norm(a_cent[:, None, :] - b_cent[None, :, :], axis=2)
    for ia, ib in zip(*np.where(dmat < 20.0)):  # prefilter on centroids
        i, j = a_ids[ia], b_ids[ib]
        xa, xb = res[ca][i][1], res[cb][j][1]
        if np.min(np.linalg.norm(xa[:, None] - xb[None], axis=2)) < CONTACT_A:
            pairs.add((i, j))
    return pairs


def region_of(regions, chain, num):
    for name, (s, e) in regions[chain].items():
        if s <= num <= e:
            return name
    return f"{chain}:other"


def main(job: str = "ghs2_bgs3") -> None:
    names = fetch(job)
    req = json.loads((DATA / f"fold_{job}_job_request.json").read_text())
    req = req[0] if isinstance(req, list) else req
    print(f"# AF3 re-analysis: {job}")
    print(f"job name={req.get('name')} seeds={req.get('modelSeeds')} "
          f"chains={[ (list(s)[0], len(list(s.values())[0]['sequence'])) for s in req['sequences']]}")
    print()
    print("model ranking_score iptm ptm chain_ptm(A,B) pae_min(A->B,B->A) disordered")
    for k in range(5):
        p = DATA / f"fold_{job}_summary_confidences_{k}.json"
        if not p.exists():
            continue
        c = json.loads(p.read_text())
        print(k, c["ranking_score"], c["iptm"], c["ptm"], c["chain_ptm"],
              (c["chain_pair_pae_min"][0][1], c["chain_pair_pae_min"][1][0]), c["fraction_disordered"])
    if job not in REGIONS:
        return
    regions = REGIONS[job]
    print()
    contact_sets = []
    for k in range(5):
        cif = DATA / f"fold_{job}_model_{k}.cif"
        fd = DATA / f"fold_{job}_full_data_{k}.json"
        if not (cif.exists() and fd.exists()):
            print(f"model {k}: missing files, skipped")
            continue
        st = gemmi.read_structure(str(cif))
        res = residue_atoms(st)
        full = json.loads(fd.read_text())
        pae = np.array(full["pae"])
        chains = full["token_chain_ids"]; resnums = full["token_res_ids"]
        tok = {(c, r): i for i, (c, r) in enumerate(zip(chains, resnums))}
        pairs = contacts(res)
        contact_sets.append(pairs)

        if k == 0:
            print("## model_0 mean pLDDT per region")
            for ch in ("A", "B"):
                for name, (s, e) in regions[ch].items():
                    vals = [res[ch][i][2] for i in range(s, e + 1) if i in res[ch]]
                    print(f"  {name}: {np.mean(vals):.1f}")
            print()

        print(f"## model_{k}: {len(pairs)} inter-chain residue contacts (<{CONTACT_A} A heavy atom)")
        by = {}
        for i, j in pairs:
            key = (region_of(regions, "A", i), region_of(regions, "B", j))
            p1 = pae[tok[("A", i)], tok[("B", j)]]; p2 = pae[tok[("B", j)], tok[("A", i)]]
            by.setdefault(key, []).append(((p1 + p2) / 2, res["A"][i][2], res["B"][j][2], i, j))
        for key, v in sorted(by.items(), key=lambda kv: -len(kv[1])):
            arr = np.array([x[:3] for x in v])
            a_res = sorted({x[3] for x in v}); b_res = sorted({x[4] for x in v})
            print(f"  {key[0]}  x  {key[1]}: pairs={len(v)} "
                  f"meanPAE={arr[:,0].mean():.1f} A (min {arr[:,0].min():.1f}) "
                  f"pLDDT A={arr[:,1].mean():.0f} B={arr[:,2].mean():.0f} "
                  f"| Ghs2 {a_res[0]}-{a_res[-1]} ({len(a_res)} res), Bgs3 {b_res[0]}-{b_res[-1]} ({len(b_res)} res)")
        if k == 0:
            print()
            print("## model_0 named residues")
            for ch, other in (("A", "B"), ("B", "A")):
                for n in NAMED[job][ch]:
                    if n not in res[ch]:
                        continue
                    rn, xyz, pl = res[ch][n]
                    part = sorted(j if ch == "A" else i for i, j in pairs if (i if ch == "A" else j) == n)
                    # nearest residue on other chain
                    best = min(((np.min(np.linalg.norm(xyz[:, None] - res[other][m][1][None], axis=2)), m)
                                for m in res[other]), key=lambda t: t[0])
                    pv = [ (pae[tok[(ch, n)], tok[(other, m)]] + pae[tok[(other, m)], tok[(ch, n)]]) / 2 for m in part]
                    print(f"  {'Ghs2' if ch=='A' else 'Bgs3'} {rn}{n} pLDDT={pl:.0f} "
                          f"contacts={[f'{res[other][m][0]}{m}' for m in part]} "
                          f"meanPAE={np.mean(pv):.1f}" if pv else
                          f"  {'Ghs2' if ch=='A' else 'Bgs3'} {rn}{n} pLDDT={pl:.0f} no contact; "
                          f"nearest {res[other][best[1]][0]}{best[1]} at {best[0]:.1f} A")
        print()
    if len(contact_sets) > 1:
        allp = set().union(*contact_sets)
        inall = set.intersection(*contact_sets)
        print(f"## reproducibility: {len(inall)}/{len(allp)} contacting pairs present in all "
              f"{len(contact_sets)} models")
        by = {}
        for i, j in allp:
            key = (region_of(regions, "A", i), region_of(regions, "B", j))
            n = sum((i, j) in s for s in contact_sets)
            by.setdefault(key, []).append(n)
        for key, v in sorted(by.items(), key=lambda kv: -len(kv[1])):
            print(f"  {key[0]} x {key[1]}: {len(v)} pairs, mean models present {np.mean(v):.1f}/{len(contact_sets)}")


if __name__ == "__main__":
    for job in sys.argv[1:] or ["ghs2_bgs3", "sbg1_bgs1"]:
        main(job)
        print("\n")
