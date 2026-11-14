"""Global alignment of P. putida UvrB (Q88LF9) with E. coli UvrB (P0A8F8).

Simple Needleman-Wunsch (match +1, mismatch -1, gap -1) on the sequences in the
cached UniProt flat files; reports identity over aligned columns and the residues
aligned to E. coli beta-hairpin positions Y92, Y93, Y95, Y96, Y101, F108 and the
Walker A segment 39-46. Run from the repository root:
    python3 genes/PSEPK/uvrB/uvrB-bioinformatics/align_ecoli.py
"""
import numpy as np


def seq(path):
    body = open(path).read().split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return "".join(body.split())


a = seq("genes/ECOLI/uvrB/uvrB-uniprot.txt")
b = seq("genes/PSEPK/uvrB/uvrB-uniprot.txt")
n, m, g = len(a), len(b), -1
S = np.zeros((n + 1, m + 1), int)
S[:, 0] = np.arange(n + 1) * g
S[0, :] = np.arange(m + 1) * g
for i in range(1, n + 1):
    for j in range(1, m + 1):
        S[i, j] = max(S[i - 1, j - 1] + (1 if a[i - 1] == b[j - 1] else -1), S[i - 1, j] + g, S[i, j - 1] + g)
i, j, pairs = n, m, {}
ident = cols = 0
while i > 0 and j > 0:
    if S[i, j] == S[i - 1, j - 1] + (1 if a[i - 1] == b[j - 1] else -1):
        pairs[i] = j
        ident += a[i - 1] == b[j - 1]
        cols += 1
        i, j = i - 1, j - 1
    elif S[i, j] == S[i - 1, j] + g:
        i -= 1
    else:
        j -= 1
print(f"E. coli length {n}; P. putida length {m}")
print(f"identity {ident}/{cols} aligned columns = {100 * ident / cols:.1f}%")
for pos in [39, 40, 41, 42, 43, 44, 45, 46, 92, 93, 95, 96, 101, 108]:
    q = pairs.get(pos)
    print(f"E. coli {a[pos - 1]}{pos} -> P. putida {b[q - 1] + str(q) if q else 'gap'}")
