# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Phylogenetic placement of CG8745 (Q9VU95) within PANTHER PTHR45688.

Fetches UniProt sequences for PTHR45688 members across subfamilies, aligns them
with MAFFT, prints a pairwise identity matrix to CG8745, builds a neighbour-joining
tree (BLOSUM62 distances), and reports which residues align to the catalytic
PLP lysine of human ETNPPL (K278) and of CG8745 (K291).

Run: uv run phylo_placement.py
"""

import subprocess
from io import StringIO
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent

# accession -> label (PANTHER subfamily from interpro/panther/PTHR45688 entries / PTHR19.0 classifications)
MEMBERS = {
    "Q9VU95": "CG8745_DROME_SF13",
    "P91408": "eppl-1_CAEEL_SF13",
    "Q9US34": "SPAC1039.07c_SCHPO_SF13",
    "Q94AL9": "AGT3_ARATH_SF13",
    "P16932": "dgdA_BURCE_SF13",
    "Q7M181": "ACLR_ACHOB_SF13",
    "Q8TBG4": "ETNPPL_HUMAN_SF1",
    "Q7SY54": "etnppl_DANRE_SF1",
    "Q8IUZ5": "PHYKPL_HUMAN_SF6",
    "Q2YDQ8": "phykpl_DANRE_SF6",
    "Q9BYV1": "AGXT2_HUMAN_SF3",
    "A8E6R2": "CG11241_DROME_SF3",
    "O02158": "T09B4.8_CAEEL_SF3",
    "Q940M2": "AGT2_ARATH_SF3",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def ungapped_index(seq: str, col: int) -> int | None:
    if seq[col] == "-":
        return None
    return len(seq[:col].replace("-", "")) + 1


def main() -> None:
    fasta = HERE / "pthr45688_members.fasta"
    seqs = {acc: fetch(acc) for acc in MEMBERS}
    fasta.write_text("".join(f">{MEMBERS[a]}\n{s}\n" for a, s in seqs.items()))
    for a, s in seqs.items():
        print(f"{MEMBERS[a]}\t{a}\tlen={len(s)}")

    aln_txt = subprocess.run(
        ["mafft", "--auto", "--quiet", str(fasta)], capture_output=True, text=True, check=True
    ).stdout
    (HERE / "pthr45688_members.aln.fasta").write_text(aln_txt)
    aln = AlignIO.read(StringIO(aln_txt), "fasta")
    rec = {r.id: str(r.seq) for r in aln}
    target = rec["CG8745_DROME_SF13"]

    print("\n# Percent identity to CG8745 (aligned, non-gap positions in both)")
    rows = []
    for name, s in rec.items():
        if name == "CG8745_DROME_SF13":
            continue
        pairs = [(a, b) for a, b in zip(target, s) if a != "-" and b != "-"]
        ident = sum(a == b for a, b in pairs) / len(pairs) * 100
        rows.append((ident, name))
    for ident, name in sorted(rows, reverse=True):
        print(f"{name}\t{ident:.1f}")

    # Catalytic lysine: human ETNPPL K278 (PDB 6TOR); CG8745 MOD_RES K291
    hs = rec["ETNPPL_HUMAN_SF1"]
    col = None
    for c in range(len(hs)):
        if ungapped_index(hs, c) == 278:
            col = c
            break
    print(f"\n# Residues aligned to human ETNPPL K278 (column {col})")
    for name, s in rec.items():
        print(f"{name}\t{s[col]}{ungapped_index(s, col)}")

    calc = DistanceCalculator("blosum62")
    dm = calc.get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup("AGXT2_HUMAN_SF3", "CG11241_DROME_SF3", "T09B4.8_CAEEL_SF3", "AGT2_ARATH_SF3")
    Phylo.write(tree, HERE / "pthr45688_nj.nwk", "newick")
    print("\n# NJ tree (BLOSUM62 distance), rooted on SF3 AGXT2 clade")
    Phylo.draw_ascii(tree)


if __name__ == "__main__":
    main()
