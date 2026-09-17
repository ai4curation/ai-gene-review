"""Shared UniProt / QuickGO REST helpers for the ARFGEF3 analyses.

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

UA = {"User-Agent": "ai-gene-review-ARFGEF3/1.0 (https://github.com/ai4curation/ai-gene-review)"}


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
    """Pull the fields the ARFGEF3 analyses care about out of a UniProt entry."""
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


def resolve_mod_id(token: str) -> tuple[list[dict[str, Any]], str]:
    """Resolve a MOD cross-reference token to UniProt entries via an xref search.

    Returns ``(hits, how)`` where ``how`` names the query actually used. Every
    hit is returned (size>=5) so that multi-hit ambiguity is reported rather
    than silently collapsed to a confident wrong answer (the ``size=1`` trap).

    ``how`` matters because some MOD namespaces are not indexed by UniProt at
    all -- WormBase *gene* ids (``WBGene...``) are absent from ``xref:wormbase``,
    which holds *protein* ids -- so those fall back to a free-text search. A
    fallback resolution is weaker evidence than an xref resolution and the
    caller must be able to say which one it got.
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
    elif db == "SGD":
        query = f"xref:sgd-{local}"
    elif db == "PomBase":
        query = f"xref:pombase-{local}"
    elif db == "dictyBase":
        query = f"xref:dictybase-{local}"
    elif db == "WB":
        query = f"xref:wormbase-{local}"
    else:
        raise ValueError(f"resolve_mod_id does not handle database {db!r} (token {token!r})")

    hits = uniprot_search(query, size=5)
    if hits:
        return hits, query
    # Documented fallback: WormBase gene ids are not in UniProt's wormbase xref
    # index. Free text finds them, but the caller is told it was a fallback.
    fallback = f'"{local}"'
    return uniprot_search(fallback, size=5), f"FALLBACK free-text {fallback}"


def quickgo_term(go_id: str) -> dict[str, Any]:
    body = _cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete",
        f"go_{go_id.replace(':', '_')}",
    )
    return json.loads(body)["results"][0]


def quickgo_annotations(acc: str, go_id: str) -> list[dict[str, Any]]:
    """Every annotation of `acc` to `go_id` or any descendant of it.

    Used to answer "what evidence does this WITH/FROM donor itself carry for the
    term it is donating?" -- which is a testable claim, not a safe hedge.

    Raises when the service reports more hits than it returned, so a silently
    truncated page can never be read as a complete answer. The comparison is
    against ``len(results)`` rather than against a page-size constant, because a
    service that *clamps* an over-large ``limit`` would sail past a constant.
    """
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId=UniProtKB:{acc}&goId={go_id}"
        "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100"
    )
    key = f"qg_ann_{acc}_{go_id.replace(':', '_')}"
    d = json.loads(_cached_get(url, key))
    n_hits = d.get("numberOfHits", 0)
    results = d.get("results", [])
    if n_hits > len(results):
        raise RuntimeError(
            f"QuickGO truncated {acc}/{go_id}: numberOfHits={n_hits} but "
            f"{len(results)} results returned; paginate before trusting this."
        )
    return results


def sec7_domain(entry: dict[str, Any]) -> tuple[int, int] | None:
    """(start, end) 1-based inclusive bounds of the entry's SEC7 domain feature.

    Returns None when UniProt annotates no SEC7 domain on the entry. The caller
    must treat that as "no domain annotated", never as "no domain present".
    """
    for feat in entry.get("features", []):
        if feat.get("type") != "Domain":
            continue
        if "SEC7" not in feat.get("description", "").upper():
            continue
        loc = feat["location"]
        return int(loc["start"]["value"]), int(loc["end"]["value"])
    return None
