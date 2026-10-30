"""Compare canonical RAC1 sequences of rat, human and mouse from UniProt REST.

Usage: python compare_orthologs.py
Prints length and pairwise identity of each sequence versus rat Q6RUV5.
"""
import urllib.request

ACCS = {"rat": "Q6RUV5", "human": "P63000", "mouse": "P63001"}


def fetch(acc: str) -> str:
    """Fetch the canonical sequence for a UniProt accession."""
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def main() -> None:
    """Report identity of human and mouse RAC1 to rat Rac1."""
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    rat = seqs["rat"]
    for name, seq in seqs.items():
        same = sum(a == b for a, b in zip(rat, seq))
        print(f"{name}\t{ACCS[name]}\tlength={len(seq)}\tidentical_positions_vs_rat={same}\tidentical={seq == rat}")


if __name__ == "__main__":
    main()
