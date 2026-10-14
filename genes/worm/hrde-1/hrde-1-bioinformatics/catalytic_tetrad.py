"""Check whether HRDE-1 (Q09249) retains the Argonaute slicer catalytic tetrad.

Fetches HRDE-1 and human AGO2 (Q9UKV8) from UniProt, performs a local
BLOSUM62 alignment, and reports the HRDE-1 residues aligned to the AGO2
catalytic tetrad D597, E637, D669, H807.

Run: uv run python genes/worm/hrde-1/hrde-1-bioinformatics/catalytic_tetrad.py
"""
import io
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        return str(next(SeqIO.parse(io.StringIO(r.read().decode()), "fasta")).seq)


def main() -> None:
    hrde1 = fetch("Q09249")
    ago2 = fetch("Q9UKV8")
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "local"
    aln = al.align(ago2, hrde1)[0]
    mapping = {}
    for (bs, be), (as_, _ae) in zip(*aln.aligned):
        for i in range(be - bs):
            mapping[bs + i + 1] = as_ + i + 1
    print(f"alignment score: {aln.score}")
    print("AGO2_pos\tAGO2_res\tHRDE1_pos\tHRDE1_res\tconserved")
    for p in (597, 637, 669, 807):
        q = mapping.get(p)
        r = hrde1[q - 1] if q else "-"
        print(f"{p}\t{ago2[p-1]}\t{q}\t{r}\t{r == ago2[p-1]}")


if __name__ == "__main__":
    main()
