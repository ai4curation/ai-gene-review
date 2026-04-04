"""Data models for prokaryotic immunity prediction."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class ProteinRecord:
    """A protein extracted from a proteome or annotated genome."""

    protein_id: str
    sequence: str
    description: str = ""
    gene_symbol: str | None = None
    locus_tag: str | None = None
    contig: str | None = None
    index: int = 0
    start: int | None = None
    end: int | None = None
    strand: str | None = None
    source_path: Path | None = None

    @property
    def display_name(self) -> str:
        """Best label to show in reports and export paths."""
        return self.gene_symbol or self.locus_tag or self.protein_id


@dataclass(slots=True)
class PreparedProteome:
    """Normalized inputs used by the pipeline and external tools."""

    proteins: list[ProteinRecord]
    faa_path: Path
    gff_path: Path | None = None
    derived_from: Path | None = None
    notes: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ExternalHit:
    """A hit from DefenseFinder, PADLOC, or CasFinder."""

    database: str
    protein_id: str
    system: str
    subtype: str | None = None
    confidence: float = 1.0
    raw_label: str | None = None
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class FamilyDefinition:
    """Canonical defense-family metadata."""

    name: str
    term_id: str
    description: str
    aliases: list[str]


@dataclass(slots=True)
class ProteinPrediction:
    """Per-protein model output."""

    protein: ProteinRecord
    family_scores: dict[str, float]
    best_family: str | None
    family_confidence: float
    defense_score: float
    neighborhood_score: float
    novel_score: float
    predicted_novel: bool
    external_hits: list[ExternalHit] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)


@dataclass(slots=True)
class BenchmarkRecord:
    """Normalized benchmark row for evaluation."""

    protein_id: str
    family: str | None
    is_defense: bool
    is_novel: bool = False
    split: str | None = None
