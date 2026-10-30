"""Fetch exact GO evidence and refresh only the disputed terms' cache entries.

Run from the repository root with ``uv run python <this-file> --fetch``.
Without --fetch, replay the committed evidence without network access.
"""

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

from linkml_term_validator.utils.oak_utils import OntologyAccess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OBSOLETE_IDS = {f"GO:{n:07d}" for n in range(6419, 6439)} | {
    "GO:0070680", "GO:0070681"
}
GO_COMMIT = "939abfae5a06a9dbb20d931465707e5e61a7c537"
OBO_URL = (
    "https://raw.githubusercontent.com/geneontology/go-ontology/"
    f"{GO_COMMIT}/src/ontology/go-edit.obo"
)


def fetch():
    previous = json.loads((HERE / "go-term-snapshot.json").read_text())
    ids = sorted({t["id"] for t in previous["results"]} | OBSOLETE_IDS)
    url = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/" + ",".join(ids)
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = json.load(response)
    assert {t["id"] for t in data["results"]} == set(ids)
    with urllib.request.urlopen(OBO_URL, timeout=60) as response:
        obo = response.read()
    selected = []
    for stanza in obo.decode().split("\n[Term]\n")[1:]:
        term_id = next(line[4:] for line in stanza.splitlines() if line.startswith("id: "))
        if term_id in OBSOLETE_IDS:
            selected.append("[Term]\n" + stanza.rstrip() + "\n")
    assert len(selected) == 22
    (HERE / "go-term-snapshot.json").write_text(json.dumps(data, indent=2) + "\n")
    (HERE / "go-obsolescence.obo").write_text("\n".join(selected))
    provenance = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "quickgo_url": url,
        "quickgo_ids": ids,
        "obo_url": OBO_URL,
        "obo_commit": GO_COMMIT,
        "obo_sha256": hashlib.sha256(obo).hexdigest(),
        "extracted_ids": sorted(OBSOLETE_IDS),
        "extraction": "Complete, unedited term stanzas, excluding the document header.",
    }
    (HERE / "go-snapshot-provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")


def refresh_caches():
    data = json.loads((HERE / "go-term-snapshot.json").read_text())
    terms = {t["id"]: t for t in data["results"] if t["id"] in OBSOLETE_IDS}
    assert set(terms) == OBSOLETE_IDS
    assert all(t["isObsolete"] is True for t in terms.values())
    access = OntologyAccess(cache_dir=ROOT / "cache", offline=True)
    for term_id, term in sorted(terms.items()):
        access.save_to_cache("GO", term_id, term["name"])
    path = ROOT / "cache/ontologies/go.tsv"
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    retrieved = json.loads((HERE / "go-snapshot-provenance.json").read_text())["retrieved_at"]
    for row in rows:
        if row["term_id"] in terms:
            row.update(label=terms[row["term_id"]]["name"], is_obsolete="true", fetched_date=retrieved)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    path = ROOT / "cache/enums/gobiologicalprocessenum_769282d9de2a.csv"
    lines = path.read_text().splitlines()
    path.write_text("\n".join(line for line in lines if line not in OBSOLETE_IDS) + "\n")
    print("Verified 22 obsolete terms; refreshed their label/metadata caches and excluded them from the BP enum.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    if args.fetch:
        fetch()
    refresh_caches()
