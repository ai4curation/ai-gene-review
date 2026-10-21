#!/usr/bin/env python3
"""Map the A0A2R8YCT7 product onto the reviewed human DTD1 reference (Q8TEA8).

Inputs (all from public databases, no prediction output is used):
- ../DTD1-uniprot.txt                 UniProt flat file for A0A2R8YCT7 (sequence, Ensembl xref)
- ../DTD1-same-gene-reference.json    UniProt REST JSON for reviewed human DTD1 (Q8TEA8)
- ensembl-gene.json                   Ensembl REST lookup of ENSG00000125821 (fetched if absent)

Run from this directory: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not protein expression or activity.
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
ENSEMBL_GENE = "ENSG00000125821"
ENSEMBL_URL = (
    f"https://rest.ensembl.org/lookup/id/{ENSEMBL_GENE}"
    "?content-type=application/json;expand=1"
)


def parse_uniprot_flat(path: Path) -> tuple[str, str, str]:
    """Return (accession, sequence, Ensembl transcript id) from a UniProt flat file."""
    text = path.read_text()
    acc = re.search(r"^AC   (\w+);", text, re.M).group(1)
    sq = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//")[0]
    seq = re.sub(r"[^A-Z]", "", sq)
    enst = re.search(r"^DR   Ensembl; (ENST\d+)", text, re.M).group(1)
    return acc, seq, enst


def ensembl_gene() -> dict:
    cache = HERE / "ensembl-gene.json"
    if not cache.exists():
        with urllib.request.urlopen(ENSEMBL_URL, timeout=60) as r:
            cache.write_text(r.read().decode())
    return json.loads(cache.read_text())


sel_acc, b, sel_enst = parse_uniprot_flat(GENE_DIR / "DTD1-uniprot.txt")
reference = json.loads((GENE_DIR / "DTD1-same-gene-reference.json").read_text())["record"]
a = reference["sequence"]["value"]

aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(a, b)[0]

pairs = {}
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
    if f["type"] not in {"Binding site", "Motif", "Beta strand", "Helix"}:
        continue
    start = f["location"]["start"].get("value")
    end = f["location"]["end"].get("value")
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

gene = ensembl_gene()
transcripts = [
    {
        "transcript": t["id"],
        "biotype": t["biotype"],
        "is_canonical": bool(t.get("is_canonical")),
        "protein": t.get("Translation", {}).get("id"),
        "protein_length": t.get("Translation", {}).get("length"),
    }
    for t in gene["Transcript"]
]
sel_tx = [t for t in transcripts if t["transcript"] == sel_enst]

out = {
    "selected_accession": sel_acc,
    "selected_length": len(b),
    "selected_ensembl_transcript": sel_tx,
    "reference_accession": reference["primaryAccession"],
    "reference_length": len(a),
    "shared_exact_prefix": prefix,
    "selected_c_terminal_tail": b[prefix:],
    "reference_residues_after_prefix": a[prefix : prefix + 10],
    "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
    "aligned_segments": segments,
    "reference_features": features,
    "ensembl_transcripts": transcripts,
}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
(HERE / "alignment.txt").write_text(str(aln) + "\n")

L = [
    "# DTD1 A0A2R8YCT7 versus reviewed DTD1 (Q8TEA8)",
    "",
    f"Selected {sel_acc}: {len(b)} residues; reference {out['reference_accession']}: {len(a)} residues.",
    f"Exact shared N-terminal prefix: residues 1-{prefix}. Selected C-terminal tail after the prefix: "
    f"`{out['selected_c_terminal_tail']}` (reference continues `{out['reference_residues_after_prefix']}...`).",
    "",
    "Ensembl transcript encoding the selected product (Ensembl REST lookup of "
    f"{ENSEMBL_GENE}):",
    "",
    "| Transcript | Biotype | Canonical | Protein | Length |",
    "|---|---|---|---|---|",
]
for t in sel_tx:
    L.append(
        f"| {t['transcript']} | {t['biotype']} | {t['is_canonical']} | {t['protein']} | {t['protein_length']} |"
    )
L += ["", out["method"] + ".", "", "| Reference interval | Selected interval | Identical residues |", "|---|---|---|"]
for s in segments:
    L.append(f"| {s['reference_start']}-{s['reference_end']} | {s['target_start']}-{s['target_end']} | {s['identical']} |")
L += [
    "",
    "Reference feature mapping (coverage does not establish retained function):",
    "",
    "| Reference feature | Interval | Mapped / length | Identical |",
    "|---|---|---|---|",
]
for f in features:
    L.append(
        f"| {f['type']}: {f['description']} | {f['reference_start']}-{f['reference_end']} | "
        f"{f['mapped_count']} / {f['length']} | {f['identical_count']} |"
    )
L += [
    "",
    "All Ensembl transcripts of the gene:",
    "",
    "| Transcript | Biotype | Canonical | Protein length |",
    "|---|---|---|---|",
]
for t in transcripts:
    L.append(f"| {t['transcript']} | {t['biotype']} | {t['is_canonical']} | {t['protein_length']} |")
L += [
    "",
    "A shared segment does not establish that a truncated product is stable, folds, dimerizes or catalyzes.",
    "",
]
(HERE / "RESULTS.md").write_text("\n".join(L))
print("\n".join(L))
