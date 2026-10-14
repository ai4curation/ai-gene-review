"""Map the magi3a / magi3b in situ probe primers of America et al. 2022
(PMID:35649360) onto the two zebrafish MAGI3 genes, to establish which ZFIN
gene each of that paper's names refers to.

The paper's names follow NCBI RefSeq ("magi3a", "magi3b"); ZFIN currently
lists the two genes as wu:fi36a10 (ZDB-GENE-030131-6139, Ensembl
ENSDARG00000101869) and magi3b (ZDB-GENE-060503-301, ENSDARG00000025974,
NCBI LOC564220). For each primer the script reports the best match
(fewest mismatches, either strand) in every Ensembl cDNA of each gene.
The T7 promoter tail (TAATACGACTCACTATAGGG) of the reverse primers is
removed before matching.

Primer sequences are copied from the Methods of PMID:35649360.

Run from the repository root:
    uv run python genes/DANRE/wu_fi36a10/wu_fi36a10-bioinformatics/primer_map.py
"""

import json
import urllib.request

T7 = "TAATACGACTCACTATAGGG"
PRIMERS = {
    "magi3a-fwd": "CCTGCCAGCCGAGAAGACAGG",
    "magi3a-rev": "TAATACGACTCACTATAGGGCTTTCCAGGGACCTGGAGTTATGG",
    "magi3b-fwd": "CGCTCAAGAGGAAGAAACACTGG",
    "magi3b-rev": "TAATACGACTCACTATAGGGTCCAACAGTAATCCACTCTCCTCC",
}
GENES = {
    "wu:fi36a10 (ENSDARG00000101869)": "ENSDARG00000101869",
    "magi3b / LOC564220 (ENSDARG00000025974)": "ENSDARG00000025974",
}


def revcomp(s: str) -> str:
    return s.translate(str.maketrans("ACGT", "TGCA"))[::-1]


def cdnas(gene: str) -> list[str]:
    url = (f"https://rest.ensembl.org/sequence/id/{gene}?type=cdna;multiple_sequences=1;"
           "content-type=application/json")
    return [d["seq"].upper() for d in json.loads(urllib.request.urlopen(url, timeout=60).read())]


def best(seqs: list[str], primer: str) -> int:
    n = len(primer)
    top = n
    for s in seqs:
        for probe in (primer, revcomp(primer)):
            for i in range(len(s) - n + 1):
                mm = sum(1 for a, b in zip(s[i : i + n], probe) if a != b)
                if mm < top:
                    top = mm
                    if mm == 0:
                        return 0
    return top


def main() -> None:
    seqs = {g: cdnas(e) for g, e in GENES.items()}
    print("| primer | gene-specific part (nt) | " + " | ".join(f"mismatches in {g}" for g in GENES) + " |")
    print("|---|---|" + "---|" * len(GENES))
    for name, p in PRIMERS.items():
        core = p[len(T7):] if p.startswith(T7) else p
        cells = [str(best(seqs[g], core)) for g in GENES]
        print(f"| {name} | {len(core)} | " + " | ".join(cells) + " |")
    print()
    for g, s in seqs.items():
        print(f"- {g}: {len(s)} Ensembl cDNA sequence(s) searched")


if __name__ == "__main__":
    main()
