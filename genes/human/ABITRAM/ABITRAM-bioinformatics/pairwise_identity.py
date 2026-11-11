#!/usr/bin/env python3
"""Reproducible global Needleman-Wunsch pairwise sequence identity for PTHR13651 members.

Computes exact global pairwise alignments across all eight PANTHER:PTHR13651
(subfamily PTHR13651:SF0, PROTEIN ABITRAM) orthologs referenced in the PR #6273
family and gene reviews:
  - Q9NX38 (Homo sapiens ABITRAM, 181 aa)
  - Q80ZQ9 (Mus musculus Abitram, 193 aa)
  - D4AE08 (Rattus norvegicus Abitram, 193 aa)
  - Q1LU93 (Danio rerio abitram, 177 aa)
  - Q9VFR1 (Drosophila melanogaster abitram / CG9288, 214 aa)
  - P34452 (Caenorhabditis elegans F54F2.7, 157 aa)
  - Q54TD9 (Dictyostelium discoideum abitram, 175 aa)
  - Q581S9 (Trypanosoma brucei Q581S9, 197 aa)

Alignment method & parameters (EMBOSS needle global Needleman-Wunsch defaults):
  - Engine: Bio.Align.PairwiseAligner(mode="global")
  - Substitution matrix: BLOSUM62
  - Affine gap penalties: open_gap_score = -10.0, extend_gap_score = -0.5
  - Global % identity denominator: alignment length (columns including internal
    and terminal gaps, matching EMBOSS needle). Gap-excluded % identity
    (identical residues / aligned residue-to-residue columns) is also tabulated.

Usage:
  PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/cjm/repos/ai-gene-review/.venv \\
    UV_NO_SYNC=1 UV_FROZEN=1 PYTHONDONTWRITEBYTECODE=1 \\
    /Users/cjm/repos/ai-gene-review/.venv/bin/python \\
    genes/human/ABITRAM/ABITRAM-bioinformatics/pairwise_identity.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

import Bio
from Bio.Align import PairwiseAligner, substitution_matrices


REPO_ROOT = Path(__file__).resolve().parents[4]
BIOINFO_DIR = Path(__file__).resolve().parent
OUTGROUPS_FASTA = BIOINFO_DIR / "inputs" / "non_chordate_outgroups.fasta"
SEQ_CACHE_DIR = REPO_ROOT / ".cache" / "uniprot_seq"
RESULTS_PATH = BIOINFO_DIR / "RESULTS.md"


@dataclass(frozen=True)
class MemberSpec:
    accession: str
    gene_symbol: str
    organism: str
    uniprot_relpath: str | None


MEMBERS: tuple[MemberSpec, ...] = (
    MemberSpec("Q9NX38", "ABITRAM", "Homo sapiens", "genes/human/ABITRAM/ABITRAM-uniprot.txt"),
    MemberSpec("Q80ZQ9", "Abitram", "Mus musculus", "genes/mouse/Abitram/Abitram-uniprot.txt"),
    MemberSpec("D4AE08", "Abitram", "Rattus norvegicus", "genes/rat/Abitram/Abitram-uniprot.txt"),
    MemberSpec("Q1LU93", "abitram", "Danio rerio", "genes/DANRE/abitram/abitram-uniprot.txt"),
    MemberSpec("Q9VFR1", "abitram", "Drosophila melanogaster", "genes/DROME/abitram/abitram-uniprot.txt"),
    MemberSpec("P34452", "F54F2.7", "Caenorhabditis elegans", "genes/worm/F54F2.7/F54F2.7-uniprot.txt"),
    MemberSpec("Q54TD9", "abitram", "Dictyostelium discoideum", None),
    MemberSpec("Q581S9", "Q581S9", "Trypanosoma brucei", None),
)


def parse_uniprot_flatfile(path: Path) -> tuple[str, int, str]:
    """Extract primary accession, sequence version, and sequence from a UniProt .txt record."""
    text = path.read_text(encoding="utf-8")
    ac_match = re.search(r"^AC\s+([A-Z0-9]+);", text, re.MULTILINE)
    sv_match = re.search(r"^DT\s+\S+,\s+sequence version (\d+)\.", text, re.MULTILINE)
    sq_match = re.search(
        r"^SQ\s+SEQUENCE\s+(\d+)\s+AA;.*?\n((?:^ {5}[A-Z ]+\n)+)^//",
        text,
        re.MULTILINE,
    )
    if not ac_match or not sv_match or not sq_match:
        raise ValueError(f"Could not parse accession/version/sequence from {path}")
    acc = ac_match.group(1)
    sv = int(sv_match.group(1))
    expected_len = int(sq_match.group(1))
    seq = re.sub(r"\s+", "", sq_match.group(2))
    if len(seq) != expected_len:
        raise ValueError(f"{path}: expected {expected_len} aa, parsed {len(seq)} aa")
    return acc, sv, seq


def parse_outgroups_fasta(path: Path) -> dict[str, tuple[int, str]]:
    """Parse pinned FASTA entries formatted as >UniProtKB:ACC|...|sv=N|len=L."""
    records: dict[str, tuple[int, str]] = {}
    current_acc: str | None = None
    current_sv: int = 1
    current_len: int = 0
    chunks: list[str] = []

    def flush() -> None:
        if current_acc is not None:
            seq = "".join(chunks)
            if len(seq) != current_len:
                raise ValueError(f"{current_acc}: expected {current_len} aa, got {len(seq)} aa")
            records[current_acc] = (current_sv, seq)

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(">"):
            flush()
            chunks = []
            m = re.match(r"^>UniProtKB:([A-Z0-9]+)\|.*\|sv=(\d+)\|len=(\d+)$", line)
            if not m:
                raise ValueError(f"Malformed FASTA header: {line}")
            current_acc = m.group(1)
            current_sv = int(m.group(2))
            current_len = int(m.group(3))
        else:
            chunks.append(line)
    flush()
    return records


def load_sequences() -> list[tuple[MemberSpec, int, str, str]]:
    """Load all member sequences and verify cache consistency where available."""
    outgroups = parse_outgroups_fasta(OUTGROUPS_FASTA)
    loaded: list[tuple[MemberSpec, int, str, str]] = []
    for spec in MEMBERS:
        if spec.uniprot_relpath is not None:
            up_path = REPO_ROOT / spec.uniprot_relpath
            acc, sv, seq = parse_uniprot_flatfile(up_path)
            if acc != spec.accession:
                raise ValueError(f"Expected {spec.accession} in {up_path}, got {acc}")
            source = spec.uniprot_relpath
        else:
            sv, seq = outgroups[spec.accession]
            source = "genes/human/ABITRAM/ABITRAM-bioinformatics/inputs/non_chordate_outgroups.fasta"

        cache_seq_path = SEQ_CACHE_DIR / f"{spec.accession}.seq"
        if cache_seq_path.exists():
            cached_seq = cache_seq_path.read_text(encoding="utf-8").strip()
            if cached_seq != seq:
                raise ValueError(f"Cache mismatch for {spec.accession} against {source}")
        loaded.append((spec, sv, seq, source))
    return loaded


def make_aligner() -> PairwiseAligner:
    aligner = PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10.0
    aligner.extend_gap_score = -0.5
    return aligner


def pairwise_stats(aligner: PairwiseAligner, seq_a: str, seq_b: str) -> tuple[int, int, int, float, float, float]:
    """Return (identical, aligned_ungapped, aln_len, pct_global, pct_ungapped, score)."""
    alignment = aligner.align(seq_a, seq_b)[0]
    row_a, row_b = alignment[0], alignment[1]
    aln_len = len(row_a)
    identical = sum(1 for a, b in zip(row_a, row_b) if a == b and a != "-")
    aligned_ungapped = sum(1 for a, b in zip(row_a, row_b) if a != "-" and b != "-")
    pct_global = 100.0 * identical / aln_len
    pct_ungapped = 100.0 * identical / aligned_ungapped if aligned_ungapped else 0.0
    return identical, aligned_ungapped, aln_len, pct_global, pct_ungapped, float(alignment.score)


def main() -> None:
    loaded = load_sequences()
    aligner = make_aligner()

    lines: list[str] = [
        "# Pairwise Sequence Identity Analysis for PANTHER:PTHR13651 (PROTEIN ABITRAM)",
        "",
        "## Method and Provenance",
        "- **Script**: `genes/human/ABITRAM/ABITRAM-bioinformatics/pairwise_identity.py`",
        f"- **Biopython version**: `{Bio.__version__}` (`Bio.Align.PairwiseAligner`, `mode=\"global\"`)",
        "- **Parameters**: Needleman-Wunsch global alignment with `BLOSUM62` substitution matrix, `open_gap_score = -10.0`, `extend_gap_score = -0.5` (EMBOSS `needle` standard parameters).",
        "- **Denominator definitions**:",
        "  - **Global % Identity (`identical / aln_len`)**: Identical aligned residues divided by full global alignment length including terminal and internal gaps (primary reported figure).",
        "  - **Aligned-Residue % Identity (`identical / ungapped_cols`)**: Identical aligned residues divided by residue-to-residue aligned columns excluding gaps (captures conservation across the shared `IPR039169` / `PF01597` barrel-sandwich hybrid core when terminal tail lengths differ).",
        "",
        "## Input Sequences (`PANTHER:PTHR13651:SF0`)",
        "",
        "| Accession | Symbol | Organism | Length (aa) | Seq Version | Source |",
        "|---|---|---|---:|---:|---|",
    ]

    for spec, sv, seq, source in loaded:
        lines.append(
            f"| `UniProtKB:{spec.accession}` | `{spec.gene_symbol}` | *{spec.organism}* | {len(seq)} | {sv} | `{source}` |"
        )

    lines.extend(
        [
            "",
            "## Global Pairwise % Identity Matrix (`identical / aln_len`)",
            "",
        ]
    )

    headers = [f"{spec.accession} ({spec.organism.split()[0][0]}. {spec.organism.split()[1]})" for spec, _, _, _ in loaded]
    lines.append("| Member | " + " | ".join(f"`{spec.accession}`" for spec, _, _, _ in loaded) + " |")
    lines.append("|---|" + "|".join("---:" for _ in loaded) + "|")

    pair_rows: list[str] = []
    for i, (spec_a, _, seq_a, _) in enumerate(loaded):
        row_cells = [f"`{spec_a.accession}` (*{headers[i].split('(')[1][:-1]}*)"]
        for j, (spec_b, _, seq_b, _) in enumerate(loaded):
            if i == j:
                row_cells.append("100.0%")
            else:
                ident, ungap, aln_len, pct_glob, pct_ungap, score = pairwise_stats(aligner, seq_a, seq_b)
                row_cells.append(f"{pct_glob:.1f}%")
                if i < j:
                    pair_rows.append(
                        f"| `{spec_a.accession}` ({spec_a.gene_symbol}) | `{spec_b.accession}` ({spec_b.gene_symbol}) | "
                        f"{ident}/{aln_len} | **{pct_glob:.1f}%** | {ident}/{ungap} ({pct_ungap:.1f}%) | {score:.1f} |"
                    )
        lines.append("| " + " | ".join(row_cells) + " |")

    lines.extend(
        [
            "",
            "## Detailed Pairwise Alignment Statistics (All 28 Unique Pairs)",
            "",
            "| Protein A | Protein B | Identical / Aln Len | Global % Identity | Identical / Ungapped Cols | NW Score |",
            "|---|---|---:|---:|---:|---:|",
            *pair_rows,
            "",
            "## Key Comparisons Referenced in Curation Notes",
            "",
        ]
    )

    seq_by_acc = {spec.accession: seq for spec, _, seq, _ in loaded}
    key_pairs = [
        ("Q9NX38", "Q80ZQ9", "Human `ABITRAM` vs Mouse `Abitram`"),
        ("Q9NX38", "D4AE08", "Human `ABITRAM` vs Rat `Abitram`"),
        ("D4AE08", "Q80ZQ9", "Rat `Abitram` vs Mouse `Abitram`"),
        ("Q1LU93", "Q9NX38", "Zebrafish `abitram` vs Human `ABITRAM`"),
        ("Q1LU93", "Q80ZQ9", "Zebrafish `abitram` vs Mouse `Abitram`"),
        ("Q1LU93", "D4AE08", "Zebrafish `abitram` vs Rat `Abitram`"),
        ("Q9VFR1", "Q9NX38", "*Drosophila* `abitram` vs Human `ABITRAM`"),
        ("Q9VFR1", "Q80ZQ9", "*Drosophila* `abitram` vs Mouse `Abitram`"),
        ("P34452", "Q9NX38", "*C. elegans* `F54F2.7` vs Human `ABITRAM`"),
        ("P34452", "Q80ZQ9", "*C. elegans* `F54F2.7` vs Mouse `Abitram`"),
        ("Q54TD9", "Q80ZQ9", "*Dictyostelium* `abitram` vs Mouse `Abitram`"),
        ("Q581S9", "Q80ZQ9", "*Trypanosoma* `Q581S9` vs Mouse `Abitram`"),
    ]
    for acc_a, acc_b, label in key_pairs:
        ident, ungap, aln_len, pct_glob, pct_ungap, _ = pairwise_stats(
            aligner, seq_by_acc[acc_a], seq_by_acc[acc_b]
        )
        lines.append(
            f"- **{label}** (`{acc_a}` vs `{acc_b}`): **{pct_glob:.1f}%** global identity ({ident}/{aln_len} columns; {pct_ungap:.1f}% [{ident}/{ungap}] over aligned residue columns)."
        )

    lines.append("")
    RESULTS_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {RESULTS_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
