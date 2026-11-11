# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare PP_0661 (Q88Q37) with characterized LysR-type regulators and list its
genomic neighbours in P. putida KT2440.

Run: uv run compare_lysr.py > compare_lysr_output.txt

Fetches sequences from UniProt and gene neighbourhoods and KO memberships from
KEGG REST at run time; nothing is hard-coded except the accessions, KO ids and
locus tags queried.
"""

import io

import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

QUERY = "Q88Q37"
# Swiss-Prot reference LysR-type regulators
REFERENCES = {
    "P24734": "AmpR, P. aeruginosa PAO1 (beta-lactamase regulator)",
    "P0A9F6": "GcvA, E. coli K-12 (glycine cleavage activator)",
    "P0A9F9": "MetR, E. coli K-12 (methionine biosynthesis activator)",
}
NEIGHBOURS = [f"PP_{i:04d}" for i in range(656, 666)]
AMPC_CANDIDATE_NEIGHBOURS = ["PP_2875", "PP_2876", "PP_2877"]
GCV_KOS = {
    "K00605": "gcvT aminomethyltransferase",
    "K02437": "gcvH glycine cleavage system H protein",
    "K00281": "gcvP glycine dehydrogenase",
}


def kegg_ko_genes(ko: str) -> list[str]:
    """Return KT2440 (ppu) locus tags linked to a KEGG orthology id."""
    r = requests.get(f"https://rest.kegg.jp/link/ppu/ko:{ko}", timeout=60)
    r.raise_for_status()
    return [
        line.split("\t")[1].removeprefix("ppu:")
        for line in r.text.strip().splitlines()
        if "\t" in line
    ]


def fetch_seq(acc: str):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return next(SeqIO.parse(io.StringIO(r.text), "fasta"))


def kegg_summary(locus: str) -> str:
    r = requests.get(f"https://rest.kegg.jp/get/ppu:{locus}", timeout=60)
    r.raise_for_status()
    keep = [
        line.strip()
        for line in r.text.splitlines()
        if line.startswith(("NAME", "ORTHOLOGY", "POSITION"))
    ]
    return " | ".join(keep)


def main() -> None:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "local"

    q = fetch_seq(QUERY)
    print(f"# Pairwise local alignment (BLOSUM62, gap -11/-1) of {QUERY} ({len(q.seq)} aa)")
    for acc, desc in REFERENCES.items():
        ref = fetch_seq(acc)
        aln = aligner.align(q.seq, ref.seq)[0]
        cols = [(x, y) for x, y in zip(aln[0], aln[1]) if x != "-" and y != "-"]
        ident = sum(x == y for x, y in cols)
        print(
            f"{acc}\t{desc}\tlen={len(ref.seq)}\tscore={aln.score:.0f}\t"
            f"aligned_pairs={len(cols)}\tidentity={100 * ident / len(cols):.1f}%"
        )

    print("\n# KEGG genomic neighbourhood of PP_0661 (ppu)")
    for locus in NEIGHBOURS:
        print(f"{locus}\t{kegg_summary(locus)}")

    print("\n# Neighbourhood of the KT2440 class C beta-lactamase gene (K01467)")
    print(f"K01467 genes in ppu: {kegg_ko_genes('K01467')}")
    for locus in AMPC_CANDIDATE_NEIGHBOURS:
        print(f"{locus}\t{kegg_summary(locus)}")

    print("\n# All KT2440 genes in KEGG KO K03566 (GcvA-like LysR regulator)")
    for locus in kegg_ko_genes("K03566"):
        print(f"{locus}\t{kegg_summary(locus)}")

    print("\n# KT2440 glycine cleavage system genes (GcvA targets in E. coli)")
    for ko, name in GCV_KOS.items():
        print(f"{ko} ({name}): {kegg_ko_genes(ko)}")


if __name__ == "__main__":
    main()
