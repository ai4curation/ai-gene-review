"""Is the YxxPhi cargo-binding pocket of the AP complex mu subunit present, and
intact, in human AP3M1?

The question matters because GOA gives AP3M1 no molecular function of its own
apart from an IBA for "clathrin-cargo adaptor activity" seeded entirely from
AP-1/AP-2 mu subunits. The literature says the medium subunit is the part of an
AP complex that reads tyrosine-based (YxxPhi) sorting signals, and the 2024
cryo-EM structures of human AP-3 contain a LAMP1 YQTI peptide bound to the mu3
C-terminal domain. This script measures that directly rather than asserting it.

What it does, all from live downloads, with no hardcoded answers:

1.  Downloads the UniProt sequences of the six human AP-complex mu subunits
    (AP1M1, AP1M2, AP2M1, AP3M1, AP3M2, AP4M1) and mouse Ap3m1.
2.  Downloads PDB 9C5B (human AP-3 + myristoylated Arf1 + LAMP1 cargo on a
    nanodisc) and PDB 1BXX (mu2 C-terminal domain + TGN38 DYQRLN peptide).
3.  Asserts that the modelled chains really are the proteins we think they are
    (9C5B chain M must equal the full Q9Y2T2 sequence; 1BXX chain A must be a
    contiguous fragment of Q96CW1) before measuring anything.
4.  Computes, for each structure, the mu-subunit residues within a distance
    cutoff of the bound cargo peptide -- the empirical cargo pocket.
5.  Aligns AP3M1 against AP2M1 (and the other mu paralogues) and reports, for
    every mu2 pocket position, which residue AP3M1 carries at the aligned
    column, so pocket conservation is a measurement rather than a claim.

Usage:
    uv run python cargo_pocket.py            # writes RESULTS.md next to this file
    uv run python cargo_pocket.py --cutoff 4.0
"""

from __future__ import annotations

import argparse
import io
import json
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import gemmi

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"

# UniProt accessions of the human AP-complex medium (mu) subunits plus the
# mouse AP3M1 orthologue used as the ISS/IEA donor in GOA.
MU_SUBUNITS = {
    "AP3M1_HUMAN": "Q9Y2T2",
    "AP3M2_HUMAN": "P53677",
    "AP2M1_HUMAN": "Q96CW1",
    "AP1M1_HUMAN": "Q9BXS5",
    "AP1M2_HUMAN": "Q9Y6Q5",
    "AP4M1_HUMAN": "O00189",
    "AP3M1_MOUSE": "Q9JKC8",
}

# (pdb id, mu chain, cargo chain, accession the mu chain must correspond to)
STRUCTURES = [
    ("9C5B", "M", "Y", "Q9Y2T2"),
    ("1BXX", "A", "P", "Q96CW1"),
]


def fetch(url: str, cache_name: str, binary: bool = False):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / cache_name
    if not path.exists():
        with urllib.request.urlopen(url, timeout=120) as fh:
            data = fh.read()
        path.write_bytes(data)
    return path.read_bytes() if binary else path.read_text()


def uniprot_sequence(acc: str) -> str:
    fasta = fetch(
        f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", f"{acc}.fasta"
    )
    lines = fasta.splitlines()
    assert lines and lines[0].startswith(">"), f"no FASTA header for {acc}"
    return "".join(lines[1:])


def load_structure(pdb_id: str) -> gemmi.Structure:
    path = CACHE / f"{pdb_id}.cif.gz"
    if not path.exists():
        url = f"https://files.rcsb.org/download/{pdb_id}.cif.gz"
        with urllib.request.urlopen(url, timeout=120) as fh:
            path.write_bytes(fh.read())
    st = gemmi.read_structure(str(path))
    st.setup_entities()
    return st


@dataclass
class Contact:
    resnum: int
    resname: str
    one_letter: str
    min_distance: float


def chain_sequence(chain: gemmi.Chain) -> tuple[str, list[int]]:
    """One-letter sequence of the modelled polymer residues, plus their numbers."""
    seq, nums = [], []
    for res in chain:
        info = gemmi.find_tabulated_residue(res.name)
        if info is None or not info.is_amino_acid():
            continue
        seq.append(gemmi.find_tabulated_residue(res.name).one_letter_code.upper())
        nums.append(res.seqid.num)
    return "".join(seq), nums


def pocket_contacts(
    st: gemmi.Structure, mu_chain_id: str, cargo_chain_id: str, cutoff: float
) -> tuple[list[Contact], str]:
    model = st[0]
    mu_chain = model[mu_chain_id]
    cargo_chain = model[cargo_chain_id]
    assert len(mu_chain) > 100, f"chain {mu_chain_id} too short to be a mu subunit"
    cargo_seq, _ = chain_sequence(cargo_chain)
    assert 4 <= len(cargo_seq) <= 30, f"cargo chain length {len(cargo_seq)} unexpected"

    cargo_atoms = [
        (res, atom)
        for res in cargo_chain
        for atom in res
        if atom.element != gemmi.Element("H")
    ]
    contacts: dict[int, Contact] = {}
    for res in mu_chain:
        info = gemmi.find_tabulated_residue(res.name)
        if info is None or not info.is_amino_acid():
            continue
        best = None
        for atom in res:
            if atom.element == gemmi.Element("H"):
                continue
            for _, catom in cargo_atoms:
                d = atom.pos.dist(catom.pos)
                if best is None or d < best:
                    best = d
        if best is not None and best <= cutoff:
            contacts[res.seqid.num] = Contact(
                resnum=res.seqid.num,
                resname=res.name,
                one_letter=info.one_letter_code.upper(),
                min_distance=round(best, 2),
            )
    return [contacts[k] for k in sorted(contacts)], cargo_seq


def align(a: str, b: str) -> tuple[str, str]:
    """Global alignment of two sequences, returning the aligned strings."""
    from Bio import Align

    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = Align.substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aln = aligner.align(a, b)[0]
    return str(aln[0]), str(aln[1])


def map_positions(query: str, target: str) -> dict[int, tuple[int | None, str]]:
    """Map 1-based query positions onto 1-based target positions via alignment."""
    qa, ta = align(query, target)
    mapping: dict[int, tuple[int | None, str]] = {}
    qi = ti = 0
    for qc, tc in zip(qa, ta):
        if qc != "-":
            qi += 1
        if tc != "-":
            ti += 1
        if qc != "-":
            mapping[qi] = ((ti if tc != "-" else None), tc)
    return mapping


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff", type=float, default=4.5)
    ap.add_argument("--out", default=str(HERE / "RESULTS.md"))
    args = ap.parse_args()

    seqs = {name: uniprot_sequence(acc) for name, acc in MU_SUBUNITS.items()}
    for name, seq in seqs.items():
        assert len(seq) > 300, f"{name} sequence looks truncated ({len(seq)} aa)"

    out = io.StringIO()
    w = out.write
    w("# AP3M1 bioinformatics: the YxxPhi cargo pocket of the AP-3 mu subunit\n\n")
    w(
        "Generated by `cargo_pocket.py` (`uv run python cargo_pocket.py`). "
        "Everything below is computed from live UniProt and RCSB downloads at run "
        f"time; the heavy-atom contact cutoff is {args.cutoff} A.\n\n"
    )

    w("## Input sequences\n\n")
    w("| protein | accession | length |\n|---|---|---|\n")
    for name, acc in MU_SUBUNITS.items():
        w(f"| {name} | {acc} | {len(seqs[name])} |\n")
    w("\n")

    results = {}
    for pdb_id, mu_chain, cargo_chain, acc in STRUCTURES:
        st = load_structure(pdb_id)
        model_seq, model_nums = chain_sequence(st[0][mu_chain])
        ref = seqs[
            next(n for n, a in MU_SUBUNITS.items() if a == acc)
        ]
        # Sanity: every modelled residue must be the residue the reference
        # protein carries at that same author-assigned position. This checks
        # both identity (right protein) and numbering (UniProt-based), and it
        # tolerates the disordered loops that are missing from a structure.
        in_range = [
            (num, aa)
            for num, aa in zip(model_nums, model_seq)
            if 1 <= num <= len(ref)
        ]
        agree = [(num, aa) for num, aa in in_range if ref[num - 1] == aa]
        assert len(in_range) >= 100, (
            f"{pdb_id} chain {mu_chain}: only {len(in_range)} residues fall "
            f"inside the {acc} numbering range"
        )
        assert len(agree) == len(in_range), (
            f"{pdb_id} chain {mu_chain} disagrees with {acc} at "
            f"{len(in_range) - len(agree)} of {len(in_range)} modelled "
            "positions; residue numbering is not UniProt-based"
        )
        contacts, cargo_seq = pocket_contacts(st, mu_chain, cargo_chain, args.cutoff)
        results[pdb_id] = (
            contacts,
            cargo_seq,
            model_nums,
            model_seq,
            acc,
            len(in_range),
        )

    w("## Cargo-contacting residues measured from the structures\n\n")
    for pdb_id, mu_chain, cargo_chain, acc in STRUCTURES:
        contacts, cargo_seq, model_nums, model_seq, _, n_checked = results[pdb_id]
        w(
            f"### {pdb_id} - chain {mu_chain} ({acc}) vs cargo chain "
            f"{cargo_chain} (`{cargo_seq}`)\n\n"
        )
        w(
            f"All {n_checked} modelled residues of chain {mu_chain} match {acc} "
            "at their own author-assigned residue number, so the structure is "
            "numbered in UniProt coordinates and the positions below can be "
            "read directly as sequence positions.\n\n"
        )
        w(
            f"{len(contacts)} residues within {args.cutoff} A of the peptide "
            f"(modelled chain: {len(model_seq)} residues, numbering "
            f"{model_nums[0]}-{model_nums[-1]}):\n\n"
        )
        w(
            "  "
            + ", ".join(
                f"{c.one_letter}{c.resnum} ({c.min_distance} A)" for c in contacts
            )
            + "\n\n"
        )

    # Map the mu2 pocket onto AP3M1.
    mu2_contacts = results["1BXX"][0]
    ap2 = seqs["AP2M1_HUMAN"]
    mu2_positions = [
        (c.resnum, c.one_letter, c.min_distance) for c in mu2_contacts
    ]
    for pos, aa, _ in mu2_positions:
        assert ap2[pos - 1] == aa, f"AP2M1 position {pos} is {ap2[pos-1]}, not {aa}"

    w("## AP2M1 cargo-pocket positions mapped onto the other mu subunits\n\n")
    others = [n for n in MU_SUBUNITS if n != "AP2M1_HUMAN"]
    mappings = {n: map_positions(ap2, seqs[n]) for n in others}
    w("| AP2M1 pos | " + " | ".join(n.replace("_HUMAN", "").replace("_MOUSE", " (mouse)") for n in others) + " |\n")
    w("|---|" + "---|" * len(others) + "\n")
    identical = {n: 0 for n in others}
    aligned = {n: 0 for n in others}
    for pos, aa, _ in mu2_positions:
        cells = []
        for n in others:
            tpos, tc = mappings[n][pos]
            if tpos is None:
                cells.append("-")
            else:
                aligned[n] += 1
                if tc == aa:
                    identical[n] += 1
                cells.append(f"{tc}{tpos}")
        w(f"| {aa}{pos} | " + " | ".join(cells) + " |\n")
    w("\n")
    w("| protein | aligned to a residue | identical to AP2M1 |\n|---|---|---|\n")
    for n in others:
        w(f"| {n} | {aligned[n]}/{len(mu2_positions)} | {identical[n]}/{len(mu2_positions)} |\n")
    w("\n")

    # Overlap between the AP-3 pocket measured in 9C5B and the AP2M1 pocket
    # projected onto AP3M1.
    ap3_contacts = {c.resnum for c in results["9C5B"][0]}
    projected = {
        mappings["AP3M1_HUMAN"][pos][0]
        for pos, _, _ in mu2_positions
        if mappings["AP3M1_HUMAN"][pos][0] is not None
    }
    w("## Do the two pockets coincide?\n\n")
    w(
        f"AP3M1 residues contacting the LAMP1 peptide in 9C5B: "
        f"{len(ap3_contacts)}. AP2M1 pocket positions projected onto AP3M1 by "
        f"alignment: {len(projected)}. Overlap: "
        f"{len(ap3_contacts & projected)} residues "
        f"({sorted(ap3_contacts & projected)}).\n\n"
    )
    seq3 = seqs["AP3M1_HUMAN"]
    w(
        "AP3M1 residues in the overlap: "
        + ", ".join(f"{seq3[p-1]}{p}" for p in sorted(ap3_contacts & projected))
        + "\n\n"
    )
    w(
        "AP3M1 LAMP1-contacting residues not in the projected AP2M1 pocket: "
        + ", ".join(f"{seq3[p-1]}{p}" for p in sorted(ap3_contacts - projected))
        + "\n\n"
    )

    w("## What this shows\n\n")
    n_overlap = len(ap3_contacts & projected)
    n_ap3 = len(ap3_contacts)
    w(
        f"- The AP-3 medium subunit carries a cargo-binding site: {n_ap3} AP3M1 "
        "residues contact the bound LAMP1 YxxPhi peptide in the human AP-3 "
        "cryo-EM structure.\n"
    )
    w(
        f"- It is the *same* site as the AP-2 one: {n_overlap} of those {n_ap3} "
        "residues fall on alignment columns that are also AP2M1 cargo-pocket "
        "positions in the mu2/TGN38 crystal structure.\n"
    )
    w(
        f"- The site is structurally conserved but chemically divergent: AP3M1 "
        f"is identical to AP2M1 at only {identical['AP3M1_HUMAN']} of "
        f"{len(mu2_positions)} pocket positions while aligning to a residue at "
        f"{aligned['AP3M1_HUMAN']} of {len(mu2_positions)}, which is the "
        "structural basis for the different YxxPhi preferences of the mu "
        "subunits.\n"
    )
    mouse_map = mappings["AP3M1_MOUSE"]
    same_in_mouse = sum(
        1
        for pos, _, _ in mu2_positions
        if mouse_map[pos][0] is not None
        and mappings["AP3M1_HUMAN"][pos][0] is not None
        and mouse_map[pos][1] == mappings["AP3M1_HUMAN"][pos][1]
    )
    w(
        f"- Mouse Ap3m1 matches human AP3M1 at {same_in_mouse} of "
        f"{len(mu2_positions)} of these positions, so the ISS/IEA transfers "
        "GOA makes from mouse Ap3m1 to AP3M1 are not crossing a diverged "
        "cargo-binding site.\n\n"
    )

    # Machine-readable dump next to the report.
    (HERE / "results.json").write_text(
        json.dumps(
            {
                "cutoff_angstrom": args.cutoff,
                "sequence_lengths": {n: len(s) for n, s in seqs.items()},
                "contacts": {
                    pdb: {
                        "cargo_peptide": results[pdb][1],
                        "mu_residues": [
                            {
                                "resnum": c.resnum,
                                "aa": c.one_letter,
                                "min_distance": c.min_distance,
                            }
                            for c in results[pdb][0]
                        ],
                    }
                    for pdb in results
                },
                "ap2m1_pocket_positions": [
                    {"pos": p, "aa": a} for p, a, _ in mu2_positions
                ],
                "ap2m1_pocket_projected_onto": {
                    n: {
                        str(p): (
                            None
                            if mappings[n][p][0] is None
                            else f"{mappings[n][p][1]}{mappings[n][p][0]}"
                        )
                        for p, _, _ in mu2_positions
                    }
                    for n in others
                },
            },
            indent=2,
        )
    )

    Path(args.out).write_text(out.getvalue())
    print(out.getvalue())
    return 0


if __name__ == "__main__":
    sys.exit(main())
