"""Locate the PROSITE PS00167 (TRP_SYNTHASE_ALPHA) motif and the TrpA catalytic
Glu/Asp pair in ZmTSAlike (A0A1D6L7U4) and E. coli TrpA (P0A877), and compare
with the ACT_SITE features in each UniProt record. Also checks the N-terminus
against the ZmTSAlike expression primer of PMID:18430213.

Usage: python check_active_site.py
Fetches sequences and records live from rest.uniprot.org.
"""
import re
import urllib.request

PS00167 = re.compile(r"[LIVM]E[LIVM]G.{2}[FY][ST][DE][PA][LIVMY][AGLM][DE]G")


def fetch(acc, fmt):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.{fmt}"
    with urllib.request.urlopen(url) as r:
        return r.read().decode()


def seq_of(acc):
    return "".join(fetch(acc, "fasta").splitlines()[1:])


def act_sites(acc):
    txt = fetch(acc, "txt")
    return [int(m.group(1)) for m in re.finditer(r"^FT   ACT_SITE\s+(\d+)", txt, re.M)]


for acc in ["P0A877", "A0A1D6L7U4"]:
    s = seq_of(acc)
    m = PS00167.search(s)
    print(f"== {acc} length={len(s)}")
    if not m:
        print("  PS00167 motif not found")
        continue
    start = m.start() + 1
    glu = start + 1  # pattern position 2 (E)
    asp = start + 12  # pattern position 13 (D of the D-G)
    print(f"  PS00167 match {start}-{m.end()}: {m.group()}")
    print(f"  catalytic Glu (pattern pos 2): {s[glu-1]}{glu}")
    print(f"  catalytic Asp (pattern pos 13): {s[asp-1]}{asp}")
    for p in act_sites(acc):
        print(f"  UniProt ACT_SITE {p}: residue {s[p-1]}")

# Primer check: ZmTSAlike forward expression primer (PMID:18430213 Methods)
primer = "CGCATATGGCCAACGGCGGCG"
orf = primer[primer.index("ATG"):]
codon = {"ATG": "M", "GCC": "A", "AAC": "N", "GGC": "G"}
pep = "".join(codon.get(orf[i:i+3], "?") for i in range(0, len(orf) - len(orf) % 3, 3))
print("ZmTSAlike primer encodes N-terminus:", pep, "| A0A1D6L7U4 starts:", seq_of("A0A1D6L7U4")[:len(pep)])
