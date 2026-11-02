"""Compare candidate awd N-terminal processing forms against the published intact mass.

Inputs are the frozen UniProt JSON records for the benchmark product (A0A0B4LHX6,
awd-PC/PD) and the reviewed product (P08879, awd-PE). The script computes average
masses for candidate mature forms and prints their deviation from an observed mass
supplied on the command line (the electrospray value recorded in P08879's
MASS SPECTROMETRY comment). It also reports where the reviewed sequence begins
inside the longer product, and the hydrophobic fraction of the extension.

Usage: python mass_rereview.py TARGET_JSON REFERENCE_JSON OBSERVED_MASS OUT_JSON
"""

import json
import sys

from Bio.SeqUtils.ProtParam import ProteinAnalysis

ACETYL = 42.0367  # average mass added by N-terminal acetylation (C2H2O)


def sequence(path: str) -> tuple[str, str]:
    record = json.load(open(path))
    return record["primaryAccession"], record["sequence"]["value"]


def mass(seq: str) -> float:
    return ProteinAnalysis(seq).molecular_weight()


def main() -> None:
    target_path, reference_path, observed_s, out_path = sys.argv[1:5]
    observed = float(observed_s)
    tacc, tseq = sequence(target_path)
    racc, rseq = sequence(reference_path)
    offset = tseq.find(rseq)
    extension = tseq[:offset] if offset >= 0 else ""
    hydrophobic = sum(extension.count(a) for a in "AILMFVWC")
    candidates = {
        f"{racc} 1-{len(rseq)} unprocessed": mass(rseq),
        f"{racc} 2-{len(rseq)} (Met removed)": mass(rseq[1:]),
        f"{racc} 2-{len(rseq)} (Met removed) + N-acetyl": mass(rseq[1:]) + ACETYL,
        f"{tacc} 1-{len(tseq)} unprocessed": mass(tseq),
        f"{tacc} 2-{len(tseq)} (Met removed) + N-acetyl": mass(tseq[1:]) + ACETYL,
        f"{tacc} 18-{len(tseq)} (after predicted signal peptide 1-17)": mass(tseq[17:]),
    }
    rows = [
        {"form": k, "average_mass": round(v, 1), "delta_vs_observed": round(v - observed, 1)}
        for k, v in candidates.items()
    ]
    result = {
        "target": tacc,
        "reference": racc,
        "observed_mass": observed,
        "reference_start_in_target": offset + 1 if offset >= 0 else None,
        "extension": extension,
        "extension_hydrophobic_fraction": round(hydrophobic / len(extension), 2) if extension else None,
        "candidates": rows,
    }
    json.dump(result, open(out_path, "w"), indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
