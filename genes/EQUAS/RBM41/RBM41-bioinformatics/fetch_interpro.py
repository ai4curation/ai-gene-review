"""Fetch the InterPro entry IPR045164 (RBM41/RNPC3) description and save it as
markdown (interpro-IPR045164.md). Run: uv run python genes/EQUAS/RBM41/RBM41-bioinformatics/fetch_interpro.py
"""
import json, re, urllib.request
from pathlib import Path
here = Path(__file__).resolve().parent
url = "https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045164"
d = json.load(urllib.request.urlopen(url))["metadata"]
text = " ".join(re.sub(r"<[^>]+>", "", x["text"]) for x in d.get("description", []))
out = [f"# InterPro {d['accession']}: {d['name']['name']}", "", f"Source: {url} (retrieved by this script)", "", text.strip(), ""]
(here / "interpro-IPR045164.md").write_text("\n".join(out))
print("\n".join(out))
