"""How much of GOA does each reference ARFGEF1 relies on actually annotate?

A reference that annotates a complex plus every subunit with identical evidence
is a projection, not N independent findings. The discriminator is two questions,
not one:

1. how many DISTINCT ENTITIES does the reference annotate (entities, not
   annotations -- one entity can hold several annotations for the same term); and
2. does the functional/phenotype term spread across the set, or stay on the
   perturbed gene?

Large references are paginated. When `numberOfHits` exceeds the rows returned,
the entity count is reported as UNAVAILABLE rather than derived from one page --
a number from a partial page is worse than no number.

Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/reference_scope.py
"""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from uniprot import quickgo_annotations  # noqa: E402

HERE = Path(__file__).parent
GOA = HERE.parent / "ARFGEF1-goa.tsv"


def references() -> list[str]:
    seen: list[str] = []
    with GOA.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            r = row["REFERENCE"]
            if r.startswith("PMID:") and r not in seen:
                seen.append(r)
    return seen


def main() -> None:
    out = []
    detail = []
    for ref in references():
        data = quickgo_annotations(reference=ref, limit="200")
        rows = data.get("results", [])
        if not data["_truncated"]:
            for r in rows:
                wf = []
                for grp in (r.get("withFrom") or []):
                    for x in grp.get("connectedXrefs", []):
                        wf.append(f"{x['db']}:{x['id']}")
                detail.append({
                    "reference": ref,
                    "gene_product": r["geneProductId"],
                    "symbol": r.get("symbol", ""),
                    "taxon": r.get("taxonId", ""),
                    "go_id": r["goId"],
                    "qualifier": r.get("qualifier", ""),
                    "evidence": r["goEvidence"],
                    "with_from": "|".join(wf),
                    "assigned_by": r.get("assignedBy", ""),
                })
        n_hits = data.get("numberOfHits", 0)
        truncated = data["_truncated"]
        if truncated:
            entities = "UNAVAILABLE (paginated)"
            terms = "UNAVAILABLE (paginated)"
            per_term = {}
        else:
            ids = {r["geneProductId"] for r in rows}
            entities = str(len(ids))
            tset = {r["goId"] for r in rows}
            terms = str(len(tset))
            per_term = defaultdict(set)
            for r in rows:
                per_term[r["goId"]].add(r["geneProductId"])
        out.append({
            "reference": ref,
            "annotations": n_hits,
            "rows_read": len(rows),
            "truncated": str(truncated),
            "distinct_entities": entities,
            "distinct_terms": terms,
            "max_entities_for_one_term": (
                str(max((len(v) for v in per_term.values()), default=0))
                if per_term else "UNAVAILABLE"
            ),
        })
        print(f"{ref:<16} annotations={n_hits:<6} rows={len(rows):<5} "
              f"truncated={truncated!s:<6} entities={entities:<24} terms={terms}")

    fields = list(out[0])
    with (HERE / "reference_scope.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        w.writeheader()
        w.writerows(out)

    with (HERE / "reference_annotations.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(detail[0]))
        w.writeheader()
        w.writerows(detail)
    print(f"\nwrote {len(detail)} per-annotation rows for the "
          f"{len({d['reference'] for d in detail})} references small enough to enumerate")

    big = [r["reference"] for r in out if r["truncated"] == "True"]
    print(f"\nreferences too large to count entities from one page: {big}")
    small = [(r["reference"], r["distinct_entities"]) for r in out
             if r["truncated"] == "False" and int(r["distinct_entities"]) <= 3]
    print(f"gene-focused references (<=3 entities annotated): {len(small)}")


if __name__ == "__main__":
    main()
