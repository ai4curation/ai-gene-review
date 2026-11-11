"""Re-review: compare the benchmark horse KRIT1 product (A0A9L0SR44) with the other
horse KRIT1 gene products (same Ensembl gene ENSECAG00000016850) and human O00522.

Inputs are cached UniProt flat files; writes RESULTS-rereview.md and results-rereview.json.
Run from repo root: uv run python genes/HORSE/KRIT1/KRIT1-bioinformatics/compare_sequences_rereview.py
"""
from pathlib import Path
import json
from Bio import Align, SwissProt

here = Path(__file__).resolve().parent
files = {
    "A0A9L0SR44": here.parent / "KRIT1-uniprot.txt",
    "A0A3Q2GZV2": here / "A0A3Q2GZV2-uniprot-rereview.txt",
    "A0A3Q2LAF1": here / "A0A3Q2LAF1-uniprot-rereview.txt",
    "O00522": here.parents[2] / "human" / "KRIT1" / "KRIT1-uniprot.txt",
}
recs = {}
for acc, p in files.items():
    with p.open() as f:
        recs[acc] = SwissProt.read(f)

aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5


def compare(a: str, b: str) -> dict:
    sa, sb = recs[a].sequence, recs[b].sequence
    aln = aligner.align(sa, sb)[0]
    x, y = str(aln[0]), str(aln[1])
    pairs = [(u, v) for u, v in zip(x, y) if u != "-" and v != "-"]
    ident = sum(u == v for u, v in pairs)
    # first and last differing alignment columns
    diffs = [i for i, (u, v) in enumerate(zip(x, y)) if u != v]
    return {
        "a": a, "b": b, "len_a": len(sa), "len_b": len(sb),
        "paired": len(pairs), "identical": ident,
        "identity": round(ident / len(pairs), 4),
        "gaps_in_a": x.count("-"), "gaps_in_b": y.count("-"),
        "first_diff_col": diffs[0] if diffs else None,
        "last_diff_col": diffs[-1] if diffs else None,
        "alignment": str(aln),
    }


def map_positions(a: str, b: str, positions: list[int]) -> dict:
    """Map 1-based positions in a onto b through the global alignment (None = gap in b)."""
    aln = aligner.align(recs[a].sequence, recs[b].sequence)[0]
    x, y = str(aln[0]), str(aln[1])
    out, pa, pb = {}, 0, 0
    for u, v in zip(x, y):
        if u != "-":
            pa += 1
        if v != "-":
            pb += 1
        if u != "-" and pa in positions:
            out[pa] = f"{u}{pa}->" + (f"{v}{pb}" if v != "-" else "gap")
    return out


# Human KRIT1 L717/L721 form the HEG1-binding groove (PMID:23007647); 430-452 Rap1B region (UniProt).
key_positions = [715, 717, 721, 731, 734, 430, 452]
mapping = {acc: map_positions("O00522", acc, key_positions) for acc in ("A0A3Q2GZV2", "A0A9L0SR44")}

results = [compare("O00522", acc) for acc in ("A0A3Q2GZV2", "A0A3Q2LAF1", "A0A9L0SR44")]
results.append(compare("A0A3Q2GZV2", "A0A9L0SR44"))
tails = {acc: r.sequence[-30:] for acc, r in recs.items()}

(here / "results-rereview.json").write_text(
    json.dumps({"comparisons": [{k: v for k, v in r.items() if k != "alignment"} for r in results],
                "c_terminal_30aa": tails, "human_position_mapping": mapping}, indent=2) + "\n")
lines = ["# KRIT1 re-review: horse KRIT1 gene products vs human O00522", "",
         "All three horse entries map to Ensembl gene ENSECAG00000016850 (UniProt DR Ensembl lines).", "",
         "| A | B | len A | len B | identical/paired | identity | gaps in A | gaps in B |",
         "|---|---|---|---|---|---|---|---|"]
for r in results:
    lines.append(f"| {r['a']} | {r['b']} | {r['len_a']} | {r['len_b']} | {r['identical']}/{r['paired']} | "
                 f"{r['identity']:.1%} | {r['gaps_in_a']} | {r['gaps_in_b']} |")
lines += ["", "## C-terminal 30 residues", ""]
for acc, t in tails.items():
    lines.append(f"- {acc}: `{t}`")
lines += ["", "## Human key positions mapped onto horse products", "",
          "L717 and L721 are the HEG1-groove leucines (KRIT1 L717,721A, PMID:23007647); 430-452 is the UniProt Rap1B-interaction region.", ""]
for acc, m in mapping.items():
    lines.append(f"- {acc}: " + ", ".join(m[k] for k in sorted(m)))
for r in results:
    lines += ["", f"## Alignment {r['a']} vs {r['b']}", "", "```", r["alignment"].rstrip(), "```"]
(here / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
for r in results:
    print(r["a"], r["b"], r["identical"], r["paired"], r["identity"], r["gaps_in_a"], r["gaps_in_b"])
print(json.dumps(tails, indent=1))
print(json.dumps(mapping, indent=1))
