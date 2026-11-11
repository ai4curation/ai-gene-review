"""Re-review: place the donkey A0A9L0JBN5 gene model relative to human MITF isoforms.

Reads the cached donkey and human UniProt flat files, reports where the human
isoform-A start sits in the donkey model, which human isoform-specific segments
are present, and (optionally, with --uniprot) lists all donkey MITF TrEMBL
entries and their Ensembl gene/transcript ids from the UniProt REST API.

Run: python3 genes/EQUAS/MITF/MITF-bioinformatics/gene_model_rereview.py [--uniprot]
"""

import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent


def read_seq(path: Path) -> str:
    text = path.read_text()
    block = text.split("\nSQ   ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", block)


def main() -> None:
    donkey = read_seq(HERE.parent / "MITF-uniprot.txt")
    human = read_seq(HERE / "human-O75030-uniprot.txt")
    print(f"donkey A0A9L0JBN5 length: {len(donkey)}")
    print(f"human O75030-1 (isoform A1) length: {len(human)}")
    a_start = human[:20]
    pos = donkey.find(a_start)
    print(f"human isoform A1 residues 1-20 ({a_start}) found in donkey at 1-based position: {pos + 1 if pos >= 0 else 'absent'}")
    ext = donkey[:pos] if pos > 0 else ""
    if ext:
        comp = {aa: ext.count(aa) for aa in "RPGS"}
        frac = sum(comp.values()) / len(ext)
        print(f"N-terminal extension length: {len(ext)}; R+P+G+S fraction: {frac:.2f}; Met count: {ext.count('M')}")
    segments = {
        "human 138-162 (A1 numbering)": human[137:162],
        "human 293-298 (A1 numbering; X1-type 6-residue insert region)": human[292:298],
    }
    for name, seg in segments.items():
        print(f"{name} {seg}: present in donkey = {seg in donkey}")
    print(f"ACIFPT (X1-type insert) present in donkey: {'ACIFPT' in donkey}")
    if "--uniprot" in sys.argv:
        url = (
            "https://rest.uniprot.org/uniprotkb/search?query=gene_exact:MITF+AND+organism_id:9793"
            "&fields=accession,length,reviewed,xref_ensembl&format=tsv"
        )
        with urllib.request.urlopen(url) as resp:
            print("\nUniProt donkey MITF entries:")
            print(resp.read().decode())


if __name__ == "__main__":
    main()
