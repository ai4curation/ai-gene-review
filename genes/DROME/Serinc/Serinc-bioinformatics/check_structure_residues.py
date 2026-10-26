"""Check which Serinc isoform's numbering matches residues named in the DmSERINC
cryo-EM paper (Pye et al. 2020, PMID:31907454): C71, C95, C238, C299 (disulphides),
Y42, Q136, W140, K143, F177, Q181, Y282, Y285, S289, Y395, H401, T414, W418, K438.

Run: uv run --with biopython python check_structure_residues.py
"""
from Bio import SeqIO

named = [("C", 71), ("C", 95), ("C", 238), ("C", 299), ("Y", 42), ("Q", 136), ("W", 140),
         ("K", 143), ("F", 177), ("Q", 181), ("Y", 282), ("Y", 285), ("S", 289), ("Y", 395),
         ("H", 401), ("T", 414), ("W", 418), ("K", 438)]
for r in SeqIO.parse("serinc_isoforms_and_TMS1.fasta", "fasta"):
    acc = r.id.split("|")[1]
    if acc == "Q12116":
        continue
    s = str(r.seq)
    hits = [f"{aa}{pos}" for aa, pos in named if pos <= len(s) and s[pos - 1] == aa]
    miss = [f"{aa}{pos}(found {s[pos - 1] if pos <= len(s) else '-'})" for aa, pos in named
            if not (pos <= len(s) and s[pos - 1] == aa)]
    print(f"{acc}\tlen={len(s)}\tmatched={len(hits)}/{len(named)}\tmismatched={miss}")

# M9PCT1 differs from isoform A (Q9VV58) by a short deletion in the cytosolic loop near
# residue 366 (see compare_isoforms.py); test the C-terminal residues at offset -7.
seqs = {r.id.split("|")[1]: str(r.seq) for r in SeqIO.parse("serinc_isoforms_and_TMS1.fasta", "fasta")}
c = seqs["M9PCT1"]
print("M9PCT1 C-terminal residues at isoform-A position minus 7:",
      [f"{aa}{pos}->{c[pos - 8]}{pos - 7}" for aa, pos in named if pos > 366])
print("PA region 360-375:", seqs["Q9VV58"][359:375], " PC region 360-368:", c[359:368])
