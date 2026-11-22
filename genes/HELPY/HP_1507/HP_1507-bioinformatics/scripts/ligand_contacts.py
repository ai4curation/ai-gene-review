#!/usr/bin/env python3
"""Report minimum heavy-atom distances from selected protein residues to a ligand.

PDB Cartesian coordinates are in Angstrom. This is a proximity report, not an
assignment of hydrogen bonds, binding energy, catalysis, or loss of function.
Uses Python standard library only. Inputs and outputs are mandatory CLI arguments.
"""
import argparse
import json
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdb', type=Path, required=True)
    parser.add_argument('--chain', required=True)
    parser.add_argument('--ligand', required=True)
    parser.add_argument('--first-residue', type=int, required=True)
    parser.add_argument('--last-residue', type=int, required=True)
    parser.add_argument('--cutoff', type=float, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.first_residue > args.last_residue or args.cutoff <= 0:
        parser.error('Invalid residue range or distance cutoff')
    atoms, ligand = [], []
    for line in args.pdb.read_text().splitlines():
        if not line.startswith(('ATOM  ', 'HETATM')) or line[21] != args.chain:
            continue
        if line[16] not in (' ', 'A') or line[76:78].strip() in ('H', 'D'):
            continue
        atom = {'residue': int(line[22:26]), 'residue_name': line[17:20].strip(),
                'atom': line[12:16].strip(),
                'xyz': [float(line[i:i+8]) for i in (30, 38, 46)]}
        if line.startswith('ATOM  '):
            atoms.append(atom)
        elif atom['residue_name'] == args.ligand:
            ligand.append(atom)
    if not atoms or not ligand:
        parser.error('Protein atoms or requested ligand absent from selected chain')
    rows = []
    for residue in range(args.first_residue, args.last_residue + 1):
        selected = [a for a in atoms if a['residue'] == residue]
        if not selected:
            rows.append({'residue': residue, 'resolved': False})
            continue
        closest = min((math.dist(a['xyz'], b['xyz']), a, b)
                      for a in selected for b in ligand)
        distance, protein_atom, ligand_atom = closest
        rows.append({'residue': residue, 'residue_name': protein_atom['residue_name'],
                     'resolved': True, 'minimum_distance_angstrom': round(distance, 3),
                     'protein_atom': protein_atom['atom'], 'ligand_atom': ligand_atom['atom'],
                     'within_cutoff': distance <= args.cutoff})
    args.output.write_text(json.dumps({'input': str(args.pdb), 'chain': args.chain,
                                     'ligand': args.ligand, 'cutoff_angstrom': args.cutoff,
                                     'ligand_heavy_atoms': len(ligand), 'residues': rows}, indent=2) + '\n')


if __name__ == '__main__':
    main()
