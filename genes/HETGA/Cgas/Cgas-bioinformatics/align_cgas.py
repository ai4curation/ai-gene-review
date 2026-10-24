"""Map functionally annotated human cGAS residues onto naked mole-rat cGAS.

Question: the GO annotations on naked mole-rat cGAS (UniProt A0AAX6RS70) are all
TreeGrafter propagations from the PANTHER ancestral node PTN000069395. The key
biochemical claim carried by that propagation is 2',3'-cyclic GMP-AMP synthase
activity (GO:0061501). Before accepting or rejecting it we want to know whether
the naked mole-rat protein retains the catalytic and DNA-binding machinery that
UniProt has experimentally annotated on the human enzyme (Q8N884).

The script does a global pairwise alignment of the naked mole-rat protein against
human and mouse cGAS, then transfers every UniProt ``ACT_SITE``/``BINDING``/``SITE``
position from the reference onto the naked mole-rat sequence and reports whether
the residue is identical, similar, or substituted.

It also reports the alignment mapping for the four C-terminal positions named in
secondary coverage of Chen et al. 2025 (S463, E511, Y527, T530), so that those
claims can be checked rather than repeated.

Nothing here is hardcoded: all residues come from the fetched UniProt records in
``data/``. Run with ``uv run python align_cgas.py``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

DATA = Path(__file__).parent / "data"

TARGET = DATA / "A0AAX6RS70_hetga_Cgas.txt"
REFERENCES = [
    ("human", DATA / "Q8N884_human_CGAS.txt"),
    ("mouse", DATA / "Q8C6L5_mouse_Cgas.txt"),
]

# Positions named in secondary coverage of Chen et al. 2025 (Science 390:eadp5056)
# as the four residues that differ in naked mole-rat cGAS. The primary abstract
# does NOT name them, so these are reported for checking, not asserted.
REPORTED_DIVERGENT_POSITIONS = [463, 511, 527, 530]


@dataclass
class Feature:
    kind: str
    start: int  # 1-based, inclusive
    end: int
    note: str


def parse_sequence(path: Path) -> str:
    text = path.read_text()
    seq_block = text.split("\nSQ   ", 1)[1]
    lines = seq_block.splitlines()[1:]
    return "".join(line.replace(" ", "") for line in lines if not line.startswith("//"))


def parse_features(path: Path, kinds: set[str]) -> list[Feature]:
    """Parse UniProt FT lines of the given kinds, collapsing continuation lines."""
    features: list[Feature] = []
    current_kind: str | None = None
    current_range: tuple[int, int] | None = None
    notes: list[str] = []

    def flush() -> None:
        if current_kind and current_range:
            note = " ".join(notes)
            features.append(Feature(current_kind, current_range[0], current_range[1], note))

    for line in path.read_text().splitlines():
        if not line.startswith("FT   "):
            continue
        header = re.match(r"^FT   ([A-Z_]+)\s+(<?\d+)(?:\.\.(>?\d+))?", line)
        if header:
            flush()
            notes = []
            kind = header.group(1)
            if kind not in kinds:
                current_kind, current_range = None, None
                continue
            start = int(header.group(2).lstrip("<"))
            end = int(header.group(3).lstrip(">")) if header.group(3) else start
            current_kind, current_range = kind, (start, end)
        elif current_kind:
            payload = line[21:].strip()
            if payload.startswith("/note=") or payload.startswith("/ligand=") or payload.startswith("/ligand_note="):
                notes.append(payload)
    flush()
    return features


def align(ref_seq: str, target_seq: str) -> Align.Alignment:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aligner.target_end_gap_score = 0.0
    aligner.query_end_gap_score = 0.0
    return aligner.align(ref_seq, target_seq)[0]


def position_map(alignment: Align.Alignment) -> dict[int, int | None]:
    """Map 1-based reference positions to 1-based target positions (None if gapped)."""
    mapping: dict[int, int | None] = {}
    ref_aln, tgt_aln = alignment[0], alignment[1]
    ref_i = tgt_i = 0
    for a, b in zip(ref_aln, tgt_aln):
        if a != "-":
            ref_i += 1
        if b != "-":
            tgt_i += 1
        if a != "-":
            mapping[ref_i] = tgt_i if b != "-" else None
    return mapping


def percent_identity(alignment: Align.Alignment) -> float:
    ref_aln, tgt_aln = alignment[0], alignment[1]
    matches = sum(1 for a, b in zip(ref_aln, tgt_aln) if a == b and a != "-")
    aligned = sum(1 for a, b in zip(ref_aln, tgt_aln) if a != "-" and b != "-")
    return 100.0 * matches / aligned


def main() -> None:
    target_seq = parse_sequence(TARGET)
    print(f"naked mole-rat A0AAX6RS70: {len(target_seq)} aa\n")

    for label, path in REFERENCES:
        ref_seq = parse_sequence(path)
        alignment = align(ref_seq, target_seq)
        mapping = position_map(alignment)

        print("=" * 78)
        print(f"{label} cGAS ({path.stem.split('_')[0]}): {len(ref_seq)} aa")
        print(f"global identity over aligned columns: {percent_identity(alignment):.1f}%")
        print("=" * 78)

        feats = parse_features(path, {"ACT_SITE", "BINDING", "SITE"})
        # single-residue features only; ranges are reported separately
        singles = [f for f in feats if f.start == f.end]
        seen: set[int] = set()
        conserved = substituted = gapped = 0
        print(f"\n{'ref pos':>8} {'ref':>3}  {'nmr pos':>8} {'nmr':>3}  status   annotation")
        print("-" * 78)
        for f in singles:
            if f.start in seen:
                continue
            seen.add(f.start)
            ref_aa = ref_seq[f.start - 1]
            tgt_pos = mapping.get(f.start)
            if tgt_pos is None:
                status, tgt_aa = "GAP", "-"
                gapped += 1
            else:
                tgt_aa = target_seq[tgt_pos - 1]
                if tgt_aa == ref_aa:
                    status = "same"
                    conserved += 1
                else:
                    status = "DIFF"
                    substituted += 1
            notes = "; ".join(n.replace("/note=", "").replace("/ligand=", "").strip('"') for n in f.note.split('" '))
            print(f"{f.start:>8} {ref_aa:>3}  {str(tgt_pos):>8} {tgt_aa:>3}  {status:<7}  {f.kind}: {notes[:60]}")
        print("-" * 78)
        print(f"annotated single-residue sites: {conserved} identical, {substituted} substituted, {gapped} gapped")

        # Zinc thumb / DNA-binding regions, reported as block identity
        regions = parse_features(path, {"REGION", "MOTIF", "ZN_FING"})
        print("\nblock identity over annotated regions:")
        for f in regions:
            if "Disordered" in f.note:
                continue
            pairs = [
                (ref_seq[p - 1], target_seq[mapping[p] - 1])
                for p in range(f.start, f.end + 1)
                if mapping.get(p) is not None
            ]
            if not pairs:
                continue
            ident = 100.0 * sum(1 for a, b in pairs if a == b) / len(pairs)
            note = f.note.replace("/note=", "").strip('"')[:52]
            print(f"  {f.start:>4}-{f.end:<4} {f.kind:<7} {ident:5.1f}% ({len(pairs)}/{f.end - f.start + 1} aligned)  {note}")

        # Which reference residue aligns to each naked mole-rat position named in
        # secondary coverage of Chen et al. 2025? Invert the map to find out.
        inverse = {t: r for r, t in mapping.items() if t is not None}
        print(f"\npositions reported in secondary coverage of Chen et al. 2025, read in")
        print(f"naked mole-rat numbering, with the aligned {label} residue:")
        for p in REPORTED_DIVERGENT_POSITIONS:
            nmr_aa = target_seq[p - 1] if p <= len(target_seq) else "-"
            ref_pos = inverse.get(p)
            ref_aa = ref_seq[ref_pos - 1] if ref_pos else "-"
            print(
                f"  nmr[{p}]={nmr_aa}   <->   {label}[{ref_pos}]={ref_aa}"
            )
        print()


if __name__ == "__main__":
    main()
