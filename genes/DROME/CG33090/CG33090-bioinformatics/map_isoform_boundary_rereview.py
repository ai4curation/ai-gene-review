"""Map the N-terminal boundary of the PC isoform onto PB and human GBA2.

Reads an existing multiple alignment (FASTA, gapped) and reports, for each
query position of a chosen sequence, the aligned residue positions in the
other sequences. Results are computed from the alignment only.

Usage:
    uv run python map_isoform_boundary_rereview.py outputs/global.fasta \
        --query X2JE45 --positions 1 28 29 51 296 356 787 \
        --output outputs/rereview-boundary-global.json
"""

import argparse
import json


def read_alignment(path: str) -> dict[str, str]:
    """Read a gapped FASTA alignment keyed by the first token of each header.

    >>> import tempfile, os
    >>> fh = tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False)
    >>> _ = fh.write(">a x\\nAC-D\\n>b\\nA-CD\\n"); fh.close()
    >>> read_alignment(fh.name)
    {'a': 'AC-D', 'b': 'A-CD'}
    >>> os.unlink(fh.name)
    """
    seqs: dict[str, str] = {}
    key = None
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if line.startswith(">"):
                key = line[1:].split()[0]
                seqs[key] = ""
            elif key is not None:
                seqs[key] += line
    return seqs


def column_positions(aligned: str) -> list[int | None]:
    """Ungapped residue number at each alignment column (None for gaps).

    >>> column_positions("A-CD")
    [1, None, 2, 3]
    """
    pos = 0
    out: list[int | None] = []
    for char in aligned:
        if char == "-":
            out.append(None)
        else:
            pos += 1
            out.append(pos)
    return out


def map_positions(
    seqs: dict[str, str], query: str, positions: list[int]
) -> list[dict[str, object]]:
    """Map query residue positions to aligned residues of every sequence.

    >>> map_positions({"a": "AC-D", "b": "A-CD"}, "a", [2, 3])
    [{'query_position': 2, 'aligned': {'a': [2, 'C'], 'b': None}}, {'query_position': 3, 'aligned': {'a': [3, 'D'], 'b': [3, 'D']}}]
    """
    cols = {name: column_positions(seq) for name, seq in seqs.items()}
    rows = []
    for p in positions:
        col = cols[query].index(p)
        aligned: dict[str, object] = {}
        for name, seq in seqs.items():
            residue_number = cols[name][col]
            aligned[name] = None if residue_number is None else [residue_number, seq[col]]
        rows.append({"query_position": p, "aligned": aligned})
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("alignment")
    parser.add_argument("--query", required=True)
    parser.add_argument("--positions", type=int, nargs="+", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    seqs = read_alignment(args.alignment)
    result = {
        "alignment": args.alignment,
        "query": args.query,
        "mappings": map_positions(seqs, args.query, args.positions),
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
