#!/usr/bin/env python3
"""Test the 'split ORF' hypothesis for NIT1 (YIL164C) + YIL165C.

UniProt CAUTION for P40447 (NIT1): "Could be the product of a pseudogene.
NIT1/YIL164C seems to be the N-terminal part of a putative nitrilase-like
protein formed of NIT1/YIL164C and YIL165C."

This script:
  1. Builds an artificial concatenation NIT1 + YIL165C.
  2. Aligns {NIT1, YIL165C, NIT1+YIL165C concat, human NIT1, human NIT2,
     Arabidopsis NIT1} with MAFFT.
  3. Reports, for each real family member, the alignment span (first/last
     non-gap column) so we can see whether NIT1 covers the N-terminal half and
     YIL165C the C-terminal half of the shared domain, and whether the
     concatenation spans the full length.

Nothing is hardcoded except the input FASTA file paths (all under data/); the
concatenation is computed from the files at run time.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from Bio import AlignIO, SeqIO

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
RESULTS = HERE.parent / "results"


def read_seq(path: Path) -> tuple[str, str]:
    rec = next(SeqIO.parse(str(path), "fasta"))
    return rec.id, str(rec.seq)


def coverage(aln_seq: str) -> tuple[int, int, int]:
    cols = [i for i, ch in enumerate(aln_seq) if ch != "-"]
    if not cols:
        return (-1, -1, 0)
    return (cols[0] + 1, cols[-1] + 1, len(cols))


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    nit1_id, nit1 = read_seq(DATA / "NIT1_yeast.fasta")
    y165_id, y165 = read_seq(DATA / "YIL165C.fasta")
    concat = nit1 + y165

    combo = RESULTS / "split_input.fasta"
    with combo.open("w") as fh:
        fh.write(f">NIT1_YIL164C\n{nit1}\n")
        fh.write(f">YIL165C\n{y165}\n")
        fh.write(f">CONCAT_NIT1_plus_YIL165C\n{concat}\n")
        for acc in ("Q86X76", "Q9NQR4", "P32961"):
            _id, s = read_seq(DATA / f"{acc}.fasta")
            fh.write(f">{acc}\n{s}\n")

    aln_path = RESULTS / "split.aln.fasta"
    with aln_path.open("w") as out:
        subprocess.run(
            ["mafft", "--auto", "--anysymbol", str(combo)],
            stdout=out,
            stderr=subprocess.DEVNULL,
            check=True,
        )

    aln = AlignIO.read(str(aln_path), "fasta")
    aln_len = aln.get_alignment_length()
    print(f"# lengths: NIT1(YIL164C)={len(nit1)}  YIL165C={len(y165)}  concat={len(concat)}")
    print(f"# alignment length = {aln_len} columns")
    print()
    print("seq_id\tfirst_col\tlast_col\tn_residues")
    for rec in aln:
        first, last, n = coverage(str(rec.seq))
        print(f"{rec.id}\t{first}\t{last}\t{n}")


if __name__ == "__main__":
    main()
