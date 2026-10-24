"""Check the ANKEF1 (Q9NU02) EF-hand for the canonical calcium-binding loop.

A canonical EF-hand loop is 12 residues, with calcium ligands at loop positions
1, 3, 5, 7, 9 and 12: typically D-x-[DN]-x-[DNS]-G-x-[ILV]-x-x-x-E, with an
invariant Gly at 6 and Glu at 12. UniProt places an EF-hand domain at
residues 335-369 but annotates no calcium-binding sites. This script slides a
12-residue window over that domain, scores each against the six ligand positions
plus Gly6, and reports the best window and whether it has the Glu at 12.
Calmodulin EF-hand 1 (P0DP23) is scored the same way as a positive control.

Run: uv run python ef_hand_check.py
"""

import urllib.request

LIGAND_OK = {1: "D", 3: "DN", 5: "DNS", 7: "", 9: "DNSTEQ", 12: "E"}  # 7 is a backbone carbonyl: any residue


def fetch_sequence(accession: str) -> str:
    """Return the canonical UniProt sequence for an accession."""
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{accession}.fasta") as handle:
        return "".join(handle.read().decode().splitlines()[1:])


def score_loop(loop: str) -> int:
    """Count canonical features in a 12-residue loop: ligand positions plus Gly6.

    >>> score_loop("DKDGDGTITTKE")  # calmodulin EF-hand 1 loop
    7
    >>> score_loop("AAAAAAAAAAAA")
    1
    """
    hits = sum(1 for pos, ok in LIGAND_OK.items() if ok == "" or loop[pos - 1] in ok)
    return hits + (1 if loop[5] == "G" else 0)


def best_loop(seq: str, start: int, end: int) -> tuple[int, str, int]:
    """Best-scoring 12-residue window within 1-based [start, end]."""
    windows = [(i + 1, seq[i:i + 12]) for i in range(start - 1, end - 12)]
    pos, loop = max(windows, key=lambda w: score_loop(w[1]))
    return pos, loop, score_loop(loop)


def main() -> None:
    for acc, name, start, end in [("Q9NU02", "ANKEF1 EF-hand 335-369", 335, 369),
                                  ("P0DP23", "calmodulin EF-hand 1 (control)", 8, 43)]:
        seq = fetch_sequence(acc)
        pos, loop, score = best_loop(seq, start, end)
        print(f"{name}\tdomain={seq[start - 1:end]}\tbest_loop_start={pos}\tloop={loop}\tscore={score}/7\tGlu12={loop[11] == 'E'}")


if __name__ == "__main__":
    main()
