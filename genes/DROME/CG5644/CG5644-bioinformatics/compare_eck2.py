# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare D. melanogaster CG5644 with the biochemically characterised
Anopheles gambiae ecdysteroid 22-kinase AgEcK2 (AGAP002181, UniProt F5HIV2)
and with the SF6 paralog CG6830 (Q9VGJ8).

Reports, for each protein, the PANTHER family/subfamily and eggNOG orthologous
group from its live UniProt record, global pairwise identities, and the
occurrence of the aminoglycoside-phosphotransferase-type catalytic-loop motif
(HxDxxxxN, 'Brenner motif') that marks the CHK/EcKL kinase fold.

Run: uv run compare_eck2.py > results-eck2.txt
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

PROTEINS = {
    "CG5644_DROME": "Q9VSS3",
    "AgEcK2_ANOGA": "F5HIV2",
    "CG6830_DROME": "Q9VGJ8",
}


def fetch_record(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60)
    r.raise_for_status()
    return r.text


def parse(record: str) -> tuple[str, list[str], list[str]]:
    seq_lines, in_seq, xrefs, eggnog = [], False, [], []
    for line in record.splitlines():
        if line.startswith("DR   PANTHER;"):
            xrefs.append(line.split(";")[1].strip())
        if line.startswith("DR   eggNOG;"):
            eggnog.append(line.split(";")[1].strip())
        if line.startswith("SQ"):
            in_seq = True
            continue
        if in_seq and not line.startswith("//"):
            seq_lines.append(line.replace(" ", ""))
    return "".join(seq_lines), xrefs, eggnog


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += a[i] == b[j]
    return 100.0 * ident / aligned, aligned


def main() -> None:
    seqs = {}
    for name, acc in PROTEINS.items():
        seq, panther, eggnog = parse(fetch_record(acc))
        seqs[name] = seq
        motifs = [(m.start() + 1, m.group()) for m in re.finditer(r"H.D.{4}N", seq)]
        print(f"{name}\t{acc}\tlength={len(seq)}\tPANTHER={','.join(panther)}"
              f"\teggNOG={','.join(eggnog)}\tHxDxxxxN={motifs}")
    names = list(seqs)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pid, n = identity(seqs[names[i]], seqs[names[j]])
            print(f"{names[i]} vs {names[j]}: {pid:.1f}% identity over {n} aligned residues")


if __name__ == "__main__":
    main()
