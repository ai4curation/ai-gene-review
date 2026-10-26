# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Re-review (2026-10-21): compare the two rat Ptk7 TrEMBL gene-model products
(A0A8I6ALM9, A0A8I6AKN3) with mouse Q8BKG3 and human Q13308, and record the
official PANTHER 19.0 rat classification row for A0A8I6ALM9.

Run: uv run --script compare_rat_models_rereview.py > RESULTS-rereview-raw.txt
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["A0A8I6ALM9", "A0A8I6AKN3", "Q8BKG3", "Q13308"]
PANTHER_RAT = ("https://data.pantherdb.org/ftp/sequence_classifications/current_release/"
               "PANTHER_Sequence_Classification_files/PTHR19.0_rat")


def fasta(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def blocks(aln):
    """Yield (target_start, target_end, query_start, query_end, identities) per aligned block (1-based)."""
    t, q = aln.target, aln.query
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        ident = sum(1 for i in range(te - ts) if t[ts + i] == q[qs + i])
        yield ts + 1, te, qs + 1, qe, ident


seqs = {a: fasta(a) for a in ACCS}
for a, s in seqs.items():
    print(f"{a}\tlength={len(s)}\tNterm40={s[:40]}")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

pairs = [("A0A8I6ALM9", "A0A8I6AKN3"), ("A0A8I6ALM9", "Q8BKG3"), ("A0A8I6AKN3", "Q8BKG3")]
for a, b in pairs:
    aln = aligner.align(seqs[a], seqs[b])[0]
    tot = 0
    print(f"\n## {a} (target) vs {b} (query)")
    print("target_interval\tquery_interval\tidentities")
    for ts, te, qs, qe, ident in blocks(aln):
        tot += ident
        print(f"{ts}-{te}\t{qs}-{qe}\t{ident}")
    print(f"total_identities\t{tot}")

print("\n## Official PANTHER 19.0 rat classification row(s) for A0A8I6ALM9 / A0A8I6AKN3")
r = requests.get(PANTHER_RAT, timeout=300)
r.raise_for_status()
for line in r.text.splitlines():
    if "A0A8I6ALM9" in line or "A0A8I6AKN3" in line:
        cols = line.split("\t")
        print("\t".join(cols[:6]))
