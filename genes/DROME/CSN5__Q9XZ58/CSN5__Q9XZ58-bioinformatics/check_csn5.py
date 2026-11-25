"""Check JAMM catalytic residues and PANTHER subfamily placement for Drosophila CSN5 (Q9XZ58).

Usage:
    uv run python check_csn5.py <uniprot.txt> <panther_classification_dir>

The PANTHER directory holds PANTHER 19.0 per-organism classification files
(PTHR19.0_<organism>), as fetched from
http://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/
"""

import re
import sys
from pathlib import Path


def read_sequence(uniprot_txt: Path) -> str:
    """Return the SQ block of a UniProt flat file as one string.

    >>> import tempfile
    >>> p = Path(tempfile.mkdtemp()) / "x.txt"
    >>> _ = p.write_text("ID   X\\nSQ   SEQUENCE   4 AA;\\n     MKHH\\n//\\n")
    >>> read_sequence(p)
    'MKHH'
    """
    seq_lines = []
    in_sq = False
    for line in uniprot_txt.read_text().splitlines():
        if line.startswith("SQ "):
            in_sq = True
            continue
        if line.startswith("//"):
            break
        if in_sq:
            seq_lines.append(line.replace(" ", ""))
    return "".join(seq_lines)


def main() -> None:
    uniprot_txt = Path(sys.argv[1])
    panther_dir = Path(sys.argv[2])
    seq = read_sequence(uniprot_txt)
    print(f"Q9XZ58 length: {len(seq)}")
    for pos, expected in [(135, "H"), (137, "H"), (148, "D")]:
        aa = seq[pos - 1]
        print(f"Residue {pos}: {aa} (expected {expected}) -> {'OK' if aa == expected else 'MISMATCH'}")
    print(f"JAMM motif region 135-148: {seq[134:148]}")
    m = re.search(r"H.H.{7,10}S.{2}D", seq)
    print(f"JAMM consensus HxH...SxxD match: {m.group(0) + ' at ' + str(m.start() + 1) if m else 'none'}")
    print()
    print("PANTHER 19.0 PTHR10410 subfamily placements of CSN5 orthologs and JAMM paralogs:")
    wanted = {"Q9XZ58", "Q92905", "O35864", "P91001", "O94454", "Q12468", "Q54PF3",
              "O00487", "O15372", "P46736", "Q9VCY3", "P43588"}
    for f in sorted(panther_dir.glob("PTHR19.0_*")):
        for line in f.read_text().splitlines():
            cols = line.split("\t")
            if len(cols) > 5 and cols[1] in wanted:
                print(f"  {cols[1]}\t{cols[2]}\t{cols[3]}\t{cols[5]}")


if __name__ == "__main__":
    main()
