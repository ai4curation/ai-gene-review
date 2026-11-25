# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Check conservation of the CDF transmembrane zinc-binding site A in Msc2.

Fetches sequences from UniProt, aligns them with MAFFT (must be on PATH), and
reports the residues aligned to E. coli YiiP (P69380) site-A ligands D45, D49,
H153, D157 (UniProt BINDING features, PubMed:19749753).
"""
import subprocess
import sys
from pathlib import Path

import requests

HERE = Path(__file__).parent
PROTEINS = {
    "P69380": "YiiP_ECOLI (structural reference)",
    "Q03455": "Msc2_YEAST (target)",
    "Q9HGQ3": "Cis4_SCHPO (PTHR45755:SF4 relative)",
    "Q8TAD4": "ZnT5_HUMAN (SLC30A5)",
    "P53735": "Zrg17_YEAST (partner)",
    "Q6NXT4": "ZnT6_HUMAN (SLC30A6, partner)",
    "P20107": "Zrc1_YEAST (vacuolar CDF control)",
}
REF = "P69380"
REF_SITES = [45, 49, 153, 157]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def read_fasta(text: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    name = None
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = ""
        elif name:
            seqs[name] += line.strip()
    return seqs


def main() -> None:
    fasta = "".join(f">{a}\n{fetch(a)}\n" for a in PROTEINS)
    (HERE / "cdf_sequences.fasta").write_text(fasta)
    out = subprocess.run(
        ["mafft", "--quiet", "--localpair", "--maxiterate", "1000", str(HERE / "cdf_sequences.fasta")],
        capture_output=True, text=True, check=True,
    ).stdout
    (HERE / "cdf_alignment.fasta").write_text(out)
    aln = read_fasta(out)
    ref = aln[REF]
    cols = []
    pos = 0
    for i, c in enumerate(ref):
        if c != "-":
            pos += 1
            if pos in REF_SITES:
                cols.append(i)
    print("accession\tdescription\t" + "\t".join(f"YiiP_{p}" for p in REF_SITES))
    for acc, desc in PROTEINS.items():
        s = aln[acc]
        row = []
        for col in cols:
            res = s[col]
            if res == "-":
                row.append("-")
            else:
                n = len(s[: col + 1].replace("-", ""))
                row.append(f"{res}{n}")
        print(f"{acc}\t{desc}\t" + "\t".join(row))


if __name__ == "__main__":
    sys.exit(main())
