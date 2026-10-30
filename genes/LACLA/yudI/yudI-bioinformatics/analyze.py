"""Compare the KBase query CP006766.1_2177 / UniProt Q9CE84 with reference Dus enzymes.

1. Exact differences between the dashboard query and Q9CE84.
2. Global pairwise identity (BLOSUM62, gap open -10, extend -0.5) to E. coli
   DusA/DusB/DusC, B. subtilis Dus1/Dus2, M. capricolum DusB and L. lactis MG1363.
3. Map E. coli DusB (P0ABT5) UniProt active site and FMN-binding positions onto Q9CE84.

Run: uv run python analyze.py > analysis_output.txt
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
DATA = HERE / "data"

NAMES = {
    "Q9CE84": "L. lactis IL1403 YudI (this review)",
    "A2RN88": "L. lactis MG1363 llmg_2209",
    "P0ABT5": "E. coli DusB",
    "P32695": "E. coli DusA",
    "P33371": "E. coli DusC",
    "P37567": "B. subtilis Dus1 (BSU00810)",
    "O31546": "B. subtilis Dus2 (BSU08030)",
    "Q2SR34": "M. capricolum DusB (MCAP_0837)",
}

# UniProt P0ABT5 features: ACT_SITE 100 (proton donor); FMN binding 16-18, 70, 139, 200-202, 224-225
ECOLI_DUSB_SITES = {
    "ACT_SITE proton donor": [100],
    "FMN binding 16-18": [16, 17, 18],
    "FMN binding 70": [70],
    "FMN binding 139": [139],
    "FMN binding 200-202": [200, 201, 202],
    "FMN binding 224-225": [224, 225],
}


def load(acc: str) -> str:
    return str(next(SeqIO.parse(DATA / f"{acc}.fasta", "fasta")).seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def identity(aln) -> tuple[float, int, int]:
    s1, s2 = aln[0], aln[1]
    cols = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    same = sum(1 for x, y in cols if x == y)
    shorter = min(len(s1.replace("-", "")), len(s2.replace("-", "")))
    return 100 * same / shorter, same, len(cols)


def position_map(aln) -> dict[int, int]:
    """Map 1-based positions of sequence 2 to 1-based positions of sequence 1."""
    m = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for k in range(e2 - s2):
            m[s2 + k + 1] = s1 + k + 1
    return m


def main() -> None:
    query = str(next(SeqIO.parse(DATA / "query_CP006766.1_2177.fasta", "fasta")).seq)
    target = load("Q9CE84")
    print("## 1. Dashboard query vs Q9CE84")
    print(f"query length {len(query)}, Q9CE84 length {len(target)}")
    diffs = [(i + 1, a, b) for i, (a, b) in enumerate(zip(query, target)) if a != b]
    for pos, a, b in diffs:
        print(f"  position {pos}: query {a} / Q9CE84 {b}")
    print(f"identity {100 * (len(query) - len(diffs)) / len(query):.1f}% ({len(diffs)} difference(s))\n")

    al = aligner()
    print("## 2. Global identity of Q9CE84 to reference Dus proteins")
    print("(identical residues / length of shorter sequence)")
    for acc, name in NAMES.items():
        if acc == "Q9CE84":
            continue
        aln = al.align(target, load(acc))[0]
        pct, same, cols = identity(aln)
        print(f"  {acc:7s} {name:36s} {pct:5.1f}%  ({same}/{cols} aligned columns)")
    print()
    print("## 2b. B. subtilis Dus1/Dus2 vs M. capricolum DusB (Mollicutes retain DusB1)")
    for acc in ("P37567", "O31546"):
        aln = al.align(load("Q2SR34"), load(acc))[0]
        print(f"  Q2SR34 vs {acc} {NAMES[acc]:30s} {identity(aln)[0]:5.1f}%")
    print()

    print("## 3. E. coli DusB (P0ABT5) functional residues mapped onto Q9CE84")
    ecoli = load("P0ABT5")
    aln = al.align(target, ecoli)[0]
    pmap = position_map(aln)
    for label, positions in ECOLI_DUSB_SITES.items():
        parts = []
        for p in positions:
            q = pmap.get(p)
            qres = target[q - 1] if q else "-"
            parts.append(f"{ecoli[p - 1]}{p}->{qres}{q if q else ''}")
        print(f"  {label:24s} " + ", ".join(parts))
    print()
    print("Alignment Q9CE84 (top) vs E. coli DusB P0ABT5 (bottom):")
    print(aln)


if __name__ == "__main__":
    main()
