#!/usr/bin/env python3
"""Map metal-ligand residues of the M. wolfeii Fwd crystal structure (PDB 5T5I)
onto a Methanothermobacter thermautotrophicus Delta H Fwd subunit sequence.

Usage:
  python map_fwd_metal_sites.py <uniprot.txt> <pdb_chain> [<cache_dir>]

Downloads 5T5I.cif.gz and the polymer-entity records from RCSB (cached),
reads the chain's canonical sequence and the metalc rows of _struct_conn whose first or second
partner is a residue of that chain, globally aligns the chain to the target
sequence (Needleman-Wunsch, BLOSUM62, gap -10/-1 linear approximation), and
prints each ligand residue with the aligned target residue. Pure Python stdlib.
"""
import gzip, os, sys, urllib.request

def read_uniprot_seq(path):
    seq, on = [], False
    for line in open(path):
        if line.startswith("SQ "):
            on = True; continue
        if line.startswith("//"):
            break
        if on:
            seq.append(line.strip().replace(" ", ""))
    return "".join(seq)

def fetch(cache):
    os.makedirs(cache, exist_ok=True)
    p = os.path.join(cache, "5T5I.cif.gz")
    if not os.path.exists(p):
        urllib.request.urlretrieve("https://files.rcsb.org/download/5T5I.cif.gz", p)
    return gzip.open(p, "rt").read().splitlines()

def loop_rows(lines, prefix):
    """Yield dicts for a mmCIF loop whose tags start with prefix."""
    i = 0
    while i < len(lines):
        if lines[i].strip() == "loop_" and i + 1 < len(lines) and lines[i+1].startswith(prefix + "."):
            tags = []
            j = i + 1
            while lines[j].startswith(prefix + "."):
                tags.append(lines[j].strip().split(".", 1)[1]); j += 1
            buf = []
            while j < len(lines) and not lines[j].startswith(("loop_", "#", "_")):
                buf.extend(lines[j].split()); 
                while len(buf) >= len(tags):
                    yield dict(zip(tags, buf[:len(tags)])); buf = buf[len(tags):]
                j += 1
            return
        i += 1

def entity_seqs(cache):
    """Return {auth_asym_id: canonical one-letter sequence} from the RCSB REST API (cached)."""
    import json
    out = {}
    for ent in range(1, 7):
        p = os.path.join(cache, f"5T5I_entity_{ent}.json")
        if not os.path.exists(p):
            urllib.request.urlretrieve(f"https://data.rcsb.org/rest/v1/core/polymer_entity/5T5I/{ent}", p)
        d = json.load(open(p))
        seq = d["entity_poly"]["pdbx_seq_one_letter_code_can"].replace("\n", "")
        for ch in d["rcsb_polymer_entity_container_identifiers"]["auth_asym_ids"]:
            out[ch] = (seq, d["rcsb_polymer_entity"]["pdbx_description"])
    return out

B62 = None
def blosum62():
    m = """A R N D C Q E G H I L K M F P S T W Y V
A 4 -1 -2 -2 0 -1 -1 0 -2 -1 -1 -1 -1 -2 -1 1 0 -3 -2 0
R -1 5 0 -2 -3 1 0 -2 0 -3 -2 2 -1 -3 -2 -1 -1 -3 -2 -3
N -2 0 6 1 -3 0 0 0 1 -3 -3 0 -2 -3 -2 1 0 -4 -2 -3
D -2 -2 1 6 -3 0 2 -1 -1 -3 -4 -1 -3 -3 -1 0 -1 -4 -3 -3
C 0 -3 -3 -3 9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
Q -1 1 0 0 -3 5 2 -2 0 -3 -2 1 0 -3 -1 0 -1 -2 -1 -2
E -1 0 0 2 -4 2 5 -2 0 -3 -3 1 -2 -3 -1 0 -1 -3 -2 -2
G 0 -2 0 -1 -3 -2 -2 6 -2 -4 -4 -2 -3 -3 -2 0 -2 -2 -3 -3
H -2 0 1 -1 -3 0 0 -2 8 -3 -3 -1 -2 -1 -2 -1 -2 -2 2 -3
I -1 -3 -3 -3 -1 -3 -3 -4 -3 4 2 -3 1 0 -3 -2 -1 -3 -1 3
L -1 -2 -3 -4 -1 -2 -3 -4 -3 2 4 -2 2 0 -3 -2 -1 -2 -1 1
K -1 2 0 -1 -3 1 1 -2 -1 -3 -2 5 -1 -3 -1 0 -1 -3 -2 -2
M -1 -1 -2 -3 -1 0 -2 -3 -2 1 2 -1 5 0 -2 -1 -1 -1 -1 1
F -2 -3 -3 -3 -2 -3 -3 -3 -1 0 0 -3 0 6 -4 -2 -2 1 3 -1
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4 7 -1 -1 -4 -3 -2
S 1 -1 1 0 -1 0 0 0 -1 -2 -2 0 -1 -2 -1 4 1 -3 -2 -2
T 0 -1 0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1 1 5 -2 -2 0
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1 1 -4 -3 -2 11 2 -3
Y -2 -2 -2 -3 -2 -1 -2 -3 2 -1 -1 -2 -1 3 -3 -2 -2 2 7 -1
V 0 -3 -3 -3 -1 -2 -2 -3 -3 3 1 -2 1 -1 -2 -2 0 -3 -1 4"""
    rows = m.split("\n"); aa = rows[0].split(); d = {}
    for r in rows[1:]:
        f = r.split()
        for a, v in zip(aa, f[1:]):
            d[(f[0], a)] = int(v)
    return d

def score(a, b):
    return B62.get((a, b), -1)

def nw(s, t, gap=-6):
    n, m = len(s), len(t)
    S = [[0]*(m+1) for _ in range(n+1)]
    P = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): S[i][0] = i*gap; P[i][0] = 1
    for j in range(1, m+1): S[0][j] = j*gap; P[0][j] = 2
    for i in range(1, n+1):
        for j in range(1, m+1):
            d = S[i-1][j-1] + score(s[i-1], t[j-1]); u = S[i-1][j] + gap; l = S[i][j-1] + gap
            best = max(d, u, l); S[i][j] = best
            P[i][j] = 0 if best == d else (1 if best == u else 2)
    i, j, mp = n, m, {}
    ident = alnlen = 0
    while i > 0 or j > 0:
        p = P[i][j]
        if i > 0 and j > 0 and p == 0:
            mp[i] = j; alnlen += 1; ident += s[i-1] == t[j-1]; i -= 1; j -= 1
        elif i > 0 and (j == 0 or p == 1):
            i -= 1
        else:
            j -= 1
    return mp, ident, alnlen

def main():
    global B62
    up, chain = sys.argv[1], sys.argv[2]
    cache = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache")
    B62 = blosum62()
    target = read_uniprot_seq(up)
    lines = fetch(cache)
    seqs = entity_seqs(cache)
    pdbseq, desc = seqs[chain]
    mp, ident, alnlen = nw(pdbseq, target)
    print(f"5T5I chain {chain} ({desc}): {len(pdbseq)} aa; target {os.path.basename(up)}: {len(target)} aa")
    print(f"aligned positions {alnlen}, identical {ident} ({100*ident/alnlen:.1f}% of aligned)")
    seen = set()
    for r in loop_rows(lines, "_struct_conn"):
        if r.get("conn_type_id") != "metalc":
            continue
        for a, b in (("ptnr1", "ptnr2"), ("ptnr2", "ptnr1")):
            if r[f"{a}_auth_asym_id"] == chain and r[f"{a}_label_seq_id"] not in (".", "?"):
                res, num = r[f"{a}_label_comp_id"], int(r[f"{a}_label_seq_id"])
                metal = f"{r[f'{b}_label_comp_id']} {r[f'{b}_auth_asym_id']}{r[f'{b}_auth_seq_id']}"
                key = (res, num, metal)
                if key in seen: continue
                seen.add(key)
                tpos = mp.get(num)
                taa = target[tpos-1] if tpos else "-"
                print(f"  {res}{num} (label_seq) -> {metal}: target {taa}{tpos if tpos else ''}")

if __name__ == "__main__":
    main()
