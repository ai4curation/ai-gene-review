"""Track C propagation audit for ORIGINS_OF_MULTICELLULARITY.

1. Collects every propagated annotation (IBA, GO_REF:0000033; TreeGrafter IEA,
   GO_REF:0000118; and the UniProt multi-method merge, GO_REF:0000120) from the
   project's gene reviews, with the reviewer's action and source node.
2. For each term the reviews down-graded (REMOVE / MARK_AS_OVER_ANNOTATED /
   MODIFY), counts how often GOA puts that exact term on proteins of the
   unicellular holozoan lineages (Choanoflagellata, Filasterea, Ichthyosporea),
   and lists the source node of each row.

Usage:
    uv run python projects/ORIGINS_OF_MULTICELLULARITY/propagation_audit.py

Writes propagation_audit_rows.tsv and propagation_audit_spread.tsv next to this
script. Nothing is hardcoded except the list of review files; the spread counts
are whatever QuickGO returns on the day.
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

REVIEWS = [
    "SALRS/rosetteless", "SALRS/jumble", "SALRS/couscous",
    "SALRS/hippo", "SALRS/warts", "SALRS/yorkie",
    "CAPO3/coHpo", "CAPO3/coWts", "CAPO3/coYki",
    "OSCPE/VIN1", "OSCPE/TLN",
]
PROPAGATED_REFS = {"GO_REF:0000033", "GO_REF:0000118", "GO_REF:0000120"}
DOWNGRADED = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}
UNICELLULAR = {28009: "Choanoflagellata", 2687318: "Filasterea", 127916: "Ichthyosporea"}
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def quickgo(params: dict) -> dict:
    url = f"{QUICKGO}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def source_nodes(row: dict) -> str:
    ids = []
    for w in row.get("withFrom") or []:
        ids += [x["id"] for x in w["connectedXrefs"] if x["id"].startswith("PTN")]
    return ",".join(sorted(set(ids)))


def main() -> None:
    rows, flagged = [], {}
    for path in REVIEWS:
        org, sym = path.split("/")
        doc = yaml.safe_load((ROOT / "genes" / path / f"{sym}-ai-review.yaml").read_text())
        for ann in doc.get("existing_annotations") or []:
            ref = ann.get("original_reference_id")
            if ref not in PROPAGATED_REFS:
                continue
            action = (ann.get("review") or {}).get("action", "")
            ents = ",".join(e for e in ann.get("supporting_entities") or [] if e.startswith("PANTHER:"))
            rows.append([org, sym, doc["id"], ann["term"]["id"], ann["term"]["label"],
                         ann.get("evidence_type", ""), ref, ents, action])
            if action in DOWNGRADED:
                flagged[ann["term"]["id"]] = ann["term"]["label"]

    with open(OUT / "propagation_audit_rows.tsv", "w") as fh:
        fh.write("organism\tgene\tuniprot\tgo_id\tgo_label\tevidence\treference\tpanther_source\taction\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")

    with open(OUT / "propagation_audit_spread.tsv", "w") as fh:
        fh.write("go_id\tgo_label\tlineage\tn_annotations\tevidence_reference_node\n")
        for go_id, label in sorted(flagged.items()):
            for taxon, lineage in UNICELLULAR.items():
                data = quickgo({"goId": go_id, "goUsage": "exact", "taxonId": taxon,
                                "taxonUsage": "descendants", "limit": 100})
                detail = sorted({f"{r['geneProductId']}|{r['goEvidence']}|{r['reference']}|{source_nodes(r)}"
                                 for r in data.get("results", [])})
                fh.write(f"{go_id}\t{label}\t{lineage}\t{data.get('numberOfHits', 0)}\t{';'.join(detail)}\n")

    n_down = sum(r[-1] in DOWNGRADED for r in rows)
    print(f"{len(rows)} propagated rows across {len(REVIEWS)} reviews; {n_down} down-graded; "
          f"{len(flagged)} distinct down-graded terms checked for spread")


if __name__ == "__main__":
    main()
