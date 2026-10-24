"""Fetch the QuickGO record for every term this review proposes or argues about.

`just validate` passing is not proof a term is current, and OLS reports a MERGED
id and an ABSENT id identically. QuickGO's `/complete` endpoint carries
`isObsolete` and `secondaryIds`, which distinguishes them. Read the DEFINITION,
not the label -- a label can be right while the definition excludes the case.

Also prints the is_a/part_of ancestor set, which is what decides whether a
proposed replacement really is more specific than the row it replaces.

Run: uv run python check_terms.py
"""

from __future__ import annotations

import json

from uniprot import _cached_get

TERMS = [
    "GO:0005634",  # nucleus (IBA + SubCell IEA rows)
    "GO:0005737",  # cytoplasm
    "GO:0005829",  # cytosol
    "GO:0005886",  # plasma membrane
    "GO:0030315",  # T-tubule
    "GO:0042383",  # sarcolemma
    "GO:0043484",  # regulation of RNA splicing
    "GO:0043034",  # costamere  -- proposed
    "GO:0042803",  # protein homodimerization activity -- proposed
    "GO:0030018",  # Z disc
    "GO:0030659",  # cytoplasmic vesicle membrane
    "GO:0060090",  # molecular adaptor activity
    "GO:0005515",  # protein binding
]
SHOW_ANCESTORS_FOR = {"GO:0043034", "GO:0042383", "GO:0030315", "GO:0042803"}


def term(t: str) -> dict:
    return json.loads(_cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{t}/complete",
        f"term_{t.replace(':', '_')}",
    ))["results"][0]


def ancestors(t: str) -> list[str]:
    d = json.loads(_cached_get(
        f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{t}/ancestors"
        "?relations=is_a,part_of",
        f"anc_{t.replace(':', '_')}",
    ))["results"][0]
    return d.get("ancestors", [])


def main() -> None:
    names = {}
    for t in TERMS:
        d = term(t)
        names[t] = d["name"]
        flag = "  *** OBSOLETE ***" if d.get("isObsolete") else ""
        print(f"{t}  {d['name']}  [{d['aspect']}]{flag}")
        if d.get("secondaryIds"):
            print(f"    merged ids: {d['secondaryIds']}")
        print(f"    def: {d.get('definition', {}).get('text', '')}")
        print()

    print("=== is_a/part_of ancestor sets (decides 'more specific than') ===")
    for t in sorted(SHOW_ANCESTORS_FOR):
        anc = ancestors(t)
        labelled = []
        for a in anc:
            if a == t:
                continue
            labelled.append(f"{a} {names.get(a) or term(a)['name']}")
        print(f"{t} {names[t]}: {len(labelled)} ancestors")
        for line in sorted(labelled):
            print(f"    {line}")
        print()


if __name__ == "__main__":
    main()
