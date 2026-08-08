"""Shared HTTP + assertion helpers for the AGFG2 analyses.

Every helper here exists because a silent failure in one of these calls has
produced a confident wrong answer elsewhere in this campaign:

* ``uniprot_entry`` asserts ``primaryAccession == requested``, because a merged
  or secondary accession returns HTTP 200 with a *different* protein's record.
* ``is_reviewed`` uses ``startswith("UniProtKB reviewed")`` — the substring test
  ``"reviewed" in entryType`` also matches ``"unreviewed"``.
* ``quickgo`` asserts ``numberOfHits == len(results)``, comparing against the
  actual result length rather than a page-size constant, because the service
  clamps ``limit`` instead of erroring.
* every function raises on a non-200 status, so a rejected query can never be
  read as an empty result.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

UA = {"User-Agent": "ai-gene-review-AGFG2/1.0 (curation analysis)"}

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}


def _get(url: str, tries: int = 4) -> bytes:
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"HTTP {resp.status} for {url}")
                return resp.read()
        except urllib.error.HTTPError as exc:  # noqa: PERF203
            # A rejected query and an empty result look identical downstream,
            # so the status must be surfaced, never swallowed.
            raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"network failure for {url}: {last}")


def get_json(url: str) -> dict:
    return json.loads(_get(url))


def uniprot_entry(acc: str, fields: str | None = None) -> dict:
    """Fetch one UniProtKB entry and assert it is the accession requested."""
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    if fields:
        url += "?" + urllib.parse.urlencode({"fields": fields})
    d = get_json(url)
    got = d.get("primaryAccession")
    if got != acc:
        raise AssertionError(
            f"accession drift: asked for {acc}, server returned {got} "
            f"({d.get('uniProtkbId')}) — a merged/secondary accession returns "
            f"another protein with HTTP 200"
        )
    if not d.get("uniProtkbId"):
        raise AssertionError(f"{acc}: empty entry (inactive/deleted accession?)")
    return d


def is_reviewed(entry: dict) -> bool:
    """Swiss-Prot test that is not defeated by 'reviewed' in 'unreviewed'."""
    return str(entry.get("entryType", "")).startswith("UniProtKB reviewed")


def uniprot_search(query: str, fields: str, size: int = 25) -> list[dict]:
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(
        {"query": query, "fields": fields, "format": "json", "size": size}
    )
    return get_json(url).get("results", [])


def uniprot_search_total(query: str) -> int:
    """Total hit count from UniProt's ``x-total-results`` header.

    A page of results is not a total: reading ``len(results)`` when the server has
    clamped ``size`` turns a truncation into a confident wrong number.  This asks
    the server for the count instead of inferring it from a value we chose.
    """
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(
        {"query": query, "fields": "accession", "format": "json", "size": 1}
    )
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} for {url}")
        total = resp.headers.get("x-total-results")
        if total is None:
            raise RuntimeError(f"no x-total-results header for {url}")
        return int(total)


def quickgo_annotations(**params) -> list[dict]:
    """Fully-paginated QuickGO annotation search with a no-silent-truncation assert."""
    params.setdefault("limit", 100)
    page = 1
    out: list[dict] = []
    total = None
    while True:
        q = dict(params, page=page)
        url = (
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
            + urllib.parse.urlencode(q)
        )
        d = get_json(url)
        if total is None:
            total = d["numberOfHits"]
        out.extend(d["results"])
        pages = d.get("pageInfo") or {}
        if not d["results"] or page >= (pages.get("total") or 1):
            break
        page += 1
    if len(out) != total:
        raise AssertionError(
            f"silent truncation: numberOfHits={total} but collected {len(out)} "
            f"for {params}"
        )
    return out


def quickgo_term(go_id: str) -> dict:
    d = get_json(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete"
    )
    results = d.get("results") or []
    if not results:
        raise AssertionError(f"{go_id}: no term record returned")
    return results[0]


def withfrom_tokens(field: str) -> list[str]:
    """Split a GOA WITH/FROM cell into db:id tokens, preserving the db prefix."""
    if not field or field.strip() == "":
        return []
    return [t for t in field.strip().split("|") if t]
