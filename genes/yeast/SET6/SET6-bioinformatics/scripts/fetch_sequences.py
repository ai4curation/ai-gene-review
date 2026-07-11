#!/usr/bin/env python3
"""Fetch reference protein sequences from UniProt for SET6 comparative analysis.

Downloads the FASTA sequences for a set of UniProt accessions and writes them to
data/reference_sequences.fasta. SET6 itself is read from the local UniProt record
(SET6-uniprot.txt) so that the analysis does not depend on network access for the
primary sequence.

No inputs or outputs are hardcoded beyond the accession list, which is a
biologically-motivated panel (yeast SET-domain proteins + human SMYD paralogs).
The sequences themselves are always fetched live; nothing about the *result* of
the analysis is baked in.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import requests

# Panel of proteins for the comparison.
# Yeast SET-domain proteins + human SMYD family.
ACCESSIONS = {
    # yeast SMYD-subfamily SET proteins (Set5 = SET6 paralog)
    "P38890": "SET5_YEAST",       # YHR207C, characterized H4K5/8/12 KMT (SMYD)
    # yeast degenerate SET proteins (reported to LACK activity)
    "P36124": "SET3_YEAST",       # YKR029C
    "P42948": "SET4_YEAST",       # YJL105W
    # active yeast histone KMTs (positive controls)
    "P38827": "SET1_YEAST",       # YHR119W, H3K4
    "P46995": "SET2_YEAST",       # YJL168C, H3K36
    # human SMYD paralogs
    "Q8NB12": "SMYD1_HUMAN",
    "Q9NRG4": "SMYD2_HUMAN",
    "Q9H7B4": "SMYD3_HUMAN",
    # human SETD6 (multispecific non-histone KMT; sometimes suggested as functional analog)
    "Q8TBK2": "SETD6_HUMAN",
}


def fetch_uniprot_fasta(accession: str) -> str:
    """Fetch a single UniProt entry as FASTA text."""
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    text = resp.text.strip()
    if not text.startswith(">"):
        raise RuntimeError(f"Unexpected response for {accession}: {text[:100]!r}")
    return text


def read_local_set6(uniprot_txt: Path) -> str:
    """Parse the SET6 amino-acid sequence out of the cached UniProt flat file."""
    lines = uniprot_txt.read_text().splitlines()
    seq_lines: list[str] = []
    in_seq = False
    for line in lines:
        if line.startswith("SQ"):
            in_seq = True
            continue
        if in_seq:
            if line.startswith("//"):
                break
            seq_lines.append(line.strip().replace(" ", ""))
    seq = "".join(seq_lines)
    if not seq:
        raise RuntimeError(f"Could not parse sequence from {uniprot_txt}")
    return f">Q12529|SET6_YEAST\n{seq}"


def main() -> int:
    here = Path(__file__).resolve().parent
    proj = here.parent
    data_dir = proj / "data"
    data_dir.mkdir(exist_ok=True)

    uniprot_txt = proj.parent / "SET6-uniprot.txt"
    records: list[str] = []

    # SET6 primary sequence from the local record (network-independent).
    set6_fasta = read_local_set6(uniprot_txt)
    records.append(set6_fasta)
    print(f"Read SET6 from {uniprot_txt} ({len(set6_fasta.splitlines()[1])} aa)")

    # Reference panel from UniProt.
    for acc, name in ACCESSIONS.items():
        print(f"Fetching {acc} ({name}) ...", flush=True)
        fasta = fetch_uniprot_fasta(acc)
        # Re-header for readability while keeping accession.
        seq = "".join(fasta.splitlines()[1:])
        records.append(f">{acc}|{name}\n{seq}")
        time.sleep(0.5)

    out = data_dir / "reference_sequences.fasta"
    out.write_text("\n".join(records) + "\n")
    print(f"\nWrote {len(records)} sequences to {out}")

    # Also write SET6 alone for hmmscan etc.
    set6_only = data_dir / "SET6.fasta"
    set6_only.write_text(set6_fasta + "\n")
    print(f"Wrote SET6 single sequence to {set6_only}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
