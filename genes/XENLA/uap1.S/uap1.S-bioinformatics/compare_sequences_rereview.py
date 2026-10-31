# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Re-review sequence comparison of Xenopus laevis uap1.S (Q6DCZ6) with human UAP1 (Q16222).

Inputs (independent of any ProtNLM output):
  ../uap1.S-uniprot.txt          UniProt flat file for Q6DCZ6 (sequence)
  ../uap1.S-human-ortholog.json  UniProt JSON for human UAP1 Q16222 (sequence, ligand-labelled features)

Outputs: RESULTS-rereview.md and results-rereview.json in this directory.
Run: uv run --script compare_sequences_rereview.py
"""

import json
from collections import defaultdict
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent


def read_flatfile_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("SQ "))
    seq = []
    for ln in lines[start + 1 :]:
        if ln.startswith("//"):
            break
        seq.append(ln.replace(" ", ""))
    return "".join(seq)


frog = read_flatfile_seq(HERE.parent / "uap1.S-uniprot.txt")
human_rec = json.loads((HERE.parent / "uap1.S-human-ortholog.json").read_text())
human = human_rec["sequence"]["value"]

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aln = aligner.align(human, frog)[0]

h2f = {}
identical = 0
aligned = 0
for (hs, he), (fs, fe) in zip(*aln.aligned):
    for k in range(he - hs):
        h2f[int(hs) + k + 1] = int(fs) + k + 1
        aligned += 1
        if human[hs + k] == frog[fs + k]:
            identical += 1
blocks = [
    {"human": [int(hs) + 1, int(he)], "frog": [int(fs) + 1, int(fe)]}
    for (hs, he), (fs, fe) in zip(*aln.aligned)
]

sites: dict[int, set[str]] = defaultdict(set)
for f in human_rec["features"]:
    if f["type"] == "Binding site":
        s = f["location"]["start"]["value"]
        e = f["location"]["end"]["value"]
        for p in range(s, e + 1):
            sites[p].add(f.get("ligand", {}).get("name", "unlabelled"))
site_rows = []
for p in sorted(sites):
    fp = h2f.get(p)
    site_rows.append(
        {
            "human_pos": p,
            "human_res": human[p - 1],
            "frog_pos": fp,
            "frog_res": frog[fp - 1] if fp else None,
            "conserved": bool(fp and frog[fp - 1] == human[p - 1]),
            "ligands": sorted(sites[p]),
        }
    )

alt = []
for f in human_rec["features"]:
    if f["type"] != "Alternative sequence":
        continue
    s = f["location"]["start"]["value"]
    e = f["location"]["end"]["value"]
    alt.append(
        {
            "start": s,
            "end": e,
            "description": f.get("description"),
            "mapped_in_frog": sum(1 for p in range(s, e + 1) if p in h2f),
        }
    )

res = {
    "frog_accession": "Q6DCZ6",
    "frog_length": len(frog),
    "human_accession": human_rec["primaryAccession"],
    "human_length": len(human),
    "aligned_pairs": aligned,
    "identical": identical,
    "percent_identity_over_aligned": round(100 * identical / aligned, 1),
    "aligned_blocks": blocks,
    "binding_sites": site_rows,
    "human_alternative_sequences": alt,
}
(HERE / "results-rereview.json").write_text(json.dumps(res, indent=2) + "\n")

n_cons = sum(r["conserved"] for r in site_rows)
md = [
    "# uap1.S re-review: Q6DCZ6 vs human UAP1 Q16222",
    "",
    "Inputs: `../uap1.S-uniprot.txt` (frog sequence) and `../uap1.S-human-ortholog.json` (human UniProt record).",
    "Global Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5.",
    "",
    f"Frog Q6DCZ6 length: {len(frog)}; human Q16222 (displayed isoform AGX2) length: {len(human)}.",
    f"Aligned residue pairs: {aligned}; identical: {identical} ({res['percent_identity_over_aligned']}%).",
    "",
    "## Aligned blocks",
    "",
    "| Human interval | Frog interval |",
    "|---|---|",
]
md += [f"| {b['human'][0]}-{b['human'][1]} | {b['frog'][0]}-{b['frog'][1]} |" for b in blocks]
md += [
    "",
    "## Human alternative-sequence features",
    "",
    "| Human interval | Description | Human positions aligned to frog |",
    "|---|---|---|",
]
md += [f"| {a['start']}-{a['end']} | {a['description']} | {a['mapped_in_frog']} |" for a in alt]
md += [
    "",
    "## Human UDP-HexNAc binding-site residues mapped to frog",
    "",
    "| Human pos | Human res | Frog pos | Frog res | Conserved | Ligands |",
    "|---|---|---|---|---|---|",
]
md += [
    f"| {r['human_pos']} | {r['human_res']} | {r['frog_pos']} | {r['frog_res']} | "
    f"{'yes' if r['conserved'] else 'NO'} | {'; '.join(r['ligands'])} |"
    for r in site_rows
]
md += [
    "",
    f"Binding-site positions conserved: {n_cons} of {len(site_rows)}.",
    "",
    "Conservation of contact residues is consistent with, but does not by itself prove, retained catalysis;",
    "substrate preference (GlcNAc-1-P vs GalNAc-1-P) of the frog product has not been measured.",
]
(HERE / "RESULTS-rereview.md").write_text("\n".join(md) + "\n")
print("\n".join(md))
