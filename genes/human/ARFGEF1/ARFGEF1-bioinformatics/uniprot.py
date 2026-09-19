"""Shared UniProt / QuickGO REST helpers for the ARFGEF1 analyses.

Everything is fetched live. Nothing is hardcoded. Responses are cached in
`cache/` so re-runs are cheap and reproducible, but the cache is disposable:
delete it and the numbers are re-derived from the APIs.

Adapted from `genes/human/AGT/AGT-bioinformatics/uniprot.py`, extended with the
MOD databases that appear in ARFGEF1's WITH/FROM column (PomBase, SGD,
WormBase, dictyBase) and with a QuickGO annotation-search helper.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import requests

CACHE = Path(__file__).parent / "cache"
CACHE.mkdir(exist_ok=True)

UA = {"User-Agent": "ai-gene-review-ARFGEF1/1.0 (https://github.com/ai4curation/ai-gene-review)"}


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
    """UniProtKB search. `size` is deliberately >= 2 so ambiguity is visible.

    A `size=1` query converts an ambiguous cross-reference into a confident
    wrong answer; callers must handle multi-hit results explicitly.
    """
    key = "search_" + "".join(c if c.isalnum() else "_" for c in query)[:120]
    url = (
        "https://rest.uniprot.org/uniprotkb/search"
        f"?query={requests.utils.quote(query)}"
        "&fields=accession,id,protein_name,gene_primary,organism_name,reviewed"
        f"&size={size}"
    )
    return json.loads(_cached_get(url, key))["results"]


def summarise(entry: dict[str, Any]) -> dict[str, Any]:
    """Pull the fields the ARFGEF1 analyses care about out of a UniProt entry.

    `reviewed` tests `startswith("UniProtKB reviewed")`: a bare
    `"reviewed" in entryType` test also matches `"unreviewed"` and silently
    promotes every TrEMBL entry to Swiss-Prot.
    """
    genes = entry.get("genes") or [{}]
    gene = genes[0].get("geneName", {}).get("value", "")
    desc = entry.get("proteinDescription", {})
    name = (
        desc.get("recommendedName", {}).get("fullName", {}).get("value")
        or (desc.get("submissionNames") or [{}])[0].get("fullName", {}).get("value", "")
    )
    panther = [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"]
    interpro = [x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "InterPro"]
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
        "panther": panther,
        "interpro": interpro,
        "locations": locations,
        "keywords": [k["name"] for k in entry.get("keywords", [])],
    }


# UniProt `xref:` index names, keyed by the database prefix GOA writes.
_XREF_DB = {
    "MGI": "mgi",
    "RGD": "rgd",
    "FB": "flybase",
    "ZFIN": "zfin",
    "AGI_LocusCode": "araport",
    "SGD": "sgd",
    "PomBase": "pombase",
    "dictyBase": "dictybase",
}


def resolve_mod_id(token: str) -> tuple[list[dict[str, Any]], str]:
    """Resolve a MOD cross-reference token to UniProt entries via an xref search.

    Returns `(hits, how)` where `how` names the query strategy actually used, so
    that a fallback is reported rather than hidden. ALL hits are returned
    (size>=5) so multi-hit ambiguity is visible instead of silently collapsed.
    """
    db, _, local = token.partition(":")
    if db == "MGI":
        # GOA writes MGI:MGI:87963. UniProt indexes the bare numeric part, so
        # `xref:mgi-MGI:87963` is an HTTP 400 and `xref:mgi-87963` is correct.
        local = token.rsplit(":", 1)[1]
    if db == "WB":
        # WormBase *gene* ids (WBGene...) are absent from UniProt's
        # `xref:wormbase` index, which holds protein ids. Free text is the
        # working fallback; report that it was used.
        hits = uniprot_search(f'"{local}"', size=5)
        return hits, "free-text (WB gene ids are not in xref:wormbase)"
    if db not in _XREF_DB:
        raise ValueError(f"resolve_mod_id does not handle database {db!r} (token {token!r})")
    query = f"xref:{_XREF_DB[db]}-{local}"
    return uniprot_search(query, size=5), query


def quickgo_term(go_id: str) -> dict[str, Any]:
    """QuickGO's complete term record (carries isObsolete and secondaryIds)."""
    body = _cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete",
        f"go_{go_id.replace(':', '_')}",
    )
    return json.loads(body)["results"][0]


def quickgo_annotations(**params: str) -> dict[str, Any]:
    """QuickGO annotation search.

    Guards against silent truncation by comparing `numberOfHits` against
    `len(results)` -- never against a page-size constant the caller chose,
    because a service that clamps instead of erroring defeats that check.
    """
    query = "&".join(f"{k}={requests.utils.quote(v)}" for k, v in sorted(params.items()))
    key = "qgo_" + "".join(c if c.isalnum() else "_" for c in query)[:120]
    body = _cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/annotation/search?{query}", key
    )
    data = json.loads(body)
    n_hits = data.get("numberOfHits", 0)
    n_rows = len(data.get("results", []))
    data["_truncated"] = n_hits > n_rows
    return data
