# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Check PANTHER subfamily placement and active-site conservation for S. cerevisiae Ubc9.

Queries the PANTHER geneinfo service for subfamily assignments of yeast Ubc9 (P50623),
fission yeast Hus5 (P40984), Neurospora NCU04302 (Q1K772) and human UBE2I (P63279),
fetches their sequences from UniProt, globally aligns each to P50623 and reports
identity and the residue aligned to the yeast catalytic cysteine (Cys93).

Run: uv run --script subfamily_and_active_site.py
"""

import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "P50623"
PROTEINS = {
    "P50623": ("559292", "S. cerevisiae UBC9"),
    "P40984": ("284812", "S. pombe hus5"),
    "Q1K772": ("367110", "N. crassa NCU04302"),
    "P63279": ("9606", "H. sapiens UBE2I"),
}
YEAST_ACTIVE_SITE = 93  # UniProt ACT_SITE, glycyl thioester intermediate


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode()


def panther_subfamily(acc: str, taxon: str) -> tuple[str, str]:
    url = (
        "https://pantherdb.org/services/oai/pantherdb/geneinfo?"
        f"geneInputList={acc}&organism={taxon}"
    )
    gene = json.loads(get(url))["search"]["mapped_genes"]["gene"]
    return gene.get("sf_id", "NA"), gene.get("sf_name", "NA")


def sequence(acc: str) -> str:
    fasta = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(fasta.splitlines()[1:])


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    seqs = {acc: sequence(acc) for acc in PROTEINS}
    q = seqs[QUERY]
    print(f"P50623 residue {YEAST_ACTIVE_SITE}: {q[YEAST_ACTIVE_SITE - 1]}")
    print("accession\tprotein\tPANTHER_subfamily\tsubfamily_name\tlength\tidentity_to_P50623\tresidue_at_yeast_C93")
    for acc, (taxon, name) in PROTEINS.items():
        sf, sfname = panther_subfamily(acc, taxon)
        s = seqs[acc]
        aln = aligner.align(q, s)[0]
        ident = aligned = 0
        mapped = "-"
        qi = si = 0
        for a, b in zip(aln[0], aln[1]):
            if a != "-":
                qi += 1
            if b != "-":
                si += 1
            if a != "-" and b != "-":
                aligned += 1
                ident += a == b
            if a != "-" and qi == YEAST_ACTIVE_SITE:
                mapped = f"{b}{si}" if b != "-" else "gap"
        print(f"{acc}\t{name}\t{sf}\t{sfname}\t{len(s)}\t{ident}/{aligned} ({100*ident/aligned:.1f}%)\t{mapped}")


if __name__ == "__main__":
    main()
