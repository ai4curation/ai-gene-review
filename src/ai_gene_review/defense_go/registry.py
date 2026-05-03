"""Load and query the in-repo defense-family to GO registry."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, cast

import yaml

from ai_gene_review.datamodel.gene_review_model import Term
from ai_gene_review.defense_go.models import (
    DefenseFamily,
    DefenseFamilyPrediction,
    GoTermMapping,
    MappingPolicy,
    WrappedDefensePrediction,
)


def default_registry_path() -> Path:
    """Return the package-local default registry path."""
    return Path(__file__).with_name("registry.yaml")


def normalize_family_query(value: str) -> str:
    """Normalize family IDs, labels, and aliases for stable lookups."""
    return "".join(character for character in value.lower() if character.isalnum())


@dataclass(slots=True)
class DefenseGoRegistry:
    """Lookup object for stable defense-family IDs and GO suggestions."""

    version: str
    families_by_id: dict[str, DefenseFamily]
    aliases_to_id: dict[str, str]

    @property
    def families(self) -> tuple[DefenseFamily, ...]:
        """Return all families in registry order."""
        return tuple(self.families_by_id.values())

    def get(self, family_id: str) -> DefenseFamily | None:
        """Return a family by its canonical ID."""
        return self.families_by_id.get(family_id)

    def resolve(self, query: str) -> DefenseFamily:
        """Resolve a family by canonical ID, label, or alias."""
        if query in self.families_by_id:
            return self.families_by_id[query]

        normalized = normalize_family_query(query)
        family_id = self.aliases_to_id.get(normalized)
        if family_id is None:
            raise KeyError(f"Unknown defense family: {query}")
        return self.families_by_id[family_id]


def load_registry(path: Path | None = None) -> DefenseGoRegistry:
    """Load a defense-family registry from YAML."""
    registry_path = path or default_registry_path()
    raw_payload = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
    if not isinstance(raw_payload, Mapping):
        raise ValueError(f"Defense GO registry must be a mapping: {registry_path}")
    payload = cast(Mapping[str, Any], raw_payload)
    version = str(payload.get("version", "0"))
    family_rows = _as_mapping_sequence(payload.get("families", ()), "families")

    families_by_id: dict[str, DefenseFamily] = {}
    aliases_to_id: dict[str, str] = {}
    for row in family_rows:
        family = _load_family(row)
        if family.id in families_by_id:
            raise ValueError(f"Duplicate defense family ID: {family.id}")
        families_by_id[family.id] = family
        for alias in (family.id, family.label, *family.aliases):
            _register_alias(alias, family.id, aliases_to_id)

    return DefenseGoRegistry(
        version=version,
        families_by_id=families_by_id,
        aliases_to_id=aliases_to_id,
    )


@lru_cache(maxsize=1)
def load_default_registry() -> DefenseGoRegistry:
    """Load and cache the package-local registry."""
    return load_registry()


def wrap_prediction(
    prediction: DefenseFamilyPrediction | str,
    registry: DefenseGoRegistry | None = None,
) -> WrappedDefensePrediction:
    """Resolve a family prediction into GO-aware review data."""
    active_registry = registry or load_default_registry()
    normalized_prediction = (
        prediction
        if isinstance(prediction, DefenseFamilyPrediction)
        else DefenseFamilyPrediction(family=prediction)
    )
    family = active_registry.resolve(normalized_prediction.family)
    return WrappedDefensePrediction(
        family=family,
        matched_input=normalized_prediction.family,
        confidence=normalized_prediction.confidence,
        source=normalized_prediction.source,
    )


def wrap_predictions(
    predictions: Iterable[DefenseFamilyPrediction | str],
    registry: DefenseGoRegistry | None = None,
) -> list[WrappedDefensePrediction]:
    """Resolve multiple family predictions into GO-aware review data."""
    active_registry = registry or load_default_registry()
    return [wrap_prediction(prediction, registry=active_registry) for prediction in predictions]


def _load_family(row: Mapping[str, Any]) -> DefenseFamily:
    """Build a DefenseFamily from registry YAML."""
    family_id = str(row["id"])
    label = str(row["label"])
    description = str(row.get("description", ""))
    aliases = tuple(str(alias) for alias in _as_sequence(row.get("aliases", ()), f"{family_id}.aliases"))
    go_terms = tuple(
        _load_go_term_mapping(mapping)
        for mapping in _as_mapping_sequence(row.get("go_terms", ()), f"{family_id}.go_terms")
    )
    review_notes = tuple(
        str(note) for note in _as_sequence(row.get("review_notes", ()), f"{family_id}.review_notes")
    )
    return DefenseFamily(
        id=family_id,
        label=label,
        description=description,
        aliases=aliases,
        go_terms=go_terms,
        review_notes=review_notes,
    )


def _load_go_term_mapping(row: Mapping[str, Any]) -> GoTermMapping:
    """Build a GoTermMapping from registry YAML."""
    term_payload = _as_mapping(row["term"], "go_terms.term")
    term = Term(
        id=str(term_payload["id"]),
        label=str(term_payload["label"]),
        ontology=str(term_payload.get("ontology", "GO")),
    )
    policy = MappingPolicy(str(row.get("policy", MappingPolicy.AUTOMATIC.value)))
    return GoTermMapping(
        term=term,
        relation=str(row.get("relation", "involved_in")),
        policy=policy,
        rationale=str(row.get("rationale", "")),
    )


def _as_sequence(value: object, path: str) -> tuple[object, ...]:
    """Return a registry list-like value as an immutable sequence."""
    if value is None:
        return ()
    if isinstance(value, (str, bytes)) or not isinstance(value, Iterable):
        raise ValueError(f"Defense GO registry field {path} must be a list")
    return tuple(value)


def _as_mapping(value: object, path: str) -> Mapping[str, Any]:
    """Return a registry mapping value with a typed string-key view."""
    if not isinstance(value, Mapping):
        raise ValueError(f"Defense GO registry field {path} must be a mapping")
    return cast(Mapping[str, Any], value)


def _as_mapping_sequence(value: object, path: str) -> tuple[Mapping[str, Any], ...]:
    """Return a registry list whose members are mappings."""
    return tuple(_as_mapping(item, f"{path}[]") for item in _as_sequence(value, path))


def _register_alias(alias: str, family_id: str, aliases_to_id: dict[str, str]) -> None:
    """Register one normalized alias, rejecting cross-family collisions."""
    normalized = normalize_family_query(alias)
    existing = aliases_to_id.get(normalized)
    if existing is not None and existing != family_id:
        raise ValueError(f"Duplicate defense-family alias '{alias}' for {family_id} and {existing}")
    aliases_to_id[normalized] = family_id
