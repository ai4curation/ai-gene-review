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
from collections.abc import Iterable, Iterator
from pathlib import Path

import yaml

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


def read_predictions(paths: Iterable[Path]) -> list[dict]:
    """Prediction records from PredictionSet YAML files or JSONL files (one Prediction per line)."""
    out: list[dict] = []
    for path in paths:
        if path.suffix == ".jsonl":
            out += [json.loads(line) for line in path.read_text().splitlines() if line]
        else:
            out += (yaml.safe_load(path.read_text()) or {}).get("predictions") or []
    return out


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

    >>> prediction_term({"claim_id": "toy-P1/GO:1"}), prediction_term({"term": "GO:2"})
    ('GO:1', 'GO:2')
    """
    if prediction.get("term"):
        return prediction["term"]
    return prediction["claim_id"].rsplit("/", 1)[1]


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
    out: Verdicts = {}
    for p in predictions:
        term = prediction_term(p)
        if (p["item_id"], term) not in asked:
            raise ValueError(
                f"prediction on {p['item_id']} {term} matches no claim of the benchmark"
            )
        key_term = SHUFFLED + term if p.get("sequence_control") == "SHUFFLED" else term
        out[(p["condition"], p["predictor"], p["item_id"], key_term)] = verdict_of(
            p, threshold
        )
    return out
