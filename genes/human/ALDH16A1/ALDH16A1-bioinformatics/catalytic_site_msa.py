"""Map the ALDH catalytic dyad (ALDH2 Cys319 nucleophile, Glu285 general base; UniProt P05091 numbering)
onto ALDH16A1 orthologs with a MAFFT L-INS-i multiple alignment.

Sequences are fetched live from UniProt. Requires `mafft` on PATH.
Run: uv run python catalytic_site_msa.py
"""
import subprocess
import tempfile
import urllib.request

SEQS = {
    "ALDH2_HUMAN": "P05091",
    "AL1A1_HUMAN": "P00352",
    "AL3A1_HUMAN": "P30838",
    "aldh16a1_XENTR": "Q28CF4",
    "aldh16a1_DANRE": "F1QGP1",
    "Aldh16a1_MOUSE": "Q571I9",
    "ALDH16A1_HUMAN": "Q8IZ83",
}
ANCHOR = "ALDH2_HUMAN"
SITES = {"nucleophile Cys": 319, "general base Glu": 285}


def fetch(acc: str) -> str:
    txt = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode()
    return "".join(txt.splitlines()[1:])


seqs = {k: fetch(a) for k, a in SEQS.items()}
with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
    for k, s in seqs.items():
        fh.write(f">{k}\n{s}\n")
out = subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", fh.name], capture_output=True, text=True, check=True).stdout
aln, name = {}, None
for line in out.splitlines():
    if line.startswith(">"):
        name = line[1:].strip(); aln[name] = ""
    else:
        aln[name] += line.strip()


def col_of(name: str, pos: int) -> int:
    n = 0
    for i, ch in enumerate(aln[name]):
        if ch != "-":
            n += 1
            if n == pos:
                return i
    raise ValueError(pos)


def pos_at(name: str, col: int):
    if aln[name][col] == "-":
        return None
    return len(aln[name][: col + 1].replace("-", ""))


for label, p in SITES.items():
    c = col_of(ANCHOR, p)
    print(f"\n## {label} (ALDH2 {seqs[ANCHOR][p-1]}{p}), alignment column {c+1}\n")
    print("| sequence | accession | residue | position | window (+/-5 columns) |")
    print("|---|---|---|---|---|")
    for k in SEQS:
        q = pos_at(k, c)
        res = aln[k][c]
        print(f"| {k} | {SEQS[k]} | {res if res != '-' else 'gap'} | {q if q else '-'} | {aln[k][c-5:c+6]} |")
