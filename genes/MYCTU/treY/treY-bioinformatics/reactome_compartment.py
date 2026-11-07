"""Fetch the compartment, inputs and catalyst activity of a Reactome reaction.

Usage: python reactome_compartment.py R-MTU-868658 > RESULTS.md
Queries the public Reactome ContentService; prints the fields verbatim.
"""
import json
import sys
import urllib.request

rid = sys.argv[1]
url = f"https://reactome.org/ContentService/data/query/{rid}"
req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
with urllib.request.urlopen(req) as fh:
    d = json.load(fh)
print(f"# Reactome reaction {rid}\n")
print(f"Source: {url}\n")
print(f"- displayName: {d.get('displayName')}")
for c in d.get("compartment", []):
    print(f"- compartment: {c.get('displayName')}")
for x in d.get("input", []):
    print(f"- input: {x.get('displayName')}")
for x in d.get("output", []):
    print(f"- output: {x.get('displayName')}")
for x in d.get("catalystActivity", []):
    print(f"- catalystActivity: {x.get('displayName')}")
