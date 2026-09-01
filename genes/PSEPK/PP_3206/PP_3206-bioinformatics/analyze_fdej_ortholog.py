# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "biopython==1.85",
# ]
# ///
"""Reproduce the PP_3206 versus Hsero_1012/FdeJ sequence comparison."""

from __future__ import annotations

from pathlib import Path
from urllib.request import Request, urlopen

from Bio import Align
from Bio.Align import substitution_matrices


ACCESSIONS = {
    "PP_3206_Q88HZ6": "Q88HZ6",
    "Hsero_1012_D8J0X4": "D8J0X4",
}
OUT_DIR = Path(__file__).resolve().parent


def fetch_fasta(accession: str) -> tuple[str, str]:
    request = Request(
        f"https://rest.uniprot.org/uniprotkb/{accession}.fasta",
        headers={"User-Agent": "ai-gene-review/PP_3206-ortholog-analysis"},
    )
    with urlopen(request, timeout=60) as response:
        lines = response.read().decode("utf-8").strip().splitlines()
    if not lines or not lines[0].startswith(">"):
        raise RuntimeError(f"UniProt returned no FASTA record for {accession}")
    return lines[0][1:], "".join(lines[1:])


def main() -> None:
    records = {name: fetch_fasta(accession) for name, accession in ACCESSIONS.items()}
    target = records["PP_3206_Q88HZ6"][1]
    ortholog = records["Hsero_1012_D8J0X4"][1]

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

    results = f"""# PP_3206 FdeJ ortholog analysis

## Method

UniProt FASTA records for Q88HZ6 (P. putida KT2440 PP_3206) and D8J0X4
(Herbaspirillum seropedicae Hsero_1012, the proposed FdeJ counterpart) were
fetched on demand and aligned globally with Biopython PairwiseAligner, BLOSUM62,
gap-open -10, and gap-extension -0.5. Identity is calculated over columns
containing a residue from both proteins.

## Results

- Q88HZ6 length: {len(target)} aa
- D8J0X4 length: {len(ortholog)} aa
- Aligned residue pairs: {len(ungapped_pairs)}
- Identical aligned residues: {identities}
- Pairwise identity over aligned residue pairs: {identity_fraction:.1%}

The whole-protein similarity and shared epimerase/dehydratase architecture
support an orthology relationship. Neither protein has direct biochemical
evidence for KEGG reaction R13076, so the alignment does not establish the
substrate or carbon-carbon hydrolase chemistry.

## Reproduction

```bash
uv run genes/PSEPK/PP_3206/PP_3206-bioinformatics/analyze_fdej_ortholog.py
```
"""
    (OUT_DIR / "RESULTS.md").write_text(results)


if __name__ == "__main__":
    main()
