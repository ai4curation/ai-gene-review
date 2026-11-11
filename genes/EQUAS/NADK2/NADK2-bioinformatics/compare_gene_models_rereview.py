# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Compare all donkey NADK2 UniProt gene models with human NADK2 (Q4G0N4).

Usage: uv run --script compare_gene_models_rereview.py <out_dir> ACC [ACC ...]

For each accession, fetches the UniProt FASTA (saved to out_dir as <ACC>.fasta),
globally aligns it to human Q4G0N4 (BLOSUM62, open -10, extend -0.5) and reports
identity, the aligned gapless blocks, which donkey residue aligns to human Met1,
the GGDG motif (human 159-162), and whether the residues aligned to human Ser306,
Lys317 and Trp319 (the positions PMID:23212377 maps to the NAD+-binding Asp/Thr/Tyr
of M. tuberculosis Ppnk) and to human 288-319 (deleted in human isoform 2) exist.
"""
import sys, pathlib, urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

def fetch(acc, out_dir):
    p = out_dir / f"{acc}.fasta"
    if not p.exists():
        p.write_text(urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode())
    txt = p.read_text()
    return txt.splitlines()[0], "".join(l.strip() for l in txt.splitlines()[1:])

out_dir = pathlib.Path(sys.argv[1]); out_dir.mkdir(parents=True, exist_ok=True)
_, hseq = fetch("Q4G0N4", out_dir)
al = Align.PairwiseAligner(mode="global")
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10; al.extend_gap_score = -0.5
print(f"human Q4G0N4 length {len(hseq)}; human 288-319 = {hseq[287:319]}")
for acc in sys.argv[2:]:
    hdr, dseq = fetch(acc, out_dir)
    aln = al.align(dseq, hseq)[0]
    h2d = {}
    for (ds, de), (hs, he) in zip(*aln.aligned):
        for i, j in zip(range(ds, de), range(hs, he)):
            h2d[j + 1] = i + 1
    ident = sum(dseq[h2d[j] - 1] == hseq[j - 1] for j in h2d)
    print(f"\n{acc} length {len(dseq)}  {hdr[:90]}")
    print(f"  aligned pairs {len(h2d)}; identical {ident}; identity {100*ident/len(h2d):.2f}%; human coverage {100*len(h2d)/len(hseq):.2f}%")
    print("  blocks (donkey:human): " + ", ".join(f"{ds+1}-{de}:{hs+1}-{he}" for (ds, de), (hs, he) in zip(*aln.aligned)))
    print(f"  donkey residue aligned to human Met1: {h2d.get(1)}; upstream donkey residues: {(h2d.get(1) or 1) - 1}")
    g = [h2d.get(k) for k in range(159, 163)]
    print(f"  human GGDG 159-162 -> donkey {g} {''.join(dseq[x-1] if x else '-' for x in g)}")
    for pos in (306, 317, 319):
        d = h2d.get(pos)
        print(f"  human {hseq[pos-1]}{pos} -> donkey {dseq[d-1] + str(d) if d else 'ABSENT'}")
    n = sum(1 for j in range(288, 320) if j in h2d)
    print(f"  human 288-319 residues aligned: {n} of 32")
