"""Scan AOPEP and characterised M1 aminopeptidases for the GXMEN exopeptidase motif and the HEXXH zinc motif.

In M1 aminopeptidases the GXMEN (GAMEN) motif binds the free alpha-amino group of the substrate and
is the sequence determinant of aminopeptidase (exopeptidase) specificity. Sequences are fetched
from UniProt at run time:
    uv run python gxmen_motif.py
"""
import re
import urllib.request

PROTEINS = {
    "Q8N6M6": "AOPEP (human aminopeptidase O)",
    "P15144": "ANPEP (aminopeptidase N; UniProt's similarity source for AOPEP)",
    "P09960": "LTA4H (leukotriene A4 hydrolase / aminopeptidase)",
    "Q9H4A4": "RNPEP (aminopeptidase B)",
}
MOTIFS = {"GXMEN": r"G.MEN", "relaxed G.M.N": r"G.M.N", "HEXXH": r"HE..H"}


def fasta(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
        return "".join(r.read().decode().split("\n")[1:])


def main() -> None:
    for acc, name in PROTEINS.items():
        seq = fasta(acc)
        hits = {k: [(m.start() + 1, m.group()) for m in re.finditer(p, seq)] for k, p in MOTIFS.items()}
        print(f"{acc}\t{name}\tlength={len(seq)}")
        for k, v in hits.items():
            print(f"  {k}: {v if v else 'none'}")


if __name__ == "__main__":
    main()
