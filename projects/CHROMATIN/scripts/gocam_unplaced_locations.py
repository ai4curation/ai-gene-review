"""Which GO-CAM activity locations reach no top-level compartment?

Reads gocams/index.tsv (one row per activity) and reports the cellular_component
values whose is_a/part_of closure reaches none of nucleus, cytoplasm, plasma
membrane or extracellular region, flagging those under chromosome (GO:0005694).
A location-based layout cannot place these by strict logic alone.

Usage:
    python gocam_unplaced_locations.py go-basic.obo gocams/index.tsv
"""

from __future__ import annotations

import collections
import csv
import sys

from go_closure import load

TOP = {
    "GO:0005634": "nucleus",
    "GO:0005737": "cytoplasm",
    "GO:0005886": "plasma membrane",
    "GO:0005576": "extracellular region",
}
CHROMOSOME = "GO:0005694"


def main(obo_path: str, index_path: str, limit: int = 30) -> None:
    """Print the unplaced share and the most frequent unplaced locations."""
    graph = load(obo_path)
    with open(index_path) as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t") if r["cellular_component"]]
    counts: collections.Counter = collections.Counter()
    models = collections.defaultdict(set)
    under_chromosome = 0
    for row in rows:
        term = graph.primary(row["cellular_component"])
        ancestors = graph.ancestors(term)
        if ancestors & TOP.keys():
            continue
        counts[term] += 1
        models[term].add(row["model_id"])
        under_chromosome += CHROMOSOME in ancestors
    total = sum(counts.values())
    print(f"activities with a location: {len(rows)}; reaching none of "
          f"{sorted(TOP.values())}: {total} ({100 * total / len(rows):.1f}%), "
          f"of which {under_chromosome} are under chromosome")
    for term, n in counts.most_common(limit):
        flag = " [chromosome]" if CHROMOSOME in graph.ancestors(term) else ""
        print(f"{n:5d} activities {len(models[term]):4d} models  {term} "
              f"{graph.names.get(term, '?')}{flag}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
