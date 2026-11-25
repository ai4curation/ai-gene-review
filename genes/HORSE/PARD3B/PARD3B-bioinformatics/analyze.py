# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "biopython"]
# ///
"""Horse PARD3B (A0A9L0RMF2) evolutionary-grounding analysis.

1. Global alignment of horse A0A9L0RMF2 to human PARD3B (Q8TEW8), mouse Pard3b
   (Q9CSB4) and human PARD3 (Q8TEW0, other PANTHER subfamily) -> identity.
2. Check the aPKC-binding FXR / KR motif region: the PARD3 peptide around S827
   (human PARD3 numbering) is located in the alignment with human PARD3 and the
   corresponding horse residues printed.
3. Experimental (non-IEA, non-IBA) GO annotations from QuickGO for human
   PARD3B and mouse Pard3b.

Run: uv run --script analyze.py > analyze_output.txt
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HORSE = "A0A9L0RMF2"
COMPARE = {
    "Q8TEW8": "human PARD3B (PTHR16484:SF4)",
    "Q9CSB4": "mouse Pard3b (PTHR16484:SF4)",
    "Q8TEW0": "human PARD3 (PTHR16484:SF10)",
}
EXP_CODES = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HDA", "HMP", "TAS", "NAS", "IC"}


def fasta(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def subfamily(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    xs = [
        x["id"]
        for x in r.json().get("uniProtKBCrossReferences", [])
        if x["database"] == "PANTHER"
    ]
    return ",".join(xs)


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def identity(aln) -> tuple[int, int, float]:
    s1, s2 = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    ident = sum(1 for x, y in pairs if x == y)
    return ident, len(pairs), 100.0 * ident / len(pairs)


def map_positions(aln, start: int, end: int) -> str:
    """Return horse residues aligned to positions start..end (1-based) of target (row 1)."""
    s_h, s_t = aln[0], aln[1]
    ti = 0
    out = []
    for x, y in zip(s_h, s_t):
        if y != "-":
            ti += 1
        if start <= ti <= end and y != "-":
            out.append((ti, y, x))
    return " ".join(f"{t}{y}->{x}" for t, y, x in out)


def segment_identity(aln, start: int, end: int) -> str:
    """Identity over horse positions start..end (1-based) against the aligned partner (row 1)."""
    s_h, s_t = aln[0], aln[1]
    hi = 0
    same = total = 0
    for x, y in zip(s_h, s_t):
        if x != "-":
            hi += 1
            if start <= hi <= end:
                total += 1
                same += int(x == y)
    return f"{same}/{total} identical ({100.0 * same / total:.1f}%)"


def indels(aln) -> str:
    """Summarise gap runs: +N at horse position = horse insertion; -N = horse deletion."""
    s_h, s_t = aln[0], aln[1]
    hi = 0
    runs = []
    cur = None
    for x, y in zip(s_h, s_t):
        if x != "-":
            hi += 1
        kind = "+" if y == "-" else ("-" if x == "-" else None)
        if kind and cur and cur[0] == kind:
            cur[2] += 1
        elif kind:
            cur = [kind, hi, 1]
            runs.append(cur)
        else:
            cur = None
    return " ".join(f"{k}{n}@{p}" for k, p, n in runs if n >= 3)


def experimental_go(acc: str) -> list[str]:
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId={acc}&limit=200"
    )
    r = requests.get(url, headers={"Accept": "application/json"}, timeout=60)
    r.raise_for_status()
    rows = []
    for a in r.json()["results"]:
        if a["goEvidence"] in EXP_CODES:
            rows.append(
                f"{acc}\t{a['qualifier']}\t{a['goId']}\t{a['goEvidence']}\t{a['reference']}\t{a.get('withFrom')}"
            )
    return sorted(set(rows))


def main() -> None:
    horse = fasta(HORSE)
    print(f"horse {HORSE} length={len(horse)} PANTHER={subfamily(HORSE)}")
    al = aligner()
    for acc, name in COMPARE.items():
        seq = fasta(acc)
        aln = al.align(horse, seq)[0]
        ident, n, pct = identity(aln)
        print(
            f"{acc} {name} length={len(seq)} PANTHER={subfamily(acc)} "
            f"aligned_pairs={n} identical={ident} identity={pct:.1f}%"
        )
        print("  indels (horse_pos:len, + = extra horse residues, - = horse gap):", indels(aln))
        if acc in ("Q8TEW8", "Q9CSB4"):
            print("  horse inter-PDZ2/PDZ3 linker (horse 488-528; LKB1-binding region in mouse Par3L):", segment_identity(aln, 488, 528))
        if acc == "Q8TEW8":
            print("  horse residues aligned to human PARD3B 740-752 (14-3-3 site S746):")
            print("  " + map_positions(aln, 740, 752))
        if acc == "Q8TEW0":
            print("  horse residues aligned to human PARD3 815-835 (aPKC-binding FXR/S827/KR region):")
            print("  " + map_positions(aln, 815, 835))
    print("\nExperimental GO annotations (QuickGO, non-electronic, non-IBA):")
    for acc in ("Q8TEW8", "Q9CSB4"):
        rows = experimental_go(acc)
        if not rows:
            print(f"{acc}\t(none)")
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
