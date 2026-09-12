"""Do the other dynactin subunits share ACTR10's granule/extracellular annotations?

Four `REMOVE` decisions in this review rest on a cross-subunit count: if dynactin were
genuinely packaged into neutrophil granules, its subunits would be annotated there as a set,
not one at a time. That number was the only quantitative claim in the review with no module
behind it, and it drifted twice while it was prose - first because not all subunits had been
checked, then because ACTR1B was miscounted inside the canonical roster. So it is computed
here instead.

The canonical roster is the 11 proteins named in UniProt's SUBUNIT line for Q9NZ32:
DCTN1, DCTN2 and DCTN3 (shoulder); ACTR1A and ACTB (filament); CAPZA1 and CAPZB (barbed
end); ACTR10, DCTN4, DCTN5 and DCTN6 (pointed end). ACTR1B is queried alongside but scored
separately: it is the beta-centractin paralog that substitutes for ACTR1A in a fraction of
dynactin, so it is a twelfth protein rather than one of the 11, and conflating the two is
exactly the error this module exists to prevent.

Evidence codes are reported per annotation, because the distinction between a Reactome `TAS`
term and an `HDA` mass-spectrometry term matters to the argument: ACTB carries an
extracellular term by HDA, which is a different artefact class from the Reactome
granule-set route under review here.

Scope of the screen, stated because it bounds what the counts mean. The three terms queried
are exactly the ones removed from ACTR10, so the question answered is "do the other subunits
carry *these* annotations", and route classification is then applied to whatever they return.
Within this panel every route-derived annotation set also contains `GO:0005576`, so the
screen caught the route for every protein here. It is *not* established that this holds in
general: a Neutrophil-degranulation reaction that emitted a granule-lumen term without
`GO:0005576` would be missed by this screen, and Reactome's `containedEvents` endpoint was
returning HTTP 521 when this was checked, so the claim was left unverified rather than
asserted.

Route classification is a hard dependency on Reactome's ContentService, which returned
HTTP 521 for several minutes while this module was being written. The failure is deliberately
left loud: degrading to "route unknown" would emit a *different, weaker* report that still
looked complete, which is the failure this campaign has been bitten by before. So the module
aborts and the committed RESULTS.md simply cannot be regenerated while Reactome is down -
that is the intended trade.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request

# (symbol, accession, sub-structure, in_canonical_11)
# DCTN3 is O75935. O15507 is an INACTIVE (deleted) UniProt entry: it returns no gene name
# and no annotations, so querying it looks indistinguishable from a subunit that genuinely
# carries nothing. An earlier hand-check of this roster used it and therefore never actually
# tested DCTN3 - hence the entry name is printed for every accession below.
SUBUNITS = [
    ("DCTN1", "Q14203", "shoulder / projecting sidearm", True),
    ("DCTN2", "Q13561", "shoulder", True),
    ("DCTN3", "O75935", "shoulder", True),
    ("ACTR1A", "P61163", "Arp1 filament", True),
    ("ACTB", "P60709", "filament (single beta-actin subunit)", True),
    ("CAPZA1", "P52907", "barbed end", True),
    ("CAPZB", "P47756", "barbed end", True),
    ("ACTR10", "Q9NZ32", "pointed end - the gene under review", True),
    ("DCTN4", "Q9UJW0", "pointed end", True),
    ("DCTN5", "Q9BTE1", "pointed end", True),
    ("DCTN6", "O00399", "pointed end", True),
    ("ACTR1B", "P42025", "Arp1 paralog, substitutes for ACTR1A", False),
]

# The three terms removed from ACTR10 in this review.
TERMS = {
    "GO:0005576": "extracellular region",
    "GO:0035578": "azurophil granule lumen",
    "GO:1904813": "ficolin-1-rich granule lumen",
}
REACTOME_EVIDENCE = "TAS"

# The route under review: ACTR10's granule terms all descend from Reactome's Neutrophil
# degranulation pathway, whose protein sets come from bulk granule proteomics. A Reactome TAS
# term is only evidence of *this* pattern if its reaction sits under that pathway - CAPZA1,
# for instance, carries an extracellular-region TAS from an unrelated S100B/AGER reaction,
# and counting that alongside ACTR10's would overstate how shared the pattern is.
NEUTROPHIL_DEGRANULATION = "R-HSA-6798695"


def http_json(url: str, tries: int = 4) -> dict:
    last = None
    for attempt in range(tries):
        # Reactome rejects the default urllib user-agent with HTTP 403, so one is set.
        req = urllib.request.Request(
            url,
            headers={"Accept": "application/json", "User-Agent": "ai-gene-review/ACTR10"},
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries} tries: {url}") from last


def assert_not_truncated(payload: dict, url: str) -> None:
    """Fail if QuickGO reported more hits than one page returned.

    A `limit=100` query that silently drops page 2 is the same class of defect as a
    denominator that silently shrinks: the result still looks complete.
    """
    hits = payload.get("numberOfHits")
    got = len(payload.get("results", []))
    if hits is not None and hits > got:
        raise SystemExit(
            f"truncated result: QuickGO reports {hits} hits but only {got} were returned "
            f"for {url} - raise the limit or paginate before trusting the counts."
        )


def entry_name(acc: str) -> str:
    """Entry name for `acc`, failing loudly unless UniProt returns that exact accession.

    This is the guard that O15507 defeated. O15507 is a dead accession, MERGED into
    P56159 (GFRA1), and it stood in for DCTN3 here for three rounds: it returns no gene
    name and no GO annotations, so it is indistinguishable from a subunit that genuinely
    carries nothing - the quietest possible false negative.

    Two weaker checks do not work, both tested against the live API:

    * Printing `uniProtkbId` does not expose it. UniProt *follows the merge*, so the
      request returns `GFRA1_HUMAN` - a different protein's identity - which reads as a
      perfectly healthy answer.
    * `entryType` does not discriminate reliably either. Repeated identical requests for
      this accession returned `entryType: "Inactive"` on some and
      `entryType: "UniProtKB reviewed (Swiss-Prot)"` with `uniProtkbId: "GFRA1_HUMAN"` on
      others, so a check on that field passes or fails by luck.

    What does hold in every observed response is that the returned `primaryAccession` is
    the *merge target* (P56159), never the accession asked for. So identity is asserted on
    `primaryAccession`, with the `entryType`/`inactiveReason` stub case caught as well. A
    wrong accession in this hand-written roster is a code defect rather than ambiguous
    data, so it stops the run and names the lookup that fixes it.
    """
    d = http_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=id")
    returned = d.get("primaryAccession")
    entry_type = d.get("entryType", "")
    if returned != acc or "Inactive" in entry_type:
        raise SystemExit(
            f"bad input: UniProt accession {acc} is not a live entry - the request returned "
            f"primaryAccession={returned!r}, entryType={entry_type!r}, "
            f"inactiveReason={d.get('inactiveReason')}. It has most likely been merged or "
            "demerged. Replace it in SUBUNITS with the current accession, found via "
            "https://rest.uniprot.org/uniprotkb/search?query=gene_exact:<SYMBOL>+AND+organism_id:9606+AND+reviewed:true"
        )
    return d["uniProtkbId"]


def annotations(acc: str) -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    """Annotations for the three terms under review, and any others QuickGO returned.

    QuickGO's comma-separated `goId` filter does not constrain the result set to exactly the
    requested terms - it also returns related terms such as GO:0070062 extracellular exosome.
    Scoring is therefore done client-side against TERMS, and anything else that came back is
    returned separately and reported rather than discarded, since it is informative: the
    exosome annotations are the HDA mass-spectrometry artefact class, distinct from the
    Reactome granule-set route under review.
    """
    url = "https://www.ebi.ac.uk/QuickGO/services/annotation/search?" + urllib.parse.urlencode(
        {"geneProductId": f"UniProtKB:{acc}", "goId": ",".join(TERMS), "limit": 100}
    )
    payload = http_json(url)
    assert_not_truncated(payload, url)
    got = {
        (r["goId"], r["goEvidence"], r.get("reference") or "-")
        for r in payload.get("results", [])
    }
    wanted = sorted(a for a in got if a[0] in TERMS)
    other = sorted(a for a in got if a[0] not in TERMS)
    return wanted, other


def reactome_route(stable_id: str) -> tuple[str, bool]:
    """(reaction display name, is it under Neutrophil degranulation?) for a Reactome id."""
    d = http_json(f"https://reactome.org/ContentService/data/query/{stable_id}")
    name = d.get("displayName", "?")
    anc = http_json(f"https://reactome.org/ContentService/data/event/{stable_id}/ancestors")
    ids = {e.get("stId") for branch in anc for e in branch} if anc else set()
    return name, NEUTROPHIL_DEGRANULATION in ids


def main() -> str:
    lines: list[str] = []
    out = lines.append
    out("## F. Granule and extracellular annotation across the dynactin subunits")
    out("")
    out(
        "QuickGO annotations to the three terms removed from ACTR10 in this review, across the "
        "11 canonical dynactin subunits named in UniProt's SUBUNIT line for Q9NZ32, plus "
        "ACTR1B scored separately as a twelfth protein. Evidence codes are shown because a "
        "Reactome `TAS` term and an `HDA` mass-spectrometry term are different artefact "
        "classes."
    )
    out("")
    out(
        "| gene | UniProt | entry name | dynactin sub-structure | in canonical 11 | "
        "annotations to the three terms | other terms QuickGO returned |"
    )
    out("|---|---|---|---|---|---|---|")
    canonical_any: list[str] = []
    canonical_tas: list[str] = []
    canonical_route: list[str] = []
    canonical_azurophil: list[str] = []
    noncanonical_route: list[str] = []
    route_cache: dict[str, tuple[str, bool]] = {}
    for symbol, acc, where, canonical in SUBUNITS:
        name = entry_name(acc)
        anns, other = annotations(acc)
        cell = (
            "; ".join(f"{gid} {TERMS[gid]} ({ev}, {ref})" for gid, ev, ref in anns)
            if anns
            else "**none**"
        )
        other_cell = (
            "; ".join(f"{gid} ({ev}, {ref})" for gid, ev, ref in other) if other else "-"
        )
        out(
            f"| {symbol} | {acc} | {name} | {where} | {'yes' if canonical else 'no'} | "
            f"{cell} | {other_cell} |"
        )
        has_tas = any(ev == REACTOME_EVIDENCE for _, ev, _ in anns)
        # A Reactome TAS only counts as this pattern if its reaction is under Neutrophil
        # degranulation; the route is resolved from Reactome, not guessed from the id.
        on_route = False
        for gid, ev, ref in anns:
            if ev != REACTOME_EVIDENCE or not ref.startswith("Reactome:"):
                continue
            stable = ref.split(":", 1)[1]
            if stable not in route_cache:
                route_cache[stable] = reactome_route(stable)
            if route_cache[stable][1]:
                on_route = True
        if canonical:
            if anns:
                canonical_any.append(symbol)
            if has_tas:
                canonical_tas.append(symbol)
            if on_route:
                canonical_route.append(symbol)
            if any(gid == "GO:0035578" for gid, _, _ in anns):
                canonical_azurophil.append(symbol)
        elif on_route:
            noncanonical_route.append(symbol)
    n_canon = sum(1 for *_, c in SUBUNITS if c)
    out("")
    out(
        f"- canonical subunits carrying any of the three terms by any evidence code: "
        f"{len(canonical_any)}/{n_canon} ({', '.join(canonical_any) if canonical_any else 'none'})"
    )
    out(
        f"- canonical subunits carrying any of the three terms by Reactome TAS: "
        f"{len(canonical_tas)}/{n_canon} ({', '.join(canonical_tas) if canonical_tas else 'none'})"
    )
    out(
        f"- canonical subunits annotated to GO:0035578 azurophil granule lumen: "
        f"{len(canonical_azurophil)}/{n_canon} "
        f"({', '.join(canonical_azurophil) if canonical_azurophil else 'none'})"
    )
    out(
        f"- canonical subunits whose Reactome TAS comes from the Neutrophil degranulation "
        f"route: {len(canonical_route)}/{n_canon} "
        f"({', '.join(canonical_route) if canonical_route else 'none'})"
    )
    out(
        "- outside the canonical 11, on the Neutrophil degranulation route: "
        + (", ".join(noncanonical_route) if noncanonical_route else "none")
    )
    out("")
    if route_cache:
        out("Reactome reactions behind the TAS annotations above:")
        out("")
        out("| reaction | name | under Neutrophil degranulation (R-HSA-6798695)? |")
        out("|---|---|---|")
        for stable, (name, under) in sorted(route_cache.items()):
            out(f"| {stable} | {name} | {'yes' if under else '**no**'} |")
        out("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.stdout.write(main())
