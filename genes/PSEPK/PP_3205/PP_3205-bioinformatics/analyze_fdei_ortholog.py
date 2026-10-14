# /// script
# requires-python = ">=3.12"
# dependencies = ["biopython==1.85"]
# ///
"""Compare PP_3205 with Hsero_1011/FdeI and fetch its KEGG reactions."""

from pathlib import Path
from urllib.request import Request, urlopen

from Bio import Align
from Bio.Align import substitution_matrices

OUT_DIR = Path(__file__).resolve().parent
ACCESSIONS = {"PP_3205_Q88HZ7": "Q88HZ7", "Hsero_1011_D8J0X3": "D8J0X3"}


def fetch(url: str) -> str:
    request = Request(url, headers={"User-Agent": "ai-gene-review/PP_3205-analysis"})
    with urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8").strip()


def fasta(accession: str) -> tuple[str, str]:
    lines = fetch(f"https://rest.uniprot.org/uniprotkb/{accession}.fasta").splitlines()
    return lines[0][1:], "".join(lines[1:])


def main() -> None:
    records = {name: fasta(accession) for name, accession in ACCESSIONS.items()}
    target = records["PP_3205_Q88HZ7"][1]
    ortholog = records["Hsero_1011_D8J0X3"][1]
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    alignment = aligner.align(target, ortholog)[0]
    pairs = [(a, b) for a, b in zip(str(alignment[0]), str(alignment[1]), strict=True) if a != "-" and b != "-"]
    identities = sum(a == b for a, b in pairs)
    kegg_link = fetch("https://rest.kegg.jp/link/ko/ppu:PP_3205").replace("\t", " -> ")
    summaries = []
    for reaction_id in ("R13078", "R13079"):
        reaction = fetch(f"https://rest.kegg.jp/get/{reaction_id}")
        lines = "\n".join(
            line
            for line in reaction.splitlines()
            if line.startswith(("DEFINITION", "COMMENT", "            unclear"))
        )
        summaries.append(f"{reaction_id}: {lines}")

    (OUT_DIR / "sequences.fasta").write_text("\n".join(f">{name} {header}\n{seq}" for name, (header, seq) in records.items()) + "\n")
    (OUT_DIR / "alignment.txt").write_text(str(alignment) + "\n")
    (OUT_DIR / "RESULTS.md").write_text(f"""# PP_3205 FdeI ortholog analysis

## Method

Q88HZ7 and D8J0X3 were fetched from UniProt and aligned globally with
Biopython PairwiseAligner, BLOSUM62, gap-open -10, and gap-extension -0.5.
KEGG mapping and reaction records were fetched through KEGG REST.

## Results

- Q88HZ7 length: {len(target)} aa
- D8J0X3 length: {len(ortholog)} aa
- Aligned residue pairs: {len(pairs)}
- Identical aligned residues: {identities}
- Pairwise identity over aligned residue pairs: {identities / len(pairs):.1%}
- KEGG target mapping: `{kegg_link}`
- KEGG reaction summaries: `{' | '.join(summaries)}`

The high whole-protein similarity and shared fumarylacetoacetate-hydrolase-like
architecture support an FdeI orthology relationship. KEGG marks both reactions
unclear; R13078 is a predicted decarboxylation, whereas R13079 eliminates water.
Neither reaction has been demonstrated for either protein.

## Reproduction

```bash
uv run genes/PSEPK/PP_3205/PP_3205-bioinformatics/analyze_fdei_ortholog.py
```
""")


if __name__ == "__main__":
    main()
