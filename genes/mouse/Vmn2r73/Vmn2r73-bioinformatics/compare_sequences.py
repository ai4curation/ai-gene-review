#!/usr/bin/env python3
"""Map the benchmark Vmn2r73 product (A0A3B2WCZ5) onto the canonical same-gene product (D3Z7M3).

Inputs (both sibling files in the gene folder):
  - Vmn2r73-uniprot.txt            UniProt flat file for A0A3B2WCZ5 (sequence parsed from SQ block)
  - Vmn2r73-same-gene-reference.json  UniProt JSON for D3Z7M3, the 851-aa product of the
                                      Ensembl canonical transcript ENSMUST00000077478

Run: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not protein expression or activity.
"""
import json
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE = HERE.parent.name

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4,
      "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8,
      "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}


def parse_flatfile(path: Path) -> tuple[str, str]:
    """Return (accession, sequence) from a UniProt flat file."""
    acc, seq, in_seq = "", [], False
    for line in path.read_text().splitlines():
        if line.startswith("AC   ") and not acc:
            acc = line[5:].split(";")[0].strip()
        elif line.startswith("SQ   "):
            in_seq = True
        elif line.startswith("//"):
            in_seq = False
        elif in_seq:
            seq.append(line.replace(" ", ""))
    return acc, "".join(seq)


def hydrophobic_windows(seq: str, window: int = 19, threshold: float = 1.6) -> list[dict]:
    """Kyte-Doolittle windows above threshold (classic TM-helix screen), merged into runs."""
    runs, cur = [], None
    for i in range(len(seq) - window + 1):
        score = sum(KD[c] for c in seq[i:i + window]) / window
        if score >= threshold:
            if cur and i <= cur["end"]:
                cur["end"] = i + window
                cur["max"] = max(cur["max"], score)
            else:
                cur = {"start": i + 1, "end": i + window, "max": score}
                runs.append(cur)
    return [{"start": r["start"], "end": r["end"], "max_kd": round(r["max"], 2)} for r in runs]


sel_acc, b = parse_flatfile(HERE.parent / f"{GENE}-uniprot.txt")
reference = json.loads((HERE.parent / f"{GENE}-same-gene-reference.json").read_text())["record"]
a = reference["sequence"]["value"]

aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(a, b)[0]

pairs, segments = {}, []
for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
    x, y, u, v = map(int, (x, y, u, v))
    segments.append({"reference_start": x + 1, "reference_end": y, "target_start": u + 1,
                     "target_end": v, "identical": sum(a[x + k] == b[u + k] for k in range(y - x))})
    for k in range(y - x):
        pairs[x + k + 1] = u + k + 1

features = []
for f in reference.get("features", []):
    if f["type"] not in {"Transmembrane", "Signal", "Domain", "Topological domain"}:
        continue
    start = f["location"]["start"].get("value")
    end = f["location"]["end"].get("value")
    if not start or not end:
        continue
    mapped = [(p, pairs[p]) for p in range(start, end + 1) if p in pairs]
    features.append({"type": f["type"], "description": f.get("description", ""),
                     "reference_start": start, "reference_end": end, "mapped_count": len(mapped),
                     "length": end - start + 1,
                     "identical_count": sum(a[p - 1] == b[q - 1] for p, q in mapped)})

out = {
    "selected_accession": sel_acc, "selected_length": len(b),
    "reference_accession": reference["primaryAccession"], "reference_length": len(a),
    "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5; "
              "Kyte-Doolittle 19-residue window, threshold 1.6",
    "aligned_segments": segments, "reference_features": features,
    "selected_hydrophobic_windows": hydrophobic_windows(b),
    "reference_hydrophobic_windows": hydrophobic_windows(a),
}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
(HERE / "alignment.txt").write_text(str(aln) + "\n")

L = [f"# {GENE}: benchmark product {sel_acc} vs canonical product {out['reference_accession']}", "",
     f"Selected {sel_acc} has {len(b)} residues (Ensembl ENSMUSP00000156768, transcript Vmn2r73-203, "
     f"non-canonical); reference {out['reference_accession']} has {len(a)} residues (Ensembl canonical "
     "transcript ENSMUST00000077478, Vmn2r73-201).", "", out["method"] + ".", "",
     "## Aligned segments", "", "| Reference interval | Selected interval | Identical residues |",
     "|---|---|---|"]
L += [f"| {s['reference_start']}-{s['reference_end']} | {s['target_start']}-{s['target_end']} | {s['identical']} |"
      for s in segments]
L += ["", "## Reference features mapped onto the selected product", "",
      "| Reference feature | Interval | Mapped / length | Identical |", "|---|---|---|---|"]
L += [f"| {f['type']}: {f['description']} | {f['reference_start']}-{f['reference_end']} | "
      f"{f['mapped_count']} / {f['length']} | {f['identical_count']} |" for f in features]
L += ["", "## Kyte-Doolittle hydrophobic windows (candidate TM helices)", "",
      "| Sequence | Start | End | Max mean KD |", "|---|---|---|---|"]
L += [f"| {sel_acc} | {w['start']} | {w['end']} | {w['max_kd']} |" for w in out["selected_hydrophobic_windows"]]
L += [f"| {out['reference_accession']} | {w['start']} | {w['end']} | {w['max_kd']} |"
      for w in out["reference_hydrophobic_windows"]]
L += ["", "A shared segment does not establish that a truncated product folds, is expressed, "
      "localizes, or signals. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py`.", ""]
(HERE / "RESULTS.md").write_text("\n".join(L))
