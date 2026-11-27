# /// script
# requires-python = ">=3.10"
# ///
"""Compare the donkey ATG3 gene models with each other, a horse model and human ATG3.

Input: atg3_models_rereview.fasta (UniProt REST FASTA, downloaded 2026-10-21).
Reports, for each sequence, its length and whether it carries the 28-residue
segment found in A0A9L0IHI0, whether removing that segment from A0A9L0IHI0 gives
exactly A0A9L0J149, and the residue at human-equivalent catalytic and
ATG12-acceptor positions.

Usage: uv run --script compare_isoforms_rereview.py atg3_models_rereview.fasta
"""

import sys


def read_fasta(path: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    key = ""
    for line in open(path):
        line = line.strip()
        if line.startswith(">"):
            key = line.split("|")[1]
            seqs[key] = ""
        elif line:
            seqs[key] += line
    return seqs


def main(path: str) -> None:
    seqs = read_fasta(path)
    human = seqs["Q9NT62"]
    target = seqs["A0A9L0IHI0"]
    short = seqs["A0A9L0J149"]
    # locate the insertion as the first position where target and the short model diverge
    i = next(k for k in range(len(short)) if target[k] != short[k])
    ins_len = len(target) - len(short)
    insertion = target[i : i + ins_len]
    print(f"insertion starts after residue {i} of A0A9L0J149; length {ins_len}: {insertion}")
    print(f"A0A9L0IHI0 minus insertion == A0A9L0J149: {target[:i] + target[i + ins_len:] == short}")
    print(f"A0A9L0J149 == human Q9NT62 length: {len(short) == len(human)}")
    ident = sum(a == b for a, b in zip(short, human))
    print(f"A0A9L0J149 vs Q9NT62 ungapped identity: {ident}/{len(human)} = {100 * ident / len(human):.2f}%")
    for acc, s in seqs.items():
        print(f"{acc}\tlength={len(s)}\thas_insertion={insertion in s}")
    for name, hpos in [("catalytic Cys", 264), ("ATG12-acceptor Lys", 243)]:
        tpos = hpos + ins_len if hpos > i else hpos
        print(
            f"{name}: human {human[hpos - 1]}{hpos}; A0A9L0J149 {short[hpos - 1]}{hpos}; "
            f"A0A9L0IHI0 {target[tpos - 1]}{tpos}"
        )


if __name__ == "__main__":
    main(sys.argv[1])
