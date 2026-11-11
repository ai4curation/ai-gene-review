"""Re-review comparison of D3VIU4 with characterised family-3 cystine-binding proteins.

Fetches sequences from UniProt REST, aligns with MAFFT (L-INS-i), prints the
pairwise identity matrix (identical / mutually ungapped columns) and the
D3VIU4 residues aligned to the Ngo0372 (Q5F9M1) binding-pocket residues
Tyr58 and Trp96 (UniProt SV2 numbering; Tyr59/Trp97 in PMID:22138345).

Run: python3 compare_sequences_rereview.py   (requires curl-free stdlib + mafft on PATH)
"""
import subprocess
import urllib.request

ACCS = ["D3VIU4", "D3VIU8", "P42199", "P42400", "Q5F9M1", "P45024",
        "P0AEM9", "O34406", "P39906"]
POCKET = {"Q5F9M1": [58, 96]}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    return urllib.request.urlopen(url).read().decode()


def parse(text: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    key = None
    for line in text.splitlines():
        if line.startswith(">"):
            key = line.split("|")[1]
            seqs[key] = ""
        elif key:
            seqs[key] += line.strip()
    return seqs


def column(aln: str, pos: int) -> int:
    n = 0
    for j, c in enumerate(aln):
        if c != "-":
            n += 1
            if n == pos:
                return j
    raise ValueError(pos)


def main() -> None:
    fasta = "".join(fetch(a) for a in ACCS)
    with open("rereview_seqs.fa", "w") as fh:
        fh.write(fasta)
    out = subprocess.run(["mafft", "--quiet", "--localpair", "--maxiterate", "1000",
                          "rereview_seqs.fa"], capture_output=True, text=True, check=True).stdout
    with open("rereview_aln.fa", "w") as fh:
        fh.write(out)
    aln = parse(out)
    ids = list(aln)
    print("pairwise % identity")
    print("\t" + "\t".join(ids))
    for a in ids:
        row = []
        for b in ids:
            m = sum(1 for x, y in zip(aln[a], aln[b]) if x == y and x != "-")
            n = sum(1 for x, y in zip(aln[a], aln[b]) if x != "-" and y != "-")
            row.append(f"{100 * m / n:.0f}")
        print(a + "\t" + "\t".join(row))
    print("\nNgo0372 pocket residues and aligned residues")
    for ref, positions in POCKET.items():
        for p in positions:
            j = column(aln[ref], p)
            cells = []
            for a in ids:
                pos = len(aln[a][:j + 1].replace("-", ""))
                cells.append(f"{a}:{aln[a][j]}{pos}")
            print(f"{ref} {p}: " + " ".join(cells))


if __name__ == "__main__":
    main()
