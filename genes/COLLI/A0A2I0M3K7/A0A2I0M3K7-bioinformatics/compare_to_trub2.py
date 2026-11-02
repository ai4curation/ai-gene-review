# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Map the 142-aa pigeon A0A2I0M3K7 onto human TRUB2 (O95900) and E. coli TruB (P60340).

Reports: the human TRUB2 span covered by the pigeon sequence, identity over that
span, and whether the E. coli TruB catalytic aspartate (D48, Hoang & Ferre-D'Amare
2001) maps to a residue present in the pigeon sequence.

Run: uv run --script compare_to_trub2.py
"""
import io
import json
from pathlib import Path

import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
PIGEON_UNIPROT = HERE.parent / "A0A2I0M3K7-uniprot.txt"


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return str(next(SeqIO.parse(io.StringIO(r.text), "fasta")).seq)


def pigeon_seq() -> str:
    rec = SeqIO.read(str(PIGEON_UNIPROT), "swiss")
    return str(rec.seq)


def aligner(mode: str) -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = mode
    return a


def residue_map(aln) -> dict[int, int]:
    """1-based target position -> 1-based query position for aligned residues."""
    m = {}
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            m[int(ts) + i + 1] = int(qs) + i + 1
    return m


def main() -> None:
    pig = pigeon_seq()
    hum = fetch("O95900")
    eco = fetch("P60340")
    out: dict = {"pigeon_length": len(pig), "human_TRUB2_length": len(hum), "ecoli_TruB_length": len(eco)}

    a_ph = aligner("local").align(hum, pig)[0]
    blocks = a_ph.aligned
    hstart, hend = int(blocks[0][0][0]) + 1, int(blocks[0][-1][1])
    ident = int(sum(hum[t] == pig[q] for (ts, te), (qs, qe) in zip(*blocks) for t, q in zip(range(ts, te), range(qs, qe))))
    alen = int(sum(te - ts for ts, te in blocks[0]))
    out["human_span_covered_by_pigeon"] = [hstart, hend]
    out["pigeon_span_aligned"] = [int(blocks[1][0][0]) + 1, int(blocks[1][-1][1])]
    out["identity_over_aligned_residues"] = round(ident / alen, 3)
    out["aligned_residues"] = alen
    print(a_ph)

    a_eh = aligner("global").align(eco, hum)[0]
    e2h = residue_map(a_eh)
    d48_h = e2h.get(48)
    out["ecoli_D48_residue"] = eco[47]
    out["ecoli_D48_maps_to_human_position"] = d48_h
    out["human_residue_at_that_position"] = hum[d48_h - 1] if d48_h else None
    out["human_context_pm5"] = hum[d48_h - 6 : d48_h + 5] if d48_h else None
    out["ecoli_context_pm5"] = eco[42:53]
    out["pigeon_covers_catalytic_asp"] = bool(d48_h and hstart <= d48_h <= hend)
    print(a_eh)
    print(json.dumps(out, indent=2))
    (HERE / "compare_to_trub2-results.json").write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
