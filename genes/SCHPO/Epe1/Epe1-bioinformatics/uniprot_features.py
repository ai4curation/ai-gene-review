#!/usr/bin/env python3
"""
Read JmjC domain boundaries and Fe(II)-binding residues from UniProt records,
so that no analysis script has to guess them from a sequence motif.

A bare `H.[DE]` regex match does not locate the Fe(II) site: it matches any
His-X-Asp/Glu string (Epe1 has H280-V281-D282, which is not the iron site).
The authoritative positions are the UniProt FT DOMAIN and FT BINDING features.

>>> feats = parse_uniprot_txt("../Epe1-uniprot.txt")
>>> feats["accession"]
'O94603'
>>> feats["jmjc"]
(243, 402)
>>> [(p, feats["sequence"][p - 1]) for p in feats["fe_ligands"]]
[(297, 'H'), (299, 'E')]
>>> feats["caution_positions"]
[(370, 'His', 'Tyr')]
>>> feats["sequence"][370 - 1]
'Y'
"""

import json
import re
from pathlib import Path


def _is_iron(ligand: str) -> bool:
    """True for UniProt Fe(II) ligand names ('Fe cation', 'Fe(2+)').

    >>> _is_iron("Fe cation"), _is_iron("Fe(2+)"), _is_iron("2-oxoglutarate")
    (True, True, False)
    """
    return ligand.startswith("Fe")


def parse_uniprot_txt(path) -> dict:
    """Parse a UniProt flat-file (.txt) record.

    Returns the accession, sequence, JmjC domain (start, end), Fe(II) ligand
    positions, other BINDING positions with their ligand, MUTAGEN records, and
    any CC CAUTION statement of the form 'catalytic His in position N which is
    replaced by a X residue'.
    """
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    accession = next(l.split()[1].rstrip(";") for l in lines if l.startswith("AC   "))

    # Sequence: lines after 'SQ' until '//'
    seq_lines, in_sq = [], False
    for l in lines:
        if l.startswith("SQ   "):
            in_sq = True
            continue
        if in_sq:
            if l.startswith("//"):
                break
            seq_lines.append(l.replace(" ", ""))
    sequence = "".join(seq_lines)

    # Feature table: an FT key line followed by qualifier lines
    features, current = [], None
    for l in lines:
        if not l.startswith("FT   "):
            continue
        key = l[5:21].strip()
        if key:
            loc = l[21:].strip()
            m = re.match(r"(\d+)(?:\.\.(\d+))?", loc)
            start = int(m.group(1))
            end = int(m.group(2)) if m.group(2) else start
            current = {"type": key, "start": start, "end": end, "qualifiers": {}}
            features.append(current)
        else:
            q = re.match(r'\s*/(\w+)="?([^"]*)"?', l[21:])
            if q and current is not None:
                current["qualifiers"][q.group(1)] = q.group(2)

    jmjc = next(
        ((f["start"], f["end"]) for f in features
         if f["type"] == "DOMAIN" and f["qualifiers"].get("note") == "JmjC"),
        None,
    )
    binding = [
        (f["start"], f["qualifiers"].get("ligand", ""))
        for f in features if f["type"] == "BINDING"
    ]
    fe_ligands = [p for p, lig in binding if _is_iron(lig)]
    mutagen = [
        (f["start"], f["qualifiers"].get("note", ""))
        for f in features if f["type"] == "MUTAGEN"
    ]

    # CC CAUTION text can wrap over several lines; join the CC block first.
    cc = " ".join(l[5:].strip() for l in lines if l.startswith("CC   "))
    caution_positions = [
        (int(m.group(2)), m.group(1), m.group(3))
        for m in re.finditer(
            r"catalytic (\w+) in position (\d+) which is replaced by a (\w+) residue", cc
        )
    ]
    return {
        "accession": accession,
        "sequence": sequence,
        "jmjc": jmjc,
        "fe_ligands": fe_ligands,
        "binding": binding,
        "mutagen": mutagen,
        "caution_positions": caution_positions,
    }


def parse_uniprot_json(path) -> dict:
    """Parse a UniProt REST JSON record into the same shape (no CC parsing)."""
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    feats = d.get("features", [])
    jmjc = next(
        ((f["location"]["start"]["value"], f["location"]["end"]["value"])
         for f in feats if f["type"] == "Domain" and f.get("description") == "JmjC"),
        None,
    )
    binding = [
        (f["location"]["start"]["value"], f.get("ligand", {}).get("name", ""))
        for f in feats if f["type"] == "Binding site"
    ]
    return {
        "accession": d["primaryAccession"],
        "entry_name": d.get("uniProtkbId", ""),
        "sequence": d["sequence"]["value"],
        "jmjc": jmjc,
        "fe_ligands": [p for p, lig in binding if _is_iron(lig)],
        "binding": binding,
        "mutagen": [],
        "caution_positions": [],
    }


def ligand_residues(feats: dict) -> list:
    """Fe(II)-ligand positions with the residue found at each, e.g. ['H297', 'E299']."""
    return [f"{feats['sequence'][p - 1]}{p}" for p in feats["fe_ligands"]]
