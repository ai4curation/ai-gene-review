#!/usr/bin/env python3
"""Align local Strongyloides stercoralis beta-tubulin UniProt records."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
STRER = REPO_ROOT / "genes" / "STRER"
REFERENCE = "Q4KS25"
QUERIES = ["A0A0K0DXA9", "A0A0K0EJ28", "A0AAF5DAP5"]
REFERENCE_COORDS = {
    "Q4KS25_F168": 168,
    "Q4KS25_E199": 199,
    "Q4KS25_F201": 201,
}


def read_uniprot_sequence(accession: str) -> str:
    path = STRER / accession / f"{accession}-uniprot.txt"
    sequence = []
    in_sequence = False
    for line in path.read_text().splitlines():
        if line.startswith("SQ"):
            in_sequence = True
            continue
        if in_sequence and line.startswith("//"):
            break
        if in_sequence:
            sequence.append("".join(char for char in line if char.isalpha()))
    return "".join(sequence)


def needleman_wunsch(first: str, second: str) -> tuple[str, str]:
    match_score = 1
    mismatch_score = -1
    gap_score = -1

    rows = len(first) + 1
    cols = len(second) + 1
    scores = [[0] * cols for _ in range(rows)]
    traceback = [[""] * cols for _ in range(rows)]

    for row in range(1, rows):
        scores[row][0] = row * gap_score
        traceback[row][0] = "up"
    for col in range(1, cols):
        scores[0][col] = col * gap_score
        traceback[0][col] = "left"

    for row in range(1, rows):
        for col in range(1, cols):
            diagonal = scores[row - 1][col - 1] + (
                match_score if first[row - 1] == second[col - 1] else mismatch_score
            )
            up = scores[row - 1][col] + gap_score
            left = scores[row][col - 1] + gap_score
            best = max(diagonal, up, left)
            scores[row][col] = best
            traceback[row][col] = (
                "diagonal" if best == diagonal else "up" if best == up else "left"
            )

    first_aligned = []
    second_aligned = []
    row = len(first)
    col = len(second)
    while row or col:
        step = traceback[row][col]
        if step == "diagonal":
            row -= 1
            col -= 1
            first_aligned.append(first[row])
            second_aligned.append(second[col])
        elif step == "up":
            row -= 1
            first_aligned.append(first[row])
            second_aligned.append("-")
        else:
            col -= 1
            first_aligned.append("-")
            second_aligned.append(second[col])

    return "".join(reversed(first_aligned)), "".join(reversed(second_aligned))


def aligned_coordinates(
    reference_alignment: str,
    query_alignment: str,
) -> dict[str, str]:
    reference_position = 0
    query_position = 0
    coordinates = {}

    wanted = {position: label for label, position in REFERENCE_COORDS.items()}
    for reference_aa, query_aa in zip(reference_alignment, query_alignment):
        if reference_aa != "-":
            reference_position += 1
        if query_aa != "-":
            query_position += 1
        if reference_position in wanted and reference_aa != "-" and query_aa != "-":
            coordinates[wanted[reference_position]] = f"{query_aa}{query_position}"

    return coordinates


def main() -> None:
    sequences = {
        accession: read_uniprot_sequence(accession)
        for accession in [REFERENCE, *QUERIES]
    }
    print(
        "reference\tquery\treference_length\tquery_length\talignment_columns\t"
        "identities\tsubstitutions\tgap_columns\tQ4KS25_F168\tQ4KS25_E199\t"
        "Q4KS25_F201"
    )

    for query in QUERIES:
        reference_alignment, query_alignment = needleman_wunsch(
            sequences[REFERENCE],
            sequences[query],
        )
        identities = sum(
            first == second
            for first, second in zip(reference_alignment, query_alignment)
        )
        gap_columns = sum(
            first == "-" or second == "-"
            for first, second in zip(reference_alignment, query_alignment)
        )
        substitutions = len(reference_alignment) - identities - gap_columns
        coordinates = aligned_coordinates(reference_alignment, query_alignment)

        print(
            f"{REFERENCE}\t{query}\t{len(sequences[REFERENCE])}\t"
            f"{len(sequences[query])}\t{len(reference_alignment)}\t"
            f"{identities}\t{substitutions}\t{gap_columns}\t"
            f"{coordinates['Q4KS25_F168']}\t{coordinates['Q4KS25_E199']}\t"
            f"{coordinates['Q4KS25_F201']}"
        )


if __name__ == "__main__":
    main()
