#!/usr/bin/env python3
"""Align frog uap1.S (Q6DCZ6) to human UAP1 (Q16222) and map curated human features.

Inputs (sibling files in the gene folder):
  - uap1.S-uniprot.txt          UniProt flat file for Q6DCZ6 (sequence source)
  - uap1.S-human-ortholog.json  UniProt JSON for human UAP1 Q16222 (features)

Run from this directory: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not expression or activity.
"""

import json
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GENE = GENE_DIR.name


def flatfile_sequence(path: Path) -> tuple[str, str]:
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


target_acc, target = flatfile_sequence(GENE_DIR / f"{GENE}-uniprot.txt")
reference = json.loads((GENE_DIR / f"{GENE}-human-ortholog.json").read_text())
ref_acc = reference["primaryAccession"]
ref = reference["sequence"]["value"]

aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(ref, target)[0]

pairs: dict[int, int] = {}
segments = []
for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
    x, y, u, v = map(int, (x, y, u, v))
    ident = sum(ref[x + k] == target[u + k] for k in range(y - x))
    segments.append(
        {"reference": [x + 1, y], "target": [u + 1, v], "identical": ident}
    )
    for k in range(y - x):
        pairs[x + k + 1] = u + k + 1

# Collapse per-ligand binding-site rows into one row per residue.
sites: dict[int, set[str]] = {}
alt_seqs = []
mutagenesis: list[dict] = []
for f in reference.get("features", []):
    start = f["location"]["start"].get("value")
    end = f["location"]["end"].get("value")
    if f["type"] == "Binding site" and start == end:
        sites.setdefault(start, set()).add(f.get("ligand", {}).get("name", ""))
    elif f["type"] == "Mutagenesis":
        mutagenesis.append(
            {
                "start": start,
                "end": end,
                "human": ref[start - 1 : end],
                "frog": "".join(
                    target[pairs[p] - 1] if p in pairs else "-"
                    for p in range(start, end + 1)
                ),
                "description": f.get("description", ""),
            }
        )
    elif f["type"] == "Alternative sequence":
        alt_seqs.append(
            {"start": start, "end": end, "description": f.get("description", "")}
        )

site_rows = []
for pos in sorted(sites):
    tpos = pairs.get(pos)
    site_rows.append(
        {
            "reference_pos": pos,
            "reference_residue": ref[pos - 1],
            "target_pos": tpos,
            "target_residue": target[tpos - 1] if tpos else None,
            "conserved": bool(tpos) and ref[pos - 1] == target[tpos - 1],
            "ligands": sorted(sites[pos]),
        }
    )

# Human residues outside any aligned block (gaps in the frog sequence).
unaligned_ref = [p for p in range(1, len(ref) + 1) if p not in pairs]

# Residues named in PMID:11707391 as nucleotide-sugar contacts: I-loop
# Arg453 and Lys455, N-acetyl contacts (Asn223, Glu303, His331, Phe381,
# Phe383) and C4-OH contacts (Gly290, Asn327). The paper numbers I-loop
# residues on AGX1, which lacks AGX2 residues 454-470, so AGX1 positions
# after 453 are shifted by 17 to reach the canonical (AGX2) sequence.
named_agx1 = [223, 290, 303, 327, 331, 381, 383, 453, 455]
named_rows = []
for agx1_pos in named_agx1:
    pos = agx1_pos + 17 if agx1_pos > 453 else agx1_pos
    tpos = pairs.get(pos)
    named_rows.append(
        {
            "agx1_pos": agx1_pos,
            "reference_pos": pos,
            "reference_residue": ref[pos - 1],
            "target_pos": tpos,
            "target_residue": target[tpos - 1] if tpos else None,
        }
    )

total_ident = sum(s["identical"] for s in segments)
aligned_len = len(pairs)
out = {
    "target_accession": target_acc,
    "target_length": len(target),
    "reference_accession": ref_acc,
    "reference_length": len(ref),
    "method": "Biopython PairwiseAligner global, BLOSUM62, gap open -10, extend -0.5",
    "aligned_residues": aligned_len,
    "identical_residues": total_ident,
    "aligned_segments": segments,
    "unaligned_reference_positions": unaligned_ref,
    "reference_alternative_sequences": alt_seqs,
    "binding_sites": site_rows,
    "mutagenesis_sites": mutagenesis,
    "named_structural_residues": named_rows,
}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
(HERE / "alignment.txt").write_text(str(aln) + "\n")


def ranges(xs: list[int]) -> str:
    if not xs:
        return "none"
    out_r = []
    start = prev = xs[0]
    for x in xs[1:]:
        if x == prev + 1:
            prev = x
            continue
        out_r.append(f"{start}-{prev}" if start != prev else f"{start}")
        start = prev = x
    out_r.append(f"{start}-{prev}" if start != prev else f"{start}")
    return ", ".join(out_r)


n_cons = sum(r["conserved"] for r in site_rows)
lines = [
    f"# {GENE} ({target_acc}) vs human UAP1 ({ref_acc})",
    "",
    f"Target {target_acc}: {len(target)} aa (sequence from `{GENE}-uniprot.txt`). "
    f"Reference {ref_acc}: {len(ref)} aa (canonical isoform AGX2, from `{GENE}-human-ortholog.json`).",
    "",
    f"Method: {out['method']}.",
    "",
    f"Aligned residue pairs: {aligned_len}; identical: {total_ident} "
    f"({100 * total_ident / aligned_len:.1f}% of aligned pairs).",
    "",
    "| Human interval | Frog interval | Identical |",
    "|---|---|---|",
]
for s in segments:
    lines.append(
        f"| {s['reference'][0]}-{s['reference'][1]} | {s['target'][0]}-{s['target'][1]} | {s['identical']} |"
    )
lines += [
    "",
    f"Human positions with no frog counterpart: {ranges(unaligned_ref)}.",
    "",
    "Human alternative-sequence features (UniProt):",
    "",
]
for a in alt_seqs:
    lines.append(f"- {a['start']}-{a['end']}: {a['description']}")
lines += [
    "",
    f"UniProt UDP-GlcNAc/UDP-GalNAc binding-site residues conserved in frog: {n_cons} of {len(site_rows)}.",
    "",
    "| Human pos | Human aa | Frog pos | Frog aa | Conserved | Ligands |",
    "|---|---|---|---|---|---|",
]
for r in site_rows:
    lines.append(
        f"| {r['reference_pos']} | {r['reference_residue']} | {r['target_pos']} | "
        f"{r['target_residue']} | {'yes' if r['conserved'] else 'no'} | {'; '.join(r['ligands'])} |"
    )
lines += [
    "",
    "Residues named as nucleotide-sugar contacts in the human AGX1/AGX2 structures (PMID:11707391):",
    "",
    "| AGX1 pos (paper) | Canonical pos | Human aa | Frog pos | Frog aa |",
    "|---|---|---|---|---|",
]
for r in named_rows:
    lines.append(
        f"| {r['agx1_pos']} | {r['reference_pos']} | {r['reference_residue']} | "
        f"{r['target_pos']} | {r['target_residue']} |"
    )
lines += [
    "",
    "Human UniProt mutagenesis sites mapped to frog:",
    "",
    "| Human interval | Human aa | Frog aa (aligned) | Human mutant phenotype |",
    "|---|---|---|---|",
]
for m in mutagenesis:
    lines.append(
        f"| {m['start']}-{m['end']} | {m['human']} | {m['frog']} | {m['description']} |"
    )
lines.append("")
(HERE / "RESULTS.md").write_text("\n".join(lines))
print("\n".join(lines))
