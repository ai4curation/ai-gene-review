#!/usr/bin/env python3
"""Structure-based analysis of CAO-1 (Neurospora crassa) stilbenoid substrate recognition.

Goal: test whether the CAO-1 co-crystal structures explain the empirical substrate
specificity reported by Diaz-Sanchez et al. 2013 (PMID:23893079) - namely that CAO-1
requires "a minimal number of unmodified hydroxyl groups" and cleaves resveratrol and
piceatannol but not trans-stilbene, 4-monohydroxystilbene, pinosylvin, trismethoxy-
resveratrol, or a 4'-methoxy glucoside.

Approach (analysis of EXISTING co-crystal structures, not de-novo docking):
  - 5U90: Co-CAO1 in complex with resveratrol (PDB ligand STL)
  - 5U97: Co-CAO1 in complex with piceatannol   (PDB ligand PIT)
For each ligand oxygen (the phenolic hydroxyls) we enumerate the protein polar atoms
within hydrogen-bonding distance, and we report the geometry of the scissile
interphenyl C=C bond relative to the catalytic metal. We do NOT invent affinities; we
report measured distances and let them speak.

Reproducible: `uv run python analyze_specificity.py`
Outputs: prints a report and writes hbond_contacts.tsv
"""
from __future__ import annotations
import sys
import csv
from pathlib import Path

import requests
from Bio.PDB import PDBParser, NeighborSearch
from Bio.PDB.Atom import Atom

HERE = Path(__file__).parent
STRUCTURES = {
    "5U90": {"ligand": "STL", "name": "resveratrol", "cleaved": True},
    "5U97": {"ligand": "PIT", "name": "piceatannol", "cleaved": True},
}
HBOND_MAX = 3.5   # Angstrom, donor/acceptor heavy-atom distance
METAL_CODES = {"CO", "FE", "MN", "NI", "ZN"}


def fetch_pdb(pdb_id: str) -> Path:
    dest = HERE / f"{pdb_id}.pdb"
    if not dest.exists():
        url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        dest.write_text(r.text)
    return dest


def is_polar(atom: Atom) -> bool:
    return atom.element in ("N", "O")


def analyze(pdb_id: str, ligcode: str, ligname: str, rows: list) -> None:
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, str(fetch_pdb(pdb_id)))
    model = structure[0]

    all_atoms = list(model.get_atoms())
    ns = NeighborSearch(all_atoms)

    # find one copy of the ligand
    lig_residues = [r for r in model.get_residues() if r.get_resname().strip() == ligcode]
    if not lig_residues:
        print(f"  !! ligand {ligcode} not found in {pdb_id}")
        return
    lig = lig_residues[0]
    lig_chain = lig.get_parent().id
    print(f"\n=== {pdb_id}: {ligname} (ligand {ligcode}, chain {lig_chain}) ===")

    # metal position(s)
    metals = [a for a in all_atoms if a.get_parent().get_resname().strip() in METAL_CODES]

    lig_oxygens = [a for a in lig.get_atoms() if a.element == "O"]
    print(f"  ligand oxygens: {[a.get_name() for a in lig_oxygens]}")

    # intra-ligand O..O distances: hydroxyls on the same (resorcinol) ring are ~5 A
    # apart (meta), those on opposite rings are farther. Confirms ring grouping.
    print("  ligand O..O distances (ring grouping):")
    for i, a in enumerate(lig_oxygens):
        for b in lig_oxygens[i + 1:]:
            print(f"    {a.get_name()}..{b.get_name()} = {round(a - b, 2)}A")

    for o in lig_oxygens:
        near = ns.search(o.coord, HBOND_MAX)
        contacts = []
        for a in near:
            par = a.get_parent()
            rn = par.get_resname().strip()
            if par is lig:            # skip intramolecular
                continue
            if rn == "HOH":
                tag = "water"
            elif rn in METAL_CODES:
                tag = f"METAL:{rn}"
            elif is_polar(a):
                tag = f"{rn}{par.id[1]}:{a.get_name()}"
            else:
                continue              # non-polar protein atom: not an H-bond partner
            d = o - a
            contacts.append((tag, round(d, 2)))
        contacts.sort(key=lambda x: x[1])
        pretty = ", ".join(f"{t} ({d}A)" for t, d in contacts) or "(no polar partner <=3.5A)"
        print(f"    {o.get_name():4s} -> {pretty}")
        for t, d in contacts:
            rows.append([pdb_id, ligname, o.get_name(), t, d])

    # scissile bond geometry: distance of ligand carbons to metal (the C=C to be cleaved
    # sits over the Fe/Co in these enzymes). Report the closest 2 ligand carbons to metal.
    if metals:
        m = min(metals, key=lambda mm: min(mm - c for c in lig.get_atoms()))
        lig_carbons = [a for a in lig.get_atoms() if a.element == "C"]
        dists = sorted(((round(m - c, 2), c.get_name()) for c in lig_carbons))[:3]
        print(f"  closest ligand carbons to {m.get_parent().get_resname().strip()} metal: " +
              ", ".join(f"{nm} {d}A" for d, nm in dists))
        rows.append([pdb_id, ligname, "SCISSILE_C..metal", m.get_parent().get_resname().strip(),
                     dists[0][0]])


def main() -> int:
    rows: list = []
    print("CAO-1 stilbenoid recognition: H-bond contacts to ligand hydroxyls "
          f"(<= {HBOND_MAX} A)")
    for pdb_id, meta in STRUCTURES.items():
        try:
            analyze(pdb_id, meta["ligand"], meta["name"], rows)
        except Exception as e:  # noqa: BLE001 - report, do not fabricate
            print(f"  !! {pdb_id} failed: {e}")

    out = HERE / "hbond_contacts.tsv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["pdb", "ligand", "ligand_atom", "protein_partner", "distance_A"])
        w.writerows(rows)
    print(f"\nWrote {out} ({len(rows)} contacts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
