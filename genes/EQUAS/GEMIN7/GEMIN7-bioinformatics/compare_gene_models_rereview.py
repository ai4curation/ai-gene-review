# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Compare the donkey GEMIN7 UniProt gene-model products with each other and with horse/human.

Usage: uv run --script compare_gene_models_rereview.py <out_dir>

For each accession, fetches the UniProt flat file from UniProt REST, records its Ensembl
gene/transcript cross-references and sequence, and reports whether one sequence is an exact
suffix (N-terminal extension) of another. All outputs are computed; nothing is hard-coded
except the accession list.
"""
import sys
import urllib.request
import pathlib

ACCESSIONS = {
    "A0A9L0ICL9": "donkey (benchmark)",
    "A0A9L0IFN2": "donkey",
    "A0A9L0J5X5": "donkey",
    "A0A9L0T0I7": "horse",
    "Q9H840": "human (Swiss-Prot)",
}


def fetch_flat(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    return urllib.request.urlopen(url).read().decode()


def parse(flat: str) -> tuple[list[str], str]:
    ensembl, seq, inseq = [], [], False
    for line in flat.splitlines():
        if line.startswith("DR   Ensembl;"):
            ensembl.append(line[5:].strip())
        if line.startswith("SQ"):
            inseq = True
            continue
        if line.startswith("//"):
            break
        if inseq:
            seq.append("".join(line.split()))
    return ensembl, "".join(seq)


def main(out_dir: str) -> None:
    out = pathlib.Path(out_dir)
    seqs = {}
    for acc, label in ACCESSIONS.items():
        flat = fetch_flat(acc)
        (out / f"rereview-{acc}.txt").write_text(flat)
        ensembl, seq = parse(flat)
        seqs[acc] = seq
        print(f"## {acc} [{label}] length {len(seq)}")
        for e in ensembl:
            print(f"  Ensembl: {e}")
    print()
    print("## suffix relationships (shorter sequence == C-terminal end of longer one)")
    for a, sa in seqs.items():
        for b, sb in seqs.items():
            if a != b and len(sb) < len(sa) and sa.endswith(sb):
                print(f"  {b} ({len(sb)} aa) == {a} residues {len(sa) - len(sb) + 1}-{len(sa)}; "
                      f"extension {len(sa) - len(sb)} aa")
    print()
    print("## pairwise identity over equal-length, ungapped comparisons")
    accs = list(seqs)
    for i, a in enumerate(accs):
        for b in accs[i + 1:]:
            sa, sb = seqs[a], seqs[b]
            if len(sa) == len(sb):
                ident = sum(x == y for x, y in zip(sa, sb))
                print(f"  {a} vs {b}: {ident}/{len(sa)} identical ({100 * ident / len(sa):.2f}%)")


if __name__ == "__main__":
    main(sys.argv[1])
