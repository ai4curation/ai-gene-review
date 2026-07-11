#!/usr/bin/env python3
"""Pairwise comparison of THI22 (Q06490) against its characterized paralog THI20 (Q08224).

Purpose: determine whether THI22 retains the substrate-binding and catalytic residues that
define the two functional domains of the S. cerevisiae thiaminase-II / HMP-P-kinase family,
so that we can distinguish "residue-dead pseudoenzyme" from "sequence-intact but activity not
demonstrated".

THI20 functional residues (from UniProt Q08224):
  - BINDING 64  : HMP substrate (N-terminal ThiD-like HMP/HMP-P kinase domain)
  - ACT_SITE 468: nucleophile (C-terminal TenA/thiaminase-II domain)
  - ACT_SITE 540: proton donor (C-terminal TenA/thiaminase-II domain)

Run: uv run python align_paralogs.py   (or: python align_paralogs.py, needs biopython)
The script prints results; it never hardcodes conclusions.
"""

from Bio import Align

# THI22 Q06490 (572 aa; signal peptide 1-19, chain 20-572)
THI22 = (
    "MVIILLGLCTLGFPRTAFCPSIMTNSTVSINTPPPYLTLACNEKLPTVMSIAGSDSSGGAGVEADIKTIT"
    "AHRCYAMTCVTTLTAQTPVKVYGAQNIPKKMVSQILDANLQDMKCNVIKTGMLTVDAIEVLHEKLLQLGE"
    "NRPKLVIDPVLCAASDSSPTGKDVVSLIIEKISPFADILTPNISDCFMLLGENREVSKLQDVLEIAKDLS"
    "RITNCSNILVKGGHIPCDDGKEKHITDVLYLGAEQKFITFKGQFVNTTRTHGAGCTLASAIASNLARGYS"
    "LSQSVYGGIEYVQNAIAIGCDVTKKAVKVGPINHVYAVEIPLEKMLTDECFTASDAVPKKPIEGSLDKIP"
    "GGSFFNYLINHPKVKPHWDAYVNHEFVKRVADGTLERKKFQFFIEQDYLYLIDYVRVCCVTGSKSPTLED"
    "LEKDLVIADCARNELNEHERRLREEFGVKDPDYLQKIKRGPALRAYCRYLIDISRRGNWQEIVVALNPCL"
    "MGYVYAVDKVKDKITAAEGSIYSEWCDTCASSFCYQAVLEGERLMNHILETYPPDQLDSLVTIFARGCEL"
    "ETNFWTAAMEYE"
)

# THI20 Q08224 (551 aa)
THI20 = (
    "MTYSTVSINTPPPYLTLACNEKLPTVLSIAGTDPSGGAGIEADVKTITAHRCYAMTCITALNAQTPVKVY"
    "SINNTPKEVVFQTLESNLKDMKCNVIKTGMLTAAAIEVLHEKLLQLGENRPKLVVDPVLVATSGSSLAGK"
    "DIVSLITEKVAPFADILTPNIPECYKLLGEERKVNGLQDIFQIAKDLAKITKCSNILVKGGHIPWNDEKE"
    "KYITDVLFLGAEQKFIIFKGNFVNTTHTHGTGCTLASAIASNLARGYSLPQSVYGGIEYVQNAVAIGCDV"
    "TKETVKDNGPINHVYAVEIPLEKMLSDECFTASDVIPKKPLKSAADKIPGGNFYEYLINHPKVKPHWDSY"
    "INHEFVKKVADGTLERKKFQFFIEQDYAYLVDYARVHCIAGSKAPCLEDMEKELVIVGGVRTEMGQHEKR"
    "LKEVFGVKDPDYFQKIKRGPALRAYSRYFNDVSRRGNWQELVASLTPCLMGYGEALTKMKGKVTAPEGSV"
    "YHEWCETYASSWYREAMDEGEKLLNHILETYPPEQLDTLVTIYAEVCELETNFWTAALEYE"
)

# THI20 functional positions (1-based) and expected residue
THI20_SITES = [
    (64, "Q", "BINDING HMP substrate (N-term kinase domain)"),
    (468, "C", "ACT_SITE nucleophile (C-term TenA/thiaminase-II)"),
    (540, "E", "ACT_SITE proton donor (C-term TenA/thiaminase-II)"),
]


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -5
    aligner.extend_gap_score = -0.5

    aln = aligner.align(THI22, THI20)[0]
    a22, a20 = aln[0], aln[1]

    ident = sum(1 for x, y in zip(a22, a20) if x == y and x != "-")
    alnlen = sum(1 for x, y in zip(a22, a20) if x != "-" and y != "-")
    print(f"THI22 length: {len(THI22)}  THI20 length: {len(THI20)}")
    print(f"Identity: {ident}/{alnlen} = {100 * ident / alnlen:.1f}% over aligned positions\n")

    def map_thi20_to_thi22(pos20: int):
        c20 = c22 = 0
        for x, y in zip(a22, a20):
            if y != "-":
                c20 += 1
            if x != "-":
                c22 += 1
            if c20 == pos20 and y != "-":
                return (y, x, c22 if x != "-" else None)
        return (None, None, None)

    all_conserved = True
    for pos, expect, name in THI20_SITES:
        res20, res22, p22 = map_thi20_to_thi22(pos)
        conserved = res22 == expect
        all_conserved &= conserved
        flag = "CONSERVED" if conserved else "CHANGED"
        print(
            f"THI20 {pos} ({name}): THI20={res20} -> THI22={res22} "
            f"(THI22 pos {p22}) [{flag}]"
        )

    print()
    print(
        "All three THI20 functional residues are conserved in THI22"
        if all_conserved
        else "NOTE: one or more THI20 functional residues are NOT conserved in THI22"
    )


if __name__ == "__main__":
    main()
