"""Re-review phylogeny of Drosophila Dic paralogs within PANTHER PTHR45618:SF13.

Fetches UniProt sequences, aligns with MAFFT (L-INS-i), computes pairwise identity
over aligned non-gap columns, and builds a neighbour-joining tree (BLOSUM62 distance)
with 200 bootstrap replicates, rooted on the 2-oxoglutarate carrier SLC25A11.
"""
import subprocess
import urllib.request
from io import StringIO
from pathlib import Path

from Bio import AlignIO, Phylo, SeqIO
from Bio.Phylo.Consensus import bootstrap_trees, get_support
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

MEMBERS = {
    "Q9VVS1": "Dic4_DROME",
    "Q9Y166": "Dic1_DROME",
    "Q9VDM3": "Dic2_DROME",
    "A1Z787": "Dic3_DROME",
    "Q9VHG7": "CG16736_DROME",
    "A0A6M3Q724": "CG6893_DROME",
    "Q9UBX3": "SLC25A10_HUMAN",
    "Q9QZD8": "Slc25a10_MOUSE",
    "Q06143": "DIC1_YEAST",
    "Q02978": "SLC25A11_HUMAN_outgroup",
}
OUT = Path(__file__).parent


def fetch() -> Path:
    fa = OUT / "sf13_members.fasta"
    recs = []
    for acc, name in MEMBERS.items():
        txt = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode()
        rec = SeqIO.read(StringIO(txt), "fasta")
        rec.id, rec.description = name, acc
        recs.append(rec)
    SeqIO.write(recs, fa, "fasta")
    return fa


def main() -> None:
    fa = fetch()
    aln_path = OUT / "sf13_members.aln.fasta"
    aln_txt = subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fa)],
                             capture_output=True, text=True, check=True).stdout
    aln_path.write_text(aln_txt)
    aln = AlignIO.read(aln_path, "fasta")
    lines = ["# Pairwise identity (aligned non-gap columns) vs Dic4", ""]
    lengths = {r.id: len(str(r.seq).replace("-", "")) for r in aln}
    dic4 = next(r for r in aln if r.id == "Dic4_DROME")
    for r in aln:
        pairs = [(a, b) for a, b in zip(str(dic4.seq), str(r.seq)) if a != "-" and b != "-"]
        ident = sum(a == b for a, b in pairs) / len(pairs)
        lines.append(f"{r.id}\tlen={lengths[r.id]}\tidentity_to_Dic4={ident:.3f}")
    calc = DistanceCalculator("blosum62")
    cons = DistanceTreeConstructor(calc, "nj")
    tree = cons.build_tree(aln)
    tree.root_with_outgroup("SLC25A11_HUMAN_outgroup")
    boots = list(bootstrap_trees(aln, 200, cons))
    tree = get_support(tree, boots)
    for clade in tree.get_nonterminals():
        clade.name = None
    Phylo.write(tree, OUT / "sf13_nj.nwk", "newick")
    buf = StringIO()
    Phylo.draw_ascii(tree, file=buf)
    lines += ["", "# NJ tree (BLOSUM62), 200 bootstraps, rooted on SLC25A11", "", buf.getvalue()]
    lines += ["", "# Newick with bootstrap support", "", (OUT / "sf13_nj.nwk").read_text()]
    (OUT / "results-rereview.txt").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
