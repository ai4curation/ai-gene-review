"""TypeSafe API adapter for closed-set AIGR classification tasks."""

from __future__ import annotations

import json
import math
import os
import time
from typing import Any, Callable, Mapping

import httpx

from ai_gene_review.classifier.base import ClassificationResult, ClassificationTask

DEFAULT_BASE_URL = "https://api.typesafe.ai/v1/systemone"
DEFAULT_MODEL = "jev-1.13.0"


def render_prompt(task: ClassificationTask) -> str:
    """Format a classification task for a JSON-constrained TypeSafe request."""
    options = "\n".join(
        f"- {choice.value}: {choice.description}" for choice in task.choices
    )
    sections = [task.instruction.strip()]
    if options:
        sections.extend(["Options:", options])
    sections.extend([task.context.strip(), task.question.strip()])
    return "\n\n".join(sections)


def response_schema(task: ClassificationTask) -> dict[str, Any]:
    """Build the JSON schema enforcing the task's allowed choice values."""
    if task.output_schema is not None:
        return dict(task.output_schema)
    return {
        "type": "object",
        "properties": {
            "label": {
                "type": "string",
                "enum": [choice.value for choice in task.choices],
                "description": (
                    " Return ".join(
                        f"{choice.value} if {choice.description}"
                        for choice in task.choices
                    )
                    + "."
                ),
            }
        },
        "required": ["label"],
        "additionalProperties": False,
    }


def _find_value_token(
    tokens: list[dict[str, Any]], allowed: set[str], start: int = 0
) -> tuple[dict[str, Any], int] | None:
    """Locate the constrained enum token rather than assuming a fixed offset."""
    candidates: list[tuple[dict[str, Any], int]] = []
    for index in range(start, len(tokens)):
        token = tokens[index]
        text = str(token.get("token", "")).strip()
        alts = {
            str(alt.get("token", "")).strip() for alt in token.get("top_logprobs", [])
        }
        if text in allowed or alts & allowed:
            candidates.append((token, index + 1))
    if not candidates:
        return None
    for token, next_index in candidates:
        alts = {
            str(alt.get("token", "")).strip() for alt in token.get("top_logprobs", [])
        }
        if len(alts & allowed) >= 2:
            return token, next_index
    return candidates[-1]


def _probabilities(
    token: dict[str, Any], choices: list[str], selected: str
) -> dict[str, float]:
    allowed = set(choices)
    probs = {choice: 0.0 for choice in choices}
    for alt in token.get("top_logprobs", []):
        label = str(alt.get("token", "")).strip()
        if label in allowed and "logprob" in alt:
            probs[label] = math.exp(float(alt["logprob"]))
    if selected in allowed and probs[selected] == 0.0 and "logprob" in token:
        probs[selected] = math.exp(float(token["logprob"]))
    total = sum(probs.values())
    if total > 0:
        probs = {label: value / total for label, value in probs.items()}
    return probs


def extract_probabilities(
    response: Mapping[str, Any], task: ClassificationTask, selected: str
) -> dict[str, float]:
    """Convert TypeSafe token logprobs into a distribution over task choices."""
    choices = [choice.value for choice in task.choices]
    tokens = response.get("logprobs")
    if not isinstance(tokens, list):
        return {choice: (1.0 if choice == selected else 0.0) for choice in choices}
    found = _find_value_token(tokens, set(choices))
    if found is None:
        return {choice: (1.0 if choice == selected else 0.0) for choice in choices}
    return _probabilities(found[0], choices, selected)


def extract_schema_answers(
    response: Mapping[str, Any],
    schema: Mapping[str, Any],
    parsed: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    """Extract labels and distributions for an object schema of enum fields."""
    tokens = (
        response.get("logprobs") if isinstance(response.get("logprobs"), list) else []
    )
    cursor = 0
    answers: dict[str, dict[str, Any]] = {}
    for name, prop in schema["properties"].items():
        if name not in parsed:
            raise ValueError(f"TypeSafe output did not include {name!r}: {parsed}")
        choices = list(prop["enum"])
        selected = str(parsed[name])
        if selected not in choices:
            raise ValueError(
                f"TypeSafe label {selected!r} for {name!r} is not in {choices}"
            )
        found = _find_value_token(tokens, set(choices), cursor) if tokens else None
        if found is None:
            probs = {choice: (1.0 if choice == selected else 0.0) for choice in choices}
        else:
            token, cursor = found
            probs = _probabilities(token, choices, selected)
        answers[name] = {"label": selected, "probabilities": probs}
    return answers


class TypeSafeClassifier:
    """HTTP client for TypeSafe JSON-schema classification."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        model: str = DEFAULT_MODEL,
        timeout: float = 90.0,
        top_logprobs: int = 10,
        post: Callable[..., httpx.Response] = httpx.post,
    ) -> None:
        self.api_key = api_key or os.environ.get("TYPESAFE_API_KEY", "")
        if not self.api_key:
            raise ValueError("TypeSafeClassifier requires api_key or TYPESAFE_API_KEY")
        self.base_url = base_url
        self.model = model
        self.timeout = timeout
        self.top_logprobs = top_logprobs
        self._post = post

    def classify(self, task: ClassificationTask) -> ClassificationResult:
        payload = {
            "model": self.model,
            "prompt": render_prompt(task),
            "output_schema": json.dumps(response_schema(task)),
            "logprobs": True,
            "top_logprobs": self.top_logprobs,
        }
        started = time.perf_counter()
        response = self._post(
            self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=self.timeout,
        )
        elapsed = time.perf_counter() - started
        response.raise_for_status()
        body = response.json()
        parsed = json.loads(body["output"])
        usage = {
            key: int(value)
            for key, value in (body.get("usage") or {}).items()
            if isinstance(value, int)
        }
        if task.output_schema is not None:
            answers = extract_schema_answers(body, task.output_schema, parsed)
            root = answers.get("/", {})
            return ClassificationResult(
                label=root.get("label"),
                probabilities=root.get("probabilities", {}),
                answers=answers,
                model=body.get("model", self.model),
                elapsed_seconds=elapsed,
                usage=usage,
                raw_response=body,
            )
        label = parsed["label"]
        allowed = {choice.value for choice in task.choices}
        if label not in allowed:
            raise ValueError(f"TypeSafe label {label!r} is not in {sorted(allowed)}")
        return ClassificationResult(
            label=label,
            probabilities=extract_probabilities(body, task, label),
            model=body.get("model", self.model),
            elapsed_seconds=elapsed,
            usage=usage,
            raw_response=body,
        )
