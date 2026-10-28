# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Tabulate PANTHER PTHR31259 subfamily membership (via UniProt cross-references).

Queries the UniProt REST API for every protein carrying each PTHR31259 subfamily
cross-reference, counts members per organism, and lists the subfamily assigned to
ENTR1 entries from selected mammals. Writes RESULTS-rereview.md next to this script.

Run: uv run --script genes/EQUAS/ENTR1/ENTR1-bioinformatics/panther_subfamily_rereview.py
"""

import csv
import io
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

API = "https://rest.uniprot.org/uniprotkb/search"
SUBFAMILIES = ["SF3", "SF4", "SF5", "SF6"]
MAMMALS = "9606 10090 10116 9913 9796 9793".split()


def fetch_tsv(query: str, fields: str) -> list[dict]:
    rows: list[dict] = []
    url = API + "?" + urllib.parse.urlencode(
        {"query": query, "fields": fields, "format": "tsv", "size": 500}
    )
    while url:
        with urllib.request.urlopen(url) as resp:
            text = resp.read().decode()
            link = resp.headers.get("Link")
        rows.extend(csv.DictReader(io.StringIO(text), delimiter="\t"))
        url = None
        if link and 'rel="next"' in link:
            url = link.split(";")[0].strip("<> ")
    return rows


def main() -> None:
    out = [
        "# ENTR1: PANTHER PTHR31259 subfamily placement (re-review)",
        "",
        f"UniProt REST queries run {date.today().isoformat()} by `panther_subfamily_rereview.py`.",
        "",
        "## Members per subfamily (top organisms)",
        "",
    ]
    for sf in SUBFAMILIES:
        rows = fetch_tsv(f'xref:"panther-PTHR31259:{sf}"', "accession,organism_name")
        counts = Counter(r["Organism"] for r in rows)
        out.append(f"- PTHR31259:{sf}: {len(rows)} entries in {len(counts)} organisms; top: "
                   + "; ".join(f"{o} ({n})" for o, n in counts.most_common(6)))
    out += ["", "## ENTR1 entries in selected mammals", "",
            "| accession | organism | length | reviewed | PANTHER |", "|---|---|---|---|---|"]
    orgs = " OR ".join(f"organism_id:{t}" for t in MAMMALS)
    rows = fetch_tsv(f"gene:ENTR1 AND ({orgs})",
                     "accession,organism_name,length,reviewed,xref_panther")
    for r in rows:
        out.append(f"| {r['Entry']} | {r['Organism']} | {r['Length']} | {r['Reviewed']} | {r['PANTHER']} |")
    Path(__file__).with_name("RESULTS-rereview.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
