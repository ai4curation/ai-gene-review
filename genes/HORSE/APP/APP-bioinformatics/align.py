# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Global alignment of the horse APP UniProt sequence to human APP770 (P05067).

Usage: uv run --script align.py <horse_uniprot.txt> <human_accession> <out_dir> [human_region ...]
Fetches the human canonical FASTA from UniProt REST (saved to out_dir), parses the
horse sequence from the local UniProt flat file, runs a Biopython global alignment
(BLOSUM62, gap open -10, extend -0.5) and prints identity/coverage, aligned blocks,
gaps, mismatches, and identity within optional human regions "start-end" (1-based).
"""
import sys, urllib.request, pathlib
from Bio import Align
from Bio.Align import substitution_matrices

def parse_flat(path):
    seq, inseq, acc = [], False, None
    for line in open(path):
        if line.startswith("AC") and acc is None:
            acc = line.split()[1].rstrip(";")
        if line.startswith("SQ"):
            inseq = True; continue
        if line.startswith("//"):
            break
        if inseq:
            seq.append("".join(line.split()))
    return acc, "".join(seq)

def fetch_fasta(acc, out_dir):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url).read().decode()
    (out_dir / f"{acc}.fasta").write_text(txt)
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))

qfile, human_acc, out_dir = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)
qacc, qseq = parse_flat(qfile)
hseq = fetch_fasta(human_acc, out_dir)
al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10; al.extend_gap_score = -0.5
al.mode = "global"
aln = al.align(qseq, hseq)[0]
pairs = ident = 0
mism = []
for (qs, qe), (hs, he) in zip(*aln.aligned):
    for i, j in zip(range(qs, qe), range(hs, he)):
        pairs += 1
        if qseq[i] == hseq[j]:
            ident += 1
        else:
            mism.append(f"{hseq[j]}{j+1}{qseq[i]}")
print(f"query {qacc} length {len(qseq)}; human {human_acc} length {len(hseq)}")
print(f"aligned pairs {pairs}; identical {ident}; identity over aligned pairs {100*ident/pairs:.2f}%")
print(f"coverage of human {100*pairs/len(hseq):.2f}%; coverage of query {100*pairs/len(qseq):.2f}%")
print("aligned blocks (query start-end : human start-end, 1-based):")
blocks = list(zip(*aln.aligned))
for (qs, qe), (hs, he) in blocks:
    print(f"  {qs+1}-{qe} : {hs+1}-{he}")
for ((qs1, qe1), (hs1, he1)), ((qs2, qe2), (hs2, he2)) in zip(blocks, blocks[1:]):
    if hs2 > he1:
        print(f"human residues {he1+1}-{hs2} ({hseq[he1:hs2]}) absent from query")
    if qs2 > qe1:
        print(f"query residues {qe1+1}-{qs2} ({qseq[qe1:qs2]}) absent from human")
print("substitutions (human residue, human position, query residue):", " ".join(mism))
print("query C-terminus:", qseq[-10:], "human C-terminus:", hseq[-10:])
for reg in sys.argv[4:]:
    rs, re_ = map(int, reg.split("-"))
    n = idn = 0
    for (qs, qe), (hs, he) in blocks:
        for i, j in zip(range(qs, qe), range(hs, he)):
            if rs <= j + 1 <= re_:
                n += 1; idn += qseq[i] == hseq[j]
    print(f"human region {reg}: {n} of {re_-rs+1} residues aligned, {idn} identical")
