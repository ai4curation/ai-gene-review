"""Typed models for translating defense-family predictions into GO review inputs."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from ai_gene_review.datamodel.gene_review_model import Term


class MappingPolicy(StrEnum):
    """How aggressively the wrapper should treat a family-to-GO mapping."""

    AUTOMATIC = "automatic"
    REVIEW_ONLY = "review_only"


@dataclass(frozen=True, slots=True)
class GoTermMapping:
    """A GO term suggested for a defense-family prediction."""

    term: Term
    relation: str
    policy: MappingPolicy
    rationale: str


@dataclass(frozen=True, slots=True)
class DefenseFamily:
    """A stable, extractable representation of a defense-family concept."""

    id: str
    label: str
    description: str
    aliases: tuple[str, ...] = ()
    go_terms: tuple[GoTermMapping, ...] = ()
    review_notes: tuple[str, ...] = ()

    @property
    def automatic_terms(self) -> tuple[GoTermMapping, ...]:
        """Return GO terms that are safe to materialize automatically."""
        return tuple(mapping for mapping in self.go_terms if mapping.policy is MappingPolicy.AUTOMATIC)

    @property
    def review_only_terms(self) -> tuple[GoTermMapping, ...]:
        """Return GO terms that should remain curation suggestions."""
        return tuple(mapping for mapping in self.go_terms if mapping.policy is MappingPolicy.REVIEW_ONLY)


@dataclass(frozen=True, slots=True)
class DefenseFamilyPrediction:
    """A minimal family assignment emitted by a defense predictor."""

    family: str
    confidence: float | None = None
    source: str | None = None


@dataclass(frozen=True, slots=True)
class WrappedDefensePrediction:
    """A family prediction enriched with stable IDs, GO terms, and review notes."""

    family: DefenseFamily
    matched_input: str
    confidence: float | None = None
    source: str | None = None

    @property
    def automatic_terms(self) -> tuple[GoTermMapping, ...]:
        """Convenience access to automatically assignable GO terms."""
        return self.family.automatic_terms

    @property
    def review_only_terms(self) -> tuple[GoTermMapping, ...]:
        """Convenience access to review-only GO suggestions."""
        return self.family.review_only_terms

    @property
    def review_notes(self) -> tuple[str, ...]:
        """Convenience access to family-level curation notes."""
        return self.family.review_notes
