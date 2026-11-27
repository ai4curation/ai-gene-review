# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare horse LNPEP (A0A9L0TDM5) with human LNPEP (Q9UIQ6).

Fetches both sequences from UniProt, makes a global alignment (BLOSUM62),
reports identity/coverage, and maps the human functional motifs (zinc-binding
HEXXH...E, GAMEN exopeptidase motif, tankyrase-binding RXXPDG, cytosolic
dileucine motifs) onto the horse sequence. Prints JSON-like text; nothing is
hard-coded except the motif patterns themselves.
"""

import json
import re

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"horse": "A0A9L0TDM5", "human": "Q9UIQ6"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(seqs["horse"], seqs["human"])[0]
    a, b = aln[0], aln[1]
    ident = sum(1 for x, y in zip(a, b) if x == y and x != "-")
    aligned = sum(1 for x, y in zip(a, b) if x != "-" and y != "-")
    out = {
        "lengths": {k: len(v) for k, v in seqs.items()},
        "identical_positions": ident,
        "aligned_positions": aligned,
        "identity_over_aligned": round(ident / aligned, 4),
        "identity_over_human_length": round(ident / len(seqs["human"]), 4),
    }
    # gaps summary: runs of '-' in human row = horse insertions
    ins = [m.span() for m in re.finditer(r"-+", b)]
    dels = [m.span() for m in re.finditer(r"-+", a)]
    out["horse_insertions_vs_human_alnpos"] = ins
    out["horse_deletions_vs_human_alnpos"] = dels
    motifs = {
        "zinc_HEXXH_18_E": r"HE..H.{18}E",
        "GAMEN": r"GAMEN",
        "tankyrase_RXXPDG": r"R..PDG",
        "dileucine_LL": r"[DE]...L[LI]",
    }
    out["motifs"] = {}
    for name, pat in motifs.items():
        out["motifs"][name] = {
            k: [(m.start() + 1, m.group()) for m in re.finditer(pat, s)]
            for k, s in seqs.items()
        }
    out["horse_Nterm_first60"] = seqs["horse"][:60]
    out["human_Nterm_first60"] = seqs["human"][:60]
    print(json.dumps(out, indent=2))
    print(aln.format()[:4000])


if __name__ == "__main__":
    main()
