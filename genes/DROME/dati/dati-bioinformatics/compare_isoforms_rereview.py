"""Re-review analysis for dati (Q9V4C9): isoform identity and zinc-finger-array relatives.

Run with:
    uv run --with biopython --with requests python compare_isoforms_rereview.py

1. Fetches all UniProt entries for FlyBase gene FBgn0262636 and aligns each
   to the benchmark accession Q9V4C9, reporting length and indels.
2. Lists the C2H2 finger motifs (C-x2,4-C-x12-H-x3,7-H) in each isoform.
3. Compares the dati zinc-finger array (Q9V4C9 residues 430-700) by local
   alignment to candidate relatives named in the primary literature
   (Squeeze, Rotund, ZNF384) plus the original phmmer donor ZNF208, and
   reports their PANTHER assignments from UniProt.
Results are printed as Markdown; nothing is hard-coded.
"""

import re

import requests
from Bio.Align import PairwiseAligner, substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb"
TARGET = "Q9V4C9"
RELATIVES = ["Q9VDZ3", "Q9VI93", "Q8TF68", "O43345"]
ZF_RE = re.compile(r"C.{2,4}C.{12}H.{3,7}H")


def fetch_tsv(query: str) -> list[dict]:
    r = requests.get(
        f"{UNIPROT}/search",
        params={
            "query": query,
            "fields": "accession,gene_primary,protein_name,length,reviewed,xref_panther,sequence",
            "format": "tsv",
            "size": 50,
        },
        timeout=60,
    )
    r.raise_for_status()
    lines = r.text.strip().split("\n")
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:]]


def aligner(mode: str) -> PairwiseAligner:
    a = PairwiseAligner()
    a.mode = mode
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def identity(aln) -> tuple[int, int]:
    s1, s2 = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    return sum(x == y for x, y in pairs), len(pairs)


def main() -> None:
    isoforms = fetch_tsv("xref:flybase-FBgn0262636")
    target = next(e for e in isoforms if e["Entry"] == TARGET)
    tseq = target["Sequence"]
    print("# dati re-review: isoforms and relatives\n")
    print("## UniProt entries for FBgn0262636\n")
    print("| Entry | Name | Length | Reviewed | PANTHER | Aligned blocks vs Q9V4C9 (target / other) | C2H2 motifs (start) |")
    print("|---|---|---|---|---|---|---|")
    g = aligner("global")
    for e in isoforms:
        aln = g.align(tseq, e["Sequence"])[0]
        blocks = "; ".join(
            f"{t[0] + 1}-{t[1]} / {o[0] + 1}-{o[1]}" for t, o in zip(*aln.aligned)
        )
        zfs = [m.start() + 1 for m in ZF_RE.finditer(e["Sequence"])]
        print(
            f"| {e['Entry']} | {e['Protein names']} | {e['Length']} | {e['Reviewed']} | "
            f"{e['PANTHER']} | {blocks} | {zfs} |"
        )
    print("\n## Zinc-finger array (Q9V4C9 430-700) vs candidate relatives\n")
    print("| Entry | Gene | PANTHER | Local score | Identity in aligned columns |")
    print("|---|---|---|---|---|")
    zf = tseq[429:700]
    loc = aligner("local")
    for acc in RELATIVES:
        e = fetch_tsv(f"accession:{acc}")[0]
        aln = loc.align(zf, e["Sequence"])[0]
        ident, n = identity(aln)
        print(
            f"| {acc} | {e['Gene Names (primary)']} | {e['PANTHER']} | {aln.score:.0f} | "
            f"{ident}/{n} ({100 * ident / n:.0f}%) |"
        )


if __name__ == "__main__":
    main()
