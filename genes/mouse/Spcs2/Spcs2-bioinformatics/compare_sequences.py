#!/usr/bin/env python3
"""Map the A0A140LHW5 Spcs2 product to the canonical Spcs2 protein (Q9CYN2).

Inputs:
  - ../Spcs2-uniprot.txt               (UniProt flat file of the benchmark accession)
  - ../Spcs2-same-gene-reference.json  (UniProt JSON of reviewed same-gene entry Q9CYN2)
  - Ensembl REST (live): exon structures of the benchmark transcript and the canonical one

Run with the repository environment: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not protein expression or activity.
"""

import json
import urllib.request
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent

BENCH_TRANSCRIPT = "ENSMUST00000208465"  # Spcs2-206 -> ENSMUSP00000146574 (A0A140LHW5)
CANON_TRANSCRIPT = "ENSMUST00000036274"  # Spcs2-201, Ensembl canonical, 226 aa


def read_uniprot_flat(path: Path) -> tuple[str, str]:
    """Return (accession, sequence) from a UniProt flat file."""
    acc = ""
    seq_lines: list[str] = []
    in_seq = False
    for line in path.read_text().splitlines():
        if line.startswith("AC   ") and not acc:
            acc = line[5:].split(";")[0].strip()
        elif line.startswith("SQ   "):
            in_seq = True
        elif line.startswith("//"):
            in_seq = False
        elif in_seq:
            seq_lines.append(line.replace(" ", ""))
    return acc, "".join(seq_lines)


def ensembl_transcript(tid: str) -> dict:
    url = f"https://rest.ensembl.org/lookup/id/{tid}?content-type=application/json;expand=1"
    with urllib.request.urlopen(url) as fh:
        return json.load(fh)


sel_acc, b = read_uniprot_flat(GENE_DIR / "Spcs2-uniprot.txt")
reference = json.loads((GENE_DIR / "Spcs2-same-gene-reference.json").read_text())["record"]
a = reference["sequence"]["value"]

aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(a, b)[0]

pairs: dict[int, int] = {}
segments = []
for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
    x, y, u, v = map(int, (x, y, u, v))
    segments.append(
        {
            "reference_start": x + 1,
            "reference_end": y,
            "target_start": u + 1,
            "target_end": v,
            "identical": sum(a[x + k] == b[u + k] for k in range(y - x)),
        }
    )
    for k in range(y - x):
        pairs[x + k + 1] = u + k + 1

# longest exact shared prefix
prefix = 0
while prefix < min(len(a), len(b)) and a[prefix] == b[prefix]:
    prefix += 1

features = []
for f in reference.get("features", []):
    if f["type"] not in {"Topological domain", "Transmembrane", "Domain", "Region"}:
        continue
    start = f["location"]["start"].get("value")
    end = f["location"]["end"].get("value")
    if not start or not end:
        continue
    mapped = [(p, pairs[p]) for p in range(start, end + 1) if p in pairs]
    features.append(
        {
            "type": f["type"],
            "description": f.get("description", ""),
            "reference_start": start,
            "reference_end": end,
            "length": end - start + 1,
            "mapped_count": len(mapped),
            "identical_count": sum(a[p - 1] == b[q - 1] for p, q in mapped),
        }
    )

# Exon structures (gene is on the minus strand; list exons 5'->3')
exons = {}
for tid in (BENCH_TRANSCRIPT, CANON_TRANSCRIPT):
    t = ensembl_transcript(tid)
    ex = sorted(((e["start"], e["end"]) for e in t["Exon"]), key=lambda se: -se[1])
    exons[tid] = {
        "display_name": t.get("display_name"),
        "biotype": t.get("biotype"),
        "translation_length": t.get("Translation", {}).get("length"),
        "exons_5p_to_3p": [{"start": s, "end": e, "length": e - s + 1} for s, e in ex],
    }

out = {
    "selected_accession": sel_acc,
    "selected_length": len(b),
    "reference_accession": reference["primaryAccession"],
    "reference_length": len(a),
    "identical_prefix_length": prefix,
    "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
    "aligned_segments": segments,
    "reference_features": features,
    "ensembl_transcripts": exons,
}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
(HERE / "alignment.txt").write_text(str(aln) + "\n")

L = [
    "# Spcs2: A0A140LHW5 product versus canonical Spcs2 (Q9CYN2)",
    "",
    f"Selected {sel_acc} has {len(b)} residues; reference {out['reference_accession']} has {len(a)} residues.",
    f"The two sequences are identical over the first {prefix} residues; the remaining "
    f"{len(b) - prefix} residues of {sel_acc} are a different C-terminal tail.",
    "",
    out["method"] + ".",
    "",
    "| Reference interval | Selected interval | Identical residues |",
    "|---|---|---|",
]
for s in segments:
    L.append(f"| {s['reference_start']}-{s['reference_end']} | {s['target_start']}-{s['target_end']} | {s['identical']} |")
L += [
    "",
    "Reference features of Q9CYN2 and how much of each the selected product covers:",
    "",
    "| Reference feature | Interval | Mapped / length | Identical |",
    "|---|---|---|---|",
]
for f in features:
    L.append(
        f"| {f['type']}: {f['description']} | {f['reference_start']}-{f['reference_end']} | "
        f"{f['mapped_count']} / {f['length']} | {f['identical_count']} |"
    )
L += ["", "Ensembl exon structures (minus strand, listed 5' to 3'):", ""]
for tid, t in exons.items():
    L.append(f"- {tid} ({t['display_name']}, {t['biotype']}, {t['translation_length']} aa): " + ", ".join(
        f"{e['start']}-{e['end']} ({e['length']} nt)" for e in t["exons_5p_to_3p"]))
L += [
    "",
    "Global alignment places isolated tail residues opposite distant reference positions; only the "
    "identical prefix is a genuine shared segment. A shared segment does not establish that the short "
    "product is expressed, folds, localizes to the ER membrane or joins the signal peptidase complex.",
    "",
    "Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.",
    "",
]
(HERE / "RESULTS.md").write_text("\n".join(L))
print("\n".join(L))
