#!/usr/bin/env python3
"""Map the selected UniProt product U4PF58 onto full-length C. elegans DPM-1 and human DPM1.

Inputs (all deterministic downloads, no prediction outputs):
  - ../dpm-1-uniprot.txt                (selected product, U4PF58 flat file)
  - ../dpm-1-same-gene-reference.json   (full-length same-gene product Q9TYJ7, UniProt JSON)
  - ../../../human/DPM1/DPM1-uniprot.txt (human DPM1 O60762, PANTHER PTHR43398:SF1)

Run from this directory: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not protein expression or activity.
"""

import json
import re
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GENES_ROOT = GENE_DIR.parent.parent


def flatfile_sequence(path: Path) -> tuple[str, str]:
    """Return (accession, sequence) from a UniProt flat file.

    >>> acc, seq = flatfile_sequence(GENE_DIR / "dpm-1-uniprot.txt")
    >>> acc, len(seq)
    ('U4PF58', 51)
    """
    text = path.read_text()
    acc = re.search(r"^AC   (\w+);", text, re.M).group(1)
    sq = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//", 1)[0]
    return acc, re.sub(r"[^A-Z]", "", sq)


def make_aligner(mode: str) -> PairwiseAligner:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = mode
    return aligner


def segments(aln, a: str, b: str) -> list[dict]:
    out = []
    for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        x, y, u, v = map(int, (x, y, u, v))
        ident = sum(a[x + k] == b[u + k] for k in range(y - x))
        out.append({"a_start": x + 1, "a_end": y, "b_start": u + 1, "b_end": v, "identical": ident})
    return out


def position_map(aln) -> dict[int, int]:
    pairs = {}
    for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        for k in range(int(y) - int(x)):
            pairs[int(x) + k + 1] = int(u) + k + 1
    return pairs


sel_acc, sel = flatfile_sequence(GENE_DIR / "dpm-1-uniprot.txt")
ref = json.loads((GENE_DIR / "dpm-1-same-gene-reference.json").read_text())["record"]
ref_acc, full = ref["primaryAccession"], ref["sequence"]["value"]
hum_acc, hum = flatfile_sequence(GENES_ROOT / "human" / "DPM1" / "DPM1-uniprot.txt")

# 1. selected product vs full-length same-gene product (global)
aln1 = make_aligner("global").align(full, sel)[0]
seg1 = segments(aln1, full, sel)
map1 = position_map(aln1)
features = []
for f in ref.get("features", []):
    start = f["location"]["start"].get("value")
    end = f["location"]["end"].get("value")
    if not start or not end:
        continue
    mapped = [p for p in range(start, end + 1) if p in map1]
    features.append({"type": f["type"], "description": f.get("description", ""),
                     "start": start, "end": end, "mapped": len(mapped), "length": end - start + 1})

# 2. full-length worm DPM-1 vs human DPM1 (global), and the fragment's human equivalent
aln2 = make_aligner("global").align(full, hum)[0]
seg2 = segments(aln2, full, hum)
aligned_cols = sum(s["a_end"] - s["a_start"] + 1 for s in seg2)
ident2 = sum(s["identical"] for s in seg2)
map2 = position_map(aln2)
frag_ref_positions = sorted(map1)  # worm full-length positions covered by the fragment
frag_human = [map2[p] for p in frag_ref_positions if p in map2]
frag_ident = sum(full[p - 1] == hum[map2[p] - 1] for p in frag_ref_positions if p in map2)

# 3. DXD-type motifs (GT-A metal/nucleotide-sugar binding) in each sequence
dxd = {name: [m.start() + 1 for m in re.finditer(r"(?=D.D)", s)]
       for name, s in [(ref_acc, full), (sel_acc, sel), (hum_acc, hum)]}

out = {
    "selected": {"accession": sel_acc, "length": len(sel)},
    "same_gene_reference": {"accession": ref_acc, "length": len(full)},
    "human_reference": {"accession": hum_acc, "length": len(hum)},
    "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
    "selected_vs_reference_segments": seg1,
    "reference_features": features,
    "worm_vs_human_aligned_columns": aligned_cols,
    "worm_vs_human_identical": ident2,
    "worm_vs_human_percent_identity_over_aligned": round(100 * ident2 / aligned_cols, 1),
    "fragment_human_interval": [min(frag_human), max(frag_human)] if frag_human else None,
    "fragment_human_identical": frag_ident,
    "dxd_motif_starts": dxd,
}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
(HERE / "alignment.txt").write_text(
    f"# {sel_acc} vs {ref_acc}\n{aln1}\n# {ref_acc} vs {hum_acc}\n{aln2}\n")

lines = [
    "# dpm-1: selected product U4PF58 vs full-length DPM-1 and human DPM1",
    "",
    f"Selected {sel_acc}: {len(sel)} residues. Same-gene full-length {ref_acc}: {len(full)} residues. "
    f"Human DPM1 {hum_acc}: {len(hum)} residues.",
    "",
    out["method"] + ".",
    "",
    "## Selected product vs full-length same-gene product",
    "",
    "| Reference interval | Selected interval | Identical residues |",
    "|---|---|---|",
]
lines += [f"| {s['a_start']}–{s['a_end']} | {s['b_start']}–{s['b_end']} | {s['identical']} |" for s in seg1]
lines += ["", "| Reference feature | Interval | Mapped / length |", "|---|---|---|"]
lines += [f"| {f['type']}: {f['description']} | {f['start']}–{f['end']} | {f['mapped']} / {f['length']} |"
          for f in features]
lines += [
    "",
    "## Full-length worm DPM-1 vs human DPM1",
    "",
    f"Aligned columns: {aligned_cols}; identical: {ident2} "
    f"({out['worm_vs_human_percent_identity_over_aligned']}% over aligned columns).",
    "",
    f"The fragment's residues map to human DPM1 positions {out['fragment_human_interval']}, "
    f"with {frag_ident} identical residues.",
    "",
    "## DXD-type motif start positions",
    "",
]
lines += [f"- {k}: {v}" for k, v in dxd.items()]
lines += [
    "",
    "A shared segment does not establish that a truncated product is expressed, folds, localizes, "
    "or catalyzes the full-length reaction.",
    "",
    "Inputs: dpm-1-uniprot.txt, dpm-1-same-gene-reference.json, human/DPM1/DPM1-uniprot.txt. "
    "Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.",
    "",
]
(HERE / "RESULTS.md").write_text("\n".join(lines))
