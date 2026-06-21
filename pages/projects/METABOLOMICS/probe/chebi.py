#!/usr/bin/env python3
"""ChEBI access via the OLS4 REST API, with protonation-state normalization.

The whole point of this module is the ``protonation_family`` function. Metabolomics
repositories (MetaboLights, Metabolomics Workbench / RefMet) report metabolites as
their *neutral* species (e.g. ``citric acid``, ``ATP``, ``D-glucose 6-phosphate``),
whereas Rhea writes reaction participants in their *major protonation state at
pH 7.3* (e.g. ``citrate(3-)``, ``ATP(4-)``, ``D-glucose 6-phosphate(2-)``). A naive
exact ChEBI match between the two therefore misses most of the bridge.

ChEBI models the relationship between these forms with the object properties
``is_protonated_form_of`` (RO:0018033) and ``is_deprotonated_form_of`` (RO:0018034).
Walking those edges in both directions from a seed compound yields the compound's
whole *protonation family* (all charge states of the same molecule). We restrict the
walk to neighbours that carry a numeric ``charge`` annotation, which excludes the
role/grouping classes (e.g. ``human metabolite``, ``fundamental metabolite``) that
OLS bundles into the same relation buckets.

All data is fetched live from OLS4 and cached on disk under ``.cache/``; nothing is
hardcoded.
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

OLS = "https://www.ebi.ac.uk/ols4/api"
CACHE = Path(__file__).parent / ".cache" / "ols"
# Object properties that relate charge states of the same molecule.
PROTONATION_RELS = {"is_protonated_form_of", "is_deprotonated_form_of"}


def _cache_get(key: str) -> dict | None:
    f = CACHE / (urllib.parse.quote(key, safe="") + ".json")
    if f.exists():
        return json.loads(f.read_text())
    return None


def _cache_put(key: str, value: dict) -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / (urllib.parse.quote(key, safe="") + ".json")
    f.write_text(json.dumps(value))


def _get_json(url: str, timeout: int = 60, retries: int = 3) -> dict:
    cached = _cache_get(url)
    if cached is not None:
        return cached
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review-metabolomics/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode())
            _cache_put(url, data)
            return data
        except Exception as e:  # noqa: BLE001 - retry on any transient network error
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"OLS request failed after {retries} tries: {url}: {last}")


def _iri(curie: str) -> str:
    num = curie.split(":", 1)[1]
    return f"http://purl.obolibrary.org/obo/CHEBI_{num}"


@dataclass
class ChebiTerm:
    curie: str
    label: str
    charge: float | None
    formula: str | None
    links: dict = field(default_factory=dict, repr=False)


def get_term(curie: str) -> ChebiTerm | None:
    iri = urllib.parse.quote(_iri(curie), safe="")
    data = _get_json(f"{OLS}/ontologies/chebi/terms?iri={iri}")
    terms = data.get("_embedded", {}).get("terms", [])
    if not terms:
        return None
    d = terms[0]
    ann = d.get("annotation", {})

    def _first(key: str) -> str | None:
        v = ann.get(key)
        return v[0] if isinstance(v, list) and v else None

    charge = _first("charge")
    return ChebiTerm(
        curie=d["obo_id"],
        label=d.get("label", ""),
        charge=float(charge) if charge is not None else None,
        formula=_first("generalized_empirical_formula") or _first("formula"),
        links=d.get("_links", {}),
    )


def search_neutral(name: str) -> ChebiTerm | None:
    """Resolve a metabolite *name* to a ChEBI chemical entity.

    Mimics how a metabolomics repository reports a compound: prefer the neutral
    (charge 0) species when one exists, since that is what curators record. Only
    returns terms that carry a numeric charge (i.e. real chemical entities, not
    role/grouping classes).
    """
    q = urllib.parse.urlencode(
        {"q": name, "ontology": "chebi", "exact": "true", "rows": 20,
         "fieldList": "obo_id,label"}
    )
    data = _get_json(f"{OLS}/search?{q}")
    docs = data.get("response", {}).get("docs", [])
    candidates: list[ChebiTerm] = []
    for doc in docs:
        term = get_term(doc["obo_id"])
        if term and term.charge is not None:
            candidates.append(term)
    if not candidates:
        return None
    # Prefer neutral; otherwise the species closest to neutral.
    candidates.sort(key=lambda t: abs(t.charge or 0))
    return candidates[0]


def protonation_family(seed: str, max_terms: int = 40) -> dict[str, ChebiTerm]:
    """Return all charge states of the molecule, keyed by ChEBI curie.

    Breadth-first walk over ``is_protonated_form_of`` / ``is_deprotonated_form_of``
    edges, keeping only neighbours with a numeric charge (drops role classes).
    """
    seed_term = get_term(seed)
    if seed_term is None:
        return {}
    family: dict[str, ChebiTerm] = {seed: seed_term}
    queue = [seed]
    while queue and len(family) < max_terms:
        cur = queue.pop()
        term = family.get(cur) or get_term(cur)
        if term is None:
            continue
        for rel, link in term.links.items():
            if rel not in PROTONATION_RELS:
                continue
            href = link["href"] if isinstance(link, dict) else link
            sub = _get_json(href)
            for nbr in sub.get("_embedded", {}).get("terms", []):
                ann = nbr.get("annotation", {})
                charge = ann.get("charge")
                if not charge:  # role/grouping class -> skip
                    continue
                cid = nbr["obo_id"]
                if cid not in family:
                    family[cid] = ChebiTerm(
                        curie=cid,
                        label=nbr.get("label", ""),
                        charge=float(charge[0]),
                        formula=None,
                        links=nbr.get("_links", {}),
                    )
                    queue.append(cid)
    return family
