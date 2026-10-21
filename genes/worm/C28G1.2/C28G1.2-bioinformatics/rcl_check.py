# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Align C28G1.2 (Q18287) against the characterised clade-L worm serpins SRP-2 and
SRP-3 and against its C. briggsae PANTHER sister CBG15466, and report whether the
reactive-centre-loop (RCL) hinge region (P17-P9, consensus E-G-T-E-A-A-A-A) that
precedes the conserved C-terminal 'DHPF' motif of inhibitory serpins is present.

Sequences are fetched live from UniProt REST. Run: uv run rcl_check.py
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q18287": "C28G1.2 (target)",
    "A8XM85": "CBG15466 (C. briggsae, PANTHER sister of target)",
    "O17365": "SRP-2",
    "G5ECY2": "SRP-3",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

hinge = re.compile(r"[EDQ].{0,2}G[TS].{0,2}[AGS][AGS][AGS][AGSV]")
print("accession\tlabel\tlength\tDHPF_pos\thinge_motif_upstream_of_DHPF")
for acc, label in ACCS.items():
    s = seqs[acc]
    m = s.find("DHPF")
    upstream = s[max(0, m - 45):m] if m >= 0 else ""
    h = hinge.search(upstream)
    print(f"{acc}\t{label}\t{len(s)}\t{m + 1 if m >= 0 else 'NA'}\t{h.group(0) if h else 'absent'}")
    print(f"  45 aa upstream of DHPF: {upstream}")

for ref in ["A8XM85", "O17365", "G5ECY2"]:
    aln = aligner.align(seqs["Q18287"], seqs[ref])[0]
    a, b = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    ident = sum(x == y for x, y in pairs)
    print(f"\nQ18287 vs {ref} ({ACCS[ref]}): aligned={len(pairs)} identical={ident} "
          f"identity_over_aligned={ident / len(pairs):.3f} "
          f"target_coverage_of_ref={len(pairs) / len(seqs[ref]):.3f}")
    print(aln)
