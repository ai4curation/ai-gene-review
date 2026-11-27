"""The generic predictor interface: claims out, predictions in.

A benchmark asks every predictor the same questions, one ``Claim`` per
(item, GO term), and reads back ``Prediction`` records (schema classes in
``schema/benchmark.yaml``). Nothing here knows which predictor answered:
LLM tools, sequence tools, annotation pipelines, agent reviews and curators
are all converted to predictions by an importer (``benchmark.importers``).

A claim never says whether its term is a target, a NOT target or a decoy;
that role is looked up from the benchmark only when scoring.
"""

from __future__ import annotations

import json
import logging
from collections.abc import Iterable, Iterator
from pathlib import Path

import yaml

from ai_gene_review.benchmark.yaml_io import load_yaml

SHUFFLED = "SHUFFLED|"
VERDICTS = ("yes", "no", "uncertain")

#: (condition, predictor, item id, term or SHUFFLED|term) -> verdict
Verdicts = dict[tuple[str, str, str, str], str]


def fasta_id(item: dict) -> str:
    """UniProt-style FASTA id for an item.

    >>> fasta_id({"protein": "UniProtKB:P00533", "entry_name": "EGFR_HUMAN"})
    'sp|P00533|EGFR_HUMAN'
    """
    return f"sp|{item['protein'].split(':', 1)[1]}|{item['entry_name']}"


def queries(item: dict) -> Iterator[tuple[str, str, str]]:
    """(term id, label, role) for every term asked about an item."""
    for target in item["target_annotations"]:
        role = "NEGATED_TARGET" if target.get("negated") else "TARGET"
        yield target["term"]["id"], target["term"].get("label") or "", role
    for decoy in item.get("decoys") or []:
        yield decoy["term"]["id"], decoy["term"].get("label") or "", "DECOY"


def claim_id(item_id: str, term: str) -> str:
    """Claim identifier.

    >>> claim_id("toy-P1", "GO:0004672")
    'toy-P1/GO:0004672'
    """
    return f"{item_id}/{term}"


def claims(items: Iterable[dict]) -> list[dict]:
    """One Claim per distinct term per item, without its role.

    >>> item = {"id": "toy-P1", "protein": "UniProtKB:P1", "entry_name": "X_HUMAN",
    ...         "target_annotations": [{"term": {"id": "GO:1", "label": "a"}}],
    ...         "decoys": [{"term": {"id": "GO:2", "label": "b"}}]}
    >>> [c["id"] for c in claims([item])]
    ['toy-P1/GO:1', 'toy-P1/GO:2']
    >>> sorted(claims([item])[0])
    ['id', 'item_id', 'protein', 'sequence_id', 'term']
    """
    out = []
    for item in items:
        for term, label in dict.fromkeys((t, lab) for t, lab, _ in queries(item)):
            out.append(
                {
                    "id": claim_id(item["id"], term),
                    "item_id": item["id"],
                    "protein": item["protein"],
                    "sequence_id": fasta_id(item),
                    "term": {"id": term, "label": label},
                }
            )
    return out


def read_prediction_set(path: Path) -> dict:
    """Read a generic PredictionSet or one JSON Prediction per nonblank line."""
    if path.suffix == ".jsonl":
        return {
            "predictions": [
                json.loads(line)
                for line in path.read_text().splitlines()
                if line.strip()
            ]
        }
    data = load_yaml(path)
    if not isinstance(data, dict) or not isinstance(data.get("predictions"), list):
        raise ValueError("expected a PredictionSet with a predictions list")
    return data


def write_predictions(benchmark_id: str, predictions: list[dict], path: Path) -> None:
    """Write predictions as JSONL (``.jsonl``) or as a PredictionSet YAML file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".jsonl":
        path.write_text(
            "".join(json.dumps(p, ensure_ascii=False) + "\n" for p in predictions)
        )
    else:
        path.write_text(
            yaml.safe_dump(
                {"benchmark_id": benchmark_id, "predictions": predictions},
                sort_keys=False,
                allow_unicode=True,
                width=100,
            )
        )


def prediction_term(prediction: dict) -> str:
    """The GO term a prediction answers, from ``term`` or from ``claim_id``.

    >>> prediction_term({"item_id": "toy-P1", "claim_id": "toy-P1/GO:1"})
    'GO:1'
    """
    item = prediction["item_id"]
    term = prediction.get("term")
    identifier = prediction.get("claim_id")
    if identifier is not None:
        owner, separator, claim_term = identifier.rpartition("/")
        if (
            not separator
            or owner != item
            or not claim_term
            or (term is not None and term != claim_term)
        ):
            raise ValueError(
                f"claim_id {identifier!r} does not match item {item} and term {term!r}"
            )
        return claim_term
    if not term:
        raise ValueError(f"prediction on {item} needs a claim_id or term")
    return term


def verdict_of(prediction: dict, threshold: float | None = None) -> str:
    """The prediction's verdict; a bare score counts only against an explicit threshold.

    >>> verdict_of({"verdict": "yes"}), verdict_of({"score": 0.7}), verdict_of({"score": 0.7}, 0.5)
    ('yes', 'missing', 'yes')
    """
    verdict = prediction.get("verdict")
    if verdict in VERDICTS:
        return verdict
    if threshold is not None and prediction.get("score") is not None:
        return "yes" if prediction["score"] >= threshold else "no"
    return "missing"


def verdicts(
    benchmark: dict, predictions: Iterable[dict], threshold: float | None = None
) -> Verdicts:
    """Verdicts keyed for scoring. Predictions on unknown items or terms raise ValueError."""
    asked = {(i["id"], t) for i in benchmark["items"] for t, _, _ in queries(i)}
    conditions = {
        c["name"]: c["context"] for c in benchmark["spec"].get("conditions") or []
    }
    out: Verdicts = {}
    for p in predictions:
        term = prediction_term(p)
        if (p["item_id"], term) not in asked:
            raise ValueError(
                f"prediction on {p['item_id']} {term} matches no claim of the benchmark"
            )
        key_term = SHUFFLED + term if p.get("sequence_control") == "SHUFFLED" else term
        condition, predictor = p["condition"], p["predictor"]
        if conditions and condition not in conditions:
            raise ValueError(
                f"unknown condition {condition!r}; declared conditions: {sorted(conditions)}"
            )
        if (
            condition in conditions
            and p.get("context", conditions[condition]) != conditions[condition]
        ):
            raise ValueError(
                f"context {p['context']} disagrees with condition {condition!r}"
            )
        key = (condition, predictor, p["item_id"], key_term)
        if key in out:
            raise ValueError(f"duplicate prediction for {key}")
        out[key] = verdict_of(p, threshold)
    declared = {p["name"] for p in benchmark["spec"].get("predictors") or []}
    if declared:
        for name in sorted({key[1] for key in out} - declared):
            logging.getLogger(__name__).warning(
                "Predictor %r is absent from the spec; its reference recency has not been assessed.",
                name,
            )
    return out
