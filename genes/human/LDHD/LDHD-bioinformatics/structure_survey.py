"""Active-site inventory and isoform-insert context from the mouse LDHD crystal structures.

1. Residues contacting D-lactate, Mn2+ and the FAD isoalloxazine ring in PDB 8JDE
   (wild-type mouse LDHD), translated to human isoform-2 (MANE) and isoform-1 (UniProt
   displayed) numbering, and compared with the UniProt Q86WU2 BINDING/ACT_SITE features.
2. Where the 23-residue isoform-1-only segment (UniProt VAR_SEQ) sits: its flanking
   residues in the crystal structure, its AlphaFold confidence, whether any ortholog has
   aligned residues there, and how close the AlphaFold-modelled segment comes to the FAD
   site after superposing the AlphaFold model on 8JDE.
3. Oligomeric state recorded by the depositors for every mouse LDHD entry.
"""
from __future__ import annotations

import json

import numpy as np
from Bio.PDB import Superimposer
from Bio.PDB.MMCIF2Dict import MMCIF2Dict

import common as c

PDB = "8JDE"
ISOALLOXAZINE = {"N1", "C2", "O2", "N3", "C4", "O4", "C4X", "N5", "C5X", "C6", "C7", "C7M", "C8", "C8M", "C9", "C9A", "N10", "C10"}


def main():
    iso = c.isoforms()
    i2to1 = c.iso2_to_iso1()
    i1to2 = c.iso1_to_iso2()
    mouse = c.orthologs()["mouse"]
    h1_to_m = c.align_map(iso["iso1"], mouse)
    m_to_h1 = {v: k for k, v in h1_to_m.items()}
    model = c.structure(PDB)[0]
    chain = next(ch for ch in model if any(r.id[0] == " " for r in ch))
    het = {}
    for ch in model:
        for r in ch:
            if r.id[0].startswith("H_"):
                het.setdefault(r.get_resname(), []).extend(r.get_atoms())
    fad_ring = [a for a in het["FAD"] if a.get_id() in ISOALLOXAZINE]
    fad_rest = [a for a in het["FAD"] if a.get_id() not in ISOALLOXAZINE]

    def contacts(atoms, cutoff):
        out = {}
        for r in chain:
            if r.id[0] != " ":
                continue
            d = min(float(a - b) for a in r for b in atoms)
            if d <= cutoff:
                out[r.id[1]] = round(d, 2)
        return out

    def label(mpos):
        h1 = m_to_h1.get(mpos)
        res_m = c.THREE[chain[mpos].get_resname()]
        return {"mouse": f"{res_m}{mpos}", "human_iso1": f"{iso['iso1'][h1 - 1]}{h1}" if h1 else None,
                "human_iso2_MANE": f"{iso['iso1'][h1 - 1]}{i1to2[h1]}" if h1 and i1to2[h1] else None}

    site = {
        "D-lactate_within_4A": contacts(het["LAC"], 4.0),
        "Mn_ligands_within_2.6A": contacts(het["MN"], 2.6),
        "FAD_isoalloxazine_within_4A": contacts(fad_ring, 4.0),
        "FAD_other_within_3.5A": contacts(fad_rest, 3.5),
    }
    site_labeled = {k: [dict(label(p), distance_A=d) for p, d in v.items()] for k, v in site.items()}
    # Mn coordination by ligand atoms too
    mn = het["MN"][0]
    site_labeled["Mn_coordination_by_non_protein_atoms"] = [
        {"ligand": a.get_parent().get_resname(), "atom": a.get_id(), "distance_A": round(float(a - mn), 2)}
        for name in het for a in het[name] if a is not mn and float(a - mn) <= 2.6]

    # compare with UniProt human features (isoform-1 numbering)
    feats = []
    for f in c.uniprot_features():
        if f["type"] in ("Binding site", "Active site"):
            p = f["location"]["start"]["value"]
            mp = h1_to_m.get(p)
            lig = f.get("ligand", {}).get("name", f.get("description"))
            atoms = {"FAD": het["FAD"], "Mn(2+)": het["MN"], "(R)-lactate": het["LAC"], "pyruvate": het["LAC"]}.get(lig)
            d = round(min(float(a - b) for a in chain[mp] for b in atoms), 2) if atoms and mp else None
            feats.append({"uniprot_feature": f["type"], "ligand_or_note": lig, "human_iso1": f"{iso['iso1'][p - 1]}{p}",
                          "human_iso2_MANE": i1to2[p], "mouse": f"{mouse[mp - 1]}{mp}" if mp else None, "min_distance_to_that_ligand_in_8JDE_A": d,
                          "residue_identical_human_mouse": bool(mp) and iso["iso1"][p - 1] == mouse[mp - 1]})

    # isoform-1-only segment
    seg = [f for f in c.uniprot_features() if f["type"] == "Alternative sequence"][0]
    a, b = seg["location"]["start"]["value"], seg["location"]["end"]["value"]
    af = c.structure("AF-Q86WU2")[0]["A"]
    seg_plddt = [float(af[i]["CA"].get_bfactor()) for i in range(a, b + 1)]
    # superpose AF (human iso1) onto 8JDE using CA atoms of aligned residues
    fixed, moving = [], []
    for h1, mp in h1_to_m.items():
        if mp in chain and "CA" in chain[mp] and h1 in af:
            fixed.append(chain[mp]["CA"])
            moving.append(af[h1]["CA"])
    sup = Superimposer()
    sup.set_atoms(fixed, moving)
    rot, tran = sup.rotran
    seg_coords = np.array([at.coord for i in range(a, b + 1) for at in af[i]]) @ rot + tran
    fad_coords = np.array([x.coord for x in het["FAD"]])
    lac_coords = np.array([x.coord for x in het["LAC"]])
    dmin = lambda X, Y: float(np.min(np.linalg.norm(X[:, None, :] - Y[None, :, :], axis=2)))
    # nearest aligned residues on either side (the alignment may place the gap a few residues off the VAR_SEQ ends)
    left = next(i for i in range(a - 1, 0, -1) if i in h1_to_m and h1_to_m[i] in chain)
    right = next(i for i in range(b + 1, len(iso["iso1"])) if i in h1_to_m and h1_to_m[i] in chain)
    flank_m = (h1_to_m[left], h1_to_m[right])
    rsa = c.relative_sasa(model)
    orth_seg = {}
    for name, seq in c.orthologs().items():
        if name == "human":
            continue
        m = c.align_map(iso["iso1"], seq)
        orth_seg[name] = {"aligned_residues_in_segment": sum(1 for i in range(a, b + 1) if i in m), "length": len(seq)}
    insert = {
        "segment_iso1": f"{a}-{b}", "sequence": iso["iso1"][a - 1:b],
        "alphafold_pLDDT_mean": round(float(np.mean(seg_plddt)), 1), "alphafold_pLDDT_min": round(min(seg_plddt), 1),
        "alphafold_superposition_rmsd_CA_A": round(float(sup.rms), 2), "n_CA_pairs": len(fixed),
        "segment_min_distance_to_FAD_A_in_superposed_AF_model": round(dmin(seg_coords, fad_coords), 2),
        "segment_min_distance_to_D-lactate_A_in_superposed_AF_model": round(dmin(seg_coords, lac_coords), 2),
        "flanking_human_iso1_residues_used": [left, right],
        "flanking_mouse_residues": [f"{mouse[p - 1]}{p}" for p in flank_m],
        "flank_rel_SASA_in_8JDE": [round(float(rsa[(chain.id, p)]), 2) for p in flank_m],
        "flank_min_distance_to_FAD_A": [round(min(float(x - y) for x in chain[p] for y in het["FAD"]), 2) for p in flank_m],
        "orthologs": orth_seg,
    }

    # deposited assemblies
    asm = {}
    for e in json.loads((c.DATA / "pdb_entries.json").read_text()):
        d = MMCIF2Dict(c.DATA / f"{e['pdb_id']}.cif")
        asm[e["pdb_id"]] = {"title": e["title"], "resolution_A": e["resolution"], "ligands": e["ligands"],
                            "oligomeric_details": d.get("_pdbx_struct_assembly.oligomeric_details"),
                            "assembly_method": d.get("_pdbx_struct_assembly.method_details")}

    out = {"pdb": PDB, "active_site": site_labeled, "uniprot_human_features_checked_on_structure": feats,
           "isoform1_only_segment": insert, "deposited_assemblies": asm,
           "observed_residue_range_8JDE": [min(r.id[1] for r in chain if r.id[0] == " "), max(r.id[1] for r in chain if r.id[0] == " ")]}
    (c.RESULTS / "structure_survey.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
