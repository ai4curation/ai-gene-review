"""Identity between the ANME-2d McrA reviewed here and the McrA of the strain whose MCR
structure was solved.

A0A284VQI9 (Ca. Methanoperedens nitratireducens, cached UniProt file) is compared with
RefSeq WP_097300250.1, the McrA of 'Ca. Methanoperedens sp.' BLZ2 named in PMID:40913044.
The BLZ2 protein maps only to deleted UniProt entries, so it is fetched from NCBI at run
time. Same aligner settings as compare_active_sites.py. Prints the result; nothing is
hard-coded.
"""
from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compare_active_sites import ROOT, map_positions, read_uniprot  # noqa: E402

REFSEQ = "WP_097300250.1"
URL = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id={REFSEQ}&rettype=fasta"


def main() -> None:
    fasta = urllib.request.urlopen(URL, timeout=60).read().decode()
    header, *lines = fasta.strip().splitlines()
    blz2 = "".join(lines)
    acc, seq, _ = read_uniprot(ROOT / "genes/9EURY/mcrA__A0A284VQI9/mcrA__A0A284VQI9-uniprot.txt")
    _, pid = map_positions(seq, blz2)
    print(f"{acc} ({len(seq)} aa) vs {header[1:80]} ({len(blz2)} aa): identity {pid:.1f}% over aligned positions")


if __name__ == "__main__":
    main()
