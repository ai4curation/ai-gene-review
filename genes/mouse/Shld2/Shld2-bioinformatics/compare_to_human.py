"""Global alignment of mouse Shld2 (Q3UEN2) against human SHLD2 isoforms.

Reads sequences from the local UniProt flat file (mouse; human canonical
835-aa form) and the human isoform-2 FASTA (904-aa long form), aligns them
with BLOSUM62 global alignment, and reports overall and region-level identity,
plus whether mouse carries the 69-residue OB-fold-B exon absent from the
human 835-aa form.

Run from the repository root:
    uv run python genes/mouse/Shld2/Shld2-bioinformatics/compare_to_human.py
"""

from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]


def uniprot_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("SQ "))
    seq = []
    for l in lines[start + 1 :]:
        if l.startswith("//"):
            break
        seq.append(l.replace(" ", ""))
    return "".join(seq)


def fasta_seq(path: Path) -> str:
    return "".join(l.strip() for l in path.read_text().splitlines() if not l.startswith(">"))


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def column_pairs(aln):
    """Yield (query_pos, target_pos) 1-based or None for gaps, per column."""
    s1, s2 = aln[0], aln[1]
    i = j = 0
    for c1, c2 in zip(s1, s2):
        p1 = p2 = None
        if c1 != "-":
            i += 1
            p1 = i
        if c2 != "-":
            j += 1
            p2 = j
        yield p1, p2, c1, c2


def region_identity(aln, start: int, end: int) -> tuple[int, int]:
    """Identity over target (human) positions start..end inclusive."""
    ident = total = 0
    for _p1, p2, c1, c2 in column_pairs(aln):
        if p2 is not None and start <= p2 <= end:
            total += 1
            if c1 == c2:
                ident += 1
    return ident, total


def main() -> None:
    mouse = uniprot_seq(ROOT / "genes/mouse/Shld2/Shld2-uniprot.txt")
    human_short = uniprot_seq(ROOT / "genes/human/SHLD2/SHLD2-uniprot.txt")
    human_long = fasta_seq(ROOT / "genes/human/SHLD2/SHLD2-isoform2.fasta")
    print(f"mouse Q3UEN2 length: {len(mouse)}")
    print(f"human Q86V20-1 (displayed) length: {len(human_short)}")
    print(f"human Q86V20-2 (long form) length: {len(human_long)}")
    a = aligner()
    for name, human in [("Q86V20-1", human_short), ("Q86V20-2", human_long)]:
        aln = a.align(mouse, human)[0]
        cols = list(column_pairs(aln))
        ident = sum(1 for _, _, c1, c2 in cols if c1 == c2 and c1 != "-")
        aligned = sum(1 for p1, p2, _, _ in cols if p1 and p2)
        gaps_mouse = sum(1 for p1, p2, _, _ in cols if p1 is None)
        gaps_human = sum(1 for p1, p2, _, _ in cols if p2 is None)
        print(f"\n== mouse vs human {name}")
        print(f"identical positions: {ident}; aligned pairs: {aligned}; "
              f"identity over aligned pairs: {ident / aligned:.3f}")
        print(f"human residues opposite mouse gaps: {gaps_mouse}; mouse residues opposite human gaps: {gaps_human}")
        for label, s, e in [("N-terminal SHLD3/REV7-binding segment (human 1-60)", 1, 60),
                            ("C-terminal OB-fold region (human long-form 421-end)", 421, len(human))]:
            if name == "Q86V20-1" and s == 421:
                continue
            i, t = region_identity(aln, s, e)
            print(f"{label}: {i}/{t} = {i / t:.3f}")
    # Where does the 69-aa exon lie? Align short vs long human; find the human-long gap block.
    hh = a.align(human_short, human_long)[0]
    block = [p2 for p1, p2, _, _ in column_pairs(hh) if p1 is None and p2 is not None]
    if block:
        print(f"\nhuman long-form residues absent from 835-aa form: {block[0]}-{block[-1]} ({len(block)} aa)")
        aln = a.align(mouse, human_long)[0]
        i, t = region_identity(aln, block[0], block[-1])
        covered = sum(1 for p1, p2, _, _ in column_pairs(aln) if p2 and block[0] <= p2 <= block[-1] and p1)
        print(f"mouse residues aligned to that exon: {covered}/{len(block)}; identity {i}/{t} = {i / t:.3f}")


if __name__ == "__main__":
    main()
