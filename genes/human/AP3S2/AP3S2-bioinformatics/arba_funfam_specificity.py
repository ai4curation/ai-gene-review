"""Is ARBA00033921 -- the rule behind AP3S2's GO:0030123 IEA -- specific to AP-3?

The GOA row `GO:0030123 AP-3 adaptor complex / IEA / GO_REF:0000120` carries
`WITH/FROM = ARBA:ARBA00033921|InterPro:IPR027155`. GO_REF:0000120 combines
several automatic methods, so it is worth knowing what each half asserts.

`ARBA00033921` is fetched live from https://rest.uniprot.org/arba/ and its
condition set printed. The rule fires on a FunFam signature plus a taxon, and
FunFam signatures carry family-level names ("AP complex subunit sigma"), which
is the shape of condition that can over-generalise: were the same FunFam to
cover the AP-1, AP-2 and AP-4 sigma subunits, the rule would call every one of
them AP-3. Whether it does is an empirical question, not something to assume in
either direction.

This script settles it by reading the FunFam cross-reference off every reviewed
human AP-complex sigma subunit and reporting which ones would satisfy the rule.
The panel is the complete set of human sigma subunits, not a hand-picked subset.

Output: arba_funfam_specificity.tsv
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import requests

HERE = Path(__file__).parent
CACHE = HERE / "cache"
OUT = HERE / "arba_funfam_specificity.tsv"

RULE = "ARBA00033921"

# Every reviewed human AP-complex sigma subunit, by complex. The first seven are the
# complete human membership of PANTHER family PTHR11753 (checked against
# interpro/panther/PTHR11753/PTHR11753-entries.csv); AP5S1 is the reviewed human sigma
# subunit that sits outside that family, and is included so the panel is the full set of
# human AP sigma subunits rather than just the family's.
PANEL = [
    ("P61966", "AP1S1", "AP-1"),
    ("P56377", "AP1S2", "AP-1"),
    ("Q96PC3", "AP1S3", "AP-1"),
    ("P53680", "AP2S1", "AP-2"),
    ("Q92572", "AP3S1", "AP-3"),
    ("P59780", "AP3S2", "AP-3"),
    ("Q9Y587", "AP4S1", "AP-4"),
    ("Q9NUS5", "AP5S1", "AP-5"),
]

FUNFAM_RE = re.compile(r"^DR   FunFam; (\S+);", re.M)


def cached(url: str, key: str, accept: str = "text/plain") -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / key
    if path.exists():
        return path.read_text()
    resp = requests.get(url, headers={"Accept": accept}, timeout=60)
    resp.raise_for_status()
    path.write_text(resp.text)
    return resp.text


def main() -> int:
    rule = json.loads(cached(f"https://rest.uniprot.org/arba/{RULE}",
                             f"arba_{RULE}.json", "application/json"))
    print(f"{RULE} (created {rule.get('createdDate')}, modified {rule.get('modifiedDate')})")
    conditions: list[str] = []
    for cs in rule["mainRule"]["conditionSets"]:
        for cond in cs["conditions"]:
            vals = "|".join(v["value"] for v in cond["conditionValues"])
            neg = "NOT " if cond.get("isNegative") else ""
            conditions.append(f"{neg}{cond['type']}={vals}")
            print(f"  condition: {neg}{cond['type']} = {vals}")
    asserted = [d["dbReference"]["id"] for d in rule["mainRule"]["annotations"]
                if d.get("dbReference", {}).get("database") == "GO"]
    print(f"  asserts: {', '.join(asserted)}")

    funfams = [c.split("=", 1)[1] for c in conditions if c.startswith("FunFam id=")]
    if not funfams:
        print("rule has no FunFam condition; nothing to test")
        return 1
    rule_funfam = funfams[0]

    seen: set[str] = set()
    rows = []
    print(f"\nWhich human AP-complex sigma subunits carry FunFam {rule_funfam}?")
    for acc, symbol, complex_ in PANEL:
        if acc in seen:
            continue
        seen.add(acc)
        txt = cached(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", f"flat_{acc}.txt")
        ffs = FUNFAM_RE.findall(txt)
        match = rule_funfam in ffs
        print(f"  {symbol:6s} {acc}  {complex_:4s}  FunFam={','.join(ffs) or '-':24s} "
              f"{'MATCHES RULE' if match else ''}")
        rows.append([symbol, acc, complex_, ",".join(ffs), str(match)])

    matched = [r for r in rows if r[4] == "True"]
    wrong = [r for r in matched if r[2] != "AP-3"]
    print(f"\npanel: {len(rows)} sigma subunits; matching the rule: {len(matched)} "
          f"({', '.join(r[0] for r in matched)})")
    print(f"non-AP-3 subunits that would be called AP-3 by this rule: {len(wrong)}"
          + (f" ({', '.join(r[0] for r in wrong)})" if wrong else ""))

    with OUT.open("w") as fh:
        fh.write("symbol\taccession\tcomplex\tfunfams\tmatches_ARBA00033921\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print(f"wrote {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
