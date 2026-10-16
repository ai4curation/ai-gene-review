"""Shared UniProt / QuickGO REST helpers for the ARFGEF2 analyses.

Everything is fetched live. Nothing is hardcoded. Responses are cached in
`cache/` so re-runs are cheap and reproducible, but the cache is disposable:
delete it and the numbers are re-derived from the APIs.

Adapted from `genes/human/AGT/AGT-bioinformatics/uniprot.py`.
"""

from __future__ import annotations

import json
import time
import urllib.parse
from pathlib import Path
from typing import Any

import requests

CACHE = Path(__file__).parent / "cache"
CACHE.mkdir(exist_ok=True)

UA = {"User-Agent": "ai-gene-review-ARFGEF2/1.0 (https://github.com/ai4curation/ai-gene-review)"}

# Experimental GO evidence codes (GO consortium definition).
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def _cached_get(url: str, key: str, accept: str = "application/json") -> str:
    """GET `url`, caching the raw body under `key`. Raises on HTTP error."""
    path = CACHE / f"{key}.cache"
    if path.exists():
        return path.read_text()
    headers = dict(UA)
    headers["Accept"] = accept
    resp = requests.get(url, headers=headers, timeout=120)
    resp.raise_for_status()
    path.write_text(resp.text)
    time.sleep(0.2)
    return resp.text


def uniprot_entry(acc: str) -> dict[str, Any]:
    """Full UniProtKB JSON entry for one accession (isoform suffix stripped)."""
    base = acc.split("-")[0]
    body = _cached_get(f"https://rest.uniprot.org/uniprotkb/{base}.json", f"up_{base}")
    return json.loads(body)


def uniprot_search(query: str, size: int = 10) -> list[dict[str, Any]]:
    """UniProtKB search. `size` is deliberately >= 2 so ambiguity is visible.

    A `size=1` query silently converts an ambiguous cross-reference into a
    confident wrong answer; callers must handle multi-hit results explicitly.
    """
    key = "search_" + "".join(c if c.isalnum() else "_" for c in query)[:120]
    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query={urllib.parse.quote(query)}"
        "&fields=accession,id,protein_name,gene_primary,organism_name,reviewed,length"
        f"&size={size}"
    )
    return json.loads(_cached_get(url, key))["results"]


def summarise(entry: dict[str, Any]) -> dict[str, Any]:
    """Pull the fields the ARFGEF2 analyses care about out of a UniProt entry.

    `reviewed` tests `startswith("UniProtKB reviewed")`, NOT `"reviewed" in ...`,
    because "reviewed" is a substring of "unreviewed" and the naive test silently
    promotes every TrEMBL entry to Swiss-Prot.
    """
    entry_type = entry.get("entryType", "")
    if entry_type not in {"UniProtKB reviewed (Swiss-Prot)", "UniProtKB unreviewed (TrEMBL)"}:
        raise ValueError(f"unexpected entryType {entry_type!r} for {entry.get('primaryAccession')}")
    genes = entry.get("genes") or [{}]
    gene = genes[0].get("geneName", {}).get("value", "")
    desc = entry.get("proteinDescription", {})
    name = (
        desc.get("recommendedName", {}).get("fullName", {}).get("value")
        or (desc.get("submissionNames") or [{}])[0].get("fullName", {}).get("value", "")
    )
    return {
        "accession": entry["primaryAccession"],
        "id": entry.get("uniProtkbId", ""),
        "gene": gene,
        "protein": name,
        "organism": entry.get("organism", {}).get("scientificName", ""),
        "reviewed": entry_type.startswith("UniProtKB reviewed"),
        "length": entry.get("sequence", {}).get("length"),
    }


def resolve_mod_id(token: str) -> list[dict[str, Any]]:
    """Resolve a MOD cross-reference token to UniProt entries via an xref search.

    Returns ALL hits (size>=5) so multi-hit ambiguity is reported rather than
    silently collapsed.
    """
    db, _, local = token.partition(":")
    if db == "MGI":
        # GOA writes MGI:MGI:87963. UniProt indexes the bare numeric part; a
        # query containing the inner colon returns HTTP 400.
        local = token.rsplit(":", 1)[1]
        query = f"xref:mgi-{local}"
    elif db == "RGD":
        query = f"xref:rgd-{local}"
    elif db == "FB":
        query = f"xref:flybase-{local}"
    elif db == "ZFIN":
        query = f"xref:zfin-{local}"
    elif db == "AGI_LocusCode":
        query = f"xref:araport-{local}"
    elif db == "SGD":
        query = f"xref:sgd-{local}"
    elif db == "PomBase":
        query = f"xref:pombase-{local}"
    else:
        raise ValueError(f"resolve_mod_id does not handle database {db!r} (token {token!r})")
    return uniprot_search(query, size=5)


def quickgo_term(go_id: str) -> dict[str, Any]:
    """QuickGO's `complete` term record. Reports `isObsolete` and `secondaryIds`,
    which is how a MERGED id is distinguished from an absent one."""
    body = _cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete",
        f"go_{go_id.replace(':', '_')}",
    )
    return json.loads(body)["results"][0]


MAX_PAGES = 25  # QuickGO's own pagination ceiling for the annotation search.


def _quickgo_paged(params: str, key: str, limit: int = 100) -> dict[str, Any]:
    """Page through a QuickGO annotation search.

    Returns `{"complete": bool, "total": int, "rows": [...]}`. `complete` is
    computed by comparing `numberOfHits` to `len(rows)` - never to a page-size
    constant, because if the service clamps `limit` instead of erroring, a
    constant-based guard passes while rows were silently dropped.

    A result set larger than the service will paginate is **data, not a missing
    input**: the caller must report "unavailable" rather than deriving a number
    from a partial page. Substituting an annotation total for an entity count,
    or a page total for a whole, is the failure this return shape prevents.
    """
    rows: list[dict[str, Any]] = []
    page = 1
    total = 0
    while True:
        body = _cached_get(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
            f"?{params}&limit={limit}&page={page}",
            f"{key}_p{page}",
        )
        d = json.loads(body)
        total = d["numberOfHits"]
        rows.extend(d["results"])
        if len(rows) >= total or not d["results"]:
            break
        page += 1
        if page > MAX_PAGES:
            break
    return {"complete": len(rows) == total, "total": total, "rows": rows}


def quickgo_by_gene(acc: str) -> list[dict[str, Any]]:
    """All GO annotations for one gene product accession.

    A gene's own annotation set is always small enough to page fully, so an
    incomplete result here is a real error and is raised.
    """
    res = _quickgo_paged(f"geneProductId=UniProtKB:{acc}", f"qg_gene_{acc}")
    if not res["complete"]:
        raise RuntimeError(
            f"QuickGO returned {len(res['rows'])} of {res['total']} annotations for "
            f"{acc}; a single gene product should page fully."
        )
    return res["rows"]


def quickgo_by_reference(pmid: str) -> dict[str, Any]:
    """All GO annotations (any species, any gene) citing one PMID.

    This is the projection discriminator: a reference that annotates a complex
    plus every one of its subunits with identical evidence is a projection, not
    N independent findings. Returns the `_quickgo_paged` envelope so callers can
    see whether the set was collected completely.
    """
    return _quickgo_paged(f"reference=PMID:{pmid}", f"qg_ref_{pmid}")


def quickgo_by_gene_and_reference(acc: str, pmid: str) -> list[dict[str, Any]]:
    """Annotations on ONE gene product from ONE reference.

    Exact even when the reference as a whole is too large to page (BioPlex-scale
    screens), so "how many rows did this paper put on this gene" stays answerable
    when "how many entities does this paper annotate" does not.
    """
    res = _quickgo_paged(
        f"geneProductId=UniProtKB:{acc}&reference=PMID:{pmid}", f"qg_gr_{acc}_{pmid}"
    )
    if not res["complete"]:
        raise RuntimeError(
            f"QuickGO returned {len(res['rows'])} of {res['total']} for {acc} x PMID:{pmid}"
        )
    return res["rows"]
