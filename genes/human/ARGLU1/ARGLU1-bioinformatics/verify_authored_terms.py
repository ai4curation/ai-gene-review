#!/usr/bin/env python3
"""Second-source every GO term this review AUTHORS, against two services.

Motivation, learned the hard way on this PR: a single service can be a confident
outlier. QuickGO reported `GO:0035259` obsolete and `GO:0016922` childless; the GO
API, OLS4 and the repository's own ontology cache all disagreed, and QuickGO was
wrong on both counts. Worse, the "two checks" behind that claim were two QuickGO
endpoints -- **two methods against one service is one check.**

So this script takes every term the review *authors* -- the ids a reviewer cannot
assume came from GOA, i.e. `core_functions`, `proposed_replacement_terms`, and the
`term.id` of any `action: NEW` row -- and checks each against **two independent
services**:

  * QuickGO      (EBI)                    /ontology/go/terms/<id>/complete
  * OLS4         (EBI, separate pipeline) /ontologies/go/terms?iri=...

Any disagreement on obsolescence, or any term either service reports obsolete, is
reported as a problem. Terms sourced from GOA (`existing_annotations` rows that are
not NEW) are deliberately NOT checked: per CLAUDE.md those ids are machine-supplied
and are not the reviewer's to second-guess.

Run:  uv run python verify_authored_terms.py
Exit status is non-zero if any authored term is obsolete or the services disagree.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml


def repo_root() -> Path:
    for base in (Path(__file__).resolve(), Path.cwd().resolve()):
        for p in (base, *base.parents):
            if (p / "genes").is_dir() and (p / "src").is_dir():
                return p
    raise SystemExit("repo root not found")


ROOT = repo_root()
REVIEW = ROOT / "genes/human/ARGLU1/ARGLU1-ai-review.yaml"


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError(f"unreachable: {url}")


def quickgo(curie: str) -> dict:
    d = _get(f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{curie}/complete")
    res = d.get("results") or []
    if len(res) != 1:
        return {"service": "QuickGO", "found": False, "n": len(res)}
    r = res[0]
    return {
        "service": "QuickGO",
        "found": True,
        "name": r.get("name"),
        "obsolete": bool(r.get("isObsolete")),
        "aspect": r.get("aspect"),
    }


def ols(curie: str) -> dict:
    iri = "http://purl.obolibrary.org/obo/" + curie.replace(":", "_")
    url = ("https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri="
           + urllib.parse.quote(iri, safe=""))
    d = _get(url)
    terms = d.get("_embedded", {}).get("terms", [])
    if len(terms) != 1:
        return {"service": "OLS4", "found": False, "n": len(terms)}
    r = terms[0]
    return {
        "service": "OLS4",
        "found": True,
        "name": r.get("label"),
        "obsolete": bool(r.get("is_obsolete")),
        "aspect": None,
    }


def authored_terms(doc: dict) -> dict[str, list[str]]:
    """Collect ids the REVIEW authors, keyed by where they appear."""
    out: dict[str, list[str]] = {}

    def add(curie, where):
        if curie:
            out.setdefault(curie, []).append(where)

    for i, cf in enumerate(doc.get("core_functions") or []):
        for slot in ("molecular_function", "contributes_to_molecular_function",
                     "in_complex"):
            t = cf.get(slot)
            if isinstance(t, dict):
                add(t.get("id"), f"core_functions[{i}].{slot}")
        for slot in ("directly_involved_in", "locations", "substrates",
                     "anatomical_locations"):
            for t in (cf.get(slot) or []):
                if isinstance(t, dict):
                    add(t.get("id"), f"core_functions[{i}].{slot}")

    for i, ann in enumerate(doc.get("existing_annotations") or []):
        review = ann.get("review") or {}
        if review.get("action") == "NEW":
            add((ann.get("term") or {}).get("id"),
                f"existing_annotations[{i}].term (action: NEW)")
        for t in (review.get("proposed_replacement_terms") or []):
            if isinstance(t, dict):
                add(t.get("id"),
                    f"existing_annotations[{i}].proposed_replacement_terms")
    return out


def main() -> int:
    doc = yaml.safe_load(REVIEW.read_text())
    terms = authored_terms(doc)
    if not terms:
        raise SystemExit(
            "no authored terms found -- the collector is looking in the wrong "
            "slots, or the review changed shape. A zero here would read as a pass."
        )

    problems: list[str] = []
    print(f"checking {len(terms)} authored term(s) against two services\n")
    for curie in sorted(terms):
        q = quickgo(curie)
        time.sleep(0.15)
        o = ols(curie)
        time.sleep(0.15)
        where = ", ".join(sorted(set(terms[curie])))
        print(f"{curie}")
        print(f"   used at: {where}")
        for r in (q, o):
            if r["found"]:
                print(f"   {r['service']:<8} name={r['name']!r} obsolete={r['obsolete']}")
            else:
                print(f"   {r['service']:<8} NOT RESOLVED (n={r['n']})")

        if not q["found"] or not o["found"]:
            problems.append(f"{curie}: not resolvable on both services")
            continue
        if q["obsolete"] or o["obsolete"]:
            problems.append(
                f"{curie}: reported OBSOLETE by "
                f"{'QuickGO' if q['obsolete'] else ''}"
                f"{' and ' if q['obsolete'] and o['obsolete'] else ''}"
                f"{'OLS4' if o['obsolete'] else ''} -- an authored term must be current"
            )
        if q["obsolete"] != o["obsolete"]:
            problems.append(
                f"{curie}: services DISAGREE on obsolescence "
                f"(QuickGO={q['obsolete']}, OLS4={o['obsolete']}). Do not rely on "
                "either alone; consult api.geneontology.org before using this term."
            )
        print()

    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("all authored terms are current and the two services agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
