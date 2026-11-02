# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Place A0A444Z7V7 (peanut, Ahy_B05g078721) among characterised CSLD and CESA proteins.

Steps:
1. Download sequences from UniProt REST (target + reviewed Arabidopsis/rice CSLD1-6 + CESA outgroups).
2. Align with MAFFT (--auto).
3. Report pairwise identity of the target to every reference over aligned (non-gap) columns.
4. Build a neighbour-joining tree from identity distances (Biopython) and print it (Newick + ASCII).
5. Report residues at the PIRSR-annotated catalytic/binding positions of the target
   (positions taken from the UniProt FT lines) and QxxRW motif occurrences.

Outputs written next to this script: csld_seqs.fasta, csld_aln.fasta, csld_tree.nwk, csld_placement.txt
"""

import re
import subprocess
from io import StringIO
from pathlib import Path

import requests
from Bio import AlignIO, Phylo, SeqIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

HERE = Path(__file__).parent
TARGET = "A0A444Z7V7"
REFS = {
    TARGET: "AhCSLD_target",
    "O49323": "AtCSLD1",
    "Q9LFL0": "AtCSLD2",
    "Q9M9M4": "AtCSLD3_KJK",
    "Q9SZL9": "AtCSLD4",
    "Q9SRW9": "AtCSLD5",
    "Q9FVR3": "AtCSLD6",
    "Q8W3F9": "OsCSLD1",
    "Q9LHZ7": "OsCSLD2",
    "Q7EZW6": "OsCSLD3",
    "Q2QNS6": "OsCSLD4",
    "Q5Z6E5": "OsCSLD5",
    "O48946": "AtCESA1",
    "Q94JQ6": "AtCESA6",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return r.text


def main() -> None:
    fasta = HERE / "csld_seqs.fasta"
    recs = []
    for acc, name in REFS.items():
        rec = SeqIO.read(StringIO(fetch(acc)), "fasta")
        rec.id = f"{name}|{acc}"
        rec.description = ""
        recs.append(rec)
    SeqIO.write(recs, fasta, "fasta")

    aln_path = HERE / "csld_aln.fasta"
    out = subprocess.run(["mafft", "--auto", "--quiet", str(fasta)], capture_output=True, text=True, check=True)
    aln_path.write_text(out.stdout)
    aln = AlignIO.read(aln_path, "fasta")

    lines = []
    tgt = next(r for r in aln if r.id.endswith(TARGET))
    lines.append(f"Target length (ungapped): {len(str(tgt.seq).replace('-', ''))}")
    lines.append("Pairwise identity of target vs references (aligned non-gap columns):")
    rows = []
    for r in aln:
        if r is tgt:
            continue
        same = tot = 0
        for a, b in zip(str(tgt.seq), str(r.seq)):
            if a != "-" and b != "-":
                tot += 1
                same += a == b
        rows.append((same / tot if tot else 0.0, r.id, tot, len(str(r.seq).replace("-", ""))))
    for ident, rid, tot, ln in sorted(rows, reverse=True):
        lines.append(f"  {rid:28s} identity={ident:.3f} over {tot} cols; ref length {ln}")

    calc = DistanceCalculator("identity")
    dm = calc.get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup({"name": "AtCESA1|O48946"})
    Phylo.write(tree, HERE / "csld_tree.nwk", "newick")
    buf = StringIO()
    Phylo.draw_ascii(tree, file=buf)
    lines.append("\nNJ tree (identity distance), rooted on AtCESA1:")
    lines.append(buf.getvalue())

    # Residues at target positions annotated in UniProt (PIRSR) as active site / binding
    positions = [374, 380, 381, 410, 602, 603, 627, 842]
    seq = str(tgt.seq)
    col_of = {}
    p = 0
    for i, c in enumerate(seq):
        if c != "-":
            p += 1
            col_of[p] = i
    lines.append("Residues at target PIRSR positions, with the aligned residue in each reference:")
    header = "  pos tgt  " + " ".join(r.id.split("|")[0][:9].ljust(9) for r in aln if r is not tgt)
    lines.append(header)
    for pos in positions:
        col = col_of[pos]
        lines.append(
            f"  {pos:4d} {seq[col]}    "
            + " ".join(str(r.seq)[col].ljust(9) for r in aln if r is not tgt)
        )
    ungapped = seq.replace("-", "")
    hits = [(m.start() + 1, m.group()) for m in re.finditer(r"Q..RW", ungapped)]
    lines.append(f"\nQxxRW motif occurrences in target (1-based start, motif): {hits}")

    report = "\n".join(lines)
    (HERE / "csld_placement.txt").write_text(report + "\n")
    print(report)


if __name__ == "__main__":
    main()
