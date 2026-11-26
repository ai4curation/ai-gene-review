# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Re-review analysis: genomic context of the donkey PDIA4 gene model and
identity of its N-terminal KRAB-C2H2 segment.

Fetches gene coordinates from the Ensembl REST API (donkey and human), and
sequences from UniProt, then aligns the donkey A0A8C4LTV9 N-terminal segment
(residues 1-580) to human ZNF786 and ZNF425, and the C-terminal segment to
human PDIA4. Writes RESULTS-rereview.md next to this script.

Run: uv run --script genes/EQUAS/PDIA4/PDIA4-bioinformatics/locus_context_rereview.py
"""

from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ENSEMBL = "https://rest.ensembl.org"
HERE = Path(__file__).parent

DONKEY_ACC = "A0A8C4LTV9"
HUMAN = {"PDIA4": "P13667", "ZNF786": "Q8N393", "ZNF425": "Q6IV72"}
SPLIT = 580  # end of the last C2H2 zinc finger (FT 552..579) in A0A8C4LTV9


def ensembl_json(path: str):
    r = requests.get(ENSEMBL + path, headers={"Content-Type": "application/json"}, timeout=60)
    r.raise_for_status()
    return r.json()


def uniprot_seq(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def local_identity(a: str, b: str) -> tuple[float, int, tuple[int, int], tuple[int, int]]:
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = paired = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            paired += 1
            ident += a[i] == b[j]
    qa = (aln.aligned[0][0][0] + 1, aln.aligned[0][-1][1])
    qb = (aln.aligned[1][0][0] + 1, aln.aligned[1][-1][1])
    return 100.0 * ident / paired, paired, qa, qb


def main() -> None:
    lines = ["# PDIA4 re-review: locus context and N-terminal segment identity", ""]
    lines.append("## Genomic context (Ensembl REST)")
    lines.append("")
    donkey_gene = ensembl_json("/lookup/id/ENSEASG00005009014")
    region = f"{donkey_gene['seq_region_name']}:{donkey_gene['start'] - 60000}-{donkey_gene['end'] + 60000}"
    lines.append(
        f"- Donkey PDIA4 gene ENSEASG00005009014: chr{donkey_gene['seq_region_name']}:"
        f"{donkey_gene['start']}-{donkey_gene['end']} strand {donkey_gene['strand']} "
        f"({donkey_gene['end'] - donkey_gene['start'] + 1} bp)"
    )
    lines.append(f"- Donkey protein-coding genes overlapping chr{region}:")
    for g in ensembl_json(f"/overlap/region/equus_asinus/{region}?feature=gene"):
        if g["biotype"] == "protein_coding":
            lines.append(
                f"  - {g['id']} {g.get('external_name')} {g['start']}-{g['end']} strand {g['strand']}"
            )
    lines.append("- Human genes (GRCh38):")
    for sym in HUMAN:
        h = ensembl_json(f"/lookup/symbol/homo_sapiens/{sym}")
        lines.append(
            f"  - {sym} {h['id']} chr{h['seq_region_name']}:{h['start']}-{h['end']} strand {h['strand']} "
            f"({h['end'] - h['start'] + 1} bp)"
        )
    lines.append("")
    lines.append("## Segment alignments (local, BLOSUM62, gap -10/-0.5)")
    lines.append("")
    donkey = uniprot_seq(DONKEY_ACC)
    nterm, cterm = donkey[:SPLIT], donkey[SPLIT:]
    lines.append(f"- {DONKEY_ACC} length {len(donkey)}; N-terminal segment 1-{SPLIT}, C-terminal segment {SPLIT + 1}-{len(donkey)}")
    for sym, acc in HUMAN.items():
        hs = uniprot_seq(acc)
        for name, seg, offset in (("N-terminal", nterm, 0), ("C-terminal", cterm, SPLIT)):
            pct, paired, qa, qb = local_identity(seg, hs)
            lines.append(
                f"- {name} segment vs human {sym} ({acc}, {len(hs)} aa): {pct:.1f}% identity over {paired} paired residues; "
                f"donkey {qa[0] + offset}-{qa[1] + offset}, human {qb[0]}-{qb[1]}"
            )
    lines.append("")
    lines.append(
        "Pairwise identity does not by itself establish orthology; the locus order is the "
        "positional (synteny) evidence."
    )
    (HERE / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
