#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
uniprot_record="${1:-${script_dir}/../bma-dpy-18.2-uniprot.txt}"

tmpdir="$(mktemp -d)"
trap 'rm -rf "${tmpdir}"' EXIT

curl -fsSL \
  'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ297845.1,AJ421993.1&rettype=gb&retmode=text' \
  > "${tmpdir}/phy1-genbank.gb"

python3 - "${uniprot_record}" "${tmpdir}/phy1-genbank.gb" <<'PY'
import re
import sys


def uniprot_sequence(path):
    in_sequence = False
    chunks = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("SQ   "):
                in_sequence = True
                continue
            if in_sequence and line.startswith("//"):
                break
            if in_sequence:
                chunks.append(re.sub(r"[^A-Za-z]", "", line))
    return "".join(chunks).upper()


def genbank_translations(path):
    with open(path, encoding="utf-8") as handle:
        records = handle.read().split("\n//")

    translations = {}
    for record in records:
        accession = re.search(r"^ACCESSION\s+(\S+)", record, re.MULTILINE)
        version = re.search(r"^VERSION\s+(\S+)", record, re.MULTILINE)
        translation = re.search(r'/translation="([^"]+)"', record, re.DOTALL)
        if not (accession and version and translation):
            continue
        sequence = re.sub(r"\s+", "", translation.group(1)).upper()
        translations[version.group(1)] = sequence
    return translations


uniprot = uniprot_sequence(sys.argv[1])
translations = genbank_translations(sys.argv[2])

print(f"A0A1P6BZ71 length: {len(uniprot)} aa")
for accession in ("AJ297845.1", "AJ421993.1"):
    sequence = translations[accession]
    matches = sum(left == right for left, right in zip(uniprot, sequence))
    print(
        f"{accession} CDS translation length: {len(sequence)} aa; "
        f"identity to A0A1P6BZ71: {matches}/{len(uniprot)} ({matches / len(uniprot):.1%})"
    )
    if sequence != uniprot:
        raise SystemExit(f"{accession} does not match A0A1P6BZ71")
PY
