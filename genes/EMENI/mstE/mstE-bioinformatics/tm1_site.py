# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""TM1 protonation-site residue (E. coli XylE Asp27 / human GLUT1 Asn29) in
A. nidulans MstE (Q5B0S0) and its A. nidulans glucose-transporter paralogs whose
glucose uptake was reported as CCCP-sensitive when expressed in yeast
(HxtB = MstC/AN6669, HxtC = AN10891, HxtE = AN1797; PMID:24282591), plus
MstA/HxtD (AN8737), N. crassa GLT-1 (SF92), and uniporter controls
(human GLUT1, S. cerevisiae HXT1).

Each protein is globally aligned (BLOSUM62, open -10, extend -0.5) to XylE
(P0AGF4); the residue aligned to XylE position 27 is reported, with the PANTHER
subfamily taken live from UniProt. Sequences are fetched live from UniProt.

Run: uv run --script tm1_site.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

REF = "P0AGF4"
REF_POS = 27
TARGETS = {
    "Q5B0S0": "MstE (A. nidulans AN5860)",
    "Q1K4S3": "GLT-1 (N. crassa NCU01633)",
    "Q5AYG1": "MstC/HxtB (A. nidulans AN6669; CCCP-sensitive in yeast)",
    "C8VDD8": "HxtC (A. nidulans AN10891; CCCP-sensitive in yeast)",
    "Q5BCD3": "HxtE (A. nidulans AN1797; CCCP-sensitive in yeast)",
    "Q5ASJ3": "MstA/HxtD (A. nidulans AN8737)",
    "P11166": "GLUT1 (human; uniporter control)",
    "P32465": "HXT1 (S. cerevisiae; low-affinity facilitator control)",
}


def entry(acc: str) -> tuple[str, str]:
    r = requests.get(
        f"https://rest.uniprot.org/uniprotkb/{acc}?fields=sequence,xref_panther&format=json",
        timeout=60,
    )
    r.raise_for_status()
    d = r.json()
    sf = ";".join(
        x["id"] for x in d.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"
    )
    return d["sequence"]["value"], sf


def mapped_residue(ref: str, tgt: str, pos: int) -> tuple[int | None, str]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(ref, tgt)[0]
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        if rs <= pos - 1 < re_:
            j = ts + (pos - 1 - rs)
            return j + 1, tgt[j]
    return None, "-"


def main() -> None:
    ref, _ = entry(REF)
    print(f"reference {REF} position {REF_POS} residue {ref[REF_POS - 1]}")
    print("accession\tlabel\tpanther\tmapped_position\tresidue\tTM1_window")
    for acc, label in TARGETS.items():
        seq, sf = entry(acc)
        p, aa = mapped_residue(ref, seq, REF_POS)
        win = seq[max(0, p - 6): p + 5] if p else "-"
        print(f"{acc}\t{label}\t{sf}\t{p}\t{aa}\t{win}")


if __name__ == "__main__":
    main()
