# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Re-review analysis for Drosophila NTPase (O76268).

1. Compare the benchmark accession O76268 (NTPase-PA) with the other UniProt
   products of the same gene (Q9VQI8 = PE, M9PBV2 = PF, Q8IPZ6 = PC/PD).
2. Check which isoform numbering matches the residues named in PMID:19467631
   (C42 in the transmembrane domain, C447 in the exoplasmic domain).
3. Report global identity of O76268 to C. elegans uda-1 (same PANTHER
   subfamily PTHR11782:SF127) and to human ENTPD5 (SF35) and ENTPD6 (SF99).

Sequences are downloaded live from UniProt REST; nothing is hardcoded.
Run: uv run compare_isoforms_rereview.py
"""

import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ISOFORMS = {"O76268": "NTPase-PA", "Q9VQI8": "NTPase-PE", "M9PBV2": "NTPase-PF", "Q8IPZ6": "NTPase-PC/PD"}
RELATIVES = {
    "Q9XU84": "uda-1 (C. elegans, PTHR11782:SF127)",
    "O75356": "ENTPD5 (human, PTHR11782:SF35)",
    "O75354": "ENTPD6 (human, PTHR11782:SF99)",
}
# ACR1 motif and PIRSR proton acceptor reported on O76268
ACR1 = "DAGSTGS"


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = sum(1 for x, y in zip(aln[0], aln[1]) if x == y and x != "-")
    aligned = sum(1 for x, y in zip(aln[0], aln[1]) if x != "-" and y != "-")
    return ident / aligned, aligned


def main() -> None:
    seqs = {acc: fetch(acc) for acc in list(ISOFORMS) + list(RELATIVES)}
    ref = seqs["O76268"]
    out: dict = {"isoforms": {}, "relatives": {}}
    for acc, name in ISOFORMS.items():
        s = seqs[acc]
        off = s.find(ref[10:40])  # shared segment after the variable N-terminus
        out["isoforms"][acc] = {
            "name": name,
            "length": len(s),
            "acr1_present": ACR1 in s,
            "offset_vs_O76268": (off - 10) if off >= 0 else None,
            "contains_O76268_C_terminal_300": ref[-300:] in s,
        }
    out["pmid19467631_residues_on_O76268"] = {"C42": ref[41], "C447": ref[446]}
    out["O76268_residue_202"] = ref[201]
    for acc, name in RELATIVES.items():
        pid, n = identity(ref, seqs[acc])
        out["relatives"][acc] = {"name": name, "identity": round(pid, 3), "aligned_columns": n}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
