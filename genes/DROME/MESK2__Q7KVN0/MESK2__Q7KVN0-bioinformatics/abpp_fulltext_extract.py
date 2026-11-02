"""Extract the MESK2 evidence from the full text of Kumar et al. 2021 (PMID:33827210, PMC7610703).

Fetches the PMC XML from NCBI E-utilities, prints the Table 1 row(s) naming MESK2,
and prints sentences describing the LC-MS/MS ABPP design and controls, so a curator
can judge what the HDA "serine hydrolase activity" row rests on.

Run: uv run python abpp_fulltext_extract.py > abpp_fulltext_extract.out
"""

import re
import urllib.request
import xml.etree.ElementTree as ET

URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=7610703&rettype=xml"


def text_of(el: ET.Element) -> str:
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def main() -> None:
    root = ET.fromstring(urllib.request.urlopen(URL).read())
    print(f"Source: {URL}")
    print("== Table rows mentioning MESK2 ==")
    for tr in root.iter("tr"):
        cells = [text_of(td) for td in tr]
        if any("MESK2" in c for c in cells):
            print(" | ".join(cells))
    print("== Table caption(s) ==")
    for tw in root.iter("table-wrap"):
        cap = tw.find("caption")
        if cap is not None and any("MESK2" in text_of(tr) for tr in tw.iter("tr")):
            print(text_of(cap))
    print("== Sentences on LC-MS/MS ABPP design, controls and probe coverage ==")
    body = root.find(".//body")
    full = text_of(body) if body is not None else ""
    sentences = re.split(r"(?<=[.])\s+", full)
    keys = ("heat denatured", "Peptide Count", "enriched by avidin", "don't react", "don’t react",
            "relative activity", "non-SH enzymes")
    for s in sentences:
        if any(k in s for k in keys):
            print("-", s)


if __name__ == "__main__":
    main()
