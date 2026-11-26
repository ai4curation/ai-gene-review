"""ai-gene-review adapter: a folder of gene reviews to predictions.

A review answers a claim "yes" when a term it asserts (a kept, NEW or MODIFY
row, a MODIFY replacement, a core-function term) entails the claim's term,
and "no" when it contests a row to that term or asserts nothing that entails
it. It is never asked about decoys, so no prediction is written for them:
silence there is not a measured "no" comparable with predictors that were
asked.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from ai_gene_review.benchmark.checks import (
    REVIEW_CONTESTS,
    REVIEW_KEEPS,
    Context,
    find_review,
)
from ai_gene_review.benchmark.predictions import queries

CORE_FUNCTION_SLOTS = (
    "molecular_function",
    "contributes_to_molecular_function",
    "directly_involved_in",
    "locations",
    "in_complex",
)


def review_claims(review: dict) -> tuple[set[str], set[str]]:
    """Terms a review asserts (kept rows, MODIFY rows and their replacements, core functions) and contests.

    >>> kept, contested = review_claims({
    ...     "existing_annotations": [
    ...         {"term": {"id": "GO:1"}, "review": {"action": "MODIFY",
    ...          "proposed_replacement_terms": [{"id": "GO:2"}]}},
    ...         {"term": {"id": "GO:3"}, "review": {"action": "REMOVE"}}],
    ...     "core_functions": [{"in_complex": {"id": "GO:4"}}]})
    >>> sorted(kept), sorted(contested)
    (['GO:1', 'GO:2', 'GO:4'], ['GO:3'])
    """
    kept: set[str] = set()
    contested: set[str] = set()
    for row in review.get("existing_annotations") or []:
        decision = row.get("review") or {}
        action = decision.get("action")
        term = (row.get("term") or {}).get("id")
        if not term or row.get("negated"):
            continue
        if action in REVIEW_KEEPS or action == "MODIFY":
            kept.add(term)
            kept |= {
                t["id"]
                for t in decision.get("proposed_replacement_terms") or []
                if t.get("id", "").startswith("GO:")
            }
        elif action in REVIEW_CONTESTS:
            contested.add(term)
    for core in review.get("core_functions") or []:
        for slot in CORE_FUNCTION_SLOTS:
            values = core.get(slot) or []
            for value in values if isinstance(values, list) else [values]:
                if isinstance(value, dict) and value.get("id"):
                    kept.add(value["id"])
    return kept, contested - kept


def predictions(
    benchmark: dict,
    ctx: Context,
    genes_dir: Path,
    condition: str,
    predictor: str,
    model: str | None = None,
) -> list[dict]:
    """Prediction records for targets and NOT targets from the reviews under ``genes_dir``."""
    out = []
    for item in benchmark["items"]:
        path = find_review(
            genes_dir, item.get("gene_symbol"), item["protein"].split(":", 1)[1]
        )
        if path is None:
            continue
        kept, contested = review_claims(yaml.safe_load(path.read_text()))
        for term, _, role in queries(item):
            if role == "DECOY":
                continue
            if term in contested:
                verdict = "no"
            elif any(
                term in ctx.ontology.ancestors(ctx.ontology.resolve(k)) for k in kept
            ):
                verdict = "yes"
            else:
                verdict = "no"
            prediction = {
                "item_id": item["id"],
                "term": term,
                "predictor": predictor,
                "model": model,
                "condition": condition,
                "verdict": verdict,
                "provenance": f"ai-gene-review review {path}",
            }
            out.append({k: v for k, v in prediction.items() if v is not None})
    return out
