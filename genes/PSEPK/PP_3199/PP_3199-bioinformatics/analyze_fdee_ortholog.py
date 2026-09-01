# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "biopython==1.85",
# ]
# ///
"""Reproduce the PP_3199 versus Hsero_1007/FdeE sequence comparison."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import tempfile
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from Bio import Align
from Bio.Align import substitution_matrices


ACCESSIONS = {
    "PP_3199_Q88I03": "Q88I03",
    "Hsero_1007_D8J0W9": "D8J0W9",
}
MOTIFS = ("GGGIGG", "GADG", "GDAAH")
OUT_DIR = Path(__file__).resolve().parent


def fetch_fasta(accession: str) -> tuple[str, str]:
    request = Request(
        f"https://rest.uniprot.org/uniprotkb/{accession}.fasta",
        headers={"User-Agent": "ai-gene-review/PP_3199-ortholog-analysis"},
    )
    with urlopen(request, timeout=60) as response:
        lines = response.read().decode("utf-8").strip().splitlines()
    if not lines or not lines[0].startswith(">"):
        raise RuntimeError(f"UniProt returned no FASTA record for {accession}")
    return lines[0][1:], "".join(lines[1:])


def fetch_proteome(query: str, output: Path) -> None:
    url = "https://rest.uniprot.org/uniprotkb/stream?" + urlencode(
        {"query": query, "format": "fasta"}
    )
    request = Request(url, headers={"User-Agent": "ai-gene-review/PP_3199-rbh"})
    with urlopen(request, timeout=300) as response:
        output.write_bytes(response.read())


def accession(header: str) -> str:
    fields = header.split("|")
    return fields[1] if len(fields) >= 3 else header


def mmseqs_hits(query: Path, database: Path, output: Path, tmp: Path) -> list[list[str]]:
    if not shutil.which("mmseqs"):
        raise RuntimeError("mmseqs is required for the reciprocal proteome search")
    subprocess.run(
        [
            "mmseqs", "easy-search", str(query), str(database), str(output), str(tmp),
            "--format-output", "query,target,evalue,bits,alnlen,pident",
            "--max-seqs", "10",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    return [line.split("\t") for line in output.read_text().splitlines() if line]


def main() -> None:
    records = {name: fetch_fasta(accession) for name, accession in ACCESSIONS.items()}
    target = records["PP_3199_Q88I03"][1]
    ortholog = records["Hsero_1007_D8J0W9"][1]

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

    with tempfile.TemporaryDirectory(prefix="pp3199-rbh-") as tmp_name:
        tmp = Path(tmp_name)
        psepk = tmp / "psepk.fasta"
        hsero = tmp / "hsero.fasta"
        forward_query = tmp / "d8j0w9.fasta"
        reverse_query = tmp / "q88i03.fasta"
        fetch_proteome("proteome:UP000000556", psepk)
        fetch_proteome("organism_id:757424", hsero)
        forward_query.write_text(f">D8J0W9\n{ortholog}\n")
        reverse_query.write_text(f">Q88I03\n{target}\n")
        forward = mmseqs_hits(forward_query, psepk, tmp / "forward.tsv", tmp / "mm-forward")
        reverse = mmseqs_hits(reverse_query, hsero, tmp / "reverse.tsv", tmp / "mm-reverse")

    forward_best = accession(forward[0][1])
    reverse_best = accession(reverse[0][1])
    reciprocal = forward_best == "Q88I03" and reverse_best == "D8J0W9"
    hit_lines = ["direction\trank\ttarget\tevalue\tbits\taligned_length\tpercent_identity"]
    for direction, hits in (("D8J0W9_to_PSEPK", forward), ("Q88I03_to_Hsero", reverse)):
        for rank, hit in enumerate(hits, start=1):
            hit_lines.append(
                "\t".join([direction, str(rank), accession(hit[1]), *hit[2:]])
            )
    (OUT_DIR / "reciprocal_hits.tsv").write_text("\n".join(hit_lines) + "\n")

    motif_lines = []
    for motif in MOTIFS:
        target_start = target.find(motif)
        ortholog_start = ortholog.find(motif)
        if target_start >= 0 and ortholog_start >= 0:
            result = (
                f"present at Q88I03 residues {target_start + 1}-{target_start + len(motif)} "
                f"and D8J0W9 residues {ortholog_start + 1}-{ortholog_start + len(motif)}"
            )
        else:
            result = "not found identically in both sequences"
        motif_lines.append(f"- `{motif}`: {result}")

    results = f"""# PP_3199 FdeE ortholog analysis

## Method

UniProt FASTA records for Q88I03 (P. putida KT2440 PP_3199) and D8J0W9
(Herbaspirillum seropedicae Hsero_1007/FdeE) were fetched on demand and aligned
globally with Biopython PairwiseAligner, BLOSUM62, gap-open -10, and gap-extension
-0.5. Identity is calculated over columns containing a residue from both
proteins.

## Results

- Q88I03 length: {len(target)} aa
- D8J0W9 length: {len(ortholog)} aa
- Aligned residue pairs: {len(ungapped_pairs)}
- Identical aligned residues: {identities}
- Pairwise identity over aligned residue pairs: {identity_fraction:.1%}
- D8J0W9 best hit in the PSEPK proteome: {forward_best}
- Q88I03 best hit in the H. seropedicae proteome: {reverse_best}
- Reciprocal best-hit relationship: {str(reciprocal).lower()}
{chr(10).join(motif_lines)}

The reciprocal best-hit result, whole-protein similarity, shared monooxygenase
architecture, and conserved flavonoid-degradation locus support an ISS
relationship between PP_3199 and the experimentally characterized Hsero_1007
FdeE. They do not constitute direct evidence that PP_3199 has identical
substrate range, regioselectivity, or cofactor preference in KT2440.

## Reproduction

```bash
uv run genes/PSEPK/PP_3199/PP_3199-bioinformatics/analyze_fdee_ortholog.py
```
"""
    (OUT_DIR / "RESULTS.md").write_text(results)


if __name__ == "__main__":
    main()
