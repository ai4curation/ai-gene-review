#!/usr/bin/env python3
"""Sequence checks for fly Atg8a against fly Atg8b and human GABARAP / LC3B.

Reports, for each protein:
  * the residue at the conserved C-terminal glycine position and the residues
    after it (the stretch Atg4 removes before PE conjugation);
  * the residues aligned to Atg8a K48/Y49 (the LIR docking site, LDS, residues
    mutated in the Atg8a-LDS flies of PMID:35649355);
  * percent identity to fly Atg8a from a simple global alignment
    (Needleman-Wunsch, BLOSUM-free: match 1, mismatch 0, gap -1), to place
    Atg8a closer to the GABARAP or the LC3 subfamily.

Sequences are fetched live from UniProt (stdlib + curl only). Nothing about
the result is hard-coded.

Usage:
  python atg8a_sequence_check.py Q9W2S2 Q9VEG5 O95166 Q9GZQ8
"""
from __future__ import annotations

import subprocess
import sys

FASTA_URL = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"


def get(url: str) -> str:
    return subprocess.run(["curl", "-sS", "-L", url], capture_output=True, text=True, check=True).stdout


def seq(acc: str) -> tuple[str, str]:
    lines = get(FASTA_URL.format(acc=acc)).splitlines()
    return lines[0], "".join(lines[1:])


def nw(a: str, b: str) -> tuple[str, str]:
    """Global alignment, match +1, mismatch 0, gap -1; returns aligned strings."""
    n, m = len(a), len(b)
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = -i
    for j in range(1, m + 1):
        s[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j - 1] + (1 if a[i - 1] == b[j - 1] else 0), s[i - 1][j] - 1, s[i][j - 1] - 1)
    i, j, x, y = n, m, [], []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s[i][j] == s[i - 1][j - 1] + (1 if a[i - 1] == b[j - 1] else 0):
            x.append(a[i - 1]); y.append(b[j - 1]); i -= 1; j -= 1
        elif i > 0 and s[i][j] == s[i - 1][j] - 1:
            x.append(a[i - 1]); y.append("-"); i -= 1
        else:
            x.append("-"); y.append(b[j - 1]); j -= 1
    return "".join(reversed(x)), "".join(reversed(y))


def map_pos(aln_ref: str, aln_other: str, ref_pos: int) -> str:
    """Residue in `other` aligned to 1-based position ref_pos of the reference."""
    k = 0
    for r, o in zip(aln_ref, aln_other):
        if r != "-":
            k += 1
            if k == ref_pos:
                return o
    return "?"


def main(accs: list[str]) -> None:
    ref_acc = accs[0]
    ref_header, ref = seq(ref_acc)
    print(f"# reference {ref_acc}: {ref_header}")
    print(f"# reference residue 116 = {ref[115]}, residues after it = '{ref[116:]}', K48/Y49 = {ref[47]}{ref[48]}")
    print("accession\tlength\tidentity_to_ref\tres_at_ref116\tres_at_ref48_49\tC-terminal 8 aa")
    for acc in accs:
        header, s = seq(acc)
        a, b = nw(ref, s)
        ident = sum(1 for x, y in zip(a, b) if x == y and x != "-")
        print(f"{acc}\t{len(s)}\t{100.0 * ident / len(ref):.1f}%\t{map_pos(a, b, 116)}\t"
              f"{map_pos(a, b, 48)}{map_pos(a, b, 49)}\t{s[-8:]}")
        print(f"#   {header}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["Q9W2S2", "Q9VEG5", "O95166", "Q9GZQ8"])
