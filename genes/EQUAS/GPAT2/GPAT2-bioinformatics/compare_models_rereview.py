# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85"]
# ///
"""Compare the donkey GPAT2 gene models with reviewed mouse Gpat2 (Q14DK4).

Usage:
    uv run --script compare_models_rereview.py REF.txt OUT.json MODEL.txt [MODEL.txt ...]

For each donkey UniProt flat file, a global alignment (BLOSUM62, gap open -10,
extension -0.5) to the reference is computed. Reported per model: length,
Ensembl gene/transcript, identity among paired residues, coverage of each
sequence, the model residues aligned to reference HXXXXD motif positions 205
and 210 (the residues mutated in PMID:23611983), the model residues aligned to
the reference predicted transmembrane segments (306-332, 450-472), and the
reference ranges with no partner in the model. Alignment identity does not by
itself establish orthology; PANTHER subfamily membership is read separately.
"""
import json
import re
import sys
from pathlib import Path

from Bio import Align, SeqIO
from Bio.Align import substitution_matrices


def ranges(positions):
    out = []
    for p in positions:
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out


def ensembl(path):
    m = re.search(r"^DR   Ensembl; (\S+); (\S+); (\S+)\.", path.read_text(), re.M)
    return {"transcript": m.group(1).rstrip(";"), "protein": m.group(2).rstrip(";"), "gene": m.group(3)}


def compare(ref, model_path, aligner):
    mod = SeqIO.read(model_path, "swiss")
    aln = aligner.align(ref.seq, mod.seq)[0]
    x, y = str(aln[0]), str(aln[1])
    ri = mi = 0
    rmap, unpaired_ref, paired, ident = {}, [], 0, 0
    for a, b in zip(x, y):
        if a != "-":
            ri += 1
        if b != "-":
            mi += 1
        if a != "-" and b != "-":
            paired += 1
            ident += a == b
            rmap[ri] = (b, mi)
        elif a != "-":
            unpaired_ref.append(ri)
    seg = lambda s, e: "".join(rmap[i][0] if i in rmap else "-" for i in range(s, e + 1))
    return {
        "accession": mod.id,
        "length": len(mod.seq),
        "ensembl": ensembl(model_path),
        "paired_residues": paired,
        "identity_pct": round(100 * ident / paired, 2),
        "ref_coverage_pct": round(100 * paired / len(ref.seq), 2),
        "model_coverage_pct": round(100 * paired / len(mod.seq), 2),
        "motif_205_210": seg(205, 210),
        "ref_H205": rmap.get(205),
        "ref_D210": rmap.get(210),
        "ref_TM1_306_332": seg(306, 332),
        "ref_TM2_450_472": seg(450, 472),
        "ref_ranges_without_partner": ranges(unpaired_ref),
        "model_C_terminal_30": str(mod.seq[-30:]),
    }


def main():
    ref_path, out = Path(sys.argv[1]), Path(sys.argv[2])
    models = [Path(p) for p in sys.argv[3:]]
    ref = SeqIO.read(ref_path, "swiss")
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    result = {
        "reference": {"accession": ref.id, "length": len(ref.seq), "motif_205_210": str(ref.seq[204:210]),
                      "C_terminal_30": str(ref.seq[-30:])},
        "models": [compare(ref, m, al) for m in models],
    }
    out.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
