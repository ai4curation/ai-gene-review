"""Locate the myotubularin HCX5R catalytic loop in MTMR9 and its active partners.

Fetches sequences from UniProt REST and aligns the motif region by a regex anchored on
the conserved loop pattern H-x-x-x-G-x-D-x-T (active myotubularins: HCSDGWDRT).
Prints the loop for each protein and whether the catalytic Cys (loop pos 2) and
Arg (loop pos 8) are present. Usage: uv run python catalytic_motif_rereview.py
"""
import re
import urllib.request

PROTEINS = {
    "MTMR9 (Q96QG7)": "Q96QG7",
    "MTMR6 (Q9Y217)": "Q9Y217",
    "MTMR7 (Q9Y216)": "Q9Y216",
    "MTMR8 (Q96EF0)": "Q96EF0",
    "mouse Mtmr9 (Q9Z2D0)": "Q9Z2D0",
}
LOOP = re.compile(r"H(.)(..)G(.)D(.)T")


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    return "".join(text.splitlines()[1:])


for name, acc in PROTEINS.items():
    seq = fetch(acc)
    hits = [(m.start() + 1, m.group(0)) for m in LOOP.finditer(seq) if 250 < m.start() < 450]
    for pos, loop in hits:
        cys = loop[1] == "C"
        arg = loop[7] == "R"
        print(f"{name}\tlen={len(seq)}\tloop_start={pos}\t{loop}\tcatalytic_Cys={cys}\tcatalytic_Arg={arg}")
    if not hits:
        print(f"{name}\tlen={len(seq)}\tno loop match")
