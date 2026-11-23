"""Count QuickGO annotation rows per apoptosis step term and species.

Prints a tab-separated matrix of `experimental/total` annotation ROW counts
(not gene counts) for each step term, including is_a/part_of/occurs_in
descendants, plus an exact-term row for GO:0006915.

The exact GO:0006915 row is the positive control: its totals should match the
snapshot in GO0006915.md (825 human, 557 mouse, 253 zebrafish on 2026-09-30).
A matrix of clean zeros means the query is broken, not that GO is empty.

Usage, from the repository root:

    uv run projects/APOPTOSIS/step_coverage.py
"""

from __future__ import annotations

import json
import os
import ssl
import time
import urllib.parse
import urllib.request

API = "https://www.ebi.ac.uk/QuickGO/services/annotation/search?"

STEP_TERMS = [
    ("GO:0006915", "apoptotic process"),
    ("GO:0097193", "intrinsic apoptotic signaling pathway"),
    ("GO:0097191", "extrinsic apoptotic signaling pathway"),
    ("GO:0071550", "death-inducing signaling complex assembly"),
    ("GO:0097345", "mitochondrial outer membrane permeabilization"),
    ("GO:0001836", "release of cytochrome c from mitochondria"),
    ("GO:0097314", "apoptosome assembly"),
    ("GO:0097194", "execution phase of apoptosis"),
    ("GO:0006309", "apoptotic DNA fragmentation"),
    ("GO:0070782", "phosphatidylserine exposure on apoptotic cell surface"),
    ("GO:0043277", "apoptotic cell clearance"),
]

TAXA = [
    ("9606", "human"),
    ("10090", "mouse"),
    ("10116", "rat"),
    ("7955", "zebrafish"),
    ("8364", "X. tropicalis"),
    ("7227", "D. melanogaster"),
    ("6239", "C. elegans"),
    ("559292", "S. cerevisiae"),
    ("284812", "S. pombe"),
    ("44689", "D. discoideum"),
    ("3702", "A. thaliana"),
]


def _context() -> ssl.SSLContext:
    cafile = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    return ssl.create_default_context(cafile=cafile)


def hits(go_id: str, taxon: str, experimental: bool = False, exact: bool = False) -> int:
    """Return QuickGO's numberOfHits for one term, taxon and evidence filter."""
    params = {
        "goId": go_id,
        "goUsage": "exact" if exact else "descendants",
        "goUsageRelationships": "is_a,part_of,occurs_in",
        "taxonId": taxon,
        "limit": 1,
    }
    if experimental:
        params.update({"evidenceCode": "ECO:0000269", "evidenceCodeUsage": "descendants"})
    request = urllib.request.Request(
        API + urllib.parse.urlencode(params), headers={"Accept": "application/json"}
    )
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60, context=_context()) as response:
                return int(json.load(response)["numberOfHits"])
        except Exception as error:  # retried; re-raised below
            last_error = error
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"QuickGO query failed for {go_id} in taxon {taxon}") from last_error


def main() -> None:
    print("term\tlabel\t" + "\t".join(name for _, name in TAXA))
    for go_id, label in STEP_TERMS:
        cells = [f"{hits(go_id, t, True)}/{hits(go_id, t)}" for t, _ in TAXA]
        print(f"{go_id}\t{label}\t" + "\t".join(cells), flush=True)
    cells = [
        f"{hits('GO:0006915', t, True, True)}/{hits('GO:0006915', t, False, True)}"
        for t, _ in TAXA
    ]
    print("GO:0006915\tapoptotic process (exact term only)\t" + "\t".join(cells))


if __name__ == "__main__":
    main()
