# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Map the experimentally defined Mg2+-binding residues of Thermus thermophilus
MgtE (UniProtKB Q5SMG8, BINDING features with ECO:0000269 evidence) onto
P. aeruginosa MgtE (Q9I544) by global pairwise alignment.

Usage: uv run mg_site_conservation.py [Q5SMG8.txt Q9I544.txt]
Without arguments, both UniProt flat files are downloaded from rest.uniprot.org.
Prints, for each Tth site, the Tth residue, the aligned Pae residue and whether
it is identical or a conservative acidic/amide substitution.
"""

import re
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def load(acc: str, path: str | None) -> str:
    if path:
        return open(path).read()
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read().decode()


def seq_of(flat: str) -> str:
    s = flat.split("\nSQ   ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", s)


def mg_sites(flat: str) -> list[tuple[int, str]]:
    lines = flat.split("\n")
    out = []
    for i, line in enumerate(lines):
        m = re.match(r"FT   BINDING\s+(\d+)$", line)
        if not m:
            continue
        block = []
        j = i + 1
        while j < len(lines) and lines[j].startswith("FT    "):
            block.append(lines[j][21:].strip())
            j += 1
        b = " ".join(block)
        if "Mg(2+)" in b and "ECO:0000269" in b:
            lab = re.search(r'ligand_label="(\d+)"', b)
            out.append((int(m.group(1)), lab.group(1) if lab else "?"))
    return out


def main() -> None:
    tth = load("Q5SMG8", sys.argv[1] if len(sys.argv) > 2 else None)
    pae = load("Q9I544", sys.argv[2] if len(sys.argv) > 2 else None)
    s_t, s_p = seq_of(tth), seq_of(pae)
    al = Align.PairwiseAligner(mode="global")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    aln = al.align(s_t, s_p)[0]
    # residue index maps
    t2p = {}
    for (ts, te), (ps, pe) in zip(*aln.aligned):
        for k in range(te - ts):
            t2p[ts + k] = ps + k
    ident = sum(s_t[t] == s_p[p] for t, p in t2p.items())
    print(f"Tth MgtE {len(s_t)} aa; Pae MgtE {len(s_p)} aa; aligned pairs {len(t2p)}; "
          f"identity over aligned pairs {ident / len(t2p):.1%}")
    print("\nTth_pos\tsite\tTth_res\tPae_pos\tPae_res\tstatus")
    acidic = set("DENQ")
    for pos, lab in mg_sites(tth):
        tr = s_t[pos - 1]
        p = t2p.get(pos - 1)
        if p is None:
            print(f"{pos}\tMg{lab}\t{tr}\t-\tgap\tNOT_ALIGNED")
            continue
        pr = s_p[p]
        status = "IDENTICAL" if pr == tr else ("CONSERVATIVE" if pr in acidic and tr in acidic else "CHANGED")
        print(f"{pos}\tMg{lab}\t{tr}\t{p + 1}\t{pr}\t{status}")


if __name__ == "__main__":
    main()
