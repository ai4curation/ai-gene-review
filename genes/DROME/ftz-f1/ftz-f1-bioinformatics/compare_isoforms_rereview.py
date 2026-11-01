"""Re-review sequence comparison of M9NFK2 against the reviewed FTZ-F1 entry P33244.

Reads the FASTA files already stored in ../ftz-f1-isoform-records/ (not modified)
and reports identity of M9NFK2 to each P33244 isoform, plus where the shared
C-terminal segment lies in the canonical (isoform 1) sequence.

Run: python3 compare_isoforms_rereview.py
"""

from pathlib import Path

RECORDS = Path(__file__).resolve().parent.parent / "ftz-f1-isoform-records"


def read_fasta(path: Path) -> str:
    """Return the concatenated sequence of a single-record FASTA file."""
    return "".join(
        line.strip() for line in path.read_text().splitlines() if not line.startswith(">")
    )


def main() -> None:
    target = read_fasta(RECORDS / "M9NFK2.fasta")
    iso2 = read_fasta(RECORDS / "P33244-2.fasta")
    iso1 = read_fasta(RECORDS / "P33244-1.fasta")
    print(f"M9NFK2 length: {len(target)}")
    print(f"P33244-2 length: {len(iso2)}; identical to M9NFK2: {target == iso2}")
    print(f"P33244-1 (canonical) length: {len(iso1)}; identical to M9NFK2: {target == iso1}")
    # longest shared suffix between target and canonical
    k = 0
    while k < min(len(target), len(iso1)) and target[-1 - k] == iso1[-1 - k]:
        k += 1
    print(f"Shared C-terminal suffix with P33244-1: {k} aa "
          f"(M9NFK2 {len(target) - k + 1}-{len(target)} = P33244-1 {len(iso1) - k + 1}-{len(iso1)})")
    print(f"Isoform-specific N-terminus: M9NFK2 1-{len(target) - k} vs P33244-1 1-{len(iso1) - k}")


if __name__ == "__main__":
    main()
