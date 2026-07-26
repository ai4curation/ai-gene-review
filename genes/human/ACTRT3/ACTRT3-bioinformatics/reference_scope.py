"""How many entities does each supporting reference annotate, and is any row a projection?

Rows that share one reference are not automatically N independent findings. Two failure shapes
have been seen in this family:

  * ComplexPortal-style **projection**: one complex-level experiment written onto every subunit,
    so a reference returns (n_subunits x n_terms) annotations with identical evidence. Found on
    ACTR8, where `PMID:23979016` yielded 80 annotations = 16 entities x 5 terms from a knockout
    in which the annotated gene was never perturbed.
  * **One experiment logged twice**: the same assay recorded by two databases, or reciprocally on
    both partners, which inflates an apparent replicate count. The ACRV1 `NbExp=3` case.

Querying QuickGO by **reference** rather than by gene exposes both, so this script does that for
every PMID the ACTRT3 review cites and reports, per reference:

  * total annotations, distinct entities, distinct terms, evidence codes and assigning databases;
  * the full matrix when it is small enough to read;
  * for each term, how many distinct entities carry it -- the projection signal; and
  * whether any *functional* (BP/MF) row is confined to fewer entities than the localisation
    rows, which is the signal that distinguishes honest multi-protein curation from a projection.
    A curator who observed twelve proteins in one structure annotates twelve locations but only
    the knocked-out gene's phenotype; a projection spreads everything.

Usage:  uv run python reference_scope.py
Writes: reference_scope.json, and prints a summary.
"""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent / "ACTRT3-ai-review.yaml"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
ASPECT = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}


def get(params: dict) -> dict:
    url = f"{QUICKGO}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as fh:
                return json.load(fh)
        except Exception as exc:
            if attempt == 3:
                raise RuntimeError(f"GET failed after 4 tries: {url}") from exc
            time.sleep(2 * (attempt + 1))
    raise AssertionError("unreachable")


def cited_pmids() -> list[str]:
    if not REVIEW.exists():
        raise FileNotFoundError(
            f"missing {REVIEW}\n  regenerate with: just fetch-gene human ACTRT3"
        )
    ids = sorted(set(re.findall(r"PMID:(\d{6,9})", REVIEW.read_text())))
    if not ids:
        raise RuntimeError(f"{REVIEW} cites no PMIDs; the extraction pattern needs revisiting")
    return ids


def scope(pmid: str) -> dict:
    """One page is enough for the projection test; the total is taken from the API's own count."""
    d = get({"reference": f"PMID:{pmid}", "limit": 200})
    rows = d.get("results", [])
    per_term: dict[str, set[str]] = defaultdict(set)
    aspect_of: dict[str, str] = {}
    for r in rows:
        per_term[r["goId"]].add(r["geneProductId"])
        aspect_of[r["goId"]] = ASPECT.get(r.get("goAspect"), "?")
    # Bare `GO:0005515 protein binding` is excluded from the functional set. An interaction paper
    # legitimately annotates every partner it reports with it, so counting it as a functional
    # claim makes any co-immunoprecipitation study look like a projection. Tested: without this
    # exclusion PMID:35793634 was mis-flagged, because its 12 partner rows outvoted the single
    # phenotype row that is the actual discriminator.
    functional = {t: len(e) for t, e in per_term.items()
                  if aspect_of[t] in ("MF", "BP") and t != "GO:0005515"}
    locational = {t: len(e) for t, e in per_term.items() if aspect_of[t] == "CC"}
    return {
        "pmid": pmid,
        "total_annotations": d.get("numberOfHits", 0),
        "rows_examined": len(rows),
        "distinct_entities": len({r["geneProductId"] for r in rows}),
        "distinct_terms": len(per_term),
        "evidence_codes": sorted({r["goEvidence"] for r in rows}),
        "assigned_by": sorted({r["assignedBy"] for r in rows if r.get("assignedBy")}),
        "entities_per_term": {t: len(e) for t, e in sorted(per_term.items())},
        "aspect_per_term": dict(sorted(aspect_of.items())),
        "max_entities_on_a_functional_term": max(functional.values(), default=0),
        "functional_terms_excluding_protein_binding": dict(sorted(functional.items())),
        "max_entities_on_a_location_term": max(locational.values(), default=0),
        "rows": [
            {"go_id": r["goId"], "aspect": ASPECT.get(r.get("goAspect"), "?"),
             "evidence": r["goEvidence"], "symbol": r.get("symbol"),
             "entity": r["geneProductId"], "taxon": r.get("taxonId"),
             "assigned_by": r.get("assignedBy"), "qualifier": r.get("qualifier")}
            for r in sorted(rows, key=lambda x: (x["goId"], x.get("symbol") or ""))
        ] if len(rows) <= 60 else "omitted: more than 60 rows",
    }


def main() -> None:
    out = {p: scope(p) for p in cited_pmids()}
    (HERE / "reference_scope.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"{'PMID':14} {'total':>7} {'entities':>9} {'terms':>6}  "
          f"{'max ents/func':>13} {'max ents/loc':>12}  codes / assignedBy")
    for pmid, s in out.items():
        print(f"PMID:{pmid:<9} {s['total_annotations']:>7} {s['distinct_entities']:>9} "
              f"{s['distinct_terms']:>6}  {s['max_entities_on_a_functional_term']:>13} "
              f"{s['max_entities_on_a_location_term']:>12}  "
              f"{','.join(s['evidence_codes']) or '-'} / {','.join(s['assigned_by']) or '-'}")
    print()
    for pmid, s in out.items():
        f, l = s["max_entities_on_a_functional_term"], s["max_entities_on_a_location_term"]
        if s["total_annotations"] == 0:
            verdict = "not curated by GOA at all"
        elif s["distinct_entities"] <= 2 and l <= 1:
            verdict = ("one experiment, recorded on <=2 entities; check for double-logging "
                       "across databases or reciprocal partner rows")
        elif l > 1 and f <= 1:
            verdict = (f"multi-entity LOCALISATION ({l} entities) with the functional claim "
                       f"confined to {f} entity: honest per-protein curation, NOT a projection - "
                       "a projection spreads the phenotype too")
        elif f > 1 and f == l:
            verdict = (f"functional and locational rows cover the same {f} entities: possible "
                       "projection; check assignedBy and whether the experiment perturbed each gene")
        else:
            verdict = f"functional rows on {f} entities, location rows on {l}"
        print(f"PMID:{pmid}: {verdict}")


if __name__ == "__main__":
    main()
