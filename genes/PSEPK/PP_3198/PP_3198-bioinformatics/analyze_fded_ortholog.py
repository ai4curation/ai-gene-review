# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "biopython==1.85",
# ]
# ///
"""Reproduce the PP_3198 versus Hsero_1006/FdeD sequence comparison."""

from __future__ import annotations

from pathlib import Path
from urllib.request import Request, urlopen

from Bio import Align
from Bio.Align import substitution_matrices


ACCESSIONS = {
    "PP_3198_Q88I04": "Q88I04",
    "Hsero_1006_D8J0W8": "D8J0W8",
}
OUT_DIR = Path(__file__).resolve().parent


def fetch_fasta(accession: str) -> tuple[str, str]:
    request = Request(
        f"https://rest.uniprot.org/uniprotkb/{accession}.fasta",
        headers={"User-Agent": "ai-gene-review/PP_3198-ortholog-analysis"},
    )
    with urlopen(request, timeout=60) as response:
        lines = response.read().decode("utf-8").strip().splitlines()
    if not lines or not lines[0].startswith(">"):
        raise RuntimeError(f"UniProt returned no FASTA record for {accession}")
    return lines[0][1:], "".join(lines[1:])


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "ai-gene-review/PP_3198-analysis"})
    with urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8").strip()


def main() -> None:
    records = {name: fetch_fasta(accession) for name, accession in ACCESSIONS.items()}
    target = records["PP_3198_Q88I04"][1]
    ortholog = records["Hsero_1006_D8J0W8"][1]

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
    kegg_link = fetch_text("https://rest.kegg.jp/link/ko/ppu:PP_3198").replace("\t", " -> ")
    kegg_reaction = fetch_text("https://rest.kegg.jp/get/R13074")
    reaction_summary = "\n".join(
        line for line in kegg_reaction.splitlines() if line.startswith(("DEFINITION", "COMMENT"))
    )

    fasta_lines = []
    for name, (header, sequence) in records.items():
        fasta_lines.extend([f">{name} {header}", sequence])
    (OUT_DIR / "sequences.fasta").write_text("\n".join(fasta_lines) + "\n")
    (OUT_DIR / "alignment.txt").write_text(str(alignment) + "\n")

    results = f"""# PP_3198 FdeD ortholog analysis

## Method

UniProt FASTA records for Q88I04 (P. putida KT2440 PP_3198) and D8J0W8
(Herbaspirillum seropedicae Hsero_1006, the proposed FdeD counterpart) were
fetched on demand and aligned globally with Biopython PairwiseAligner, BLOSUM62,
gap-open -10, and gap-extension -0.5. Identity is calculated over columns
containing a residue from both proteins.

## Results

- Q88I04 length: {len(target)} aa
- D8J0W8 length: {len(ortholog)} aa
- Aligned residue pairs: {len(ungapped_pairs)}
- Identical aligned residues: {identities}
- Pairwise identity over aligned residue pairs: {identities / len(ungapped_pairs):.1%}
- KEGG target mapping: `{kegg_link}`
- KEGG R13074 summary: `{reaction_summary}`

Both proteins are compact Rieske [2Fe-2S]-domain proteins. The similarity and
conserved cysteine/histidine-rich region support orthology, but neither sequence
comparison nor the Herbaspirillum pathway paper establishes which enzyme accepts
electrons from FdeD or whether FdeD is required for KEGG reaction R13074.

## Reproduction

```bash
uv run genes/PSEPK/PP_3198/PP_3198-bioinformatics/analyze_fded_ortholog.py
```
"""
    (OUT_DIR / "RESULTS.md").write_text(results)


if __name__ == "__main__":
    main()
