#!/usr/bin/env python3
"""Map zebrafish dcxr (Q567K5) onto human DCXR and place it among PTHR44252 members.

Run with the repository environment: UV_NO_SYNC=1 uv run python compare_sequences.py

Inputs (all UniProt flat files, downloaded from rest.uniprot.org):
  ../dcxr-uniprot.txt           Q567K5 zebrafish dcxr (target)
  Q7Z4W1.txt                    human DCXR (PTHR44252:SF2)
  Q91X52.txt                    mouse Dcxr (SF2)
  Q8JIS3.txt                    chicken DER, D-erythrulose reductase (SF3)
  Q21929.txt                    C. elegans dhs-21, L-xylulose reductase (SF3)
  P08074.txt, Q29529.txt        mouse / pig CBR2 (SF1, outgroup subfamily)

Outputs: results.json, alignment.txt, RESULTS.md.
Alignments describe sequence correspondence, not activity.
"""

import json
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor
from Bio import Phylo

HERE = Path(__file__).resolve().parent

MEMBERS = [
    ("Q567K5", HERE.parent / "dcxr-uniprot.txt"),
    ("Q7Z4W1", HERE / "Q7Z4W1.txt"),
    ("Q91X52", HERE / "Q91X52.txt"),
    ("Q8JIS3", HERE / "Q8JIS3.txt"),
    ("Q21929", HERE / "Q21929.txt"),
    ("P08074", HERE / "P08074.txt"),
    ("Q29529", HERE / "Q29529.txt"),
]


def parse_flat(path: Path) -> dict:
    """Parse sequence, PANTHER subfamily, gene name and FT active/binding sites."""
    lines = path.read_text().splitlines()
    seq, in_seq = [], False
    subfamily, gene = "", ""
    features = []
    current = None
    for line in lines:
        if line.startswith("SQ   "):
            in_seq = True
            continue
        if in_seq:
            if line.startswith("//"):
                break
            seq.append(line.replace(" ", ""))
            continue
        if line.startswith("DR   PANTHER;") and ":SF" in line:
            subfamily = line.split(";")[1].strip()
        if line.startswith("GN   Name=") and not gene:
            gene = line.split("Name=")[1].split(";")[0].split(" ")[0]
        if line.startswith("FT   ") and line[5] != " ":
            ftype = line[5:21].strip()
            loc = line[21:].strip()
            current = None
            if ftype in {"ACT_SITE", "BINDING"} and loc.isdigit():
                current = {"type": ftype, "pos": int(loc), "note": ""}
                features.append(current)
        elif line.startswith("FT   ") and current is not None:
            q = line[21:].strip()
            if q.startswith("/note=") or q.startswith("/ligand="):
                current["note"] += q.split("=", 1)[1].strip('"') + " "
    return {
        "sequence": "".join(seq),
        "subfamily": subfamily,
        "gene": gene,
        "features": features,
    }


def make_aligner() -> PairwiseAligner:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    return aligner


def identity(aln, a: str, b: str) -> tuple[int, int]:
    ident, cols = 0, 0
    for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        x, y, u, v = int(x), int(y), int(u), int(v)
        for k in range(y - x):
            cols += 1
            ident += a[x + k] == b[u + k]
    return ident, cols


def main() -> None:
    data = {acc: parse_flat(p) for acc, p in MEMBERS}
    aligner = make_aligner()
    target = data["Q567K5"]["sequence"]
    human = data["Q7Z4W1"]
    aln = aligner.align(human["sequence"], target)[0]
    pairs = {}
    for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        x, y, u, v = int(x), int(y), int(u), int(v)
        for k in range(y - x):
            pairs[int(x) + k + 1] = int(u) + k + 1
    feats = []
    for f in human["features"]:
        q = pairs.get(f["pos"])
        feats.append(
            {
                "type": f["type"],
                "note": f["note"].strip(),
                "human_pos": f["pos"],
                "human_res": human["sequence"][f["pos"] - 1],
                "zebrafish_pos": q,
                "zebrafish_res": target[q - 1] if q else None,
            }
        )
    accs = [a for a, _ in MEMBERS]
    pid = {}
    for i, a in enumerate(accs):
        for b in accs[i + 1 :]:
            al = aligner.align(data[a]["sequence"], data[b]["sequence"])[0]
            ident, cols = identity(al, data[a]["sequence"], data[b]["sequence"])
            pid[(a, b)] = pid[(b, a)] = ident / cols
    labels = [f"{a}_{data[a]['gene']}" for a in accs]
    matrix = [[1 - pid[(accs[i], accs[j])] for j in range(i)] + [0.0] for i in range(len(accs))]
    tree = DistanceTreeConstructor().nj(DistanceMatrix(labels, matrix))
    tree.root_with_outgroup({"name": labels[accs.index("P08074")]}, {"name": labels[accs.index("Q29529")]})
    import io

    buf = io.StringIO()
    Phylo.write(tree, buf, "newick")
    newick = buf.getvalue().strip()

    out = {
        "target": "Q567K5",
        "target_length": len(target),
        "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5; NJ on 1 - pairwise identity",
        "human_alignment": {
            "identical": identity(aln, human["sequence"], target)[0],
            "human_length": len(human["sequence"]),
        },
        "human_feature_mapping": feats,
        "members": {a: {"gene": data[a]["gene"], "subfamily": data[a]["subfamily"], "length": len(data[a]["sequence"])} for a in accs},
        "identity_to_target": {b: round(pid[("Q567K5", b)], 3) for b in accs if b != "Q567K5"},
        "nj_tree_newick": newick,
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
    (HERE / "alignment.txt").write_text(str(aln) + "\n")

    lines = [
        "# dcxr (Q567K5): human DCXR mapping and PTHR44252 subfamily placement",
        "",
        "Target sequence is read from `dcxr-uniprot.txt` (UniProt Q567K5, 244 aa).",
        "",
        out["method"] + ".",
        "",
        "## Alignment to human DCXR (Q7Z4W1)",
        "",
        f"Q567K5 ({len(target)} aa) vs Q7Z4W1 ({len(human['sequence'])} aa): {out['human_alignment']['identical']} identical residues.",
        "",
        "| Human feature | Human pos | Human res | Zebrafish pos | Zebrafish res |",
        "|---|---|---|---|---|",
    ]
    for f in feats:
        lines.append(f"| {f['type']} {f['note']} | {f['human_pos']} | {f['human_res']} | {f['zebrafish_pos']} | {f['zebrafish_res']} |")
    lines += [
        "",
        "## Pairwise identity of Q567K5 to PTHR44252 members",
        "",
        "| Accession | Gene | PANTHER subfamily | Identity to Q567K5 |",
        "|---|---|---|---|",
    ]
    for b in accs[1:]:
        lines.append(f"| {b} | {data[b]['gene']} | {data[b]['subfamily']} | {pid[('Q567K5', b)]:.3f} |")
    lines += [
        "",
        "## Neighbour-joining tree (rooted on the CBR2 subfamily SF1)",
        "",
        "```",
        newick,
        "```",
        "",
        "A distance tree from seven sequences is a coarse check on placement, not a substitute for the PANTHER/PAINT tree.",
        "",
    ]
    (HERE / "RESULTS.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
