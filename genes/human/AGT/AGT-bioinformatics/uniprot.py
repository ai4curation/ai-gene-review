"""Shared UniProt / QuickGO REST helpers for the AGT analyses.

Everything is fetched live. Nothing is hardcoded. Responses are cached in
`cache/` so re-runs are cheap and reproducible, but the cache is disposable:
delete it and the numbers are re-derived from the APIs.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import requests

CACHE = Path(__file__).parent / "cache"
CACHE.mkdir(exist_ok=True)

UA = {"User-Agent": "ai-gene-review-AGT/1.0 (https://github.com/ai4curation/ai-gene-review)"}


def _cached_get(url: str, key: str, accept: str = "application/json") -> str:
    """GET `url`, caching the raw body under `key`. Raises on HTTP error."""
    path = CACHE / f"{key}.cache"
    if path.exists():
        return path.read_text()
    headers = dict(UA)
    headers["Accept"] = accept
    resp = requests.get(url, headers=headers, timeout=90)
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
    """UniProtKB search. `size` is deliberately >= 2 so ambiguity is visible."""
    key = "search_" + "".join(c if c.isalnum() else "_" for c in query)[:120]
    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query={requests.utils.quote(query)}"
        "&fields=accession,id,protein_name,gene_primary,organism_name,reviewed,xref_merops"
        f"&size={size}"
    )
    return json.loads(_cached_get(url, key))["results"]


def summarise(entry: dict[str, Any]) -> dict[str, Any]:
    """Pull the fields the AGT analyses care about out of a UniProt entry."""
    genes = entry.get("genes") or [{}]
    gene = genes[0].get("geneName", {}).get("value", "")
    desc = entry.get("proteinDescription", {})
    name = (
        desc.get("recommendedName", {}).get("fullName", {}).get("value")
        or (desc.get("submissionNames") or [{}])[0].get("fullName", {}).get("value", "")
    )
    merops = [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "MEROPS"]
    panther = [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"]
    locations: list[str] = []
    for c in entry.get("comments", []):
        if c["commentType"] == "SUBCELLULAR LOCATION":
            for loc in c.get("subcellularLocations", []):
                locations.append(loc["location"]["value"])
    return {
        "accession": entry["primaryAccession"],
        "id": entry.get("uniProtkbId", ""),
        "gene": gene,
        "protein": name,
        "organism": entry.get("organism", {}).get("scientificName", ""),
        "reviewed": entry.get("entryType", "").startswith("UniProtKB reviewed"),
        "length": entry.get("sequence", {}).get("length"),
        "sequence": entry.get("sequence", {}).get("value", ""),
        "merops": merops,
        "panther": panther,
        "locations": locations,
        "keywords": [k["name"] for k in entry.get("keywords", [])],
    }


def resolve_mod_id(token: str) -> list[dict[str, Any]]:
    """Resolve a MOD cross-reference token (MGI:..., RGD:..., FB:..., ZFIN:...,
    AGI_LocusCode:...) to UniProt entries via an xref search.

    Returns ALL hits (size>=5) so that multi-hit ambiguity is reported rather
    than silently collapsed to a confident wrong answer.
    """
    db, _, local = token.partition(":")
    if db == "MGI":
        # GOA writes MGI:MGI:87963. UniProt indexes the bare numeric part, so
        # `xref:mgi-MGI:87963` is a syntax error and `xref:mgi-87963` is correct.
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
    else:
        raise ValueError(f"resolve_mod_id does not handle database {db!r} (token {token!r})")
    return uniprot_search(query, size=5)


def quickgo_term(go_id: str) -> dict[str, Any]:
    body = _cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete",
        f"go_{go_id.replace(':', '_')}",
    )
    return json.loads(body)["results"][0]
