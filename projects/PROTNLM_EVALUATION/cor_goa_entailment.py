"""Check each COR ProtNLM GO call against the target's own cached GOA using GO graph closure.

COR in this project means "biologically supported and absent from the target's cached
GOA/UniProt record". This script asks a narrower, mechanical question for every COR call:
is the predicted term already *entailed* by a term the target carries in its cached
``*-goa.tsv``? It uses the pinned GO release loaded by
``ai_gene_review.bioreason_ontology.get_go_adapter`` (go-basic 2026-03-25, checksum-verified,
downloaded into the git-ignored ``cache/ontologies/``) and follows ``is_a`` and ``part_of``.

Relation classes (first match wins):

* ``EXACT`` -- the predicted id is itself in the target GOA (inconsistent with COR).
* ``ANCESTOR_SAME_ASPECT`` -- the predicted term is an is_a/part_of ancestor of a target GOA term
  in the same GO aspect, i.e. a generalisation of something already annotated.
* ``ANCESTOR_CROSS_ASPECT`` -- the predicted term is reached from a target GOA term of another
  aspect via part_of (e.g. an MF that is part_of the predicted BP).
* ``DESCENDANT`` -- the predicted term is more specific than an existing target GOA term.
* ``NONE`` -- no is_a/part_of path in either direction.

Domain-to-GO entailment (InterPro2GO) and relations beyond is_a/part_of (e.g. regulates,
has_part, occurs_in) are not checked. A non-NONE class is a flag for re-review, not a verdict:
the assessment remains the curated YAML call. Writes ``cor-goa-entailment.tsv``.

Run: ``uv run python projects/PROTNLM_EVALUATION/cor_goa_entailment.py``
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

import yaml

from ai_gene_review.bioreason_ontology import GO_RELEASE, get_go_adapter

PREDICATES = ["rdfs:subClassOf", "BFO:0000050"]  # is_a, part_of
ASPECT = {"GO_MF": "molecular_function", "GO_BP": "biological_process", "GO_CC": "cellular_component"}


def target_goa(gene_dir: Path) -> list[dict[str, str]]:
    files = sorted(gene_dir.glob("*-goa.tsv"))
    if not files:
        return []
    return [
        r
        for r in csv.DictReader(files[0].open(), delimiter="\t")
        if not (r.get("QUALIFIER") or "").startswith("NOT")
    ]


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    base = root / "projects/PROTNLM_EVALUATION"
    scope = list(csv.DictReader((base / "family-curation/scope.csv").open()))
    targets = {r["accession"] for r in scope if r["role"] == "prediction_target"}
    cohorts: dict[str, list[str]] = {}
    for r in scope:
        cohorts.setdefault(r["accession"], []).append(r["cohort"])
    go = get_go_adapter()
    ancestor_cache: dict[str, set[str]] = {}

    def ancestors(term: str) -> set[str]:
        if term not in ancestor_cache:
            ancestor_cache[term] = set(go.ancestors(term, predicates=PREDICATES, reflexive=False))
        return ancestor_cache[term]

    rows = []
    for path in sorted(root.glob("genes/*/*/*-protnlm-predictions-review.yaml")):
        doc = yaml.safe_load(path.read_text())
        if doc["id"] not in targets:
            continue
        goa = target_goa(path.parent)
        for prediction in doc.get("predictions") or []:
            if prediction["review"]["assessment"] != "COR":
                continue
            pred = prediction["predicted_term"]["id"]
            aspect = ASPECT[prediction["predicted_term_type"]]
            relation, evidence = "NONE", ""
            goa_ids = {r["GO TERM"]: r for r in goa}
            if pred in goa_ids:
                relation, evidence = "EXACT", pred
            else:
                same = [t for t, r in goa_ids.items() if r["GO ASPECT"] == aspect and pred in ancestors(t)]
                cross = [t for t, r in goa_ids.items() if r["GO ASPECT"] != aspect and pred in ancestors(t)]
                desc = [t for t in goa_ids if t in ancestors(pred)]
                if same:
                    relation, evidence = "ANCESTOR_SAME_ASPECT", ";".join(sorted(same))
                elif cross:
                    relation, evidence = "ANCESTOR_CROSS_ASPECT", ";".join(sorted(cross))
                elif desc:
                    relation, evidence = "DESCENDANT", ";".join(sorted(desc))
            rows.append(
                dict(
                    gene="/".join(path.parts[-3:-1]),
                    accession=doc["id"],
                    cohorts=";".join(sorted(set(cohorts[doc["id"]]))),
                    term_id=pred,
                    term_label=prediction["predicted_term"]["label"],
                    aspect=aspect,
                    target_goa_rows=len(goa),
                    relation=relation,
                    via_target_goa_terms=evidence,
                    via_labels=";".join(go.label(t) or "" for t in evidence.split(";") if t),
                )
            )
    out = base / "cor-goa-entailment.tsv"
    with out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(
        json.dumps(
            dict(
                go_release=GO_RELEASE,
                cor_calls=len(rows),
                relation=dict(Counter(r["relation"] for r in rows)),
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
