"""Compare the C-terminal membrane-anchoring segment of F4JLB7 with characterised
PTHR48004 relatives, and scan each sequence for a CRIB motif.

Usage: uv run --no-project python c_terminus_and_crib_scan.py

Sequences are fetched live from UniProt REST (FASTA). Stdlib only.
"""

import re
import urllib.request

ACCESSIONS = {
    "F4JLB7": "AT4G28560 (benchmark target)",
    "Q9SSD1": "TMM / RLP17 (PTHR48004:SF42)",
    "Q9SJH6": "RLP29 (PTHR48004:SF42)",
    "Q5PP26": "PII-2 (PTHR48004:SF55)",
    "O80809": "CLV2 / RLP10 (PTHR48004:SF9)",
    "Q1G3K8": "RIC7 CRIB protein, AT4G28556 (not PTHR48004; control)",
}

KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}

# Loose CRIB patterns. CRIB_ANIMAL is the Cdc42/Rac effector consensus
# (I-S-x-P-x(2,4)-F-x-H-x(2)-H-V-G); CRIB_PLANT matches the plant RIC form
# (I-x(2)-P-x(3,5)-H-V-x-H-x-G), validated on the positive control Q1G3K8
# (UniProt CRIB domain 36..49, IGNPTDVKHVAHIG).
CRIB_ANIMAL = re.compile(r"[ILV]S.P.{2,4}F.H.{2}H[VI]G")
CRIB_PLANT = re.compile(r"[ILV].{2}P.{3,5}H[VI].H.G")


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def last_hydrophobic_segment(seq: str, window: int = 19, cutoff: float = 1.6):
    """Return (start, end, mean KD) of the most C-terminal window above cutoff (1-based)."""
    best = None
    for i in range(len(seq) - window + 1):
        score = sum(KD[a] for a in seq[i : i + window]) / window
        if score >= cutoff:
            best = (i + 1, i + window, round(score, 2))
    return best


def main() -> None:
    print("accession\tlabel\tlength\tlast_hydrophobic_window\tresidues_after_window\ttail\tbasic_in_tail\tCRIB_match")
    for acc, label in ACCESSIONS.items():
        seq = fetch(acc)
        seg = last_hydrophobic_segment(seq)
        if seg is None:
            after, tail, basic = "NA", "", "NA"
        else:
            after = len(seq) - seg[1]
            tail = seq[seg[1] :]
            basic = sum(tail.count(a) for a in "KR")
        hits = [m for pat in (CRIB_ANIMAL, CRIB_PLANT) for m in pat.finditer(seq)]
        crib_str = ",".join(f"{m.start() + 1}:{m.group()}" for m in hits) or "none"
        print(f"{acc}\t{label}\t{len(seq)}\t{seg}\t{after}\t{tail}\t{basic}\t{crib_str}")


if __name__ == "__main__":
    main()
