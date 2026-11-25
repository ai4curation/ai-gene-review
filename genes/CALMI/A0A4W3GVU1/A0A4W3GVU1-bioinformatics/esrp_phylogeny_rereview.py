"""Place A0A4W3GVU1 (Callorhinchus milii esrp1) relative to ESRP1, ESRP2 and other PTHR13976 members.

Fetches sequences from UniProt, aligns with MAFFT (must be on PATH), reports
pairwise identity of the target to each member over aligned non-gap columns,
and builds a neighbour-joining tree (identity distance) with Biopython.

Run:  uv run --with biopython --with requests python esrp_phylogeny_rereview.py
"""

import subprocess
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
MEMBERS = {
    "A0A4W3GVU1": "CALMI_esrp1_target",
    "Q6NXG1": "HUMAN_ESRP1_SF37",
    "Q3US41": "MOUSE_Esrp1_SF37",
    "A1L1G1": "DANRE_esrp1",
    "Q6DEZ7": "XENTR_esrp1",
    "Q9H6T0": "HUMAN_ESRP2_SF30",
    "Q8K0G8": "MOUSE_Esrp2_SF30",
    "Q7ZVR8": "DANRE_esrp2",
    "Q9BJZ5": "DROME_fus_SF25",
    "P52597": "HUMAN_HNRNPF",
    "P31943": "HUMAN_HNRNPH1",
    "Q12849": "HUMAN_GRSF1",
    "Q9NTZ6": "HUMAN_RBM12",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    fasta = HERE / "esrp_members_rereview.fasta"
    seqs = {MEMBERS[a]: fetch(a) for a in MEMBERS}
    fasta.write_text("".join(f">{k}\n{v}\n" for k, v in seqs.items()))
    aln_path = HERE / "esrp_members_rereview.aln.fasta"
    out = subprocess.run(
        ["mafft", "--auto", "--quiet", str(fasta)], capture_output=True, text=True, check=True
    )
    aln_path.write_text(out.stdout)
    aln = AlignIO.read(aln_path, "fasta")
    rec = {r.id: str(r.seq) for r in aln}
    tgt = rec["CALMI_esrp1_target"]
    print("Lengths:", {k: len(v) for k, v in seqs.items()})
    print("\nIdentity of target to each member (aligned columns where both non-gap):")
    rows = []
    for name, s in rec.items():
        if name == "CALMI_esrp1_target":
            continue
        pairs = [(a, b) for a, b in zip(tgt, s) if a != "-" and b != "-"]
        ident = sum(a == b for a, b in pairs) / len(pairs)
        rows.append((ident, name, len(pairs)))
    for ident, name, n in sorted(rows, reverse=True):
        print(f"  {name:22s} {ident*100:5.1f}%  over {n} columns")
    dm = DistanceCalculator("identity").get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup("HUMAN_RBM12")
    print("\nNJ tree (identity distance, rooted on RBM12):")
    Phylo.draw_ascii(tree)
    Phylo.write(tree, HERE / "esrp_members_rereview.nwk", "newick")


if __name__ == "__main__":
    main()
