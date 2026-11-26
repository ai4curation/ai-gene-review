"""Shared helpers: cached downloads and sequence utilities for the AK1 analyses.

Everything is fetched from public services and cached under data/ (git-ignored).
No result is hard-coded: if a fetch fails the calling script reports the failure.
"""
from __future__ import annotations

import json
import pathlib
import re
import time

import requests

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
RESULTS = HERE / "results"
DATA.mkdir(exist_ok=True)
RESULTS.mkdir(exist_ok=True)

UNIPROT = "P00568"
UNIPROT_FLATFILE = HERE.parent / "AK1-uniprot.txt"
HEADERS = {"User-Agent": "ak1-bioinformatics/0.1 (python-requests)"}


def fetch(url: str, name: str, *, post_json: dict | None = None, binary: bool = False,
          retries: int = 3) -> pathlib.Path:
    """Download url to data/name unless already cached; return the path."""
    path = DATA / name
    if path.exists() and path.stat().st_size > 0:
        return path
    last = None
    for attempt in range(retries):
        try:
            if post_json is not None:
                r = requests.post(url, json=post_json, headers=HEADERS, timeout=120)
            else:
                r = requests.get(url, headers=HEADERS, timeout=120)
            if r.status_code == 200:
                if binary:
                    path.write_bytes(r.content)
                else:
                    path.write_text(r.text)
                return path
            last = f"HTTP {r.status_code}"
        except requests.RequestException as exc:  # pragma: no cover - network
            last = repr(exc)
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"could not fetch {url}: {last}")


def uniprot_sequence(flatfile: pathlib.Path = UNIPROT_FLATFILE) -> str:
    """Canonical sequence from the UniProt flat file committed with the review."""
    text = flatfile.read_text()
    block = text.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", block)


def uniprot_features(flatfile: pathlib.Path = UNIPROT_FLATFILE) -> list[dict]:
    """Parse FT lines into dicts: type, start, end, note, ligand."""
    feats: list[dict] = []
    cur = None
    for line in flatfile.read_text().splitlines():
        if not line.startswith("FT   "):
            continue
        m = re.match(r"FT   (\S+)\s+(\d+)(?:\.\.(\d+))?\s*$", line)
        if m:
            cur = {"type": m.group(1), "start": int(m.group(2)),
                   "end": int(m.group(3) or m.group(2)), "qualifiers": ""}
            feats.append(cur)
        elif cur is not None:
            cur["qualifiers"] += line[21:].strip() + " "
    for f in feats:
        q = f["qualifiers"]
        note = re.search(r'/note="([^"]*)"', q)
        lig = re.search(r'/ligand="([^"]*)"', q)
        f["note"] = note.group(1) if note else None
        f["ligand"] = lig.group(1) if lig else None
    return feats


def dump(obj, name: str) -> pathlib.Path:
    path = RESULTS / name
    def default(o):
        if hasattr(o, "item"):  # numpy scalars
            return o.item()
        raise TypeError(type(o).__name__)
    path.write_text(json.dumps(obj, indent=2, sort_keys=False, default=default) + "\n")
    return path


THREE = {"A": "Ala", "R": "Arg", "N": "Asn", "D": "Asp", "C": "Cys", "Q": "Gln", "E": "Glu",
         "G": "Gly", "H": "His", "I": "Ile", "L": "Leu", "K": "Lys", "M": "Met", "F": "Phe",
         "P": "Pro", "S": "Ser", "T": "Thr", "W": "Trp", "Y": "Tyr", "V": "Val", "*": "Ter"}
