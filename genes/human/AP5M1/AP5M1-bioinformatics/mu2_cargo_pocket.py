"""Define the mu2 YxxPhi cargo pocket empirically, from the solved complex.

Hirst et al. 2011 (PMID:22022230) state that "the key residues in the mu subunits
that bind to YXXPhi sorting signals ... are altered in C14orf108" (= AP5M1/mu5),
and Hirst et al. 2018 (PMID:29381698) that "the highly conserved cargo binding
sites found in the other AP complexes are absent in AP-5".  Neither paper lists
the residues, so this script derives them rather than taking them from memory:

  PDB 1BXX = "MU2 ADAPTIN SUBUNIT (AP50) OF AP2 ADAPTOR (SECOND DOMAIN),
  COMPLEXED WITH TGN38 INTERNALIZATION PEPTIDE DYQRLN"

Every mu2 residue with a heavy atom within CUTOFF angstroms of a heavy atom of
the bound DYQRLN peptide is taken as a cargo-pocket residue.  Author numbering in
1BXX is checked residue-by-residue against the UniProt Q96CW1 sequence before any
position is reported, so the output is in Q96CW1 numbering.

Writes mu2_cargo_pocket.tsv.
"""

from __future__ import annotations

import csv
import io
import pathlib

from Bio.Data.IUPACData import protein_letters_3to1_extended as three_to_one
from Bio.PDB import MMCIFParser, NeighborSearch

from common import rcsb_cif, uniprot_record

PDB_ID = "1BXX"
MU2 = "Q96CW1"
CUTOFF = 4.5  # angstroms, heavy atom to heavy atom

HERE = pathlib.Path(__file__).parent


def main() -> None:
    cif_text = rcsb_cif(PDB_ID)
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure(PDB_ID, io.StringIO(cif_text))
    model = next(iter(structure))

    chains = {}
    for chain in model:
        residues = [r for r in chain if r.id[0] == " "]
        if residues:
            chains[chain.id] = residues
    if len(chains) < 2:
        raise RuntimeError(f"{PDB_ID}: expected >=2 polymer chains, found {sorted(chains)}")

    # The peptide is the short chain; mu2 is the long one.
    by_len = sorted(chains.items(), key=lambda kv: len(kv[1]))
    peptide_id, peptide = by_len[0]
    mu2_id, mu2_residues = by_len[-1]
    peptide_seq = "".join(three_to_one.get(r.get_resname().capitalize(), "X") for r in peptide)
    print(f"{PDB_ID}: mu2 chain {mu2_id} ({len(mu2_residues)} residues), "
          f"peptide chain {peptide_id} = {peptide_seq} ({len(peptide)} residues)")
    if "YQRL" not in peptide_seq:
        raise RuntimeError(f"peptide chain {peptide_id} is {peptide_seq!r}; expected the TGN38 YQRL motif")

    rec = uniprot_record(MU2)
    seq = rec["sequence"]
    print(f"{MU2} {rec['entry_name']} {rec['gene']} {rec['organism']}: "
          f"{rec['length']} aa, sequence version {rec['sequence_version']}")

    # Verify the PDB author numbering is UniProt numbering.
    mismatches = []
    for res in mu2_residues:
        pos = res.id[1]
        aa = three_to_one.get(res.get_resname().capitalize(), "X")
        if not (1 <= pos <= len(seq)) or seq[pos - 1] != aa:
            mismatches.append((pos, aa, seq[pos - 1] if 1 <= pos <= len(seq) else "-"))
    if mismatches:
        raise RuntimeError(
            f"{PDB_ID} chain {mu2_id} author numbering does not match {MU2}: "
            f"{len(mismatches)} mismatches, first {mismatches[:5]}"
        )
    observed = [r.id[1] for r in mu2_residues]
    print(f"author numbering verified against {MU2} for all {len(mu2_residues)} residues "
          f"(range {min(observed)}-{max(observed)})")

    mu2_atoms = [a for r in mu2_residues for a in r if a.element != "H"]
    ns = NeighborSearch(mu2_atoms)
    contacts: dict[int, dict] = {}
    for pres in peptide:
        pep_pos = pres.id[1]
        pep_aa = three_to_one.get(pres.get_resname().capitalize(), "X")
        for patom in pres:
            if patom.element == "H":
                continue
            for matom in ns.search(patom.coord, CUTOFF):
                mres = matom.get_parent()
                pos = mres.id[1]
                entry = contacts.setdefault(
                    pos,
                    {"residue": three_to_one.get(mres.get_resname().capitalize(), "X"),
                     "peptide_partners": set(), "min_dist": 1e9},
                )
                entry["peptide_partners"].add(f"{pep_aa}{pep_pos}")
                d = float(((patom.coord - matom.coord) ** 2).sum() ** 0.5)
                entry["min_dist"] = min(entry["min_dist"], d)

    rows = []
    for pos in sorted(contacts):
        e = contacts[pos]
        rows.append({
            "mu2_accession": MU2,
            "mu2_position": pos,
            "mu2_residue": e["residue"],
            "min_distance_A": f"{e['min_dist']:.2f}",
            "peptide_contacts": ",".join(sorted(e["peptide_partners"])),
        })

    out = HERE / "mu2_cargo_pocket.tsv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"\n{len(rows)} mu2 residues within {CUTOFF} A of the DYQRLN peptide -> {out.name}")
    for r in rows:
        print(f"  {r['mu2_residue']}{r['mu2_position']:>4}  {r['min_distance_A']} A  "
              f"contacts {r['peptide_contacts']}")

    # The Tyr and Phi (Leu) pockets specifically: residues contacting the motif Tyr
    # and the motif Leu of DYQRLN.
    tyr = [r for r in rows if any(p.startswith("Y") for p in r["peptide_contacts"].split(","))]
    phi = [r for r in rows if any(p.startswith("L") for p in r["peptide_contacts"].split(","))]
    print(f"\nY-pocket ({len(tyr)}): " + " ".join(f"{r['mu2_residue']}{r['mu2_position']}" for r in tyr))
    print(f"Phi-pocket ({len(phi)}): " + " ".join(f"{r['mu2_residue']}{r['mu2_position']}" for r in phi))


if __name__ == "__main__":
    main()
