"""Are AGGF1's IntAct interactions independent experiments, or one screen?

UniProt's INTERACTION block lists 14 partners for AGGF1, almost all `NbExp=3`.
`NbExp` counts *sub-methods*, and a single Y2H screen is routinely logged as
`two hybrid array` + `two hybrid pooling` + `validated two hybrid` -- three rows
for one experiment. Expand the records and count distinct experiments and
distinct detection methods instead.

Also records which AGGF1 chain each interaction was measured on, and -- because
several IntAct records are logged against an isoform accession rather than the
canonical chain -- fetches each isoform's true length and asks whether that
isoform even contains the FHA domain, the G-patch and the 604-613 angiogenic
motif. A partner scored against a construct that stops short of a domain cannot
report on it. Domain boundaries are read from the canonical entry's feature
table, never hardcoded.

Run: uv run python intact_partners.py
"""

from __future__ import annotations

import json
from collections import Counter

from uniprot import _cached_get, uniprot_entry

ACC = "Q8N302"
# The mapped angiogenic motif (PMID:34551592, Fig. 6): not a UniProt feature, so
# it is carried here as the one literature-sourced coordinate in this script.
ANGIOGENIC_MOTIF = (604, 613)


def isoform_coverage() -> None:
    """Print each annotated isoform's length and which features it can contain."""
    entry = uniprot_entry(ACC)
    feats = {
        f["description"]: (f["location"]["start"]["value"], f["location"]["end"]["value"])
        for f in entry["features"]
        if f["type"] == "Domain"
    }
    feats["angiogenic motif (604-613)"] = ANGIOGENIC_MOTIF
    iso_ids = [
        iso["isoformIds"][0]
        for c in entry.get("comments", [])
        if c["commentType"] == "ALTERNATIVE PRODUCTS"
        for iso in c.get("isoforms", [])
    ]
    if not iso_ids:
        raise SystemExit(f"{ACC}: no ALTERNATIVE PRODUCTS isoforms found -- UniProt schema changed?")
    print("  isoform coverage of the domains this review adjudicates:")
    for iso in iso_ids:
        body = _cached_get(f"https://rest.uniprot.org/uniprotkb/{iso}.fasta", f"fa_{iso}",
                           accept="text/plain")
        seq = "".join(line for line in body.splitlines() if not line.startswith(">"))
        have = [name for name, (s, e) in feats.items() if len(seq) >= e]
        missing = [name for name, (s, e) in feats.items() if len(seq) < e]
        print(f"    {iso}: {len(seq):>4d} aa  contains={have or 'none'}  lacks={missing or 'none'}")
    print()


def main() -> None:
    # Paginate to completion. The guard compares the accumulated row count
    # against the server's own totalElements, never against the page size we
    # chose -- a server that clamps pageSize instead of erroring would sail
    # past the latter.
    page, size, rows, total = 0, 200, [], None
    while True:
        url = (f"https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/{ACC}"
               f"?page={page}&pageSize={size}")
        d = json.loads(_cached_get(url, f"intact_{ACC}_p{page}"))
        got = d.get("content", d if isinstance(d, list) else [])
        total = d.get("totalElements", len(got)) if total is None else total
        rows.extend(got)
        if not got or len(rows) >= total:
            break
        page += 1
        if page > 50:
            raise SystemExit("IntAct pagination did not terminate")
    if len(rows) != total:
        raise SystemExit(f"IntAct: read {len(rows)} rows but totalElements={total}")
    print(f"IntAct: {len(rows)} interaction evidence record(s) for {ACC} "
          f"(totalElements={total}, {page + 1} page(s))")

    methods = Counter(r.get("detectionMethod") for r in rows)
    pubs = Counter(r.get("publicationPubmedIdentifier") for r in rows)
    types = Counter(r.get("type") for r in rows)
    hosts = Counter(r.get("hostOrganism") for r in rows)
    print(f"  distinct publications: {len(pubs)}")
    for p, n in pubs.most_common():
        print(f"    PMID:{p}: {n} record(s)")
    print(f"  detection methods: {dict(methods)}")
    print(f"  interaction types: {dict(types)}")
    print(f"  host systems: {dict(hosts)}")
    print()

    def bare(v: str) -> str:
        return v.split(" ")[0]

    # Which AGGF1 chain was actually tested?
    isoforms: Counter[str] = Counter()
    partners: set[str] = set()
    for r in rows:
        for side in ("idA", "idB"):
            v = bare(r.get(side, ""))
            if v.split("-")[0] == ACC:
                isoforms[v] += 1
            else:
                partners.add(v)
    print(f"  AGGF1 chain tested: {dict(isoforms)}")
    print(f"  distinct partners: {len(partners)}")
    print()
    isoform_coverage()

    # How many of these partners reached GOA as a GO:0005515 row on AGGF1?
    d2 = json.loads(_cached_get(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId=UniProtKB:{ACC}&goId=GO:0005515&limit=100",
        "qg_aggf1_0005515"))
    if d2["numberOfHits"] > len(d2["results"]):
        raise SystemExit("truncated QuickGO GO:0005515 result")
    goa_partners = {
        x["id"] for r in d2["results"] for c in (r.get("withFrom") or [])
        for x in c.get("connectedXrefs", [])
    }
    print(f"  GO:0005515/GO:0042802 rows on AGGF1 in GOA: {d2['numberOfHits']}, "
          f"naming partners {sorted(goa_partners)}")
    print(f"  IntAct partners that reached GOA: "
          f"{sorted(goa_partners & {p.split('-')[0] for p in partners}) or 'none'}")
    print()

    # Per-partner detail for exactly the partners GOA turned into an annotation.
    # A curator has to decide each of these separately, so print the method,
    # publication, host system and which AGGF1 chain was used for each.
    print("=== every IntAct record naming a partner that GOA annotated ===")
    for acc in sorted(goa_partners):
        if acc == ACC:
            # Self-interaction: EVERY row has AGGF1 on one side, so require it on
            # both. Matching on "acc appears" would return the whole dataset.
            hits = [
                r for r in rows
                if bare(r.get("idA", "")).split("-")[0] == ACC
                and bare(r.get("idB", "")).split("-")[0] == ACC
            ]
        else:
            hits = [
                r for r in rows
                if acc in {bare(r.get("idA", "")).split("-")[0],
                           bare(r.get("idB", "")).split("-")[0]}
            ]
        print(f"  {acc}: {len(hits)} IntAct record(s)")
        seen = set()
        for r in hits:
            chains = sorted({bare(r.get(s, "")) for s in ("idA", "idB")})
            k = (r.get("publicationPubmedIdentifier"), r.get("detectionMethod"),
                 r.get("hostOrganism"), tuple(chains))
            if k in seen:
                continue
            seen.add(k)
            n = sum(
                1 for x in hits
                if (x.get("publicationPubmedIdentifier"), x.get("detectionMethod"),
                    x.get("hostOrganism"),
                    tuple(sorted({bare(x.get(s, "")) for s in ("idA", "idB")}))) == k
            )
            print(f"      PMID:{k[0]:<9} {k[1]:<44} x{n}  host={k[2]}  chains={'/'.join(chains)}")
    print()

    # A self-interaction detected in a proximity-labelling screen in which the
    # subject is the BAIT is a property of the method: a BirA*-fusion bait
    # biotinylates itself, so it is recovered by the streptavidin pull-down
    # whether or not it homodimerises. Y2H self-interaction is different -- the
    # DB and AD fusions have to associate. Print the experimental roles so the
    # distinction is derived from the record, not assumed.
    print("=== self-interaction records: method and experimental role ===")
    for r in rows:
        a = bare(r.get("idA", "")).split("-")[0]
        b = bare(r.get("idB", "")).split("-")[0]
        if a != ACC or b != ACC:
            continue
        print(f"  PMID:{r.get('publicationPubmedIdentifier'):<9} "
              f"{r.get('detectionMethod'):<44} type={r.get('type'):<20} "
              f"roleA={r.get('experimentalRoleA')} roleB={r.get('experimentalRoleB')} "
              f"miscore={r.get('intactMiscore')}")
    bio = [r for r in rows if r.get("detectionMethod") ==
           "proximity-dependent biotin identification"]
    roles = Counter(r.get("experimentalRoleA") for r in bio)
    print(f"  across all {len(bio)} proximity-labelling records, AGGF1's role as side A: "
          f"{dict(roles)}")


if __name__ == "__main__":
    main()
