"""Re-verify, on two independent services, the ontology claims the ARHGAP23 review turns on.

Three statements in the review are load-bearing and are the kind that quietly go stale:

  1. ``GO:0005100`` "Rho GTPase activator activity" is obsolete / merged into ``GO:0005096``.
  2. ``GO:0005096`` has no ``is_a`` children, so no molecular-function term can name a GAP's
     substrate. (This is the whole basis of the ONTOLOGY knowledge gap, and of accepting the
     two Reactome ``GO:0005096`` rows rather than specialising them.)
  3. ``GO:0035024`` and ``GO:0035021`` are descendants of ``GO:0051056`` and are **not**
     descendants of ``GO:0007165``. (This is why the ``GO:0007165`` row is a branch change
     rather than a specialisation, and why the ``GO:0051056`` row is a specialisation.)

Each is checked against **two different services** - OLS4 and ``api.geneontology.org`` - and a
disagreement between them is a failure, not something to average. Two endpoints of one service
is one check, which is how an agent elsewhere in this campaign convinced itself it had
cross-checked when it had not; QuickGO in particular silently resolves merged ids and answers
for the surviving term, so it cannot be read at face value in either direction.

``--self-test`` asserts each check can fail, by running the same predicates against terms whose
answers are known to be the opposite.

Usage:
    uv run python check_ontology_claims.py
    uv run python check_ontology_claims.py --self-test
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

OLS4 = "https://www.ebi.ac.uk/ols4/api/ontologies/go"
GOAPI = "https://api.geneontology.org/api/ontology/term"


class ClaimError(RuntimeError):
    """A hard failure: a claim in the review is no longer supported, or the services disagree."""


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as fh:
            return json.load(fh)
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        raise ClaimError(f"could not reach {url}: {exc}. Re-run with network access.") from exc


def _iri(term: str) -> str:
    return f"http://purl.obolibrary.org/obo/{term.replace(':', '_')}"


def ols_term(term: str) -> dict | None:
    url = f"{OLS4}/terms?iri=" + urllib.parse.quote(_iri(term), safe="")
    terms = _get(url).get("_embedded", {}).get("terms", [])
    return terms[0] if terms else None


def _ols_rel(term: str, rel: str) -> dict[str, str]:
    url = (
        f"{OLS4}/terms/"
        + urllib.parse.quote(urllib.parse.quote(_iri(term), safe=""), safe="")
        + f"/{rel}?size=500"
    )
    d = _get(url)
    page = d.get("page", {})
    if page.get("totalPages", 1) > 1:
        raise ClaimError(f"{term} {rel} is paged ({page}); this check would read a partial set")
    return {t["obo_id"]: t["label"] for t in d.get("_embedded", {}).get("terms", [])}


def ols_children(term: str) -> dict[str, str]:
    return _ols_rel(term, "hierarchicalChildren")


def ols_ancestors(term: str) -> dict[str, str]:
    return _ols_rel(term, "hierarchicalAncestors")


def go_term(term: str) -> dict:
    return _get(f"{GOAPI}/{urllib.parse.quote(term)}")


def go_subgraph(term: str, key: str) -> dict[str, str]:
    d = _get(f"{GOAPI}/{urllib.parse.quote(term)}/subgraph")
    return {x.get("id"): x.get("lbl") for x in d.get(key, []) if x.get("id")}


def _agree(name: str, a: bool, b: bool, a_src: str = "OLS4", b_src: str = "GO API") -> bool:
    if a != b:
        raise ClaimError(
            f"{name}: {a_src} says {a} and {b_src} says {b}. The services disagree, so this "
            "claim cannot be treated as settled; check it by hand before relying on it."
        )
    return a


def claim_merged(obsolete_term: str, surviving: str) -> dict:
    """GO:0005100 is gone; GO:0005096 is the live term."""
    ols = ols_term(obsolete_term)
    ols_gone = ols is None or bool(ols.get("is_obsolete"))
    go = go_term(obsolete_term)
    go_gone = not go.get("label")
    gone = _agree(f"{obsolete_term} is obsolete/absent", ols_gone, go_gone)

    ols_live = ols_term(surviving)
    live_ok = ols_live is not None and not ols_live.get("is_obsolete")
    go_live = bool(go_term(surviving).get("label"))
    live = _agree(f"{surviving} is live", live_ok, go_live)
    return {
        "obsolete_term": obsolete_term,
        "surviving_term": surviving,
        "obsolete_term_gone": gone,
        "surviving_term_live": live,
        "holds": gone and live,
    }


def claim_no_children(term: str) -> dict:
    ols = ols_children(term)
    go = go_subgraph(term, "descendents")
    none = _agree(f"{term} has no children", not ols, not go)
    return {
        "term": term,
        "ols4_children": sorted(ols),
        "go_api_descendents": sorted(go),
        "holds": none,
    }


def claim_ancestry(term: str, must_be_under: str, must_not_be_under: str) -> dict:
    ols = ols_ancestors(term)
    go = go_subgraph(term, "ancestors")
    under = _agree(f"{term} under {must_be_under}", must_be_under in ols, must_be_under in go)
    not_under = _agree(
        f"{term} not under {must_not_be_under}",
        must_not_be_under not in ols,
        must_not_be_under not in go,
    )
    return {
        "term": term,
        "is_under": {must_be_under: under},
        "is_not_under": {must_not_be_under: not_under},
        "holds": under and not_under,
    }


CLAIMS = [
    ("GO:0005100 is merged into GO:0005096", lambda: claim_merged("GO:0005100", "GO:0005096")),
    ("GO:0005096 has no is_a children", lambda: claim_no_children("GO:0005096")),
    (
        "GO:0035024 is under GO:0051056 and not under GO:0007165",
        lambda: claim_ancestry("GO:0035024", "GO:0051056", "GO:0007165"),
    ),
    (
        "GO:0035021 is under GO:0051056 and not under GO:0007165",
        lambda: claim_ancestry("GO:0035021", "GO:0051056", "GO:0007165"),
    ),
]


def self_test() -> int:
    # Each predicate is run against a case whose answer is the opposite, so a pass above is
    # evidence the check discriminates rather than evidence that it always returns True.
    live = claim_merged("GO:0005096", "GO:0005096")
    assert not live["holds"], "claim_merged calls a live term obsolete"

    parent = claim_no_children("GO:0051056")
    assert not parent["holds"], (
        "claim_no_children says GO:0051056 is a leaf; it has the Rho/Rac regulation terms "
        "under it, so this check is not discriminating"
    )

    inverted = claim_ancestry("GO:0035024", "GO:0007165", "GO:0051056")
    assert not inverted["holds"], "claim_ancestry accepts a reversed ancestry assertion"

    print("self-test OK: each claim predicate returns False on a case where it should")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    failures = 0
    for name, fn in CLAIMS:
        result = fn()
        status = "HOLDS" if result["holds"] else "FAILS"
        print(f"{status}  {name}")
        print(f"        {json.dumps(result, sort_keys=True)}")
        if not result["holds"]:
            failures += 1
    print(f"\n{len(CLAIMS)} claim(s) checked on OLS4 and api.geneontology.org, {failures} failing")
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ClaimError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
