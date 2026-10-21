#!/usr/bin/env python3
"""Map the G3V4H1 RHOJ product onto the reviewed canonical RHOJ (Q9H4E5).

Run from this directory with the repository environment:

    UV_NO_SYNC=1 uv run python compare_sequences.py

Inputs:
  * ../RHOJ-uniprot.txt (UniProt flat file for G3V4H1; target sequence)
  * ../RHOJ-same-gene-reference.json (UniProt JSON record for Q9H4E5)
  * Ensembl REST (transcript biotypes for ENSG00000126785), fetched live

Alignments describe sequence correspondence, not protein expression or activity.
"""

import json
import re
import urllib.request
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
ENSEMBL_GENE = "ENSG00000126785"
TARGET_TRANSCRIPT = "ENST00000557447"

# Canonical Rho-family G-box motifs (Ras numbering G1-G5) and the C-terminal CAAX box.
MOTIFS = {
    "G1 P-loop GxxxxGK[ST]": r"G..{3}GK[ST]",
    "G3 DTAGQE": r"DTAGQE",
    "G4 [NT][KQ]xD": r"[NT][KQ].D",
    "G5 [ST]A[KL]": r"[ST]A[KL]",
    "CAAX box (C-terminal)": r"C[A-Z]{3}$",
}


def uniprot_flat_sequence(path: Path) -> tuple[str, str]:
    """Return (accession, sequence) from a UniProt flat file.

    >>> acc, seq = uniprot_flat_sequence(GENE_DIR / "RHOJ-uniprot.txt")
    >>> acc, len(seq)
    ('G3V4H1', 153)
    """
    text = path.read_text()
    acc = re.search(r"^AC   (\w+);", text, re.M).group(1)
    sq = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//", 1)[0]
    return acc, re.sub(r"[^A-Z]", "", sq)


def motif_hits(seq: str) -> dict[str, list[int]]:
    """1-based start positions of each motif in seq.

    >>> motif_hits("GDGAVGKTDTAGQE")["G3 DTAGQE"]
    [9]
    """
    return {name: [m.start() + 1 for m in re.finditer(f"(?={pat})", seq)] for name, pat in MOTIFS.items()}


def ensembl_transcripts() -> list[dict]:
    url = f"https://rest.ensembl.org/lookup/id/{ENSEMBL_GENE}?content-type=application/json;expand=1"
    with urllib.request.urlopen(url, timeout=60) as fh:
        gene = json.load(fh)
    return [
        {
            "transcript": t["id"],
            "name": t.get("display_name"),
            "biotype": t["biotype"],
            "is_canonical": bool(t.get("is_canonical")),
            "protein_length": t.get("Translation", {}).get("length"),
        }
        for t in sorted(gene["Transcript"], key=lambda t: t["id"])
    ]


def main() -> None:
    sel_acc, b = uniprot_flat_sequence(GENE_DIR / "RHOJ-uniprot.txt")
    reference = json.loads((GENE_DIR / "RHOJ-same-gene-reference.json").read_text())["record"]
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

    # Longest exact shared prefix
    prefix = 0
    while prefix < min(len(a), len(b)) and a[prefix] == b[prefix]:
        prefix += 1

    features = []
    for f in reference.get("features", []):
        if f["type"] not in {"Active site", "Binding site", "Motif", "Lipidation", "Modified residue", "Propeptide"}:
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
                "within_shared_prefix": end <= prefix,
                "mapped_count": len(mapped),
                "identical_count": sum(a[p - 1] == b[q - 1] for p, q in mapped),
            }
        )

    ref_motifs = motif_hits(a)
    sel_motifs = motif_hits(b)
    transcripts = ensembl_transcripts()

    out = {
        "selected_accession": sel_acc,
        "selected_length": len(b),
        "reference_accession": reference["primaryAccession"],
        "reference_length": len(a),
        "shared_exact_prefix": prefix,
        "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
        "aligned_segments": segments,
        "reference_features": features,
        "motifs_reference": ref_motifs,
        "motifs_selected": sel_motifs,
        "ensembl_transcripts": transcripts,
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
    (HERE / "alignment.txt").write_text(str(aln) + "\n")

    L = [
        "# RHOJ: G3V4H1 product versus canonical RHOJ (Q9H4E5)",
        "",
        f"Selected {sel_acc} has {len(b)} residues; reference {out['reference_accession']} has {len(a)} residues.",
        f"Exact shared N-terminal prefix: residues 1-{prefix}; downstream sequence is divergent.",
        "",
        "## Ensembl transcripts of " + ENSEMBL_GENE,
        "",
        "| Transcript | Name | Biotype | Canonical | Protein length |",
        "|---|---|---|---|---|",
    ]
    for t in transcripts:
        mark = " (G3V4H1 source)" if t["transcript"] == TARGET_TRANSCRIPT else ""
        L.append(
            f"| {t['transcript']}{mark} | {t['name']} | {t['biotype']} | {t['is_canonical']} | {t['protein_length']} |"
        )
    L += [
        "",
        "## G-box and CAAX motifs (1-based start positions; empty = absent)",
        "",
        "| Motif | Q9H4E5 | G3V4H1 |",
        "|---|---|---|",
    ]
    for name in MOTIFS:
        L.append(f"| {name} | {ref_motifs[name]} | {sel_motifs[name]} |")
    L += [
        "",
        "## Global alignment segments",
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
        "## Reference (Q9H4E5) feature mapping",
        "",
        "| Feature | Interval | Within shared prefix | Mapped | Identical |",
        "|---|---|---|---|---|",
    ]
    for f in features:
        L.append(
            f"| {f['type']}: {f['description']} | {f['reference_start']}-{f['reference_end']} | {f['within_shared_prefix']} | {f['mapped_count']} | {f['identical_count']} |"
        )
    L += [
        "",
        "Residues mapped downstream of the shared prefix are placed by global alignment across a non-homologous "
        "tail and should not be read as conserved features.",
        "A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes "
        "the full-length reaction.",
        "",
    ]
    (HERE / "RESULTS.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()
