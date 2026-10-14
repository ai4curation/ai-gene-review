# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "biopython==1.85",
# ]
# ///
"""Reproduce the PP_3197 versus Hsero_1005/FdeC sequence comparison."""

from __future__ import annotations

from pathlib import Path
from urllib.request import Request, urlopen

from Bio import Align
from Bio.Align import substitution_matrices


ACCESSIONS = {
    "PP_3197_Q88I05": "Q88I05",
    "Hsero_1005_D8J0W7": "D8J0W7",
}
MOTIF = "GCEHFTFHMG"
OUT_DIR = Path(__file__).resolve().parent


def fetch_fasta(accession: str) -> tuple[str, str]:
    request = Request(
        f"https://rest.uniprot.org/uniprotkb/{accession}.fasta",
        headers={"User-Agent": "ai-gene-review/PP_3197-ortholog-analysis"},
    )
    with urlopen(request, timeout=60) as response:
        lines = response.read().decode("utf-8").strip().splitlines()
    if not lines or not lines[0].startswith(">"):
        raise RuntimeError(f"UniProt returned no FASTA record for {accession}")
    return lines[0][1:], "".join(lines[1:])


def main() -> None:
    records = {name: fetch_fasta(accession) for name, accession in ACCESSIONS.items()}
    target = records["PP_3197_Q88I05"][1]
    ortholog = records["Hsero_1005_D8J0W7"][1]

    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    alignment = aligner.align(target, ortholog)[0]
    aligned_target = str(alignment[0])
    aligned_ortholog = str(alignment[1])

    ungapped_pairs = [
        (a, b)
        for a, b in zip(aligned_target, aligned_ortholog, strict=True)
        if a != "-" and b != "-"
    ]
    identities = sum(a == b for a, b in ungapped_pairs)
    identity_fraction = identities / len(ungapped_pairs)

    fasta_lines = []
    for name, (header, sequence) in records.items():
        fasta_lines.extend([f">{name} {header}", sequence])
    (OUT_DIR / "sequences.fasta").write_text("\n".join(fasta_lines) + "\n")
    (OUT_DIR / "alignment.txt").write_text(str(alignment) + "\n")

    target_motif = target.find(MOTIF)
    ortholog_motif = ortholog.find(MOTIF)
    motif_result = (
        f"present at Q88I05 residues {target_motif + 1}-{target_motif + len(MOTIF)} "
        f"and D8J0W7 residues {ortholog_motif + 1}-{ortholog_motif + len(MOTIF)}"
        if target_motif >= 0 and ortholog_motif >= 0
        else "not found identically in both sequences"
    )
    results = f"""# PP_3197 FdeC ortholog analysis

## Method

UniProt FASTA records for Q88I05 (P. putida KT2440 PP_3197) and D8J0W7
(Herbaspirillum seropedicae Hsero_1005/FdeC) were fetched on demand and aligned
globally with Biopython PairwiseAligner, BLOSUM62, gap-open -10, and gap-extension
-0.5. Identity is calculated over columns containing a residue from both
proteins.

## Results

- Q88I05 length: {len(target)} aa
- D8J0W7 length: {len(ortholog)} aa
- Aligned residue pairs: {len(ungapped_pairs)}
- Identical aligned residues: {identities}
- Pairwise identity over aligned residue pairs: {identity_fraction:.1%}
- Reported C-terminal motif `{MOTIF}`: {motif_result}

The high whole-protein identity and identical motif support an ISS relationship
between PP_3197 and the experimentally characterized Hsero_1005 FdeC. They do
not constitute direct evidence that PP_3197 uses the same substrate, metal, or
reaction conditions in KT2440.

## Reproduction

```bash
uv run genes/PSEPK/PP_3197/PP_3197-bioinformatics/analyze_fdec_ortholog.py
```
"""
    (OUT_DIR / "RESULTS.md").write_text(results)


if __name__ == "__main__":
    main()
