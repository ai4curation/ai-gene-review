# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85"]
# ///
"""Align donkey GPAT2 A0A8C4KXU5 with reviewed GPAT2 orthologs.

Usage:
    uv run --script compare_to_orthologs.py DONKEY.txt OUT.json REF.txt [REF.txt ...]

For each reviewed reference (UniProt flat file), a global alignment (BLOSUM62,
gap open -10, extension -0.5) to the donkey sequence is computed. Reported per
reference: identity among paired residues, coverage of each sequence, the donkey
residues aligned to each reference MOTIF and TRANSMEM feature, the reference
ranges with no donkey partner, and the PANTHER subfamily read from each record.
Alignment identity does not by itself establish orthology.
"""
import json
import re
import sys
from pathlib import Path

from Bio import Align, SeqIO
from Bio.Align import substitution_matrices


def features(path, key):
    text = Path(path).read_text()
    return [(int(a), int(b)) for a, b in re.findall(rf"^FT   {key}\s+(\d+)\.\.(\d+)", text, re.M)]


def panther_sf(path):
    return re.findall(r"^DR   PANTHER; (PTHR\d+:SF\d+);", Path(path).read_text(), re.M)


def ranges(positions):
    out = []
    for p in positions:
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out


def compare(donkey_path, ref_path, aligner):
    d = next(SeqIO.parse(donkey_path, "swiss"))
    r = next(SeqIO.parse(ref_path, "swiss"))
    aln = aligner.align(r.seq, d.seq)[0]
    ref_to_model = {}
    for (rs, re_), (ms, me) in zip(*aln.aligned):
        for i in range(int(re_ - rs)):
            ref_to_model[int(rs) + i + 1] = int(ms) + i + 1
    paired = len(ref_to_model)
    ident = sum(1 for rp, mp in ref_to_model.items() if r.seq[rp - 1] == d.seq[mp - 1])

    def mapped(a, b):
        return "".join(d.seq[ref_to_model[p] - 1] if p in ref_to_model else "-" for p in range(a, b + 1))

    return {
        "reference": r.id,
        "reference_length": len(r.seq),
        "reference_panther_subfamily": panther_sf(ref_path),
        "paired_residues": paired,
        "identity_pct": round(100 * ident / paired, 2),
        "ref_coverage_pct": round(100 * paired / len(r.seq), 2),
        "donkey_coverage_pct": round(100 * paired / len(d.seq), 2),
        "motifs": {
            f"{a}-{b}": {"reference": str(r.seq[a - 1 : b]), "donkey": mapped(a, b),
                         "donkey_start": ref_to_model.get(a)}
            for a, b in features(ref_path, "MOTIF")
        },
        "transmembrane": {
            f"{a}-{b}": {"reference": str(r.seq[a - 1 : b]), "donkey": mapped(a, b)}
            for a, b in features(ref_path, "TRANSMEM")
        },
        "ref_ranges_without_partner": ranges([p for p in range(1, len(r.seq) + 1) if p not in ref_to_model]),
    }


def main():
    donkey, out, *refs = sys.argv[1:]
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    d = next(SeqIO.parse(donkey, "swiss"))
    result = {
        "donkey": {"accession": d.id, "length": len(d.seq), "panther_subfamily": panther_sf(donkey)},
        "comparisons": [compare(donkey, ref, aligner) for ref in refs],
    }
    Path(out).write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
