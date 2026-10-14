"""Compare zebrafish vcla (B3DI32) and vclb (A0A0S2I7K2) with human VCL isoforms.

Reproducible: reads the cached UniProt records for the zebrafish proteins and
fetches human P18206 isoforms from the UniProt REST API. Reports:
  * pairwise global identity of each zebrafish protein to human vinculin and
    metavinculin isoforms;
  * whether each zebrafish protein carries the metavinculin-specific insert
    (region of human metavinculin absent from the 1066-aa vinculin isoform);
  * the residue aligned to human vinculin Y822 (numbering of the 1066-aa isoform)
    and to key residues named in the literature (A50, Y100, S1033, S1045, Y1065).
Run: uv run python genes/DANRE/vcla/vcla-bioinformatics/compare_vinculins.py
"""
import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def fetch_fasta(url: str) -> dict[str, str]:
    data = urllib.request.urlopen(url, timeout=60).read().decode()
    out, name = {}, None
    for line in data.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            out[name] = ""
        elif name:
            out[name] += line.strip()
    return out


def aligner():
    a = Align.PairwiseAligner(mode="global")
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def pos_map(aln):
    """map query (target=seq0) positions (1-based) to seq1 residue or '-'."""
    s0, s1 = aln[0], aln[1]
    m, i = {}, 0
    for c0, c1 in zip(s0, s1):
        if c0 != "-":
            i += 1
            m[i] = c1
    return m


def ident(aln):
    s0, s1 = aln[0], aln[1]
    cols = len(s0)
    same = sum(1 for x, y in zip(s0, s1) if x == y and x != "-")
    return 100.0 * same / cols, cols


def main():
    zf = {
        "vcla_B3DI32": uniprot_txt_seq(ROOT / "genes/DANRE/vcla/vcla-uniprot.txt"),
        "vclb_A0A0S2I7K2": uniprot_txt_seq(ROOT / "genes/DANRE/vclb/vclb-uniprot.txt"),
    }
    hs = fetch_fasta(
        "https://rest.uniprot.org/uniprotkb/stream?query=accession:P18206"
        "&includeIsoform=true&format=fasta"
    )
    al = aligner()
    print("Lengths:", {k: len(v) for k, v in {**zf, **hs}.items()})
    hs_short = min(hs.items(), key=lambda kv: abs(len(kv[1]) - 1066))
    hs_long = max(hs.items(), key=lambda kv: len(kv[1]))
    print(f"Human vinculin isoform used for numbering: {hs_short[0]} ({len(hs_short[1])} aa)")
    print(f"Human longest isoform (metavinculin): {hs_long[0]} ({len(hs_long[1])} aa)")
    for hn, hseq in hs.items():
        for zn, zseq in zf.items():
            aln = al.align(hseq, zseq)[0]
            pid, cols = ident(aln)
            print(f"identity {zn} vs {hn}: {pid:.1f}% over {cols} columns")
    a = al.align(zf["vcla_B3DI32"], zf["vclb_A0A0S2I7K2"])[0]
    pid, cols = ident(a)
    print(f"identity vcla vs vclb: {pid:.1f}% over {cols} columns")

    # metavinculin insert: human long-isoform positions absent from short isoform
    a_ls = al.align(hs_long[1], hs_short[1])[0]
    lmap = pos_map(a_ls)
    insert = [p for p, c in lmap.items() if c == "-"]
    if insert:
        print(f"Metavinculin-specific region in {hs_long[0]}: {insert[0]}-{insert[-1]} ({len(insert)} aa)")
    for zn, zseq in zf.items():
        aln = al.align(hs_long[1], zseq)[0]
        m = pos_map(aln)
        covered = sum(1 for p in insert if m.get(p, "-") != "-")
        same = sum(1 for p in insert if m.get(p) == hs_long[1][p - 1])
        print(f"{zn}: aligned residues in metavinculin insert {covered}/{len(insert)}, identical {same}")

    # key residues (numbering of 1066-aa human vinculin)
    keys = [50, 100, 822, 1033, 1045, 1065]
    for zn, zseq in zf.items():
        aln = al.align(hs_short[1], zseq)[0]
        m = pos_map(aln)
        res = ", ".join(f"{hs_short[1][k-1]}{k}->{m.get(k)}" for k in keys)
        print(f"{zn} residues aligned to human vinculin: {res}")


if __name__ == "__main__":
    main()
