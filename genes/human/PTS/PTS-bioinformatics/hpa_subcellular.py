"""Extract Human Protein Atlas subcellular (ICC/IF) evidence for a gene.

Usage:
    python hpa_subcellular.py ENSG00000150787 [--xml PATH] > hpa_subcellular.yaml

Without --xml the entry is downloaded from https://www.proteinatlas.org/<ENSG>.xml.
Only the immunofluorescence (ICC/IF) and protein-array sections are kept.
"""

import argparse
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date

import yaml


def load(ensg: str, path: str | None) -> tuple[ET.Element, str]:
    if path:
        return ET.parse(path).getroot(), path
    url = f"https://www.proteinatlas.org/{ensg}.xml"
    with urllib.request.urlopen(url, timeout=120) as resp:
        return ET.fromstring(resp.read()), url


def extract(root: ET.Element) -> dict:
    entry = root.find("entry")
    out: dict = {"gene": entry.findtext("name"), "hpa_version": root.get("schemaVersion")}
    summary = entry.find("cellExpression[@technology='ICC/IF']")
    if summary is not None:
        out["if_summary"] = (summary.findtext("summary") or "").strip()
        out["if_reliability"] = summary.findtext("verification[@type='reliability']")
        out["if_locations"] = [
            {"location": loc.text, "status": loc.get("status"), "go_id": loc.get("GOId")}
            for loc in summary.findall("data/location")
        ]
    antibodies = []
    for ab in entry.findall("antibody"):
        rec: dict = {"id": ab.get("id")}
        pa = ab.find("proteinArray/verification[@type='validation']")
        if pa is not None:
            rec["protein_array"] = {"call": pa.text, "description": pa.get("description")}
        for sub in ab.findall("cellExpression[@technology='ICC/IF']/subAssay"):
            rec["if_validation"] = sub.findtext("verification[@type='validation']")
            lines = []
            for d in sub.findall("data"):
                channels = sorted(
                    {c.text for c in d.findall("assayImage/image/channel")} - {"Target protein"}
                )
                lines.append(
                    {
                        "cell_line": d.findtext("cellLine"),
                        "locations": [loc.text for loc in d.findall("location")],
                        "counterstains": channels,
                    }
                )
            rec["if_cell_lines"] = lines
        if len(rec) > 1:
            antibodies.append(rec)
    out["antibodies"] = antibodies
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ensg")
    ap.add_argument("--xml", help="local copy of the HPA entry XML")
    args = ap.parse_args()
    root, source = load(args.ensg, args.xml)
    result = {"source": source, "retrieved": date.today().isoformat(), **extract(root)}
    yaml.safe_dump(result, sys.stdout, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
