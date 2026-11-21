"""Task and result types for deterministic or model-backed AIGR classifiers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol


@dataclass(frozen=True)
class Choice:
    """One closed-set classification option."""

    value: str
    description: str


@dataclass(frozen=True)
class ClassificationTask:
    """Closed-set classification prompt and candidate labels."""

    instruction: str
    context: str
    choices: tuple[Choice, ...] = ()
    question: str = "Label:"
    output_schema: Mapping[str, Any] | None = None

    def __post_init__(self) -> None:
        if not self.instruction.strip():
            raise ValueError("ClassificationTask.instruction must be non-empty")
        if not self.context.strip():
            raise ValueError("ClassificationTask.context must be non-empty")
        if self.output_schema is not None:
            if self.output_schema.get("type") != "object" or not self.output_schema.get(
                "properties"
            ):
                raise ValueError(
                    "ClassificationTask.output_schema must be a non-empty JSON object schema"
                )
            return
        if len(self.choices) < 2:
            raise ValueError("ClassificationTask requires at least two choices")
        values = [choice.value for choice in self.choices]
        if any(not value.strip() for value in values):
            raise ValueError("Choice.value must be non-empty")
        if len(set(values)) != len(values):
            raise ValueError("Choice values must be unique")


@dataclass(frozen=True)
class ClassificationResult:
    """Calibrated or scored closed-set classification result."""

    label: str | None = None
    probabilities: Mapping[str, float] = field(default_factory=dict)
    answers: Mapping[str, Any] = field(default_factory=dict)
    model: str | None = None
    elapsed_seconds: float | None = None
    usage: Mapping[str, int] = field(default_factory=dict)
    raw_response: Mapping[str, Any] = field(default_factory=dict)

    @property
    def confidence(self) -> float | None:
        if self.label is None:
            return None
        return self.probabilities.get(self.label)


class Classifier(Protocol):
    """Backend protocol for classifying AIGR benchmark tasks."""

    def classify(self, task: ClassificationTask) -> ClassificationResult: ...
