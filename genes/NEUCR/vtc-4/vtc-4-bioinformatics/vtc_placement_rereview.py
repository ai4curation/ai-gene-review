# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.81", "requests"]
# ///
"""Phylogenetic placement and catalytic-site check for N. crassa VTC-4 (Q7SCX0).

Fetches SPX-VTC family members (Vtc4 orthologs, Vtc2/Vtc3 paralogs) from UniProt,
aligns them with MAFFT, maps yeast Vtc4 (P47075) catalytic/ATP-binding and SPX
InsP-binding positions (UniProt FT, PubMed:19390046 / 27080106) onto each sequence,
computes pairwise identity and a neighbour-joining tree. Results printed to stdout.
"""
import io
import subprocess
import sys
from pathlib import Path

import requests
from Bio import AlignIO, SeqIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
ACCS = {
    "Q7SCX0": "NEUCR vtc-4 (target)",
    "Q1K5R9": "NEUCR NCU01745",
    "P47075": "YEAST Vtc4",
    "Q02725": "YEAST Vtc3",
    "P43585": "YEAST Vtc2",
    "P78810": "SCHPO vtc4",
    "O13718": "SCHPO vtc2",
    "G0SCH1": "CHATD Vtc4",
    "Q382V9": "TRYB2 vtc4",
}
# yeast Vtc4 positions from UniProt P47075 FT (ACT_SITE 458; ATP BINDING sites)
SITES = {200: "ATP", 264: "ATP", 266: "ATP", 281: "ATP", 294: "ATP",
         359: "ATP", 361: "ATP", 458: "ACT_SITE"}
SPX_REGION = range(126, 134)  # 'Important for inositol polyphosphate binding'


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return r.text


def panther(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60)
    r.raise_for_status()
    return ";".join(l.split(";")[1].strip() for l in r.text.splitlines()
                    if l.startswith("DR   PANTHER;"))


def main() -> None:
    fasta = HERE / "vtc_family_rereview.fasta"
    fasta.write_text("".join(fetch(a) for a in ACCS))
    aln_path = HERE / "vtc_family_rereview.aln.fasta"
    out = subprocess.run(["mafft", "--auto", "--quiet", str(fasta)],
                         capture_output=True, text=True, check=True).stdout
    aln_path.write_text(out)
    aln = AlignIO.read(io.StringIO(out), "fasta")
    recs = {r.id.split("|")[1]: r for r in aln}

    print("## PANTHER assignments (UniProt DR lines)")
    for a, lab in ACCS.items():
        print(f"{a}\t{lab}\t{panther(a)}")

    ref = recs["P47075"].seq
    col_of = {}
    pos = 0
    for i, c in enumerate(ref):
        if c != "-":
            pos += 1
            col_of[pos] = i

    def residue_at(acc: str, col: int) -> str:
        s = recs[acc].seq
        if s[col] == "-":
            return "-"
        n = sum(1 for c in s[: col + 1] if c != "-")
        return f"{s[col]}{n}"

    print("\n## Yeast Vtc4 catalytic/ATP-binding positions mapped by alignment")
    print("acc\t" + "\t".join(f"{ref[col_of[p]]}{p}({t})" for p, t in SITES.items()))
    for a in ACCS:
        print(a + "\t" + "\t".join(residue_at(a, col_of[p]) for p in SITES))

    print("\n## SPX InsP-binding region (yeast Vtc4 126-133)")
    for a in ACCS:
        print(a + "\t" + " ".join(residue_at(a, col_of[p]) for p in SPX_REGION))

    print("\n## Pairwise identity to target over aligned non-gap columns")
    tgt = recs["Q7SCX0"].seq
    for a in ACCS:
        s = recs[a].seq
        pairs = [(x, y) for x, y in zip(tgt, s) if x != "-" and y != "-"]
        ident = sum(x == y for x, y in pairs) / len(pairs)
        print(f"{a}\t{ACCS[a]}\t{ident:.3f}\t({len(pairs)} cols)")

    for r in aln:
        r.id = r.id.split("|")[1]
        r.name = r.id
    dm = DistanceCalculator("blosum62").get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup("Q382V9")
    print("\n## NJ tree (BLOSUM62 distances, rooted on T. brucei vtc4)")
    buf = io.StringIO()
    Phylo.write(tree, buf, "newick")
    print(buf.getvalue().strip())
    Phylo.draw_ascii(tree, file=sys.stdout)


if __name__ == "__main__":
    main()
