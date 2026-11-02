# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Compare the A0A1P8ARD2 FTSH12 gene model with the canonical Swiss-Prot entry Q9SAJ3.

Fetches both sequences from the UniProt REST API, reports the shared prefix and the
divergent C-terminal tails, and checks the conserved FtsH motifs (Walker A, Walker B,
HEXXH zinc site, third zinc ligand) in the benchmark product.

Run: uv run --script compare_gene_models_rereview.py > RESULTS-rereview.md
"""

import re
import urllib.request

ACCESSIONS = {"benchmark": "A0A1P8ARD2", "canonical": "Q9SAJ3"}


def fetch_sequence(acc: str) -> str:
    """Return the UniProt sequence for an accession."""
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as handle:
        lines = handle.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def shared_prefix(a: str, b: str) -> int:
    """Length of the identical N-terminal prefix.

    >>> shared_prefix("ABCDE", "ABCXY")
    3
    """
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return n


def motif_hits(seq: str, pattern: str) -> list[tuple[int, str]]:
    """1-based start positions and matches of a regex motif.

    >>> motif_hits("AAGPPGTGKTAA", "G..G.GK[ST]")
    [(3, 'GPPGTGKT')]
    """
    return [(m.start() + 1, m.group()) for m in re.finditer(pattern, seq)]


def main() -> None:
    bench = fetch_sequence(ACCESSIONS["benchmark"])
    canon = fetch_sequence(ACCESSIONS["canonical"])
    n = shared_prefix(bench, canon)
    print("# FTSH12 gene-model comparison (re-review)\n")
    print(f"- A0A1P8ARD2 length: {len(bench)}")
    print(f"- Q9SAJ3 (Swiss-Prot canonical) length: {len(canon)}")
    print(f"- Identical N-terminal prefix: residues 1-{n}")
    print(f"- A0A1P8ARD2 divergent tail ({n + 1}-{len(bench)}): {bench[n:]}")
    print(f"- Q9SAJ3 divergent tail ({n + 1}-{len(canon)}): {canon[n:]}\n")
    print("## Conserved motifs in A0A1P8ARD2\n")
    print("| Motif | Pattern | Hits (position, sequence) |")
    print("|---|---|---|")
    motifs = {
        "Walker A (P-loop)": "G..G.GK[ST]",
        "Walker B": "[ILVMF]{4}DE",
        "HEXXH zinc site": "HE..H",
    }
    for name, pattern in motifs.items():
        print(f"| {name} | `{pattern}` | {motif_hits(bench, pattern)} |")
    print(f"\nResidue 849 (third zinc ligand annotated in Q9SAJ3; Asp in FtsH M41 proteases): {bench[848]}")
    print(f"Residues 769-773 in A0A1P8ARD2: {bench[768:773]}")


if __name__ == "__main__":
    main()
