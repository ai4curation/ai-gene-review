"""Global alignment of the donkey UniProt sequence to its human ortholog.

Usage: uv run python align.py <donkey_uniprot.txt> <human_accession> <out_dir> [human_region ...]
Fetches the human canonical FASTA from UniProt REST (saved to out_dir), parses the
donkey sequence from the local UniProt flat file, runs a Biopython global alignment
(BLOSUM62, gap open -10, extend -0.5) and prints identity/coverage, the aligned
blocks, the C-termini, and identity within optional human regions "start-end"
(1-based, inclusive).
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

donkey_file, human_acc, out_dir = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)
dacc, dseq = parse_flat(donkey_file)
hseq = fetch_fasta(human_acc, out_dir)
al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10; al.extend_gap_score = -0.5
al.mode = "global"
aln = al.align(dseq, hseq)[0]
pairs = ident = 0
for (ds, de), (hs, he) in zip(*aln.aligned):
    for i, j in zip(range(ds, de), range(hs, he)):
        pairs += 1; ident += dseq[i] == hseq[j]
print(f"donkey {dacc} length {len(dseq)}; human {human_acc} length {len(hseq)}")
print(f"aligned pairs {pairs}; identical {ident}; identity over aligned pairs {100*ident/pairs:.2f}%")
print(f"coverage of human {100*pairs/len(hseq):.2f}%; coverage of donkey {100*pairs/len(dseq):.2f}%")
print("aligned blocks (donkey start-end : human start-end, 1-based):")
for (ds, de), (hs, he) in zip(*aln.aligned):
    print(f"  {ds+1}-{de} : {hs+1}-{he}")
print("donkey C-terminus:", dseq[-10:], "human C-terminus:", hseq[-10:])
for reg in sys.argv[4:]:
    rs, re_ = map(int, reg.split("-"))
    n = idn = 0
    for (ds, de), (hs, he) in zip(*aln.aligned):
        for i, j in zip(range(ds, de), range(hs, he)):
            if rs <= j + 1 <= re_:
                n += 1; idn += dseq[i] == hseq[j]
    print(f"human region {reg}: {n} of {re_-rs+1} residues aligned, {idn} identical")
