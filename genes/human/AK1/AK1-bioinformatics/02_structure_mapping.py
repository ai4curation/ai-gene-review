"""Place every residue of AK1 (and each reported variant) on experimental structures.

Structures: 1Z83 (human AK1 + Ap5A, 1.90 A), 2C95 (human AK1 + Ap4A, 1.71 A),
7X7S (apo wild type, NMR), 8X1G (R97W, NMR), 7DE3 (R128W, 2.20 A) and the AlphaFold model. For each residue
the script computes, from coordinates: the minimum heavy-atom distance to the
bisubstrate inhibitor, which nucleotide half and which chemical group it faces,
side-chain polar partners, relative solvent accessibility, and domain. It also
compares inter-domain geometry and local contacts in the two variant structures
with the apo and inhibitor-bound wild type. Residues are mapped to UniProt
positions by sequence alignment, because 7X7S is numbered with a 5-residue tag.
"""
from __future__ import annotations

import csv
import io
import json
import re
import warnings

import numpy as np
from Bio.PDB import PDBParser, ShrakeRupley, Superimposer
from Bio.PDB.PDBExceptions import PDBConstructionWarning
from Bio.PDB.Polypeptide import protein_letters_3to1

from ak1_common import dump, fetch, uniprot_features, uniprot_sequence, UNIPROT

warnings.simplefilter("ignore", PDBConstructionWarning)

# Tien et al. 2013 theoretical maximum ASA (A^2)
MAX_ASA = {"A": 129, "R": 274, "N": 195, "D": 193, "C": 167, "E": 223, "Q": 225, "G": 104,
           "H": 224, "I": 197, "L": 201, "K": 236, "M": 224, "F": 240, "P": 159, "S": 155,
           "T": 172, "W": 285, "Y": 263, "V": 174}
# side-chain volumes (A^3, Zamyatnin 1972) and formal charge at pH 7
VOLUME = {"G": 60.1, "A": 88.6, "S": 89.0, "C": 108.5, "D": 111.1, "P": 112.7, "N": 114.1,
          "T": 116.1, "E": 138.4, "V": 140.0, "Q": 143.8, "H": 153.2, "M": 162.9, "I": 166.7,
          "L": 166.7, "K": 168.6, "R": 173.4, "F": 189.9, "Y": 193.6, "W": 227.8}
CHARGE = {"D": -1, "E": -1, "K": 1, "R": 1}


def load(pdb_id: str):
    path = fetch(f"https://files.rcsb.org/download/{pdb_id}.pdb", f"{pdb_id}.pdb")
    return PDBParser(QUIET=True).get_structure(pdb_id, str(path))[0]


def protein_residues(chain):
    return {r.id[1]: r for r in chain if r.id[0] == " " and r.resname in protein_letters_3to1}


def ligand_atoms(model, chain_id: str, resname: str):
    out = []
    for r in model[chain_id]:
        if r.resname.strip() == resname:
            out.extend(a for a in r if a.element != "H")
    return out


BASE = re.compile(r"^(N9|C8|N7|C5|C6|N6|N1|C2|N3|C4)([AB])$")


def classify_ligand(lig) -> dict:
    """Group (phosphate / ribose / adenine) and adenosine half of each ligand atom.

    Phosphate = P atoms and oxygens bonded to P (within 1.75 A); adenine = purine ring
    atoms by name; the rest is ribose, assigned to the adenosine whose N9 is nearest.
    """
    P = np.array([a.coord for a in lig if a.element == "P"])
    n9 = {m.group(2): a.coord for a in lig if (m := BASE.match(a.get_id())) and m.group(1) == "N9"}
    out = {}
    for a in lig:
        name = a.get_id()
        m = BASE.match(name)
        if a.element == "P" or (a.element == "O" and np.min(np.linalg.norm(P - a.coord, axis=1)) < 1.75):
            out[name] = ("phosphate", None)
        elif m:
            out[name] = ("adenine", m.group(2))
        else:
            half = min(n9, key=lambda k: np.linalg.norm(n9[k] - a.coord))
            out[name] = ("ribose", half)
    return out


def analyse(pdb_id: str, chain_id: str, lig_name: str, seq: str, feats: list[dict]) -> dict:
    model = load(pdb_id)
    chain = model[chain_id]
    residues = protein_residues(chain)
    # numbering check against UniProt
    mism = [(i, protein_letters_3to1[r.resname], seq[i - 1]) for i, r in residues.items()
            if 1 <= i <= len(seq) and protein_letters_3to1[r.resname] != seq[i - 1]]
    lig = ligand_atoms(model, chain_id, lig_name)
    lig_xyz = np.array([a.coord for a in lig])
    # split the dinucleotide into its two adenosines by atom-name suffix and decide which
    # sits in the ATP site by proximity to the P-loop (UniProt ATP binding 18-23)
    ploop = np.array([a.coord for i in range(18, 24) for a in residues[i]])
    lig_class = classify_ligand(lig)
    halves: dict[str, list] = {}
    for a in lig:
        group, half = lig_class[a.get_id()]
        if group == "adenine":
            halves.setdefault(half, []).append(a)

    def dmin(atoms):
        xyz = np.array([a.coord for a in atoms])
        return float(np.min(np.linalg.norm(xyz[:, None, :] - ploop[None, :, :], axis=2)))
    half_site = {}
    if len(halves) == 2:
        k = sorted(halves, key=lambda h: dmin(halves[h]))
        half_site = {k[0]: "ATP-site adenosine", k[1]: "AMP-site adenosine"}

    # SASA on the protein chain alone (ligands and other chains removed)
    for other in [c.id for c in model if c.id != chain_id]:
        model.detach_child(other)
    for r in list(chain):
        if r.id[0] != " ":
            chain.detach_child(r.id)
    ShrakeRupley().compute(model, level="R")

    def domain(i: int) -> str:
        for f in feats:
            if f["type"] == "REGION" and f["start"] <= i <= f["end"]:
                return f["note"] + " domain"
        return "CORE domain"

    per_res = {}
    all_atoms = [(i, a) for i, r in residues.items() for a in r if a.element != "H"]
    xyz_all = np.array([a.coord for _, a in all_atoms])
    for i, r in residues.items():
        aa = protein_letters_3to1[r.resname]
        atoms = [a for a in r if a.element != "H"]
        xyz = np.array([a.coord for a in atoms])
        d = np.linalg.norm(xyz[:, None, :] - lig_xyz[None, :, :], axis=2)
        ai, li = np.unravel_index(np.argmin(d), d.shape)
        la = lig[li]
        group, half = lig_class[la.get_id()]
        which = half_site.get(half) if half else None
        # side-chain polar partners (N/O within 3.5 A of a side-chain N/O/S, not i +/- 1)
        partners = set()
        sc = [a for a in atoms if a.get_id() not in ("N", "CA", "C", "O") and a.element in "NOS"]
        for a in sc:
            dd = np.linalg.norm(xyz_all - a.coord, axis=1)
            for idx in np.where(dd < 3.5)[0]:
                j, b = all_atoms[idx]
                if abs(j - i) > 1 and b.element in "NO":
                    partners.add(f"{protein_letters_3to1[residues[j].resname]}{j}:{b.get_id()}")
            dl = np.linalg.norm(lig_xyz - a.coord, axis=1)
            for idx in np.where(dl < 3.5)[0]:
                if lig[idx].element in "NO":
                    partners.add(f"{lig_name}:{lig[idx].get_id()}")
        # neighbours: residues with any heavy atom within 4 A
        dn = np.linalg.norm(xyz_all[:, None, :] - xyz[None, :, :], axis=2).min(axis=1)
        neigh = sorted({j for (j, _), dist in zip(all_atoms, dn) if dist < 4.0 and abs(j - i) > 1})
        per_res[i] = {
            "aa": aa,
            "domain": domain(i),
            "min_dist_to_ligand_A": round(float(d.min()), 2),
            "closest_protein_atom": atoms[ai].get_id(),
            "closest_ligand_atom": la.get_id(),
            "closest_ligand_group": group,
            "closest_ligand_half": which,
            "relative_sasa": round(r.sasa / MAX_ASA[aa], 2),
            "sidechain_polar_partners": sorted(partners),
            "n_neighbour_residues_4A": len(neigh),
            "mean_bfactor": round(float(np.mean([a.bfactor for a in atoms])), 1),
        }
    return {"pdb": pdb_id, "chain": chain_id, "ligand": lig_name,
            "n_residues_modelled": len(residues),
            "numbering_mismatches_vs_uniprot": mism,
            "ligand_half_assignment": half_site,
            "residues": per_res}


def alphafold(seq: str) -> dict:
    meta = json.loads(fetch(f"https://alphafold.ebi.ac.uk/api/prediction/{UNIPROT}", "af_meta.json").read_text())[0]
    pdb = fetch(meta["pdbUrl"], "af_model.pdb")
    model = PDBParser(QUIET=True).get_structure("af", str(pdb))[0]
    plddt = {r.id[1]: round(r["CA"].bfactor, 1) for r in model["A"]}
    out = {"version": meta.get("latestVersion"), "mean_plddt": meta.get("globalMetricValue"), "plddt": plddt}
    # AlphaMissense scores are fetched here so the cache is complete; they are read from the
    # cache by 05_variant_table.py and not copied wholesale into results/
    try:
        fetch(meta["amAnnotationsUrl"], "alphamissense.csv")
        out["alphamissense_available"] = True
    except Exception as exc:  # the file is not always served to scripted clients
        out["alphamissense_available"] = False
        out["alphamissense_error"] = str(exc)
    return out


def mapped_models(pdb_id: str, seq: str):
    """Yield {uniprot_position: residue} for each model, mapping by sequence, not by label."""
    from Bio.Align import PairwiseAligner
    path = fetch(f"https://files.rcsb.org/download/{pdb_id}.pdb", f"{pdb_id}.pdb")
    structure = PDBParser(QUIET=True).get_structure(pdb_id, str(path))
    aligner = PairwiseAligner(); aligner.mode = "local"
    aligner.open_gap_score = -10; aligner.extend_gap_score = -1
    for model in structure:
        res = [r for r in model["A"] if r.id[0] == " " and r.resname in protein_letters_3to1]
        cseq = "".join(protein_letters_3to1[r.resname] for r in res)
        aln = aligner.align(seq, cseq)[0]
        m = {}
        for (s0, s1), (c0, c1) in zip(*aln.aligned):
            for k in range(s1 - s0):
                m[s0 + k + 1] = res[c0 + k]
        yield m


def centroid(m, lo, hi):
    pts = [m[i]["CA"].coord for i in range(lo, hi + 1) if i in m]
    return np.mean(pts, axis=0) if pts else None


def domain_geometry(pdb_id: str, seq: str) -> dict:
    """Inter-domain CA-centroid distances (A), mean and SD over models."""
    core_ranges = [(1, 37), (68, 130), (142, 194)]
    rows = []
    label_offsets = set()
    seq_diffs = set()
    n_missing = None
    for m in mapped_models(pdb_id, seq):
        core = np.mean([m[i]["CA"].coord for lo, hi in core_ranges for i in range(lo, hi + 1) if i in m], axis=0)
        nmp, lid = centroid(m, 38, 67), centroid(m, 131, 141)
        ploop, lidtip = centroid(m, 15, 23), centroid(m, 131, 141)
        rows.append([
            np.linalg.norm(nmp - core),
            np.linalg.norm(lid - core) if lid is not None else np.nan,
            np.linalg.norm(nmp - lid) if lid is not None else np.nan,
        ])
        label_offsets |= {r.id[1] - i for i, r in m.items()}
        seq_diffs |= {(i, seq[i - 1], protein_letters_3to1[r.resname]) for i, r in m.items()
                      if protein_letters_3to1[r.resname] != seq[i - 1]}
        n_missing = [i for i in range(1, len(seq) + 1) if i not in m]
    arr = np.array(rows)
    def ms(col):
        v = arr[:, col]
        if np.all(np.isnan(v)):
            return None
        return {"mean": round(float(np.nanmean(v)), 2), "sd": round(float(np.nanstd(v)), 2)}
    return {"entry": pdb_id, "n_models": len(rows),
            "author_label_minus_uniprot_position": sorted(label_offsets),
            "sequence_differences_vs_uniprot": sorted(seq_diffs),
            "uniprot_positions_not_modelled": n_missing,
            "NMP_to_CORE_A": ms(0), "LID_to_CORE_A": ms(1), "NMP_to_LID_A": ms(2)}


def local_environment(pdb_id: str, seq: str, pos: int) -> dict:
    """Residues whose side chain or backbone comes within 4 A of residue pos (model 1)."""
    m = next(mapped_models(pdb_id, seq))
    r = m[pos]
    atoms = [a for a in r if a.element != "H"]
    out = {}
    for j, rr in m.items():
        if abs(j - pos) <= 1:
            continue
        d = min(np.linalg.norm(a.coord - b.coord) for a in atoms for b in rr if b.element != "H")
        if d < 4.0:
            out[f"{protein_letters_3to1[rr.resname]}{j}"] = round(float(d), 2)
    return {"entry": pdb_id, "residue": f"{r.resname}{pos}", "contacts_within_4A": out}


def compare_mutants(seq: str) -> dict:
    """Apo wild type (7X7S, NMR) versus the two deposited disease-variant structures."""
    out = {"domain_geometry": [domain_geometry(e, seq) for e in ("1Z83", "2C95", "7X7S", "8X1G", "7DE3")],
           "local_environment": [local_environment("7X7S", seq, 97), local_environment("8X1G", seq, 97),
                                 local_environment("1Z83", seq, 97),
                                 local_environment("7X7S", seq, 128), local_environment("7DE3", seq, 128),
                                 local_environment("1Z83", seq, 128)],
           "entries": {"1Z83": "wild type + Ap5A, X-ray (closed)", "2C95": "wild type + Ap4A, X-ray (closed)",
                       "7X7S": "wild type, no ligand, solution NMR", "8X1G": "R97W, solution NMR",
                       "7DE3": "R128W, X-ray, no nucleotide modelled"}}
    return out


def main() -> None:
    seq = uniprot_sequence()
    feats = uniprot_features()
    out = {"structures": {}}
    for pdb_id, chain, lig in [("1Z83", "A", "AP5"), ("2C95", "A", "B4P")]:
        out["structures"][pdb_id] = analyse(pdb_id, chain, lig, seq, feats)
    out["alphafold"] = alphafold(seq)
    out["variant_structures"] = compare_mutants(seq)
    dump(out, "structure_mapping.json")
    for k, v in out["structures"].items():
        print(k, "modelled", v["n_residues_modelled"], "mismatches", v["numbering_mismatches_vs_uniprot"],
              v["ligand_half_assignment"])
    print(json.dumps(out["variant_structures"], indent=1, default=lambda o: o.item()))
    print("AF", out["alphafold"].get("mean_plddt"), out["alphafold"].get("alphamissense_error", "AM ok"))


if __name__ == "__main__":
    main()
