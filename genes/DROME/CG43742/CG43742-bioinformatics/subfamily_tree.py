"""Place CG43742 (A0A0B4KFF2) among its PANTHER 19.0 subfamily members.

Reads the PANTHER 19.0 fruit-fly classification (repo cache), takes every
Drosophila member of PTHR24260:SF147 (the subfamily PANTHER's HMMs assign
CG43742 to) plus three CLIP outgroups seeding PAINT node PTN000667087, fetches
sequences from UniProt, aligns with MAFFT, and reports:

* pairwise identity of CG43742 to every member over aligned non-gap columns
* a neighbour-joining tree (identity distance)
* catalytic-triad residues of CG43742 S1 domain 1 and domain 2, located by
  local motif search (TAAHC / D-I-A-L-L / GDSGGP-like) on the exact sequence.

Usage: uv run python subfamily_tree.py
"""

import io
import re
import subprocess
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
REPO = HERE.parents[3]
PANTHER_FLY = REPO / ".cache" / "panther" / "PTHR19.0_fruit_fly"
SUBFAMILY = "PTHR24260:SF147"
TARGET = "A0A0B4KFF2"
OUTGROUPS = {"Q9VWU1": "psh", "Q9VER6": "modSP", "Q9VCJ8": "SPE"}


def subfamily_members() -> dict[str, str]:
    members = {}
    for line in PANTHER_FLY.read_text().splitlines():
        cols = line.split("\t")
        if cols[3] == SUBFAMILY:
            members[cols[1]] = cols[2].replace("Dmel\\", "")
    return members


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    members = subfamily_members()
    print(f"{SUBFAMILY}: {len(members)} D. melanogaster members")
    allseqs = {**members, **OUTGROUPS}
    seqs = {acc: fetch(acc) for acc in allseqs}
    fasta = HERE / "sf147_plus_outgroups.fasta"
    fasta.write_text(
        "".join(f">{acc}_{allseqs[acc]}\n{seq}\n" for acc, seq in seqs.items())
    )
    aln_txt = subprocess.run(
        ["mafft", "--auto", "--quiet", str(fasta)],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    (HERE / "sf147_plus_outgroups.aln.fasta").write_text(aln_txt)
    aln = AlignIO.read(io.StringIO(aln_txt), "fasta")
    target_rec = next(r for r in aln if r.id.startswith(TARGET))

    rows = []
    for rec in aln:
        if rec.id == target_rec.id:
            continue
        pairs = [
            (a, b) for a, b in zip(str(target_rec.seq), str(rec.seq)) if a != "-" and b != "-"
        ]
        ident = sum(a == b for a, b in pairs) / len(pairs) if pairs else 0.0
        rows.append((ident, len(pairs), rec.id, len(seqs[rec.id.split("_")[0]])))
    rows.sort(reverse=True)
    print("\nIdentity of CG43742 to each sequence (aligned non-gap columns):")
    for ident, n, rid, length in rows:
        print(f"  {rid:28s} len={length:5d} overlap={n:4d} identity={ident:.3f}")

    tree = DistanceTreeConstructor(DistanceCalculator("identity"), "nj").build_tree(aln)
    tree.root_with_outgroup({"name": [r.id for r in aln if r.id.startswith("Q9VWU1")][0]})
    out = io.StringIO()
    Phylo.write(tree, out, "newick")
    (HERE / "sf147_nj.nwk").write_text(out.getvalue())
    print("\nNJ tree (identity distance, rooted on psh):")
    Phylo.draw_ascii(tree)

    target = seqs[TARGET]
    print(f"\nCG43742 length: {len(target)}")
    for label, start, end in (("domain1", 35, 258), ("domain2", 282, 472)):
        dom = target[start - 1 : end]
        his = [m.start() + start + 3 for m in re.finditer(r"[TS]A[AG]HC", dom)]
        ser = [m.start() + start + 2 for m in re.finditer(r"[GSA]D[SA]GG[PS]", dom)]
        print(f"  {label} {start}-{end}: His-motif positions(H)={his} GDSGG-motif Ser={ser}")
        print(f"    residue at 73={target[72]} 121={target[120]} 207={target[206]}")


if __name__ == "__main__":
    main()
