"""Fetch taxonomy (species, taxon ID) for ProtNLM accessions from UniProt REST API.

Produces: taxonomy.tsv (accession, organism, taxon_id)
"""

import csv
import json
import time
import urllib.request
from pathlib import Path


def fetch_batch(accessions: list[str]) -> dict[str, tuple[str, int]]:
    """Query UniProt for a batch of accessions. Returns {acc: (organism, taxid)}."""
    query = " OR ".join(f"accession:{a}" for a in accessions)
    url = (
        f"https://rest.uniprot.org/uniprotkb/search?"
        f"query={urllib.parse.quote(query)}"
        f"&fields=accession,organism_name,organism_id"
        f"&format=json&size={len(accessions)}"
    )
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())

    results = {}
    for r in data.get("results", []):
        acc = r["primaryAccession"]
        org = r.get("organism", {}).get("scientificName", "")
        taxid = r.get("organism", {}).get("taxonId", 0)
        results[acc] = (org, taxid)
    return results


def main():
    import urllib.parse

    base = Path(__file__).parent
    entries_path = base / "entries.tsv"
    out_path = base / "taxonomy.tsv"

    # Read accessions
    with open(entries_path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        accessions = [row["accession"] for row in reader]

    print(f"Fetching taxonomy for {len(accessions)} accessions...")

    # Check for partial results
    done = {}
    if out_path.exists():
        with open(out_path) as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                done[row["accession"]] = (row["organism"], row["taxon_id"])
        print(f"  {len(done)} already fetched, resuming...")

    remaining = [a for a in accessions if a not in done]

    # Batch query (100 at a time to stay under URL length limits)
    batch_size = 100
    all_results = dict(done)

    with open(out_path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["accession", "organism", "taxon_id"])

        # Write existing results first
        for acc in accessions:
            if acc in done:
                org, taxid = done[acc]
                w.writerow([acc, org, taxid])

        for i in range(0, len(remaining), batch_size):
            batch = remaining[i : i + batch_size]
            try:
                results = fetch_batch(batch)
                for acc in batch:
                    if acc in results:
                        org, taxid = results[acc]
                        w.writerow([acc, org, taxid])
                        all_results[acc] = (org, taxid)
                    else:
                        w.writerow([acc, "", ""])
                        all_results[acc] = ("", "")
                f.flush()
            except Exception as e:
                print(f"  Error at batch {i}: {e}")
                # Write blanks for failed batch
                for acc in batch:
                    if acc not in all_results:
                        w.writerow([acc, "", ""])
                        all_results[acc] = ("", "")
                f.flush()

            if (i // batch_size) % 10 == 0:
                print(f"  {i + len(batch)}/{len(remaining)} done")
            time.sleep(0.5)  # rate limit

    found = sum(1 for v in all_results.values() if v[0])
    print(f"Done. {found}/{len(accessions)} mapped to species.")


if __name__ == "__main__":
    main()
