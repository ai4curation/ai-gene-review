"""Locate the PROPPIN phosphoinositide-binding motif in fly Atg18a and its paralogs.

PROPPINs (Atg18/WIPI) bind PI3P and PI(3,5)P2 through two sites on blades 5 and 6
of the beta-propeller, built around a conserved [F/L]RRG motif (Baskaran et al. 2012;
Krick et al. 2012). This script fetches sequences from UniProt (REST), aligns each fly
PROPPIN and yeast Atg18 globally to human WIPI2 (Q9Y4P8), and reports which residues
align to the WIPI2 FRRG motif. It prints what it finds; nothing is hard-coded except
the accession list and the motif search pattern.

Usage: python proppin_motifs.py
"""

import re
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCESSIONS = {
    "Q9Y4P8": "human WIPI2",
    "Q5MNZ9": "human WIPI1",
    "Q9Y484": "human WDR45/WIPI4",
    "P43601": "yeast Atg18",
    "M9PER1": "fly Atg18a (isoform E)",
    "Q9VSF0": "fly Atg18a (isoform A)",
    "Q9VIE1": "fly Atg18b",
    "Q9VHJ2": "fly CG11975",
}
REFERENCE = "Q9Y4P8"
MOTIF = re.compile(r"[FL]RRG")


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def main() -> int:
    seqs = {acc: fetch(acc) for acc in ACCESSIONS}
    ref = seqs[REFERENCE]
    ref_hits = [(m.start(), m.group()) for m in MOTIF.finditer(ref)]
    print(f"Reference {REFERENCE} ({ACCESSIONS[REFERENCE]}), {len(ref)} aa")
    print(f"  [FL]RRG matches: {[(s + 1, g) for s, g in ref_hits]}")
    if not ref_hits:
        print("  no motif in reference; stopping")
        return 1
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    for acc, name in ACCESSIONS.items():
        if acc == REFERENCE:
            continue
        seq = seqs[acc]
        aln = aligner.align(ref, seq)[0]
        # map reference positions to target positions
        ref_to_tgt = {}
        for (rs, re_), (ts, te) in zip(*aln.aligned):
            for k in range(re_ - rs):
                ref_to_tgt[rs + k] = ts + k
        identical = sum(
            1 for r, t in ref_to_tgt.items() if ref[r] == seq[t]
        )
        print(f"\n{acc} ({name}), {len(seq)} aa; identical aligned residues to WIPI2: {identical}"
              f" ({100.0 * identical / len(ref):.1f}% of WIPI2 length)")
        own = [(m.start() + 1, m.group()) for m in MOTIF.finditer(seq)]
        print(f"  own [FL]RRG matches: {own}")
        for start, motif in ref_hits:
            window = []
            for k in range(-3, 7):
                r = start + k
                t = ref_to_tgt.get(r)
                window.append(seq[t] if t is not None else "-")
            tpos = ref_to_tgt.get(start)
            print(f"  aligned to WIPI2 {motif}{start + 1}-{start + 4} (context -3..+6): "
                  f"{''.join(window)} (target start {tpos + 1 if tpos is not None else 'gap'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
