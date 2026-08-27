#!/usr/bin/env python3
"""Fetch the raw spondylometaphyseal dysplasia (SMD) landscape used by this project.

Three public sources are queried and joined into a single TSV:

1. **MONDO** (EBI OLS4) -- every ``hierarchicalDescendants`` of
   ``MONDO:0016763`` (spondylometaphyseal dysplasia), i.e. what MONDO itself
   considers an SMD.
2. **Monarch** (``api.monarchinitiative.org`` v3) -- the causal gene(s) asserted
   for each of those diseases, plus the OMIM/Orphanet cross-references.
3. **MedGen** (NCBI E-utilities) -- the OMIM entry title for each cross-referenced
   MIM number, so the OMIM naming can be compared against the MONDO label.

The output is deliberately *raw*: it records what the sources say, not what this
project concluded. The curated nosology-group assignments live in
``smd-nosology-classification.tsv`` and are authored, not derived, because
assigning an ISDS group is a judgement call (see ``curation-notes.md``).

The ISDS 2023 nosology table itself is **not** downloaded or redistributed here.
It is published open access by the International Skeletal Dysplasia Society at
https://www.isds.ch/ (Unger et al. 2023, PMID:36779427); individual facts taken
from it (NOS identifier, gene, inheritance, MIM number) are cited in the curated
table.

Usage::

    python3 fetch_smd_landscape.py                # writes smd-landscape.tsv
    python3 fetch_smd_landscape.py --out other.tsv

Stdlib only -- no third-party dependencies.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

OLS = "https://www.ebi.ac.uk/ols4/api"
MONARCH = "https://api.monarchinitiative.org/v3/api"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

#: Root of the MONDO subtree that defines "what MONDO calls an SMD".
SMD_ROOT = "MONDO:0016763"

#: Disorders the ISDS nosology places in or next to group 12 that are *not*
#: reachable from ``SMD_ROOT`` in MONDO. Fetched explicitly so the gaps between
#: MONDO's classification and the nosology are visible in the same table.
EXTRA_DISEASES = [
    "MONDO:0030074",  # SMD with corneal dystrophy (PLCB3) -- NOS 12-0050
    "MONDO:0010814",  # chondrodysplasia-pseudohermaphroditism (HHAT) -- NOS 12-0060
]


def _get(url: str, retries: int = 5) -> dict:
    """GET a JSON document, retrying with linear backoff on transient errors."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    last: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last}")


def mondo_descendants(root: str) -> list[tuple[str, str]]:
    """Return ``(curie, label)`` for every hierarchical descendant of *root*."""
    purl = f"http://purl.obolibrary.org/obo/{root.replace(':', '_')}"
    double_quoted = urllib.parse.quote(urllib.parse.quote(purl, safe=""), safe="")
    url = f"{OLS}/ontologies/mondo/terms/{double_quoted}/hierarchicalDescendants?size=500"
    payload = _get(url)
    terms = payload.get("_embedded", {}).get("terms", [])
    return sorted((t["obo_id"], t["label"]) for t in terms if not t.get("is_obsolete"))


def disease_record(curie: str) -> dict:
    """Return label, xrefs and Monarch-asserted causal genes for one disease."""
    entity = _get(f"{MONARCH}/entity/{curie}")
    # In Monarch's association model the gene is the subject and the disease the
    # object, so a causal-gene query is anchored on ``object=``.
    assoc = _get(
        f"{MONARCH}/association?object={curie}"
        "&category=biolink:CausalGeneToDiseaseAssociation&limit=100"
    )
    genes = sorted({i["subject_label"] for i in assoc["items"] if i.get("subject_label")})
    xrefs = [x for x in (entity.get("xref") or []) if x.split(":")[0] in {"OMIM", "OMIMPS", "Orphanet"}]
    return {
        "curie": curie,
        "label": entity.get("name") or "",
        "genes": genes,
        "omim": [x for x in xrefs if x.startswith("OMIM:")],
        "omim_ps": [x for x in xrefs if x.startswith("OMIMPS:")],
        "orphanet": [x for x in xrefs if x.startswith("Orphanet:")],
    }


def omim_title(mim: str) -> str:
    """Return the MedGen-recorded title for an OMIM MIM number (may be empty)."""
    search = _get(
        f"{EUTILS}/esearch.fcgi?db=medgen&retmode=json&retmax=5&"
        + urllib.parse.urlencode({"term": f"{mim}[MIM]"})
    )
    uids = search["esearchresult"]["idlist"]
    time.sleep(0.4)
    if not uids:
        return ""
    summary = _get(f"{EUTILS}/esummary.fcgi?db=medgen&retmode=json&id={','.join(uids)}")
    titles = [summary["result"][u].get("title", "") for u in summary["result"]["uids"]]
    time.sleep(0.4)
    return " | ".join(t for t in titles if t)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).with_name("smd-landscape.tsv"),
        help="output TSV path (default: smd-landscape.tsv beside this script)",
    )
    args = parser.parse_args(argv)

    curies = [c for c, _ in mondo_descendants(SMD_ROOT)]
    in_subtree = set(curies)
    curies += [c for c in EXTRA_DISEASES if c not in in_subtree]
    print(f"{len(in_subtree)} MONDO descendants of {SMD_ROOT}", file=sys.stderr)

    rows = []
    for curie in curies:
        rec = disease_record(curie)
        titles = [omim_title(x.split(":")[1]) for x in rec["omim"]]
        rows.append(
            {
                "mondo_id": curie,
                "mondo_label": rec["label"],
                "in_mondo_smd_subtree": "yes" if curie in in_subtree else "no",
                "monarch_causal_genes": ",".join(rec["genes"]),
                "omim_ids": ",".join(rec["omim"]),
                "omim_titles": " || ".join(t for t in titles if t),
                "omim_phenotypic_series": ",".join(rec["omim_ps"]),
                "orphanet_ids": ",".join(rec["orphanet"]),
            }
        )
        print(f"  {curie}\t{rec['label']}", file=sys.stderr)
        time.sleep(0.2)

    fields = list(rows[0]) if rows else []
    with args.out.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(fields) + "\n")
        for row in rows:
            fh.write("\t".join(row[f] for f in fields) + "\n")
    print(f"wrote {len(rows)} rows to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
