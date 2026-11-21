# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests", "pyyaml"]
# ///
"""Map E. coli ThiI (P77718) functional residues onto other PTHR43209 members.

Global pairwise alignment (Bio.Align.PairwiseAligner, BLOSUM62, gap open -10, extend
-0.5) of each target against P77718, using current UniProt sequences. Writes
PTHR43209-residue-alignment.yaml beside this script. Supports the residue
correspondences cited in PTHR43209-review.yaml. MJ0421 (Q57864) and MJ1257 (Q58654) are
included only to show that their mapped positions are not meaningful: neither has the
ThiI PP-loop or rhodanese domain, so the alignment pairs unrelated sequence.

Run: uv run interpro/panther/PTHR43209/PTHR43209-residue-alignment.py
"""
from pathlib import Path
import requests, yaml
from Bio import Align
from Bio.Align import substitution_matrices

ANCHOR = "P77718"
RESIDUES = [189, 321, 344, 414, 456]  # D189, K321 (PP-loop); C344; R414, C456 (rhodanese)
TARGETS = ["O34595", "A0KZA4", "Q8EGR4", "Q8ZT61", "Q58341", "Q58654", "Q57864"]


def fetch(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    d = r.json()
    return d["sequence"]["value"], d["entryAudit"]["sequenceVersion"], d["organism"]["scientificName"]


def main():
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    anchor, aver, _ = fetch(ANCHOR)
    out = {"anchor": {"accession": f"UniProtKB:{ANCHOR}", "sequence_version": aver,
                      "residues": {p: anchor[p - 1] for p in RESIDUES}},
           "method": "Bio.Align.PairwiseAligner global, BLOSUM62, open -10, extend -0.5",
           "targets": []}
    for acc in TARGETS:
        seq, ver, org = fetch(acc)
        aln = aligner.align(anchor, seq)[0]
        pos = {}
        for (a0, a1), (t0, _t1) in zip(*aln.aligned):
            for i in range(a1 - a0):
                pos[a0 + i + 1] = t0 + i + 1
        out["targets"].append({
            "accession": f"UniProtKB:{acc}", "organism": org, "sequence_version": ver,
            "length": len(seq),
            "aligned": {p: ({"position": int(pos[p]), "residue": seq[pos[p] - 1]} if p in pos else None)
                        for p in RESIDUES}})
    path = Path(__file__).with_name("PTHR43209-residue-alignment.yaml")
    path.write_text(yaml.safe_dump(out, sort_keys=False))
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
