#!/usr/bin/env python3
"""Compare the predicted COX2 CuA site against experimental PDB structures.

Sanity check for the ESMFold2 metal-aware runs: the 3-Cu holo prediction
(``cox2_sco1_model_a_cu_out``) reconstructed a binuclear CuA centre unforced.
This script pulls the real CuA geometry from experimental human cytochrome c
oxidase structures and compares the metal-site geometry quantitatively.

CuA is a *binuclear* mixed-valence copper centre bridged by two cysteine
thiolates (plus 2 His, 1 Met, 1 backbone carbonyl). CuB (in COX1) is a *single*
copper with His-only ligation, so we identify CuA as the copper(s) coordinated
by a cysteine SG and ignore CuB.

Nothing is hardcoded: experimental structures are downloaded from RCSB and
measured at runtime. Resolution caveats apply (cryo-EM metal-metal distances are
not atomic-resolution accurate); the topology comparison is the robust readout.

Usage:
    python3 validate_cua_vs_pdb.py            # default: 9I6F, 5Z62 vs prediction
    python3 validate_cua_vs_pdb.py 9I6F       # specific PDB id(s)
"""

from __future__ import annotations

import math
import sys
import urllib.request
from pathlib import Path

from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.Structure import Structure

ROOT = Path(__file__).resolve().parent
PRED_CIF = ROOT / "cox2_sco1_model_a_cu_out" / "esmfold2_model_0.cif"
DEFAULT_PDB_IDS = ["9I6F", "5Z62"]
LIG_RADIUS = 3.0   # copper coordination shell (A); generous for cryo-EM
PAIR_RADIUS = 4.0  # max Cu-Cu separation to call a binuclear pair (A)


def dist(a, b) -> float:
    return math.dist(a.coord, b.coord)


def fetch_cif(pdb_id: str) -> Path:
    out = Path("/tmp") / f"{pdb_id}.cif"
    if not out.exists():
        url = f"https://files.rcsb.org/download/{pdb_id}.cif"
        urllib.request.urlretrieve(url, out)
    return out


def load(path: Path, name: str) -> Structure:
    return MMCIFParser(QUIET=True).get_structure(name, str(path))


def copper_ligands(cu, ns: NeighborSearch):
    """Coordinating atoms (S/N/O) within LIG_RADIUS of a copper."""
    ligs = []
    for n in ns.search(cu.coord, LIG_RADIUS):
        if n is cu or n.element not in ("S", "N", "O"):
            continue
        res = n.parent
        ligs.append(
            {
                "res": res.resname,
                "chain": res.parent.id,
                "resnum": res.id[1],
                "atom": n.name,
                "d": round(dist(cu, n), 2),
            }
        )
    return sorted(ligs, key=lambda x: x["d"])


def cua_report(structure: Structure, label: str) -> None:
    model = next(structure.get_models())
    atoms = list(model.get_atoms())
    ns = NeighborSearch(atoms)
    coppers = [a for a in atoms if a.element == "CU"]

    cua = []  # coppers with at least one cysteine-SG ligand
    for cu in coppers:
        ligs = copper_ligands(cu, ns)
        if any(l["res"] == "CYS" and l["atom"] == "SG" for l in ligs):
            cua.append((cu, ligs))

    print(f"\n=== {label} ===")
    print(f"total Cu atoms: {len(coppers)}; Cu with Cys-SG ligand (CuA-type): {len(cua)}")
    if not cua:
        print("  no cysteine-ligated copper found")
        return

    # binuclear pair: two CuA coppers within PAIR_RADIUS
    for i in range(len(cua)):
        for j in range(i + 1, len(cua)):
            d = dist(cua[i][0], cua[j][0])
            if d <= PAIR_RADIUS:
                print(f"  binuclear CuA: Cu-Cu = {d:.2f} A")

    for cu, ligs in cua:
        ch = cu.parent.parent.id
        cys = [l for l in ligs if l["res"] == "CYS" and l["atom"] == "SG"]
        his = [l for l in ligs if l["res"] == "HIS"]
        met = [l for l in ligs if l["res"] == "MET"]
        print(f"  Cu (chain {ch}):")
        print(f"    Cys-SG: {[(l['chain']+str(l['resnum']), l['d']) for l in cys]}")
        if his:
            print(f"    His-N : {[(l['chain']+str(l['resnum'])+'/'+l['atom'], l['d']) for l in his]}")
        if met:
            print(f"    Met-S : {[(l['chain']+str(l['resnum']), l['d']) for l in met]}")

    # bridging cysteines: SG-SG distance between the two cysteines shared by CuA
    sgs = []
    seen = set()
    for cu, ligs in cua:
        for l in ligs:
            if l["res"] == "CYS" and l["atom"] == "SG":
                key = (l["chain"], l["resnum"])
                if key not in seen:
                    seen.add(key)
                    # find the actual atom object
                    for n in ns.search(cu.coord, LIG_RADIUS):
                        if (n.parent.resname == "CYS" and n.name == "SG"
                                and n.parent.parent.id == l["chain"]
                                and n.parent.id[1] == l["resnum"]):
                            sgs.append(n)
                            break
    if len(sgs) >= 2:
        pairs = [
            (sgs[i], sgs[j], dist(sgs[i], sgs[j]))
            for i in range(len(sgs)) for j in range(i + 1, len(sgs))
        ]
        d = min(p[2] for p in pairs)
        print(f"  bridging Cys SG-SG (min): {d:.2f} A")


def main() -> int:
    pdb_ids = sys.argv[1:] or DEFAULT_PDB_IDS
    for pid in pdb_ids:
        cif = fetch_cif(pid)
        cua_report(load(cif, pid), f"EXPERIMENTAL {pid}")

    if PRED_CIF.exists():
        cua_report(load(PRED_CIF, "pred"), f"PREDICTED {PRED_CIF.parent.name} (ESMFold2 3-Cu)")
    else:
        print(f"\n(prediction CIF not found at {PRED_CIF})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
