"""Build compact static browser facets from GO and UniProt taxonomy lineages.

Only subset nodes and memberships for terms/taxa actually in the data are shipped.
The ontology is used at build time, never fetched by the browser.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from functools import cache
from hashlib import sha256
import json
from pathlib import Path
import re
from typing import Any
import warnings

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


GO_URL = "https://current.geneontology.org/ontology/go-basic.obo"
GO_ROOTS = {"GO:0003674", "GO:0008150", "GO:0005575"}
# Names select the desired depth; IDs and relationships come from the source.
TAXON_GROUPS = {
    "Bacteria",
    "Archaea",
    "Eukaryota",
    "Viruses",
    "Opisthokonta",
    "Metazoa",
    "Fungi",
    "Viridiplantae",
    "Amoebozoa",
    "Alveolata",
    "Stramenopiles",
    "Discoba",
    "Rhizaria",
}
MARKER = "\n/* Generated hierarchical facets */\n"


def read_go_obo(path: Path) -> tuple[dict[str, dict[str, Any]], str]:
    """Read named GO terms and only is_a/part_of edges from a GO OBO release.

    A subset OBO alone is insufficient: hidden intermediate terms are necessary
    to map detailed annotations to the subset. Use the full go-basic.obo file.
    """
    terms: dict[str, dict[str, Any]] = {}
    term: dict[str, Any] | None = None
    version = ""
    with path.open() as stream:
        for raw in stream:
            line = raw.strip()
            if line.startswith("data-version: "):
                version = line.split(": ", 1)[1]
            if line.startswith("["):
                term = (
                    {"parents": [], "subsets": [], "aliases": []}
                    if line == "[Term]"
                    else None
                )
            if term is None or ": " not in line:
                continue
            key, value = line.split(": ", 1)
            if key == "id" and value.startswith("GO:"):
                terms[value] = term
            elif key == "name":
                term["label"] = value
            elif key == "is_a":
                term["parents"].append(value.split()[0])
            elif key == "relationship" and value.split()[0] == "part_of":
                term["parents"].append(value.split()[1])
            elif key == "subset":
                term["subsets"].append(value)
            elif key == "alt_id":
                term["aliases"].append(value)
            elif key == "is_obsolete" and value == "true":
                term["obsolete"] = True
    return terms, version


def build_go_hierarchy(
    terms: dict[str, dict[str, Any]], observed: set[str], subset: str = "goslim_generic"
) -> dict[str, Any]:
    """Project safe ancestry onto the selected subset, retaining all parent paths."""
    active = {key: term for key, term in terms.items() if not term.get("obsolete")}
    selected = {key for key, term in active.items() if subset in term["subsets"]}
    if not selected:
        raise ValueError(f"GO source contains no active terms in {subset}")
    selected |= GO_ROOTS & active.keys()
    aliases = {alias: key for key, term in active.items() for alias in term["aliases"]}
    visiting: set[str] = set()

    @cache
    def ancestors(key: str) -> frozenset[str]:
        if key in visiting:
            raise ValueError(f"Cycle in GO ancestry at {key}")
        if key not in active:
            return frozenset()
        visiting.add(key)
        result = {key}
        for parent in active[key]["parents"]:
            result.update(ancestors(parent))
        visiting.remove(key)
        return frozenset(result)

    memberships = {
        key: sorted(ancestors(aliases.get(key, key)) & selected) or ["unmapped"]
        for key in sorted(observed)
    }
    used = set().union(*map(set, memberships.values())) if memberships else set()
    nodes = {}
    for key in sorted(used - {"unmapped"}):
        candidates = (ancestors(key) & used) - {key}
        # Nearest displayed parents: omit an ancestor reachable via another one.
        parents = candidates - set().union(
            *(ancestors(parent) - {parent} for parent in candidates)
        )
        label = active[key]["label"]
        if key in GO_ROOTS:
            label = label.replace("_", " ").capitalize()
        nodes[key] = {"label": label, "parents": sorted(parents)}
    if "unmapped" in used:
        nodes["unmapped"] = {"label": "Unmapped / obsolete GO terms", "parents": []}
    return {
        "field": "go_slim",
        "sourceField": "term_id",
        "label": "GO · generic slim",
        "before": "review.action",
        "type": "hierarchy",
        "nodes": nodes,
        "memberships": memberships,
        "unmappedNode": "unmapped",
        "unmappedLabel": "Unmapped / obsolete GO terms",
        "description": "Includes detailed terms beneath each category. Groups annotation terms, including negated and rejected annotations; use the review and negation filters to refine.",
    }


def build_taxonomy_hierarchy(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Keep selected clades and each observed taxon, preserving source ancestry."""
    nodes: dict[str, dict[str, Any]] = {}
    memberships = {}
    observed = {record["taxonId"] for record in records if not record.get("unmapped")}
    for record in sorted(records, key=lambda item: str(item["taxonId"])):
        lineage = [
            node
            for node in record["lineage"]
            if node["scientificName"] in TAXON_GROUPS or node["taxonId"] in observed
        ] + [record]
        path: list[str] = []
        if record.get("unmapped"):
            nodes["unmapped-taxonomy"] = {"label": "Unmapped taxa", "parents": []}
            path.append("unmapped-taxonomy")
        for node in lineage:
            key = (
                node["key"] if node.get("unmapped") else f"NCBITaxon:{node['taxonId']}"
            )
            if key in path:
                continue
            nodes[key] = {"label": node["scientificName"], "parents": path[-1:]}
            path.append(key)
        memberships[path[-1]] = path
    return {
        "field": "taxon_id",
        "sourceField": "taxon_id",
        "label": "Species",
        "replaces": "taxon_label",
        "type": "hierarchy",
        "nodes": nodes,
        "memberships": memberships,
        "unmappedNode": "unmapped-taxonomy",
        "unmappedLabel": "Unmapped taxa",
        "description": "Selecting a group includes all represented species beneath it.",
    }


def fetch_taxonomy(
    taxon_labels: dict[str, str], cache_dir: Path
) -> list[dict[str, Any]]:
    """Cache authoritative full lineages; fail the build on an unresolved taxon."""
    cache_dir.mkdir(parents=True, exist_ok=True)

    def fetch(taxon_id: str) -> dict[str, Any]:
        if not re.fullmatch(r"NCBITaxon:\d+", taxon_id):
            warnings.warn(
                f"Unmapped taxonomy identifier in browser data: {taxon_id}",
                stacklevel=2,
            )
            return {
                "key": taxon_id,
                "taxonId": taxon_id,
                "scientificName": taxon_labels[taxon_id] or taxon_id,
                "lineage": [],
                "unmapped": True,
            }
        number = taxon_id.split(":")[1]
        path = cache_dir / f"{number}.json"
        if path.exists():
            return json.loads(path.read_text())
        record = json.loads(
            download_source(f"https://rest.uniprot.org/taxonomy/{number}", timeout=60)
        )
        if str(record["taxonId"]) != number:
            raise ValueError(
                f"Taxonomy source redirected {taxon_id}; review its mapping"
            )
        path.write_text(json.dumps(record) + "\n")
        return record

    with ThreadPoolExecutor(max_workers=6) as pool:
        return list(pool.map(fetch, sorted(taxon_labels)))


def download_source(url: str, *, timeout: float) -> bytes:
    """Retry transient GET failures at most three times, with bounded backoff.

    A separate session per request is safe for the taxonomy thread pool.
    Retry-After is ignored so an upstream response cannot suspend a build for
    an unbounded interval. Permanent errors (including 404) fail immediately.
    """
    retries = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=False,
    )
    with requests.Session() as session:
        adapter = HTTPAdapter(max_retries=retries)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        return response.content


def append_hierarchies(
    schema_path: Path, facets: list[dict[str, Any]], provenance: dict[str, Any]
) -> None:
    """Attach build metadata without changing row data or requiring another asset."""
    original = schema_path.read_text().split(MARKER)[0]
    payload = json.dumps(
        {"facets": facets, "provenance": provenance},
        ensure_ascii=True,
        separators=(",", ":"),
    )
    schema_path.write_text(
        original + MARKER + "window.searchSchema.hierarchies = " + payload + ";\n"
    )


def main() -> None:
    """Add hierarchies to a generated annotation browser schema."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data", type=Path, default=Path("exports/exported_annotations.json")
    )
    parser.add_argument("--schema", type=Path, default=Path("app/schema.js"))
    parser.add_argument(
        "--go-obo", type=Path, help="Use a local/pinned full GO OBO release"
    )
    parser.add_argument(
        "--cache-dir", type=Path, default=Path(".cache/browser-hierarchies")
    )
    args = parser.parse_args()
    rows = json.loads(args.data.read_text())
    terms_used = {
        row["term_id"] for row in rows if str(row.get("term_id", "")).startswith("GO:")
    }
    taxa_used = {
        row["taxon_id"]: row.get("taxon_label") or row["taxon_id"]
        for row in rows
        if row.get("taxon_id")
    }
    go_path = args.go_obo or args.cache_dir / "go-basic.obo"
    if not go_path.exists():
        if args.go_obo:
            raise FileNotFoundError(go_path)
        go_path.parent.mkdir(parents=True, exist_ok=True)
        go_path.write_bytes(download_source(GO_URL, timeout=120))
    terms, version = read_go_obo(go_path)
    facets = [
        build_taxonomy_hierarchy(
            fetch_taxonomy(taxa_used, args.cache_dir / "taxonomy")
        ),
        build_go_hierarchy(terms, terms_used),
    ]
    provenance = {
        "go_source": GO_URL,
        "go_version": version,
        "go_sha256": sha256(go_path.read_bytes()).hexdigest(),
        "subset": "goslim_generic",
        "predicates": ["is_a", "part_of"],
        "taxonomy_source": "https://rest.uniprot.org/taxonomy/",
    }
    append_hierarchies(args.schema, facets, provenance)
    print(
        json.dumps(
            {
                "schema": str(args.schema),
                "go_version": version,
                "nodes": {facet["field"]: len(facet["nodes"]) for facet in facets},
            }
        )
    )


if __name__ == "__main__":
    main()
