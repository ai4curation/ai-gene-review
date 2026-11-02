"""Re-review analysis for Drosophila Gpdh3 (benchmark accession E1JIT1).

1. Fetches the three Gpdh3 polypeptides (E1JIT1 = Gpdh3-PB, Q8IN06 = Gpdh3-PA,
   Q9VD20 = Gpdh3-PC), the paralog Gpdh1 (P13706) and human GPD1 (P21695)
   from the UniProt REST API.
2. Reports where the Gpdh3 isoforms differ from one another.
3. Aligns the first 400 residues of each with MAFFT and reports the residues
   at the human GPD1 positions UniProt annotates as active site / NAD /
   substrate binding (P21695 FT lines).

Requires `mafft` on PATH. Usage: python compare_isoforms_rereview.py
"""

import difflib
import subprocess
import tempfile
import urllib.request

ACCS = {
    "E1JIT1": "Gpdh3-PB",
    "Q8IN06": "Gpdh3-PA",
    "Q9VD20": "Gpdh3-PC",
    "P13706": "Gpdh1",
    "P21695": "human GPD1",
}

# Human GPD1 (P21695) positions from its UniProt FT ACT_SITE/BINDING lines.
GPD1_SITES = {
    10: "NAD", 11: "NAD", 12: "NAD", 13: "NAD", 14: "NAD", 15: "NAD",
    41: "NAD", 97: "NAD", 120: "substrate", 153: "NAD",
    204: "active site (proton acceptor)", 269: "substrate+NAD",
    270: "substrate", 296: "NAD", 298: "NAD",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    return "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))


def main() -> None:
    seqs = {acc: fetch(acc) for acc in ACCS}
    for acc, label in ACCS.items():
        print(f"{acc}\t{label}\tlength={len(seqs[acc])}")

    print("\n## Differences of other Gpdh3 isoforms relative to E1JIT1 (0-based slices)")
    for other in ("Q8IN06", "Q9VD20"):
        sm = difflib.SequenceMatcher(None, seqs["E1JIT1"], seqs[other], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal":
                print(
                    f"{other}: {op} E1JIT1[{i1}:{i2}]={seqs['E1JIT1'][i1:i2]!r} "
                    f"-> {other}[{j1}:{j2}]={seqs[other][j1:j2]!r}"
                )

    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for acc in ACCS:
            fh.write(f">{acc}\n{seqs[acc][:400]}\n")
        path = fh.name
    aln_text = subprocess.run(
        ["mafft", "--quiet", "--localpair", "--maxiterate", "1000", path],
        capture_output=True, text=True, check=True,
    ).stdout
    aln: dict[str, str] = {}
    cur = None
    for line in aln_text.splitlines():
        if line.startswith(">"):
            cur = line[1:].strip()
            aln[cur] = ""
        elif cur:
            aln[cur] += line.strip().upper()

    # map human GPD1 residue numbers to alignment columns
    col_of: dict[int, int] = {}
    pos = 0
    for col, ch in enumerate(aln["P21695"]):
        if ch != "-":
            pos += 1
            col_of[pos] = col

    def resnum(acc: str, col: int) -> str:
        s = aln[acc]
        if s[col] == "-":
            return "-"
        return f"{s[col]}{len(s[: col + 1].replace('-', ''))}"

    print("\n## Residues at human GPD1 functional positions")
    print("GPD1_pos\trole\t" + "\t".join(ACCS))
    for p, role in GPD1_SITES.items():
        col = col_of[p]
        print(f"{p}\t{role}\t" + "\t".join(resnum(a, col) for a in ACCS))

    ident = sum(
        1 for x, y in zip(aln["E1JIT1"], aln["P13706"]) if x == y and x != "-"
    )
    print(f"\nIdentical aligned residues E1JIT1 vs P13706 (first 400 aa): {ident}")


if __name__ == "__main__":
    main()
