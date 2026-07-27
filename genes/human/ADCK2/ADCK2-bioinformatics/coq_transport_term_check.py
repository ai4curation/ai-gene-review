#!/usr/bin/env python3
"""Does GO contain a term for coenzyme Q / ubiquinone transport or distribution?

Why this script exists
----------------------
The first version of this claim was established by enumerating the descendants of
``GO:0006743 ubiquinone metabolic process`` and observing that none of them is a transport
term.  A reviewer pointed out that this is the wrong query and cannot support the
conclusion: a transport term would never be classified under a metabolic-process term, so
that enumeration was guaranteed to find nothing regardless of whether such a term exists.

The claim is load-bearing (it justifies a ``proposed_new_terms`` entry), so it is
re-established here from two directions that *could* return a hit:

1. **Label sweep.** Every GO term whose **label** matches one of the ``KEYWORDS`` is
   retrieved (QuickGO's text search also indexes synonyms, but the filter applied here is
   on the label alone), and each is classified by whether it reads as transport or
   localization.  If a CoQ transport term exists under any name, it must appear here unless
   its label avoids every keyword.
2. **Branch sweep.** The descendants of the relevant transport/localization terms are
   enumerated and searched for any ubiquinone-specific child.  This catches a term whose
   label uses different words but which is correctly classified.

Either sweep alone is weak; together they cover both failure modes.  The script prints
what it found rather than asserting absence, and reports the two sweeps separately.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"

# Roots under which a CoQ transport/distribution term would have to sit.
TRANSPORT_ROOTS = {
    "GO:0006869": "lipid transport",
    "GO:0010876": "lipid localization",
    "GO:0032365": "intracellular lipid transport",
    "GO:0120009": "intermembrane lipid transfer",
    "GO:0006810": "transport",
}

# "quinol" is NOT covered by "quinone" -- the two words share no such substring, and GO
# does name terms after the reduced form ("mitochondrial electron transport, ubiquinol to
# cytochrome c", "3-demethylubiquinol 3-O-methyltransferase activity"). Omitting it left
# BOTH sweeps blind to a hypothetical "ubiquinol transport" term, which is precisely the
# shared blind spot the two-sweep design exists to rule out. "quinol" subsumes "ubiquinol"
# as a substring, so listing it once is sufficient.
KEYWORDS = ("ubiquinone", "coenzyme q", "quinone", "quinol")
TRANSPORTY = ("transport", "localization", "localisation", "distribution", "transfer",
              "translocation", "import", "export", "efflux", "influx", "trafficking")

# "electron transport" is a different sense of the word: there the ELECTRON is the cargo
# and the quinone is the acceptor, so those terms say nothing about moving CoQ itself. A
# bare substring test on "transport" conflates the two, which is why the first run of this
# script reported 8 spurious hits. Every exclusion below is printed with its reason, so
# the filtering is auditable rather than hidden inside the verdict.
EXCLUDE_LABEL = ("electron transport",)

# Widening KEYWORDS with "quinol" immediately produced the mirror of the same trap:
# "quinol" is a substring of "quinolinic"/"quinoline", an unrelated tryptophan-pathway
# chemical family, and GO:1903222 "quinolinic acid transmembrane transport" sailed through
# every other filter as a genuine transport process. Excluded only when the false friend is
# the SOLE reason the label matched (see matched_only_via_quinoline), so a label that also
# names a real CoQ species still survives to be judged on its merits.
QUINOLINE_FALSE_FRIEND = "quinolin"


def matched_only_via_quinoline(label: str) -> bool:
    """True when a label matches KEYWORDS *solely* through a 'quinolin' occurrence.

    Testing 'quinolin in label and no real CoQ species named' is not good enough: a label
    like "pyrroloquinoline quinone biosynthetic process" contains 'quinolin' AND matches on
    its own 'quinone', so that test would exclude it while reporting the wrong reason.
    Deleting the false-friend substring and re-testing is exact -- whatever keyword still
    matches did not come from 'quinolin'.
    """
    low = label.lower()
    if QUINOLINE_FALSE_FRIEND not in low:
        return False
    cleaned = low.replace(QUINOLINE_FALSE_FRIEND, "")
    return not any(k in cleaned for k in KEYWORDS)


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    return json.load(urllib.request.urlopen(req))


def paged_search(query: str, limit: int = 100) -> list[dict]:
    """Ontology text search, paging until exhausted. Never infer a total from page size."""
    out: list[dict] = []
    page = 1
    while True:
        url = f"{QUICKGO}/ontology/go/search?" + urllib.parse.urlencode(
            {"query": query, "limit": limit, "page": page}
        )
        d = get(url)
        results = d.get("results") or []
        out.extend(results)
        total = d.get("numberOfHits", 0)
        if not results or len(out) >= total or page >= 20:
            if len(out) < total and page >= 20:
                raise SystemExit(
                    f"FATAL: paging stopped at page 20 with {len(out)}/{total} results for "
                    f"{query!r}; raise the cap rather than reporting a partial sweep."
                )
            break
        page += 1
        time.sleep(0.2)
    return out


def descendants(term: str) -> list[str]:
    d = get(f"{QUICKGO}/ontology/go/terms/{term}/descendants?relations=is_a,part_of")
    return d["results"][0].get("descendants") or []


def label_of(ids: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i: i + 50]
        d = get(f"{QUICKGO}/ontology/go/terms/" + ",".join(chunk))
        for r in d["results"]:
            out[r["id"]] = r["name"]
        time.sleep(0.15)
    return out


def main() -> int:
    print("=" * 72)
    kw_str = " / ".join(KEYWORDS)
    print(f"SWEEP 1: every GO term whose label mentions {kw_str}")
    print("=" * 72)
    seen: dict[str, str] = {}
    for kw in KEYWORDS:
        for r in paged_search(kw):
            name = (r.get("name") or "")
            if any(k in name.lower() for k in KEYWORDS):
                seen[r["id"]] = name
    print(f"{len(seen)} terms whose LABEL contains one of {KEYWORDS}")
    hits1 = {i: n for i, n in seen.items() if any(t in n.lower() for t in TRANSPORTY)}
    if hits1:
        print("  transport/localization-flavoured labels among them:")
        for i, n in sorted(hits1.items()):
            print(f"    {i}  {n}")
    else:
        print("  none of them has a transport/localization-flavoured label")

    print()
    print("=" * 72)
    print("SWEEP 2: descendants of the transport/localization roots, searched for CoQ terms")
    print("=" * 72)
    hits2: dict[str, str] = {}
    for root, root_label in TRANSPORT_ROOTS.items():
        kids = descendants(root)
        labels = label_of(kids)
        matched = {
            i: n for i, n in labels.items() if any(k in n.lower() for k in KEYWORDS)
        }
        print(f"{root} {root_label}: {len(kids)} descendants, "
              f"{len(matched)} mentioning {kw_str}")
        for i, n in sorted(matched.items()):
            print(f"    {i}  {n}")
        hits2.update(matched)

    print()
    print("=" * 72)
    print("ADJUDICATION: which candidates actually describe moving CoQ as cargo?")
    print("=" * 72)
    candidates = sorted(set(hits1) | set(hits2))
    meta = {}
    for i in range(0, len(candidates), 50):
        d = get(f"{QUICKGO}/ontology/go/terms/" + ",".join(candidates[i: i + 50]))
        for r in d["results"]:
            meta[r["id"]] = r
        time.sleep(0.15)

    verdict = []
    for cid in candidates:
        r = meta.get(cid)
        if r is None:
            print(f"  ? {cid}: could not be fetched; treating as unresolved")
            verdict.append(cid)
            continue
        name, aspect = r["name"], r.get("aspect")
        if r.get("isObsolete"):
            print(f"  excluded {cid} ({name}): obsolete")
        elif any(x in name.lower() for x in EXCLUDE_LABEL):
            print(f"  excluded {cid} ({name}): 'electron transport' - the electron is the "
                  f"cargo, the quinone is the acceptor")
        elif matched_only_via_quinoline(name):
            print(f"  excluded {cid} ({name}): matched only because 'quinol' is a substring "
                  f"of 'quinolin'; quinoline/quinolinic acid is an unrelated chemical family")
        elif aspect != "biological_process":
            print(f"  excluded {cid} ({name}): aspect is {aspect}, not a transport process")
        else:
            verdict.append(cid)

    print()
    print("=" * 72)
    if verdict:
        print(f"FOUND {len(verdict)} genuine CoQ transport/localization term(s):")
        for i in verdict:
            print(f"  {i}  {meta[i]['name']}")
        print("A proposed_new_terms entry for CoQ distribution would be REDUNDANT.")
        return 1
    print("No GO term for ubiquinone/coenzyme Q transport, distribution or localization was")
    print("found by either sweep. The two sweeps are complementary: sweep 1 would catch a")
    print("term classified in the wrong branch, sweep 2 a term whose label avoids the word.")
    print("This is evidence of absence only to the extent those two together are exhaustive.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
