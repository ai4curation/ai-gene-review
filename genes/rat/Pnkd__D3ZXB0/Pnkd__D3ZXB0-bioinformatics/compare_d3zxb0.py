# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Map rat Pnkd D3ZXB0 onto the reviewed mouse (Q69ZP3) and human (Q8N490) PNKD isoforms.

Fetches sequences live from UniProt REST, does global BLOSUM62 alignments, and reports
(i) identity per isoform, (ii) whether the MR-1S-specific exon segment is present,
(iii) conservation of the human Zn(2+) ligand positions and the PNKD disease residues
(A7, A9, A33) and (iv) Phobius-free hydrophobicity scan of residues 60-130.
Writes RESULTS-d3zxb0.md next to this script. Nothing is hardcoded.
"""
from pathlib import Path
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["D3ZXB0", "B4F7D2", "Q69ZP3", "Q69ZP3-2", "Q69ZP3-3", "Q69ZP3-4",
        "Q8N490", "Q8N490-2", "Q8N490-3", "Q8N490-4"]
HUMAN_ZN = [172, 174, 176, 177, 229, 253, 291]  # Q8N490 isoform 1 Zn ligand positions (UniProt FT BINDING)
DISEASE = {7: "A", 9: "A", 33: "A"}  # human A7V, A9V, A33P (Q8N490 isoform 1 numbering)
KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
          L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def pos_map(aln) -> dict[int, int]:
    """Map 1-based positions of seqB -> seqA."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            m[b0 + k + 1] = a0 + k + 1
    return m


REPO = Path(__file__).resolve().parents[4]


def paint_section() -> list[str]:
    """Report PAINT IBD rows for PTHR11935 (committed TSV) relevant to the HAGH/PNKD split."""
    tsv = REPO / "interpro/panther/PTHR11935/PTHR11935-paint.tsv"
    keep = {"GO:0004416", "GO:0016790", "GO:0005739", "GO:0006749", "GO:0051596"}
    lines = ["", "## PAINT IBD rows in PTHR11935 for the terms under review",
             f"Source: {tsv.relative_to(REPO)}", "",
             "| node | GO id | aspect | evidence | seeds | taxon |", "|---|---|---|---|---|---|"]
    rows = [r.split("\t") for r in tsv.read_text().splitlines()[1:]]
    for r in rows:
        if r[2] in keep:
            lines.append(f"| {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[6]} | {r[7]} |")
    pnkd_seeds = [r[1] for r in rows if "Q8N490" in r[6]]
    lines.append("")
    lines.append(f"PAINT nodes seeded by human PNKD Q8N490: {', '.join(pnkd_seeds) if pnkd_seeds else 'none'}")
    return lines


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    q = seqs["D3ZXB0"]
    al = aligner()
    out = ["# D3ZXB0 (rat Pnkd canonical) vs reviewed mouse/human PNKD isoforms", "",
           "Sequences fetched live from UniProt REST; Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5.", "",
           "| Entry | Length | Identical residues | Identity over D3ZXB0 length |", "|---|---|---|---|"]
    for acc in ACCS[1:]:
        aln = al.align(q, seqs[acc])[0]
        ident = sum(1 for (a0, a1), (b0, b1) in zip(*aln.aligned)
                    for k in range(a1 - a0) if q[a0 + k] == seqs[acc][b0 + k])
        out.append(f"| {acc} | {len(seqs[acc])} | {ident} | {ident / len(q):.3f} |")

    # MR-1S-specific segment: residues of mouse isoform 2 (Q69ZP3-2) after the shared 1-79 exon
    s_tail = seqs["Q69ZP3-2"][79:]
    seg = s_tail[:39]
    out += ["", "## MR-1S-specific exon segment",
            f"Mouse Q69ZP3-2 residues 80-118: `{seg}`",
            f"Exact substring of D3ZXB0: {seg in q}; position in D3ZXB0: {q.find(seg) + 1 if seg in q else 'n/a'}",
            f"D3ZXB0 residues 80-118: `{q[79:118]}`"]
    hseg = seqs["Q8N490-2"][79:118]
    aln = al.align(q[79:118], hseg)[0]
    hid = sum(1 for (a0, a1), (b0, b1) in zip(*aln.aligned) for k in range(a1 - a0) if q[79 + a0 + k] == hseg[b0 + k])
    out.append(f"Human Q8N490-2 residues 80-118: `{hseg}` (identical to D3ZXB0 80-118 at {hid}/39 aligned positions)")

    # Zn ligands and disease residues, mapped from human isoform 1 onto D3ZXB0
    aln = al.align(q, seqs["Q8N490"])[0]
    m = pos_map(aln)
    out += ["", "## Human Q8N490 Zn(2+) ligand and PNKD disease positions mapped onto D3ZXB0", "",
            "| Q8N490 position | Q8N490 residue | D3ZXB0 position | D3ZXB0 residue |", "|---|---|---|---|"]
    for p in sorted(HUMAN_ZN + list(DISEASE)):
        dp = m.get(p)
        out.append(f"| {p} | {seqs['Q8N490'][p - 1]} | {dp if dp else '-'} | {q[dp - 1] if dp else '-'} |")

    # Hydrophobicity scan (19-residue window, Kyte-Doolittle) over residues 60-140
    win = 19
    scores = [(i + 1, sum(KD[c] for c in q[i:i + win]) / win) for i in range(55, 140 - win)]
    best = max(scores, key=lambda x: x[1])
    out += ["", "## Kyte-Doolittle 19-residue window, D3ZXB0 residues 56-140",
            f"Maximum mean hydropathy {best[1]:.2f} for window starting at residue {best[0]} (`{q[best[0] - 1:best[0] - 1 + win]}`); values > 1.6 are conventionally taken as candidate transmembrane segments.",
            "", "N-terminal 40 residues of D3ZXB0 (region containing the reported mitochondrial targeting sequence of MR-1L/MR-1S):",
            f"`{q[:40]}`", "",
            ]
    out += paint_section()
    out += ["", "Interpretation is left to the review; alignment does not establish expression, localization or activity."]
    Path(__file__).with_name("RESULTS-d3zxb0.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
