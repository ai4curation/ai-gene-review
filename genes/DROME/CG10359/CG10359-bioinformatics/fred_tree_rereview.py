# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Phylogenetic placement of the CG10359 (B7Z0B2) fibrinogen C-terminal domain (FReD).

Fetches FReD sequences (UniProt 'Fibrinogen C-terminal' DOMAIN feature) for all
Drosophila PTHR19143 members (PANTHER 19.0 fruit-fly classification) plus the
C. elegans SF327 member and characterised human FReD proteins, aligns them with
MAFFT, builds a neighbour-joining tree (BLOSUM62 distance) and reports pairwise
identities of the CG10359 FReD to each sequence.

Run: uv run --script fred_tree_rereview.py
Outputs: fred_rereview.fa, fred_rereview.aln.fa, fred_rereview_nj.nwk, fred_rereview_results.tsv
"""

import re
import subprocess
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent

# accession -> (label, PANTHER subfamily as given by PANTHER 19.0 / UniProt xref)
SEQS = {
    "B7Z0B2": ("CG10359_DROME", "SF327"),
    "A0A0B4K7T3": ("AAF57948_DROME", "SF327"),
    "A1Z7G6": ("AAF59068_DROME", "SF327"),
    "Q7KT80": ("DS00929_DROME", "SF327"),
    "Q8IRM2": ("AAN09619_DROME", "SF327"),
    "Q9VW70": ("FBpp0074674_DROME", "SF327"),
    "Q9VX04": ("FBpp0074269_DROME", "SF327"),
    "Q9W302": ("AAF46535_DROME", "SF327"),
    "Q5ZR75": ("T15B7.1_CAEEL", "SF327"),
    "Q9VF34": ("FBpp0082632_DROME", "SF185"),
    "Q5BIB8": ("CG17443_DROME", "SF426"),
    "P21520": ("sca_DROME", "SF444"),
    "Q4V4U2": ("AAF46801_DROME", "SF458"),
    "Q95SM8": ("CG6676_DROME", "SF458"),
    "Q9VME7": ("AAF52372_DROME", "SF458"),
    "Q8N539": ("FIBCD1_HUMAN", "SF45"),
    "O00602": ("FCN1_HUMAN", "SF377"),
    "Q15485": ("FCN2_HUMAN", "?"),
    "O75636": ("FCN3_HUMAN", "?"),
    "Q15389": ("ANGPT1_HUMAN", "?"),
    "O15123": ("ANGPT2_HUMAN", "?"),
    "P55083": ("MFAP4_HUMAN", "?"),
    "P24821": ("TNC_HUMAN", "?"),
    "P02679": ("FGG_HUMAN", "?"),
    "Q08830": ("FGL1_HUMAN", "?"),
    "Q14314": ("FGL2_HUMAN", "?"),
}


def fetch_fred(acc: str) -> str:
    """Return the sequence of the first 'Fibrinogen C-terminal' DOMAIN of an entry."""
    rec = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60).json()
    seq = rec["sequence"]["value"]
    doms = [
        f
        for f in rec.get("features", [])
        if f["type"] == "Domain" and re.search("Fibrinogen C-terminal", f.get("description", ""))
    ]
    d = doms[0]["location"]
    return seq[d["start"]["value"] - 1 : d["end"]["value"]]


def main() -> None:
    fa = HERE / "fred_rereview.fa"
    with fa.open("w") as fh:
        for acc, (label, sf) in SEQS.items():
            fh.write(f">{label}|{acc}|{sf}\n{fetch_fred(acc)}\n")
    aln_path = HERE / "fred_rereview.aln.fa"
    out = subprocess.run(["mafft", "--quiet", "--localpair", "--maxiterate", "1000", str(fa)],
                         capture_output=True, text=True, check=True).stdout
    aln_path.write_text(out)
    aln = AlignIO.read(aln_path, "fasta")

    dm = DistanceCalculator("blosum62").get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_at_midpoint()
    Phylo.write(tree, HERE / "fred_rereview_nj.nwk", "newick")
    Phylo.draw_ascii(tree)

    target = next(r for r in aln if r.id.startswith("CG10359"))
    rows = []
    for r in aln:
        if r is target:
            continue
        pairs = [(a, b) for a, b in zip(str(target.seq), str(r.seq)) if a != "-" and b != "-"]
        ident = sum(a == b for a, b in pairs) / len(pairs)
        rows.append((r.id, len(pairs), ident))
    rows.sort(key=lambda x: -x[2])
    with (HERE / "fred_rereview_results.tsv").open("w") as fh:
        fh.write("sequence\taligned_columns\tidentity_to_CG10359_FReD\n")
        for rid, n, ident in rows:
            fh.write(f"{rid}\t{n}\t{ident:.3f}\n")
            print(f"{rid}\t{n}\t{ident:.3f}")


if __name__ == "__main__":
    main()
