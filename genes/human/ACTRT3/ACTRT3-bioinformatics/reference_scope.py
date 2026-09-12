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
every PMID the ACTRT3 review cites.

Counting discipline, which is the whole point of the rewrite. An earlier version fetched one
`limit=200` page and reported the per-term, per-code and per-database breakdowns from it while
taking the *total* from `numberOfHits`. For a large screen that silently mixes a true total with a
2 per cent sample: PMID:33961781 has 9514 annotations, so the page saw 200 of them, and the
review then asserted sample-derived facts ("the only term it contributes", "all assigned by
IntAct") as totals. Both were false, and one of them hid a real ComplexPortal projection tail in
that very reference.

So every count this script reports as a total is obtained from its own **filtered count query**
(`limit=1`, read `numberOfHits`), never from the sampled page:

  * `total_annotations`            - unfiltered
  * `true_annotations_per_term`    - one exact-usage query per term. These are ANNOTATION ROW
                                     counts; `numberOfHits` never collapses per gene product.
                                     `entities_per_term` is the distinct-gene-product count, and
                                     is emitted ONLY when `rows_complete` (i.e. NOT truncated),
                                     because it is counted from the returned rows and a distinct
                                     count taken from a sampled page is a lower bound. Note this is
                                     row completeness, not `term_list_provably_complete`, which is
                                     weaker: the latter only proves every term was queried.
                                     The projection test uses the entity counts when available, and
                                     `spread_units` records which quantity the maxima are in.
  * `true_annotations_per_code`    - one query per evidence code seen. NOTE: these do not
                                     partition the total, because QuickGO's `evidenceCode` filter
                                     is not exact-only; on PMID:35793634 they sum to 57 against a
                                     total of 35. Reported for orientation, never as a basis for
                                     an "every annotation is code X" claim.
  * `true_annotations_per_db`      - one query per assigning database seen
  * `true_annotations_per_aspect`  - three queries, so terms absent from the sampled page are
                                     still accounted for

`unaccounted_annotations` is then `total - sum(true_annotations_per_term)`; when it is non-zero the
term list is provably incomplete and the script says so rather than implying coverage. The
sampled page is retained only for the readable row matrix, and every field derived from it is
named `*_seen` and marked as a lower bound when `truncated` is true.

The projection test itself: compare how many entities carry the reference's *functional* rows
against how many carry its *localisation* rows. A curator who observed twelve proteins in one
structure annotates twelve locations but only the knocked-out gene's phenotype; a projection
spreads everything. Bare `GO:0005515 protein binding` is excluded from the functional set,
because an interaction paper legitimately annotates every partner it reports with it and counting
it makes any co-immunoprecipitation study look like a projection.

Usage:  uv run python reference_scope.py
Writes: reference_scope.json, and prints a summary.
"""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent / "ACTRT3-ai-review.yaml"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
ASPECT = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}
PAGE = 200

# ECO ids for the evidence codes QuickGO filters on, so a per-code total can be requested.
ECO = {"IPI": "ECO:0000353", "IDA": "ECO:0000314", "IMP": "ECO:0000315",
       "IGI": "ECO:0000316", "IEP": "ECO:0000270", "TAS": "ECO:0000304",
       "IBA": "ECO:0000318", "ISS": "ECO:0000250", "IEA": "ECO:0000501"}

# Databases probed even when the sampled page never shows them. ComplexPortal is the documented
# complex-to-subunit projector, so a reference's projected tail can sit entirely outside a 200-row
# sample of a large screen -- which is exactly what happened on PMID:33961781, where 5 projected
# GO:0005813 rows were invisible while the review asserted "all assigned by IntAct".
ALWAYS_PROBE_DBS = ("ComplexPortal",)


def get(params: dict) -> dict:
    url = f"{QUICKGO}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as fh:
                return json.load(fh)
        except Exception as exc:
            if attempt == 3:
                raise RuntimeError(f"GET failed after 4 tries: {url}") from exc
            time.sleep(2 * (attempt + 1))
    raise AssertionError("unreachable")


def count(**params) -> int:
    """A total, from the API's own hit count rather than from a page of results."""
    return get({"limit": 1, **params}).get("numberOfHits", 0)


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
    ref = f"PMID:{pmid}"
    total = count(reference=ref)
    page = get({"reference": ref, "limit": PAGE})
    rows = page.get("results", [])
    truncated = len(rows) < total

    per_term_seen: dict[str, set[str]] = defaultdict(set)
    aspect_of: dict[str, str] = {}
    for r in rows:
        per_term_seen[r["goId"]].add(r["geneProductId"])
        aspect_of[r["goId"]] = ASPECT.get(r.get("goAspect"), "?")
    codes_seen = sorted({r["goEvidence"] for r in rows})
    dbs_seen = sorted({r["assignedBy"] for r in rows if r.get("assignedBy")})

    # --- totals, each from its own filtered count query
    true_per_code = {c: count(reference=ref, evidenceCode=ECO[c]) for c in codes_seen if c in ECO}
    probe_dbs = sorted(set(dbs_seen) | set(ALWAYS_PROBE_DBS)) if total else []
    true_per_db = {d: n for d in probe_dbs if (n := count(reference=ref, assignedBy=d))}
    # Rows from a projecting database are few by nature, so fetch them and fold their terms into
    # the term map; otherwise a projection outside the sample stays invisible.
    extra_rows: list[dict] = []
    for d in ALWAYS_PROBE_DBS:
        if true_per_db.get(d):
            extra_rows += get({"reference": ref, "assignedBy": d, "limit": PAGE}).get("results", [])
    for r in extra_rows:
        per_term_seen[r["goId"]].add(r["geneProductId"])
        aspect_of[r["goId"]] = ASPECT.get(r.get("goAspect"), "?")
    true_per_aspect = {
        ASPECT[a]: count(reference=ref, aspect=a) for a in ASPECT
    } if total else {}
    # Now that the term map includes anything the projecting-database probe added, ask for each
    # term's own true total. NOTE the semantics: numberOfHits counts ANNOTATION ROWS, never
    # distinct gene products. PMID:18692047 proves the distinction against this very file - its
    # GO:0005515 total is 4 while only 2 entities are involved, each logged once by UniProt and
    # once by IntAct. Naming this "entities" once caused the review to assert an entity count that
    # was really an annotation count.
    true_annotations_per_term = {
        t: count(reference=ref, goId=t, goUsage="exact") for t in sorted(per_term_seen)
    }
    codes_seen = sorted(set(codes_seen) | {r["goEvidence"] for r in extra_rows})
    dbs_seen = sorted(set(dbs_seen) | {r["assignedBy"] for r in extra_rows if r.get("assignedBy")})
    # Sound precisely because these are annotation counts, not entity counts.
    unaccounted = total - sum(true_annotations_per_term.values())
    db_total = sum(true_per_db.values())

    # Distinct gene products per term, counted from the rows -- so the precondition is that every
    # ROW was seen, i.e. `not truncated`. `unaccounted == 0` is a different and weaker property: it
    # proves every annotation's TERM was queried, not that every row was returned. The two came
    # within one annotation of diverging on this dataset: PMID:33961781 has 9508 + 5 = 9513 against
    # a total of 9514, so the single stray row is the only reason its term list stayed open while
    # the page showed 200 of 9514. Without it the old gate would have emitted a 119-entity count
    # from that page and labelled it complete -- the round-1 sampling defect wearing a total's name.
    rows_complete = not truncated and total > 0
    term_list_complete = unaccounted == 0 and total > 0
    complete = rows_complete
    all_rows = rows + extra_rows
    entities_per_term = {
        t: len({r["geneProductId"] for r in all_rows if r["goId"] == t})
        for t in sorted(per_term_seen)
    } if complete else {}

    # The projection test needs ENTITY counts, so it uses entities_per_term when that is
    # trustworthy and falls back to annotation counts otherwise -- with the fallback recorded,
    # since entities <= annotations means a fallback can only overstate the spread.
    basis = entities_per_term if complete else true_annotations_per_term
    functional = {t: n for t, n in basis.items()
                  if aspect_of.get(t) in ("MF", "BP") and t != "GO:0005515"}
    locational = {t: n for t, n in basis.items() if aspect_of.get(t) == "CC"}
    max_func = max(functional.values(), default=0)
    max_loc = max(locational.values(), default=0)
    # These are entity counts only when the basis is entities; in the fallback they are annotation
    # counts. The round-2 rename did not reach them, so the units are now carried alongside rather
    # than implied by the name.
    spread_units = "entities" if complete else "annotations"

    proj_line = (
        f"{ref} projection test on {spread_units}: "
        + ", ".join(f"{t}={n}" for t, n in sorted(basis.items()))
        + f"; max functional {max_func}, max localisation {max_loc}"
    ) if total else f"{ref} projection test: not curated by GOA"
    summary = (
        f"{ref}: {total} annotations total, {len(rows)} rows examined"
        f"{' (TRUNCATED)' if truncated else ''}, {len(per_term_seen)} terms seen, "
        f"{unaccounted} unaccounted; codes {','.join(codes_seen) or '-'}; "
        f"assignedBy {','.join(f'{d}={n}' for d, n in sorted(true_per_db.items())) or '-'}"
    )
    return {
        "pmid": pmid,
        "summary_line": summary,
        "projection_test_line": proj_line,
        "total_annotations": total,
        "rows_examined": len(rows),
        "truncated": truncated,
        "unaccounted_annotations": unaccounted,
        "term_list_provably_complete": term_list_complete,
        "distinct_entities_seen": len({r["geneProductId"] for r in rows}),
        "distinct_entities_is_lower_bound": truncated,
        "evidence_codes_seen": codes_seen,
        "assigned_by_seen": dbs_seen,
        "true_annotations_per_code": true_per_code,
        "true_annotations_per_db": true_per_db,
        "assigning_databases_provably_complete": db_total == total,
        "annotations_from_unprobed_databases": total - db_total,
        "projecting_database_rows": [
            {"go_id": r["goId"], "aspect": ASPECT.get(r.get("goAspect"), "?"),
             "evidence": r["goEvidence"], "symbol": r.get("symbol"),
             "entity": r["geneProductId"], "assigned_by": r.get("assignedBy")}
            for r in sorted(extra_rows, key=lambda x: (x["goId"], x.get("symbol") or ""))
        ],
        "true_annotations_per_aspect": true_per_aspect,
        "true_annotations_per_term": true_annotations_per_term,
        "entities_per_term": entities_per_term,
        "entities_per_term_available": complete,
        "rows_complete": rows_complete,
        "projection_test_basis": "entities_per_term" if complete else "true_annotations_per_term",
        "aspect_per_term": dict(sorted(aspect_of.items())),
        "functional_terms_excluding_protein_binding": dict(sorted(functional.items())),
        "max_functional_spread": max_func,
        "max_location_spread": max_loc,
        "spread_units": spread_units,
        "projection_test_reliable": rows_complete,
        "rows": [
            {"go_id": r["goId"], "aspect": ASPECT.get(r.get("goAspect"), "?"),
             "evidence": r["goEvidence"], "symbol": r.get("symbol"),
             "entity": r["geneProductId"], "taxon": r.get("taxonId"),
             "assigned_by": r.get("assignedBy"), "qualifier": r.get("qualifier")}
            for r in sorted(rows, key=lambda x: (x["goId"], x.get("symbol") or ""))
        ] if len(rows) <= 60 else f"omitted: {len(rows)} rows on the sampled page",
    }


def verdict(s: dict) -> str:
    """A sentence per reference. Projection by a projecting database is stated as such.

    The location-versus-function heuristic is applied only to rows NOT assigned by a database
    that projects by design. Without that split the heuristic inverts: ComplexPortal's five
    GO:0005813 rows on PMID:33961781 are one complex-level fact written onto the complex and its
    four subunits, yet with bare GO:0005515 excluded from the functional set they present as
    "multi-entity localisation with no functional claim" -- which the earlier version of this
    function reported as NOT a projection, exactly backwards.
    """
    if s["total_annotations"] == 0:
        return "not curated by GOA at all"

    parts: list[str] = []
    proj = s["projecting_database_rows"]
    if proj:
        dbs = sorted({r["assigned_by"] for r in proj})
        terms = sorted({r["go_id"] for r in proj})
        parts.append(
            f"{len(proj)} of {s['total_annotations']} annotations are assigned by "
            f"{'/'.join(dbs)}, which projects a complex-level observation onto the complex and "
            f"each subunit by design: terms {','.join(terms)} across "
            f"{len({r['entity'] for r in proj})} entities. Those are ONE finding written "
            f"{len(proj)} times, not independent support"
        )

    f, l = s["max_functional_spread"], s["max_location_spread"]
    units = s["spread_units"]
    if proj:
        parts.append(
            "the remaining rows are not from a projecting database; the location-versus-function "
            "test is not applied to them here because this reference's non-projected content is "
            "a single interaction term"
            if l and not f else
            f"the remaining rows carry functional claims on {f} {units} and locations on {l}"
        )
    elif l > 1 and f <= 1:
        parts.append(
            f"multi-entity LOCALISATION ({l} {units}) with the functional claim confined to "
            f"{f} {units}, and no projecting database involved: honest per-protein curation, NOT "
            "a projection - a projection spreads the phenotype too"
        )
    elif f > 1 and f == l:
        parts.append(
            f"functional and locational rows cover the same {f} {units}: possible projection; "
            "check whether the experiment perturbed each gene"
        )
    elif s["distinct_entities_seen"] <= 2 and l <= 1 and not s["truncated"]:
        parts.append(
            "one experiment, recorded on <=2 entities; check for double-logging across databases "
            "or reciprocal partner rows"
        )
    else:
        parts.append(f"functional rows on {f} {units}, location rows on {l} {units}")

    if s["unaccounted_annotations"]:
        parts.append(
            f"CAVEAT: {s['unaccounted_annotations']} of {s['total_annotations']} annotations are "
            "to terms neither the sampled page nor the projecting-database probe showed, so the "
            "term list is a lower bound"
        )
    return "; ".join(parts)


def selftest() -> None:
    """Exercise the verdict() branches this dataset cannot reach, on every run.

    Twice now a defect has survived because the branch carrying it was unreachable with the six
    references actually cited: the location-versus-function inversion on projected rows, and then
    two branches still hardcoding the noun "entities" over what may be annotation counts. Live
    data cannot cover them, so synthetic blocks do, and a failure here aborts before any report is
    written. The invariant is simply that no printed count is ever labelled with a unit the block
    did not declare.
    """
    base = {
        "pmid": "00000000", "total_annotations": 5000, "rows_examined": 200, "truncated": True,
        "unaccounted_annotations": 0, "term_list_provably_complete": True, "rows_complete": False,
        "distinct_entities_seen": 119, "projecting_database_rows": [],
        "max_functional_spread": 3000, "max_location_spread": 12, "spread_units": "annotations",
    }
    cases = {
        "general fallback, annotations basis": base,
        "localisation branch, annotations basis": {**base, "max_functional_spread": 1},
        "same-count branch, annotations basis": {**base, "max_location_spread": 3000},
    }
    for label, block in cases.items():
        got = verdict(block)
        if "entities" in got:
            raise AssertionError(
                f"selftest: verdict() said 'entities' for a block declaring "
                f"spread_units={block['spread_units']!r} ({label}): {got}"
            )
        if "annotations" not in got:
            raise AssertionError(f"selftest: verdict() declared no units at all ({label}): {got}")
    # and the mirror: an entities basis must say entities
    ent = verdict({**base, "spread_units": "entities", "truncated": False, "rows_complete": True,
                   "max_functional_spread": 1})
    if "entities" not in ent:
        raise AssertionError(f"selftest: entities basis did not say entities: {ent}")


def main() -> None:
    selftest()
    out = {p: scope(p) for p in cited_pmids()}
    (HERE / "reference_scope.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    for s in out.values():
        print(s["summary_line"])
    print()
    for pmid, s in out.items():
        print(f"PMID:{pmid}: {verdict(s)}")
        if s["total_annotations"] and not s["assigning_databases_provably_complete"]:
            print(f"    note: {s['annotations_from_unprobed_databases']} annotations come from a "
                  "database neither seen on the sampled page nor probed, so any 'all assigned by "
                  "X' claim is unproven for this reference")
        if len(s["true_annotations_per_db"]) > 1:
            print(f"    note: more than one assigning database - {s['true_annotations_per_db']} - "
                  "so a claim of the form 'all assigned by X' would be false for this reference")


if __name__ == "__main__":
    main()
