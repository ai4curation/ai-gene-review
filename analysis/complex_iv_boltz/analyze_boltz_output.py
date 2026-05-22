#!/usr/bin/env python3
"""Summarize Boltz confidence and chain contacts for the domain pilot."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from Bio.PDB import MMCIFParser, NeighborSearch

CHAIN_LABELS = {
    "A": "MT-CO2_88-227",
    "B": "SCO1_112-301",
    "C": "SCO2_79-266",
    "D": "COA6_55-98",
}


def chain_atoms(chain):
    return [
        atom
        for atom in chain.get_atoms()
        if atom.element != "H" and atom.parent.id[0] == " "
    ]


def residue_contacts(chain_a, chain_b, cutoff=5.0):
    atoms_b = chain_atoms(chain_b)
    ns = NeighborSearch(atoms_b)
    contacts = set()
    for atom_a in chain_atoms(chain_a):
        for atom_b in ns.search(atom_a.coord, cutoff, "A"):
            res_a = atom_a.parent
            res_b = atom_b.parent
            contacts.add((res_a.id[1], res_b.id[1]))
    return contacts


def print_confidence(path: Path) -> None:
    if not path.exists():
        print(f"No confidence JSON found: {path}")
        return
    data = json.loads(path.read_text())
    keys = [
        "confidence_score",
        "ptm",
        "iptm",
        "protein_iptm",
        "complex_plddt",
        "complex_iplddt",
        "complex_pde",
        "complex_ipde",
    ]
    print("Confidence")
    for key in keys:
        if key in data:
            print(f"  {key}: {data[key]}")
    if "pair_chains_iptm" in data:
        print("Pair-chain ipTM")
        print(json.dumps(data["pair_chains_iptm"], indent=2))


def print_contacts(cif: Path) -> None:
    structure = MMCIFParser(QUIET=True).get_structure("prediction", str(cif))
    model = next(structure.get_models())
    chains = {chain.id: chain for chain in model}
    print("Chain contacts at 5 A")
    for i, chain_a in enumerate(CHAIN_LABELS):
        for chain_b in list(CHAIN_LABELS)[i + 1 :]:
            if chain_a not in chains or chain_b not in chains:
                continue
            contacts = residue_contacts(chains[chain_a], chains[chain_b])
            print(
                f"  {CHAIN_LABELS[chain_a]} vs {CHAIN_LABELS[chain_b]}: "
                f"{len(contacts)} residue-residue contacts"
            )


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: analyze_boltz_output.py <prediction_directory>")
    pred_dir = Path(sys.argv[1])
    if pred_dir.is_file():
        pred_dir = pred_dir.parent

    confidence = next(pred_dir.glob("confidence_*.json"), None)
    cif = next(pred_dir.glob("*_model_0.cif"), None)
    if confidence:
        print_confidence(confidence)
    else:
        print("No confidence JSON found")
    if cif:
        print_contacts(cif)
    else:
        print("No model_0 CIF found")


if __name__ == "__main__":
    main()
