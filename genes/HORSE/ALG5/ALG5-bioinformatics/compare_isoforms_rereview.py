"""Re-review: place the benchmark horse ALG5 model (A0A5F5PM72) relative to
human ALG5 isoforms 1 and 2 and to PTHR10859:SF91 orthologs, and test whether
the segment it lacks (human 95-124, VSP_041019) is conserved across the subfamily.

Inputs (all cached in this folder or the repo):
  ../ALG5-uniprot.txt                       horse A0A5F5PM72
  ../../../human/ALG5/ALG5-uniprot.txt      human Q9Y673 (isoform 1)
  Q9Y673-2-rereview.fasta                   human isoform 2 (UniProt REST)
  horse_ALG5_all_models-rereview.fasta      all horse ALG5 UniProt entries
  alg5_sf91_orthologs-rereview.fasta        mouse, fly, Dictyostelium, S. pombe, S. cerevisiae ALG5

Writes RESULTS-rereview.md and results-rereview.json.
Run from repo root:
  uv run python genes/HORSE/ALG5/ALG5-bioinformatics/compare_isoforms_rereview.py
"""
from pathlib import Path
import json
from Bio import Align, SeqIO, SwissProt

here = Path(__file__).resolve().parent
with (here.parent / "ALG5-uniprot.txt").open() as f:
    horse = SwissProt.read(f)
with (here.parents[2] / "human" / "ALG5" / "ALG5-uniprot.txt").open() as f:
    human = SwissProt.read(f)
iso2 = str(next(SeqIO.parse(here / "Q9Y673-2-rereview.fasta", "fasta")).seq)
horse_models = {
    r.id.split("|")[1]: str(r.seq)
    for r in SeqIO.parse(here / "horse_ALG5_all_models-rereview.fasta", "fasta")
}
orthologs = {
    r.id.split("|")[1] + " " + r.id.split("|")[2]: str(r.seq)
    for r in SeqIO.parse(here / "alg5_sf91_orthologs-rereview.fasta", "fasta")
}

aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5


def ident(a: str, b: str) -> dict:
    aln = aligner.align(a, b)[0]
    x, y = str(aln[0]), str(aln[1])
    pairs = [(u, v) for u, v in zip(x, y) if u != "-" and v != "-"]
    same = sum(u == v for u, v in pairs)
    gaps_in_b = sum(1 for u, v in zip(x, y) if u != "-" and v == "-")
    return {
        "len_a": len(a),
        "len_b": len(b),
        "paired": len(pairs),
        "identical": same,
        "identity": round(same / len(pairs), 4),
        "a_residues_unpaired": gaps_in_b,
    }


def map_segment(ref: str, other: str, start: int, end: int) -> str:
    """Return the residues of `other` aligned to ref[start..end] (1-based, inclusive)."""
    aln = aligner.align(ref, other)[0]
    x, y = str(aln[0]), str(aln[1])
    pos = 0
    out = []
    for u, v in zip(x, y):
        if u != "-":
            pos += 1
            if start <= pos <= end:
                out.append(v)
        elif start <= pos < end:
            out.append(v.lower())
    return "".join(out)


hs = human.sequence
seg_start, seg_end = 95, 124
deleted = hs[seg_start - 1 : seg_end]

result = {
    "horse_accession": horse.accessions[0],
    "horse_length": len(horse.sequence),
    "human_isoform1_length": len(hs),
    "human_isoform2_length": len(iso2),
    "human_95_124_segment": deleted,
    "horse_vs_human_isoform1": ident(hs, horse.sequence),
    "horse_vs_human_isoform2": ident(iso2, horse.sequence),
    "human_isoform2_equals_isoform1_minus_95_124": iso2 == hs[: seg_start - 1] + hs[seg_end:],
    "segment_in_orthologs": {k: map_segment(hs, s, seg_start, seg_end) for k, s in orthologs.items()},
    "segment_in_horse_models": {
        k: map_segment(hs, s, seg_start, seg_end) for k, s in horse_models.items()
    },
    "horse_model_lengths": {k: len(s) for k, s in horse_models.items()},
    "DXD_motif_ADADG_in_horse": "ADADG" in horse.sequence,
    "DXD_motif_position_in_horse": horse.sequence.find("ADADG") + 1,
}
(here / "results-rereview.json").write_text(json.dumps(result, indent=2) + "\n")

lines = [
    "# ALG5 re-review: isoform identity of A0A5F5PM72 and conservation of the missing segment",
    "",
    "Script: `compare_isoforms_rereview.py` (Biopython global alignment, match 2, mismatch -1,"
    " gap open -10, extend -0.5). Raw values: `results-rereview.json`.",
    "",
    "## Which product is A0A5F5PM72?",
    "",
    f"- Human isoform 2 (Q9Y673-2) is isoform 1 minus residues 95-124:"
    f" {result['human_isoform2_equals_isoform1_minus_95_124']}",
    f"- Horse vs human isoform 1: {result['horse_vs_human_isoform1']}",
    f"- Horse vs human isoform 2: {result['horse_vs_human_isoform2']}",
    f"- Human segment 95-124 absent from the horse model: `{deleted}`",
    "",
    "## The missing segment across PTHR10859:SF91 orthologs",
    "",
    "| Ortholog | Residues aligned to human 95-124 |",
    "|---|---|",
]
for k, v in result["segment_in_orthologs"].items():
    lines.append(f"| {k} | `{v}` |")
lines += [
    "",
    "## The missing segment in all horse ALG5 UniProt entries",
    "",
    "| Horse entry | Length | Residues aligned to human 95-124 |",
    "|---|---|---|",
]
for k, v in result["segment_in_horse_models"].items():
    lines.append(f"| {k} | {result['horse_model_lengths'][k]} | `{v}` |")
lines += [
    "",
    f"DXD motif ADADG present in A0A5F5PM72: {result['DXD_motif_ADADG_in_horse']}"
    f" (position {result['DXD_motif_position_in_horse']}).",
    "",
    "Gap characters ('-') mark residues absent from the compared sequence; lowercase marks"
    " insertions relative to human. This is sequence evidence only: it does not measure"
    " enzyme activity of either isoform.",
    "",
]
(here / "RESULTS-rereview.md").write_text("\n".join(lines))
print("\n".join(lines))
