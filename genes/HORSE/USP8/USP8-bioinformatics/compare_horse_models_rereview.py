"""Compare all horse USP8 gene-model products with human P40818 (re-review).

Fetches (live) the four horse UniProt entries that map to Ensembl gene
ENSECAG00000006611 (USP8) and human P40818 isoform 1, aligns each horse
product globally to human, and reports:

* identity and coverage;
* internal gaps (insertions/deletions) relative to human;
* whether human landmark segments are present: MIT domain (33-116),
  rhodanese domain (195-313), SH3-binding motif (405-413), the 601-629
  segment that is absent from human isoform 2, the 14-3-3 site S718, the
  USP domain (777-1109) and the catalytic Cys786 / His1067;
* the C-terminal sequence from human position 1090, to expose alternative
  terminal exons.

Writes RESULTS-rereview.md and results-rereview.json next to this script.
Run from the repository root:
    uv run python genes/HORSE/USP8/USP8-bioinformatics/compare_horse_models_rereview.py
"""

import json
from pathlib import Path
from urllib.request import urlopen

from Bio import Align

HERE = Path(__file__).resolve().parent
HUMAN = "P40818"
TARGET = "A0A9L0T7K6"
HORSE = ["A0A9L0T7K6", "F7BV54", "A0A3Q2HXC7", "A0A5F5PIL5"]
SEGMENTS = {
    "MIT 33-116": (33, 116),
    "rhodanese 195-313": (195, 313),
    "SH3-binding 405-413": (405, 413),
    "isoform-2-absent 601-629": (601, 629),
    "USP 777-1109": (777, 1109),
}
SITES = {718: "S", 786: "C", 1067: "H"}


def fasta_seq(acc: str) -> str:
    with urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
        text = r.read().decode()
    return "".join(text.splitlines()[1:])


def compare(human: str, horse: str) -> dict:
    aligner = Align.PairwiseAligner(
        mode="global", match_score=2, mismatch_score=-1,
        open_gap_score=-10, extend_gap_score=-0.5,
    )
    aln = aligner.align(human, horse)[0]
    hmap = {}
    for (s, e), (t, u) in zip(*aln.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            hmap[i + 1] = j + 1
    ident = sum(human[i - 1] == horse[j - 1] for i, j in hmap.items())
    blocks = list(zip(*aln.aligned))
    gaps = []
    for ((s1, e1), (t1, u1)), ((s2, e2), (t2, u2)) in zip(blocks, blocks[1:]):
        if s2 > e1:
            gaps.append(f"human {e1 + 1}-{s2} absent from horse")
        if t2 > u1:
            gaps.append(f"horse {u1 + 1}-{t2} inserted (no human counterpart)")
    (s0, _), (t0, _) = blocks[0]
    if s0 > 0:
        gaps.insert(0, f"human 1-{s0} absent (N-terminal)")
    if t0 > 0:
        gaps.insert(0, f"horse 1-{t0} N-terminal extension")
    seg = {}
    for name, (a, b) in SEGMENTS.items():
        present = sum(1 for k in range(a, b + 1) if k in hmap)
        seg[name] = f"{present}/{b - a + 1} residues aligned"
    sites = {}
    for pos, aa in SITES.items():
        j = hmap.get(pos)
        sites[f"{aa}{pos}"] = f"{horse[j - 1]}{j}" if j else "absent"
    return {
        "horse_length": len(horse),
        "paired": len(hmap),
        "identity_percent": round(100 * ident / len(hmap), 2),
        "human_coverage_percent": round(100 * len(hmap) / len(human), 2),
        "gaps": gaps,
        "segments": seg,
        "sites": sites,
        "human_1090_end": human[1089:],
        "horse_aligned_to_human_1090_end": horse[hmap[1090] - 1:] if 1090 in hmap else None,
    }


def main() -> None:
    human = fasta_seq(HUMAN)
    res = {"human": HUMAN, "human_length": len(human), "models": {}}
    for acc in HORSE:
        res["models"][acc] = compare(human, fasta_seq(acc))
    (HERE / "results-rereview.json").write_text(json.dumps(res, indent=2) + "\n")
    lines = [
        "# USP8 horse gene models vs human P40818 (re-review)",
        "",
        f"All four horse UniProt entries below are products of Ensembl gene ENSECAG00000006611 (USP8). "
        f"Benchmark target is {TARGET}. Human P40818 isoform 1 is {len(human)} aa. "
        "Global alignment: Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extend -0.5.",
        "",
    ]
    for acc, r in res["models"].items():
        lines.append(f"## {acc}{' (benchmark target)' if acc == TARGET else ''}")
        lines.append("")
        lines.append(
            f"- {acc}: {r['horse_length']} aa; {r['identity_percent']}% identity over {r['paired']} paired residues; "
            f"{r['human_coverage_percent']}% of human covered."
        )
        lines.append(f"- Gaps: {'; '.join(r['gaps']) if r['gaps'] else 'none'}")
        for k, v in r["segments"].items():
            lines.append(f"- {k}: {v}")
        lines.append("- Sites: " + ", ".join(f"human {k} -> horse {v}" for k, v in r["sites"].items()))
        lines.append(f"- C-terminus from human 1090: human {r['human_1090_end']}; horse {r['horse_aligned_to_human_1090_end']}")
        lines.append("")
    (HERE / "RESULTS-rereview.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
