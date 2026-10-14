"""Check the archaemetzincin zinc-binding motif HEXXHXXGXXH in AMZ1 and comparators.

Metzincins coordinate the catalytic zinc with three histidines: two in HEXXH and a
third ten residues after the first. This script fetches each sequence from UniProt,
finds every HEXXHXXG match, and reports the residue at the third-ligand position
(first His + 10). It prints what it finds; it does not assume the answer.

Run: uv run python zinc_motif_check.py
"""

import re
import urllib.request

ACCESSIONS = {
    "Q400G9": "human AMZ1",
    "Q86W34": "human AMZ2",
    "Q8TXW1": "Methanopyrus kandleri AmzA (structure, PMID:20597090)",
    "O29917": "Archaeoglobus fulgidus AmzA (structure, PMID:22937112)",
}

MOTIF = re.compile(r"HE..H..G")


def fetch_sequence(accession: str) -> str:
    """Return the canonical UniProt sequence for an accession."""
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    with urllib.request.urlopen(url) as handle:
        fasta = handle.read().decode()
    return "".join(fasta.splitlines()[1:])


def third_ligand(sequence: str, start: int) -> str:
    """Residue at first-His + 10 (0-based start of the HEXXH match).

    >>> third_ligand("HEIGHIFGLRHCQ", 0)
    'H'
    >>> third_ligand("HELCHLLGLGNCR", 0)
    'N'
    """
    return sequence[start + 10]


def main() -> None:
    print("accession\tprotein\tlength\tmotif_start\tmotif_window\tthird_ligand_pos\tthird_ligand")
    for accession, name in ACCESSIONS.items():
        sequence = fetch_sequence(accession)
        for match in MOTIF.finditer(sequence):
            start = match.start()
            print(
                f"{accession}\t{name}\t{len(sequence)}\t{start + 1}\t"
                f"{sequence[start:start + 14]}\t{start + 11}\t{third_ligand(sequence, start)}"
            )


if __name__ == "__main__":
    main()
