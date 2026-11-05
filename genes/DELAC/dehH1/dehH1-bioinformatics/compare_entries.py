#!/usr/bin/env python3
"""Compare UniProtKB Q7DI61 (TrEMBL, Delftia acidovorans dehH1) with Q01398
(Swiss-Prot, Moraxella sp. strain B dehH1), and report simple sequence-derived
features relevant to the GO review (catalytic residues, hydrophobic stretches).

Reproducible: fetches both records live from the UniProt REST API.
No result is hardcoded; the script prints whatever it finds.
"""

import re
import sys
import urllib.request

ACCESSIONS = ("Q7DI61", "Q01398")
URL = "https://rest.uniprot.org/uniprotkb/{}.txt"


def fetch(acc: str) -> str:
    with urllib.request.urlopen(URL.format(acc), timeout=60) as fh:
        return fh.read().decode()


def sequence(flat: str) -> str:
    body = flat.split("\nSQ   ", 1)[1].split("\n", 1)[1]
    return re.sub(r"[^A-Z]", "", body.split("//")[0])


def crc64(flat: str) -> str:
    m = re.search(r"^SQ   SEQUENCE.*?(\w{16}) CRC64;", flat, re.M)
    return m.group(1) if m else "?"


def taxid(flat: str) -> str:
    m = re.search(r"^OX   NCBI_TaxID=(\d+)", flat, re.M)
    return m.group(1) if m else "?"


# Kyte-Doolittle hydropathy, used only as a crude screen for a candidate
# membrane-spanning segment (>=19 residues averaging >1.6).
KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}


def tm_candidates(seq: str, window: int = 19, cutoff: float = 1.6):
    hits = []
    for i in range(len(seq) - window + 1):
        avg = sum(KD[a] for a in seq[i:i + window]) / window
        if avg > cutoff:
            hits.append((i + 1, i + window, round(avg, 2)))
    return hits


def main() -> int:
    records = {}
    for acc in ACCESSIONS:
        try:
            records[acc] = fetch(acc)
        except Exception as exc:  # network / API failure
            print(f"ERROR: could not fetch {acc}: {exc}", file=sys.stderr)
            return 1

    seqs = {a: sequence(f) for a, f in records.items()}
    for acc in ACCESSIONS:
        f = records[acc]
        print(f"{acc}: length={len(seqs[acc])} crc64={crc64(f)} taxid={taxid(f)}")

    a, b = ACCESSIONS
    print(f"\nsequences identical: {seqs[a] == seqs[b]}")
    if seqs[a] != seqs[b] and len(seqs[a]) == len(seqs[b]):
        diffs = [i + 1 for i, (x, y) in enumerate(zip(seqs[a], seqs[b])) if x != y]
        print(f"differing positions: {diffs}")

    seq = seqs[a]
    print("\nnucleophile-elbow / catalytic residues reported for this enzyme")
    for pos in (105, 272):
        print(f"  position {pos}: {seq[pos - 1]} (context {seq[pos - 6:pos + 5]})")

    print("\nKyte-Doolittle candidate transmembrane segments "
          f"(window 19, mean > 1.6): {tm_candidates(seq) or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
