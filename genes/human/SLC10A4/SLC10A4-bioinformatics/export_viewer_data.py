"""Export superposed coordinates + the site table as a JS payload for a web viewer.

Writes one `data.js` defining `window.SLC10`, holding:

* `pdb.ntcp`   -- the experimental NTCP chain from 7ZYI, with its bound Na+ ions
                  and glycochenodeoxycholate kept and cholesterol/water dropped.
* `pdb.a4`     -- the AlphaFold model of SLC10A4, rotated onto that chain.
* `pdb.a7`     -- the AlphaFold model of SLC10A7, rotated onto that chain.
* `sites`      -- the site definitions and the per-paralogue residue table, read
                  back from pocket_conservation.json so the page cannot drift
                  from the analysis.

The superposition reuses the TM-align transform from pocket_conservation.py,
applied in the direction that module verified empirically (chain 1 onto chain 2,
then inverted here so the models move and the experimental chain stays put).

Usage:
    uv run python export_viewer_data.py --out /path/to/data.js
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import gemmi
import numpy as np
from tmtools import tm_align

import pocket_conservation as pc

HERE = Path(__file__).parent
STRUCT = HERE / "structures"

# Ligands worth keeping in the viewer: the sodium ions and the bile salt.
# Cholesterol (CLR) is annular lipid and water is noise.
KEEP_LIGANDS = {"NA", "CHO"}


def ntcp_reference() -> tuple[gemmi.Structure, str]:
    """7ZYI with only the NTCP chain and the two functional ligand types."""
    st = gemmi.read_structure(str(STRUCT / "7ZYI.cif"))
    st.setup_entities()
    st.remove_alternative_conformations()
    st.remove_hydrogens()
    ntcp_seq = pc.uniprot_sequence("Q14973")
    chain = pc.find_ntcp_chain(st, ntcp_seq)
    model = st[0]
    for ch in list(model):
        if ch.name != chain.label:
            model.remove_chain(ch.name)
    # Drop the ligands we do not want to show.
    ch = model[0]
    for i in range(len(ch) - 1, -1, -1):
        name = ch[i].name
        if name not in pc.AA3to1 and name not in KEEP_LIGANDS:
            del ch[i]
    return st, chain.label


def model_chain(accession: str) -> gemmi.Structure:
    st = gemmi.read_structure(str(STRUCT / f"AF-{accession}.pdb"))
    st.setup_entities()
    st.remove_hydrogens()
    return st


def superpose(target: gemmi.Structure, ref: pc.Chain) -> None:
    """Rotate `target` in place onto the frame of the experimental NTCP chain."""
    chains = pc.protein_chains(target)
    tgt = chains[0][1]
    res = tm_align(ref.coords, tgt.coords, ref.seq, tgt.seq)
    # pocket_conservation verified that (ref @ u.T + t) lands in the target's
    # frame. The inverse moves the target into the reference frame:
    #   x_ref = (x_tgt - t) @ u
    u, t = res.u, res.t
    for ch in target[0]:
        for residue in ch:
            for atom in residue:
                v = np.array([atom.pos.x, atom.pos.y, atom.pos.z])
                w = (v - t) @ u
                atom.pos = gemmi.Position(*w)
    print(f"    TM={res.tm_norm_chain1:.3f} RMSD={res.rmsd:.2f}")


def to_pdb_string(st: gemmi.Structure) -> str:
    st.setup_entities()
    return st.make_pdb_string()


NA_SITE_MAP = {
    # NTCP anchor position -> aligned position, from pocket_conservation.json
    "a4": {68: 146, 105: 183, 106: 184, 119: 197, 123: 201, 257: 335, 261: 339},
    "a7": {68: 80, 105: 120, 106: 121, 119: 135, 123: 139, 257: 263, 261: 267},
}
BACKBONE = {"N", "CA", "C", "O", "OXT"}


def _parse_atoms(pdb: str) -> list[tuple[str, int, str, np.ndarray]]:
    out = []
    for line in pdb.splitlines():
        if line.startswith(("ATOM", "HETATM")):
            out.append((
                line[17:20].strip(), int(line[22:26]), line[12:16].strip(),
                np.array([float(line[30:38]), float(line[38:46]), float(line[46:54])]),
            ))
    return out


def measure_geometry(pdbs: dict[str, str]) -> dict:
    """Per-position CA-CA offset and side-chain distance to the nearest Na+."""
    parsed = {k: _parse_atoms(v) for k, v in pdbs.items()}
    na = [a[3] for a in parsed["ntcp"] if a[0] == "NA"]

    def side_chain_to_na(atoms, pos):
        sel = [a[3] for a in atoms if a[1] == pos and a[2] not in BACKBONE]
        if not sel or not na:
            return None
        return round(float(min(np.linalg.norm(s - i) for s in sel for i in na)), 2)

    def ca(atoms, pos):
        hit = [a[3] for a in atoms if a[1] == pos and a[2] == "CA"]
        return hit[0] if hit else None

    out: dict[str, dict] = {"anchor": {}, "a4": {}, "a7": {}}
    for anchor_pos in sorted(NA_SITE_MAP["a4"]):
        out["anchor"][str(anchor_pos)] = side_chain_to_na(parsed["ntcp"], anchor_pos)
        for key in ("a4", "a7"):
            tgt = NA_SITE_MAP[key][anchor_pos]
            ca_ref, ca_tgt = ca(parsed["ntcp"], anchor_pos), ca(parsed[key], tgt)
            offset = (
                round(float(np.linalg.norm(ca_ref - ca_tgt)), 2)
                if ca_ref is not None and ca_tgt is not None
                else None
            )
            out[key][str(anchor_pos)] = {
                "target_position": tgt,
                "ca_offset": offset,
                "side_chain_to_na": side_chain_to_na(parsed[key], tgt),
            }
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    print("Reference: 7ZYI NTCP chain with Na+ and glycochenodeoxycholate")
    ref_st, ref_label = ntcp_reference()
    ref_chain = [c for n, c in pc.protein_chains(ref_st) if n == ref_label][0]
    n_lig = sum(
        1 for ch in ref_st[0] for r in ch if r.name in KEEP_LIGANDS
    )
    print(f"  kept {len(ref_chain.seq)} residues and {n_lig} ligand copies")

    payload: dict[str, object] = {"pdb": {}, "sites": {}}
    payload["pdb"]["ntcp"] = to_pdb_string(ref_st)

    for key, acc in [("a4", "Q96EP9"), ("a7", "Q0GE19")]:
        print(f"  superposing AlphaFold model {acc}")
        st = model_chain(acc)
        superpose(st, ref_chain)
        payload["pdb"][key] = to_pdb_string(st)

    # Geometry for the viewer's per-position trust column: how far each
    # paralogue's aligned residue sits from its NTCP counterpart (CA-CA) and
    # from the nearest bound Na+. A large CA-CA offset means the alignment
    # register is unreliable there, which the page must say rather than
    # reporting the ion distance as if it were a finding.
    print("  measuring per-position geometry")
    payload["geometry"] = measure_geometry(payload["pdb"])

    analysis = json.loads((HERE / "pocket_conservation.json").read_text())
    payload["sites"] = {
        "cutoff": analysis["cutoff_angstrom"],
        "definitions": analysis["sites"],
        "conservation": analysis["conservation"],
    }

    js = "window.SLC10 = " + json.dumps(payload) + ";\n"
    args.out.write_text(js)
    size_mb = len(js) / 1e6
    print(f"\nWrote {args.out} ({size_mb:.2f} MB)")
    if size_mb > 12:
        print("WARNING: approaching the 16 MB artifact limit")


if __name__ == "__main__":
    main()
