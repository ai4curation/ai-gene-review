"""Global pairwise identity of walnut A0A2I4G8T1 against Arabidopsis UGT73C/UGT89 members.

Fetches sequences and PANTHER subfamily from UniProt REST, aligns with
Bio.Align.PairwiseAligner (BLOSUM62, gap open -10, extend -0.5) and reports
percent identity over aligned columns. Also reports the residue at the
conserved PSPG-box positions (W..HCGWNS..E..Q) in the target.
"""
import io
import json
import re
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

TARGET = "A0A2I4G8T1"
OTHERS = ["Q9ZQ96", "Q9ZQ97", "Q9ZQ98", "Q9ZQ99", "Q9ZQ94", "Q9ZQ95", "Q9SCP5", "Q9C9B0", "Q9LZD8", "Q8VZE9"]


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}?format=json&fields=accession,gene_primary,sequence,xref_panther"
    d = json.load(urllib.request.urlopen(url))
    gene = d.get("genes", [{}])[0].get("geneName", {}).get("value", "")
    sfs = [x["id"] for x in d.get("uniProtKBCrossReferences", []) if ":SF" in x["id"]]
    return gene, d["sequence"]["value"], ";".join(sfs)


aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

tg, tseq, tsf = fetch(TARGET)
print(f"target\t{TARGET}\tlen={len(tseq)}\t{tsf}")
m = re.search(r"W.PQ..IL.H..[VI]G.F.THCGWNS..E", tseq)
print("PSPG motif:", m.group(0) if m else "NOT FOUND", "start", m.start() + 1 if m else None)
if m:
    box = tseq[m.start():m.start() + 44]
    print(f"PSPG box (44 aa, {m.start() + 1}-{m.start() + 44}): {box}; last residue: {box[-1]}")
rows = []
for acc in OTHERS:
    g, s, sf = fetch(acc)
    aln = aligner.align(tseq, s)[0]
    ident = sum(1 for a, b in zip(*aln) if a == b and a != "-")
    cols = sum(1 for a, b in zip(*aln) if a != "-" and b != "-")
    rows.append((ident / cols * 100, acc, g, len(s), sf))
for pid, acc, g, n, sf in sorted(rows, reverse=True):
    print(f"{acc}\t{g}\tlen={n}\t{sf}\tidentity={pid:.1f}%")
