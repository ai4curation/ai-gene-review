"""Re-review: place Nepl19 (Q9VAS1) among PANTHER PTHR11733:SF238 fly members.

Fetches sequences from UniProt REST, aligns with MAFFT L-INS-i, builds a
neighbour-joining tree from identity distances (Biopython), reports pairwise
identity of Nepl19 to each sequence, and the HExxH motif window at the
position aligned to human MME H584/E585.
Outputs: subfamily_rereview.fasta, subfamily_rereview_aln.fasta,
subfamily_rereview_tree.nwk, subfamily_rereview_results.json (printed too).
"""
import json
import subprocess
import urllib.request
from pathlib import Path

from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
# SF238 fly members (canonical FlyBase-gene products, per UniProt PANTHER xref)
# plus out-of-subfamily references: human MME, fly Nep2 (SF224).
ACCS = {
    "Q9VAS1": "Nepl19",
    "Q9VAS0": "Nepl20",
    "Q9VAS2": "Nepl18",
    "Q9VAS4": "Nepl17",
    "Q9Y136": "Nepl21",
    "Q9VCU1": "Nepl15",
    "Q9VYJ1": "Nep6",
    "Q8T062": "Nep4",
    "A0A0B4K692": "Nep2_SF224",
    "P08473": "human_MME",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(l.strip() for l in lines if not l.startswith(">"))


def main() -> None:
    seqs = {f"{n}_{a}": fetch(a) for a, n in ACCS.items()}
    fa = HERE / "subfamily_rereview.fasta"
    fa.write_text("".join(f">{k}\n{v}\n" for k, v in seqs.items()))
    aln_path = HERE / "subfamily_rereview_aln.fasta"
    out = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fa)],
        capture_output=True, text=True, check=True,
    )
    aln_path.write_text(out.stdout)
    aln = AlignIO.read(aln_path, "fasta")
    calc = DistanceCalculator("identity")
    dm = calc.get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup("human_MME_P08473")
    Phylo.write(tree, HERE / "subfamily_rereview_tree.nwk", "newick")
    Phylo.draw_ascii(tree)

    rows = {r.id: str(r.seq) for r in aln}
    target = rows["Nepl19_Q9VAS1"]
    ident = {}
    for k, s in rows.items():
        if k == "Nepl19_Q9VAS1":
            continue
        pairs = [(a, b) for a, b in zip(target, s) if a != "-" and b != "-"]
        ident[k] = round(100 * sum(a == b for a, b in pairs) / len(pairs), 1)
    # column of human MME H584
    ref = rows["human_MME_P08473"]
    pos, col584 = 0, None
    for i, c in enumerate(ref):
        if c != "-":
            pos += 1
            if pos == 584:
                col584 = i
                break
    motif = {}
    for k, s in rows.items():
        window = s[col584:col584 + 12].replace("-", "")
        motif[k] = window[:5]
    result = {
        "identity_to_Nepl19_pct_aligned_cols": dict(sorted(ident.items(), key=lambda x: -x[1])),
        "HExxH_window_at_MME_H584": motif,
        "tree_newick": (HERE / "subfamily_rereview_tree.nwk").read_text().strip(),
    }
    (HERE / "subfamily_rereview_results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
