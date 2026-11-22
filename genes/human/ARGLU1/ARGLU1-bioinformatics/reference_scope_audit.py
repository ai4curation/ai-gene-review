#!/usr/bin/env python3
"""Measure how many gene products each reference cited on ARGLU1 annotates.

A reference that assigns the same GO term to hundreds of gene products with
identical evidence is reporting a *screen*, not N independent findings about N
proteins. This is the projection/promiscuity discriminator described in the
campaign brief, applied to the references behind ARGLU1's interaction-derived
rows:

* ``PMID:25468996`` -> ``GO:0045296`` cadherin binding  (E-cadherin BioID)
* ``PMID:33961781`` -> ``GO:0005515`` protein binding   (BioPlex 3.0 AP-MS)
* ``PMID:22365833`` -> ``GO:0005515``                   (spliceosome PPI map)
* ``PMID:23602568`` -> ``GO:0005515``                   (CMGC kinase interactome)
* ``PMID:39251607`` -> ``GO:0005515``                   (post-transcriptional modules)
* ``PMID:30698747`` -> ``GO:0005515``                   (ARGLU1 primary paper; control)

Two numbers are reported per (reference, term) pair and they are NOT the same
thing: ``numberOfHits`` counts *annotations*, while the entity count is the size
of the distinct ``geneProductId`` set. Conflating them inflates the projection
signal. Where the result set is too large to enumerate, the entity count is
reported as unavailable rather than estimated from one page.

Run:  uv run python reference_scope_audit.py
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# (reference, go_id, short label for the reference)
PAIRS = [
    ("PMID:25468996", "GO:0045296", "E-cadherin proximity biotinylation (BioID)"),
    ("PMID:33961781", "GO:0005515", "BioPlex 3.0 AP-MS interactome"),
    ("PMID:22365833", "GO:0005515", "human spliceosome PPI wiring"),
    ("PMID:23602568", "GO:0005515", "CMGC kinase-group interactome"),
    ("PMID:39251607", "GO:0005515", "post-transcriptional regulatory modules"),
    ("PMID:30698747", "GO:0005515", "ARGLU1 primary paper (control)"),
]

# Enumerating beyond this many annotations costs more pages than the answer is
# worth; past it we report the entity count as unavailable rather than guessing.
MAX_ENUMERATE = 2000


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError(f"unreachable: {url}")


def count_only(params: dict) -> int:
    qs = urllib.parse.urlencode({**params, "limit": 1, "page": 1})
    return _get(f"{QUICKGO}?{qs}")["numberOfHits"]


def enumerate_rows(params: dict, expected: int, page_size: int = 100) -> list[dict]:
    rows: list[dict] = []
    page = 1
    while True:
        qs = urllib.parse.urlencode({**params, "limit": page_size, "page": page})
        data = _get(f"{QUICKGO}?{qs}")
        rows.extend(data["results"])
        if not data["results"] or len(rows) >= data["numberOfHits"]:
            break
        page += 1
        if page > 100:
            raise RuntimeError("pagination runaway")
        time.sleep(0.2)
    # Anti-truncation guard: compare against the server's own total, never against
    # the page size we chose -- QuickGO clamps the per-page limit silently.
    if len(rows) != expected:
        raise RuntimeError(
            f"truncated fetch for {params!r}: numberOfHits={expected}, got {len(rows)}"
        )
    return rows


def audit(reference: str, go_id: str, label: str) -> dict:
    base = {"reference": reference, "goId": go_id,
            "goUsage": "descendants", "goUsageRelationships": "is_a,part_of"}
    n_ann = count_only(base)
    rec: dict = {
        "reference": reference,
        "go_id": go_id,
        "reference_label": label,
        "annotations": n_ann,
    }
    if n_ann > MAX_ENUMERATE:
        rec["entities"] = None
        rec["entities_note"] = (
            f"not enumerated: {n_ann} annotations exceeds the {MAX_ENUMERATE} cap; "
            "entity count unavailable rather than estimated from one page"
        )
        rec["evidence_codes"] = None
        return rec
    rows = enumerate_rows(base, n_ann)
    rec["entities"] = len({r["geneProductId"] for r in rows})
    rec["evidence_codes"] = dict(Counter(r["goEvidence"] for r in rows))
    rec["assigned_by"] = dict(Counter(r["assignedBy"] for r in rows))
    rec["human_entities"] = len({r["geneProductId"] for r in rows
                                 if r.get("taxonId") == 9606})
    return rec


def main() -> int:
    out = []
    for reference, go_id, label in PAIRS:
        rec = audit(reference, go_id, label)
        out.append(rec)
        ents = rec["entities"]
        ent_s = str(ents) if ents is not None else "unavailable"
        print(f"{reference} -> {go_id}  [{label}]")
        print(f"    annotations={rec['annotations']}  distinct gene products={ent_s}")
        if rec.get("evidence_codes"):
            print(f"    evidence={rec['evidence_codes']}  assignedBy={rec['assigned_by']}")
        if rec.get("entities_note"):
            print(f"    NOTE: {rec['entities_note']}")
        time.sleep(0.2)

    here = Path(__file__).resolve().parent
    (here / "reference_scope.json").write_text(json.dumps(out, indent=2, sort_keys=True))
    print(f"\nwrote {here / 'reference_scope.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
