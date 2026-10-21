"""Compare Piliocolobus OLFML2A (A0A8C9H9A8) with human Q68BL7 and mouse Q8BHP7.

Fetches current UniProt sequences and PANTHER cross-references, runs global
pairwise alignments (BLOSUM62, gap open -10, extend -0.5), and reports identity
over aligned (non-gap) columns and the conservation of cysteines in the
olfactomedin domain region of the target (397..655 per PROSITE PS51132).

Run: uv run --with biopython --with requests python compare_orthologs.py
"""

import json
import re

import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "A0A8C9H9A8"
OTHERS = ["Q68BL7", "Q8BHP7", "A0A8C9H4D2"]
OLF_DOMAIN = (397, 655)


def fetch(acc: str) -> dict:
    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).text
    seq = "".join(
        line[5:].replace(" ", "")
        for line in txt.split("\n//")[0].split("\nSQ ", 1)[1].splitlines()[1:]
    )
    panther = re.findall(r"^DR   PANTHER; (PTHR\d+:SF\d+);", txt, re.M)
    signal = re.findall(r"^FT   SIGNAL\s+(\S+)", txt, re.M)
    return {"acc": acc, "seq": seq, "len": len(seq), "panther_sf": panther, "signal": signal}


def align(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aligner.end_gap_score = 0
    return aligner.align(a, b)[0]


def main() -> None:
    target = fetch(TARGET)
    results = {"target": {k: v for k, v in target.items() if k != "seq"}, "comparisons": []}
    results["target"]["cxcxcx9c_motifs"] = [
        [m.start() + 1, m.group()] for m in re.finditer(r"C.C.C.{9}C", target["seq"])
    ]
    for acc in OTHERS:
        other = fetch(acc)
        aln = align(target["seq"], other["seq"])
        ident = aligned = 0
        dom_cys_target = dom_cys_conserved = 0
        for (ts, te), (os_, oe) in zip(*aln.aligned):
            for i, j in zip(range(ts, te), range(os_, oe)):
                aligned += 1
                if target["seq"][i] == other["seq"][j]:
                    ident += 1
                if OLF_DOMAIN[0] - 1 <= i < OLF_DOMAIN[1] and target["seq"][i] == "C":
                    dom_cys_target += 1
                    if other["seq"][j] == "C":
                        dom_cys_conserved += 1
        results["comparisons"].append(
            {
                "acc": acc,
                "len": other["len"],
                "panther_sf": other["panther_sf"],
                "signal": other["signal"],
                "aligned_columns": aligned,
                "identical": ident,
                "percent_identity_aligned": round(100 * ident / aligned, 1) if aligned else None,
                "target_coverage_percent": round(100 * aligned / target["len"], 1),
                "olf_domain_target_cys_aligned": dom_cys_target,
                "olf_domain_cys_conserved": dom_cys_conserved,
            }
        )
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
