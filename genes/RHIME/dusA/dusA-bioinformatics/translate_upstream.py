"""Translate 300 nt upstream of each annotated dusA start in frame and list start codons.

Shows that the annotated 359-aa start (MIDWTD..., UniProt Q92P85 and RefSeq
WP_010969552.1) begins at the equivalent of E. coli DusA M33, so the FMN-binding
P32 is missing from it, and that
the open reading frame continues upstream in both strains with different
sequence. Run after fetch_gene_models.sh:
  uv run python translate_upstream.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq

HERE = Path(__file__).parent
REGIONS = {
    "S. meliloti 1021": "sm1021_dusA_region_AL591688.1.fasta",
    "E. meliloti USDA1810": "usda1810_dusA_region_NZ_RPHN01000062.1.fasta",
}
UPSTREAM = 300


def main() -> None:
    for name, fn in REGIONS.items():
        s = str(next(SeqIO.parse(HERE / fn, "fasta")).seq)
        prot = str(Seq(s[UPSTREAM % 3:]).translate())
        upstream_aa = prot[: UPSTREAM // 3]
        orf_start = upstream_aa.rfind("*") + 1
        print(f"== {name} ==")
        print(f"upstream in-frame translation: {upstream_aa}")
        print(f"open frame upstream of annotated start: {upstream_aa[orf_start:]} "
              f"({len(upstream_aa) - orf_start} codons)")
        print(f"annotated start onward: {prot[UPSTREAM // 3:UPSTREAM // 3 + 12]}...")
        for i in range(UPSTREAM % 3 + 3 * orf_start, UPSTREAM + 3, 3):
            codon = s[i:i + 3]
            if codon in ("ATG", "GTG", "TTG"):
                print(f"  start codon {codon} at {i - UPSTREAM:+d} nt "
                      f"(+{(UPSTREAM - i) // 3} aa); preceding 15 nt {s[i - 15:i]}")
        print()


if __name__ == "__main__":
    main()
