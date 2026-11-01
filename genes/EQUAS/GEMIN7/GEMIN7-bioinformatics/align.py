"""Global alignment of a donkey UniProt sequence to its human ortholog (and optional isoforms).

Usage: uv run python align.py <donkey_uniprot.txt> <out_dir> <human_acc> [<human_acc_or_isoform> ...]
Fetches each human FASTA (canonical or isoform, e.g. P49757-2) and the human canonical
UniProt flat file from UniProt REST into out_dir, parses the donkey sequence from the local
UniProt flat file, runs a Biopython global alignment (BLOSUM62, gap open -10, extend -0.5)
and prints identity/coverage and aligned blocks. Optional --pos donkey positions to report
the aligned human residue (e.g. catalytic residues): --pos 131,415
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

def fetch(url, dest):
    txt = urllib.request.urlopen(url).read().decode()
    dest.write_text(txt)
    return txt

args = sys.argv[1:]
pos = []
if "--pos" in args:
    i = args.index("--pos"); pos = [int(x) for x in args[i+1].split(",")]; del args[i:i+2]
donkey_file, out_dir, accs = args[0], pathlib.Path(args[1]), args[2:]
out_dir.mkdir(parents=True, exist_ok=True)
dacc, dseq = parse_flat(donkey_file)
canon = accs[0].split("-")[0]
fetch(f"https://rest.uniprot.org/uniprotkb/{canon}.txt", out_dir / f"human-{canon}-uniprot.txt")
al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10; al.extend_gap_score = -0.5
al.mode = "global"
for acc in accs:
    txt = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", out_dir / f"{acc}.fasta")
    hseq = "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))
    aln = al.align(dseq, hseq)[0]
    pairs = ident = 0
    mapping = {}
    for (ds, de), (hs, he) in zip(*aln.aligned):
        for i, j in zip(range(ds, de), range(hs, he)):
            pairs += 1; ident += dseq[i] == hseq[j]; mapping[i+1] = j+1
    print(f"## donkey {dacc} length {len(dseq)} vs human {acc} length {len(hseq)}")
    print(f"aligned pairs {pairs}; identical {ident}; identity over aligned pairs {100*ident/pairs:.2f}%")
    print(f"coverage of human {100*pairs/len(hseq):.2f}%; coverage of donkey {100*pairs/len(dseq):.2f}%")
    print("aligned blocks (donkey start-end : human start-end, 1-based):")
    for (ds, de), (hs, he) in zip(*aln.aligned):
        print(f"  {ds+1}-{de} : {hs+1}-{he}")
    for p in pos:
        h = mapping.get(p)
        print(f"donkey {dseq[p-1]}{p} aligns to human " + (f"{hseq[h-1]}{h}" if h else "gap"))
    print()
