"""Scan every condition set of a keyword ARBA rule against Swiss-Prot.

For each condition set of the live rule, two UniProtKB queries: the reviewed
entries that match the whole conjunction, and those among them that lack the
rule's keyword. Writes one TSV row per set: number, query, matched, lacking,
examples of matches, examples lacking the keyword. Nothing is inferred: a set
whose query fails after retries is written with ``ERROR`` and must be re-run.

Usage: python keyword_set_scan.py ARBA00022679 KW-0808 out.tsv [workers]
"""
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Tuple

SEARCH = "https://rest.uniprot.org/uniprotkb/search"
XREF = {"InterPro id": "interpro", "FunFam id": "funfam", "PANTHER id": "panther"}


def set_query(conditions: List[Dict[str, Any]]) -> str:
    """The UniProtKB query for one condition set (an AND of its conditions).

    >>> set_query([{"type": "InterPro id", "conditionValues": [{"value": "IPR000850"}]},
    ...            {"type": "taxon", "conditionValues": [{"value": "Bacteria", "cvId": "2"}]}])
    '(xref:interpro-IPR000850) AND (taxonomy_id:2)'
    >>> set_query([{"type": "PANTHER id", "isNegative": True, "conditionValues": [{"value": "PTHR1:SF0"}]}])
    'NOT (xref:"panther-PTHR1:SF0")'
    """
    parts = []
    for condition in conditions:
        alternatives = []
        for value in condition["conditionValues"]:
            if condition["type"] == "taxon":
                alternatives.append(f"taxonomy_id:{value['cvId']}")
            else:
                ref = f"{XREF[condition['type']]}-{value['value']}"
                alternatives.append(f'xref:"{ref}"' if ":" in value["value"] else f"xref:{ref}")
        part = "(" + " OR ".join(alternatives) + ")"
        parts.append(("NOT " if condition.get("isNegative") else "") + part)
    return " AND ".join(parts)


def search(query: str) -> Tuple[int, str]:
    """Total hits and up to three examples (accession, gene, protein name) for a query."""
    url = SEARCH + "?" + urllib.parse.urlencode(
        {"query": query, "size": 3, "fields": "accession,gene_primary,protein_name", "format": "json"})
    for attempt in range(6):
        try:  # external service: retry transient failures
            with urllib.request.urlopen(url, timeout=90) as response:
                total = int(response.headers["x-total-results"])
                results = json.load(response)["results"]
            break
        except Exception:  # noqa: BLE001
            if attempt == 5:
                raise
            time.sleep(5 * (attempt + 1))
    examples = []
    for entry in results:
        gene = (entry.get("genes") or [{}])[0].get("geneName", {}).get("value", "")
        description = entry.get("proteinDescription", {})
        name = (description.get("recommendedName") or (description.get("submissionNames") or [{}])[0]
                ).get("fullName", {}).get("value", "")
        examples.append(f"{entry['primaryAccession']} {gene} {name[:60]}".replace("\t", " "))
    return total, ";".join(examples)


def scan_set(number: int, conditions: List[Dict[str, Any]], keyword: str) -> List[Any]:
    """One TSV row for a condition set."""
    query = set_query(conditions)
    try:
        matched, examples = search(f"{query} AND (reviewed:true)")
        lacking, lacking_examples = (0, "") if matched == 0 else search(
            f"{query} AND (reviewed:true) AND NOT (keyword:{keyword})")
    except Exception as error:  # noqa: BLE001
        return [number, query, "ERROR", "ERROR", str(error)[:200], ""]
    return [number, query, matched, lacking, examples, lacking_examples]


def write_rows(path: Path, rows: Dict[int, List[Any]]) -> None:
    """Write the rows gathered so far, in set order (also a checkpoint: a re-run resumes from it)."""
    with path.open("w", newline="") as handle:
        csv.writer(handle, delimiter="\t", lineterminator="\n").writerows(rows[n] for n in sorted(rows))


def main() -> None:
    rule_id, keyword, out = sys.argv[1:4]
    workers = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    with urllib.request.urlopen(f"https://rest.uniprot.org/arba/{rule_id}", timeout=120) as response:
        sets = json.load(response)["mainRule"]["conditionSets"]
    path = Path(out)
    done = {}
    if path.exists():
        done = {int(row[0]): row for row in csv.reader(path.open(), delimiter="\t") if row[2] != "ERROR"}
    todo = [(n, s["conditions"]) for n, s in enumerate(sets, 1) if n not in done]
    with ThreadPoolExecutor(workers) as pool:
        for row in pool.map(lambda item: scan_set(item[0], item[1], keyword), todo):
            done[row[0]] = row
            if len(done) % 200 == 0:
                write_rows(path, done)
                print(len(done), "of", len(sets), flush=True)
    write_rows(path, done)
    print("sets", len(sets), "written", len(done), "errors", sum(1 for r in done.values() if r[2] == "ERROR"))


if __name__ == "__main__":
    main()
