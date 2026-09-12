"""Small QuickGO helper with the anti-truncation and status assertions the
campaign brief requires.

Rules encoded here:
  * assert HTTP 200 explicitly - a rejected query and an empty result are
    otherwise indistinguishable downstream (MOD ids return HTTP 400);
  * compare ``numberOfHits`` against ``len(results)`` accumulated over pages,
    never against a page-size constant the caller chose;
  * reassemble ``withFrom`` as ``db:id`` so it can be compared against a GOA
    WITH/FROM string.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://www.ebi.ac.uk/QuickGO/services"
PAGE = 100  # QuickGO's documented maximum for the annotation search


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as fh:
            assert fh.status == 200, f"HTTP {fh.status} for {url}"
            return json.load(fh)
    except urllib.error.HTTPError as exc:  # make a rejected query loud
        raise AssertionError(f"HTTP {exc.code} for {url}: {exc.read()[:300]!r}") from exc


def annotations(**params) -> list[dict]:
    """Fully paginated annotation search. Raises if the server truncates."""
    params.setdefault("limit", PAGE)
    out: list[dict] = []
    page = 1
    total = None
    while True:
        q = urllib.parse.urlencode({**params, "page": page})
        d = _get(f"{BASE}/annotation/search?{q}")
        if total is None:
            total = d["numberOfHits"]
        out.extend(d["results"])
        if not d["results"] or len(out) >= total:
            break
        page += 1
    assert total is not None
    assert len(out) == total, (
        f"truncated: numberOfHits={total} but collected {len(out)} for {params}"
    )
    return out


def count(**params) -> int:
    """numberOfHits for a query, without downloading the hits."""
    q = urllib.parse.urlencode({**params, "limit": 1})
    return _get(f"{BASE}/annotation/search?{q}")["numberOfHits"]


def withfrom_tokens(ann: dict) -> list[str]:
    """Reassemble db:id. Dropping ``db`` turns a resolvable MOD gene id into an
    opaque number, which has caused real mis-readings."""
    out = []
    for group in ann.get("withFrom") or []:
        for c in group.get("connectedXrefs", []):
            out.append(f"{c['db']}:{c['id']}")
    return out


def descendants(go_id: str, relations: str = "is_a,part_of") -> set[str]:
    """Descendant set over the given relations only.

    Regulation edges (`regulates`, `positively_regulates`, ...) deliberately do
    NOT subsume in GO, so they must be excluded from any ancestry claim.
    """
    d = _get(
        f"{BASE}/ontology/go/terms/{go_id}/descendants?relations={relations}"
    )
    res = d["results"][0]
    assert res["id"] == go_id, f"{go_id} resolved to {res['id']}"
    out = set(res.get("descendants") or [])
    assert out, f"no descendants returned for {go_id} - query may have failed"
    return out


def term(go_id: str) -> dict:
    d = _get(f"{BASE}/ontology/go/terms/{go_id}/complete")
    res = d["results"][0]
    assert res["id"] == go_id or go_id in (res.get("secondaryIds") or []), (
        f"{go_id} resolved to {res['id']}"
    )
    return res
