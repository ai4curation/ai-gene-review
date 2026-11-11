"""Compare Glorund isoform C (Q8INJ6) with the long Glorund product (Q9VGH5).

Fetches both sequences from UniProt REST and reports the shared N-terminal
prefix, the isoform-C-specific C-terminal tail, and which of the qRRM
boundaries used in PMID:35699205 (qRRM1 45-141, qRRM2 142-234, qRRM3 475-562,
numbered on the long product) are fully contained in isoform C.

Usage: python3 compare_isoforms_rereview.py
"""

import json
import urllib.request

QRRMS = {"qRRM1": (45, 141), "qRRM2": (142, 234), "qRRM3": (475, 562)}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def shared_prefix(a: str, b: str) -> int:
    """Length of the identical N-terminal prefix.

    >>> shared_prefix("MSNAX", "MSNAY")
    4
    """
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def main() -> None:
    short, long_ = fetch("Q8INJ6"), fetch("Q9VGH5")
    p = shared_prefix(short, long_)
    result = {
        "Q8INJ6_length": len(short),
        "Q9VGH5_length": len(long_),
        "identical_prefix_length": p,
        "Q8INJ6_unique_tail": short[p:],
        "Q9VGH5_residues_after_prefix_start": long_[p : p + 20],
        "qRRM_contained_in_Q8INJ6": {
            name: (end <= p) for name, (start, end) in QRRMS.items()
        },
        "qRRM2_residues_retained": max(0, min(p, QRRMS["qRRM2"][1]) - QRRMS["qRRM2"][0] + 1),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
