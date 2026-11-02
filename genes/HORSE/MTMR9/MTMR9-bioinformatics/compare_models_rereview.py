"""Re-review: place the benchmark horse MTMR9 product (A0A9L0T3C1, 507 aa) among
all horse MTMR9 UniProt models and PTHR10807:SF56 orthologs, and characterise the
segment it lacks relative to human Q96QG7.

Inputs (all in this folder, fetched from UniProt REST / Ensembl REST on 2026-10-20):
  horse_MTMR9_all_models-rereview.fasta   A0A9L0T3C1, F7CCR9, A0A5F5PR89
  mtmr9_sf56_orthologs-rereview.fasta     human Q96QG7, mouse Q9Z2D0, bovine A7MB43
  ensembl_ENSECAT*-rereview.json          Ensembl transcript/exon models of ENSECAG00000014120

Writes RESULTS-rereview.md and results-rereview.json.
Run from repo root:
  uv run python genes/HORSE/MTMR9/MTMR9-bioinformatics/compare_models_rereview.py
"""

import json
from pathlib import Path

from Bio import Align, SeqIO

here = Path(__file__).resolve().parent


def read_fasta(name: str) -> dict[str, str]:
    return {r.id.split("|")[1]: str(r.seq) for r in SeqIO.parse(here / name, "fasta")}


horse = read_fasta("horse_MTMR9_all_models-rereview.fasta")
orth = read_fasta("mtmr9_sf56_orthologs-rereview.fasta")
human = orth["Q96QG7"]

aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5


def compare(ref: str, other: str) -> dict:
    aln = aligner.align(ref, other)[0]
    x, y = str(aln[0]), str(aln[1])
    pairs = [(u, v) for u, v in zip(x, y) if u != "-" and v != "-"]
    same = sum(u == v for u, v in pairs)
    # human positions (1-based) left unpaired in `other`
    missing, pos = [], 0
    for u, v in zip(x, y):
        if u != "-":
            pos += 1
            if v == "-":
                missing.append(pos)
    extra = sum(1 for u, v in zip(x, y) if u == "-" and v != "-")
    runs: list[list[int]] = []
    for p in missing:
        if runs and p == runs[-1][1] + 1:
            runs[-1][1] = p
        else:
            runs.append([p, p])
    return {
        "length": len(other),
        "paired": len(pairs),
        "identity": round(same / len(pairs), 4),
        "human_segments_missing": [f"{a}-{b}" for a, b in runs],
        "extra_residues_vs_human": extra,
        "c_terminal_10": other[-10:],
    }


results: dict = {"human_Q96QG7_length": len(human), "human_c_terminal_10": human[-10:]}
results["vs_human"] = {acc: compare(human, s) for acc, s in {**horse, **orth}.items() if acc != "Q96QG7"}

# Conservation of the segment that A0A9L0T3C1 lacks (human 98-139)
seg = human[97:139]
results["human_98_139"] = seg

exons = {}
for f in sorted(here.glob("ensembl_ENSECAT*-rereview.json")):
    d = json.loads(f.read_text())
    exons[d["id"]] = [(e["start"], e["end"]) for e in d["Exon"]]
all_exons = sorted({e for ex in exons.values() for e in ex})
results["ensembl_exons"] = {
    t: {"n_exons": len(ex), "skipped": [f"{a}-{b} ({b - a + 1} nt)" for a, b in all_exons if (a, b) not in ex]}
    for t, ex in exons.items()
}

(here / "results-rereview.json").write_text(json.dumps(results, indent=2) + "\n")

lines = ["# MTMR9 horse gene-model re-review (2026-10-20)", ""]
lines.append(f"Human Q96QG7 length {len(human)}; segment 98-139 = `{seg}`.")
lines.append("")
lines.append("| accession | length | identity to human | human segments missing | extra residues | C-terminal 10 |")
lines.append("|---|---|---|---|---|---|")
for acc, r in results["vs_human"].items():
    lines.append(
        f"| {acc} | {r['length']} | {r['identity']:.1%} | {', '.join(r['human_segments_missing']) or 'none'} "
        f"| {r['extra_residues_vs_human']} | {r['c_terminal_10']} |"
    )
lines.append(f"| Q96QG7 (human) | {len(human)} | - | - | - | {human[-10:]} |")
lines.append("")
lines.append("Ensembl ENSECAG00000014120 transcripts (exons absent relative to the union of all exons):")
lines.append("")
for t, r in results["ensembl_exons"].items():
    lines.append(f"- {t}: {r['n_exons']} exons; absent: {', '.join(r['skipped']) or 'none'}")
lines.append("")
(here / "RESULTS-rereview.md").write_text("\n".join(lines))
print("\n".join(lines))
