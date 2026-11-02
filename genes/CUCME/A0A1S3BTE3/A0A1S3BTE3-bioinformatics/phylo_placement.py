# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Phylogenetic placement of melon A0A1S3BTE3 among the 20 Arabidopsis MPKs.

Fetches sequences from UniProt, aligns with MAFFT (L-INS-i), computes pairwise
identity over aligned (non-gap) columns, builds a neighbour-joining tree, and
reports activation-loop TxY motif and C-terminal length for each sequence.
Arabidopsis PANTHER 19.0 subfamily assignments are passed in from the PANTHER
classification file (PTHR19.0_arabidopsis).
"""
import subprocess
import sys
from io import StringIO
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
TARGET = "A0A1S3BTE3"
ATH = {  # accession: (symbol, PANTHER 19.0 subfamily from PTHR19.0_arabidopsis)
    "Q39021": ("MPK1", "SF378"), "Q39022": ("MPK2", "SF561"), "Q39023": ("MPK3", "SF391"),
    "Q39024": ("MPK4", "SF439"), "Q39025": ("MPK5", "SF227"), "Q39026": ("MPK6", "SF589"),
    "Q39027": ("MPK7", "SF401"), "Q9LM33": ("MPK8", "SF463"), "Q9LV37": ("MPK9", "SF429"),
    "Q9M1Z5": ("MPK10", "SF594"), "Q9LMM5": ("MPK11", "SF439"), "Q8GYQ5": ("MPK12", "SF351"),
    "Q9LQQ9": ("MPK13", "SF601"), "O23236": ("MPK14", "SF401"), "Q9C9U4": ("MPK15", "SF414"),
    "Q8W4J2": ("MPK16", "SF211"), "Q84M93": ("MPK17", "SF560"), "Q9C5C0": ("MPK18", "SF420"),
    "Q9LUC3": ("MPK19", "SF200"), "Q9SJG9": ("MPK20", "SF392"),
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    seqs = {TARGET: fetch(TARGET)}
    names = {TARGET: TARGET}
    for acc, (sym, _) in ATH.items():
        seqs[acc] = fetch(acc)
        names[acc] = f"{sym}_{acc}"
    fasta = HERE / "mpk_seqs.fasta"
    fasta.write_text("".join(f">{names[a]}\n{s}\n" for a, s in seqs.items()))
    aln_path = HERE / "mpk_aln.fasta"
    out = subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fasta)],
                         capture_output=True, text=True, check=True).stdout
    aln_path.write_text(out)
    aln = AlignIO.read(StringIO(out), "fasta")
    tgt = next(r for r in aln if r.id == TARGET)
    print("Pairwise identity of target to each Arabidopsis MPK (aligned non-gap columns):")
    rows = []
    for rec in aln:
        if rec.id == TARGET:
            continue
        pairs = [(a, b) for a, b in zip(str(tgt.seq), str(rec.seq)) if a != "-" and b != "-"]
        ident = sum(a == b for a, b in pairs) / len(pairs)
        acc = rec.id.split("_")[-1]
        rows.append((ident, rec.id, ATH[acc][1], len(seqs[acc])))
    for ident, rid, sf, ln in sorted(rows, reverse=True):
        print(f"  {rid:16s} PANTHER:{sf:7s} len={ln:4d} identity={ident:.3f}")
    print("\nActivation-loop TxY motif (first T[DEG]Y after 'DFGLAR'):")
    import re
    for acc, s in seqs.items():
        m = re.search(r"DFGLAR.{5,25}?(T[DEG]Y)", s)
        print(f"  {names[acc]:16s} {m.group(1) if m else 'not found'} len={len(s)}")
    tree = DistanceTreeConstructor(DistanceCalculator("blosum62"), "nj").build_tree(aln)
    tree.root_with_outgroup("MPK1_Q39021")  # group C MPK used as outgroup
    Phylo.write(tree, HERE / "mpk_nj.nwk", "newick")
    print("\nNJ tree (BLOSUM62 distance, rooted on group C MPK1):")
    Phylo.draw_ascii(tree, file=sys.stdout)


if __name__ == "__main__":
    main()
