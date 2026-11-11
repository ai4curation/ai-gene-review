# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare every horse PPP4R4 (ENSECAG00000019485) UniProt product with human PPP4R4.

Fetches sequences from UniProt REST, globally aligns each horse model to human
Q6NUP7 (isoform 1, canonical) and Q6NUP7-2, and reports length, identity,
coverage and the positions of large indels relative to human isoform 1.
Also reports which accession is in the UniProt reference-proteome canonical
(gene-centric) set, using the downloaded proteome FASTA if supplied.

Usage: uv run compare_horse_models_rereview.py [UP000002281_9796.fasta.gz]
"""
import gzip
import json
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HORSE = ["A0A9L0S961", "A0A9L0S938", "A0A9L0RAK5", "A0A9L0T1D2", "F7CC09",
         "A0A3Q2KRD2", "A0A9L0RGM2", "A0A9L0RGB6", "A0A3Q2KK51", "A0A9L0R809"]
HUMAN = ["Q6NUP7", "Q6NUP7-2"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def compare(h: str, q: str, al: Align.PairwiseAligner) -> dict:
    aln = al.align(h, q)[0]
    ident = paired = 0
    gaps = []  # (human_start, human_end, kind, length)
    hc, qc = aln.coordinates
    for i in range(len(hc) - 1):
        hl = hc[i + 1] - hc[i]
        ql = qc[i + 1] - qc[i]
        if hl and ql:
            for k in range(hl):
                paired += 1
                ident += h[hc[i] + k] == q[qc[i] + k]
        elif hl and hl >= 5:
            gaps.append({"human_from": int(hc[i]) + 1, "human_to": int(hc[i + 1]),
                         "kind": "missing_in_horse", "length": int(hl)})
        elif ql and ql >= 5:
            gaps.append({"after_human": int(hc[i]), "kind": "extra_in_horse", "length": int(ql)})
    return {"paired": paired, "identity_pct": round(100 * ident / paired, 1),
            "human_coverage_pct": round(100 * paired / len(h), 1),
            "horse_coverage_pct": round(100 * paired / len(q), 1),
            "indels_ge5": gaps}


def main() -> None:
    canon = set()
    if len(sys.argv) > 1:
        with gzip.open(sys.argv[1], "rt") as fh:
            for line in fh:
                if line.startswith(">"):
                    canon.add(line.split("|")[1])
    al = aligner()
    hum = {a: fetch(a) for a in HUMAN}
    out = {"human_lengths": {a: len(s) for a, s in hum.items()}, "horse": {}}
    for acc in HORSE:
        s = fetch(acc)
        out["horse"][acc] = {"length": len(s),
                             "in_reference_proteome_canonical_set": (acc in canon) if canon else None,
                             **{f"vs_{h}": compare(hs, s, al) for h, hs in hum.items()}}
    # benchmark target vs the UniProt gene-centric canonical horse product
    t, c = fetch("A0A9L0S961"), fetch("A0A9L0S938")
    aln = al.align(c, t)[0]
    out["target_A0A9L0S961_vs_canonical_A0A9L0S938"] = {
        "alignment_coordinates": aln.coordinates.tolist(),
        **compare(c, t, al)}
    # PP4c-interaction residues mutated in human PPP4R4 (UniProt FT MUTAGEN, PMID:18715871)
    h = hum["Q6NUP7"]
    aln = al.align(h, t)[0]
    pos = {}
    for (hs, he), (qs, _qe) in zip(*aln.aligned):
        for k in range(he - hs):
            pos[int(hs) + k + 1] = int(qs) + k + 1
    out["pp4c_interface_residues_in_A0A9L0S961"] = {
        f"{h[p - 1]}{p}": {"horse_pos": pos.get(p),
                           "horse_residue": t[pos[p] - 1] if p in pos else None,
                           "human_context": h[p - 6:p + 5],
                           "horse_context": t[pos[p] - 6:pos[p] + 5] if p in pos else None}
        for p in (501, 618)}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
