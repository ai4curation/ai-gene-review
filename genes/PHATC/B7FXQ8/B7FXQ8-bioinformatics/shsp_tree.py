"""Place B7FXQ8 among small heat shock proteins (sHSPs).

Fetches sequences from UniProt, aligns with MAFFT, trims to the alpha-crystallin
domain (ACD) span of the target, computes pairwise ACD identity and builds a
neighbour-joining tree (BLOSUM62 distances, Biopython). Also checks the
C-terminal I/V-X-I/V motif.

Run: uv run --with biopython python shsp_tree.py
"""
import re
import subprocess
import urllib.request
from pathlib import Path

from Bio import AlignIO, Phylo, SeqIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
PANEL = {
    # target and P. tricornutum paralogs (no PANTHER tree placement: not a PANTHER genome)
    "B7FXQ8": "PHATC HSP20A target",
    "B7G195": "PHATC sHSP",
    "B5Y3Y4": "PHATC sHSP",
    "B5Y4C1": "PHATC sHSP",
    "B5Y472": "PHATC sHSP (PTHR46733)",
    "B5Y4C3": "PHATC sHSP",
    "B7G194": "PHATC sHSP",
    # Thalassiosira pseudonana, in the PANTHER tree (PTHR11527:SF175)
    "B8BTA8": "THAPS sHSP PTHR11527:SF175",
    "B8CD87": "THAPS sHSP PTHR11527:SF175",
    # experimentally characterised PTHR11527 members
    "P15992": "YEAST HSP26",
    "O14368": "SCHPO hsp16",
    "Q9XIE3": "ARATH HSP17.6A",
    "O81822": "ARATH HSP17.7",
    "P27777": "ORYSJ Hsp16.9A",
    "Q41560": "WHEAT Hsp16.9B",
    "P9WMK1": "MYCTU HspX/Acr",
    "Q57733": "METJA Hsp16.5",
    # other PANTHER families (outgroups)
    "P04792": "HUMAN HSPB1 (PTHR45640)",
    "P02511": "HUMAN CRYAB (PTHR45640)",
    "P0C054": "ECOLI IbpA (PTHR47062)",
}
TARGET = "B7FXQ8"
ACD = (47, 155)  # PROSITE PS01031 SHSP domain on B7FXQ8


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def main() -> None:
    fasta = HERE / "shsp_panel.fasta"
    recs = []
    for acc in PANEL:
        txt = fetch(acc)
        header, *seq = txt.strip().splitlines()
        recs.append(f">{acc}\n{''.join(seq)}\n")
    fasta.write_text("".join(recs))
    aln_path = HERE / "shsp_panel.aln.fasta"
    out = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fasta)],
        check=True, capture_output=True, text=True,
    ).stdout
    aln_path.write_text(out)
    aln = AlignIO.read(aln_path, "fasta")
    tgt = next(r for r in aln if r.id == TARGET)
    # map target residue positions to alignment columns
    cols, pos = {}, 0
    for i, c in enumerate(str(tgt.seq)):
        if c != "-":
            pos += 1
            cols[pos] = i
    start, end = cols[ACD[0]], cols[ACD[1]]
    acd = aln[:, start : end + 1]
    AlignIO.write(acd, HERE / "shsp_panel.acd.aln.fasta", "fasta")

    tseq = str(next(r for r in acd if r.id == TARGET).seq)
    print("Pairwise identity to B7FXQ8 over its ACD columns (47-155):")
    rows = []
    for r in acd:
        s = str(r.seq)
        pairs = [(a, b) for a, b in zip(tseq, s) if a != "-" and b != "-"]
        ident = sum(a == b for a, b in pairs) / len(pairs) if pairs else 0.0
        rows.append((ident, r.id, len(pairs)))
    for ident, acc, n in sorted(rows, reverse=True):
        print(f"  {acc}\t{PANEL[acc]}\t{ident:.3f}\t(aligned {n})")

    calc = DistanceCalculator("blosum62")
    dm = calc.get_distance(acd)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup({"name": "P0C054"})
    for t in tree.get_terminals():
        t.name = f"{t.name} {PANEL[t.name]}"
    Phylo.write(tree, HERE / "shsp_panel.nj.nwk", "newick")
    print("\nNJ tree (ACD, BLOSUM62 distance, rooted on E. coli IbpA):")
    Phylo.draw_ascii(tree)

    print("C-terminal [IV]x[IV] motif after the ACD (target):")
    full = str(SeqIO.read(fasta.open(), "fasta").seq) if False else None
    seqs = {r.id: str(r.seq) for r in SeqIO.parse(fasta, "fasta")}
    s = seqs[TARGET]
    for m in re.finditer(r"(?=([IVL]\w[IVL]))", s[ACD[1] - 20 :]):
        p = ACD[1] - 20 + m.start() + 1
        print(f"  {m.group(1)} at {p}-{p + 2}")
    print(f"Target length {len(s)}")


if __name__ == "__main__":
    main()
