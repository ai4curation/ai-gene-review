"""Check whether the brorin (vwc2) splice morpholinos of Miyake et al. 2017
(PMID:28448525) could also target the paralog si:dkey-283b1.7 or vwc2l.

A morpholino binds the sense (pre-mRNA) strand, so its target site is the
reverse complement of the morpholino sequence. For each gene, the script
scans the full genomic sequence of the gene (sense strand, Ensembl REST
/sequence, type=genomic) and reports the best-matching 25-mer (fewest
mismatches) for each morpholino. Zero mismatches identifies the intended
target; four or more mismatches in a 25-mer is generally taken to abolish
morpholino activity.

Morpholino sequences are copied from the Methods of PMID:28448525:
  brorin MO1 5'-ATGGAGACACCTAGAAGAACAAACC-3'
  brorin MO2 5'-CACTTAATGTGCTGCTCTAACCTTA-3'

Run from the repository root:
    uv run python genes/DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/morpholino_check.py
"""

import json
import urllib.request

MOS = {
    "brorin MO1": "ATGGAGACACCTAGAAGAACAAACC",
    "brorin MO2": "CACTTAATGTGCTGCTCTAACCTTA",
}
GENES = {
    "vwc2 (ENSDARG00000076495)": "ENSDARG00000076495",
    "si:dkey-283b1.7 (ENSDARG00000053460)": "ENSDARG00000053460",
    "vwc2l (ENSDARG00000069134)": "ENSDARG00000069134",
}


def revcomp(s: str) -> str:
    return s.translate(str.maketrans("ACGTacgt", "TGCAtgca"))[::-1]


def genomic(gene: str) -> str:
    url = f"https://rest.ensembl.org/sequence/id/{gene}?type=genomic;content-type=application/json"
    return json.loads(urllib.request.urlopen(url, timeout=60).read())["seq"].upper()


def best_match(seq: str, target: str) -> tuple[int, int]:
    n = len(target)
    best = (n + 1, -1)
    for i in range(len(seq) - n + 1):
        mm = sum(1 for a, b in zip(seq[i : i + n], target) if a != b)
        if mm < best[0]:
            best = (mm, i)
            if mm == 0:
                break
    return best


def main() -> None:
    seqs = {k: genomic(v) for k, v in GENES.items()}
    print("| morpholino | gene | gene length (bp) | best-match mismatches (of 25) | position in gene |")
    print("|---|---|---|---|---|")
    for mo, s in MOS.items():
        target = revcomp(s)
        for g, seq in seqs.items():
            mm, pos = best_match(seq, target)
            print(f"| {mo} | {g} | {len(seq)} | {mm} | {pos + 1} |")


if __name__ == "__main__":
    main()
