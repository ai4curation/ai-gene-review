#!/usr/bin/env python3
"""Compare the domain architecture of fly Drp1 with classical dynamins.

Question: the PAINT microtubule-binding IBD that fly Drp1 inherits sits at the
PTHR11566 root and is seeded by fly shibire (classical dynamin). Classical
dynamins carry a PH domain and a C-terminal proline-rich domain (PRD) that
DRP1-type proteins lack. This script checks, for each protein, which Pfam
domains InterPro reports and how proline-rich the C-terminal stretch after the
last Pfam domain is.

Inputs are fetched live (stdlib only):
  * Pfam matches: https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/<ACC>
  * Sequence:     https://rest.uniprot.org/uniprotkb/<ACC>.fasta

Usage:
  python domain_architecture.py Q9VQE0 P27619 O00429 Q05193
Prints a table; nothing is hard-coded about the result.
"""
from __future__ import annotations

import json
import subprocess
import sys

PFAM_URL = "https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/{acc}"
FASTA_URL = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"


def get(url: str) -> str:
    # curl honours the environment's proxy and CA settings
    return subprocess.run(["curl", "-sS", "-L", url], capture_output=True, text=True, check=True).stdout


def pfam(acc: str) -> list[tuple[int, int, str, str]]:
    data = json.loads(get(PFAM_URL.format(acc=acc)))
    out = []
    for r in data.get("results", []):
        m = r["metadata"]
        for p in r["proteins"]:
            for loc in p["entry_protein_locations"]:
                for f in loc["fragments"]:
                    out.append((f["start"], f["end"], m["accession"], m["name"]))
    return sorted(out)


def sequence(acc: str) -> tuple[str, str]:
    lines = get(FASTA_URL.format(acc=acc)).splitlines()
    return lines[0], "".join(lines[1:])


def main(accs: list[str]) -> None:
    print("accession\tlength\tpfam_domains\tPH_domain(PF00169)\tC-term_after_last_domain\tPro_fraction_C-term")
    for acc in accs:
        header, seq = sequence(acc)
        doms = pfam(acc)
        last_end = max(e for _, e, _, _ in doms) if doms else 0
        tail = seq[last_end:]
        pro = tail.count("P") / len(tail) if tail else 0.0
        dom_txt = "; ".join(f"{a} {n} {s}-{e}" for s, e, a, n in doms)
        has_ph = any(a == "PF00169" for _, _, a, _ in doms)
        print(f"{acc}\t{len(seq)}\t{dom_txt}\t{has_ph}\t{len(tail)} aa\t{pro:.2f}")
        print(f"#   {header}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["Q9VQE0", "P27619", "O00429", "Q05193"])
