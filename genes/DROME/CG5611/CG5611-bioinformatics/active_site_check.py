# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Pairwise global alignment of CG5611 (Q9VB17) against characterised crotonase-fold
enzymes, reporting which CG5611 residue aligns to each reference catalytic/binding
position. Positions are taken from the reference UniProt feature tables (fetched live).

Usage: uv run active_site_check.py > active_site_check.out
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q9VB17"
# reference accession -> positions of interest (from UniProt FT lines; see fetch_features)
REFS = ["P14604", "Q93TU6", "Q9VG69", "Q2LXU2"]


def fetch(acc: str) -> str:
    return requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).text


def seq_of(txt: str) -> str:
    s = txt.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", s)


def features(txt: str) -> list[tuple[str, int]]:
    out = []
    for m in re.finditer(r"^FT   (ACT_SITE|BINDING|SITE)\s+(\d+)\s*$", txt, re.M):
        out.append((m.group(1), int(m.group(2))))
    return out


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    t = seq_of(fetch(TARGET))
    print(f"target {TARGET} length {len(t)}")
    for acc in REFS:
        txt = fetch(acc)
        r = seq_of(txt)
        aln = aligner.align(t, r)[0]
        # map ref position -> target position
        rmap = {}
        ident = aligned = 0
        for (ts, te), (rs, re_) in zip(*aln.aligned):
            for k in range(te - ts):
                rmap[rs + k + 1] = ts + k + 1
                aligned += 1
                ident += t[ts + k] == r[rs + k]
        print(f"\n== {acc} length {len(r)}; aligned {aligned}, identity {ident/aligned:.1%} over aligned columns")
        for kind, pos in features(txt):
            tp = rmap.get(pos)
            tres = t[tp - 1] if tp else "-"
            print(f"  {kind:8s} ref {r[pos-1]}{pos} -> CG5611 {tres}{tp if tp else ''}")
        if acc == "P14604":
            for pos in (141, 144, 164):
                tp = rmap.get(pos)
                print(f"  ECHS1 catalytic-core ref {r[pos-1]}{pos} -> CG5611 {t[tp-1] + str(tp) if tp else 'gap'}")


if __name__ == "__main__":
    main()
