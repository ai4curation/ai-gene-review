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
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

OLS = "https://www.ebi.ac.uk/ols4/api"
CACHE = Path(__file__).parent / ".cache" / "ols"
# Object properties that relate charge states of the same molecule.
PROTONATION_RELS = {"is_protonated_form_of", "is_deprotonated_form_of"}
# Broader structural relations that stay on the same molecular *skeleton*
# (connectivity): charge states, tautomers, enantiomers/stereoisomers, and the
# is_a `children` that take a generic 2D compound (e.g. "isoleucine", which has
# no InChIKey) down to its stereospecific forms ("L-isoleucine", and its
# zwitterion — the form Rhea uses). NB: OLS does not cleanly separate these
# buckets, so we take their union and rely on the InChIKey-skeleton filter.
STRUCTURAL_RELS = PROTONATION_RELS | {
    "is_conjugate_acid_of", "is_conjugate_base_of",
    "is_tautomer_of", "is_enantiomer_of", "children",
}


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
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):  # deterministic "no such term / bad id" — don't retry
                _cache_put(url, {})
                return {}
            last = e
            time.sleep(2 ** attempt)
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
    skeleton: str | None = None  # InChIKey first block (connectivity, no charge/stereo)
    links: dict = field(default_factory=dict, repr=False)


def _term_from_doc(d: dict) -> ChebiTerm:
    ann = d.get("annotation", {})

    def _first(*keys: str) -> str | None:
        for key in keys:
            v = ann.get(key)
            if isinstance(v, list) and v:
                return v[0]
        return None

    charge = _first("charge")
    inchikey = _first("inchikey", "inchi_key_string")
    return ChebiTerm(
        curie=d["obo_id"],
        label=d.get("label", ""),
        charge=float(charge) if charge is not None else None,
        formula=_first("generalized_empirical_formula", "formula"),
        skeleton=inchikey[:14] if inchikey else None,
        links=d.get("_links", {}),
    )


def get_term(curie: str) -> ChebiTerm | None:
    iri = urllib.parse.quote(_iri(curie), safe="")
    data = _get_json(f"{OLS}/ontologies/chebi/terms?iri={iri}")
    terms = data.get("_embedded", {}).get("terms", [])
    if not terms:
        return None
    return _term_from_doc(terms[0])


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


def _neighbours(term: ChebiTerm, rels: set[str]) -> list[ChebiTerm]:
    """Chemical-entity neighbours of ``term`` over ``rels`` (drops role classes)."""
    out: list[ChebiTerm] = []
    for rel, link in term.links.items():
        if rel not in rels:
            continue
        href = link["href"] if isinstance(link, dict) else link
        for doc in _get_json(href).get("_embedded", {}).get("terms", []):
            nbr = _term_from_doc(doc)
            if nbr.charge is None:  # role/grouping class -> skip
                continue
            out.append(nbr)
    return out


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
        term = family[queue.pop()]
        for nbr in _neighbours(term, PROTONATION_RELS):
            if nbr.curie not in family:
                family[nbr.curie] = nbr
                queue.append(nbr.curie)
    return family


def structural_family(seed: str, max_terms: int = 80) -> dict[str, ChebiTerm]:
    """Return the molecule's *skeleton* family — same connectivity, any charge or
    stereochemistry — keyed by ChEBI curie.

    This recovers the second mismatch class that protonation expansion does not:
    a study reports a generic, non-stereospecific compound (``isoleucine``) while
    Rhea uses the stereospecific zwitterion (``L-isoleucine zwitterion``). We BFS
    over the broader ``STRUCTURAL_RELS`` (adding tautomer/enantiomer and the
    generic→specific ``children`` hop), and bound the walk to the seed's InChIKey
    **skeleton** (first block): a neighbour is followed/kept only if it shares an
    anchor skeleton, or is itself a generic node with no InChIKey (which we pass
    through to reach its stereospecific children). Anchors are seeded from the
    first InChIKey-bearing terms encountered.

    The match is therefore skeleton-level — **stereo- and charge-blind** — which
    is appropriate when the reported ChEBI is itself stereo-unspecified (common
    for NMR), but should be reported as a distinct, more permissive tier.
    """
    seed_term = get_term(seed)
    if seed_term is None:
        return {}
    family: dict[str, ChebiTerm] = {seed: seed_term}
    anchors: set[str] = {seed_term.skeleton} if seed_term.skeleton else set()
    queue = [seed]
    while queue and len(family) < max_terms:
        term = family[queue.pop(0)]
        # A specific term off the seed's skeleton is a dead end: keep it (it may
        # itself be a Rhea participant we want to record) but do not expand it.
        if term.skeleton and anchors and term.skeleton not in anchors:
            continue
        for nbr in _neighbours(term, STRUCTURAL_RELS):
            if nbr.skeleton and not anchors:
                anchors.add(nbr.skeleton)
            if nbr.curie not in family:
                family[nbr.curie] = nbr
                queue.append(nbr.curie)
    # Final skeleton filter: keep the seed, generic pass-through nodes, and any
    # term on an anchor skeleton; drop anything that drifted off-skeleton.
    if anchors:
        family = {
            cid: t for cid, t in family.items()
            if cid == seed or t.skeleton is None or t.skeleton in anchors
        }
    return family


def resolve_curie(token: str) -> str | None:
    """A reported metabolite token (a ``CHEBI:xxxx`` id or a name) -> ChEBI curie.

    Returns the id unchanged if the token already is one, otherwise resolves the
    name via :func:`search_neutral`. ``None`` if the name cannot be resolved.
    """
    if token.upper().startswith("CHEBI:"):
        return token
    term = search_neutral(token)
    return term.curie if term else None


def rhea_forms(seed: str, participants: set[str]) -> set[str]:
    """Map a reported metabolite ChEBI to the Rhea-participant id(s) it denotes.

    Returns the members of the seed's protonation family — and, only if those
    miss, its skeleton family — that are actually Rhea participants. This is the
    normalization used to place study metabolites into Rhea/GO space for
    enrichment (so both background and foreground live in participant space).
    """
    forms = {c for c in protonation_family(seed) if c in participants}
    if seed in participants:
        forms.add(seed)
    if not forms:
        forms = {c for c in structural_family(seed) if c in participants}
    return forms
