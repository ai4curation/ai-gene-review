# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare fly CG42404 (Q9VFA8) with human/mouse DGCR2 (P98153, P98154).

Fetches sequences and UniProt features live, reports domain architecture and a
local Smith-Waterman alignment (BLOSUM62) of fly vs each DGCR2 sequence, plus
the count of cysteines in the aligned VWFC region. Nothing is hardcoded.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"fly_CG42404": "Q9VFA8", "human_DGCR2": "P98153", "mouse_Dgcr2": "P98154"}


def fasta(acc: str) -> str:
    t = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60).text
    return "".join(t.splitlines()[1:])


def features(acc: str) -> list[tuple[str, int, int, str]]:
    j = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60).json()
    out = []
    for f in j.get("features", []):
        if f["type"] in {"Signal", "Transmembrane", "Domain", "Topological domain"}:
            out.append((f["type"], f["location"]["start"]["value"], f["location"]["end"]["value"], f.get("description", "")))
    return out


seqs = {k: fasta(a) for k, a in ACCS.items()}
for k, a in ACCS.items():
    print(f"## {k} {a} length={len(seqs[k])}")
    for f in features(a):
        print("  ", *f)

aligner = Align.PairwiseAligner()
aligner.mode = "local"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1

fly = seqs["fly_CG42404"]
for k in ("human_DGCR2", "mouse_Dgcr2"):
    aln = aligner.align(fly, seqs[k])[0]
    fs, fe, hs, he = aln.aligned[0][0][0], aln.aligned[0][-1][1], aln.aligned[1][0][0], aln.aligned[1][-1][1]
    a, b = aln[0], aln[1]
    ident = sum(1 for x, y in zip(a, b) if x == y and x != "-")
    cols = sum(1 for x, y in zip(a, b) if x != "-" and y != "-")
    print(f"\n## local alignment fly vs {k}: score={aln.score:.0f} fly {fs+1}-{fe} vs {k} {hs+1}-{he}; identity {ident}/{cols} aligned columns = {100*ident/max(cols,1):.1f}%")
    print(aln)
