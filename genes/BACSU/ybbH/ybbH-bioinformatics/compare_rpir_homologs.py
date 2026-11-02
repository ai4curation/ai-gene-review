"""Compare B. subtilis YbbH/MurR (Q45581) with characterized RpiR-family regulators.

Reproducible check of two questions raised in the ybbH review:

1. How close is YbbH to E. coli MurR (P77245) versus the paralogous RpiR-family
   regulators HexR (E. coli P46118, S. oneidensis Q8EE97) and RpiR (E. coli P0ACS7)?
   Pairwise identity alone cannot assign orthology in this family (all members share
   the HTH_6 + SIS architecture), but it shows how much of the MurR assignment rests on
   gene context rather than sequence.
2. How similar is the KBase dashboard query sequence (NZ_CP017763.1_2226) to Q45581?

Also fetches the SubtiWiki gene record for murR (BSU_01690) and records the operon and
regulation fields verbatim.

Usage (from repo root):
    uv run python genes/BACSU/ybbH/ybbH-bioinformatics/compare_rpir_homologs.py

Outputs are written to genes/BACSU/ybbH/ybbH-bioinformatics/data/.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
DASHBOARD_FASTA = HERE.parent / "ybbH-dashboard-prediction-evidence" / "NZ_CP017763.1_2226.fasta"

ACCESSIONS = {
    "Q45581": "B. subtilis YbbH/MurR (query)",
    "P77245": "E. coli MurR (YfeT), characterized MurNAc-6P repressor",
    "P46118": "E. coli HexR (YebK)",
    "Q8EE97": "S. oneidensis HexR (SO_2490)",
    "P0ACS7": "E. coli RpiR (AlsR)",
    "Q2G1G4": "S. aureus NCTC8325 SAOUHSC_00160 (MurR-like, murQ cluster)",
}

SUBTIWIKI_MURR = "https://subtiwiki.uni-goettingen.de/v5/api/gene/174"


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as resp:  # noqa: S310
        return resp.read()


def get_fasta(acc: str) -> str:
    path = DATA / f"{acc}.fasta"
    if not path.exists():
        path.write_bytes(fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"))
    return str(next(SeqIO.parse(path, "fasta")).seq)


def identity(a: str, b: str) -> tuple[float, float, int]:
    """Global alignment (BLOSUM62, gap open -10, extend -0.5).

    Returns (identity over aligned columns, identity over shorter sequence, aligned columns).
    """
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = 0
    cols = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            if a[i] == b[j]:
                ident += 1
    return 100.0 * ident / cols, 100.0 * ident / min(len(a), len(b)), cols


def main() -> int:
    DATA.mkdir(exist_ok=True)
    seqs = {acc: get_fasta(acc) for acc in ACCESSIONS}
    if DASHBOARD_FASTA.exists():
        seqs["NZ_CP017763.1_2226"] = str(next(SeqIO.parse(DASHBOARD_FASTA, "fasta")).seq)
        ACCESSIONS["NZ_CP017763.1_2226"] = "KBase dashboard query (B. subtilis strain)"

    query = seqs["Q45581"]
    lines = ["subject\tdescription\tlength\tpct_id_aligned_cols\tpct_id_shorter_seq\taligned_cols"]
    for acc, seq in seqs.items():
        if acc == "Q45581":
            continue
        pid_cols, pid_short, cols = identity(query, seq)
        lines.append(
            f"{acc}\t{ACCESSIONS[acc]}\t{len(seq)}\t{pid_cols:.1f}\t{pid_short:.1f}\t{cols}"
        )
    out = DATA / "pairwise_identity_vs_Q45581.tsv"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))

    # SubtiWiki record (operon and regulation fields only)
    try:
        rec = json.loads(fetch(SUBTIWIKI_MURR))["data"]
        keep = {
            "name": rec.get("name"),
            "synonyms": rec.get("synonyms"),
            "description": rec.get("description"),
            "function": rec.get("function"),
            "product": rec.get("product"),
            "uniprot": rec.get("outlinks", {}).get("uniprot"),
            "locus_tag": [g.get("locus_tag") for g in rec.get("genomic_annotations", [])],
            "operons": [
                {
                    "genes": [g["name"] for g in op.get("genes", [])],
                    "regulations": [
                        {
                            "regulator": r.get("regulon", {}).get("regulator_gene", {}).get("name"),
                            "mode": r.get("mode"),
                            "mechanism": r.get("mechanism"),
                            "effect": r.get("custom_effect_specifier"),
                            "reference": r.get("description"),
                        }
                        for r in op.get("regulations", [])
                    ],
                }
                for op in rec.get("operons", [])
            ],
            "effectors": rec.get("protein", {}).get("effectors"),
            "references": [
                ref["pubmed"]["id"] for ref in rec.get("references", []) if ref.get("pubmed")
            ],
        }
        (DATA / "subtiwiki_murR_BSU_01690.json").write_text(json.dumps(keep, indent=2) + "\n")
        print(json.dumps(keep, indent=2))
    except Exception as exc:  # network failure is reported, not hidden
        print(f"SubtiWiki fetch failed: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
