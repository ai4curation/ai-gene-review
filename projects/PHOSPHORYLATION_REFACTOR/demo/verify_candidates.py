# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Check the demo shortlist against its snapshot and the current checkout.

uv run --script projects/PHOSPHORYLATION_REFACTOR/demo/verify_candidates.py
Add --live to recheck all GO rows and UniProt identities over the network.
No gene reviews are created or modified. The live check does not overwrite the
dated snapshot; it reports drift/failures so the shortlist can be reconsidered.
"""

import argparse
import concurrent.futures
import csv
import json
from collections import Counter
from pathlib import Path
import time
import urllib.parse
import urllib.request

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
API = "https://www.ebi.ac.uk/QuickGO/services/"


def get_json(url):
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=45) as response:
                return json.load(response)
        except (OSError, ValueError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def descendants(term):
    url = API + "ontology/go/terms/" + term + "/descendants?relations=is_a,part_of"
    return set(get_json(url)["results"][0]["descendants"]) | {term}


def fetch_product(candidate):
    accession = candidate["uniprot_id"]
    params = {"geneProductId": "UniProtKB:" + accession, "limit": 100}
    page = get_json(API + "annotation/search?" + urllib.parse.urlencode(params))
    rows = list(page["results"])
    for number in range(2, page["pageInfo"]["total"] + 1):
        params["page"] = number
        rows.extend(get_json(API + "annotation/search?" + urllib.parse.urlencode(params))["results"])
    uniprot = get_json("https://rest.uniprot.org/uniprotkb/" + accession + ".json")
    aliases = {candidate["gene"]}
    for gene in uniprot.get("genes", []):
        for values in gene.values():
            for value in values if isinstance(values, list) else [values]:
                aliases.add(value["value"])
    return accession, {
        "goa_rows": rows,
        "aliases": sorted(aliases),
        "accessions": [accession, uniprot["primaryAccession"], *uniprot.get("secondaryAccessions", [])],
        "uniprot": uniprot,
    }


def review_inventory():
    """Include partial stubs and prediction reviews; compare aliases and accessions."""
    names, accessions = {}, {}
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    for path in (ROOT / "genes").glob("*/*/*review.y*ml"):
        data = yaml.load(path.read_text(), Loader=loader) or {}
        organism = path.relative_to(ROOT / "genes").parts[0]
        for name in [path.parent.name, data.get("gene_symbol", "")]:
            if name:
                names[(organism, name.casefold())] = str(path.relative_to(ROOT))
        accession = str(data.get("id", "")).removeprefix("UniProtKB:").split("-")[0]
        if accession:
            accessions[accession] = str(path.relative_to(ROOT))
    return names, accessions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    with (HERE / "candidates.tsv").open() as stream:
        candidates = list(csv.DictReader(stream, delimiter="\t"))
    snapshot = json.loads((HERE / "snapshot.json").read_text())
    if args.live:
        kinase_terms = descendants("GO:0004672")
        process_terms = descendants("GO:0006468")
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            products = dict(pool.map(fetch_product, candidates))
    else:
        ontology = snapshot["ontology"]
        kinase_terms = set(ontology["protein_kinase_activity"]["results"][0]["descendants"])
        process_terms = set(ontology["protein_phosphorylation"]["results"][0]["descendants"])
        products = snapshot["products"]
    process_terms |= {"GO:0016310", "GO:0046835"}
    process_terms -= {"GO:0042976"}  # Janus kinase activation is regulatory.
    names, accessions = review_inventory()
    problems, seen, gene_keys = [], set(), set()
    count_rows = 0
    for candidate in candidates:
        acc = candidate["uniprot_id"]
        key = (candidate["organism"], candidate["gene"].casefold())
        if acc in seen or key in gene_keys:
            problems.append(f"Duplicate gene/product: {key}, {acc}")
        seen.add(acc)
        gene_keys.add(key)
        product = products[acc]
        if product["uniprot"]["organism"]["taxonId"] != int(candidate["taxon_id"]):
            problems.append(f"Taxon mismatch: {key}")
        for alias in product["aliases"]:
            match = names.get((candidate["organism"], alias.casefold()))
            if match:
                problems.append(f"Already reviewed by symbol/alias: {key}: {match}")
        for accession in product["accessions"]:
            if accession in accessions:
                problems.append(f"Already reviewed by accession: {key}: {accessions[accession]}")
        rows = product["goa_rows"]
        kinases = [r for r in rows if r["goId"] in kinase_terms and "NOT" not in r["qualifier"].split("|")]
        if kinases:
            problems.append(f"Positive protein kinase activity: {key}: {kinases}")
        positive = [r for r in rows if r["qualifier"] == "involved_in"
                    and r["goAspect"] == "biological_process" and r["goId"] in process_terms]
        count_rows += len(positive)
        if not positive:
            problems.append(f"No current positive target process row: {key}")
        for field, source in [("go_ids", "goId"), ("evidence", "goEvidence"), ("references", "reference")]:
            actual = set(r[source] for r in positive)
            if actual != set(candidate[field].split(";")):
                problems.append(f"{field} drift: {key}: {sorted(actual)}")
    report = {
        "mode": "live" if args.live else "snapshot",
        "snapshot_retrieved_at_utc": snapshot["retrieved_at_utc"],
        "candidates": len(candidates),
        "species": dict(Counter(c["organism"] for c in candidates)),
        "positive_target_rows": count_rows,
        "problems": problems,
    }
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(problems))


if __name__ == "__main__":
    main()
