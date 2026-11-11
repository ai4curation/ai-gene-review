"""Fetch OST-alpha/TMEM184 family members from UniProt, align with MAFFT,
and build a neighbour-joining tree from pairwise identity distances.

Usage: uv run python fetch_and_tree.py
Outputs: family.fasta, family.aln.fasta, identity.tsv (Biopython 'identity' similarity, gaps counted), tree.nwk;
prints the midpoint-rooted NJ tree and CG6836 ungapped pairwise identities.
"""
import subprocess
import urllib.request
from pathlib import Path

from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

# accession -> label (PANTHER 19.0 subfamily as given in PANTHER classification files; '?' = not assigned)
MEMBERS = {
    "Q9VVV2": "DROME_CG6836_SF?",
    "A1A714": "DROME_Tmep_SF17",
    "M9PD30": "DROME_CG5850_SF10",
    "Q86UW1": "HUMAN_SLC51A_SF11",
    "Q8R000": "MOUSE_Slc51a_SF11",
    "Q66I08": "DANRE_slc51a_SF80",
    "Q6ZMB5": "HUMAN_TMEM184A_SF59",
    "Q9Y519": "HUMAN_TMEM184B_SF28",
    "Q9NVA4": "HUMAN_TMEM184C_SF10",
    "O17204": "CAEEL_osta-1_SF14",
    "Q18071": "CAEEL_osta-2_SF76",
    "Q9XU63": "CAEEL_osta-3_SF21",
    "G5EGF1": "CAEEL_F40E10.6_SF17",
    "P36142": "YEAST_YKR051W_SF10",
    "Q75JN3": "DICDI_tmem184B_SF17",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(lines[1:])


def main() -> None:
    out = Path(__file__).parent
    fasta = out / "family.fasta"
    with fasta.open("w") as fh:
        for acc, label in MEMBERS.items():
            seq = fetch(acc)
            fh.write(f">{label}|{acc}|len{len(seq)}\n{seq}\n")
    aln_path = out / "family.aln.fasta"
    with aln_path.open("w") as fh:
        subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fasta)], stdout=fh, check=True)
    aln = AlignIO.read(aln_path, "fasta")
    dm = DistanceCalculator("identity").get_distance(aln)
    names = dm.names
    with (out / "identity.tsv").open("w") as fh:
        fh.write("seq\t" + "\t".join(n.split("|")[0] for n in names) + "\n")
        for i, a in enumerate(names):
            fh.write(a.split("|")[0] + "\t" + "\t".join(f"{1 - dm[i, j]:.3f}" for j in range(len(names))) + "\n")
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_at_midpoint()
    Phylo.write(tree, out / "tree.nwk", "newick")
    Phylo.draw_ascii(tree)
    target = [n for n in names if n.startswith("DROME_CG6836")][0]
    ti = names.index(target)
    seqs = {r.id: str(r.seq) for r in aln}
    t = seqs[target]

    def ungapped_identity(a: str, b: str) -> float:
        cols = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
        return sum(x == y for x, y in cols) / len(cols)

    print("\nCG6836 vs each member: percent identity over columns where both are ungapped")
    for name in sorted(seqs, key=lambda n: -ungapped_identity(t, seqs[n])):
        if name != target:
            print(f"  {name}\t{100 * ungapped_identity(t, seqs[name]):.1f}")


if __name__ == "__main__":
    main()
