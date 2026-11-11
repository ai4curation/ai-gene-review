"""Map the DmSERINC cryo-EM structure (Pye et al. 2020, PMID:31907454; PDB 6SP2)
onto Serinc isoform F (M9PFR2), the UniProt/FlyBase gene-centric canonical product.

The paper's residue numbering follows isoform A (Q9VV58). This script asks:
  1. where isoform F diverges from isoform A,
  2. which of the structurally named DmSERINC residues isoform F still carries,
  3. how many Phobius transmembrane helices each isoform is predicted to have.

Run: uv run --with biopython python compare_isoformF_rereview.py
"""

from Bio import SeqIO

# Residues named in DmSERINC (isoform A) numbering in Pye et al. 2020:
#  - subdomain A pocket at the membrane-cytosol interface
POCKET_A = [("Y", 42), ("Q", 136), ("W", 140), ("K", 143), ("Y", 395), ("H", 401)]
#  - hydrophilic cleft between the subdomains, corked by Trp418, plugged by Phe177
CLEFT = [("Q", 181), ("Y", 282), ("Y", 285), ("S", 289), ("T", 414), ("K", 438),
         ("W", 418), ("F", 177)]
#  - the two disulphides
DISULPHIDE = [("C", 71), ("C", 95), ("C", 238), ("C", 299)]
NAMED = POCKET_A + CLEFT + DISULPHIDE

seqs = {r.id.split("|")[1]: str(r.seq)
        for r in SeqIO.parse("serinc_isoforms_and_TMS1.fasta", "fasta")}
A, F = seqs["Q9VV58"], seqs["M9PFR2"]

# Isoform F lacks the 7-residue VLTEALS segment that isoform A carries in the
# cytosolic TM8-TM9 loop, so after that indel A position n corresponds to F n-7.
pre = 0
while pre < min(len(A), len(F)) and A[pre] == F[pre]:
    pre += 1
print(f"identical N-terminal prefix: 1-{pre} (A len {len(A)}, F len {len(F)})")

def run_length(off: int) -> int:
    """How far A n == F n-off runs, starting just after the shared prefix."""
    n = pre + off + 1
    while n <= len(A) and n - off <= len(F) and A[n - 1] == F[n - off - 1]:
        n += 1
    return n - 1


offset = max(range(1, 16), key=run_length)
last_common = run_length(offset)
print(f"after the indel, A n == F n-{offset} up to A{last_common} (= F{last_common - offset})")
print(f"isoform A C-terminal segment A{last_common + 1}-{len(A)}: {A[last_common:]}")
print(f"isoform F C-terminal segment F{last_common - offset + 1}-{len(F)}: {F[last_common - offset:]}")

print("\nstructurally named DmSERINC residues in isoform F:")
for aa, n in NAMED:
    assert A[n - 1] == aa, (aa, n, A[n - 1])
    m = n if n <= pre else n - offset
    if n > last_common:
        print(f"  {aa}{n}\tABSENT (lies in the isoform-A-specific C-terminus)")
    else:
        print(f"  {aa}{n}\t-> F{m} = {F[m - 1]}\t{'ok' if F[m - 1] == aa else 'MISMATCH'}")

# Phobius transmembrane helices, as recorded in the UniProt flat files
PHOBIUS = {
    "Q9VV58": [(38, 58), (103, 125), (137, 157), (169, 193), (205, 231),
               (243, 261), (333, 355), (399, 419), (439, 459)],
    "M9PFR2": [(38, 58), (103, 125), (137, 157), (169, 193), (205, 231),
               (243, 264), (333, 352), (396, 416)],
}
print("\nPhobius transmembrane helices (UniProt):")
for acc, tms in PHOBIUS.items():
    print(f"  {acc}: {len(tms)} helices, last at {tms[-1]}")
