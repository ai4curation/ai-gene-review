"""Place wheat F6LAX4 among PP2A scaffold A subunits (PTHR10648).

Fetches sequences from UniProt REST, aligns with MAFFT (must be on PATH),
reports percent identity of F6LAX4 to each sequence and a neighbour-joining
tree (identity distance) in Newick format.

Run: uv run --with biopython python phylogeny_rereview.py
"""

import subprocess
import urllib.request
from io import StringIO
from pathlib import Path

from Bio import AlignIO, Phylo, SeqIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

ACCESSIONS = [
    "F6LAX4",  # wheat target
    "Q6K4K9", "B7EGU3",  # rice
    "I1IIW4", "I1IIX4",  # Brachypodium
    "K7V7I6", "A0A1D6LKF6",  # maize
    "U5CQS6", "W1PIA3",  # Amborella
    "A0A3Q7GXD1", "A0A3Q7GDK7",  # tomato
    "A9TEJ4", "A9STM1",  # Physcomitrium
    "Q38845", "Q38950", "Q38951",  # Arabidopsis PP2AA1/RCN1, PP2AA2, PP2AA3
    "P30153", "P30154",  # human PPP2R1A, PPP2R1B
    "P36179",  # fly Pp2A-29B
    "P31383", "Q9UT08",  # yeasts TPD3, paa1
]

HERE = Path(__file__).parent


def fetch() -> str:
    q = "+OR+".join(f"accession:{a}" for a in ACCESSIONS)
    url = f"https://rest.uniprot.org/uniprotkb/stream?query={q}&format=fasta"
    return urllib.request.urlopen(url).read().decode()


def main() -> None:
    fasta = fetch()
    recs = list(SeqIO.parse(StringIO(fasta), "fasta"))
    for r in recs:
        acc, mnemonic = r.id.split("|")[1:3]
        r.id = f"{acc}_{mnemonic.split('_')[1]}"
        r.description = ""
    raw = HERE / "pp2aa_rereview.fa"
    SeqIO.write(recs, raw, "fasta")
    aln_txt = subprocess.run(
        ["mafft", "--quiet", "--auto", str(raw)], capture_output=True, text=True, check=True
    ).stdout
    (HERE / "pp2aa_rereview.aln.fa").write_text(aln_txt)
    aln = AlignIO.read(StringIO(aln_txt), "fasta")
    seqs = {r.id: str(r.seq) for r in aln}
    target = next(k for k in seqs if k.startswith("F6LAX4"))
    print("Percent identity of F6LAX4 (aligned, gap-free columns):")
    for k, s in seqs.items():
        if k == target:
            continue
        pairs = [(a, b) for a, b in zip(seqs[target], s) if a != "-" and b != "-"]
        pid = 100 * sum(a == b for a, b in pairs) / len(pairs)
        print(f"  {k:22s} {pid:5.1f}")
    dm = DistanceCalculator("identity").get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup("P31383_YEAST", "Q9UT08_SCHPO")
    out = StringIO()
    Phylo.write(tree, out, "newick")
    print("\nNJ tree (identity distance, rooted on fungi):")
    print(out.getvalue())
    Phylo.draw_ascii(tree)


if __name__ == "__main__":
    main()
