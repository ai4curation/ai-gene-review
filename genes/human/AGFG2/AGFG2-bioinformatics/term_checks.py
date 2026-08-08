#!/usr/bin/env python3
"""Verify, against QuickGO, every term-level fact the AGFG2 review leans on.

Nothing here is inferred from a label. For each id the script records
``isObsolete``, ``secondaryIds`` (which distinguishes a MERGED id from an absent
one — OLS reports both identically), the definition, and the direct parents/
children needed for the specific claims made in the review:

* ``GO:0005096`` has no substrate-specific children (the ARF-specific GAP terms
  were merged into it), so no child can be proposed for "ARF GAP activity".
* ``GO:0008060`` must resolve as a *secondary id of* ``GO:0005096``, not as a
  live term.
* ``GO:0031410`` must be a descendant of ``GO:0005737`` (else the two location
  rows are not redundant with one another).
* whether GO has any live term for von Willebrand factor secretion or
  Weibel-Palade body exocytosis, and which already-curated siblings exist under
  ``GO:0045055``.
* the ancestor set of any candidate replacement/NEW term.
"""

from __future__ import annotations

import json
import pathlib
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import get_json, quickgo_annotations, quickgo_term  # noqa: E402

HERE = pathlib.Path(__file__).parent

IDS = [
    "GO:0005737", "GO:0031410", "GO:0001675", "GO:0007289", "GO:0045109",
    "GO:0005096", "GO:0016020", "GO:0045055", "GO:0033093", "GO:0008060",
    "GO:0002576", "GO:0060471", "GO:0044794", "GO:1903077", "GO:0017157",
    "GO:0046784", "GO:0006406", "GO:0031267", "GO:0060090",
]

# claim -> (child, ancestor) pairs that must hold
ANCESTRY_CLAIMS = [
    ("GO:0031410", "GO:0005737"),   # cytoplasmic vesicle is under cytoplasm
    ("GO:0045055", "GO:0006887"),   # regulated exocytosis is under exocytosis
    ("GO:0002576", "GO:0045055"),   # platelet degranulation is a curated sibling
    ("GO:0060471", "GO:0045055"),   # cortical granule exocytosis likewise
]


def term(go_id: str) -> dict:
    t = quickgo_term(go_id)
    return {
        "id": t["id"],
        "name": t.get("name"),
        "aspect": t.get("aspect"),
        "isObsolete": t.get("isObsolete"),
        "secondaryIds": t.get("secondaryIds"),
        "definition": (t.get("definition") or {}).get("text"),
        "replacements": t.get("replacements"),
        "children": [(c["id"], c.get("name"), c.get("relation"))
                     for c in (t.get("children") or [])],
        "parents": [(h["id"], h.get("name"), h.get("relation"))
                    for h in (t.get("history") or []) if False] or None,
    }


def ancestors(go_id: str) -> list[str]:
    url = ("https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
           + urllib.parse.quote(go_id)
           + "/ancestors?relations=is_a,part_of")
    d = get_json(url)
    return d["results"][0].get("ancestors") or []


def main() -> None:
    out: dict = {"terms": {}, "ancestry_claims": {}, "extra": {}}
    for i in IDS:
        out["terms"][i] = term(i)

    for child, anc in ANCESTRY_CLAIMS:
        anc_set = ancestors(child)
        out["ancestry_claims"][f"{child} under {anc}"] = {
            "holds": anc in anc_set,
            "n_ancestors": len(anc_set),
        }

    # GO:0008060 must be a MERGED id, i.e. a secondaryId of GO:0005096.
    sec = out["terms"]["GO:0005096"]["secondaryIds"] or []
    out["extra"]["GO_0008060_is_secondary_of_GO_0005096"] = "GO:0008060" in sec

    # Live children of GO:0005096: is there any substrate-specific GAP term left?
    out["extra"]["GO_0005096_children"] = out["terms"]["GO:0005096"]["children"]

    # Curated siblings under regulated exocytosis, to show the class is curatable.
    out["extra"]["GO_0045055_children"] = out["terms"]["GO:0045055"]["children"]

    # Children of GO:0044794, to check whether a more specific host/viral term exists.
    out["extra"]["GO_0044794_children"] = out["terms"]["GO:0044794"]["children"]

    # Human usage of every candidate term the review either chose or declined, so the
    # "actively used" / "zero annotations" claims are evidence in the repository rather
    # than assertions made in a conversation.  GO:0045055 is the non-zero control that
    # makes the GO:0046784 zero interpretable.
    for go in ("GO:0046784", "GO:0044794", "GO:1903077", "GO:0045055", "GO:0031623"):
        rows = quickgo_annotations(goId=go, goUsage="descendants",
                                   goUsageRelationships="is_a,part_of",
                                   taxonId="9606", limit=100)
        out["extra"][f"human_usage_{go.replace(':', '_')}"] = {
            "goId": go,
            "n_annotations": len(rows),
            "n_entities": len({r["geneProductId"] for r in rows}),
            "evidence": sorted({r["goEvidence"] for r in rows}),
        }
    ctrl = out["extra"]["human_usage_GO_0045055"]["n_annotations"]
    if ctrl == 0:
        raise AssertionError(
            "positive control GO:0045055 returned 0 human annotations — the query "
            "pattern is broken, so the GO:0046784 zero is uninterpretable"
        )

    (HERE / "term_checks.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    for i, t in out["terms"].items():
        print(f"{i} {t['name']!r} aspect={t['aspect']} obsolete={t['isObsolete']} "
              f"secondaryIds={t['secondaryIds']}")
    print("\nancestry claims:")
    for k, v in out["ancestry_claims"].items():
        print(f"  {k}: {v['holds']} (n_ancestors={v['n_ancestors']})")
    print(f"\nGO:0008060 is a secondaryId of GO:0005096: "
          f"{out['extra']['GO_0008060_is_secondary_of_GO_0005096']}")
    print(f"\nlive children of GO:0005096: {out['extra']['GO_0005096_children']}")
    print(f"\nchildren of GO:0045055 (regulated exocytosis):")
    for c in out["extra"]["GO_0045055_children"] or []:
        print(f"   {c}")
    print(f"\nchildren of GO:0044794:")
    for c in out["extra"]["GO_0044794_children"] or []:
        print(f"   {c}")
    print("\nhuman usage of the candidate terms:")
    for k, v in out["extra"].items():
        if k.startswith("human_usage_"):
            print(f"  {v['goId']}: {v['n_annotations']} annotations over "
                  f"{v['n_entities']} entities; evidence={v['evidence']}")
    print("\ndefinitions of the terms the argument turns on:")
    for i in ("GO:0005096", "GO:0016020", "GO:0045055", "GO:0044794", "GO:0031410",
              "GO:0045109", "GO:0046784"):
        print(f"  {i} {out['terms'][i]['name']}: {out['terms'][i]['definition']}")


if __name__ == "__main__":
    main()
