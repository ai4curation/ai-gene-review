"""Kyte-Doolittle hydropathy scan of ANKAR (Q7Z5J8).

UniProt annotates a single helical transmembrane segment (residues 309-329) by
sequence prediction (ECO:0000255). The sequence is read from the cached
ANKAR-uniprot.txt record in the parent folder. This script fetches the sequence and reports every
19-residue window with mean KD hydropathy >= 1.6, the classic threshold for a
candidate membrane-spanning helix (Kyte & Doolittle 1982). It also prints the
annotated segment and its score. It reports what it finds; it does not assume.

Run: uv run python hydropathy_check.py
"""

from pathlib import Path

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4,
      "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8,
      "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}
WINDOW = 19
THRESHOLD = 1.6


UNIPROT = Path(__file__).resolve().parent.parent / "ANKAR-uniprot.txt"


def read_sequence(path: Path) -> str:
    """Return the sequence from a UniProt flat file (lines after SQ, before //)."""
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ   "))
    body = []
    for line in lines[start + 1:]:
        if line.startswith("//"):
            break
        body.append(line.replace(" ", ""))
    return "".join(body)


def mean_kd(segment: str) -> float:
    """Mean Kyte-Doolittle hydropathy of a segment.

    >>> round(mean_kd("LLLL"), 2)
    3.8
    >>> round(mean_kd("KKDD"), 2)
    -3.7
    """
    return sum(KD[aa] for aa in segment) / len(segment)


def main() -> None:
    seq = read_sequence(UNIPROT)
    print(f"length\t{len(seq)}")
    tm = seq[308:329]
    print(f"annotated_TM_309-329\t{tm}\tmean_KD={mean_kd(tm):.2f}")
    hits = [(i + 1, mean_kd(seq[i:i + WINDOW])) for i in range(len(seq) - WINDOW + 1)]
    ranked = sorted(hits, key=lambda h: -h[1])
    print("top_windows\t" + "; ".join(f"{start}:{score:.2f}" for start, score in ranked[:4]))
    above = [(start, score) for start, score in hits if score >= THRESHOLD]
    print(f"windows_ge_{THRESHOLD}\t{len(above)}")
    for start, score in above:
        print(f"window_start\t{start}\t{seq[start - 1:start - 1 + WINDOW]}\t{score:.2f}")
    print(f"has_N_terminal_signal_window\t{any(start <= 30 for start, _ in above)}")


if __name__ == "__main__":
    main()
