#!/usr/bin/env python3
"""Look up GO terms by id or label (QuickGO), to ground module specs.

    python3 projects/FLYBASE_GENE_GROUPS/go_lookup.py GO:0070652 "HAUS complex"

Ids print their current label and obsolete status; any other argument is a
text search that prints the top matching non-obsolete terms.
"""
import json
import sys
import urllib.parse
import urllib.request

Q = "https://www.ebi.ac.uk/QuickGO/services/ontology/go"


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


for arg in sys.argv[1:]:
    if arg.startswith("GO:"):
        for t in get(f"{Q}/terms/{arg}")["results"]:
            print(f"{t['id']}\t{t['name']}\t{t['aspect']}\t{'OBSOLETE' if t['isObsolete'] else ''}")
    else:
        q = urllib.parse.quote(arg)
        res = get(f"{Q}/search?query={q}&limit=8")["results"]
        print(f"# {arg}")
        for t in res:
            if not t.get("isObsolete"):
                print(f"  {t['id']}\t{t['name']}\t{t['aspect']}")
