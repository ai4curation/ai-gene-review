"""Compare Cys-loop channel hallmark motifs of NtR (Q9W288) with characterised nAChR subunits.

Fetches sequences from UniProt REST, aligns with MAFFT (must be on PATH), and prints the
aligned regions around (i) the Cys-loop disulfide, (ii) the loop-C vicinal cysteine pair
that defines nAChR alpha subunits, and (iii) the M2 pore-lining segment of each reference.
Coordinates are reported in each protein's own UniProt numbering.

Run: python compare_motifs_rereview.py
"""
import subprocess
import tempfile
import urllib.request

ACCS = {
    "Q9W288": "Dmel NtR (target)",
    "P17644": "Dmel nAChRalpha2 (same PANTHER SF430)",
    "P04755": "Dmel nAChRbeta1",
    "P36544": "Human CHRNA7",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    lines = urllib.request.urlopen(url).read().decode().splitlines()
    return "".join(lines[1:])


def align(seqs: dict[str, str]) -> dict[str, str]:
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for k, s in seqs.items():
            fh.write(f">{k}\n{s}\n")
        path = fh.name
    out = subprocess.run(["mafft", "--quiet", "--localpair", "--maxiterate", "1000", path],
                         capture_output=True, text=True, check=True).stdout
    aln: dict[str, str] = {}
    cur = None
    for line in out.splitlines():
        if line.startswith(">"):
            cur = line[1:].strip()
            aln[cur] = ""
        else:
            aln[cur] += line.strip().upper()
    return aln


def col_to_pos(aligned: str, col: int) -> int:
    return len(aligned[: col + 1].replace("-", ""))


def pos_to_col(aligned: str, pos: int) -> int:
    n = 0
    for i, c in enumerate(aligned):
        if c != "-":
            n += 1
            if n == pos:
                return i
    raise ValueError(pos)


def show(aln: dict[str, str], ref: str, start: int, end: int, label: str) -> None:
    a, b = pos_to_col(aln[ref], start), pos_to_col(aln[ref], end)
    print(f"\n## {label} (columns spanning {ref} {start}-{end})")
    for k, s in aln.items():
        seg = s[a : b + 1]
        print(f"{k:8s} {col_to_pos(s, a):>4d} {seg}  {ACCS[k]}")


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    for a, s in seqs.items():
        print(f"{a} length={len(s)} {ACCS[a]}")
    aln = align(seqs)
    # nAChRalpha2 P17644 UniProt features: DISULFID 169..183 (Cys-loop), 243..244 (vicinal loop C),
    # TRANSMEM 293..311 (M2).
    show(aln, "P17644", 160, 190, "Cys-loop disulfide (P17644 C169-C183)")
    show(aln, "P17644", 233, 252, "Loop C vicinal cysteines (P17644 C243-C244)")
    show(aln, "P17644", 286, 316, "M2 pore-lining helix (P17644 TM 293-311)")
    ident = sum(1 for x, y in zip(aln["Q9W288"], aln["P17644"]) if x == y and x != "-")
    print(f"\nIdentical aligned residues Q9W288 vs P17644: {ident}")


if __name__ == "__main__":
    main()
