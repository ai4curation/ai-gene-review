"""peptalk adapter: claims to ``peptalk ask`` input, ``peptalk ask`` JSONL to predictions.

peptalk (https://github.com/ai4curation/peptalk) is one example predictor: it
asks an LLM about a sequence under a context level (``--context blind``,
``organism`` or ``full``), with an optional shuffled-sequence control.
"""

from __future__ import annotations

import ast
import json
from collections.abc import Iterable, Iterator
from pathlib import Path

from aigr_benchmark.predictions import VERDICTS, fasta_id

CLAIM_COLUMNS = ("id", "task", "term", "label", "position", "residue")
TASK = "ask-function"


def claims_tsv(claims: Iterable[dict]) -> str:
    """``peptalk ask --claims`` TSV for generic claims.

    >>> print(claims_tsv([{"sequence_id": "sp|P1|X_HUMAN", "term": {"id": "GO:1", "label": "a"}}]), end="")
    id	task	term	label	position	residue
    sp|P1|X_HUMAN	ask-function	GO:1	a
    """
    rows = ["\t".join(CLAIM_COLUMNS)]
    rows += [
        "\t".join((c["sequence_id"], TASK, c["term"]["id"], c["term"]["label"], "", ""))
        for c in claims
    ]
    return "\n".join(rows) + "\n"


def read_jsonl(paths: Iterable[Path]) -> Iterator[tuple[Path, dict]]:
    """(file, record) for JSON lines, skipping peptalk's TSV summary lines."""
    for path in paths:
        for line in path.read_text().splitlines():
            if line.startswith("{"):
                yield path, json.loads(line)


def answer_of(record: dict) -> dict:
    """The parsed answer; older peptalk versions wrote it as a Python repr.

    >>> answer_of({"answer": {"verdict": "yes"}}), answer_of({"answer": "{'verdict': 'no'}"})
    ({'verdict': 'yes'}, {'verdict': 'no'})
    >>> answer_of({"answer": None})
    {}
    """
    answer = record.get("answer")
    if isinstance(answer, str):
        answer = ast.literal_eval(answer)
    return answer or {}


def condition_for(conditions: list[dict], context: str) -> str:
    """The single spec condition with this context level.

    >>> condition_for([{"name": "seq-only", "context": "BLIND"}], "blind")
    'seq-only'
    """
    names = [c["name"] for c in conditions if c["context"] == context.upper()]
    if len(names) > 1:
        raise ValueError(f"several conditions have context {context}: {names}")
    if not names:
        raise ValueError(f"no declared condition has context {context!r}")
    return names[0]


def predictions(benchmark: dict, records: Iterable[tuple[Path, dict]]) -> list[dict]:
    """Prediction records from ``peptalk ask`` records (``ask-function`` only)."""
    by_fasta = {fasta_id(i): i["id"] for i in benchmark["items"] if i.get("entry_name")}
    conditions = benchmark["spec"].get("conditions") or []
    out = []
    for path, record in records:
        item_id = by_fasta.get(record.get("id", ""))
        term = (record.get("params") or {}).get("term")
        if item_id is None or term is None or record.get("task") != TASK:
            continue
        answer = answer_of(record)
        model = record.get("model") or ""
        prediction = {
            "item_id": item_id,
            "term": term,
            "predictor": f"peptalk:{model}",
            "predictor_version": record.get("annotator_version"),
            "model": model,
            "effort": record.get("effort"),
            "condition": condition_for(conditions, record.get("context", "")),
            "context": record.get("context", "").upper() or None,
            "sequence_control": (
                "NATIVE" if record.get("condition", "real") == "real" else "SHUFFLED"
            ),
            "verdict": answer.get("verdict")
            if answer.get("verdict") in VERDICTS
            else None,
            "evidence": answer.get("reason"),
            "cost_usd": record.get("cost_usd"),
            "prediction_date": (record.get("started_at") or "")[:10] or None,
            "provenance": f"peptalk {path.name} uid={record.get('uid')}",
        }
        out.append({k: v for k, v in prediction.items() if v is not None})
    return out
