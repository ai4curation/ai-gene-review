#!/usr/bin/env python3
"""Fetch a MetaboLights study's curated metabolite ChEBI ids (live, reproducible).

MetaboLights stores per-study metabolite identifications in a Metabolite
Assignment File (MAF, ``m_*.tsv``) inside the public ISA-Tab archive. The
``database_identifier`` column holds the curator-assigned ChEBI id. This script
downloads the MAF(s) for a study accession and writes the distinct ChEBI ids to
``studies/<ACC>.chebi.txt`` (one per line, with a provenance header), ready for
``coverage_probe.py --chebi-file``.

Nothing is hardcoded; the study is pulled live from the EBI FTP mirror.

Usage:
    uv run python fetch_metabolights.py MTBLS1
"""
from __future__ import annotations

import csv
import io
import re
import sys
import urllib.request
from pathlib import Path

FTP = "https://ftp.ebi.ac.uk/pub/databases/metabolights/studies/public"


def _get(url: str, timeout: int = 90) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review-metabolomics/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode(errors="replace")


def list_maf_files(acc: str) -> list[str]:
    listing = _get(f"{FTP}/{acc}/")
    files = re.findall(r'href="([^"]+)"', listing)
    return sorted({f for f in files if f.startswith("m_") and f.endswith(".tsv")})


def study_title(acc: str) -> str:
    try:
        inv = _get(f"{FTP}/{acc}/i_Investigation.txt")
        for line in inv.splitlines():
            if line.startswith("Study Title"):
                parts = line.split("\t", 1)
                if len(parts) == 2:
                    return parts[1].strip().strip('"')
    except Exception:  # noqa: BLE001
        pass
    return ""


def chebi_ids_from_maf(acc: str, maf: str) -> list[tuple[str, str]]:
    text = _get(f"{FTP}/{acc}/{maf}")
    rows = list(csv.DictReader(io.StringIO(text), delimiter="\t"))
    out: list[tuple[str, str]] = []
    for r in rows:
        did = (r.get("database_identifier") or "").strip()
        name = (r.get("metabolite_identification") or "").strip()
        if did.upper().startswith("CHEBI:"):
            out.append((did.upper().replace("CHEBI: ", "CHEBI:"), name))
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    acc = sys.argv[1].strip().upper()
    title = study_title(acc)
    mafs = list_maf_files(acc)
    if not mafs:
        print(f"No MAF files found for {acc}", file=sys.stderr)
        return 1

    seen: dict[str, str] = {}
    for maf in mafs:
        for cid, name in chebi_ids_from_maf(acc, maf):
            seen.setdefault(cid, name)

    out_dir = Path(__file__).parent / "studies"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"{acc}.chebi.txt"
    lines = [
        f"# MetaboLights {acc}",
        f"# title: {title}",
        f"# source: {FTP}/{acc}/ ({', '.join(mafs)})",
        f"# distinct ChEBI metabolite ids: {len(seen)}",
    ]
    for cid, name in sorted(seen.items()):
        lines.append(f"{cid}\t# {name}")
    out_file.write_text("\n".join(lines) + "\n")

    print(f"{acc}: {title}", file=sys.stderr)
    print(f"  MAF(s): {', '.join(mafs)}", file=sys.stderr)
    print(f"  distinct ChEBI ids: {len(seen)} -> {out_file}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
