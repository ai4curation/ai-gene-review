#!/usr/bin/env python3
"""Map FUNG-GROWTH carbon sources to GO biological-process terms.

Only term *labels* are written here. Every GO id in the output is resolved
from the label by an exact-label search against GO in OLS4
(https://www.ebi.ac.uk/ols4), and the hit is checked to be a current,
non-obsolete biological_process term with exactly that label. A label that
does not resolve is reported as UNRESOLVED rather than guessed.

The mapped term is the catabolic process for the substrate on the plate: a
NO_GROWTH call on that plate is evidence against an annotation saying the
organism carries out that process. Crude biomass plates (brans, pulps,
alfalfa meal) contain many polymers and have no single process term; casein
plates mix secreted proteolysis with amino-acid use. These are left
unmapped on purpose.

A second, activity tier lists substrate-specific enzyme activities (and
binding) whose annotation implies the organism can break the substrate down.
Some GO activity terms have descendants that act on other substrates:
beta-glucosidase activity (GO:0008422) subsumes cell-wall 1,3- and 1,6-
glucanases and steryl-glucosidases, so it is queried as the exact term only,
with its two cellobiose-specific children listed separately.

Writes data/carbon_source_go_map.tsv (process tier) and
data/carbon_source_go_activity_map.tsv (activity tier).
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

DATA = Path(__file__).parent / "data"
OLS = "https://www.ebi.ac.uk/ols4/api"

# carbon source (as named in FUNG-GROWTH) -> GO label of the catabolic process, or None with a reason
MAP: dict[str, tuple[str | None, str]] = {
    "D-glucose": ("glucose catabolic process", "monosaccharide"),
    "D-fructose": ("fructose catabolic process", "monosaccharide"),
    "D-galactose": ("galactose catabolic process", "monosaccharide"),
    "D-mannose": ("mannose catabolic process", "monosaccharide"),
    "D-xylose": ("D-xylose catabolic process", "monosaccharide"),
    "L-arabinose": ("L-arabinose catabolic process", "monosaccharide"),
    "L-rhamnose": ("rhamnose catabolic process", "monosaccharide"),
    "D-ribose": ("D-ribose catabolic process", "monosaccharide"),
    "D-galacturonic acid": ("galacturonate catabolic process", "sugar acid"),
    "D-glucuronic acid": ("glucuronate catabolic process", "sugar acid"),
    "cellobiose": ("cellobiose catabolic process", "disaccharide"),
    "lactose": ("lactose catabolic process", "disaccharide"),
    "maltose": ("maltose catabolic process", "disaccharide"),
    "sucrose": ("sucrose catabolic process", "disaccharide"),
    "raffinose": ("raffinose catabolic process", "trisaccharide"),
    "soluble starch 1%": ("starch catabolic process", "polysaccharide"),
    "cellulose 3%": ("cellulose catabolic process", "polysaccharide"),
    "inulin 1%": ("inulin catabolic process", "polysaccharide"),
    "guar gum 1%": ("galactomannan catabolic process", "polysaccharide (guar galactomannan)"),
    "apple pectin 1% pH=6": ("pectin catabolic process", "polysaccharide"),
    "citrus pectin 1% pH=6": ("pectin catabolic process", "polysaccharide"),
    "beechwood xylan 1%": ("xylan catabolic process", "polysaccharide"),
    "birchwood xylan 1%": ("xylan catabolic process", "polysaccharide"),
    "oat spelt xylan 1%": ("xylan catabolic process", "polysaccharide"),
    "arabic gum 1%": (None, "arabinogalactan-protein; GO has no arabinogalactan catabolic process term (checked in OLS4)"),
    "arabinogalactan 1%": (None, "GO has no arabinogalactan catabolic process term (checked in OLS4); plate never scored"),
    "lignin 1%": ("lignin catabolic process", "polyphenol"),
    "casein 3%": (None, "protein; plate mixes secreted proteolysis and amino-acid use"),
    "alfalfa meal 3%": (None, "crude plant biomass"),
    "citrus pulp 3% pH=6": (None, "crude plant biomass"),
    "cotton seed pulp 3%": (None, "crude plant biomass"),
    "rice bran 3%": (None, "crude plant biomass"),
    "soybean hulls 3%": (None, "crude plant biomass"),
    "sugar beet pulp 3%": (None, "crude plant biomass"),
    "wheat bran 3%": (None, "crude plant biomass"),
}


PECTIN = ["apple pectin 1% pH=6", "citrus pectin 1% pH=6"]
XYLAN = ["beechwood xylan 1%", "birchwood xylan 1%", "oat spelt xylan 1%"]
# (carbon sources, GO label, QuickGO goUsage, why the term implies use of the substrate)
ACTIVITY: list[tuple[list[str], str, str, str]] = [
    (["cellobiose"], "beta-glucosidase activity", "exact",
     "hydrolyses cellobiose to glucose; descendants are other-substrate glucanases, so exact term only"),
    (["cellobiose"], "cellobiose glucosidase activity", "descendants", "cellobiose-specific child of GO:0008422"),
    (["cellobiose"], "glucan 1,4-beta-glucosidase activity", "descendants",
     "exo-acting on cellodextrins, releases glucose from cellobiose"),
    (["cellobiose"], "cellulose catabolic process", "descendants",
     "cellobiose is the main product of cellulose breakdown and is degraded within this process"),
    (["soluble starch 1%"], "alpha-amylase activity", "descendants", "endo-hydrolysis of starch"),
    (["soluble starch 1%"], "glucan 1,4-alpha-glucosidase activity", "descendants", "glucoamylase, exo-hydrolysis of starch"),
    (["soluble starch 1%"], "starch binding", "descendants", "CBM20/21 starch-binding module"),
    (PECTIN, "polygalacturonase activity", "descendants", "hydrolyses homogalacturonan"),
    (PECTIN, "pectate lyase activity", "descendants", "eliminative cleavage of pectate"),
    (PECTIN, "pectin lyase activity", "descendants", "eliminative cleavage of methylated pectin"),
    (PECTIN, "pectinesterase activity", "descendants", "de-methylesterifies pectin"),
    (XYLAN, "endo-1,4-beta-xylanase activity", "descendants", "endo-hydrolysis of the xylan backbone"),
    (XYLAN, "xylan 1,4-beta-xylosidase activity", "descendants", "releases xylose from xylo-oligosaccharides"),
]


def get(url: str, retries: int = 4):
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.loads(r.read())
        except Exception as exc:
            if attempt == retries - 1:
                raise
            print(f"retry {url} ({exc})", file=sys.stderr)
            time.sleep(2 ** (attempt + 1))


def resolve(label: str, namespaces=("biological_process",)) -> dict:
    q = urllib.parse.urlencode({"q": label, "ontology": "go", "exact": "true",
                                "fieldList": "obo_id,label,iri,is_obsolete"})
    docs = get(f"{OLS}/search?{q}")["response"]["docs"]
    hits = [d for d in docs if d.get("label") == label and str(d.get("obo_id", "")).startswith("GO:")]
    if len(hits) != 1:
        return {"status": "UNRESOLVED", "note": f"{len(hits)} exact-label hits"}
    iri = urllib.parse.quote(urllib.parse.quote(hits[0]["iri"], safe=""), safe="")
    term = get(f"{OLS}/ontologies/go/terms/{iri}")
    ns = (term.get("annotation") or {}).get("has_obo_namespace", [""])[0]
    if term.get("is_obsolete"):
        return {"status": "UNRESOLVED", "note": "obsolete"}
    if ns not in namespaces:
        return {"status": "UNRESOLVED", "note": f"namespace {ns}"}
    return {"status": "OK", "id": term["obo_id"], "definition": (term.get("description") or [""])[0]}


def main() -> None:
    today = dt.date.today().isoformat()
    cache: dict[str, dict] = {}
    with open(DATA / "carbon_source_go_map.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["carbon_source", "substrate_class", "go_id", "go_label", "status",
                    "go_definition", "lookup"])
        for src, (label, cls) in MAP.items():
            if label is None:
                w.writerow([src, cls, "", "", "UNMAPPED", "", ""])
                continue
            if label not in cache:
                cache[label] = resolve(label)
            r = cache[label]
            w.writerow([src, cls, r.get("id", ""), label, r["status"],
                        r.get("definition", r.get("note", "")),
                        f"OLS4 exact label, GO, {today}"])
            print(f"{r['status']:10} {src:24} {r.get('id', ''):11} {label}")

    with open(DATA / "carbon_source_go_activity_map.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["carbon_source", "go_id", "go_label", "go_usage", "status", "rationale",
                    "go_definition", "lookup"])
        for sources, label, usage, why in ACTIVITY:
            r = resolve(label, ("biological_process", "molecular_function"))
            for src in sources:
                w.writerow([src, r.get("id", ""), label, usage, r["status"], why,
                            r.get("definition", r.get("note", "")), f"OLS4 exact label, GO, {today}"])
            print(f"{r['status']:10} activity {r.get('id', ''):11} {label} ({usage})")


if __name__ == "__main__":
    main()
