"""Survey the NAD-binding and catalytic-lysine motifs in long (>=900 aa)
PTHR11728 members from Drosophilidae (the Gpdh3 ortholog group), plus fly
Gpdh1 (P13706), fly Gpdh2 (Q9W1U3) and human GPD1 (P21695) as controls.

Motif windows printed (no alignment; homologous windows are located by the
conserved flanking 'GAG' after the catalytic loop and 'CGV' before the
GPD1 D260 position):
  - NAD-binding glycine loop (human GPD1 residues 10-15, GSGNWG)
  - catalytic-loop window ending in GAG (human GPD1 ... GALKNVVAVGAG, K204)
  - CGV window (human GPD1 CGVAD, D260)

Usage: python survey_orthologs_rereview.py
"""

import re
import urllib.request

QUERY = (
    "https://rest.uniprot.org/uniprotkb/stream?query=(xref:panther-PTHR11728)"
    "+AND+(taxonomy_id:7214)+AND+(length:%5B900+TO+*%5D)&format=fasta"
)
CONTROLS = ["P21695", "P13706", "Q9W1U3"]


def parse(fasta: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    cur = ""
    for line in fasta.splitlines():
        if line.startswith(">"):
            cur = line[1:]
            seqs[cur] = ""
        else:
            seqs[cur] += line.strip()
    return seqs


def get(url: str) -> str:
    return urllib.request.urlopen(url).read().decode()


def main() -> None:
    seqs = parse(get(QUERY))
    for acc in CONTROLS:
        seqs.update(parse(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")))
    print("accession\torganism\tlength\tNAD_loop(6-20)\tcatalytic_window\tCGV_window")
    rows = []
    for header, s in seqs.items():
        acc = header.split("|")[1]
        org_m = re.search(r"OS=(\S+ \S+)", header)
        org = org_m.group(1) if org_m else "?"
        i = s.find("GAG", 150, 300)
        j = s.find("CGV", 230, 330)
        rows.append(
            (
                org,
                acc,
                len(s),
                s[5:20],
                s[i - 14 : i + 4] if i > 0 else "not_found",
                s[j : j + 9] if j > 0 else "not_found",
            )
        )
    for org, acc, n, nad, cat, cgv in sorted(rows):
        print(f"{acc}\t{org}\t{n}\t{nad}\t{cat}\t{cgv}")


if __name__ == "__main__":
    main()
