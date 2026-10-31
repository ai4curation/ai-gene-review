"""Reproduce a focused ARBA candidate search; standard-library dependencies only."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def fetch(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={"Accept": "application/json"}), timeout=45) as response:
                return json.load(response), dict(response.headers)
        except (OSError, ValueError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def condition_query(condition_set):
    parts = []
    for condition in condition_set["conditions"]:
        values = []
        for value in condition["conditionValues"]:
            kind = condition["type"]
            if kind == "taxon":
                query = "taxonomy_id:" + value["cvId"]
            elif kind == "InterPro id":
                query = "xref:interpro-" + value["value"]
            elif kind in {"FunFam id", "PANTHER id"}:
                # Structured PANTHER xref search does not find subfamily IDs.
                query = '"' + value["value"] + '"'
            else:
                raise ValueError(f"Unsupported condition type: {kind}")
            values.append(query)
        parts.append(("NOT " if condition.get("isNegative") else "") + "(" + " OR ".join(values) + ")")
    return " AND ".join(parts)


def search(task):
    number, condition_set, exclude_kinases = task
    query = condition_query(condition_set) + " AND (reviewed:true)"
    if exclude_kinases:
        query += " AND NOT (go:0004672)"
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode({"query": query, "format": "json", "size": 500})
    original_url = url
    proteins = []
    total = None
    while url:
        data, raw_headers = fetch(url)
        headers = {k.lower(): v for k, v in raw_headers.items()}
        if total is None:
            total = int(headers["x-total-results"])
        proteins.extend(data["results"])
        match = re.search(r'<([^>]+)>;\s*rel="next"', headers.get("link", ""))
        url = match.group(1) if match else None
    if len(proteins) != total:
        raise ValueError(f"Incomplete result for condition {number}: {len(proteins)} / {total}")
    return {
        "condition_set": number,
        "exclude_kinases": exclude_kinases,
        "query": query,
        "url": original_url,
        "total": total,
        "returned": len(proteins),
    }, proteins


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rule", default="ARBA00027234")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    # Refuse accidental replacement of a previous evidence snapshot.
    args.output.mkdir(parents=True, exist_ok=False)
    rule, _ = fetch(f"https://rest.uniprot.org/arba/{args.rule}.json")
    (args.output / f"{args.rule}.json").write_text(json.dumps(rule, indent=2) + "\n")
    tasks = [(n, condition, excluded) for n, condition in enumerate(rule["mainRule"]["conditionSets"], 1)
             for excluded in [False, True]]
    queries, proteins, memberships = [], {}, {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result, matches in pool.map(search, tasks):
            queries.append(result)
            if not result["exclude_kinases"]:
                for protein in matches:
                    accession = protein["primaryAccession"]
                    proteins[accession] = protein
                    memberships.setdefault(accession, set()).add(result["condition_set"])
    rule_ids = list(dict.fromkeys([args.rule, "ARBA00026648", "ARBA00026662", "ARBA00085084", "ARBA00088043", "ARBA00089890"]))
    presence = []
    for rule_id in rule_ids:
        url = "https://www.ebi.ac.uk/QuickGO/services/annotation/search?" + urlencode({"withFrom": "ARBA:" + rule_id, "limit": 1})
        data, _ = fetch(url)
        presence.append({"rule": rule_id, "url": url, "payload": data})
    summary = {
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "rule_id": args.rule,
        "condition_sets": len(rule["mainRule"]["conditionSets"]),
        "distinct_swissprot_matches": len(proteins),
        "nonkinase_queries_with_hits": [q for q in queries if q["exclude_kinases"] and q["total"]],
        "queries": queries,
        "quickgo_rule_queries": presence,
    }
    (args.output / "audit.json").write_text(json.dumps(summary, indent=2) + "\n")
    (args.output / "matched-proteins.json").write_text(json.dumps(proteins, indent=2) + "\n")
    with (args.output / "reviewed-matches.tsv").open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["accession", "entry", "taxon", "condition_sets"])
        for accession, protein in sorted(proteins.items()):
            writer.writerow([accession, protein["uniProtkbId"], protein["organism"]["taxonId"],
                             ";".join(map(str, sorted(memberships[accession])))])
    print(json.dumps({k: v for k, v in summary.items() if k not in {"queries", "quickgo_rule_queries"}}, indent=2))


if __name__ == "__main__":
    main()
