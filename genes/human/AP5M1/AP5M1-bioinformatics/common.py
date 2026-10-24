"""Shared fetch helpers for the AP5M1 bioinformatics checks.

Everything is fetched live from UniProt / RCSB and cached under ``cache/``
(disposable).  No result is hardcoded.
"""

from __future__ import annotations

import pathlib
import re

import requests

CACHE = pathlib.Path(__file__).parent / "cache"
CACHE.mkdir(exist_ok=True)


def _get(url: str, name: str) -> str:
    path = CACHE / name
    if path.exists():
        return path.read_text()
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    path.write_text(resp.text)
    return resp.text


def uniprot_txt(accession: str) -> str:
    return _get(f"https://rest.uniprot.org/uniprotkb/{accession}.txt", f"{accession}.txt")


def uniprot_record(accession: str) -> dict:
    """Return accession, id, sequence, length and sequence version from the flat file."""
    text = uniprot_txt(accession)
    ac_line = next(l for l in text.splitlines() if l.startswith("AC   "))
    primary = ac_line[5:].split(";")[0].strip()
    if primary != accession:
        raise RuntimeError(f"requested {accession} but record's primary accession is {primary}")
    id_line = next(l for l in text.splitlines() if l.startswith("ID   "))
    entry_name = id_line.split()[1]
    # "DT   03-OCT-2003, sequence version 2."
    sv = None
    for line in text.splitlines():
        m = re.search(r"sequence version (\d+)", line)
        if m:
            sv = int(m.group(1))
    seq_lines = []
    in_seq = False
    for line in text.splitlines():
        if line.startswith("SQ   "):
            in_seq = True
            declared_len = int(re.search(r"SEQUENCE\s+(\d+) AA", line).group(1))
            continue
        if line.startswith("//"):
            in_seq = False
            continue
        if in_seq:
            seq_lines.append(line.replace(" ", ""))
    seq = "".join(seq_lines)
    if len(seq) != declared_len:
        raise RuntimeError(f"{accession}: parsed {len(seq)} aa but SQ line declares {declared_len}")
    gene = ""
    for line in text.splitlines():
        if line.startswith("GN   Name="):
            gene = line.split("Name=")[1].split(";")[0].split("{")[0].strip()
            break
    organism = next(l[5:].strip().rstrip(".") for l in text.splitlines() if l.startswith("OS   "))
    return {
        "accession": accession,
        "entry_name": entry_name,
        "gene": gene,
        "organism": organism,
        "sequence": seq,
        "length": len(seq),
        "sequence_version": sv,
    }


def rcsb_cif(pdb_id: str) -> str:
    return _get(f"https://files.rcsb.org/download/{pdb_id.upper()}.cif", f"{pdb_id.upper()}.cif")
