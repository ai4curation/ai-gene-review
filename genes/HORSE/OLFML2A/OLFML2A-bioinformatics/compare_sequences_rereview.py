# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython", "httpx"]
# ///
"""Re-review comparison of horse OLFML2A gene products against human Q68BL7.

Fetches the benchmark horse model (A0A9L0SKW1), the other horse TrEMBL model
from the same Ensembl gene (A0A3Q2LAT7), all horse RefSeq OLFML2A isoforms,
human Q68BL7 and mouse Q8BHP7, then reports for each horse product: length,
N-terminal sequence, global-alignment identity to human, human positions left
unpaired (gaps), and the maximum Kyte-Doolittle hydropathy of any 11-residue
window within the first 40 residues (a crude signal-peptide h-region proxy;
NOT a SignalP prediction).

Run: uv run compare_sequences_rereview.py > RESULTS-rereview.json
"""

import json
import sys

import httpx
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = ["A0A9L0SKW1", "A0A3Q2LAT7", "Q68BL7", "Q8BHP7"]
REFSEQ_QUERY = 'OLFML2A[gene] AND "Equus caballus"[Organism] AND refseq[filter]'

KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}


def parse_fasta(text: str) -> dict[str, str]:
    seqs: dict[str, str] = {}
    name = None
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].strip()
            seqs[name] = ""
        elif name:
            seqs[name] += line.strip()
    return seqs


def fetch_uniprot(acc: str) -> str:
    r = httpx.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return next(iter(parse_fasta(r.text).values()))


def fetch_refseq() -> dict[str, str]:
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    r = httpx.get(f"{base}/esearch.fcgi", params={"db": "protein", "term": REFSEQ_QUERY,
                                                   "retmode": "json", "retmax": 50}, timeout=60)
    r.raise_for_status()
    ids = r.json()["esearchresult"]["idlist"]
    r = httpx.get(f"{base}/efetch.fcgi", params={"db": "protein", "id": ",".join(ids),
                                                  "rettype": "fasta", "retmode": "text"}, timeout=60)
    r.raise_for_status()
    return {k.split()[0]: v for k, v in parse_fasta(r.text).items()}


def max_hydropathy(seq: str, window: int = 11, region: int = 40) -> float:
    head = seq[:region]
    return round(max(sum(KD[a] for a in head[i:i + window]) / window
                     for i in range(len(head) - window + 1)), 2)


def compare(horse: str, human: str) -> dict:
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(horse, human)[0]
    paired = ident = 0
    human_paired = set()
    for (hs, he), (us, ue) in zip(*aln.aligned):
        for i, j in zip(range(hs, he), range(us, ue)):
            paired += 1
            ident += horse[i] == human[j]
            human_paired.add(j + 1)
    gaps, start = [], None
    for pos in range(1, len(human) + 2):
        if pos <= len(human) and pos not in human_paired:
            start = start or pos
        elif start:
            gaps.append([start, pos - 1])
            start = None
    return {"paired": paired, "identity_pct": round(100 * ident / paired, 1),
            "human_positions_unpaired": gaps}


def main() -> None:
    up = {a: fetch_uniprot(a) for a in UNIPROT}
    human = up["Q68BL7"]
    products = {"UniProtKB:A0A9L0SKW1": up["A0A9L0SKW1"], "UniProtKB:A0A3Q2LAT7": up["A0A3Q2LAT7"]}
    products |= {f"RefSeq:{k}": v for k, v in fetch_refseq().items()}
    products["UniProtKB:Q8BHP7 (mouse)"] = up["Q8BHP7"]
    out = {"human_reference": {"id": "UniProtKB:Q68BL7", "length": len(human),
                               "nterm40": human[:40], "max_kd_first40": max_hydropathy(human)}}
    for name, seq in products.items():
        out[name] = {"length": len(seq), "nterm40": seq[:40],
                     "max_kd_first40": max_hydropathy(seq), **compare(seq, human)}
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
